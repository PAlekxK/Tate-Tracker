# Lap 9 — READINESS. What is defined enough to plan, and what is not

- **stage:** `concept`
- **ready:** `agent-proposed — this is NOT a build plan. It says, per row, what must happen before a build plan can be written.`
- **row:** `cycle/release/CYCLE-LOG.md` § *Laps 8 and 9 — SCOPE COMMITTED BY RULING* (`767242c`) §"Lap 9" ·
  `.plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md` §2
- **objective:** O3 · **class:** engine
- **Author:** engineering-partner, mode **path-evaluation**, commissioned beside the lap-8 plan
  `[paul-stated 2026-09-11: "…once we get to a point where it's defined enough for a detailed work plan to be built
  out of it."]` — **lap 9 is not yet at that point, and this file says exactly where each row stops.**
- **Companion:** `.plans/2026-09-11-lap8-build-PLAN.md` (the build plan). Every dependency below cites a **step id**
  in that file, so a lap-8 slip is visible here.
- **HEAD at writing:** `06c2a16` — ⚠️ **the lap-7 build window was committing while this was written** (five
  commits in one reading window). Re-measure before acting.

> ⛔ **What this is not.** Not a build plan. Not a commitment — **the pick is Paul's at lap 9's beat 6**, and
> `767242c`'s lap-9 table is a set of rulings about *order and shape*, not an opened lap. Not a ranking of value;
> the ranking below is **readiness**, which is a different axis and says so on its own face.

---

# 0 · THE HEADLINE

**One lap-9 row is plannable today. The other four are not, and each stops in a different place — which is the
useful finding, because four different blockers want four different acts.**

| | row | stops at |
|---|---|---|
| 🟢 | **A · the weather card from an address** | a **stamp**, not a scoping — its plan exists, is `[paul-approved]`, and carries one **blocking** open question (Q8) |
| 🟡 | **C · Bob founds twice (J0 × 2)** | a **surface that does not exist** plus a **ruled refusal that must be reversed deliberately** |
| 🟠 | **E · the glance build** | **evidence that has not been collected**, behind a tool that has not shipped |
| 🟠 | **D · the capture write path** | a **design pass nobody has scheduled** — and lap 10's theme now depends on it |
| ⚪ | **F · zones preload** | **a person's act.** ⛔ Cannot be committed to a lap by construction |

⭐⭐ **And the sharpest thing in this file is not about lap 9 at all.** `[paul-ruled 2026-09-11]` **lap 10's theme is
THE PLACE — zones v1 (TIER 2 · 7) + the capture write path (TIER 2 · 8)**. Both are `design`/`concept` stage, both
need a design pass, and **the capture write path's pass has no slot in any lap today.** §6 is that timing question,
answered.

---

# 1 · ROW A — the weather card from an address 🟢 **READY TO PLAN, with one blocker**

**Ruled:** lap 9's **first row** (8·3, 9·2). *"The top priority of what we need to get ready to implement in the next
lap"* `[paul-ruled 2026-09-07]` — and it has now missed two laps, which is itself a signal about how the loop ranks.

**Its plan exists:** `.plans/2026-09-07-weather-card-PLAN.md` **[header block read; body not read]** —
`stage: concept`, `ready: [paul-approved 2026-09-08]` (*"Wherever you have a clear recommendation, go ahead and do
it"*), with a `wip-exception` declaring it executes nothing between concept and qa until Paul stamps it.

### What is defined
- **The v1 cut is ruled** — tiers 2 + 3 together (W-5) · accrual rides on the station opt-in (W-6) · a per-estate KV
  row carries credential + history + notes (W-8) · the two asks sit beside the address at setup (W-10) · every
  critical derived figure is surfaced for confirmation, elevation first (W-7) · source applicability keyed on
  address-derived facts (W-9).
- **The floor already shipped** — W0, address → lat/lon + county FIPS, US Census, keyless, **no default coordinate
  ever** (`worker.js:809`, cited on TIER 2 · 11).
- **The capture path is named**, down to the field values: `postAnswer(...)` → `POST /api/feedback`, read by
  `read-onboarding.py`, two new `field:` values `weather-radar` and `weather-station` **[read, plan header]**.
- **Its seats are declared** with trails **[read]** — engineering-partner · ux-expert · content-steward ·
  user-researcher · ai-advisor **waived by reason** (no model on this path) · practice-steward waived.

### What is NOT defined
1. 🔴 **Q8 is BLOCKING and is IN the v1** — *"a Georgia EPD literal in engine code tells a Maine household Georgia's
   law"* (TIER 2 · 11). ⛔ This is the estate-neutrality class with a legal claim attached, and it is the one thing
   that cannot ship un-ruled.
2. ⚠️ **Every declared seat cites a PRIOR trail, none of them a read of this scope** (the plan's own 12:45 PM
   stage-note: *"a fresh pass by each declared seat is owed before `ready:`"*). The `[paul-approved]` stamp landed
   anyway. **Both facts are in the file and they disagree** — put it to Paul rather than resolving it in a plan.
3. ⚠️ **No estate has weather at all.** `read-geocodes.py` reads *"the geocoder was not asked"* at `home`, `paul`,
   `bob` and `lab`; only `qa` has outcomes. ⭐ *"This starts as a retry that has never fired, not as a feature."*
4. ⛔ **A separate live defect rides on the same card:** a household never gets a climate panel — three of four
   seats' extracts carry `CLIMATE LOADING ERA5 ACTUALS…` forever because `fetchClimateNormalsInner` asks for ~33k
   values and blows `WEATHER_STALL_MS = 20000` (TIER 2 · 11, measured at `95b8559`). **A build plan must decide
   whether that is in the row or beside it.**

### Depends on lap 8, by step id
- **A2 · A9** — one origin, and a real `estates[]`, so *"every household's card reads one address model"*.
- **A1** — the sentinel: the weather **cache** keys (`ambient` by MAC, `airnow` by lat/lon) are `check-scope-sites`
  batch **B-CACHE** (lap 8 · A3). ⛔ **This row is the largest consumer of the four keys whose suffix is
  household-identifying data.** If A3 slips, this row ships a cache that is a directory of where people live.
- **TIER 2 · 12** — the per-estate canon store seam for the station opt-in. ⚠️ **Not a lap-8 row.** It is stamped
  *"size it BEFORE a lap opens"* and it **fires W6** (species vs instance, deferred since July). **This is the
  quiet dependency most likely to surprise a lap-9 build window.**

### What must run before a build plan can be written
**Not a scoping — a ruling and a re-read.** (i) **Paul rules Q8** (how a jurisdiction-specific source is declared
per household rather than typed into engine code); (ii) **the four declared seats do a fresh pass on this scope**,
or Paul waives that explicitly; (iii) **TIER 2 · 12 is sized** at least far enough to say whether the station
opt-in needs it in v1 or can wait.

> ### ⭐ **Defined enough when:** Q8 is ruled, TIER 2 · 12's seam is sized, and the plan's own seat lines cite a read
> of *this* scope. **At that point I can write `.plans/<date>-lap9-build-PLAN.md` for this row in one pass** — the
> rulings are already there, and what is missing is authority, not design.

---

# 2 · ROW C — Bob founds his own, twice (J0 × 2) 🟡 **NOT PLANNABLE — one surface missing, one refusal to reverse**

**Ruled:** 9·1 — *"J0 twice — founds his own houses at the open door"*, **no invite**, INVITE & JOIN off lap 9's
critical path. ⚠️ The ruling itself names the dependency: *"a second house needs the **add another place** path
(TIER 1 · 19) — lap 8's estate-as-row **plus a founding-surface step**."*

### What is defined
- **The journey shape.** J0 exists and is built (`journey_founding`, entered from the bare door, shape (b)) —
  `tools/journey-walk.py:790` **[read]**. Walking it twice is not a new journey, it is the **second** run that has
  nowhere to start.
- **Done means** is stated: *"Bob reaches his house(s) from his own device; every read he makes for another estateId
  is 404"* — the multi-tenancy falsifier with a real person in it.
- **He has no live invite**, and that is settled, not a gap: `bob`'s deployment was DESTROYED 2026-09-10 and the
  unspent invite died with it (teardown §1; `.plans/2026-09-10-teardown-REPORT.md`). Under the fifth lens he founds
  his own.

### What is NOT defined — and one of the two is a ruled invariant
1. 🔴 **`POST /api/estate` REFUSES a second estate, by design.** `measured` at `06c2a16`,
   `worker.js:1403–1407`: **409 `already-has-an-estate`**, with the comment *"ONE ESTATE PER PERSON, FOR NOW, AND
   THE REFUSAL IS THE POINT… a second one cannot be reached until a request can say WHICH — and that is the unruled
   question."* And **`walk-founding.py`'s acceptance clause B pins that refusal as correct behaviour** (`:246–271`
   **[read]**). ⛔ **So lap 9 · C reverses a ruled invariant and its own harness clause.** That is legitimate — lap 8
   · A7 builds the mechanism (`X-Estate`) that the comment names as the missing piece — **but it must be reversed
   deliberately, in one commit with the clause, not discovered by a build window.**
2. 🔴 **There is no "add another place" surface anywhere.** TIER 1 · 19, verbatim: *"two things must both exist and
   only one is scoped: ① per-request scope… ② a **found-a-new-estate flow**, which does not exist even after ①."*
   ⚠️ `homes/index.html`'s `＋ Add a home` is **live at qa and no walk has ever tapped it**
   (OPEN-ITEMS ③) — *"there is no person→estates enumeration behind it."* Lap 8 · A6/A9 builds that enumeration;
   **what happens when the button is tapped is undesigned.**
3. ⚠️ **The shelf's 2+ case has never been designed or walked** (lap-8 plan §10, and A12's own note: the 2+ branch
   has no fixture until this row).
4. ⚠️ **Bob is a real person, so this is a gate-kit walk, not a seat's** (TIER 1 · 25). His walk is Paul's to run.

### Depends on lap 8, by step id
**A6** (the `grant:<personId>:<estateId>` edge — the only thing that can hold two houses for one person) ·
**A7** (`X-Estate`: a request names which) · **A9** (`estates[]` as an array) · **A10** (the 409's comment rewritten
rather than the refusal deleted) · **A12** (the shelf's 2+ branch) · **B6c** (the apex link is what Bob receives).

### What must run before a build plan can be written
A **ux-expert design pass on the founding-surface step** — reached from the shelf, entered by someone who already
has a house. Small in surface, and it inherits every founding ruling already made (the gate card, the PO-box
refusal, the receipt, one filled control). ⛔ **What it may not inherit is the entry state**: J0's list starts at
the bare door and this walk starts signed in, so **`journey_founding` cannot be reused unchanged** — the same lesson
J2 taught on 09-08 when its list was re-pointed at J3 and five of five clicks failed against the wrong screen, *not
one of those failures a defect*.

> ### ⭐ **Defined enough when:** lap 8 · A6/A7/A9 have landed and passed A15, **and** a ux-expert pass has closed
> the add-another-place surface's shape and entry state. Until then a build plan would be specifying a screen
> nobody has drawn against an endpoint that still refuses.

---

# 3 · ROW E — the glance build 🟠 **NOT PLANNABLE — it is two dependencies deep, and the first has not shipped**

**Ruled:** the *shape* is fully ruled (GL-1…GL-13, `[paul-ruled 2026-09-07]`). The **design pass** is lap 8 · D,
**conditional on ≥ 10 real sessions** in `read-glance-order.py` at lap 8's beat 6, *"else it moves to lap 9 by
rule"*. The **build** is lap 9 · E *"if D ran in lap 8"*.

### The chain, and where it actually stands
`measured` at `06c2a16`: **`tools/read-glance-order.py` does not exist.** It is lap 7 · **C7**, and the lap-7 build
window has landed P1–P4, D1–D4 and the B6 security read — **row C has not started.** So:

> **G6 events must ship → the reader must ship → the reader must accumulate ≥ 10 real sessions → the design pass →
> the build.** Five links, and link 1 and link 2 are both inside a lap that is still open.

⚠️ **And the sessions must be *real*** — across the real households, of which there are **two accounts total**
(`pkirsch` at the condo with **zero metrics batches**, consistent with the app having had no Worker there until
lap 7 · D; `marguerite` at `home`, 13 sessions over 3 days ending at her signup, **nothing after it**). **10 real
sessions is roughly a week of two people using the app**, not a day.

### What is NOT defined
1. **Whether the threshold's window is stated.** 10 sessions *since when*? Lap-8 plan §9 Q7 puts this to Paul:
   ⛔ *a count without its window* is the reading this loop has been burned by twice (`check-telemetry.py --before`
   exists precisely because *"a zero is only readable if the event was live before the window opened"*).
2. **The design itself.** By ruling, it may not be designed from zero — *"a design pass with no reading is the thing
   the exclusion forbids."*
3. ⚠️ **A live unreproduced report sits on the same row** — Paul, 2026-09-08: *"the formatting of local resources
   within the Grant Park Condo window is a little off"*, recorded as **his observation, unreproduced.** ⛔ Reproduce
   before acting.

### Depends on lap 8, by step id
Nothing in lap 8's candidate. It depends on **lap 7 · C1–C7** and then on **lap 8 · D** (the design pass), which is
itself conditional. ⭐ **This is the row whose slip rule is already written, and a slip is therefore a rule and not a
failure** — say so at beat 6 rather than treating it as a miss.

> ### ⭐ **Defined enough when:** the reader exists, has read ≥ 10 real sessions **inside a stated window**, and the
> ux-expert/user-researcher design pass has produced a proposal citing G6 evidence **by sha**. Realistically that is
> **lap 10 or later**, and saying so now is cheaper than discovering it at lap 9's beat 6.

---

# 4 · ROW D — the capture write path 🟠 **NOT PLANNABLE — and lap 10 now depends on it**

**Stage:** `concept` `[paul-approved]` — and the ⏭ rung says **a design pass is owed before any build.**
Plan: `.plans/2026-09-07-capture-write-path-PLAN.md` **[header read: `stage: concept`, no `ready:` line]**.

### What is defined — and it is smaller than its reputation
TIER 2 · 8, verbatim: *"⚠️ Smaller than it was first called. Verified: all eight `ghPutFile` sites belong to three
handlers, and the five capture handlers (feedback · observations · conversations · zone-feedback · zone-audio) touch
no git and work at `home` today. **Exactly one create is broken** — `handleZoneSave`'s 503 sits at the TOP of the
handler, blocking a KV write ~80 lines below whose own comment reads 'if git commits fail later, KV still has the
new data'… **Move the gate down.**"*

### What is NOT defined
1. ⛔ **R-Z6(B) is a SAME-COMMIT co-requisite**: before her first save `home`'s KV has no `zones:all` key, which is
   the condition that makes `handleZonesGet` **serve Fernwood's 23 zones to another household**. Fixing the write
   without gating the read *"shows her 'The bank' on her first map load."* ⭐ **That is the estate-neutrality leak
   class, armed by the fix itself.**
2. ⚠️ **Two pre-registered refutation checks are UNRUN** — POST the five capture endpoints against `home`, and
   `GET /api/zones` against `home`. **Both are cheap and neither has been done.** A design pass that runs them first
   is a design pass working from measurement.
3. ⛔ **The site premise has never been answered by this plan** (§6).

### Depends on lap 8, by step id
**A2** — `zones` (3 sites), `zones-last-seen` (2), `zone-feedback` (2), `zone-audio` (2), `zone-audio-blob` (2),
`observations` (2), `conversation` (1), `feedback` (2) are **all in batch B-CALLER**. ⛔ **Every capture handler this
row fixes writes through a key whose scope lap 8 · A2 converts.** Doing D before A2 means writing per-estate capture
against a deployment-scoped key — the work would be done twice and the second time silently.

> ### ⭐ **Defined enough when:** the design pass has run (§6 says when), the two refutation checks have been run
> against `home`, and R-Z6(B)'s read-gate is specified in the same document as the write-gate move.

---

# 5 · ROW F — zones preload (Z-13) ⚪ **NOT A LAP ROW, BY RULING**

**Ruled:** 9·3 — *"Mom's founding is a disposition when it happens, never a commitment — the loop rests; her input
fires it."* TIER 2 · 7's gate: *not until Mom has created her Fernwood and is ready.*

⛔ **It is listed so the gate is visible, not so it can be picked.** A person's act cannot be committed to a lap, and
committing it would convert the mom cycle into a backlog-driven loop — the exact inversion `MOM-CYCLE-MAP.md`
forbids.

**What it depends on:** lap 8 · **B** (she has an origin to found at) and **B6c** (the link she receives is the
apex). **What it needs beyond that:** the cleaned 23 zones and her sixteen names on them — `stage: design`,
stamped, *"the stage gate to build is a sha on QA."*

⚠️ **One thing that IS a lap's to do:** when she founds, **the preload must be ready to fire**, not started. A
disposition that finds nothing built is a disposition that costs her a wait.

---

# 6 · ⭐⭐ LAP 10 IS **THE PLACE**, AND ITS DESIGN PASS HAS NO SLOT — this is the scheduling decision

`[paul-ruled 2026-09-11]` **[relayed by the coordination window]**: **lap 10's theme is THE PLACE — zones v1
(TIER 2 · 7, `design`) + the capture write path (TIER 2 · 8, `concept`, LEG 0).**

**The problem, stated plainly:** both rows need a design pass; **one of them (D) has no pass scheduled in any lap**;
and `BACKLOG.md`'s ⏭ note says *"zones' design work is not a lap slot"* — i.e. it runs in **its own window, beside a
lap**, not as a beat. So **nobody's beat owns it**, which is this repo's most-recorded failure shape: *a capability
the loop cannot reach by running its own procedure is not a capability the loop has.*

### WHEN the capture write path's design pass must run

| option | verdict |
|---|---|
| **Lap 8, beside the door** | ⛔ **No.** Lap 8 · A2 is actively converting the very key-building sites this pass must specify against. A design written against pre-conversion code is a design that must be re-read after A2 lands |
| ⭐ **Lap 9, beside the weather card — RECOMMENDED** | ✅ A2/A3 have landed and passed A15, so the pass designs against **the scope model that will exist**. Lap 9's candidate is the weather card (an engine feature), so a design window beside it does not compete for the build window. **And it leaves one full lap between the design and the lap-10 build** |
| **Lap 10, at its own open** | ⛔ **No.** It makes the design a beat-6 dependency of the lap it is supposed to feed, and a design pass that gates its own lap is how a lap opens with nothing to build |

> ### ⭐ **The recommendation in one sentence: run the capture-write-path design pass as its own window during lap 9,
> after lap 8 · A15 has passed, so lap 10 opens with a plan rather than a scoping.**

### What its declared seats must produce

| seat | what it must hand back for a lap-10 build to be plannable |
|---|---|
| **engineering-partner** | the gate-move specification (`handleZoneSave`'s 503 moved below the KV write) **plus** R-Z6(B)'s read-gate **in the same document** — ⛔ they are one change; the co-requisite is the whole finding · and the per-estate key shape for all five capture handlers **against the post-A2 code**, not today's |
| **user-researcher** | what a person is actually capturing, standing where they capture it — and ⭐ **the standing question first**: *what has she asked Paul for lately* (her own repeated ask is the zone→plant set, not retrieval) |
| **ux-expert** | what capture looks like **with no network** — the receipt that must not lie, the queued state, what "saved" may mean before a sync |
| **content-steward** | every word of that receipt. ⛔ *"Saved ✓"* against a queue is the exact sentence that already failed once (FINDINGS §3.1, the condo's dead Worker) |
| **security-steward** | what a queued capture holds on the device and for how long; whether a pending write survives a sign-out (lap 8 · A11's key allow-list is the control) |
| **ai-advisor** | **waived by rule, and say so** — capture stays deterministic and AI-free (CLAUDE.md's design-time default). Naming the waiver is what stops it being re-asked |

### ⛔ THE CONSTRAINT THE PASS MUST ANSWER, AND IT IS PERMANENT

`CLAUDE.md` § **THE SITE'S PHYSICAL PREMISE** `[paul-stated 2026-08-31]`, stated as a founding premise: **no cell
reception · coverage falls off with distance from the house · heavy tree cover.** ⚠️ **Note the shape:**
connectivity is *inversely* correlated with how far into the property you are — *"the places worth walking to are
exactly the places with no network."*

> **PERMANENT. Never propose a design whose mitigation is "improve the signal."**

**What that disqualifies for this pass:** anything that syncs, authenticates, calls an API or fetches a tile **at the
moment of capture.** In the field, capture is **entirely local, with sync deferred until whoever it is walks back
into range of the house.**

⛔ **And it applies to what already exists, not only to what gets built:** Mom's tap-a-zone-and-speak surface POSTs
to the Worker. If she records standing among the plants — *which is precisely where she would want to* — that POST
has no network. **A capture path that can lose her words while appearing to succeed breaks the one rule her surfaces
are built on: capture must not lie.** ⭐ **This is why the design pass is not optional and cannot be folded into a
build window:** the premise changes the shape of the write path, not its wording.

### What zones v1 depends on from lap 8

- ⛔ **Per-estate zone writes need estate-as-row.** `zones` (3 sites), `zones-last-seen` (2) and `zone-feedback` (2)
  are batch **B-CALLER** in lap 8 · **A2** `measured` at `06c2a16`. Until they resolve the caller's estate, "her
  zones" and "his zones" are the same key.
- **A9/A6** — a household's zones belong to an estate a person holds, and `grantsFor` is what says which.
- **A1** — the sentinel decides where a zone write lands if a site is missed. ⭐ **Zones are the richest per-household
  record in the product**, so this row is the one where a missed conversion would be most visible and most costly.
- **Lap 9 · D's own design pass** (above), because **LEG 0 is zones' co-requisite**: *"she cannot define a zone, and
  therefore cannot add a plant to one, until it lands."*
- ⚠️ **Z-13's preload stays gated on Mom's act** (row F) and is **not** part of a lap-10 build commitment.

---

# 7 · § INVITE & JOIN — the five-seat scoping **runs in lap 8**; the build is now a **lap-11** candidate

**Ruled:** 9·4 — *"convene INVITE & JOIN's five seats in lap 8"*; the build is **off lap 9's critical path** (9·1).
`[paul-ruled 2026-09-11, relayed]`: **the build moves to a lap-11 candidate** — lap 10 is THE PLACE.

⭐ **The scoping still runs in lap 8.** That is not made redundant by the slip; it is made *cheaper*, because a
scoping that lands two laps before its build is a scoping whose findings can change the two laps in between.
⭐⭐ **And one of its findings already has:** *"nothing can see within-estate, cross-person"* (OPEN-ITEMS ⑤·1) is
**the reason lap 8 declares `synced` clause s3 out of scope** (lap-8 plan §2 A5).

### The five seats, and what each must produce **in lap 8** for a lap-11 build

| seat | what it must produce |
|---|---|
| **user-researcher** | who the second person actually is at each real household — ⭐ and the uncovered walk shape the register already names: **multi-household person, cold device** (TIER 1 · 46's P-list). ⛔ Bob's *succession* case is a **requirement, not a persona**: two houses, one to each daughter, **each seeing only her own** (TIER 1 · 19, Paul's words) |
| **engineering-partner** | what the **pending invitation** is as a record and **where it lives** (the invitee's account, or the estate?) · how `relationship`/`capability` carry Paul's three roles · ⭐ **and the instrument**: a falsifier for **within-estate, cross-person**, which `falsifier-tenancy.py` (C1/C2/C3/C5, all estate-A-vs-B) and `check-household-isolation.py` (*"the subject is always TWO ESTATE PREFIXES"*) structurally cannot see. ⛔ **The row's own words: the instrument is a precondition of shipping, not a follow-up** |
| **security-steward** | **roster mode on the username-exists check before the field is built** — it is an enumeration oracle, and it sits beside the two that already publish username existence (lap-8 plan §2 A8) · whether an owner may confer `administrator` · what the invitee may learn about a house before accepting |
| **ux-expert** | the invite composer in estate settings · **the notification on the menu screen** · the accept/decline screen for someone who may already own a house · ⛔ and what the shelf shows **before** acceptance |
| **content-steward** | every word of the invitation — ⭐ *"you've been invited to join `<house name as the owner set it>` by `<owner's username>`"* is Paul's own sentence and it names a house to someone who is not yet in it; that is a disclosure decision wearing copy's clothes |

**Its own falsifier, already written and inherited unchanged:** *"a synthetic owner at qa invites a second synthetic
by username; the second signs in, sees the notification naming the house and the inviter, accepts, and `whoami`
lists that estate with the conferred role — **with no new `est-` id minted**."*

⚠️ **The three roles Paul named** — read-only · member (read and write) · owner (controls structure and modules) —
*"read as a capability ladder of three, not a relationship. Whether it maps onto `relationship SET · capability
SINGLE` or replaces it is scoping, not transcription."*

⭐ **And the spill-over he named himself:** *"if there's a multi-member household — we display who had each
conversation with the Garden Guru."* That is **attribution of a turn to a member** — a display question **and** a
privacy question **and** the first named instance of the invisible class. It touches the AI boundary's
administrator clause. **security-steward roster mode before any field.**

---

# 8 · THE READINESS RANKING

⛔ **This ranks READINESS, not value.** A row can be the most valuable thing in the backlog and still be unplannable
tonight — row A is ruled the priority and sits at the top here only because it is *also* the closest to plannable.

| # | row | state | the ONE thing standing between it and a build plan |
|---|---|---|---|
| **1** | **A · the weather card** | 🟢 **plannable after a ruling** | ⛔ **Q8** — the Georgia EPD literal in engine code. *(Then: TIER 2 · 12 sized, the seats' fresh pass.)* |
| **2** | **C · Bob founds twice** | 🟡 **plannable after a design pass** | **The add-another-place surface does not exist** — and the 409 that blocks it must be reversed in the same commit as `walk-founding.py`'s clause B |
| **3** | **D · the capture write path** | 🟠 **plannable after its design pass** — ⭐ and that pass is now **lap 10's** critical path, not lap 9's | **Nobody's beat owns the pass.** §6 recommends: its own window, during lap 9, after lap 8 · A15 |
| **4** | **E · the glance build** | 🟠 **two links away** | **`read-glance-order.py` does not exist** (lap 7 · C7, unstarted at `06c2a16`), so the reading window has not opened — and 10 real sessions across two accounts is about a week |
| **5** | **F · zones preload** | ⚪ **not rankable** | **Mom's act.** ⛔ Ruled never a commitment |

⭐ **What this says about lap 9's likely shape:** **A leads (ruled), C follows if its design pass runs, and E almost
certainly slips** — by its own written slip rule, which makes it a rule and not a failure. **D's design pass runs
beside the lap rather than in it.** That is a lap with one build row and one design window, which is a smaller lap
than lap 7 or 8 — ⭐ **and after two large candidates in a row, that is the right shape, not a thin one.**

---

# 9 · FALSIFIER

If lap 9's beat-6 table contains a row that appears in neither §1–§5 nor `767242c`'s lap-9 table, this file's
derivation was wrong and the fix is in the register, not in a wider table here. And **if any row above is called
"ready" at lap 9's beat 6 while the "defined enough when" line beneath it is unmet, this file failed at its one
job** — which is to make that gap visible before the lap opens rather than at its build window.

# 10 · QA

```
ls tools/read-glance-order.py                      # row E's first link — absent at 06c2a16
grep -n "already-has-an-estate" worker/worker.js   # row C's ruled refusal (:1406)
grep -E "^- (stage|ready):" .plans/2026-09-07-weather-card-PLAN.md      # row A's stamp
grep -E "^- (stage|ready):" .plans/2026-09-07-capture-write-path-PLAN.md # row D — concept, no ready
python3 tools/check-backlog-ready.py --ladder      # the rungs these rows sit on
```
