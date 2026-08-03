# Diligence Memo: INDEX (yield-bearing memecoin, Robinhood chain)

**Summary:** Contract-verified "hold it, get paid in stocks" token staged as a plateau on decaying inflow; the desk's call was exit into bounces, do not add. Nine days later market cap was down 44 percent and the yield engine had quietly lost 86 percent of its inflow. The lifecycle read was right; the exit execution left money on the table.

## Asset and market context

INDEX pitched the strongest hook in the pay-you class I studied: hold a memecoin, get paid in tokenized NVDA and AAPL. At my first full census pass on July 24, 2026 it sat at a $12.3M market cap, off a roughly $16M press-cycle high. This memo documents desk research and a lifecycle staging call; the desk's trading books are paper books on a paper desk.

## Mechanism / how it works

I verified the mechanism at the contract level rather than taking the site's word. The token is a clean fixed-supply 1B ERC20; the "ReflectionToken" name is vestigial. It holds only a holder registry, auto-adding and removing wallets at a 10,000 INDEX threshold on every transfer (on-chain minShareBalance reads exactly 10,000e18, matching the docs). The 3 percent each-way fee is not in the token: it is taken in native ETH by a fee hook on the Uniswap v4 pool, and an external distributor buys a tokenized-stock basket (AAPL, NVDA, TSLA, MSFT and others via Rialto) and pays registered holders on a keeper cycle. Docs and contract were consistent. Disclosed admin powers: owner can change supported assets, keeper permissions, and the payout asset.

## Holder base and flow evidence

On July 24: 2,379 registered holders, $610K of 24h volume implying about $18.3K per day flowing into stock buys, roughly 0.15 percent per day gross against market cap. Structurally there is no insolvency mode, only a volume-decay mode: traders pay holders, so the yield dies exactly as fast as the tape. The staging evidence was already bearish: $610K trailing 24h volume but only $52K in the last six hours and $6.5K in the last hour, with price printing +34.7 percent on the day. Shill-wave timing sealed it: the LBank listing and press coverage arrived after the vertical, which my model reads as exit-liquidity recruitment.

## Risks and invalidation

Staged as plateau-entry, a distribution phase, not an accumulation phase. Collapse triggers written on July 24: sustained 24h volume under $200K, registry holder count rolling over, liquidity under $800K confirming unwind.

## Decision taken and sizing logic

The desk had a live position from earlier in its history with a standing failed-thesis exit order: exit the remainder into bounces, no adds, watch-only below $10M. The census pass independently concurred with that order. Re-rate condition: volume rebuilding above $1M per day with buyer-majority uniques at 1.5 to 1 or better.

## Outcome and post-mortem

By August 2 the card read plateau to early unwind: market cap $6.9M, down 44 percent in nine days, liquidity about $628K (the unwind trigger tripped). The best finding was structural: INDEX volume had migrated off the fee hook. A hookless v3 pool created July 10 carried $428K of the $517K headline volume, while the canonical hooked v4 pool did $33K. Headline volume looked alive; yield-carrying volume was under $100K per day, holder inflow about $2.6K per day versus $18.3K on July 24, down 86 percent, while the site still advertised the loop. My own July 24 trigger had measured the wrong volume, a calibration lesson I logged. Per $1,000 held, the stream was worth about $0.41 per day at current tape versus $2.55 at the healthy-period median. I also audited the "PONS integration" narrative: the router machinery was real and live on-chain, but actual burns totaled about $280 all time against claims of tens of thousands per day, off by three orders of magnitude, a late-plateau narrative injection.

Reasoning grade: the mechanism verification, staging, and direction were right and early. Execution critique: an exit window above $10M closed unmonetized because the exit relied on discretionary bounces instead of resting limits. Right read, incomplete conversion.
