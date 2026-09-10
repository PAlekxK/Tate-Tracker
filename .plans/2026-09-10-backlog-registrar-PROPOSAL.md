# The backlog registrar — the door lanes forward to, and the three rulings it cannot make

- row: `BACKLOG.md` § ▶️ NEXT (process; **no row yet — this proposes one**, and §2·A is the ruling that decides whether it may have one)
- objective: O5
- class: engine · declared
- class-note: how work is registered is shared machinery every estate's work is planned through; nothing renders from it, so a divergence is a legibility cost, not a defect
- kind: process
- stage: draft
- ready: **agent-proposed 2026-09-10 — Paul rules.** ⛔ Nothing in §2 is applied.
- seats: practice-steward → **waived with a reason**: it rules on METHOD and *"does not prioritize"* by charter, and §2·C is a packaging-and-renewal call, which is outside it · engineering-partner → waived: no code is proposed; the one tool change (§0) is handed to its owner as a finding · ux-expert · content-steward · ai-advisor → waived: nothing here reaches a person
- commissioned: `paulkirschenbauer-af` (coordinator), 2026-09-10 — a standing registrar lane `[paul-raised 2026-09-10]`
- depends-on: `.plans/2026-09-10-PLAN-OF-RECORD.md`
- depends-on: `.plans/2026-09-10-G1-RULING-PACKET.md`
- stage-note: 2026-09-10 — written after one live transaction (`06874b7`) proved the door on a real forward rather than in the abstract.
- stage-note: 2026-09-10 ~5:20 PM ET — **first session as a WINDOW closed clean** (`handoff/handoff-backlog-registrar.md` @ `15b4f9a`). Four lanes forwarded in one session (b8 · b3 · claude-meta · ec); four rows transcribed verbatim at `ea63a0e` and `d3f14dd`; two prior placements read back rather than duplicated. ⭐ `tools/registrar-sweep.py` found **five defects in itself, all on its author**, in its first two hours — selftest 12 → 17, each pinned by a mutation (`9271c4c`). The ③/④ ruling packet is with Paul (`.plans/2026-09-10-link-syntax-and-proposal-intent-RECOMMENDATIONS.md`); nothing in it is applied. ⛔ Three refusals of the coordinator, all measured right: the "four rows" count was the wrong predicate (2 false pointers, 5 stale-prose, 5 consistent); a discharge was not authored unmeasured; this file stays an orphan rather than clear itself with a false claim. **Later the same evening:** Paul ruled both packet questions as recommended (*"I'm good with the recommendation there"*); ③ landed (`e5626b7`, `889ae75` — `→ PLAN ·` defined at `BACKLOG.md:14`, two false pointers flipped, the checker now reads every pointer against its header both ways; 0 false claims, 2 stale-prose rows named for their owners); ④ **ruled and PARKED** at close-out rather than half-landed — recorded in `check-backlog-ready.py`'s `UNGRADED_BY_DESIGN` and the handoff, first task of the next session. Five more forwards placed (`e5626b7`). This file's own `row:` becomes `proposed` when ④ is built.

> ⛔ **FLAG AND PROPOSE.** Nothing below is applied. The registrar transcribes; it does not adjudicate.

---

## 0 · 🔴 THE FIRST TASK ON MY OWN LIST WAS WRONG — retracting it, with the measurement

I reported *"the 4 back-pointers are ONE write, ~4 lines, zero judgement — the cheapest closable thing on the board."* The coordinator ranked it first, twice. **It is not a write at all, and doing it would have been a false status claim.**

`measured 2026-09-10`, all four candidates:

| plan | `stage:` | `ready:` |
|---|---|---|
| `2026-09-10-testing-architecture-PLAN.md` | draft | agent-proposed — **Paul rules** |
| `2026-09-03-c3-trace-query-PLAN.md` | ready | agent-proposed — **Paul rules** |
| `2026-09-03-c3-trace-query-PROPOSAL.md` | *(none)* | *"Paul's; nothing here is stamped"* |
| `2026-09-03-product-name-PLAN.md` | ready | agent-proposed — **Paul rules** |

⛔ **`POINTER_PAT` (`tools/check-backlog-ready.py:114`) requires the literal `→ READY · .plans/…` — and `BACKLOG.md:14` defines READY as *"cleared by Paul."*** **The register has exactly one link syntax and it is welded to a status.** Writing the back-pointer any of these four is owed asserts a clearance Paul has not given. **Not mine to author, and `.decisions/fernwood-22.md` already refused it by name** — minted against a relayed instruction to *"fix the orphan by adding the pointer"*, with a standing recommendation: **accept the flag.**

### ⭐ AND THE MEASUREMENT THAT MAKES THIS WORTH A RULING RATHER THAN A SHRUG

**Four live rows already write `→ READY ·` and then disclaim it in prose:**

| line | the pointer | the prose beside it |
|---|---|---|
| `:139` | `→ READY · …vocabulary-nicknames-PLAN.md` | *"the pointer is the readiness check's row shape, **not a claim**"* |
| `:248` | `→ READY · …zones-PLAN.md` | *"stage `design`, **awaiting Paul's `ready:` stamp**"* |
| `:1441` | `→ READY · …guru-retrieval-PLAN.md` | *"**Not stamped.**"* |
| `:3297` | `→ READY · …c7-condo-paper-model-PLAN.md` | *"**Not stamped.**"* |

⭐ **So the file already says READY to its instrument and NOT-READY to its reader, four times, and the disclaimer is invisible to the tool.** That is not a workaround; it is **the register lying to its own instrument in the one field the instrument exists to read.** Adding four more instances makes the lie load-bearing. ⛔ **I decline the write and recommend against anyone else making it.**

**The fix is already written down** — `.decisions/fernwood-22.md` option **(c)**: *"a real instrument gap worth its own row: `stage: draft` is exempt from the `ready:` stamp (`:395`) but **not** from the orphan check — so the checker cannot currently express *a plan for something not yet ranked*."* **Proposed shape, for the tool's owner, not built here:** a second recognised syntax — `→ PLAN · .plans/…` — meaning *this row has a plan and the plan is not cleared*. Orphan-clearing, status-free. Then the four disclaimed rows above can drop their prose caveats and say what they mean.

⚠️ **This is the fourth instance today of one shape — a correct measurement carrying a wrong inference** (`home` UNREADABLE · *"A2 is partial"* · the `testing-arch` merge · **this**). The other three were caught by the receiving lane. **This one is mine, and it was caught by checking the tool's source before writing rather than after.** `grep` located the gap; reading `:114` and `:14` established it.

---

## 1 · THE CADENCE — a commit trailer, proved on a live forward

⛔ **Do not build a second inbound door.** `cycle/requests.jsonl` already exists (52 lines, `~/.claude/tools/ask-cycle.py`, readers in `fleet_probe.py` and `check-public-build.py`), and `BACKLOG.md`'s own head names its two defects: **Track-B-scoped**, and ***"nothing sweeps that door on a cadence."*** Both are what a registrar fixes. Last write: 2026-09-05.

**But the door a lane must remember is a door a lane does not use.** So the forward is a **git trailer** — zero extra commands, zero extra files, `git` is the transport:

```
Backlog-Register: <BACKLOG section or row> — <what changed in one clause>
Backlog-Forwarded-By: <lane> @ <sha>       # only when transcribing another lane's status
```

⛔ **BOTH LINES GO IN THE SAME FINAL PARAGRAPH AS `Co-Authored-By:`, WITH NO BLANK LINE BETWEEN.** This is
not style — see the two defects below.

**`Backlog-Register: none — <what it needs>`** is legal and is the **highest-value line in the system**:
*"I built X and it has no row"* is exactly what `onboarding-ask-b3` reported and what nothing captured.

**The sweep, and it needs no tool:**

```bash
git log --format='%h %(trailers:key=Backlog-Register,valueonly)' | grep -v '^[0-9a-f]* *$'
```

**Four properties, each earned:**
1. ⭐ **The trigger is the commit, not a clock.** A cadence in hours is a thing to remember; a cadence in commits fires when there is something to say. `MOM-CYCLE-MAP.md`: *the loop rests, input fires it.*
2. ⭐ **The sweeper already exists** — `git` parses trailers natively. **Nothing to build, install or keep in sync.** A registrar that needs a tool written before it can start is a registrar that starts late.
3. ⛔ **A lane never edits `BACKLOG.md` and never decides where a row goes.** Placement is the registrar's; that is the whole trade.
4. ⚠️ **Counts derive from `git log`, never typed.**

### 🔴 TWO DEFECTS IN THE FIRST VERSION OF THIS SPEC — found by running it, and both are why it is stated so exactly

⭐ **I shipped this spec as `Register:` in its own paragraph and claimed *"proved, not proposed"* on `06874b7`. Both halves of that claim were wrong, and one command found it.**

1. ⛔ **IT WAS NOT A TRAILER AT ALL.** `git` parses trailers only from the **last paragraph**. My `Register:` block sat above a blank line and the `Co-Authored-By:` block, so `git log --format='%(trailers:key=Register)'` returned **nothing** on my own commits — while `Co-Authored-By` parsed fine from the paragraph below it. **The spec was passing only under `--grep`, which is string matching, not parsing.** ⭐ *Matching the string rather than the thing* — the coordinator's own recorded failure from this morning, arriving on my instrument by the same route.
2. ⛔ **`Register:` IS ALREADY DOUBLE-BOOKED IN THIS REPO'S HISTORY.** `eac5648` carries `Register: radar basemap → Esri light-gray…` — a different meaning entirely, and it is a **false positive on the `--grep` sweep today.** `VOCABULARY.md` §4's whole discipline is that a double-booked key costs more than the name saves (`group` is the standing example, still unfixed). **So `Register:` is REJECTED, and this line is the record of why** — otherwise the next reader re-proposes it.

⭐ **The general lesson, which is the same one three times today: a control that has never been run against its own output is a claim, not a check.** I wrote a falsifier saying the sweeper works, then ran it, and it did not.

### ⛔ The half a trailer cannot carry, stated so it is not discovered later
A trailer rides on a **commit**. Two of today's most valuable register facts had none: `paulkirschenbauer-b8`'s assessment existed for two hours with **zero commits**, and `.plans/2026-09-10-interests-reframe-VERIFY-82.md` is **still uncommitted** in a closed window's worktree. **A trailer registers what was committed; it cannot register what was not.** The complement is the registrar's own sweep at each lane's close — and it must print **what it could not place**, never drop silently.

---

## 2 · THE THREE RULINGS — one packet, one root cause

⭐ **The root cause they share: this register cannot say *"a thing exists and nobody has ranked it yet."*** It has ACTIVE, DEFERRED, IDEATION, READY, SHIPPED, KILLED — and no state for *scoped, unranked, awaiting you*. Everything below is that gap wearing three costumes.

### A · ⭐⭐ Is a `-PROPOSAL` a DOCUMENT or an ITEM? — **carried as ⑥ of the G1 packet; cited, not restated**

⛔ **The ruling itself lives in `.plans/2026-09-10-G1-RULING-PACKET.md` ⑥** (`51199b5`), which carries this
finding and its reasoning. **Read it there.** Repeating a live ruling in a second file is how this corpus
mints two registers that each read current — its own most-repeated failure.

**What this file adds, and it is only the measurement behind ⑥:** `measured` — **10 of the 28 "orphans"
carry `row: process (no BACKLOG row yet — this proposes one)`.** They are not orphaned; **they are queued
on Paul**, and the register has no state that says so. That absent state is the root cause §2 opens with,
and ⑥ is the call that creates it.

### B · Sole writer — confirmed as SCRIBE, with one hole only Paul can close

The coordinator has confirmed the shape and the reasoning: **transcribe verbatim, attributed to the lane and its sha; flag and propose separately in a marked voice.** The property that carries it: **every status becomes attributable to the lane that measured it**, rather than to whichever session last had the file open.

⛔ **The hole:** `CLAUDE.md` records `BACKLOG.md` as *"written by **two loops** (mom + fleet)."* A registrar is a **third** writer unless those loops forward too. **One door, or it isn't a door** — and the coordinator cannot settle this by fiat, because those loops are chartered elsewhere.

⚠️ **The measurement that makes sole-writer safe, and it inverts the expected objection:** `BACKLOG.md` took **1 commit today** against a 09-03→09-08 rate of **17/day** (36 · 18 · 2 · 7 · 20 · 27). **The bottleneck risk of one writer is smaller than the current failure — the write rate is already one.** The file is not contended; it is **abandoned**, because six lanes each correctly refuse to touch it and nothing catches what they drop.

### C · The product-steward trial — renew ONE round, conditionally, or kill it

`measured`, from the run:
- ✅ First falsifier **not tripped**: redundancy **18 of 37 = 49%**, threshold 80%.
- 🔴 Second falsifier **IS tripped**: **20 questions opened against 19 carried** — its own words, *"a bottleneck wearing a helper's name."*
- ⬜ **INCONCLUSIVE**, 2 rounds, **both confounded by its own ledger.**
- 🔴 The round produced nothing: 5 seats, **0 readable reports**, 4 carrying `WALK-REPORT-UNWRITTEN`, no consolidation at build `196e146`.

⭐ **The decisive point: the trial cannot be settled by anything the steward controls.** Its own settling condition is *a round that starts CLEAN* + *a THIRD round*. Clean needs (a) a rationalization applied — unread on `backlog-rat` — and (b) walk reports written, which is **the harness lane's, not the steward's**. ⛔ **Renewing for a round that cannot settle it is how a trial becomes permanent.**

**Recommended:** renew for **one** round, **conditional on a clean round being scheduled**; if the reports are unwritten again, **kill it** rather than record a third confounded row. **Options:** (a) conditional renewal *(recommended)* · (b) unconditional renewal · (c) kill now on the tripped second falsifier.

⚠️ **And an instrument defect worth one line:** two of three triggers are **majority-UNCHECKABLE by their own predicates** — T1 sees 20 of 29 ruling lines (9 have no quotable verbatim); T3 sees 2 of 10 plans (8 have no stage-note to age). **Those are floors reported as counts.** T1's 8 quotable misses are the registrar's natural inbox — `cycle/release/CYCLE-LOG.md:610` *"i want an invite link for myself"* and `:889` *"we should have an automatic feedback check"*; **the second is a feedback-loop capability, not paperwork.**

---

## 3 · THE LANE REGISTER — 2026-09-10, and what each has produced

| lane | durable output | register debt |
|---|---|---|
| `tate-tracker-ec` | `worker.js` credential/account path · `publish-digest.py` swallow fix (`b21e286`) · now building B3's `found` verb, lab only | rulings landed today are in the register; the **B3 open gate is Paul's** |
| Lane 3 · walk harness | ✅ **merged to main at `6b0785a`, 9/9 selftest** — `journey-walk` · `elicitation-lens` · `check-canon-scope` · `seat-portfolio` · `household-fixtures` · `.decisions/fernwood-15..22` | **10 of 22 decision cards are reachable from no `BACKLOG.md` row**; the header says *"11 of 12"* and `:184` forbids stating a count on that line |
| `paulkirschenbauer-b8` (zones) | ✅ `2395268` — the assessment, keyless, $0, 23/23 answer key | ⭐ **first live forward, transcribed at `06874b7`**; its other three edits are its own files |
| `onboarding-ask-b3` | `4439010`, copy staged | 🔴 `.plans/2026-09-10-interests-reframe-VERIFY-82.md` **uncommitted, orphaned, belongs to a closed window** — needs a disposition |
| `paulkirschenbauer-3b` | `~/.claude` only; zero Fernwood writes | ⚠️ **the security seat was ratified 09-02 as a BLOCKING PREREQUISITE on the auth build; auth shipped; `security` appears ZERO times in the plan of record and the work queue** |
| coordinator | `PLAN-OF-RECORD.md` · the boundary | ⑥c went stale within four hours of being written; fixed at `0538f4a` |

---

## Files touched

| file | what | status |
|---|---|---|
| `BACKLOG.md` TIER 2 · 9 | b8's buildings-falsifier discharge, **transcribed** | ✅ **applied** `06874b7` |
| this file | the proposal | ✅ applied |
| **everything in §0 and §2** | — | ⛔ **proposed only** |

⛔ **Not touched, and not mine:** `worker/worker.js` and `worker/digest.json` were modified-uncommitted in the main tree throughout (`tate-tracker-ec` working); `cycle/release/cycle-state.json` is generated by the post-commit hook. **Only `BACKLOG.md` was staged.**

## Sequence

1. **G1 packet ⑥** — the `-PROPOSAL` ruling. Discharges ten orphans, most of the suffix ambiguity, and the argue-with-the-checker habit in one call. ⛔ Ruled there, not here.
2. **§2·B** — sole-writer, and the two-loops door with it. They are one question.
3. **§0's instrument fix** — `→ PLAN ·` as a status-free pointer, handed to `check-backlog-ready.py`'s owner. ⛔ **Until it exists, nobody writes the four back-pointers.**
4. **§2·C** — the trial. Independent of the rest.
5. **§1's trailer** — already live; the coordinator pushes the format to the lanes.

## Falsifier

> ⭐ **A lane that commits with a `Register:` trailer and never opens `BACKLOG.md` still has its work registered within one sweep — and the registrar's sweep names everything it could not place.**

**Three narrower ones, each one command:**
- `git log --format='%h %(trailers:key=Backlog-Register,valueonly)' | grep -v '^[0-9a-f]* *$'` grows by at least one line per lane per working session. **If it stays at the registrar's own entries, the trailer is a discipline nobody follows and should be replaced by the `ask-cycle` door, not re-exhorted.** ⛔ Use the trailer parse, never `--grep`: `--grep` matched a 2026-08 commit using the word for something else.
- `python3 tools/check-backlog-ready.py` reports **fewer** orphans after §2·A is ruled, **without any new `→ READY ·` appearing in `BACKLOG.md`.** If orphans fall because pointers were added, the ruling was implemented as the lie §0 refuses.
- No `.plans/` header ever again contains the string *"the orphan flag is expected"*. **A file arguing with its own checker is the measure of this failing.**

⛔ **And the falsifier for the registrar seat itself:** if a lane's work reaches `BACKLOG.md` only because a human remembered to carry it — the condition that produced 28 orphans and a 1-commit day — **the seat has not earned its place and should be closed**, not renewed.

## QA

**Ships no code.** Every `measured` claim was read at `06874b7` and is re-checkable:

| claim | how to re-check |
|---|---|
| all four back-pointer candidates await Paul | `grep -m1 '^- ready:' .plans/2026-09-{10-testing-architecture,03-c3-trace-query,03-product-name}-PLAN.md` |
| the register already disclaims four `→ READY ·` pointers | `grep -n "→ READY ·" BACKLOG.md` → `:139`, `:248`, `:1441`, `:3297` |
| `POINTER_PAT` requires the literal, and READY means cleared-by-Paul | `tools/check-backlog-ready.py:114` · `BACKLOG.md:14` |
| 28 orphans, 18 of which declare their own `row:` | `python3 tools/check-backlog-ready.py \| grep -c "orphan)"` |
| `BACKLOG.md` took 1 commit today vs 17/day | `git log --since=2026-09-01 --format='%ad' --date=format:'%m-%d' -- BACKLOG.md \| sort \| uniq -c` |
| the trial's two falsifiers | `python3 tools/product-steward.py` |
| the drift detector reads **rested** — correctly | `python3 tools/check-backlog-drift.py` → last 2026-09-08 (2d) |
| b8's discharge is b8's, not the registrar's | `git show 2395268:.plans/2026-09-10-zones-automation-ASSESSMENT.md` §0, §1b |

⚠️ **What this does NOT verify:** any live KV, any origin, any deployment. **No network call was made.** ⭐ **And the lane states in §3 for `tate-tracker-ec` and `paulkirschenbauer-3b` are the coordinator's readings, not mine** — by this repo's own rule they are **relayed, therefore hypotheses**, and are labelled as such rather than promoted.
