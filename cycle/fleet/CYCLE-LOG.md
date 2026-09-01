# FLEET CYCLE — chronicle

Append-only. One section per lap. A lap that has CLOSED says so in its own heading (S4);
a lap still open says that instead. **A heading that says it is not a lap is not one.**

State artifact: `cycle/fleet/cycle-state.json` · map: `CYCLE-MAP.md` beside this file.

---

## Lap 1 — 2026-09-01 · 🔓 **OPEN at beats 4 + 6 (Paul's gates)** — the first lap this loop has ever run

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
| **4 · VERIFY** | 👤 **PAUL** — three physical checks, batched. Not attempted from paper. |
| **5 · SEASON** | Quiet. 46d to frost; the put-away window opens at 45d, so **the next lap should expect SEASON to fire.** Parts lead time is the gate, not the weather. |
| **6 · RECORD** | 👤 ✅ **RAN 2026-09-01** — Paul ruled: 5 Bolores items CLOSED on a standing rule, transmission ANSWERED at the truck, emissions DEFERRED. P7 cleared by order record. See "Beat 6 RAN" below. |
| **7 · AMEND** | below. |

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
