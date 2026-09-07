# Map design — what the discipline already knows

- **status:** RESEARCH. Mine, done at Paul's instruction `[paul-stated 2026-09-06]`:
  *"go online and do research about best practices in maps... don't over-rely on my little map,
  it's just, like, a little local festival."*
- **why it exists:** the proposal's visual language was argued from **one genre sample** — the Grant
  Park Summer Shade Festival map — which Paul correctly declined to let carry the weight. This file
  replaces that with cited practice. ux-expert is separately re-grounding its own §3.
- **method:** web research 2026-09-06. **Every claim below is VERIFIED against a source** unless
  marked RECALLED. Sources at the foot.

---

## 1 · ⭐⭐ THE FINDING — Lynch's five elements are the schema, and four seats derived them independently

**Kevin Lynch, *The Image of the City* (1960).** People build mental maps of a place out of five
elements: **paths · edges · districts · nodes · landmarks.** His organising concept is **legibility** —
*"the ease with which its parts can be recognised and can be organised into a coherent pattern."*

⭐ **And the cartographic reduction is exactly our schema question:**
> *"If represented in a cartographic map, the five elements can be put into three categories:
> **points** (nodes and landmarks), **lines** (paths, edges), and **polygons** (districts)."*

**Four independent derivations of the same three primitives, tonight and over the last week:**

| who | reached it from | what they said |
|---|---|---|
| **Paul**, 2026-08-31 | standing on his own land | *"It's a wall. More of a dividing line than a zone."* / *"the path is a landmark, not a zone."* |
| **Paul**, 2026-09-04 voice | thinking about annotations | *"specific points where specific projects or repairs happened, or a shut-off valve is"* |
| **engineering-partner**, tonight | the storage boundary | `geometry: {kind, coordinates}` — one record shape, **three validators** |
| **ai-advisor**, tonight | the capability scan | *"§12 is an independent argument for lines-and-points in the schema"* |
| **Lynch**, 1960 | how humans actually hold a place in mind | points · lines · polygons |

⭐ **This is not a schema convenience. It is a cognitive model with 65 years behind it**, and it gives
the primitives their names and their rationale. It also stops us inventing a taxonomy.

### ⛔ And it explains a defect the record already has
Two of Mom's sixteen names are **not districts**:
- **"Fairway Border"** — *border* is an edge word. She named an **edge**.
- **"The Path"** — a path. It is currently stored as a **17-vertex polygon** reporting a meaningless
  acreage.
- And *"Upper-Uber Wall Area"* — the record straining to say **edge** in a vocabulary that only has
  *district*. Paul ruled it a wall.

**A polygon-only schema cannot record two of the five things people use to hold a place in their
heads.** That is the argument for lines and points, stated better than any of us stated it.

---

## 2 · The view-mode question, which is Paul's own

He raised it: *"you can look at Google Maps and say they've got all these different views that serve
different purposes."* **Google Maps ships four base types** (Maps JavaScript API, verified):

| type | what it is | the job |
|---|---|---|
| `roadmap` | drawn map with labels | general navigation and reference |
| `satellite` | photorealistic aerial | *what is actually there* |
| ⭐ `hybrid` | **satellite imagery WITH drawn labels on top** | both at once |
| `terrain` | physical/topographic | elevation, natural features, hiking |

⭐⭐ **THE CORRECTION THIS FORCES.** The proposal currently recommends a **two-state toggle, "Photo" /
"Drawn."** Google does not offer two states — it offers **three**, and the third is the one most
people actually use for looking at their own property: **imagery underneath, drawn names on top.**

**That maps onto our problem exactly.** The measured defect at 414px is not that the aerial is
present; it is that **the drawn layer is too weak to read against it** — 6px labels, 49 collisions,
0.08-alpha fills that do not render. **Hybrid is not a compromise between photo and drawn; it is a
distinct product with its own design job**, and it is probably our default rather than either pure
state.
⚠️ Note also that `terrain` is a *separate* type, not an overlay — which supports the record's
existing instinct that the lidar hillshade is a layer, not a blend.

---

## 3 · Generalization — the discipline for "show less so it reads"

**Töpfer's Radical Law / Principle of Selection (Töpfer & Pillewizer, 1961/1966)** is a *mathematical*
rule for how many features from a source map should survive into a smaller-scale derived map. The
standard generalization operations are **elimination · simplification · aggregation · collapse**.

⭐ **`collapse` is the operation nobody here has named, and it is the one we need.** It converts a
feature to a lower dimension when it is too small to resolve — **a polygon becomes a point or a
line.** Measured in this record: **nine zones under 50 m², 2.8–6.6 m across, which is 5–11 pixels on
the trace frame.** At default zoom those nine should not be polygons at all. They should be points.

⚠️ **And this reframes the smoothing work.** *Simplification* (fewer vertices) is one of four
operations and it is the one the 09-04 plan chose. **Elimination and collapse were never considered**,
and on this data they are the ones that pay — because the problem is not that the outlines are noisy,
it is that we draw 23 features at every scale regardless of whether they can be resolved.

> **The durable statement: the map should show a different number of things at different zooms.**
> Today it shows 23 at all of them.

---

## 4 · Labels — Imhof, and why ours fail

**Eduard Imhof's name-placement rules (1962)** are still the canonical source, and contemporary GIS
implements them directly (Esri's Maplex engine). His fundamental rules: names should be **legible**;
**easily associated** with their feature; **not overlap other map content**; placed to **show the
extent** of the object; **reflect hierarchy** through differing type styles; and be **neither densely
clustered nor evenly dispersed**. He also gave the **five-position model** for point labels, with
**top-right preferred** for left-to-right languages.
⚠️ Imhof himself noted these rules are **routinely violated because satisfying one breaks another** —
so this is a constraint-solving problem, not a styling choice.

**Measured against ours, at 414 × 848:** legible — **no**, 6px rendered. Non-overlapping — **no**, 49
colliding pairs. Hierarchy through type style — **no**, one style for all 23. Densely clustered —
**yes**, worst exactly where the gardens are.
**Four of six rules broken.** And `viewer.html` has **no label-fit test of any kind**; the fit rule
lives only in the tracer and tests fit *within its own polygon*, never collision with a neighbour.

---

## 5 · Colour — a hard ceiling we are far past

**ColorBrewer (Brewer & Harrower) and the categorical-colour literature:** beyond **8–9 classes**
readers stop reliably matching colour to a legend; **7 is the commonly recommended safe maximum**; the
eye discriminates about **12 hues** at best; and for colour-vision-deficient readers, qualitative
schemes **cannot exceed 4 classes.**

⛔ **We have 23 zones. A colour per zone is not available at any quality.**
✅ **But the fix is already latent in the data:** zones carry a `type` — `planted` · `turf` ·
`structure`, plus water and woods as obvious additions. **That is 4–6 classes, comfortably inside the
ceiling, including for colour-vision-deficient readers.**

> **Fill encodes TYPE. The NAME identifies the place.** Exactly what the discipline permits, and it
> independently confirms ux-expert's type-based-fill recommendation.

---

## 6 · The genre standard, and an honest limit on it

**NPS Harpers Ferry Center** is the closest published standard to our problem — place maps for
non-expert visitors, produced since 1970, with the **Unigrid** system (Massimo Vignelli, 1977):
uniform fold, **shaded relief**, consistent colour range, and a stated **placement hierarchy**. They
publish **236 map symbols** and their stated philosophy is customisation by park rather than one
template — *"just as every park is different, so too are park maps."*

⚠️ **What I could NOT verify:** the detailed `map-standards.pdf` is a scanned/binary PDF and did not
yield readable rules. So the specifics — line weights, exact palettes, type specs — are **not
sourced**, and the HTML pages carry philosophy rather than specification. **Do not cite NPS for a
specific numeric standard on my evidence.** The symbol set and Unigrid are real and verified; the
granular rules are not, from me.

⛔ **And the honest limit on the whole discipline for our case:** essentially every cartographic
standard assumes **surveyed or authoritative source data.** Ours is hand-traced off a shadowed
0.6 m/px January aerial with a stated budget worse than ±30 ft. **So the craft transfers and the
epistemics do not.** Where professional practice would draw a crisp line because its source is
crisp, we must not — which is why the EDGE/SEAM/REFUSAL language is still needed *on top of* the
standards, not replaced by them.

---

## 7 · What this changes in the proposal

1. ⭐ **Lines and points get a name and a citation.** Not "Paul asked for annotations" but *the record
   cannot hold two of the five elements people use to think about places.* Strengthens ruling #4.
2. ⭐ **The two-state toggle is probably wrong.** Google's `hybrid` says the answer is likely
   **imagery + a strong drawn layer as the default**, with pure-drawn and pure-photo as the
   alternates. Revises §6-A step 2.
3. ⭐ **Add `collapse` and `elimination` to the geometry work** — nine zones should be points at
   default zoom. This is cheaper and higher-value than further vertex simplification, and it is the
   operation nobody proposed.
4. **Fill encodes type, not identity** — forced by the 7-class ceiling, and already supported by the
   `type` field the data carries.
5. **Labels are a constraint-solving problem with a canonical rule set**, not a styling pass, and
   `viewer.html` has no fit test at all.
6. **Scale-dependent rendering** becomes a first-class requirement rather than a nicety: *show a
   different number of things at different zooms.*

---

## Sources
- [NPS Harpers Ferry Center — map information](https://www.nps.gov/subjects/hfc/map-information.htm) ·
  [NPS cartography](https://www.nps.gov/carto) ·
  [Harpers Ferry Center (Wikipedia — Unigrid/Vignelli)](https://en.wikipedia.org/wiki/Harpers_Ferry_Center) ·
  [CLUI on HFC](https://clui.org/newsletter/winter-2024-47/harpers-ferry-center)
- [Google Maps JavaScript API — Map Types](https://developers.google.com/maps/documentation/javascript/maptypes)
- [Kevin Lynch's 5 elements](https://www.architecturecourses.org/design/kevin-lynchs-5-elements-city-guide-urban-design) ·
  [Computing the Image of the City](https://arxiv.org/pdf/1212.0940) ·
  [A computational approach to 'The Image of the City'](https://www.sciencedirect.com/science/article/pii/S0264275118309776)
- [Töpfer's Radical Law, applied](https://www.isprs.org/proceedings/XXXVIII/part4/files/Wilmer.pdf) ·
  [The Principles of Selection (Töpfer & Pillewizer, 1966)](https://www.tandfonline.com/doi/abs/10.1179/caj.1966.3.1.10) ·
  [Map generalization notes](https://dspmuranchi.ac.in/pdf/Blog/MAP%20GENERALISATION.pdf)
- [Label placement — PSU GEOG 486](https://courses.ems.psu.edu/geog486/node/557) ·
  [Automated names placement (Imhof's rules restated)](https://cartogis.org/docs/proceedings/archive/auto-carto-9/pdf/automated-names-placement-in-a-non-interactive-environment.pdf) ·
  [From Top-Right to User-Right (Imhof's 5-position model)](https://arxiv.org/pdf/2407.11996)
- [ColorBrewer.org paper](https://www.cs.rpi.edu/~cutler/classes/visualization/S18/papers/colorbrewer.pdf) ·
  [ColorBrewer scheme types](https://colorbrewer2.org/learnmore/schemes_full.html) ·
  [Colour for categories (EU data-viz guide)](https://data.europa.eu/apps/data-visualisation-guide/colour-for-categories)
