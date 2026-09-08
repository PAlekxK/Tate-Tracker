# zones-v1-path · ZONES v1 = zones × plants — a path evaluation
- row: BACKLOG.md § ▶️ NEXT · zones as an epic (ROW TO ADD — mirrors `.plans/2026-09-07-zones-PLAN.md`)
- objective: O3
- class: engine · declared
- seats: engineering-partner → .engineering/2026-09-07-zones-v1-path.md (this file)
         user-researcher → .user-research/2026-09-07-zones-uses-landscape.md · .user-research/2026-09-07-zones-plants-v1-journey.md
         ux-expert → .ux-reviews/2026-09-06-map-drawing-mobile.json
         content-steward → OWED for the ZonePanel plant line's words; not yet run
         ai-advisor → .plans/2026-09-06-ai-mapping-capability-SCAN.md
- stage: concept
- stage-note: 2026-09-07 — design lane of release lap 3. NOTHING SHIPPED FROM THIS SESSION. Reaction only.

> ⚠️ **THIS FILE IS A SEAT TRAIL, NOT THE ITEM'S PLAN.** `.plans/2026-09-07-zones-PLAN.md` is the
> plan of record and cites this file as the engineering seat; **its header governs.** The keys above
> mirror it so the two cannot be read as disagreeing by accident. Where I would argue differently,
> say so out loud rather than in a header field: I read v1's *centre of gravity* as **O2** (*the
> record about the place is true, accumulated, and hers to correct*) rather than O3, because zones ×
> plants makes the place record say something whether or not a second estate ever exists — and I
> read the two render paths as **`must-not-diverge`** rather than `declared`, because a zone's plant
> list is the same act at every estate and there is no per-estate reason for it to differ. Neither is
> a strong disagreement and **neither is mine to settle.**

> ⚠️ **AND THIS FILE IS NOT GRADED WHERE IT SITS.** `tools/check-backlog-ready.py` globs
> `.plans/*-PLAN.md` + `.plans/*-PROPOSAL.md` (`:261-262`, `:423-424`) and nothing else. A file in
> `.engineering/` is invisible to it, so the header above is a *convention* here, not a *check*. The
> grading happens on the plan; this header exists to be read, not to pass. Do not read it as evidence
> anything passed.

---

## THE VERDICT IN FIVE LINES

1. **v1 as scoped needs no geometry at all.** `plant.zones[].zoneId` → `zone.id` is a string join.
   It needs no coordinates, no basemap, no snapping, no topology. **The entire staged pipeline (A)
   and the entire edge-snapping question (B) are orthogonal to v1** and can be sequenced behind it.
2. **Structure-first is right, and the claim about Tier 2 is right for the wrong reason.** Shared
   lines would make slivers impossible *going forward*; they do nothing for the 23 already traced.
   Tier 2 dies because **its subject is frozen and Mom starts blank** — ruling 3, not ruling 5.
3. ⛔ **Rulings 1 and 4 do not compose.** v1 is zones × plants; the first instance to serve is the
   condo; and the condo is `garden: off` by a **stamped** plan (`c7-condo-paper-model-PLAN.md`,
   `[paul-approved 2026-09-03]`). **v1 has no surface at the first instance that ships.** This is
   the highest-value thing in this file.
4. **Two blockers are live and cheap; two are not tripped by v1.** The digest hard-fail is a
   three-line guard, not a rework. The condo geometry envelope is a real hard stop *if* geometry is
   ever drawn off-Fernwood. `ghPutFile` tenancy and the three-geometry schema are **deferrable**.
5. **The gradient-confidence idea is unsound on this basemap specifically**, and the literature says
   why in one sentence: livewire *"tends to adhere to the strongest edge in the neighbourhood."* On a
   32°-sun January frame the strongest edge **is the shadow**. The number would be highest exactly
   where it is most wrong.

---

## §0 · WHAT I MEASURED AT HEAD — your numbers, checked

HEAD moved during this session (`3b3e193` → `c1fec39`); another lane is live in this repo. All
measurements below are at `c1fec39`.

| your claim | verdict | what I measured |
|---|---|---|
| 40 plants, 27 carry `zones[]`, 6 multi-zone | ✅ **exact** | 40 / 27 / 6 |
| 13 plants have no place, incl. `hydrangea`, `white-pine`, `holly`, `clematis`, `wisteria`, `lizards-tail` | ✅ **exact** | all six named are in the 13; the other seven are `pyracomeles-berry-box`, `butterfly-weed`, `clematis-elpis`, `hydrangea-dreamcloud`, `endless-summer-pop-star-hydrangea`, `spiderwort`, `creeping-fig` |
| `plant.zones` read by ZERO code in `viewer.html` | ✅ **confirmed** | every `.zones` hit resolves to `ZONES_DATA.zones`, the localStorage key, or a sync payload. No `plant.zones`, no `p.zones`, no join anywhere. The field is **write-only canon**. |
| `pond-area` holds **16 of 42** placements | ⚠️ **16 of 35** | total placements = 35, not 42. `pond-area` = 16 (46%). The rest: `st-francis-garden` 3; `the-green-ring`/`western-fern-azalea-garden`/`the-meadow`/`western-garden`/`lower-40` 2 each; six zones at 1. |
| Ten of 23 zones hold zero plants, incl. `fern-garden` | ✅ **exact** | `fern-garden`, `house`, `lawn`, `lower-parking`, `main-parking`, `stable-grounds`, `the-bank`, `the-bluff`, `the-green`, `the-green-terrace` |
| `zones[].type` untrustworthy — five parking/bank/bluff zones typed `planted` | ✅ **confirmed** | 19 `planted` / 3 `turf` / 1 `structure`. All five you named are `planted`. |
| `ZonePanel` at ~11317 with rename/confirm/flag/delete + offline voice; fires `zone_confirmed`; 23/23 `draft` | ✅ **confirmed** | module opens at `:11197`; `zone_confirmed` at `:11395`, `zone_flagged` at `:11405`; **23 of 23 `status: draft`** — it has never fired. No plant list in the panel. |
| `digest_zones()` keeps id/name/type/status only; zones is a `CORE_INCLUDES` floor with non-zero exit | ✅ **confirmed, and re-priced** | `CORE_INCLUDES = ("property","zones","turf")` `:390`; `assert_core_floor` raises either side of 4,096 / 24,000 `:550`. **But zones contributes only 489 of Fernwood's 16,614 core tokens (2.9%)** — removing it does *not* breach the floor. See §3-B3. |
| `vehicles.json` has six `household-system`; well/septic/shut-off/spigots/crawlspace hatch nowhere in canon | ✅ **confirmed** | 6 `household-system` (thermostat, furnace, water heater, washer, fridge, panel), 7 `vehicle`, 10 `equipment`. ⭐ **And all 6 carry `zoneId: null` and no `location`.** "shutoff" and "spigot" appear once each as *prose*, not records. |
| `ghPutFile` has eight call sites | ✅ **exact at HEAD** | `worker.js` `:2832 :2858 :2906 :2933 :2993 :3006 :3955 :3969`, defined `:2476`. (A 09-06 audit said "9" — that counted the definition.) |
| 24 touching pairs + 11 sub-metre slivers | ✅ **reconciles exactly** | `zone-topology-report.py` at HEAD gives 21 pairs at 0.00 m plus three at 0.03/0.06/0.07 m — **24** within rounding — and 11 pairs in 0.13–0.90 m. My raw bucketing differed; the plan's figures are right. 49 pairs under 3 m, **23 vertex-to-EDGE**. |
| Google Solar `dataLayers` never run; `LAND-SOURCES.md` says the CHM is "not yet built" | ✅ **confirmed** | zero `dataLayers` calls anywhere; the only mention is in `.plans/2026-09-06-ai-mapping-capability-SCAN.md`. `LAND-SOURCES.md:62` — *"Not yet built: a canopy-height model (DSM − DTM)…"* |

### ⭐ ONE THING YOUR BRIEF MISSES, AND IT CHANGES THE PRICE OF (B)

**The shadow-free instrument is already downloaded and already registered.**
`images/property-map/lidar-slope-2018.png` and `lidar-hillshade-2018.png` exist at HEAD, and their
`.bounds.json` reads:

- `"registeredTo": "IDENTICAL bounds to base-naip-2022-01-leafoff — drop-in layer, no re-registration"`
- `"why": "lidar is an ACTIVE sensor: no sun, therefore no shadows."`
- `"siblings": { "slope": "lidar-slope-2018.png (0-30 deg ramp; **a break of slope IS the border of several named areas**)" }`

Your argument — *for walls the right instrument is elevation, not the photograph* — is not a proposal.
**It is already half-built, and the record already states your conclusion in its own words.** The
missing piece is not a Google Solar probe or a CHM build; it is a **layer toggle in
`tools/area-trace.html`** so the person tracing can flip between the optical frame and the slope
raster at identical bounds. That is an `<img src>` swap and a keypress. See §5.

⚠️ **Its stated caveat is load-bearing and is also already recorded:** the lidar is **2018**, the
aerial **2022-01**, the traces **2026** — and Paul reshaped the western garden and that patio with
heavy equipment since. `"do NOT correct a 2026 polygon to match 2018 terrain."`

---

## §1 · VERDICT ON THE STAGED PIPELINE (A) — structure-first

### Is structure-first cheaper here?

**Yes, for a reason your framing understates:** it is not primarily a *quality* argument, it is a
**work-allocation** argument. Step 1 is downloads. Step 2 is accept/reject. Step 3 is close-against-
existing. Step 4 is the only step that needs a human who has stood on the ground. Region-first puts
a human on **all four**, and puts him on the hardest one (freehand vertex placement against a
shadowed 0.6 m/px frame) with no scaffolding. The record already measured what that costs: **437
vertices at a median 2.57 m spacing against a ±9.1 m budget** — *"sampling finer than the error is
what makes a traced line look ragged."* Structure-first is how you stop sampling finer than the
error: you stop asking a human to place points at all, and ask him to accept lines.

**But the ordering claim needs one correction.** Your table runs frame → edges → regions → names.
`_meta.fold_2026_08_31` records that Fernwood ran **names → regions**: Mom named 16 areas on
2026-08-30 and Paul traced them on 08-31. That order was *right* and produced the answer key. So
step 4 is not "last"; it is **independent**, and it is the only step that produces value if the
other three never happen. At the condo it is the *only* step that runs at all (§4).

### Does it front-load a data-structure problem region-first avoids?

**Yes — and you should take that on knowingly, because the problem is already open and dated.**

Structure-first says *"regions are closed against edges that already exist."* An edge that exists is
a **line**, and `zones.json` has no place to put one. `_meta.fold_2026_08_31` says so verbatim: three
linear features (The Path, the Upper-Uber wall, the Driveway) *"are NOT here — the zone-save round-trip
rebuilds {_meta, zones} wholesale and would silently drop any other key, so lines stayed in the plan
file pending a schema v3."* Then: *"⚠ CORRECTED 2026-09-04: schema v3 SHIPPED and added `partOf`,
NOT lines — this deferral's own stated trigger has already fired and the deferral is still open."*

So structure-first's step 2 **cannot be saved** at HEAD. The drawing half exists (`area-trace.html`
gained open polylines at `badf097`); the persistence half does not. **This is a save-path problem,
not a drawing problem**, and the 09-04 plan already says so at its §4.

⚠️ **And there is a second, sharper reason the line cannot ride in quietly.** `sanitizeZone`
(`worker.js:3745`) is a **field whitelist**: it reconstructs each zone from an explicit key list and
drops everything else, wholesale, into git *and* into the inlined `ZONES_DATA`. The repo has already
been bitten by exactly this — `partOf` and `provenance` were stripped from `the-green` and the
deletion committed, and **`check-data-inline.py` could not see it** because both sides were stripped
consistently. A `lines` key added to the schema but not to the whitelist would be **silently deleted
on the next zone save**, behind a 200.

### ⭐ THE CLAIM YOU ASKED ME TO TEST

> *"if regions are built from SHARED lines, adjacent zones cannot disagree — the 24 touching pairs
> and 11 sub-metre slivers stop existing by construction, and Tier 2 becomes unnecessary rather than
> deferred."*

**The mechanism is true. The conclusion is true. The stated reason is false, and the true reason is
better.**

**True:** a planar/topological model stores each boundary **once** and links the faces that share it,
so two adjacent regions *cannot* disagree — there is nothing to disagree with. That is the standard
distinction between the simple-features model (each polygon is a separate unit; shared boundaries are
duplicated in every geometry) and the topological model (nodes/edges/faces; shared boundaries stored
once, consistency enforced at the data layer, not by cleanup). PostGIS Topology exists precisely for
cadastral work where *"you want to make sure two parcels don't overlap even if you change the
boundaries of one."* The 09-04 plan reached the same verdict independently at its Tier 3: Model A is
*"the only option that makes the defect structurally impossible rather than periodically cleaned."*

**False as stated:** shared lines fix nothing retroactively. QGIS's topological editing detects a
shared boundary **when you edit through it**; the 23 traced polygons were digitized independently and
their 24 touches / 11 slivers are baked into 437 stored vertices. Converting them to a coverage is
not a mode change, it is a **repair pass** — and a repair pass is exactly what Tier 2 is. Structure-
first does not delete Tier 2's work. It deletes Tier 2's *future*.

**⭐ The true reason Tier 2 dies is ruling 3, not ruling 5.** Tier 2's entire subject is the 23 traced
polygons. Ruling 3 freezes them as the answer key and says Mom starts blank. **Nobody will ever edit
those 24 pairs again.** Fixing them would be work on a record whose only remaining job is to be
compared against — and "improving" an answer key after the fact is the one thing you must not do to a
control. **Tier 2 is not unnecessary because a better mechanism replaced it; it is unnecessary
because its subject was retired.** Say it that way in the epic, because the two reasons predict
different futures: the first implies "build topology and the sliver problem is solved," the second
implies "the sliver problem is solved *whether or not* you build topology, and topology has to earn
its keep on new work alone."

### Is there a cheaper 80%?

**Yes, and one of the two candidates is measured to fail here. Do not propose vertex snapping.**

`zone-topology-report.py --snap` at HEAD:

```
tol 0.25 m → 365 nodes from 437 vertices · largest cluster   3 · max point moved  0.12 m
tol 0.50 m → 351 nodes from 437 vertices · largest cluster   5 · max point moved  0.47 m
tol 1.00 m → 285 nodes from 437 vertices · largest cluster  15 · max point moved  2.12 m
tol 2.00 m → 171 nodes from 437 vertices · largest cluster 119 · max point moved 20.13 m
```

Two independent reasons it under-delivers, both already in the record:
- **23 of 49 sub-3 m pairs are vertex-to-EDGE** — the nearest thing is the *middle* of the neighbour's
  segment. **Vertex snapping cannot close a vertex-to-edge gap.** It is the wrong operator.
- **Tolerance is bounded by vertex spacing (~0.5 m), not by the accuracy budget (±9.1 m).** The
  intuitive choice destroys the map — read the largest-cluster column. QGIS practitioners hit the
  same wall: too-generous tolerance welds features that were never meant to share geometry.

**The cheap 80% that does work is the one Paul proposed himself on 09-04**, and the record calls it
better than the question it was answering:

> *"what would be best is for you to help me be able to draw the barriers or the landmarks on the map…
> maybe landmarks on the map are more important than trying to set zones by individual vertices."*

Because ***a shared border IS a line*** (`badf097`'s own commit body), drawing the wall between two
zones **is** answering "do these two abut?" — and it yields a **record** instead of an opinion.
That is the 80%: **lines in the schema + a line-aware tracer, with regions still stored as ordinary
closed rings.** You get the authored shared boundary without the node/edge/face data structure, and
you keep GeoJSON-shaped storage that every tool can read.

⛔ **What the cheap 80% does NOT give you:** nothing *enforces* that a region's ring follows the line
it was closed against. It is a convention held by the editor, not an invariant held by the data. A
later drag through the region reopens a sliver and no code notices. That is the honest gap, and it is
the reason a `check-zone-topology.py` — reporting slivers as *numbers that move*, flagging and never
editing — is the right companion to the 80% and not a substitute for it.

**Full planar enforcement (Tier 3 / Model A) is real, and it is not this quarter's work.** The
academic tooling is converging (GeoPlanar, 2026 — planar enforcement and coverage-topology repair for
Python; PostGIS `postgis_topology`; GRASS's native topological vector model). But adopting it forces
a storage format on you — an edge table and a face table, not a polygon list — and this app stores
its geometry as **a JSON file in a git repo re-inlined into a 17,900-line HTML page**. That is not a
place a topology store goes. It goes in behind the geometry-leaves-git work, or not at all.

---

## §2 · WHAT ZONES × PLANTS COSTS AT HEAD

### The finding that sets the price

**The join already exists in canon and is read by nothing.** 35 placements across 27 plants, stored
as `[{"zoneId": "..."}]` — a single-key wrapper object, which is a good shape (it has room for
`count`, `plantedAt`, `note` later without a migration). And **`ZONES_DATA` and `PLANTS_DATA` are
both already in scope in the same file.** There is no fetch, no API, no schema change, no migration,
no deploy dependency.

**So the cost of v1 is not data work. It is two render functions and the words in them.**

### The smallest genuinely useful thing

Not a map feature. **Two reciprocal lists, each answering a question someone actually has:**

1. **In `ZonePanel.open()` — "what's here?"** The panel currently shows a name, a status, a rename
   control, confirm/flag/delete, and a microphone. It answers *what is this called* and never *what
   is in it*. Filter `PLANTS_DATA.plants` where any `zones[].zoneId === zone.id`; render the names.
   **~15 lines.** This is the half that pays: it turns a shape into a place with things in it, and it
   is the first content the panel has ever had that was not authored *about* the panel.
2. **On the plant card — "where is this?"** `renderPlantCard` gains one line resolving
   `plant.zones[].zoneId` → `zone.name`. **~8 lines.**

⭐ **Do (1) before (2), and if only one ships, ship (1).** Measured reason, not taste: her funnel is
**depth 2 and depth 3 both zero across lap 8's window** — *"she reads card faces and does not open
individuals."* A line on a plant card lives at depth 2. The ZonePanel is reached from the map, which
is a **jump-strip-adjacent affordance**, and the jump strip is the one thing in the app with a
**5→5, 100% take rate**. Put v1 where she demonstrably goes.

### What v1 buys beyond the pixels

- **It makes `zoneId` assignment worth doing.** The A2 hold explicitly does *not* cover
  `zoneId` assignment on unplaced plants — it is *"canon structure, invisible to her, and W9's soil
  fold depends on it."* Today filling in the 13 unplaced plants changes **nothing anyone can see**,
  which is why 13 are still unplaced. After v1 it changes a rendered list. **v1 is the thing that
  gives the canon work a consequence.**
- ⭐ **It is the cheapest honest test of whether zones matter to her at all** — which is the A2 hold's
  own un-park trigger. Today the hold is waiting on a signal from a surface that has never had
  content in it. `zone_tapped` already fires (`viewer.html:11346`), so depth is measurable the day it ships.

### What v1 exposes, and you should decide before it ships

- **`pond-area` holds 46% of all placements and ten zones hold zero.** Nine of the 23 panels will
  render an empty list. Under Paul's 09-04 rule — ***"it's better to not display something rather
  than display something that's empty"*** — an empty list must be **omitted, not rendered hollow**.
  This is already an enforced check (`qa-walk` asserts no rendered container is empty), so getting it
  wrong will trip a red on QA rather than reach her. Good.
- ⚠️ **`hydrangea` — the hub record — has no zone, while `hydrangea-dreamcloud` also has none.** The
  taxonomy rule's hub-and-roster case has **no answer for where a hub lives**, because a genus is not
  in a place. Decide whether a hub is exempt from `zones[]` or inherits the union of its roster's.
  Do not let the render function decide this by accident.
- ⚠️ **`zones[].type` is wrong on five records** (`main-parking`, `lower-parking`, `the-bank`,
  `the-bluff`, `stable-grounds` are all `planted`). v1 does not read `type`, so this is not a v1
  blocker — but the moment anything filters "planted zones" it becomes one. Fix it as canon work,
  not inside v1.

---

## §3 · THE V1 SEQUENCE, AND WHICH BLOCKERS IT TRIPS

**Which of your four it actually trips: B3 only. B1, B2 and B4 are not on v1's path.**

### B1 · `ghPutFile` has eight call sites and no household — ⏭ **NOT TRIPPED. Defer.**
Confirmed at HEAD (8 sites; the write path is one repo via `env.GITHUB_REPO`). **But v1 writes
nothing.** It reads two constants already inlined in the page. Zone *editing* trips it; zone×plant
*rendering* does not.
⛔ **One thing to record while deferring, because it is the answer-key risk in ruling 3.** If the
geometry envelope is ever widened (§4) without B1 being cleared first, **a zone save from any estate
overwrites Fernwood's `zones.json` and re-inlines `ZONES_DATA` into `viewer.html`** — two commits, in
the same repo, at the same paths (`:3955`, `:3969`). Git history makes it recoverable, so "irreversible"
overstates it; **"silently destroyed until someone notices"** is exact, and that is bad enough.
**Widening the envelope and clearing B1 must be the same change.** Write that down as a paired
constraint, not two backlog rows.

### B2 · one geometry, needs three — ⏭ **NOT TRIPPED by v1. Do not defer the schema *shape* decision.**
v1 needs no geometry. But the shape you proposed deserves a correction now, while it is free:

⭐ **Do not mint `geometry: {kind, coordinates}`. Nest a literal RFC 7946 Geometry object at
`zone.geometry` and use its own `type` discriminator.** Reasons:
1. **RFC 7946 already standardized this exact discriminated union** — `{"type":"Polygon","coordinates":…}`,
   `{"type":"LineString",…}`, `{"type":"Point",…}`. Minting `kind` means writing three validators by
   hand that already exist (`geojson/schema`, and every GIS library on earth). Inventing a synonym for
   a standard field is the shape `VOCABULARY.md` §4 exists to prevent.
2. **The `type` collision you are probably worried about does not occur.** `zone.type` is the surface
   axis (`planted`/`turf`/`structure`); `zone.geometry.type` is the geometry axis. Nesting keeps them
   in different namespaces. **Do not flatten geometry onto the zone record** — flattened, you get the
   exact `group` double-booking `VOCABULARY.md` already records as an unresolved defect.
3. **Mixed geometry in one collection is legal and normal** under RFC 7946; the practical caution in
   the field is *renderers*, not storage — some viewers display only the first type they meet. That
   is a rendering concern you own entirely (one `switch` in `renderPropertyMap`), not a storage one.
4. **`sanitizeZone` must gain `geometry` in the same commit as the schema**, or the whitelist deletes
   it. This is not optional and it is not a follow-up; it is the same defect that already ate `partOf`.

### B3 · geometry leaving git breaks `build-digest.py` — ⭐ **TRIPPED, AND MUCH CHEAPER THAN PRICED**
**Verified by execution.** With `zones.json` unavailable, `compose()` raises `FileNotFoundError` —
the build **fails**, it does not degrade. Your claim is correct.

**But the diagnosis in the brief is wrong, and the wrong diagnosis buys an expensive fix.** The
failure is **not** the `CORE_INCLUDES` floor. Measured: **zones contributes 489 of Fernwood's 16,614
core tokens (2.9%)**; dropping it lands at 16,125, comfortably inside the 4,096 / 24,000 band. The
failure is an **unguarded `load("zones.json")`** with no absent-domain path.

**So the fix is a guard, not a rework** — and the repo already has the vocabulary for it:
`instance/home.json` declares `absent: [... "zones" ...]`, and the viewer already honours
`ABSENT_DOMAINS`. Teach `build-digest.py` the same word. **Estimate: a try/except plus a conditional
`CORE_INCLUDES` filter, single digits of lines**, plus a selftest case that composes a digest with
zones absent and asserts the floor still holds.

⚠️ **Your "must land in the same commit" instinct is right and I would keep it** — not because the
fix is large, but because the failure mode is a **hard build break on the one instrument that grounds
every Guru place answer**. `MODULE_VOICE["place"]` promises *"an id that does not resolve here is not
a place"* — a closed-world negative that **requires** the names index to be present. Failing the build
is the correct behaviour today; the guard's job is to make *absence* a declared state rather than a
crash, and it must never make a **missing-by-accident** zones file look like a **declared-absent** one.

### B4 · a plural, typed place field on the nine domains that have none — ⏭ **NOT TRIPPED. But start it here.**
v1 is plants-only and plants already have the field. ⭐ **The right move is to make v1's field shape
the one the other nine copy**, rather than inventing a second one later.

Two things measured today that should shape it:
- **All six `household-system` records carry `zoneId: null` and no `location`.** The condo's whole
  place story is household systems in rooms (§4). These six are the natural second consumer and they
  are already shaped to receive it.
- ⭐ **Your "where a thing lives ≠ where the work happened" distinction is confirmed by the record,
  not just by argument** — the mower blades sharpened 707 m off-property. **Two different keys, and
  the second one is not a zone at all.** A service event's place is a point, possibly off-estate,
  possibly a business; a plant's place is a named area on this ground. Do not let one field carry
  both. `plant.zones[]` is *residence*; a service entry wants something like `performedAt`, and
  `read-geocodes.py` already exists as the instrument for a coordinate that is not a zone.

### The sequence

| # | step | trips | why here |
|---|---|---|---|
| **0** | **Rule on the ruling-1 / ruling-4 collision (§4).** Does v1 ship to the condo (reopening C7's `garden: off`) or to Mom's blank production Fernwood? | — | **Everything below branches on this.** Do not start step 1 until it is answered. |
| **1** | ZonePanel renders the plants in this zone; empty list ⇒ section omitted | — | ~15 lines, no schema, no write, no deploy dependency. Ships behind `content-steward` on the words. |
| **2** | Plant card names its zones | — | ~8 lines. |
| **3** | `zoneId` backfill pass on the 13 unplaced plants, hub case ruled first | — | Canon work, explicitly outside the A2 hold. Now has a visible consequence. |
| **4** | `build-digest.py` absent-aware guard + selftest | **B3** | Pays immediately: unblocks any instance that declares zones absent. Do **not** couple it to geometry work. |
| **5** | Read `zone_tapped` depth against the A2 un-park trigger | — | The measurement that tells you whether the epic is wanted. |
| **6** | Lines in the schema (`zone.geometry` as RFC 7946) + `sanitizeZone` whitelist + `check-data-inline` roster, one commit | **B2** | Only after 0–5. This is where the epic proper starts. |
| **7** | Geometry envelope derived from the estate anchor + `ghPutFile` tenancy — **paired, one change** | **B1** | Hard prerequisite for any drawing off Fernwood. |

---

## §4 · ⛔ WHAT BREAKS AT THE CONDO

**This is the section I would read first.**

### The blocking finding: v1 has no surface at the first instance that ships

`.plans/2026-09-03-c7-condo-paper-model-PLAN.md` is **`[paul-approved 2026-09-03]`, `stage: ready`**,
and it settles the module set: *"weather yes, **garden off** are settled by the row"* (§218). The
condo's falsifier is literally *"the 'no garden' falsifier"* — 2d asserts the condo digest has **no
plants / weeds / turf key**, `_meta.declares` says *no garden*, and `test-modules.py` proves the
harvester yields zero plant candidates.

**Ruling 1 says v1 is zones × plants. Ruling 4 says the first instance to serve is the condo. The
condo has no plants, by a stamped decision with a falsifier already written to enforce it.**

Three ways out; they are not equivalent and the choice is yours:
- **(a) v1 ships to Mom's blank production Fernwood, not the condo.** The condo remains the
  *onboarding* trial (which is what C7 and the 09-04 development goal actually scoped it as), and
  zones × plants is proven where plants exist. **Cheapest, and it contradicts no stamped plan.**
- **(b) Flip `garden: on` at the condo.** Reopens a stamped ruling and its falsifier, and asks Mom to
  populate a garden module for a condo balcony to exercise a feature — the tail wagging the dog.
- **(c) Re-scope v1 to zones × *records*, plants being the first domain.** Then the condo exercises
  it with `household-system` records in rooms, and Fernwood exercises it with plants. **Most
  faithful to the epic**, more work than (a), and it makes B4 a v1 concern rather than a deferral.
  ⭐ Note it costs less than it looks: all six household-system records already carry `zoneId: null`,
  so the field exists and is empty rather than absent.

### The second finding: at the condo the map does not render at all

Shipped 2026-09-04: *"`renderPropertyMap` returns nothing when the zones record declares no basemap."*
The condo has no basemap and never will — NAIP is farmland imagery and there is no parcel. Combined
with Paul's rule *"better to not display something rather than display something that's empty,"*
**the condo has no map surface.** So at the condo, "zones" cannot mean *shapes on a picture*. It can
only mean **named places in a list.**

⭐ **The schema already supports exactly that, deliberately.** `sanitizeZone:3751` —
*"An EMPTY vertex list is valid: a named place that has no boundary drawn yet… It must round-trip."*
**The condo's rooms, balcony and storage cage are geometry-free zones, and that is a first-class
state, not a degradation.** This is the strongest argument for v1-as-scoped: the useful half of the
zone record has never needed coordinates, and the condo proves it.

### The third finding: the geometry envelope is a hard stop, and it fails loudly

```js
const ZONE_LON_MIN = -84.40, ZONE_LON_MAX = -84.33;
const ZONE_LAT_MIN =  34.52, ZONE_LAT_MAX =  34.58;
```
A ~6.4 × 6.7 km box around Fernwood, in the **engine's** Worker, applied to every estate. At any
other address **every vertex fails `validVertex`**, so **every zone fails `sanitizeZone`**, so the
all-or-nothing check returns `400 invalid-zones` with the hint *"within the property envelope."*

**Credit where it is due: this is correctly designed.** The comment at `:3723` — *"REJECT, never
clamp… an out-of-envelope vertex means the caller's units are wrong, and the only safe answer is to
refuse the write loudly"* — is exactly right, and the all-or-nothing rule at `:3862` correctly
refuses to let a rejected zone become a **silent deletion behind a 200**. This is the honest failure
mode. **v1 never reaches it, because v1 never writes.** But **any drawing at any second estate is
100% blocked at HEAD**, and the fix is to derive the box from the estate's own anchor (which
`read-geocodes.py` and the arrival record already produce) rather than to widen it — and, per §3-B1,
**in the same change as `ghPutFile` tenancy**.

### ⚠️ The fourth finding: turning zones ON at the condo is what removes its protection

`instance/home.json` declares `zones` in `absent[]`, and the viewer short-circuits before the fetch:
`if (ABSENT_DOMAINS.includes("zones")) return;` (`:14044`). **That guard is the only thing standing
between a fresh estate and this**, at `handleZonesGet`:

> KV miss → `ghGetFile(env, "zones.json")` → **Fernwood's 23 zones, served to whoever asked.**

There is **no estate guard on the git fallback**, and a fresh estate is *by definition* a KV miss.
So **the moment `zones` leaves a new estate's `absent[]` — which is precisely what turning on any
zone feature requires — that estate is served "The bank", "Eastern Woodlands", "St Francis Garden"
on its first load.** Ruling 3 says Mom starts blank; this is the code path that breaks ruling 3, and
it breaks it *because* of the step v1 takes.

⛔ **This is my one critical (§6). It must be closed before `zones` leaves any instance's `absent[]`.**
The fix is small — the fallback should serve `{zones: []}` unless the requesting estate is the one
the repo's `zones.json` belongs to — but the sequencing is not negotiable.

---

## §5 · EDGE-SNAPPING, THE SPLIT, AND THE CONFIDENCE IDEA

### The split — **I agree, and I would make the split sharper than "accuracy vs cosmetic"**

Your argument is right and the evidence for it is already in the repo. But the cleanest line is not
accuracy-vs-cosmetic; it is **what each operation does to the stored record**:

| | intelligent scissors / livewire | Chaikin / Douglas-Peucker |
|---|---|---|
| when | **authoring time**, before a coordinate exists | **after**, on coordinates that exist |
| effect on the record | **decides** what gets stored | **changes** what is stored, or nothing (render-only) |
| failure mode | stores a wrong boundary confidently | **area bias** — measured `-10.5%` on `western-fern-azalea-garden`, `-7.7%` on `house`, while displacement stays inside the noise |
| honest label | a **capture** aid | a **rendering** choice |

⭐ **That framing does more work than yours**, because it explains *why* Tier 1 was measured as not
improving the map and still shipped correctly: it was **render-only**, changed no stored coordinate,
and is reversible by deletion. The danger you are guarding against is not "cosmetic" work — it is
**cosmetic work written back to canon**, which the topology report already names as the reason
smoothing must never be persisted: *"every distance check reads green while the smallest zones
shrink."*

So: **keep them separate, and label the axis `capture` vs `render`, never `accuracy` vs `beauty`.**
A reader six months out can check which side of that line a change falls on. "Is this cosmetic?" is
an argument; "does this write a coordinate?" is a fact.

### ⛔ The gradient-magnitude confidence idea — **do not build it, on this basemap**

The idea is not silly and it has a published relative: *A Confidence Measure for Boundary Detection
and Object Selection* (IEEE, 2001) does derive a boundary confidence from edge-cost structure. **But
it does not use raw gradient magnitude — it uses the cost of fixed-length paths from each end of a
graph arc on a watershed graph**, i.e. it deliberately measures something *more* than local contrast.
That the literature moved away from the simple form is itself the answer to your question.

**The killer is specific to this frame, and it is one sentence from the livewire literature:**

> *"Without enhancements, the boundary tends to adhere to the strongest edge in the neighbourhood
> rather than the specific type of edge currently being followed."*

**On a 2022-01-10 leaf-off NAIP frame at 34.55°N with the sun near 32°, the strongest edge in the
neighbourhood of a garden bed IS the shadow.** So:

1. **The snapper will prefer shadow boundaries to real ones.** This is not a risk, it is the
   documented default behaviour of the algorithm on an image whose highest-contrast features are
   shadows. `zones.json._meta.accuracyHonesty` already records Paul hitting exactly this by eye:
   *"a lot of shadows and that made it very hard to be exact."*
2. **The derived confidence would be maximal precisely where the result is wrong.** A shadow edge is
   a *high* gradient magnitude → *low* livewire cost → *high* "confidence". You would be building an
   instrument that is **most confident about its worst errors** — and then wiring it to the
   soft-edge honesty encoding, which is the app's mechanism for telling Mom what to trust.
3. ⛔ **That is the 2,800 ft failure mode with a decimal point on it.** This project's own doctrine —
   *"a confidently-wrong model is worse than an honestly-unsure one"* — is not a slogan here; it is
   the reason the `confidence` markers exist at all. A number that measures **local contrast** and is
   labelled **boundary confidence** is a mislabelled instrument on the surface where trust is
   load-bearing.

**And a design note independent of all that:** even a *correct* gradient confidence would measure
*"how sharp is this edge in the picture"*, never *"is this where the named place ends."* The record
already says the second question is not an imagery question: *"these polygons record WHERE A NAME
APPLIES, at the resolution of a name."* A wall can be crisp and be the wrong wall. **Retiring the
manual operator stamp in favour of a derived one would replace a human's judgement about *meaning*
with a machine's measurement of *contrast*.** Those are different quantities. Keep the manual stamp.

### ⭐ What to do instead — and most of it is already downloaded

1. **Toggle `lidar-slope-2018.png` into `tools/area-trace.html` as an alternate layer.** Identical
   bounds, drop-in, no re-registration, already in the repo, public domain. Its own bounds file says
   *"a break of slope IS the border of several named areas."* **This is the cheapest high-value item
   in the whole epic** and it needs no API, no key, no cost and no new data.
2. **Predict the shadows deterministically instead of fighting them.** The standard remote-sensing
   move is cast-shadow delineation from **known sun geometry + a DEM** — and this repo has **all
   three inputs already**: `baseImageCaptureDate: "2022-01-10"`, `sun-horizon.json`, and the 1 m
   3DEP DEM. That yields a **shadow mask** for the frame — which is both a QA overlay ("this edge
   falls in shadow, don't trust it") and, if livewire is ever built, a hard exclusion region. This is
   an honest confidence signal: *derived from geometry we know*, not from contrast we measured.
3. ⚠️ **Price the resolution honestly.** 1 m lidar at roughly ±15 cm vertical RMSE finds a wall's
   height step, but a 0.3 m-wide garden wall is **sub-pixel horizontally** and will smear. Expect
   ~±1–2 m placement — a real improvement on ±9.1 m, roughly **5×, not 50×**. Say that number out
   loud in the epic so nobody expects survey lines.
4. **On Google Solar `dataLayers` — lower your expectations before spending a probe.** Two
   corrections: the **0.1 m/px DSM is the `HIGH` tier only**, sourced from *low-altitude aerial*;
   `MEDIUM` is 0.25 m from high-altitude aerial and `BASE` is 0.25 m from **satellite**. And the API
   is explicitly **building-centric** — *"solar data for hundreds of millions of buildings"* — with
   rural coverage requiring `requiredQuality=BASE` + `experiments=EXPANDED_COVERAGE`, and `NOT_FOUND`
   expected outside coverage. For 282 Church Mountain Road, the realistic outcomes are *no coverage*
   or *0.25 m satellite around the house only* — and the meadow, the bank and the woodland edge are
   the features that need it. **It is still worth one probe** (it is cheap and it either resolves or
   closes the question) — but it is a **complement to the 3DEP work, not a substitute**, and the 3DEP
   raster is free, public-domain, redistributable, already downloaded and already registered.

---

## §6 · CRITICALITY — ENGINEERING LANE ONLY

⛔ **This ranks nothing against UX, content, research or product. Paul ranks across lanes.**

### 🔴 CRITICAL — must be closed before `zones` leaves any instance's `absent[]`
**`handleZonesGet`'s git fallback serves Fernwood's zones to any estate on a KV miss.**
`worker/worker.js` `handleZonesGet` — KV read fails or returns nothing → `ghGetFile(env,"zones.json")`
→ Fernwood's 23 named places → returned to the caller. **No estate guard on that branch.**
- **Evidence:** read at HEAD. The only thing preventing it today is the client-side
  `ABSENT_DOMAINS.includes("zones")` early return at `viewer.html:14044`, and **the v1 epic's first
  step is to stop that guard from applying.**
- **Why critical at *this* project's stakes, not enterprise stakes:** this is not a hypothetical
  multi-tenant leak. Ruling 3 says *Mom starts blank* and the frozen 23 are an answer key. If her new
  instance loads pre-filled with the very names the experiment is measuring her against, **the
  experiment is destroyed and cannot be re-run** — she cannot un-see them. The engineering defect is
  small; what it costs is not recoverable.
- **Related and already measured:** `viewer.html:14024-14034` documents this exact class — *"fetched
  `zones.json` from the ORIGIN ROOT with no estate guard… At the QA origin that file is FERNWOOD'S 23
  zones."* The client half was fixed; **the server half was not.**

### 🟠 IMPORTANT
1. **`build-digest.py` hard-fails when `zones.json` is absent** (verified by execution). Blocks every
   instance that declares zones absent from having a digest at all. Small fix; do it at step 4.
2. **`sanitizeZone`'s field whitelist will silently delete any new key.** It has already eaten
   `partOf` + `provenance` once, and `check-data-inline.py` was structurally blind to it. **Any**
   schema addition — `geometry`, `lines`, anything — must land with the whitelist in the same commit.
   *The general rule, which is worth more than the fix: a field whitelist at a storage boundary is a
   copy of the schema and it drifts silently every time the schema moves.*
3. **The geometry envelope and `ghPutFile` tenancy are one change, not two.** Widening the envelope
   without tenancy lets a second estate's save overwrite Fernwood's `zones.json` and re-inline over
   `viewer.html`. Two backlog rows invite doing the easy one first.

### 🟡 NICE-TO-HAVE
4. **`zones[].type` is wrong on five of 23 records.** Not read by v1; becomes a correctness bug the
   first time anything filters on it.
5. **`_meta.sharedBorders` still opens with a sentence its own correction retracts** — *"traced
   independently, by eye… with no vertex snapping"* is corrected 200 words later. A cold reader who
   stops at the first clause gets a false premise about the record. Lead with the correction.
6. **`ZonePanel` fires `zone_confirmed` and 23/23 are `draft` after ~40 days.** The control exists and
   has never been used. Either it is unreachable, or confirming means nothing to anyone yet. v1 is
   the change most likely to answer which.

---

## §7 · WHAT I COULD NOT VERIFY

**In the repo:**
1. **Whether the condo's places are actually rooms/balcony/storage cage.** That is from your brief and
   from the C7 stage-notes; I found **no condo zone record anywhere** — `instance/neutral-canon/`
   holds only `estate.json` and `property.json`. So "no land, no parcel, no polygons" is confirmed;
   the specific place list is your input, unverified in code.
2. **Whether the frozen answer-key instance is a separate repo or origin.** `GITHUB_REPO` is a Worker
   secret in `owner/name` form; I read no secret. My B1 overwrite argument assumes the frozen
   `zones.json` shares a repo with production's write path. **If it does not, that risk drops
   sharply** — worth one deterministic check before you act on it.
3. **Whether `read-geocodes.py` actually yields an estate anchor usable for a per-estate envelope.** I
   read that it exists and reports outcomes-only, never coordinates. Whether a coordinate is
   *available* to the Worker at save time is unverified.
4. **The 09-06 blocker list's items 2, 6 and 7** — I re-priced 1, 3, 4 and 5 against HEAD and did not
   re-verify the field-whitelist drift claim beyond reading the code comment, the "no basemap for an
   unresearched address" claim, or the full git-departure cost.
5. **Runtime behaviour of anything.** I ran read-only Python (`zone-topology-report.py`,
   `build-digest.py` in-process, canon parsing). I loaded no page, walked no seat, and called no API.
   Every claim about rendering is read from source, not observed.
6. ⚠️ **HEAD moved under me** (`3b3e193` → `c1fec39`) and the working tree changed **twice** while I
   worked: `.user-research/2026-09-07-zones-uses-landscape.md` was committed, a second research file
   `2026-09-07-zones-plants-v1-journey.md` appeared, and `.plans/2026-09-07-zones-PLAN.md` went
   modified. **Another lane is writing the plan this file is a seat for, concurrently.** All
   measurements here are at `c1fec39`; nothing that lane wrote after that is reflected. ⛔ **I read
   neither research file nor the plan's body before writing** — deliberately, so this is an
   independent read of the code rather than a restatement of theirs. Where we agree, that is
   corroboration; where we disagree, **the disagreement is real and worth resolving rather than
   averaging.** Read them side by side.

**Sources I could not reach (per your instruction — these need a browser-driven fetch):**
- ⛔ **Mortensen & Barrett 1995, *Intelligent Scissors for Image Composition* (SIGGRAPH '95) — the
  primary source. NOT REACHED.** The Drexel mirror (`cs.drexel.edu/~deb39/Classes/Papers/p191-mortensen.pdf`)
  failed TLS: *"unable to verify the first certificate."* **Everything I say about the exact cost
  function weights is therefore secondary.** The ACM DL copy is behind a paywall.
- ⚠️ **Mortensen & Barrett 1998, *Interactive Segmentation with Intelligent Scissors* (GMIP) — REACHED
  BUT NOT USEFUL.** The Cornell PDF fetched (2.1 MB) but the extractor could not recover the cost-
  function formula, the component weights, or any failure-mode discussion from it. Cached at
  `~/.claude/projects/…/tool-results/webfetch-1788828915183-v76gek.pdf` if you want to read it directly.
  **My §5 quote about adhering to the strongest edge is from a secondary summary, not from this PDF.**
- ⛔ **GeoPlanar (Rey, Fleischmann, Winkler 2026), *Planar enforcement and coverage topology repairing
  for Python*, EPB — NOT REACHED.** SAGE returned **HTTP 403** (bot-blocked). I have only the search
  snippet. This is the most current source on planar-enforcement repair cost and would be the one to
  get if you want the Tier-3 price defended properly.
- ⛔ **IEEE Xplore, *A Confidence Measure for Boundary Detection and Object Selection* (2001) — NOT
  REACHED** (paywall). My characterisation of its method — fixed-length path costs on a watershed
  graph rather than raw gradient magnitude — is from the abstract snippet only.
- ⚠️ **Google Solar coverage for Pickens County, GA — NOT DETERMINED.** The coverage page defers to an
  interactive map and downloadable GeoJSON coverage files, neither of which I could fetch. **The
  quality tiers and the building-centric framing are confirmed from the docs; the actual answer for
  this address is not.** One authenticated `dataLayers` probe settles it and nothing else will.

**Open questions I would put to Paul before step 1:**
1. **The ruling-1 / ruling-4 collision (§4).** (a), (b) or (c)?
2. **Does a hub record (`hydrangea`) carry `zones[]`, inherit its roster's, or is it exempt?**
3. **Does v1 count as un-parking the A2 hold, or does it run beside it** the way the corpus-driven
   naming pass question at BACKLOG `:329` is still unanswered? v1 renders to Mom, so I read it as
   un-parking — but the hold's trigger is *"a signal from Mom that zones matter,"* and v1 is an
   attempt to **create** that signal rather than a response to one. That inversion is worth a ruling.

---

## Files touched

**Nothing was touched. This session shipped no code and no tracked-file edit.** This artifact is the
only file written. The files below are what a v1 implementation *would* touch, listed so the sequence
in §3 can be costed.

| file | what changes | step |
|---|---|---|
| `engine/viewer.template.html` | `ZonePanel.open()` — render the zone's plants; omit when empty | 1 |
| `engine/viewer.template.html` | `renderPlantCard` — name the plant's zones | 2 |
| `viewer.html` | regenerated by `tools/build-viewer.py`; **never hand-edited** | 1, 2 |
| `plants.json` | `zones[]` backfill on the 13 unplaced; hub case ruled first | 3 |
| `tools/reinline.py` / `tools/check-data-inline.py` | re-inline `PLANTS_DATA` after the backfill | 3 |
| `tools/build-digest.py` | absent-aware `load` + conditional `CORE_INCLUDES`; selftest case | 4 |
| `RELEASE_NOTES.md` + `tools/build-release-notes.py` | user-visible change ⇒ a note | 1, 2 |
| `worker/worker.js` `handleZonesGet` | 🔴 estate guard on the git fallback | **before** any `absent[]` change |
| `tools/area-trace.html` | lidar-slope layer toggle (§5) | independent, cheap, any time |
| — deferred — | `sanitizeZone` whitelist · `zone.geometry` · `validVertex` envelope · `ghPutFile` tenancy | 6, 7 |

## Sequence

See §3's table. In one line: **rule the condo collision → ZonePanel plant list → plant-card zone line
→ zoneId backfill → digest guard → read the depth signal → then, and only then, lines in the schema.**
The 🔴 in §6 sits **outside** that order: it must close before `zones` leaves any instance's `absent[]`,
which may be earlier than step 1 depending on how the collision is ruled.

## Falsifier

Each is a statement that would be **shown false by evidence**, not by argument.

1. **"v1 needs no geometry."** → FALSIFIED if the ZonePanel plant list cannot render on a zone with
   `vertices: []`. **Test:** add a vertex-free zone to a scratch instance, place one plant in it, open
   the panel. If it renders, the condo path (§4, option c) is real. *This is also the condo's own
   falsifier and it is the cheapest test in this document.*
2. **"Structure-first makes Tier 2 unnecessary."** → FALSIFIED if any of the 24 touching pairs or 11
   slivers is ever edited after ruling 3 takes effect. **Test:** `zone-topology-report.py` on the
   frozen instance at two dates; the numbers must be identical. If they move, the answer key moved,
   and it is no longer a control.
3. **"The digest failure is a guard, not a floor."** → ALREADY TESTED, HOLDS. `compose()` with
   `zones.json` unavailable raises `FileNotFoundError`, and core tokens without zones = **16,125**
   against a 4,096 floor. Re-run if `CORE_INCLUDES` or the budget moves.
4. **"The git fallback would serve Fernwood's zones to another estate."** → **Test deterministically
   before fixing:** `GET /api/zones` against the `home` or `lab` env, whose KV holds no `zones:all`
   key. If the response carries "The bank", the finding is proven. **If it returns empty, I am wrong
   and the 🔴 downgrades** — I read the code path, I did not exercise it.
5. **"Gradient magnitude would be maximal on shadow edges."** → **Test:** compute Sobel magnitude on
   `base-naip-2022-01-leafoff.png` and compare the distribution along a known shadow boundary against
   a known bed edge. If shadow edges do **not** dominate, the §5 objection weakens. *Falsifiable in
   an afternoon with the images already in the repo, and worth doing before anyone builds a snapper.*
6. **"The condo cannot exercise zones × plants."** → FALSIFIED if `garden: on` at the condo without
   reopening C7's stamped falsifier. **Test:** `python3 tools/test-modules.py` against the condo
   estate; 2d asserts zero plant candidates. If that assertion can pass with a garden on, my §4 is wrong.

## QA

**No QA is owed by this session — nothing shipped.** For the v1 build when it runs:

- **Gate ① `tools/release-gate.py`** — per-sha, every seat walked in Chrome, zero failed actions.
  Evidence expires when the build moves.
- **`python3 tools/build-viewer.py --check`** after every template edit. ⚠️ **Green means
  REPRODUCIBLE, never RUNNING** — it compares bytes and does not parse JavaScript (measured 09-07:
  green on a build with four unterminated strings). The deploy's headless PAGEERROR check
  (`pages-deploy.py:96`) is what actually catches it.
- **`python3 tools/check-data-inline.py`** after the `zoneId` backfill — plain check first, `--fix`
  only after Paul confirms the drift is legit.
- **`python3 tools/check-estate-neutral.py --url <origin>`** — ⚠️ the **bare** form does not scan
  `viewer.html` (`_shipped_pages():61` drops it deliberately), so it says nothing about the file v1
  changes. ⛔ **And even run correctly it is coverage for NAMES ONLY.** v1 renders **Fernwood's plant
  names inside Fernwood's zone names** — if the estate guard in §6 fails, the leak is *names*, so
  this check would catch it. That is a narrower guarantee than it sounds and the §6 fix is still the
  real control.
- **`python3 tools/check-domains.py`** — the `place` domain's `cardable` / marker declarations if
  anything about zone markers moves.
- **Empty-container walk** — Paul's 09-04 rule is enforced: an empty plant list must be **omitted**,
  and the walk expands collapsed cards before judging. Nine of 23 panels will hit this path.
- **Playwright flow worth saving** (matching the standing posture): *open the map → tap a zone with
  plants → assert the plant names render → tap a zone with none → assert no empty section exists →
  open a plant card → assert its zone names render.* Six assertions, covers both halves of v1 and the
  empty case, and it is the regression guard for the omit-don't-render rule.
- ⛔ **Before any `absent[]` change:** exercise falsifier 4 above against a non-Fernwood env. That is
  the QA step that protects the answer key, and no existing check covers it.
