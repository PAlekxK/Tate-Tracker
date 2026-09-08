# derived-first-draft · Process B — address in, a confirmable first draft of a household's map out

- row: BACKLOG.md § ▶️ NEXT · Process B — the derived first draft (**ROW TO ADD** — see § Row to add; the orphan flag is expected until it lands)
- objective: O3
- class: engine · declared
- question: what is the SMALLEST thing that turns an address into something a household can correct — and what does running it actually cost in installs, minutes and silent wrongness?
- seats: engineering-partner → .engineering/2026-09-07-zones-v1-path.md
         ai-advisor → .plans/2026-09-07-mapping-sources-SCAN.md
         ux-expert → waived: the v1 renders to an operator on a laptop and to nobody else. ⛔ NOT waived at v2, and the waiver is scoped for that reason — the moment a derived draft reaches a household's phone it is a surface
         content-steward → waived: the v1 produces geometry and a coverage report, no prose and no words that reach a person
         user-researcher → OWED, not waived, before v2: step 7 of the chain — *"they correct it in words"* — rests on **zero observations**, and that is a research question, not an engineering one
         practice-steward → waived: this is a product capability, not a loop
- depends-on: .plans/2026-09-07-capture-write-path-PLAN.md
- trails-read: .plans/2026-09-06-ai-mapping-capability-SCAN.md · .plans/2026-09-07-mapping-sources-SCAN.md (ai-advisor's two scans — this plan builds on them and does not redo them) · .plans/2026-09-07-lap3-BRIEFING.md §8 (the grade-the-v1 rubric)
- stage: concept
- stage-note: 2026-09-07 — design lane of release lap 3. NOTHING SHIPPED. No code written; five read-only, keyless, zero-cost network probes run and reported below.

> ⚠️ **NO `ready:` LINE, DELIBERATELY.** `check-backlog-ready.py` will flag *"stage `concept` with no
> `ready:` stamp"*. **That flag is correct.** The stamp is Paul's alone.

> **WIP:** `concept` is uncapped by ruling, so this waits on nothing and needs no exception. It
> cannot enter `build` today (`build 1/1` + three exceptions). **Paul rules that, not this file.**

---

## §0 · THE FIVE PROBES — run tonight, and they are the plan's central argument

Free, keyless, read-only, `$0`. **Python standard library only** — `urllib.request` + `json`.

| # | probe | result | what it means |
|---|---|---|---|
| 1 | TIGERweb `Transportation/0` over Fernwood's bbox, `f=geojson` | **200 · 42 B · `features: []`** | ⚠️ **silent empty** |
| 2 | TIGERweb `Transportation/2`, same bbox | **200 · 42 B · `features: []`** | ⚠️ **silent empty** |
| 3 | ⭐ TIGERweb `Transportation/8` (Local Roads), same bbox | **200 · 991 B · n=1 · `Church Mountain Rd` · LineString · 0.4 s** | ✅ **the frame is fetchable with zero installs** |
| 4 | "Microsoft Building Footprints" Esri FeatureServer, same bbox | **200 · 98 B · `features: []`** | ⚠️ **silent empty — and the service extent is `6.36M, 1.72M`, State Plane feet, NOT Georgia** |
| 5 | FEMA NFHL flood zones, same bbox | **200 · n=1 · 6.5 s · MultiPolygon** | ⚠️ **10,530,925 bytes for ONE feature** |

> ### ⭐⭐ FINDING 1 — THE PIPELINE NEEDS NO INSTALLS, AND THAT DECIDES ITS ARCHITECTURE
> Probe 3 returned the property's road, correctly georeferenced, in 0.4 s, using nothing but
> `urllib.request` and `json`. **Measured at HEAD: `pdal`, `gdalinfo`, `laszip`, `lasinfo`, `ogr2ogr`
> are all absent, and `laspy`, `rasterio`, `pdal`, `shapely`, `pyproj`, `geopandas` and even `numpy`
> and `requests` all fail to import. The only third-party package on this machine is `PIL`.**
>
> ⭐ **And that is not a gap — it is the existing design.** Every one of the 63 tools in `tools/`
> runs on the standard library; exactly two import `PIL`. `fetch-basemap.py` already produces a
> georeferenced NAIP crop this way, because **ArcGIS ImageServer and STAC render server-side and
> return a PNG.** The reprojection happens on someone else's computer.
>
> ⛔ **So the v1 boundary is not a judgement call, it is a measurement:** everything reachable as
> *server-rendered raster* or *ArcGIS REST `f=geojson` over a bbox* is **free to build today**.
> Everything requiring the raw point cloud — the CHM above all — needs PDAL + GDAL via conda,
> a native dependency chain, *"a real afternoon, with a real chance of a bad hour."* **That line is
> the v1/v2 seam, and it costs nothing to respect it.**

> ### ⭐⭐ FINDING 2 — ONE OF FIVE FIRST ATTEMPTS WAS RIGHT, AND THE OTHER FOUR LOOKED FINE
> Probes 1, 2 and 4 returned **HTTP 200, valid GeoJSON, an empty FeatureCollection.** Probe 5
> returned a correct answer no one would want to store.
>
> ⛔ **Probes 1 and 2 are the subtle ones and they are the reason this plan exists.** TIGERweb's
> layers are **scale-banded** — `0` is *Primary Roads Interstates 5M scale*, `8` is *Local Roads*.
> So `features: []` was **TRUE of the layer queried and FALSE of the question asked.** There are no
> interstates at Fernwood. The service was healthy, the bbox was right, the CRS was right, the
> response was well-formed — **and the answer was worthless.** ⚠️ **A status check cannot catch this.
> Neither can a feature-count check**, because zero is a legitimate answer for that layer.
> **Only a positive control catches it: an assertion that a thing known to be there comes back.**
>
> ⚠️ **Probe 4 is the scan's own §15 warning, reproduced live** — *"an ArcGIS Hub search returns a
> `Parcels` service that is Virginia (EPSG:2283)."* I hit the identical class with a differently
> named service: a plausible *"Microsoft Building Footprints"* FeatureServer whose extent is in
> State Plane feet somewhere that is not Georgia. **My `n=0` was never about Fernwood.**
>
> ⚠️ **Probe 5 is a failure mode neither scan names.** A bbox query returns whole features, and a
> feature's extent is not the query's extent. One FEMA flood polygon is **10.5 MB**. A pipeline that
> naively keeps what it fetched writes ten megabytes per household for one layer. The fix is
> ordinary (`maxAllowableOffset`, or `returnGeometry=false` for a presence check) but it must be
> **designed in, not discovered at household 40.**

---

## §1 · WHAT PROCESS B'S V1 IS — arguing it, not taking it

**The coordinator's instinct — *"one address, one operator, the frame assembled and rendered on
Paul's laptop"* — is right in shape and one word too broad.** The word is **rendered**.

⭐ **My v1: `address → the frame, fetched, georeferenced to one bbox, with a coverage report that
refuses to be green by absence.` Rendering is a viewer over that folder, not part of the derivation.**

**Why split rendering out, when it looks like the same afternoon's work:**

1. **The artifact is the deliverable, and the artifact is what Process A measures.** R-Z4 says the
   23 hand-traced zones are the answer key for what Process B derives. **You compare geometry to
   geometry**, not screenshots. A frame folder with a `bounds.json` per layer can be diffed against
   `zones.json` by a script; a rendering cannot.
2. ⭐ **A viewer already exists and is one line from generalising.** `tools/area-trace.html:253` and
   `tools/zone-capture.html:216` carry the **byte-identical** literal
   `const B={west:-84.36990044993301,…}; const W=1500,H=1500;` — and **every other coordinate
   function in both files (`toLon`/`toLat`/`toX`/`toY`) is a pure function of `B` and `W,H`.** So
   "render the frame" is *read `B` from the sidecar `.bounds.json` that already sits beside every
   basemap*, not a build. **Bundling it into v1 hides how small it is.**
3. **Z-9 says the tracer is disposable scaffolding with a known expiry.** *"Invest in the record;
   treat the tracer as disposable."* Making the render part of the v1's definition of done invests
   in the disposable half.

⛔ **And one thing must be IN the v1 that the eight-step chain buries at step 2:** the coverage
report. **A first map that silently omits the parcel because the county was not covered is worse
than no first map** — that is the brief's own sentence and it is the correct one. **Coverage is not
QA for the v1; it is the v1's product.** What Process B actually delivers to an operator is *here is
what I could find about this address, here is what I could not, and here is which of those I am not
sure about.* Geometry without that report is a confident guess, which is the one thing this repo's
doctrine forbids.

### The v1, stated so it can be graded

> **`tools/fetch-frame.py --lat <> --lon <> --span-ft <> --slug <>`** — one Python script, standard
> library plus PIL, no installs. It walks a **declared source register**, fetches each layer over one
> shared bbox, writes each to `research/frames/<slug>/` with a sidecar `.bounds.json`, and writes
> **`coverage.json`** recording per source: `ok` · `empty` · `unreachable` · **`unverified`**.
> **Exit 3 if any source is `unverified` — never green by absence.**

- **What it does:** turns one address into a folder of georeferenced layers plus an honest statement
  of what is in it.
- **For whom:** **Paul, as operator, on his laptop.** Nobody else, in v1.
- **How we would know it worked:** run it at Fernwood's anchor; every layer whose truth is already
  known in this repo (NAIP frame, road, terrain) must come back and match. Then run it at the condo
  and at one address in a state neither of us has touched. See § Falsifier.
- **What it needs:** nothing installed, no key, no account, no credential, `$0`. It needs the source
  register written and each entry's positive control chosen.

---

## §2 · WHAT THE V1 DEFERS — named, with somewhere to live

*(Per BRIEFING §8: "we'll refine it later" is only honest if the refinement has somewhere to live.)*

| deferred | why not v1 | where it lives |
|---|---|---|
| ⭐ **The CHM (canopy height model) from the 3DEP point cloud** | The only item that breaks the zero-install rule: PDAL + GDAL by conda. **It is also the single most valuable derived layer** (the sources scan ranks it #1 in its lane; two independent arguments converge on it) — which is exactly why it deserves its own row and its own afternoon, not a corner of this one | **its own row**, gated on the install |
| **Step 3 — the edges** (driveway as least-cost path, walls, tree line) | Needs the CHM and the slope raster as inputs. Deriving edges from the optical frame alone re-opens the shadow problem the sources scan just retired | follows the CHM row |
| **Tracer generalisation** (`area-trace.html` / `zone-capture.html`) | ⭐ **One line each** — and it is Process A's tool, which Z-9 rules disposable. Cheap enough to do opportunistically; wrong to let it define a v1 | a `nit`-sized row, or opportunistically |
| **Step 6 — rendering on a household's phone** | ⛔ `viewer.html` is not on the household deploy allow-list and `images/` is not either. **A new build.** §5 | `.plans/2026-09-07-capture-write-path-PLAN.md` §5 already records the `images/` half |
| **Step 5 — loading into the household's store** | LEG 0, already planned | `.plans/2026-09-07-capture-write-path-PLAN.md` |
| **Step 7 — they correct it in words** | **Zero observations behind the premise.** An engineering plan cannot manufacture that evidence | user-researcher seat, marked OWED above |
| **The parcel at Fernwood's own county** | Pickens County GA publishes no free parcel API; free-only is ruled. **Record it as a known limit** | the source register's own `unavailable` state |
| **Paid sources, Regrid, Google Solar** | Free-only ruled. *(Solar is separately disqualified by its 30-day cache limit — a licensing term, not a price)* | out of scope by ruling |

⛔ **Not deferred, and it must not be:** the coverage report and the positive controls. **They are the
v1.** Deferring them produces a pipeline that is confidently wrong, which is worse than no pipeline.

---

## §3 · WHAT ACTUALLY RUNS IT

**A plain `python3` script in `tools/`, run by hand. Not a notebook, not a Worker, not an Action.**
Each rejection has a reason:

| candidate | verdict |
|---|---|
| ⭐ **`python3 tools/fetch-frame.py`** | **Yes.** It is what all 63 existing tools are; it needs no runtime this machine lacks; it is greppable, diffable and re-runnable; and it inherits the repo's own conventions (`--check`, `--selftest`, exit 3) for free |
| Jupyter notebook | ⛔ **No.** Nothing in this repo is a notebook. A notebook's output is not reproducible from the file, its state is invisible in a diff, and it would be the first artifact in the corpus that cannot be run by a check |
| Cloudflare Worker | ⛔ **No, and this is the one worth explaining.** Tempting because onboarding already geocodes server-side. But a Worker has a **CPU-time ceiling**, cannot hold a 10.5 MB response comfortably, has no filesystem to land artifacts on, and — decisively — **derivation is an operator act, not a request.** Putting it on the request path makes a household's page load depend on FEMA's 6.5 seconds |
| GitHub Action | ⚠️ **Not yet, and the door stays open.** An Action is the right home once the register is stable and the run is unattended. Today the run needs a human reading a coverage report, and an Action that emails a report nobody opens is this repo's most-repeated failure. ⭐ **Revisit when the falsifier below has passed at three addresses** |

### Where the artifacts land

```
research/frames/<slug>/
  naip.png              + naip.bounds.json          ← fetch-basemap.py already writes this pair
  terrain-slope.png     + terrain-slope.bounds.json
  roads.geojson         + roads.source.json
  buildings.geojson     + buildings.source.json
  water.geojson         · flood.geojson · soil.json · parcel.geojson  (each + a .source.json)
  coverage.json         ← ⭐ THE DELIVERABLE
```

⭐ **`research/` and not `images/`**, deliberately: `images/property-map/` is Fernwood's *published*
map material and is entangled with the deploy allow-list (§5). A derived frame is **research output
until a human promotes it**, which keeps promotion an explicit act rather than a path default.

⚠️ **Every artifact gets a `.source.json` sidecar carrying the URL, the layer id, the CRS asked for,
the CRS returned, the fetch timestamp and the positive-control result.** This is not bureaucracy —
it is the only thing that would have told me probes 1, 2 and 4 were wrong, and it is the same
`.bounds.json` pattern `fetch-basemap.py` already established and `lidar-hillshade-2018.bounds.json`
already demonstrates at its best.

### The source register, and why `class: engine · declared`

**One register in engine code; the per-county binding is a DECLARED divergence.** The pipeline must
be identical everywhere — that is what makes household N cheap. But **the parcel source cannot be**:
Fulton County publishes a free REST service, Pickens County publishes none, and about ten states
have a statewide layer. **A register with a per-county entry and an explicit `unavailable` state is
the honest shape**; a hardcoded county lookup buried in a fetcher is the third instance of the
embedded-Fernwood-literal defect this repo already carries in `validVertex` and both tracers.

⭐ **And the geocoder already hands us the routing key.** `worker.js` `GEOCODERS.census` returns
`countyFips` — *"the county FIPS the drought and burn-ban readers need."* **The parcel router keys on
FIPS, which is already being stored per household.** Nothing new is needed to route.

---

## §4 · PER-SOURCE FAILURE BEHAVIOUR — the part the probes earned

**Rule, inherited not invented:** `exit 3 = UNCHECKABLE, never green by absence` — the convention
`check-public-build.py` and `check-estate-neutral.py` already carry. The sources scan §15 argues the
same and asks that any new fetcher inherit it rather than mint a second.

**Every register entry declares four things:**

1. **The request** — URL, layer id, bbox, expected CRS.
2. ⭐ **A POSITIVE CONTROL** — a predicate that must hold if the fetch answered the question asked.
   This is the new part and probes 1–2 are why. Examples: *roads → at least one LineString whose
   extent intersects the inner half of the bbox*; *NAIP → the PNG is not a uniform grey*
   (`fetch-trace-hires.py` already does exactly this); *any Esri service → the advertised `extent`
   contains our bbox, checked BEFORE the query.* ⛔ **Probe 4 would have been caught by that last one
   for free, before a single feature was requested.**
3. **A size guard** — `maxAllowableOffset` proportional to the bbox, and a byte ceiling that
   downgrades to `unverified` rather than silently writing 10 MB (probe 5).
4. **Its own `unavailable` declaration** — *"Pickens County GA publishes no free parcel service"* is
   a **fact about the world recorded once**, not a failure rediscovered per run. A source that is
   declared unavailable reports `unavailable`, not `empty`. ⭐ **Those must never print the same**,
   for the same reason `refused:box` and `failed:no-match` are separate outcomes in the geocoder, and
   for the same reason *nobody listened* and *we listened and it was Paul's* must never print the same.

**The four states, and what each licenses:**

| state | meaning | licenses |
|---|---|---|
| `ok` | fetched, positive control passed | use it |
| `empty` | fetched, control passed, genuinely nothing here | say "none here" |
| `unavailable` | declared: no free source exists for this county/layer | say "we cannot know this yet" |
| ⛔ `unverified` | fetched but the control failed, or could not run | **exit 3.** Nothing may be built on it |

⚠️ **`empty` vs `unverified` is the whole design.** Probe 1 would report `unverified` (control: a road
must be found within a bbox that contains a named road) rather than `empty`. That single distinction
is the difference between a pipeline that tells you it does not know and one that tells you there is
no road.

---

## §5 · DELIVERY — the right shape, and why the obvious one is wrong

**Measured:** `tools/pages-deploy.py:67` — `HOUSEHOLD_ALLOW` is nine named paths, no `images/`;
`HOUSEHOLD = {"bob","paul","home"}`; anything else is deleted from the export **and tombstoned**.

⛔ **Adding `images/` as a prefix would ship Fernwood's NAIP frames, the lidar hillshade and slope
rasters, and the historical topo crops to Bob's origin.** That is precisely the failure the
allow-list was written for — the file's own comment records `onboarding/` as a prefix shipping an
unsent outbound draft, publicly readable, measured 2026-09-06. *An exclude-list is a promise that we
thought of everything; an allow-list fails toward serving too little.*

⭐ **The right shape: the instance declares its own frame, and the allow-list is DERIVED from that
declaration.** `instance/<env>.json` gains a frame path; `pages-deploy.py` extends `HOUSEHOLD_ALLOW`
with *that instance's* named files. **Bob's origin ships Bob's frame and nothing else, and the
allow-list stays a list of names rather than a prefix.** This is the same *derive, never re-type*
rule `momlib.config()` enforces on canon values, applied to a deploy manifest.

⚠️ **Deferred to v2 and recorded, not solved here** — v1's frame is read by an operator on a laptop.
But note the failure mode is **a deploy refusal, not a silent leak.** Good failure; still a wall.

---

## §6 · WHAT PROCESS B COSTS PER HOUSEHOLD

| | v1 (frame only, this plan) | with the CHM (deferred) |
|---|---|---|
| **Dollars** | **$0.** Every v1 source is free and keyless: NAIP/STAC, 3DEP ImageServer, TIGERweb, NHD, FEMA NFHL, SSURGO, county parcel where free | **$0** — the point cloud is free too |
| **Installs** | ⭐ **none.** stdlib + PIL, both already present | ⛔ PDAL + GDAL by **conda**, not pip. *"A real afternoon, with a real chance of a bad hour"* — **once**, not per household |
| **Wall-clock per household** | **~30–90 s**, dominated by one or two slow layers (FEMA measured at **6.5 s / 10.5 MB**; TIGERweb at **0.4 s**) | + minutes for an HTTP-ranged EPT crop (tens of MB, not the 43 bn points of the block) |
| **Operator minutes** | ⭐ **~0 to run.** The cost is **reading the coverage report** — call it **2–5 minutes**, and it is the minutes that matter, because that is where a wrong map gets caught | unchanged |
| **Recurring** | none. Every v1 source is **storable** — keep the bytes | none |

⭐ **The target was *"minutes for an operator, not a session,"* and the v1 clears it — but only
because the v1 stops before the tracing.** Naming places is 0-of-16-derivable and permanent; that
time is the household's and is not a cost this pipeline can reduce. **Honest framing: Process B
compresses the *frame* to seconds and does not touch the *naming* at all.**

⚠️ **The cost that does not appear in this table is the one that will bite:** writing a register
entry for a new county's parcel service. That is **research minutes, per county, forever** — and the
sources scan already priced generalising to 3,000+ counties as the load-bearing weak point. **v1 does
not solve it and must not pretend to; `unavailable` is how it stays honest at scale.**

---

## Files touched

**Nothing has been touched.** This session wrote this file and ran five read-only network probes.

| file | change | when |
|---|---|---|
| `tools/fetch-frame.py` | **new** — the assembler; stdlib + PIL; `--lat/--lon/--span-ft/--slug`; `--check`; `--selftest`; exit 3 on `unverified` | v1 |
| `tools/frame-sources.json` | **new** — the declared register: per layer, the request, the positive control, the size guard, the `unavailable` declarations | v1 |
| `tools/fetch-basemap.py` | ⭐ **small**: `main()` passes `momlib.config(...)`-derived `PROPERTY_LAT/LON` into an already-pure `bbox_for_span(lat, lon, span_ft)`. Add `--lat/--lon` (or an `--estate` seam mirroring `build-digest.compose(est, load)`) so the anchor is a parameter, not this checkout's | v1 |
| `research/frames/<slug>/` | **new** output directory (gitignored until a human promotes a frame) | v1 |
| `LAND-SOURCES.md` | record the register and the `unavailable` findings beside the existing source notes | v1 |
| `tools/area-trace.html` `:253` · `tools/zone-capture.html` `:216` | read `B` and `W,H` from a `.bounds.json` instead of the literal — **one line each, byte-identical today** | deferred (cheap) |
| `tools/pages-deploy.py` `HOUSEHOLD_ALLOW` | derive the frame's named files from the instance declaration | deferred (v2) |
| `BACKLOG.md` | § Row to add | on stamp |

### Row to add

> **⭐ PROCESS B — THE DERIVED FIRST DRAFT.** Address in → a georeferenced frame plus an honest
> coverage report out, in seconds, for `$0`, with no installs. **v1 is the frame and the report on an
> operator's laptop**; the CHM, the edges, the tracer generalisation, household delivery and
> "correct it in words" are named deferrals with their own rows. Measured 2026-09-07: **one of five
> first-attempt layer queries returned what was actually wanted; three returned HTTP 200 with an
> empty body.** → READY · `.plans/2026-09-07-derived-first-draft-PLAN.md`

## Sequence

1. **Write the register for Fernwood's anchor only** — NAIP, terrain/slope, roads, water, flood,
   soil. Six entries, each with a positive control. *(Parcel is `unavailable` at Pickens; declare it.)*
2. **`fetch-frame.py` walks the register**, writes artifacts + sidecars + `coverage.json`, exits 3 on
   any `unverified`.
3. ⭐ **Run it at Fernwood and diff against what this repo already knows** — the NAIP bounds, the
   registered lidar rasters, `Church Mountain Rd`, the SSURGO series already probed. **This is the
   only address where the answer is independently known, so it is the only honest first test.**
4. **Parameterise `fetch-basemap.py`'s anchor** (it is already a pure function; only `main()` binds).
5. **Run it at the condo** — a different county, a *free* parcel service, and no land. Expect a very
   different coverage report and treat that as the correct output, not a failure.
6. **Run it at an address in a state neither of us has touched.** ⛔ **Do not skip this** — steps 3
   and 5 are both Georgia, and a pipeline validated only in Georgia is `validVertex` again.
7. **Read the three coverage reports and write down what `unavailable` actually costs.** That number
   decides whether Process B generalises or stays an operator tool for a handful of households.
8. Only then: the CHM row, the edge row, the delivery row.

## Falsifier

Each would kill or materially reshape the v1. Written to be run, not argued.

1. ⛔ **"The frame is assemblable with zero installs."** → **FALSIFIED if any register entry cannot be
   satisfied by a server-rendered raster or an ArcGIS REST `f=geojson` bbox query.** *Partially tested
   tonight: roads ✅ (probe 3), flood ✅ (probe 5), buildings ❌ so far (probe 4 hit a wrong-region
   service; a correct source is not yet identified).* ⭐ **If buildings turn out to require Overture
   GeoParquet, this falsifier fires** — DuckDB/parquet is not stdlib, and the v1 must then either
   drop buildings to `unavailable` or accept an install it was defined to avoid. **This is the most
   likely way this plan is wrong.**
2. ⭐⭐ **"A positive control catches what a status check cannot."** → **Test:** run the v1 against
   TIGERweb layer `0` deliberately. It must report **`unverified`**, not `empty`. If it reports
   `empty`, the control is decorative and the whole coverage report is theatre.
3. **"Process B's output is comparable to Process A's answer key."** → **Test:** run at Fernwood and
   compute the overlap between derived regions and the 23 traced zones. ⚠️ **If nothing in the v1
   frame is region-shaped, this cannot even be attempted — which would mean the v1 stopped one step
   short of being measurable, and should absorb one edge derivation.** *This is the falsifier I am
   least confident about and the reason step 3 comes before step 8.*
4. **"Minutes for an operator, not a session."** → **Test:** time step 5 end to end, including
   reading the report. **If a fresh address costs more than ~15 operator minutes, the register model
   is too manual and the county problem has surfaced early** — which is useful, not fatal.
5. **"$0 per household."** → FALSIFIED if any register entry needs a key, an account or a card. ⚠️
   **Watch this one:** the sources scan found Google Solar's *free tier* still requires a Cloudplatform
   project with **billing enabled and a card on file** — *"free" and "reachable without a credential"
   are different columns.*
6. **"`unavailable` is rare enough to be honest."** → **Test:** step 6, an out-of-state address. **If
   more than half the register reports `unavailable`, the v1 does not produce a first draft — it
   produces a list of things it could not find**, and the deferral table needs re-ranking toward the
   national layers that always answer.
7. **"The derived draft is worth correcting."** ⛔ **NOT TESTABLE BY ENGINEERING.** Zero observations
   stand behind step 7. Flagged to the user-researcher seat rather than assumed away.

## QA

- **`python3 tools/fetch-frame.py --selftest`** — the repo's own convention. Must include a fixture
  that **mutates a positive control into failure** and asserts exit 3. *(`check-arrival-dispositions.py`
  proving itself with three mutations is the model to copy: a check never exercised against a failure
  it should catch is an opinion with a decimal point.)*
- **`python3 tools/check-engine-manifest.py`** — the new tool and register must classify engine/config/instance.
- **`python3 tools/check-config-derivation.py`** — ⭐ **directly relevant.** It guards canon values
  typed into engine code (`34.5496`, `2,873`). **A hardcoded anchor or bbox in `fetch-frame.py` is
  exactly what it exists to catch**, and the v1 must pass it by construction rather than by luck.
- **Two-address rule:** every run of the falsifier set covers **at least two counties in two states.**
  Every embedded-Fernwood-literal defect in this repo passed a single-address review.
- **⛔ Do not add `research/frames/` output to git without a human promoting it.** A NAIP crop is
  public domain and safe; **a parcel response can carry an owner name and a mailing address**, and
  this repo is public. ⚠️ **Strip or refuse owner attributes at fetch time**, and record that the
  register does so — this is the one place the v1 touches personal data and it should be handled
  before the first county service is queried, not after.
- **No Playwright flow in v1** — there is no surface. The first Playwright flow belongs to the
  deferred delivery row.

---

## What I could not verify

1. **A correct, keyless building-footprint source.** Probe 4 was the wrong service. Overture's
   documented paths are DuckDB/GeoParquet or a browser Explorer download — **neither is stdlib**, and
   the Esri-hosted alternative I found does not cover Georgia. **This is falsifier 1 and it is
   unresolved.**
2. **Whether NHD's empty result (probe: 200 · 42 B · n=0) is a wrong layer id or genuinely no mapped
   hydrography.** Fernwood has a pond. I did not introspect that service the way I did TIGERweb.
   ⚠️ **On the evidence of probes 1–2, assume wrong layer until proven otherwise.**
3. **Fulton County's parcel service from this seat.** The sources scan probed it (373,305 parcels,
   151 records / 22 polygons at 166 m, point query zero); I did not re-run it and the condo address
   is deliberately not in this repo.
4. **Operator minutes.** My 2–5 minute figure is reasoned from what a coverage report contains, not
   observed. Falsifier 4 measures it.
5. **Whether `momlib.config()` can be pointed at another estate's `property.json`.** I read that it
   takes a `root` parameter and caches `property.json` globally (`_PROPERTY`); ⚠️ **that module-level
   cache is a live hazard for a multi-estate pipeline in one process** and I did not test it.
6. **Nothing was run against a deployed Worker or a household origin.**

**Sources I could not reach** — per the standing instruction, named rather than dropped:
- ⛔ **Overture's S3/Azure GeoParquet endpoints** — not fetchable from this seat; I could not test
  whether a bbox subset is retrievable over plain HTTP range requests without DuckDB. **This is the
  single fetch that would settle falsifier 1** and it wants a browser or a shell with network.
- ⛔ **`tandfonline.com` multi-temporal shadow papers** — HTTP 403, bot-blocked (carried forward from
  the sources scan, which flagged the same two as *"worth Paul's browser"*). Not load-bearing here:
  shadow rejection is deferred with the edge work.
- ⚠️ **Google Solar coverage at the anchor** — still unprobed, and deliberately: probing requires
  creating a credential, which is out of scope by ruling and by the free-only constraint.
- ⚠️ **Regrid pricing** — account-gated. Out of scope by the free-only ruling; noted only so the
  deferral is not mistaken for an oversight.
