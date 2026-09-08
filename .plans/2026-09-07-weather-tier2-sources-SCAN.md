# From an address — four axes: derived analysis · advisory ask fodder · civic links · events

- row: `BACKLOG.md` § ▶️ NEXT · TIER 3 · STEER · **weather card from an address** — this file seats under `.plans/2026-09-07-weather-card-PLAN.md` as a **source scan** for its § 0-PRIME ⑤ tier-2 row. **Axes 3 and 4 extend `BACKLOG.md` C7-R5 / census D3 / `PRODUCT-ENGINE.md`'s *"a domain family that does not exist yet (events, the neighbourhood)"*** — ⛔ **not a new thread.** ⛔ **No row proposed, nothing ranked across lanes** (`[paul-ruled 2026-09-07, J-b]`); §15 states only what is critical *within this lane*, with evidence.
- objective: **O3** — *Fernwood is instance 1 of a product; the engine transfers to a second estate without a fork.* Every question here is *"what can be known from an address alone, at household N."*
- class: engine · **declared** *(a research artifact, not machinery. ⚠️ If any of it becomes a **source registry** the card reads, that registry is `engine · must-not-diverge` — a second copy of "where the frost date comes from" is the drift this repo pays for. Paul assigns the tier.)*
- question: four separate ones, kept separate on purpose — **① what free source DERIVES each figure in Fernwood's analysis layer · ② what ADVISORY classes exist to ask people about · ③ what CIVIC facts fall out of an address · ④ whether any free national EVENTS source exists at all**
- seats: ai-advisor (sole). ⛔ Not a substitute for engineering-partner on any build; nothing here is scoped as work.
- kind: scan
- gate: ⛔ **NOTHING SHIPPED.** No code, no deploy, no purchase, **no API key created, no account signed up for, no paid call made.** **69 free, unauthenticated, read-only probes** were run (§ Probes run). No tracked file edited outside this one.

> ### ⭐⭐ THE FOUR AXES, AND WHY THEY ARE NOT ONE LIST
>
> | axis | what it is | who decides | needs a ruling? |
> |---|---|---|---|
> | **① DERIVED ANALYSIS** §§3–7 | elevation · frost · hardiness · normals, computed from the address | ⭐ **nobody — it is AUTOMATIC** | no |
> | **② ADVISORY ASK FODDER** §11 | pollen · UV · AQI · fire · flood · aurora — *"what are you interested in"* | ⭐ **the household**, at setup | no |
> | **③ CIVIC LINKS** §12 | fire district · school district · library · Extension · utility | ⭐ **jurisdiction** — membership by rule | no |
> | **④ EVENTS** §13 | *"what's on near me"* | ⛔ **something must SELECT** | ⭐⭐ **YES — J-e's trigger fires** |
>
> ⛔ **Merging them would hide the one thing that matters most:** ① costs nothing and asks nothing, ② and ④ are a person's choice against a **5-slot cap**, ③ is decided by a polygon, and **only ④ crosses the line `[paul-ruled 2026-09-07, J-e]`**: *"the first time anything SELECTS or FILTERS what appears on the card, the order-not-membership rule must be ruled before that ships."*
- extends: `research-resources.md` § Category 6 (NCEI · NWS API · PRISM · SERCC · USDM · AirNow · Georgia Forestry). ⛔ **That list is not re-derived.** It is **probed**, and §6 records where it is **wrong**.
- precedent: `.plans/2026-09-07-mapping-sources-SCAN.md` — same shape (access gates · storability · cost at N · how each source FAILS), different domain. Its axes are reused by name rather than re-invented.
- trails-read: `.plans/2026-09-07-weather-card-PLAN.md` § 0-PRIME ⑤ · `.plans/2026-09-07-weather-card-ARCHAEOLOGY.md` §§3–7 · `property.json` · `tools/momlib.py` (DOMAINS, MODULE_STATES) · `estate.json` · `engine/viewer.template.html:16774` `:20244`
- cites-does-not-edit: `.plans/2026-09-07-weather-card-PLAN.md` · `research-resources.md` · `BACKLOG.md` · `CLAUDE.md`

> **Grades, on every claim:** `measured` = I ran the probe this session and the number is in § Probes run · `inferred` = derived from two measured facts · `assumption` = neither, and marked so it can be shot down.

---

## 0 · Thirteen findings, before the tables

> **Findings 1–9 are AXIS ①. Findings 10–13 are axes ②③④** and are stated here because three of them are **negative results**, which the brief correctly says are valuable early.

10. ⭐⭐ **AXIS ② — POLLEN, THE FIRST THING PAUL NAMED, HAS NO FREE US SOURCE, AND THE PROBE IS THE CLEANEST POSITIVE CONTROL IN THIS FILE.** `measured` — Open-Meteo's pollen variables return **HTTP 200 with `null` for every species at all three US addresses**, and **real values in Berlin** (`grass_pollen 0.1`, `ragweed_pollen 0.7`). The CAMS pollen layer is **Europe-only**. ⛔ **A healthy service, a well-formed 200, a valid response, and nothing in it** — the exact shape that cost the zones lane five false verifications, caught here only because I ran a positive control at a location where the layer *does* have data. **US pollen is G2 (Google Pollen, billing card) or G3.** §11.
11. ⭐⭐ **AXIS ③ — ONE CALL THE WORKER ALREADY MAKES RETURNS 17 CIVIC GEOGRAPHIES, AND THE CODE READS TWO OF THEM.** `measured` — the Census geocoder with `layers=all` returns, from Fernwood's address: **Unified School District** (Pickens County School District), Congressional District 11, State House 11, State Senate 51, **County Subdivision "Nelson-Tate-Marble Hill CCD"**, CSA, MSA, tract, block group, ZCTA and more. `worker.js:809` takes **lat/lon and county FIPS**. ⭐ **This is a capability already reached and not read** — the same shape as the geocode instrumentation `read-geocodes.py` was built to fix. ⚠️ **And what is NOT in those 17: fire district, police jurisdiction, library, utility.** §12.
12. ⭐⭐ **AXIS ③ — THE MAPPING PASS'S ASYMMETRY REPRODUCES EXACTLY, IN A THIRD DOMAIN, AND IT IS A DENSITY PROBLEM NOT A COVERAGE ONE.** `measured` — OpenStreetMap within **8 km**: the Midtown condo returns **97** civic features (25 libraries · 25 fire stations · 22 police · 22 community centres); Bangor **24**; ⛔ **Fernwood returns `{}` — literally zero, from a healthy 200.** Widen to 15 km and Fernwood returns 7 fire stations and a library (*Talking Rock Volunteer Fire Department* · *Pickens Fire Rescue Station 11* · *Tate Fire Department*). ⭐⭐ **So the data exists and A FIXED RADIUS IS THE WRONG PRIMITIVE** — the same query is a firehose at one household and an empty page at the other. §12.
13. ⭐⭐ **AXIS ④ — THERE IS NO FREE, NATIONAL, LICENCE-CLEAN EVENTS SOURCE. Stating it plainly, as asked.** `.plans/2026-09-07-place-card-AI-BOUNDARY.md` row 9 already establishes it (*"Eventbrite killed public Event Search in Feb 2020 and has not replaced it"*); nothing tonight contradicts it and finding 12 **sharpens it into the boundary question**: ⭐ **selection is forced by DENSITY, and density is what the condo has and Fernwood does not.** At 25 libraries within 8 km something must choose; at zero there is nothing to choose from. ⛔ **So the household that most needs axis ④ is the one that makes J-e's trigger fire — and it is the condo, which is exactly the household C7-R5 serves worst today.** §13.

---

### Findings 1–9 — axis ① (derived analysis)

1. ⭐⭐ **THE 86-FOOT ELEVATION ERROR IS SOLVED BY ONE FREE KEYLESS CALL, AND I PROVED IT AGAINST THE NUMBER THIS REPO ALREADY KNOWS.** `measured` — USGS **EPQS** (`epqs.nationalmap.gov/v1/json`) at Fernwood's anchor returns **2,873.28 ft at 1 m resolution**. `property.json` carries **2,873 ft**, obtained on 2026-08-31 by hand-sampling a 3DEP lidar product. **The free national point service reproduces the hand-measured value to 0.3 ft.** In the same breath it exposes the whole tier-2 thesis: at that same point, Open-Meteo returns **2,959.3 ft (+86.0)**, the NWS gridpoint **2,953.0 (+79.7)**, ACIS's PRISM 800 m cell **2,638 (−235)** and ACIS's NRCC 2.5 km cell **1,854 (−1,019)**. **A 1,105-foot spread across five free sources at one address.** §4.
2. ⭐⭐ **THE FROST DERIVATION REPRODUCES CANON'S FALL DATE TO THE DAY, FROM THREE KEYLESS CALLS.** `measured` — NCEI's **keyless** Access Data Service returns 1991–2020 frost/freeze normals at **JASPER 1 NNW** (record **1937 → today**): T36 first-fall-50% = **10/27**. Apply canon's own lapse rule (7 days per 1,000 ft × the **1,408 ft** the property sits above that station) → **10/17**. `property.json` `atPropertyElevation.firstFall_50pct` = **"October 17."** ⭐ **A number a human researched in July, regenerated tonight by arithmetic over free data.** ⚠️ The spring date does **not** match — derived 04/24 vs canon **May 3** — and the entire 9-day gap traces to canon's *baseline* (April 23) disagreeing with NCEI's T36 (04/14). **One of the two is wrong and nothing in the repo says which.** §5.
3. ⭐⭐ **THE POSITIVE CONTROL EARNED ITS KEEP ON THE SECOND PROBE.** `measured` — `api.weather.gov/points/<lat>,<lon>` returns **HTTP 301** when the coordinate carries more than **4 decimal places**. Fernwood's coordinates are hand-typed at 4 dp and work. **The Census geocoder — which shipped into `worker.js:809` today — returns 12 dp.** `viewer.template.html:16774` concatenates the raw values. The 301 carries a `location:` header so a redirect-following client recovers; ⛔ **but this is a defect that is invisible at Fernwood and present at every geocoded household, and only a non-Fernwood probe could see it.** §6.
4. ⭐⭐ **A FREE KEYLESS CALL PRODUCES THE QUANTITY THAT *DEFINES* A HARDINESS ZONE.** `measured` — RCC-**ACIS** returns the **mean annual extreme minimum temperature, 1991–2020**, from station dailies in one request: **+10.0 °F** at Jasper 1 NNW, **+15.2 °F** at Atlanta Hartsfield, **−16.9 °F** at Bangor Intl. Bangor's derives to zone **5a**, which is exactly what the official map says for that ZIP. ⭐ **The derivation validates at a flat site and diverges at the mountain site — which is the product argument, not a defect.** §5.
5. ⛔⛔ **THE FREE ZIP-KEYED HARDINESS ANSWER IS NOT WRONG — IT ANSWERS A DIFFERENT QUESTION, WHICH IS WORSE.** `measured` — `phzmapi.org/30143.json` returns **zone 8a** and, in the same payload, the coordinate it used: **34.4549, −84.4158** — the **ZIP centroid, 11 km away and ~1,400 ft lower**. It is a correct statement about a valley and a false one about this property. ⛔ **This is the repo's named failure mode wearing a new hat, and there is no status code that catches it.** §6.
6. ⭐⭐ **THE LICENCE, NOT THE PRICE, IS WHAT CONSTRAINS THE BACKBONE — the mapping scan's exact lesson, in a second domain.** Open-Meteo's free tier is **non-commercial use only**, CC BY 4.0, and rate-limited to **<10,000 calls/day · 5,000/hour · 600/minute**. Open-Meteo currently supplies the **forecast, the 25-year archive, the elevation and (if adopted) the air quality** — four of tier 1 and 2's load-bearing rows. ⚠️ And the approved Open-Meteo proxy **concentrates every household onto one IP** against that ceiling. §9.
7. ⭐ **`research-resources.md` IS WRONG ABOUT PRISM, AND THE CORRECTION CHANGES A V1 ROW.** `measured` — the old point service is retired; `services.nacse.org/prism/data/get/us/800m/ppt/<date>` returns **`Content-Type: application/zip`, `prism_ppt_us_30s_<date>.zip`** — a **whole-US raster**, not a point value. ⛔ *"One-time pull of PRISM 800 m point values"* is not a call anyone can make. **The reachable route to PRISM at a point is ACIS grid 21** — and ACIS reports that cell's elevation as **2,638 ft**, i.e. **235 ft below the property**. §6.
8. ⭐ **THERE IS NO NATIONAL BURN-BAN DATASET, SO W17 CANNOT BE FIXED BY FETCHING ANYTHING.** Every aggregator found is commercial and links back to 50 state agencies. ⛔ The Georgia literal `(m >= 4 && m <= 8)` in engine code cannot be replaced by a feed — it can only be replaced by a **declaration with a `not-applicable` state**, which is what §8's rule is for. `measured` (search) / `assumption` (that no free API exists — absence of evidence).
9. ⭐ **EVERY TIER-2 SOURCE EXCEPT TWO SENDS `access-control-allow-origin: *`.** `measured` — EPQS, `api.weather.gov`, NCEI, ACIS, Open-Meteo (both), NOAA Tides all allow the browser. **USDM and the Census geocoder do not** — and both already sit behind the Worker. ⭐ **So the *plumbing* question for tier 2 is settled and it is not the interesting one.** The interesting one is that tier 2 should be computed **once per household and stored**, never per load — which §9 prices.

---

## 1 · What tier 2 actually is, restated so the tables have a subject

`.plans/2026-09-07-weather-card-PLAN.md` § 0-PRIME ⑤ states it: *"the sources were never the hard part… what made Fernwood's card good is the **analysis layer**."* This file agrees and sharpens it into **five derived figures**, because *"the analysis layer"* is not a build target and these are:

| # | derived figure | what Fernwood did by hand | W-row |
|---|---|---|---|
| **D1** | **Point elevation** | a lidar sample, 2026-08-31, after a 90 m model was 86 ft wrong | W22 |
| **D2** | **A reference station** — which long-record station this place is measured against, and how far above it we sit | chose KJZP (1,535 ft) by hand; `property.json` resources.nearestWeatherStation | W23 |
| **D3** | **Frost dates, elevation-adjusted** | NOAA normals + `+10 days spring / −10 days fall` from 1,338 ft × 7 d/1,000 ft | W23 |
| **D4** | **Hardiness zone, elevation-adjusted** | `officialZone 7b` → `elevationAdjustedZone "6b to 7a"` via 3.5 °F/1,000 ft | W23 |
| **D5** | **Normals + "how is this month tracking"** | 25-yr Open-Meteo archive as the regional baseline; PRISM named but never pulled | W11 |

⭐ **And a sixth that Fernwood earned and no new household can have: the station-vs-grid BIAS (~24%).** ⛔ **It is not tier 2.** It requires a device and time — `[W-6]`, tier 3′. Naming it here only to say it is **out of this file**: no free source produces a per-address precipitation bias, because the whole point of the number is that it is measured *against* the free sources.

---

## 2 · The four EVALUATION columns — reused from the mapping scan by name, not re-invented

⚠️ **Not to be confused with the four SCAN axes in §0.** These are the columns every source row is graded on; those are the four kinds of question this file answers.

**2a · ACCESS GATE (G0–G4).** Every tier-2 candidate probed tonight sits at **G0 — anonymous HTTPS, no account, no key, no terms click**. That is genuinely different from the mapping domain, where G2 (billing card) and G4 (government-gated) removed the best sources. ⭐ **In weather, the free tier is not a consolation prize; it is the frontier.** The two G1s in `research-resources.md` — **AirNow** (free key) and **NCEI CDO** (free token) — both have **G0 alternatives measured tonight** (Open-Meteo AQ; the NCEI *Access Data Service*, which is a different service from CDO and needs no token).

**2b · CORS** — `measured`, § Probes run #26–34. `*` on EPQS · NWS · NCEI · ACIS · Open-Meteo × 2 · NOAA Tides. **None** on USDM · Census geocoder.

**2c · STORABLE / REDISTRIBUTABLE** — the mapping scan's product boundary, and it re-fires here for a different reason. Under `CLAUDE.md` § THE SITE'S PHYSICAL PREMISE (no cell, canopy), **a derived figure must survive with no network** — which it does trivially, *because tier 2's output is five numbers stored on the estate record*. ⭐ **Tier 2 is the most offline-friendly thing on the board**, and that is an under-argued point in its favour.

**2d · COVERAGE — national vs patchy.** ⭐ **The axis that broke the mapping pass** (free solved the condo, not Fernwood). Tested deliberately at three addresses in two states plus six spot checks. §3's coverage column is the answer, and **for once it comes out the right way round.**

---

## 3 · The landscape — every candidate, probed

**All rows `measured` tonight unless the grade says otherwise.** ⭐ = recommended path for that figure.

| source | gives | gate | CORS | resolution | coverage | licence / storable | how it FAILS |
|---|---|---|---|---|---|---|---|
| ⭐⭐ **USGS EPQS** `epqs.nationalmap.gov/v1/json` | **D1** point elevation + the DEM's own resolution + acquisition date | **G0** | ✅ `*` | ⭐ **1 m** returned at **8 of 9** probes (Fernwood · condo · Bangor · rural NV · Hilo · Leadville · New Orleans · W Texas) | ⭐ **national**; ⚠️ **Alaska returns a different product** and expresses `resolution` in **degrees** (3.09e-05 ≈ 1/9 arc-sec), not metres | ✅ **public domain** (`assumption` — USGS policy, no terms page read tonight); store forever | ⛔ **LOUD** on a bad coordinate; ⚠️ **SILENT on `resolution` units** — a reader that assumes metres reads Alaska as 3-hundredths of a metre |
| ⭐⭐ **NCEI Access Data Service** `ncei.noaa.gov/access/services/data/v1` | **D3** frost/freeze normals (**T36 · T32 · T28**, at **FP10/50/90**), growing-season length, **D5** monthly Tmax/Tmin/precip normals 1991–2020 | ⭐ **G0 — NO TOKEN.** *(distinct from **NCEI CDO**, which does need one — `research-resources.md` names only CDO)* | ✅ `*` | per **station** | ⚠️ **station-based, and stations are sparse.** `measured`: **exactly 1** station with annual/seasonal normals in a ~25 km box around Fernwood | ✅ public domain (`assumption`) | ⛔ LOUD on a bad station id; ⚠️ **SILENT when the nearest station is nothing like your place** — §5's whole subject |
| ⭐⭐ **RCC-ACIS** `data.rcc-acis.org` (`StnMeta` · `StnData` · `GridData`) | **D2** station discovery *with elevation and record span* · **D4** mean annual extreme minimum · gridded values at a point (grid 21 = PRISM, grid 1 = NRCC 2.5 km) | **G0** | ✅ `*` (GET form: `?params=<urlencoded JSON>`) | station; grids 800 m / 2.5 km | ⭐ **national** — 44 stations near the condo, 16 near Bangor, 10+ near Fernwood | ⚠️ **no published terms, no published rate limit, no key** — free in practice, **contract-free** (`measured`: docs.rcc-acis.org carries none) | ⛔ LOUD on malformed JSON; ⚠️⚠️ **SILENT AND SEVERE**: `GridData` accepted `"normal":"1"` and returned **twelve monthly values that are not normals** (0.04″, 0.00″, 0.39″ for a place whose normals are 4–6″/month) — **HTTP 200 carrying the wrong quantity** |
| ⭐ **Census geocoder** | lat/lon + **state FIPS + county FIPS** (already shipped, `worker.js:809`) | G0 | ⛔ **none** | address-range **interpolated** | national | ✅ public domain | ⚠️ **SILENT** — `measured`: it places Fernwood **60 m** from canon, and EPQS at that point reads **33.9 ft lower**. On a spur, *where* is *what* |
| ⭐ **`api.weather.gov`** | zones (forecast · fire · county), radar, grid, **alerts**, gridpoint elevation | G0 (User-Agent required) | ✅ `*` | zone / 2.5 km grid | ⚠️ **US only** | ✅ public domain | ⛔ LOUD without a UA (403); ⚠️ **301 above 4 dp on `/points`** — finding 3. `/alerts/active?point=` accepts 12 dp fine |
| ⭐ **US Drought Monitor** `usdmdataservices.unl.edu` | D0–D4 percentages **by county FIPS** | G0 | ⛔ **none — server-side** | county | ⭐ national. `measured` tonight: Pickens **D0 100%**, Fulton **D0 100%**, **Penobscot ME D1 100% / D2 21.4%** | ⚠️ free; attribution to NDMC/USDA/NOAA (`assumption`) | ⛔ LOUD |
| **Open-Meteo** — forecast · **archive (ERA5)** · elevation · **air quality** | tier 1's live half; **D5**'s 25-yr baseline; a **keyless US AQI** | G0 | ✅ `*` | ~11 km ERA5 · ~90 m elevation model | global | ⛔⛔ **free tier is NON-COMMERCIAL ONLY**; CC BY 4.0; <10k/day · 5k/hr · **600/min** | ⚠️ **SILENT on elevation** — it returns 902.0 m at Fernwood with no error; ⛔ LOUD at the rate limit (429), which this repo has already hit |
| **AirNow** | **measured** EPA AQI at a monitor | **G1** — free key | ⛔ none | monitor (75-mile search here) | national, sparse rural | ⚠️ terms unread | already proxied |
| **NOAA Tides & Currents** | water levels — **the applicability worked example** | G0 | ✅ `*` | 302 stations | ⭐ coastal only, by construction. `measured`: nearest station **423 km** (Fernwood), **376 km** (condo), **64 km** (Bangor) | ✅ public domain (`assumption`) | ⛔ LOUD |
| ⛔ **PRISM direct** `services.nacse.org` | 800 m normals | G0 | — | 800 m | national | ⚠️ academic terms unread | ⛔ **NOT A POINT SERVICE** — returns a whole-US **ZIP raster per date**. Finding 7 |
| ⛔ **phzmapi.org** | hardiness zone by **ZIP** | G0 | — | **ZIP centroid** | national | unofficial third party | ⚠️⚠️ **SILENT — answers about the ZIP, not the household.** Finding 5 |
| ⛔ **USDA PHZM official** | the authoritative zone | — | — | 800 m | national | — | ⛔ **no public JSON point API found** (`measured`: `/api/zone?lat&lon` returns the site's HTML). ⚠️ *not found* ≠ *does not exist* |
| ⛔ **Burn-ban aggregators** (FireRisk.ai · Burn Ban Radar · CityRuleLookup) | state/county burn restrictions | G3 commercial | — | county | claim 47–51 states | ⛔ display-bound | — |
| **SERCC · SECASC · Climate Explorer · DarkSky · IMO · Stellarium** | context and deep-dives | G0 | — | — | ⚠️ **SERCC is 8 Southeast states only** | — | — |

> ⭐⭐ **THE COVERAGE VERDICT, and it inverts the mapping pass.** In mapping, *"use what's free"* solved the condo and **failed at Fernwood's own county**. In weather it is the other way round: **every D1–D5 input is national, keyless and available at all three probe addresses**, and the *only* regional row on the board (SERCC) is a deep-dive link nothing depends on. ⛔ **The one genuinely patchy resource is station DENSITY** — and that is not a coverage gap, it is the quantity §5 is about.

---

## 4 · D1 — the elevation measurement, five sources × three addresses

`measured`, all values from § Probes run #4–#12.

| source | **Fernwood** (true: 2,873 ft lidar) | **Midtown condo** | **Bangor ME** |
|---|---|---|---|
| ⭐ **USGS EPQS (1 m)** | **2,873.3 ft** — **+0.3** | **987.8 ft** | **127.8 ft** |
| NWS gridpoint (2.5 km NDFD) | 2,953.0 — **+79.7** | 879.0 — −108.8 | 131.0 — +3.2 |
| Open-Meteo (~90 m model) | 2,959.3 — **+86.0** | 1,013.8 — +26.0 | 131.2 — +3.4 |
| ACIS PRISM cell (800 m) | 2,638 — **−235.3** | — | — |
| ACIS NRCC cell (2.5 km) | 1,854 — **−1,019.3** | — | — |
| **spread** | ⛔ **1,105 ft** | 135 ft | **3.4 ft** |

> ### ⭐⭐ THE FINDING IS NOT "EPQS IS BEST." IT IS THAT THE ERROR TRACKS THE TERRAIN.
>
> At Bangor every source agrees within **3.4 ft** and tier 2 buys nothing. At Fernwood they span **1,105 ft** and tier 2 is the difference between a card that is right and a card that is confidently wrong. ⭐ **So tier 2's value is not uniform across households — it is concentrated exactly where a household would most notice.** That is a better draw argument than *"we compute more things,"* and it is measured.
>
> ⚠️ **And the NRCC row is the one to stare at.** ACIS's own 2.5 km grid believes this property sits at **1,854 ft**. Every temperature it serves is a valley temperature. **A product that quietly used it would be wrong by a thousand feet and would never say so.**

**The second half, and it is the one Paul's ruling anticipates:** `measured` — the Census geocoder lands **60.5 m** from canon (Δ 31.4 m N–S, 51.7 m E–W), and EPQS at *that* point reads **2,839.4 ft — 33.9 ft lower**. ⛔ **On a spur, the derived elevation is a function of where the geocoder put the pin.** Confirming the elevation is therefore *partly* confirming the placement, and §7 designs the ask accordingly.

---

## 5 · D2–D4 — the full derivation, end to end, at three addresses

**The pipeline, five keyless calls, run once per household:**

```
address → [Census]  lat/lon + state FIPS + county FIPS          (shipped, worker.js:809)
lat/lon → [EPQS]    point elevation, 1 m                        → D1
lat/lon → [ACIS StnMeta bbox]  candidate stations + elev + record span → D2
station → [NCEI normals-annualseasonal]  T36/T32 frost dates, GSL       → D3 (base)
station → [ACIS StnData yly-min 1991–2020]  mean annual extreme minimum → D4 (base)
Δelev = D1 − station.elev
  D3 = base ± (Δelev × 7 days / 1,000 ft)          ← property.json frostDates.atPropertyElevation.note
  D4 = base −  (Δelev × 3.5–5.5 °F / 1,000 ft)     ← property.json hardiness.lapseRate_F_per_1000ft
```

⭐ **Both lapse constants are already written down in `property.json` and are already Fernwood's own doctrine.** Tier 2 does not invent a method; it **executes the method the repo already used by hand.**

| | **Fernwood** | **Midtown condo** | **Bangor ME** |
|---|---|---|---|
| **D2** station chosen | **JASPER 1 NNW** `USC00094648` | **ATLANTA HARTSFIELD** `USW00013874` | **BANGOR INTL** `USW00014606` |
| station elevation | **1,465 ft** | 1,011 ft | 147 ft |
| record span | **1937-06-01 → today** | 1928 → today | 1953 → today |
| **Δ elevation** | ⭐ **+1,408 ft** | **−23 ft** | **−19 ft** |
| **D3** base T36 last-spring / first-fall | 04/14 · **10/27** | 03/29 · 11/07 | 05/17 · 09/25 |
| **D3** base T32 last-spring / first-fall / GSL | 03/31 · 11/05 · 221 d | 03/15 · 11/20 · **252 d** | 05/04 · 10/04 · **152 d** |
| lapse shift | **±10 days** | ~0 | ~0 |
| ⭐ **D3 derived (T36)** | **04/24 · 10/17** | 03/29 · 11/07 | 05/17 · 09/25 |
| **canon says** | **May 3 · October 17** | — | — |
| **D4** base mean annual extreme min | **+10.0 °F** | **+15.2 °F** | **−16.9 °F** |
| ⭐ **D4 derived zone** | **7a–7b** (5.1 °F at 3.5 °F/kft; 2.3 °F at 5.5) | 8a/8b boundary | **5a** |
| **the free ZIP answer** (`phzmapi`) | ⛔ **8a** | 8a | ✅ **5a** |
| **canon says** | official **7b** · adjusted **"6b to 7a"** | — | — |

> ### ⭐⭐ THREE READINGS OF THAT TABLE, IN ORDER OF WEIGHT
>
> **① The fall frost date is an exact hit.** 10/27 − 10 days = **10/17** = canon. The derivation reproduces a hand-researched number it has never seen. ⭐ **This is the positive control the brief asked for, and it passed.**
>
> **② The spring frost date is a 9-day MISS, and the miss is informative.** Derived **04/24**, canon **May 3**. The gap is **not** in the lapse arithmetic — it is entirely in the baseline: canon's `valleyFloor_KJZP.lastSpring_50pct` says **April 23**; NCEI's T36 at Jasper 1 NNW says **04/14**. ⚠️ Canon also names a *different station* (KJZP, the airport, 1,535 ft) than the one with the long record (Jasper 1 NNW, 1,465 ft), and canon's own **fall** figure matches NCEI's Jasper 1 NNW **exactly** — which makes the spring figure the odd one out. ⛔ **I cannot say which is right and I am not going to guess.** What I can say: **a hand-authored number and a free reproducible one disagree by nine days, and until tonight nothing in this repo could have noticed.**
>
> **③ Hardiness validates at the flat site and diverges at the mountain — as it must.** At Bangor the derivation (**5a**) and the official ZIP answer (**5a**) agree, because Δelev is 19 ft. At Fernwood the ZIP answer (**8a**) describes a valley 11 km away and 1,400 ft down; the derivation gives **7a–7b**; canon's hand read gives **6b–7a**. ⚠️ **Derived and canon are one half-zone apart and canon is the more conservative.** For a gardening product, conservative is the right side to be wrong on — which is an argument for **surfacing the derived value as a floor-and-ceiling, not a point.**
>
> ⚠️ **And a station-choice caveat that will bite at scale.** `measured` — near the condo, **DeKalb-Peachtree (979 ft, ~8 km)** is a *better* elevation match than **Hartsfield (1,011 ft, ~19 km)**, and both are active long records. ⛔ **"Nearest" is not the selection rule; "nearest with a long record AND the smallest elevation gap" is** — and no free service ranks them for you. That ranking is the one piece of tier 2 that is genuinely ours to write.

---

## 6 · How each source fails — because a 200 carrying the wrong thing is this repo's named mode

⛔ **LOUD** = you find out. ⚠️ **SILENT** = it looks fine. All `measured` tonight.

| source | failure | loud / silent |
|---|---|---|
| ⛔⛔ **ACIS `GridData` with `"normal":"1"`** | **HTTP 200 with twelve monthly values that are not normals** (0.04″ / 0.00″ / 0.39″ where the true normals are 4–6″). The flag was accepted and something else was returned | ⚠️⚠️ **SILENT, and it would have shipped a plausible number** |
| ⛔⛔ **`phzmapi.org`** | returns **8a** for Jasper's ZIP, computed at a **centroid 11 km away and 1,400 ft lower**. Correct about the ZIP, false about the household | ⚠️⚠️ **SILENT — and it helpfully returns the coordinate it used, which is the only reason I caught it** |
| ⛔ **`api.weather.gov/points` above 4 dp** | **HTTP 301** + a `location:` header carrying the same point truncated to 4 dp. Recovers if the client follows redirects — `fetch()` does by default — but the repo concatenates raw geocoder output at `:16774` and has never met a 12-dp coordinate | ⚠️ **SILENT-ish** — invisible at Fernwood, universal at every geocoded household |
| ⛔ **Census geocoder** | address-range interpolation puts Fernwood **60 m** off; EPQS there reads **−33.9 ft** | ⚠️ **SILENT** — the same class the mapping scan measured at the condo parcel |
| **USGS EPQS in Alaska** | `resolution` switches from **metres to degrees** with no unit field | ⚠️ **SILENT** |
| **NCEI normals** | returns a real station that is **nothing like your place** (Jasper 1 NNW is 1,408 ft below Fernwood) | ⚠️ **SILENT — this is the whole reason tier 2 exists** |
| **Open-Meteo elevation** | **902.0 m at Fernwood**, no error, no flag, 86 ft wrong | ⚠️ **SILENT — and it was believed for four months** |
| **Open-Meteo rate limit** | 429 above 600/min · 5k/hr · 10k/day; the repo has already hit it (~16 walks, one IP) | ⛔ LOUD |
| ⛔ **PRISM direct** | a **whole-US ZIP** where `research-resources.md` expects a point value | ⛔ LOUD (it is a zip file) |
| ⛔ **W17 Georgia burn literal** | `(m >= 4 && m <= 8)` tells a **Maine** household Georgia's law | ⚠️⚠️ **SILENT — and `check-estate-neutral.py` cannot see it, because it tests for NAMES** |

> ⭐⭐ **THE ASSERTION SET THAT CATCHES ALL OF THEM — and it is not a status-code check.** Adapted from the mapping scan's three, plus one this domain adds:
> **(1)** did it return a value at all · **(2)** is the value **plausible for the place** (an elevation within the DEM's stated range; a frost date in the right hemisphere-season) · **(3)** ⭐ **does the response say WHERE it answered from**, and is that within tolerance of where we asked — *EPQS echoes the coordinate; ACIS echoes the cell centre and elevation; `phzmapi` echoes the centroid; NCEI names the station.* ⛔ **Every silent failure above is caught by (3), and (3) is free because all four services already volunteer it.** · **(4)** a source that cannot answer publishes **UNCHECKABLE**, never a default — the `check-public-build.py` **exit 3** convention, inherited rather than re-invented.

---

## 7 · ⭐⭐ The human-confirmable form of every derived figure `[paul-ruled 2026-09-07]`

> *"It's important about elevation — let's have the user confirm their elevation. Some of these critical figures, let's always surface it and have them confirm it as best they can."*

### 7a · The rule the probes argue for, and it is one line

> ### ⭐ CONFIRM THE INPUT, NEVER THE OUTPUT.
> **Nobody can confirm a lapse-rate-adjusted 50th-percentile freeze date, or a mean annual extreme minimum of 5.1 °F.** They *can* confirm an elevation, a pin on a map, whether they sit in a hollow, and what they have lost to frost. ⛔ **An ask a person cannot honestly answer is worse than no ask** — it manufactures a `verified` stamp on a guess, which is the one thing this repo's honesty markers exist to prevent.

**Why this is the right reading of the ruling rather than a narrowing of it:** the precedent Paul's own doctrine leans on is Mom disbelieving the rainfall number. ⭐ **She could check it because she was standing in the rain.** She could not have checked a 30-year normal. *"As best they can"* is the operative clause, and it points at inputs.

### 7b · Per figure — what shows, how it is marked, what is asked, what changes

| | shown as | unconfirmed marker | **the ask** (a person can answer this) | on **confirm** | on **correct** |
|---|---|---|---|---|---|
| ⭐ **D1 elevation** | *"About **2,873 ft**"* | the existing **`estimated — verify on-site`** idiom (`:13795`), plus the source in plain words: *"read from national lidar at the spot we placed you"* | ⭐ *"We put you here **[map pin]** at about 2,873 ft. Does that look right?"* — **the pin and the number in ONE ask**, because §4 proved they are one quantity (60 m ⇒ 34 ft) | `confidence: verified`; D3/D4 recompute; **the pin is confirmed too** | re-run EPQS at the corrected pin, or accept a typed elevation as `owner-stated` (a distinct grade — *their* claim, not ours, and not lidar) |
| **D2 reference station** | ⭐ **shown, always** — *"We compare you to **Jasper 1 NNW**, 1,408 ft below you, recording since 1937"* | it is not a guess; it is a **choice**, and a choice is disclosed rather than hedged | *"Is there a station nearer you that you'd trust more?"* — **only offer it if we can act on it**; otherwise disclose and do not ask | — | swap the station; everything downstream recomputes |
| **D3 frost dates** | *"Last frost usually around **late April**; first around **mid-October**"* ⚠️ **a WINDOW, never a date** — §5's own 9-day disagreement is the argument | *"estimated from the valley station, adjusted for your elevation"* | ⭐ *"Have you lost plants to a late frost? Roughly when?"* — **the real instrument, and it is a memory anyone gardening has** | fold as an **observation**, not a canon overwrite | ⭐ **their answer becomes an additional data point beside the derivation, never a replacement** — one year is not a normal, and saying so is the honest form |
| **D4 hardiness zone** | *"Around zone **7a–7b** here — the valley reads 8a"* ⭐ **a range, and the contrast is the content** | *"estimated from your elevation above the valley"* | *"Anything you've planted that didn't make it through a winter?"* | recorded as evidence | shifts the range, flagged as owner-evidence |
| **D5 normals** | *"September normally brings **4.18″** at the valley station"* | ⭐ **label the STATION, not the place** — the honest claim is about Jasper, not about here | ⛔ **no ask.** Nobody can confirm a 30-year normal | — | — |
| ⭐ **frost pocket / aspect** | *"If you're in a hollow, expect frost 1–4 weeks earlier"* — `property.json` already carries this prose | — | ⭐⭐ *"Is your garden in a hollow, on a slope, or in the open?"* — **the single highest-value ask on this whole list**: canon says a pocket is worth **8–15 °F**, i.e. **more than the entire 1,408 ft elevation correction**, and **no free source can derive it** | applies canon's own offsets | — |

> ⭐⭐ **THE ASK THAT BUYS THE MOST IS THE ONE NO DATA SOURCE CAN ANSWER.** Every derived figure above is worth 5–8 °F. `property.json` § microclimate.frostPockets says a hollow is worth **8–15 °F**. ⛔ **So the highest-value input in the entire weather card is a one-tap question about topography that costs nothing to ask and cannot be bought at any price.** That is the input-to-value cycle Paul named `[~11:30 ET]`, and it is the strongest single row this scan found.

### 7c · Three constraints the existing doctrine imposes on all of the above

1. **Reuse the machinery, do not invent a surface.** The confirm-card queue, the `confidence: inferred|verified` markers, and the provenance chip (*"our read from a photo"* → *"confirmed on the ground · <month>"*) already do exactly this job. ⛔ A second confirmation idiom on the weather card would be a parallel surface.
2. ⚠️ **Supply, not schema, is the risk.** `CLAUDE.md` warns it directly: `MAX_VISIBLE` is **5** and **8 cards already sit on the bench unapproved**. Six new confirmable figures is six new cards competing for five slots. ⭐ **Ship ONE ask (the pin + elevation) and let the rest render as `estimated` with no ask at all.** An unconfirmed figure honestly labelled is fine; an unanswerable queue is not.
3. **"Everything is changeable"** `[paul-stated 2026-08-04]` applies here more than anywhere: a household that confirms an elevation must be able to change it, and **that must be true, not just said** — a corrected elevation has to actually re-run D3 and D4, or the promise is a lie.

---

## 8 · ⭐⭐ The source-applicability rule `[paul-ruled 2026-09-07]`

> *"We're gonna have to build some smart checks on what sources to show. The Georgia burn ban is an example… we're in the state of Georgia so we show that; we're not in the state of Georgia, we don't. That's data we're pulling from the address."*

### 8a · The mechanism, in the vocabulary that already exists

**Three things, and only the middle one is new.**

**① `place.facts` — derived once, at geocode time, stored on the estate record.** ⭐ **Not new state — an extension of the write that already happens** (`worker.js:809` already stores lat/lon *and county FIPS*). Everything below is `measured` tonight as free and keyless:

| fact | source | Fernwood | condo | Bangor |
|---|---|---|---|---|
| `state` (USPS + FIPS) | Census | GA · 13 | GA · 13 | ME · 23 |
| `countyFips` | Census *(already stored)* | 13227 | 13121 | 23019 |
| `elevationFt` + `demResolution` | EPQS | 2,873 · 1 m | 988 · 1 m | 128 · 1 m |
| `nwsZones` (forecast · fire · county · radar · grid) | NWS | GAZ013 · GAZ013 · GAC227 · KFFC · FFC 49,122 | GAZ033 · GAC121 · KFFC | **MEZ113 · MEC019 · KGYX · CAR 66,75** |
| `refStation` (id · elev · record span) | ACIS StnMeta | JASPER 1 NNW · 1,465 · 1937– | HARTSFIELD · 1,011 · 1928– | BANGOR INTL · 147 · 1953– |
| `coastKm` (nearest NOAA water-level station) | NOAA Tides | **423** | 376 | **64** |

**② `momlib.SOURCES` — ONE registry, mirroring `momlib.DOMAINS`' shape exactly.** `DOMAINS` already proves the pattern: one dict, N readers, and `check-domains.py` stops it drifting. A source row declares `gives · gate · cors · storable · applies_when`, where **`applies_when` is a predicate over `place.facts` and NOTHING ELSE**:

```
burn-ban-state   applies_when: state in DECLARED_BURN_STATES        # {"GA"} today
tides            applies_when: coastKm < 40
usdm             applies_when: countyFips is not None               # national
frost-lapse      applies_when: refStation is not None and elevationFt is not None
nws-fire-zone    applies_when: nwsZones.fire is not None            # US only
```

**③ Three states per (source, household) — and the third is the load-bearing one.**

| state | means | renders as |
|---|---|---|
| `applies` | the predicate is true | the block |
| ⭐ **`not-applicable`** | the predicate is **false** — a *derived positive fact* | ⭐ **nothing, silently and correctly.** *"You are not on the coast"* is not news |
| ⛔ **`unknown`** | **we have no predicate for this place** | ⛔ **nothing, and it is a FINDING** — the exit-3 / `?` idiom, never a default |

> ### ⭐⭐ THE DISTINCTION THAT IS THE WHOLE RULE
> **Georgia's burn ban at a Maine household is `not-applicable`.** **Maine's own burn law at a Maine household is `unknown`.** Both render as nothing on the card and they are **completely different facts about our coverage** — one is us being right, the other is us having a hole.
>
> ⛔ **And today the code does neither: it renders GEORGIA'S LAW IN MAINE**, because the predicate does not exist at all. `viewer.template.html:19728`. That is the defect, stated in the vocabulary that fixes it.
>
> ⚠️ **`momlib.MODULE_STATES` already carries `declared-absent`, which is the same *idea* one layer up** — *"this family was never built here."* **Do not reuse the word.** A module state is **the household's or the builder's choice**; applicability is **a fact about the earth**. Collapsing them would let a hand edit to `estate.json` override a fact about where a place is, which is exactly backwards.

### 8b · Where each piece lives, and the one boundary that matters

| piece | lives in | why there |
|---|---|---|
| `place.facts` | the **estate record**, written by the geocode path | per-household, derived, and the write already exists |
| `SOURCES` + `applies_when` | ⭐ **`momlib.SOURCES`** — engine, one file | same shape and same argument as `DOMAINS`; a second copy is the named drift |
| `DECLARED_BURN_STATES` and its like | ⭐ **a data table beside the registry, not a literal in a renderer** | finding 8: there is nothing to fetch, so this **is** the source. A table can be audited, extended one state at a time, and *counted* — `(m >= 4 && m <= 8)` can do none of those |
| the check | ⭐ a `--check` in the pickup block, in the shape `check-domains.py` already has | *a capability the loop cannot reach is not a capability* (`CLAUDE.md`) |

⛔ **`estate.json`'s `modules` block is NOT where any of this goes.** That block is the household's declared switches; `place.facts` is derived and must not be hand-editable, or a typo becomes a fact about the earth.

⭐ **The falsifier for the whole mechanism, and it is cheap:** *stand up a Maine household and a coastal household and confirm the burn block renders `not-applicable`, the tide block renders `applies`, and Georgia's literal renders nowhere.* **QA already has 33 placed households.** ⚠️ `measured` — production `home` has **zero** (`read-geocodes.py`), which is the PLAN's finding ② and is upstream of everything here.

---

## 9 · Cost at household N — and the licence that outranks it

Assume tier 2 is derived **once per household and stored** (which §2c argues it should be).

| | n=1 | n=100 | n=1,000 | n=10,000 |
|---|---|---|---|---|
| ⭐ **Tier 2 derivation** — EPQS 1 + ACIS StnMeta 1 + NCEI 2 + ACIS yly-min 1 = **5 calls, once, cached forever** | $0 · 5 calls | $0 · 500 | $0 · 5,000 | **$0 · 50,000 one-time** |
| **NWS · USDM · NOAA Tides** (per load / per day) | $0 | $0 | $0 | ⚠️ $0, courtesy limits unpublished |
| ⛔ **Open-Meteo** — forecast + **25-yr archive** + elevation + AQ, **per card load** | $0 | $0 | ⚠️ **at the 10k/day ceiling** | ⛔ **over it, on a non-commercial licence** |
| **AirNow** | free key | free key | ⚠️ one key, N households | ⚠️ terms unread |

> ### ⭐⭐ THE COST FINDING IS THE MAPPING SCAN'S FINDING AGAIN, AND IT SHOULD BE SAID TWICE
>
> **Tier 2 is free at every n, permanently, because its output is five stored numbers.** ⛔ **What is not free at scale is TIER 1** — the commodity half — because **Open-Meteo's free tier is non-commercial only** and it carries four of that half's rows.
>
> ⭐ **A licensing term, not a price, is the binding constraint — exactly as the 30-day cache clause (not $0.075/call) is what removed Google Solar.** Two source scans in one day have now reached that finding independently, in unrelated domains. **It is a general rule about this product and it should be written down as one.**
>
> ⚠️ **Two aggravating facts, both `measured`:** the **25-year archive pull happens per card load** (W11), which is the single most expensive call on the card; and the **approved Open-Meteo proxy** (`BACKLOG.md` § PROXY OPEN-METEO `[paul-approved 2026-09-07]`) **concentrates every household onto one IP** against a **600/min** limit. The proxy is right for CORS and caching and **wrong for the rate limit** unless it caches aggressively. ⛔ **Not a reason to undo it — a reason to size its cache before N grows.**

---

## 10 · The three remaining axes — why they are priced differently from axis ①

**Axis ① ends here.** Everything above is *automatic*: five calls, once, no ask, no choice, no ruling. The three axes below all cost something axis ① does not.

| | what it costs that axis ① does not | the hard cap |
|---|---|---|
| **② ADVISORY** | ⭐ **a person's attention.** Every class is a thing we *ask about*, and asking is the scarcest resource this product has | ⛔ **5 slots · 8 benched · none approved · one rendered at a time** |
| **③ CIVIC** | ⚠️ **outbound precision.** Every link hands a third party something about where someone lives | ⛔ the live Wundermap defect, §12c |
| **④ EVENTS** | ⛔ **a ruling.** Something must select | ⭐ **J-e's trigger** |

---

## 11 · ⭐ AXIS ② — ADVISORY CLASSES, as ask fodder `[paul-stated 2026-09-07]`

> *"We may wanna ask whether people are interested in different pollen advisories or sun advisories, or there's anything in particular that is of interest to them related to the weather. There's probably all kinds of alerts and stuff we could pull — let's use that as fodder to ask people."*

### 11a · The inventory — probed, not recited

| class | source | gate | CORS | coverage | cadence | licence | **card-honest?** (§11b) |
|---|---|---|---|---|---|---|---|
| ⛔⛔ **Pollen / allergen** | Open-Meteo (CAMS) | G0 | ✅ | ⛔⛔ **EUROPE ONLY.** `measured`: **null at all three US points, real in Berlin** | hourly | CC BY | — |
| | **Google Pollen API** | ⛔ **G2 — billing card**, and `grep googleapis` in this repo = **0** | — | US + 65 countries (`assumption`, vendor) | daily | ⛔ display terms unread | — |
| | Ambee / Breezometer-class | G3 | — | — | — | — | — |
| ⭐ **UV index** | ⭐ **Open-Meteo `uv_index_max`** | G0 | ✅ | ⭐ **global.** `measured`: 5.15 · 7.10 · 5.95 tomorrow at the three points | hourly/daily | CC BY | ✅ **YES — a forecast, wanted the night before** |
| | ⭐ **EPA Envirofacts UV by ZIP** | ⭐ **G0, no key.** `measured`: `getEnvirofactsUVDAILY/ZIP/30143` → **UV_INDEX 9, UV_ALERT 0**; `04401` → **3** | — | US, **ZIP-keyed** ⚠️ (the `phzmapi` trap — 30143 resolved to *"Jasper"*, 04401 to *"Hampden"*, not Bangor) | daily | public domain | ✅ yes |
| ⭐ **Air quality** | Open-Meteo AQ (**modelled**) · AirNow (**measured**, G1 key) | G0 / G1 | ✅ / ⛔ | ⭐ national. `measured`: US AQI 44 · 48 · (Bangor) | hourly | CC BY / EPA | ✅ yes — ⚠️ **and the measured/modelled label is not optional here** |
| ⭐⭐ **Severe weather · fire · frost · wind · heat · flood · marine · air-stagnation** — **111 event types in ONE feed** | ⭐ **`api.weather.gov/alerts`** | **G0** | ✅ `*` | ⚠️ **US only** | continuous | ✅ public domain | ⚠️ **SPLIT — see §11b.** Watches/advisories yes; warnings **no** |
| ⭐ **Fire weather** | the same feed's *Red Flag Warning* / *Fire Weather Watch* + `fireWeatherZone` | G0 | ✅ | US | continuous | public domain | ✅ yes (watch) / ⛔ no (warning) |
| ⭐ **Drought** | USDM by FIPS | G0 | ⛔ | national. `measured`: **Penobscot D2 21.4%** vs both GA counties D0 | ⭐ **weekly** | free + attribution | ✅⭐ **ideal card content** — it changes on Thursdays |
| ⭐ **Streamflow / river level** | ⭐ **USGS Water Services** | G0 | — | ⚠️ **gauge-based.** `measured`: 4 active gauges in a 0.45°×0.40° box near Fernwood, **all 10–20 km away in the next watershed** | 15-min | public domain | ✅ yes |
| ⭐⭐ **Aurora / geomagnetic** | ⭐ **NOAA SWPC** `planetary_k_index_1m.json` | **G0** | ✅ `*` | global. `measured`: 359 records, latest **Kp 3.33** | ⭐ **1-minute** | public domain | ⚠️ **the sharpest case — see §11b** |
| **Earthquake** | USGS FDSN | G0 | ✅ | global | continuous | public domain | ✅ yes |
| **Celestial — moon · meteor showers** | NASA SVS (image by hour) · IMO calendar (**no API — annual transcription**) | G0 | ✅ | global | daily / annual | public domain | ✅ yes |
| ⛔ **Tick / mosquito / mould / burn-permit status** | — | — | — | ⛔ **no free national source found** | — | — | — |

### 11b · ⛔⛔ THE DELIVERY CONSTRAINT — stated plainly, because it disqualifies half the list

> **Fernwood is a page you open. There is no notification path, and by the site premise there cannot be one where it would matter most:** no cell reception, Wi-Fi only near the house, coverage falling off with distance. ⛔ **So an "alert" here is a CARD, and a card is only seen on the next open.**

⭐ **The load-bearing consequence, and it is a trust argument, not a technical one:** *an advisory someone opted into and did not receive in time is worse than one never offered.* Opting in is a promise. **Three classes therefore split, and the split is by the advisory's own USEFUL LIFE, not by its severity:**

| tier | useful life | classes | verdict |
|---|---|---|---|
| ✅ **CARD-HONEST** | **days to a season** — still true on the next open | ⭐ **drought · UV forecast · AQI · fire-weather WATCH · frost outlook · streamflow trend · aurora outlook · meteor showers · moon** | ⭐ **offer these.** A card is the right instrument and degrades honestly |
| ⚠️ **CARD-MARGINAL** | **hours** | heat advisory · air-stagnation · wind advisory · flood watch | ⚠️ **offer, but never call it an alert.** Copy must be *"as of when you opened this"*, with the observation time visible |
| ⛔⛔ **STRUCTURALLY REQUIRES A CHANNEL WE DO NOT HAVE** | **minutes** | ⛔ **Tornado Warning · Severe Thunderstorm Warning · Flash Flood Warning · Evacuation** | ⛔ **DO NOT OFFER. DO NOT ASK ABOUT.** Putting a life-safety warning behind *"open the app"* at a property with no cell signal is the worst thing in this entire scan |

⚠️ **And the aurora row is the one to think hardest about, because it is the most tempting.** Bortle 3 makes it genuinely valuable and SWPC updates every minute — ⛔ **which is exactly why it fails.** A Kp reading is useful for **an hour**; a card read the next morning says *"there was an aurora last night and we didn't tell you."* ⭐ **The card-honest form is the 3-day SWPC forecast, not the live Kp** — an outlook survives being read late; a nowcast does not.

### 11c · ⭐ ASK versus JUST SHOW — the discriminator the brief asked for

> ### ⭐⭐ **SHOW what is free, national and universally wanted. ASK where the ANSWER CHANGES THE CARD.**
>
> ⛔ **Not "ask about the niche things"** — that is a proxy, and it produces asks nobody can answer. The real test: *does knowing this person's answer change what we render?* If a thing renders identically whether they answered or not, asking was theatre.

| | classes | why |
|---|---|---|
| ✅ **JUST SHOW — never ask** | ⭐ **NWS watches/advisories · drought · UV · AQI · frost outlook** | free, national, keyless, and **nobody opts out of knowing there is a freeze warning**. `generateAlerts` already shows most of these. ⭐ **Asking permission to show a frost warning to a gardener is a question with one answer** |
| ⭐ **ASK — the answer genuinely changes the card** | ⭐ **pollen · aurora/dark-sky · meteor showers · streamflow · earthquakes · marine** | each is **niche, or keyed, or regional, or all three** — and each is a *whole block* that either renders or does not. ⭐ **Pollen is the strongest ask on the list precisely BECAUSE it is not free** (finding 10): the answer tells us whether it is worth paying for, which is information we cannot get any other way |
| ⛔ **NEITHER — do not offer** | ⛔ **short-fuse warnings** | §11b |

### 11d · ⭐ The FORM of the ask — recommended, Paul rules

⛔ **Eight advisory classes cannot become eight cards.** `MAX_VISIBLE` is **5**, **8 cards sit benched with none approved**, and one renders at a time. Paul has already ruled the weather opt-ins sit **beside the address at setup** (W-10), not in the queue. ⭐ **Recommended:**

1. ⭐⭐ **ONE multi-select at setup, beside the address, with ~6 checkboxes** — the ASK column of §11c and no more. It costs one screen, it is answered once, and it never enters the queue.
2. ⭐⭐ **AND THE FREE-TEXT LINE, which matters more than the checkboxes.** *"Anything else about the weather here you'd want to know?"* — the shape that produced **"Houseplants!"** on `onboard-interests-other`, and the **WHAT'S MISSING** line `read-onboarding.py` prints **first**: ⭐ *the only line where someone can name a need we never anticipated.* ⛔ **Ship the free-text even if the checkboxes are cut.** A checkbox can only return an answer we already thought of; this is the one instrument on the whole surface that can return one we did not.
3. ⚠️ **Nothing goes in the confirm queue.** Not one advisory class. The queue is for ground-truth only someone standing on the property can settle; an interest is not ground-truth.

---

## 12 · ⭐ AXIS ③ — CIVIC facts and links from an address `[paul-stated 2026-09-07]`

> *"There's probably also just good publicly available information you can pull based on the address — like the local fire department, police department, local library. Let's not limit ourselves too much."*

⛔ **This is NOT weather.** It extends `BACKLOG.md` **C7-R5** / census **D3** / `PRODUCT-ENGINE.md` § *"a domain family that does not exist yet (events, the neighbourhood)"*. ⭐ **Its starting form is already ruled** `[paul-ruled 2026-09-07, J-e]`: **start with LINKS**, because a link is **membership-by-rule** — nothing filters, so there is nothing for a model to silently drop.

### 12a · What actually falls out of an address

**TIER A — free, national, keyless, and MEMBERSHIP-BY-RULE.** `measured` unless graded.

| fact | source | Fernwood | the condo | Bangor | rule side |
|---|---|---|---|---|---|
| ⭐ **School district** | ⭐ Census `layers=all` — **already being called** | **Pickens County School District** | (Fulton) | (Penobscot) | ✅ **membership** — a polygon contains you |
| ⭐ **Congressional · state house · state senate** | same call | CD 11 · SH 11 · SS 51 | — | — | ✅ membership |
| ⭐ **County subdivision / CCD** | same call | ⭐ **Nelson-Tate-Marble Hill CCD** | — | — | ✅ membership |
| tract · block group · ZCTA · CSA · MSA · PUMA | same call | Tract 501.02 · BG 2 · 30143 · Atlanta CSA | — | — | ✅ membership |
| ⭐ **NWS forecast office · zones · radar** | `api.weather.gov` | **FFC** · GAZ013 · KFFC | FFC · GAZ033 | ⭐ **CAR (Caribou)** · MEZ113 · **KGYX** | ✅ membership |
| ⭐ **County Extension office** | ⛔ **NO API EXISTS.** `measured` (search): NIFA publishes a **state-level land-grant directory**; county offices live on 50 per-state sites | UGA Extension, Pickens County | UGA, Fulton | UMaine, Penobscot | ✅ membership — ⭐ **via a 50-row table, exactly like §8's burn-ban table. Second instance of the same mechanism** |

> ⭐⭐ **THE EXTENSION ROW IS THE BEST CIVIC LINK ON THIS PAGE AND IT IS NOT CLOSE.** For a product whose entire record is plants, **the land-grant Cooperative Extension office is the most on-point civic institution in the United States** — free soil tests, a county agent who answers plant questions, and the exact authority `property.json`'s soil section is currently guessing at. ⛔ **And it needs no fetch:** state → land-grant URL is **50 rows**, county office is one more level. ⭐ **A table, not a feed** — which is the same conclusion §8 reached for burn bans and is starting to look like a general shape for civic content.

**TIER B — free, but density-dependent.**

| fact | source | gate | the measured problem |
|---|---|---|---|
| ⭐ **Library · fire station · police · town hall · community centre** | ⭐ **OpenStreetMap / Overpass** | G0 | ⛔⛔ **finding 12.** Within 8 km: **97** at the condo, 24 at Bangor, **0 at Fernwood**. At 15 km Fernwood returns 7 fire stations, 3 police, 1 library. ⚠️ ODbL — attribution attaches |
| **Wildfire · medical-response structures** | NAPSG / NIFC ArcGIS open data | G0 | `measured`: the catalogue lists 82 fire-related services (`USA_Wildfires_v1`, `Structures_Medical_Emergency_Response_v1`) |
| **Fire department jurisdiction boundaries** | ⭐ **NERIS** (USFA + FSRI + NAPSG), >30,000 departments | G0 (`inferred` — read from its own docs, ⛔ **not probed**) | ⭐ **the one national fire-jurisdiction layer found.** If it holds up, it converts fire from tier B (nearest-N) to tier A (**membership**) |
| **Electric utility territory** | HIFLD Electric Retail Service Territories | G0 | ⛔ **endpoint not found tonight** — my guessed service id returned `Invalid URL`. ⚠️ *not found* ≠ *does not exist* |
| ⛔ **Police jurisdiction · waste/recycling · polling place** | — | — | ⛔ **no free national source found.** All three are municipal, and municipal is the patchiest tier in the US |

### 12b · ⭐⭐ The finding that matters most on this axis: a RADIUS is the wrong primitive

> **The same 8 km query returns 97 civic features at the condo and `{}` at Fernwood.** Any radius you pick is wrong at one of the two households, and it fails **silently** — HTTP 200, valid JSON, empty array, indistinguishable from *"we didn't ask."*
>
> ⭐ **The correct primitive is JURISDICTION, not proximity.** *Your* fire department is the one whose district contains you, not the nearest three. *Your* library is the system your address belongs to. *Your* Extension office is your county's. ⭐⭐ **Every tier-A row above is a containment test with exactly one answer — which is why axis ③ needs no AI ruling at all, and axis ④ does.**
>
> ⛔ **And it is the whole argument against "nearest N":** the moment you rank by distance you have selected, and at 25 libraries within 8 km you have selected a lot.

### 12c · ⛔ PRIVACY — a live defect, so this is a constraint and not a note

`CLAUDE.md` and `property.json` record it: the **Wundermap** link on the property card hands a third party **the household's coordinates**, undisclosed, on a screen where the Google link *does* disclose. **Security is a stated selling point of this product.**

> ### ⭐ THE RULE: NEVER SEND MORE PRECISION THAN THE LOOKUP NEEDS.
> **A library serves a town. A school district is a polygon. An Extension office is a county. None of them needs a point.**

| link class | precision it actually needs | what the third party learns |
|---|---|---|
| Extension · school district · county services | ⭐ **county name.** No coordinate at all | the county |
| Library · fire · police | ⭐ **town / ZIP** | the town |
| NWS office · zone page | ⭐ **the zone id** (GAZ013) — already public, already coarse | the zone |
| ⛔ Wundermap / any map deep-link | ⛔ **currently 11 dp** | ⛔ **the house** |

⭐ **Two cheap moves:** round every outbound coordinate to **2–3 dp** (~1 km) unless the link's purpose *is* the point; and **disclose on every outbound link, not just the ones we remembered** — the inconsistency is what makes the current state a defect rather than a choice.

### 12d · ⚠️ ALTITUDE — where durable content goes, and it may not be this card

**C7-R5's measured defect:** Pickens-County events render at a **Midtown** address, **at the bottom of the location card**, *"violating our rules about getting the freshest data near the top."*

⭐ **A civic link is DURABLE — it is the same next year.** Under `CLAUDE.md`'s governing principle (**freshness sets altitude**), durable content belongs in **the repository layer, not the glance**. ⛔ **So the honest recommendation is that civic links do not belong on the weather card at all**, and probably not near the top of the place card either: they are *reference*, and reference is what the parent card holds on demand. ⚠️ **The exception is when a durable link becomes situationally fresh** — the Extension office beside a soil question, the fire district beside a Red Flag Warning. ⭐ **That is a placement question for `ux-expert`, and this file only names the constraint.**

### 12e · ASK versus JUST SHOW

| | why |
|---|---|
| ✅ **JUST SHOW** — Extension · school district · NWS office · county services | derived by rule, one right answer, no preference involved. ⛔ **Asking "would you like to know your county Extension office?" is asking someone to predict whether they will want a thing they have not seen** |
| ⭐ **ASK** — *"anything local you'd want on hand here?"* as **free text**, once | ⭐ same instrument as §11d·2 and it should be **the same field**. The value is not in the checkbox; it is in the household naming a thing we never listed |

---

### 12f · ⭐⭐ A CLASS WITHIN THIS AXIS — interest-aligned local organisations `[paul-stated 2026-09-07]`

> *"Certainly local neighborhood associations — not necessarily the HOA — but local conservancies, organizations, especially that may line up with the interest of the user."*

⭐ **Why this class is different from fire, police and library.** Those are decided by **jurisdiction alone**. This one is decided by **jurisdiction JOINED TO THE HOUSEHOLD'S OWN DECLARED INTERESTS** — and the join is what puts it on either side of J-e's line:

| build | is it selection? |
|---|---|
| ✅ *"Show land-trust and native-plant links **because this household ranked Gardening**"* | ⭐ **NO — a JOIN on their own answer.** Deterministic, membership-by-rule, **no ruling needed** |
| ⛔ *"The most relevant local organizations for you"* | ⛔ **YES — selection.** Needs the order-not-membership ruling first |

> ⭐ **Same data, two builds, opposite sides of the line — and the cheap version is the safe one.** ⛔ **That is the operative sentence of this section.** The join costs a `WHERE` clause; the ranking costs a doctrine ruling.

**⭐ THE REPO ALREADY DID THIS ONCE AND NOBODY CONNECTED IT.** `research-resources.md` § Category 6 already inventories the **Atlanta Astronomy Club** (*"the nearest organized astronomy community for a Pickens County stargazer"*), **DarkSky International** and **Deerlick Astronomy Village**, and sites them as *"Property card → **Community** link list · depth tier: deep-dive link"* — for an interest **Fernwood genuinely has** (Bortle 3). ⭐ **The class, the siting and the depth tier were all proposed by this repo's own research, months ago, for one interest.** This section is that pattern generalised, not a new taxonomy.

#### The discoverability probe — and it is the most interesting negative in the file

⭐ **There IS a federal, free, national, purpose-classified registry, and I probed it.** The **IRS Exempt Organizations Business Master File**, reachable two ways:

| route | gate | CORS | what it gives |
|---|---|---|---|
| ⭐ **ProPublica Nonprofit Explorer API** `projects.propublica.org/nonprofits/api/v2` | **G0 — keyless** | ⛔ none — server-side | name · **NTEE code** · full address + **ZIP** · EIN · filings |
| **IRS BMF bulk CSV** `irs.gov/pub/irs-soi/eo1.csv` | **G0** | — | `measured`: **HTTP 200, `text/csv`**. The whole file, hostable, joinable on ZIP |

**What it returned — `measured`, eight queries across two states:**

| query | result |
|---|---|
| GA · land trust (NTEE grp 3) | 15 — *Athens Land Trust · St Simons · Ocmulgee · Cobb · Oconee River* |
| ⭐ **ME · land trust** | **30 — including `Bangor Land Trust`, NTEE C34, Bangor 04402** — ⭐ the household's own town, found by purpose + state |
| GA · native plant | 11 — *Georgia Native Plant Society* + **four regional chapters** |
| GA · riverkeeper | 6 — *Chattahoochee · Flint · Ogeechee-Canoochee · Savannah · Altamaha*, all NTEE C32 |
| GA · master gardener | 13 — *Georgia Master Gardener Association*, **Cherokee County**, Gwinnett, Fayette |
| GA · astronomy | **2** — *Atlanta Astronomy Club Inc* |
| ME · astronomy | 1 — *Astronomy Institute of Maine* |

> ### ⚠️⚠️ AND THE DEFECT, WHICH IS SILENT AND LANDS ON THIS REPO'S OWN EXAMPLE
>
> **`Atlanta Astronomy Club Inc | NTEE None`.** ⛔ **The single organisation `research-resources.md` already names has no NTEE code at all** — so a query filtered on purpose, which is the entire reason to use this source, **would miss it.**
>
> **It is not an isolated row.** `Brewer Land Trust` is **C32** (water) while `Holden Land Trust` next door is **C34** (land); `Cherokee County Master Gardener` is **B90** (education) while every other master-gardener group is **C42**. ⭐ **The registry is national and free, and its classification — the one field that makes it useful — is missing or inconsistent on the very examples we care about.**
>
> ⛔ **A second silent failure, measured:** searching GA for *"jasper historical"* returns **`Jasper County Historical Foundation Inc, Monticello`** — **Jasper County, 100+ miles away**, not Jasper *city* in Pickens County. **A name search on a household's town returns a plausible, well-formed, wrong organisation.** Same shape as `phzmapi` (§6) and the Pickens-AL/Pickens-SC hit in the mapping scan. ⭐ **Third occurrence of "right name, wrong place" in two scans.**
>
> ⚠️ **Two more honest limits.** ProPublica filters no finer than **STATE** — county proximity is a client-side join on city/ZIP, which is what the **bulk BMF** is for. And the address is often a **PO Box** (`Bangor Land Trust → PO BOX 288`): fine for *which town*, ⛔ **useless for proximity.**

#### ⚠️ The property-owners' association is a separate, lower-value case — and Paul said so

*"Not necessarily the HOA."* Three reasons that instruction is right and should be honoured rather than softened:
1. ⛔ **It is not interest-aligned — it is compulsory.** A household does not *choose* its POA, so the join that makes this class valuable does not apply.
2. ⚠️ **It is the most privacy-loaded link on the page.** A named POA plus a coordinate identifies a small set of houses; a state native-plant society identifies nothing. §12c binds hardest here.
3. ⛔ **It is the least discoverable.** Many have no web presence, no EIN filing, and no registry entry — and the boundary file already records a **live defect found on a neighbourhood association's own website** during the 09-07 probes.

⭐ **Fernwood's own case makes the distinction concrete:** *Tate Mountain Estates* is the surrounding development — that is a POA-shaped fact. *Land trusts, riverkeepers, the Georgia Native Plant Society and the Atlanta Astronomy Club* are interest-shaped. **Only the second set gets better as we learn more about the household.**

#### ⭐ The join key — and it should not be the onboarding answer alone

The declared ranking exists as **`READER_RANKING`** from the onboarding tap-order step. ⚠️ **But Paul ruled tonight (GL-1) that behaviour may override a declared ranking**, and this repo has the receipts: every ask-shaped affordance ran **0-for-35** while the one that simply moved her ran **5-for-5**, and the zones session's *"she does not need retrieval"* was falsified by one sentence from Paul.

> ⭐ **RECOMMEND the join key be `momlib.DOMAINS`' `group` — the ACTION axis — not the onboarding tap order.** A household with plants in its record `tends`; that is a fact about the record, not a claim about a preference, and **it is already the repo's own organising axis.** ⭐ **Then `READER_RANKING` and behaviour are two additional inputs that can only ADD a category, never remove one** — the same one-way shape as the engagement gate, which may raise ARMED→FIRED and may never quiet a fired loop.
>
> ⛔ **Why one-way matters:** removing a link because someone did not tap something is **selection by inference**, and it fails silently — the household never learns what they were not shown. Adding one is membership-by-rule.

#### Siting and freshness — ⭐ `research-resources.md`'s call still holds

**Confirm.** These are **durable**, like every other axis-③ link and unlike events. ⭐ **Property card → a "Community" link list, depth tier deep-dive** is the right answer and was the right answer when it was written. ⛔ **Not the weather card.** ⚠️ **One amendment:** the list should be **grouped by the interest that admitted it** (*"Because there are plants here: …"*), because that is what makes the join legible to the household and keeps it honestly membership-by-rule rather than a mysterious curated list.

---

## 13 · ⭐⭐ AXIS ④ — EVENTS, and the boundary it makes live

⛔ **I am NOT ruling this boundary.** `.plans/2026-09-07-place-card-AI-BOUNDARY.md` (ai-advisor, stage `concept`, unstamped) already scopes it — its §0 table rows **8, 9, 13, 14** and rulings **R2/R3** are the artifact. ⭐ **This section says only what tonight's measurements mean FOR it.**

### 13a · ⛔ The source reality — a clear negative, stated early as asked

| | state |
|---|---|
| **Free, national, licence-clean events feed** | ⛔⛔ **DOES NOT EXIST.** The boundary file establishes it: *"Eventbrite killed public Event Search in Feb 2020 and has not replaced it."* Nothing tonight contradicts it |
| **Ticketed events at real venues** | **Ticketmaster Discovery API — G1**, free key, `geoPoint` + `radius`, **5,000 calls/day, 5 req/sec** (from the boundary file, `inferred`, ⛔ not probed tonight — probing would have required a key) |
| **Park / civic / library / church events** | ⛔ **per-venue ICS · RSS · JSON, curated per household.** A **RESEARCH row**, the same class as `droughtFips` and `streamGauge.site` — things nobody pretended a model could derive |
| **City/community calendars** | ⛔ per-city; Localist-class aggregators are **G3 and display-bound** |
| ⭐ **The consequence** | **This is a decision about spending and curation, not a build.** ⛔ It should be priced that way before anyone scopes it |

### 13b · ⭐⭐ Where selection enters — named concretely, which is what the ruling turns on

| candidate source | returns | **rule or judgement?** |
|---|---|---|
| **A curated per-household ICS/RSS register** | ⭐ **a bounded set** — *these six feeds, chronological* | ✅ **RULE.** Membership is decided when the feed is registered, by a human. Ordering is by date, which is not a judgement |
| **NERIS / school district / Extension** (axis ③) | **one answer** | ✅ **RULE** — containment |
| ⛔ **Ticketmaster by radius** | ⛔ **more than fits.** A 25-mile radius around Midtown returns hundreds | ⛔⛔ **JUDGEMENT.** Something must rank, and ranking is J-e's trigger |
| ⛔ **"Events near you" from any aggregator** | ⛔ unbounded | ⛔ **JUDGEMENT** |
| ⚠️ **A household's own interest answers filtering a bounded register** | *"live music"* over six registered feeds | ⭐⭐ **RULE — and this is the design that avoids the ruling entirely.** Deterministic filtering of a set a human authored is `membership-by-rule` twice over |

> ### ⭐⭐ THE CONTRIBUTION THIS SCAN MAKES TO R2, AND IT IS FROM MEASUREMENT
>
> **Selection is forced by DENSITY, and finding 12 measured the density.** At the condo, 8 km holds **97** civic features and an unbounded events supply — *something must choose.* At Fernwood, 8 km holds **zero** — *there is nothing to choose from.*
>
> ⭐ **So the AI-boundary question is not a question about the product. It is a question about URBAN households**, and it becomes live at exactly one place in this portfolio: **the condo**. ⛔ **Which is the household C7-R5 currently serves worst** — Pickens-County events, at a Midtown address, at the bottom of the card. **Wrong content, wrong place, wrong altitude, at the one household the feature is for.**
>
> ⭐ **And it points at a cheaper path than the ruling:** ⛔ **a bounded, human-registered feed set never triggers J-e at all.** *Ranking is only needed when the supply is unbounded, and the supply is only unbounded if we choose an unbounded source.* **Choosing curation over aggregation is the deterministic option, and it is available.** ⚠️ It costs per-household research — which is a real cost and is exactly what §13a says should be priced.

### 13c · ⭐ Freshness and altitude — yes, events are the exception

**Confirmed, and it is the one place in this whole scan where content earns the top.** Under **freshness sets altitude**, an event has the shortest useful life of anything here: it **expires**. ⭐ **So dated, near-horizon events are the only axis-③/④ content with a legitimate claim on the glance** — and C7-R5's *"move fresh, dated content up"* is right.

⚠️ **Two conditions, both from this repo's own record:**
1. ⛔ **An expired event must vanish, not grey out.** *"It's better to not display something rather than display something that's empty"* `[captured 2026-09-04]`. An events block with nothing upcoming is **hidden**, not rendered hollow — and at Fernwood, with zero civic features in 8 km, **hidden is the normal state**.
2. ⚠️ **It must be gated by module/instance** — C7-R5's first fix. **Canon that no module gates is how Pickens events reached Midtown**, and it is the same defect class as the Georgia burn literal (§8) and Fernwood's gauge rendering in Bangor.

### 13d · The ask, and whether it shares a form with axis ②

⭐ **RECOMMEND: ONE form at setup, three groups, one free-text line.** Paul ruled the weather opt-ins sit beside the address (W-10); event kinds are the **same multi-select shape** and adding a second setup surface for them would be a parallel ask path.

```
While we're setting up <place>:
  Weather & sky      [ ] pollen  [ ] dark sky / aurora  [ ] meteor showers
                     [ ] river & stream levels  [ ] earthquakes
  Around here        [ ] live music  [ ] festivals & markets  [ ] sports
                     [ ] civic meetings  [ ] library & talks
  ⭐ Anything else you'd want to know about this place?   [______________]
```

⛔ **None of this enters the confirm queue.** 5 slots, 8 benched, one rendered at a time — unchanged and binding. ⚠️ **And an interest answer must not silently become a promise:** ticking *"live music"* at a household where no feed is registered has to render as **nothing**, honestly, per §13c·1 — ⭐ **or better, as the one place a household can tell us the feed:** *"we don't have a music listing for your area yet."* That converts an empty promise into an ask, which is the input-to-value cycle working.

---
## 14 · ⭐ Recommendation — one v1 per axis, and what each defers

⛔ **Agent-proposed. Paul rules.** ⭐ **Four axes, four different verdicts — which is the argument for having kept them apart.**

### 14a · AXIS ① DERIVED ANALYSIS — **BUILD IT.** Two rows, five calls, one ask

**① D1 · elevation from EPQS.** ⭐ **The highest value-to-cost row in this entire scan.** One keyless CORS-enabled call; 1 m national across 8 of 9 probes; **reproduces this repo's hand-measured lidar figure to 0.3 ft**; and it retires an error the repo already paid for once. Replaces Open-Meteo's elevation everywhere.

**② D2 + D3 + D4 · reference station, frost window, hardiness range.** Four more keyless calls, computed once, stored forever. ⭐ **It unblocks something already broken:** `generateAlerts`' frost rule reads hand-authored `frostDates`, so **today every new household silently gets no frost warning at all.** Rendered as **windows and ranges, never dates and points** — §5's own 9-day disagreement is the evidence.

**③ ONE ask: the pin + the elevation together** (§7b), and only one (§7c·2).

⭐ **Non-negotiable and free:** store **the source, the station, the cell and the derivation date** with every figure — §6's assertion (3) is only possible if we keep what the service told us about *where it answered from*.

⛔ **Defers:** PRISM point normals (no free point service — reach it via ACIS grid 21, whose cell is **235 ft** below the property) · keyless AQI (trades **measured for modelled**; a content decision) · burn-ban beyond `not-applicable` outside GA · terrain horizon (EPQS would cost **1,000+ calls**) · station ranking better than nearest-long-record · the ~24% bias (tier 3′, needs a device and time).

### 14b · AXIS ② ADVISORY — **ASK, don't build.** One multi-select and one free-text line

⭐ **Ship the ask before any advisory source.** Six checkboxes and a free-text line beside the address at setup (W-10), **nothing in the confirm queue.** ⛔ **The free-text line is the one to protect if anything is cut** — it is the only instrument that can return a need we never listed, and it has already produced one (*"Houseplants!"*).

⛔ **And two hard stops, stated as stops:** **do not offer short-fuse warnings** — a tornado warning behind *"open the app"* at a property with no cell signal is the worst idea in this scan (§11b); and **do not offer live aurora** — offer the **3-day outlook**, because a nowcast read the next morning is a card that says *we knew and didn't tell you*.

⛔ **Defers:** pollen itself — **no free US source exists**, so the ask is how we learn whether it is worth a Google billing account. **The ask precedes the spend, which is the right order and is only visible because the probe returned null.**

### 14c · AXIS ③ CIVIC — **SHOW the four that are membership-by-rule.** Read the call we already make

⭐ **Zero new sources.** `worker.js:809` already calls the Census geocoder; adding `layers=all` returns **school district, congressional and legislative districts, county subdivision, tract, CSA** — and the code reads two fields of seventeen. ⭐ **Plus the one table worth writing: state → land-grant Extension office**, 50 rows, the most on-point civic institution in the US for a product whose record is plants.

⭐ **And within it, `12f`'s cheap build:** interest-aligned organisations as a **JOIN on `momlib.DOMAINS`' `group`**, one-way (a signal may add a category, never remove one), sited on the **Property card → Community list** exactly where `research-resources.md` already put it. ⛔ **Never as "most relevant for you"** — same data, and that version needs the ruling.

⛔ **Defers:** OSM civic amenities (a radius is the wrong primitive — §12b) · NERIS fire jurisdiction (⛔ **not probed**; if it holds it converts fire from nearest-N to membership) · electric utility (endpoint not found) · police, waste, polling (no free national source) · the POA (§12f — lower value, higher privacy load, and Paul said so).

⚠️ **One thing to fix regardless:** §12c's outbound-precision rule. Round outbound coordinates to **2–3 dp** and **disclose on every outbound link**. The Wundermap 11-dp handoff is a live defect on a product whose selling point is security, and the inconsistency is what makes it a defect rather than a choice.

### 14d · AXIS ④ EVENTS — ⛔ **DO NOT BUILD. Price it, then decide.**

⛔ **There is no free, national, licence-clean events source.** Every path is a **spend or a curation cost**, and this scan's only contribution to the ruling is that **selection is forced by density, density lives at the condo, and a bounded human-registered feed set avoids J-e's trigger entirely.**

⭐ **The one thing worth doing now costs nothing:** **C7-R5's gate.** Pickens-County events rendering at a Midtown address is the same defect class as the Georgia burn literal and Fernwood's gauge in Bangor — **canon that no module gates.** ⛔ **Fixing the leak is not the same as building the feature, and only the first is free.**

⛔ **Defers:** the ruling itself (`.plans/2026-09-07-place-card-AI-BOUNDARY.md` R2/R3, Paul's) · Ticketmaster (G1, and it is the *unbounded* option) · per-household feed registers (a real per-household research cost).

### 14e · ⚠️ Two things to look at before the lap opens, not during

1. ⛔ **The 4-decimal-place 301** (finding 3). Two characters (`.toFixed(4)`) at `:16774` and `:20244`. Invisible at Fernwood, present at **every geocoded household**. ⭐ **Not this file's to make** — but it is the cheapest thing on this page.
2. ⛔ **Open-Meteo's non-commercial licence** (finding 6). It touches the whole card, not just tier 2, and it is a **Paul question, not an engineering one.**

---

## 15 · What is critical WITHIN this lane

⛔ **I do not rank across lanes and I decide nothing. Paul ranks** `[paul-ruled 2026-09-07, J-b]`. Within *sources reachable from an address*, with evidence:

1. ⭐⭐ **EPQS.** Free, keyless, CORS, national at 1 m, and **verified against the one number this repo measured by hand.** Retires an 86 ft error in one call. *§4.*
2. ⭐⭐ **The frost/hardiness derivation is real** — it reproduced canon's fall date exactly, while exposing that canon's **spring** date and the free record disagree by nine days. *§5.*
3. ⭐⭐ **Three probes returned a well-formed 200 carrying the wrong thing, and one of them is the first thing Paul named.** Pollen null in the US and real in Berlin · ACIS's `normal` flag · `phzmapi`'s ZIP centroid · *"Jasper historical"* landing 100 miles away. ⭐ **All four are caught by one free assertion: does the response say WHERE it answered from.** *§6, §11a, §12f.*
4. ⭐⭐ **A fixed radius is the wrong primitive, measured: 97 civic features at the condo, `{}` at Fernwood.** Jurisdiction is the right one — and that is also why axis ③ needs no ruling and axis ④ does. *§12b.*
5. ⭐ **Selection is forced by DENSITY, and density is the condo's** — which is the household C7-R5 serves worst today. ⭐ **And a bounded, human-registered feed set never triggers J-e at all.** *§13b.*
6. ⭐ **Confirm the input, never the output — and the highest-value input is "are you in a hollow,"** which no source can supply and canon prices at **8–15 °F**, more than the entire 1,408 ft elevation correction. *§7.*
7. ⭐ **The interest-join is the cheap build AND the safe one.** Same data as *"most relevant for you"*, opposite side of the line, and `research-resources.md` already sited it. ⛔ **Its federal registry is national and free and its purpose codes are missing on this repo's own example.** *§12f.*
8. ⚠️ **Open-Meteo's non-commercial free tier is the binding constraint on the whole card** — a licence, not a price. Second independent occurrence of that shape today. *§9.*
9. ⛔ **Do not offer short-fuse warnings at a property with no cell signal.** *§11b.*

⛔ **Not proposed, deliberately:** no `BACKLOG.md` row, no tool, no schema change, no key, no purchase, no household-facing copy, **and no AI-boundary ruling** — that is `.plans/2026-09-07-place-card-AI-BOUNDARY.md`'s and Paul's. **The measurements are the deliverable.**

---

## Probes run — free, unauthenticated, read-only, zero cost, 2026-09-07

⛔ **The Midtown condo's coordinates are NOT written into this file**, per `.private/condo-location.md`. Bangor is an arbitrary street address used as a probe point, not a household.

| # | probe | result |
|---|---|---|
| 1–3 | **Census geocoder**, three addresses | Fernwood 34.549318,−84.367964 · Pickens **13227** · Fulton **13121** · Penobscot **23019** |
| 4–7 | ⭐ **USGS EPQS** — Fernwood canon · Fernwood geocoded · condo · Bangor | **2,873.28** · **2,839.41** · 987.79 · 127.80 ft; all `resolution: 1` |
| 8–12 | **EPQS** — rural NV · Fairbanks · Hilo · Leadville · New Orleans · W Texas | 1 m everywhere but **Alaska** (resolution in **degrees**); Leadville **10,155.7 ft** |
| 13 | **Open-Meteo elevation**, four points | **902.0 m** at Fernwood (the documented +86 ft), 893 · 309 · 40 m |
| 14 | ⭐ **ACIS `GridData` grid 21 (PRISM)** at Fernwood | cell 34.5417,−84.375 · **elev 2,638 ft** |
| 15 | ⭐ **ACIS `GridData` grid 1 (NRCC)** at Fernwood | cell **elev 1,854 ft** |
| 16 | ⭐ **ACIS `StnMeta`** near Fernwood | **JASPER 1 NNW `USC00094648`, 1,465 ft, 1937-06-01 → 2026-09-07** |
| 17–18 | **ACIS `StnMeta`** near condo · Bangor | 44 stations / 4 active long records · 16 stations / **BANGOR INTL 147 ft** |
| 19 | ⭐ **NCEI Access Data Service** — monthly normals, Jasper 1 NNW | Jan Tmin 31.1 / Tmax 47.5 / 5.53″ … Sep 4.18″. **No token** |
| 20–22 | ⭐ **NCEI** — frost/freeze normals, Jasper · Atlanta · Bangor | T36 **04/14 · 10/27**, GSL 196 · T36 03/29 · 11/07 · T36 05/17 · 09/25 |
| 23–25 | ⭐ **ACIS `StnData` yly-min 1991–2020** — mean annual extreme minimum | **+10.0 °F** · **+15.2 °F** · **−16.9 °F**, 30 years each |
| 26–34 | ⭐ **CORS headers**, nine services | `*` on EPQS · NWS · NCEI · ACIS · Open-Meteo ×2 · NOAA Tides; **none** on USDM · Census |
| 35–37 | **`api.weather.gov/points`**, three addresses | Fernwood 200; ⭐ **condo and Bangor 301** (`location:` at 4 dp); zones/radar recovered on redirect |
| 38 | **`api.weather.gov/alerts/active?point=`** at 12 dp | **200** — the alerts path does *not* 301 |
| 39–41 | **NWS gridpoint elevation** | 900.07 m · 267.92 m · 39.93 m |
| 42–44 | ⭐ **US Drought Monitor by FIPS** | Pickens **D0 100%** · Fulton **D0 100%** · **Penobscot D1 100% / D2 21.4%** |
| 45 | ⭐ **Open-Meteo Air Quality** (keyless), three points | US AQI 44 · 48 · (Bangor returned); **no key** |
| 46–48 | ⛔ **`phzmapi.org`** 30143 · 30308 · 04401 | **8a** (centroid 34.4549,−84.4158) · 8a · **5a** |
| 49 | ⛔ **PRISM `services.nacse.org/prism/data/get/us/800m/ppt/<date>`** | **`Content-Type: application/zip`**, `prism_ppt_us_30s_<date>.zip` |
| 50 | ⛔ **USDA PHZM `/api/zone?lat&lon`** | HTML, no JSON API |
| 51 | **NOAA Tides & Currents** station list | 302 stations; nearest **423 km** · 376 km · **64 km** |
| 52 | **Open-Meteo archive (ERA5)** at Bangor, 2001 | 365 days, 730.9 mm — the 25-yr baseline path works outside Georgia |
| 53 | ⛔ **ACIS `GridData` with `"normal":"1"`** | **200 carrying non-normals** — §6 |
| | ***— axis ② advisory —*** | |
| 54–56 | ⛔⛔ **Open-Meteo POLLEN**, three US points | **200 with `null` for all six species at all three** |
| 57 | ⭐ **Same query, Berlin — the positive control** | **`grass_pollen 0.1` · `ragweed_pollen 0.7`** → **the layer is Europe-only** |
| 58 | ⭐ **Open-Meteo `uv_index_max`**, three points | 5.15 · 7.10 · 5.95 (tomorrow) |
| 59–60 | ⭐ **EPA Envirofacts UV by ZIP** (keyless) | 30143 → **UV 9, alert 0, "Jasper"**; 04401 → **UV 3, "Hampden"** ⚠️ (not Bangor) |
| 61 | ⭐ **`api.weather.gov/alerts/types`** | ⭐ **111 event types in one feed** |
| 62–63 | **`/alerts/active?area=`** GA · ME | 2 (both *Rip Current Statement*) · 0 |
| 64 | ⭐ **NOAA SWPC `planetary_k_index_1m.json`** | 359 records, latest **Kp 3.33**; CORS `*` |
| 65 | **USGS Water Services** bbox near Fernwood | 4 active stream gauges, **all 10–20 km away, next watershed** |
| | ***— axis ③ civic —*** | |
| 66 | ⭐⭐ **Census geocoder `layers=all`**, Fernwood | ⭐ **17 geographies** — school district, CD 11, SH 11, SS 51, **Nelson-Tate-Marble Hill CCD**, tract, CSA, MSA, ZCTA |
| 67–69 | ⭐⭐ **OSM Overpass**, civic amenities within **8 km** | ⛔ **Fernwood `{}`** · Bangor **24** · condo **97** (25 libraries · 25 fire · 22 police) |
| 70–71 | **Overpass at Fernwood, 15 km / 25 km** | 7 → 19 fire stations, 1 → 3 libraries (*Talking Rock VFD · Pickens Fire Rescue 11 · Tate FD*) |
| 72 | **NAPSG open-data catalogue** | 82 fire-related feature services (`USA_Wildfires_v1`, medical-response structures) |
| 73 | ⛔ **HIFLD electric service territory** (guessed id) | `Invalid URL` — **endpoint not found** |
| | ***— axis ③ · interest-aligned organisations (12f) —*** | |
| 74–81 | ⭐⭐ **ProPublica Nonprofit Explorer** (keyless), 8 queries | GA land trust **15** · **ME land trust 30 incl. `Bangor Land Trust` C34** · GA native plant **11** · riverkeeper **6** · master gardener **13** · GA astronomy **2** · ME astronomy 1 · ⛔ *"jasper historical"* → **Monticello, 100 mi away** |
| 82 | ⚠️ **Org detail, Bangor Land Trust** | full address + ZIP `04402-0288`; ⚠️ **a PO Box**; NTEE `C34` |
| 83 | ⛔ **`Atlanta Astronomy Club Inc`** — this repo's own named example | **`ntee_code: None`** — invisible to a purpose-filtered query |
| 84 | **IRS EO BMF bulk** `irs.gov/pub/irs-soi/eo1.csv` | **HTTP 200, `text/csv`** — free, hostable, joinable on ZIP |

⛔ **No paid call, no account created, no key created, no credential written, no tracked file edited but this one.** ⛔ **Axis ④ was probed with ZERO calls** — every candidate is key-gated or commercial, and probing would have required creating a credential.

## Could not reach

| source | why | what it would have settled |
|---|---|---|
| **ACIS terms of use / rate limit** | `docs.rcc-acis.org` publishes none | whether a product may lean on it at N. ⚠️ **A free service with no stated contract is a real risk, not a free lunch** |
| **NCEI Access Data Service licence page** | not fetched; federal public-domain status is `assumption` | redistribution rights in a stored derivation |
| **Official USDA PHZM point service** | no public JSON endpoint found | whether the authoritative zone is reachable. ⚠️ *not found* ≠ *does not exist* |
| **AirNow terms for a multi-household product** | key-gated | whether one engine key may serve N households |
| **RainViewer / Esri tile terms at N** | already flagged unverified in the archaeology | tier 3ⓐ, not tier 2 |
| **Any free national burn-restriction API** | search only; all hits commercial | finding 8's strength — it is *not found*, not *proven absent* |
| ⛔ **Google Pollen API** | **G2 — requires a Google Cloud project with a billing card**, and this repo holds **zero** `googleapis` references | ⭐ **whether US pollen exists at these addresses at all, and at what quality.** The single most consequential unprobed thing on axis ② |
| ⛔ **Ticketmaster Discovery API** | **G1 — needs a key** | axis ④'s only concrete supply. Figures cited from `.plans/2026-09-07-place-card-AI-BOUNDARY.md`, ⛔ **not probed tonight** |
| ⭐ **NERIS fire-department jurisdiction layer** | found by search, **service endpoint not located** | ⭐ whether fire converts from *nearest-N* (judgement) to *membership* (rule). **The highest-value unreached probe on axis ③** |
| **HIFLD electric service territories** | my guessed ArcGIS id returned `Invalid URL` | who supplies power at an address |
| **IMLS Public Library Survey locations** | not probed | a national library layer better than OSM |
| **Cooperative Extension county-office lookup** | ⛔ **no API exists** — NIFA publishes a state-level directory; county offices live on 50 per-state sites | confirms §12a: it is a **table**, not a feed |
| **ProPublica CORS / rate limit / terms** | no header returned, no terms page read | whether it may be called at N, or whether the **bulk BMF** is the only durable route |

## What I did not verify

- ⛔ **I built nothing and ran no code in this repo.** Every derivation in §5 is arithmetic I did by hand over probe outputs; **no tool computed it and none was written.**
- **Which of canon's April 23 and NCEI's 04/14 is correct.** ⛔ **I state the disagreement and refuse the guess.**
- **Canon's `officialZone: 7b` against tonight's ZIP read of 8a.** ⚠️ Plausibly the **2012 → 2023 PHZM revision**; I did not read either map.
- **EPQS's vertical accuracy** — I compared it to `property.json`, which was **itself derived from 3DEP**. ⛔ **That is a consistency check, not an independent validation.** It shows EPQS returns the same product the repo sampled by hand; it does not prove either is right on the ground.
- **National coverage is 9 probe points, not a coverage map.** The Alaska result shows the edge is real.
- **Whether `fetch()` in the browser and in a Worker both follow the NWS 301** — both should by default; **I did not test either runtime**, only `curl`.
- **The ~24% bias number** was read from the repo, not recomputed.
- **The condo's own station selection** — Hartsfield vs DeKalb-Peachtree — I noted the elevation gap and **did not run the derivation both ways.**
- **Open-Meteo's non-commercial clause** comes from a search summary of their pricing/terms pages, **not from a page I fetched**. ⭐ **It is load-bearing enough that Paul should read the terms himself before it is relied on.**
- ⚠️ **Fernwood's OSM zero is "zero within 8 km," not "there is no fire department."** At 15 km it returns 7. ⛔ **I did not establish which station actually serves the property** — that is a jurisdiction question and OSM does not answer it.
- **The NTEE inconsistency is 8 queries, not an audit.** ⭐ It is enough to say *do not filter on NTEE alone*; it is **not** a measured error rate.
- **ProPublica's `total_results` is a name-match count, not a coverage figure.** *"GA astronomy → 2"* means two organisations whose **name** matched, not two astronomy nonprofits in Georgia.
- ⛔ **Axis ④ carries NO probe of mine.** Every claim is cited from `.plans/2026-09-07-place-card-AI-BOUNDARY.md` or reasoned from finding 12. **It is the weakest-evidenced axis in this file and it is the one where I am recommending "do not build," which is the safe direction to be under-evidenced in.**
- **The advisory useful-life tiers in §11b are my judgement**, not measured. ⭐ The one I would defend hardest is the short-fuse stop; the marginal tier is genuinely arguable.
- **`READER_RANKING` and GL-1** are described from the coordinator's brief; ⛔ **I did not read the onboarding tap-order code.**

## Files touched

| file | change |
|---|---|
| `.plans/2026-09-07-weather-tier2-sources-SCAN.md` | **created — this file, and the only one** |

⛔ **Nothing else.** No `BACKLOG.md`, `CLAUDE.md`, `cycle/*`, `tools/*`, `worker/*` or zones file touched. No commit, no deploy, no key, no purchase. Scratch stayed in the session scratchpad.

## Falsifier

1. ⭐⭐ **§4 falsifies if EPQS and the repo's own lidar sample are the same measurement wearing two hats** — which, honestly, they may partly be. **Test: a third independent elevation** — a GPS reading on the ground, a plat, a survey. ⛔ **If that third source disagrees with 2,873 ft, the "+0.3 ft" headline is a circularity, not a validation.** *This is the falsifier I would run first, and it tests my own strongest claim.*
2. ⭐ **§5 falsifies if the 9-day spring gap turns out to be canon using KJZP** (1,535 ft) rather than Jasper 1 NNW. *Test: pull KJZP's own 1991–2020 normals — one call. If KJZP's T36 last-spring is 04/23, canon is right and my station choice is wrong.* ⭐ **Cheap, decisive, and it tests me.**
3. **§8 falsifies if `not-applicable` and `unknown` collapse in practice** — i.e. if no reader ever does anything different with them. Then it is ceremony and one state suffices.
4. **§7's "confirm the input" rule falsifies if a household confidently corrects a derived OUTPUT and is right.** ⭐ Precedent cuts the other way: the one time a user disbelieved a number here, she was right by 14× — **about a measurement she was standing in.**
5. **§10a falsifies if EPQS is unavailable, slow or rate-limited at N.** ⚠️ **No published limit was found**, which is a gap, not a reassurance.
6. **§9 falsifies if Open-Meteo's non-commercial clause does not attach to a personal project serving family members** — plausible, and **Paul's call, not mine.**
7. ⭐ **§11's pollen finding falsifies if Google Pollen returns real US data at these addresses** — which it very likely does. ⛔ **My claim is narrower than it may read: there is no *free, keyless* US pollen source, not that US pollen data does not exist.** *Test: one Google Cloud project — which is a spend decision, which is the point.*
8. ⭐⭐ **§12b's "a radius is the wrong primitive" falsifies if a single radius can be found that serves both households.** *Test: is there an r where Fernwood returns ≥1 and the condo returns ≤10? Between 8 km and 15 km the condo is already past 97.* ⛔ **I believe no such r exists, and that is a checkable arithmetic claim, not an opinion.**
9. ⭐ **§12f's join falsifies if a household's declared interests and their record's `group` set diverge badly** — e.g. someone with no plants who wants the native-plant society. **Then keying on the record is wrong and the tap order is right.** ⚠️ **This is the falsifier most likely to fire**, and it is why the recommendation is one-way (add, never remove).
10. **§13b falsifies if a bounded human-registered feed set turns out to be unaffordable per household** — then aggregation is the only path and **the ruling becomes unavoidable rather than optional.** ⭐ That is the real decision hiding under axis ④.
11. ⭐ **§11b's short-fuse stop falsifies only if a notification channel appears** — and `CLAUDE.md` states the site premise is **PERMANENT**, so this one falsifies only by Paul overruling the premise.

## QA

| check | how | status |
|---|---|---|
| Every `measured` claim traces to a probe run tonight | § Probes run lists **84** with results | ✅ |
| ⭐ **Probed at NON-Fernwood addresses** | two states, three addresses, six elevation spot checks, two states for organisations; **findings 3, 10 and 12 were all invisible at Fernwood** | ✅ |
| ⭐ **Positive controls on the derivations themselves** | EPQS vs the known lidar value · frost fall-date vs canon · Bangor hardiness vs the official ZIP · ⭐ **Berlin pollen vs US pollen** | ✅ |
| ⛔ **`research-resources.md` extended, not re-derived** | §3 probes its rows; §6 records **two corrections** (PRISM; NCEI token); §12f **builds on** its Community-list proposal rather than replacing it | ✅ |
| **Access · CORS · resolution · coverage · licence stated per source** | §3 · §11a · §12a columns | ✅ |
| **Coverage flagged national vs patchy** | §2d · §3's verdict · the Alaska edge · ⭐ **finding 12's 97-vs-zero** | ✅ |
| ⭐ **Human-confirmable form for every derived figure** | §7b, six rows | ✅ |
| ⭐ **Applicability mechanism proposed, not just the Georgia case** | §8, in `DOMAINS`/`MODULE_STATES` vocabulary | ✅ |
| **How each source FAILS, loud vs silent** | §6, plus §11a and §12f's three new silent cases | ✅ |
| ⭐ **The four axes kept separate** | §0's axis table · §10's bridge · §§11/12/13 · §14's four verdicts | ✅ |
| ⭐ **ASK vs JUST-SHOW stated per class** | §11c · §12e · §13d | ✅ |
| ⭐ **The delivery constraint stated, not assumed away** | §11b — three tiers, and a named **do-not-offer** | ✅ |
| ⭐ **Rule-vs-judgement stated per candidate** | §12f's two-build table · §13b's five rows | ✅ |
| ⭐ **Privacy precision addressed per link class** | §12c, with the live Wundermap defect named | ✅ |
| **A v1 cut per axis with its deferrals named** | §14a–14d, four verdicts, ~15 deferrals | ✅ |
| ⛔ **The AI boundary CITED, not re-ruled** | §13 opens by naming `place-card-AI-BOUNDARY.md` as the artifact and adds only measurement | ✅ |
| ⛔ **Nothing shipped; no cross-lane ranking** | § Files touched; §15 is lane-internal | ✅ |
| ⛔ **Condo address and coordinates absent** | *"the Midtown condo"* only — ⚠️ its Overpass and geocode probes are reported as **counts, never coordinates** | ✅ |
| ⛔ **`kind: scan`, no `stage:`** | header | ✅ |

⚠️ **The QA this file cannot do:** it cannot check that a source behaves next month. **Every probe is a reading taken on 2026-09-07 and expires the way any live reading does** — and two of these services have already changed under this repo (CARTO's watermark, RainViewer's payload).

---

## Sources

**Verified today (2026-09-07) — by query:**
[USGS EPQS](https://epqs.nationalmap.gov/v1/json) ·
[NCEI Access Data Service](https://www.ncei.noaa.gov/access/services/data/v1) (`normals-monthly-1991-2020`, `normals-annualseasonal-1991-2020`) ·
[RCC-ACIS Web Services v2](https://data.rcc-acis.org) (`StnMeta`, `StnData`, `GridData`) ·
[api.weather.gov](https://api.weather.gov) (`/points`, `/gridpoints`, `/alerts/active`) ·
[US Drought Monitor data services](https://usdmdataservices.unl.edu) ·
[Census geocoder](https://geocoding.geo.census.gov) ·
[Open-Meteo](https://api.open-meteo.com) forecast · [archive](https://archive-api.open-meteo.com) · [air quality](https://air-quality-api.open-meteo.com) · elevation ·
[NOAA Tides & Currents MDAPI](https://api.tidesandcurrents.noaa.gov) ·
[phzmapi.org](https://phzmapi.org) ·
[PRISM web service](https://services.nacse.org/prism/data/get/us/800m/ppt/20250624) ·
[EPA Envirofacts UV](https://data.epa.gov/efservice/getEnvirofactsUVDAILY/ZIP/30143/JSON) ·
[NOAA SWPC planetary K index](https://services.swpc.noaa.gov/json/planetary_k_index_1m.json) ·
[USGS Water Services](https://waterservices.usgs.gov/nwis/site/) ·
[OpenStreetMap Overpass API](https://overpass-api.de/api/interpreter) ·
[ProPublica Nonprofit Explorer API v2](https://projects.propublica.org/nonprofits/api/v2/) ·
[IRS Exempt Organizations Business Master File](https://www.irs.gov/pub/irs-soi/eo1.csv) ·
[NAPSG open-data catalogue](https://data-napsg.opendata.arcgis.com/)

**Verified today — by reading:**
[Open-Meteo pricing](https://open-meteo.com/en/pricing) · [Open-Meteo terms](https://open-meteo.com/en/terms) ·
[ACIS documentation](https://docs.rcc-acis.org/) ·
[PRISM downloads web service documentation](https://prism.oregonstate.edu/documents/PRISM_downloads_web_service.pdf) (pointer returned by the service itself)

**Read for the burn-ban landscape (finding 8) — all commercial, none with a free API:**
[FireRisk.ai burn ban map](https://firerisk.ai/burn-ban-map) · [Burn Ban Radar](https://burnbanradar.com/) · [CityRuleLookup](https://cityrulelookup.com/fire)

**Read for axis ③ (civic) — searched, not probed:**
[NERIS public fire departments — NAPSG open data](https://data-napsg.opendata.arcgis.com/maps/0ac459746be44023a1b33ba00bb5f628) · [NERIS public](https://neris.fsri.org/public) · [USDA NIFA land-grant university directory](https://nifa.usda.gov/land-grant-colleges-and-universities-partner-website-directory) · [Extension Foundation — find Cooperative Extension in your state](https://extension.org/find-cooperative-extension-in-your-state/)

**In-repo trails read:** `.plans/2026-09-07-weather-card-PLAN.md` § 0-PRIME · `.plans/2026-09-07-weather-card-ARCHAEOLOGY.md` §§3–7 · `.plans/2026-09-07-mapping-sources-SCAN.md` · ⭐ `.plans/2026-09-07-place-card-AI-BOUNDARY.md` §0 rows 8/9/13/14 + R1–R5 (**cited, not duplicated, not re-ruled**) · `research-resources.md` § Category 6 · `BACKLOG.md` C7-R5 · `property.json` · `tools/momlib.py` · `estate.json` · `engine/viewer.template.html`
