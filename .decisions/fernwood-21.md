## fernwood-21 · How does the ruled `4-fresh/1-returning` ratio re-express itself?

- project: Tate-Tracker
- loop: tate-tracker
- source: `.plans/2026-09-10-testing-architecture-PLAN.md` §6, minted 2026-09-10
- options: a-declared-cell-list-per-lap | keep-a-ratio-over-journeys | a-fixed-budget-allocated-by-longest-unwalked

### Why it's here
A ratio over `seat` cannot survive the unit change in **fernwood-16**, and it was never checkable in the first place — nothing could say whether a lap had honoured it.

### What it means
This card exists so the question is **reachable**. The plan it came from is 534 lines and its own
thesis is *"a capability the loop cannot reach by running its own procedure is not a capability the
loop has"* — and it then put eight rulings into prose nothing reads. ⛔ It stalled for an hour on
exactly that the day it landed. The card carries the recommendation and the alternatives so the
ruling can be made without re-reading the plan.

### Recommendation
**It stops being a ratio and becomes a declared cell list per lap** — *this lap walks these cells* — with the gate reporting which cells have gone longest unwalked.

**Alternatives.** **(b)** keep a ratio over journeys — preserves *"the mix follows the population"* literally, and stays unfalsifiable. **(c)** a fixed per-lap budget allocated by longest-unwalked — ⛔ that is the scheduler the plan recommends against building.
