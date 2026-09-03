---
type: path-evaluation
item: BACKLOG.md § C7 · THE CONDO AS A PAPER MODEL — and the "no garden" falsifier
project: fernwood (repo rename to Fernwood pending — C4 4a/4d)
seat: engineering-partner
date: 2026-09-03
state: AT PAUL'S GATE — planning and backlog definition only. No canon touched, nothing built.
depends-on: C4 § Sequence 5a · 5b · 5c · C5 § THE MODULE-SET DECLARATION
citation-rule: cited by SECTION and ROLE, never by line number (the repo is being renamed)
measured-against: HEAD 86b062d (HEAD moved twice under this read — see the reply)
---

# C7 — the condo as a paper model, priced

**⚠️ Read this first.** Every number below was measured today by command, in this repo. Two figures
the item rests on have moved: **plants are 44.1% of the digest, not 41%**, and the dashboard strip has
**five data cells, not four**. And the item's headline size is wrong in a way that matters: *the
plants card is the easy half.* The measured blocker is the **place** group — `renderProperty()` and
the boot sequence — which no "garden off" declaration touches.

---

## §1 · THE PAPER MODEL — what `instance/<condo>.json` declares

`build-viewer.py --instance` does not exist yet (`ls tools/ | grep build-viewer` → nothing;
`git ls-files engine/ | wc -l` → 0), so this section defines the **file** — writable before any of
that lands, and the whole of what ships in this item's first step.

| block | what it declares | why this shape |
|---|---|---|
| **identity** | placeholder name `"Midtown condo"`, `subtitle`, **no address, no unit** | The engine half of `viewer.html` still carries **52 hard-coded identity strings** on lines outside the inlined `*_DATA` consts (`2,873` ×10, `Fernwood` ×32, `Jasper` ×2, `Bortle` ×4, `Cherokee` ×2, `Tate Mountain` ×1, `Lake Sequoyah` ×1 — `awk 'length<400'` then grep). Each is a place where a condo build renders Fernwood's face. This is C5 §5b's list; C7 is what *proves* it complete. ⛔ Address and unit stay in `.private/condo-location.md` — I did not open it. |
| **module set** | `modules: { weather: on, garden: off, machines: ?, household: ?, neighbourhood: declared-absent }` | Named bundles, per C5 §3's recommendation — measured there: a per-domain switch **cannot reach `turf`**, so "garden off" would leave `TURF_DATA` rendering. Confirmed today: `renderTurf()` and `renderWeeds()` are both called **unconditionally in the INIT block**. |
| **the outward-facing family** | one key, `declared-absent`, with a `reason` string. **Captured, not built.** | `momlib.DOMAINS` has five groups — `tend · fight · visit · run · place` — and every one names a thing on the property (`python3 -c` over `momlib.DOMAINS`). A neighbourhood is none of them. Writing the placeholder now buys the thing C5 §3 exists for: an OFF module and an *unbuilt* one stop reading the same. |
| **calibration** | `cPerson` ported (her text size), `cEdge: null`, and a **grant-level `contributorLoop: false`** | Per `.plans/2026-09-02-data-model-design.md` §2c. See the sub-finding below — the declaration alone does not close it. |
| **config** | `coordinates`, `elevation {value, confidence, basis}`, `frost {source, …}` | Fernwood's own `property.json § location.elevation` is the template: it carries `confidence: "measured"` and a `basis` string naming the USGS 3DEP 1 m lidar product — *and* a `supersededValue` block whose `lesson` reads **"A single global-model API is not a measurement."** |
| **weather source** | `station: declared-absent` | Not `null`, not omitted. See below — the difference is a red error dot on her screen. |

**⭐ The `answer-age` sub-finding, worse than §2c assumed.** `mom-cycle-status.py` emits `answer-age`
from a **single global `last_answer_days`** with **no estate dimension anywhere in the signal**, so
`contributorLoop: false` in the instance file **cannot stop it firing.** Closing it takes one more
thing — the signal reads the estate's module set and **publishes `?` where no grant carries a
contributor loop**, reusing the file's `"UNMEASURED: no dated answer on record"` idiom rather than
inventing a state.

**⭐ And the loop is empty by data too**, which makes the condo the clean case: only **`plant` and
`weed` are `cardable`**, and **16 of 22** `questions.json` records carry a garden `entityRef`
(`plant` ×14, `weed` ×2); the other 6 are *product* questions (`q-almanac-name`), not estate ground
truth. Zero confirm-card supply at a gardenless estate.

**Elevation — I did not verify it, and I will not guess.** The brief's `~1,050 ft` is `assumption`: I
made no network call (no standing OK to hit an external service), and this repo already paid for the
alternative — the superseded 2,959 ft was an Open-Meteo `~90 m` global-model read stamped
`confidence: "confirmed"`. ⭐ **The terrain argument inverts at Midtown**: `property.json`'s `basis`
attributes the 86 ft error to a 90 m cell *averaging across a mountain spur and pulling toward the
ridge*. On flat urban ground that mode is absent, so the cheap API is defensible there where it was
not here — **provided the record says which source it is.** Sample 3DEP at the private coordinates and
write `value`/`confidence`/`basis`; until then the key ships `confidence: "assumption"`.

**Frost anchors differ by *derivation*, and the schema is Fernwood-shaped.** `property.json
§ frostDates` is **two-tier** — a `valleyFloor_KJZP` baseline, an `atPropertyElevation` block adjusted
±10 days for 1,338 ft of lapse, and a `frostPocketWarning` — and `renderProperty()` dereferences **all
three**. The condo has no reference station, no lapse adjustment and no frost pockets, and it sits in
a documented urban heat island (condo research § Tier 1, `validated`). **Config carries the
derivation, not just the dates.**

**The weather card with `AMBIENT` absent fails loudly in the wrong direction today.**
`fetchAmbientWeather()` on any non-OK response sets `stationOnline = false` and calls
`renderAmbientStationPanel(null, msg)`, which renders a **`live-dot error`** plus *"Hardware not yet
online — data will appear when station is powered on."* At the condo that is a red error dot promising
hardware that will never exist. **The right shape exists one function over:** `stationRain7()` returns
`null` with no station history and the strip silently relabels the figure **"past 7d (regional est.)"**
instead of "past 7d here" — a *degrade-and-label*. Recommendation: `station: declared-absent` →
suppress the panel, label the card **modelled / regional grid**, never render the error dot. C5 §3's
OFF-vs-ON-but-EMPTY, applied to weather.

**Priced.** ~3–4 h (a data file plus the three-state weather label) · fully reversible (one untracked
file in a local-only repo) · **costs Mom nothing** — she never sees it, which is the point of "model
it, don't ship it" · **buys** a second consumer for the module-set declaration to be true against, and
a completeness proof for the 52-string identity list instead of a hand-kept roster.

**Falsifier for §1:** if the condo model can be written without any key that Fernwood's own
`instance/fernwood.json` (C4 5b) also needs, it is a fixture rather than an instance — and the second
instance is doing no work the first one couldn't fake.

---

## §2 · THE FALSIFIER RUN — the predicate, and the item's real size

**⛔ First: the stated pass predicate is vacuously true today.** I ran it — `git diff --stat -- engine/`
prints nothing and exits 0, because there is no `engine/` directory (`git ls-files engine/ | wc -l` →
0). A harness that passes before the thing it tests exists is this repo's
*match-the-payload-not-the-container* failure. **The predicate must first assert
`git ls-files engine/ | wc -l` > 0**, then assert the diff is empty — a one-line fix, and the
difference between a check and a decoration.

**The checkable predicate.** The run passes when **all five** hold:

1. `build-viewer.py --instance <condo> --out <tmp>/condo.html` exits 0 with **no** engine edit.
2. `git ls-files engine/ | wc -l` > 0 **and** `git diff --stat -- engine/` empty for the whole run.
3. At **414 × A+**: no Plants cell in the strip, no Plants/Turf/Weeds cards, no bloom/care/season-note
   surface, no Mama's Perspective queue — and **the page finishes booting** (see below).
4. `build-digest.py` omits `plants`/`turf`/`weeds`/`zones` **as keys** + one `_meta` line — not `[]`.
5. No Guru plant scaffolding: `GARDEN_GURU_SYSTEM` mentions plants **60 times** (`grep -c -i plant`)
   and opens by naming the street address, the elevation and *"Garden Guru."* An instance-neutral
   prompt is a **precondition** of the run, not an output of it.

**⭐ Now the count — the item's real size, and it is not 38 `if (plants)` guards.** Mapping every
garden identifier to its enclosing function (script over `viewer.html`, skipping the inlined consts)
returns **38 engine-half functions** — but 28 are leaves inside the Plants, Turf and Weeds cards and
die with their card. What actually needs the module set:

| class | count | sites |
|---|---|---|
| **Cross-cutting renderers** (not the plants card, would render wrong or empty) | **10** | `renderDashboardStrip` · `renderBanner` · `renderTodayGlance` · `renderFieldNotes` · `generateGardenerInsight` · `gatherTodayState` · `gatherGuruLiveState` · `computeLookFors` · `makeZoneId` (mints ids from `PLANTS_DATA` + `WEEDS_DATA`) · `fnSpeciesOptionsFor` (the capture composer's dropdown) |
| **Unconditional garden calls in the INIT block** | **11** | `renderPlantsSummary` · `renderFilters` · `renderBanner` · `renderThisMonthPlants` · `renderPlantList` · `renderPlantPeakPanel` · `renderCalendarSummary` · `renderCalendarLegend` · `renderCalendarBody` · `renderTurf` · `renderWeeds` — straight-line, no guards |
| 🔴 **Unguarded DOM lookups that throw on a plantless build** | **6 of 14** | `plants-summary` `.textContent` · `plant-list` `.innerHTML` · four `plant-*-content` `.style` · **`plant-view-tabs` `.querySelectorAll`** |
| 🔴 **`renderProperty()` — the place group, behind no module switch** | **11 unguarded dereferences, 0 guards** | incl. `p.frostDates.atPropertyElevation`, `p.frostDates.valleyFloor_KJZP`, `p.frostDates.frostPocketWarning`, and `p.resources.nearestWeatherStation.elevation_ft.toLocaleString` — four levels deep, no `?.`, no `if (p.`, measured by grep over the function body |

**⭐⭐ The sharpest single finding.** The `plant-view-tabs` wiring sits at **top level, immediately
above INIT**, and calls `.querySelectorAll` on a `getElementById` result with no null check. Strip the
plants markup and it throws a TypeError, **and every statement after it — the entire INIT block —
never runs.** The condo build's most likely first failure is not a missing tile; it is a **blank
page**, from a wiring line, before a single renderer is reached. Second most likely is
`renderProperty()` throwing on a missing `frostDates` subtree.

**What that means for the plan:** the fix is not 38 conditionals. **(a)** Null-guard the 6 throw sites
and the 11 property dereferences — mechanical, ~2 h, zero design risk, and *worth doing at Fernwood
regardless* since it hardens the boot path against any data gap. **(b)** Render the strip from a
**declared tile roster × the estate's module set** rather than static ids (C5 §3's largest-consumer
note — five cells, not four). **(c)** Gate the 11 INIT calls through the same resolver. Guard-first,
roster-second: (a) ships before C4 5b and makes the falsifier run *diagnostic* instead of *fatal*.

**Priced.** ~2 h (a) · ~6–8 h (b)+(c) · ~1 h the run. (a) and (c) reversible; (b) is a real refactor
of a surface Mom uses daily, so it must clear `herConditions()` `clean:true` at 414 × A+ before
`main`. **Costs Mom** nothing otherwise. **Buys:** the engine/instance line stops being an assertion.

**A FAIL means — hold this line — re-classify, no repo moves** (C4 5c). It says the boundary is drawn
wrong and 5d stays shut; it does *not* license moving files to make the check pass.
**Falsifier for §2:** if the run needs an edit under `engine/` to render — or renders only because a
guard was added to `engine/` *during* the run — the line is wrong. And if it passes first try with no
guards added, re-read predicate 2: the container was probably empty.

---

## §3 · `<family-b>`'s TWO GARDENLESS ESTATES — the second falsifier

⛔ Planning only. **No third-party name enters a tracked file** (C4's forward rule) — `<family-b>`
throughout. What the two estates add that the condo does not:

| | the condo (family A, estate 2) | `<family-b>` estate 1 — household with equipment | `<family-b>` estate 2 — a lodge with neither |
|---|---|---|---|
| module set | weather on · garden off · household ? | weather + **machines on** · garden off | weather only |
| what it newly tests | one gardenless instance under one grant | **`run` on with `tend` off** — the first estate where a non-garden domain carries the record | ⭐ an estate with **no `cardable` domain at all**, so the contributor loop is forced by the module set rather than by a hand-written `false` |
| the chooser | ⛔ absent at one grant (condo research § R.2 — navigation, never an ask) | **two grants inside one family door** — the C4 three-level routing exercised before family A ever has two | same |
| `check-domains.py` | one OFF module | **the inverted sweep matters**: a non-empty domain file at an OFF module becomes a finding | the whole roster reads `declared off` |

**⭐ The load-bearing addition is estate 2.** The condo still has *something* — the dwelling record. An
estate with **no cardable domain** is the only case that proves the loop's absence is *derived* rather
than declared, and it is the cheapest instance file to write. **Recommendation: model estate 2
alongside the condo** (~1 h more) and hold estate 1 until the machines bundle's membership is settled
— `vehicles.json` groups by *kind* while `momlib.DOMAINS` groups by *action*, C5 §3's flagged
VOCABULARY §5 seam and not C7's to resolve.

**Priced.** ~1 h · reversible · costs Mom nothing · buys the derived-vs-declared proof. **Falsifier:**
if estate 2's loop is silent only because someone hand-wrote `contributorLoop: false`, the resolver is
not reading the module set.

---

## §4 · THE THIRD PATH THROUGH THE AI BOUNDARY — named, not decided

Two paths exist today: a model **drafts and Paul approves** before she reads it (harvest → confirm →
fold), and a model **analyses the record on the ask path** (Guru answering her question). The third:

> **A model choosing what she SEES** — which events, which openings, which "positive local news" reach
> her surface at all. The AI boundary is silent on it, because Fernwood has never had a surface where
> selection was the model's act.

`user-researcher` recommended against it with the harm named (condo research §4.2): a positivity
filter **silently drops the water-main break on her street** — it fails hardest exactly where local
news is most useful — and there is no seat for Paul in a daily automated selection.

**The smallest design that keeps capture deterministic**, and it is a *sourcing* decision rather than
an editorial one: **(1)** a **curated source list Paul approves once**, versioned in the instance
file, each row carrying why it was chosen; **(2)** a **deterministic feed** — newest item in a
category, no model, no ranking (the Conservancy's categorised RSS is `validated` in the research and
the park's Tribe Events JSON returns 43 events, so the AI-free door exists on the first try);
**(3)** a model may **only summarise an item already selected deterministically**, source link beside
it. Selection stays out of the model's hands; the model touches prose only, on the ask path.

⚠️ One measured trap for whatever gets built: the events feed's `cost` field was **empty on all 10
sampled rows**. *Empty ≠ free.* Rendering "free" off an absent field is the unchecked-box failure with
a person walking to a park at the end of it.

**Handed to Paul + `ai-advisor`.** Not mine to rule. **Falsifier for §4:** if a model's output
determines *which* items reach her list — not just how they read — the boundary moved.

---

## §5 · ORDER, and what ships independently

| # | step | gated on | ships alone? |
|---|---|---|---|
| 1 | the condo paper model + `<family-b>` estate 2, in `fernwood-private` | **nothing** — data files, no engine dependency | ✅ **now** |
| 2 | null-guard the 6 throw sites + `renderProperty()`'s 11 dereferences | nothing | ✅ **now**, and worth it at Fernwood regardless |
| 3 | the three-state weather label (`declared-absent` ≠ offline) | C5 §3's resolver | ✅ |
| 4 | `answer-age` reads the module set, publishes `?` at a loopless grant | C5 §2 (grant as data) | ✅ |
| 5 | instance-neutral Guru prompt | C4 5a's classification of `worker/` as engine | ✅ |
| 6 | tile roster × module set in the strip | C5 §3 | ships to `staging` first |
| 7 | **the falsifier run** | **C4 5b + C5 §3** | ⛔ waits |
| 8 | the repo split (C4 5d) | **7 passing** | ⛔ waits |

Steps 1–5 are the readiness work; step 7 is the only one that truly needs C4's build step, and
sequencing it last is what keeps this item from blocking on the rename.

---

## §6 · WHAT I DID NOT DECIDE — Paul's calls

1. **Her role at the condo** — owner or contributor; §1's whole calibration block follows from it, and
   data-model §2c is explicit that no global answer is right for everyone.
2. **Which modules are ON** — `machines` and `household` are `?` deliberately; the household record is
   the condo's only unsubstitutable content (research § Tier 4) and one walk-through closes it.
3. **Whether the outward-facing family is ever built** — §1 captures a placeholder, §4 names the
   ruling it needs; neither is a decision to build it.
4. **Where the condo directory lives** — C4 Q5's default is `fernwood-private`; C7's own text flags a
   throwaway directory in the public repo as Paul's. I assumed the default.
5. **A vs B as the on/off unit** — C5 §3 recommends B and marks it Paul's; A reopens ratified
   VOCABULARY §3. I wrote §1 against B.

---

## §7 · OPEN QUESTIONS — one sentence each

1. Does `answer-age`'s fix belong in C7 or back in C5 §3's consumer table as a sixth row?
2. Is `neighbourhood` one module or several (`events` · `civic` · `dwelling`), given that a single OFF
   switch cannot later be half-on without a migration?
3. Should the null-guard pass be filed as its own Tier-1 Fernwood defect, since `plant-view-tabs`
   kills the whole page on *any* markup change, not just a condo build?
4. Does the condo carry `frostDates` at all, or declare frost `not-applicable` and drop it from
   `renderProperty()`?
5. Who owns making `GARDEN_GURU_SYSTEM` instance-neutral — C7, C5 §5b, or C4 5a — and does the prompt
   keep the name *Garden* Guru at a place with no garden?
6. Is the 44.1% figure worth correcting in `BACKLOG.md` § C7 and `PRODUCT-ENGINE.md` § four things
   this collides with, now that the size argument has moved to the place group anyway?
