## fernwood-16 · Does gate ① change its unit from `seat` to `(journey, lens)`?

- project: Tate-Tracker
- loop: tate-tracker
- source: `.plans/2026-09-10-testing-architecture-PLAN.md` §6, minted 2026-09-10
- options: change-the-unit-at-P4 | keep-seat | ship-(seat,journey-kind)-as-interim

### Why it's here
⚡⚡ **THIS IS THE ONE WITH A LIVE CONSEQUENCE.** Lap 5's gate ① has sat **0/4 with no reachable close**.

⭐ **The gate's unit was never decided — it is a directory name.** `release-gate.py`'s `seats()` is `os.listdir(WALKS)` over `.private/synthetic-walks/<role>/`, which `journey-walk.py` writes. *(Verified independently, 2026-09-10.)* So `seat` became the unit because that is what the filesystem contained, and the journey and lens axes were never expressible because there was nowhere to put them. Two additive keys in `transcript.json` dissolve it **without moving a single run folder**, and lap 4/5 evidence backfills exactly.

### What it means
This card exists so the question is **reachable**. The plan it came from is 534 lines and its own
thesis is *"a capability the loop cannot reach by running its own procedure is not a capability the
loop has"* — and it then put eight rulings into prose nothing reads. ⛔ It stalled for an hour on
exactly that the day it landed. The card carries the recommendation and the alternatives so the
ruling can be made without re-reading the plan.

### Recommendation
**YES, at P4, with falsifier ③ gating the change itself.** This alters the release condition, which is why it is a card and not a step.

**Alternatives.** **(b)** keep `seat` and accept that a failing returning walk stays invisible — ⛔ contradicts `CYCLE-MAP.md`'s own ruling that *"the returning walk is what makes gate ① able to fail for the right reason"*. **(c)** `(seat, journey-kind)` as an interim — writes `seat` deeper into the one file whose unit is the problem.
