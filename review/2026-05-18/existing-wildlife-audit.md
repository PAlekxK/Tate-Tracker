# Existing Wildlife Audit — Depth Filter Pass (2026-05-18)

**Filter applied:** [[feedback_tate_tracker_depth_filter]] — "what would Paul realistically hear, see, or observe on this property" — never regional completeness.

**Status:** Research only. **No data files edited.** All recommendations require your sign-off before any species is removed or reworked.

---

## Triage outcomes (live walk-through, 2026-05-18)

**Pattern Paul established:** preserve everything, but rewrite framing on unconfirmed entries from observed-fact to *regionally possible / watch for* — more honest than aspirational. Zero deletions across all five files.

### Lake Sequoyah scope
✅ **In, with explicit framing** — keep Belted Kingfisher, Great Blue Heron, Northern Water Snake, all 3 fishing species. Label cards/tabs so the lake is honestly framed as a nearby place Paul fishes at, not on the property itself. **Side task:** resolve the distance inconsistency (`birds.json._meta` says 0.3 mi; `research-resources.md` says ~6.2 mi).

### Birds (16)
- 13 keep-as-is (the strong-fit list above)
- **Broad-winged Hawk** → keep, **soften prose** from observation-implying to "watch for September migration" + summer presence as plausible
- Belted Kingfisher → keep (lake in scope)
- Great Blue Heron → keep (lake in scope)

### Amphibians (12)
- 8 keep-as-is
- **Slimy Salamander** → confirmed observed; keep as-is
- **Two-lined Salamander** → confirmed observed; keep as-is
- **Fowler's Toad** → keep, **soften prose** to regionally-possible
- **Marbled Salamander** → keep, **soften prose** to regionally-possible

### Snakes (12)
- 3 keep-as-is (Copperhead, Eastern Rat Snake, Eastern Garter Snake)
- **Confirmed observed (keep as-is):** Northern Water Snake, Ring-necked Snake, Eastern Kingsnake, Black Racer, Dekay's Brown Snake
- **Soften prose to regionally-possible / watch for:** Timber Rattlesnake, Rough Green Snake, Worm Snake, Eastern Hognose Snake

### Lizards (5)
- 3 keep-as-is (Five-lined Skink, Broad-headed Skink, Eastern Fence Lizard)
- **Ground Skink** → confirmed observed; keep as-is
- **Six-lined Racerunner** → keep, **soften prose** to regionally-possible / near elevation limit

### Fishing (3)
- All 3 keep (lake in scope)

### Summary counts
- **Species preserved:** 48 / 48 (zero deletions)
- **Confirmed observed (keep as-is):** 39
- **Soften prose to regionally-possible:** 9 (1 bird, 2 amphibians, 4 snakes, 1 lizard, plus Hognose flagged earlier as unverified)
- **Distance fact-check pending:** Lake Sequoyah (~0.3 vs ~6.2 mi inconsistency)

### Work remaining
1. **9 prose-softening edits** across `birds.json`, `amphibians.json`, `snakes.json`, `lizards.json` + re-inline `*_DATA` constants in `viewer.html`
2. **Lake Sequoyah distance resolution** — fact-check actual distance and correct one of the two sources
3. **Lake-scope framing label** — small subtitle/note on the Wildlife & Fishing surfaces making the "nearby, not on-property" framing explicit

None of this is data deletion. All of it is honest-framing edits. Voice-craftable — could be a focused content-steward pass or a direct Paul-and-Claude session.

---

**Headline:** the existing wildlife data is already remarkably well-curated under this filter. Every species file has property-anchored prose throughout (south-facing fairway, mature mixed forest, the pond, Lake Sequoyah at 0.3 mi, etc.) — this is not encyclopedia-import data, it's already field-journal-flavored. Most species pass cleanly. The audit below flags the ~10 entries across all 5 tabs that are worth a second look — usually because the habitat fit is slightly off the property's profile, OR the prose reads more aspirational than confirmed-observed.

---

## A scope question to resolve first

The depth filter says "what Paul realistically hears, sees, or observes **on this property**." Strictly applied, that excludes Lake Sequoyah (~0.3 mi away by the bird data, ~6.2 mi away per the research-resources / Tate Mountain Estates context — there's an inconsistency to resolve, but either way it's not *on* the property).

Affected entries:
- **Birds:** Belted Kingfisher, Great Blue Heron (both tagged "Lake Sequoyah")
- **Fishing:** All 3 species are Lake Sequoyah by definition
- **Snakes:** Northern Water Snake (likely tied to the lake or property pond)

**Two ways to read this:**
1. **Strict:** drop Lake Sequoyah-only species. The fishing tab effectively goes away.
2. **Generous:** "the property" includes the immediate environment Paul actually moves through — fairway, forest, pond, AND the lake he fishes at. Keep Lake Sequoyah content, but label it explicitly so the framing is honest.

Recommend (2): generous. Lake Sequoyah is part of how Paul lives on this land — it's the source of the property's name (Col. Sam Tate's reservoir), it's where he fishes, the kingfisher and heron are present on visits. Removing them would be filter-strict but life-inaccurate. Just be clear about the framing.

The Lake Sequoyah distance discrepancy in `birds.json._meta` (says 0.3 mi) vs. `research-resources.md` (~6.2 mi) is worth resolving regardless of this decision.

---

## Birds (16 species)

The bird data is the most observationally written of the five files — almost every entry has property-specific prose that reads like genuine field-journal observation. Most pass without question.

### ✅ Keep — strong property fit, confident prose

- **Ruby-throated Hummingbird** — universal at GA feeders, prose is grounded ("expect first male by late April")
- **Scarlet Tanager** — mature deciduous forest at elevation = textbook habitat
- **Rose-breasted Grosbeak** — forest edges + elevation, prose confident
- **Indigo Bunting** — south-facing fairway edge = exactly the described habitat
- **Wood Thrush** — mature deciduous forest with deep leaf litter, prose says "the voice of the Blue Ridge forest in summer"
- **Pileated Woodpecker** — mature forest, hard to miss (large, loud, leaves obvious excavation marks)
- **Barred Owl** — mature forest near water, audible at night; prose says "step outside and listen"
- **Dark-eyed Junco** — THE Blue Ridge mountain bird at elevation; year-round breeding at 2,959 ft is a real property signature
- **Eastern Towhee** — shrubby edges = fairway edge fit
- **Wild Turkey** — prose says "regularly move across the property" — strong observational claim
- **Ovenbird** — distinctive "TEACHER-teacher-teacher" call; "you'll hear this bird constantly on Church Mountain Road in May–June"
- **Carolina Chickadee** — universal feeder bird
- **White-throated Sparrow** — "common winter visitor to Church Mountain Road, often in loose flocks"

### ❓ Verify with Paul — habitat-plausible, but prose may be more aspirational than confirmed

- **Broad-winged Hawk** — the September kettle migration claim ("watch the sky on Sep 12–20 from the fairway") reads as a prediction, not a confirmed observation. Summer breeding in surrounding forest is plausible but easy to miss (forest-interior + quiet call). **Worth asking:** have you actually seen the kettles? Or heard the thin "peeeee" whistle in summer?
- **Belted Kingfisher** — Lake Sequoyah scope question. If yes-keep-lake → keep. If property-strict → drop.
- **Great Blue Heron** — same Lake Sequoyah scope question.

### ⚠️ Consider — none

Birds tab passes the filter cleanly. The only edits I'd flag are the two Lake Sequoyah-only entries and the Broad-winged Hawk's confirm-status.

---

## Amphibians (12 species)

The amphibian data leans heavily on the property pond + moist forest floor — both real features of the property. Some salamander entries are habitat-plausible but cryptic enough that observation may not be guaranteed.

### ✅ Keep — strong fit

- **Spring Peeper** — universal in NoGA pond areas; loud spring chorus
- **Upland Chorus Frog** — NoGA mountain species, breeds in temporary pools
- **American Toad** — universal
- **Green Frog** — permanent pond resident
- **American Bullfrog** — permanent pond resident
- **Gray Treefrog** — universal where pond + trees coexist
- **Spotted Salamander** — Blue Ridge classic, breeds in the pond
- **Woodland Salamander (Plethodon sp.)** — already conservatively relabeled by you. Keep.

### ❓ Verify with Paul

- **Fowler's Toad** — range overlaps American Toad but prefers sandier/drier disturbed habitat. Less likely at a heavy-clay mountain property than American Toad. **Worth asking:** do you see two distinguishable toad types, or just one? If the field observation is just "toads," consider dropping Fowler's.
- **Marbled Salamander** — less abundant than Spotted; breeds in dry pond basins in fall (unusual). Possible but more specialized. **Worth asking:** have you ever found one in late summer / early fall, or in a fall pond margin?
- **Slimy Salamander** — habitat says "moist rocky slopes, ravines, cave entrances." If the property has rocky outcrops, very plausible. If not, less so. **Worth asking:** does the property terrain include rocky slopes Paul has flipped rocks on?
- **Two-lined Salamander** — habitat is "under rocks in and alongside small, fast-moving streams." Requires actual flowing water. **Worth asking:** does the property have flowing streams Paul could find these in, or just seeps?

### ⚠️ Consider — none

Same pattern as birds — verify the ❓ ones, drop none without you naming the call.

---

## Snakes (12 species)

The snake data was added recently and is well-anchored, but snakes are cryptic enough that several entries may be "habitat-plausible regional inclusions" rather than "confirmed observations." This is the tab where the depth filter has the most teeth.

### ✅ Keep — strong fit, confident prose

- **Copperhead** — universal in NoGA forest; real safety topic; you've explicitly framed this as "the venomous snake to know on this property"
- **Eastern Rat Snake** — common around houses; prose says "the largest snake at Church Mountain Road"
- **Eastern Garter Snake** — prose says "probably the most encountered snake on the property" — confident observation

### ❓ Verify with Paul

- **Timber Rattlesnake** — possible in mature mountain forest, but the prose itself says "encounters near houses are rare." **Worth asking:** have you actually seen one on the property, or is this included for regional completeness as the second venomous species?
- **Northern Water Snake** — depends on the pond/lake question (see scope above). **Worth asking:** seen at the property pond, only at Lake Sequoyah, or only in the data file?
- **Ring-necked Snake** — common but cryptic ("flip enough flat rocks..."). **Worth asking:** have you actually flipped rocks and found one?
- **Eastern Kingsnake** — possible, less universal than rat snake/garter. **Worth asking:** seen one?
- **Black Racer** — plausible at fairway edge. **Worth asking:** seen one?
- **Rough Green Snake** — gentle, easy-to-miss arboreal species. **Worth asking:** seen one in low vegetation?
- **Dekay's Brown Snake** — cryptic, often around garden edges. **Worth asking:** seen one?
- **Worm Snake** — rarely above ground; mostly subterranean. **Worth asking:** seen one?

### ⚠️ Consider removing

- **Eastern Hognose Snake** — the prose itself flags the elevation/soil mismatch: "*less common in heavy clay or pure forest interior*" — which is the property's profile. Hognose prefers sandy and loamy soils with toads as primary prey; at 2,959 ft on Blue Ridge clay-loam, this is the most likely regional-completeness entry in the snakes file. **Recommend:** drop unless you've specifically seen one.

---

## Lizards (5 species)

### ✅ Keep — strong fit

- **Five-lined Skink** — universal, common around houses
- **Broad-headed Skink** — oak forests, prose-grounded
- **Eastern Fence Lizard** — "sunny edges of mixed pine-hardwood" = property fit

### ❓ Verify with Paul

- **Ground Skink** — tiny, cryptic, easy to mistake for a snake when seen. Plausible but worth confirming.

### ⚠️ Consider removing

- **Six-lined Racerunner** — the prose itself flags it: *"At 2,959 ft the species is near..."* (likely "near its elevational limit"). Open sandy/rocky habitats only. Property has neither in significant amount. **Recommend:** drop unless you've seen one — this is the clearest regional-completeness candidate in the file.

---

## Fishing (3 species — all Lake Sequoyah)

This whole tab depends on the Lake Sequoyah scope decision above. Assuming you keep the lake in scope:

### ✅ Keep — all three

- **Largemouth Bass** — primary target species
- **Crappie** — prose hedges with "likely present" — fine for the lake
- **Bluegill** — universal

If you drop Lake Sequoyah from scope, the fishing tab disappears entirely. Recommend keeping the lake in scope and being explicit about the framing in the card subtitle ("Lake Sequoyah · ~6 mi away" or similar).

---

## Summary

| Tab | Keep | Verify | Consider removing |
|---|---|---|---|
| Birds (16) | 13 | 3 (Broad-winged Hawk, Belted Kingfisher, Great Blue Heron) | 0 |
| Amphibians (12) | 8 | 4 (Fowler's Toad, Marbled Salamander, Slimy Salamander, Two-lined Salamander) | 0 |
| Snakes (12) | 3 | 8 | 1 (Eastern Hognose Snake) |
| Lizards (5) | 3 | 1 (Ground Skink) | 1 (Six-lined Racerunner) |
| Fishing (3) | 3 (if lake in scope) | 0 | 0 (or all 3 if lake out of scope) |
| **Total** | **30** | **16** | **2** |

**Strongest "consider removing" cases** — only two entries clearly fail the depth filter on the data's own evidence:
1. **Eastern Hognose Snake** (snakes) — prose admits the habitat mismatch
2. **Six-lined Racerunner** (lizards) — prose admits the elevation limit

**Verification cluster** — 16 species are habitat-plausible but worth your "have I actually seen this?" check. Most likely outcome: confirm most, drop a few you've never observed.

**Scope decision needed:**
- Lake Sequoyah in or out → affects 5 species total (2 birds, 3 fishing, possibly 1 snake)
- Recommend in, with explicit framing

---

## Process recommendation

I'd suggest one of two paths:

**Path 1 — Quick triage session:** you and I sit with this audit, you answer the verification questions species by species. ~20–30 minutes. End with a precise drop-list. Then I make the edits in one focused commit per file, with you reviewing the diff before push.

**Path 2 — Async:** I leave this doc, you mark up ✅/❌/Maybe next to each ❓ entry on your own time, and we do the data edits as a separate pass later.

Both work. Path 1 is faster if you have the headspace this week; Path 2 fits better if you'd rather move on to Phase 1 cleanup first and come back to this when your wildlife observation memory is fresh.

**Either way: no edits to JSON files or viewer.html `*_DATA` constants until you sign off on the drop list.**

---

*— Existing wildlife audit · 2026-05-18*
