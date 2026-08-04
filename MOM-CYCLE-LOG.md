# MOM-CYCLE LOG — the lap chronicle

One section per lap, **written as the lap runs**, every line pointing at something durable. This is
the evidence half of `MOM-CYCLE-MAP.md`: the map says what the loop *is*, this says what it *did*.

A log written afterwards is a story. A log written at each leg's completion is a record — and the
difference is why the other repo's 63 KB pickup-point had to be archived.

**Scoring uses the pre-registered clean-lap definition in `MOM-CYCLE-MAP.md`.** It may not be
amended mid-lap.

---

## Lap 1 — 2026-08-04 · ⏸ OPEN, standing at leg 6

**Trigger:** Paul, after confirming Mom's 08-03 visit in the data — *"let's run our feedback loop,
take care of the things waiting on me."*

| leg | what happened | artifact |
|---|---|---|
| **0 · GUARD** | HEAD `b5a596c`, working tree clean at start. No concurrent session. | `git log --oneline -1` |
| **1 · READ** | Five checks run. `check-cards` 🔴 1 contradiction · `check-mom-ack` 🟡 R1 4d, 🔴 R2b two channels unread · `check-data-inline` ✅ 10/10 in sync · `check-digest-fresh` ✅ · `read-mom-feedback` 1 new answer, 0 ready to fold. | tool output, this table |
| **2 · TRIAGE** | Two items. **(a)** `q-top-categories` answered 08-03 but still served → *preference*, settled, needs retirement. **(b)** ribbon does not cover her 08-03 session → *return leg owed*. Neither is a correctness bug; canon is clean. | — |
| **3 · RESOLVE** 👤 | One genuine ambiguity, routed to **tier 2 (Paul)**, not to a card: *does "tabs across the top" mean the nav strip that shipped, or a re-organization of the app into her five categories?* Tier 1 could not settle it — telemetry shows she has never tapped the strip (`jumpstrip_tapped` = 0 from `d-szqlt0h7`), which is consistent with both readings. **Spending a card on this would have been the ladder failing.** | funnel query; the question is put to Paul in-conversation |
| **4 · EXPERT** | **No seat convened, deliberately.** Both items are execution, and the one interpretive question routed to tier 2, where it is free. Recording the reason because an unexplained skipped leg is indistinguishable from a forgotten one. | this line |
| **5 · SHIP** | Two channel read-attestations (`observations`, `guru`) — her 08-03 Almanac conversation on creeping-fig cuttings was **actually read**, not stamped. Meta work: the map, the status surface, this chronicle, the map control. | `.private/channel-read-state.json`; commits below |
| **6 · GATE** 👤 | **⏸ HERE.** Ribbon draft + card retirement presented to Paul as exact text. Nothing applied, nothing pushed. | pending |
| **7 · CLOSE** | not reached | — |

### What the lap found that it was not looking for

- **`creeping-fig` propagate: canon and the Almanac agree, and the look-for fired correctly.** The
  08-03 session offered `plant:creeping-fig|propagate` and she then asked the Almanac about
  cuttings. Canon's `peakDates` are 08-01 → 09-10 and its August `seasonNotes` line says take
  cuttings as insurance; the Almanac answered "August or early September." **The loop worked
  end-to-end and nobody had checked that it did.**
- **A defect I reported to myself and withdrew.** `care.propagate.months = [6, 7]` read as June/July
  against an August peak window — until the schema note showed `months` is **0-indexed** (`0=Jan`),
  making it July/August. Correct as written. Logged because a near-miss on a plant she had just
  asked about is exactly the shape of a real one, and `check-season-notes.py` had already returned
  clean on it — the tool was right and the reader was wrong.

### ⚠️ The double-check found a control that had gone dead

Paul asked for a verification pass **after** the lap, not just inside it. It paid immediately:
`test-feedback-cycle.py` was **RED, and had been since 2026-08-03** — one day, caught early.

- **What it asserted:** the confirm carousel's `prev` / `next` arrows both capture drafts before
  re-rendering (`>= 2` handlers, matched by NAME).
- **What is true:** commit `05db30a` (2026-08-03, the folded-receipt / one-question view)
  deliberately replaced the carousel with a single *"Another question ›"* control — **and that
  control is correctly guarded** (`viewer.html:11410`, `captureDrafts()` before `render()`).
- **So the invariant held the whole time; the test was asserting a retired UI shape.** Verified
  against git: 0 `prev`/`next` handlers at `05db30a`, 2 at its parent `6c5d462`.

**Why this is worth more than the fix.** A control that fails for a reason nobody can act on is
worse than no control — everyone correctly learns to ignore it, and the red line still *looks* like
a gate. That is the market-digest staleness ratchet's pathology in miniature, and this one was
caught at one day old instead of weeks.

**Fixed by asserting the invariant instead of the widget:** *any* click handler that calls
`render()` must call `captureDrafts()` first, whatever it is named, `>= 1`. The next redesign that
renames the control will not re-break it. Negative-controlled before adoption — an injected
unguarded handler FAILS, an empty queue FAILS, the real file PASSES.

### Decisions

Every lap records what it **decided**, what that **supersedes**, and **why now** — the record that
lets a later lap tell a trajectory from a flip-flop `[paul-stated 2026-08-04]`. Enforced as a record
shape by `check-cycle-map.py`; it checks that the block exists, never whether the trajectory is good.

| # | decision | supersedes | why now | evidence |
|---|---|---|---|---|
| D1 | **Reorganize the top nav around Mom's five categories** (vehicles · equipment · household systems · gardening · wildlife) | the 2026-08-02 hand-picked strip (Almanac · Weather · Plants · Wildlife · Mama's Perspective), whose own code comment called the five a PLACEHOLDER | she confirmed the list herself 08-03 ("That's all of them"), so the input the placeholder was waiting on has arrived | `q-top-categories` answer; `BACKLOG` ② |
| D2 | **Ship the reorganization now, ahead of the 8/10 rationalization** | the 08-02 freeze — *"nothing here ships early; tonight's surface gets clean air for the window's final week"* | Paul's call 08-04. ⚠️ **This IS a reversal of his own two-day-old decision, and it is recorded as one** — the freeze existed to protect a clean measurement window, and shipping into that window means the 8/10 funnel read cannot be pooled across the change line | Paul, this session |
| D3 | **Split Machines into Vehicles + Equipment**, filtering the record-level `group` field | one "Machines" card — a third word neither Mom nor Paul used | her split already exists in the data as a declared field (7 `vehicle` / 9 `equipment`), so this is a display change, not a migration | `vehicles.json`; verified |
| D4 | **Keep Weather in the strip** `[paul-stated 08-04]` | the domains-only rule the researcher recommended | Paul: *"weather is important"* — and the ack will say we made that call and it can change. ⭐ **The counter-argument was then REFUTED on fact** (below), so this is no longer a preference overriding an analysis; the analysis was wrong | Paul, this session; DOM verified |
| D5 | **Adopt her coined term "household systems"** | the card's shortened "house systems" | *adopt her words, never improve them*; CLAUDE.md already records shortening this exact term as a past violation | `BACKLOG:363`; Paul confirmed |
| D6 | **Leg 4 becomes a scoped expert sequence** | *"one seat by default"* `[paul-stated 2026-07-29]` | Paul's 08-04 call. Recorded as a reversal of a Paul-stated rule, with the 4-lens week as the named cost and a latency guard against repeating it. **Effective lap 2** | `MOM-CYCLE-MAP.md` § Leg 4 |
| D7 | **Seed Household Systems with the record we already have** (Nest thermostat, propane forced-air heat, electric cooling) `[paul-stated 08-04]` | the empty-card plan | `devices.json` already holds a real, deterministically-sourced record — the domain was never empty, so an empty card would have been a fabricated blank | `devices.json`; verified |
| D8 | **Keep an AUTHORSHIP affordance on that card, not adjudication only** `[paul-stated 08-04]` | the researcher's pure-adjudication recommendation | Paul: *"she's still warming up to her feedback and adjudication role, so let's not not give her the opportunity to provide authorship-level input."* Seeding gives her something to react to; it must not become a ceiling on what she can add | Paul, this session |

**Two of these reverse a prior Paul decision (D2, D6); two reverse a researcher recommendation
(D4, D8).** That is not a problem — it is the record working. The failure this table exists to
prevent is reversing something *without noticing*.

### ⚠️ A seat's finding was tagged `validated` and was false

The `user-researcher` pass argued domains-only on the premise that **"Weather is card #1, directly
beneath the strip… access cost of dropping it is zero,"** tagged `[validated — structure]`.

**It is not.** Verified against the DOM: `unified-input` (5983) → jump strip (6003) → **Almanac card
(6026)** → **Mama's Perspective envelope (6090)** → `card-weather` (6164). Weather is the **third**
major block, below two substantial ones — which is exactly where Paul said it was, from memory,
before anyone checked. (Honest nuance: the MP envelope collapses, so the distance varies; Weather is
never the first thing under the strip.)

**Two things follow, and the second is the durable one:**
1. D4 is no longer a preference overriding an analysis — the analysis was wrong, and keeping Weather
   is now the better-supported call.
2. **`validated` is a claim about provenance, not a guarantee of truth.** The tag was applied to a
   structural read that a two-second `grep` refutes. The seat did excellent work elsewhere in the
   same pass (`devices.json`, the `group` field, the `Machines` title, the impression-event gap —
   all four independently confirmed), which is precisely why one false `validated` is dangerous: it
   travels on the credibility of the true ones. **Spot-check a seat's load-bearing structural claims
   before acting on them**, the same standing rule this repo already carries for BACKLOG rows.

### Score against the pre-registered definition — **NOT CLEAN (yet)**

| # | criterion | lap 1 |
|---|---|---|
| 1 | every leg left an artifact | ✅ so far |
| 2 | legs 1, 6, 7 non-empty | ⏸ 6 open, 7 not reached |
| 3 | nothing served that she answered | ❌ **NOT MET** — `q-top-categories` still active |
| 4 | every newer-than-mark channel attested read | ✅ observations + guru attested 08-04 |
| 5 | the return leg shipped | ❌ **NOT MET** — at Paul's gate, unpushed |
| 6 | watermark stepped over nothing | ✅ clamp held; the reflective card is holding it, correctly |

**This is the definition doing its job.** It was written before it was scored, and it came back with
two ❌ on the very lap that authored it. A clean-lap definition that congratulated its own lap would
have been worthless.

### Meta work shipped this lap

- `MOM-CYCLE-MAP.md` — the loop's formal definition, to the definable-loop standard.
- `tools/mom-cycle-status.py` — the glanceable, non-AI status surface.
- `tools/check-cycle-map.py` — the map's own staleness control. **Caught a real gap on its first
  real run** (this file did not exist), and `--selftest` proves it can fail rather than asserting it.
- This chronicle.
- `tools/test-feedback-cycle.py` — the DRAFT leg de-coupled from a retired widget (see above).
