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
| **3 · INTAKE** | ✅ **Door drained, 2 of 2.** Now reads `inbox clear (2 filed, all handled)`. |
| **4 · VERIFY** | 👤 **PAUL** — three physical checks, batched. Not attempted from paper. |
| **5 · SEASON** | Quiet. 46d to frost; the put-away window opens at 45d, so **the next lap should expect SEASON to fire.** Parts lead time is the gate, not the weather. |
| **6 · RECORD** | 👤 **PAUL'S GATE** — the open rows are in `BACKLOG.md` Track B § FLEET LAP 1. Nothing folded that contradicts him. |
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
