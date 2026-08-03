# Calibration report: every graded call across my paper desks

**Status: all paper, all tiny samples.** Nothing below involves real money except where a row is explicitly marked as a real execution of a paper twin, and those were small. The sample sizes are small enough that none of these numbers prove skill. That is the point of publishing them anyway: most people in crypto only show you their winners, and the fastest way to demonstrate judgment with two months of track record is to show the full ledger, graded, with the losses and the process failures attached. Every number below carries its n. Reproducible from the scrubbed CSVs via `data/calibration.py`.

## 1. Why publish a paper track record

I run several paper trading and forecasting desks as a forcing function for one skill: making explicit, timestamped calls with pre-stated invalidation, then grading them without mercy. A paper book with honest grades tells you more about how someone thinks than a screenshot of one green trade. What I am selling here is not returns. It is calibration: do I know when I am guessing, do I separate a good decision from a good outcome, and do I fix the process when it breaks.

## 2. The numbers

### Hyperliquid perps desk (HL)

Eleven scorecard rows as of extraction on 2026-08-01; 6 resolved, 5 still open, offered, or vetoed and awaiting their grading horizon.

| Metric | Value | n |
|---|---|---|
| Resolved outcomes | 0 WIN, 3 LOSS, 1 SCRATCH, 2 MISS | 6 |
| Total R (rows with an R multiple) | -3.36R | 4 |
| Desk-card lane R | -2.36R | 3 |
| Real-execution lane R | -1.0R | 1 |

No wins yet. The desk went 0 for 4 on R-graded attempts in a stretch that included a failed ETH breakout (-1.3R) and an oil long stopped on a ceasefire headline (-1.0R paper and -1.0R real, the one real execution). The two MISS rows matter as much as the losses: both were oil limit bids placed too deep that never filled while the market ran, and MISS is tracked as its own result class because an entry that never triggers during a 12 percent move is a sizing-of-patience error, not neutral.

### Robinhood-chain memecoin paper book (RH)

Twenty-three book rows; 15 closed with a clean numeric paper PnL. Dollar figures are paper ticket sizes, not personal capital.

| Metric | Value | n |
|---|---|---|
| Win rate | 4 wins, 11 losses (27%) | 15 |
| Net paper PnL | -$659 | 15 |
| Gross wins / gross losses | +$436 / -$1,095 | 4 / 11 |

The headline is ugly and the interesting result is underneath it. Ten closed rows carry the book's dual grades, one letter for outcome and one for reasoning, assigned separately. Sorting by reasoning grade:

| Reasoning tier | Trades | Winners | Net paper PnL |
|---|---|---|---|
| A | 3 | 3 | +$333 |
| B | 4 | 0 | -$344 |
| C | 3 | 0 | -$283 |

Every A-reasoning trade won and every sub-A trade lost. With n=10 that could easily be noise, and I say so. But the direction is exactly what a grading system is supposed to surface: the A-reasoning trades (a conviction fade of an overextended chart, a resting bid into a panic dip, an air-pocket flush fill) were structurally different decisions from the C-reasoning trades, which were full-green market chases and cascade knife-catches. The grade was assigned on the logic at entry, before the outcome column existed.

### Prediction markets, World Cup 2026

Fourteen verdicts across two lanes, model lane and my lane, at Kalshi, Robinhood, and book prices.

| Lane | Verdicts | Settled | Won | Lost | Void | Open | Hit rate |
|---|---|---|---|---|---|---|---|
| claude | 12 | 8 | 4 | 4 | 2 | 2 | 50% (n=8) |
| ces | 2 | 2 | 1 | 1 | 0 | 0 | 50% (n=2) |

A 50 percent hit rate on n=8 mixed-price markets is uninformative on its own; the useful judgment question is whether the wins came at prices below fair, and the sample is too small to answer it yet. Logged anyway because the ledger only compounds if it starts before the numbers flatter me.

### mc-sniper daemon closes (separate system lane)

This is not a judgment book. These are 106 mechanical closes from a paper launchpad-sniping daemon; I designed the rules, the daemon pulled the trigger. Excluding 4 position-hygiene cleanup rows (including one +$3,323 accounting artifact from ejecting USDC off the book, which no honest report counts as a trade):

| Close reason | n | Winners | Net paper PnL |
|---|---|---|---|
| liq-kill | 66 | 16 | -$1,382 |
| disaster-stop | 19 | 0 | -$564 |
| stage2:inverted-uniques | 10 | 0 | -$15 |
| trail | 7 | 7 | +$627 |
| All ex-cleanup | 102 | 23 (22.5%) | -$1,334 |

The distribution is the finding. Every trade that survived long enough to activate a trailing stop was a winner (+$627 across 7); everything else bled. The system's edge, if it exists, lives entirely in the entry filter that decides what survives to trail, and the current filter was not selective enough. That conclusion came from this table, not from vibes.

### Agent trading desk (pipeline context only)

Forty verdicts logged, 37 still open or pending, 3 graded (two target hits at +15 percent, one stop at -20 percent, and one of the target hits is a duplicate logging of the same NVDA verdict). Too early to report as a book; listed so the full pipeline is visible.

## 3. Human vs model lanes

Two books were deliberately built with two lanes so my calls and the model desk's calls could be graded against each other on the same markets.

On HL the comparison mostly did not happen the way I expected, and that non-result is itself the result. Of my 5 CES_CALL cards, I took exactly 1 (a small ZEC narrative ticket, still open), left 1 offered entry untaken, gated 1 on a trigger that never fired, and vetoed 2. The desk lane took its shots and posted -2.36R (n=3); my lane's only R print is the -1.0R real execution of a desk card. So the honest read is not "human beat model" or the reverse. It is that my dominant behavior under uncertainty was refusal, and the ledger now grades my vetoes against logged counterfactual baselines so refusal stops being free. On the prediction book both lanes sit at 50 percent on samples (n=8, n=2) too small to separate.

## 4. Where I was wrong

**Duplicate-writer double counting.** The RH book let two lanes write to the same positions. One lane stopped VEX out at -69 while another lane kept it open and scaled it; a later re-adjudication double-counted the R2 and R4 CASHCAT stops that had already printed on 7/12. The fix: one writer per book, and the contemporaneous print always beats a retrospective re-adjudication. Both rules are now standing desk law.

**Two consecutive too-deep oil bids.** DESK-5 and DESK-6 were the same mistake made twice: limit bids placed for a better price than the market ever offered, cancelled unfilled while oil ran from the low 80s past 92. The fix was structural, not motivational: the replacement card (DESK-7) switched to market entry with a wider stop, and MISS became a first-class graded result so unfilled bids show up in the record instead of vanishing.

**The GME dark window.** I left a resting paper ticket on a collapsing token with nothing watching it. The fill and the stop both printed inside a monitoring gap, so the true path is unverifiable. I graded it -40, the worst defensible print, and the rule since then is that unattended resting tickets in illiquid windows are either flagged unadjudicated (the WALLET row) or graded against myself, never in my favor.

## 5. Method notes

**Outcome and reasoning graded separately.** Every RH trade gets two letters. A bad-process win is graded A/F-adjacent, not celebrated; the F/B rows (right thesis, wrong execution) get different fixes than F/C rows (bad decision at entry).

**R multiples on the perps desk.** Every HL card pre-states entry, stop, and size at roughly 2 percent lane risk, so results normalize to R (profit divided by planned risk). -1.0R means the stop did its job; the number I watch is total R, not dollar PnL.

**Result taxonomy.** WIN, LOSS, MISS, SAVE, SCRATCH. MISS and SAVE exist so that unfilled orders and correct vetoes get graded instead of ignored; vetoed and offered-untaken calls carry logged baselines for counterfactual grading at fixed horizons.

**Unit-normalized stakes and paper dollars.** Prediction verdicts log stake units, not dollars; desk books log paper ticket sizes. No personal capital figures appear anywhere in this report.

**Adjudication bias.** Where the record is ambiguous (dark windows, dual-lane conflicts), the grade goes against me. A track record you can trust is one where every judgment call in the bookkeeping made the numbers worse, not better.
