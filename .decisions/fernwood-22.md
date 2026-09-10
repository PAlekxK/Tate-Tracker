## fernwood-22 · `check-backlog-ready.py` reads the testing plan as an ORPHAN. Accept the flag, or add a pointer?

- project: Tate-Tracker
- loop: tate-tracker
- source: `.plans/2026-09-10-testing-architecture-PLAN.md` §6, minted 2026-09-10
- options: accept-the-flag | add-the-pointer-when-the-row-is-ruled | fix-the-instrument-gap

### Why it's here
⚠️ **A conflicting instruction was relayed to this session** — *"fix the orphan by adding the `BACKLOG.md` pointer row"* — which is the **opposite** of the plan's own recommendation. Not acted on; raised here instead.

`POINTER_PAT` requires the literal `→ READY · …`, and this row is explicitly **not ready**. Adding one would be a false readiness claim made to silence a checker.

### What it means
This card exists so the question is **reachable**. The plan it came from is 534 lines and its own
thesis is *"a capability the loop cannot reach by running its own procedure is not a capability the
loop has"* — and it then put eight rulings into prose nothing reads. ⛔ It stalled for an hour on
exactly that the day it landed. The card carries the recommendation and the alternatives so the
ruling can be made without re-reading the plan.

### Recommendation
**Accept the flag.** One honest flag beats a false readiness claim.

**Alternatives.** **(b)** add the pointer when Paul rules the row, in the same commit — the clean sequencing. **(c)** ⭐ **a real instrument gap worth its own row:** `stage: draft` is exempt from the `ready:` stamp (`check-backlog-ready.py:395`) but **not** from the orphan check — so the checker cannot currently express *"a plan for something not yet ranked."*
