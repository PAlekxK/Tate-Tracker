# FLEET CYCLE — chronicle

Append-only. One section per lap. A lap that has CLOSED says so in its own heading (S4);
a lap still open says that instead. **A heading that says it is not a lap is not one.**

State artifact: `cycle/fleet/cycle-state.json` · map: `CYCLE-MAP.md` beside this file.

---

## Lap 2 — 2026-09-01 · 🔓 **OPEN** — held at beat 4 (Paul, physical) and beat 6 (contended file)

**Fired on: Paul's update, in person.** The probe was **RESTING** — all four signals quiet — so this
lap has a *human* trigger, not a signal one. That is legitimate for this loop (it rests and fires on
a signal; Paul is one), and it is recorded as such rather than dressed up as a probe fire.

⚠️ **The handoff brief was wrong about SEASON, by one day.** It said to *expect SEASON to fire*. It
did not: 2026-09-01 is **46d** to first frost against a 45d window. The brief's own arithmetic put
the window opening **2026-09-02**. The probe was right; the brief was reading a day ahead of itself.

| beat | what happened |
|---|---|
| **0 · BRIEF** | 🔴 **FAILED, THEN FIXED.** Resolved Paul's sentence to **bronco-1989 (61)** over **dr200s-2017 (2)**. Root-caused, fixed, 18 new paired selftests, committed `760f9a5`. See below — this is the lap. |
| **1 · FIELD** | **Not run, correctly.** Conditional: it fires when the record has NO answer to a symptom. The record has a full protocol for this one (`guides/blue-thunder-starting-diagnosis.md`, T1–T6) and FIELD sweep 1 already ran on this exact question. Nothing added to `FIELD-NOTES.md`. |
| **2 · SWEEP** | `fleet_probe.py` → **RESTING**, 4 signals checked, none fired. Map-control selftests PASSED. |
| **3 · INTAKE** | Door clear — `6 filed, all handled`. Nothing new arrived. |
| **4 · VERIFY** | 👤 **IN PROGRESS with Paul today.** He has the bike, a NEXPEAK NC201 PRO charger and an All-Sun EM830 meter in hand. T1 → draw A/B → charge on AGM → T2b → T3 → a clean T4 overnight. **Lap cannot close until these land.** |
| **5 · SEASON** | Quiet at 46d. **The put-away window opens tomorrow, 2026-09-02** — the next lap opens on it. Parts lead time is the gate, not the weather. |
| **6 · RECORD** | ⛔ **BLOCKED, not skipped** — `vehicles.json` is held uncommitted by a concurrent session. See the concurrency section. |
| **7 · AMEND** | One **APPLIED** (the resolver). Three **PROPOSED**, none applied. |

### 🔴 Beat 0 — THE FOUNDING DEFECT RECURRED INSIDE THE CONTROL BUILT TO PREVENT IT

Paul's verbatim update — *"after charging the 200 for a good amount and then left it overnight…
it just wound up clicking"* — resolved to **bronco-1989**, score **61**, against **dr200s-2017** at
**2**. The right machine placed **last of eight**, and the tool **did not refuse**, because it was
never a tie.

This loop exists because a session read the wrong *manual* and confidently told Paul to kick-start a
bike with no kickstarter. `CYCLE-MAP.md` says beat 0 is *"a script, not a discipline"* precisely so
that cannot recur. **It recurred, in the script.**

**Three compounding bugs, all one shape:**

1. ⭐ **`str()` ON A CONTAINER.** The haystack was `str(v.get(k) or "")` over six fields, and
   **`doorLabel` is a dict on exactly 1 of 22 machines** — the Bronco. Python stringified it into
   **1,557 characters of English prose** (`'summary'`, `'confidence'`, *"verified — paul read every
   field off the label photo"*, a file path, whole sentences). That one record then won **any**
   dictated query, because `the`/`and`/`a`/`to`/`of`/`not`/`is` were matching a **repr, not a name**
   — 21 such hits, 61 points, **not one of them about a Bronco**.
2. **No stopword filter**, so function words scored as identity. ⚠️ **Note the direction: the more
   naturally Paul speaks, the worse it got.** He dictates; the tool built to accept *"whatever Paul
   said"* was **maximally vulnerable to how he actually talks**. Terse `"the 200"` scored 3–2; his
   real sentence scored 61–2.
3. **It could not refuse.** *"Refuses on a tie"* was an exact-equality test, so 61 vs 2 sailed
   through with no margin test at all.

**Fixed:** strings-only haystack (a non-string field is skipped and REPORTED); `STOPWORDS` plus
`STOPWORD_COLLISIONS` as a **closed set** — a stopword that is also a real name token (`turn` in
*Zero-Turn*, `i` in *"i-30 Starter"*) must be **declared with a reason** or `--selftest` fails;
strong (id/name/nickname) vs weak (trim/category) grading, because symptom vocabulary lands in
description — `start` is a substring of the CS-352's trim; digit-bearing tokens graded as strongly as
names, since **a model designation is the one reliable signal in loose speech**; model **years**
whole-token-matchable but never substring-matchable (`"the 200"` was otherwise a 3-way tie against
2001/2005/2006); and a `MIN_SCORE` floor so a lone 1-point hit refuses (`"it won't start"` → a
chainsaw) instead of answering.

⭐⭐ **THIS ANSWERS LAP 1'S PRE-REGISTERED QUESTION ③** — *"is beat 0's resolution good enough on
Paul's real speech, or does it need aliases?"* **Lap 1 recorded its metric as met and closed.** But
it never ran beat 0 on his speech — it ran `--check` across documents. The existing test,
`resolve("the 200 blue thunder")`, passes **only because the machine's name is in the query.** His
real sentence contained no name at all. *A pre-registered question can be carried forward unanswered
while the lap that owned it reads green.*

### 🚨 CONCURRENCY — a second session is live in this repo, and the guard is half-blind to it

Paul, mid-lap: *"There's another session right now looking at the refrigerator."* Verified: `3f52e5b`
(Track A, the feedback reader) landed **between** this lap's guard start and its commit, and five
files are held uncommitted — **`vehicles.json`**, `viewer.html`, `worker/digest.json`,
`RELEASE_NOTES.md`, `arrival-dispositions.json`.

- ✅ **The commit was clean.** `760f9a5` staged an **explicit path**, so it did not sweep their work
  — [[feedback_git_add_all_in_shared_repo]] honoured.
- ⭐ **NEAR-MISS.** `check-data-inline.py` flagged `refrigerator-lg-bottom-freezer` as canon-ahead
  drift. **`--fix` would have re-inlined their half-finished record into `viewer.html`, the publicly
  served file, mid-edit.** Paul's standing rule (surface drift, never auto-fix) held — and it paid
  off for a reason it was **not** written for.
- 🐛 **DEFECT · the guard watches HEAD and not the working tree.** `verdict()` compares shas only
  (`moved = now != mark["sha"]`). `repo_state()` **does** compute `dirty_files` — and **only
  `mom-cycle-status.py` reads it, to display a board signal.** The guard's own check path never
  consults it. *The check exists and has no caller.* It fired today only because the other session
  also **committed**; had they merely been editing, it would have said CLEAR over a contended
  `vehicles.json`. Its own docstring says the lap-4 failure *"was caught only because the remote
  happened to have moved too"* — **it is still relying on a coincidence, just a different one.**
- 🐛 **DEFECT · the concurrency guard is not concurrency-safe.** `.private/cycle-guard-state.json` is
  **one flat document with a single `start` slot** and no namespacing by lap or track (`"lap": null`,
  never set). Fernwood runs **two loops in one repo by design** (D41), so concurrent laps are the
  architecture, not the exception — and the second `start` silently overwrites the first, leaving a
  lap measuring from another lap's baseline.
- ⚠️ **Process error, mine:** I committed with bare `git commit`, so the guard reported **my own
  commit as a foreign incursion**. `guard-concurrent.py commit` is the intended path (check → commit
  → record, no window). Corrected with `record-commit`. **The handoff brief names `start` and no
  other guard subcommand** — that is a gap in the brief, not just in the operator.

⛔ **Nothing in `guard-concurrent.py` was fixed this lap, deliberately.** The other session is
actively invoking it. Editing a shared tool mid-flight is the exact failure the finding describes.

### 👤 Beat 4 — what Paul is running, and what the update already changed

⭐ **His update breaks the record's own pattern.** Every prior episode had *charging restores
starting*, which is why the record read this as charge **state**. A full charge that does not survive
one night is a different claim: **the battery is not holding, or something drained it.** It is an
**uninstrumented T4 failure** — and the clean T4 for that night is gone, because it was cranked
repeatedly before any reading.

✅ **One named gap CLOSED:** the 8/30 results-log row said *"charger make/model not yet recorded —
read the label."* It is a **NEXPEAK NC201 PRO**, a 7-stage smart charger with AGM/GEL and pulse-repair
modes — **not** the dumb trickle charger the back-feed hypothesis assumed. ⚠️ `[photo-MODEL-READ,
unverified]`, and it **weakens that hypothesis without excluding it**; T5's A/B settles it by
measurement. Paul's own read is hedged — *"I don't think the bike was plugged into the charger."*

⛔ **T5 AS WRITTEN CANNOT BE RUN ON THE METER HE OWNS** (All-Sun EM830, `[photo-MODEL-READ]`). The
guide said *"meter on 10 A DC"*; that range resolves in **~10 mA steps** against a **5–10 mA**
threshold, so it would read `0.00` and **look like a valid measurement while being unable to see the
answer** — and its 10 A jack is rated 10 s max. Caveat folded into the guide: use `VΩmA` on `200m`
or `20m`. **Third instance of one defect shape in a single lap** — the manual, the resolver, the
meter: *match the payload, not the container.*

### Beat 7 · AMEND — 1 applied, 3 proposed

**Applied:** the beat-0 resolver (above), with 18 paired selftests.

**Proposed, Paul rules — none applied:**
1. ⭐ **The guard must read the WORKING TREE, not just HEAD.** The data already exists in
   `repo_state()['dirty_files']` and has no caller in the check path. Cheapest real fix on the board.
2. ⭐ **Namespace the guard state per track** (`fleet` / `mom`), so two concurrent laps cannot
   overwrite each other's `start`. The `"lap"` field is already there and unused.
3. **Beat 0 should be able to say *"I am not confident"* out loud in the brief**, not only refuse.
   Today it either prints a full confident card or bails; a resolution at bare margin prints the same
   as one at 22 points.
4. **`--selftest` should carry a DICTATED query for every machine**, not one tidy phrase. Every
   existing resolution case names the machine; that is the hole this lap fell through.
5. **The guard has no ACKNOWLEDGED state, so a legitimate concurrent commit cannot pass it.**
   `cmd_commit` returns `MOVED` and refuses whenever HEAD moved, with no flag to record *"I checked,
   the commits are the other track's, my paths do not overlap, and I am performing no history
   operation."* So the correct behaviour today — confirm with Paul, then commit explicit paths — has
   to route **around** the guard (`git commit` + `record-commit`), which is precisely the bare-commit
   path that produced this lap's own process error. ⚠️ **A control with no legitimate path through it
   trains people to step around it** — the N8 · COSTLY CONTROL shape the map already warns about.

**Pre-registered for the next lap:** ① does SEASON fire on 09-02 as computed, and is 45d the right
window once parts lead time is real? ② does the fixed resolver survive Paul's *next* unrehearsed
sentence — one measurement is not a fix. ③ do T1/T2b/T3 actually discriminate, or does the bike start
fine and strand the protocol untested again?

---

## Lap 1 — 2026-09-01 · ✅ **CLOSED** — the first lap this loop has ever run, and the first it has ever closed

**Declared 2026-08-30. `lap_count` was 0 for two days while the probe read FIRED.** Run unattended
at Paul's instruction — *"I'm gonna step away, and you can work through as much of the queue as
possible."*

**Fired on:** `INBOX` (2) · `PROVENANCE` (6) · `STALE-OPEN` (3). SEASON quiet — 46d to first frost,
outside the 45d window.

| beat | what happened |
|---|---|
| **0 · BRIEF** | `vehicle-brief.py --check` run across **25 documents / 22 machines**: 4 MISMATCH · 2 NO-OVERLAP · 11 unverifiable · 8 match. Every flag opened and read against the document's own text — see below. `card values sourced to a link: 0`. |
| **1 · FIELD** | **Not run, correctly.** Conditional by design: it fires when the record has no answer to a symptom. No symptom was in play — this lap was provenance and intake. No forum search, nothing added to `FIELD-NOTES.md`. |
| **2 · SWEEP** | `fleet_probe.py`. Reasons read, not just the verdict. |
| **3 · INTAKE** | ✅ **Door drained 2 of 2 at 09:17 — then REOPENED at 09:25** when the mine filed 4 more. All 6 disposed: 1 resolved, 5 routed. Now reads `inbox clear (6 filed, all handled)`. See "Beat 3 REOPENED" below. |
| **4 · VERIFY** | 👤 ✅ **DISPOSED** — 5 of the Bronco items CLOSED by Paul at beat 6, transmission ANSWERED at the truck, emissions **DEFERRED** to `nextLook 2026-10-01`. Nothing answered from paper. |
| **5 · SEASON** | Quiet. 46d to frost; the put-away window opens at 45d, so **the next lap should expect SEASON to fire.** Parts lead time is the gate, not the weather. |
| **6 · RECORD** | 👤 ✅ **RAN 2026-09-01, twice** — Paul ruled: 5 Bolores items CLOSED on a standing rule, transmission ANSWERED at the truck, emissions DEFERRED. P7 cleared by order record. See "Beat 6 RAN" below. |
| **7 · AMEND** | ✅ **APPLIED** — `s4_stale_open` rewritten at Paul's ask: closed-set `state`, `deferred`+`nextLook`, and a printed denominator. 13 new paired selftests. STALE-OPEN now rests. See below. |

### ✅ Beat 3 — the door, both rows disposed

- **GTI 2026-07-21 (photo-organizer)** → **RESOLVED, already in the record.** It is
  `sr-2026-07-21-cone-strike-repair-a` — a traffic cone off a truck ahead, sucked under the car,
  grill + underbody panels repaired in place with washers, zip ties and tape. Not a thin row: it
  carries a linked open item *(underbody/radiator eyeball post-cone-strike)* and a **2026-08-26
  corroboration**, where VW of Marietta quoted both front bumper vents and the card reasons that is
  the strike showing through the in-place repair. ⭐ **The ask was premised on a gap that was not
  there**: the 8/28 `ask-cycle` refusal concerned a *shop visit* with no entry; this date is **DIY
  work and was recorded all along.** The ten photographs are corroboration, not a missing event.
- **Handwritten Bronco parts list (photo-organizer)** → **ROUTED to `BACKLOG.md` Track B, still
  open.** ⛔ Deliberately not transcribed — see P4 there.

### 🔓 Beat 3 REOPENED — 2026-09-01, four more rows, all four routed

**Why it reopened rather than opening a lap 2.** Beat 3 drained the door at **09:17** (2 of 2). At
**09:25** — eight minutes later — the ChatGPT-archive mine filed **four corrections** (commit
`03dc6d1`). `cycle-state.json` was written at 09:17 and so its `why` still read *PROVENANCE,
STALE-OPEN* with no INBOX; the 10:20 handoff brief saw all four rows but labelled the work "lap 2."
Neither was right: **lap 1 never closed.** It is held at beats 4 and 6 on Paul's gates and
`lap_count` is still 0. So the door was drained inside the lap that owns it. Door now reads
`inbox clear (6 filed, all handled)`.

⛔ **Nothing folded as fact.** All four rows are model reads of a chat archive. What this beat could
do deterministically is test each row's claims **about our own record** — and per the standing rule,
*a tool that reads OUR files reports on the RECORD, not the world.* Three claims confirmed, one
reasoning corrected, one thing the mine missed.

| row | disposition | what the check found |
|---|---|---|
| **Water heater** — record vs a 2025 Kenmore photo | **ROUTED** → P6 | Open field `installedHere` is real, 0 serviceHistory. ⭐ **Corrected the mine's own reasoning**: it ranked the 2026 record over the 2025 photo as *"newer and serial-decoded"*, but the card's `_provenance` says it too was **added from photographs**, with the build date decoded from a serial read off a photographed plate. Two model reads, one grade. |
| **GTI spark plugs** — -8 vs -9 | **ROUTED** → P7 | Confirmed: the GTI register holds exactly 2 rows (wipers, coolant tank), **neither is plugs**. No purchase evidence for either heat range. Resolution is physical — pull a plug. The proposed source-line edit is **held as a beat-6 proposal**. |
| **Bronco second window switch** | **ROUTED** → P8 | Confirmed no switch row. ⭐ **The mine missed the adjacent arc**: `2025-10-24 · Dorman 742-251 Power Window Lift Motor · INSTALLED`, seven days after the short and three before the breaker. Sequence is short → **motor** → breaker; the short may have cost a motor too. Cross-linked to P4 (same truck, same era, still unread). |
| **Mower 5/8" rounded bolt** | **ROUTED** → P9 | ⭐ The row this loop exists for. Both mowers: **0 serviceHistory, 0 openMechanicalItems**. TOOLS.md: **0** matches for *extract* — but its own coverage warning means *not yet swept*, not *not owned*. Which mower **not asserted** (bolt size is an inference, and there is no history on either machine to test it against). Joins beat 4. |

**0 resolved, 4 routed.** That is the honest outcome, not a punt: every one of the four turns on
something only Paul can settle — a machine he owns, a purchase only an order number clears, or a
bolt somebody has to go look at. What the beat added is that each now lands on a surface with its
premises **checked** rather than assumed, and P8 and P9 came out of it with more than they went in.

**Beat 4's trip grew.** It was three Bronco checks; it is now three Bronco checks **+ pull a GTI plug
(P7) + look at both mowers' blade and deck bolts (P9)**. Still one trip with a light.

### 👤 Beat 6 RAN — Paul ruled, 2026-09-01. Five Bolores items closed, one answered, one deferred.

**The standing rule** `[paul-stated]`: *"none of these leaks… are current. They've all been replaced or
repaired with the new engines. So if you're flagging old issues for bolores that come from the old
documentation, don't resurface them because they've been resolved."* Folded into
`openMechanicalItems._note` so it governs future laps.

Closed: rear main seal · transfer case leak · valve covers · **frame crack at the steering box** ·
front-end noise. Answered at the truck: **transmission quadrant — *"The P R N D 2 1, that's what I see"***,
which is the three-speed quadrant, so **C6 confirmed physically** and the circumstantial case (door-tag K
+ vacuum modulator + rebuilt-not-swapped) now has its read. Deferred, and the only Bolores item still
open: **emissions hardware** — *"I'll look… next time I'm with Bolores, but I'm not by the truck now."*

⚠️ **The frame crack was flagged once and ruled anyway, and the record says so.** It is a FRAME finding,
not an engine one, so the engine-replacement rationale does not mechanically reach it, and it carried the
record's own strongest warning (F-2, *"THE load-bearing one on a lifted 351"*, *"inspect before trusting
her on the road"*). Paul re-affirmed directly. Recorded with that disagreement visible rather than lost —
he has been under the truck and the record has not.

⚠️ **Provenance stated on every closure:** the owner's read of his own truck, **not** a repair record.
Higher-grade than the shop paperwork it supersedes, and a *different kind* of evidence — so the record
says which it is instead of implying an invoice exists.

### ✅ P7 CLEARED BY ORDER RECORD — a three-year SEQUENCE the mine read as a contradiction

Paul: *"I definitely bought those NGK plugs."* Gmail holds **both** confirmations: **NGK140052**
(2022-10-03, NGK 4654 **R7437-9**, $153.04) and **NGK196860** (2025-03-25, NGK 4901 **R7437-8**, $178.80,
shipped 03-26). His 2025-03-23 *"I previously ordered… R7437-9"* was **true and referred to the 2022
order**; advised against the -9 for daily driving, he bought the **-8** two days later.

⭐ **The record's `R7437-8` was right all along** — upgraded `inferred → verified` with the order number,
the only thing that clears a purchase here. The mine saw one statement and one field and nothing in
between, so a sequence looked like a conflict. ⚠️ Which set is *installed* is still unestablished.

**Beat 3's P9 routed OUT**, at Paul's suggestion: a request for the mower-blade-sharpening **date and
machine** is filed at `photo-organizer/cycle/requests.jsonl`. Date and visible machine only — not a
transcription.

### 🐛 SECOND DEFECT FILED — `s4_stale_open` cannot see a closure

Re-ran the probe after folding five closures. **It did not move.** `s4_stale_open` keys only on
`firstFlagged` and **never reads `status`**, so a closed item still counts as open; the 2026-07-29 exhaust
closure escapes only because its date is under the 60-day threshold — luck, not logic. Second, undated
items are skipped while line 160's comment claims *"the denominator below says so"* — **no denominator is
printed**, which is why the probe reported *3 open checks* while **7** were open (two have prose dates that
fail `fromisoformat`). The skip is deliberate and selftested; the non-disclosure is the defect. Both
**filed in `BACKLOG.md`, proposed not applied** — same posture as lap 7's `--bench`/`--apply` finding.

⚠️ **So STALE-OPEN still reads ⚡ and the lap still cannot rest on it** — not because the checks are open,
but because the instrument cannot see that they closed. *Match the payload, not the container.*

### ✅ Beat 7 AMENDMENT APPLIED — `s4_stale_open` now reads the payload, and a check can REST honestly

Filed as proposed-not-applied earlier this lap; **Paul asked for it** — *"Let's fix the probe. gonna be
able to defer these looks to when I'm back with Beloris and be able to close the lap smoothly."* Three
changes, one commit:

1. ⭐ **`state` is a CLOSED SET — `open | closed | deferred`.** The probe reads that, not prose. An
   unknown value raises `Unknown` rather than defaulting; a missing one means `open`, so the old shape
   still works. This is the doctrine fix, not just the bug fix: sniffing a status string for "✅ CLOSED"
   would have re-created the same silent-wrong failure one layer up. **A closed set makes the mistake
   error instantly.**
2. ⭐ **`deferred` + `nextLook` lets a physical check rest without a schedule masquerading as an
   answer** — beat 7's own lap-1 amendment, now built. It rests until the date and then **FIRES**. A
   `deferred` item with no readable `nextLook` raises `Unknown`: *a deferral that cannot announce its own
   expiry is just a nicer way to forget.*
3. ⭐ **The denominator is printed** — `[N open (M undated, not testable) · C closed · D deferred]`, on
   the fired path AND the rest path. The old comment claimed *"the denominator below says so"* and no
   denominator existed, which is how *"3 open checks"* stood in for seven open items.

**13 new selftest cases, every fire paired with the near-miss that must not fire** — a closed item and
the same item left open · a deferral before and on its date · `Unknown` on a bad state and on an undated
deferral · the denominator counting the undated item rather than dropping it. `--selftest` PASSED;
map-control (`fleet_probe --selftest && vehicle-brief --selftest`) PASSED.

**11 items migrated to explicit state:** 7 closed, 1 deferred, 3 open (the DR200S no-start trio, which
were correctly open all along and now say so).

⏸ **Emissions is deferred to `2026-10-01`** so lap 1 can close without pretending the look happened.
⚠️ **I picked that date, Paul did not** — he said *"next time I'm with Bolores."* It is a placeholder
that fires; move it freely. Worth knowing: **the fall put-away window opens 2026-09-02** (46d → 45d to
frost), which is itself a with-the-truck moment and a natural anchor.

**Result — STALE-OPEN RESTS:** `no open check older than 60d [3 open (0 undated) · 7 closed · 1 deferred]`.

⚡ **PROVENANCE is now the only thing standing between this lap and its close** — P1 Husqvarna
(wrong machine), P2 Homelite (never positively identified), P3 DR200SE-vs-DR200S (one sentence from
Paul). All three are his calls, and the lap declines to ack them for him.

### ✅ LAP CLOSED — 2026-09-01. All four signals RESTING.

```
· SEASON      46d to first frost · outside the 45d window
· INBOX       inbox clear (6 filed, all handled)
· PROVENANCE  6 flagged document(s), all acknowledged
· STALE-OPEN  no open check older than 60d [3 open (0 undated) · 7 closed · 1 deferred]
RESTING — 4 signal(s) checked, none fired.
```

**Beat 6, second sitting — Paul ruled the last three provenance flags:**

- **P3 `dr200s-2017-service` → ACKED. Canonical designation is `DR200S`, ruled.** *"We just have one
  motorcycle. You should have the VIN so you determine what it is. It's 200 SE or 200 S, and make that
  canonical, no confusion."* ⭐ **The answer was already in the record.** The VIN's model-year letter
  `H` = 2017; Suzuki sold this machine in the US as the DR200SE in the earlier generation and as the
  DR200S from 2015. ⚠️ **Grades separated in the ack:** the VIN read is deterministic, but `SH42A`
  spans the SE/S family and does **not** split them — the model *year* does, and that half is
  designation knowledge, not a VIN read. Recorded on the card as `canonicalDesignation`.
- **P1 `husqvarna-mower-yth24v54` → ACKED.** *"We just have our current riding mower for the Husqvarna.
  That's fine."* This answers the flag's substantive half — the worry was never the filename, it was
  *"or Paul has/had a YTH24V54 the record does not know about."* One mower, no other. ⚠️ **The ack
  silences the signal; it does not make the document usable.** A YTH24V54 is a ride-on tractor, the card
  is a Z254F zero-turn — different controls, drivetrain and maintenance. ⛔ Replacing it with a Z254F
  manual is open work.
- **P2 `homelite-blower-vac` → ACKED because the machine is LEAVING SERVICE, not because it was
  identified.** *"It's decommissioned. I don't remember seeing a model number on it."* ⭐ His
  recollection and the card's own `photoEvidence` (*"No model sticker found on the unit"*) agree,
  arrived at independently. Card status set to DECOMMISSIONED, with the never-identified fact stated.

**Beat 4 — DEFERRED, not skipped.** Emissions hardware carries `state: deferred, nextLook: 2026-10-01`.
The lap closes without pretending the look happened, and the probe fires on that date on its own.

**Beat 7 — the amendment was APPLIED this lap, not just proposed** (see above): `s4_stale_open` now
reads a closed-set `state`, supports `deferred`+`nextLook`, and prints its denominator. 13 new paired
selftests.

**Raised at close and NOT this lap's work — the V-series in `BACKLOG.md`:** 8 of 22 machines carry an
identifier across **three** stores that nothing joins; the six vehicle VINs say *"full VIN in private
records"* and **no such record exists** — they are in git history at `4e83137`, on the **public**
`origin/main`, because the mask two minutes later changed the working tree and not history. Paul's own
conclusion — a login-gated surface — is the measured remedy, and it is unscoped by design.

**`lap_count` 0 → 1.** The first closed lap this loop has.

### ⭐ Beat 0 — PROVENANCE went 6 → 3, and the 3 that remain are the real ones

**Acked with reasons (3):** `echo-pb7910t` · `homelite-trimmer` · `g22a-2005-ax2` — each reason
states what was compared *and its residual limit* (the G22 ack explicitly does **not** cover values
that differ between G22A gas and G22E electric).

**NOT acked (3), and two are substantive:**
- ⛔ **`husqvarna-mower-yth24v54` is the wrong MACHINE** — a **ride-on lawn tractor** manual filed
  against a **zero-turn**. Read from the document itself: *"Safe Operation Practices for Ride-O[n]"*,
  *"Operator's Manual … YTH24V54"*.
- ⛔ **`homelite-blower-vac` is the wrong MODEL FAMILY** — doc names `UT26HBV`; the card's own
  `photoEvidence` best-guess is the `UT09521 / UT09565` family. The machine has never been positively
  identified.
- ❓ **`dr200s-2017-service` names DR200SE, card is DR200S.** Plausibly the same machine — **this lap
  declined to assert it.** Paul settles it in a sentence.

⭐ **This is the check earning its keep on its first real run.** Its own header warns that
*"unverifiable is NOT a pass — a sparse scan and a correct document look identical."* Two of the six
flags were genuinely wrong documents; four were cosmetic. **A lap that acked all six to clear the
board would have silenced exactly the finding the check exists for.**

### Beat 7 · AMEND — pre-registered before the lap, honoured after

**Pre-registered metric:** *does a lap move `lap_count` off 0 and leave the board legible?* → **yes**;
INBOX cleared, PROVENANCE 6 → 3 with every remaining flag substantive.

**Amendments proposed from what this lap actually showed — Paul rules, none applied:**

1. ⭐ **PROVENANCE should distinguish COSMETIC from WRONG-MACHINE.** Today one signal covers
   "PB-7910 vs PB-7910T" and "a lawn-tractor manual on a zero-turn." Those are not the same finding
   and a count of six told you nothing about which you had. **Proposal:** grade the mismatch (suffix
   / family / different-machine) so the probe line says *"1 different-machine, 2 family, 3 suffix"*.
   The data to do it is already in the check.
2. **STALE-OPEN cannot be discharged by a lap and will fire every lap until Paul is under the
   truck.** Three Bronco items are past 60d. It is honest, but a signal that cannot rest makes the
   board read FIRED permanently. **Proposal:** let a physical check be *scheduled* (a dated
   next-look) so it rests until that date — without letting a schedule masquerade as an answer.
3. **SEASON is 1 day outside its window** (46d vs 45d). Next lap will almost certainly open on it.

---

## 2026-08-30 — LOOP DECLARED, no lap has run

`paul-decided`. The loop was declared today and its machinery built and tested; **lap 1 has
not run.** `lap_count: 0`, and the state artifact says so rather than claiming a closed lap.

**What exists now:** `CYCLE-MAP.md` (8 beats, gate at 6), `tools/fleet_probe.py` (4 signals,
all proven both ways), `tools/vehicle-brief.py` (beat 0, proven against the failure that
prompted it), and this chronicle.

**What prompted it** — the DR200SE manual and a kickstarter that does not exist. Full account
in the map's *Why this loop exists*, and in `guides/blue-thunder-starting-diagnosis.md`.

**Probe on the day of declaration:** `FIRED — INBOX, PROVENANCE, STALE-OPEN` (SEASON resting
at 48 days). So lap 1 has a real, un-manufactured agenda: 2 inbound rows from
photo-organizer, 6 flagged manuals, 3 Bronco physical checks past 60 days.

**⚡ AMENDED THE SAME DAY, before lap 1 — the FIELD beat** `paul-stated`: *"it's important to
also get kind of third-party forum takes, which can be kind of dangerous… that information may
need to be sequestered and treated differently than the user's manual."* Added as **beat 1 ·
FIELD (conditional)**, with `cycle/fleet/FIELD-NOTES.md` as the quarantine and a mechanical
guard in `vehicle-brief.py --check` (a card value's `source` may never be a URL — **0 findings
on the fleet today**, which is the point: fitted before the problem). Tiers were NOT invented —
`A/B/C` were promoted from the Bolores `SOURCES.md` to the fleet standard, carrying its rule
that *a C never silently becomes an A*. The beats renumbered 0–7; the gate moved to **beat 6**.

**Pre-registered for lap 1** (S6/amendment 3 — mandatory to attempt, conditional to produce):
① do the four thresholds survive contact, or is 45d/60d wrong? ② does PROVENANCE actually go
quiet after one review pass, or is the ack file a permanent snooze button? ③ is beat 0's
resolution good enough on Paul's real speech, or does it need aliases? ④ **does the FIELD beat
earn its place** — does a forum sweep on the Blue Thunder charging question produce a hypothesis
with a test attached, or only noise? Blue Thunder is the natural first subject.

⚠️ **NOT a lap.** Do not count this section as one.
