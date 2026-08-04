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
