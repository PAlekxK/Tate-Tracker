# weather-card · ARCHAEOLOGY — what it took to get Fernwood's weather to its current state

- row: none — evidence file for `.plans/2026-09-07-weather-card-PLAN.md` (same posture as the 09-06 STATE / CENSUS files: it is graded, not ranked)
- objective: O3 (evidence for an O3 row; it ranks nothing)
- class: instance · Fernwood's build-out, read so the ENGINE row can be scoped
- written: 2026-09-07, read-only, at `e132d63` — no tracked file edited, no commit, no network call, no KV value opened

> **Grades:** `[measured]` = read from a file or a commit in this checkout, cited `file:line` or sha ·
> `[inferred]` = derived from two measured facts · `[unverified]` = could not be confirmed by reading —
> a hypothesis, marked so it can be shot down · `[corpus <session>]` = the conversation index
> (`operating-layer/tools/corpus_search.py`, message mode), a claim about what was SAID, not what is.
>
> **Two readings of the brief flagged before anything else:**
> 1. ⚠️ **`KGAJASPE279` is NOT the Ambient station's id in this repo.** It was a *Weather Underground*
>    PWS wired on 2026-05-05 (`a822bb9`: *"Nearby PWS KGAJASPE279 wired into weather card (Weather
>    Underground)"*), removed the next day (`0476b88` *"Remove WU PWS fetch"*), and is listed under KILLED:
>    *"Killed as a data source — the on-site Ambient Weather station is the sole source. Don't reintroduce"*
>    (`BACKLOG.md:3080`). `95dc0bf` *"correct stale KGAJASPE279 PWS refs to the actual on-site station"*.
>    The on-site Ambient station is identified by its **MAC** (a Worker secret since 09-04, `6871c02`), was
>    named *"Tate"* on the Ambient account (`f9e6c2e`), and is displayed as **Fernwood Weather Vane**
>    (`instance/fernwood.json:18`, renamed from *"Kirschenbauer"* in `9754139`). Whether the Ambient
>    hardware ALSO publishes to WU under `KGAJASPE279` is `[unverified]` — a hunt for Paul, §7.
> 2. *"Kirschenbauer station"* in the transcript is read as **"their own station"** (the household's).
>    Consistent with the repo: the station's own provenance label was *"Kirschenbauer Ambient Weather
>    Station"* until 07-14 and still is in the data files (`weather-history.json:4`, `weather-bias.json:6`).
>
> **The coordinator's relayed generalisation (Paul, ~11:30 ET), verbatim, is the column set of §3:**
> *"during the setup process, what information do we ask for? What does that allow us to do automatically
> versus with research versus with the build-out? What functions of each card do we want additional
> input before we unlock, to reinforce this input-to-value cycle."* §3 is written as that matrix so it
> can be the template for every other card; a parallel agent drafts the skeleton for the rest and cites
> this file for the weather rows.

---

## 0 · The one-paragraph answer

Fernwood's weather is **five sources, one of them hardware, stitched over four months** `[measured]`:
a keyless forecast model (Open-Meteo, from 05-05), the household's own Ambient Weather station (from
05-06, through a Worker proxy since 08-04), NWS alerts + sky cover (keyless, 05-13/19), a keyless radar
(RainViewer + Esri tiles, 08-14 door), and two Worker proxies with a key or a county code (AirNow,
US Drought Monitor, 05-18). On top of the live card sit **three research artifacts that exist only for
this one address**: a hand-authored place record (`property.json` — coordinates, lidar elevation, county
FIPS, KJZP reference station, elevation-adjusted frost dates and zone), a terrain-horizon sun table from
a DEM (`sun-horizon.json`, 07-25), and two GitHub-Actions bots that write the station's daily history and
its bias against the regional grid into files at the repo root (05-13, 07-03). **Every one of those three
is Fernwood-only by construction.** A brand-new household that has typed only an address gets, today,
**no weather at all** — the viewer's `SITE_PLACED` flag is false without coordinates, every location
fetch returns early, and the place card says the weather is *"being worked out from this address"*
(`5727efe`, 09-07). *"No geocoding exists; separate item, Paul's go pending"* (`cycle/release/CYCLE-LOG.md:722`).

---

## 1 · Timeline — the capability's build-out, dated, from the commits

572 commits match `weather` (`git log --all -i --grep=weather | wc -l`); ~450 are the recorder bot's
*"rollup update"* and ~15 the bias bot's *"analysis refresh"*. The rest, by era. Each step: **what was
added · the research or decision it took · the external dependency it introduced · per-HOUSEHOLD or
engine-wide.**

| date | sha | what was added | research / decision it required | dependency introduced | scope |
|---|---|---|---|---|---|
| 04-30 | `98ad742` | Initial commit; `weather.json` is a **placeholder hand-copied from FOX Weather**: *"Replace with live API when CORS/sandbox issues are resolved"* (`weather.json:2-7`) | none — a mock | none | — |
| 05-05 | `a822bb9` | KGAJASPE279 (Weather Underground PWS) wired; **coordinates corrected** to 34.5496/−84.3674 (*"previous coordinates … were pointing near Jasper town center"*, `property.json` location.note); elevation 2,959 ft from the Open-Meteo elevation API | a coordinate check against Google Maps; an elevation read off a 90 m model (later −86 ft wrong) | WU PWS (killed next day); Open-Meteo forecast API (keyless, CORS) — `viewer.template.html:7954` | forecast: engine · coords: per-household |
| 05-06 | `f9e6c2e` `0476b88` `5829285` `5a61b2f` `4b74aca` | **Ambient Weather station** wired client-side by MAC; *"the configured MAC … has never reported data … the active station is [MAC] (named 'Tate')"*; WU dropped; source chips 📡/☁️/📊; station hero; 24-h sparklines | which physical device on the account reports; the **measured-vs-modelled** distinction as a design rule (the chip system) | Ambient REST API — an `applicationKey` + `apiKey` pair **embedded in `viewer.html`**, world-readable from 05-05 (`worker.js:995-1000`) | **per-household** (hardware + account + key pair + MAC) |
| 05-06 | `dc1d271` `195213e` | **Phase 6 archive foundation**: `weather-history.json` + `tools/record-daily-rollup.mjs` (daily rollups of 5-min station rows); *"Credentials read from env … or fall back to viewer.html-embedded keys"* | the decision to accumulate the household's own record so the card can one day say *"wettest May on our record"* | a second copy of the credential (the seed of the 08-05 outage) | Fernwood-only (one file at repo root) |
| 05-08/11 | `3751af8` `5d5465c` | card restructured *by topic*; hourly forecast; field-journal voice | — | — | engine |
| 05-13 | `2b79600` `9ccaebe` `b9379f7` | **GitHub Action `record-weather.yml`**, cron `0 */6 * * *`, commits as `weather-recorder[bot]`; alerts source chips | *"GitHub Action long-term so accumulation doesn't depend on the laptop being awake"* (`dc1d271` body) | GitHub Actions secrets `AMBIENT_*` (removed 08-08) | Fernwood-only (`git push` to `origin/main`) |
| 05-18 | `b7daff6` `5dc765e` `348289f` | **Worker proxies**: `/api/airnow?lat=&lon=` (15-min KV cache, **75-mile** radius because *"Pickens County is rural"*), `/api/drought?fips=` (6-h cache), `/api/today-line` (Claude); NCEI normals **dropped** — 1991–2020 normals computed client-side from the Open-Meteo archive | which upstreams need a server (CORS/keys) vs none; each 503s *not-configured* and the UI hides | `AIRNOW_API_KEY` (free, one key); USDM (keyless, needs a **county FIPS** — `property.json` resources.droughtFips); Anthropic key | AirNow key: engine-wide · FIPS: per-household research · Guru: out of scope here |
| 05-19 | `cf3a329` `8dbbb6b` | **Burn status** block: NWS Red Flag/Fire Weather Watch (tier 1) · USDM D2+ or ≥10 dry days (tier 2) · **Georgia EPD seasonal ban rule hard-coded** *"May 1 – Sep 30"* (tier 3, `viewer.template.html:19728`) | reading GA EPD's rule; deciding the synthesis order | `api.weather.gov/alerts/active?point=` (keyless, CORS) | NWS: engine · **the GA rule is a Georgia literal** |
| 07-03 | `95dc0bf` | **Bias analysis**: `tools/analyze-weather-bias.mjs` (station vs Open-Meteo ERA5 grid, deterministic, keyless) + weekly Action `analyze-weather-bias.yml` + the card's *"runs wetter here"* note; first finding *+26 % wetter, +1.7 °F, wind ≈ 0 → anemometer flag* | that a station-vs-grid delta is a Mom-readable fact AND a hardware-health signal (the wind-stall flag) | Open-Meteo archive API (keyless) | Fernwood-only (second file at repo root, second bot) |
| 07-14 | `124d8ff` `9754139` | card IA **glance → forecast → reference**, *measured vs modelled* kept distinct; the top strip becomes a **source KEY**; station renamed **Fernwood Weather Vane** | ux-expert + user-researcher seats ran first: `.ux-reviews/2026-07-14-weather-card-reorg.json`, `.user-research/2026-07-14-weather-card-reader-jobs.md` | — | engine (IA) · the NAME is instance identity (`INSTANCE-RECIPE.md:30`) |
| 07-23/25 | `e8f2ab6` `628abf1` `7da8559` `91e62a9` `7100226` | **Hyperlocalization audit** → `sun-horizon.json` + `tools/gen-sun-horizon.py` (terrain skyline from a 1-arcsec SRTM tile, house AND lake; sundown on the water 7–16 min earlier); the **rain day-boundary bug** (12 duplicate rain days; +78 % → +20 %); Paul: *"station is by the pond"*; measured leads modelled in the type scale | `.engineering/2026-07-23-hyperlocalization-audit.md` — two DEMs cross-checked; nearby CoCoRaHS gauges compared; TZ bug traced to a GitHub runner in UTC | an SRTM tile (`N34W085.hgt`, not in the repo — `gen-sun-horizon.py:13`) | **per-household research** (a tile + a run per address) |
| 07-26→29 | `d6d0bdc` `7a57b78` `8dc4394` | Mom: *"I don't believe it's literally the past seven days"* — she was right (the 7-day figure was ERA5, the gauge had 2″ the model missed) → **day-by-day at our gauge**, 30-day + whole-record totals with coverage; *"the YEAR does not exist and the card says so"* (`BACKLOG.md:371`) | her feedback as the steer; coverage shown beside every total | — | engine (render) · the DATA is Fernwood-only (`weather-history.json`) |
| 08-01→08 | `eb9863e` `f920849` `6365912` `7957b65` | **Key exposure remediated in the right order**: proxy `/api/ambient` ships (120 s cache, `limit` clamped, upstream error bodies never echoed) → viewer switches → keys rotated → MAC moved out of 8 public files → **recorder reads the proxy and holds no credential** after failing every 6 h for four days *invisibly* (the dashboard stayed green) | *"a second copy of a credential is the bug"* (`record-weather.yml:22-29`); the proxy is **deliberately ahead of the token gate** so an unpaired device still sees conditions (`eb9863e` body) | Worker secrets `AMBIENT_APP_KEY` / `AMBIENT_API_KEY`; `AMBIENT_MAC` as a default in code | per-household secrets, held **one pair per Worker env** |
| 08-14/19 | `4b38e82` `65608de` `7db2476` `c7e441b` | **Radar door** — exhibit R-C from a `/design-options` run (*"if it's a key feature, let's highlight it … still nested within the weather card"*); the seats found a live bug (every observed frame labelled *forecast* when RainViewer serves 0 nowcast frames) and a wrong glyph; lap 4 moves the radar from 2,447 px to 115 px (*"put it where she lands"*) | `.ux-reviews/2026-08-14-radar-door.json`; Mom named the radar twice (*"didn't know how to access it"*) | RainViewer public API + tile cache (keyless); Leaflet | engine (keyless) |
| 08-31 | `viewer.template.html:15405-15417` | basemap swapped CARTO → **Esri light-gray canvas** after CARTO began watermarking *"API KEY REQUIRED"* on Mom's ratified surface `[corpus 8f98321a]` | a keyless tile source can change under you | Esri ArcGIS Online tiles (keyless) | engine |
| 08-31 | `property.json` location.elevation | elevation **2,959 → 2,873 ft** from USGS 3DEP 1 m lidar; *"A single global-model API is not a measurement"* | a lidar sample; corroborated by the 17 traced zones (2,819–2,894 ft) | none new | per-household research |
| 09-03 | `64096b0` `79c4bae` `9d65723` `7c07655` | **C5**: `weather` is a **NON-DOMAIN module** (a renderer switch; `estate.json:12`, `momlib.py:359`); `sky` likewise; **`AMBIENT_MAC` becomes per-env config — 503 without** (*"engine code holds no station"*, `worker.js:1012-1014`); tools derive LAT/LON from canon (`analyze-weather-bias.mjs:31-32`) | C5 7c: the Worker holds no instance data; C7 1c: the station is **three-state** present · declared-absent · undeclared (`viewer.template.html:7231-7246`); C7 Q7: frost = a three-layer derivation, engine rule, **not built** | — | engine (declaration) |
| 09-04 | `322a416` | `withCache` serves uncached on a failed KV put — the account-wide KV write cap took `/api/ambient` to 502 and the recorder down (memory `reference_cloudflare_kv_write_cap_account_wide`); Workers Paid the same day; **MAC becomes a Worker secret** (`6871c02` body; `wrangler.toml` at HEAD carries no `AMBIENT_MAC` var `[measured]`) | — | Workers Paid plan | engine |
| 09-06/07 | `viewer.template.html:7263-7268` `5727efe` `50f28ff` `c821051` | **`SITE_PLACED`**: *"A new household has an ADDRESS … and no COORDINATES — nothing has geocoded it yet. Weather, sky, water and the property page all need a point on the earth, so without one they must say nothing rather than throw"*; the place card carries the typed address + *"We're working out your weather and what grows here from this address"*; a box number gets the honest refusal | Paul, beat 3 09-07: *"we can at least put the address there and say that we are populating it"*; the strict seat: a box number cannot yield weather | none — **and none exists**: `grep -rn geocod worker/worker.js` → 0; *"There is no geocoding path in this product"* (`estate/index.html:330`) | the seam this row opens |

**What the eras say, read together `[inferred]`:** the *live* half (forecast · station · alerts · radar)
was built in the first two weeks and has been *re-shaped* since; the *research* half (the place record,
the horizon, the bots) accreted around one address and was never designed to be repeated. The
09-03 module/three-state work made the card **switchable**; nothing yet makes it **derivable** from an
address.

---

## 2 · The current card — what renders, from which function

`renderWeather()` (`viewer.template.html:9130`), IA of 07-14, top to bottom `[measured]`:

| block | function | reads |
|---|---|---|
| source KEY strip | `renderWeather` head (`:9153`) | `STATION_NAME` + `ESTATE_STATION` (build-time identity) · `WEATHER_DATA.stationOnline` |
| Radar (`.radar-section`, precedes `#weather-content` since 08-19) | `toggleRadar` / `initRadarMap` (`:15343`, `:15392`) | `siteCoords()` · RainViewer · Esri tiles |
| Worth knowing | `generateAlerts()` (`:9387`) + severe burn (`computeBurnStatus`, `:19726`) | Open-Meteo current/daily · station overrides · NWS alerts · USDM |
| Glance sentence (also the collapsed header + strip tile) | `generateGardenerInsight()` (`:8371`) via `renderWeatherSummary` (`:9091`) | same four inputs; frost low from `property.json` frostDates; fungal line from `property.json:100` |
| Right now — *measured on the property* | `renderAmbientStationPanel` (`:8579`): hero · comfort line · sparklines · battery chip | `/api/ambient` (288 × 5-min rows) |
| Right now — modelled sub-row | `renderWeather` (`:9260`) | Open-Meteo current |
| Forecast — 7-day + hourly | `renderWeather` (`:9278`) | Open-Meteo daily/hourly (flat-horizon sunrise/sunset included) |
| Rainfall — regional vs 25-yr normal · **day by day at our gauge** · 30 days / whole record · *"reads wetter than the region"* | `renderRainfallPanel` (`:8923`), `stationRainRange` (`:8889`), `fetchPrecipHistory` (`:8741`) | Open-Meteo archive 2001–2025 · station rows · `weather-history.json` · `weather-bias.json` |
| Inside | `:9336` (hidden without a station) | the station's indoor sensors |
| Burn status (reference, bottom) | `computeBurnStatus` | NWS fire alerts · USDM (FIPS) · days-since-rain · the GA seasonal literal |
| AQI chip (on the summary) | `fetchAirNowAQI` (`:19500`) | `/api/airnow` — **requires `WorkerAPI.isConfigured()`** (a paired device) |
| *not on this card:* Sky & Stars tile's *"last light here"* | `terrainSunTimes(now,"house")` (`:18157`) | `sun-horizon.json` (SUN_HORIZON_DATA, inlined) — a **separate module** (`sky`), grouping question open (`INSTANCE-RECIPE.md:107`) |

---

## 3 · THE MATRIX — function · input · unlock · gate · fernwood-evidence

Column set = Paul's *input-to-value cycle* ask, verbatim (header). Definitions used, so the parallel
agent's rows compose with these:

- **input** — what the household must have SUPPLIED: `address` · `name` · `station id + key` (the
  Ambient application/API key pair + device MAC) · `a traced zone` · `a photo` · `nothing`. An answer
  to an ask is an input.
- **unlock** — `AUTOMATIC` (derivable now from inputs already held — for weather, that means *once the
  address is geocoded*; geocoding itself is the first BUILD-OUT row) · `RESEARCH` (a one-time
  per-household lookup someone performs) · `BUILD-OUT` (engineering not yet in the engine).
- **gate** — `at-setup` (shows once the input exists) · `opt-in` (needs an additional explicit answer —
  the ask is named) · `never-for-this-household` (Fernwood-only, cannot generalise as built).

⚠️ **One row is the floor under every AUTOMATIC row: address → coordinates.** Until it exists, every
"AUTOMATIC · at-setup" below reads as *reachable*, not *reached* (`SITE_PLACED`, `viewer.template.html:7267`).

| # | function | input | unlock | gate | fernwood-evidence |
|---|---|---|---|---|---|
| W0 | **place the household on the earth** (lat/lon; county FIPS falls out of the same lookup) | address | **BUILD-OUT** — no geocode route in the Worker (`grep geocod worker/worker.js` = 0); the Census geocoder named as the keyless interim, USPS blocked on business registration (`BACKLOG.md:304`); *"suggest, never decide … degrade open"* | at-setup | Fernwood's coords were typed by hand and checked against Google Maps (`property.json` location.note); `CYCLE-LOG.md:722` *"no geocoding exists; separate item, Paul's go pending"* |
| W1 | glance sentence + strip tile + collapsed header (*"what's it like out"*) | address (→W0) | AUTOMATIC — `generateGardenerInsight` over Open-Meteo current/daily | at-setup | `viewer.template.html:7950-7960`, `:8371`, `:9091` |
| W2 | 7-day + hourly forecast, flat-horizon sunrise/sunset | address (→W0) | AUTOMATIC — keyless Open-Meteo | at-setup | `:7954-7960`; `a822bb9` |
| W3 | *Worth knowing* — weather alerts (rain, wind, heat, frost) | address (→W0) | AUTOMATIC — `generateAlerts` over the same inputs; **frost rule reads `property.json` frostDates, hand-authored** | at-setup (without frost) · RESEARCH or BUILD-OUT for the frost line (C7 Q7 three-layer derivation ruled engine-wide, **not built**, `c0d31dc`) | `:9387`; `.plans/2026-09-03-c7-condo-paper-model-PLAN.md` Q7 |
| W4 | NWS severe fire-weather alert (promoted to *Worth knowing*) | address (→W0) | AUTOMATIC — `api.weather.gov/alerts/active?point=`, keyless, US only | at-setup | `:19633-19650`; `cf3a329` |
| W5 | modelled *Right now* (temp, feels-like, wind, humidity, pressure, cloud, visibility) | address (→W0) | AUTOMATIC | at-setup — **this is the base card's "right now" when no station is declared**; the panel says *"This place declares no weather station — readings here are regional (modelled)"* | `:8585-8589`; `:9149`; C7 1c |
| W6 | the source KEY strip — names each source once, live dot | name (a station name), `identity.station` state | AUTOMATIC given the declaration; **the declaration is a hand-edited instance file today** | at-setup (regional) · the station row appears with W8 | `INSTANCE-RECIPE.md:30-33` (*"Absent → `undeclared`, loudly"*); `engine/place-claims.json` `17f7ddaf43` (*"gate the row on the estate declaring a station"*) |
| W7 | **Radar** — animated RainViewer frames over a keyless Esri basemap, centred on the place, marker labelled with the short address | address (→W0) | AUTOMATIC — keyless; **renders for every placed estate today, no switch exists** (`estate.json` modules has no radar key) | **opt-in** `[paul-stated 2026-09-07]` — the ask: *"do you want the radar?"* (words: content-steward). The switch itself is BUILD-OUT | `:15392-15463`; `4b38e82`; `7db2476`; `BACKLOG.md:285` (`radar_toggled`); RELEASE_NOTES 08-14/08-19 |
| W8 | **measured *Right now*** — station hero, dew point/comfort, pressure, solar, UV, battery chip | station id + key (Ambient `applicationKey` + `apiKey` + MAC) | AUTOMATIC once the Worker env is configured — **but the Worker holds ONE pair + ONE MAC per env** (`worker.js:1017-1026`, `wrangler.toml` per-env); a per-household store is BUILD-OUT | **opt-in** — the ask: *"do you have your own weather station?"* + a gated credential handoff (never through `/api/feedback`) | `5829285`; `eb9863e`; `9d65723`; `/health.configured.ambient` `worker.js:3156` |
| W9 | 24-h trend sparklines (temp · humidity · pressure) | station id + key | AUTOMATIC with W8 (same 288-row call) | opt-in (rides on W8) | `5a61b2f`; `:8131-8134` |
| W10 | *Inside* — indoor temp/humidity/dew | station id + key **and** a station with indoor sensors | AUTOMATIC with W8; hidden otherwise | opt-in (rides on W8; `[unverified]` that every Ambient model reports indoor) | `:9336-9339`; `f9e6c2e` (*"including indoor temp/humidity"*) |
| W11 | Rainfall — regional 7/30/365-day vs 25-year normal | address (→W0) | AUTOMATIC — Open-Meteo archive, keyless (one 25-year pull per load) | at-setup | `:8741-8760`; labelled REGION explicitly since 07-26 |
| W12 | Rainfall — **day by day at our gauge**, 7 days | station + **a history store** — `stationRain7()` reads `WEATHER_DATA.history.days`, i.e. `weather-history.json`, the recorder bot's file (`:8841`), NOT the live 288-row window | **BUILD-OUT** — same store as W13 (a per-estate history the Worker writes; the bot cannot) | opt-in **and** never-for-this-household **as built** — ⚠️ the one measured-rain row Mom asked for by name (`BACKLOG.md:579`) is behind the bot, not behind the station | `d6d0bdc`; `:8840-8841`; `:8990-9005`; `BACKLOG.md:579` (her 07-26 note) |
| W13 | Rainfall — last 30 days · whole record · coverage caveat | station + **a history store** (`weather-history.json`, written by the recorder bot; `stationRainRange` reads `WEATHER_DATA.history.days`, `:8890`) | **BUILD-OUT** — the recorder is one GitHub Action writing one root file to `origin/main` (`record-weather.yml`); per-household needs a per-estate store the Worker writes (no git) | opt-in **and** never-for-this-household **as built** | `dc1d271`; `2b79600`; `7957b65`; `:8889-8923`; `BACKLOG.md:371` |
| W14 | *"Our gauge reads wetter/drier than the region across N days"* (+ the wind-stall flag for Paul) | station + history + ERA5 | **BUILD-OUT** — `analyze-weather-bias.mjs` reads the root file, LAT/LON derived from `property.json` (`analyze-weather-bias.mjs:31-32`), writes a second root file weekly | never-for-this-household as built (would become opt-in once W13 exists) | `95dc0bf`; `analyze-weather-bias.yml`; `:9056-9068` |
| W15 | Burn status — NWS tier | address (→W0) | AUTOMATIC (=W4) | at-setup | `cf3a329` |
| W16 | Burn status — drought tier (USDM by county) | address → **county FIPS** | AUTOMATIC once W0 returns FIPS (the Census geocoder does); today `property.json` resources.droughtFips is hand-authored | at-setup after W0 · RESEARCH if W0 does not return FIPS | `:19529`; `b7daff6` |
| W17 | Burn status — regulatory tier (*"State outdoor-burning ban active"*) | nothing | **BUILD-OUT** for anywhere but Georgia — `(m >= 4 && m <= 8)` is a GA EPD literal in engine code | **never-for-this-household** as built (a non-GA address gets Georgia's law) | `:19728`; `cf3a329` body *"Seasonal rule hardcoded (Georgia EPD)"* |
| W18 | days since meaningful rain (feeds burn tier 2 and the glance) | address (7-day cap, Open-Meteo) · station history extends it | AUTOMATIC (capped) · opt-in extends (W13) | at-setup | `:19664`; `8dbbb6b` |
| W19 | AQI chip | address (→W0) + **a paired device** (`WorkerAPI.isConfigured()`) | AUTOMATIC — one engine-wide `AIRNOW_API_KEY`, 75-mile search | at-setup **only on a paired device** — `[unverified]` how a new household's grant maps onto `X-Tate-Token` pairing after C6 | `:19500-19505`; `worker.js:1095-1107` |
| W20 | *"Local Weather Stations ↗"* link (WU map at the coords) — on the Property card | address (→W0) | AUTOMATIC | at-setup | `:13956` |
| W21 | terrain-horizon *"last light here"* (Sky tile) and the fishing dawn/dusk windows | address + **a DEM tile + a run of `gen-sun-horizon.py`** | **RESEARCH** per household (the script derives coords from canon; the SRTM tile is not in the repo) | at-setup after research — **not on the weather card**; `sky` is its own module, nesting is an open UX question | `628abf1`; `gen-sun-horizon.py:13`; `sun-horizon.json` `_meta`; `INSTANCE-RECIPE.md:107` |
| W22 | elevation (place card, Guru facts, bias `_meta`) | address (→W0) | AUTOMATIC from Open-Meteo's ~90 m elevation API — **and that was −86 ft wrong here**; lidar = RESEARCH | at-setup, labelled *estimated* (the `elevConf` idiom already exists, `:13795`) | `property.json` location.elevation.supersededValue.lesson |
| W23 | elevation-adjusted hardiness zone + frost dates (feed W3's frost line and the place card) | address → nearest long-record station + lapse-rate adjustment | **RESEARCH** today (hand-authored from NOAA normals for KJZP/Jasper 1 NNW) · BUILD-OUT per C7 Q7 | at-setup after research | `property.json` hardiness.explanation, frostDates.source; `.engineering/2026-07-23-hyperlocalization-audit.md:229-240` |
| W24 | fungal advisory with a subject (*"for the boxwood"*) | a traced/known plant in canon + the place's risk note | RESEARCH (instance content) | at-setup once a plant is in the record | `BACKLOG.md:2871`; `property.json:100` |
| W25 | the Guru's weather awareness (today-line, chat live state) | address + station (whatever W1–W10 hold) | AUTOMATIC given the above (Guru reads `WEATHER_DATA`) | out of this row — Guru is its own plan (`.plans/2026-09-03-guru-retrieval-PLAN.md`) | `worker.js:1165-1172`, `:1312` |

**Reading the matrix `[inferred]`:** with W0 built, **eleven rows (W1–W5, W11, W15, W16, W18, W20,
W22) are AUTOMATIC at-setup with no key and no research** — that is the base card Paul asked for, and
it is the C7 *declared-absent* card that already renders at the condo paper model. **W7 is AUTOMATIC
but Paul wants it opt-in**, so the only build there is the switch and the ask. **W8–W10 are the
own-station opt-in**, and the build is the *per-household credential store*, not the card (the card
already renders them). ⚠️ **W12–W14 — every measured-RAIN row, including the 7-day strip Mom asked
for by name — read the bot's file, not the station**; with W17 (the GA literal) they cannot generalise
as built and should be named OUT of the row (or scoped as their own build) rather than left to read as
reachable. **W21–W24 are the research tier** — the part of *"what it took"* that nobody will repeat by
hand for a second household.

---

## 4 · The two bots — what they do, and whether they are engine or Fernwood

| bot | runs | reads | writes | per-household? |
|---|---|---|---|---|
| `weather-recorder[bot]` · `record-weather.yml` | every 6 h on GitHub's runners; `node tools/record-daily-rollup.mjs --today` then the previous day | `/api/ambient?limit=288&endDate=` on the **production** Worker (`record-daily-rollup.mjs:39-40`, override `AMBIENT_PROXY`); **holds no credential** since `7957b65` | `weather-history.json` at the repo root, committed to `origin/main` (~4/day; 447 commits by 09-06, `BACKLOG.md:145`) | **No.** One workflow, one Worker URL, one file, one branch — and that branch is Mom's frozen page, which *"has republished every six hours since the ruling"* (`BACKLOG.md:145-149`, open, Paul's). The 09-06 sunset order ends with *"stop the bots"* (`BACKLOG.md` rule 3) |
| `analyze-weather-bias.yml` | weekly, Sundays 08:10 UTC | `weather-history.json` + Open-Meteo ERA5 archive (keyless; ERA5 lags ~5 days) at LAT/LON from `property.json` | `weather-bias.json` (headline precip/temp/humidity deltas, rolling 36 snapshots, flags such as `wind-stall`) | **No.** Same shape. Its one engine-shaped idea — *a station-vs-grid delta doubles as a hardware-health check* — is worth carrying; the mechanism (a root file on a git branch) is not |

`ENGINE-MANIFEST.md:49` already classes the recorder's schedule as *"a declared per-instance exception
(C4 process Q4)"* and `BACKLOG.md:2341` as *"a deterministic recorder writing one data file"*. **Both
bots are Fernwood-only** `[measured]`; the memory `project_fernwood_weather_bot` carries the operating
caveat (*expected VOLUME is not expected OUTCOME* — the 08-05 four-day silent outage).

---

## 5 · Almanac / sun-horizon — does the weather card depend on it?

**No** `[measured]`. `terrainSunTimes` is called at four sites (`viewer.template.html:15931, 15986,
16063, 18157`): three in the fishing card (lake) and one in the Sky tile's *"last light here"* (house).
The weather card's forecast block shows Open-Meteo's flat-horizon sunrise/sunset (W2). So the horizon is
a **Sky/fishing dependency**, and it enters this row only if Paul rules that Sky nests under Weather
(`INSTANCE-RECIPE.md:107`, open). *"Almanac"* in the brief is the journal's name, not a data source
(`VOCABULARY.md:349`) — nothing on the weather card reads the almanac.

---

## 6 · Keys, secrets and per-env configuration — the inventory

| thing | where it lives | who supplies it | scope |
|---|---|---|---|
| `AMBIENT_APP_KEY` + `AMBIENT_API_KEY` | Worker secrets (`/secrets`), one pair per env (`INSTANCE-RECIPE.md:83`) | the household's Ambient account (Paul's, today) | **per-household** — and the Worker's shape is one-per-env |
| `AMBIENT_MAC` | a `[vars]` entry 09-03 (`9d65723`) → a Worker secret since 09-04 (`6871c02`); absent → 503 `ambient-not-configured` | the device | per-household |
| `AIRNOW_API_KEY` | Worker secret | free at airnowapi.org | engine-wide, one |
| Open-Meteo forecast / archive / elevation · NWS · RainViewer · Esri tiles · USDM · USGS | none | — | engine-wide, keyless (⚠️ two have changed under us: CARTO watermark 08-31; RainViewer 0-nowcast payload 08-14) |
| county FIPS · KJZP reference · frost/zone · coordinates · lidar elevation | `property.json` (hand-authored canon) | research | per-household research |
| `identity.stationName` · `identity.station` (present/declared-absent/undeclared) | `instance/<estate>.json` → built into the viewer | a hand edit today | per-household config |
| `modules.weather` / `modules.sky` | `estate.json` | a hand edit today | per-household config |
| SRTM tile + `gen-sun-horizon.py` run | local disk (tile not in repo) | research | per-household research |
| `weather-history.json` · `weather-bias.json` | repo root, written by two Actions on `origin/main` | the bots | Fernwood-only |

---

## 7 · Unverified — what this file could not confirm by reading

1. **`KGAJASPE279` ↔ the Ambient station.** Whether the Ambient hardware also publishes to Weather
   Underground under that id. The repo calls it a killed WU source; the brief calls it Fernwood's Ambient
   PWS. **A hunt for Paul** — one sentence closes it.
2. ~~Whether the 7-day day-by-day strip (W12) reads live rows or `weather-history.json`~~ — **resolved
   while writing**: `stationRain7()` (`:8840-8841`) and `stationRainRange()` (`:8889-8890`) both read
   `WEATHER_DATA.history.days`, the bot's file. Only the *today* gauge total in the station hero comes
   from the live rows (`dailyrainin`, `5829285`).
3. **Every Ambient model reports indoor sensors** (W10) — Fernwood's does; the general claim is not read.
4. **How a new household's grant reaches `WorkerAPI.isConfigured()`** (W19) — C6 changed the door;
   this file did not re-read the pairing path.
5. **RainViewer's free-tier terms for a multi-household product** (W7) — one household has been fine.
6. **Ambient's per-key rate limit** (~1 req/s, `worker.js:1022`) against N households on one proxy.
7. **The corpus searches** for *"weather bias"*, *"ambient"*, *"radar"*, *"sun horizon"* return mostly
   September process traffic; the design conversations that produced 05-06 and 07-14 are **older than
   the ~59-day corpus** (memory `reference_conversation_corpus`) — the commits are the record. Sessions
   cited: `4e5d404f` (08-14 radar bug), `8f98321a` (08-31 CARTO watermark), `d3499a49` (07-25
   hyperlocalization close-out), `679418cc` (08-07 S19 privacy), `ff8a43b0` (07-27 key exposure),
   `agent-a9` 07-19 (Bolo show-weather path evaluation — the one prior *reuse* of this weather stack).
8. `KGAJASPE279` yields **no matches** in the corpus (`corpus_search.py "KGAJASPE"` → *no matches*).
