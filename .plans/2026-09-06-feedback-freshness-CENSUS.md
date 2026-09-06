# FEEDBACK & INPUT CENSUS — item by item, claim vs. world

**Built 2026-09-06.** Read-only pass: nothing tracked was edited, nothing was committed, nothing
was pushed. This file is the only thing written.

**THE ANCHOR.** The freeze begins at **`475872f` · 2026-09-03 14:11:59 -0400** ("FOCUS FREEZE:
instance work rests, the migration is the only active Fernwood work"). *Measured* —
`git log -1 --format='%H %ci %s' 475872f`. Every row below is positioned against it.

**GRADING.** Every verdict carries its grade. **measured** = a named command or file read on
2026-09-06. **inferred** = derived from two measured facts. **assumption** = neither. A status
string is never evidence for itself; where a row's own label is the only support, the verdict says
so.

**⛔ TRACK A BOUNDARY HONOURED.** No feedback body was opened, no `--address` was run, no
disposition was proposed or drafted. Track A appears here as *arrival metadata only* — counts,
timestamps, channels, record ids, and whether a disposition exists. Item-level tracking of Track A
**was achievable without reading content**: the repo's two disposition ledgers are explicitly
built to hold "where it went, never her words," and `check-arrival-dispositions.py` renders only
channel · id · timestamp · origin. See § 2 for the one place this ran into a wall.

---

## 1 · TRACK B — Paul's fleet & equipment door

**The door:** `cycle/requests.jsonl`. **15 data rows** (52 lines, 37 of them the `#` header block).
*measured* — `python3` json parse skipping `#` lines.

**Status field distribution** *measured*: `<MISSING>` ×8 · `routed` ×5 · `resolved` ×1 · `open` ×1.

**What the probe sees:** `tools/fleet_probe.py` line 112 —
`open_rows = [r for r in rows if (r.get("status") or "open") == "open"]`. A missing status defaults
to open; **`routed` and `resolved` both vanish.** Live run 2026-09-06: `⚡ INBOX 9 unread fleet
correction(s) filed`. **9 = the 8 missing-status rows + the 1 explicit `open`.** *measured* —
`python3 tools/fleet_probe.py`. The finding handed to me is **confirmed exactly.**

| # | id / source | arrived | vs. freeze | claimed status | **verified status** | evidence for the verification | what remains |
|---|---|---|---|---|---|---|---|
| **TB-01** | photo-organizer — GTI 2026-07-21, ten repair photos | 2026-08-28 (`a54a07c`/`4eaed4a`) | **before** | `resolved`, closed 2026-09-01 | ✅ **TRUE.** Row was never a gap | `grep -c 'sr-2026-07-21-cone-strike-repair-a' vehicles.json` → 1. *measured* | Its own stated optional residue — link the 10 photos as `photoEvidence` — **not done**: `photoEvidence` occurs 2× in `vehicles.json`, both on `homelite-blower-vac`, none on the cone-strike row. *measured* |
| **TB-02** | photo-organizer — handwritten Bronco parts list, 2 photos, 2026-07-20 | 2026-08-28 | **before** | `routed` → BACKLOG Track B; disposition "**ROUTED, NOT RESOLVED**" | ✅ **TRUE — fully open.** Nobody has read the document | BACKLOG.md:1180 `### 📄 P4 · The handwritten Bronco parts list — routed here from the door, still unread`. No transcription anywhere in the repo. *measured* | The whole item. Needs the eyeball/verify path **with Paul in it** — deliberately not an agent's job |
| **TB-03** | chatgpt-archive-mine — water heater: record vs. 2025 photo | 2026-09-01 (`2bd85d2`) | **before** | `routed` → BACKLOG § P6; "**ROUTED, NOT RESOLVED**" | ✅ **TRUE — fully open.** Nothing moved | `water-heater-bradford-white.specs.installedHere` still reads *"Not yet on record — no invoice in email…"*; `serviceHistory` = **0** rows; `openMechanicalItems` = 0. *measured* | One sentence from Paul: replaced, or a different building? Also open as **H4** in the household block (BACKLOG:1961) — the same fact tracked twice, on two surfaces, neither pointing at the other |
| **TB-04** | chatgpt-archive-mine — GTI spark plugs, -8 vs -9 | 2026-09-01 | **before** | `routed`; "**ROUTED, NOT RESOLVED** … all three claims stand … the real resolution is physical" | 🔴 **FALSE — this was RESOLVED the same day.** See Disagreement #1 | `vehicles.json` `maintenance.sparkPlugs.confidence` = **`verified`** (was `inferred`); source line carries **two order numbers** — NGK196860 (2025-03-25, R7437-**8**) and NGK140052 (2022-10-03, R7437-**9**). BACKLOG.md:1322 `### ✅ P7 RESOLVED — the spark plugs were never a contradiction. They were a SEQUENCE.` CYCLE-LOG.md:587 same. *measured* | Only **which set is physically in the engine** — a plug pull, self-described "low stakes now, not zero." Two of the row's three claims were closed by order record |
| **TB-05** | chatgpt-archive-mine — Bronco second rear-window switch | 2026-09-01 | **before** | `routed` → § P8; "**ROUTED, NOT RESOLVED**" | ✅ **TRUE — fully open** | `.private/service-records/AMAZON-PARTS.md` § Bronco (15 items): **zero** matches for `switch` anywhere in the file; October-2025 rows present, no switch row of any date. *measured* | Paul's answer: same part twice, or a second burnt switch on a shelf / in the truck |
| **TB-06** | chatgpt-archive-mine — mower 5/8" bolt rounded off, Apr 2025 | 2026-09-01 | **before** | `routed` → § P9; "**ROUTED, NOT RESOLVED**" | 🟡 **TRUE but the row understates progress.** The documentary half came back; the physical half is open | Still true: `husqvarna-mower` and `kobalt-km2040x-06` both **0** serviceHistory / **0** openMechanicalItems; `TOOLS.md` **0** matches for `extract` across 220 lines. *measured*. **AND** photo-organizer answered the routed-out request — BACKLOG.md:2063 gives the date **2025-04-10**, the machine (Husqvarna Z254F, *Paul's word not the photo's*), and the shop (Herman's). *measured* | The live question: **is that bolt still rounded?** A look at both mowers' blade and deck bolts. Nothing has looked |
| **TB-07** | session-process-audit — nobody owns `viewer.html` | 2026-09-01 (`98f8812`) | **before** | *(no status field — counts as open)* | 🟡 **HALF RESOLVED.** The seeded half is fixed; the row's own headline is not | **Fixed:** `~/.claude/tools/health-probe.py` `DERIVED_VIEWS` now lists `("tate-tracker", …, "check-data-inline.py")` — committed `26488bb`, **2026-09-03 21:50:29**, i.e. *during* the freeze, in a different repo. **Not fixed:** BACKLOG.md:1669 still reads *"Missing is exactly one thing: an owner for `viewer.html`."* *measured* | The owner. The prover now has a caller; the write-duty/ship-duty split across Track A and Track B is unchanged |
| **TB-08** | photo-organizer lap 26 — 6 vehicle/equipment events, 115-card window | 2026-09-01 (`7efd141` era) | **before** | *(no status — open)* | ✅ **TRUE — nothing folded**, exactly as the row says of itself | `grep -c 'observed:' vehicles.json` → **0**. The F-150 naming convention (*"I generally call the truck the F-150"*) appears in **no** `.md` or `.json` in the repo. `g22a-2005` serviceHistory = 0. *measured* | All six proposals, incl. the standing naming convention that would disambiguate every future dictation against `bronco-1989` |
| **TB-09** | photo-organizer lap 27 — Bolores, 6 months, 550 cards / 316 rulings | 2026-09-01 (`7efd141`) | **before** | *(no status — open)* | ✅ **TRUE — nothing folded** | `bolores-restoration-narrative` is referenced **nowhere** in this repo. `bronco-1989` newest serviceHistory row is **2026-08-28**; its 8 `openMechanicalItems` are all pre-existing (5 closed at beat 6, exhaust + transmission closed, emissions standing). *measured* | The whole narrative: the tailgate repair arc, the actuator that a part did **not** fix, the three open items in his own words, the two label photographs |
| **TB-10** | photo-articles follow-up — transcript pointer + 2 corrections | 2026-09-01 (`b99a55b`) | **before** | *(no status — open)* | ✅ **TRUE — nothing folded** | The three verbatim open items (driver door lock actuator #87; actuator voltage #46; **broken dash screw holes** #199) appear in **none** of `bronco-1989`'s 8 open items. *measured* | Same as TB-09. #199 is stated in the future tense and is real work |
| **TB-11** | health-record — zone colour + a `zone-capture.py` TypeError | 2026-09-02, filed `b23eda1` **13:25:14** | **before** (by 46 min) | *(no status — open)* | ✅ **BOTH DATA TRUE, BOTH OPEN** | Colour: all **23** zones in `zones.json` carry `[122,149,104]`, zero distinct values. Bug: `tools/zone-capture.py` `log_message` still reads `if "/api/save" not in (args[0] if args else "")` with no `str()` coercion; last commit to the file **`badf097` 2026-08-31**, before the row was filed. *measured* | The one-line fix, and the design question: should per-zone colour be in the record? |
| **TB-12** | health-record — amendment / partial withdrawal of TB-11 | 2026-09-02, filed `f0f64ec` **13:25:14** | **before** | *(no status — open)* | 🟡 **SELF-WITHDRAWING.** Its framing is retracted by its own text; the two data it keeps are TB-11's | Same measurements as TB-11 | Nothing of its own. It is a duplicate the door still counts as an unread item |
| **TB-13** | photo-organizer — VW invoice, VIN mismatch vs. recorded Tiguan | 2026-09-03, filed `89f43c5` **16:40:36** | 🔒 **DURING** | *(no status — open)* | ✅ **TRUE — untouched** | `tiguan-2018` has **2** serviceHistory rows (2026-01-16, 2026-01-07) — **no 2022-06-02**. `vin` still `3VV1B7AX1JM••••••`. *measured* | A human eye on one photograph: misread VIN, different Tiguan, or a wrong recorded VIN |
| **TB-14** | session 2026-09-04 — driver-side washer, the PREP-not-chemistry correction | 2026-09-04, filed `b028dc2` **17:48:39** | 🔒 **DURING** | *(no status — open)*; row says of itself "nothing … written to the guide" | ✅ **TRUE — not folded** | `guides/bolores-door-panel-repair.md` last commit **`b6f5586` 2026-08-29**, before the row existed. STEP 7 line 286 still carries the superseded framing *"CA is brittle and fails better under impulse than steady force."* *measured* | The corrected rule; the residual-epoxy flatness check (nobody has inspected whether the epoxy came away); and **Paul's unmade ruling** on the DPPRK87 bracket adhesive |
| **TB-15** | session 2026-09-05 — fleet lap 3 + parts run residue | 2026-09-05, filed `0c908de` **13:56:43** | 🔒 **DURING** | `open` + `hold` = "HELD until the prod freeze lifts" | ✅ **THE LABEL IS HONEST, AND IT SAYS SO ITSELF.** Held = the **push**, not the work | All four named commits exist and **none is in `origin/main`**: `18a69fe`, `08f43a6`, `d43679a`, `3a5459a` → `git merge-base --is-ancestor … origin/main` fails for each; `475872f` passes. Local `main` is **256 commits ahead**. `TOOLS.md:144` carries the new `THE 2026-09-05 HOME DEPOT RUN` section, so the in-repo writes did land. *measured* | Release condition **not met** (freeze holds). Residue: 4 questions only Paul closes, T3 at ~5000 rpm (nextLook 09-12), the Batteries Plus lookup, 7 prep buys, the STEP 0 acetone gate, 2 probe amendments |

### 1b · Track B items that never reached the door at all

*measured* — read directly from the surfaces named.

| # | item | where it lives | vs. freeze | verified status |
|---|---|---|---|---|
| **TBX-01..04** | **H1–H4** household gaps — furnace data plate · air-filter size · panel rows 28 & 30 flip-test · water-heater install invoice | BACKLOG.md:1961, landed `ed298c4` **2026-08-31** | before | **All four open.** Each is "a two-minute physical act at the property." **H4 is TB-03 under another name** and neither row references the other |
| **TBX-05..31** | **27 `P-nn` capability rows** (`P-01`…`P-26`) — the reminder engine, asset lifecycle, aliases/"motor pool", the project arc as a record type, machine lore, *where the things that live only in his head go*, a one-at-a-time answer queue … | BACKLOG.md:3110 § O4 · Track B, landed `17ec631` **2026-09-04 06:23** | 🔒 **during** | **All open, none at any door.** These are Paul's own asks mined from the conversation corpus, tagged `validated` with recurrence counts. `P-12` names the hole explicitly: *"`cycle/requests.jsonl` is an inbound door for* other projects*. Neither is a free capture surface for him."* ⚠️ The commit that carried them **does not describe them** — a concurrent session's broad stage absorbed them; left unrewritten `[paul-ruled 2026-09-04]` |
| **TBX-32** | **Two `fleet_probe.py` s4 defects** — "FILED, NOT FIXED" | BACKLOG.md:1353 | before | 🔴 **STALE — both were FIXED.** See Disagreement #3 |
| — | `.private/service-records/` | AMAZON-PARTS.md · EMAIL-RECEIPTS.md · TOOLS.md · vehicle-history-candidates.md · 5 per-vehicle dirs | — | Swept: no item found here that is open and absent from BACKLOG or the door. `TOOLS.md`'s own coverage warning stands — **absence there means not-yet-swept, never not-owned** |

---

## 2 · TRACK A — Mom's channel (ARRIVAL METADATA ONLY)

⛔ **No content read.** Everything in this section comes from (a) the two disposition ledgers, whose
own `_meta` states they hold *"never her words … only where the record went"*, and (b)
`check-arrival-dispositions.py`, which renders channel · id · timestamp · origin and nothing else.
The authorized detector `read-mom-feedback.py --pickup` was run. **`--address` was not run.**

**Item-level tracking WAS possible without opening content.** No wall was hit. One caveat is
recorded below rather than escalated, because it is an instrument fact, not a content one.

### 2a · The arrival census

*measured* — `python3 tools/check-arrival-dispositions.py` (default 60-day window) plus a per-channel
recount through `momlib.undispositioned_arrivals`'s own definitions.

| channel | arrivals | individually dispositioned | baselined (batch-cleared) | **undispositioned** | arrived before freeze | during |
|---|---|---|---|---|---|---|
| `feedback` (Mama's Perspective) | 10 | 5 | 5 | **0** | 10 | 0 |
| `observations` | 53 | 8 | 45 | **0** | 53 | 0 |
| `zone-audio` | 6 | 1 | 5 | **0** | 6 | 0 |
| `guru` | 12 | 3 | 8 | **1** | 11 | 1 |
| **total** | **81** | **17** | **63** | **1** | **80** | **1** |

**The one undispositioned item:** `guru` · **`mtooovq3-echf1`** · **2026-09-05 1:58 PM ET** ·
`deviceId d-szqlt0h7…` (not a bench device) · `owed_to_mom: true`. It arrived **during the freeze**
and is **correctly untouched** — the ruling is that it not be ingested or actioned. It is a real
undispositioned arrival, not a defect.

**Every one of the 17 dispositions predates the freeze.** Latest `dispositionedOn` =
**2026-09-02T03:21:48Z** (= 2026-09-01 11:21 PM ET). *measured*. And **zero commits after
`475872f` touched `arrival-dispositions.json` or `feedback-log.json`** —
`git log 475872f..HEAD -- arrival-dispositions.json feedback-log.json` returns nothing. **The freeze
is being obeyed, verifiably, on the Track A side.**

### 2b · The `feedback` channel item by item (metadata only)

| noteId | noteTs | addressedOn | vs. freeze | acknowledgedToHer |
|---|---|---|---|---|
| `fb-an5q0hiu-mro92d67` | 2026-07-17 | 2026-07-26 | before | false — *bench, Paul's own device* |
| `fb-4goj8swu-mro93jhe` | 2026-07-17 | 2026-07-26 | before | false — *bench* |
| `fb-v0xl2jv6-ms1ts7ml` | 2026-07-26 | 2026-07-26 | before | **true** |
| `fb-946dp0qk-ms639ds6` | 2026-07-29 | 2026-07-29 | before | **true** |
| `fb-0wk7w59c-mt1k6tll` | 2026-08-20 | 2026-08-24 | before | **true** |

Her last card answer is **2026-08-20**, addressed 2026-08-24 — 10 days before the freeze. *measured*
— `read-mom-feedback.py --pickup` prints `her last card answer 2026-08-20 (17d ago)`.

### 2c · Two instrument facts about this census, recorded so the number is not over-trusted

1. **63 of 81 arrivals were never individually attested.** They sit behind the declared baseline
   (**2026-08-28T00:00:00Z**) and are covered by the batch channel watermark. The tool is scrupulous
   about this — it prints *"Not dispositioned; baselined"* — but a reader who takes "1
   undispositioned" as the whole answer is wrong by 63. This is a **declared, dated** batch clear,
   not a leak; it is named here because the census asks *how many were actually looked at*, and the
   honest answer is **17**.
2. **⚠️ Widening the window silently breaks the `feedback` channel.** At `--days 90`,
   `/api/feedback` returns **HTTP 400** and the run degrades to *"could not read: feedback —
   reported, never counted as clean."* At 7 / 30 / 60 days it reads fine. *measured* — four ranges
   driven. **The tool behaves correctly** (it refuses to print a green line over a hole), but the
   default 60-day window is the only one that works, and nothing says so. Separately,
   `/api/observations` returns the same **53** records at `--days 7` as at `--days 60` — it
   **ignores the range**, so "in the last 60 days" is not true of that channel (it reaches back to
   2026-05-19). *measured*. Neither changes the counts above; both change how much a future reader
   should trust the window label.

---

## 3 · CROSS-PROJECT INBOUND

**Into Track B** (`cycle/requests.jsonl`, by `from`): photo-organizer **6** (TB-01, 02, 08, 09, 10,
13) · chatgpt-archive-mine **4** (TB-03…06) · health-record **2** (TB-11, 12) · in-repo sessions
**3** (TB-07, 14, 15). *measured*.

**Into Track A** — `cycle/mom/requests.jsonl`, and this is the worst structural finding in the
census:

| # | source | arrived | vs. freeze | claimed status | **verified status** |
|---|---|---|---|---|---|
| **MD-01** | photo-organizer lap 26 — nature + plant observations, 9 findings | 2026-09-01 | before | *(no status field)* | **OPEN, and invisible to every probe** |
| **MD-02** | photo-organizer — plants × zones table (`plant-zone-table.md`) | 2026-09-01 | before | *(no status field)* | **OPEN** — partially consumed: BACKLOG.md:3015 cites `plant-zone-table.md`, so some content reached a surface. No disposition exists |
| **MD-03** | photo-organizer — plant-identification handoff, **56 photographs**, zone-confirmed by Paul, plants unnamed | 2026-09-01 | before | *(no status field)* | **OPEN** — the explicit half photo-organizer cannot do, handed over and never picked up |

**These three rows are read by nothing.** *measured* — `grep -rln 'cycle/mom' tools/` returns **no
file**; `tools/mom-cycle-status.py` contains no `requests.jsonl` or inbox check. `MOM-CYCLE-MAP.md`
declares the door (§ *"Inbox — this loop CAN be asked `[opened 2026-09-01]`"*) and says an open ask
is disposed *"at the LAP-OPENING GATE SWEEP"* — a human/agent procedure, not a probe. **No mom-cycle
lap has run since lap 8 closed 2026-09-01**, so the gate sweep has not fired since the door opened.
*measured* — `MOM-CYCLE-LOG.md` headers.

⚠️ **These three are NOT under the Mom freeze.** They are photo-organizer's asks about plants and
nature, not Mom's feedback. Nothing prevents actioning them except that no surface counts them.

---

## 4 · THE DISAGREEMENTS — ordered by how badly the record misleads a reader

### 🔴 #1 — TB-04 says "ROUTED, NOT RESOLVED"; it was resolved the same day, by order record

The door row's disposition reads *"all three claims stand — the record says -8 …, Paul stated he
ordered -9, and nothing establishes what is installed"* and *"the real resolution is physical …
Batched into beat 4's trip."* **Hours later, beat 6 closed it.** Gmail held both order
confirmations: **NGK140052** (2022-10-03, R7437-**9**) and **NGK196860** (2025-03-25, R7437-**8**).
The "contradiction" was a **three-year sequence**. `vehicles.json` was promoted
`inferred → verified`; BACKLOG.md:1322 and CYCLE-LOG.md:587 both record the clearance.

**Why this is the worst one:** the door row is the *only* one of the three surfaces still claiming
open work, and it is the row a reader reaches by asking the question the loop was built for. It
over-reports open work, it re-opens a settled fact, and it points a physical trip at a documentary
question that a search already answered. *measured.*

**Second-order:** BACKLOG's own `### 🔌 P7` **header at line 1230 carries no resolution marker** —
the `✅ P7 RESOLVED` block sits **92 lines later**, past two other sections. A reader scanning
headers sees P7 open. Same defect, milder.

### 🔴 #2 — three inbound rows sit in a door that has no reader

`cycle/mom/requests.jsonl` (MD-01…03, all 2026-09-01, all with **no status field**) is declared in
`MOM-CYCLE-MAP.md` and read by **zero tools**. `fleet_probe.py` reads only `cycle/requests.jsonl`.
If a probe with the same logic existed, all three would count as open — but none exists, so the
deterministic answer to *"is anything waiting for the mom-cycle?"* is structurally **0**, and the
true answer is **3**, including a 56-photograph handoff Paul designed himself.

⚠️ And the two Track A artifacts disagree about whether this door should exist at all:
`MOM-CYCLE-LOG.md:2050` says *"this loop still has no inbox of its own … do not clear it by giving
the mom-cycle a door,"* while `MOM-CYCLE-MAP.md` opened one on 2026-09-01. *measured.* Which of
those is right is process territory and not mine to rule; the **inventory** fact is that three items
are parked in the gap between them.

### 🟠 #3 — BACKLOG says two probe defects are "FILED, NOT FIXED"; both are fixed

BACKLOG.md:1353 `### 🐛 TWO DEFECTS IN fleet_probe.py s4_stale_open — FILED, NOT FIXED`, closing
*"Both are beat-7 amendments and are **proposed, not applied**."* **Both were applied.**
`s4_stale_open` now reads `state (open|closed|deferred)` — its docstring names the fix and dates it
2026-09-01 — and it **prints its own denominator**: the live run emits
`[3 open (0 undated, not testable) · 7 closed · 0 deferred · 1 standing]`. `CYCLE-LOG.md:615`
records the application; a *third* defect (a deferral vanishing from the census on the day it fired)
was found and fixed on top. *measured.*

This one misleads in the **opposite** direction from the repo's usual failure mode — it
**under-reports** completed work, and it is the same commit window (`3ef3ee1`, 2026-09-01 11:05)
that wrote the heading. Cheaper to a reader than #1, but it makes a healthy instrument look broken.

### 🟠 #4 — TB-07's headline and its footnote have opposite truth values now

The row is titled *"NOBODY OWNS `viewer.html`"* and carries a "related, separately seeded"
sub-claim that `health-probe.py`'s `DERIVED_VIEWS` omits Tate-Tracker and its prover has no caller.
**The sub-claim is now false** — wired `26488bb`, 2026-09-03 21:50, with a comment naming the
measured cost of the gap. **The headline is still true** (BACKLOG.md:1669). A reader who checks the
verifiable half will conclude the row is stale and skip the half that isn't.

### 🟡 #5 — "routed" is a synonym for "invisible", and it is doing real damage

Five rows carry `status: "routed"` (TB-02…06). All five **are** genuinely present on BACKLOG.md as
P4, P6, P7, P8, P9 — *measured*, so the routing was real, not a euphemism. But the door reports 9
when **13** rows carry open work, and **4 of the 5 missing are still fully open**. TB-15's own
`hold` note documents this trap from the inside, having stepped in it: it was filed as
`deferred-by-paul`, *"and the INBOX count did not move."* It now keeps `status: "open"` deliberately
so it can be seen — a row lying about its own state to stay visible.

### 🟡 #6 — the same water-heater fact is tracked twice, on two surfaces, neither aware of the other

TB-03 / BACKLOG § P6 (record-vs-photo mismatch) and BACKLOG § H4 (find the install invoice) are the
same missing document. Closing either closes most of the other. Neither cross-references it.
*measured.*

### 🟡 #7 — TB-12 is a duplicate the door counts as unread work

It withdraws its own framing in its first line (*"READ 44dd853 FIRST, IT OUTRANKS MINE"*) and keeps
two data that TB-11 already carries. Its own closing lesson is the finding: *"an inbox that carries
duplicates costs the receiving loop the time it was meant to save."* It is 1 of the probe's 9.

### ⚪ #8 — the known case, re-confirmed as still wrong

`.plans/2026-08-31-zones-traced-with-mom.json` `_meta.status` still reads **"PROPOSAL — NOT FOLDED.
zones.json is unchanged."** It was folded **2026-08-31 18:41:13** by `51d6007` ("THE FOLD — Mom's map
is canon"), and `zones.json._meta` carries `fold_2026_08_31`. *measured.* Confirmed exactly as
handed to me. Listed last only because it is already known — as a *pattern* it is #1's parent.

---

## 5 · THE TWO COUNTS

### How many items are genuinely unactioned

**Track B door — 13 of 15 rows carry real open work.** *verified item by item above.*

- **10 are fully untouched** — nothing has happened since they were filed: TB-02, TB-03, TB-05,
  TB-08, TB-09, TB-10, TB-11, TB-12, TB-13, TB-14.
- **3 carry live residue** with partial progress: TB-06 (documentary half answered, the physical
  bolt unlooked-at), TB-07 (prover wired, owner still missing), TB-15 (work committed locally,
  push held, 4 questions + 2 dated actions outstanding).
- **2 are effectively closed:** TB-01 (accurate `resolved`, one optional residue) and **TB-04**
  (resolved by order record, its label wrong; residue is a low-stakes plug pull).

**Track A — 1 undispositioned arrival**, `guru mtooovq3-echf1`, 2026-09-05, and it is **correctly**
untouched under the freeze. Plus the honest caveat: **63 of 81 arrivals were batch-cleared by
watermark and never individually attested** — declared and dated, not lost, but not "looked at"
either.

**Track A cross-project door — 3 items**, MD-01…03, open and **counted by nothing**.

**Track B off-door surfaces — 32 items**: 4 household gaps (H1–H4) + 27 `P-nn` capability rows +
1 stale defect block. All open; none has ever passed through a door.

> ### Genuinely unactioned, by scope
> - **17** inbound items filed at a door: **13** (Track B) + **3** (Track A cross-project) + **1** (Track A arrival, frozen on purpose)
> - **+32** open Track B items that never reached a door
> - **= 49 open items total**, of which **16 are unactioned inbound that nothing is holding back**
>   (the 17th is the frozen Guru arrival)

### How many the tooling currently reports

- `tools/fleet_probe.py` → **`INBOX 9 unread`** *measured*
- `tools/check-arrival-dispositions.py` → **1 undispositioned** *measured*
- `cycle/mom/requests.jsonl` → **no probe exists** → **0**
- BACKLOG.md Track B / O4 / household → **no probe exists** → **0**

> ### **Tooling total: 10. Verified total: 49.**
>
> **The gap is 39 items no probe counts.**
>
> Even inside the one door that *is* instrumented, the probe reports **9** where **13** rows carry
> open work — **understated by 4**, every one of them a `status: "routed"` row — while
> simultaneously counting **1** row that is a self-withdrawn duplicate (TB-12) and **1** whose
> headline is half-fixed (TB-07). The count is not merely low; it is low **and** noisy, and the
> two errors do not cancel.

### The freeze split, stated plainly

| | before the freeze | during the freeze |
|---|---|---|
| **arrived** | 12 of 15 Track B rows · 80 of 81 Track A arrivals · all 3 MD rows · H1–H4 | 3 Track B rows (TB-13, 14, 15) · 1 Track A arrival · the 27 `P-nn` rows |
| **acted on** | all 17 Track A dispositions · TB-01 · TB-04's real resolution · both probe fixes · the P9 route-out | **`DERIVED_VIEWS` wiring only** (`26488bb`, and in `~/.claude`, not here) |

**Nothing in Fernwood was dispositioned after 2026-09-03 14:11:59.** *measured* —
`git log 475872f..HEAD` over the two ledgers returns empty, and the three post-freeze door commits
**add** rows without disposing any. The freeze is real and it is being kept. What the census shows
is that the backlog it froze was **already** larger than any instrument was reporting — by roughly
a factor of five.
