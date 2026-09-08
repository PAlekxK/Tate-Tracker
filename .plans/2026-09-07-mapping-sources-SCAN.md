# Mapping sources — every scale, what it costs to REACH, and whether we may KEEP it

- row: `BACKLOG.md` § ▶️ NEXT · zones as an epic — this file seats under it as a **source scan**. ⛔ **No row proposed and nothing ranked across lanes** (`[paul-ruled 2026-09-07, J-b]`); §16 states only what is critical *within this lane*, with evidence.
- objective: **O3** — *Fernwood is instance 1 of a product; the engine transfers to a second estate without a fork.* Every question in this file is *"does this source exist at household N, and may we keep it."*
- class: engine · **declared** *(this is a research artifact, not shared machinery. ⚠️ If any of it becomes a **source registry** that the onboarding path reads, that registry is `engine · must-not-diverge` — a second copy of "where the parcel comes from" is exactly the drift this repo pays for. Paul assigns the tier.)*
- question: what mapping data exists at every scale from a room to the globe; what it takes to **reach** it; whether we may **store and serve** it; and what it costs at household **N**
- seats: ai-advisor (sole). ⛔ Not a substitute for engineering-partner on any build; nothing here is scoped as work.
- kind: census
- gate: ⛔ **NOTHING SHIPPED.** No code, no deploy, no purchase, **no API key created, no paid call made, no account signed up for.** Four **free, unauthenticated, read-only** probes were run (§Probes run). No tracked file edited outside this one.
- extends: `.plans/2026-09-06-ai-mapping-capability-SCAN.md` (mine, 817 lines). ⭐ **Part II §10 is not redone.** Where it was right this file says so in one line and moves on; §§3–9 below extend it along **five axes it did not carry**: the indoor scale, access mechanics, storability-as-product-boundary, cost at scale, and how each source *fails*.
- trails-read: `.plans/2026-09-06-ai-mapping-capability-SCAN.md` · `LAND-SOURCES.md` · `images/property-map/*.bounds.json` · `.user-research/2026-09-06-what-a-map-is-for.md` §3 · `OBJECTIVES.md` · `property.json` §soils
- cites-does-not-edit: `.plans/2026-09-07-zones-PLAN.md`

---

## 0 · The eight findings, before the tables

1. ⭐⭐ **AT THE UNIT SCALE THE PUBLIC RECORD GIVES YOU IDENTITY WITHOUT GEOMETRY — and I measured it.** Fulton County's free parcel service carries **151 parcel records over 22 distinct polygon areas** within ~166 m of Mom's condo (**935 records / 136 polygons** at ~333 m); **112 of the 151 carry a unit number**; one neighbouring record declares **322 living units on a single 3.6-acre polygon**. Condo units are **stacked on one shape**. So the free record answers *which unit* and never *where in the building* — which is, arriving from a completely different direction, the **`a named place, geometry optional`** primitive `.user-research/2026-09-06-what-a-map-is-for.md` §3.1 already reached. **Third independent occurrence.**
2. ⭐⭐ **THE FREE-ONLY RULING'S WEAK POINT IS THE COUNTY, AND IT IS WEAK AT FERNWOOD'S OWN COUNTY.** Aggregators cover ~3,227 counties / 99.7% of the US population — but **only about ten states publish a full, free, digital statewide parcel layer**, and in New York only **38 of 62 counties** have permitted public sharing at all. A targeted ArcGIS Online / Hub search for *Pickens County Georgia parcels* returns **Pickens County AL and Pickens County SC** and no Georgia service. **Pickens County GA appears to publish no free parcel API** — qPublic is a web application. **Free-only means: the parcel is solved at Mom's condo (Fulton, free REST, 373,305 parcels, no key) and unsolved at Fernwood.** That is the honest statement the brief asked for.
3. ⭐ **THE GOOGLE SOLAR PER-CALL FIGURE WAS RIGHT; THE ACCESS CLAIM WAS THE ERROR — and there is a free tier nobody had found.** `dataLayers` is **$75.00 per 1,000 calls = $0.075/call**, confirmed on Google's own price list — **and the first 1,000 calls per month are free** (Building Insights: $10/1,000, first **10,000/month free**). ⚠️ **The free tier is not "free":** it requires a Google Cloud project with **billing enabled and a card on file**, and `grep` for `googleapis` across every `.py`/`.js`/`.json`/`.toml` in this repo returns **zero**. **Reach cost ≫ call cost.** That is the whole reason this pass exists, and it generalises: *"free" and "reachable without a credential" are different columns.*
4. ⭐⭐ **THE ENTIRE FREE STORY RESTS ON ONE PROGRAM, AND THAT PROGRAM HAS A DOCUMENTED LICENSING PROPOSAL IN ITS PAST.** In 2017–18 USDA FSA weighed making NAIP a **licensed COTS product** over a **$3.1 M** funding shortfall, and stated it had *"not identified any regulatory or statutory requirements that mandate the release of NAIP data to the general public."* **It was never enacted** — NAIP is public domain today. ⚠️ But this is the single-point-of-failure under "use what's free," it has no statutory floor, and **it should be a named risk rather than an assumption.**
5. ⭐ **RAW POINT CLOUD BUYS ~2×, NOT ~10× — measured, not recalled.** The USGS public EPT for the two 2018 Georgia blocks whose bounding boxes contain the anchor carry **42.7 bn and 43.1 bn points**, giving a **lower bound of 3.7–3.9 pts/m²** and a **nominal point spacing of ≤ 0.50–0.52 m**. So the raw cloud takes 1 m → ~0.5 m and **stops there**: terraces yes, a 0.5 m wall marginal, a bed edge never. ⭐ **Its real value is not resolution at all** — it is the three things the finished DEM cannot express: **CHM (first return − ground), intensity, and return classification.** §10.
6. ⚠️ **THE MULTI-TEMPORAL SHADOW IDEA HAS A NAME, A LITERATURE — AND A GEOMETRIC DEFECT THAT KILLS IT AT n=7.** The family is **median / medoid compositing** and **multi-temporal shadow detection**, and it works because clouds and shadows land in *different places* across dozens of passes. **NAIP shadows do not move.** All seven frames are near-noon at 34.5° N, so every shadow points **broadly north from the same object every time**; only the *length* varies (0.50× → 1.52×). The intersection of seven shadows is **the shortest one**, so *"present in all seven"* promotes the first **0.50 × height** of every shadow to "real feature" — a ~10 m persistent dark band off a 20 m tree. §11 gives three more confounds and the repair.
7. ⭐ **NO FREE 0.1 m DSM EXISTS IN THE US.** The free ceiling is lidar-derived: **QL1 (>8 pts/m²) publishes a 0.5 m DEM cell**; Fernwood's 2018 block measures ~3.7–3.9 pts/m², i.e. a ~0.5 m ceiling if derived from the raw cloud. Google Solar's 0.1 m is **5× finer than anything free**, and it is the one product we may not store. §12.
8. ⭐ **TWO STANDING `LAND-SOURCES.md` LEADS ARE NOW VERIFIED, FREE, IN ONE CALL EACH.** SSURGO via Soil Data Access returns **`Tallapoosa cobbly sandy loam, 25 to 60 percent slopes` (mukey 531363, survey area GA622)** at the anchor — which **selects one of the four candidates `property.json` has carried as INFERRED since July**. And `api.weather.gov` resolves the anchor to county zone **GAC227**, forecast/fire zone **GAZ013**, radar **KFFC** — no key, no account. §Probes run.

---

## 1 · The seating — what changed, and what it re-prices

| the seating | what it does to the 09-06 scan |
|---|---|
| ⭐ `[paul-ruled 2026-09-07]` **free only, for now** | **Regrid leaves the near-term path.** Re-verified this session: Regrid publishes **no flat rate** for parcel access — a **hybrid monthly base + per-record overage** behind an account, with a 30-day sandbox trial; rate limits ~200 req/min, 1,000 records/request. §10d of the prior scan said *"it is a BUY"* and that stands; what changes is **when**. It is an **engine cost at household N**, not a Fernwood cost. |
| ⚠️ **Google Solar mis-priced to Paul as "$0.075 a call"** | The number was right (**$75/1,000**). The *sentence* was wrong, because it implied reachability. **No Google credential exists in this repo** (verified: zero `googleapis` hits). It drops to **fallback**, and **ACCESS MECHANICS becomes a first-class column everywhere below.** |
| **7 NAIP frames · 2 lidar rasters · GEP 2015-03 · Esri/OSM/USGS tiles already on disk** | Not re-proposed. They are the **corpus §11 attacks and §10 extends**, not a shopping list. |
| **The v1 is zones × plants and needs no geometry** | ⭐ **So this file is honest about horizon.** Every row below carries a horizon marker: **NEAR** (usable inside the next few laps) · **LONG** (real, and years from mattering) · ⛔ **NOT FOR US**. |
| **Site premise: no cell, Wi-Fi near the house only, heavy canopy** | ⭐ **This is what turns "redistributable" from a licensing footnote into a product boundary.** See §2. |

---

## 2 · The two axes that make this more than a source list

### 2a · ⭐ ACCESS MECHANICS — because "free" and "reachable" are different claims

Five distinct gates, and they are **not** ordered by cost:

| gate | meaning | example measured here |
|---|---|---|
| **G0 — open** | anonymous HTTPS GET/POST, no account, no key, no terms click | 3DEP EPT on S3 · Soil Data Access · `api.weather.gov` · Census geocoder · Fulton parcels REST |
| **G1 — account** | free registration, then a key | USGS EarthExplorer M2M · Copernicus Data Space |
| **G2 — billing card** | free tier exists, but a payment instrument must be on file | ⭐ **Google Solar** — this is the gate the repo tripped on |
| **G3 — paid** | metered or subscription | Regrid · GSCCCA plat images · Matterport-class capture |
| **G4 — government-gated** | eligibility, not money: employment or a contract | ⛔ **Georgia 15 cm statewide ortho** · Copernicus **EEA-10** |

⚠️ **A sixth, quieter gate: CORS.** County ArcGIS REST endpoints are open to a *server* and frequently unreachable from a *browser* because they send no cross-origin headers. For a static-file product served from Pages, that is the difference between "the app can call it" and "something else must fetch and cache it." **Assume server-side for every county source.**

### 2b · ⭐⭐ STORABLE / REDISTRIBUTABLE — the product boundary

> ⛔ **Against a property with no cell signal, a source we cannot store is a materially worse PRODUCT — not a legal caveat.**

`CLAUDE.md` § THE SITE'S PHYSICAL PREMISE is permanent: no cell reception, coverage falls off with distance from the house, and **the places worth walking to are exactly the places with no network**. A live-tile basemap is therefore not *"the same map with a licence note"* — it is **a map that is blank in the half of the property the map is for**.

**Three tiers, and the ranking in §13 is on this axis:**

| tier | means | consequence |
|---|---|---|
| ✅ **KEEP** | public domain or permissive; store, re-project, serve offline, derive from | can be the shipped basemap; can be pre-cached to a phone before a walk |
| ⚠️ **KEEP-WITH-ATTRIBUTION** | ODbL / CC-BY class; storable, share-alike or attribution obligations attach | fine for vector overlays; the obligation must be *designed in*, not remembered |
| ⛔ **LOOK-ONLY** | display-only terms, or a cache expiry | **an operator may look; the app may not show it, and a phone in the woods may never hold it** |

---

## 3 · SCALE 1 — INDOOR / UNIT  ⭐ least researched, first to ship

**The condo is the trial estate, so this scale is not hypothetical.** `.user-research/2026-09-06-what-a-map-is-for.md` §3.1 already ruled the outdoor aerial map **void** here — *"an aerial photograph of a condo shows a roof belonging to sixty people."* The question this file adds: **what data exists at all.**

### 3a · What the free public record actually holds — MEASURED this session

| source | gate | what it gives at unit scale | resolution | currency | coverage | storable | horizon |
|---|---|---|---|---|---|---|---|
| ⭐ **County parcel/assessor REST** (Fulton: `gismaps.fultoncountyga.gov`, `PropertyMapViewer/MapServer/11`) | **G0** — no key, no charge | **the unit as a RECORD**: `ParcelID`, `AddrUnit`, `AddrUntTyp`, `LivUnits`, `LUCode`, `ClassCode`, assessed/appraised values, `Subdiv` | ⛔ **geometry is the BUILDING, not the unit** | annual tax roll | ⚠️ per county — see §6 | ⚠️ terms vary by county; usually silent | **NEAR** |
| ⭐ **Recorded condominium plat + plans** — GA `O.C.G.A. 44-3-74`, `15-6-67` | **G3** — GSCCCA subscription **$14.95/mo** (Premium $29.95, both from 2025-07-01) **+ $0.50/page** | ⭐ **THE ONLY PUBLIC SOURCE OF UNIT GEOMETRY.** Statute requires a *"condominium floor plan, plot plan, or site plan"* recorded **before the first unit conveys**, into a dedicated **"Condominium Plat Book,"** e-filed | a **scanned drawing**, dimensioned, not vector | frozen at declaration + amendments | ⚠️ **Georgia-specific statute.** Most states have an analogue (UCA/UCIOA-derived); ⛔ uniformity **unverified** | ⚠️ it is a purchased record image; treat as ⛔ LOOK-ONLY absent a terms read | **LONG** |
| **National Address Database (USDOT)** | **G0** | address points, **including *some* sub-units**; 80 M records, compiled 2026-06-30 | point | annual-ish | ⚠️ **voluntary state participation — full / partial / none** | ✅ public domain | NEAR (as a *check*, not a map) |
| **MS / Overture building footprint** | G0 | the **building** outline the units sit in | vector | Overture monthly | ✅ national/global | ⚠️ ODbL | NEAR |
| ⛔ **Aerial imagery of any kind** | — | a shared roof | — | — | — | — | ⛔ **NOT FOR US at this scale** |

> ### ⭐⭐ THE MEASUREMENT, and it is the finding of this section
>
> Fulton County's Tax Parcel layer, queried live at the condo's geocoded point:
>
> | query radius | parcel **records** | **distinct polygon areas** | records carrying a **unit number** |
> |---|---|---|---|
> | ~67 m | 3 | 3 | 0 |
> | ~166 m | **151** | **22** | **112** |
> | ~333 m | **935** | **136** | **676** |
>
> **~7 legal records per physical shape.** One neighbouring record declares **`LivUnits = 322`** on a single **3.6-acre / 129,927 ft²** polygon.
>
> ⭐ **So the county gives every unit an identity and no shape.** The unit is a *record stacked on a building*. Whatever the product does indoors, **it is not consuming a public unit geometry, because there isn't one.**
>
> ⚠️ **AND THE POINT LOOKUP FAILED SILENTLY.** A point-in-polygon query at the geocoded address returned **HTTP 200, valid JSON, `features: []`** — while a 67 m envelope around the same point returned 3. The Census geocoder interpolates along an address range and can land in the right-of-way. ⛔ **`address → geocode → parcel-by-point` returns success carrying nothing**, which is this repo's named failure mode and is directly upstream of `tools/read-geocodes.py`. **A parcel lookup must use a tolerance/envelope and must distinguish `no match` from `zero features`.**

### 3b · Capture — because the geometry has to be *made*, not found

| path | gate | accuracy | cost | what it produces | honest read |
|---|---|---|---|---|---|
| ⭐ **Apple RoomPlan** (iPhone/iPad Pro LiDAR) | **G0** — free Apple framework, requires a Pro device | **~1–3 cm** interior, vendor-reported | free | structured room: walls, doors, windows, openings, coarse furniture | ⭐ **the only free unit-geometry source that exists.** ⚠️ Requires a *Pro* device — **Mom's device is not established as one.** |
| **Polycam / magicplan / RoomScan Pro** | G3 | *"a few centimetres"* / *"1–2 inches"*, vendor-reported | ~**$10–36 / user / month** | floor plan + export | fine for an **operator**; ⛔ a subscription per household does not survive §14 |
| **CubiCasa / Matterport class** | G3 | — | vendor comparison quotes $300–$800 tiers; ⚠️ **not normalized, treat as order of magnitude only** | polished plans, hosted | ⛔ out of scope at this stage |

⚠️ **Every accuracy figure in this table is VENDOR-REPORTED.** None was measured, none is independent, and iPhone LiDAR degrades on glass, dark, glossy and large open spans.

### 3c · ⭐ The brief asked me to test the room-by-room finding. It holds, and it now has a second leg.

`.user-research/2026-09-06-what-a-map-is-for.md` verified that **HomeZada and Encircle organise room by room, not by floor plan**. Nothing found this session contradicts it, and **the county data now corroborates it from the record side**: the public record itself is organised as *identity + container*, with no unit geometry to organise by. **Two independent industries and one government record all reached "named container, no shape."**

⛔ **Consequence, stated plainly:** at the condo, **there is no map to fetch — only a plan to capture.** Any indoor geometry is an act of *capture by a person in the room*, and by the site premise it must work with **no network at the moment of capture**. The cheapest honest v1 indoors is **a list of named containers**, and the schema change that unlocks it is the one already named — **geometry optional** — not a floor-plan pipeline.

---

## 4 · SCALE 2 — PROPERTY / PARCEL

Prior scan §§10a–10e were **right** on optical, archive, elevation and the derived national layers; not redone. Three extensions:

| what the prior scan said | the extension |
|---|---|
| *"NAIP: free, public domain, 0.6 m"* | ⭐ **correct — and it is the single point of failure.** §8. |
| *"the parcel boundary is the highest-value missing artifact… it is a BUY"* | ⭐ **still true, and free-only now means Fernwood's parcel stays missing.** §6. |
| *"3DEP point cloud is THE under-used source"* | ⭐ **still true, and now quantified: ~2× linear gain, plus CHM/intensity/returns.** §10. |
| *"Google Solar dataLayers ~$0.075/call"* | number right; **1,000 free/month** found; **billing card + no credential** is the real gate. §14. |

⭐ **One thing the prior scan under-weighted: the 30-day cache clause is not a licensing footnote, it is a §2b tier-⛔ verdict.** A basemap that must be re-fetched every 30 days **cannot be pre-cached to a phone for a walk into a no-signal property.** Under the site premise, Solar is an **operator instrument**, never a shipped layer — and that conclusion no longer depends on Paul ruling the licence question, because the *product* answer arrives first.

---

## 5 · SCALE 3 — NEIGHBOURHOOD

⭐ **The live ruling: events/neighbourhood content STARTS AS LINKS** — membership by rule, nothing filtering, no AI-boundary ruling owed; the trigger to re-open is *the first time anything SELECTS or FILTERS*.

### 5a · What actually exists as standard data

| source | gate | what it gives | storable | horizon |
|---|---|---|---|---|
| ⭐ **`api.weather.gov`** — **VERIFIED at the anchor this session** | **G0** (User-Agent required, no key) | forecast zone **GAZ013**, county zone **GAC227**, fire zone, radar **KFFC**, grid **FFC/49/122**; **active alerts by zone** | ✅ public domain | ⭐ **NEAR — the one genuinely good, genuinely free neighbourhood-scale feed** |
| **Census TIGER / places / block groups** | G0 | boundaries, road centerlines, tract/block-group | ✅ public domain | NEAR (as *frame*, not content) |
| **USGS GNIS** | G0 | official place names — *Burnt Mountain*, *Lake Sequoyah*, *Tate Mountain Estates* | ✅ public domain | NEAR |
| **OpenStreetMap / Overture places** | G0 | POIs, trails, water, some businesses | ⚠️ ODbL | NEAR; ⚠️ rural coverage thin |
| **County / city open-data portals** | G0–G1 | zoning, districts, school zones (Fulton publishes all three) | ⚠️ varies | LONG |
| ⛔ **Community events** | G1–G3 | Eventbrite / Ticketmaster / Meetup / Bandsintown / SeatGeek all offer keys; **Localist** aggregates | ⛔ almost all display/terms-bound | ⛔ **NOT NOW** |
| ⛔ **Nextdoor, HOA lists, church calendars, the actual neighbourhood** | — | — | — | ⛔ **no standard source exists** |

### 5b · ⭐ So is starting with LINKS right? **Yes, and the evidence is stronger than "it's cheap."**

Three independent reasons:

1. **There is no standard to aggregate.** Every practitioner account of event aggregation describes **per-platform keys plus deduplication plus NLP enrichment** to get a usable feed. That is a pipeline, and it buys **national event coverage** — which is exactly the wrong shape for *a mountain estate in Pickens County*, where the events that matter (the HOA, the church, the lake) are **on none of those platforms**.
2. **The one high-quality free feed is already a link's worth of value.** `api.weather.gov` alerts are genuine, local, and free — and they are *already* what a link to the NWS zone page shows.
3. ⭐ **The measured reader evidence forbids the alternative.** `.user-research/2026-09-06-what-a-map-is-for.md`: Mom's **depth 2 and depth 3 are both zero across lap 8** — she reads card faces and does not open individuals. **A filtered, curated, aggregated neighbourhood feed would be content behind a tap, i.e. content she has not seen.** A link costs nothing and fails visibly; an aggregator costs a pipeline and fails *silently, into a surface nobody opens*.

⚠️ **How much must be custom to be worth anything: essentially all of it.** Which is the argument *for* links, not against neighbourhood content — it says the value is in **knowing which five links matter at this place**, and that is knowledge from the household, not a dataset. ⛔ **And the moment anything SELECTS or FILTERS among links, the ruling says re-open it** — including an AI that picks which link to show.

---

## 6 · SCALE 4 — COUNTY  ⭐ the load-bearing scale, and the honest weak point

### 6a · The generalisation numbers

| measure | value | source |
|---|---|---|
| counties in aggregated national parcel databases | **~3,227–3,230**, **99.7% of US population** | vendor coverage statements, mid-2025 |
| states with a **full, freely available, digital statewide parcel layer** | ⭐ **about ten** | landrecords.us coverage documentation |
| New York counties that have **permitted public sharing** | **38 of 62** | same |
| ⛔ **free parcel API found for Pickens County, GA** | **none** | ArcGIS Online + Hub search returned **Pickens AL** and **Pickens SC** only; a candidate `Parcels` FeatureServer proved to be **EPSG:2283 — Virginia** |
| free parcel service for **Fulton County, GA** | ✅ **373,305 parcels**, G0, no key | queried live |

### 6b · ⭐⭐ The honest statement the brief asked for

> **"Use what's free" solves the parcel at Mom's condo and does not solve it at Fernwood.**
>
> Fulton County is a large metro county with a modern open-data programme. Pickens County is a rural county of ~22,000 parcels whose public face is a **Schneider qPublic web application** — a viewer, not an API. The very property this product is named for sits in the harder half.
>
> ⚠️ **And the shape of the gap is not "some counties are behind."** It is that **county parcel publication is a policy choice made ~3,140 times**, with no federal mandate, no common schema, no common licence and no common endpoint. The aggregators' 99.7% figure is real — **and it is a description of their acquisition effort, not of open access.** ⭐ **It is the clearest measurable statement of the vision/short-term-reality split Paul named.**

### 6c · Generalising to 3,000+ counties — the four costs, in order

| cost | what it is |
|---|---|
| **1 · Discovery** | there is no registry of county endpoints; each is found by hand |
| **2 · Schema** | every county names its fields differently (Fulton `AddrUnit`/`LUCode`/`TotAppr`; the Virginia service `GPIN`/`TaxMapNumb`/`Acreage`) — **the normalisation layer is the actual product** |
| **3 · Licence** | mostly *silent*, which is not the same as permissive; §2b tier is **unknown by default** |
| **4 · Liveness** | a county server changes URL, retires a layer, or drops CORS with no notice; **it will fail as an HTTP 200 with an empty feature array** |

⭐ **That list is precisely what a paid aggregator sells** — which is why the prior scan's *"Regrid is the only path that generalises"* survives the free-only ruling **as a statement about household N**, while being correctly out of scope today.

---

## 7 · SCALE 5 — STATE  ⚠️ the Georgia pattern is NOT general, and that is good news

**The 09-06 finding stands:** Georgia's 15 cm statewide leaf-off orthoimagery is **G4 government-gated** — the best imagery over this property, unreachable. The brief asks whether that pattern is general. **It is not.**

| state | product | gate |
|---|---|---|
| ⛔ **Georgia** | **15 cm statewide, 7.5 cm urban, includes leaf-off** | **G4** — government employees / contractors under contract |
| ✅ **North Carolina** | **6-inch (15 cm)** statewide ortho, 4-year cycle, ~¼ of the state per year | ⭐ **"made freely available to the public"** — *the identical product, openly published, one state north* |
| ✅ **New York** | statewide digital ortho since 2000, high-resolution | free view + download |
| ✅ **Utah (SGID)** | HRO / DOQ / NAIP / UAO, 1 ft to 1 m | open |
| ✅ **Vermont** | ⭐ **statewide QL1 lidar (2023)** derived elevation products | open |
| ✅ **Wisconsin, North Carolina** (parcels) | statewide parcel initiatives | open |

> ⭐⭐ **THE FINDING: the highest-resolution imagery over any given US address is a STATE POLICY VARIABLE, not a technology limit.** North Carolina publishes at 15 cm what Georgia restricts at 15 cm. **So the product's imagery quality at household N depends on which state the household is in, and that is not something engineering can fix.**
>
> **What legitimate access would require in Georgia:** eligibility, not money — a government employment relationship or a contract with a government body. ⛔ **Not a purchase, not a licence fee, not a negotiation.** It is correctly recorded as *exists and is unreachable*, and it will stay that way.

⚠️ **Design consequence:** the shipped basemap must be **NAIP, everywhere, always** — the one layer whose terms and access do not vary by state. A per-state "best available" imagery strategy would produce a product whose core surface is **inconsistent between households in a way the household can see**, which is worse than uniformly-good-enough.

---

## 8 · SCALE 6 — NATIONAL  ⭐ solid, free, and resting on one program

Prior scan §10e is **correct and not redone**: 3DEP · NAIP · TIGER · MS/Overture buildings · SSURGO · NWI · FEMA NFHL · NHD/WBD · historical topo · hardiness zone · climate normals — *"a lot of a place, for free, before anyone draws anything."* Four extensions:

### 8a · ⭐⭐ The NAIP tail risk, stated once and properly

- **Today:** NAIP is public domain, free, redistributable. Unchanged.
- **The history:** in 2017–18 USDA FSA presented a plan to make NAIP a **licensed COTS product** because a **$3.1 M** shortfall had made cost-sharing unworkable, with a decision deadline of **May 1 2018** affecting the 2019 collection. It stated it had *"not identified any regulatory or statutory requirements that mandate the release of NAIP data to the general public."* Mapbox and others publicly opposed it. **It did not happen.**
- ⚠️ **The honest weight: this is an eight-year-old proposal that was never enacted, and I am not claiming it is imminent.** What it establishes is **structural**: the free-ness of NAIP is a **budget outcome, not a legal guarantee**, and the funding pressure that produced the proposal has never been removed.
- ⭐ **The design consequence is cheap and worth taking now:** because NAIP is public domain and storable, **every frame we fetch is ours permanently.** *A stored frame cannot be un-licensed.* ⛔ A design that **streams** NAIP from a third-party STAC on demand inherits the risk; one that **fetches once and keeps the bytes** does not. This repo already does the right thing by accident — §13 makes it deliberate.

### 8b · SSURGO — ⭐ VERIFIED at the anchor, settling a July LEAD

One anonymous POST to Soil Data Access returned:

```
mukey 531363 · "Tallapoosa cobbly sandy loam, 25 to 60 percent slopes" · survey area GA622
```

`property.json` § soils carries **Ashe, Edneyville, Porters, Tallapoosa** as candidates, `seriesNote: "INFERRED, not tested."` ⭐ **The free authoritative source selects Tallapoosa** — and independently corroborates the 2026-07-25 removal of Cecil and Pacolet.

⚠️⚠️ **THIS DOES NOT CLOSE W9 AND MUST NOT BE WRITTEN AS IF IT DID.** SSURGO is a **map unit**, typically acres, digitised at roughly 1:12,000–1:24,000. On a steep spur it carries real positional uncertainty, and *"25 to 60 percent slopes"* is a range, not a reading. Under this repo's own doctrine it is a **better-sourced inference, not a measurement** — the W9 soil test is still the only thing that returns a texture result from the actual ground. ⛔ **Do not promote `confidence` on a map-unit read alone.**

### 8c · The NWS point service — free, keyless, immediately useful (§5a).

### 8d · What no national layer contains, restated
⛔ Utilities are still **not a dataset** — 811 is a *request service*. Building permits remain county-level and rarely an API. Neither moved this session.

---

## 9 · SCALE 7 — GLOBAL / NON-US  ⛔ NAIP is why this is free, and NAIP is US-only

### 9a · The two-tier world

| region | imagery | elevation | parcels | verdict |
|---|---|---|---|---|
| ⭐ **Western Europe / ANZ — BETTER than the US** | **Netherlands: 7.5 cm LEAF-OFF nationwide every spring + 25 cm leaf-on every summer, free.** Switzerland **SWISSIMAGE 10 cm**, annual, open. France **BD ORTHO** open | **France LiDAR HD** (national programme, open) · **Netherlands AHN** (multi-epoch, free) · Vermont-class QL1 across several countries | national cadastres, variously open | ⭐ **materially BETTER.** The exact leaf-off 7.5 cm product Georgia gates is a **free annual national deliverable** in the Netherlands |
| ⛔ **Most of the rest of the world** | **Sentinel-2 at 10 m** is the free floor. ⛔ Nothing at lot scale | **Copernicus DEM GLO-30 — 30 m, free, global**, and it is a **DSM** (includes vegetation and buildings). ⚠️ The **10 m EEA-10** instance is **G4 access-restricted to a specific user subset** | ⛔ typically none | ⛔ **materially WORSE, and not marginally** |

### 9b · The verdict the brief asked for — say which

> ⛔ **Outside the handful of countries with open national mapping, this is a MATERIALLY WORSE PRODUCT, not an acceptable degradation.**
>
> The arithmetic is not close. At Fernwood a `hosta-garden` bed is a few metres across. **NAIP at 0.6 m gives it dozens of pixels. Sentinel-2 at 10 m gives it a quarter of one.** Elevation degrades the same way: **1 m 3DEP → 30 m Copernicus** is a 900× loss in cell area, and it is a *radar DSM* that cannot separate ground from canopy at all — so **the CHM, the slope break, the bank, the bluff and the woods/open line all disappear together.** Every terrain-derived feature in the prior scan's §11a is a US feature.
>
> ⭐ **But the honest inverse matters as much: in the Netherlands, Switzerland, France and Vermont-class jurisdictions the product would be BETTER than at Fernwood** — leaf-off at 7.5 cm annually, against Fernwood's one leaf-off frame in fifteen years at 0.6 m.
>
> ⭐⭐ **So the correct engine statement is not "US-only." It is: the map layer's quality is a property of the JURISDICTION, and the engine must degrade LEGIBLY** — the same conclusion §7 reached one scale down, which is the corroboration. **A place with no usable imagery must render as *a named place with no map*, not as a broken map** — which is, once more, **`a named place, geometry optional`**. ⛔ **This is a reason to build the geometry-optional primitive, not a reason to fear non-US expansion.**

---

## 10 · ⭐ Q1 — does the raw point cloud recover what the gridded DEM smears?

### 10a · The measurement

I fetched the USGS public **EPT** metadata for the 2018 Georgia blocks and located the anchor (**EPSG:3857 = −9,391,736 · 4,102,841**) inside two of them:

| block | points | bbox area | **density (lower bound)** | **nominal spacing** |
|---|---|---|---|---|
| `GA_Statewide_B2_2018` | 42.68 bn | 10,831 km² | **3.94 pts/m²** | **≤ 0.50 m** |
| `GA_Statewide_B3_2018` | 43.10 bn | 11,615 km² | **3.71 pts/m²** | **≤ 0.52 m** |

⭐ **Why "lower bound" is rigorous, not a hedge:** points ÷ *bounding-box* area ≤ points ÷ *flown* area. The bounding box is never smaller than the coverage, so the true density is **at least** this. ⚠️ Both bounding boxes contain the anchor and I did not descend the EPT hierarchy to determine which block actually holds the returns; the two figures agree closely enough that it does not change the answer. ⛔ **And note `LAND-SOURCES.md`'s product id is `GA_Statewide_2018_B18_DRRA`, which does not appear as a public-bucket prefix** — the delivery blocks and the TNM product tiles are named differently. **Confirm the block before any fetch.**

### 10b · The answer

| feature | 1 m gridded DEM | **raw cloud at ~0.5 m spacing** | verdict |
|---|---|---|---|
| **Bank, bluff, slope break** | already good | marginally better | ⭐ the DEM was **already sufficient** |
| **Terrace (multi-metre tread, ≥0.5 m riser)** | smeared | ⭐ **recovered as a genuine step; a TIN with breaklines beats an interpolated grid** | ⭐ **YES — the real win** |
| **A single 0.5 m retaining wall** | invisible | ⚠️ **~1 point across its top; a vertical face gets few near-nadir returns** | ⚠️ **MARGINAL — do not promise it** |
| **Mulch / bed edge** | invisible | ⛔ invisible | ⛔ **NO. Not at any point density this flight has** |
| ⭐ **Woods vs open (CHM)** | ⛔ **impossible — the DEM is bare earth; the trees are gone** | ⭐⭐ **first return − ground = canopy height. Shadow-free, season-free** | ⭐⭐ **THE ANSWER, and it is a capability, not an improvement** |
| ⭐ **Water, pavement** | ⛔ | ⭐ **return intensity + low/absent returns over water** | ⭐ **new capability** |
| **Specimen trees** | ⛔ | CHM local maxima | ⭐ new capability (⚠️ needs **points** in the schema) |

> ⭐⭐ **THE HONEST HEADLINE: the point cloud is worth ~2× on resolution and ∞ on KIND.**
>
> Framing it as *"does it recover the walls the DEM smears"* undersells it and will disappoint. **1 m → 0.5 m is one doubling.** The reason to do it is that the DEM is a **bare-earth product with the trees deleted**, and the point cloud is **the trees, the ground, the water and the pavement, separately.** ⭐ `LAND-SOURCES.md` has said since 2026-09-01 that the CHM is *"the strongest available source for the field zones"* and *"not yet built."* **This measurement is the argument for building it — and the argument is CHM, not walls.**

### 10c · What it costs in tooling and skill — measured, and it is the real barrier

⛔ **Zero of the stack is installed.** `pdal`, `gdal`, `laszip`, `lasinfo` all absent; `laspy`, `rasterio`, `pdal` (python) all fail to import.

| cost | honest read |
|---|---|
| **Install** | PDAL + GDAL via conda/homebrew — **not a `pip install`.** ⚠️ Native dependency chain; a real afternoon, with a real chance of a bad hour |
| **Download** | ⭐ **small, and this is the good news.** EPT/COPC support **spatial subsetting over HTTP** — a 500 m × 500 m crop is tens of MB, not the 43 **billion** points of the block |
| **Skill** | a PDAL pipeline is declarative JSON: `readers.ept` (bounds) → `filters.range` on classification → `writers.gdal` twice (max = DSM, ground-only = DTM) → subtract. ⭐ **This is a well-trodden recipe, not research** |
| **Verification** | ⭐ **cheap and available: two raster products already sit at identical bounds.** A new CHM must be checked against `lidar-hillshade-2018.png` and the leaf-off NAIP frame **at the same georeference** |

⚠️ **The one caveat that is not tooling.** `lidar-hillshade-2018.bounds.json` already records it: *"the western garden and that patio area we have kind of reshaped with heavy equipment."* **A CHM from this flight is a 2018 canopy.** Trees have grown, and some have gone. **Where it disagrees with the ground the first hypothesis is change, not error** — the same rule already written for the terrain.

---

## 11 · ⭐⭐ Q2 — multi-temporal shadow rejection. Attacking it, as asked.

**The claim under test:** *an edge present in all seven NAIP frames is a real feature; an edge present only in the January leaf-off frame is a shadow.*

### 11a · Does it have a name and a literature? **Yes — a family, not one method.**

| named technique | what it is | how close to the claim |
|---|---|---|
| ⭐ **Median / medoid compositing** | take the per-pixel median (or medoid, a multidimensional median) across a temporal stack; shadows and clouds are radiometric outliers and the median rejects them | ⭐ **the closest established analogue.** Standard practice for Landsat/Sentinel; medoid is preferred for radiometric consistency, BAP for temporal consistency |
| **Multi-temporal shadow detection** | detect shadows *in order to* protect change detection; a recognised open problem | same family |
| **Pseudo-invariant features (PIF)** + histogram matching / mean-variance normalisation | normalise brightness across dates so transient shadows stop registering as change | the *radiometric* half |
| **Physical/geometric shadow modelling** | predict shadows from solar elevation and object height | ⭐ **the method the claim SHOULD have used** — §11c |

⭐ **So the instinct is a real technique.** The defect is not the family; it is **n and geometry.**

### 11b · ⛔ Where it breaks — four confounds, worst first

> ### ⛔⛔ 1 · THE KILLER: NAIP SHADOWS DO NOT MOVE, THEY ONLY SHORTEN
>
> Median compositing works because a cloud is somewhere *else* next pass. **A tree's shadow is in the same place every pass.** All seven frames are near-noon acquisitions at 34.55° N, so **every shadow falls broadly north of its object in every frame**; the repo's own metadata records that only the *length* changes — **0.50× to 1.52× of height**.
>
> **Therefore the intersection of seven shadows is the SHORTEST shadow.** Every pixel within **0.50 × height** of the object's north side is shadowed in **all seven frames** and the test promotes it to *"real feature."* ⛔ **For a 20 m tree that is a 10 m-wide persistent dark band that the method certifies as ground truth.** The test cannot reject the shadow **core** — only the **tail**, which was the easy part.
>
> ⚠️ **And a metadata caveat that bites here.** `noonSunAltitudeDeg` in every `*.bounds.json` is computed **at solar noon**, not at the frame's actual acquisition time, which is not recorded. NAIP is flown within a sun-angle window, not at noon. **So the seven altitudes are idealised, the seven azimuths are unknown, and the azimuth spread — the only thing that could move a shadow — is exactly the quantity nobody has.**

**2 · The intersection is capped by the WORST frame.** Frames are **1.0 m** (2010, 2013, 2015, 2017) and **0.6 m** (2019, 2022, 2023). Requiring presence in *all seven* means nothing finer than **1.0 m** can survive — ⛔ **the operator throws away the entire resolution gain of the three modern frames.** The brief flagged this; it is worse than a confound, it is a **structural cap.**

**3 · Co-registration.** NAIP's stated horizontal accuracy is **±6 m**; published assessments put baseline NAIP misregistration in the **3–10 m** range, and change-detection literature holds that **~0.2 pixel** co-registration is needed before per-pixel comparison is trustworthy. ⛔ **A 3 m relative shift between epochs makes "the same edge" a different pixel**, and every derived conclusion is noise. ⭐ **The frames on disk share one *requested bbox*; that is a common frame, not proven sub-pixel alignment.**

**4 · Relief displacement, and it is the subtle one.** NAIP is orthorectified against a **bare-earth** DEM, so anything *above* the ground — a tree crown, a roof — leans outward from nadir by an amount that varies with its position in the flight line. **A tree's crown edge is not at the same ground coordinate in two flights even with perfect georeferencing.** Trees are the tallest things at Fernwood and the canopy is heavy.

**5 · Real change is punished.** Leaf-on October vs leaf-off January: the canopy edge genuinely moves. Over fifteen years, so do the trees. ⛔ **"Present in all seven" systematically prefers what has not changed — in a fifteen-year stack over a property that has been regraded.**

### 11c · ⭐ The repair — three moves, in order of how much they change

1. ⭐ **Stop counting presence; predict the shadow.** A shadow's direction and length are **computable** from date, time and sun position — the repo already computes half of it. **Test whether a dark region sits where the geometry says a shadow must be, and shrinks/rotates between frames as predicted.** That is *physical/geometric shadow modelling*, it is a named method, and it is far stronger than a vote — **it can reject the shadow core, which presence-counting provably cannot.** ⚠️ It needs the **acquisition time**, not solar noon.
2. **If a vote is kept: use k-of-n over the four 0.6 m frames, not 7-of-7 over mixed GSD** — and register them to each other first, with measured residuals.
3. ⭐⭐ **Or don't. A shadow has no height.**

> ### ⭐⭐ THE RECOMMENDATION — and it is to spend the effort elsewhere
>
> **The multi-temporal stack is a clever workaround for a problem that already has a direct instrument sitting on disk.** Lidar is an **active sensor: no sun, therefore no shadows** — `lidar-hillshade-2018.bounds.json` says so in its own `why` field. **A DSM/CHM from §10 answers "is this dark thing a shadow or a real object" definitively, with one dataset, no registration problem, no GSD mismatch and no sun-angle assumption.**
>
> ⭐ **Which frees the seven-frame stack for the thing ONLY it can do:** *change over time* — including **§3c of the prior scan, mowing regime as a time-series signal**, which is still the only proposed way to separate `the-turf` from `the-meadow`, **74% of the mapped area**. ⚠️ Confounds 3 and 4 apply there too, but a **texture/NDVI statistic over a neighbourhood** is far more robust to a 3 m shift than an **edge test**, which is the most registration-sensitive operator there is.
>
> ⛔ **So: don't soften the shadow idea, retire it — and keep the stack.** The prior scan's own rule for §3c applies to §11 now: *if the test fails, delete the section rather than softening it.*

⚠️ **What would change my mind, cheaply:** measure the **relative** registration of the seven frames against each other on a hard invariant (a road intersection, a building corner). If they align to well under a metre, confounds 3 and 4 shrink and the time-series work gets easier. **That measurement is worth doing regardless of the shadow question**, because §3c depends on it too.

---

## 12 · Q3 — is there a free or open equivalent of Google Solar's 0.1 m shadow-free DSM?

⛔ **No. Not in the US, not in Georgia, not at 0.1 m.**

| candidate | best free resolution | why it is not equivalent |
|---|---|---|
| **3DEP QL1 lidar** (>8 pts/m²) | **0.5 m DEM cell** — *the free national ceiling* | ⚠️ **QL1 is not everywhere.** Vermont has it statewide (2023); **Georgia's 2018 statewide is not QL1** |
| ⭐ **DSM from the 3DEP point cloud at Fernwood** | **~0.5 m** (measured, §10a) | **5× coarser than Solar.** ✅ **but genuinely shadow-free — active sensor** |
| **3DEP 1 m DEM** | 1 m, and it is **bare earth** | ⛔ not a surface model at all |
| **Copernicus GLO-30** | 30 m, global, a DSM | ⛔ two orders of magnitude off |
| ⛔ **Photogrammetric DSM from NAIP** | in principle sub-metre | ⛔ NAIP delivers **orthos, not stereo pairs**; and a photogrammetric surface is **shadow-limited by construction** — the thing being solved for |
| **Vexcel / Nearmap / EagleView** | 5–7 cm | ⛔ **G3 commercial**, and ⛔ LOOK-ONLY |

⭐ **And Google Solar's "0.1 m shadow-free DSM" deserves a caveat of its own, which the 09-06 scan did not carry:** it is a **photogrammetric product rendered on a 0.1 m grid.** *Rendered at* 0.1 m is not *accurate to* 0.1 m, and occluded areas — under canopy, behind walls, in permanent shade — are **interpolated**. ⚠️ **Under heavy canopy, the place its 0.1 m matters most is the place it is most likely inferred.** ⛔ **Coverage at this rural anchor remains UNPROBED** and the prior scan's warning about documented rural 404s stands.

> **The straight answer:** the best free surface model over Fernwood is **~0.5 m from the 3DEP point cloud** — which is **within reach today, free, storable forever, and not yet built.**

---

## 13 · ⭐⭐ Ranking on the product boundary — storable or live-only

**Ranked on §2b, as the brief asked, because under the site premise this axis outranks resolution.**

| # | source | tier | resolution | ⭐ works with no signal? |
|---|---|---|---|---|
| **1** | ⭐ **NAIP** | ✅ KEEP — public domain | 0.6 m | ✅ **yes — bytes on disk, ours permanently** |
| **2** | ⭐ **3DEP DEM + point cloud** (and every derivative: hillshade, slope, CHM, geomorphons) | ✅ KEEP — public domain | 1 m / ~0.5 m | ✅ **yes** |
| **3** | **SSURGO · NWI · FEMA NFHL · NHD/WBD · TIGER · historical topo · NWS zones · NAD** | ✅ KEEP — public domain | vector | ✅ yes |
| **4** | **MS / Overture buildings · OSM** | ⚠️ ODbL — storable, **share-alike attaches** | vector | ✅ yes, with the attribution designed in |
| **5** | **County parcel REST** (where it exists) | ⚠️ **usually silent on terms**; assume unknown | vector | ⚠️ yes *if* cached server-side; ⛔ CORS usually blocks the browser |
| **6** | **Recorded condo plat (GSCCCA)** | ⚠️ purchased record image | scanned drawing | ⚠️ only as a purchased artifact |
| **7** | ⛔ **Google Solar dataLayers** | ⛔ **LOOK-ONLY — 30-day cache limit** | 0.1 m | ⛔ **NO — expires** |
| **8** | ⛔ **Esri World Imagery** | ⛔ LOOK-ONLY | 0.31 m (⚠️ 8.47 m placement) | ⛔ no |
| **9** | ⛔ **Google Earth Web** | ⛔ LOOK-ONLY | ~0.45 m/px | ⛔ no |
| **10** | ⛔ **Georgia 15 cm state ortho** | ⛔ **G4 — unreachable** | 15 cm | — |

> ⭐⭐ **THE RANKING INVERTS THE RESOLUTION RANKING, AND THAT IS THE POINT.** The two sharpest optical sources over this property (Solar at 0.1 m, Esri at 0.31 m) sit at **7 and 8**, below a 1 m elevation raster, because **a walk to the pond has no network and a licence that expires is a blank screen in the woods.** ⛔ **Every LOOK-ONLY source is an OPERATOR instrument. None may be the shipped basemap.** The repo already behaves this way — Esri lands in gitignored `.local/` and is barred from `zones.json._meta.baseImage`. **This is the general rule behind that specific one.**

---

## 14 · ⭐ Cost at household N — pricing the model, not the call

Assume one full derivation per household, once.

| source | n=1 | n=100 | **n=1,000** | n=10,000 |
|---|---|---|---|---|
| **NAIP · 3DEP · SSURGO · NWI · FEMA · TIGER · NHD · NWS · NAD · buildings** | **$0** | **$0** | **$0** | **$0** (⚠️ + egress/compute, which is not nothing at 10k) |
| ⭐ **Google Solar `dataLayers`** | **$0** *(free tier)* | **$0** | **$0** *(1,000/mo free — exactly at the line)* | **$675/mo** *(9,000 × $0.075)* |
| **Google Solar `buildingInsights`** | $0 | $0 | $0 | $0 *(10,000/mo free)* |
| **Regrid** | ⛔ no published rate | ⛔ | ⛔ **monthly base + per-record overage, account-gated** | ⛔ |
| **GSCCCA plat images** (GA only) | $14.95/mo + $0.50/page | same sub, more pages | same sub | ⚠️ ⛔ **and it is one state of fifty** |
| **Per-household floor-plan subscription** | $10–36/mo | ⛔ **$1,000–3,600/mo** | ⛔ **$10k–36k/mo** | ⛔ |

> ### ⭐ THE COST FINDING — and it reverses the intuition
>
> **Google Solar is FREE up to 1,000 households per month.** The 09-06 scan treated it as a paid source and a licence problem; the *money* is not the constraint until ~1,000/mo, and even then $675/mo at 10,000 households is not a business-model problem.
>
> ⛔ **What actually disqualifies it is §13, not §14** — the **30-day cache limit** means it can never be stored, so it cannot serve a property with no signal, **at any n, at any price, including free.** ⭐ **A licensing term, not a price, is what removes it.** That is precisely the kind of thing a cost column hides and a storability column catches, which is the argument for having made storability a first-class axis.
>
> ⚠️ **The subscription-per-household row is the one that actually breaks.** Anything priced **per user per month** multiplies by N and dies; anything priced **per call** with a free tier does not. **Prefer per-call or free-and-storable; refuse per-seat.**

---

## 15 · ⭐ How each source FAILS — because a success carrying nothing is this repo's named failure mode

**Measured this session unless marked.** ⛔ **LOUD** = you find out. ⚠️ **SILENT** = it looks fine.

| source | failure mode | loud or silent |
|---|---|---|
| ⛔ **County parcel point query** | **HTTP 200, valid JSON, `features: []`** at the correct address, because the geocode landed in the right-of-way — while a 67 m envelope returned 3. **MEASURED at the condo today** | ⚠️⚠️ **SILENT — and it reads exactly like "this address has no parcel"** |
| **Census geocoder** | interpolates along an address range; returns a confident point that is not the building | ⚠️ SILENT |
| ⛔ **Esri World Imagery z20/z21** | HTTP 200 carrying a valid PNG of a grey square reading *"Map data not yet available"* | ⚠️ SILENT — ✅ *already trapped* by `fetch-trace-hires.py` pixel inspection |
| ⛔ **Google Earth Web 1985 tick** | renders 100% loaded and **completely blank**; attribution date **lags** the header | ⚠️ SILENT — ✅ already documented |
| **ArcGIS Online / Hub search** | returns the **same county name in a different state** (`Pickens AL`, `Pickens SC`) and a `Parcels` service that is **Virginia** (EPSG:2283). **MEASURED** | ⚠️ **SILENT — and highly plausible.** ⭐ **Always verify the CRS/extent before believing a county service** |
| **USGS EPT** | wrong project prefix → **S3 `NoSuchKey`** | ⛔ **LOUD** — clean failure |
| **Soil Data Access** | malformed T-SQL → an error body; a GET where a POST is required → **400**, which `LAND-SOURCES.md` correctly read as *"my probe being wrong, not the service"* | ⛔ LOUD |
| **`api.weather.gov`** | missing User-Agent → **403** | ⛔ LOUD |
| **Google Solar** | **rural 404** (documented by Google); or returns **BASE** (0.25 m satellite) instead of the 0.1 m aerial DSM | ⚠️ **SILENT in the second case — a 200 with a coarser product** |
| **NAIP STAC** | a state-level gap year (ND, 2026) → **no item** | ⛔ LOUD |
| **County server drift** | URL retired, layer renumbered, CORS dropped | ⚠️ **SILENT — and it happens without notice** |
| **MS / Overture footprints** | a building newer than the derivation epoch is simply **absent** | ⚠️ SILENT — ⭐ **and the absence is itself the change signal** (prior scan §11a) |
| **SSURGO** | returns a map unit whose polygon does not actually cover the ground you stand on | ⚠️ SILENT — **a plausible, authoritative, possibly wrong series name** |
| **3DEP CHM** | reflects the **2018** canopy | ⚠️ SILENT — ⭐ *and disagreement means change, not error* |

> ⭐⭐ **THE CROSS-CUTTING RULE THIS TABLE ARGUES FOR.** Every silent failure above has the same shape: **a valid response carrying nothing, or carrying the wrong place.** ⛔ **A status-code check does not verify a geospatial fetch.** Three assertions catch all of them: **(1) did it return a feature at all; (2) is the returned CRS/extent the one asked for; (3) does the payload contain data rather than a valid empty container.** `fetch-trace-hires.py` already does (3) for one source, and `check-public-build.py`'s **exit 3 = UNCHECKABLE** already encodes the doctrine — **never green by absence.** ⭐ **Any future source fetcher should inherit that exit-3 convention rather than inventing a second one.**

---

## 16 · What is critical WITHIN this lane

⛔ **I do not rank across lanes and I decide nothing. Paul ranks** `[paul-ruled 2026-09-07, J-b]`. Within *mapping sources*, with evidence:

1. ⭐⭐ **The CHM from the 3DEP point cloud.** Free, storable forever, shadow-free, season-free, the strongest signal for the woods/open line (**74% of the mapped area**), **named as "not yet built" since 2026-09-01**, and — new this session — **it also retires the shadow problem §11 was invented to solve.** Two independent arguments now converge on the same unbuilt artifact. *Evidence: §10, §11c, `LAND-SOURCES.md`.*
2. ⭐⭐ **The unit scale has no geometry to fetch, and the schema change is the unlock.** 151 records over 22 shapes, 322 units on one polygon. ⛔ **No pipeline, no purchase and no model changes that.** The condo is served by **`a named place, geometry optional`** — now reached from **three** independent directions. *Evidence: §3.*
3. ⭐ **Storability is a product boundary and should be written down as one.** It inverts the resolution ranking and it is what actually removes Google Solar — **not price, which is $0 to 1,000 households/month.** *Evidence: §13, §14.*
4. ⭐ **The free-only ruling is sound and has one named hole: Fernwood's own county.** Fulton free, Pickens not; ~ten states with open statewide parcels. **This should be recorded as a known limit, not discovered later as a bug.** *Evidence: §6.*
5. ⚠️ **The shadow-rejection idea should be retired, not softened** — the geometry defeats it at n=7. **The seven-frame stack survives for change-over-time, which is what only it can do.** *Evidence: §11.*
6. ⚠️ **NAIP is a single point of failure with no statutory floor.** The mitigation is free and already half-done: **keep the bytes.** *Evidence: §8a.*

⛔ **Not proposed, deliberately:** no BACKLOG row, no tool, no schema change, no purchase, no credential, no householder-facing surface. **The measurements are the deliverable.**

---

## Probes run — free, unauthenticated, read-only, zero cost

| # | probe | result |
|---|---|---|
| 1 | **USGS 3DEP EPT metadata**, 12 Georgia 2018 blocks (S3, anonymous) | anchor located; **3.71–3.94 pts/m²**, spacing **≤ 0.50–0.52 m** |
| 2 | ⭐ **USDA Soil Data Access** POST at the anchor | **`Tallapoosa cobbly sandy loam, 25 to 60 percent slopes`** · mukey **531363** · **GA622**. **Settles a July LEAD; selects 1 of 4 inferred candidates** |
| 3 | ⭐ **`api.weather.gov/points`** at the anchor | grid **FFC 49,122** · county **GAC227** · forecast+fire **GAZ013** · radar **KFFC**. No key |
| 4 | ⭐ **Fulton County Tax Parcel REST** at the condo (Census-geocoded) | **373,305 parcels countywide**; **151 records / 22 polygons** at 166 m; **112 with unit numbers**; one record **`LivUnits = 322`**; ⚠️ **point query returned zero** |

⛔ **No paid call, no account created, no key created, no credential written.** ⛔ **The condo address is not written into this file, per `.private/condo-location.md`** — only *"a Midtown Atlanta condo."*

---

## Could not reach

| source | why | what it would have settled |
|---|---|---|
| **`tandfonline.com`** — *"Detecting shadows in multi-temporal aerial imagery to support near-real-time change detection"* and *"Normalizing shadows in multi-temporal aerial frame imagery…"* | **HTTP 403, bot-blocked** | ⭐ **The two most on-point papers for §11.** My §11 conclusion rests on the *geometry* (near-noon azimuth invariance), which is independent of them — but a Chrome fetch would either sharpen or falsify the repair in §11c. ⭐ **Worth Paul's browser** |
| **Regrid live pricing** | account-gated self-serve portal | the actual number at household N. ⚠️ A **free "Starter" tier with ~25 lookups/day** appears in secondary sources — **unverified, and it is a lookup allowance, not redistribution** |
| **Google Solar coverage at the anchor** | ⛔ **would require creating a credential — out of scope by instruction** | whether 0.1 m exists here at all. **Still UNPROBED, as on 09-06** |
| **Pickens County GA GIS, direct** | no public endpoint found via ArcGIS Online/Hub | ⭐ **a phone call or an email to the county is the honest next probe, and it is free.** ⚠️ **My finding is "not found," which is weaker than "does not exist"** |
| **landrecords.us coverage page, primary** | read via search summary, page not fetched | the exact list of the ~ten open-parcel states |
| **GSCCCA behind the paywall** | subscription | whether the condo's recorded plans are legible/dimensioned enough to be useful |

## What I did not verify

- ⛔ **I ran no geospatial processing.** No point cloud read, no CHM built, no raster opened, **no image looked at.** §10's conclusions are arithmetic on metadata, not a derived product.
- **The GA_Statewide block containing the anchor is one of B2/B3 — I did not descend the EPT hierarchy to say which.** Both give the same answer.
- **The density figure is a bounding-box lower bound**, not a per-tile measurement.
- **Every floor-plan accuracy figure is vendor-reported.** So are the CubiCasa/Matterport comparison prices, which are **not normalized** and are order-of-magnitude only.
- **"Most states have a condominium-plat recording analogue" is my inference** from the uniform-act lineage. ⛔ **Only Georgia's statutes were read.**
- **The Fulton measurements characterise ONE building's neighbourhood.** The ~7-records-per-polygon ratio is a strong local signal, not a national statistic.
- **NAIP's licensing history is read from a 2018 account and a 2018 blog post.** ⚠️ **I found no evidence of a current proposal** and have deliberately not implied one.
- **The "about ten states" open-parcel figure is a search-surfaced secondary claim**, not read from the primary page.
- **`api.weather.gov` alert *content* was not fetched** — only the point/zone resolution.
- **SSURGO's map unit was not compared against its own polygon extent**, so I cannot say how far the anchor sits from a map-unit boundary. ⛔ **This is exactly the check that decides how much weight the Tallapoosa result carries.**
- **§11's azimuth argument assumes near-noon acquisition.** ⚠️ **NAIP acquisition times are not in the repo's metadata and I did not retrieve them.** If the seven frames turn out to span a wide azimuth range, the killer confound weakens — ⭐ **that is the single cheapest test of my own §11 conclusion.**

---

## Files touched

| file | change |
|---|---|
| `.plans/2026-09-07-mapping-sources-SCAN.md` | **created — this file, and the only one** |

⛔ **Nothing else.** No tracked file edited, no `.plans/2026-09-07-zones-PLAN.md` change (cited only), no `.plans/2026-09-07-lap3-PROCESS-AUDIT.md` touch, no `LAND-SOURCES.md` edit — **the four verified probes in §Probes are a PROPOSED promotion for Paul, not an applied one.** No commit, no deploy, no credential, no purchase. Scratch artifacts stayed in `/tmp`.

## Sequence

⛔ **This is the order the questions resolve in, NOT a work plan and NOT a ranking.** Paul ranks.

| # | step | why here | cost |
|---|---|---|---|
| 0 | **Paul reads §16 and rules on what, if anything, leaves this file** | ⛔ nothing below is authorised | — |
| 1 | ⭐ **Promote the four probe results into `LAND-SOURCES.md`'s VERIFIED tier** — SSURGO, NWS, Fulton, EPT density | four LEADs are now measured; ⚠️ **VERIFIED means "queried and returned data," which is exactly what happened** | minutes |
| 2 | ⚠️ **Record SSURGO's Tallapoosa result in `property.json` as a better-sourced INFERENCE** | ⛔ **W9 stays open.** A map unit is not a texture test | minutes |
| 3 | ⭐ **Measure the seven NAIP frames' RELATIVE registration** against a hard invariant | ⭐ **the cheapest test of my own §11**, and §3c needs it regardless | ~1 hr |
| 4 | ⭐⭐ **Build the CHM** (PDAL install → EPT crop → DSM/DTM → subtract → check against the existing hillshade at identical bounds) | §16 · 1 | ~half a day + install risk |
| 5 | **Fix the parcel-lookup failure mode** wherever address→parcel is used | ⚠️ §15 row 1 is **live and silent** | small |
| 6 | **Ask Pickens County GA directly** whether parcel data is obtainable | free; converts "not found" into an answer | an email |
| 7 | **Only then** revisit Solar, Regrid, or anything paid | 1–6 are free and change what the paid question even is | — |

## Falsifier

**What would show this scan is wrong:**

1. ⭐⭐ **The unit-scale finding falsifies if a county — any county — publishes per-unit condominium polygons as free vector geometry.** My claim is that the record gives identity without shape. **One counter-example collapses §3 and the third leg under `geometry optional`.** *Test: a jurisdiction with a 3D/stratified cadastre (some are being built) exposing unit footprints.*
2. ⭐ **§11 falsifies if the seven NAIP frames' sun AZIMUTHS span a wide range.** My case is *shadows do not move, they only shorten*. **If acquisition times are far from noon and spread across the day, shadows rotate, the intersection shrinks, and presence-counting becomes defensible.** *Test: retrieve the acquisition times from the NAIP STAC items already referenced in the bounds files.* ⭐ **Cheap, decisive, and it tests MY claim, not Paul's.**
3. **§10 falsifies if a derived CHM fails to draw the woods/open line legibly** at the existing bounds. **Then the point cloud's "∞ on kind" is rhetoric and the DEM was the ceiling.**
4. **§6 falsifies if Pickens County GA turns out to publish parcel data** by a route I did not search. ⚠️ **I found nothing; that is not proof of absence, and the section says so.**
5. **§13's ranking falsifies if the product never needs to work without a signal** — but `CLAUDE.md` states the site premise is **PERMANENT**, so this one falsifies only by Paul overruling the premise.
6. **§14 falsifies if Google's free tier is per-*billing-account* in a way that does not scale**, or if the 30-day clause is read by counsel as not attaching to derived polygons. ⚠️ **Both are Paul's call, and both are recorded as unresolved.**

## QA

**This is a research artifact; the QA is on the claims, not on a build.**

| check | how | status |
|---|---|---|
| Every ⭐ **MEASURED** claim traces to a command run this session | §Probes run names all four with their results | ✅ |
| No claim promoted from the prior scan without re-checking | prior §10 rows are **cited, not restated**; the four re-priced rows are named in §1 | ✅ |
| Every unverified claim is tagged | §Could not reach + §What I did not verify | ✅ |
| **Storability stated for every source** | §13 tiers all ten; §§3–9 tables carry the column | ✅ |
| **Access mechanics stated as a gate, not as "free"** | §2a G0–G4, applied per row | ✅ |
| **Cost priced at household N, not per call** | §14 | ✅ |
| **How each source FAILS, loud vs silent** | §15 | ✅ |
| ⛔ **No cross-lane ranking, no decision** | §16 is lane-internal and evidence-cited; §Sequence is explicitly not a work plan | ✅ |
| ⛔ **Nothing shipped** | `Files touched` = this file only | ✅ |
| ⛔ **Condo address not written to a tracked file** | *"a Midtown Atlanta condo"* only; no street number, no unit, no name | ✅ |
| ⛔ **`.plans/2026-09-07-zones-PLAN.md` cited, not edited** | header `cites-does-not-edit` | ✅ |
| ⛔ **`.plans/2026-09-07-lap3-PROCESS-AUDIT.md` untouched** | not read, not written | ✅ |

⚠️ **The QA this file CANNOT do:** it cannot check that a source still behaves next month. **Every probe here is a reading taken on 2026-09-07 and expires the way any live reading does** — which is the same reason `LAND-SOURCES.md` splits VERIFIED from LEAD by *date of query*, and the reason a promotion in §Sequence step 1 must carry today's date.

---

## Sources

**Verified today (2026-09-07) — by query:**
USGS 3DEP lidar EPT on AWS (`usgs-lidar-public`, 12 Georgia 2018 project prefixes) ·
[USDA Soil Data Access](https://sdmdataaccess.nrcs.usda.gov/webservicehelp.aspx) (POST, T-SQL, `SDA_Get_Mukey_from_intersection_with_WktWgs84`) ·
[NWS API](https://api.weather.gov) ·
[Census geocoder](https://geocoding.geo.census.gov) ·
Fulton County `PropertyMapViewer` ArcGIS REST ·
ArcGIS Online + [ArcGIS Hub](https://hub.arcgis.com) dataset search

**Verified today — by reading:**
[Google Maps Platform pricing — Solar API SKUs](https://developers.google.com/maps/billing-and-pricing/pricing) ·
[Solar API usage and billing](https://developers.google.com/maps/documentation/solar/usage-and-billing) ·
[USDA considers switching NAIP to a license model — UC ANR IGIS](https://ucanr.edu/blog/igis/article/usda-considers-switching-naip-imagery-license-model) ·
[NAIP: The Loss of a Public Good](https://engelsjk.com/posts/naip-the-loss-of-a-public-good/) ·
[O.C.G.A. § 44-3-74 — recording condominium instruments and plats](https://law.justia.com/codes/georgia/2022/title-44/chapter-3/article-3/section-44-3-74/) ·
[O.C.G.A. § 15-6-67 — Condominium Plat Book, electronic submission](https://law.justia.com/codes/georgia/title-15/chapter-6/article-2/section-15-6-67/) ·
[GSCCCA plat index](https://www.gsccca.org/learn/search-systems/plat-index) ·
[NC OneMap orthoimagery — 6-inch, freely available](https://www.nconemap.gov/pages/imagery) ·
[NYS orthoimagery](https://gis.ny.gov/orthoimagery) ·
[USGS topographic data quality levels — QL1 > 8 pts/m², 0.5 m cell](https://www.usgs.gov/3d-elevation-program/topographic-data-quality-levels-qls) ·
[Vermont statewide QL1 2023](https://vcgi.vermont.gov/data-release/statewide-2023-ql1-lidar-derived-elevation-products-now-available) ·
[Copernicus DEM — GLO-30 free, EEA-10 restricted](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM) ·
[National Address Database](https://www.transportation.gov/mission/open/gis/national-address-database/national-address-database-nad-disclaimer) ·
[Regrid parcel API](https://regrid.com/api) · [Regrid — Pickens County GA](https://app.regrid.com/store/us/ga/pickens) ·
[landrecords.us coverage](https://landrecords.us/documentation/coverage) ·
[Medoid/median compositing](https://github.com/bharathk113/Medoid-HLS-Compositing) ·
[Assessment of spatial co-registration of multitemporal large-format imagery](https://pmc.ncbi.nlm.nih.gov/articles/PMC3673411/) ·
[Topography-aware registration refinement — Landsat/Sentinel-2/NAIP](https://pubs.usgs.gov/publication/70278954) ·
[Polycam floor-plan software comparison](https://poly.cam/blog/best-floor-plan-software-compared-accuracy-speed-and-cost) ·
[Apple RoomPlan for contractors](https://www.scanmanifold.com/blog-posts/roomplan-scan-contractors) ·
[AHN + Dutch national orthophoto programme](https://en.wikipedia.org/wiki/National_lidar_dataset) ·
[IGN France LiDAR HD](https://lidarvisor.com/download-ign-france-lidar/)

**⛔ Could not reach (bot-blocked / paywalled) — named, not dropped:**
[Detecting shadows in multi-temporal aerial imagery](https://www.tandfonline.com/doi/full/10.1080/15481603.2017.1279729) (403) ·
[Normalizing shadows in multi-temporal aerial frame imagery](https://www.tandfonline.com/doi/full/10.1080/15481603.2018.1489446) (403) ·
Regrid live pricing portal (account-gated) ·
GSCCCA document images (subscription)
