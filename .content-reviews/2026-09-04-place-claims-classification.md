# Place-claim classification — all 58 shared-engine sentences

**Date:** 2026-09-04 · **Mode:** review (classification pass) · **Reviewer:** content-steward
**Register:** `engine/place-claims.json` (58 claims, all `unclassified`, baseline `renderingAtCondo: 58`)
**Audience:** the person reading a Fernwood-engine instance — Mom at Fernwood, Mom at the Midtown condo (paper-model instance: no garden, no lake, no slope, no canopy)
**Surface:** in-app prose across plants, sky, weather, machines, capture
**Charter applied:** `~/.claude/content-principles/fernwood.md` + `cross-project/voice-and-stance.md` (could-be-anyone test)
**Grounding:** `VOCABULARY.md` §4 — *"each estate names its own thing"*; *"Almanac" is not a portable noun*; `estate` never reaches a user-facing surface, **the interface names places**

⛔ **PROPOSAL ONLY.** Nothing in `engine/` was edited. Main session applies after Paul reads.

---

## How the three classes were drawn

- **engine-neutral** — the sentence is true *and sensible* wherever the reader is. Control labels, empty states, category definitions, and `here` used to mean *wherever you are*. Stays engine copy.
- **instance-prose** — the sentence asserts something about **this** place (chestnut canopy, the pond, the slope, the fairway, the thermal belt, a dark sky, the Blue Ridge ecoregion). Belongs in the estate's canon and must not render where canon does not declare it.
- **reword** — engine copy whose *job* is right everywhere but whose *wording* names a place. Reworded sentence supplied.

**The dividing line I used inside the candidates payload**, so it is checkable rather than felt: a **category definition** with no place claim is engine-neutral; a **record judgment** about Fernwood's own list is instance-prose. That is why `"Multi-decade canopy / regional restoration species."` is neutral and `"Most ecologically meaningful candidate on this list…"` is not.

**On the "renders canon" flag.** Paul asked me to mark rows where the fix is a data-driven render rather than a copy edit. 39 of the 44 instance-prose rows are quotes of a canon record the engine already inlines. The other 5 are **hardcoded in `engine/viewer.template.html` with no canon behind them at all** — those need a canon field minted before they can move. That distinction is the actionable half of this pass.

---

## The 58 rows

| key | class | note / reword | sentence |
|---|---|---|---|
| `fc2730efad` | instance-prose | renders canon: `candidates.json` → `candidates[].rationale`. Also names a Fernwood plant fact ("the hydrangeas already by the porch") | A native of the cove forests at this elevation — the wild cousin to the hydrangeas already by the porch. |
| `298221de9b` | instance-prose | renders canon: `candidates.json` → `candidates[].rationale`. Asserts a pond and a spring drainage | A wet-meadow native that would suit the pond's edge or the spring drainage seepage. |
| `d21001261e` | instance-prose | renders canon: `candidates.json` → `candidates[eastern-hemlock].notes`. ⚠️ Also a **charter breach independent of the condo**: "ACTIONABLE NOW" + bare imperative violates *Field journal, not task manager* and *Action sentences soften toward "worth doing"* | ACTIONABLE NOW: check existing hemlocks on the property for HWA and treat (imidacloprid + dinotefuran soil drench at root flare). |
| `a117d99f33` | instance-prose | **No canon behind it** — hardcoded meteor-shower `tip`, `engine/viewer.template.html:7228`. The astronomy is engine; this sentence is a dark-sky claim and must move to the estate's record | Always worth watching from your dark property skies. |
| `50a0bef48f` | instance-prose | renders canon: `events.json` → `events[].name`. A Midtown condo's local events are not Blue Ridge festivals | Blue Ridge Blues & BBQ Festival |
| `f2f0893448` | instance-prose | renders canon: `candidates.json` → `curationNotes`. Places the reader in a Blue Ridge cove-forest community | Confirmed in GNPS Blue Ridge Cove Forest list. |
| `3e7ef179a1` | instance-prose | renders canon: `candidates.json` → `curationNotes` | Confirmed in GNPS Blue Ridge landscaping list for both Montane Oak and Cove Forest understory. |
| `29ae2a7067` | instance-prose | renders canon: `candidates.json` → `curationNotes` | Confirmed in GNPS Blue Ridge list across Cove, Low-Mid Oak, and Seepage communities. |
| `73fd4f1fff` | instance-prose | renders canon: `candidates.json` → `curationNotes` | Confirmed in GNPS Blue Ridge Seepage Wetland list. |
| `d2bc7b9256` | instance-prose | renders canon: `candidates.json` → `candidates[].notes`. Names two Fernwood features | Direct fit for the pond area and the spring drainage. |
| `c2868040dc` | instance-prose | renders canon: `property.json` → `sky.bortleEstimate` + the celestial roster's `georgiaVisibility` (today hardcoded in the engine template; label map at `viewer.template.html:16215`). The rating is a **dark-sky claim**, not a label — rewording "from property" leaves it false at Bortle 8 | Excellent from property · 🌒 Thin crescent — minimal · 60–120/hr |
| `38e33e7a64` | instance-prose | same as `c2868040dc` — renders canon: `property.json` → `sky.bortleEstimate` | Excellent from property · 🌓 Quarter moon — moderate |
| `eebc2bd4a7` | instance-prose | renders canon: `candidates.json` → `candidates[].notes`. "up here… 10–15°F cooler" is a 2,873 ft claim; false at 1,050 ft | Fine fescues struggle in the hot, humid Piedmont but are far more viable up here, where summers run 10–15°F cooler. |
| `ce7e13e649` | instance-prose | renders canon: `candidates.json` → `candidates[].notes` (sentence-split artifact of the ledger) | For a Blue Ridge native alternative, 'Zagreb' threadleaf coreopsis (C. |
| `79ba4cb2a6` | instance-prose | **No canon behind it** — hardcoded callout body, `engine/viewer.template.html:6662`. Same shape as the property-card callouts already moved to `property.json` → `story.callouts` on 2026-09-03 | GA DNR lists these rich-cove species as worth noticing if you find them on the property — special-concern, not yet endangered: cucumber-root, galax, trailing arbutus, partridge-berry, round-leaved violet. |
| `ad1c23441c` | instance-prose | renders canon: `sources.json` → `sources[].name`. A regional nursery roster; each estate sources from its own region | Gardens of the Blue Ridge |
| `0620a31356` | instance-prose | same as `c2868040dc` — renders canon: `property.json` → `sky.bortleEstimate` | Good from property · 🌑 New moon — ideal · 15–30/hr |
| `ea13f11802` | instance-prose | same as `c2868040dc` — renders canon: `property.json` → `sky.bortleEstimate` | Good from property · 🌒 Thin crescent — minimal · 25–60/hr |
| `cd5d9a8863` | instance-prose | same as `c2868040dc` — renders canon: `property.json` → `sky.bortleEstimate` | Good from property · 🌔 Gibbous — significant · 10–15/hr |
| `989d549d5d` | instance-prose | same as `c2868040dc` — renders canon: `property.json` → `sky.bortleEstimate` | Good from property · 🌕 Full/bright — severe · 10–20/hr |
| `19f43c0c06` | instance-prose | same as `c2868040dc` — renders canon: `property.json` → `sky.bortleEstimate` | Good from property · 🌕 Full/bright — severe · 30–50/hr |
| `fcb35179fc` | instance-prose | same as `c2868040dc` — renders canon: `property.json` → `sky.bortleEstimate` | Good from property · 🌕 Full/bright — severe · 50–100/hr |
| `336e23d2fc` | instance-prose | renders canon: `candidates.json` → `_meta.categories.turf`. ⚠️ **And the built copy has drifted from its source**: `candidates.json` says *"the managed turf"*; the inlined `CANDIDATES_DATA` says *"the managed **fairway** turf"* (`viewer.template.html:7253`). "Fairway" is Fernwood's own noun and it leaked into engine-shipped copy | Grasses and lawn alternatives for the managed fairway turf — the practical tall fescue alongside lower-input and native-leaning options worth trialing as the lawn leans toward the natural approach. |
| `d0357c448a` | instance-prose | renders canon: `candidates.json` → `candidates[].notes`. Assumes rich-cove flora underfoot | If found on the property, leave alone and support — do not transplant. |
| `18bdb41932` | instance-prose | renders canon: `candidates.json` → `candidates[flame-azalea].notes` | If sourcing from Gardens of the Blue Ridge: they specialize in native azaleas including hard-to-find color forms. |
| `2fbd846698` | **reword** | Drop "the house" — a condo unit is not a house. Also check the trailing button string *"Tell the Almanac ›"* (`viewer.template.html:14356`), which is out of this register but carries the same defect as `68b119a817` | **Reword:** *"Is there something else this place runs on?"* — was: Is there something else the house runs on? |
| `4cec61cf54` | instance-prose | renders canon: `candidates.json` → `candidates[].notes`. Asserts a spring drainage exists here | Likely already present on the property in the spring drainage. |
| `5f2174a422` | instance-prose | renders canon: `candidates.json` → `_meta.categories.rich-cove` | Look-don't-pick if found on the property; if planting, only ethical-propagation sources. |
| `41f1d2a2f8` | instance-prose | renders canon: `candidates.json` → `candidates[american-chestnut].notes`. ⚠️ The register's place-word regex matched "on this" — a false positive — but the sentence is a judgment about **Fernwood's** candidate list, so it moves with the record either way | Most ecologically meaningful candidate on this list; also the slowest and least guaranteed. |
| `72b6516528` | engine-neutral | A category **definition**, not a claim about where the reader is — true wherever a restoration module runs. Renders only where that module is on; that is module gating, not copy | Multi-decade canopy / regional restoration species. |
| `58d3782a85` | instance-prose | renders canon: `candidates.json` → `candidates[tall-fescue].notes`. "at this elevation" is the place claim | Non-native (Eurasian) — the one practical exception to the native-first thinking on this list, earned by being the realistic choice for a lush mowed turf at this elevation. |
| `62fbe973eb` | **reword** | Section title, `viewer.template.html:6656`. Charter — *anchored naming beats field-journal-fluent naming*: do **not** reword to "Here" or "This Place" (names the register, not the thing). Render the estate's own name through the existing `data-site="estateName"` door | **Reword:** *"At Fernwood"* (engine renders `estateName`) — was: On the property |
| `15c54dc50b` | instance-prose | renders canon: `candidates.json` → `candidates[american-chestnut].rationale`. "at this elevation" | Once a dominant canopy species at this elevation in the southern Appalachians. |
| `c2b55d010d` | instance-prose | renders canon: `candidates.json` → `candidates[].notes`. Presumes the reader has existing tree canopy | One of the easiest natives to establish under existing tree canopy. |
| `4025a34f1f` | instance-prose | renders canon: `candidates.json` → `curationNotes`. A Blue-Ridge-relative claim | palustris is a coastal-plain wetland species, not a Blue Ridge native. |
| `3962a6c5a8` | instance-prose | renders canon: `candidates.json` → `candidates[switchgrass].notes`. "this slope" | Roundstone offers a Georgia-ecotype switchgrass — the right provenance for this slope. |
| `cb3080d7e9` | engine-neutral | Control label; "device" is not a place | Show all sync phases on this device |
| `60e0a8744a` | instance-prose | renders canon: `candidates.json` → `candidates[].rationale` | Signature North Georgia mountain native — the Cohutta and Smokies range is centered on this species. |
| `9dc785661e` | instance-prose | renders canon: `candidates.json` → `curationNotes` | sphaerocarpa is a south-central species, not a Blue Ridge native. |
| `800d4ad9ab` | instance-prose | renders canon: `candidates.json` → `_meta.categories.keystone`. Ecoregion-scoped by construction | Tallamy-defined keystone genera for Blue Ridge ecoregion — species that support disproportionate caterpillar / Lepidoptera diversity (oaks 400+, cherries 450+, willows 380+). |
| `ff0d1cfdbc` | **reword** | `viewer.template.html:9125`. "the property gauge" → the on-site gauge; the row should also only render where the estate declares a gauge | **Reword:** *"The 25-year historical normal the rainfall percentile chips compare against — regional, not the on-site gauge."* |
| `b3f592f076` | instance-prose | **No canon behind it** — hardcoded callout body, `viewer.template.html:6669`. Regionally true anywhere, but it is the **body of the chestnut callout** whose heading (`41ef349fc8`) is the false claim. Classed instance-prose deliberately so the ratchet keeps counting it: neutral-classing it would let the condo render southern-Appalachian chestnut history under a clean check | The American chestnut was a dominant canopy tree across the southern Appalachians until the chestnut blight, introduced from Asia in 1904, killed virtually all mature trees by 1950. |
| `90136ced35` | engine-neutral | "here" = this phone. Sync-maintenance help text | The cloud copy is the source of truth, so nothing here is lost. |
| `b15e031271` | engine-neutral | Empty state; "here" = this list | The first observation goes here. |
| `d1d56fd311` | instance-prose | renders canon: `candidates.json` → `candidates[tall-fescue].notes`. "the fairway" and "the North Georgia mountains" are both Fernwood claims | The grass already running the fairway, listed here for the choice that matters when overseeding: a quality turf-type blend, not old pasture-grade "Kentucky 31." UGA's standard cool-season lawn grass for the North Georgia mountains. |
| `db24a895a0` | **reword** | Weather source legend | **Reword:** *"The live measured readings, the indoor sensors, and the on-site rain-gauge totals."* |
| `9660e008ce` | instance-prose | renders canon: `candidates.json` → `candidates[].notes` | The pond and spring drainage could host it if the trial winner is the priority. |
| `ad4a2e083d` | **reword** | House-systems module blurb, `viewer.template.html:14328`. Keeps its job everywhere once "the house" goes | **Reword:** *"The systems this place runs on — what each one is, the rhythms that keep it happy, and which breaker feeds it."* |
| `41ef349fc8` | instance-prose | **No canon behind it** — hardcoded heading, `viewer.template.html:6667`. ⭐ Paul's own named example. Needs a canon home first (see recommendation below) | This forest was once chestnut canopy |
| `ccff0e2ba2` | instance-prose | renders canon: `candidates.json` → `candidates[american-chestnut].rationale`. The data twin of the row above | This slope was once chestnut canopy. |
| `c95d46fefe` | instance-prose | renders canon: `candidates.json` → `candidates[].notes`. "the pond's edge" | verticillata 'Zagreb') was also a top performer in the same trial — and a better fit for dry sunny spots than for the pond's edge. |
| `68b119a817` | **reword** | Capture-surface intro, `viewer.template.html:19272`. `VOCABULARY.md` §4 — *"Almanac" is not a portable noun*: a genre promise earned by 178 month-keyed season notes, false at a gardenless condo. Render the estate's name through the existing `data-site="estateName"` door | **Reword:** *"What you set down here is what Fernwood knows."* (engine renders `estateName`) — was: What you set down here is what the Almanac knows. |
| `ef5477c768` | **reword** | Machines summary, `viewer.template.html:14002`. A condo has no shed. If Paul wants "garage and shed" kept at Fernwood, it becomes a per-estate string rather than engine copy | **Reword:** *"What's parked and stored here — and what each one needs"* |
| `687a807b67` | instance-prose | renders canon: `candidates.json` → `curationNotes` | Year-round evergreen native fern — confirmed in GNPS Blue Ridge Low-to-Mid Oak Forest list. |
| `d0fe3682cf` | instance-prose | **No canon behind it** — hardcoded meteor-shower `tip`, `viewer.template.html:7153`. The Orionid facts around it stay engine; this sentence is the dark-sky claim | Your property's dark skies reveal Orion brilliantly as a backdrop. |
| `5809e4ac60` | engine-neutral | "here" = wherever you are; the time is computed from the instance's own coordinates. ⚠️ Neutral **only** while sunset derives from instance coords, never a typed value | · last light here 8:05 PM |
| `17f7ddaf43` | **reword** | Weather source legend, `viewer.template.html:9124`. Also gate the row on the estate declaring a station — at the condo there is none | **Reword:** *"— the on-site weather station."* |
| `4b0a0f7309` | **reword** | Weather source legend, `viewer.template.html:9124` | **Reword:** *"— the third-party forecast model, pulled in from off-site."* |

---

## Counts

| class | rows |
|---|---|
| **instance-prose** | **44** — of which **39 render canon** (a data-driven render fixes them) and **5 are hardcoded in `engine/viewer.template.html` with no canon field to move to** |
| **reword** | **9** — reworded sentence supplied for each |
| **engine-neutral** | **5** |
| total | **58** |

**Canon sources behind the 39:** `candidates.json` (29) · `property.json` → `sky.bortleEstimate` (8, the visibility ratings) · `events.json` (1) · `sources.json` (1).

**The 5 with no canon home:** `41ef349fc8`, `b3f592f076`, `79ba4cb2a6` (the plant-context callouts) and `a117d99f33`, `d0fe3682cf` (the meteor-shower tips).

**Ratchet effect if all of this is applied:** `renderingAtCondo` should fall 58 → 5 as the reworded and neutral rows stop counting, then → 0 as the instance-prose stops rendering where canon does not declare it.

---

## Three rows for Paul's eye

**1. `41ef349fc8` — "This forest was once chestnut canopy" (plus `b3f592f076` and `79ba4cb2a6`).**
This is the exact sentence Paul named, and it is the worst-placed one in the register: it is **hardcoded HTML in the engine template** (`viewer.template.html:6655–6677`), not a canon quote, so no data change moves it — someone has to mint the field. The good news is the pattern is already proven: on 2026-09-03 the property card's callouts were moved out of `renderProperty` into `property.json` → `story.callouts[]`, with `"An estate with no story renders no lead and no callouts."` The plant-context block is the same defect that migration missed. **Recommend extending it — `property.json` → `plantContext.callouts[]`, read through the existing `data-record-prose` door (the section intro directly above it, line 6657, already uses it).** One mechanism, no new one.

**2. The eight "Excellent / Good from property" sky ratings.**
These read as labels and are actually **claims**. Rewording "from property" away would leave a condo under a Bortle 8 sky being told meteor viewing is *Excellent* — a claim Mom would act on by walking outside, and the one failure this project's own doctrine calls unforgivable (*trust is the load-bearing emotion; a confidently-wrong record is worse than an honestly-unsure one*). `property.json` → `sky.bortleEstimate` already exists at Fernwood, so the fix is available today: derive the rating from the estate's own sky, and let an estate with no sky record render the shower without a verdict — which is also *describe, don't grade* doing its job.

**3. `68b119a817` — "What you set down here is what the Almanac knows."**
`VOCABULARY.md` §4 rejects *"Almanac"* as a portable noun in as many words, and this sentence sits on the **capture surface** — the moment a person is deciding whether her note is worth writing. It is the highest-traffic identity claim in the engine, and at the condo it promises a seasonal almanac over a record that is systems and receipts. The `data-site="estateName"` door already exists (`INSTANCE-RECIPE.md` lists `estateName`, `regionShort`), so *"…what Fernwood knows"* is a render, not a rewrite — and it satisfies §4's *each estate names its own thing* rather than working around it.

**Runner-up, non-place, worth two minutes:** `d21001261e` opens *"ACTIONABLE NOW:"* with a bare imperative. That breaks the Fernwood charter's two oldest rules — *field journal, not task manager* and *action sentences soften toward "worth doing"* — at Fernwood, today, independent of the condo. Suggested: *"Worth checking the hemlocks already here for HWA — the treatment that works is an imidacloprid or dinotefuran soil drench at the root flare."*

---

## Open questions for Paul

1. **`ef5477c768` — "the garage and shed."** Reworded here to *"What's parked and stored here."* Would you rather keep "garage and shed" at Fernwood as a per-estate string? It is warmer and more anchored; it just cannot be engine copy.
2. **`62fbe973eb` — "On the property"** as a section title becomes *"At Fernwood."* Confirm you want the estate name in a section heading (the charter's anchored-naming rule points that way, and it repeats the card name).
3. **The `candidates.json` inline drift** (`"managed turf"` in source vs `"managed fairway turf"` in the built viewer) is a real finding outside this pass. Worth checking whether `check-data-inline.py` covers `candidates.json` — if it does, it should have caught this; if it does not, that is the gap.
4. **`5809e4ac60`'s neutrality is conditional.** *"last light here"* is safe only while sunset derives from the instance's coordinates. If a future build ever types a Fernwood sunset into engine code, this row silently becomes a place claim and nothing in the register would notice.

---

## Principles this pass proposes (not yet added to the library)

- **Scope: cross-project.** *A label whose value is a claim cannot be fixed by rewording the label.* "Excellent from property" reads as chrome; delete the place word and the falsehood survives in the verdict. When a rendered string mixes engine framing with a place-dependent judgment, the judgment has to derive from the instance's own record or not render.
- **Scope: Fernwood.** *Genre nouns are estate property, not engine property.* "Almanac," "fairway," "the house," "the shed" all name what this estate happens to be. Engine copy gets the generic frame; the estate supplies its own noun — the same rule `VOCABULARY.md` §4 already states for "Almanac," generalized to every noun that only Fernwood has earned.

Both need a second instance before promotion — the condo build is the natural test.
