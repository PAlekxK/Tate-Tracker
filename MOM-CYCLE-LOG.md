# MOM-CYCLE LOG — the lap chronicle

One section per lap, **written as the lap runs**, every line pointing at something durable. This is
the evidence half of `MOM-CYCLE-MAP.md`: the map says what the loop *is*, this says what it *did*.

A log written afterwards is a story. A log written at each leg's completion is a record — and the
difference is why the other repo's 63 KB pickup-point had to be archived.

**Scoring uses the pre-registered clean-lap definition in `MOM-CYCLE-MAP.md`.** It may not be
amended mid-lap.

---

## Interlap note — 2026-08-10 · **no lap ran — and this is the state the loop is supposed to be in**

Third interlap note, and unlike 08-06/08-07 this one is not "the work was meta." A Mom surface
**was** touched. It still was not a lap, and the distinction is the point.

**What the sweep found.** `check-cards.py` flagged `q-fairway-grass-seedheads` as SERVED WITH NO
PHOTO. Verified against the world rather than the checkbox and the flag was right: the card names
two grasses, asks about one, and asked her to judge a feature — digitate seed spikes — with nothing
on screen showing what one looks like. Fixed in `29cc154` (card-level `photo`/`attribution` slot;
`crabgrass` also filled the only weed-photo gap in canon). **Committed, not pushed** — it reaches
her, so leg 6 holds it at Paul's gate. He has seen the rendered card.

**Why this is not lap 3.** A lap disposes of *what Mom gave*. This disposed of a defect *we* found
in what we were asking her, before she ever answered it — leg 5 work (a win that never reaches her)
that happened to surface a leg-6 item. Calling it a lap would let a lap close with her side empty.

**Her side is empty, verified — not assumed.** Zero records carrying her deviceId on **any**
channel since 2026-08-03 (feedback · observations · zone-audio · guru · pending-species, 30-day
window), and zero telemetry events from her device in 14 days. Her active days were 07-26, 07-28,
07-29, 08-03. The 08-09 traffic that lit the board is Paul's own — the Guru turn says so in its own
text.

**The state this leaves the loop in, and Paul's call on it** `[paul-stated 2026-08-10]`:

> *"we've kind of got, at this point, a clean moment with a gate defined that will trigger our whole
> cycle… let's continue to ensure this is documented and structured."*

Lap 2 closed clean, her side is quiet, and the entry condition is now written down rather than
implied — `MOM-CYCLE-MAP.md` § **"What STARTS a lap"**. The loop is **ARMED**: monitoring runs at
every pickup via the session-start block, and **her input is what fires the next lap.** Not a
schedule, not a backlog, not our shipping cadence.

Two things a future reader should not have to reconstruct:
- **`jumpstrip_viewed` still has no post-`8718f46` reading** — carried forward from the 08-06 and
  08-07 notes, still true, and it will stay unmeasured until she opens the app.
- **The board cannot currently tell ARMED from FIRED** (Paul's test taps raise Mom's flags).
  Named in the map and filed as **Tier 1 · 9**. Until it is fixed, a 🔴 on this loop must be read
  against the device, not taken at face value — which is exactly what happened today.

---

## Interlap note — 2026-08-07 · **no lap ran**

Same flag, same answer, second day running. `cycle-docs-check.py` reported *"repo moved 2026-08-07,
newest chronicled lap 2026-08-06."* **It was meta again.** Both 08-07 commits were checked and
neither touches any Mom surface:

- `835e4e2` — `BACKLOG.md` only. A dispatched verification found the Bolores corpus row's four
  "open" legs had closed on 08-05 and nobody updated the row; the row now reads ALL FIVE LEGS
  CLOSED, with the old claim struck rather than deleted.
- `9837ab2` — `manuals/LINKS.md` + `.private/` asset sidecars. Retracts a link-decay figure that
  was **falsified by Paul from memory on 08-05** and re-propagated on 08-06 anyway. Re-probing all
  30 links found one REAL new loss (`sourceresearch.com`, NXDOMAIN) that the inflated number had
  been hiding. `viewer.html` untouched; `.private/` is gitignored.

So **lap 2 is still unstarted** — everything under *"What lap 2 inherits"* stands, and
`jumpstrip_viewed` still has no post-`8718f46` reading.

⚠️ **Two interlap notes in a row is itself a reading.** One is a quiet week; two consecutive days of
repo movement with no lap means the Fernwood *vehicle/manuals* thread is active while the *Mom*
thread is idle. That is a legitimate state — but it is now a fact on the record rather than
something a future reader has to reconstruct from commit archaeology. If a third lands, the
question stops being "did a lap run" and becomes "is lap 2 blocked on something nobody has named."

---

## Interlap note — 2026-08-06 · **no lap ran**

Recorded because `cycle-docs-check.py` (close-out C4·cycle) correctly flagged *"repo moved 08-06,
newest chronicled lap 08-04 — either a lap went unrecorded, or the work was meta and the chronicle
should say so."* **It was meta.** Both 08-06 commits were checked file-by-file and neither touches
any Mom surface:

- `66932b1` (10:49) — `worker/digest.json`, a rebuild stamp from a deploy.
- `9f12147` (14:49) — `BACKLOG.md` only, correcting a **Bolores/vehicle** row that had read open for
  a day after the work shipped. Nothing to do with Mama's Perspective.

So lap 2 is still unstarted and everything under *"What lap 2 inherits"* below stands untouched —
in particular, **`jumpstrip_viewed` still has no post-`8718f46` reading**, because no lap has run to
take one.

⭐ **The note exists so the gap is a stated fact rather than an inference.** An un-updated chronicle
and a loop that did not run are indistinguishable from outside, and the ambiguity resolves in the
flattering direction ([[feedback_hand_maintained_facts_drift]]) — a reader assumes the loop is
healthy and merely under-documented. Writing "no lap ran" costs one paragraph and removes the guess.

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

| D15 | **The acknowledgment card is THE RIBBON, not a change list — and its specific job is ATTRIBUTION** `[paul-stated 2026-08-04]` | the open fork the content-steward named ("decide once, not per-refresh") | Paul: *"the ribbon is intended to be a we-heard-you, because we DO have a changelog / release notes elsewhere in the app. So this top-of-Mama's-Perspective card is about we heard you — but very specific and clear. Not just 'we heard you' but 'we actioned these things because of you. You are driving these changes, and you can go look at them if you want.'"* ✅ **Premise verified:** the app does carry a changelog — the **"Recent updates"** card, rendering the latest five `RELEASE_NOTES_DATA` entries. So the ribbon never has to inform; that job is taken. **Consequences that follow and are now binding:** ① it refreshes on **her** events, never on ours — it goes quiet when she does, and a ribbon that fires on our shipping cadence is a changelog wearing the ribbon's clothes; ② every line must trace to something **she** gave; ③ ⚠️ **the intent is carried by STRUCTURE, not by explaining itself** — Paul: *"we don't wanna add all that wording."* The title *"what your answer changed"* already does the attribution in four words; adding "because of you" anywhere would be the card describing its own purpose to her | Paul, this session; "Recent updates" card verified |
| D16 | **Ratify "Monday, August 3 — what your answer changed:"** `[paul-stated 2026-08-04]` | Paul's own earlier phrasing, "Actioning your feedback from Monday, August 3:" | I overrode his wording on the steward's argument (subject = us, verb = our process) and shipped it flagged as unratified. He has now taken it. **The override becomes his decision rather than my deviation** — which is the only thing that makes it safe to have shipped | Paul, this session |
| D17 | **DO NOT merge Plants + Turf + Weeds into one Gardening card — decide it in lap 2 with data** `[paul-agreed 2026-08-04]` | Paul's own proposal to collapse them | His instinct names something real: her taxonomy has five buckets and the page has six cards for two of them, so matching her meant **splitting** for machines and would mean **merging** here. **The counter is that we split the Machines card TODAY precisely because sections inside a collapsed card are not glance objects** — merging would rebuild the thing we just took apart, on the domain with the most content (36 plants). ⚠️ **And a verified counter-signal:** the Weeds card holds *"the only unprompted praise in project history"* `[validated, .user-research/2026-07-26-feedback-loop-audit.md]` — for being the section that **asks nothing**. That does not block a merge, but it binds wherever that content lands: **put no asks there.** Deferred because the strip now has a denominator for the first time, so lap 2 can see whether she taps Gardening at all and whether she ever reaches Turf or Weeds. **It changes an organizing model → all three seats** | Paul, this session |
| D18 | **Weeds gets its own glyph — 🥀** `[shipped 2026-08-04]` | 🌿 on Plants, Weeds AND the Gardening tab — one mark, three referents | the concrete harm underneath D17, fixable now without deciding the structure. Chosen for a different **shape and colour**, not a different green — a second green sprig would not survive her text size. The tab keeps 🌿 deliberately: a door should wear the mark of the card it opens. ⚠️ **One character, and Paul's to overrule** | W11 |

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

---

## Lap 2 — 2026-08-08 (ET) · ✅ CLOSED — 7/7 clean, **stamped 2026-08-12 after re-verification**

**Shape:** tooling / meta only. **Nothing Mom-facing changed, and no return leg was owed** —
`check-mom-ack` is green on every channel and the ribbon covers through her newest input
(2026-08-03 7:56 AM ET). Per the ribbon's own doctrine it refreshes on HER events, not ours; she
has given none since. Drafting one anyway would have been the changelog-in-the-ribbon's-clothes
failure the doctrine names.

**Leg 4 (expert seats): NONE — and the scoping table is why.** The lap produced no Mom-facing
surface and no copy, which the table routes to "none, and the chronicle says so." Recorded rather
than skipped silently. Clean-lap criterion 7 (effective this lap) is therefore MET by naming it.

| leg | what happened | artifact |
|---|---|---|
| 0 · GUARD | HEAD unmoved, tree clean at start and before each commit | `git log` |
| 1 · READ | full sweep; **work-list EMPTY** — 9 answers all folded/retired/dispositioned, 0 ready to fold, 0 unaddressed notes, 0 channels with uncovered arrivals | tool output |
| 2 · TRIAGE | nothing of hers to route. Every item this lap was OUR instrument | — |
| 3 · RESOLVE | one tier-2 question put to Paul (what does 8/10 decide now?) — **answered: hold the line** | below |
| 4 · EXPERT | none convened — see above | this row |
| 5 · SHIP | three tooling fixes, none reaching her | `49abc62`, `ad7392a`, `99eb648` |
| 6 · GATE | **no return leg owed.** Preview served + PID-verified; telemetry walked | `tools/telemetry-walk.js` |
| 7 · CLOSE | watermark untouched (nothing to advance); `check-cards` exit 0 | tool output |

### What this lap found

1. **`check-mom-ack`'s R3 had gone blind for four days.** The ribbon migrated to `changes[]` on
   08-04; `message` has been `""` since, and `ribbon_state()` never exposed the new fields — so the
   one check asking *"does this name what she actually gave?"* printed an empty string and **could
   not fail**. Fixed, and a blank-rendering ribbon is now a hard failure. Proven able to fail on a
   synthetic empty ribbon before adoption.
2. **The 23 never-fired events were 23 cold paths and ZERO broken wiring.** A call-site sweep of all
   23 found no defect. The undifferentiated list was the problem, not the events;
   `check-telemetry.py` now classifies by reachability.
3. **⛔ `momack_unfolded` is UNREACHABLE in this build** — the "Read the rest ›" fold lives only on
   the legacy prose branch. Confirmed in the DOM, not just by reading: 4 change bullets render,
   **0** `.ack-read-rest`, **0** `.ack-msg-lead`. Note `momack_followed` WAS deliberately re-wired
   into the new branch and survived — so this is a metric that died silently in a migration, which
   is the failure class worth guarding.
4. **A second missing denominator.** `species_id_confirmed`/`_declined` sit downstream of a
   suggestion fence that emits no event, so *"Guru never proposed"* and *"proposed and ignored"* are
   indistinguishable — the same gap `jumpstrip_viewed` was added to close on 08-04. It is a pattern.
5. **The 8/10 window is closing on an unmeasurable question.** Her last session was **08-03**; the
   strip she asked for shipped **08-04**. She has never loaded the build containing the thing 8/10
   was meant to decide. `jumpstrip_viewed`/`_tapped` have fired only from Paul's device.
   **Paul's call: HOLD THE LINE** — close the window as pre-registered, do not extend, do not prompt
   her; then reassess how the cycle runs and how to structure and time each lap.
6. **BACKLOG:402's claim that "the strip does not yet carry her list" was stale.** It was rebuilt
   08-04 (`e58bdde`) and carries her five in her order; the ribbon's claim to her is TRUE on screen.
   So 8/10 no longer decides *which list* — that is settled in favour of hers.

### Decisions

| # | decision | supersedes | why now | evidence |
|---|---|---|---|---|
| D15 | **HOLD THE LINE — close the 4-week window on 2026-08-10 as pre-registered** `[paul-stated 08-08]` | the option to extend it until she had loaded the 08-04 build, and the option to prompt her into opening it | her last session was 08-03 and the strip shipped 08-04, so the window's headline question is **structurally unmeasurable** and two more days cannot fix it. Extending would amend a pre-registration to rescue a result; prompting would contaminate *"does she open it unprompted,"* which IS the question. **Better to record an honest null than manufacture a measured one** | funnel: `jumpstrip_viewed` 2/0, `jumpstrip_tapped` 2/0, both Paul's |
| D16 | **The baseline telemetry walk becomes a leg of the cycle, cadence UNSET** `[paul-stated 08-08]` | ad-hoc "trigger it yourself once and confirm it lands" — advice nobody had a reason to follow | Paul: *"not necessarily monthly… whatever the mom feedback cycle is."* ⭐ The cadence is deliberately **not** decided here: it is an input to the 8/10 reassessment of how laps are timed, and guessing it now would pre-empt that | `tools/telemetry-walk.js` |
| D17 | **The walk runs INERT on localhost, not against the live record** | the test-device approach (`d-telemetrytest-harness-v1`) drafted earlier this lap | on localhost the Worker is unconfigured, so `track()` runs and `flush()` returns — pollution is prevented by construction rather than by an exclusion someone must maintain. Measured: `attempted_network: 0`. The test device stays registered as the **fallback** for a future end-to-end test | `tools/people.json`; run output |
| D18 | **`check-telemetry.py` reports reachability, not a flat never-fired list** | the undifferentiated 23-item list | the list read as 23 defects and there were **zero**; that misreading is why it sat unexamined since 08-04. A flag nobody can act on is the same as no flag | `ad7392a` |
| D19 | **A test-harness event may never count as behaviour** | nothing — this is new, and it is the guard the walk required before it was allowed to exist | firing real events to prove wiring would otherwise flip a dead event to "fired" for every later reader. `isTestHarness` keeps *proven wired* apart from *a human did this* — the 2026-07-28 wrong-device error run in reverse | `99eb648` |

### The baseline telemetry walk — new, and now a leg of the cycle

`[paul-stated 2026-08-08]` *"worth having a baseline telemetry test that we probably work into the
cycle… not necessarily monthly. We don't know what the cycle is, but whatever the mom feedback
cycle is."* **Cadence deliberately unset — one run per lap, wherever the lap lands.**

**5 of 5 walkable Mom-facing paths fire correctly**: `jumpstrip_tapped` ·
`household_author_prompt_tapped` · `mp_envelope_toggled` · `launcher_dismissed` ·
`composer_empty_tap`.

**Why it cannot pollute, structurally rather than by promise:** run against localhost,
`tateTracker.sync.v1` is unset → `WorkerAPI.isConfigured()` false → `flush()` returns before
sending, while `track()` still runs. Measured on this run: `worker_configured: false`,
`attempted_network: 0`. **Nothing left the browser.** `metricsExclude` was rejected as the
mechanism because it makes `track()` a no-op and would prove nothing.

⛔ **Not walked, by choice:** anything POSTing to `/api/feedback` — a card answer, a note, the ack
"Got it" receipt (`viewer.html:11147`). Those write into Mom's answer record, which no metrics
exclusion covers. Localhost inertness would have stopped them too; they are excluded anyway,
because defending her record with a shim written in the same session is a single point of failure.

**The harness failed its own second run and that is why it is trustworthy.** Walk #2 reported the
launcher dismiss as ELEMENT ABSENT — the first walk had written today's date to
`tateTracker.zoneJourney.launcherDismissed.v1`, so the control stopped rendering for the day. A
baseline that only works once per day is not a baseline. It now clears the two day-scoped keys
first, read off `viewer.html:10559` and `:10702` rather than guessed — **a reset that clears a
misspelled key silently does nothing and the walk still looks green.**

### Score against the pre-registered definition — **CLEAN, 7/7** `[stamped 2026-08-12]`

⚠️ **Lap 2 ran to leg 7 on 08-08 and was never stamped.** Four days of chronicle were written on
top of it — three interlap notes, one of which asserts in passing that *"Lap 2 closed clean"* —
without the score table the definition requires. **Recording a closure and closing a thread are two
acts, and only the first has a natural trigger.** So this stamp was NOT taken on the log's say-so:
every criterion below was re-derived from the record on 2026-08-12, four days late, and the
verification is written out because a stamp whose evidence is "the section above says so" is the
thing this table exists to prevent.

| # | criterion | lap 2 | how it was verified on 08-12, not assumed |
|---|---|---|---|
| 1 | every leg that ran left its artifact | ✅ | all three leg-5 commits exist and are ancestors of HEAD (`49abc62` 06:51, `ad7392a` 07:05, `99eb648` 07:10 ET); leg 6's artifact `tools/telemetry-walk.js` is on disk and first landed in `4bfd9ca` |
| 2 | legs 1, 6, 7 non-empty (2, 4, 5 may be empty) | ✅ | all eight legs carry a row; legs 1/6/7 each name a durable output. Leg 4 is empty **and says why**, which the definition permits |
| 3 | nothing served that she has answered — `check-cards.py` exits 0 | ✅ | re-run at HEAD: **exit 0**, 18 cards, 6 served, 0 contradictions. ⚠️ This is a re-verification, not a replay — `questions.json` has moved 5 times since lap 2 closed, so what this proves is that the property still holds |
| 4 | every channel with input past its mark is attested read — R2b not red | ✅ | reconstructed per channel at the lap's own close (cutoff `2026-08-08T11:10:28Z`): feedback, observations, zone-audio and guru each had a read mark **exactly equal** to their newest record at that instant — **0 unread on all five channels**. ⚠️ Honest caveat: `.private/channel-read-state.json` is gitignored and un-versioned, so the marks cannot be proven to predate the close. What *can* be shown is that they have not moved since — the 08-09 arrivals are still unread — so no post-hoc advance flatters this row |
| 5 | the return leg shipped | ✅ | **none was owed, and that is derivable rather than asserted.** `MOM_ACK_DATA.acknowledgedThrough` at `99eb648` reads `2026-08-03T11:56:17.964Z` — **exactly** her newest input across every channel at that moment. The commit is on `origin/main` |
| 6 | the watermark stepped over nothing actionable | ✅ | `read-mom-feedback.py` prints **Ready to fold — (none)** and emits no held-back message; the four addressed notes each carry a disposition |
| 7 | the seats the scoping table calls for either ran, or the chronicle names why not `[effective this lap]` | ✅ | none convened, named in the leg-4 row with the scoping-table reason. **This is criterion 7's first-ever scoring**, and it scored by the naming clause rather than by a seat running |

**What the four-day gap actually cost, stated rather than glossed:** nothing in the world — the lap
was genuinely finished, and every criterion holds. What it cost was *legibility*. For four days the
chronicle held a closed lap that looked open, and the 08-10 interlap note asserted the closure in
prose beside a section that did not carry it — **a fully-closed lap reads exactly like a live one**
`[[feedback_unchecked_box_is_not_open_work]]`. The fix is the stamp, not a new control: laps are
rare enough that a checker for this would fire less often than a reader would.

### What lap 3 inherits

1. **The 8/10 reassessment** — how the cycle runs, and how to structure and time each lap. Paul's,
   and the first cadence decision this loop has ever made deliberately.
2. **`momack_unfolded`** — decide: re-wire the fold into the `changes[]` branch, or retire the event.
   Leaving it is the third state, and the one that reads as a bug forever.
3. **The suggestion-fence denominator** — instrument `suggestion_offered`, or accept two
   permanently uninterpretable events.
4. **Leg 6c, the Mom-proxy** — designed lap 1, skipped lap 1, skipped lap 2. Third lap running.
5. **The bench** — 1 open slot, `q-fairway-grass-seedheads` ripe in August. Only Paul runs `--approve`.

---

## 2026-08-09 — NO LAP. Meta only, recorded so the gap is explained rather than open.

`cycle-docs-check.py` flags a repo that moved past its newest chronicled lap. It did move —
twice, from two sessions — and **neither touch was a lap**, so nothing was skipped:

- **Tooling / controls (agent):** `tools/manuals-search.py` (the deterministic manuals door,
  `feedback_non_ai_door`), the W12 telemetry reclassification (the manual walk is **3 events,
  not 23**), and the `map-control` declaration this checker itself now reads.
- **Fleet data (other session):** the Bolores audio identification and its manual ingests.

**Nothing reached Mom's surface.** `viewer.html` is untouched across all of it, which is the
test that matters here — a commit is not a ship, a push is, and no lap of her cycle ran.

⚠️ **One thing DID come out of it that the next lap owes an answer on:** `check-mom-ack.py`
does **not** filter test-harness devices, so a synthetic chat turn registers as input she is
owed an acknowledgment ribbon for. That is the 2026-07-28 attribution error running backwards.
It is written up in `BACKLOG.md`'s W12 row; the designed escape is `--acknowledged-through`.
