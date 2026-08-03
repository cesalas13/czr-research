# Diligence Memo: DATABEAR (mascot-lane memecoin, Robinhood chain)

**Summary:** Paper long at the bottom of a mapped rotation range, stopped across all books for a combined -$216 when the chain's anchor coin broke regime and the range floor failed. Graded Outcome F, Reasoning B: the level was called almost exactly, but a level is not a floor during a regime break.

## Asset and market context

DATABEAR was a mascot-lane memecoin on the Robinhood chain. Its day-one tape set a desk benchmark: the fastest distinct-buyer accumulation the scanner had recorded, later used as the reference signature for new launches. By July 12, 2026 it had settled into a $1M to $2.3M market cap trading range. Every position below was a paper position on a paper desk, sized off $10,000 notional books.

## Mechanism / how it works

No yield mechanism; the relevant structure was holder behavior. A top-holder overlay showed the largest wallets running a repeated rotation: entering around $1.28M and exiting at $2.21M to $2.31M, with at least two completed cycles. This produced the desk's farmed-range doctrine, written that morning with DATABEAR as the exhibit: when top-holder entry and exit bands bracket price with repeated completed cycles, the coin is a rotation farm. Trade the bands with the farmers, never hold through the upper band (that is volunteering as their exit liquidity), and treat parity uniques through big moves as the tell that the holders are the day traders. A breakout only counts if price holds above the exit band.

## Holder base and flow evidence

The desk had separately published a bottom prediction: a $1.05M to $1.45M zone with a $1.2M point estimate. Supporting evidence at entry: the coin had based between $1.4M and $1.8M all day rather than cascading, the wallet-cohort that farms the range had reloaded in the $1.32M to $1.44M band, and liquidity was intact at $143k, so rug risk was low.

## Risks and invalidation

The written risk was the regime: the anchor coin was in WARNING, and the desk had a live doctrine proposal that satellite resting bids should be pulled entirely in warning, not merely halved. The DATABEAR fill was explicitly logged as the test case for that proposal. Invalidation was the $1.05M contract line (the $1.02M band on the aggressive book), stops written at entry.

## Decision taken and sizing logic

Balanced book: two rungs of $250 at $1.28M and $1.20M (effective $1.293M and $1.212M with slippage), stop below $1.05M, scale at $2.2M, the farmers' own exit band. Aggressive book: $560 band-trade at $1.30M, stop below $1.02M. Sizes were regime-adjusted per the meter.

## Outcome and post-mortem

The anchor deepbroke that evening ($146.96M print through its $147M line) and the cascade ran through every satellite shelf. DATABEAR broke the range floor: both balanced-book rungs stopped at a $1.046M print for -$48 (-19 percent) and -$36 (-14 percent); the aggressive book stopped at $1.009M for -$132 (-23.1 percent). Combined paper loss $216. There was no rug: liquidity held, the floor simply failed. Overnight the abandonment tail printed, $690k by morning, then $536k, $348k, and eventually roughly $50k. The reclaim-only re-entry lines were never earned.

Grade on the book: Outcome F, Reasoning B. The thesis was well-founded on its own terms: prediction zone, farmers' entry band, mascot lane, intact LP. The bottom prediction itself was graded a HIT with roughly 3 percent error. The post-mortem line I keep: the prediction was right about where, wrong about it being a buyable where during a regime break. Even the farmers who reloaded above my entry were 25 percent underwater in the cascade. The trade became the third and fourth exhibits for the pull-bids-in-warning rule (alongside two other stopped longs), which is exactly what a graded paper desk is for: the loss was cheap, the doctrine change was not.
