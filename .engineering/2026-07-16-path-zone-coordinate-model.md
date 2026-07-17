# Path-eval — a zone coordinate model that endures

**Date:** 2026-07-16
**Mode:** path-evaluation
**Subject:** W0/W2 — what coordinate system should `zones.json` vertices live in, so zones survive
basemap swaps and absorb future refinement (GPS walks, drone, NAIP, lidar, EXIF photos) without a redraw?
**Stakes:** hobby project, two users (Paul + Mom, who reads with difficulty). Calibrated accordingly —
this is a small-code decision, not an enterprise GIS build.
**Code context confidence:** high (all claims below verified by reading the files, 2026-07-16)
**User context confidence:** high (`.user-research/persona-mom.md`, `2026-07-16-mom-ownership-read.md`,
`BACKLOG.md` "Mom's map")

---

## Recommendation (one line)

**Store vertices as WGS84 lat/lon. Make the basemap a swappable *view* registered by a 4-number
bounds box in `_meta`. Tag every zone's geometry with its provenance (`digitized-off-imagery` vs
`walked`), reusing the provenance pattern the plants already have.**

The smallest first step is **not** a code change — it's a **17-line contract commit** (schema v2 +
bounds in `_meta`) that costs nothing and forecloses nothing. Details in §7.

---

## 1. The actual defect (reframing the question)

Paul's question is "what's the most effective way to set these zones that will endure and be
refined?" The framing in `BACKLOG.md` W0 attributes the problem to the basemap: *"it's a Google Earth
Pro screenshot… oblique 3-D… vertices are fractional coords of that image, so swapping it moves every
polygon."*

That's true but it's the symptom. The obliqueness is why **these** polygons are lost. The
**coordinate model** is why the **next** basemap swap loses them again.

> The current system anchors the truth of a zone to *a picture of the property* rather than to
> *the property*. `zones.json` is not a record of where the Pond Area is. It's a record of where the
> Pond Area appears in `gep-2015-03-leafoff.webp`. Delete that JPEG and the data means nothing.

This matters because of what's coming. Every refinement source on Paul's list — a GPS-walked track, a
drone flight, NAIP 2026, 3DEP terrain, an EXIF-geotagged photo out of the 50K library — arrives in
**lat/lon**. Under fractional-of-image, every one of those requires a conversion *into* the frame of
whatever JPEG is current that month, and that conversion is itself lossy and re-does itself on every
basemap change. Under lat/lon, they just… land.

**The redraw is sunk.** The 8 existing polygons are unsalvageable under *any* option — oblique pixel
coords can't be cleanly reconciled to nadir. So the data-migration cost is identical across all
options and should be **excluded from the comparison**. The only question left is: *which model makes
this the last redraw?* That's the whole decision.

---

## 2. Verified current state (every claim below was read, not inferred)

| Claim | Verdict | Evidence |
|---|---|---|
| Vertices are fractional 0–1 of the base image | ✅ | `zones.json._meta.coordinateSystem`; 8 zones, all `[[x,y]]` in 0–1 |
| 2 confirmed / 6 draft, drawn 2026-05-28 | ✅ | `fairway` + `pond-area-3` = `confirmed` |
| `IMG_W/IMG_H` hardcoded at two sites | ✅ **and a third** | `viewer.html:7694-95` (render), `:7977` (draw mode) |
| CSS hardcodes the gep webp | ✅ | `viewer.html:2884` — dashboard tile background (decorative) |
| **`.pmap-stage { aspect-ratio: 1600 / 1103 }`** | ⚠️ **NOT in the brief — 4th coupling site** | `viewer.html:~514` — **load-bearing, see F2** |
| Draw mode writes via Worker → GitHub Contents API | ✅ | `worker.js:1978` `/api/zone-save` → `ghPutFile("zones.json")` + re-inline `ZONES_DATA` |
| `check-data-inline.py` does NOT track zones | ✅ **confirmed** | `SOURCES` (line 65) = 8 entries: plants, mammals, birds, amphibians, snakes, lizards, fishing, vehicles. **No zones.** |
| `property.json.propertyZones` is a placeholder stub | ✅ | still literally `{"id": "zone-placeholder", "name": "Example: Front Beds…"}` |
| `zoneId` references | ✅ **only 2** | `plants.json`: 24/26 `null`, 1 `fairway`, 1 `fairway-fringe` |
| **`sanitizeZone` clamps vertices to 0–1** | 🚨 **the critical one** | `worker.js:2013` → `clamp01(v[0]), clamp01(v[1])` |

**Two corrections to the record while I'm here:**
- `CLAUDE.md` (2026-07-08 pickup) says *"`check-data-inline.py` does NOT track vehicles"* — **stale**.
  `VEHICLES_DATA` is in `SOURCES` now. Zones are the untracked one.
- The brief says "two hardcoded IMG_W/IMG_H sites AND the CSS background." There are **four**
  basemap-coupled sites; the CSS `aspect-ratio` is the one that will silently corrupt drawing (F2).

---

## 3. The options

### (a) Keep fractional-of-image, record bounds in `_meta`

Vertices stay 0–1; `_meta` gains `bounds: {n,s,e,w}` so the fractions are *interpretable* as lat/lon
later.

This is the tempting middle. It is worse than it looks. It doesn't change the storage model — it
attaches a **decoder ring** to it. The data still says "position in a JPEG"; `_meta` says "and here's
how to decode that JPEG." Three problems:

1. **The decoder ring is a single point of silent failure.** If anyone crops, re-fetches at a
   different grid, or swaps the image without updating `bounds` in the same commit, every polygon is
   now confidently wrong with no way to detect it. Nothing in the codebase would catch it — zones
   aren't in `check-data-inline.py`.
2. **It doesn't absorb anything.** A GPS track still has to be projected into image-fraction space at
   ingest time. That conversion needs `bounds` anyway — so you've paid for lat/lon and not bought it.
3. **It re-does itself on every swap.** New imagery → new bounds → run a migration over every vertex,
   forever. NAIP drops annually.

Cheapest today. Pays rent monthly.

### (b) WGS84 lat/lon; basemap is a swappable view ⭐

Vertices become `[lon, lat]` (GeoJSON axis order) or `[lat, lon]` (plain). `_meta` carries the
current basemap + its bounds. The renderer projects lat/lon → image fraction at paint time; draw mode
inverts it.

The objection people reach for is *"now we need map math / Leaflet / proj4."* **At this scale that's
false, and I checked rather than assuming:**

```
image span:  440.7 m × 440.7 m     ground res: 0.246 m/px (0.81 ft/px — matches Paul's figure)
MAX error, naive linear lat↔pixel vs true Web Mercator, across the whole 1792px image:
    0.0026 m  =  0.26 cm  =  0.011 px
```

Over 440 m at this latitude, **linear interpolation between the bounds is exact to a hundredth of a
pixel** — roughly *1,000× smaller* than the imagery's own georegistration error. So the entire
projection layer is:

```js
const B = ZONES_DATA._meta.bounds;            // {n, s, e, w}
const fx = (lon - B.w) / (B.e - B.w);         // → 0..1
const fy = (B.n - lat) / (B.n - B.s);
```

Six lines of arithmetic. No library, no tiles, no Leaflet. The 5/27 path-eval's call to reject map
libraries (*"we have one bitmap of one property at one zoom level"*) **still holds** — this doesn't
reverse it. Lat/lon storage and a no-library SVG renderer are orthogonal choices, and we keep both.

*Why the right shape is right:* lat/lon is the **lingua franca** of every source Paul named. Storing
in the lingua franca means each new source is an *import*, not a *migration*. Storing in image
fractions means every source is a migration, and the basemap is load-bearing infrastructure instead
of a picture you can swap on a whim.

### (c) Local ENU / meters anchored at the property

Vertices as metres east/north from a property anchor (34.5496, -84.3674).

Genuinely appealing for one reason: **areas and distances become subtraction.** "How big is the
Lower 40?" is a shoelace formula on metres, no projection.

Rejected anyway. Every inbound source (GPS, EXIF, NAIP, drone, lidar) speaks lat/lon, so ENU adds a
mandatory conversion at *every* boundary to save one at the renderer. It invents a private
coordinate system only Fernwood speaks — which is a real cost against
*future-Paul-with-Claude maintainability*: in six months, `[34.5501, -84.3679]` is self-describing
and pasteable into any map; `[122.4, -87.1]` requires finding the anchor and the convention. And the
benefit is available anyway — you can compute metres *from* lat/lon in the one place that wants it
(§6), which is the right direction of dependency.

Keep ENU as a **derived** view, never as storage.

### (d) Full GeoJSON `FeatureCollection`

Considered and rejected as over-fitting. The value would be interop with real GIS tooling, which
isn't on Paul's roadmap; the cost is restructuring `zones.json` (`properties` nesting, `Polygon` ring
closure, winding rules) and rewriting `sanitizeZone` around a spec that exists to serve problems
Fernwood doesn't have.

**But borrow the one cheap thing: GeoJSON's `[lon, lat]` axis order.** It costs nothing today and
means a future `zones.json` → real GeoJSON is a wrapper, not a rewrite. (Flagged as an open question
in §8 — it's the one point where I'd rather Paul choose than have me pick for him, because `[lat,lon]`
reads more naturally to a human and this codebase's reader *is* the human.)

---

## 4. Trade-off table

| Dimension | (a) fractional + bounds | **(b) WGS84 lat/lon ⭐** | (c) local ENU |
|---|---|---|---|
| **Complexity** | Lowest today — zero new concepts | +6 lines of arithmetic, +1 concept ("the basemap is a view") | +anchor, +conversion at every boundary |
| **Scalability** | Breaks on every basemap swap | Basemap swap = change 5 values in `_meta` | Fine internally, friction at every edge |
| **Absorbs GPS walk** | ✗ convert at ingest, redo on swap | ✅ native | ⚠️ convert at ingest |
| **Absorbs drone / NAIP / 3DEP** | ✗ full re-migration each time | ✅ new basemap = new bounds, polygons untouched | ⚠️ convert |
| **Absorbs EXIF photo → zone** | ✗ needs bounds anyway | ✅ point-in-polygon directly on lat/lon | ⚠️ convert |
| **Future-Paul-with-Claude** | ⚠️ `0.4381` is meaningless without the JPEG | ✅ `34.5501` is self-describing, pasteable into any map | ✗ private convention, needs the anchor |
| **Precision honesty** | ✗ actively hides it — no place to state a frame | ✅ forces the question, gets a provenance field | ✅ same |
| **Learning value** | ~none | ✅ real: georeferencing, projection, frames-vs-accuracy — transferable to photo-miner | ⚠️ teaches a Fernwood-only idiom |
| **Migration cost** | 0 code (data redraw sunk) | ~1 session (§5) | ~1 session + ongoing |

---

## 5. Migration cost — concrete, in *this* codebase

Ordered by risk, not by effort.

### 🚨 F1 — `sanitizeZone`'s `clamp01` will silently destroy every zone (`worker/worker.js:2013`)

```js
// worker.js:2012-2014 — TODAY
const verts = z.vertices
  .map(v => Array.isArray(v) && v.length === 2 ? [clamp01(v[0]), clamp01(v[1])] : null)
  .filter(Boolean);
```

With lat/lon vertices and this line unchanged: `clamp01(34.5501) → 1`, `clamp01(-84.3679) → 0`. Every
polygon collapses to the image corner. The Worker returns 200. The chip says **synced**. `zones.json`
is committed to git with the destroyed data, `ZONES_DATA` is re-inlined from it, and the destroyed
version propagates to every device via `refreshZonesFromCloud()`.

**This is the exact failure shape as the 7/15 bug**: the write path silently mangles while the UI
acknowledges a success it never verified. Same family as the 7/03 incident. Fernwood has now been
bitten twice by this and there is a live principle for it —
*"Loud failure beats silent fallback in personal-stakes pipelines"* (cross-project) and Fernwood's own
*"sanitize at the storage boundary."* `clamp01` is a **correct** boundary sanitizer for the model it
was written for; it becomes a **data shredder** the moment the model changes underneath it.

**The right shape:** validate against the declared frame and **reject**, don't clamp.

```js
function sanitizeVertex(v, bounds) {
  if (!Array.isArray(v) || v.length !== 2) return null;
  const [lon, lat] = v.map(Number);
  if (!isFinite(lon) || !isFinite(lat)) return null;
  // Reject anything outside a generous property envelope — a coordinate that
  // isn't near Fernwood is a bug, not a value to be squashed into range.
  if (lat < bounds.s - 0.01 || lat > bounds.n + 0.01) return null;
  if (lon < bounds.w - 0.01 || lon > bounds.e + 0.01) return null;
  return [lon, lat];
}
```
…and when a zone's vertices don't survive, return a **4xx with a reason**, so the client can say
something true instead of "synced."

*Why reject-not-clamp:* a clamp encodes the belief "this value is roughly right, just out of range."
For a coordinate that belief is never true. Out-of-envelope means the frame is wrong, and the only
honest response is to refuse the write.

**Do this fix first, before any lat/lon data exists.** Effort: low. It is the whole risk.

### ⚠️ F2 — the CSS `aspect-ratio` is the silent-corruption one (`viewer.html:~514`)

```css
.pmap-stage { aspect-ratio: 1600 / 1103; /* matches the WebP base */ }
```

`eventToFractional()` (`:7778`) divides by `stage.clientWidth/clientHeight` — the **stage** box. The
SVG overlay uses `preserveAspectRatio` default (`xMidYMid meet`) against `viewBox="0 0 IMG_W IMG_H"`.
Today these agree **only because** the stage aspect equals the image aspect. The renderer's own
comment says so explicitly (`:7690-93`).

The new base is **1792×1792 (1:1)**; the old is **1600×1103 (1.45:1)**. Swap the image and update
`IMG_W/IMG_H` but *not* the CSS, and: the SVG letterboxes inside the stage while `eventToFractional`
still maps against the full stage box → **taps land offset from where the polygon draws**, worst at
the edges, zero at the centre. It looks like "the map is a bit off," not like a bug.

**The right shape:** one source of truth for the basemap's geometry. Put `imageWidth`/`imageHeight` in
`_meta` and set the aspect from JS at render (`stage.style.aspectRatio = W + "/" + H`), so the CSS
can't disagree with the data. Effort: low. This kills coupling sites 1, 2 **and** 3 together.

### F3 — the other sites
- `viewer.html:2884` — dashboard tile `background-image`. Decorative only, no coordinate meaning. Swap the URL. Effort: trivial.
- `viewer.html:7686-87` — `meta.baseImage` / `baseImageFallbackPng` already read from `_meta` with a hardcoded fallback. **Already correct.** Drop the hardcoded fallback string so a missing `_meta` fails loud rather than rendering the wrong picture. Nit.

### F4 — `property.json.propertyZones` — delete the stub (SSOT break)

Still ships `{"id": "zone-placeholder", "name": "Example: Front Beds (East-facing, mid-slope)"}` with
a note telling the reader to "edit to match your actual layout." Two records claim to define zones;
one is real (`zones.json`), one is scaffolding from a template that was never removed. Violates
*"Single source of truth per record, declared explicitly."*

It also carries fields `zones.json` **doesn't** have and that a zone genuinely wants —
`aspect`, `sunExposure`, `knownFrostPocket`, `soilNotes`. So this isn't only deletion: it's a small
design question about whether those attributes belong on a `zones.json` zone. My read — **yes, later,
and they're a strong argument for (b)**: `aspect` and `knownFrostPocket` are *derivable from
lat/lon + 3DEP terrain* the moment geometry is georeferenced, and un-derivable while it's pixels.

**Now:** delete the stub, leave a one-line pointer to `zones.json`. Effort: low.

### F5 — zones are invisible to the drift check (`tools/check-data-inline.py:65`)

`SOURCES` has 8 entries; zones aren't one. But `ZONES_DATA` **is** an inlined const (`viewer.html:5460`)
re-inlined by the Worker on every `/api/zone-save`. That's a re-inline path with **no drift alarm** —
precisely the shape that hid Lizard's Tail for weeks and that `check-digest-fresh.py` was written to
close for the digest.

Zones don't fit `SOURCES`'s `(json, const, species_path, category)` shape (no species list), so this
is a small extension, not a one-line add. Worth doing **as part of this work** — a coordinate
migration is exactly when you want the drift alarm already armed. Principle:
*"A deploy-bundled context artifact needs a rebuild-and-diff drift alarm"* (fernwood, 2026-07-07)
— this is the same class, and it's currently the only re-inlined const without one. Effort: medium.

### F6 — `zoneId` references: migrate now, while there are two

`plants.json`: 24/26 `null`, plus `fairway` and `fairway-fringe`. `zoneId` is a **string key**, not a
coordinate, so it survives the coordinate change untouched — **zero migration cost today**.

Flagging it because of W6: the instance model turns `zoneId` from ~2 references into one per plant
*instance*. Do the coordinate model **before** W6 multiplies the references, not after. Effort: none now; high if deferred.

**Not touched by this migration:** the draw-mode UI/gestures, `ZonePanel`, `ZoneSyncStatus`, the
KV/GitHub write path, `refreshZonesFromCloud`, tombstones. The architecture is sound — this changes
what the numbers *mean*, not how they move.

---

## 6. Precision honesty — what we'd actually be claiming

Trust is load-bearing here, and this is where storing lat/lon creates a **new way to be
confidently wrong**. Calling a number `lat` implies a claim about the Earth. Here's the honest version:

**What's real:**
- The linear projection is exact to **0.26 cm** across the image (§3). *Not* the error term.
- ESRI World Imagery georegistration in mountainous terrain: **±3–5 m absolute** is the realistic
  envelope (Maxar/NAIP sourcing, varies by capture).
- The property sits at **2,959 ft on a slope**. World Imagery is orthorectified against a DEM, but
  residual **relief displacement** persists on slopes — features get pushed radially from nadir.
- Net: a vertex digitized off this basemap is **±3–5 m absolute**, but **internally consistent to
  ~1 m** (all zones share the same frame, so they're right *relative to each other*).

**So the claim we can honestly make is:**

> *These are lat/lon **in the ESRI World Imagery frame**, digitized off 0.25 m/px nadir imagery.
> Good to roughly ±3–5 m against the real world; internally consistent to ~1 m.*

**Not** *"this is where the Pond Area is."*

**The good news, and it's the load-bearing point:** the precision that matters to Fernwood is
**topological, not metric**. Mom's question is *"what's growing here?"* — the answer is a **zone name**,
not a coordinate. Zones are tens of feet across; a 3–5 m frame error essentially never changes which
zone a point falls in, except within a few metres of a boundary. **The accuracy budget is generous
because the unit of meaning is the zone, not the point.** Anything metric ("this plant is 2 ft from
the pond edge") is outside what this data can support, and should stay outside.

**Where this bites — and the fix:** when Paul walks a boundary with a phone (±3–5 m) or RTK (±cm),
the walked track and the digitized polygon **will disagree by several metres**. Neither is wrong.
They're in **different frames**. Without a provenance field, that disagreement reads as "the map is
broken" or — worse — gets "fixed" by dragging good walked data onto bad imagery.

**Therefore: geometry carries provenance, exactly like the plants do.**

```jsonc
"geometry": {
  "frame": "wgs84",
  "source": "digitized:esri-world-imagery-2026-07",
  "confidence": "inferred",       // ← "our read from a photo"
  "accuracyClaim": "±3-5 m absolute; ~1 m internally consistent"
}
// after Paul walks it:
"geometry": {
  "frame": "wgs84",
  "source": "walked:gps-2026-09-14",
  "confidence": "verified",       // ← "confirmed on the ground"
  "accuracyClaim": "±3-5 m (phone GPS)"
}
```

This is **not a new concept** — it's `plants.json`'s `variety.confidence` (`inferred`→`verified`,
`askable`) applied to geometry, and it makes zone boundaries legible to the **same harvest engine**
(`harvest-questions.py` reads `confidence != verified && askable`) and the **same provenance chip**
(`renderVarietyRow`: "our read from a photo" → "confirmed on the ground · <month>").

**Which means the zone map gets Mama's Perspective for free.** A `confidence: inferred` boundary is,
by the existing machinery's own definition, **a question only someone standing on the property can
settle.** That's W2's *"which of these is wrong?"* — and it falls out of the data model rather than
being built. Fractional-of-image cannot express this at all: there's no frame to be honest about.

*Note (2026-07-16, engineering-partner-proposed — not Paul-validated):* this is a proposal about how
provenance should attach to geometry. It reuses a Paul-ratified pattern but hasn't been through him.

---

## 7. The smallest first step that forecloses nothing

**Do not swap the basemap and redraw yet.** The order that wastes nothing:

**Step 0 — write the contract, no code (~17 lines, this session).**
Bump `zones.json` to `schemaVersion: 2` and commit the `_meta` that describes the *target* model,
while `zones: []` still holds the 8 dead polygons:

```jsonc
"_meta": {
  "schemaVersion": 2,
  "coordinateSystem": "wgs84",
  "coordinateNotes": "Vertices are [lon, lat] WGS84. The basemap is a VIEW, not the frame — swapping it must not move a polygon. Digitized off nadir imagery: ±3-5 m absolute, ~1 m internally consistent. Zones are the unit of meaning; do not read metric distances off these.",
  "baseImage": "images/property-map/base-esri-z19-wide.webp",
  "baseImageFallbackPng": "images/property-map/base-esri-z19-wide.jpg",
  "imageWidth": 1792,
  "imageHeight": 1792,
  "bounds": { "n": 34.5518114, "s": 34.5478526, "w": -84.3695068, "e": -84.3647003 },
  "boundsSource": "Web Mercator z19 tile grid, computed 2026-07-16; reproducible via tools/fetch-aerial.py",
  "imagerySource": "ESRI World Imagery, nadir, 0.246 m/px, leaf-off"
}
```

Free, reversible, and it turns the decision into a **reviewable artifact** instead of an intention.

**Step 1 — fix `clamp01` → reject-not-clamp (F1), before any lat/lon exists.** The one real risk,
neutralized while there's nothing to lose.

**Step 2 — de-hardcode the geometry (F2/F3):** `_meta.imageWidth/imageHeight` drive both `IMG_W/IMG_H`
sites and the stage `aspect-ratio` from JS. Add the 6-line projection helper + its inverse. Swap the
basemap. **The map now renders the new nadir image with zero zones** — honest, and briefly the truest
the map has ever been.

**Step 3 — Paul draws.** Draw mode writes lat/lon through the already-hardened boundary. Every zone
lands `geometry.confidence: "inferred"`, tagged `heard-from-her` / `paul-inferred` per W2.

**Step 4 — housekeeping:** delete the `propertyZones` stub (F4); add zones to the drift check (F5).

**Why this order:** each step is independently committable and useful; the risky one (F1) happens when
the blast radius is zero; and Step 0 costs ~nothing while making Steps 1–4 obvious. If Paul stops
after Step 0, the next session — or the next Claude — picks up a **declared contract** instead of
re-deriving this from a JPEG's aspect ratio.

---

## 8. Open questions for Paul

1. **`[lon, lat]` or `[lat, lon]`?** GeoJSON says `[lon, lat]` (free future interop). Humans read
   `[lat, lon]` ("34.55, -84.37" is the pasteable order). This codebase's reader is a human with
   Claude open. **My weak lean: `[lon, lat]`** for the free interop — but this is genuinely
   Paul's call, and whichever wins must be stated **loudly** in `_meta.coordinateNotes`, because a
   silently-swapped axis order is a bug that renders as a plausible-looking map rotated into the woods.
2. **Do the 6 draft zones' *names* survive the redraw?** The geometry is dead; `fairway`,
   `western-garden`, `lower-40` etc. are Paul-and-Mom's actual vocabulary and are the more valuable
   half. My assumption: **keep the ids/names, drop the vertices.** That also preserves the 2 live
   `zoneId` refs in `plants.json` (F6). Confirm.
3. **W6 interaction (flagged, not answered here):** the instance model may want a plant instance to
   carry its **own point** (a lat/lon where *that individual* stands), not just a `zoneId`. Under (b)
   that's free and arrives in the same frame as the zones; under (a) it's incoherent. **This
   strengthens the case for (b), but the instance model needs its own path-eval** — don't let it
   widen this one.
4. **Leaf-off basemap + Mom's legibility.** Paul chose leaf-off ESRI over leaf-on NAIP for legibility
   — right call for *drawing*. But the map Mom looks at is the one she has to **recognise as her
   place**, and she'd be seeing it in July. Basemap-as-a-view means this isn't either/or: draw on
   leaf-off, and a leaf-on display layer is later a `_meta` swap with **no redraw** — which is the
   whole thesis, and probably its best demonstration. Worth a ux-expert read, not an engineering call.

---

## 9. Principles to propose (proposals — not applied)

1. **"Anchor coordinates to the world, not to a picture of the world."** *(scope: cross-project)*
   Any geometry that will outlive its current rendering surface stores position in a frame that
   exists independently of that surface. Fractional-of-image couples the truth of a record to an
   asset you will replace. *Rationale:* this whole path-eval. Related to the existing
   *"Single source of truth per record"* but distinct — this is about the **frame** being SSOT.

2. **"A boundary sanitizer encodes a model; when the model changes, the sanitizer becomes a shredder."**
   *(scope: cross-project)*
   `clamp01` was correct for fractional coords and silently destroys lat/lon. Whenever a data model
   changes, audit the sanitizers *first* — they're the code most likely to be correct-looking and
   catastrophic. Corollary: **reject out-of-envelope values, don't clamp them** — clamping asserts
   "roughly right, just out of range," which is false for identifiers, coordinates, and keys.
   *Rationale:* F1; third instance of the silent-write-path family (7/03, 7/15, this).

3. **"Precision is a claim; a frame is a fact — store the frame."** *(scope: fernwood, promotable)*
   When a value's accuracy depends on its source, the source rides with the value. Two measurements
   of the same thing in different frames disagree *correctly*; without a frame tag that disagreement
   reads as a bug and gets "fixed" by corrupting the better data. *Rationale:* §6; extends the
   Paul-ratified **provenance-honesty** design principle (2026-07-14) from display into storage.

---

*Path-eval by engineering-partner, 2026-07-16. All code claims verified against
`viewer.html`, `worker/worker.js`, `zones.json`, `property.json`, `plants.json`,
`tools/check-data-inline.py` at HEAD on this date.*
