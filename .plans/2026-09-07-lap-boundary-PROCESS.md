# WHAT DO WE COMMIT TO, AND WHEN? — two cadences, and the boundary each one owns

- row: process (no BACKLOG row — same posture as the 09-07 flex-point AUDIT)
- objective: O5 (the loops are the artifact) · bears on O3 (instance 1 of N)
- kind: process
- seats: practice-steward (this file) · engineering-partner → owed only at R-A's one-line wiring;
        nothing is designed here · ux-expert · content-steward · user-researcher · ai-advisor → waived:
        no surface, no copy, no person, no model on any path
- depends-on: .plans/2026-09-07-pipeline-flex-point-AUDIT.md (R6, R7)
- depends-on: .plans/2026-09-07-product-steward-CHARTER.md
- depends-on: .plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔ NOTHING HERE EXECUTES and nothing here is due before the 13:00 EDT deadline. No item is
  ranked; every call below is dependency and sequence, never value.

---

## The answer, in one line

**The lap is the right unit for one thing — a build becoming released to a household — and the wrong
clock for everything else. What you described this afternoon is not a repair to the release loop; it
is the second cadence, and its boundary is a COMMITMENT, not a close.**

| | **the estate-manager loop** (what you just described) | **the release loop** (exists, works) |
|---|---|---|
| what it decides | what we will do next, and at what scope | whether *this build* may be released |
| its boundary | ⭐ **scope committed** — the point after which the plan does not keep evolving | `cleared_sha` — Paul cleared a build |
| its unit | a **scope-setting round** | a **lap** (n rounds → one clear) |
| who gates | Paul, in a discussion | Paul, walking production |
| fires on | accounts · feedback · health, swept | a build existing |

**One follows the other; neither times the other.** `measured` 2026-09-07: of 75 commits since
midnight, **22 touch deployable app surface and 53 do not** (predicate: paths under `engine/ worker/
onboarding/ estate/ homes/ settings/ instance/ viewer.html`); `cycle/LAP-2-WORK-QUEUE.md` says the
same on its face — **3 of its 4 lanes declare `deploys: no`.** Work that cannot reach beat 1 of the
release loop cannot be timed by its beat 5. And `PRODUCT-ENGINE.md:55` — *a product that does not run
through Paul's mouth* — means a cadence whose exit is his own walk cannot be the one that scales to
household 3. `inferred`.

## Your loop's beats already have instruments — four of eight

| # | your words | instrument | state |
|---|---|---|---|
| 1 | *check for new accounts* | `tools/watch-accounts.py` | ✅ **`measured`** — landed today, `7b058a0` 12:47 ET |
| 2 | *feedback across all accounts, users and channels in production* | `tools/watch-feedback.py` | ✅ **`measured`** — `0a7bbf6` 12:40 ET. Its per-record sweep + six-key labelling contract is designed at `.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md`, unbuilt |
| 3 | *run all the full health checks* | `~/.claude/tools/health-probe.py --only fernwood` + CLAUDE.md's session-start block | ✅ exists, predates today |
| 4 | *consolidate that feedback* | the same PRACTICE design (dispositions per channel+record, clamped watermark) | 🟡 designed, not built |
| 5 | *put it into the backlog* | `product-steward` carries ruling → row, citation-bound | 🟡 on trial, round 1 recorded |
| 6 | *backlog rationalization* | `tools/check-backlog-drift.py` | ✅ **`measured`** — ran clean just now: *"rested. Last 2026-09-03 (4d) · 7 sections above the tracks · ranked list 336 lines below its head"* |
| 7 | ⭐ *scope-setting **discussion*** | **none, and none should be built.** You said discussion; this is the human gate (S2) | ⬜ by design |
| 8 | *a plan, then analyse how to execute it within the other loops* | the plan-of-record repair (D1) is the same seam | 🟡 queued |

⚠️ **Beat 3 must read the executors' FINDINGS, not their green lights.** Twenty minutes ago four seats
found Fernwood's rain-gauge record served to households in Roswell, Dahlonega and Bangor while
`check-estate-neutral.py` read **green** — it tests names; the leak is numbers and possessive
pronouns. `[[reference_match_payload_not_container]]`, again. A scope loop that consumes only the
checks' verdicts would have swept a green board over a production blocker.

## The named practice, since you asked for one — and it is not SAFe

The shape you described is **Kanban's cadence separation**: replenishment/commitment and delivery run
on **decoupled cadences**, with a **commitment point** — before it, items are *options* that may be
discarded at no cost; after it, they are committed and scope stops moving. That is exactly *"some kind
of commitment so scope doesn't just keep evolving,"* and it is the vocabulary for what your loop's
boundary is. Its **Service Delivery Review** is your beats 1–3; its **Replenishment** is beats 5–7.
⛔ **Do not import the seven cadences.** They assume many humans and shared capacity; you are one
operator with fourteen loops, which is the inverse, and this stack's own rule is that a ceremony
nobody runs is worse than none. Take the two ideas — *decoupled cadences* and *a commitment point* —
and leave the meetings.

## Against the spine (`~/.claude/rituals/CYCLE-SPINE.md`)

The release loop is the one loop in this repo whose **lap number is typed, not derived**. `measured`:
`momlib.lap_outcomes()` returns **8 laps for `MOM-CYCLE-LOG.md`, 3 for `cycle/fleet/CYCLE-LOG.md`, 0
for `cycle/release/CYCLE-LOG.md`** — the release heading at `:15` carries no date, so nothing matches;
`tools/release-state.py:49` supplies `{"lap": 1, …}` as a hardcoded default and **no code path
increments it**, while the CLI offers `--write`, `--cleared`, `--sha` and **no opener**. Both siblings
already do it right (`fleet_probe.write_state`: *"this writer never invents a lap"*). S4 asks that a
lap which HAS closed is MARKED; lap 1 closed at 11:19 ET and the chronicle carries no machine-readable
marker. **This is the boundary defect, and it is a one-line-per-lap fix, not a redesign.**

## What this does to the two rulings that depend on a boundary

- **R7 — the one-lap trial.** Its charter already measures its falsifiers **per round**, with round 1
  recorded and its confound named. It never needed a lap to be *measured*, only to be *ended*.
- **R6 — unruled proposals expire at lap close.** ⛔ **Unsafe as written, and the reason is measured,
  not preferred:** **22 files** now carry `ready: agent-proposed` (18 at the audit, four hours
  earlier) — **and one is `.plans/2026-09-07-pipeline-flex-point-AUDIT.md:13`, which you ruled at
  ~12:45 ET and which still reads `agent-proposed — Paul rules`.** `ready:` does not record a ruling,
  so an expiry on any clock closes decisions you already made. ⭐ **And the right clock is the new
  loop's, not the release lap's:** an unruled proposal is an *option before the commitment point* —
  it should expire when scope is next set, which is the beat that exists to look at it. (Weaker
  instrument, labelled: 21 of the 22 *name* practice-steward — literal grep; naming a seat is not
  authorship. The audit's own count of mine was 6.)

## ⛔ What I am not saying

Not that the release loop should change its beats — it ran 15 rounds and produced the first approved
production build. Not that anything matters more than anything else. Not that the executors need
replacing: `cycle/LAP-2-WORK-QUEUE.md` is already doing the engine-work tracking correctly **while it
is lap-scoped**. ⚠️ One risk, one line: `measured` — of 6 sampled queue rows, **5 appear nowhere in
`BACKLOG.md`**. A queue that outlives its lap with rows the backlog has never seen is a second backlog.

---

## What Paul must rule — five, each yes/no or A/B

| # | ruling | my answer | falsifier |
|---|---|---|---|
| **R-A** | **Is the estate-manager loop DECLARED before its first run** — a `cycle/estate/CYCLE-MAP.md` naming beats 1–8, marking 1·2·3·6 as instruments that already exist and beat 7 as an undesigned human gate? **A) declare, then run · B) run it once by hand, write the map from what ran.** | **A.** Your own standing rule — *before a cadence runs, its loop is designed* — and the release loop's own lesson: *a loop with no chronicle cannot tell you it only ran once*. One file, lane D, nothing before tomorrow. | If the first run's beats differ substantially from the map, A bought a fiction. Cheap test: run beats 1–3 at the next firing and diff what actually happened against the map before writing beat 4 onward. |
| **R-B** | **What is that loop's boundary — the commitment?** **A) scope committed at beat 7 = the boundary; the plan does not move until the next firing · B) no boundary; scope stays continuously open.** | **A.** It is the thing you asked for in your own words. It also makes "what changed since we committed" answerable, which nothing can answer today. | If a production blocker lands mid-cycle and the commitment cannot be reopened, A is too rigid — so the map should say what may break a commitment (a blocker of the rain-gauge class), not pretend nothing can. |
| **R-C** | **Where does R6's expiry hang?** **A) at the estate-manager loop's scope-setting beat, and not until `ready:` actually records a ruling · B) at release-lap close, as originally ruled.** | **A.** B expires the audit you ruled today. Sequence, not priority: R6 depends on R7's carry landing. | If `ready:` lines start being rewritten within a day of a ruling once product-steward runs, the precondition is met and the clock can start — measure at round 3, don't argue it. |
| **R-D** | **What ends the product-steward trial?** **A) the next `cleared_sha`, floor of 3 rounds · B) one full estate-manager cycle.** | **A.** Its falsifiers are already per-round and the release event is the boundary that exists today; B makes a trial wait on a loop that has never run. | If the next clear comes after 1 round, A without the floor rules on n=1 — that is what the floor is for. If every lap runs 3+ rounds, the floor never fires and is dead weight. |
| **R-E** | **Derive the release lap from its own chronicle** — rewrite `CYCLE-LOG.md:15` to `## Lap 1 — 2026-09-06`, add `<!-- outcome:closed at:<utc> -->`, open lap 2 with its own heading, and read `momlib.lap_outcomes('cycle/release/CYCLE-LOG.md')` instead of the default at `release-state.py:49`. **yes/no** | **Yes.** One borrowed parser, no new vocabulary, no second register, and both siblings already prove it. | If lap 2's heading never actually gets written, the borrow fails at lap 3 — check that the heading exists before wiring anything to read it. |
