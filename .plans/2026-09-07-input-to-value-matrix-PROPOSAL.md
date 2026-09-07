# input-to-value matrix · What setup asks, what each answer unlocks, and what every card needs before it stops being empty

- row: BACKLOG.md § 🔓 2026-09-06 — FOUR RULINGS · rule 5's general shape ("what we know informs the design, it does not pre-fill her work") + PRODUCT-ENGINE.md § ② THE POPULATION ORDER ("each card carries its own population journey") — no row exists yet; the text is in the callout below (orphan expected)
- objective: O3
- class: engine · declared
- seats: user-researcher → waived: OWED, not judged — this file is the evidence skeleton the seat designs the asks FROM (which input to ask for, in what order, in whose words); commission when Paul rules §3 Q1–Q3
         ux-expert → waived: OWED, not judged — the gate column (at-setup · opt-in) is a screen decision the seat owns; nothing here places anything on a screen; commission with user-researcher
         engineering-partner → waived: OWED, not judged — every BUILD-OUT cell in §1 is a feasibility claim read off the code, not a path-evaluation; the seat prices them once §3 Q1 (coordinates) is ruled, because that one input reprices the rest
         content-steward → waived: no copy is drafted here; the "never-for-this-household" cells cite the seat's own 2026-09-04 place-claims classification rather than re-judging it
         ai-advisor → waived: the AI boundary is not moved by this file — capture stays deterministic; the one AI-on-capture finding (§2.6, /api/classify) is raised as a hunt for Paul, not ruled
- ready: agent-proposed 2026-09-07 — Paul rules
- stage: concept
- wip-exception: a proposal that builds nothing — it opens no item between concept and qa; it is the template Paul asked for (11:30 ET) filled as far as the repo's own evidence allows

> **ROW TO ADD** (`BACKLOG.md`, under § 🔓 2026-09-06 — FOUR RULINGS, after rule 6; the orphan flag stands until it lands):
> `| **⭐ Input-to-value matrix — what setup asks · what each answer unlocks (AUTOMATIC · RESEARCH · BUILD-OUT) · what each card needs before it stops being empty** → READY · .plans/2026-09-07-input-to-value-matrix-PROPOSAL.md — agent-proposed 2026-09-07, Paul rules; O3; engine · declared; user-researcher · ux-expert · engineering-partner OWED (waived with reason, not judged). Weather's rows live in .plans/2026-09-07-weather-card-ARCHAEOLOGY.md, not here. |`

> **Paul's ask, voice, ~11:30 ET 2026-09-07:** *"We should be going through this in a whole process very clearly of saying: OK, during the setup process what information do we ask for? What does that allow us to do automatically versus with research versus with the build-out? What functions of each card do we want additional input before we unlock, to reinforce this input-to-value cycle."*

**What this file is.** The SKELETON for every card and module the engine declares, one row per function, six columns exactly as Paul framed them. It is filled from the repo's own evidence (the manifest, the template, each canon file's `_meta`, the tools that derive things, the place-claims ledger) and nowhere from memory. **Weather is deliberately NOT here** — a parallel agent is writing its rows in this same shape at `.plans/2026-09-07-weather-card-ARCHAEOLOGY.md` (on disk at 11:17 ET, 33 KB; a sibling `2026-09-07-weather-card-PLAN.md` landed at 11:20 — neither was read by this file, by instruction, so their rows and this skeleton have not been reconciled). **Nothing is ranked.** §2 counts; §3 asks.

**Column vocabulary** (the template Paul asked for):

| column | values |
|---|---|
| `input` | what the household must have supplied — `account` · `name` · `address` · `coordinates` · `station id + key` · `a traced zone` · `a photo` · `a species sighting` · `a machine` · `a note` · `roster` (a per-household record already assembled) · `nothing` (verified two ways) · `[new ask]` (no capture exists today) |
| `unlock` | **AUTOMATIC** — derivable now from inputs already held, by code that exists · **RESEARCH** — a one-time per-household lookup a person or script performs (who: `script` / `agent` / `Paul`) · **BUILD-OUT** — engineering not yet done in the engine |
| `gate` | **at-setup** — shows once the input exists · **opt-in** — needs an additional explicit answer (the ask is named) · **never-for-this-household** — Fernwood-only content that cannot generalize as written |
| `fernwood-evidence` | sha or `file:line` showing what it took to reach Fernwood's current state, or `unverified` |

---

## 0 · THE BASELINE — what setup asks today, and the counts

### 0.1 · The roster this matrix enumerates from (the engine, not memory)

| source | what it declares | read |
|---|---|---|
| `tools/momlib.py:226-262` `DOMAINS` | 11 record domains: plant · weed · bird · mammal · amphibian · snake · lizard · insect · fish · vehicle · zone (2 cardable: plant, weed) | ✅ |
| `tools/momlib.py:337-372` `MODULES` + `NON_DOMAIN_MODULES` | 6 domain bundles: garden · motor-pool · equipment · house-systems · wildlife · place; 3 renderer switches: weather · sky · neighbourhood (unbuilt) | ✅ |
| `tools/check-domains.py:44-58` `NON_DOMAINS` | 15 files that are deliberately not domains — property · turf · questions · references · sources · candidates · devices · events · feedback-log · weather ×3 · sun-horizon · plants.draft · estate | ✅ |
| `engine/viewer.template.html` card ids | `card-weather` `card-vehicles` `card-equipment` `card-household` `card-plants` `card-turf` `card-weeds` `card-candidates` `card-wildlife` `card-fishing` `card-celestial` `card-property` `card-fieldnotes` `card-references` `card-release-notes` + `mp-master` (Mama's Perspective) + `unified-input` + the dashboard strip (7 tiles, `:6627-6673`) + `household-add-link` (`:14698`) | ✅ |
| `estate.json` `modules` | Fernwood: all 8 declared `on` (bfb631d, 2026-09-03) | ✅ |
| `instance/fernwood.json` · `instance/home.json` | the per-household switch already built: `absent` (18 files declared absent on the neutral `home` instance), `identity`, `display`; `station: present` vs `declared-absent` | ✅ |
| `INSTANCE-RECIPE.md` §3–§4 (generated) | module → card map; canon file → const → "if absent" | ✅ |
| `engine/place-claims.json` | 58 prose claims: 44 instance-prose · 9 reword · 5 engine-neutral; **29 render `candidates.json`, 8 `property.json`, 1 `events.json`, 1 `sources.json`, 19 are typed in the template itself** | ✅ |
| `tools/check-estate-neutral.py:73` + canon | 7 FIXED identity tokens + every canon species name; ran clean on disk 2026-09-07 12:35 ET (rendered=0 on all six shipped pages; 10 comment-only hits) | ✅ ran |

**Checked against Paul's list of expected domains — three are NOT cards and are placed, not omitted:** *arrivals/deliveries* = `arrival-dispositions.json` + `COMMS-CHANNELS.json`, a Paul-side inbound-feedback process (no card, no module); *land sources* = `LAND-SOURCES.md`, a research registry (VERIFIED vs LEAD tiers) that feeds the RESEARCH cells of property and place; *guides* = `guides/` (9 files), referenced 17× from `vehicles.json` and **0× from the viewer** (grep) — rowed under vehicles. *Sounds* is a per-species asset inside wildlife; *almanac/sun-horizon* is a derived table inside sky and fishing; *journal* is `card-fieldnotes`; *feedback* is the ribbon + `mp-master`.

### 0.2 · What setup ASKS today (`onboarding/index.html`, adde066 2026-09-04 → HEAD; reader `tools/read-onboarding.py`, d4f0fc1 2026-09-06)

| screen | control (`id`) | the ask | where the answer lands | file:line |
|---|---|---|---|---|
| s0 account | `uname` · `uword` · `uword2` | username + password (both optional by ruling; no reset exists) | `/api/account` (worker.js:3184) | onboarding:345, 358, 378 |
| s0 contact | `contactpick` → `uemail` (optional) · `uphone` (optional) | "How should Paul reach you?" — email · call/text · please don't; the detail only after the permission | profile `contactPref` · `email` · `phone` (worker.js:3222-3224, 3240-3242) | onboarding:398-420 |
| s0 colour | `swatches` | the place's accent ("Stone unless you pick another") | `fw-accent` → profile `accent`; person's `profileAccent` separate | onboarding:428, 765; worker.js:3225, 3231 |
| s1 name | `pname` | "what do you call the place?" (rename later at s4 `rename2`) | `postAnswer("onboard-name")` → profile `placeName` | onboarding:458, 1535; 629, 1454 |
| s2 address | `a1` · `a2` · `city` · `state` · `zip` | the address, as components ("for the map query and the later USPS step" — **no USPS call, no geocoding exists**: grep tools/worker = 0; estate/index.html:329-333 says so in words) | `postAnswer("onboard-address")` + profile `address` · `addressParts` | onboarding:499-521, 763, 1706; worker.js:3226-3227 |
| s3 the wait | `go3` | nothing — says only what is true for every reader | — | onboarding:551-558 |
| s4 confirm | `ok1` · `ok2` · `s4note` · `maplink` | "is this it?" beside a Google Maps link that fires only on tap; a free note | `onboard-addr-confirm` / `-dispute` / `onboard-<kind>` | onboarding:619-620, 643-665, 1634-1651 |
| s5 ranking | `interests` (11 options) · `othernote` | "What matters most at your place? Tap them in the order they matter." — **6 built** (house-systems · equipment · garden · motor-pool · wildlife) + **5 marked `soon`** (papers · map-points · map-zones · ask · handover) + "Something else" → "What's missing?" | `onboard-interests` (ranked ids) + profile `ranked`; `onboard-interests-other` | onboarding:687-702, 850-887, 1492-1495; worker.js:3228 |
| every screen | `fbnote` | "Something not right? Tell me." | `note-<screen>` | onboarding:743-749, 1293 |

**Where those answers already reach the app** (the input→value wiring that EXISTS): the ranking orders the cards and opens #1 (`READER_RANKING`, template:17560-17575, 17742-17750); each ranked-but-empty module carries a three-line invitation (`EMPTY_CARD_COPY`, template:17509-17537); each ranked `soon` item renders as an idea card "not built yet" (`renderIdeaCards`, 17627); unranked modules are offered as "ask next" chips whose tap is recorded with the account (17673-17718); the address lands on the property card's face (`renderHouseholdFirstScreen`, 17886-17925); and **`SITE_PLACED` is false for every new household** (template:7262-7268) because nothing turns the address into coordinates — so weather, sky, water and the property page say "Your address isn't on the map yet" (`UNPLACED_COPY`, 17538-17549).

**What setup does NOT ask** (verified two ways — no control on the page, no field on the profile row): the kind of place (ruled 2026-09-06: never assume), coordinates, county, a weather station id or key, a photo, what is planted, what machines exist, whether there is water, who else lives there. Every `[new ask]` in §1 is one of these.

### 0.3 · The counts (predicates stated)

| count | value | predicate |
|---|---|---|
| cards enumerated | **18** | `### ` headings in §1 — weather (rows deferred to the archaeology file), neighbourhood (unbuilt) and papers (no card yet) are each counted as one |
| functions rowed | **92** | table rows in §1 whose first cell is a card name (weather's pointer row excluded) |
| unlock split | AUTOMATIC **31** · RESEARCH **27** · BUILD-OUT **9** · mixed (a cell naming two classes — "RESEARCH today; BUILD-OUT for…") **22** · other (a gate-only cell: "opt-in by design", "never … as built") **3** | leading class word of the `unlock` cell; a cell naming two classes counts as mixed |
| cells `unverified` | **9** | occurrences of the literal token `unverified` inside §1 table cells; each names what was not checked |
| `[new ask]` inputs | **6** | rows whose `input` cell carries `[new ask]` — an opt-in whose capture does not exist |
| never-for-this-household | **10** | rows whose `gate` cell carries `never-for-this-household` (content, not function) |

---

## 1 · THE MATRIX

Rows are grouped by card. `unlock` names WHO for RESEARCH. A `gate` of *at-setup* means "as soon as the input exists" — for most of the property, sky and fishing rows that input is `coordinates`, which no household has today (§0.2).

### weather (`card-weather`, module `weather`, strip tile)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| weather | **→ every row lives in `.plans/2026-09-07-weather-card-ARCHAEOLOGY.md`** (parallel agent, same six columns). Not redone here. Two seams this matrix depends on and hands to that file: the station is three-state (`present` · `declared-absent` · `undeclared`, `build-viewer.py:73`) and its MAC/keys are DEPLOYMENT inputs, not setup asks (`worker.js:37-41`, `INSTANCE-RECIPE.md` §6); and frost is ruled a **weather-module** three-layer derivation (`.plans/2026-09-03-c7-condo-paper-model-PLAN.md:205-212`) — see property row 5 and §3 Q7 | — | — | — | pointer |

### sky (`card-celestial`, module `sky`, strip tile `dash-astronomy`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| sky | moon phase · illumination · NASA Dial-a-Moon image | coordinates (the renderer returns before anything if `!SITE_PLACED`) | AUTOMATIC | at-setup | template:16468-16490 (`calcMoonAge`, `dialAMoonUrl`) |
| sky | tonight's stargazing from live cloud layers (NWS) with WMO fallback | coordinates + current weather | AUTOMATIC | at-setup | template:16281-16290 (`api.weather.gov/points/lat,lon`), 16476-16477 |
| sky | moon rise/set · true-dark window (sun 18° below) | coordinates | AUTOMATIC (SunCalc) | at-setup | template:15764 (`loadSunCalc`), 16512-16520 |
| sky | meteor-shower and celestial-event roster with per-event tips | nothing (a calendar) — but the tips assert a dark-sky place ("from your property's dark Bortle N skies", "from a south-facing clearing") | AUTOMATIC roster; the tips are engine prose carrying a place claim | at-setup for the roster; **never-for-this-household** for the tips as written | place-claims `a117d99f33` (template:7228) · `c2868040dc` (`georgiaVisibility` hardcoded, template:7294-7459); `:7328` interpolates `sky.bortleEstimate` into a claim |
| sky | Bortle rating · SQM estimate · Milky Way months · best spots | `sky` block in `property.json` — hand-authored; no atlas lookup by coordinates exists | RESEARCH (agent, from a light-pollution atlas, 2026-05); BUILD-OUT if it is to be automatic | at-setup once researched | `property.json` `sky._meta` (moved from `CELESTIAL_DATA` 2026-09-03); `research-resources.md` "Top finds" #4 |
| sky | terrain-horizon sunrise/sunset — when the sun actually clears the ridge (drives the sunset tile) | coordinates + a 1-arcsec SRTM tile | RESEARCH (script: `tools/gen-sun-horizon.py`, run by Paul/agent; the tile name `N34W085.hgt` is typed, coordinates are read from canon) | at-setup once run | `sun-horizon.json` 628abf1 (2026-07-25); `gen-sun-horizon.py:171` (`momlib.config("location.coordinates…")`), TILE literal near :10 |

### property (`card-property`, module `place`; strip tile `dash-property`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| property | address on the card face, two lines, "Apt 3B" kept whole | address | AUTOMATIC (built) | at-setup | template:17886-17925; `renderHouseholdFirstScreen` |
| property | **coordinates → `SITE_PLACED`** (the one input most rows below wait on) | coordinates — no ask, no derivation: "There is no geocoding path in this product" | BUILD-OUT — a free, keyless geocoder is named and not built (`ai-mapping SCAN` §6 row 1: "US Census Geocoder … no — trivial") | at-setup once built (or `[new ask]`: place a pin) | template:7262-7268; estate/index.html:329-333; `.plans/2026-09-06-ai-mapping-capability-SCAN.md:356` |
| property | county · region rows | address → county | RESEARCH today (typed in `property.json`); derivable from a geocode → BUILD-OUT | at-setup | `property.json` `property.county/region`; template:13800-13804 |
| property | elevation (measured, with confidence) | coordinates | RESEARCH (Paul/agent sampled USGS 3DEP 1 m lidar by hand 2026-08-31; the automatic Open-Meteo elevation API read 86 ft high here) | at-setup | `property.json` `location.elevation.basis` + `supersededValue.lesson` |
| property | USDA hardiness zone + elevation-adjusted zone | coordinates + elevation | RESEARCH today (hand-authored from the 2023 map + lapse rate); BUILD-OUT for a derivation — estate/index.html refuses to invent one from a state name | at-setup | `property.json` `hardiness`; estate/index.html:329-333 |
| property | frost dates at elevation (valley station + lapse) with frost-pocket warning | coordinates + elevation + nearest NOAA normals station | BUILD-OUT — Paul ruled frost a three-layer ENGINE derivation, not a per-instance fact; today RESEARCH (hand-authored from KJZP normals) | at-setup | `property.json` `frostDates.source`; `.plans/2026-09-03-c7-condo-paper-model-PLAN.md:205-212`; template:13818-13822 (panel omitted when absent) |
| property | 30-year climate normals chart (live) | coordinates | AUTOMATIC | at-setup | template:16698-16712 (Open-Meteo archive by lat/lon; returns if no coordinates) |
| property | soils — series, texture, pH, drainage | coordinates → USDA Web Soil Survey | RESEARCH (agent; two series removed 2026-07-25 as impossible at this elevation; "INFERRED until the W9 soil test returns") | at-setup; a soil test is opt-in `[new ask: send a sample to the extension lab?]` | `property.json` `_meta.dataSources` (WSS + NRCS OSDs), `soils.likelySeries` |
| property | microclimate prose — thermal belt, aspect, frost pockets, orographic rain | coordinates + aspect (read off satellite imagery) | RESEARCH (agent prose) | at-setup | `property.json` `microclimate`; `location.aspect` "Confirmed via satellite imagery (May 2026)" |
| property | the almanac's opening page — story lead + callouts (Cherokee land · Sam Tate · the AT's first terminus) | nothing derivable — local history | RESEARCH (Paul + agent, `research-resources.md`) | at-setup once written; the content is **never-for-this-household** | `property.json` `story._meta` (moved into canon 2026-09-03 so the engine names no place); place-claims: 8 rows render `property.json` |
| property | local resources — extension office · soil lab · nearest ASOS station · eBird region · drought FIPS · stream gauge · seismic | county | RESEARCH today (hand-authored); county-derived rows (FIPS, extension office, eBird region) are BUILD-OUT | at-setup | `property.json` `resources`; ⚠️ `worker.js` `handleDrought` defaults `fips` to `"13227"` — a Pickens County literal in engine code (mixed) |
| property | watershed panel — USGS stream gauge live flow/stage/temp | a gauge site id (`resources.streamGauge.site`) | RESEARCH (someone picks the gauge) | at-setup; panel omitted when null | template:16208-16222 (`USGS_ETOWAH_SITE` from canon; null → no panel) |
| property | earthquakes nearby (USGS) | coordinates | AUTOMATIC | at-setup | template:16243 |
| property | drought status (US Drought Monitor, by county) | county FIPS | RESEARCH today; BUILD-OUT (FIPS from address) | at-setup | template:19526-19529; `worker.js` `handleDrought` (6 h cache) |
| property | air quality (AirNow, by lat/lon) | coordinates + `AIRNOW_API_KEY` (deployment) | AUTOMATIC | at-setup | template:19500-19505; `worker.js:1097-1107` |
| property | local events roster (annual, ~45 min drive, "not a live feed") | region | RESEARCH (agent-curated 2026-05-19; "Annual review each January") | at-setup once curated; the content is **never-for-this-household** (place-claim `50a0bef48f`, Blue Ridge festivals) | `events.json` `_meta` (902bc47); template:7782 `upcomingEvents()`; **which card hosts the list: unverified** (no `card-events` id; caller not traced) |
| property | the property map (basemap + drawn areas) — opens the card | a basemap (NAIP capture + bounds) + at least one traced zone; an estate whose zones record declares no basemap renders NO map section | RESEARCH today (operator runs `tools/fetch-basemap.py`, which "works at any US coordinate today", then commits `images/property-map/`); BUILD-OUT to run from an address at setup | opt-in — the map is shown EMPTY and she draws (rule 5, 2026-09-06) | `zones.json` `_meta.baseImage*` / `bounds`; `tools/fetch-basemap.py` (2026-07-16); `LAND-SOURCES.md` NAIP table; template:10250-10264; `.plans/2026-09-06-ai-mapping-capability-SCAN.md:359` |

### garden · plants (`card-plants`, module `garden`; strip tile `dash-plants`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| plants | the plant roster (40) with guide prose, soil/aspect/frost notes | `[new ask: what's planted?]` — Paul's stated order: address → aerial → she draws zones → "asks what plants are in what zones" | RESEARCH today (Paul + agent authored all 40; 12 carry `_provenance`); BUILD-OUT for an in-app "add a plant" door — **none found in the viewer: unverified** (no add-plant control traced) | opt-in | `plants.json` 98ad742 (2026-04-30), schemaVersion 9; `PRODUCT-ENGINE.md:1322-1330` |
| plants | reference photo per plant (37 of 40) | roster (scientific name) | AUTOMATIC (script: `tools/fetch-photos.py --category plants`, Wikipedia lead image + attribution) | at-setup once a roster exists | `tools/fetch-photos.py` docstring; `images/plants/_attribution.json`; `plants.json` `photo` 37/40 |
| plants | month-by-month care calendar (prune · feed · water · seasonNotes) | roster + hardiness/frost | RESEARCH (agent-authored `care` per record, 40/40) | at-setup once a roster exists | `momlib.DOMAINS` plant `time=(care, bloom, seasonNotes)`; template:14150 `renderCareBlock` |
| plants | bloom windows + peak panel + narrow-window badges | roster | RESEARCH (authored `bloom`, 26/40) | at-setup | template:17404 `renderPlantPeakPanel`, 14136-14140 |
| plants | "this month" list + today's look-fors on the glance | roster + date | AUTOMATIC from records | at-setup | template:18293 `renderThisMonthPlants`; 17284 `computeLookFors` |
| plants | a plant placed in a zone (plant ↔ zone) | a traced zone + a plant + her answer | opt-in by design — the join is her act, not a derivation; the photo→zone join was measured under its floor for 12 of 18 zones | opt-in | `plants.json` `zones` 40/40; BACKLOG § INBOUND photo-organizer 2026-09-01 (dogwood can be zoned; floor finding) |
| plants | confirm cards from honesty markers (variety · bloom) | roster with `confidence` markers | AUTOMATIC selection (`harvest-questions.py`, deterministic) + Paul's approval gate (RESEARCH: Paul) | opt-in — an ask to her, invitation never obligation | `tools/harvest-questions.py` docstring; `momlib.DOMAINS` plant `markers`, `cardable=True` |
| plants | an observation attached to a species | a note (in-app) | AUTOMATIC (built) | at-setup | template:20307 `fnSaveObservationOnPlant` |
| plants | photo → species suggestion | a photo | BUILD-OUT on the viewer side — `/api/classify` (worker.js:1245, Haiku) classifies a NOTE body, not an image; **whether any photo path reaches a model: unverified** | opt-in | `worker.js:1245-1262`; template calls `/api/classify` once |

### garden · turf (`card-turf`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| turf | the two regimes (turf mown regularly · meadow mown once or twice) and the why | `[new ask: is there lawn or meadow, and where?]` — the prose is about two named Fernwood zones | RESEARCH (agent, 2026-05-28) | opt-in for the function; the content is **never-for-this-household** | `turf.json` `_meta` (f217980), `zoneRepoint_2026_09_01`; `check-domains.py` NON_DOMAINS "care regimes, not entities" |
| turf | grass options with sourcing | candidates roster (native-grass + turf categories) | RESEARCH | at-setup once candidates exist | `turf.json` `_meta` "renders live from CANDIDATES_DATA" |

### garden · weeds (`card-weeds`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| weeds | the weed roster (5) — what to get after, where seen, by whom | a species sighting (`observedOn` · `observedZones` · `observedBy`) | RESEARCH (Paul-observed, agent-authored; "every entry is a HYPOTHESIS until confirmed on the ground") | opt-in — each carries `momConfirm` (5/5) | `weeds.json` `_meta` (e065743, 2026-07-20) |
| weeds | seed-timing window ("worth getting after this before it seeds") | roster + month | AUTOMATIC from records | at-setup once a roster exists | `momlib.DOMAINS` weed `time=(seedTiming,)`; template:14845 |
| weeds | combat advice per weed | roster | RESEARCH (agent drafts behind Paul's gate; capture stays AI-free) | at-setup | `weeds.json` `_meta` "AI may draft combat advice behind Paul's gate" |
| weeds | confirm cards from `confidence` | roster markers | AUTOMATIC selection (harvest) + Paul's gate | opt-in | `momlib.DOMAINS` weed `markers=(confidence,)`, `cardable=True` |

### garden · worth considering (`card-candidates`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| candidates | plants that could be brought in (22) with rationale per natural community | region + natural community + elevation | RESEARCH (agent, GNPS Blue Ridge community lists, 2026-05-26) | at-setup once researched; the content is **never-for-this-household** — 29 of the 58 place-claim rows render this file | `engine/place-claims.json` (29 rows → `candidates.json`); `candidates.json` `_meta` (9fd5ebb) |
| candidates | sourcing — 7 programs + 10 nurseries with a freshness convention | state/region | RESEARCH (Georgia programs; UGA nursery list PDF) | at-setup; content **never-for-this-household** (place-claim on `sources.json`) | `sources.json` `_meta` (9fd5ebb) |
| candidates | a candidate promoted into the plant roster | her/Paul's decision | opt-in — a decision, not a derivation | opt-in | `candidates.json` `_promoted` (1) |
| candidates | intro prose | `property.intros.candidates` | RESEARCH (authored) | at-setup | `INSTANCE-RECIPE.md` §4 `data-record-prose` |

### wildlife (`card-wildlife`: birds · mammals · amphibians · snakes · lizards · insects; module `wildlife`; strip tile `dash-wildlife`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| wildlife | species roster per group — 16 birds · 19 mammals · 12 amphibians · 12 snakes · 5 lizards · 16 insects | coordinates + county + habitat | RESEARCH (agent, from eBird county data · GA herp atlas · Songs of Insects, 2026-05-05 → 08-15); **no automatic roster builder exists — `resources.ebirdRegion` is declared in canon and whether any tool queries it: unverified** | at-setup once researched | `birds.json` `_meta.dataSources` (a822bb9); mammals bde8fe9; snakes/lizards 083d62d; insects ea59e8b |
| wildlife | habitat context / "why good birding" intro | coordinates + habitat prose | RESEARCH (agent prose; names the pond, Lake Sequoyah at 0.3 mi, the clearing) | at-setup; the prose is **never-for-this-household** | `birds.json` `_meta.habitatContext`; template:16901 |
| wildlife | reference photo per species (insects: three, from independent iNaturalist observers) | roster (scientific name) | AUTOMATIC (scripts: `fetch-photos.py`, `fetch-bird-photos.py`, `fetch-insect-photos.py`) | at-setup once a roster exists | tool docstrings; `images/<group>/_attribution.json`; the 2026-08-15 magpie-for-cicada incident is why insects get three |
| wildlife | a sound per vocal species (birds · frogs · insects · mammals; salamanders skipped) | roster | AUTOMATIC (script: `tools/fetch-sounds.py`, Wikimedia Commons by scientific name) | at-setup once a roster exists | `tools/fetch-sounds.py:47-73` CATEGORIES; `sounds/` (instance class, ENGINE-MANIFEST) |
| wildlife | months present · peak · arrival/departure windows ("arriving now") | roster records | AUTOMATIC from records | at-setup | `momlib.DOMAINS` bird/mammal/amphibian/snake/lizard `time`; template:9752, 7552-7568 |
| wildlife | monthly "what to watch for" calendar | roster + `seasonalCalendar` prose | RESEARCH (authored per month) | at-setup | `birds.json` `seasonalCalendar`; template:16905-16915 |
| wildlife | citizen-science programs (eBird · FrogWatch · …) | state/region | RESEARCH | at-setup | `birds.json` `citizenScience` (3), amphibians (2), insects (1); template:16844 |
| wildlife | chorus now — which insects are singing by hour, month and temperature | roster (`hoursActive`, `minTempF`) + current temperature | AUTOMATIC from records + weather | at-setup | template:18716 `renderChorusNow`; `insects.json` `hoursActive` 16/16 |
| wildlife | "we think it's here" — insect presence confirm | roster markers (`presence.confidence`, inferred on 16/16) | AUTOMATIC selection; **deliberately not cardable** → BUILD-OUT to reach her queue | opt-in | `momlib.DOMAINS` insect note ("Deliberately NOT cardable: buildCard is untouched") |
| wildlife | a sighting → pending species → promote/remove | a species sighting | BUILD-OUT on the viewer — `/api/pending-species`, `/api/promote-species`, `/api/remove-species` exist and the template calls none of them (grep = 0) | opt-in | `worker.js:3481-3483`; template grep `pending-species` = 0 |
| wildlife | per-species voice · feeder · fun-fact notes | roster | RESEARCH (authored, 16/16) | at-setup | `birds.json` keys `voice` `feeder` `funFact` |

### fishing (`card-fishing`; wildlife domain `fish`; strip tile `dash-fishing`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| fishing | the lake — name · acres · elevation · distance · history | `[new ask: is there water you fish, and which?]` | RESEARCH (Lake Sequoyah history via Pickens Past, KSU postcard archive) | opt-in; the content is **never-for-this-household** | `fishing.json` `_meta.dataSources` (98ad742); the elevation is the declared confusable sibling in `guru-facts.py` |
| fishing | estimated lake temperature from air-temperature climatology | recent air mean (weather) + month + `waterTempGuide` | AUTOMATIC once a lake and weather exist | at-setup | template:9917 `estimateLakeTemp` → `lakeTempFromClimatology` |
| fishing | 7-day bite forecast with dawn/dusk windows on the LAKE's terrain horizon | daily forecast + `SUN_HORIZON_DATA.lake` | AUTOMATIC given the sun-horizon run (RESEARCH — sky row 6) | at-setup | template:15911-15935 `buildFishingDays`; `sun-horizon.json` `_meta` "LAKE drives the fishing dawn/dusk windows" |
| fishing | species tabs (bass · crappie · bluegill) with temperature phases | lake | RESEARCH (3 species authored) | at-setup | `fishing.json` `species` (3); `momlib.DOMAINS` fish `time=(tempPhases,)` |
| fishing | regulations bar (10/day · 12" min · "verify at georgiawildlife.com") | state | **never-for-this-household as built** — Georgia's limits are typed in the ENGINE template, not read from canon | at-setup | template:10064-10067 |
| fishing | season-at-a-glance (worth fishing by month) | `seasonalCalendar` | RESEARCH | at-setup | `fishing.json` `seasonalCalendar`; template:10040-10050 |

### vehicles · equipment · household systems (`card-vehicles` · `card-equipment` · `card-household`; three modules over one domain, `vehicles.json` by `group`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| vehicles | the machine roster — 7 vehicles · 10 equipment · 6 household systems | a machine `[new ask per machine: what it is; a photo of its plate]` | RESEARCH today (Paul-authored; "household-system group built out from Paul's photos" 2026-08-31); **no in-app "add a machine" door traced: unverified** | opt-in | `vehicles.json` `_meta.householdNote` (98ad742 → 2026-09-06) |
| vehicles | specs table · VIN badge · VIN decode (6 records) | model / VIN | RESEARCH (typed; **the source of `vinDecode` is unverified** — no NHTSA/vPIC tool in the repo, grep = 0) | at-setup once a record exists | `vehicles.json` keys `specs` 23/23, `vinDecode` 6; template:14433-14455 |
| vehicles | maintenance reference (fuel · oil · plug · filters) tagged verified / inferred / tbd | model → manual or on-unit sticker | RESEARCH (manufacturer spec, OEM doc, sticker) | at-setup | `vehicles.json` `_meta.notes` "Confidence convention"; template:14456-14470 |
| vehicles | manual link (📖) + a searchable manuals corpus (no model) + Guru's `search_library` | a manual (URL, or a PDF Paul files) | RESEARCH (Paul downloads via `manuals/download.sh`, `pdftotext` → `manuals/text/`); search is AUTOMATIC once filed | at-setup once a manual is filed | template:14621-14622; `manuals/INDEX.md` (2026-07-08); `tools/manuals-search.py` (517ec38); `worker.js:129` |
| vehicles | service history, newest first, filterable by topic | service events — a note on a machine (in-app) or Paul's ledger | AUTOMATIC capture (built) + RESEARCH for the back-history (8 records) | at-setup | template:20371 `fnSaveNoteOnVehicle`; `worker.js:123` `service_history` tool; `vehicles.json` `serviceHistory` 8 |
| vehicles | rhythms — recurring chores (every N months, last done) | per-machine rhythm entries | RESEARCH (authored, 5 records); **BUILD-OUT: no reader turns "last done + every N" into a due signal on the card — unverified** (the season signal that exists is Paul-side, `fleet_probe.py` S1) | at-setup | `vehicles.json` `rhythms` 5; `worker.js:125` `rhythms` tool; `tools/fleet_probe.py` (07cb089) |
| vehicles | restoration record · open mechanical items · shop contacts · guides (9 files) | Paul's project record | RESEARCH; `guides/` is referenced 17× from `vehicles.json` and 0× from the viewer (grep) | at-setup; the content is **never-for-this-household** (Bolores, Blue Thunder, the DR-Z) | `vehicles.json` `restoration` 6, `serviceContacts` 1; `guides/` ls; template grep `guides/` = 0 |
| vehicles | frost-window put-away signal (a fleet lap is owed) | frost date from canon | AUTOMATIC — Paul-side, non-AI door, not a card | n/a (Paul-facing, O4) | `tools/fleet_probe.py` S1 SEASON; `momlib.config("frostDates…")` |
| vehicles | maintenance confirm cards (`maintenance.*.confidence`) | roster markers | AUTOMATIC selection; vehicle is not cardable → BUILD-OUT to reach a card | opt-in | `momlib.DOMAINS` vehicle `markers`, `cardable` default False |

### place · zones (module `place` + `garden`; the map inside `card-property`; the zone walk inside `mp-master`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| zones | a basemap of the place (NAIP capture, bounds, capture date, leaf state) | coordinates | RESEARCH today (operator: `tools/fetch-basemap.py` — STAC search on Planetary Computer intersecting the anchor; seven captures pulled to one frame); BUILD-OUT to run at setup | at-setup once run | `zones.json` `_meta.baseImageStacItem` / `baseImageCaptureDate` / `bounds`; `LAND-SOURCES.md` NAIP table; `SCAN:359` "works at any US coordinate today" |
| zones | drawing her own areas onto the photo (`map-zones`) | a traced zone — her act on a basemap | BUILD-OUT for a stranger — both tracing tools carry hardcoded Fernwood bounds (maps proposal §7 F; `zone-capture.html:216`); Fernwood's 23 were traced by Paul with Mom via `area-trace.html`, Google Earth Pro and `kml-to-zones.py` | opt-in — the map arrives EMPTY and is built together (rule 5); `map-zones` is `soon` in setup's ranking | `zones.json` 7e7c91b → v3 2026-09-01 (23 zones, 16 names hers); `.plans/2026-09-06-maps-and-zones-PROPOSAL.md:383, §7`; `tools/kml-to-zones.py` (53140cf); BACKLOG § rule 5 |
| zones | zone status (draft → confirmed / flagged) + sync + zone feedback | a traced zone | AUTOMATIC capture (built: `/api/zone-save`, `/api/zones`, sync status) — **but what "confirmation" means (her tap vs Paul's transcription) is ruling B, open** | opt-in | template:13402-13430, 13603-13713; `worker.js:3486-3490`; proposal §7 B |
| zones | the zone walk — a spoken note per area, uploaded | a traced zone + the device mic | AUTOMATIC capture (built: `/api/zone-audio`, `uploadZoneAudio`, an honest-ack outbox) | opt-in — a door, "Another day" rests it until tomorrow | template:10700-10708, 11845-11860; `worker.js:3375` |
| zones | points and lines — the shut-off valve, a path (`map-points`) | `[new ask]` | BUILD-OUT — the schema holds polygons only (ruling C: "lines and points into the schema") | opt-in; `soon` in setup's ranking | onboarding:874-876 `soon: true`; proposal §7 C; `PRODUCT-ENGINE.md:1359` |
| zones | the parcel boundary | address → assessor parcel | BUILD-OUT — Regrid, paid, "a BUY decision"; assessor geometry "is not a survey" | at-setup if bought | `SCAN:357, 430` |
| zones | photos joined to zones | photos with GPS/time + traced zones | BUILD-OUT — measured floor: 12 of 18 zones are under it and "re-tracing will not fix it" | opt-in | BACKLOG § INBOUND photo-organizer 2026-09-01 |

### Mama's Perspective (`mp-master`: acknowledgment · confirm carousel · zone walk; not a module — hidden when `questions` and `ack` are both declared absent)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| perspective | the confirm-card queue (5 slots + bench) | canon with honesty markers → `questions.json` after Paul's approval | AUTOMATIC harvest + RESEARCH (Paul flips `active`) | opt-in — every card is an ask; invitation, never obligation | `questions.json` (efcd060, 22 rows, 5 active); `tools/harvest-questions.py`; `tools/check-cards.py`; template:17756-17758 (hides when absent) |
| perspective | the acknowledgment ribbon — what her answers changed | her prior answers folded into canon | RESEARCH (Paul/agent fold via `fold-answer.py`) then AUTOMATIC render | at-setup once a fold exists | `tools/fold-answer.py`; `tools/check-mom-ack.py`; template:11430-11491 |
| perspective | general feedback ribbon ("Something not right? Tell me.") on every surface | an account | AUTOMATIC (built; `/api/feedback` behind the grant) | at-setup | onboarding:743-749; template CSS :4966; `worker.js:3168` |

### the Almanac door · field notes · Guru (`unified-input` · `card-fieldnotes` · strip tile `dash-journal` · `today-line`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| almanac | a field note — inline, synced to the store or kept on the phone | a note | AUTOMATIC (built; `ObservationStore`, `/api/observations`) | at-setup — the card is hidden until the first note exists (n > 0) | template:20164-20200, 17926-17930 |
| almanac | note classification (a category for the note) | a note + `ANTHROPIC_API_KEY` | AUTOMATIC — ⚠️ a model on the capture path (Haiku over her words); **whether its output writes anything durable: unverified** — raised as §3 Q6 | at-setup | `worker.js:1245-1262` `handleClassify`; template calls `/api/classify` once |
| almanac | Ask Guru — chat over the digest with tools (service history · rhythms · library search) | canon → `digest.json` (`build-digest.py`, rebuilt at deploy) + `ANTHROPIC`/`OPENAI` keys + a daily budget | AUTOMATIC once canon exists | at-setup; ⚠️ setup ranks `ask` as `soon` ("not built yet") while the engine serves it at Fernwood — see §2.5 | `tools/build-digest.py`; `worker.js:123-129`; `.github/workflows/deploy-worker.yml:84`; onboarding:880-882 `soon: true` |
| almanac | the today line (one AI sentence from weather + canon state) | a placed site + weather + a key | AUTOMATIC once placed | at-setup | `worker.js:1176`; template:19615 |
| almanac | today's glance — look-fors from plants and birds | roster records + date | AUTOMATIC from records | at-setup | template:17270-17300 `computeLookFors` |
| almanac | past conversations ("look back") | prior Guru chats | AUTOMATIC | at-setup | `/api/conversations`; template:4264, 17930 |

### references (`card-references`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| references | the research library — 167 entries in 8 categories | region | RESEARCH (Paul's notebook `research-resources.md` → `tools/build-references.py`) | at-setup once assembled; the content is **never-for-this-household** (the Etowah, Cherokee plants, Mount Oglethorpe) | `references.json` `_meta` (5474aad); `research-resources.md` (3f525e4); `INSTANCE-RECIPE.md` §4 "declare absent → the References card hides" |

### release notes (`card-release-notes`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| release notes | the latest five notes | a per-instance `RELEASE_NOTES.md` | AUTOMATIC parse at build; each note is authored per release (RESEARCH: Paul/agent) | at-setup; a new household has none → the card hides | `INSTANCE-RECIPE.md` §4 RELEASE_NOTES row; `tools/build-release-notes.py` |

### the household shell (`homes/` · `estate/` · `settings/` · `household-add-link`)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| shell | the arrival receipt — name, address and ranking read back as the order the work happens in | name + address + ranking | AUTOMATIC (built) | at-setup | estate/index.html:279-340 |
| shell | invite another person into the home | an account | AUTOMATIC (built; a grant) | opt-in | template:14698; `tools/grant-mint.py` |
| shell | place settings · account settings | an account | AUTOMATIC (pages exist); **a reader-facing module on/off menu (PRODUCT-ENGINE ③) is BUILD-OUT — what `settings/place` actually toggles: unverified** (grep `module` = 0) | opt-in | `settings/place/index.html`, `settings/account/index.html`; `PRODUCT-ENGINE.md:1341-1346` |
| shell | the place's colour and the person's colour | a swatch tap | AUTOMATIC | at-setup | onboarding:428; `worker.js:3225, 3231` |

### neighbourhood (module, declared-absent everywhere)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| neighbourhood | community · local events · the urban side (the condo's family) | address | BUILD-OUT — "an unbuilt family; needs the AI-boundary ruling" | never until built | `momlib.NON_DOMAIN_MODULES`; `PRODUCT-ENGINE.md:376-388` |

### papers · handover · export (ranked at setup, no card, no domain)

| card | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| papers | warranties · manuals · deeds; "organised well enough that someone else could pick it up"; export | `[new ask]` | BUILD-OUT — `papers` and `handover` are `soon` in the ranking with no card behind them; `tools/household-export.py` exists for the export half | opt-in; `soon` | onboarding:859-861, 883-885; `tools/household-export.py` |

---

## 2 · WHAT THE MATRIX SHOWS STRUCTURALLY

Method observations only. Counts are of rows in §1 (weather excluded); nothing here ranks.

### 2.1 · Which inputs unlock the most functions (a count)

| input | rows whose `input` names it | what those rows are |
|---|---|---|
| **coordinates** | **17** | every sky row, half of property (elevation · hardiness · frost · normals · quakes · air · basemap), the fishing forecast, the today line — and NONE of them can fire today, because `SITE_PLACED` is false for every new household and no geocoder exists (§0.2) |
| **roster** (a per-household record someone already assembled) | **18** | photos · sounds · months · calendars · chorus · look-fors · harvest — the AUTOMATIC layer is almost entirely *derivations over a roster*, and every roster at Fernwood was RESEARCH |
| **a traced zone** | **6** | plant placement · zone status · the zone walk · the photo join · the map itself |
| **address** | **6** | the card face, the receipt, county (typed) |
| **account** | **3** | the feedback ribbon, invites, settings |
| **a note / a machine / a sighting / a photo** (in-app captures) | **10** | the capture doors that exist (notes, service notes, zone audio) and the three that do not (add a plant, add a machine, a sighting) |
| **nothing** | **2** | the celestial calendar only — and its tips still claim a place |
| `[new ask]` | **6** | what's planted · which machines · lawn/meadow · water you fish · a soil sample · points on the map · papers |

The shape: **one input (coordinates) sits under the largest AUTOMATIC block and is neither asked for nor derived.** The second-largest block (roster derivations) is automatic only *after* a research step that today has no owner other than "an agent, in May."

### 2.2 · Cards whose CONTENT is entirely Fernwood-bound (the function generalizes; the words do not)

`turf` (two named zones) · `candidates` + `sources` (29 + 1 of the 58 place-claim rows) · `references` (Georgia/Etowah/Cherokee) · `events` (Blue Ridge festivals) · the property `story` (8 place-claim rows) · fishing's `lake` · vehicles' restoration/guides. Each is already classed *instance* by `ENGINE-MANIFEST.md` and hides by construction when declared absent (`instance/home.json` declares 18 absent). **None of these is a defect; every one is a RESEARCH function whose Fernwood output cannot be copied.**

### 2.3 · Engine prose that carries a place claim (a different thing: the ENGINE is Fernwood-bound)

Three sites where the template or Worker, not canon, asserts a place: the celestial tips (`a117d99f33`, template:7228; `georgiaVisibility` at 7294-7459), the fishing regulations bar (template:10064-10067, Georgia limits), and `handleDrought`'s default FIPS `"13227"` (Pickens County). `check-condo-falsifier.py` holds the engine at 0 *identity strings*; these are *facts*, which it does not count.

### 2.4 · Functions that are BUILD-OUT and therefore cannot be promised at setup

9 rows. The ones the setup screens already touch: coordinates (the receipt says "We're working out your weather and what grows here from this address", template:17917 — a RESEARCH/BUILD-OUT promise with no script behind it); `map-zones`, `map-points`, `papers`, `handover`, `ask` (five of the eleven ranking options are `soon`; a ranked `soon` item renders an idea card and unlocks nothing). The ones no screen touches: frost and hardiness derivation, county-derived resources, the basemap at setup, a stranger's zone drawing, the parcel, the photo→zone join, a sighting reaching pending-species, insect/vehicle markers reaching a card, a rhythms due-signal, the neighbourhood family, a module menu for readers.

### 2.5 · Where an opt-in ask has NO capture path today

| the ask | what exists | what does not |
|---|---|---|
| "what's planted?" | 40 authored records; a note-on-a-plant door | an add-a-plant door (unverified: none traced) |
| "which machines?" | 23 authored records; a note-on-a-machine door | an add-a-machine door (unverified: none traced) |
| "I saw a …" (a sighting) | `/api/pending-species` + promote/remove in the Worker | any caller in the viewer (grep = 0) |
| "is there water you fish?" · "lawn or meadow?" · "a soil sample?" | canon fields | any ask, anywhere |
| "where is the shut-off valve?" (a point) | ranked `soon` | a schema slot (polygons only) |
| coordinates / "put a pin where the house is" | the address | any ask or any derivation |
| Guru (`ask`) | served at Fernwood, tools wired | the ranking says `soon: true` — the setup screen and the engine disagree about whether this is built |

### 2.6 · One boundary finding, not ruled here

`/api/classify` runs a model over a field note at capture time (worker.js:1245). Capture is ruled AI-free (ai-advisor seat, every plan since 09-05). Whether the classification is decorative (a label the reader sees) or durable (a category written into the record) is not established by this read — §3 Q6.

---

## 3 · OPEN — rulings or hunts for Paul

Each is a yes/no or an A/B, or a hunt with the method that closes it. None is ranked.

1. **Coordinates — A or B?** (A) derive them at setup from the address with the free, keyless US Census geocoder the mapping scan already named (deterministic, no model, no key; `SCAN:356`), or (B) ask the person to place a pin on a map (a `[new ask]`, her act). **This one input sits under 17 rows** and both `UNPLACED_COPY` sentences. (Hybrid — geocode, then show the pin for her to confirm — is A with s4's confirm pattern reused.)
2. **Is RESEARCH a named, visible step of setup — yes or no?** The receipt already promises it ("working out … what grows here from this address", template:17917) while no script performs any of it. Yes → the receipt names who does it and that it lands on the card as it comes in (the sentence half-does this). No → the sentence goes, and RESEARCH functions unlock silently when an operator runs them.
3. **Species roster — A or B?** (A) built per household at setup by research (agent, from eBird/county atlases at the geocoded point — the way Fernwood's were built in May), or (B) empty until a sighting, with the roster growing from what she reports (the `pending-species` path, which needs a viewer door). A fills wildlife on day one with things she has never seen; B keeps rule 5's shape ("what we know informs the design, it does not pre-fill her work").
4. **Machines and plants — a setup ask, or a later door?** Both rosters at Fernwood were Paul-authored; neither has an add door in the viewer. (A) ask at setup ("name three things with an engine"), or (B) the card's own invitation (EMPTY_CARD_COPY) is the door and a capture control is built behind it. Either way the door is BUILD-OUT.
5. **The five `soon` interests — keep ranking them, yes or no?** Yes = they stay as a learning instrument (ruled 09-06: "let them select things … teach us") and render as idea cards. No = hide until built. ⚠️ Independent of the answer: **`ask` is marked `soon` while Guru is served** — hunt: is that a copy error or a decision that a new household's Guru waits for canon? Method: read the commit that added `soon: true` to `ask` (onboarding:880).
6. **Hunt — does `/api/classify` write?** Method: trace the template's one caller of `/api/classify` to where its response goes; if it lands in `ObservationStore` or a canon field, capture is not AI-free and the ai-advisor waiver on every current plan is wrong; if it only paints a label, record that as the boundary's worked example.
7. **Frost and hardiness — weather's rows or property's?** Q7 ruled frost a weather-module derivation (c7 plan :205-212); the property card renders the panel (template:13818). A = weather owns the derivation and property reads it (then the archaeology file carries the row and this file's property row 5 becomes a pointer); B = property owns it. Decides which file the BUILD-OUT lands in.
8. **Hunt — which card hosts the events roster?** Method: grep the callers of `upcomingEvents(` (template:7782) and the element they write into; then the row moves under that card and its gate is checked against `instance/home.json`'s `events` absence.
9. **Hunt — what does `settings/place` toggle today?** Method: read the page's controls; if it exposes no module switch, PRODUCT-ENGINE ③ (a personalization menu for Mom and Bob) is BUILD-OUT and should be rowed as such under the shell.
10. **Engine literals that state a place — move to canon before household #2, yes or no?** The three in §2.3 (celestial tips · Georgia fishing limits · FIPS 13227). Yes = each becomes a canon field with an `if absent → omit` guard, the C7 0b pattern. No = accepted and logged in the divergence contract.
11. **Hunt — is any roster builder wired to `resources.ebirdRegion`?** Method: `grep -rn ebirdRegion tools worker`; a hit makes wildlife row 1 partly AUTOMATIC; none confirms RESEARCH.

---

## Files touched

None. This proposal edits nothing; it reads. The one file it creates is itself.

## Sequence

Not applicable to a proposal (the checker grades proposals on the header alone). If Paul rules §3 Q1–Q3, the sequence belongs to the plan that follows, and it starts with the seats declared OWED above.

## Falsifier

If, after the weather archaeology lands and a second household's setup runs, a function unlocks that this matrix classed BUILD-OUT, or one it classed AUTOMATIC stays dark with its input present, the classification method (reading the code's derivation sites) is wrong in a way the counts in §0.3 would have hidden — re-grade that card from the live surface, not the template.

## QA

`python3 tools/check-backlog-ready.py` after writing (flags recorded in the handoff reply); `python3 tools/check-estate-neutral.py` ran clean on disk 2026-09-07 12:35 ET; every `file:line` above was read in this session against HEAD `e132d63`.
