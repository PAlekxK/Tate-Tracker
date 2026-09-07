# ai-mapping-capability · What AI can actually do to turn imagery of a place into usable zones

- kind: scan
- status: **RESEARCH + RECOMMENDATION. Not a queued row.** Paul reads this and decides whether it becomes one.
- seat: ai-advisor, commissioned directly by Paul 2026-09-06. Given ownership of the AI half.
- raised: [paul-stated 2026-09-06, voice] *"doing research on what mapping capabilities exist already from
  images… how easy and seamless we can make this process… taking advantage of AI and everything else at our
  disposal."* Plus the 2026-09-04 memo on reading contour/elevation/big shapes from overhead footage.
- amended mid-session: [paul-ruled 2026-09-06] **short term, WE draw and THEY confirm** — see §0b.
- writes: **this file only.** No code, no geometry, no `zones.json`, no BACKLOG row, no deploy, no commit.
- extends, does not re-derive: `.plans/2026-09-04-map-region-smoothing-PLAN.md` §6 · `LAND-SOURCES.md` ·
  `GOOGLE-EARTH-NOTES.md` · `BACKLOG.md` §BASEMAP & LAND-DATA SESSION.

⭐ **Read in two parts.** **Part I (§1–§9)** answers the original question — what AI can do and where it may sit.
**Part II (§10–§13)** is the wide scan Paul commissioned mid-session: **every view of a property obtainable from
an address** (§10), **whether image recognition can draw the founding features** (§11), **the starter vocabulary
of a place** (§12), and **the overstep line, tiered** (§13). §12a carries the number he asked for.

---

## 0 · The answer in one line

> **Imagery can propose an EXTENT. Only a person can supply an IDENTITY.**

Everything below is that line with numbers attached. The models are good enough — today, off the shelf, on
Paul's laptop — to propose where the hard surface, the roof, the water and the woods/open line are, for any US
address, in minutes. **None of them can propose that a strip of ground is called "The Bank,"** and on this
property the names are the product. `.plans/2026-08-31-zones-traced-with-mom.json` holds sixteen names a person
gave unprompted; not one is derivable from a pixel.

⭐ **That is Paul's own ceiling, stated back with a measurement:** *"there's a limit to what AI can do because it
relies on knowledge of the land and the property."* Correct, and §5 draws the line precisely.

---

## 0b · The ruling that re-prices everything `[paul-ruled 2026-09-06]`

> *"For the short term let's focus on you and I defining the zones and presenting them for confirmation."*
> Reasons: the demographic is **older and less tech-friendly**; mobile-first drawing is hard unless heavily
> automated; and **AI is limited because it relies on knowledge of the land.**

⭐ **The AI's user is now an OPERATOR in a terminal, not a householder on a phone.** Three consequences, and they
change the shape of this scan rather than trimming it:

1. **Heavy techniques come into scope.** A 2.4 GB model, a QGIS plugin, a 40-second encode pass, a GPU rental, a
   paid API call — all fine when one operator runs them once per household. None of that was affordable on a
   consumer capture surface.
2. ⭐ **Most of the AI-boundary tension dissolves by construction.** A polygon a model proposes to an operator who
   accepts or rejects it *is* draft-for-approval, which the boundary explicitly permits. The boundary's hard
   clause — *the administrator's eyes sit between the model and the estate's people* — is satisfied by the
   workflow itself, not by a control someone has to remember. §4 still states where each step sits, because "it
   is obviously fine" is how a boundary erodes.
3. ⚠️ **It moves the risk rather than removing it.** The failure mode is no longer *a model wrote to canon*; it is
   ***a plausible machine polygon gets confirmed by a householder who is being agreeable.*** An older, less
   tech-confident person shown a finished-looking map will say yes. That is the same instrument problem as
   `q-clematis-variety` asking Mom to read a flower colour on a day the vine had none — **a confirm surface
   manufactures a confirmation.** §7 names the countermeasure.

---

## 1 · The measurement that decides this whole scan

Computed from `zones.json` at HEAD, projected to local metres about 34.5496° N. **23 zones · 10,681 m².**

| | zones | share of zones | area | share of area |
|---|---|---|---|---|
| **the two field zones** (`the-meadow` 4,764 m², `the-turf` 3,117 m²) | 2 | 9% | 7,882 m² | **74%** |
| the mid zones (50–800 m²) | 12 | 52% | 2,525 m² | 24% |
| ⭐ **the small planted zones (<50 m²)** | **9** | **39%** | **275 m²** | **2.6%** |

The nine small ones, with their **short** dimension:

`western-lower-patio` 4.8×5.0 m · `hosta-garden` 4.9×4.4 m · `western-fern-azalea-garden` 10.4×**2.8** m ·
`western-garden` 13.4×5.1 m · `western-upper-patio` 9.6×**3.3** m · `the-green-terrace` 12.5×4.0 m ·
`fern-garden` 13.1×**3.8** m · `st-francis-garden` 10.1×6.0 m · `eastern-patio` 9.4×6.6 m

⭐⭐ **This is the labour split as a number, and it is the single most useful thing in this document.**
**Automation can plausibly propose 74% of the AREA in two polygons, and cannot touch 39% of the ZONES.** The
field zones are large, texture-distinct, and defined by a physical process (mowing) a sensor can see. The nine
small ones are 2.8–6.6 m across their narrow axis — **5 to 11 pixels on the 0.6 m NAIP frame the zones were
traced on** — and are defined by what is planted, which is a human decision about ground, not a discontinuity in it.

⚠️ **So a scan that reports "SAM segments aerials well" would be answering the wrong question.** The right
question is *how well does it do on a 3 m-wide bed*, and the answer (§5) is: worse than Paul, at any resolution,
for a reason that is not about resolution.

---

## 2 · The capability table

**VERIFIED** = vendor/primary doc read or benchmark paper read **today, 2026-09-06**. **RECALLED** = from
knowledge, not re-checked. ⛔ **Nothing here was run.** No model was downloaded, no API called, no raster fetched.
Every row is a capability claim, not a result at this address.

### 2a · Interactive segmentation — a click becomes a polygon

| technique | produces | resolution / accuracy floor | cost | on a phone? | maturity |
|---|---|---|---|---|---|
| **SAM 3** (Meta, released 2025-11-19; SAM 3.1 since) — concept prompts: short noun phrases + image exemplars, segments **all** instances | masks for every instance of a concept | inherits the raster's; documented failure on unclear edges, low colour contrast, small objects | free weights, custom **SAM License** (research + commercial, with restrictions) | ⚠️ int8 ONNX browser builds exist (FP32 was ~3.5 GB); operator-side is the sane place | **production** — VERIFIED |
| **SAM 2 / SAM 1** point + box prompts | one mask per prompt | same | free | yes, via ONNX Runtime Web / WebGPU | production — VERIFIED |
| ⭐ **Geo-SAM** (QGIS plugin) — **encode the raster once, then click in milliseconds on a laptop CPU**; outputs pixel-level or simplified polygons straight to a vector layer | georeferenced polygons | raster's | free, open source | no — desktop | **production** — VERIFIED |
| **GeoOSAM** (QGIS plugin) — SAM 2.1 **and SAM 3** with text prompts, vector ROI, similar-object detection | same | raster's | free | no | published plugin — VERIFIED it exists; performance RECALLED |
| **samgeo / segment-geospatial** (opengeos) — Python; SAM v1/v2/v3, FastSAM, HQ-SAM, LangSAM; point / box / **text** prompts on georeferenced rasters | GeoJSON / vector | raster's | free; GPU strongly preferred for batch, CPU workable interactively | no | mature, widely taught — VERIFIED |

⭐ **Geo-SAM's architecture is the one that matters here:** the expensive image encoder runs **once per raster**,
then every click is a cheap decoder pass. That is precisely the operator workflow — encode Fernwood's basemap
once, then adjudicate 23 zones at conversational speed. No GPU rental, no service, no data leaving the machine.

### 2b · Already-derived vector data — geometry with zero drawing

| source | produces | floor | cost | maturity |
|---|---|---|---|---|
| **Microsoft US Building Footprints / GlobalMLBuildingFootprints** — 130M+ US buildings; MS-stated **99.3% precision / 93.5% recall**; refreshed through Aug 2026 (Vexcel-derived adds in Jul 2026) | house + outbuilding outlines | machine-derived from imagery; roof outline, not foundation | free (ODbL) | production — VERIFIED (dataset); ⛔ **LEAD at this address — not queried** |
| **Overture Maps** — buildings **GA** (2B+ footprints, monthly), base theme (land cover / land use / water), divisions **GA**, addresses **alpha** | footprints + coarse land cover + water | building GA; land cover coarse | free, GeoParquet on AWS/Azure | production — VERIFIED |
| ⭐ **Regrid** — **159M parcels, 3,229 counties, 99% of Americans**, sourced from county assessors; match by **lat/lon, address or APN**; CSV/SHP/KML export | **the property boundary** + owner, land use, deed | county-assessor quality (varies wildly) | **paid** | production — VERIFIED (covers Pickens Co. GA) |
| **county qPublic / Schneider** (Pickens Co. GA is on it) | same, one county at a time | same | free | ⛔ **does not generalize** — a per-county web app, not an API |
| **OpenStreetMap** | roads, some buildings, water | volunteer; rural residential is usually empty | free (ODbL) | production — RECALLED |

⭐ **`BACKLOG.md` is right that the property boundary is missing from every source in this repo — and this is
a BUY, not a BUILD.** Regrid is the only path that works for an arbitrary US address. qPublic answers Fernwood
and nothing else.

### 2c · Rasters — what the ground actually looks like

| source | produces | resolution | cost | maturity |
|---|---|---|---|---|
| **USDA NAIP** via Planetary Computer STAC (already wired: `tools/fetch-basemap.py`) | multi-date RGB+NIR ortho, **public domain, redistributable** | 0.6 m (1.0 m pre-2019) | free | **proven in this repo** — VERIFIED |
| ⭐⭐ **Google Solar API `dataLayers`** — one call per lat/lon returns GeoTIFFs: **RGB at 0.1 m/px** and **DSM at 0.1 m/px** (fixed, regardless of tier), plus flux/shade | shadow-free **surface model** + 10 cm nadir photo | **HIGH** = low-altitude aerial @0.1 m; MEDIUM = high-altitude @0.25 m; BASE = satellite @0.25 m | **~$0.075 per call**; ⛔ **30-day cache limit** (§4) | production — VERIFIED (docs); ⛔ **coverage at this address UNVERIFIED — rural 404s are documented** |
| **Esri World Imagery / WorldView-3** — already measured in `LAND-SOURCES.md` | 0.31 m source, **8.47 m stated placement accuracy** | z19 ceiling (0.246 m/px) | free to display, ⛔ not redistributable | proven in repo — VERIFIED |
| **Google Earth Web** — 16+ captures 1985→2025, URL-addressable date | best leaf-off frame that exists here (2018-04-12) | fixed raster per screenshot (~0.45 m/px at 700 m) | free to display, ⛔ not redistributable | proven in repo — VERIFIED |
| **USGS 3DEP lidar 1 m DEM** (already pulled for this property) | bare-earth DEM, hillshade, slope — **active sensor, no shadows** | ~1 m posting | free, public domain | proven in repo; ⚠️ **CONUS coverage is expanding, not complete — must fail loudly** |

### 2d · Land cover and vegetation — the honest resolution floor

| source | produces | resolution | verdict at lot scale |
|---|---|---|---|
| ⛔ **Chesapeake Conservancy 1 m land cover** | 1 m LULC, ~91% vs ground | 1 m | ⛔ **DOES NOT COVER GEORGIA.** It is the Chesapeake Bay watershed + adjacent counties. Fernwood is in the Coosa-Tallapoosa / Gulf drainage (`LAND-SOURCES.md`). Excellent product, wrong hemisphere of the country. — VERIFIED |
| **NAIP-CHM — 0.6 m canopy height + structure, CONTIGUOUS US**, from NAIP 2012–2023 (96% from 2022–23) | canopy height nationwide at 0.6 m | 0.6 m | ⭐ **strongest lead in this table** for the woods/open line at any US address. 2025 preprint — RECALLED/LEAD, availability not checked |
| **Meta + WRI 1 m Global Canopy Height** (DINOv2 on 0.5 m Maxar, trained against ALS) | canopy height, global | 1 m, **MAE 2.8 m** | usable for **woods vs open**; ⛔ useless for tree-vs-shrub-vs-lawn. Imagery 2018–2020. — VERIFIED |
| **Dynamic World / Sentinel-2** | 9-class near-real-time LULC | **10 m** | ⛔ `western-lower-patio` (4.8×5.0 m) is **a quarter of one pixel** |
| **NLCD** (thematic, % impervious, % canopy) | national land cover | **30 m** | ⛔ the entire mapped estate is ~12 pixels |
| **NDVI from Sentinel-2** | greenness | 10 m | ⛔ same wall; see §3c for the version that *does* work |

⭐ **The floor is blunt: below ~1 m there is no free national land-cover product, and above ~1 m nothing on this
property is resolvable.** Everything useful at lot scale is either (a) NAIP/lidar you classify yourself, or
(b) the 0.1 m Google Solar layers, which are paid and cache-limited.

### 2e · VLMs reading an aerial

| capability | verdict |
|---|---|
| **Naming what is in a tile** — "driveway, mown field, planted bed, pond" | plausible and useful **as a caption**, not as geometry |
| ⛔ **Placing a boundary / returning coordinates** | ⛔ **DISQUALIFIED, with a number.** The best RS-tuned VLM in the VRSBench evaluation reaches **49.8% grounding accuracy at IoU 0.5**, and GPT-4V-class models are documented to hallucinate on aerial content. **A coin flip on whether a box even half-overlaps the thing it names.** — VERIFIED |
| **Reading a rendered map and critiquing it** ("this polygon's edge follows a shadow, not a bed") | ⭐ the genuinely good VLM seat — see §3b |

⚠️ **This is the row most likely to be re-proposed by a future session, so it gets the strongest statement:**
*a VLM is a competent reader of a picture and an incompetent surveyor of one.* Use it to **label and to
critique**, never to **locate**.

### 2f · Phone-side capture

| technique | verdict at property scale |
|---|---|
| **Apple RoomPlan** | ⛔ out. Parametric **room** scans; the API is indoor by design |
| **iPhone Pro LiDAR** | ⛔ out outdoors. **~5 m effective range**, and **direct sunlight overwhelms the IR return** — the sensor cannot see its own pulses. Shade works, sun does not. — VERIFIED |
| **Photogrammetry (Polycam / RealityScan / KIRI)** | works outdoors in daylight, but produces an **unreferenced mesh**: no georeference without ground control, and property-scale coverage is a long capture. Wrong output shape — we need a plan, not a model |
| ⭐ **Walk-the-boundary GNSS** | **the only phone technique that survives contact with this property.** Dual-frequency smartphone under forest canopy: **DRMS 4.56 m**; ~**2.5 m** with PPP where canopy openness R>0.7; sub-metre needs survey-grade gear. — VERIFIED |

⭐ **Read the GNSS number against this record's own budget: `zones.json` `_meta.accuracyHonesty` is ±9.1 m.**
A walked boundary at 2.5–4.6 m is therefore **better than the instrument that drew the current map** — for
`the-meadow` (135 m across). For `hosta-garden` (4.9 m across) a 4.6 m error is the whole zone. And the site
premise binds absolutely: **no cell, Wi-Fi only near the house, and coverage falls off exactly where the
interesting ground is.** Any walk tool captures fully offline and syncs on return, or it is not a candidate.

---

## 3 · The moves that actually change the product

Two, plus one finding that is new evidence against §6 of the smoothing plan.

### 3a · ⭐ MOVE 1 (operator, now) — encode once, click 23 times, propose a diff

**Stand up promptable segmentation over the frames this repo already registers, as a PROPOSAL LAYER in
`tools/area-trace.html`, and never as a writer to `zones.json`.**

Concretely: **Geo-SAM or GeoOSAM in QGIS**, or **samgeo** in a notebook, run against a registered frame; export
candidate rings as GeoJSON; load them into the tracer beside Paul's existing vertices; he accepts, edits or
rejects each one. The polygons come out in WGS84 **for free**, because this repo already solved the hard part —
every frame is registered to one byte-identical georeference, and `zones.json` v2 stores real coordinates rather
than image fractions.

**Why this one:**
- It is exactly *"automated and iterative"* — encode is one pass, clicks are milliseconds, nothing is committed.
- It replaces **437 hand-clicks at 2.57 m median spacing** with ~23 prompts. The smoothing plan already proved
  the hand-click density is the *source* of the raggedness (a random walk sampled every 2.5 m with ±9 m of
  error), so a machine-proposed boundary is not merely faster — **it removes the mechanism that made it ragged.**
- ⛔ **But not for all 23.** Expect it to earn its keep on `the-meadow`, `the-turf`, `lower-parking`,
  `stable-grounds`, `main-parking`, `house`, `pond-area` — large, high-contrast, physically bounded — and to be
  **worse than Paul** on the nine small beds (§1, §5). **Score it that way from run one:** per-zone accept /
  edit / reject, not an overall impression. A technique that wins on 8 of 23 and is honest about the other 15 is
  a good technique.

**The prerequisite probe, and it is 10 minutes:** ⭐ **check Google Solar `dataLayers` coverage at
34.5496, −84.3674.** If it returns **HIGH**, this property gains a **0.1 m RGB and a 0.1 m shadow-free DSM** —
6× the NAIP basemap and 10× the lidar posting — and §5's floor moves materially. If it 404s or returns BASE, we
have learned that in one call and the answer is NAIP + the 2018 leaf-off Earth frame. ⚠️ Read §4's licence
clause before the call, not after.

### 3b · ⭐ MOVE 2 (engine, for a stranger) — the derived shell, assembled deterministically

**Address in → a confirmable draft out, from public sources only, with zero local knowledge.** Full spec in §6.
The AI content is deliberately thin: this is mostly **deterministic assembly of already-derived vector data**,
because that is what makes it repeatable in minutes for household N+1 rather than a research arc.

⭐ **The one AI seat worth adding to it** is not segmentation — it is **a VLM as a critic of the assembled draft**,
run before a human ever sees it: *"this region's edge follows a shadow"* · *"this polygon spans the driveway and
the lawn"* · *"the footprint and the parcel disagree."* That is the §2e row VLMs are actually good at, it produces
**flags for the operator**, never geometry, and it fits the repo's strongest existing pattern —
`AI flags, humans clear`.

### 3c · ⭐ A NEW FINDING — mowing regime is a TIME-SERIES signal, and §6 only looked at single frames

`.plans/2026-09-04-map-region-smoothing-PLAN.md` §6 correctly concludes that **terrain** cannot draw a bed edge,
and that segmenting **the aerial** would segment the shadows. Both hold. But it evaluated the imagery as *one
picture*, and this repo has **seven NAIP dates and 16+ Google Earth dates over the same ground**.

⭐ **`the-turf` and `the-meadow` are not distinguished by what they are — both are grass — but by how often they
are cut.** `zones.json` `_meta` says so in its own retirement note: *"A meadow is mown once or twice a year;
frequently mown grass is a lawn."* **Mowing frequency is invisible in one frame and is exactly what a multi-date
stack measures**: a mown surface has low, stable texture and reverts within weeks; an unmown one accumulates
height and heterogeneity through a season and shows up in a canopy-height / texture differencing pass.

**So the honest amendment to §6 is narrower and more useful than "mostly no":**
- terrain (a static DEM) draws **terrain-named** zones — unchanged, §6 stands;
- a **multi-date** stack can propose the **management-named** zones — turf vs meadow vs woods — which is
  **74% of the mapped area**;
- neither draws a bed edge.

⚠️ **This is a hypothesis with a cheap test and it must not be reported as a capability.** The test: take the
seven NAIP dates already on disk, difference NIR/NDVI texture inside `the-turf` vs `the-meadow`, and see whether
the boundary Paul drew shows up as a signal. **If it does not, say so and delete this section.**
⛔ And the 2018-vs-now caveat that governs the lidar governs this too: a difference is **first evidence of work
done**, not evidence of a bad trace.

### 3d · Two things NOT to build (and why they will be re-proposed)

- ⛔ **A VLM that outputs coordinates.** §2e. It looks like the obvious use of a vision model and it is a coin flip.
- ⛔ **An automated terrain-fit pipeline.** Already ruled in the smoothing plan §6 and unchanged by anything here.
  A terrain fit improves **accuracy**, which Paul's own criterion says is already at its floor, and it would
  silently fight the *"regraded since 2018"* ruling on every reshaped surface.

---

## 4 · Where each step sits against the AI boundary

The binding rule, from `CLAUDE.md` as amended 2026-09-02: *AI never touches an estate's people or their words. It
may only draft for approval on the way in, or analyze the record on the way out — **the administrator's eyes sit
between the model and the estate's people**, both directions.* Plus: **capture stays deterministic and AI-free**;
**deterministic things need a non-AI door**; **model reads are hypotheses until a deterministic source or a human
confirms them.**

| step | class | where the human gate is | verdict |
|---|---|---|---|
| Fetch NAIP / lidar / footprints / parcel | **deterministic capture** — no model in the path | none needed | ✅ allowed, and it is the **non-AI door**: the map must be reachable without invoking a model |
| SAM proposes a candidate ring | **draft-for-approval on the way in** | ⭐ **the operator accepts, edits or rejects PER ZONE** in the tracer before anything is written | ✅ allowed **only** with the per-zone gate |
| VLM captions / critiques an assembled draft | **analysis of the record on the way out** | operator reads flags; flags are never geometry | ✅ allowed |
| ⛔ SAM output written to `zones.json` by a script | — | — | ⛔ **OUT. Nothing a model proposes may become geometry without a human accepting that specific ring.** Replaced by: a **proposal layer** in `area-trace.html` plus the existing `zone-save` path, so the accept **is** the write |
| ⛔ Model-derived zone shown to a householder as settled | — | — | ⛔ **OUT.** It reaches her as a question, dated, revisable, and labelled as a guess — the honesty-marker rule this record already runs on |
| ⛔ A model naming a zone | — | — | ⛔ **OUT, and it is the ceiling itself** (§5). A name is a fact about a household |
| ⛔ A model reading a householder's words to refine geometry | — | — | ⛔ **OUT** — the INGRESS clause. Paul relays; the model does not fetch |

⭐ **The mechanical form of the gate, because a prompt-level rule is not a control** (this is the standing
tool-boundary principle): **the segmentation tool must not have a write path to `zones.json` at all.** It emits
GeoJSON to a scratch/proposal location. The only writer stays the human-driven save. That way the boundary is
enforced by what the tool *can address*, exactly as the one-environment plan's attenuated KV handle enforces
tenancy — *a handler cannot address another household because the handle it holds cannot name one.*

⭐ **Provenance is not optional and this record already has the vocabulary.** Every zone carries `status`
(`draft`/`confirmed`/`flagged`) and a `history` log. A machine-proposed, human-accepted ring is **a different
object** from a hand-traced one and must say so in `history` — *"proposed by <tool/model/version> from
<frame, date>, accepted by <person> on <date>."* Without it, six months from now nobody can tell which
boundaries a model drew, and `AI verification flags, never clears` has no surface to act on.

⚠️ **One licence clause is load-bearing and is not mine to settle.** Google Maps Platform terms permit caching
Solar API Building Insights and Data Layers for **up to 30 consecutive calendar days**, after which the cached
Solar Data must be deleted (with a carve-out for data incorporated into fixed media for a downstream
transaction). **This repo's existing posture handles the raster fine** — display-only, gitignored `.local/`,
never `_meta.baseImage`, same class as Esri and Google Earth. **What it does not settle is whether a polygon
traced off that DSM is itself "Solar Data."** My read is that a human-authored WGS84 ring is a new object, not
cached content — but that is a legal judgement, **Paul's call, not an agent's**, and it should be made before the
first call, not after 30 days of drift.

---

## 5 · The ceiling — stated as flatly as §6 states its own

**Given every source in §2, at every resolution obtainable, here is the line.**

### What imagery + models CAN propose
1. **The building.** Roof outline, from a free national dataset, without drawing.
2. **The parcel.** From an assessor record, not from a picture at all.
3. **Hard surface vs. soft.** Driveway, parking, patio, roof — strong albedo and texture contrast, and in a 0.1 m
   DSM a height discontinuity.
4. **Water.** Flat, spectrally distinct, and lidar-distinctive.
5. **Woods vs. open.** Canopy height, shadow-free, at 0.6–1 m nationally.
6. **Mown vs. unmown** — *hypothesis*, §3c, cheap to test.
7. **Terrain-named regions** — a bank, a bluff, a pond margin: a slope break is genuinely in the DEM.

### ⛔ What no imagery contains, at any resolution
1. ⭐ **The name.** *"The Bank," "The Green," "The Bluff," "Fern Garden."* Sixteen of them, given unprompted by
   one person in one session, and every one is a fact about how a family uses ground.
2. ⭐ **Whether a 0.3 m gap between two zones is a wall, a trail, or a strip of nothing.** Ruled by Paul:
   *"Some do have a wall or a trail or a strip of nothing, and some don't."* **Nine of the eleven measured
   slivers are 0.13–0.90 m — sub-pixel on the 0.6 m basemap** and *at* the pixel on a 0.1 m one. Higher
   resolution helps this one; it does not close it, because the three cases can look identical from above.
3. **`partOf` containment.** Already ruled: *geometry proposes, Paul rules* — `the-green` tests only 60% inside
   `the-turf`, which the ±9.1 m budget can neither confirm nor refute.
4. **Which of two adjacent mown areas is which** — a management fact, not an appearance one.
5. **What changed since the frame was flown.** The 2018 lidar predates the regrading. A disagreement is evidence
   of *work done*, and only a person knows which.
6. ⭐ **Where a bed's edge is *meant* to be.**

### ⭐ On the brief's own challenge: *is "a bed edge isn't in the ground, so it isn't in the imagery" still true at 0.1 m?*

**Partly false, and the correction is worth having — but it does not move the ceiling.**

**Where §6 is too pessimistic:** at 0.1 m, a **mulched** bed edge is one of the strongest texture and albedo
edges on a residential lot, and a **raised** bed, a wall or a terrace lip **is** in a 0.1 m DSM — a 20 cm rise is
two pixels of height, where the 1 m lidar could not see it at all. `western-upper-patio`, `western-lower-patio`
and `the-green-terrace` are exactly the class a 0.1 m surface model would resolve and a 1 m DEM cannot. **So the
correct statement is not "a bed edge is not in the imagery." It is: *a mulch-or-masonry edge is in a 10 cm
image; a mow-line edge is a decision, and decisions are not in any image.***

**Where §6 is exactly right, and it is the part that governs:** the failure on the nine small zones is **not a
resolution failure**. SAM's documented weaknesses are *unclear edges, minimal colour distinction, small objects,
and shadow misclassification* — and a bed grading into lawn under a January canopy at 33° sun is all four at
once. More pixels give you a sharper picture of an edge **that is genuinely ambiguous on the ground**.
`hosta-garden` is 15.8 m² and 4.4 m across; where the hostas stop and the lawn starts is a question the household
answers by where they put the mower, and the honest ceiling is that **a model at 0.1 m will produce a confident,
plausible, arbitrary boundary there** — which under this record's doctrine is worse than an honestly-unsure one.

⛔ **Therefore: no automated pass over the nine small zones. Ever, on current technique.** They are 2.6% of the
area. Paul should keep drawing them, and the win is that automation frees his attention *for* them.

---

## 6 · First run for a stranger's address — what is derivable before anyone draws

**Target (per the amendment): minutes for an operator, not a session.** Fernwood took a multi-day arc because it
was *research*. Household N+1 is a *re-run*, and everything below is either already built here or a documented
endpoint.

### The pipeline

| # | step | source | cost | already in this repo? |
|---|---|---|---|---|
| 1 | address → lat/lon | US Census Geocoder (free, no key) or Nominatim | free | no — trivial |
| 2 | ⭐ **parcel boundary** | **Regrid** (159M parcels, 3,229 counties, match by lat/lon or address) | **paid — a BUY decision** | ⛔ no, and `BACKLOG` names it as the gap |
| 3 | building footprints | Microsoft US Building Footprints or Overture buildings | free | no — a spatial filter on an open dataset |
| 4 | basemap, multi-date | **NAIP via Planetary Computer STAC** | free, public domain | ✅ `tools/fetch-basemap.py` — works at any US coordinate today |
| 5 | terrain | USGS 3DEP 1 m DEM | free | ✅ path proven; ⚠️ **coverage is not universal — must report ABSENT, never empty** |
| 6 | canopy / woods line | NAIP-CHM 0.6 m (lead) or Meta+WRI 1 m | free | no |
| 7 | water + flood | USGS NHD / WBD + FEMA NFHL | free | ✅ both queried successfully at Fernwood |
| 8 | *optional* 0.1 m RGB + DSM | Google Solar `dataLayers` | ~$0.075/call, **30-day cache limit**, may 404 rural | no — §3a's probe |
| 9 | *optional* candidate regions | SAM over 4/8, operator-adjudicated | free, local | no — §3a |

### What comes out, and what it is honestly called

A frame with: **the lot outline · the house and outbuildings · the hard surface · the water · the woods/open
line** — and, if step 9 runs and the operator accepts them, a handful of large candidate regions.

⭐ **It is NOT "your map." It is *the public record of your place* — and every region on it is unnamed.**
That name matters, because it sets the householder's job correctly: she is not approving our work, she is
**telling us what these places are called and where we have it wrong.** A surface called "your map" invites a
yes; a surface called "here is what the public record says, and it doesn't know what you call anything" invites
a correction. Same geometry, opposite instrument.

⚠️ **The trap this repo has measured three times, applied here:** Esri z20 returns a valid PNG of a grey square;
Google Earth's 1985 tick renders 100% loaded and blank; the attribution date lags the header. **Every source in
the table above can return success while carrying nothing.** So the first-run pipeline must carry
**per-source VERIFIED / ABSENT status onto the artefact**, and an absent source must render as *absent*, not as
empty ground — the same `exit 3 = UNCHECKABLE, never green by absence` discipline `check-public-build.py` and
`check-estate-neutral.py` already enforce. **A first map that silently omits the parcel because the county
wasn't covered is worse than no first map.**

⚠️ **And the estate-neutrality rule binds this artefact:** a derived map for another household must carry
nothing of Fernwood's — no species, no zone vocabulary, no names. `check-estate-neutral.py` is the existing
control and should be pointed at whatever this produces.

---

## 7 · ⭐⭐ The division of labour — the actual deliverable

| | **THE MODEL** proposes | **THE OPERATOR** (Paul, terminal) decides | **THE HOUSEHOLDER** (standing there) settles |
|---|---|---|---|
| **owns** | extents | the draft | the identity |
| roof / hard surface / water / woods line | ✅ | accept · edit · reject **per region** | — |
| mown vs unmown (§3c, unproven) | ✅ hypothesis | tests it before trusting it | confirms the line is where they mow |
| the nine small beds | ⛔ **hands off** | draws them | corrects them |
| shadow artefacts, spanning polygons | flags them (VLM critic) | clears them | — |
| simplification tolerance, vertex density | — | ✅ picks from rendered exhibits | — |
| adjacency — wall vs trail vs nothing | ⛔ cannot | ⛔ cannot from a screen | ✅ **only they can** |
| ⭐ **the name** | ⛔ **never** | ⛔ never | ✅ **only they can** |
| what changed since the imagery | ⛔ | flags the disagreement | ✅ explains it |

**The rules that fall out, and they are short:**

1. **The model may propose an extent; only a person may supply an identity.**
2. **The operator's accept is the write.** No tool that proposes has a path to canon (§4).
3. ⭐ **The householder is asked to CORRECT, never to APPROVE.** This is the countermeasure to §0b's risk. An
   older, agreeable person shown a finished map says yes to all of it and we learn nothing. The surfaces this
   repo already runs on know this: name what she gave, adopt her words, never improve them, and carry
   *everything is changeable* lightly. **A confirmation surface that cannot produce a "no" has not measured
   anything** — and on lap 8's own numbers, *every affordance that asks her to answer us returned zero, and the
   one that simply moves her returned 100%.* ⛔ **Do not design this as another ask card.** Prefer instrumenting
   a door she already opens: the naming session that produced sixteen names was **a conversation over a map**,
   not a form — and it is the only n that exists.
4. **Automation buys attention, not coverage.** It should propose the 74% of area that is two field polygons so
   that Paul's hand-tracing goes where only hand-tracing works.

---

## 8 · What I did not verify

- ⛔ **I ran nothing.** No model downloaded, no raster fetched, no API called, no polygon produced. Every §2 row
  is a capability claim from a document, not a result at 34.5496, −84.3674.
- **Google Solar coverage at this address is UNKNOWN**, and rural 404s are documented by Google itself. The whole
  0.1 m argument in §3a and §5 is conditional on a probe nobody has run. ⚠️ If it returns BASE (0.25 m satellite),
  the §5 correction about mulch edges weakens considerably.
- **Regrid's price and its Pickens County data quality are unchecked.** "Sourced from county assessors" is
  Regrid's claim; assessor parcel geometry is notoriously variable and is **not a survey**.
- **Microsoft footprints were not queried at this anchor.** 99.3% precision is a national self-reported figure.
- **NAIP-CHM (0.6 m CONUS canopy) is from a 2025 preprint I did not open.** Treat as LEAD.
- **SAM 3's behaviour on 0.6 m residential aerial is RECALLED, not measured.** The failure modes I cite (unclear
  edges, small objects, shadows) come from SAM-1/2-era remote-sensing evaluations; SAM 3 may be better and I have
  no number for it. ⭐ **§3a's per-zone accept/edit/reject scoring is exactly the instrument that would settle it.**
- **The VRSBench 49.8% figure is for the best RS-tuned open model, not for current frontier VLMs.** The
  conclusion (do not let a VLM place geometry) is robust to that being conservative; the number is not a claim
  about Claude or Gemini specifically.
- **§3c (mowing as a time-series signal) is my own hypothesis and is unproven.** It has a cheap test using
  rasters already on disk. If the test fails, delete the section rather than softening it.
- **The 30-day Solar cache clause is read from Google's policy page, not from counsel.** Whether a derived
  polygon inherits it is unresolved and is Paul's call.
- **I did not look at a single image.** Not the lidar hillshade, not the 2018 leaf-off frame, not the viewer's
  map. §1's numbers are computed from coordinates; everything visual is reasoned, not seen.

**Part II additions:**
- **Nothing in §10 was queried at this address except what `LAND-SOURCES.md` already marks VERIFIED.** Every new
  row — SSURGO/SDA, NWI, TIGER, MS footprints, Regrid, EarthExplorer, the 3DEP point cloud — is a **LEAD** here.
- **The Georgia 15 cm imagery access restriction is read from the state GIO's own page**, not tested. If Paul
  ever holds a government contract the row changes.
- **3DEP's 98.3% is an end-FY2024 national figure** for "available or in progress," not a guarantee at any
  specific address, and *in progress* is not *downloadable*.
- **§11a's driveway-as-routing formulation is my own proposal and has not been implemented or evaluated
  anywhere I checked.** It is reasoned from the constraint structure, not cited.
- **§12's confidence column is judgement, not measurement.** No feature in that table has been derived and
  scored against a hand-trace. The pilot in §9 item 4 is what would replace judgement with a number.
- **§12a's ratio is my classification of Mom's sixteen names**, not hers and not Paul's. The extent/name split
  is defensible and the boundary cases (`The Green`, `Stable Grounds`, `the bank`) are arguable — the **0 of 16
  verbatim** figure is the robust one; the 9/16 and 7/16 are mine to defend.

---

## 9 · Punch list

**Cheap probes first — every one of these answers a question this document had to leave open.**

1. ⭐ **Probe Google Solar `dataLayers` coverage at the anchor** (~10 min, ~$0.075). Cheapest decisive question
   here: it moves §5's floor either way. ⚠️ Paul rules on the 30-day licence clause **before** the call.
2. ⭐⭐ **Build the CHM from the 3DEP point cloud** (DSM − DTM). `LAND-SOURCES.md` has named this as *"not yet
   built"* and *"the strongest available source for the field zones"* since 2026-09-01. It is shadow-free,
   season-free, free, and it draws the woods/open line — **74% of the mapped area** — with no model at all.
   **Highest value-to-effort item in this document.**
3. **Query SSURGO via Soil Data Access** (POST, T-SQL). The repo's soil series are **inferred and never tested**;
   this settles them and adds real polygons. A morning's work.
4. ⭐ **Run §3a on ONE zone as a pilot** — `the-meadow` or `lower-parking`, Geo-SAM over the existing NAIP frame,
   output to a scratch GeoJSON, rendered beside Paul's ring. ⛔ **Do not wire a save path.** One zone answers
   *"is this worth a workflow."*
5. **Test §3c (mowing as a time-series signal)** on the seven NAIP dates already on disk, before it is cited
   anywhere as a capability. If it fails, delete §3c rather than softening it.
6. **Decide Regrid** — buy or don't. It is the only generalizable parcel path, and §6/§10d have a hole without
   it. ⭐ It is also the **frame** every other feature sits inside.
7. **Prototype the driveway as a routing problem** (§11a) — least-cost path from the TIGER road to the building
   footprint over a drivability surface (slope + curvature + leaf-off brightness). The most interesting single
   technical idea in this scan, and it is the one that survives heavy canopy.
8. ⚠️ **Raise lines-and-points in the schema as a live row.** §12 needs three primitives and the record has one;
   the deferral that was to add lines **named its own trigger and the trigger has fired**. This scan reaches that
   conclusion independently of the smoothing plan — treat the corroboration as the signal.
9. **Only then** consider a first-run script. Items 1–8 tell you what it can honestly contain.

⛔ **Not proposed and deliberately so:** no BACKLOG row, no tool, no schema change, no householder-facing surface,
no commit. This is a scan; the pilots earn anything more.

---

# PART II — the wide scan `[commissioned mid-session, paul-stated 2026-09-06]`

> *"I want you to go and put your best effort in… there's always a limit of what we can draw without that
> person's direct input and we should not overstep on that, but you can leave it to me to fine-tune about
> what's overstepping."*

⭐ **Taken literally.** Part II proposes the full set and **marks the overstep risk on every item** (§13) rather
than pre-trimming. Nothing here is built, nothing is queued.

---

## 10 · Address in → every view of the property we can get

`LAND-SOURCES.md` does this **for Fernwood**. This section answers the harder question: **what generalises to an
arbitrary US address**, and at what cost, resolution and licence.

⭐ **The column that matters most is LICENCE**, and this repo learned why the hard way: Esri and Google imagery
are **display-only**, so they can inform a trace and can never be the shipped basemap. For a product served to
households, a source that cannot be redistributed is a source the operator may look at and the app may not show.

### 10a · Optical imagery — what the ground looks like now

| source | any US address? | resolution | cadence | cost | redistributable? | what it lets us DRAW |
|---|---|---|---|---|---|---|
| ⭐ **USDA NAIP** (Planetary Computer STAC) | ✅ CONUS | **0.6 m** standard since 2018; **0.3 m** in some states | ~2–3 yr per state, ⚠️ **not uniform — 2026 has state-level gaps** (ND explicitly not collected) | free | ✅ **public domain** | the shipped basemap; every optical feature; **4-band incl. NIR** — see §11 |
| **Google Solar `dataLayers`** | ⚠️ 472M+ buildings, **rural 404s documented** | **0.1 m RGB + 0.1 m DSM** | one epoch | ~$0.075/call | ⛔ **30-day cache limit** | walls, terraces, mulch edges, roof detail — the only cheap sub-metre surface model |
| **Esri World Imagery** (Maxar/WV-3) | ✅ | 0.31 m source; **8.47 m stated placement accuracy here** | ~annual | free to display | ⛔ no | a look; ⚠️ sharper ≠ better placed |
| **Google Earth Web** | ✅ | ~0.45 m/px per screen capture | 16+ epochs 1985→2025 here | free to display | ⛔ no | ⭐ the best leaf-off frame that exists over Fernwood (2018-04-12) |
| **State orthoimagery programs** | ⚠️ **state by state, terms vary wildly** | ⭐ Georgia: **15 cm statewide, 7.5 cm urban, includes leaf-off** | ~3 yr | free… | ⛔ **ACCESS-GATED to government employees / contractors under contract** | ⛔ nothing, for us. **Named because it is the highest-resolution leaf-off imagery that exists over this property and we cannot have it** |
| **Sentinel-2** | ✅ global | 10 m | 5 days | free | ✅ | ⛔ nothing at lot scale (`hosta-garden` = ¼ pixel). Useful only as a **phenology time series** |
| **Landsat** | ✅ global, **1972→** | 30 m | 16 days | free | ✅ | ⛔ nothing to draw; answers *"was this forest in 1985?"* |

### 10b · Imagery over TIME — the archive

| source | reach | any US address? | notes |
|---|---|---|---|
| **NAIP archive** | 2003→ | ✅ | ⭐ **7 flights over Fernwood, exactly ONE leaf-off — and that is geometry, not luck.** At 34.55° N the leaf-off window caps the noon sun near 55°, so bare trees + high sun **cannot co-occur**. This generalises with latitude and is a property of the *place*, computable before any fetch |
| **Google Earth Web** | **1985→** | ✅ | date is URL-addressable → scriptable. ⚠️ two measured traps: attribution date **lags** the header; the 1985 tick renders **100% loaded and blank** |
| **USGS EarthExplorer — Aerial Single Frames / NHAP / NAPP** | **1930s–1990s** | ⚠️ varies by area | public domain, **scanned and NOT orthorectified** — each frame needs control-point registration. ⭐ The only path to a *photograph* of land before the house |
| **USGS topoView historical topo** | **1880s→** | ✅ | free GeoPDF; 17 sheets cover this land; the 1971 1:24,000 already proves **no building at the anchor** then. ⚠️ NAD27 — a 20–40 m shift in north Georgia; for looking, not tracing |
| **Sanborn fire insurance maps** | 1860s–1960s | ⛔ **urban only** | not applicable to rural property |

### 10c · Elevation and terrain — the shadow-free instrument

| source | any US address? | resolution | cost | what it lets us DRAW |
|---|---|---|---|---|
| ⭐ **USGS 3DEP 1 m DEM** (bare earth) | ✅ **98.3% of the nation available or in progress as of end FY2024; baseline likely complete 2026** | 1 m | free, public domain | slope breaks, banks, bluffs, pads, terraces (partly), contours at any interval, drainage |
| ⭐⭐ **3DEP POINT CLOUD** (AWS Registry of Open Data, COPC/EPT) | ✅ same footprint | sub-metre point spacing | free | ⭐ **THE UNDER-USED SOURCE IN THIS REPO.** It holds `first return` and `ground` separately, so you can derive a **DSM**, a **DTM**, and a true **CHM = DSM − DTM** — plus **return intensity**, which separates water and pavement. The repo has only the finished DEM |
| **Derived rasters** (GDAL / GRASS / WhiteboxTools) | ✅ wherever a DEM exists | 1 m | free | hillshade (multi-azimuth), **slope**, aspect, **curvature**, **geomorphons** (`r.geomorphon` → ridge / slope / footslope / hollow as *named* landform classes), **watershed + flow accumulation**, **TWI** (where water collects) |
| **Google Solar DSM** | ⚠️ see 10a | **0.1 m** | ~$0.075 | walls, terrace lips, raised beds — everything a 1 m posting smears |

⚠️ **The floor, stated once:** a 1 m posting gives a 4 m-wide zone **four cells**. Terrain answers the big
questions and cannot answer the small ones.

### 10d · Parcel and legal — the frame every zone sits inside

| source | any US address? | cost | what it gives |
|---|---|---|---|
| ⭐⭐ **Regrid** | ✅ **159M parcels, 3,229 counties, 99% of Americans**; match by **lat/lon, address or APN**; CSV/SHP/**KML** export | **paid** | **the parcel polygon**, owner, land use class, deed reference, year built, sales history, lot dimensions |
| **County GIS / qPublic (Schneider)** | ⛔ **per-county web app, not an API** | free | same, for one county. ⚠️ often includes the **assessor's dimensioned building sketch** and a street-facing photo — a legal-grade footprint |
| **Census TIGER/Line** | ✅ | free, public domain | **road centerlines**, address ranges → **road frontage** |
| **State/tribal history** (e.g. GA 1832 Cherokee Land Lottery) | ⛔ state-specific | free | provenance, not geometry |

⭐⭐ **The parcel boundary is the single highest-value missing artifact, and `BACKLOG.md` already says so.** It is
the **frame**: every zone sits inside it, it bounds every search, it is the one polygon the householder already
believes in, and it is the only line on the map that is a **legal** fact rather than a photographic inference.
⛔ **It is a BUY.** qPublic answers Fernwood and nothing else; Regrid is the only path that generalises.

### 10e · Derived national layers — geometry that already exists

| source | any US address? | resolution | cost | what it lets us DRAW |
|---|---|---|---|---|
| **Microsoft US Building Footprints** | ✅ **130M+ US buildings**, refreshed through Aug 2026 | vector; MS-stated 99.3% precision / 93.5% recall | free (ODbL) | ⭐ **the house — as a download, not an inference** |
| **Overture buildings** | ✅ 2B+ global, GA, monthly | vector | free | same, plus land cover / land use / water in the `base` theme |
| **OpenStreetMap** | ✅ | vector | free (ODbL) | roads, water, some buildings; ⚠️ rural residential is usually empty |
| ⭐ **NRCS SSURGO via Soil Data Access** — REST, **T-SQL over POST**; WFS/WMS also published | ✅ nearly all US | map-unit polygons (typically acres) | free, public domain | **soil map units and series as real polygons.** ⚠️ This repo's soil series are **inferred and never tested** — SDA settles that, and `LAND-SOURCES.md` already records the failed GET probe as *"my probe being wrong, not the service."* **Low effort, high value for a gardening product** |
| **USFWS National Wetlands Inventory** | ✅ | polygons | free | wet ground; would classify the pond |
| **FEMA NFHL** | ✅ | polygons | free | flood zone (Fernwood: **Zone X**) |
| **USGS NHD + WBD** | ✅ | lines/polygons | free | streams, waterbodies, the full watershed hierarchy |
| **NAIP-CHM — 0.6 m canopy height, CONUS** | ✅ (LEAD) | **0.6 m** | free | ⭐ strongest candidate for the **woods/open line at any US address** |
| **Meta + WRI 1 m canopy height** | ✅ global | 1 m, **MAE 2.8 m**, imagery 2018–20 | free | woods vs open only |
| **NLCD / USFS Tree Canopy Cover** | ✅ | **30 m** | free | ⛔ nothing at lot scale |
| **Dynamic World** | ✅ | **10 m** | free | ⛔ nothing at lot scale |
| **USDA Plant Hardiness Zone (2023)** | ✅ | point lookup | free | a zone attribute — ⚠️ and this repo already knows the official county zone (7b) is **wrong at elevation** (6b) |
| **NOAA climate normals** | ✅ nearest station | point | free | already in this repo |

### 10f · What the public record says that is not geometry

**Building permits** (county/city — coverage poor, rarely an API) · **assessor photo + sketch** (often on
qPublic; a dimensioned structure outline) · **EPA WATERS / 303(d)** stream quality · **state geologic survey**
bedrock · **state natural-heritage / protected species** · **USFS Wildfire Risk to Communities** · **EPA radon
zone** · ⛔ **utility maps are NOT available as data** — 811 is a *request* service, not a dataset; utilities are
found from above (§11) or not at all.

### 10g · ⭐ The generalisation verdict

**Available for essentially ANY US address, free, redistributable, no model:** NAIP · 3DEP DEM + point cloud ·
building footprints · TIGER roads · SSURGO soils · NWI wetlands · FEMA flood · NHD/WBD water · historical topo ·
hardiness zone · climate normals.
**Available but PAID:** the parcel (Regrid) · 0.1 m RGB+DSM (Google Solar).
**Available but DISPLAY-ONLY:** Esri · Google Earth.
**Exists and is unreachable:** state orthoimagery at 15 cm.

⭐ **That is a lot of a place, for free, before anyone draws anything.**

---

## 11 · Can image recognition draw the founding features?

⭐⭐ **The answer that reframes the build: MOST OF THE FOUNDING FEATURES ARE NOT INFERENCES. THEY ARE
DOWNLOADS OR RASTER ARITHMETIC.**

Paul's instinct — *"some of these things are gonna be recurring and should be easy to identify, and maybe
there's pre-existing models or datasets we can leverage"* — is right, and the strong form is stronger than the
question: **the house is a file. The road is a file. The parcel is a file. The soil is a file. The wetland is a
file. Water is a one-line NIR threshold. Forest is a subtraction. A bank is a derivative.** The features that
genuinely need a *learned* model are a short list, and SAM's role is **refinement in the operator's hands**, not
the engine of the pipeline.

### 11a · Best signal per feature — and whether combining beats either alone

⭐ **Paul's specific idea — leaf-off optical × terrain — is the technically correct one, and it is strongest
exactly where he pointed it.**

| founding feature | free derived data? | best SINGLE signal | ⭐ best COMBINATION | does combining beat either alone? |
|---|---|---|---|---|
| **House / outbuildings** | ✅ **MS / Overture footprint** | the footprint file | footprint **+ DSM height jump + leaf-off optical** | ⭐ **YES, but not for accuracy — for CURRENCY.** Footprints are derived from an imagery epoch; a 2024 shed is missing from a 2021 derivation. **Footprint ⊕ DSM disagreement is a change detector**, and the disagreement is the finding |
| ⭐ **Driveway** | partial (OSM sometimes) | bright, uniform **impervious** in leaf-off optical | **leaf-off brightness + LOW slope + LOW curvature (smooth) + it must CONNECT the TIGER road to the building footprint** | ⭐⭐ **YES, decisively — and the fourth signal is topological, not spectral.** A driveway is not just a class of pixel, it is *the thing that joins the road to the house*. **Formulate it as a least-cost path over a drivability surface, not as a segmentation** — the constraint is free, it fixes canopy occlusion (the path continues under the trees), and it is exactly the case where this property's heavy cover defeats a pure classifier |
| **Parking / hardstand** | ⛔ | impervious + flat + adjacent to driveway | optical + slope + adjacency | yes; ⚠️ **gravel is spectrally close to bare soil** — the weakest hard surface |
| **Road frontage** | ✅ **TIGER** | TIGER ∩ parcel | none needed | no model at all |
| ⭐ **Water — pond / creek** | ✅ NHD | ⭐ **NIR.** Water is near-black in near-infrared, and **NAIP carries a NIR band** | NIR + lidar (flat, distinctive/low return) + NHD | ⭐ **the single most reliable test in this entire document.** Near-deterministic |
| ⭐ **Forest / woods** | ✅ NAIP-CHM (lead), Meta 1 m | ⭐ **CHM = DSM − DTM** from the 3DEP point cloud, thresholded ~2–3 m | CHM alone is nearly sufficient | ⭐ **shadow-free and season-free — it MEASURES the trees instead of photographing them.** `LAND-SOURCES.md` already names this as the strongest source for the field zones and it is still **not built** |
| **Tree line / forest edge** | derived from above | CHM boundary | + leaf-off optical to confirm | yes, marginally |
| **Open ground (lawn / field / clearing)** | ⛔ | the **complement**: inside parcel, minus canopy, minus impervious | complement + NDVI | mostly deterministic once the other two are drawn |
| ⚠️ **Mown vs unmown** | ⛔ | ⚠️ **none in a single frame — both are grass** | ⭐ **multi-date texture / NDVI stack** (§3c) | ⭐ **YES — and it is the only signal that can separate `the-turf` from `the-meadow`, which is 74% of the mapped area.** ⚠️ **UNPROVEN.** Sentinel-2's 10 m is too coarse; it must run on the **NAIP archive** |
| ⭐ **Steep ground — bank / bluff / slope break** | ⛔ | ⭐ **slope raster from 3DEP** | slope + **geomorphon classification** (names ridge / slope / footslope / hollow) | ⭐⭐ **This is Paul's point exactly: INVISIBLE in optical, OBVIOUS in lidar.** For `the-bank` and `the-bluff` a slope-break trace is plausibly **more accurate than the hand-trace**, and the smoothing plan already says so |
| **Terraces / retaining walls** | ⛔ | **0.1 m DSM** (Solar) or the raw point cloud | DSM + leaf-off optical | ⛔ **1 m DEM smears a 0.5 m wall.** Needs sub-metre or it does not exist |
| **Paths** | ⛔ | leaf-off optical, weak | + a routing constraint like the driveway | ⚠️ low confidence. And this repo already learned **The Path is a LINE mis-modelled as a polygon** — 87% of all zone overlap |
| **Specimen trees** | ⛔ | **CHM local maxima / crown delineation** | + optical crown texture | ⭐ a *solved* problem in forestry; samgeo ships a tree-mapping example. Produces **points**, which the record cannot hold today |
| **Utility corridor / overhead lines** | ⛔ | a **linear canopy gap** in the CHM; thin high returns in the point cloud | CHM + point cloud | real but niche |
| **Parcel · soil · wetland · flood · watershed** | ✅ all | the file | — | **no model. Ever.** |

### 11b · Which model, if a model is needed at all

| task | right tool | honest expectation at 0.3–0.6 m on a residential lot |
|---|---|---|
| refine an extent the operator points at | ⭐ **SAM 2/3 via Geo-SAM or samgeo** (§2a) | good on large, high-contrast, physically bounded regions; ⛔ **poor on the nine small beds** — documented failure on unclear edges, low colour contrast, small objects, and **shadow misclassification**, which at 33° sun is the strongest edge in the frame |
| find every instance of a recurring thing | **SAM 3 concept prompts** ("driveway", "pond", "roof") | ⚠️ **untested on residential aerial.** Promising and unmeasured — §3a's per-zone scoring is what would settle it |
| classify land cover wall-to-wall | a **trained classifier over NAIP 4-band + CHM + slope** (a random forest is genuinely competitive here) | ⭐ better than SAM for *cover*, because the inputs are physical, not visual. **This is the underrated option** |
| name what is in a tile | a VLM, as a **caption** | fine |
| ⛔ place a boundary | ⛔ **not a VLM** | **49.8% grounding accuracy at IoU 0.5** for the best RS-tuned model |

---

## 12 · The founding points of interest — a starter vocabulary for any place

**What this is:** the set of features that (a) exist at almost every residential/rural property, (b) are
auto-derivable to a stated standard, and (c) are worth having **before the owner says a word**.

⚠️⚠️ **THE RECORD CANNOT HOLD MOST OF THIS TODAY.** `zones.json` has **one primitive — the polygon**. This
starter vocabulary needs **areas, lines AND points**, and the deferral that was supposed to add lines
(`_meta.fold_2026_08_31`, *"until a schema v3 adds them"*) **named its own trigger, the trigger fired, schema v3
shipped with `partOf` and no lines, and nothing noticed.** ⭐ **So the starter vocabulary is itself an
independent argument for the lines-in-schema work** — arrived at from a completely different direction than the
smoothing plan's §4b, which is the strongest kind of corroboration.

| # | feature | primitive | source | honest confidence | at almost every property? | tier (§13) |
|---|---|---|---|---|---|---|
| **THE FRAME** |
| 1 | **Parcel boundary** | area | Regrid / county | **high** — but assessor-grade, ⚠️ **not a survey** | ✅ | 1 |
| 2 | Road frontage | line | TIGER ∩ parcel | high | ✅ | 1 |
| **BUILT** |
| 3 | **House** | area | MS/Overture + DSM | **high** | ✅ | 2 |
| 4 | Outbuildings | area | same | medium — small sheds get missed | ✅ | 2 |
| 5 | **Driveway** | **line + area** | §11a combination | medium-high | ✅ | 2 |
| 6 | Parking / hardstand | area | impervious + flat | medium | common | 2 |
| 7 | Walls / terraces | **line** | 0.1 m DSM / point cloud | low-medium; ⛔ absent without sub-metre | common | 2 |
| 8 | Paths | **line** | weak optical + routing | **low** | common | 3 |
| **WATER** |
| 9 | **Pond / water body** | area | ⭐ NIR + NHD + lidar | **high** | where present | 2 |
| 10 | Stream / drainage | line | NHD + flow accumulation | medium-high | common | 2 |
| 11 | Wet ground | area | NWI + TWI | medium | where present | 2 |
| **COVER** |
| 12 | **Forest / woods** | area | ⭐ CHM threshold | **high** | ✅ | 2 |
| 13 | Tree line / forest edge | line | CHM boundary | high | ✅ | 2 |
| 14 | **Open ground** | area | complement | high | ✅ | 2 |
| 15 | ⚠️ Mown vs unmown split | area | §3c multi-date | ⚠️ **unproven** | ✅ | 3 until proven |
| 16 | Specimen trees | **point** | CHM local maxima | medium | ✅ | 2 |
| **TERRAIN** |
| 17 | **Steep ground / bank / bluff** | area | ⭐ slope + geomorphon | **high where relief exists** | ⚠️ not flat lots | 2 |
| 18 | Ridge / knoll / hollow | area | geomorphon | medium | varies | 2 |
| 19 | Flat pad / terrace | area | slope + curvature | medium | ✅ | 2 |
| **CONTEXT — known, not drawn as a place** |
| 20 | Soil map units | area | SSURGO | high (⚠️ acre-scale polygons) | ✅ | 1 |
| 21 | Flood zone | area | FEMA | high | ✅ | 1 |
| 22 | Contours / slope / aspect | line/raster | 3DEP | high | ✅ | 1 |
| 23 | Hardiness zone · frost dates · normals | point attrs | USDA / NOAA | ⚠️ **wrong at elevation** — measured here | ✅ | 1 |

### 12a · ⭐⭐ The ratio Paul asked for — measured against Mom's sixteen names

Source: `.plans/2026-08-31-zones-traced-with-mom.json` — **16 areas + 3 lines**, named unprompted in one session.
This is the only evidence anywhere of how a person names their own ground, and n=1.

> The bank · Eastern Woodlands · Western Garden · Western Upper Patio · Western Lower Patio · **Fairway Border** ·
> The Green · The Bluff · Lawn · **Fern Garden** · Pond Area · Eastern Patio · **Lower 40** ·
> **St Francis Garden** · Lower Parking · **Stable Grounds** — and the lines: The Path · **Upper-Uber wall** · Driveway

| measure | count | share |
|---|---|---|
| **EXTENT a sensor could propose** (terrain, canopy, water, impervious, roof) — the bank · Eastern Woodlands · W Upper Patio · W Lower Patio · The Bluff · Lawn · Pond Area · Eastern Patio · Lower Parking | **9 / 16** | **56%** |
| ⚠️ conditional on the unproven mowing signal — The Green | +1 | +6% |
| ⛔ **extent NOT derivable** — Western Garden · Fairway Border · Fern Garden · Lower 40 · St Francis Garden · Stable Grounds | **6 / 16** | **38%** |
| **NAME approximable** by a model as *feature type + spatial modifier* ("east woods", "west upper patio", "pond", "parking") | **7 / 16** | **44%** |
| ⭐⭐ **NAME a model would have produced VERBATIM** | **0 / 16** | **0%** |
| lines: extent derivable — Driveway ✅ · Upper-Uber wall ✅ (sub-metre only) · The Path ⚠️ weak | 2 / 3 | |

⭐ **Read it as one sentence: automation gets a little over half the shapes and none of the words.**

⭐⭐ **And the sharpest item in the whole record is `Fairway Border` + `The Green`.** `zones.json` `_meta`
records that **the family's golf vocabulary was INVERTED** — a golf fairway is mown to 0.5–1.5″ and the
unmaintained ground is the *rough*; a meadow is cut once or twice a year. **Both words had been applied to the
opposite half of the field, and each read perfectly sensibly alone; the defect existed only in the aggregate.**

⛔ **A model shown that map would have "corrected" it — and would have been destroying the household's own
language.** A household's vocabulary can be internally inconsistent, technically wrong, and still be **correct,
because it is theirs.** That is the single strongest argument in this record for the rule in §0: *the model may
propose an extent; only a person may supply an identity.*

⚠️ **And two of Mom's names carry things no sensor will ever reach:** `St Francis Garden` is named for a statue,
and `Lower 40` is a family joke on "the back 40." Those are not hard cases. They are the point.

---

## 13 · The overstep line, made legible

For every auto-derived feature: **what claim are we making about someone's property without asking them, and how
is it presented?**

### TIER 1 — safe to render without asking
**Public record about the LAND. Makes no claim about how the household uses it.**
Parcel boundary · contours / slope / aspect · soil map units · flood zone · watershed · road centerline ·
hardiness zone · climate normals · historical topo.
**Claim made:** *"a public record says this about your address."* **True by construction, and attributable.**
**Presentation:** rendered as context, **always with the source and date on its face.**
⚠️ **Even here there is one trap:** the parcel boundary *looks* like a survey and is not. It must say
*"county assessor record, not a survey"* wherever it appears, or we have upgraded someone's tax map into a
property line — which is the highest-consequence silent claim in this entire document.

### TIER 2 — propose, labelled as a guess, presented as a shape to CORRECT
**Extents a sensor measured. Real evidence, real uncertainty, and a date.**
House · outbuildings · driveway · parking · pond / stream · wet ground · forest · forest edge · open ground ·
specimen trees · steep ground · landforms · flat pads · walls (sub-metre only).
**Claim made:** *"a photograph or a laser from `<date>` shows a thing of this shape here."* **That is a claim
about the ground, not about them** — and it is falsifiable by someone standing there, which is exactly the
property this record wants.
**Presentation:** pre-drawn, visibly provisional (this record's own `status: draft` and honesty markers), with
the **source and capture date attached**, and the correction cheaper than the confirmation.
⚠️ **The stale-imagery clause:** every Tier-2 shape carries the date of the frame it came from. *"The 2022 photo
shows a building here"* stays true even when the building is gone; *"you have a shed here"* does not.

### TIER 3 — never without them
**Every name.** · every garden bed and planted area · **whether a gap is a wall, a trail, or a strip of
nothing** · containment (`partOf`) · mown-vs-unmown until §3c is proven · anything about how they use ground ·
anything that changed since the imagery · **anything that would correct their vocabulary.**
**Claim that would be made:** *"we know what this place is to you."* ⛔ **We do not, and cannot.**
**Presentation:** a question, or nothing.

### ⭐ The presentation rule that makes the tiers safe

**Tier 1 renders. Tier 2 is corrected. Tier 3 is asked.** And the countermeasure from §7 governs all three:
**the householder is asked to CORRECT, never to APPROVE.** A finished-looking map shown to an older, agreeable
person returns a yes and measures nothing — and on this record's own numbers, **every affordance that asked her
to answer returned zero, and the one that simply moved her returned 100%.** The sixteen names came from **a
conversation over a map**, not a form. ⭐ **Whatever this becomes, the confirmation surface should look like that
session, not like a card queue.**

⚠️ **One more overstep that is easy to miss because it looks like generosity:** drawing *more* than we can
support. A map that renders 23 confident regions for a stranger's address teaches them the system knows their
place. **A map that renders 9 and says "we can't see the rest — what's there?" is both more honest and more
likely to produce the input we actually need.** The empty space is the ask.


---

## Sources

**Verified today (2026-09-06):**
[SAM 3 — Meta AI](https://ai.meta.com/blog/segment-anything-model-3/) ·
[SAM 3 research](https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/) ·
[SAM 3 browser ONNX int8](https://huggingface.co/rusen/sam3-browser-int8) ·
[segment-geospatial (samgeo)](https://samgeo.gishub.org/) ·
[Geo-SAM QGIS plugin](https://github.com/coolzhao/Geo-SAM) ·
[GeoOSAM QGIS plugin](https://plugins.qgis.org/plugins/GeoOSAM/) ·
[Microsoft GlobalMLBuildingFootprints](https://github.com/microsoft/globalmlbuildingfootprints) ·
[Microsoft USBuildingFootprints](https://github.com/microsoft/USBuildingFootprints) ·
[Overture 2026-08-19 release notes](https://docs.overturemaps.org/blog/2026/08/19/release-notes/) ·
[Regrid — Pickens County GA](https://app.regrid.com/store/us/ga/pickens) ·
[qPublic — Pickens County GA](https://qpublic.schneidercorp.com/Application.aspx?App=PickensCountyGA&Layer=Parcels&PageType=Search) ·
[Google Solar API — data layers](https://developers.google.com/maps/documentation/solar/data-layers) ·
[Google Solar API — coverage](https://developers.google.com/maps/documentation/solar/coverage) ·
[Google Solar API — policies](https://developers.google.com/maps/documentation/solar/policies) ·
[VRSBench (VLM grounding on remote sensing)](https://arxiv.org/html/2406.12384v1) ·
[SAM efficacy on agriculture / urban green space](https://doi.org/10.3390/rs16020414) ·
[Meta + WRI 1 m canopy height](https://registry.opendata.aws/dataforgood-fb-forests/) ·
[Chesapeake Conservancy high-resolution land cover](https://www.chesapeakeconservancy.org/projects/cbp-land-use-land-cover-data-project) ·
[GNSS accuracy under forest canopy](https://pmc.ncbi.nlm.nih.gov/articles/PMC8838512/) ·
[iPhone LiDAR accuracy and outdoor limits](https://www.scanmanifold.com/blog-posts/lidar-on-iphone-how-accurate-is-it-plus-the-biggest-errors-that-manifold-corrects) ·
[Apple RoomPlan](https://developer.apple.com/videos/play/wwdc2022/10127/)

**Verified today — Part II:**
[USGS 3DEP coverage FAQ / 98.3% status](https://www.usgs.gov/3d-elevation-program/about-3dep-products-services) ·
[USGS 3DEP lidar point clouds on AWS](https://registry.opendata.aws/usgs-lidar/) ·
[NRCS Soil Data Access web-service help](https://sdmdataaccess.nrcs.usda.gov/webservicehelp.aspx) ·
[SSURGO overview](https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo) ·
[Georgia State Imagery Program (15 cm, access-gated)](https://gio.ga.gov/state-imagery-program/) ·
[Vexcel Georgia coverage](https://vexceldata.com/countries/united-states/georgia/) ·
[NAIP dataset record](https://catalog.data.gov/dataset/national-agriculture-imagery-program-naip-imagery) ·
[NAIP 2026 state-level gap (ND)](https://www.gis.nd.gov/news/updated-dataset-2025-imagery-reminder-and-important-2026-imagery-news-march-31-2026)

**Leads, not opened:**
[NAIP-CHM 0.6 m CONUS canopy height (preprint)](https://www.biorxiv.org/content/10.64898/2025.12.12.694075.full.pdf) ·
[USGS 3DEP coverage FAQ](https://www.usgs.gov/faqs/what-coverage-3d-elevation-program-3dep-dems)
