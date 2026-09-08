# LAP 3 — A PROPOSED PROCEDURE, written to be followed

- row: process — no BACKLOG row, same posture as the lap-boundary PROCESS and the flex-point AUDIT. **The orphan flag is expected and is not a defect to repair.**
- objective: O5
- class: engine · declared
- kind: process
- seats: practice-steward → .plans/2026-09-07-lap2-RETRO.md
         engineering-partner → owed, not waived: §4 beat 0 step 2 and the retro's C-2 both need a build. Stated here, designed nowhere here.
         ux-expert → waived: no surface is specified, changed or reviewed in this document.
         content-steward → waived: no word that reaches a person is written here.
         user-researcher → owed, not waived: §4 beat 2 step 15 and §5's journey rung are its work. Waived at authoring only.
         ai-advisor → waived: no model sits on any path in this document.
- depends-on: .plans/2026-09-07-lap2-RETRO.md
- depends-on: .plans/2026-09-07-lap-boundary-PROCESS.md
- depends-on: .plans/2026-09-07-pipeline-flex-point-AUDIT.md
- depends-on: .plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md
- depends-on: .plans/2026-09-07-lap3-paul-feedback-CAPTURE.md
- depends-on: .plans/2026-09-07-lap3-paul-feedback-CAPTURE-2.md
- depends-on: cycle/release/CYCLE-MAP.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- stage: draft
- wip-exception: none needed — `draft` is not in `check-backlog-ready.IN_FLIGHT`, so this document opens no WIP. Declared so the in-flight count stays honest.
- stage-note: 2026-09-07 — ⚠️ **two expected flags, neither a defect to repair.** (1) *orphan* — no `BACKLOG.md` row points here, same as every process document in `.plans/`; its siblings escape only because `-PROCESS` and `-AUDIT` are in `DOC_SUFFIXES` and `-PROPOSAL` is not. (2) *"stage `draft` with no `ready: [paul-approved …]` stamp"* — this **contradicts the checker's own comment** at `check-backlog-ready.py:50`: *"`draft` sits BEFORE `ready`, so it is not 'past ready' and needs no approval stamp."* The code flags every stage except `ready`; the comment says `draft` is exempt. ~~**Reported, not resolved**~~ → ✅ **RESOLVED 2026-09-07** `[paul-ruled: "number four seems like it's worth fixing"]`: the COMMENT was right and the code was wrong. `check-backlog-ready.py` now exempts `draft` as well as `ready`. ⚠️ The `-PROPOSAL`-not-in-`DOC_SUFFIXES` half of this note still stands and is still deliberately unresolved — whether a proposal is a document or an item changes what the gate means.
- gate: ⛔ **THIS IS A PROPOSAL AND NOTHING IN IT STARTS.** No step below runs until §7 is ruled.
  ⛔ **Nothing here is ranked.** Every ordering is dependency and sequence. Where the lap needs a
  value call — *which concepts enter which stage, what we take on* — this document **lays out the
  board and stops**, which is option (b) of the F3 blocker.
- stage-note: 2026-09-07 evening — written at `92be1bf`. Every tool named here was executed tonight;
  every count carries its predicate. Grades: `measured` · `inferred` · `proposed`.

---

## ⛔ STATUS, 2026-09-07 — THIS DOCUMENT'S GATE LINE IS NO LONGER TRUE, AND ITS BEAT NUMBERS ARE SUPERSEDED

`[process-audit D1 + the status pass it recommended]`

Its `gate:` above reads *"NOTHING IN IT STARTS. No step below runs until §7 is ruled."* **§7 WAS
RULED on 2026-09-07 and beats 0 and 1 ran against it**, so that line is now false where it sits.

**Disposition of each part, so nothing is left ambiguous:**

| part | state |
|---|---|
| **§7 A-1, A-2, A-3, A-5, A-6** | ✅ **RULED** by Paul 2026-09-07 and applied — see `cycle/release/CYCLE-LOG.md` § Lap 3 |
| **§7 A-4** (does the FOCUS FREEZE bind Mom on `est-e6696a`?) | ⛔ **MOOT** — it was already answered by J-a the same evening. The question was stale, not open |
| **§4's BEAT NUMBERING** | ⛔ **SUPERSEDED by `CYCLE-MAP.md`.** This file's *"BEAT 1 · CONSOLIDATE"* predates A-1; in the map beat 1 is **"a BUILD exists"** and the estate-manager beats are 0 and 6–11. ⚠️ **Do not cite a beat number from this document.** |
| **§2.1's warning** that `design` and `journey` are not strictly sequential | ⬜ **never ruled** — stated, unsolved, and still true: the checker compares by list index |
| **§2.2's WIP numbers** | 🟡 ruled as a **first cut** (A-3), with their own falsifier to be read at close |

⛔ **`stage: draft` is CORRECT and stays** — `draft` opens no WIP and needs no approval stamp. **No
`superseded` stage is being minted for this**; that is precisely the ceremony the ladder exists to
avoid `[[feedback_reuse_vocabulary_before_adding_state]]`.

---

## 0 · THE ONE-LINE ANSWER

> **Lap 3 opens with a proving beat, not a build beat. It runs the three sweeps and proves them
> end-to-end, consolidates what they return, and only then — at a single commitment point — lays out
> the options board for Paul. Some items advance a stage and ship nothing; that is a successful lap.**

Paul's own order, stated tonight, and this document does not reorder it:
*run the sweeps and prove them → consolidate → then, once the data is in, build the options list
extensively.*

---

## 1 · THE TWO CADENCES, RECONCILED — this is not a new loop

`.plans/2026-09-07-lap-boundary-PROCESS.md` separates two cadences. Lap 3 is where they meet, so it
is worth being exact about which one owns what.

| | **the estate-manager cadence** | **the release loop** (`cycle/release/CYCLE-MAP.md`) |
|---|---|---|
| decides | what we do next, and at what scope | whether **this build** may be released |
| boundary | ⭐ **scope committed** | `cleared_sha` — Paul cleared a build |
| unit | a **scope-setting round** | a **lap** (n rounds → one clear) |
| gates | Paul, in a discussion | Paul, walking production |

⭐ **What lap 3 does that lap 2 did not:** it runs the estate-manager beats **first and explicitly**,
before any build exists, instead of discovering them mid-lap. Lap 2 ran them — the sweeps were *built*
in lap 2 — but ran them **inside** a build lap, which is why the account watcher landed 35 minutes
after Mom's invite went out (`measured`: invite ~12:05 ET; `7282f7e` 12:12 ET).

⛔ **No fourteenth loop.** These beats live **inside** `cycle/release/CYCLE-MAP.md` as beats 0 and
6–11, sharing `cycle/release/cycle-state.json`. That is C-5 in the retro and it is Paul's call; if he
rules two loops instead, everything below still holds, only the file it lives in changes.

---

## 2 · THE STAGE LADDER — ⭐ it already exists, and it is missing exactly one rung

Paul, tonight (F3): *"every lap we're moving some concepts along from a design and journey point of
view, and others that have already been well defined are being pushed out to production — so we have
not just different processes but a pipeline of things moving through that process."*

**`measured`, and this is the finding that saves lap 3 a build:** the ladder is already implemented.

    tools/check-backlog-ready.py:51
    STAGES = ["draft", "ready", "concept", "build", "qa", "shipped", "retro"]

…with a `stage:` key on every plan, a `paul-approved` gate required past `ready`, a `## Retro` heading
required at `shipped`, and — `:374-379` — **a work-in-progress limit already enforced** with a
`wip-exception:` escape. **F3's "missing axis" is not missing.** What it is missing is one rung and
one piece of placement.

### 2.1 The missing rung

`concept → build` has nothing between it. Paul named the two states he wants items to move through —
**design** and **user journey** — and neither is a legal `stage:` word, so an item that has been
designed but not built has nowhere to stand and reads as `concept` forever.

**Proposed, and it is a one-line enum change plus a definition:**

    STAGES = ["draft", "ready", "concept", "design", "journey", "build", "qa", "shipped", "retro"]

| rung | it is at this stage when | the artifact that proves it |
|---|---|---|
| `concept` | the thing is named and bounded; nobody has said how it works | a PROPOSAL with a `row:` and an `objective:` |
| **`design`** | the mechanism is specified — screens, states, data, refusals — and could be built by someone who was not in the room | a PLAN whose seats are declared or waived |
| **`journey`** | a person's path through it is drawn end to end, including the failure paths | a user-researcher journey artifact under `.user-research/` |
| `build` | code is being written | commits |

⚠️ **`design` and `journey` are not strictly sequential and the enum will imply they are.** Paul's own
words put design before journey; `check-backlog-ready.py` compares by list index, so an item that
does journey work first will read as moving backwards. **Stated, not solved** — the cheapest honest
answer is that the ladder records the *furthest* rung reached, not the last one worked on.

### 2.2 The WIP limit — ⭐ it exists, it is crossed 13-to-1 right now, and its alarm is buried

`measured`, executed tonight:

    🧭 In flight: 13 items between concept and qa
       8 @ concept · 4 @ build · 1 @ qa · 7 carry a declared `wip-exception:`
    · WIP: 13 items between concept and qa and not every extra one carries `wip-exception:` —
      the one-at-a-time default was crossed silently

That line is **flag 137 of 131 findings** in a report nobody reads to the bottom. **A true alarm
nobody can see is the failure mode Paul's own rule exists to prevent**, and this one is not
permanently red by construction — it is red because the limit is genuinely crossed.

**Proposed limit, and the number is argued from the measured bottleneck, not from Kanban:**

| stage band | limit | why this number |
|---|---|---|
| `design` + `journey` | **2 in flight** | these consume Paul's attention in a discussion, and a discussion is the scarce thing |
| `build` + `qa` | **1 in flight**, the existing default | unchanged; it is already the rule and it already has an escape hatch |
| `concept` | **no limit** | ⭐ **deliberately.** A concept costs nothing to hold and capping it would push ideas out of the record, which is the one failure this corpus cannot afford. `.plans/2026-09-07-dropped-ideas-MINE.md` exists because ideas leaked once already |

⭐ **The binding constraint is disposal, not throughput.** `measured` tonight: **25** `.plans/` files
carry `ready: agent-proposed`, **1** carries a `paul-` stamp. **480 feedback records await disposition
across 6 environments, 0 disposed.** A stage ladder with no limit is N queues; a limit that ignores
where the queue actually backs up is decoration. **The queue backs up at Paul's ruling, in both
cases.** So the limit that matters is on things *awaiting his word*, which is what the design/journey
cap of 2 is really counting.

**Falsifier:** if lap 3 closes with the in-flight count unchanged at 13 and nothing was blocked by the
limit, the limit is not binding and the number is wrong. Read it at lap 3's close, not by argument.

---

## 3 · THE THREE DETERMINISTIC SWEEPS — where each fires, and what each gates

Paul asked for these to be **formalised and tested** in lap 3. `measured` tonight: all three exist and
all three pass their own mutation-proven selftests.

| sweep | command | selftest tonight | fires | **what it gates** |
|---|---|---|---|---|
| **health** | `python3 ~/.claude/tools/health-probe.py --only fernwood` | ✅ **PASS (34/34)** | **beat 0**, before anything | ⛔ **Nothing, by design.** It reports whether the *record* is intact — a short weather day, a dead Action, a Pages or Worker failure. A red here is a **finding for the lap's agenda**, not a block on opening one. Blocking a lap on it would make the loop unable to open in order to fix the thing that is broken |
| **accounts** | `python3 tools/watch-accounts.py` | ✅ **PASS** | **beat 0** | ⭐ **It gates the CONSOLIDATION beat, not the build.** An arrival nobody has looked at means beat 2 (consolidate) has an input it has not read. ⚠️ Its `exit 3` — *an unreadable namespace is UNREADABLE, never "no new accounts"* — is the important half and must never be treated as clean |
| **feedback** | `python3 tools/watch-feedback.py` | ✅ **PASS** | **beat 0**, and again at close | ⭐ **It gates the COMMITMENT POINT.** The options board may not be built while records nobody has read are sitting in the store — that is the whole of Paul's stated order. `measured` tonight: **10 of 10 production records awaiting disposition, 1 of 10 fully labelled** |

### 3.1 ⭐ What "prove them" must mean in lap 3, because the unit tests already pass

The three selftests prove each tool **in isolation**. What has **never been proven is the chain**:
`measured` — beat **F3 (dispose) has fired zero times**, so F4 (read), F5 (carry) and F6 (arm) have
never had an input, and the design that specifies them
(`.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md`) is built only through F2.

**So the proof lap 3 owes is end-to-end, and one record is enough:**

> Take **one** production record. Sweep it (F1) → confirm it is labelled (F2) → Paul disposes it
> `act|fold|hold|not-a-finding` (F3) → it reaches a BACKLOG row or a pre-registration **citing its
> record id** (F5) → the undisposed count falls by exactly one (F6).

**That is the falsifier for the whole consolidation design.** If one record cannot make that trip, the
design is wrong and no amount of sweeping fixes it. It is also §6 P4 of the retro, pre-registered.

⚠️ **A ruling Paul owes before F3 can run at all, and the sweep must not settle it by existing:** the
mom-cycle **FOCUS FREEZE** says *hold all feedback from Mom* and was written for the frozen estate
`est-3c9f1a`. **Does it bind her arrivals on `est-e6696a`?** Her invite `p-b91e4d` is out and unspent.
Whether a first arrival from her is swept, read, or held is his word, not a tool's.

---

## 4 · THE PROCEDURE — lap 3, step by step

⚠️ Written so a person could follow it. Beats 0 and 6–11 are the **estate-manager** beats proposed
into the release map (C-5); beats 1–5 are the release loop's existing five, unchanged.

### BEAT 0 · OPEN THE LAP — *and lap 2 must be closed first*

`[[feedback_close_a_loop_before_opening_the_next]]`, and it is symmetric.

1. **Close lap 2 in the record.** Run `python3 tools/release-state.py --cleared 1e2748d`. `measured`
   tonight: `cycle-state.json` still reads `last_lap {lap: 1, cleared_sha: c821051}` and **lap 2 and
   Paul's clear are absent from it.**
2. **Apply R-E** (retro C-1): rewrite both chronicle headings to `## Lap N — YYYY-MM-DD · …`, add
   `<!-- outcome:closed at:<utc> -->`, and read `momlib.lap_outcomes()` at `release-state.py:49`.
   Verify: `lap_outcomes('cycle/release/CYCLE-LOG.md')` returns **2**, not 0.
3. **Dispose the two lap-1 pre-registrations** — the retro §5 discharges `instrumented-counted` (yes,
   4 of 4) and states why `second-viewport` cannot be discharged. Write both dispositions into
   `pre_registered[]`; `open` is not a carry-forward.
4. **GATE SWEEP** (the spine's 08-31 amendment): read every fired item-gate and dispose each —
   *act · fold · snooze · kill*. **Snooze is gated on Paul and batched** (*"these 3 push to X — go"*),
   and a third snooze on any row flags out loud.
5. **Run the three sweeps** (§3). Record what each returned, including **UNREADABLE**, which is never
   zero.
6. **Open lap 3** with its own dated heading and `<!-- outcome:open -->`.

**Exit:** lap 2 marked closed and machine-readable · both pre-registrations disposed · three sweeps
run and their output recorded · lap 3 heading written.

### BEAT 1 · CONSOLIDATE — *before any option is discussed*

7. **Run the end-to-end proof** (§3.1) on one record.
8. **Merge the two capture files** — `.plans/2026-09-07-lap3-paul-feedback-CAPTURE.md` (F1–F6) and
   `-CAPTURE-2.md` (F7–F15). They were split deliberately mid-read and their own text says *"merge
   the two after the panel reports."*
9. **Bring tonight's walk into `GATE2-paul-findings.md`**, whose Lap 3 section reads `*(open)*`. Its
   third column — *did any seat raise it?* — is the loop's only instrument for its own blind spots,
   and its own text says *"a lap that adds rows without answering the third column has not been read,
   only filed."* **F4 is the row that matters:** the answer is *no seat could*, and the retro §3.0
   says why in three measurements.
10. **Count the repeat asks** (retro C-7). `measured`: roles-and-invite was asked at **11:21 ET** into
    the production store (`homes-second-home`) and again tonight (F14); logout twice the same evening
    (F12). ⛔ **Record the count. Rank nothing by it.**

**Exit:** one record has made the full F1→F6 trip · the captures are one document · the walk is in the
findings register with its third column answered.

### BEAT 2 · ⭐ THE COMMITMENT POINT — the options board, built once, with the data in

11. **Lay out the board.** Every item that could advance, with: its current rung · what it is blocked
    on · what advancing it costs · what it would ship, if anything. ⛔ **Unranked.** Dependency and
    sequence are stated; value is not.
12. **Paul picks**, in a discussion. This is beat 7 of the estate-manager loop and **no instrument
    should ever be built for it** — it is the human gate.
13. **Scope is committed.** After this point the plan does not keep evolving. ⚠️ **The map must say
    what may break a commitment** — a production blocker of the rain-gauge class — rather than
    pretending nothing can.
14. **Apply the WIP limits** (§2.2) to what was picked, or declare a `wip-exception:` with a reason.

**Exit:** a committed scope, with each item's target rung named, and the in-flight count inside the
limit or explicitly excepted.

### BEATS 3–7 · THE RELEASE LOOP, unchanged — *for the items that are shipping*

The five existing beats run exactly as mapped, with **three amendments** carried from the retro, all
of them already ruled or safe:

- **`4a3a61b` is the first candidate.** It is on `main`, unwalked, and fixes two knowingly-shipped
  defects in `estate/index.html`. It is also **in the same file and the same journey** the harness
  cannot reach.
- **The returning journey gets walked** (retro C-2). `measured`: 39 of 39 lap-2 walks were `--fresh`;
  the returning mode is a flag with no step list behind it past stop 2; `journey-view.py:63` opens an
  empty browser context every run, so the device state F4 lives in has never existed in the harness.
  **This enacts Paul's own 2026-09-06 two-classes ruling, which the map already lists as owed.**
- **Gate ① prints the intersection** (retro C-3): which seats both can exercise a placed household
  **and** had undegraded data. Counted, never graded, no refusal.

### BEATS 8–11 · DISPOSE, READ, CARRY, ARM — the successor beats

15. Sweep · label · **Paul disposes** · user-researcher reads only `act`/`fold` · a citation-bound
    seat carries each to a row · the state arms for the next beat 1 when **zero records are
    undisposed**.

⭐ **This is the beat lap 2 did not have**, and it is why 10 production records have sat since 11:22
ET this morning.

---

## 5 · THE DESIGN LANE — zones, and what a successful shipless lap looks like

Paul, tonight: zones get a **dedicated session**, move **concept → design → ideally journey**, and are
⛔ **explicitly not released to production this lap.**

**Zones is the test case for whether the ladder is real.** It must be possible for zones to advance a
rung and produce no deploy without that reading as a failed lap.

| | |
|---|---|
| **Rung at open** | `concept` — `measured`: 23 named polygons, 2.64 acres, a georeferenced 2022 aerial, per-estate from KV. **Works once, by hand, for one property, on a surface only Paul can drive** |
| **Target rung** | `design`, and `journey` if the session gets there |
| **Ships** | ⛔ **nothing.** Zones do **not** migrate to production — Mom's map is blank when she arrives and the 23 hand-traced zones stay on the frozen control as the answer key `[paul-ruled, BACKLOG:228-235]` |
| **What must exist for the rung to be earned** | `design`: a PLAN with seats declared or waived. `journey`: an artifact under `.user-research/` drawing a householder's path including the failure paths |
| **Already-ruled constraints that bound the session** | *we draw, they confirm* `[paul-ruled 2026-09-06]` · the standing 2026-07-31 hold un-parks on a signal from Mom that zones matter · the record holds **areas only** and Paul has asked twice for lines and points · the participation surface got **0 taps in 10 offers** |
| **Unread input** | ⚠️ an **812-line** `.plans/2026-09-06-maps-and-zones-PROPOSAL.md` exists and was not read by the window that captured F1. Read it before the session, not during |

⭐ **The lap's closing condition must therefore be stated in two halves**, or a shipless advance will
read as failure at close:

> **Lap 3 closes when (a) the release loop's gate ① and Paul's clear are satisfied for whatever
> shipped, INCLUDING the case where nothing shipped, and (b) every item in the committed scope is at
> or past its target rung, or its shortfall is recorded with a reason.**

⛔ **Which is not the same as "the lap succeeded."** That judgement is Paul's; the closing condition is
only what makes it *checkable*.

---

## 6 · F4 AND THE COHESIVE FRAMING — where it enters this procedure

Paul's framing (F6): *"an account's facts and its credential are two separate records, and exactly one
code path reconciles them — the one with no door."*

⛔ **Not six tickets. One seam.** Everything falls out of it: the missing sign-in screen (row 20), a
minted grant born blank, a spinner with three causes and no exit, a stale identity nulls can never
correct, no sign-out, the owner guard fighting the reconcile, and Mom's unspent invite carrying the
same blankness right now.

**Where it sits in this procedure, and this is sequence, not priority:**

- It is a **candidate for the design lane** alongside zones, not a fix queued behind a deploy — his
  own reading, and `.plans/2026-09-07-sign-in-door-PROPOSAL.md` already scopes the returning half at
  `stage: concept` with a `wip-exception:` declared.
- ⚠️ **It is also the one item with a live dependency on the release lane:** `4a3a61b` is unwalked and
  fixes two defects on the same card. **Advancing the seam in design does not make the shipped
  regression go away**, and the two must not be collapsed into one item.
- ⭐ **The retro's C-2 is its prerequisite, not its consequence.** The harness cannot walk a returning
  person; F4 is a returning person's defect; **until C-2 lands, no amount of design work on this seam
  can be certified by the loop.** That is a dependency and I will state it that plainly.

⚠️ **Whether the seam or zones goes first is Paul's.** Both are legitimate; the WIP cap of 2 in the
design band means **both can be in flight and a third cannot**.

---

## 7 · WHAT PAUL MUST RULE BEFORE THIS RUNS — six, each yes/no or A/B

| # | ruling | my answer | falsifier |
|---|---|---|---|
| **A-1** | **Does the release map gain beats 0 and 6–11, or is the estate-manager cadence a second loop?** (retro C-5) | **One loop.** A second loop is a fourteenth for a solo operator, and the state artifact is already shared. ⚠️ `render.py:832` cannot parse `F1 · SWEEP` — renumber or accept prose | If beats 6–11 fire and the undisposed count does not fall, the beat was bookkeeping and the constraint was never the beat |
| **A-2** | **Add `design` and `journey` to `STAGES`?** (§2.1) | **Yes.** It is a one-line enum change to a ladder that already exists, and without it an item Paul has designed reads as `concept` forever | If no lap-3 item ever sits at `design` or `journey` for more than a day, the rungs are ceremony — read it at lap 4 |
| **A-3** | **WIP: 2 in the design band, 1 in build/qa, uncapped at concept?** (§2.2) | **Yes**, and the concept exemption is the load-bearing half | If the cap blocks nothing in lap 3, it is not binding and the number is wrong |
| **A-4** | ⭐ **Does the mom-cycle FOCUS FREEZE bind Mom's arrivals on `est-e6696a`?** (§3.1) | ⛔ **No answer from me — this is his and only his.** The sweep must not settle it by existing. A hold needs a release condition or it is abandonment with manners | If her first arrival is swept without this being ruled, the freeze was decided by a tool |
| **A-5** | **Does the lap's closing condition have the two halves in §5** — so a shipless advance closes clean? | **Yes.** Without it, F3's pipeline cannot survive its first lap: zones will advance and the lap will read as failed | If lap 3 ships nothing and Paul reads it as a bad lap anyway, the condition did not do its job and the problem was never the wording |
| **A-6** | **Who lays out the options board at the commitment point** — a ranking seat, or agents lay out the board and Paul picks? | **Agents lay out the board; Paul picks.** No seat in the stack may rank: `product-steward`'s charter forbids it at `:92` and `:144`; mine forbids it outright. Option (b) needs no new agent | If the board is consistently so long that picking from it is the bottleneck, a bounded ranking seat becomes a real question — measure it at cycle 2, do not argue it now |

### R-A…R-F, carried forward with their current state

| | state tonight |
|---|---|
| **R-A** declare the estate-manager loop before its first run | **still A** — this document is that declaration, in map form. `measured`: nothing has changed the argument |
| **R-B** scope committed at the commitment point | **still A**, and §4 beat 2 step 13 is where it happens |
| **R-C** R6's expiry hangs at the scope-setting beat, not at lap close | **still A**, and stronger: `measured` tonight, **25** files carry `ready: agent-proposed` against **1** `paul-`. `ready:` still does not record a ruling, so any clock-based expiry would close decisions already made |
| **R-D** the product-steward trial ends at the next `cleared_sha`, floor of 3 rounds | **still A.** Lap 2 cleared with the trial at **round 1** — the floor is exactly what stops a ruling on n=1 |
| **R-E** derive the lap from its own chronicle | **still yes, and the case is now much stronger** — retro §2.4. The state artifact lost lap 2 and Paul's clear |
| **R-F** one corpus-bounded review per cycle at the disposal beat | **still A.** The lap-2 retro was that one. §4 beat 1 is where lap 3's belongs |

---

## 8 · WHAT THIS PROPOSAL COULD GET WRONG

- **The ladder may be over-specified for one operator.** Two new rungs and two caps is real
  bookkeeping. **Cheapest test:** run lap 3 with them and count how many times a rung or a cap changed
  what happened. If the answer is zero, cut them at lap 4 — do not defend them.
- **Beat 0 is long.** Six steps before any work. `inferred`: most of it is one-time (closing lap 2,
  applying R-E, disposing two pre-registrations) and beat 0 shrinks to *sweep, gate-sweep, open* from
  lap 4. If it does not shrink, it is a procedure and not a repair, and it is too heavy.
- **The end-to-end proof (§3.1) needs Paul's attention to happen at all.** F3 is his beat. If it does
  not fire, the proof does not run, and the honest reading is that the consolidation design is
  waiting on the same constraint everything else is.
- ⛔ **I have not designed the sign-in door, the zone surface, or anything else on the board.** This
  document says where things go and in what order. What goes into them is not mine.
