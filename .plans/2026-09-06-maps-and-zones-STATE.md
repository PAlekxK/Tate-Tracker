# Maps & zones — where we actually are

- **status:** STATE OF PLAY + BACKLOG COMB. No proposal in this file; the proposal is
  `.plans/2026-09-06-maps-and-zones-PROPOSAL.md`, which is built on top of this.
- **raised:** `[paul-stated 2026-09-06]`, voice — *"everything having to do with maps... combing the
  backlog for ideas and kinda figuring out where we are in our ability to take a map and define
  zones... I think that's a critical next feature."*
- **writes:** this file only. Nothing tracked was edited; nothing was committed. Two other sessions
  were live in this repo while it was written.
- ⚠️ Every number below is measured at HEAD `dedf849` on 2026-09-06, not recalled. Where a document
  in this repo disagrees with a measurement, the measurement is reported and the document is named.

---

## 0 · The one-paragraph answer to "where are we"

**Fernwood can already do this, once, by hand, for one property, on a surface only Paul can drive.**
There are 23 named polygons covering 2.64 acres, drawn on a georeferenced 2022 aerial, served
per-estate from KV, rendered on Mom's map, and round-trippable through Google Earth. That is a
genuinely working zone capability and it is further along than the backlog's own framing suggests.
**What does not exist is any of it as a product**: the write path is bound to one GitHub repo, the
basemap took a multi-day research arc for a single address, every zone is `status: draft` with no way
to leave that state, the record can only hold areas (not the lines and points Paul has now asked for
twice), and the one surface that would let a householder participate got **zero taps in ten offers**
while the same person, sitting at a kitchen table with a pen, named sixteen areas in one evening.
⭐ **That contrast is the most useful fact in this document**, and Paul's ruling tonight — *we draw,
they confirm* — is the conclusion it supports.

---

## 1 · The progression — how zone work has actually gone here

*Paul asked for this explicitly: "you can look at our work with Fernwood where I've already been
developing, and all the history there about how we've tried to develop zones and the process we've
been through already — that progression is also probably important to capture."*

Seven phases. Dates and commits are from `git log`; the readings are mine.

### Phase 1 — A list, not a map (2026-05-19)
`images/property-map/zones.md`. Seven zones as a **markdown table** — `eastern-patio`,
`western-patio`, `pond-area`, `fairway-edge-west`, `front-lawn`, `fairway-meadow`,
`forest-interior`. No geometry at all. Three zone *types* invented on the spot (`planted` · `turf` ·
`meadow`) because the care pattern differs. Paul's framing note the same day: *"Treat every zone as a
gardening zone — the area around the feature, not the feature itself. Plants are what we're locating;
structures are just useful anchors for naming."*

⭐ **The first shape was a NAMED LIST, and it worked.** Nothing here needed a basemap. That is worth
holding on to, because six weeks of geometry work followed and the names survived all of it.

### Phase 2 — Geometry welded to a picture (2026-05-27)
`Property Map v1`. Twenty-four `Zone update` commits in a single day — 8 zones, then 7, then 2, then
0, then 8 again, with tombstone counts sloshing between 1 and 9. An editor existed and was being
driven hard.
⛔ **All of it was thrown away.** The v1 polygons were pixel coordinates against an **oblique 2015
Google Earth screenshot**. When the basemap changed, the geometry meant nothing.

### Phase 3 — The correction that made everything after it possible (2026-07-16)
`e2966dc — "Zones v2: vertices are real coordinates; the basemap is now just a view"`. Vertices
became **WGS84 lon/lat**. The 8 surviving zones kept their names and ids; **their geometry was
deliberately cleared** as unsalvageable.
⭐ **This is the single best decision in the whole arc.** Everything cheap that happened later —
the lidar hillshade registering byte-identically to the NAIP base, the Google Earth frame becoming a
layer, the KML round trip — is the dividend of it. It also cost a full re-trace, and the record says
so plainly rather than hiding it.

### Phase 4 — Paul draws, and the count climbs (2026-07-17 → 07-22)
Nine `Zone update` commits: 9 → 10 → 11 → 12 → 13 → 14 → 15 zones. Then a reconciliation pass
(`646d57e`, `c5e5e07`) that renamed four `-2` ids, dropped six empty ghosts, and preserved 55
vertices exactly, with assertions run before writing.
The backlog row that governed this is **W2 — "Zones — Paul draws, she reconciles"**, and its own
words are: *"Paul walked them with her; he's sure; he draws (not relitigated)."*
⭐⭐ **Tonight's ruling is not new. It is W2, restated in July, and it was right then.**

### Phase 5 — The invitation, and the zero (2026-07-17 → 07-31)
A five-lens panel (`.user-research/2026-07-17-zone-journey-panel-synthesis.md`) designed a
**zone-journey front door**: a position-1 card inviting Mom into a guided flow — pick one zone at a
time, large name in serif, colour swatch, the patch highlighted, one big 🎤 *"Tell me about this
spot."* The panel was careful and mostly right; its own critical finding was that **raw
polygon-hunting is not an acceptable pick interaction** for her.

It shipped. Then:

| affordance | offered → taken (lap 8 window) |
|---|---|
| jump strip — *moves* her | 5 → **5 tapped** |
| front-door launcher — *asks* her | 10 → 4 viewed → **0 tapped** |
| Mama's Perspective queue — *asks* her | 10 → 4 viewed → **0 tapped** |

⛔ **2026-07-31, Paul holds the entire track**: *"hold on any further zone work, basically, until we
get some signal from mom that the zones are important."* The row records the honest reason — the
front door had **0 taps from her device** and none of her four real inputs had ever been about a zone.

### Phase 6 — The kitchen table (2026-08-30 → 08-31)
Paul sat with his mother and **she named sixteen areas of the property, unprompted, in her own
words**: The Bank · The Bluff · The Green · The Green Ring · The Green Terrace · Fern Garden ·
Fairway Border · Hosta Garden · St Francis Garden · Lower 40 · Lower Parking · Main Parking · Stable
Grounds · Eastern Woodlands · The Meadow · The Turf. Paul traced them the next day.
`51d6007 — THE FOLD — Mom's map is canon`.

⭐⭐ **THE FINDING OF THE WHOLE ARC.** The in-app zone journey, designed by five expert seats and
built correctly, produced **zero** contributions in ten offers. A pen, a kitchen table and one
conversation produced **sixteen** — described in the backlog as *"the largest single contribution Mom
has made to this project."*

Three things follow, and all three are load-bearing tonight:
1. **The demand signal the 07-31 hold was waiting for ARRIVED on 2026-08-30** — a zone named in her
   own words is literally the first item on the row's own un-park trigger list. Nothing appears to
   have re-read the hold against its own condition. *(Flagged to practice-steward; it is their beat,
   not mine to rule on.)*
2. **She contributed NAMES, not SHAPES.** Sixteen names, zero polygons. Every subsequent vertex on
   this property was drawn by Paul.
3. **She has still never been thanked for it.** `Z-ACK` — the ack ribbon is gated on *"zone work
   ready to distribute"*, and the zone work has not been ready since. The biggest thing she ever gave
   this project is the thing she got the least back on.

### Phase 7 — Four months of measurement, in nine days (2026-08-31 → 09-04)
The most productive stretch, and none of it was drawing:
- **Layers proven cheap** — 2018 3DEP lidar hillshade rendered to *byte-identical bounds* with the
  NAIP base. A drop-in layer needing no registration (`a67e776`, `ba03473`).
- **A Google Earth frame georeferenced** by homography off Earth's own cursor readout (`2403f28`) —
  after a correlation-based fit scored NCC 0.21 and **got worse at higher resolution**, the signature
  of model mismatch. The guard that refused the bad fit is why that is a note and not a corrupt layer.
- **Google Earth round-trip** via KML, byte-exact across all 23 zones (`53140cf`).
- **Snapping and Chaikin smoothing built into the tracer** (`badf097`, `b661d59`) — smoothing
  deliberately as a **view, never a write**.
- **The elevation corrected** from a 4-month-old "confirmed" 2,959 ft to a lidar-measured 2,873 ft
  (`f2bec82`).
- **Land sources inventoried** (`LAND-SOURCES.md`), historical topos back to 1888 (`4086810`).
- **The topology measured** (`.plans/2026-09-04-map-region-smoothing-PLAN.md`): 437 vertices, 1,706 m
  of boundary, median segment 2.57 m against a ±9.1 m error budget, 11 sliver gaps under 1 m, 24
  touching/overlapping pairs, 5 degenerate zero-length segments, and the measured proof that
  snapping at the accuracy budget would **collapse 119 of 437 vertices into one cluster**.

⚠️ **And the shape that keeps recurring, now named three times in this repo:** snapping and smoothing
landed on the **authoring** surface and never reached the **reading** one. Paul's ragged-map
complaint on 2026-09-04 was about `viewer.html`, which has neither. *A capability pointed at the
wrong surface is not a capability the product has.*

---

## 2 · What the product can do TODAY — verified, not claimed

### ✅ Works
| capability | evidence |
|---|---|
| 23 named zones, real WGS84, 437 vertices, 2.64 acres | `zones.json` schema v3, measured at HEAD |
| Per-estate read path | `handleZonesGet` → KV `keyFor(scopeOf(env),"zones","all")`, falls back to the git file |
| Rendered on Mom's map | `viewer.html` `.pmap-*`, pan/zoom, labels that refuse to draw if they don't fit |
| In-app zone add/edit | `.pmap-add-btn` / `.pmap-add-popover`, `/api/zone-save`, sync ribbon + `zones-sync-status` |
| Device-level sync tracking | `zones-last-seen:<deviceId>` |
| Tombstones | 6 `_deleted` ids so cached devices drop retired zones |
| Voice capture per zone | `/api/zone-audio` — blobs in KV, **never git**, AI-free |
| Free-text capture per zone | `/api/zone-feedback` |
| Google Earth round trip | `zones-to-kml.py` / `kml-to-zones.py`, dry-run by default, byte-exact |
| Georeferencing a new frame | `register-gearth-frame.py` — four cursor reads and a screenshot |
| Layer sources already registered to the same bounds | NAIP 2022-01, 7 NAIP frames, lidar hillshade + slope, 2018 Google Earth, historical topos |
| Topology measurement | `zone-topology-report.py` |

### ⛔ Does not work, or does not exist
| gap | evidence |
|---|---|
| **The write path is not multi-tenant** | `handleZoneSave` calls `ghPutFile(env,"zones.json",…)` **and** re-inlines `ZONES_DATA` into `viewer.html` in one GitHub repo. Read is per-estate; write is per-repo. |
| **No basemap for an unresearched address** | `onboarding/index.html` header rules zones out of first run for exactly this reason. Fernwood's basemap took a multi-day arc. |
| **Nothing can leave `draft`** | 23 of 23 zones `status: draft`. There is no confirm act and no state after it. The map renders entirely dashed as a consequence. |
| **One geometry only** | `zones.json` holds polygons. Walls, paths, the driveway and the property line have no slot. The Path is stored as a **17-vertex polygon** and reports a meaningless acreage. |
| **No point annotations** | Paul asked 2026-09-04 for shut-off valves, repair sites, project locations. No primitive exists. |
| **No layer model** | Both map tools use a single hard-wired `<img>`. The registered layers cannot be toggled. |
| ~~**Smoothing/snapping only on the authoring tool**~~ | ⚠️ **CORRECTED 2026-09-06 by execution.** Tier 1 of the smoothing plan **shipped** on 2026-09-04 (`6408706`, ancestor of HEAD): `viewer.html` now has `stroke-linejoin: round`, `stroke-linecap: round` **and 2-iteration render-time Chaikin**, with an assertion publishing `window.__pmapVertexIdentityOK`. The plan file still reads as unbuilt. **Snapping remains tracer-only.** And the before/after exhibits (`.playwright-mcp/{before,after}-bluff.png`) show it worked as designed and **did not visibly fix the complaint** — see the PROPOSAL §3. |
| **No topology check in the loop** | `zone-topology-report.py` exists and is in no session-start block; `check-zones-drift` (repo vs live `/api/zones`) was proposed 2026-08-31 and never built — the two disagreed in both directions for six weeks with nothing flagging it. |
| **Photo→zone join has a hard floor** | 12 of 18 zones sit in pairs closer than the ±9.1 m budget. `st-francis-garden`↔`eastern-patio` centroids are 5.9 m apart — less than either zone's own width. |

### 📐 The record's own honesty statement, which governs everything
`zones.json _meta.accuracyHonesty`: *"these polygons record **WHERE A NAME APPLIES, at the resolution
of a name**. They are NOT survey lines, NOT parcel boundaries, and NOT a basis for anything that
turns on where an edge actually falls."*
⭐ That sentence is the best thing in the zone record and it is the constraint any "make it look good"
work has to survive.

### 📊 Two measurements that surprised me
- **Plant↔zone linkage is thinner than the backlog says.** The record now carries a `zones[]` **array**
  per plant (the backlog still says *"`zoneId` is singular, so a second location is a schema
  question"* — that question has been answered in the data and the row was never updated).
  Measured: **27 of 40 plants carry at least one zone; 13 carry none. 13 of 23 zones are referenced
  by a plant; 10 zones hold no plants at all.** `pond-area` alone accounts for 16 of the 44 links.
- **Nothing has left draft in 23 of 23 zones**, including the sixteen Mom named herself.

---

## 3 · The backlog comb

Every map/zone-adjacent row, with provenance. **`paul-*` = his demand. Unmarked = an agent proposed
it.** Paul asked for this distinction and it is stark: *almost every substantive map idea in this
backlog is his.*

### Paul-voiced — his own demand, recurring
| row | provenance | state | recurrence |
|---|---|---|---|
| **W2 · Zones — Paul draws, she reconciles** | `paul` (Jul) | 🟢 partly done | ⭐ **Restated verbatim tonight.** Twice, two months apart. |
| **🎨 An ILLUSTRATED map, not a photograph** | `paul-raised 2026-08-31` | ⏸ IDEATION | Reference: the Grant Park Summer Shade Festival map. *"more conceptual rather than a real image, but still lays out exact areas, borders, paths."* Backlog calls it *"the cheapest big win on this list."* **Re-raised tonight as "what's a good looking map."** |
| **🗂 LAYERS — toggleable views** | `paul-stated 2026-08-31` | ⏸ IDEATION | *"being able to layer and toggle views is an end goal we need to work towards."* Named as the structural prerequisite for three other rows. **Re-raised tonight as "all the different views of the property we can get."** |
| **📏 ONE GEOMETRY — not everything is an area** | `paul-stated 2026-08-31` | ⏸ IDEATION | *"It's a wall. More of a dividing line than a zone."* / *"the path is a landmark, not a zone."* **Re-raised 2026-09-04** as "draw the barriers or the landmarks — maybe landmarks are more important than setting zones by individual vertices." |
| **📍 Point annotations** | `paul-stated 2026-09-04` (voice) | ⏸ not filed as a row | Shut-off valves, repairs, projects. *"probably worth its own individual discovery research journey."* |
| **🕰 THREE DATES FOR ONE PIECE OF GROUND** | `paul-stated 2026-08-31` | ⏸ standing constraint | ⛔ Do not snap polygons to the 2018 lidar; a mismatch is first evidence of **work done since**, not a bad trace. |
| **📐 The Tate lot drawing as an overlay** | `paul-raised 2026-08-28`, re-raised 08-31 | ⏸ IDEATION | *"ideally we would also lay the property line drawing over it as an option."* Photo of the lot drawing, iCloud only — repo is public. |
| **🔴 Zoom resolution is structural** | `paul-stated 2026-09-01` | 🔜 owed, blocked on a flaky dependency | A screen capture is a fixed raster. One ~350 m Google Earth capture would cover all 23 zones at 2.7× NAIP. |
| **Map region smoothing** | `paul-stated 2026-09-04` (voice) | 📄 researched, not queued | *"some little gaps... not always smooth."* Acceptance criterion he gave: accuracy is at its floor, **"the remaining job is just making it clean."** |
| **Zone consolidation (Z2)** | `paul-raised 2026-09-02` | 🔍 surveyed only | *"I definitely have done some draws recently that are not reflected here."* Those draws were never found. |
| **⭐ Zones as rich content-containers** | `paul 2026-07-25` | ⏸ | A zone as a place that holds its contents — flagship example the pond. |
| **Household systems / points of interest** | `paul` | partly shipped | *"which breakers control which outlets, where is the water shut-off valve"* — the point-annotation ask arriving from the other direction. |

### Agent-proposed
| row | state | note |
|---|---|---|
| Zone-journey front door | ✅ shipped | **0 taps in 10 offers.** Well-designed; the wrong bet. |
| Zone naming-completeness pass · `zoneAffinity` · zone-journey v2 · map-highlight | ⏸ HELD 07-31 | The hold's own un-park trigger fired 2026-08-30 and nothing re-read it. |
| `check-zones-drift` in session-start | ⏸ never built | repo `zones.json` vs live `/api/zones` disagreed in both directions for six weeks, unflagged. |
| `tools/check-zone-topology.py` as a standing check | ⏸ proposed | Explicitly gated: *do not build it before Paul rules on whether a gap is a defect.* |
| Photo→zone join | ⛔ measured and refused | Works at property scale, fails at garden scale. *"Do not let anything auto-assign a zone from this join."* |
| Terrain-derived boundaries | ⛔ scoped and refused | Works only where the zone's NAME is a terrain word. |
| Model A — polygonal coverage (shared edges) | ⏸ Tier 3, do not start | Blocked on an adjacency statement and on lines-in-the-schema. |
| W6 instance model | ⏸ deferred | Repeatedly named as blocking; gate has never fired. |

### 🔁 The recurrence pattern, stated plainly
**Four of Paul's map ideas have been raised two or three times each across five weeks** — the
illustrated map, layers, lines/landmarks, and the honest-but-clean rendering. Every one is tagged
`IDEATION` and none has an owner, a stage or a gate. Tonight is the third raising of at least two of
them.
⭐ **That is the finding the process seat should act on: this is not a shortage of ideas or of
research. It is a feature with no pipeline.** Paul said exactly that tonight — *"this feature in
itself should have kind of a vision and a current state and then a series of improvements and
investigations."*

---

## 4 · Two things this file will not do

- **It does not rule on the 07-31 hold.** The un-park trigger appears to have fired on 2026-08-30.
  Saying so is a measurement; deciding what follows is Paul's, and whether the loop should have
  caught it is practice-steward's.
- **It does not choose a path.** That is the proposal, and it waits on five seats: practice-steward
  (process), user-researcher (how people define a place), ai-advisor (what imagery and models can
  derive from an address), ux-expert (what a good-looking map is, and how a person confirms one), and
  engineering-partner (what multi-household maps require).
