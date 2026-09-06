# MIGRATION READINESS — where the record disagrees with the world

**Author:** practice-steward (method only) · **Date:** 2026-09-06 ~19:00 ET
**Reconciled against:** local `main` `6d94a9a` · `origin/main` `294c0b4` · `origin/staging` (fetched 18:31)
**Companion:** `.plans/2026-09-06-freeze-register-PROCESS.md` — the register Paul asked for. Read that
first; this file is its evidence.

⛔ **Read-only run.** No tracked file was edited, nothing was committed, nothing pushed. Three sessions
share this tree tonight.
⛔ **Mom's feedback was NOT read.** No channel was fetched, `--pickup` was not run, `--address` was not
run. Everything below about her queue comes from *source code and state files*, never from her records.
⭐ **Method, not content.** Nothing here says one vehicle, one note or one feature matters more than
another. Where a call needs real-world context, it is named as Paul's and left there.

**Grades:** `[measured]` = verified against the world tonight, cited · `[inferred]` = derived from two
measured facts · `[assumption]` = neither, and marked so it can be shot down.

---

## THE HEADLINE, in four lines

1. **The record's errors all point the same way: they say *more frozen* and *more open* than reality.**
   Seven of the eight drifted artifacts found tonight err in the safe-looking direction. That is
   consistent with this repo's own ratified rule — *closing a thread and recording the closure are two
   acts and only the first has a natural trigger.*
2. **Track B's door reports 9 unread; the honest number is 5 never-actioned + 1 deliberately held.**
   Neither figure is the door's, and the door's zero-branch would call the other 6 *"all handled."*
3. **There IS a coherent path to Mom-on-production, and its first blocker is a ruling, not a build:**
   two of Paul's rulings (*"poured into that instance"* vs *"her blank slate"*) imply different sunset
   checklists, and the newer one exists only in a Python docstring.
4. **The sunset's hardest requirement is already satisfied and nobody scheduled its refresh.** A
   complete 175-key archive of her estate exists, taken 2026-09-06 00:08:36. Nothing re-takes it, and
   her instance is still live.

---

## Q1 · WHERE THE RECORD DISAGREES WITH THE WORLD

Eight disagreements, each with the direction it errs and what it would have caused.

### 1 · `BACKLOG.md:74` — the fleet freeze that was already lifted `[measured]`
**Says:** *"Track B fleet laps (lap 3 is FIRED on SEASON + INBOX and **stays unrun on purpose**)."*
**World:** lap 3 opened and **closed** 2026-09-05, on Paul's word — *"launch a fleet cycle… focusing on
the 200."* `cycle/fleet/CYCLE-LOG.md:45` (heading `✅ CLOSED`), `cycle/fleet/cycle-state.json`
(`lap_count: 3`, `last_lap.outcome: "closed"`, `date: 2026-09-05`).
**Errs:** toward MORE frozen. **Would have caused:** a session to refuse fleet work Paul had released —
i.e. exactly the "partial unfreeze" being invisible where a reader looks.
⭐ The fleet chronicle got this right and kept the superseded note beside the release, saying why:
*"Kept rather than deleted so the two are not read as one."* **The canonical file is the one that
drifted**, and BACKLOG.md was itself committed four times today (last `382b1d0`, 14:07) without touching
this block. Last substantive edit to § FOCUS FREEZE: `d41b2e7`, **2026-09-04 11:16 ET**.

### 2 · `.plans/2026-08-31-zones-traced-with-mom.json` — a status string outlived its fold by 6 days `[measured, two methods]`
**Says:** `_meta.status` = *"PROPOSAL — NOT FOLDED. zones.json is unchanged."*
**World, method 1:** `51d6007` (2026-08-31 18:41) — *"THE FOLD — Mom's map is canon: 18 zones."*
**World, method 2 (independent of git):** `zones.json` holds 23 zones, and **14 of the plan's 16 traced
`zoneId`s are present verbatim** (`the-bank`, `eastern-woodlands`, `western-garden`, `western-upper-patio`,
`western-lower-patio`, `the-bluff`, `lawn`, `fern-garden`, `pond-area`, `eastern-patio`, `lower-40`,
`st-francis-garden`, `lower-parking`, `stable-grounds`).
⭐ **The file also contradicts itself internally:** its status text says the fold *"must decide the four
open questions below"* while its own `openQuestions` is `[]` and its `resolved[]` array carries the
rulings. **A reader had a falsifier inside the same object and the string still won** — which is why a
subagent reported the stale string as a live finding earlier today.
**Errs:** toward MORE open. **Would have caused:** re-doing a completed fold, or re-litigating four
questions Paul already ruled.

### 3 · `data/cycle-state.json` — the mom loop publishes "nothing is waiting" `[measured]`
`state: ARMED` · `unresolved_arrivals: 0` · `generated_at: 2026-09-01T23:24:08` — five days old, written
two days before the hold existed. **Errs:** toward clean. **Would have caused:** any board or `/pickup`
rendering Track A as owing nothing while arrivals are deliberately held. The § FOCUS FREEZE block
predicted exactly this — *"neither `mom-cycle-status.py` nor `fleet_probe.py` publishes a HELD phase"* —
which makes the drift *documented*, not *detected*.

### 4 · `cycle/fleet/cycle-state.json` — the inbox count is one behind its own door `[measured]`
State says `INBOX … 8 unread` (written 2026-09-05T14:31Z = 10:31 ET). The door's own predicate now
yields **9** — row 52 was appended later the same day. Small, and it is the shape that matters: **a
state artifact is a snapshot and the door is the truth**, so a board reading the snapshot under-reports.

### 5 · `cycle/requests.jsonl:41` vs `BACKLOG.md:1322` — one item, two verdicts `[measured]`
Door row 41's disposition: *"ROUTED, NOT RESOLVED — fleet lap 1 beat 3 REOPENED."*
Destination: *"✅ **P7 RESOLVED** — the spark plugs were never a contradiction. They were a SEQUENCE"*
(with both Gmail order numbers, NGK140052 / NGK196860).
**Errs:** toward MORE open, at the door. **Report the contradiction, do not resolve it:** which copy
should be updated is a bookkeeping call, but *whether the door's rows are maintained after routing* is a
process question, and today the answer is measurably *no*.

### 6 · `fleet_probe.py` — the zero-branch would call 4 live items "all handled" `[measured, latent]`
`tools/fleet_probe.py:112` — `open_rows = [r for r in rows if (r.get("status") or "open") == "open"]` —
and `:125` returns `f"inbox clear ({len(rows)} filed, all handled)"`. **6 of 15 rows are not `open`**, and
**4 of those 6 are still live work at their destinations** (P4, P6, P8, and P9-routed-out).
⚠️ **Latent, not firing:** the 9 open rows keep the probe on the other branch, so the misleading string
has never been printed. It becomes true the moment the 9 are drained — which is the exact moment
somebody would trust it.

### 7 · A meta-lap note pasted into the wrong chronicle `[measured]`
`MOM-CYCLE-LOG.md:40` and `cycle/fleet/CYCLE-LOG.md:40` are **byte-identical**, including *"⛔ This
loop's trigger is unchanged and was not fired: it still rests on HER input."* That is true of the mom
loop and **false of the fleet loop**, whose four declared signals are SEASON · INBOX · PROVENANCE ·
STALE-OPEN (`cycle-state.json`, `cycle/fleet/CYCLE-MAP.md:119`). **Errs:** by describing the wrong loop.
**Would have caused:** a reader to conclude the fleet loop waits on Mom, and therefore that it is
covered by her channel hold — which is precisely the axis collapse the register exists to prevent.

### 8 · `.plans/2026-09-06-one-environment-DECISIONS.md:F5/§4` — 23 minutes stale `[measured]`
§4 lists as still open: *"**F5's sentence** — is the legacy viewer left in place at `home`?"* The file's
mtime is 17:46; `9cb468d` at **18:09:36** records Paul answering it — *"Fernwood as it exists that mom
has access to just stays as it is. The production home is her blank slate"* — and changes
`tools/pages-deploy.py` accordingly. **Errs:** toward MORE open. Included **not** as a criticism of a
three-hour-old file but as the cleanest possible demonstration of the rot rate: **a decisions file went
stale in 23 minutes, and the ruling that staled it landed in a Python comment.**

### 9 · A marker that looks machine-readable and is read by nothing `[measured, two methods]`
Both chronicles carry `<!-- freeze: 2026-09-03 -->`, in the same style as `<!-- meta-lap: … -->`.
`<!-- meta-lap: … -->` **is** parsed — `~/.claude/tools/cycle-docs-check.py:141`, `META_ACK_RX`.
`<!-- freeze: … -->` is parsed by **nothing**: `git grep 'FOCUS FREEZE' -- '*.py'` → 0, and the portfolio
checker has no freeze branch. **Errs:** by implying a mechanism where there is a convention. ⭐ It is
also the cheapest hook available — extend the existing marker rather than invent a format.

### 10 · One live control that is correctly RED, and nothing drains it `[measured — I ran it]`
`python3 tools/qa-divergence.py --check` → **exit 1**:
- **247 commits** on `origin/staging` that Mom's instance does not have;
- **17 SURFACE commits** — what she would see change — of which **11 are 🔴, named by no plan
  stage-note**, against Paul's 2026-09-04 ruling *"additions must be trackable"*;
- **`migration fast-forward: 🔴 BLOCKED`** — 1 commit on `main` not on `staging`: `294c0b4`
  *weather-history: rollup update*, 16:03 today.

⚠️ **This is not stale bookkeeping; it is a working instrument reporting real drift.** Two structural
consequences: (a) the *"one line per QA addition"* discipline has 11 gaps, so the divergence record is
incomplete **by its own definition**; (b) the fast-forward will be blocked again within ~6 hours of any
clearing, because `record-weather.yml:6` is `cron: "0 */6 * * *"` and commits straight to `origin/main`.
**A fast-forward procedure and an automated writer on the target branch cannot both be unmanaged** — the
back-merge has to be part of the bot's job or part of the migration script. That is a mechanism gap, and
which fix to take is engineering's call, not mine.

### 11 · A finding that is still true in the world and has no destination `[measured]`
Door row 48 (from `health-record`, 2026-09-02) reported *"all 23 zones in zones.json carry the IDENTICAL
color [122, 149, 104] — zero distinct values,"* against Paul's *"I've drawn them in full color before."*
Re-measured tonight: **1 distinct colour, 23 zones.** Still true. Its sibling row 49 correctly withdrew
the *geometry* half (commit `44dd853` had already surveyed it, better) — but `BACKLOG.md`'s Z2 section
contains **no mention of colour**. **The half that was answered got a destination; the half that stands
did not.** This is the partial-withdrawal failure mode: a well-behaved amendment can retire a whole row.

---

## Q2 · TRACK B — ACTED ON vs RECORDED AS ACTED ON

`cycle/requests.jsonl`: 52 lines, **15 data rows** (37 comment/header lines). Verified by parsing, then
each row's destination verified by name in `BACKLOG.md`, `vehicles.json` or `guides/`, and each absence
verified a **second** way with `git grep` across every tracked file.

| # | row (line) | door's view | destination in the record | real state |
|---|---|---|---|---|
| 1 | 37 GTI 2026-07-21 repairs | `resolved` | verified at lap 1 beat 3 → `sr-2026-07-21-cone-strike-repair-a` | ✅ **closed** |
| 2 | 41 GTI spark plugs | `routed` — *"NOT RESOLVED"* | `BACKLOG.md:1322` **P7 RESOLVED** | ✅ **closed** (door is stale) |
| 3 | 49 zone-map amendment | invisible (no `status`) | self-withdrawn in favour of `44dd853` | ✅ **closed by withdrawal** |
| 4 | 38 handwritten Bronco parts list | `routed` | `BACKLOG.md:1180` **P4 · still unread** | 🟠 **live, correctly parked** (a model read of a handwritten doc is refused by rule) |
| 5 | 40 water heater ≠ photograph | `routed` | `BACKLOG.md:1210` **P6** | 🟠 **live** |
| 6 | 42 second Bronco window switch | `routed` | `BACKLOG.md:1249` **P8** | 🟠 **live** |
| 7 | 43 mower 5/8" rounded bolt | `routed` | `BACKLOG.md:1272` **P9** → `BACKLOG.md:1344` **ROUTED OUT** to photo-organizer for a date | 🟠 **live, in another loop** |
| 8 | 44 nobody owns `viewer.html` | counted open | `BACKLOG.md:1649` **W1** — *"Paul routed it to BOTH surfaces"* | 🟠 **live, dual-filed on purpose** |
| 9 | 48 zone colour + provenance | counted open | geometry half → `44dd853`; **colour half: nowhere** | 🟠 **half live, half undestinationed** |
| 10 | 45 vehicle/equipment events, lap 26 | counted open | ⛔ **none** — `git grep 'window-2026-08-28'` finds it only in `cycle/mom/requests.jsonl` | 🔴 **never actioned** |
| 11 | 46 Bolores six-month narrative | counted open | ⛔ **none** — `git grep 'bolores-restoration-narrative'` = **0** tracked files outside the door | 🔴 **never actioned** |
| 12 | 47 follow-up: transcript pointer + 2 corrections | counted open | ⛔ **none** (same grep) | 🔴 **never actioned** |
| 13 | 50 VW invoice + a VIN that does not match | counted open | ⛔ **none** — `git grep '83848F2F'` = **0** outside the door | 🔴 **never actioned** |
| 14 | 51 driver-side J-B Weld washer failed | counted open | ⛔ **none** — `git grep 'J-B WELD'` = **0** outside the door; `guides/bolores-door-panel-repair.md:242` still describes only the cyanoacrylate stopgap, which is the prediction this row **refutes** | 🔴 **never actioned** (the row says so itself: *"Nothing in this row has been written to vehicles.json or the guide"*) |
| 15 | 52 fleet lap 3 + parts-run residue | `open` **on purpose** | `hold` field names the work and its release condition | ⏸ **held, correctly** |

### The real count, with its predicate

| | count | predicate |
|---|---|---|
| **Closed** | **3** | verified at a named destination or self-withdrawn |
| **Live, with a destination** | **5** (+1 half) | P4 · P6 · P8 · P9 · W1 · half of row 48 |
| **Never actioned, no destination anywhere** | **5** | rows 45 · 46 · 47 · 50 · 51 — absence verified by `git grep` across all tracked files |
| **Held on purpose** | **1** | row 52 |
| **The door reports** | **9** | `status == "open"` or absent (`fleet_probe.py:112`) |

⭐ **The door's 9 is not wrong; it is answering a different question.** It counts *rows nobody has
dispositioned at the door*. It cannot see that 4 of its 6 "handled" rows are live elsewhere, and it
cannot see that 5 of its 9 "unread" rows have no destination while 4 do. **Neither number is the one a
person needs**, and the gap is structural, not clerical: **the door has no state for *routed and still
open*,** so `routed` silently means both *dealt with* and *dealt with somewhere else.*

⚠️ **Minimum honest fix, and it is not mine to choose:** either the door's `routed` rows carry a
`routed_to` that a tool can follow, or the door stops copying dispositions it will not maintain. Both
are one-line schema calls. **What I will assert:** a row whose only live copy is a prose disposition in
an append-only log is unreachable by any check, and 4 rows are in that state today.

### The asymmetry between the two doors `[measured]`
| | Track B `cycle/requests.jsonl` | Track A `cycle/mom/requests.jsonl` |
|---|---|---|
| rows | 15 (9 undisposed) | **3, all opened 2026-09-01, none carrying any `status` field at all** |
| a **detector** | ✅ `fleet_probe.py` signal `s2_inbox` | ⛔ **none** — `git grep` finds the path named in exactly one file, `MOM-CYCLE-MAP.md:832`; no tool reads it |
| a **drain** | ⛔ none — *"Nothing sweeps that door on a cadence"* (`BACKLOG.md:5`) | ✅ the lap-opening GATE SWEEP (`MOM-CYCLE-MAP.md:846`) |

**Each door has exactly the half the other lacks.** Track A's three asks are structurally undrainable
while the loop is HELD — which is *correct by design*, and invisible to every board, which is not.

---

## Q3 · IS THERE A COHERENT PATH TO "MOM ON THE NEW PRODUCTION INSTANCE"?

**Yes — and it is blocked by a ruling, not by a build.** `[inferred, from the four artifacts below]`

### The four artifacts point the same way
- `OBJECTIVES.md` **O3** — *"Fernwood is instance 1 of a product; the engine transfers to a second estate
  without a fork"* — is the freeze's declared active objective.
- `.plans/2026-09-05-production-promotion-PLAN.md` is `stage: executed`: production promoted and verified
  @ `bce212a`, S1–S6 passed each *"against the world rather than a tool's success line."*
- `.plans/2026-09-06-one-environment-DECISIONS.md` carries tonight's architecture ruling and its
  falsifier (T1–T4 with four mutations).
- `9cb468d` (18:09 tonight) makes `home` a household rather than an environment.

### Where they diverge — three named gaps, all structural

**(a) The freeze declares O1 resting; tonight's goal is O1 work.** `BACKLOG.md:77` — *"O1 · O2 · O4
rest."* O1 is *"Mom uses Fernwood as her field journal, on her own initiative."* Onboarding her onto
production is O1 by that text. **Nothing is wrong with doing it; the register cannot describe the state
until Paul says whether O1 is lifted or whether "the migration" now contains it.** `[measured against
OBJECTIVES.md + BACKLOG.md:77]`

**(b) The release cascade's gate 2 has not run.** The promotion plan's own stage-note: *"⛔ NOT DONE:
synthetics have not given experiential feedback on production; **Paul has not walked it**; Mom has not
been invited. Stopped mid-gate deliberately."* Under the ratified cascade — synthetic persona → Paul →
Mom — **Mom is gate 3.** Moving her tonight crosses gate 3 with gate 2 unrun. ⛔ **That is a sequencing
statement, not a recommendation:** whether to skip his own walk is entirely Paul's, and he may have
already done it in a session I cannot see. `[measured from the plan; the "not done" claim is the plan's
own and may be stale — it is 20 hours old]`

**(c) Two rulings imply different sunset checklists (the blocking one).** Detailed as C2 in the register.
*Pour her input into the new instance* (09-04, still standing in `BACKLOG.md:99`) needs an import path
that **does not exist**. *She rebuilds from scratch; the frozen version is a data control; none of her
input should get lost* (09-05, `tools/archive-frozen-estate.py:8-11`) needs only that the archive be
current — **and it is.** These are not compatible checklists, and the newer ruling is the one that is
harder to find. **Paul's to confirm as a supersession.**

### Structurally unreachable — work nothing triggers, doors nothing drains, gates with no owner

| # | what | evidence | grade |
|---|---|---|---|
| U1 | **The whole freeze** — no tool reads it | `git grep 'FOCUS FREEZE' -- '*.py'` = 0; 33 session-start commands are freeze-blind | measured |
| U2 | **19 of 24 `check-*.py` have no automated caller.** CI runs 5 (`build-viewer`, `check-data-inline`, `check-public-build`, `check-qa-fixtures`, `check-live`, `check-digest-fresh`); `pre-push` runs 2 | enumerated `.github/workflows/*` + `.git/hooks/pre-push` | measured |
| U3 | **`archive-frozen-estate.py --verify` has no caller and no cadence** — the sunset's key control depends on someone remembering | `git grep` = 1 plan + 1 sibling docstring | measured |
| U4 | **`cycle/mom/requests.jsonl` has no detector**; its 3 asks are invisible to every board | Q2 table | measured |
| U5 | **`routed` rows at Track B's door** — no tool follows them, and the probe calls them handled | Q2, `fleet_probe.py:112,125` | measured |
| U6 | **The `.plans/` stage enum** — 5 files now need a word that does not exist; unruled since 09-04 | `check-backlog-ready.py` enum vs 5 headers | measured |
| U7 | **`fleet_probe.py` does not read `nextLook`** — lap 1's amendment 2 was applied to the data and is *"documentation, not a control"* (its own words) | `cycle-state.json` `_note` | measured |
| U8 | **`tools/deploy-worker.sh` takes no `--env`** and gates nothing the conversion touches | `.plans/2026-09-06-one-environment-DECISIONS.md` §F1 | inferred (peer's measurement, not re-run) |

⚠️ **U2 is a count, not a grade.** A check with no CI caller is not thereby useless — `CLAUDE.md`'s
session-start block is a real cadence, and this repo's own doctrine says *a capability the loop cannot
reach by running its own procedure is not a capability.* The block **is** that procedure. The finding is
narrower: **only 7 checks can refuse an act. Everything else depends on a session reading a list of 33
commands, and none of the 33 knows about the freeze.**

---

## Q4 · WHAT THE SUNSET ACTUALLY REQUIRES — enumerated, method only

Ten conditions. ⛔ **Not one of them is an opinion about whether to do it.** ✅ = satisfied tonight,
🟠 = partly, 🔴 = not.

| # | must be true | state | evidence |
|---|---|---|---|
| **S1** | **The blank-slate / pour-in contradiction is ruled.** Every item below branches on it | 🔴 | register §5·C2 |
| **S2** | **Which shape the data control takes — artifact or live site** (register §5·C3). Shape B is new work; shape A is done | 🔴 | her origin is public GitHub Pages with **no access control to revoke** |
| **S3** | **A complete archive of her estate exists and is verified** | ✅ | `.private/frozen-fernwood-archive/frozen-2026-09-06T000836.json` — **175/175 keys, `unreadable: []`**, 6.0 MB, mode 600 |
| **S4** | **…and it is CURRENT at the moment of sunset** | 🟠 | taken 00:08:36 today; her Worker still accepts writes on 4 channels; **nothing schedules a re-take or `--verify`** |
| **S5** | **The archive's completeness bound is understood** | 🟠 | it enumerates via `wrangler kv key list`, which **this repo has measured to be eventually consistent and unable to prove presence or absence** (`household-export.py:9-13`). ⚠️ **171 of her 175 keys are LEGACY unprefixed** — `household-export.py`'s prefix-derived enumeration would miss them; only `archive-frozen-estate.py` can see them |
| **S6** | **A restore path exists, or its absence is accepted** | 🔴 | there is no restore tool. `git grep` finds export + reset only. *"restore-proven 13/13"* (`13dfb7d`) is the **private sibling repo's** encrypted backup, **not KV** |
| **S7** | **Every credential on her estate is enumerated and revoked** | 🔴 | a 2026-09-05 18:05 dump of `est-3c9f1a` (`.private/kv-exports/lab-est-3c9f1a-preswitch.json`, key names only) shows **11 `account:` keys and 13 `grant:` keys**, most from synthetic walks (`marguerite*`, `riverbend*`, `syn-*`, `walker5_*`). `reset-production-estate.py:44` — *"a leftover grant is a live credential."* ⚠️ **Snapshot, not a live read** — I did not query KV. Live verification is engineering's |
| **S8** | **Her browser-local state is rostered and each key dispositioned** | 🟠 | the roster exists — `check-storage-keys.py`, 18 keys, C4 2b, *"a key the origin-move migration does not know about is a key she loses."* A **per-key** migrate/abandon/re-collect decision is not on disk `[inferred]` |
| **S9** | **The automated writers to her instance have a destination** | 🔴 | `record-weather.yml` commits to `origin/main` every 6h (**11 commits since the last human one**) and `fernwood-deployer[bot]` adds digests. If Pages is unpublished, an Action keeps writing to a dead surface; if it is repointed, the control stops matching what she saw |
| **S10** | **The one-way door is understood.** After she onboards, `reset-production-estate.py` **must never run** — one `real` record aborts it by design | ✅ documented | its own header + the promotion plan S6. So the only recovery from a botched migration is the archive, i.e. **S3–S6 are the whole safety net** |

### The two orderings this implies `[inferred]`
1. **S1 before everything.** *Pour in* makes S6 (a restore/import path) blocking; *archive* makes S4 (a
   refresh at the moment) blocking. You cannot write the checklist before the ruling.
2. **S4 last, and adjacent to the act.** Any archive taken before her final write is incomplete by
   construction. The natural shape is: `--verify` → 0 gone → re-archive → then revoke.

### Which of these are method-actionable, and which are not
**Method-actionable:** S4 (give `--verify` a caller and a place in the sunset procedure), S8 (write the
per-key disposition beside the roster), S9 (decide the bot's destination as part of the procedure), S10
(already written down — leave it alone).
**Not method-actionable, and I am not going to pretend otherwise:** S1, S2, S6, S7. S1 and S2 are
Paul's rulings. S6 and S7 are engineering builds whose *necessity* depends on S1/S2.

---

## Q5 · THE HUMAN / AI / DETERMINISTIC HANDOFF, AND WHERE IT BREAKS UNDER THE FREEZE

### What the handoff structure actually is `[measured]`
| layer | what it owns here | how it is evidenced |
|---|---|---|
| **Deterministic** | every gate that can refuse: CI (5 checks), `pre-push` (2), `pages-deploy.py`'s refusal on a household needle, `reset-production-estate.py`'s abort on one `real` record | exit codes, plus **selftests / mutation proofs** on the newer tools |
| **AI (agent)** | building, measuring, drafting, writing the chronicles; may commit freely | *"an agent may commit a hundred times in a lap and may not send one email"* |
| **Human (Paul)** | every ruling, every irreversible act: the push to `main`, the outbound message, the migration itself | classifier blocks an agent push to `main`; S7 of the promotion plan ends *"⛔ Do not send"* |

**This is maker-checker with risk-tiered approval, and it is well built.** The gate sits on
irreversibility, not on importance — which is why 247 unpushed QA commits are unremarkable and one link
to Mom is gated.

### Four places it breaks under the freeze

**B1 · The freeze is a human rule with no deterministic layer at all.** U1. Every instrument is
freeze-blind, so the freeze is enforced entirely by *each session reading a prose block* — and the block
is 26 hours behind on one line (Q1·1). ⭐ **This is the repo's own most-ratified failure shape: a written
rule is not a mechanism.** The register's §4(c) is the smallest available fix — one axis of three
becomes machine-checked, sited on the pre-push hook where it can actually refuse.

**B2 · The one tool the ruling sanctions violates the ruling.** `read-mom-feedback.py:556,578-580` prints
her words; `BACKLOG.md:88-90` says its output *"is a COUNT… and nothing more."* **The handoff boundary is
stated correctly and implemented wrongly**, which is the worst of the three possibilities (stated wrong
would at least be honest). Register §3. Paul's to resolve: change the tool or change the ruling.

**B3 · Held work has no state anywhere a machine can see it.** `HELD` exists in prose in three files and
in **zero** state artifacts: `data/cycle-state.json` says `ARMED`, `cycle/fleet/cycle-state.json` says
`FIRED`, `cycle/requests.jsonl:52` keeps `status: "open"` *deliberately* — its own note explains why:
*"fleet_probe.py counts a row only when status is literally 'open', so any other string would hide it."*
⭐ **That is a correct workaround and a diagnosis at the same time:** a person had to choose between an
honest state word and remaining visible, and chose visibility. **The vocabulary is missing a word the
tools can read, and the register does not fix that — `freeze.json` would carry it.**

**B4 · The AI layer's output is the layer with the least deterministic coverage.** `.plans/` holds 58
files; the drift found tonight is in 3 of them (Q1·2, Q1·8) plus 2 chronicles. Nothing checks a plan's
status string against the world; `check-backlog-ready.py` checks that a *claim of readiness* has a trail,
which is a different assertion. **The counterfactual gap has no owner here either** — but that is a
portfolio finding, not a Fernwood one, and it is already open in my foundation.

---

## FALSIFIERS FOR THIS AUDIT

| claim | what would show it wrong |
|---|---|
| The record errs toward safe-looking | a drifted artifact that under-reports open work or over-reports permission |
| 5 door rows were never actioned | any tracked file, or a `.private/` file, holding their payload — `git grep` was run on tracked files only |
| The archive is complete | `archive-frozen-estate.py --verify` reporting any `GONE` key, which would mean the 00:08 archive is not a superset of her estate |
| S7's 13 grants | a live `wrangler kv key list` on namespace `100f2b95…` showing fewer — my number is from a **2026-09-05 18:05 snapshot** |
| Gate 2 has not run | Paul saying he walked production, in which case the promotion plan's stage-note is what is stale |
| The three axes are enough | register §6 |

## WHAT I DID NOT DO, SO NOBODY INFERS COVERAGE
- **Did not read Mom's feedback, or fetch any channel.** Every statement about her queue is from source
  code, state files and key names.
- **Did not run the arrival census** — the peer seat owns that inventory.
- **Did not verify KV live.** S7's grant count and the archive's currency are both snapshot-based.
- **Did not audit deploy topology, the Worker conversion, or the onboarding journey** — engineering's.
- **Did not rank anything.** No row, vehicle, note or feature was called more important than another.
