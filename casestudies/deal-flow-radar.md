# Deal Flow Radar: Sourcing Narratives Before Consensus

## The sourcing problem

Venture returns are concentrated in deals you see before everyone else does. By the time a theme has a conference track and a Twitter consensus, the price of entry already reflects it. The hard part of sourcing is not evaluating what is in front of you; it is building a repeatable system that surfaces signals while they are still cheap to act on. I built and ran that system in the fastest feedback-loop market that exists, memecoins, where the gap between "narrative ignites" and "asset exists and is priced" is measured in hours, and where every sourcing mistake gets graded by a chart within days.

## The system

The pipeline is called narrative radar. It runs on my machine, uses only keyless public surfaces (no paid APIs), and hands off to a 24/7 daemon so nothing depends on me being awake.

```
 KnowYourMeme      Google Trends      trends24
      |                 |                 |
      +--------+--------+--------+--------+
               |
   narrative-cross-hit.mjs  (deterministic fetch, keyless)
               |
   DexScreener cross-hit    (does a token already exist?)
               |            verdict: fresh / in-window / late / dead
               |
   coinability judgment     (the human/LLM step: is this narrative
               |             investable? character or absurdist bit
               |             beats news event; flagship over $1M = late)
               |
   name-watch registry      (mc-drop "<name>": pattern list + 72h TTL,
               |             written to a canonical watchlist.json)
               |
   24/7 deploy catcher      (daemon matches every new token birth
                             against armed patterns; on hit it runs a
                             safety gate, opens a paper seat, and pushes
                             an alert in roughly 2 to 6 seconds)
```

The design premise, written into the skill definition itself, is a roughly 48 hour window from meme ignition to flagship token. If you spot the narrative inside that window, you can be waiting at the deploy instead of chasing the chart. So the system splits the job: trend surfaces find candidates, a judgment step filters for coinability (most trending topics are news events, which do not coin well; characters, animals, and absurdist phrases do), and the keepers become TTL'd name-watch patterns that a daemon matches against every new token deployment around the clock. Measured alert latency from deploy detection to gated alert with a logged paper position: 2.3 to 5.6 seconds.

## Receipts

**Jimothy, the benchmark case.** A Seattle raccoon with short spine syndrome went viral in mid July 2026 off an Instagram video, amplified by the NY Post and large aggregator accounts. Per the pipeline's own benchmark note: ignition on 7/14/2026, flagship token deployed on pump.fun on 7/16, at $7.5M market cap within the tracked window. My desk logs then followed the flagship the rest of the way: 28,197 holders within six days, and a logged peak of $42.3M on 7/22. Jimothy is the case that proved the 48 hour thesis and motivated the build. I have to be straight about the sequencing: the radar did not catch Jimothy. The first automated sweep ran 7/27 and its own log honestly files "jimothy the raccoon" under `late`. Jimothy is the calibration target, not a trophy.

**What the sweeps actually produced.** Two logged sweeps on 7/27: the first scanned 27 candidates and kept zero (everything was past ignition or news-class). The second scanned 25 and armed two second-wave watches, "nikki frowning" and "i am a fucking architect," each with a 72 hour TTL expiring 7/30. The sweep log flagged its own risk in the same line: the architect pattern included the bare word as a match term, which it labeled high false-positive risk. That flag was correct. The watch fired repeatedly on ordinary chat profanity over the next two days, and the architect tokens that did deploy were sub-$5K dust. Honest verdict: armed correctly, narrative fizzled, TTL expired it. That is the system working, not failing; most watches should die quietly.

**CATE, the near-real-time validation.** During the first sweep window, Catecoin ran to $7.4M (a logged +23,700%) as that day's in-window case. I armed a `cate` name-watch, and the catcher then flagged every derivative deploy for days (CUPCATE, CATESEM, CATEWIF, BULLCATE), each gated and paper-seated in seconds. None graded into winners. The flagship had already run; the catcher was fielding the echo wave.

**The failure log is real.** Two infrastructure defects ate signal silently. A launchd PATH bug meant every name-watch alert from 7/20 to 7/26 died with "command not found," so the daemon was catching deploys and shouting into the void. Separately, one hand-edited registry entry with wrong field names crashed the births scanner's schema validation and killed every scan cycle for five days (7/22 to 7/26), invisible because stderr was discarded. Both were found, fixed, and written up in the desk log. The lesson generalizes: a sourcing pipeline you do not actively verify is a pipeline you do not have.

## What this maps to in a VC seat

Sourcing is the same loop at a slower clock speed. Replace KnowYourMeme and Google Trends with GitHub stars, hiring pages, dev forum chatter, and conference lineups. Replace "coinability" with fundability: is this a narrative that founders will build companies around, or a news event that passes? Replace the name-watch registry with a thesis watchlist that has explicit expiry, and replace the deploy catcher with monitoring for the observable event that a thesis has become a company (incorporation, repo goes public, stealth site, first hire).

The transferable skills are concrete: separating narrative ignition from asset creation, writing judgment criteria down so they can be graded later, letting watches expire instead of accumulating a stale pipeline, and logging misses with the same rigor as hits. My logs show more fizzles than wins, timestamped. That is what an honest sourcing record looks like, and it is the habit I would bring to a fund's top-of-funnel.

## Limitations

The radar has not yet caught a flagship pre-deploy; its verified catches are clone waves and derivatives after ignition. It launched after its own benchmark case. Pattern matching on bare words generates noise, and the highest-value step, coinability judgment, is still manual and unscored. The infrastructure failed silently twice in its first two weeks. And memecoin cycles compress feedback in a way venture does not; a 48 hour window becomes an 18 month one, which makes the discipline more important and the grading slower. The system is a working prototype of a sourcing habit, not a finished machine.
