# ZONES — the semi-automated definition pipeline, assessed · what is a DOWNLOAD, what is a DERIVATION, and what only a person can say

- row: BACKLOG.md ▶️ NEXT · TIER 2 · 7 (the zones epic) · TIER 2 · 9 (Process B) — assessment, not a new row
- objective: O3
- class: engine · declared
- kind: assessment
- question: `[paul-asked 2026-09-10]` *"push us closer to a semi-automated zone definition, leveraging existing tools, known data sources, and quick feedback cycles… we looked last at using image recognition to define a house — could we also define a driveway and start there? What can we define automatically with some precision and validation… how do we ensure we have the right level of zoom for the screenshot… how are we gonna make this work in an end state of fully automated in-app."* Plus, mid-session: *"when do we ask if they have zones? If they're interested in the outside, how do we get to the point where zones start to play a role? Do we have a clear sense of how zone data helps reinforce and expand what we can provide from a personalized point of view?"* And: *"we have 23 zones for Fernwood… and a hand-drawn drawing from Bob of his property with zones — two evidence points."*
- seats: ai-advisor → web research on the free stack (report folded at §3; see § What I could not verify for the gaps it left)
         two read-only extraction passes over the prior corpus (the two 09-06/09-07 scans; the four research artifacts + the decisions handoff) — cited by file, not re-derived
- trails-read: handoff/handoff-zones-session.md · handoff/handoff-zones-decisions.md · .plans/2026-09-07-zones-PLAN.md (§0 first) · .engineering/2026-09-08-zones-derivability-EXPERIMENT.md · .plans/2026-09-07-derived-first-draft-PLAN.md · .plans/2026-09-07-mapping-sources-SCAN.md · .plans/2026-09-06-ai-mapping-capability-SCAN.md · .user-research/2026-09-07-zones-uses-landscape.md · .user-research/2026-09-07-zones-plants-v1-journey.md · .user-research/2026-09-06-what-a-map-is-for.md · .user-research/2026-09-06-defining-your-place-research.md · LAND-SOURCES.md · GOOGLE-EARTH-NOTES.md · tools/derive-property.py · ~/Developer/tate-commons/research/2026-09-06-bob-rolader-discovery-log.md (+ the photo)
- depends-on: .plans/2026-09-07-zones-PLAN.md · .plans/2026-09-07-derived-first-draft-PLAN.md
- stage: concept
- gate: ⛔ **NOTHING SHIPPED.** Dev only. Read-only keyless network probes; no deploy, no origin, no canon write, no `zones.json` edit, no paid API, nothing to Mom's surface. Written in worktree `zones-assess`; `worker/worker.js`, `onboarding/index.html`, `viewer.html`, `BACKLOG.md`, `tools/*` untouched (sole-writer lanes, coordinator's map 2026-09-10).
- stage-note: 2026-09-10 ET. The G1 line stands (*"features — plants, vehicles, zones — are out of scope until G1 is met"*, PLAN-OF-RECORD §G1); this is design-side and proposes no build under it.

**Grades:** `measured` (run today at HEAD `67ae3bb`) · `inferred` (from measured facts) · `proposed` (mine) · `[paul-…]` (his). The code and the exhibit: `.engineering/zones-derivability/anchors.py` · `frame-anchors.png` · `anchors-ms-footprints.json` · `anchors-osm-highways.json`. Re-runnable offline.

---

## 0 · THE ANSWER IN ONE SCREEN

⭐⭐ **The house and the driveway are not things to RECOGNISE — at Fernwood they are things to DOWNLOAD.** Both came back today from free, keyless sources on the standard library alone, and both land on the answer key. `measured`

| object | source | cost | vs. the 23-zone answer key |
|---|---|---|---|
| **the house** | Microsoft Global ML Building Footprints, one quadkey tile, filtered to the bbox | $0 · no key · stdlib+PIL · ~11 MB once per ~80 km tile | **IoU 0.76** against the hand-traced `house`; centroid **1.5 m** off; 140 m² vs 139 m² traced; height 4.96 m |
| **the driveway** | OpenStreetMap, `highway=service · service=driveway`, via Overpass | $0 · no key · stdlib · 60 KB | the way named *Church Mountain Road* ends **9 m from the house** and runs **519 m** to the public road; two branches join it. **Every one of the 23 zones has a vertex within 21 m of that network** |
| **the frame** | house footprint ∪ driveway network connected to it, + 30 m | derived from the two above | **contains 23 of 23 zones** at **408 × 433 m** — and the 459 m frame pulled by hand in August **clipped 17 of 61 spine vertices** (the lower driveway) |

⛔ **What this does NOT say.** n = 1 property. OSM driveway coverage in rural counties is a fact about the mappers, not the ground — Fernwood's drive was traced by someone, and Bob's may not have been. The Microsoft footprint is a roof outline from 2018–2022 imagery, absent for anything built since. Both are **positive-control** questions per source, not guarantees.

⭐ **And it re-reads the 09-08 experiment's loop correctly.** That loop's step 1 said *"propose the 2–3 highest-confidence objects — house · main-parking · the driveway."* Two of the three are **fetches, not proposals**. So the derivation budget — terrain ridges, texture regions, the things §5 of the plan calls edges — is spent **after** the downloads, on what the downloads do not cover, and the first human act is not *"accept this derived edge"* but ***"is this your house?"*** That is a cheaper, more answerable, more honest first question, and it is the Mama's-Perspective card shape this repo already runs on.

**Three things follow, each worked below:**

1. **The application order Paul asked for is measured, not judged** (§2): download → confirm → derive built edges → seed managed regions → hand over the rest as a refusal. Each step carries *what its view cannot tell*.
2. **The zoom question has a rule** (§3): parcel when the county gives one; otherwise the spine bbox; otherwise a radius — and **whichever tier produced the frame is written on the frame**, so the first confirm card can be *"does this picture show your whole place?"* rather than a silent guess.
3. **Zones enter the journey at the founding moment, silently, as inferred facts — and are ASKED about only through a job or a confirm card, never through a "draw your zones" step** (§5). The cascade is address → frame → anchors → names → the plants in those places, and Bob's drawing is one more data point that people think POI-first (n = 2 now, still `inferred`).

---

## 1 · WHAT WAS MEASURED TODAY — new facts, none of which the corpus held yesterday

### 1a · The two downloads, against the answer key `measured`

Run: `python3 .engineering/zones-derivability/anchors.py` (network) or `--offline` (cached). Exhibit: `frame-anchors.png`.

- **Buildings in the 459 m bbox: 3.** The house (IoU 0.76 vs traced, 1.2 m E / 1.0 m S centroid offset), a **310 m² building 99 m W / 194 m S** near the public road, and a **175 m² building 120 m E / 144 m S at the east end of a driveway branch** — 64 m from `the-meadow`'s centroid and covered by no traced zone. ⚠️ **Whose it is, nothing here knows.** That is a question, and it is exactly the kind the pipeline should produce (§5).
- **Service ways in the bbox: 6. Connected to the house by a shared node: 3.** The other three are neighbours' drives down by the road — which is why the spine must be *the network connected to the house*, not *every driveway in the frame*. First cut of the script took all six and produced a 593 × 491 m frame; connectivity brought it to 408 × 433. The rule is in the code.
- **Distance from every zone to the spine:** `main-parking` 0.1 m · `the-meadow` 0.4 m · `the-bank` 0.9 m · `lower-parking` 1.7 m … `stable-grounds` 21 m (the worst). Median vertex distance across all 23 is under 21 m for every zone but one (`stable-grounds`, 41 m).
- **Radius test, for the fallback tier:** house + 60 m holds 18/23 zones · +120 m holds 22/23 · +200 m holds 23/23. The one that needs 200 m is `the-meadow` (farthest vertex 187 m).

### 1b · Three things the Process B plan called open are now answered `measured`

| the plan said | today |
|---|---|
| *"A correct, keyless building-footprint source — Overture's paths are DuckDB/GeoParquet, neither stdlib… **This is falsifier 1 and it is unresolved**"* (derived-first-draft-PLAN § What I could not verify, 1) | ✅ **Discharged.** Microsoft's own per-quadkey tiles are plain GeoJSON-lines over HTTPS; `dataset-links.csv` indexes them by quadkey; stdlib fetches and filters one in seconds. Overture is not needed for buildings. |
| TIER 2 · 9: *"Most likely falsifier: buildings"* | same — the row's stated risk is retired |
| *"Pickens County GA publishes no free parcel API… record it as a known limit"* | ⚠️ **Refined, not reversed.** A **statewide Georgia parcel layer exists** — *"Improved Parcels"*, 3,724,546 records, *"provided as-is by the counties… made available by ITOS (University of Georgia)"*, hosted by GDOT on ArcGIS Online, last modified 2024-08 — and its MapServer answers **HTTP 403 `User does not have permissions`** without a credential. So Fernwood's parcel is **G1 (account) at best, not G0**, and not *"does not exist."* Pickens's own qPublic page sits behind a Cloudflare challenge (403 to a script). Fulton (the condo) stays G0. |

### 1c · Two instruments checked for the woods/open line, both negative today `measured`

- **Planetary Computer's 3DEP-derived rasters** (`3dep-lidar-hag`, `-dsm`, `-classification`) — the collections exist, and a bbox search at Fernwood returns **0 items**. The Georgia 2018 flight is not in that derived set. So the canopy-height model stays where the plan put it: PDAL + the raw point cloud, a conda afternoon.
- **Meta/WRI 1 m canopy height** — the level-9 quadkey tile covering Fernwood **exists on the public bucket (HTTP 200) and is 986 MB.** A COG supports range reads, but nothing on this machine reads a COG; a full-tile download per household is not a v1 act. **Lead, priced, not a v1 source.**
- **NAIP's NIR band IS fetchable** the same way the RGB is (`asset_bidx=image|4`, same bbox, same server-side render) — 2019, 2022 and 2023 pulled today. But at 8-bit, a 7-px texture window separates `the-meadow` (median 11) from `eastern-woodlands` (18) leaf-on by ~1.6× — **enough to say a region is managed, not enough to draw where it stops.** That is the 09-08 finding again (*regions, not edges*), now with NIR in hand and still true.

### 1d · What is fetchable in-app, and what is not — the seam, re-measured

Everything in §1a–1c that worked is *server-rendered raster* or *plain GeoJSON over HTTPS*. The Microsoft tile is the one thing too large for a request path (11 MB per tile; a Worker holds it badly). ⭐ **So the in-app shape is: an operator/scheduled step fetches the tile once per quadkey and stores the few KB of footprints per household; the app only ever reads those.** Same seam the plan drew, one source moved to the operator side of it.

---

## 2 · WHAT CAN BE DEFINED AUTOMATICALLY — the application order, with each view's blind spot

`[paul-stated 2026-09-08]` *"the house and a few other distinct shapes — that'll also be the order in which we apply this… at each point, what CAN'T we tell from the different views."* The order below is the confidence order, and confidence is measured where a number is given.

| # | object | how | confidence at Fernwood | ⛔ what this view CANNOT tell |
|---|---|---|---|---|
| **1** | **the house** | download (Microsoft footprints); confirm | **IoU 0.76**, 1.5 m centroid `measured` | which building is *the* house when there are three; anything built after the imagery epoch; a porch or deck (roof outline only) |
| **2** | **the driveway + parking** | download (OSM service ways connected to the house); confirm | 9 m from the house, every zone within 21 m `measured` | whether OSM has it at all at household N; the parking *area* (OSM gives a line; `main-parking` is a 168 m² polygon 2.7 m off the line) |
| **3** | **other buildings** | download; **ask** | present `measured` | ownership — *"is the building at the end of the east branch yours?"* |
| **4** | **road frontage** | TIGERweb Local Roads (layer 8) | `Church Mountain Rd` in 0.4 s `measured 09-07` | the parcel edge along it |
| **5** | **the parcel** | county REST where free; statewide layer where an account exists; else `unavailable` | Fulton G0 · Georgia statewide **G1/403** · Pickens qPublic bot-blocked `measured` | ⛔ nothing — it is the legal frame — but it carries **owner name and mailing address**, strip at fetch |
| **6** | **water** | NAIP NIR threshold (near-black) ∩ NHD | NIR band fetchable `measured`; the threshold **untested** on the pond | a spring, a dry pond, a stream under canopy |
| **7** | **built edges** — pads, cuts, patio rims, terrace rings | 2018 lidar break-of-slope ridges | **7 of 23 borders**, +21 % lift over a wrong placement `measured 09-08` | anything regraded since 2018 (the western garden/patio, by Paul's own note); ≥30° (ramp clips); **precision 45 %** — half of what it offers is drainage in woodland |
| **8** | **managed regions** — meadow, turf | multi-date NAIP texture, interior vs surround (0.71 in all 7 frames) | *that* it is managed `measured 09-08`; NIR adds ~1.6× `measured today` | **where the mowing stops.** Regions, not edges. The line is the person's |
| **9** | **woods / open line** | canopy height (DSM − DTM) | ⛔ **no free G0 instrument reaches it today** — PC derived rasters absent here, Meta CHM 986 MB/tile `measured` | — |
| **10** | **the nine small beds** (4–11 px, 39 % of zones, 2.6 % of area) | — | ⛔ **never, on current technique** (capability scan §, unchanged) | everything |
| **11** | **names** | — | ⛔ **0 of 16, permanently** | everything |

⭐ **Read rows 1–3 against rows 7–8.** The 09-08 experiment's most useful line was *"the machine proposes edges to snap to; it never proposes a place."* That is still true of rows 7–8. **But rows 1–3 are places, and they arrive closed** — because somebody else already closed them. The one place a model *can* deliver a polygon here is the one where the polygon was a download.

⚠️ **The order is also a coverage report waiting to be written.** Each row's *cannot tell* is what `coverage.json` should carry per household, in the four states the plan already defined (`ok · empty · unavailable · unverified`). Today's run would read: house `ok` · driveway `ok` · buildings `ok (3, ownership unasked)` · road `ok` · parcel `unavailable (G1)` · water `unverified` · built edges `ok (7/23)` · managed regions `ok (region only)` · canopy `unavailable` · beds `unavailable (by design)` · names `unavailable (by design)`.

---

## 3 · THE FRAME — how the picture knows it shows the whole place

Paul: *"how do we ensure that we have the right level of zoom for the screenshot… that it encompasses all the grounds — maybe that requires verification of plot information."*

**Two different questions hide in that sentence, and they get different answers.**

- **The legal grounds** = the parcel. Only the county knows it. When it is fetchable it is the frame, full stop, and the map should draw it — it is *"the one line on the map that is a legal fact"* (capability scan). ⚠️ At Fernwood it is **not** fetchable today (§1b), and **the repo still holds no parcel polygon from any source.** The 23 zones cover 2.64 acres; whether the parcel is 3 or 30 is a number Paul can read off qPublic in a browser in one minute and nothing here can. **That read is the cheapest missing fact in this whole workstream** — see R-A2.
- **The managed grounds** = where the household's places actually are. **That is what the 23 zones measure, and the spine bbox recovers it** (§1a): everything a person named sits within 21 m of the house-plus-driveway network. `inferred`: a household's *managed* extent is the driveway network's extent plus a margin, because the driveway is how the household reaches the parts of the land it tends. Bob's drawing (§5c) is drawn around exactly that — house, garage, the drive looping in from the west.

### ⭐ The frame rule `proposed`

```
tier P  · PARCEL       parcel polygon fetched and positive-controlled  → frame = parcel bbox + 10 %
tier S  · SPINE        house footprint ∪ driveway network CONNECTED to it → frame = bbox + 30 m
tier R  · RADIUS       house footprint only (no driveway in OSM)          → frame = house + 200 m
tier X  · NOTHING      no footprint at the geocode                        → ⛔ REFUSE a frame; ask
```

**The tier that produced the frame is written ON the frame** (`frame.tier`, `frame.basis`), and it decides the first question:

| tier | the first confirm card says |
|---|---|
| P | *"We drew your property line from the county record. Does this look right?"* |
| S | *"We found your house and the drive. Does this picture show your whole place?"* |
| R | *"We found your house. Is the rest of your place inside this picture?"* |
| X | *"We couldn't find a building at that address. Which of these is your house?"* (multi-building) or a plain refusal |

**Why 200 m for tier R and 30 m for tier S:** the radius numbers are Fernwood's (`the-meadow` needs 187 m; 60 m holds 18/23) and Fernwood is *"the top of the range, not the middle"* (what-a-map-is-for §). A suburban lot needs 40 m. **These are first cuts to be replaced by the parcel whenever one exists**, and by the person's answer when it does not. ⚠️ The margin is not a precision claim: it is *"we would rather show too much ground than clip a place you will name."* Clipping costs a re-fetch and a re-registration of everything; showing extra costs pixels.

### ⛔ Two things the rule refuses to do

1. **Never centre on the geocode alone.** The Census geocoder interpolates along an address range and can land in the right-of-way (mapping-sources scan). The house footprint nearest the geocode is the anchor; the geocode is only how we find it. At Fernwood the hand-confirmed anchor sits 3.6 m from the footprint centroid, so the two agree — **that agreement is a positive control, not an assumption.**
2. **Never let the frame become the coordinate system.** `LAND-SOURCES.md`'s standing rule. Every layer registers to one WGS84 bbox with a sidecar; a new tier is a new bbox, never a redraw. Zones stay in real coordinates (`zones.json` v2) so a re-framed household loses nothing.

### The Fernwood-specific lesson

**The August frame was 1500 ft (459 m) square, centred on the house by hand — and it clipped 17 of the 61 spine vertices, the lower 130 m of the drive.** It happened to hold all 23 zones because the zones stop 187 m out. A tier-S frame would have been 408 × 433 m, shifted south, and would have held the drive to the road as well. Neither is wrong for tracing; **only one was derived from a rule that a second household can inherit.**

---

## 4 · THE LOOP — anchor, confirm, re-scope, refuse

The 09-08 experiment's §8 loop survives with one step rewritten:

```
0 · FRAME     — tier P/S/R per §3; write the tier on the frame
1 · ANCHOR    — ⭐ FETCH, not derive: house footprint(s), driveway network, other buildings, road
                → cards: "is this your house?" · "is that building yours?" · "does this show your whole place?"
2 · RE-SCOPE  — each confirmed anchor constrains the rest (a datum for the 2018 lidar offset; a
                60 m radius that removes 41 of 70 ridge candidates, measured 09-08; a texture exemplar)
3 · PROPOSE   — built edges from terrain (7 of 23 at Fernwood), water from NIR, managed REGIONS from
                texture — each carrying the view it came from and what that view cannot see
4 · HAND OVER — the remainder stated as a REFUSAL, never a weak guess: "these borders are not
                visible to any view we have — this is where the names come from you"
```

**Step 1 is the change, and it is cheaper than the version it replaces.** A derived edge asks the operator to judge a line; a download asks a person to recognise their own house. The second is a yes/no with an obvious answer, which is the only card shape that has ever run at 100 % on this project's telemetry (the jump strip) rather than 0-for-35.

⛔ **Three rules carried forward unchanged:** no cosmetic smoothing under an accuracy label · never auto-accept · never fit a 2026 polygon to a 2018 surface. And one added: **a download's absence is a fact about the dataset, not the ground** — an empty OSM driveway result at household N reports `empty` only after a positive control (a service way exists *somewhere* in a 2 km bbox), otherwise `unverified`.

### Where it runs `proposed`, in three stages toward "fully automated in-app"

| stage | who runs it | what | when it is right |
|---|---|---|---|
| **now** | Paul, laptop, `python3` | `anchors.py` + the frame rule as an operator tool; output = a frame folder + `coverage.json` + the exhibit | until three addresses in two states have run clean (the Process B falsifier set) |
| **next** | a scheduled step or an operator command at founding | the same fetches, run **once per household at `POST /api/estate`**, storing a few KB (footprint · driveway polyline · frame · tier · coverage) beside the place record as `inferred` facts | once the founding write path (coordinator's design, 2026-09-10) lands and the fetches have positive controls |
| **later** | the app, on the household's phone | reads the stored anchors; renders the frame over NAIP tiles; serves the confirm cards; the person names places over the picture | after Leg 0 (the per-estate write path) and after the map surface exists at a household origin — ⚠️ **there is no map in production at all today** (deploy allow-list) |

⭐ **Nothing in the "later" column needs a model at request time.** The whole anchor layer is deterministic fetch + store + confirm, so it sits on the right side of the capture rule (*capture stays AI-free*) and of Z-7's re-open trigger (*nothing selects or filters*). AI, if it enters at all, enters at step 3 as a *proposer* of edges the person snaps to — the seat the plan already reserved for it.

---

## 5 · DISCOVERY — when do zones enter a household's journey, and how

Paul, mid-session: *"do we even ask, and when do we ask, if they have zones? If they're interested in the outside, how do we even get to the point where zones start to play a role?"*

### 5a · The honest current answer, from the corpus

- **Onboarding today ends at the address and a wait.** Three screens: recognised · the address · the wait. No zone is asked for. The interests list already offers a rankable **`map-zones`** row (*"A map you draw yourself — trace your own areas"*) and `map-points` (*"The shut-off valve. That repair."*) — so *whether they are interested* is already an onboarding signal, and `read-onboarding.py` reads it (0 real rows so far).
- **The founding moment is being designed right now** (coordinator, 2026-09-10, design not ruling): `POST /api/estate` writes the registry row, then `<estateId>:place` — verbatim address · coordinates · **countyFips** · elevation · hardiness · provenance — then the digest, then the grant. **One asked field, six derived facts, three honestly absent**, and the derived facts become the household's *first Mama's-Perspective cards* (*"I think you're at about 1,420 ft — is that right?"*).
- **The rulings that bind:** Z-10 zones first, plants second; Z-11 the cascade (each ask scoped by the previous answer); Z-12 ready ≠ pushed; *"the surface answers, it never summons"*; the trigger is hers and cannot be scheduled (v1 journey §); Mom starts blank; Z-ACK closed.

### 5b · ⭐ Where zones enter: at founding, silently — and are ASKED about only through a door the person opens `proposed`

**The cascade, extended one rung down:**

```
address  →  frame + anchors (derived at founding, inferred, unasked)
         →  "is this your house / your whole place?"     (a confirm card, waiting at the door)
         →  "what do you call the bit by the …?"           (naming, over the picture, in conversation)
         →  "what's growing in the <her name>?"            (plants, per place, the set closed by her)
```

**Three consequences, and the second is the one that answers Paul's question:**

1. **Zone data exists before anyone is asked anything.** The house, the drive, the frame and the coverage report are derived at founding the way elevation is — `inferred`, sourced, absent-when-missing. A household that never opens the outdoors still has a correctly framed picture of its place, and a household that does has the picture already waiting. **Nothing is asked to get here.**
2. **"When do we ask if they have zones" dissolves into "which door did they open."** Three doors, each with its ready question (Z-12: prepared, never fired):
   - **the interest door** — they ranked `map-zones` or `map-points` at onboarding → the first outdoor card is the tier-appropriate frame confirm (§3);
   - **the job door** — *"I'm breaking out the fertilizer — what plants?"* — the only validated trigger, and it arrives as a *worklist need*, not a map need → the answer is a per-place list, which needs places, which needs names, which the picture elicits (v1 journey, steps 3–5: aerial on the table, *"what do you call this bit?"*);
   - **the capture door** — a photo, a note, a Guru turn *about* a place → the place gets named at the moment of capture (*"a plant added while she is in or naming a place carries its place for free"*, plan §6b).
   ⛔ **There is no fourth door called "we ask everyone to define zones."** That is the 0-for-35 ask shape, and Z-12's guard exists to stop exactly this feature from growing one.
3. **The first outdoor question is never "draw."** It is *recognise* (your house), then *name* (over a picture), then *list* (what is in it). Drawing stays Paul's test instrument (Z-4, Z-9) until the derived edges are good enough to snap to — and at the condo there is nothing to draw at all, so the same three questions run over a floor sketch or nothing.

### 5c · The two evidence points Paul named

**Fernwood's 23 zones** — the answer key, 23 of 23 `draft`, 0 ever confirmed, 16 names that have never changed across every re-trace. Today they measured the downloads (§1a). ⚠️ Two numbers are in circulation: **23 in canon, 18 served** in production KV (plan §9a). This file uses 23 throughout, per `[paul-stamped 2026-09-08]`.

**Bob's hand-drawn map** (`tate-commons/research/2026-09-06-bob-map-and-paul-notes.jpeg`, his hand, one of his two houses). Read today against §2's order:
- He drew **POI-first**: Main House, Master Bedroom, Garage, Parking Zone, steps, *a drive looping in from the west* — then filled the space between with named places: Lawn, House Garden, Grill Garden, Cut Flower Garden, Sun Garden, Rose Garden, White Pine Garden, Hemlock Garden, Play Ground, Wild Zone, Uphill Zone. **~14 names, one house.**
- **Every anchor he drew first is a §2 row 1–3 object** — house, garage, drive, parking. What he filled in afterwards is rows 8–11: managed regions and named beds. ⭐ **His own ordering is the pipeline's ordering**, reached from the other side.
- His labels include **"Wild Zone"** and **"Uphill Zone"** — places defined by *what is not done there* and by *terrain*. Row 8 (managed vs not) and row 7 (slope) would propose both as regions; neither could name them.
- ⚠️ **Grades, kept honest:** the labels are a **model read off a photograph, unverified handwriting** (discovery log's own flag) — confirm with Bob before any becomes a record. POI-first-then-infill is now **n = 2** (Mom over an aerial, 16 names; Bob on paper, ~14) — still `inferred`, and both drawn *for Paul*. And the second sheet in that photo is Paul's, not Bob's — *"file the items as things said; do not file the structure as Bob's."*
- **What Bob's case adds that Fernwood cannot:** his OSM driveway and Microsoft footprint are **unmeasured**. Running `anchors.py` at his address is the first out-of-answer-key test of §1a, and it is one command — ⛔ **his address is never-public and the output must land in `.private/`, never `research/frames/`** (the plan's own privacy QA line).

### 5d · What the research says is NOT clear, and this file does not pretend to settle

- Whether a person will **correct a map somebody else drew** — zero observations behind the whole of *we draw, they confirm*.
- Whether hidden-at-n=0 is right for the garden module (Paul's call).
- Whether the shipped `This Month` grouping already answers her sentence unaided — *"if it does, the v1 is smaller than anyone thought."*
- The next-question machinery cannot yet produce *"what do you call this place?"* at a blank instance — no card, no marker, no fold target (plan §6c-b, the honest gap).

---

## 6 · WHAT ZONE DATA BUYS — personalization, in the order it becomes true

Paul: *"do we have a very clear sense of how zone data helps reinforce and expand what we can provide from a personalized point of view?"* **Partly. Here is the honest ledger.**

| what zones make possible | needs | state at HEAD | grade |
|---|---|---|---|
| **Garden Guru answers by place name** (*"what's near the pond?"*) | names only | ✅ shipped — `digest_zones()` is a name index, since July | `measured` |
| **The per-place worklist for a job she chose** — *"you're fertilizing? here are the 4, in these 2 places"* — and the **honest gap** beside it (*"12 more we haven't written a place for yet"*) | names + `plant.zones[]` + care months | data exists (27/40 placed); **no code reads `plant.zones`**; the confirm act has never fired | `measured` · v1 |
| **Completeness closed by her, per place, on a date** — the first honest denominator | the cascade (name a place, then list what is in it) | designed (Z-11), not built | `inferred` |
| **A correctly framed picture of the place, with the house and drive on it, before anyone is asked** | §2 rows 1–3 + §3 | **measured today at n=1**; nothing stored per household yet | `measured` / `proposed` |
| **Household-system points** — well, septic, shut-off, spigots (Bob's own list: shut-off valves, breakers, water filters, ditch levels) | a point primitive + the subject records | ⛔ no point primitive; well/septic/shut-off are records nowhere in canon | `assumption` on demand, `validated` as words Bob and Mom both said |
| **Photos by place** | a name to join on (never a polygon) | photo-organizer joins to `serviceHistory`; 12 of 18 zones under the join's floor | `measured` |
| **Sun / horizon / frost-pocket per place** (which bed gets afternoon shade; which hollow frosts first) | terrain layer + the frame; zero user input | derivable from the 2018 lidar already on disk; nobody has asked for it | `assumption` on demand |
| **Weather per place** | multiple sensors or microclimate zones | ⛔ decoration today — one station, one place | `inferred` future |
| **Project sites over time, handover to the daughters, the portrait** | names + dates + photos | Bob named all three unprompted (*"one repository: how things work, what he has worked on, and when"*, share with daughters) | `inferred` from n=1 conversation |
| **A coverage denominator** — *how much of the place has a record at all* | names + the frame | computable, never computed | `validated` computable |

⭐ **The pattern:** every row's *needs* column starts with **names**, and none of them starts with *polygons*. That is the plan's primitive (*a named place, geometry optional*) confirmed from the demand side. **Geometry buys exactly two things** — the picture that elicits the names (§5c: both evidence points came from a person looking at a picture), and, later, per-place terrain facts nobody has yet asked for. Everything else is a join on a name.

⚠️ **What is genuinely not clear:** how much of this a *non-gardening* household wants. Every validated demand signal is Mom's (gardening) or Bob's (systems, handover, finances). The `map-zones` interest row at onboarding is the instrument for that and it has 0 real rows.

---

## 7 · ⭐ RULE THIS — Paul's, each as question · recommendation · alternatives

| # | question | recommendation | alternatives |
|---|---|---|---|
| **R-A1** | **Adopt the frame rule (§3) as the v1 of Process B's frame step?** | ✅ **Yes, as a first cut** — tier P/S/R/X with the tier written on the frame and the confirm card wording per tier. Replace the numbers as parcels and answers arrive. | (b) parcel-only, refuse without one — kills every county like Pickens · (c) fixed span from the geocode — the August method, and it clipped the drive |
| **R-A2** | **The parcel at Fernwood — three cheap paths, pick one or none.** | ⭐ **Read the acreage and lot shape off qPublic in your browser** (one minute; Claude-in-Chrome can drive it if bot-blocked, per Z-8) and record it in `LAND-SOURCES.md` as VERIFIED. It answers *"is the frame the whole grounds"* at the one address with an answer key. | (b) request an account on the UGA ITOS / Georgia GIS Clearinghouse statewide layer (G1 — an account, not a card) · (c) phone the county (the scan's own suggestion) · (d) leave `unavailable` |
| **R-A3** | **Is the 175 m² building at the east end of the driveway branch yours?** (120 m E / 144 m S; no traced zone covers it) | Answer it — it is the pipeline's first *"is that building yours?"* card, asked of the one person who knows. If yes, it is a place with no name yet; if no, the frame rule has a neighbour case to learn from. | — |
| **R-A4** | **Do the anchors (footprint · driveway · frame · tier · coverage) get written at founding, beside the place record, as `inferred` facts?** | ✅ **Yes** — it is the same tier-2 *deferrable, must not gate founding* class as elevation, it costs a few KB, and it makes the first outdoor card possible without an ask. ⚠️ Routes through the coordinator (`POST /api/estate` is `tate-tracker-ec`'s lane); this file only proposes the fields. | (b) derive on first open of the outdoors — later, but the fetch is then on a request path (the Worker cannot hold the 11 MB tile) · (c) operator-only forever — Z-9 says no |
| **R-A5** | **Run `anchors.py` at Bob's address** (dev, `.private/`, nothing sent)? | ✅ **Yes** — it is the first test outside the answer key, it costs one command, and it tells us whether OSM has his drive before anything is designed around OSM. | wait for a third address first |
| **R-A6** | **The G1 line vs this file.** Everything above is design; the operator tool exists in `.engineering/`. Does *"run it at founding"* (R-A4) count as feature work under G1? | It is founding-record plumbing, not a surface — but **that is a reading, and the line is yours.** Recommend: design now, wire after G1. | wire now as part of the founding write |

---

## 8 · THE NEXT EXECUTABLE STEPS — sized, in order, none started

1. **R-A2 + R-A3** — two facts only Paul can supply, ten minutes, and they decide whether Fernwood's frame is *the grounds* or *the managed grounds*.
2. **`anchors.py` → `fetch-frame.py`'s first two register entries** (Process B plan § Sequence 1–2): buildings and driveways join roads/NAIP/terrain in `tools/frame-sources.json`, each with its positive control (*a footprint within 60 m of the geocode* · *at least one service way in a 2 km bbox*) and the four-state result. Half a day; ⚠️ `tools/*` is a BUILD-window path — lands via the coordinator, not from this worktree.
3. **Water from NIR** — the pond is the positive control (row 6), and NHD's earlier `n=0` needs the layer-id introspection the plan flagged. One session.
4. **Bob's address** (R-A5) and **one out-of-state address** — the Process B falsifier set, now with buildings answered. Two commands.
5. **The frame confirm card** — content-steward owes the wording (the seat the plan already declared OWED); the shape is the existing Mama's-Perspective card, tier-keyed per §3. ⛔ Nothing reaches Mom; Bob is gate 3 of the cascade, never gate 1.
6. **Then, and only then:** the derived edges (rows 7–8) as snap targets inside whatever tracer survives Z-9 — the 09-08 experiment's next step, unchanged.

---

## Falsifier

- **The download claim (§0) is falsified at household N** if Bob's address returns no OSM driveway and no Microsoft footprint within 60 m of the geocode. Then row 2 falls back to the least-cost path (still `proposed`, never run) and the frame to tier R. *One command tests it.*
- **The spine rule (§3 tier S) is falsified** if a household's named places sit beyond the driveway network plus margin — a back field reached on foot, an orchard across a lane. ⚠️ Likely at some rural addresses; the parcel tier exists for exactly that, and tier S must say on its face that it is the *managed* grounds, not the *legal* ones.
- **"Recognise beats derive" (§4 step 1) is falsified** if the *"is this your house?"* card runs at the same 0-for-35 as every other ask. Then the door is wrong, not the data — and the interest and job doors (§5b) are the fallback.
- **The IoU 0.76 is falsified as a quality claim** if the traced `house` was itself drawn from a roof outline — then the two agree because they share a source, not because either is right. ⚠️ Not checked: what the tracer's base image showed at the house. The 1.5 m centroid agreement with the *hand-confirmed anchor* (Google Maps, May 2026) is the independent control.
- **The whole assessment is scoped to n = 1 property + 1 drawing.** Nothing here generalises until step 4 runs.

## What I could not verify

- **Whether the ai-advisor's web-research report changes any source claim above.** It was commissioned in parallel and had not returned when this file was written; its findings are folded in a dated amendment below when they land, and any row it contradicts is corrected there rather than silently edited here.
- **OSM driveway coverage in rural Pickens generally** — one property queried.
- **The NIR water threshold** — the band was fetched, the pond was not tested.
- **The Georgia statewide parcel layer's terms** — 403 says *account*, it does not say *free account*. The clearinghouse home page answered 200; its search path answered 404.
- **The parcel's acreage** — not in the repo, not fetchable today (R-A2).
- **Whether `tools/derive-property.py` (A0) can carry the anchor fields** — read its docstring, not its writer.

## QA

- `python3 .engineering/zones-derivability/anchors.py --offline` — reproduces every number in §1a from the cached JSON; `python3 …/anchors.py` re-fetches (network, keyless). The three preconditions inherited from the 09-08 experiment still apply (frame identity; the house rasterises to ~139 m²).
- ⛔ **Not claimed:** `check-estate-neutral.py` — this file names Fernwood's places, correctly. `check-backlog-ready.py` grades `-ASSESSMENT` under no suffix it knows (the plan's own naming hazard, 2026-09-07) — **it will draw zero flags and that is a silent pass, not a clean one.** Named so it is not mistaken for coverage.
- Nothing deployed; nothing under `research/frames/`; Bob's address not used.

## Files touched

- `.plans/2026-09-10-zones-automation-ASSESSMENT.md` (this file, new)
- `.engineering/zones-derivability/anchors.py` (new) · `anchors-ms-footprints.json` · `anchors-osm-highways.json` (cached fetch results, new) · `frame-anchors.png` (exhibit, new, 1500 px)
- **Nothing else.** No `BACKLOG.md`, no `tools/`, no code the other lanes own.

## Register edits owed — for the refinement/coordinator window, not this one

1. **TIER 2 · 9** — *"most likely falsifier: buildings"* is **discharged** (Microsoft quadkey tiles, stdlib); the parcel note becomes *"Pickens: no G0 service; a Georgia statewide layer (UGA ITOS via GDOT) exists at G1/403."*
2. **`.plans/2026-09-07-derived-first-draft-PLAN.md`** § What I could not verify, item 1 — answered; § Sequence step 1 gains two register entries (buildings, driveways).
3. **`.engineering/2026-09-08-zones-derivability-EXPERIMENT.md` §8 step 1** — *"propose the 2–3 highest-confidence objects"* → *"FETCH the anchors; propose only what no download covers."*
4. **`LAND-SOURCES.md`** — promote Microsoft footprints and OSM driveways from LEAD to VERIFIED at these coordinates (2026-09-10); add the Georgia statewide parcel layer as a G1 lead with the 403.

---

## AMENDMENT · 2026-09-10 later — the ai-advisor web-research seat returned; what it changes above

The seat ran its own probes at Fernwood (not a re-read of mine) and **independently reproduced §1a**: Microsoft footprint IoU **0.754**, centroid **1.53 m**, area 141 m²; OSM way 1507899125 at **3 m** from `main-parking` and `lower-parking`, **7 m** from `house`. Two measurements, two sessions, one answer. Its full report is in the session transcript; the rows it changes are corrected here rather than edited above.

### ① ⛔ A LICENSING SPLIT the assessment did not carry, and it decides what may be STORED `[reported by the seat; licences read from the sources' own pages]`

| source | licence | consequence |
|---|---|---|
| NAIP · 3DEP | public domain | ship, store, redistribute |
| **Microsoft footprints, pulled DIRECT** | **CDLA-Permissive-2.0** | store as household geometry |
| **OSM driveway (Overpass)** | **ODbL — share-alike on a derived database** | ⛔ a stored polyline is a derived database. **Store it as a HINT with its source; the record is the human's retrace over it** |
| Overture buildings | ODbL — *the same Microsoft geometry, re-licensed worse* | never — pull Microsoft direct |

⭐ **This does not weaken §0; it sharpens §4 step 1.** The driveway is still a download, and the *frame* derived from it is a produced work, not a database. What changes is the **record**: the house footprint may be written to the household as geometry; the driveway is rendered as a distinct-style hint that a person retraces with two clicks — which is Z-5's *"points and walls first, then subdivide"* with the wall already drawn for them. **R-A4's field list is amended:** `footprint` (stored) · `drivewayHint` (source + timestamp, not canon) · `frame` · `tier` · `coverage`.

### ② ⭐ NAIP IS BROWSER-CALLABLE, 4-BAND, WITH NO ZOOM CEILING `[verified by the seat: HTTP 200, 800×800 GeoTIFF, `bandCount=4`, `pixelSize=0.3`, `access-control-allow-origin: *`]`

`imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage` renders any bbox server-side and answers CORS `*`. **The "later" column of §4's table just got cheaper:** the household's phone can fetch its own basemap at the frame bbox directly, no Worker relay, no Python. ⚠️ The free XYZ tile cache is **not** this — it 404s above z16 at Fernwood (2.4 m/px), confirming `images/property-map/README.md`'s note. Use `exportImage`, never the tile cache, for tracing resolution.

### ③ ROW 9 (woods/open) MOVES: the data is G0 and range-readable; only the tool is missing `[verified by the seat]`

The 2018 LAZ tiles are on the public bucket with `accept-ranges: bytes` — three tiles ≈ **65 MB one-time** — carrying ASPRS classification (**class 6 = building**, class 2 = ground). That is (a) a shadow-free, canopy-blind building mask to cross-check Microsoft with a sensor that shares none of its failure modes, and (b) the DSM − DTM canopy height model. **PDAL is still the gate** (a conda afternoon, as the plan priced it). Row 9's *"no free G0 instrument"* becomes *"G0 data on disk in minutes; the instrument is one install away."* Also confirmed: the 2025 Georgia 9-county 0.5 m leaf-off lidar **does not reach Pickens** (TNM returns nothing here) — watch it, do not wait for it.

### ④ THE GEOCODER IS 55 m OFF AT FERNWOOD `[verified by the seat: Census → 34.549318, −84.367964]`

§3's first refusal (*never centre on the geocode alone*) now has its number. The nearest Microsoft footprint within 100 m of the seed is the anchor; at Fernwood that snap corrects 55 m to 1.5 m. **A 100 m search radius and a 30–1,000 m² plausibility band** are the seat's proposed acceptance floor for the anchor step, and they are adopted into the frame rule as tier X's threshold: no footprint inside 100 m → refuse and ask.

### ⑤ ⚠️ A DISAGREEMENT ON THE FALLBACK FRAME, resolved by the answer key

The seat recommends **a fixed 250 m square centred on the footprint** and states the 23 zones *"span 138 × 231 m."* The span is right; the conclusion is not: **the zones are not centred on the house.** Measured (§1a): W −65 · E +166 · S −121 · N +16 m from the anchor, and `the-meadow`'s farthest vertex is **187 m** out. A ±125 m square centred on the footprint **clips `the-meadow`**; ±120 m holds 22/23, ±200 m holds 23/23. **Tier R stays at 200 m** — and this is the argument for tier S over any fixed number: the drive is what tells you *which way* the grounds run.

### ⑥ Smaller corrections carried

- **Microsoft's `confidence = −1.0` is a placeholder**, not a score — the footprint carries no usable confidence signal. Published: precision 92–97 %, **recall 71–86 %**, IoU 63–68 %, imagery 2014–2024. So row 3 (other buildings) is **1-of-N recall**: an outbuilding may simply be absent, and absence is not evidence.
- **Published rural-NAIP building detection tops out at IoU 0.43** (Remote Sensing 14(15):3622, 2022, failures attributed to *"roofs covered by trees, areas in shade"*). Microsoft's shipped 0.754 nearly doubles it. ⭐ **Do not build a NAIP building detector** — the seat's conclusion, and it is the `[[feedback_check_standards_before_building]]` shape in a new domain. The seat proposed a playbook line (*"check the shipped product before building the detector"*); **not written — Paul's call whether it is a second example under that memory or a Fernwood pattern.**
- **Parcel, three more paths for R-A2:** a $300 one-time county shapefile (MappingSolutionsGIS, 22,091 parcels, 2025 vintage — an engine-N cost, not a today cost); the **GSCCCA plat index** (free search; the recorded plat is the *authoritative* boundary, a one-time human read); the Georgia GIS Clearinghouse parcel list (**unverified** — the page would not render for the seat either). And `LAND-SOURCES.md`'s *"Pickens County GIS / qPublic"* LEAD should be **downgraded to 403-walled** (register edit 4 gains a line).
- **Overpass is rate-limited and not a production dependency** — snapshot the hint at founding, never fetch it on a request path. Same rule as the Microsoft tile.

### ⑦ One test added to §8, between steps 2 and 3

**Buffer the OSM driveway at 2.5 / 4 / 6 m half-width and score it against `main-parking` and `lower-parking`.** If a width explains the linear part of both and leaves a residual apron, *"derive the drive, the person draws the apron"* is a real division of labour; if not, it is wishful. One script, cached data, no network.

### What the seat could not verify, carried honestly
Whether Pickens appears in the Clearinghouse parcel list · whether qPublic has a browser-reachable service behind its 403 (a Claude-in-Chrome session answers it in two minutes — Z-8) · Regrid free-tier geometry terms · Clay/DOFA at sub-metre.
