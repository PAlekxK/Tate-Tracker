# map-region-smoothing · Making the zone map read as one drawn map, not 23 traced ones

- status: **RESEARCH + RECOMMENDATION. Not a queued row.** Paul reads this and decides whether it becomes one.
- raised: [paul-stated 2026-09-04 ~1:54 PM ET] — voice memo, `.private/voice-memos/2026-09-04-1354-map-region-smoothing.txt`
  ⚠️ whisper transcript = a model read. Substance is used; nothing below is stamped as a verbatim ruling.
- lane: B of the 2026-09-04 parallel run (`.plans/contracts/lane-b-map-smoothing.md`)
- scope: **polygon topology.** NOT image quality — BACKLOG §478 owns resolution/shadows/tiles and is a different defect.
  A perfect basemap would not close a single gap measured below.
- writes: this file only. No code, no geometry, no `zones.json`.

---

## 1 · The ask, and the acceptance criterion

Paul: the regions have *"some little gaps,"* they are *"not always smooth,"* he wants something **automated and
iterative**, he asks whether contour lines / elevation / a visual read of landscape shapes could refine the
boundaries, and he says explicitly **don't reinvent the wheel — look at what's already out there.** He also takes
part of it himself: *"a lot of that is on me for the vertices I've selected."*

And the frame that decides everything else:

> accuracy is bounded by the margin of error of satellite, GPS and pixels anyway — past that,
> **the remaining job is just making it clean.**

⭐ **That sentence is the specification, and it is a strong one.** It says the goal is *not* accuracy. Below the
record's own ±9.1 m trace budget there is no truth left to recover, so every option here must be judged on whether
it makes the map **read** better while **provably changing no claim** the record makes about the ground. That is a
much easier bar than "get the boundaries right" — and it is the bar this plan is written against.

⛔ It also disqualifies the reflexive answer. *"Retrace more carefully"* fails on his own terms: it spends real
effort chasing precision the instrument cannot deliver, and it treats the cause as carelessness when the
measurements below say it is mostly **model** and **render**.

---

## 2 · Most of this is already built, and one ruling already exists

**Read this section before proposing anything.** Two commits on 2026-08-31 already did the obvious work, and one of
them already ruled against the obvious next step.

| Already shipped | Where | What it means for this plan |
|---|---|---|
| **Vertex snapping in the tracer** — a click within 11 *screen* px takes an existing vertex EXACTLY | `badf097`, `tools/area-trace.html` `findSnap()` / `SNAP_PX=11` | Snapping is solved **going forward**. It does nothing for geometry traced before it existed. |
| **Chaikin smoothing as a VIEW, never a write** (`Smooth` / `S` toggle) | `b661d59`, `tools/area-trace.html` `chaikin()` | Smoothing already exists as a render-time transform, with a verified property: stored vertices byte-identical before and after. |
| **The overlap measurement that reframed the problem** — 87% of all overlap was The Path, a *line* modelled as a polygon | `badf097` commit body | The defect class "this isn't a tracing error, it's a modelling error" is already established here. |
| **The deferral itself, recorded in the data** | `zones.json` `_meta.sharedBorders` | *"Adjacent zones were traced independently, by eye, with no vertex snapping… Deferred deliberately (Paul, 2026-08-31): border smoothing and snapping come after the zones exist, not before. Do not read a gap between two zones as unclaimed ground."* |

⭐ **So this is not a new problem. It is a deliberate deferral coming due**, and Paul's memo is the trigger the
deferral was waiting for. Treat it that way in the BACKLOG row, if it becomes one.

⭐⭐ **And the ruling in `b661d59` binds anything proposed here:**

> *"It is inside the noise, so it corrects nothing — it only looks better. Baking it in would overwrite what Paul
> actually clicked with an interpretation of it… smoothing each polygon independently would PULL APART the vertices
> that snapping just made identical."*

Both halves are still true, and §6 below adds a third reason with a number attached.

⚠️ **One inconsistency, flagged not fixed.** `_meta.sharedBorders` says *"no vertex snapping."* That is now false:
snapping shipped the same day and **58 distinct coordinates are exactly shared across 20 zone pairs** (§3). The
note is stale in the safe-looking direction — it under-reports how much shared structure the record already has.
It is a one-line correction to a field this lane does not own; hand it to whoever next writes `zones.json`.

---

## 3 · What the 23 zones actually measure

All numbers below are computed from `zones.json` at HEAD (schema v3, 2026-09-01), projected to local metres about
34.5496° N. **23 zones · 437 vertices · 1,706 m of drawn boundary · 10,681 m² (2.64 acres) · every one `status: draft`.**

**a. The outlines are over-vertexed relative to the accuracy that produced them.**

| | |
|---|---|
| median segment length | **2.57 m** (p10 0.82 m, max 21.7 m) |
| record's own positional budget (`_meta.accuracyHonesty`) | **±9.1 m** |
| segments shorter than 2 m | **166 of 437 (38%)** |
| vertices turning >60° off straight | **93 of 437 (21%)** |
| worst case | `the-bluff`: **46 vertices** around a 65 m perimeter enclosing 95 m² — 1.4 m spacing |

⭐ **This is the mathematical statement of "not smooth."** The boundary is sampled every ~2.5 m with ~9 m of error
per sample. A sequence like that is a random walk, and a random walk *must* look ragged — the wobble is not a bad
day at the mouse, it is the instrument's noise made visible by drawing every sample as a corner. Paul's *"a lot of
that is on me"* is generous and largely wrong: **you cannot hand-click a boundary at 1.4 m spacing off a 0.6 m/px
shadowed January aerial and get a smooth line.** No amount of care fixes an over-sampled noisy signal; you sample
it less, or you filter it.

**b. Half the map's boundary is a shared border, whether or not the record says so.**

| within… of another zone's edge | length | share of all boundary |
|---|---|---|
| 0.5 m | 531 m | **31%** |
| 1.0 m | 704 m | **41%** |
| 2.0 m | 897 m | **53%** |
| 3.0 m | 1,050 m | **62%** |

**c. The gaps and overlaps, by class.**

| class | count | examples |
|---|---|---|
| pairs whose boundaries **touch or overlap** (distance 0) | **24 pairs** | `the-green`↔`the-turf`, `house`↔`main-parking`, `pond-area`↔`the-turf` |
| **slivers** — a visible gap under 1 m | **11 pairs** | `lower-40`↔`lower-parking` 0.13 m · `st-francis-garden`↔`stable-grounds` 0.14 m · `eastern-patio`↔`st-francis-garden` 0.17 m · `fern-garden`↔`eastern-patio` 0.33 m · `lawn`↔`house` 0.34 m · `house`↔`hosta-garden` 0.50 m · `western-garden`↔`the-turf` 0.62 m · `western-garden`↔`the-green` 0.74 m · `lawn`↔`pond-area` 0.80 m · `western-upper-patio`↔`main-parking` 0.83 m · `lawn`↔`main-parking` 0.90 m |
| gaps 1–3 m | 13 pairs | `the-bank`↔`main-parking` 1.25 m, `western-upper-patio`↔`western-lower-patio` 1.89 m … |
| **exactly shared coordinates** (snapping already worked) | **58 coords across 20 pairs** | `the-bluff`↔`western-lower-patio` 8 · `the-green`↔`the-turf` 7 · `pond-area`↔`the-turf` 6 · `house`↔`main-parking` 5 |
| **degenerate** — zero-length segments (duplicate consecutive clicks) | **5** | `western-garden`[16] · `western-lower-patio`[15] · `the-bluff`[45] · `lower-40`[7] · `the-meadow`[32] |

**d. ⭐ The finding that kills the obvious fix: 9 of the 11 slivers are vertex-to-EDGE, not vertex-to-vertex.**

| pair | edge gap | nearest vertex↔vertex | closest approach is |
|---|---|---|---|
| `lower-40` ↔ `lower-parking` | 0.13 m | 0.20 m | **vertex-to-edge** |
| `st-francis-garden` ↔ `stable-grounds` | 0.14 m | 0.28 m | **vertex-to-edge** |
| `eastern-patio` ↔ `st-francis-garden` | 0.17 m | 0.44 m | **vertex-to-edge** |
| `fern-garden` ↔ `eastern-patio` | 0.33 m | 0.33 m | vertex-to-vertex |
| `lawn` ↔ `house` | 0.34 m | 0.83 m | **vertex-to-edge** |
| `house` ↔ `hosta-garden` | 0.50 m | 0.66 m | **vertex-to-edge** |
| `western-garden` ↔ `the-turf` | 0.62 m | 0.74 m | **vertex-to-edge** |
| `western-garden` ↔ `the-green` | 0.74 m | 0.74 m | vertex-to-vertex |
| `lawn` ↔ `pond-area` | 0.80 m | 1.09 m | **vertex-to-edge** |
| `western-upper-patio` ↔ `main-parking` | 0.83 m | 1.71 m | **vertex-to-edge** |
| `lawn` ↔ `main-parking` | 0.90 m | 1.45 m | **vertex-to-edge** |

The tracer's snap — and every hand-rolled "snap nearby points together" anyone would write next — matches
**vertex to vertex**. On 9 of these 11 the nearest thing is the *middle of the neighbour's segment*, where there is
no vertex to take. **Vertex snapping cannot close most of the gaps that are actually showing.** Closing them needs
vertex-to-*edge* snapping, which means inserting a vertex into the neighbour's ring — i.e. editing a zone Paul did
not touch. That is a coverage operation, not a cleanup pass, and it is why §5's tools exist.

**e. ⭐ And a bigger snap tolerance makes it catastrophically worse — measured, not feared.**

Transitive vertex clustering at tolerance *t* over all 437 vertices:

| tolerance | resulting nodes | largest cluster | max distance a vertex moves |
|---|---|---|---|
| 0.25 m | 365 | 3 | 0.12 m |
| 0.50 m | 351 | 5 | **0.47 m** |
| 1.00 m | 285 | 15 | 2.12 m |
| 2.00 m | 171 | **119** | **20.13 m** |
| 3.00 m | 102 | **174** | **23.25 m** |

At 2 m a single cluster swallows **119 of 437 vertices** and drags points **20 m**. The cause is chaining: with a
median spacing of 2.57 m and a p10 of 0.82 m, a tolerance near the spacing lets clusters walk down a dense ring
and merge the whole boundary into one point.

⛔ **So "snap at the ±9.1 m trace budget" — the intuitive move, since that is the stated accuracy — would destroy
the map.** Snap tolerance is bounded by *vertex spacing*, not by *positional accuracy*, and here that ceiling is
**~0.5 m**. Any plan that names a tolerance must name this constraint beside it.

---

## 4 · The gap question, which is the actual decision

**Are adjacent zones meant to share edges?** Everything else follows from the answer, and it is Paul's to give.

The record currently says *no* by construction and *maybe* by content. `zones.json` holds 23 **independent rings**;
nothing declares adjacency; `_meta.sharedBorders` says explicitly *"Do not read a gap between two zones as unclaimed
ground."* Yet 41% of boundary length sits within a metre of a neighbour, 58 coordinates are already exactly shared,
and `partOf` (schema v3) already admits that zones have structural relationships to each other.

**Two models, and they are genuinely different products:**

**Model A — a POLYGONAL COVERAGE (shared-edge / topological).** The border between two zones is stored **once**, as
one edge that both reference. Gaps and overlaps become *structurally impossible* rather than cosmetically closed;
smoothing and simplification act on the shared edge, so neighbours can never separate. This is what GIS calls a
coverage, and it is what TopoJSON, GRASS, TIGER/Line and OpenStreetMap's way model all encode.
- ✅ Permanently closes the class. Fixes Paul's complaint at the root and cannot regress.
- ✅ Makes the illustrated-map row (BACKLOG) far cheaper — a drawn map of a coverage has clean seams for free.
- ⛔ **It is a schema change**, and a substantial one: `vertices` stops being the primary record. `zone-save`,
  `area-trace.html`, `zone-capture.html`, `kml-to-zones.py`, `zones-to-kml.py`, the viewer's renderer and
  `ZONES_DATA` re-inline all read rings today.
- ⛔ **It asserts adjacency the record has never established.** Two zones sharing an edge is a *claim about the
  ground* — that they abut with nothing between them. On this property that is often false: there are paths,
  walls, beds and untended strips between named places. Forcing a coverage would silently annex them.

**Model B — INDEPENDENT RINGS, cleaned and rendered well** (today's model, repaired). Keep 23 rings; fix the
degenerate vertices; close the 11 named slivers by explicit, reviewed edits; and do the rest at **render time**.
- ✅ No schema change, no migration, nothing downstream breaks.
- ✅ Honest: a gap stays a gap unless someone decides it should not be.
- ⛔ Cosmetic. Nothing prevents the next traced zone from opening a new sliver.
- ⛔ Every fix is per-pair and manual — the opposite of the *automated and iterative* Paul asked for.

⭐ **The honest read of the middle:** most of Paul's *visible* complaint is Model B work, and the durable answer is
Model A. But **Model A is blocked on something the record does not have** — a statement of which zones abut which.
Adjacency cannot be derived from proximity: `lawn`↔`house` at 0.34 m and `western-garden`↔`the-green` at 0.74 m
look identical to a distance test, and only Paul knows whether either pair actually touches on the ground or has a
bed, a walk or a drop between them. **Geometry proposes, Paul rules** — the rule `zones.json` v3 already states for
`partOf`, and the same rule applies here.

✅ **ANSWERED IN PART, AND IT SETTLES THE PREMISE** `[paul-stated 2026-09-04, asked in-lane with the 11 pairs and
their gap distances in front of him]`:

> **"Some do have a wall or a trail or a strip of nothing, and some don't."**

⭐ **This upgrades the per-pair recommendation from CAUTION to EVIDENCE, and that is a change in the grade of the
claim, not a rewording.** §7 Tier 2 step 6 previously said "review each pair" as a *method* hedge — the safe posture
when you cannot tell. It is now a *fact about the ground*, stated by the only person who can state it: the 11 slivers
are a genuine mix. ⛔ Therefore **no global tolerance pass is safe at any value.** "Close every gap under 1 m" would
silently weld shut a wall, a trail, or a strip of open ground — and the geometry is identical either way, so nothing
downstream would ever flag it.

⭐ **It also independently vindicates `_meta.sharedBorders`'s own warning** — *"Do not read a gap between two zones
as unclaimed ground."* The **"strip of nothing"** case is exactly that, and it is **neither an abutment nor a
defect**: it is real ground no zone claims. A cleanup that closed it would not be fixing a sliver, it would be
**inventing a boundary**.

⚠️ **STILL OPEN: which pair is which.** That is a map question, not a memory question, and it should not be answered
from recall. ⛔ **But it may not be answerable from imagery either** — the 11 gaps are 0.13–0.90 m on a 0.6 m/px
basemap, so **several are sub-pixel**, and a rendered zoom would look authoritative while carrying no information
about whether a wall is there. An exhibit built on the NAIP base alone would be a confidently-wrong instrument.
The lidar hillshade is the only candidate that could carry a wall or grade break the photo cannot — but §478's
3DEP coverage for Pickens County is **recorded as unconfirmed**, and at ~1 m posting it is a *shadow* answer, not a
*resolution* answer, so it may still not resolve a sub-metre feature. **Honest possibility to hold: some of these
pairs are not decidable from any imagery obtainable, and are settled only by standing there.** If that is where the
lidar check lands, it belongs here as a stated limit, not as a question anyone keeps re-asking Paul.

⚠️ **And there is a third thing in the way, already on the BACKLOG:** the record has **one geometry, the polygon**,
and paths / walls / the driveway are **lines**. A coverage built before lines exist would have to model The Path as
either an area (the mis-modelling `badf097` already found and refused to bake in) or as *nothing* — and "nothing"
means two zones sharing an edge where a path actually runs. **Lines-in-the-schema is a prerequisite for Model A,
not an adjacent nicety.**

---

## 5 · Prior art — what is already out there

Paul asked not to reinvent the wheel. Nothing below needs inventing; all of it is standard, and most of it is a
CLI away.

**Coverage cleaning and topology-preserving simplification (this is the wheel).**

- **PostGIS ≥ 3.4 / GEOS ≥ 3.12 coverage functions.** `ST_CoverageInvalidEdges` returns the *specific edges* where a
  set of polygons fails to be a valid coverage — non-overlapping and edge-matched. `ST_CoverageSimplify` simplifies a
  coverage using a **Visvalingam–Whyatt variant** while *preserving coverage topology*, so shared edges stay
  consistent. `ST_CoverageClean` and `ST_CoverageUnion` round it out. This is exactly the problem, solved, by people
  who named it first. Cost: it means putting the zones through PostGIS, which this repo does not run.
- **mapshaper** (Matthew Bloch) — the same capability with **no database**. It detects topology on import by finding
  coordinates that are **exactly shared** between features, stores each shared boundary once as an *arc*, and
  simplifies/dissolves/clips the arc once so neighbours cannot separate. `-simplify` (Visvalingam, with
  `prevent-shape-removal`), `-clean` with `gap-fill-area=` (fills gaps under an area threshold, keeps larger ones as
  real holes), and `snap`/`snap-interval=` for pre-alignment. Node CLI, reads/writes GeoJSON.
  ⭐ **Its topology rule is the exact shape of our data:** 58 of our coordinates are exactly shared and would be
  detected as arcs immediately; the rest are "misaligned" in mapshaper's own vocabulary and need `snap` first —
  bounded at ~0.5 m by §3e.
- **GRASS GIS** `v.clean` (`tools=snap,break,rmdupl,rmarea,rmsa`) — a topological vector model natively; `rmdupl`
  alone removes the 5 degenerate vertices, `rmsa` removes small angles. Heavier install than the job warrants.
- **JTS/GEOS `CoverageValidator` / `CoverageSimplifier` / `CoverageGapFinder`** — the library layer under the PostGIS
  functions, if this ever wants to be a repo tool rather than a one-off.
- **ArcGIS geodatabase topology** rules *"Must Not Have Gaps"* / *"Must Not Overlap"*, and **ArcInfo's cluster
  tolerance** — the 1970s-vintage origin of the term **sliver polygon**. Not a tool we will use; useful because it
  names the classes and shows the constraint-based framing (declare the rule, let the engine enforce it) that
  Model A is.

**Simplification (fewer vertices — this is the one that fixes "not smooth").**

- **Douglas–Peucker (1973)** — perpendicular-distance tolerance. Measured on our data: **47%** of vertices survive at
  1 m, **35%** at 2 m, **28%** at 3 m. Preserves extremes; can leave spikes.
- **Visvalingam–Whyatt (1993)** — drops the vertex forming the smallest triangle with its neighbours. **Visually
  better than DP for exactly this case** (it removes wobble before it removes shape) and it is what `ST_CoverageSimplify`
  and mapshaper both use by default. **This is the right family here.**
- ⛔ **Neither is topology-aware on its own.** Simplifying rings independently separates shared borders — the same
  failure `b661d59` named for smoothing. That is *the* reason to run simplification through a coverage tool rather
  than a for-loop.

**Smoothing (same vertices, softer path).**

- **Chaikin corner-cutting (1974)** — already implemented in the tracer. Measured on the current 23 zones: it moves
  the drawn curve a **median of 0.10 m** from the original vertices (p90 0.55 m, max 2.79 m) — far inside ±9.1 m.
- **PAEK** (ArcGIS *Smooth Polygon*) and **Bézier interpolation** — the same idea with a tolerance parameter.
- **Cubic B-spline / Catmull–Rom**; the R **`smoothr`** package packages Chaikin, spline and KS smoothing.
- ⚠️ **New finding, and it is why smoothing must stay a view even more firmly than `b661d59` said.** Chaikin is
  **area-biased inward on small, few-vertex, convex rings**: `western-fern-azalea-garden` **−10.5%**, `house`
  **−7.7%**, `hosta-garden` **−6.1%**. The *displacement* is trivially inside the noise, but the *area* is not —
  and area is a derived claim this record already publishes per zone. **Baking Chaikin in would silently shrink the
  smallest zones by up to a tenth while every distance check said "inside the budget."**

**Rendering (free, changes no data at all).**

- SVG `stroke-linejoin: round` + `stroke-linecap: round`; a small `paint-order`/casing; and — the biggest one here —
  **`stroke-dasharray`**. Today every one of the 23 zones renders `is-draft` (`viewer.html` `.pmap-zone.is-draft`,
  dash `10 7`), because **all 23 are `status: draft`**. A dashed outline advertises every corner and makes a 0.3 m
  sliver read as a deliberate opening. The draft-honesty rule that put it there is correct and must not be reversed
  by an agent — but *"the map is entirely dashed"* was already flagged as an unintended consequence in BACKLOG
  ("ALL 10 zones are draft, so the whole map now reads dashed"), and the population has since grown to 23.

**Terrain-derived boundaries** — see §6.

---

## 6 · Can terrain data draw the boundaries? Mostly no, and here is the honest read

Paul asked about contour lines, elevation, and reading big landscape shapes from the overhead imagery. The instinct
is sound — these *are* regions of landscape, so physical indicators should exist — but the answer splits sharply.

**What we have:** USGS 3DEP lidar, 2018, already pulled and rendered to byte-identical bounds with the NAIP basemap
(`images/property-map/lidar-hillshade-2018.png`, `lidar-slope-2018.png`). Free, no licence gate, and **no shadows at
all**, since lidar is an active sensor. Its posting is **~1 m**.

**The techniques that exist:** slope-break / breakline extraction from a DEM; curvature-based terrain segmentation;
geomorphon classification (GRASS `r.geomorphon`); watershed delineation (D8 flow accumulation, GRASS `r.watershed`,
TauDEM); and image-side segmentation of the aerial itself (SLIC superpixels, OBIA). All real, all standard.

**Where it would genuinely work — and it is a short list:**
- **`the-bank`** and **`the-bluff`** are named for terrain. A bank and a bluff *are* slope breaks: a 1 m DEM
  resolves a 2–4 m grade change cleanly, and a slope-break trace would likely be **more accurate than Paul's
  hand-trace**, not merely smoother. `the-bluff` is also the worst-vertexed zone in the record (46 vertices, 95 m²).
- The **pond margin** — water is flat and lidar returns it distinctively.
- Possibly the **retaining wall** line, which is a linear feature and belongs to the lines work anyway.

**Where it cannot work, and this is most of the map:**
- **A garden bed edge is not a terrain feature.** `hosta-garden` (16 m²), `western-lower-patio` (14 m²),
  `fern-garden` (43 m²) are defined by *what is planted*, by mulch, by mowing. The ground under them is continuous.
  No DEM at any resolution contains that boundary, because the boundary is not in the ground.
- **~1 m posting is not a resolution answer.** Several zones are ~4 m across. A 1 m grid gives them four cells.
- ⛔ **The 2018/2026 date problem, already ruled.** BACKLOG: *"that patio and area we have kind of reshaped with
  heavy equipment"* — a mismatch between a traced area and the terrain is **first evidence of work done since 2018**,
  not evidence of a tracing error. *"Do not snap or auto-correct polygons to the lidar."* An automated terrain-fit
  would fight that ruling on every regraded surface, invisibly.
- ⚠️ Reading landscape shapes off the aerial (segmentation) inherits §478's defects wholesale — it would segment the
  **shadows**, which at 32° sun elevation are the strongest edges in the image.

⭐ **The verdict, and it is a reframe worth keeping:** terrain is **evidence for a handful of specific zones**, and
those are exactly the ones whose *names* are terrain words. It is not a boundary engine for the map. And a terrain
fit that succeeded would improve **accuracy** — which Paul's own criterion says is already at its floor. It does not
answer *"make it clean."*

⛔ **Do not build a terrain-fit pipeline for this row.** If `the-bank` and `the-bluff` are worth re-deriving from
the hillshade, that is a **two-zone, Paul-gated, one-off** with the 2018-vs-now caveat attached to each — not an
automated pass.

---

## 7 · Recommendation

**Do the render tier now; do the data tier as one reviewed pass; hold the schema decision for Paul.**

The ordering is not caution for its own sake — it is the acceptance criterion applied literally. Paul asked for the
map to look clean. **Tier 1 is entirely look, changes no stored coordinate, and is where most of the visible win is.**

⭐⭐ **CONFIRMED — IT IS THE VIEWER'S MAP** `[paul-stated 2026-09-04, in the session that raised this]`. Asked
whether he was looking at the viewer or the tracer, Paul: *"it was the viewer's map."* Three consequences, and the
last one is the finding:

1. **"Turn on the smoothing that already exists" is NOT available.** The Chaikin toggle lives in
   `tools/area-trace.html` and renders nothing on `viewer.html`. Tier 1 step 2 is a real (small) build, not a
   default flip.
2. **Tier 1 is now the whole near-term answer, and its confidence goes up.** Every one of the three things that
   make a noisy polyline read as ragged is present *and unmitigated* on the surface he was looking at: miter joins
   on 93 sharp turns, no corner-cutting, and a dashed stroke on all 23 zones. The tracer has two of the three
   fixed; the viewer has none. That is a straightforward explanation of why the map looks worse than the tool that
   drew it.
3. ⭐ **The real finding: the 2026-08-31 work landed on the AUTHORING surface and never reached the READING one.**
   Snapping and smoothing were both built into the tracer, both verified, both correct — and the map Paul and Mom
   actually open got neither. This is the shape `CLAUDE.md` already names about `/ux-sweep`: *a capability the loop
   cannot reach by running its own procedure is not a capability the loop has.* Here it is one step worse — the
   capability exists, is proven, and is pointed at the wrong surface. **Whatever ships from this plan, the check
   is "does it render on `viewer.html`," never "does the tracer do it."**

### Tier 1 — render only. No data write. (small)
1. **`stroke-linejoin: round`, `stroke-linecap: round`** on `.pmap-zone`. Removes the miter spikes on the 93
   sharp turns. One CSS declaration, zero data risk.
2. **Chaikin (2 iterations) at render time in the viewer**, mirroring `b661d59`'s tracer implementation and its
   proof obligation: assert the stored array is byte-identical before and after. Median curve displacement 0.10 m,
   which is 1% of the record's own budget. ⛔ **Render only** — §5's area-shrink finding is the third independent
   reason never to write it.
3. **Revisit the dash on a map where 23 of 23 zones are draft.** ⚠️ The honesty rule stays; this is a question about
   *how* provisionality is carried when it is universal, and it is **Paul's authoring call, not an agent's** — the
   BACKLOG row already anticipated it. Options for him: confirm the zones he actually trusts (which is the real fix,
   and it is a `status` edit, not a geometry one); or carry draft-ness by fill weight alone with a solid rounded
   stroke. Whichever way — one dashed zone among 22 solid ones says something; 23 of 23 say nothing.

⭐ **Tier 1 alone is likely to close most of Paul's complaint**, because rounded joins plus corner-cutting plus a
non-dashed edge remove exactly the three things that make a noisy polyline read as ragged. **Do it first and let
him look before spending anything on Tier 2.** That is also what makes the work *iterative* in the sense he asked
for: a render transform can be tuned, toggled and reverted with no migration.

### Tier 2 — a single reviewed data pass, proposed as a diff. (medium)
4. **Delete the 5 zero-length segments.** Pure degeneracy, no information, no judgment. The one unambiguous write.
5. **Simplify with Visvalingam–Whyatt through a coverage-aware tool** (mapshaper: `snap snap-interval=0.5` →
   `-simplify` → `-clean gap-fill-area=`), **at a tolerance Paul picks from rendered exhibits**, not from a number in
   a document. `/design-options` is the existing mechanism for exactly this and should be used: show him the same
   map at DP/VW ~0.5 / 1 / 2 m beside today's.
   ⚠️ **Simplification IS a write and it does change the record**, unlike Tier 1 — so it needs the honest framing:
   at 1 m tolerance it discards 53% of the vertices as noise. That is defensible *because* the noise is ±9 m, but it
   is a claim, and the `history` entry must say so.
   ⛔ **Never run a per-ring simplifier in a for-loop** — it separates the 58 already-shared coordinates.
6. **Close the 11 named slivers explicitly**, as a reviewed list, not a global tolerance. §3d says 9 of 11 need
   vertex-to-edge insertion — a coverage tool does this; a snap loop cannot.
   ⛔ **NOT a judgment call any more — a RULING.** `[paul-stated 2026-09-04]` *"Some do have a wall or a trail or a
   strip of nothing, and some don't."* The 11 are a mix, so **there is no tolerance at which a global pass is
   correct**; a per-pair verdict from Paul is a hard prerequisite, and any pair he has not ruled on stays open
   rather than being closed by default. See §4. ⚠️ And do not assume the verdicts can be collected from a screen —
   several gaps are sub-pixel on the current basemap.
7. ⛔ **Snap tolerance is capped at ~0.5 m and the cap is measured** (§3e). Any value near the ±9.1 m accuracy
   budget collapses the map. Whatever ships, this number belongs in a comment beside it with the table.

### Tier 3 — hold for Paul. (large; do not start)
8. **Model A, the polygonal coverage.** Blocked on two things that are Paul's and one that is the BACKLOG's:
   an **adjacency statement** (which zones abut, which have something between them — undecidable from geometry),
   the **lines-in-the-schema** work (a coverage without lines forces paths and walls to be either areas or nothing),
   and a schema migration touching seven consumers. ⭐ **Worth it eventually** — it is the only option that makes
   the defect structurally impossible rather than periodically cleaned — but it should follow the lines work and
   Paul's adjacency call, not lead them.

### Cost
Tier 1 is a CSS line, a ~15-line render function and an exhibit — small, and reversible by deleting it. Tier 2 is
mostly *review*, not code: a node dependency (mapshaper) used once, a proposed diff, and Paul reading exhibits.
Tier 3 is a schema migration and should be scoped separately when its prerequisites land.

### What would make this iterative, which is what he actually asked for
A `tools/check-zone-topology.py` in the session-start block — reporting slivers, overlaps, degenerate segments and
over-vertexed rings as **numbers that move**, flagging and never editing. That is the mechanism this repo already
trusts, it makes the next traced zone's sliver visible the day it appears, and it is the honest form of *automated*:
the detection automates, the fix stays gated. ⚠️ Do not build it before Paul rules on §4 — a checker that reports
"gap" needs to know whether a gap is a defect, and today the record says it is not.

---

## 8 · What I could not verify

- ~~**Whether Paul's complaint is about the viewer's map, the tracer's map, or both.**~~ ✅ **ANSWERED
  `[paul-stated 2026-09-04, same session]`: "it was the viewer's map."** See the box below — it removes an option
  and hardens Tier 1.
- **I did not render anything.** Every number here is computed from coordinates; none is a look at the map. The
  claim *"Tier 1 closes most of the complaint"* is reasoned from what makes polylines read as ragged — it is a
  hypothesis, and the exhibit in Tier 2 step 5 is what would test it.
- **Which zones actually abut on the ground.** Named as §4's blocking decision. Not derivable, not guessed.
- **The lidar's real usefulness on `the-bank` / `the-bluff`.** I did not open `lidar-hillshade-2018.png` or the
  slope raster; the assessment is from the sensor's ~1 m posting and the zones' sizes, not from looking.
- **Tool version claims.** `ST_CoverageSimplify` (PostGIS 3.4 / GEOS 3.12, Visvalingam variant, topology-preserving),
  `ST_CoverageInvalidEdges`, and mapshaper's exact-coordinate topology detection + `-clean gap-fill-area=` +
  `snap-interval=` are from vendor docs read 2026-09-04, **not from running either tool**. GRASS `v.clean` flags,
  JTS `CoverageSimplifier`, ArcGIS PAEK and `smoothr` are cited from knowledge and are **not** re-verified here.
- **The `_meta.sharedBorders` "no vertex snapping" line is stale** (§2) — reported, not fixed; this lane does not
  own `zones.json`.
- **Whether any downstream consumer reads zone area or slope.** If per-zone acreage or slope is published anywhere,
  the Chaikin area-shrink finding (§5) becomes a correctness issue and not merely a caution. Not traced.

## 9 · What this lane did NOT do

No code. No geometry write. `zones.json`, `viewer.html`, `tools/area-trace.html`, `BACKLOG.md` and `property.json`
untouched — read only. No BACKLOG row created; §478 not merged with this, and not re-litigated. No terrain pipeline
built. No tolerance chosen: every number above is a measurement or a bound, and the value that ships is Paul's pick
off an exhibit.

Sources for §5's verified claims: [ST_CoverageSimplify](https://postgis.net/docs/ST_CoverageSimplify.html) ·
[ST_CoverageInvalidEdges](https://postgis.net/docs/ST_CoverageInvalidEdges.html) ·
[mapshaper — Topology and cleaning](https://mapshaper.org/docs/guides/topology.html) ·
[mapshaper — Simplification](https://mapshaper.org/docs/guides/simplification.html) ·
[mapshaper — Command reference](https://mapshaper.org/docs/reference.html)
