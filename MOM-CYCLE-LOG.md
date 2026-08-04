# MOM-CYCLE LOG — the lap chronicle

One section per lap, **written as the lap runs**, every line pointing at something durable. This is
the evidence half of `MOM-CYCLE-MAP.md`: the map says what the loop *is*, this says what it *did*.

A log written afterwards is a story. A log written at each leg's completion is a record — and the
difference is why the other repo's 63 KB pickup-point had to be archived.

**Scoring uses the pre-registered clean-lap definition in `MOM-CYCLE-MAP.md`.** It may not be
amended mid-lap.

---

## Lap 1 — 2026-08-04 · ✅ CLOSED — shipped `8718f46`, pushed and verified live

**Trigger:** Paul, after confirming Mom's 08-03 visit in the data — *"let's run our feedback loop,
take care of the things waiting on me."*

| leg | what happened | artifact |
|---|---|---|
| **0 · GUARD** | HEAD `b5a596c`, working tree clean at start. No concurrent session. | `git log --oneline -1` |
| **1 · READ** | Five checks run. `check-cards` 🔴 1 contradiction · `check-mom-ack` 🟡 R1 4d, 🔴 R2b two channels unread · `check-data-inline` ✅ 10/10 in sync · `check-digest-fresh` ✅ · `read-mom-feedback` 1 new answer, 0 ready to fold. | tool output, this table |
| **2 · TRIAGE** | Two items. **(a)** `q-top-categories` answered 08-03 but still served → *preference*, settled, needs retirement. **(b)** ribbon does not cover her 08-03 session → *return leg owed*. Neither is a correctness bug; canon is clean. | — |
| **3 · RESOLVE** 👤 | One genuine ambiguity, routed to **tier 2 (Paul)**, not to a card: *does "tabs across the top" mean the nav strip that shipped, or a re-organization of the app into her five categories?* Tier 1 could not settle it — and ⛔ **the reason recorded here at the time was WRONG**: it said *"telemetry shows she has never tapped the strip"*, which treats an unmeasured zero as a measured one. Corrected same day (see below). **Spending a card on this would have been the ladder failing.** | funnel query; the question is put to Paul in-conversation |
| **4 · EXPERT** | **No seat convened, deliberately.** Both items are execution, and the one interpretive question routed to tier 2, where it is free. Recording the reason because an unexplained skipped leg is indistinguishable from a forgotten one. | this line |
| **5 · SHIP** | Two channel read-attestations (`observations`, `guru`) — her 08-03 Almanac conversation on creeping-fig cuttings was **actually read**, not stamped. Meta work: the map, the status surface, this chronicle, the map control. | `.private/channel-read-state.json`; commits below |
| **6 · GATE** 👤 | **6a PREVIEW** — served at `localhost:8765`, Paul flipped through it and caught two errors from the page itself (the "your five" count over six tabs; the collapsed feedback notes). **6b TELEMETRY** — built mid-lap after his question, found 23 never-fired events. **6c PROXY** — SKIPPED, named (D14). **6d** — all three seats ran, Paul approved, **pushed**. | `8718f46`; verified live by unauthenticated fetch |
| **7 · CLOSE** | `q-top-categories` retired · watermark advanced (only after the ribbon actually shipped) · Worker deployed `fc7aea9b` · all seven checks green · `mom-cycle-status.py` reads 🟢 | this file |

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
| D9 | **`vehicles.json` stays the single home for household systems; do NOT wire `devices.json` as a second one** | the researcher's prerequisite ("declare `device` in `momlib.DOMAINS`, inline `DEVICES_DATA`"), which I had already implemented and then REVERTED | `renderVehicles()` already declares `group: 'household-system'` with the label "Household systems" — her taxonomy is built. A second home would entrench a single-source-of-truth violation on the domain she proposed | viewer.html:13026; `VEHICLES_DATA._comment` |
| D8 | **Keep an AUTHORSHIP affordance on that card, not adjudication only** `[paul-stated 08-04]` | the researcher's pure-adjudication recommendation | Paul: *"she's still warming up to her feedback and adjudication role, so let's not not give her the opportunity to provide authorship-level input."* Seeding gives her something to react to; it must not become a ceiling on what she can add | Paul, this session |

| D10 | **Move Vehicles / Equipment / Household Systems OUT of the Reference drawer** | their current home in `#ref-drawer-body` | ⛔ **SHIP-BLOCKER.** `card-vehicles` (6423) is inside `#ref-drawer-body` (6407–6481), which ships `hidden` / `display:none`, and the strip handler never opens the drawer — it only adds `.expanded` and scrolls. Three of her five strip links would scroll to a hidden element and **visibly do nothing.** And the drawer's own label is *"the estate's back pages"*: you cannot promote three of her five categories to the top nav while filing them under back pages | viewer.html:6407/6423/19257; verified |
| D11 | **Drop the per-group item counts** | `groupHeader()`'s `N items` in 10px uppercase | it renders `HOUSEHOLD SYSTEMS · 1 ITEM` beside `9 ITEMS` — a completeness meter that makes her domain read as neglect at the exact moment she is invited into it | viewer.html:13041 |
| D13 | **The jump strip IS what she meant by "tabs"** `[paul-stated 2026-08-04]` | the researcher's open confound — the app has three tab-like controls (plant view tabs, wildlife sub-tabs, the strip), so "I saw the tabs and liked them" could have named any of them | Paul confirmed it directly. **This is Leg 3 tier 2 working exactly as designed** — the ladder said telemetry could not settle it and a card would have spent her attention, so it went to Paul and cost one sentence | Paul, this session |
| D14 | **Lap 1 ships WITHOUT the Leg 6b proxy** | the Leg 6b amendment, which places the proxy before the push | the proxy is designed and not built, and Paul's sequencing is steward → push → the rest. **Named rather than skipped silently** — the clean-lap criterion explicitly permits a seat that "either ran, or the chronicle names why not," and this is that clause being used for the first time. It runs from lap 2 | `MOM-CYCLE-MAP.md` § Leg 6b |
| D12 | **The authorship affordance goes on the CARD, not the confirm queue** | the queue as the default home for any ask | an authorship ask has no `_foldTarget`, so it becomes an unprobeable card that **holds the feedback watermark** until retired by hand — the 2026-07-27 rule this loop already carries. The queue is also capped at 5 with 8 on the bench | `MOM-CYCLE-MAP.md`; ux-expert |

**Two of these reverse a prior Paul decision (D2, D6); two reverse a researcher recommendation
(D4, D8).** That is not a problem — it is the record working. The failure this table exists to
prevent is reversing something *without noticing*.

### ⭐ THE FINDING THAT SHRINKS THE WORK: her taxonomy is already built

`renderVehicles()` (viewer.html:13026) has carried an explicit three-way split since before any of
this, in a declared order, **using her words as the labels**:

```
{ key: 'vehicle',          label: 'Vehicles' },
{ key: 'equipment',        label: 'Yard equipment' },
{ key: 'household-system', label: 'Household systems' },
```

and `VEHICLES_DATA._comment` says so out loud: *"Holds THREE groups, not just vehicles… Renders as
the **Machines** card (Vehicles · Yard equipment · Household systems)."*

**So three of her five categories are already the card's three sections.** What is actually wrong is
narrower than a rebuild:
1. the card is **titled "Machines"** — a fourth word neither she nor Paul used, and it hides the
   structure underneath it;
2. the **Household systems section renders nothing** (`if (!rows.length) return;`) because **zero**
   records carry `group: 'household-system'`;
3. its one real record — the Nest thermostat, propane forced-air heat — sits in **`devices.json`**,
   a file referenced by nothing but `check-domains.py`.

**A near-miss worth recording.** Acting on the researcher's prerequisite, I declared a `device`
domain in `momlib.DOMAINS` and was about to inline `DEVICES_DATA` — which would have made
`devices.json` a **second permanent home** for the domain Mom herself proposed, against
[[feedback_single_source_of_truth]]. `check-domains.py` failed on it immediately (`viewer.html has no
const DEVICES_DATA`), which is what sent me to read `renderVehicles()` and find the existing split.
**Reverted.** The check did not catch the SSOT problem — it caught an inconsistency that made me
look, which is most of what a check is for.

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

### ⛔ THE ZERO WAS UNMEASURED, AND I REPORTED IT TWICE AS A FINDING

**Paul's question, unprompted, at the end of the lap:** *"Zero taps — truly, because there were zero
taps, or because we didn't have telemetry for it?"*

The record answers it, and the answer overturns something this lap leaned on twice:

| the three events instrumented 08-02 22:58 ET (`bbf764a`) | first-ever firing |
|---|---|
| `jumpstrip_tapped` | **2026-08-04T00:02:55Z** — i.e. 08-03 **8:02 PM ET** |
| `mp_envelope_toggled` | **NEVER** |
| `composer_empty_tap` | **NEVER** |

**Her only session since the strip shipped was 08-03 at 7:52 AM ET — twelve hours EARLIER than the
earliest proof that any of that commit's code has ever run.** So *she did not tap the strip* is
indistinguishable from *nothing could have recorded it if she had*. The zero carries no information.

**What I actually did wrong, which is worse than the fact.** I checked the deploy timing early in the
lap, could not verify it (no `gh` on this machine), and correctly said so once — then went on to
state the zero as a finding in `BACKLOG.md` and again in this log, with the caveat quietly dropped
both times. **A caveat that survives only in the sentence where it was born is not a caveat.**
[[feedback_absence_of_records_is_weak_evidence]] is a standing rule in this stack and it did not fire,
because the searched-negative got promoted one restatement at a time.

**It did not change what shipped** — the rebuild rests on her confirmed category list, not on the
zero — and the impression event shipped *because* the gap was real. But the qualifier it was used
for (*"she likes seeing it, NOT that she navigates with it"*) had no evidence under it.

⭐ **And it makes `jumpstrip_viewed` load-bearing rather than nice-to-have.** With a denominator,
`viewed > 0, tapped 0` becomes a real finding and `viewed 0` correctly says nothing.

### Seat measurement — the D6 experiment's first data (informational; D6 scores from lap 2)

| seat | position | changed the artifact? | overturned an earlier seat? |
|---|---|---|---|
| `user-researcher` | 1 | **YES, materially** — found `devices.json`, the record-level `group` field, the "Machines" title, and the impression-event gap. All four independently confirmed | n/a |
| `ux-expert` | 2 | **YES, and caught a ship-blocker** — the drawer (D10), the tap-band overlap on wrap, the counts (D11), the watermark trap in the authorship ask (D12) | **corrected the researcher's Weather premise** (which I had already refuted independently) |

**Two flags fired between seats, and one of them was wrong.** ux-expert flagged my `card_expanded`
citation as a retracted figure — it conflated it with the persona's retracted *"Plants and Weather
most-viewed, 60 views each"* line, a different claim at a different grain. **Re-derived from
`/api/metrics` rather than argued: 4 `card_expanded` across 15 sessions / 10 distinct days on her
device, 07-05→08-04. The figure holds exactly.** (Incidental finding worth keeping: the four were
`card-candidates`, `card-weeds`, and `card-fieldnotes` ×2 — **she has never expanded the vehicles
card once**, which is what D10 predicts of a card buried in a drawer.)

**The early read on the sequence, stated as a read and not a result:** both seats changed the
artifact, the second caught something the first missed *and* something I missed, and the one
cross-seat flag that was wrong was cheap to settle by re-deriving instead of debating. That is the
sequence behaving as designed. It is n=1 and proves nothing yet — D6's rules need three laps.

### Score against the pre-registered definition — **NOT CLEAN (yet)**

| # | criterion | lap 1 |
|---|---|---|
| 1 | every leg left an artifact | ✅ |
| 2 | legs 1, 6, 7 non-empty | ✅ all three ran |
| 3 | nothing served that she answered | ✅ retired; `check-cards.py` exits 0 |
| 4 | every newer-than-mark channel attested read | ✅ observations + guru attested 08-04 |
| 5 | the return leg shipped | ✅ `8718f46` on `origin/main`; the new copy verified in the PUBLIC file by unauthenticated fetch |
| 6 | watermark stepped over nothing | ✅ clamp held; the reflective card is holding it, correctly |

**CLEAN — 6/6.** But the reading that matters is the one from earlier in the same lap: written before
it was scored, this definition came back **2/6 down** on the lap that authored it, and both ❌ named
real unfinished work (a card still being served to her; an unshipped ribbon). It scored clean only
after both were actually fixed. A definition that had congratulated its own lap would have been
worthless, and this one demonstrably could not.

⚠️ **And clean still does not mean she felt heard.** Six green criteria prove the loop closed its
loops on OUR side. `momack_shown` counts exposure, not receipt. No outcome measure for the return leg
exists — the gap is named in the map and is not papered over by this score.

### Meta work shipped this lap

- `MOM-CYCLE-MAP.md` — the loop's formal definition, to the definable-loop standard.
- `tools/mom-cycle-status.py` — the glanceable, non-AI status surface.
- `tools/check-cycle-map.py` — the map's own staleness control. **Caught a real gap on its first
  real run** (this file did not exist), and `--selftest` proves it can fail rather than asserting it.
- This chronicle.
- `tools/test-feedback-cycle.py` — the DRAFT leg de-coupled from a retired widget (see above).
- `tools/check-telemetry.py` — **an event in the SOURCE is not an event in the RECORD.** Built after
  Paul asked whether the zero taps were real or unmeasured. Wired in as Leg 6b, before any push.
- `tools/read-mom-feedback.py --retire` — retirement as one command with two refusing guards.
- `tools/read-mom-funnel.py` — reads the strip funnel, and prints each event's **first-ever firing**
  beside the count so no reader takes a zero on trust.
- `~/.claude/tools/cycle-docs-check.py` + close-out **C4·cycle** — every documented loop's chronicle
  checked against its repo HEAD.

### What lap 2 inherits

1. **Build Leg 6c**, the Mom-proxy. Designed this lap, skipped this lap (D14).
2. **W12** — 23 never-fired events. Trigger the six on paths that should have run.
3. **The strip now has a denominator.** `jumpstrip_viewed` shipped with this push, so lap 2 is the
   first lap that can say anything at all about whether she uses the tabs. **Do not pool across
   `8718f46`** — before it, both the control and the instrumentation were different.
4. **D6 scores from here.** Three seats ran this lap; the demote/re-order/cost rules need three laps.
