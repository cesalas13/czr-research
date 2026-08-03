#!/usr/bin/env python3
"""Calibration report numbers. Reads the scrubbed CSVs alongside this script
and prints a JSON summary. Every stat carries its n. Paper desks only.

Run: python3 calibration.py
"""
import csv, json, re
from collections import defaultdict
from pathlib import Path

OUT = Path(__file__).parent


def rows(name):
    with open(OUT / name, newline="") as f:
        return list(csv.DictReader(f))


def hl():
    score = rows("hl_scorecard.csv")
    cards = rows("hl_cards.csv")
    resolved = [r for r in score if r["result"]]
    by_result = defaultdict(int)
    for r in resolved:
        by_result[r["result"]] += 1
    r_vals = [float(r["r_multiple"]) for r in score if r["r_multiple"]]
    by_origin = defaultdict(lambda: {"n": 0, "resolved": 0, "total_r": 0.0})
    for r in score:
        o = by_origin[r["origin"]]
        o["n"] += 1
        if r["result"]:
            o["resolved"] += 1
        if r["r_multiple"]:
            o["total_r"] += float(r["r_multiple"])
    lanes = defaultdict(int)
    for c in cards:
        lanes[c["lane"]] += 1
    ces_cards = [c for c in cards if c["lane"] == "CES_CALL"]
    ces_taken = [c for c in ces_cards if c["taken"].upper().startswith("TAKEN")]
    return {
        "scorecard_rows": len(score),
        "resolved_rows": len(resolved),
        "results": dict(by_result),
        "total_R": round(sum(r_vals), 2),
        "n_with_R": len(r_vals),
        "by_origin": {k: {**v, "total_r": round(v["total_r"], 2)} for k, v in by_origin.items()},
        "cards_by_lane": dict(lanes),
        "ces_calls_taken": len(ces_taken),
        "ces_calls_total": len(ces_cards),
    }


def rh():
    book = rows("rh_paper_book.csv")
    closed_pnl = []
    for r in book:
        m = re.match(r"^([+-]\d+)$", r["result"].strip())
        if m:
            closed_pnl.append((r["coin"], int(m.group(1)), r["outcome_grade"], r["reasoning_grade"]))
    wins = [p for _, p, _, _ in closed_pnl if p > 0]
    losses = [p for _, p, _, _ in closed_pnl if p < 0]
    graded = [(c, p, o, g) for c, p, o, g in closed_pnl if g]
    by_reasoning = defaultdict(lambda: {"n": 0, "wins": 0, "pnl": 0})
    for _, p, _, g in graded:
        tier = g[0]  # collapse B+/C+ into letter tier
        t = by_reasoning[tier]
        t["n"] += 1
        t["wins"] += 1 if p > 0 else 0
        t["pnl"] += p
    return {
        "book_rows": len(book),
        "closed_numeric": len(closed_pnl),
        "wins": len(wins),
        "losses": len(losses),
        "net_paper_pnl_usd": sum(p for _, p, _, _ in closed_pnl),
        "gross_win": sum(wins),
        "gross_loss": sum(losses),
        "graded_rows": len(graded),
        "by_reasoning_tier": dict(by_reasoning),
        "note": "GME row (-40 adjudicated, path unverifiable) and text-result rows excluded from numeric PnL",
    }


def predict():
    v = rows("predict_verdicts.csv")
    by_lane = defaultdict(lambda: defaultdict(int))
    for r in v:
        by_lane[r["lane"]][r["outcome"]] += 1
    out = {}
    for lane, d in by_lane.items():
        settled = d["won"] + d["lost"]
        out[lane] = {"n": sum(d.values()), "settled": settled, **dict(d),
                     "hit_rate": round(d["won"] / settled, 3) if settled else None}
    return out


def sniper():
    closes = rows("mcsniper_closes.csv")
    by_reason = defaultdict(lambda: {"n": 0, "pnl": 0.0, "wins": 0})
    for r in closes:
        d = by_reason[r["reason"]]
        p = float(r["net_pnl_usd"])
        d["n"] += 1
        d["pnl"] += p
        d["wins"] += 1 if p > 0 else 0
    trades = [r for r in closes if not r["reason"].startswith("cleanup:")]
    tp = [float(r["net_pnl_usd"]) for r in trades]
    return {
        "total_closes": len(closes),
        "by_reason": {k: {**v, "pnl": round(v["pnl"], 2)} for k, v in sorted(by_reason.items())},
        "ex_cleanup": {"n": len(tp), "net_pnl": round(sum(tp), 2),
                       "wins": sum(1 for p in tp if p > 0),
                       "win_rate": round(sum(1 for p in tp if p > 0) / len(tp), 3)},
        "note": "mechanical daemon closes, not judgment calls; cleanup:* rows are position-hygiene artifacts",
    }


def atd():
    v = rows("atd_verdicts.csv")
    graded = [r for r in v if r["status"] == "graded"]
    return {"rows": len(v), "graded": len(graded),
            "graded_detail": [(r["asset"], r["grade"], r["realized_pct"]) for r in graded]}


if __name__ == "__main__":
    print(json.dumps({"hl": hl(), "rh": rh(), "predict": predict(),
                      "sniper": sniper(), "atd": atd()}, indent=2))
