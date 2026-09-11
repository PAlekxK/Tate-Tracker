# Handoff: fernwood — TESTING REVAMP · scope and audit the testing cycle (lap 8 · row T), its own window

<!-- generated 2026-09-11 ~7:15 AM ET · source: Tate-Tracker@a95413d1 on LOCAL main · written by the coordination window (tate-tracker-ea)
     RECEIVER: verify the sha against HEAD. Cite symbols, stamp the sha. Written with a QUOTED heredoc — the previous brief tonight
     committed empty on a backtick; check this one is not zero bytes before you trust it. -->

## 1. Mission

Paul, 2026-09-11 ~7:10 AM ET: **"launch a dedicated session to fully scope and audit the testing cycle revamp."** Earlier:
*"our testing takes a long time and has a lot of the same journeys… it seems a little repetitive"* · *"move it up to the next
lap… ideally we can figure it all out and do it in one piece"* · *"this is a very good lap to audit the testing cycle with,
with context, because it seems like the testing is just going on and on and on."*

You own TWO things and deliver ONE file the build window can execute:
1. **The AUDIT of lap 7's testing cycle** — where the time went, what each stop bought, the structural causes. A
   practice-steward audit is ALREADY RUNNING from the coordination window and lands at
   `.practice/2026-09-11-lap7-testing-cycle-AUDIT.md`; **read it when it lands, do not re-run it**; extend it only where it
   says "not measurable from the record" and you can measure.
2. **The SCOPE — row T of lap 8, sized by symbol**: `.plans/2026-09-11-testing-revamp-PLAN.md` (`stage: ready`, `ready:
   agent-proposed — Paul reads before the lap-8 build window opens`), superseding the SEQUENCE of
   `.plans/2026-09-10-testing-architecture-PLAN.md` under Paul's eight rulings (below), in the lap-7 build plan's shape:
   ordered steps by file:symbol · per-step CHECK · what moves the candidate · seams with lap 8's other rows (the door) ·
   the falsifiers · what is OUT with its ruling · what the build window's brief must say · what Paul must still rule.
   **Say plainly whether one piece fits beside the door in lap 8; the ruled fallback is two laps.**

## 1b. Paul's caveat on the audit's framing `[paul-stated 2026-09-11 ~7:20 AM ET]` — binding on both deliverables

*"To be fair, we also did commission a big UX review, so there's probably a lot of changes, and this is a big build. I don't
want to artificially restrict how much testing we do. I think it's probably too much, but I do want to call out that we're
launching pretty big builds as well."* So: **normalize every cost against build size** (lap 7 = 59 steps across five rows,
four pages, the Worker and the template, carrying a two-pass UX sweep's findings and an 11-ruling design bundle; compare to
lap 6's one row on the same basis) · **separate THOROUGH from MIS-SHAPED** — time that found real defects (F1, B) is
thoroughness paid for; time re-driving unchanged paths, harness self-testing (F2) or the battery testing its own cadence (A)
is shape · **recommend no ceiling on testing volume** — recommend where a walk's cost buys nothing. The plan's steps are
judged by cost-per-finding and re-work avoided, never by fewer walks for their own sake.

## 2. Paul's rulings — in force, cite never re-open (`cycle/release/CYCLE-LOG.md` § "LAP 8 GAINS A ROW", 2026-09-11 ~7:00 AM ET)

Q2 gate ① changes its unit from `seat` to **(journey, lens)** — a change to the release condition; its own falsifier gates it ·
Q3 a lens is a **reading posture only**, no inputs · Q4 first cut **J0 · J3 · J8 built; J1 · J5 · J7 named-unbuilt** (printed
unwalked every lap); J2 re-scoped ("returning, founded nothing") or retired · Q5 **properties cap 3**, a fourth only for a
named code branch · Q7 the ratio becomes **a declared cell list per lap at beat 6**, the gate prints the longest-unwalked
cells, **no scheduler, no test-selection engine** · Q1 **unbundle the credential axis and ship the per-run unspent invite
first** (a property of the arrival, never a role) · Q6 roster **five owners including Paul** (fernwood-20) · Q8 add the
`→ PLAN ·` pointer · **impact-scoped re-runs**: a re-sha re-runs the journeys that touch what changed and carries the
untouched journeys' evidence forward with the byte proof named (a change classifier in `release-gate`) · **placement: lap 8,
one piece, gate change FIRST**, before the door's battery, so the door is certified on the new unit.

## 3. Read first

1. `.plans/2026-09-10-testing-architecture-PLAN.md` — the whole thing (§1 inventory · §2 the unit redesign · §3 the three
   axes · §4 the journey set · §5 migration · Sequence P0–P6 · §7 where the row's own argument is wrong · Q1–Q8).
2. `BACKLOG.md` § 🧪 SPLIT THE JOURNEY FROM THE READER (the row) · TIER 1 · 22 (the gate's camera cannot see the stop it was
   built for) · TIER 1 · 25 (the gate kit) · the `seat-portfolio.py` and `walk-fixtures.py` lines in CLAUDE.md's pickup block
   (a seat is a SHAPE not a person; a journey is an action list PLUS its entry state).
3. `cycle/release/CYCLE-LOG.md` "## Lap 7" — the battery's whole story tonight: the shake-out · candidate 1 `d7d6c9f` ·
   beat 10 (F1 a ranked-household throw lab could not see; F2 a correct PO-box refusal scored as failure) · candidate 2
   `12912b9` · J2 unwalkable by model · beat 10 again (A the lane's own limiter hit by the battery's cadence; B a pre-existing
   session defect only a sign-out/return walk reaches) · candidate 3 `87c7aae` · "Prepared for beats 9–12".
4. The tools: `tools/journey-walk.py` (JOURNEYS, per-run browser context, `--watch`, journey_entered, the refusal branch) ·
   `tools/release-gate.py` (the per-sha unit, six clauses, M8a–M9b) · `tools/walk-integrity.py` · `tools/walk-brief.py` ·
   `tools/seat-portfolio.py` (RUN IT) · `tools/walk-fixtures.py` · `tools/household-fixtures.py` · `tools/synthetic-identity.py`
   · `tools/pages-deploy.py`'s headless PAGEERROR check · `tools/check-telemetry.py` · `tools/read-glance-order.py`.
5. `.private/synthetic-walks/<seat>/<timestamp>/` — tonight's runs: counts, timestamps, failed actions, stop ids. ⛔ Never
   quote a synthetic's typed text; counts and ids only.
6. `.plans/2026-09-11-lap8-build-PLAN.md` (row T's stage-note; the door's steps you must not collide with) ·
   `.plans/2026-09-10-lap7-build-PLAN.md` §5 (what "full battery once" meant) · `cycle/release/CYCLE-MAP.md` (beats 7–11).
7. `.plans/2026-09-03-qa-test-vs-ux-review-PROPOSAL.md` · `.plans/2026-09-05-journey-test-cycle-PROPOSAL.md` ·
   `cycle/release/LAP3-AUDIT.md` §5.

## 4. Seats

practice-steward (audit — running; read it) · **engineering-partner LEADS the sizing** (path-evaluation: the gate unit, the
lens/journey split, the change classifier, the cell-list print, the per-run invite — by symbol, with checks) ·
user-researcher (the READER axis is its ruling per the 09-10 plan: what a lens IS, named lenses with their falsifiers —
never a persona presented as fact) · security-steward (fixtures and credentials per env; the per-run invite; what a
transcript may record). Each writes its own trail in its own directory; you synthesize into the one plan.

## 5. State at a95413d1

Lap 7's battery is RUNNING at candidate 3 (`87c7aae`) in the build window `tate-tracker-94` — **do not touch
`tools/journey-walk.py`, `tools/release-gate.py`, `tools/walk-integrity.py` or anything it is using until lap 7 closes**; you
READ them and SPECIFY changes. Lap 8 is scoped (door · migration gate · email editor · Midtown · fixture stamp · ribbon
seam · riders) and now row T. The backlog window is CLOSED; forward rows to coordination (`tate-tracker-ea`) by message.

## 6. Guardrails

Read-only on every tool while lap 7 runs. No BACKLOG.md, CLAUDE.md, VOCABULARY.md, CYCLE-MAP.md (a release-condition change
is Paul's; you SPECIFY the CYCLE-MAP edit, quoted, not made). `git commit --only <your paths>`. No deploy, no KV write, no
browser. Hold the plan's own "do not build" list to account: no scheduler, no test-selection engine, no sampling budget.

## 7. Open for Paul (do not resolve)

Whether one piece fits lap 8 beside the door (you recommend; he rules) · J2 re-scope vs retire · the named lenses
(user-researcher proposes; he rules) · any release-condition wording.

## 8. First tasks

0. Verify the stamp and that this file is not empty; write `handoff/handoff-testing-revamp.readback.md`; tell Paul; wait for
   the grade.
1. On clear: read §3, check whether the AUDIT has landed, run `seat-portfolio.py`, convene the seats, draft the plan.
