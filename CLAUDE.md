# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project purpose & tone

Tate Tracker is a **personal property reference dashboard** for 282 Church Mountain Road, Jasper, GA 30143 — a rural mountain property at 2,959 ft elevation in the Blue Ridge. It is hyper-personalized, not a generic app.

**Tone is everything here.** This is a fun, evocative reference tool — a field journal, not a task manager. Language like "17 actions due" or "3 alerts" is wrong for this project. Prefer "What's happening in May" or "Worth checking this month." The dashboard should feel like looking out at the land, not a to-do list with deadlines.

## How to run

Open `viewer.html` directly in a browser — no build step, no server, no install. For Playwright testing or CORS-sensitive API testing, serve locally:

```bash
cd /Users/paulkirschenbauer/Downloads/Tate-Tracker
python3 -m http.server 8765
# then open http://localhost:8765/viewer.html
```

## Architecture

`viewer.html` is a single ~4,600-line self-contained file: all CSS, JS, and inlined JSON data live in one file. There is no build system, no module bundler, no framework. The JSON files (`plants.json`, `fishing.json`, etc.) are the source of truth for data — they are fetched at page load and the inlined copies in `viewer.html` serve as fallback. When updating data, edit the JSON files and re-inline them.

### Data layer

All domain data is loaded as JS constants from inlined JSON at the top of the script section (~line 1550):

- `PLANTS_DATA` — 8 plants with per-plant care calendars (schema v3). Care entries have `months[]`, `peakWindow`, `narrow` (boolean for timing-critical windows), and optional `subcategories[]`.
- `FISHING_DATA` — Lake Sequoyah species profiles, scoring weights, seasonal notes.
- `BIRDS_DATA` / `AMPHIBIANS_DATA` — Species with `monthsPresent`/`monthsActive`, status (resident/summer/winter/migrant).
- `VEHICLES_DATA` — Fleet registry with status badges.
- `PROPERTY_DATA` — Microclimate, soil series, watershed, elevation notes.

Live data is fetched async at init from Open-Meteo (weather + pressure), RainViewer (radar), and the Weather Underground PWS API (KGAJASPE279 — the nearest personal weather station).

### CSS conventions

Color utilities are defined per care type and reused throughout:

```css
.c-{type}   /* colored text */
.b-{type}   /* solid background */
.bg-{type}  /* solid background (alias) */
.br-{type}  /* left border color */
.t-{type}   /* combined with .tag for action pills */
```

Care types: `prune`, `propagate`, `fertilize`, `water`, `repot`, `inspect`

**Action pills** (`.tag.t-{type}`) are the unified label element across all four plant views. Use this class — never invent new badge/chip patterns for care actions. The corresponding JS constants:

```js
const CARE_TYPES = { prune: { label, icon }, propagate: ..., ... }
const CARE_COLORS = { prune: "#c0622f", propagate: "#3d8a5e", ... }
```

### Key rendering functions

| Function | What it renders |
|---|---|
| `renderWeather()` | Full weather card with forecast, radar, PWS panel |
| `renderRainfallPanel()` | Rainfall context with rv-badge status chips |
| `renderFishing()` | Fishing tab content (lives inside Wildlife card; writes to `#wildlife-tab-content`) |
| `renderProperty()` | Property profile card |
| `renderPlantList()` | By Species view (calls `renderPlantCard` per plant) |
| `renderThisMonthPlants()` | This Month view grouped by care type |
| `renderTimeline()` | 3 Month view |
| `renderCalendarBody()` + `renderCalendarLegend()` | Full Year heatmap |
| `renderBirds()` / `renderAmphibians()` | Wildlife tabs (Birds, Amphibians) |
| `renderDashboardStrip()` | Top 4-tile teaser strip (Weather, Plants, Wildlife, Vehicles) |

### Plant view tabs

Four tabs share the `#plant-view-tabs` switcher. `switchPlantView(view)` controls visibility. Timeline and Full Year are rendered on demand (not at init). The active filter for By Species is stored in the module-level `activeFilter` variable.

### Card expand/collapse

Cards expand/collapse via `.expanded` class toggled on `.main-card` when its `.main-card-header` is clicked. CSS controls visibility of `.main-card-body` (display none → block). There is currently no animation — cards hard-toggle.

## Design system

**Fonts:** `Crimson Text` (serif) for the header title and plant guide prose. `DM Sans` for all UI chrome, labels, data, and tags.

**Header:** Dark forest green gradient (`#183524 → #2a6040 → #3a8a58`). Decorative circles in `::before`/`::after` at low opacity.

**Body background:** Soft green gradient (`#edf7e6 → #e2f0d8`). Max content width 660px, centered.

**Cards:** White, `border: 1.5px solid #d8eacc`, `border-radius: 18px`. Card icons are 42×42px rounded squares with context-appropriate gradients.

## Next steps

### ~~Fishing card — temperature/verdict contradiction~~ ✓ Done
Verdict now steps down when `lakeTemp < hwtMonth.low_F`. A context note and Early/Mid/Late month progression strip appear in shoulder seasons. See `projectLakeTempProgression()` and the `belowHistFloor` logic in `renderFishing()`.

### ~~Dashboard strip redesign — teaser tiles + Vehicles tile + Fishing merged into Wildlife~~ ✓ Done
- Strip now has 4 tiles using `repeat(auto-fit, minmax(150px, 1fr))` so it reflows 2×2 on mobile.
- Each tile shows actual content (icon + label + plant/species names) instead of count pills. The `.dash-alert-pill` orange/red styling was removed in favor of `.dash-tease-row` (icon + body, quiet text).
- Vehicles & Equipment tile is static "Reference" (no month-based content).
- Standalone Fishing card removed; Fishing is now a third tab inside the Wildlife card (Birds, Amphibians, Fishing). `renderFishing()` writes to `#wildlife-tab-content`. Fishing-related text in the Wildlife card subtitle includes lake temp + phase.

### ~~Tone audit — urgency language~~ ✓ Mostly done
Replaced: "17 actions due" → month-name + per-care-type teaser; "3 alerts" → quiet alert teaser rows; "3 need attention" / "items in fleet" → "Specifications and maintenance". Remaining strings to scan: any internal weather alert titles that read "Warning" / "Severe" — those are arguably right when the conditions are dangerous (freeze, damaging wind), so probably leave them as-is.

### ~~Ambient Weather integration — full sensor data~~ ✓ Done
Switched the configured AMBIENT_MAC to the active reporting station (`D8:F1:5B:15:28:B8`, "Tate"). The on-property hero now populates with all 25 sensor fields including indoor temp/humidity, solar radiation, UV, and the physical rain gauge. Removed the Weather Underground PWS fetch (CORS-blocked, redundant with Ambient).

### ~~Weather card UI overhaul — source-grouped blocks + live indicators~~ ✓ Done
Each weather subsection is now a tinted bordered `.wblock` container (one source per block). Three variants:
- `.wblock-station` (green) → 📡 Kirschenbauer Station — on-property hero, rain gauge, 24h trends
- `.wblock-forecast` (blue) → ☁️ Open-Meteo — current condition, 7-day strip, alerts
- `.wblock-historical` (gray) → 📊 ERA5 — rainfall percentile context

Each block carries a `wblock-status` line with a `liveIndicator(timestamp, freshMin, staleMin)` showing a pulsing green dot when data is fresh, yellow when stale, red when offline.

### ~~Phase 4 — gardener insight line~~ ✓ Done
The on-property hero leads with a synthesized italic "Today" callout (Crimson Text serif). Rule-based: storm imminent / active rain / frost / heat / saturated soil / muggy / ideal window / generic mild. Each rule returns observation + optional action sentence.

### ~~Phase 5 — station-aware alert engine~~ ✓ Done (uncommitted)
`generateAlerts()` now produces both station-driven and forecast-driven alerts. New station alerts: heavy/steady/light rain in progress, saturated soils, hot now, freezing now, high gusts now, pressure dropping fast, station battery low. Forecast alerts get tagged `source: "forecast"`. Each alert renders a per-alert source chip (📡 Station / ☁️ Forecast). Dedup logic: forecast "Heavy Rain Today" suppressed when station already firing in-progress rain alert; forecast wind suppressed when station gust alert active; etc. **Status:** edits are local, not yet committed. User will visually verify on return.

### Phase 6 — long-term archive — foundation built ✓ (data accumulating)
- New `weather-history.json` at repo root holds daily rollups (min/max/avg for temp, humidity, wind, rain, pressure, solar, UV, indoor sensors).
- New `tools/record-daily-rollup.mjs` — Node 18+ script (zero deps) that fetches Ambient Weather, builds a daily rollup, and merges it into `weather-history.json`. Idempotent — re-running on a day already recorded replaces it. See `tools/README.md` for usage.
- Already backfilled: 5 days (May 2 partial, May 3, May 4, May 5, May 6 partial).
- **Scheduling plan documented in `tools/SCHEDULING.md`** — concrete YAML for a GitHub Action running every 6h + a midnight finalize, plus alternative launchd plist for local-only. Recommend GitHub Action long-term so accumulation doesn't depend on the laptop being awake. Setup needs: `AMBIENT_APP_KEY` and `AMBIENT_API_KEY` as repo secrets, then drop in the workflow file. Schema-extension ideas (rain event timing, GDD, solar hours, predominant wind direction) are in the same doc.
- **Viewer integration is not done yet.** Once the file has ~30+ days, the rainfall block can switch from ERA5 grid baselines to property-recorded comparisons ("wettest May on our 14-month record"). For now the file is just accumulating.

### ~~Hourly forecast strip — next 48h under the daily tiles~~ ✓ Done (2026-05-11)
- Extended `fetchLiveWeather()`'s Open-Meteo request with `temperature_2m,precipitation_probability,precipitation,weather_code` and `forecast_hours=48`.
- Hourly payload is split at "now": past hours feed the existing `WEATHER_DATA.hourlyPressure` (used by `pressureTrend()` for fishing forecast — unchanged behavior); future hours populate the new `WEATHER_DATA.hourly[]` (up to 48 entries).
- `renderWeather()` renders a horizontally-scrollable `.hourly-strip` directly below the 7-day `.forecast-strip`, with an italic-Crimson label "Next two days · hour by hour".
- Each cell: short time label (`Now` / `3p` / `noon` / `12a` / `Tue 12a` at day-breaks), weather glyph from `WEATHER_CODES`, temperature, precip % when ≥20%. Day rollover gets a subtle left-border separator + weekday prefix in the time label.
- Helper `hourLabel(hr)` formats 0–23 as `12a / 1a … noon … 11p`.
- New CSS classes: `.hourly-strip`, `.hourly-cell`, `.hourly-cell.now` (highlighted), `.hourly-cell.day-break` (separator), `.hour-time`, `.hour-icon`, `.hour-temp`, `.hour-precip`.

### ~~Gardener insight — station outage fallback~~ ✓ Done (2026-05-11)
- `generateGardenerInsight()` no longer bails when `WEATHER_DATA.stationData` is missing. Variables fall back to `WEATHER_DATA.current` (Open-Meteo) when station is offline.
- Station-only rules (storm-by-pressure, active rain, saturated soil, muggy/dew-point, cool damp morning) are guarded by `hasStation` and silently skipped when the station is down.
- Forecast-driven rules work either way: frost tonight, hot day ahead, **rain coming today** (new — fires at ≥70% chance or >0.25" expected), **rain coming tomorrow** (new), ideal garden window, generic comfort descriptor.
- Prose adjusts honestly: with station, observation says "at the property"; without, no observational claim. Ideal-window lead reads either "Comfortable May afternoon — 66°F, light winds" (station) or "Forecast looks comfortable today — high near 66°F" (forecast-only).

### ~~Icon/emoji audit — collisions and poor fits~~ ✓ Done
- Vehicles & Equipment card: 🚗 → 🛻 (better fits the actual fleet)
- Propagate: 🌿 → 🌱 (resolved the Plants-card collision)
- Fertilize: 🌱 → 🌾 (broke up the green-plant cluster of propagate/fertilize/repot)
- Meteor showers: 7 regular ones ☄️ → 🌠 (semantically correct — comets are reserved for "Exceptional Year" / "Best of the Year" markers)

### Additional live data sources + dynamic summarization
Goal: make the page as dynamically informed as possible at load time — beyond just the weather forecast.

**Additional data sources worth exploring** (all should be free/CORS-accessible or proxiable):
- **USGS stream gauges** — nearby creek/river levels and flow rates; relevant for flood risk, fishing conditions, and seasonal context
- **AirNow API** — air quality index; relevant for outdoor work and burn days on the property
- **NOAA Climate Data Online** — actual observed rainfall/temp at the nearest station vs. historical normals (more authoritative than the estimated lake temp lag currently used)
- **iNaturalist API** — recent wildlife observations within a radius of the property coordinates; could surface what neighbors are actually seeing right now
- **Georgia DNR / local fishing reports** — actual reported conditions at Lake Sequoyah or nearby waters
- **USFS fire danger ratings** — Southern Region; relevant for a rural mountain property with wooded acreage

**Dynamic AI summarization (higher complexity, worth exploring):**
Once multiple live data streams are available, explore using the Claude API to synthesize them into a natural-language "conditions brief" at the top of the dashboard — something like: *"Cool overcast May morning — good window for garden work, lake still warming toward bass territory, mountain laurel likely opening this week."* This would synthesize weather + fishing + plant calendar + wildlife activity into a single grounded, property-specific read. Implementation would require a lightweight backend or serverless function to proxy the Claude API call (can't call Anthropic directly from the browser without exposing a key).

✓ **Researched May 2026** — every source above (and many more) is verified with endpoints, CORS status, and integration ideas in `research-resources.md`. Prioritized backlog in the next section.

### Research-derived integration backlog

A wide research pass on 2026-05-06 produced `research-resources.md` (~85 verified resources across UGA Extension, native plants, wildlife, watershed, fishing, climate/dark sky/homesteading). Top-priority integrations, ordered roughly by signal-to-effort:

**Surface-fact callouts (low effort, high signal):**
- Property card → "On Cherokee land" subsection. Pickens Co was Cherokee Nation territory 1793–1838; Talking Rock Creek (~6 mi) was a settlement. Link to EBCI Natural Resources + the USFS × EBCI culturally-significant-plants research.
- Property card → "Tate Mountain Estates" historical note. Lake Sequoyah at Tate Mountain Estates (~6.2 mi from the property) was built by Col. Sam Tate around 1929 — gives "Tate Tracker" a real local-historical anchor.
- ~~Wildlife card → "Endemic fish of the Etowah" subtitle~~ **Deferred / probably drop (2026-05-13).** Paul's ground-truth: he has spent significant time in the streams on the property and has never observed these species. Habitat is downstream of the property's 2,959 ft headwater elevation — mainstem Etowah near Dawsonville and larger named tributaries (Long Swamp, Talking Rock). Saying they're on or near the property over-implies proximity; the data was "in the watershed somewhere," not "in the streams you walk." Keep the species in the research file as regional context; don't promote to a dashboard callout without clearer property relevance.
- Property card → "Bortle 3 — Stephen C. Foster SP (Bortle 2) is GA's only IDA-certified site" reference for sky-quality calibration.
- Plants card → keystone genera for Blue Ridge ecoregion (oak ~400+ Lepidoptera, willow, cherry, blueberry, goldenrod) sourced from NWF Keystone Plants by Ecoregion.
- Property card → seasonally-conditional burn-ban banner (May 1–Sep 30 = state ban active; rest of year = permit required via gatrees.org).

**Live data integrations (CORS-enabled, no key):**
- ~~**USGS NWIS streamflow + water temp**~~ ✓ Done (2026-05-13) — gauge 02389150 reports all three params (00060/00065/00010). Surfaced as a "Watershed — Etowah River" panel on the property card with ft³/s, gage, and water temp in °F. (Originally shipped with an Etowah Darter context note; removed 2026-05-13 after Paul flagged that the fish live in downstream river reaches, not in headwater streams at the property's 2,959 ft elevation — see deferred Wildlife-card callout note below.)
- ~~**USGS earthquake events**~~ ✓ Done (2026-05-13) — surfaced as a "Seismic Activity" panel on the property card. Threshold widened to **300 km / M2.0+** because 200 km / M2.5 returned nothing — East TN Seismic Zone activity is mostly small. Shows magnitude badge, place, time-ago, distance, depth, and USGS event link.
- ~~**NWS api.weather.gov skyCover**~~ ✓ Done (2026-05-13) — two-step fetch (`/points` → `/gridpoints/FFC/49,122`), expanded to hourly samples, averaged across tonight's dark window (SunCalc). Renders as a footer strip under the Tonight's Sky grid: "🛰️ NWS dark-window cloud · X% avg · min–max range · Nh".
- ~~**NASA SVS Dial-a-Moon**~~ ✓ Done (2026-05-13) — hero moon image (220px circle) at the top of the celestial card body, hour-of-year indexed in UTC. **Visualization ID must be refreshed annually** when SVS publishes the next year — see `DIAL_A_MOON_VIZ` constant in viewer.html. Currently set to 2026 (`a005587`). A year-guard hides the hero cleanly if the date drifts out of sync.
- ~~**Open-Meteo expansion**~~ ✓ Done (2026-05-13) — added `cloud_cover_low/mid/high,visibility` to `&current=` in `fetchLiveWeather`. New `stargazingFromClouds(cur)` helper weights low cloud 1.0 / mid 0.7 / high 0.4 with a sub-10 km visibility penalty. The Tonight's Sky "Transparency" cell becomes "Stargazing" when live cloud data is present, with the breakdown ("Clouds: X% lo / Y% mid / Z% hi · N km vis") as the sub line; falls back to the old WMO-derived label otherwise.
- ~~**Open-Meteo hourly forecast (with rain)**~~ ✓ Done (2026-05-11) — shipped as the 48-hour hourly strip under the daily forecast tiles. See "Hourly forecast strip" below.

**Live data integrations (need server proxy — not CORS):**
- AirNow AQI chip for Weather card (free key, server proxy needed).
- US Drought Monitor pill (FIPS 13227 = Pickens GA, server proxy).
- NOAA NCEI 1991–2020 normals for "May normal high/low" subtitle (free token, server proxy, monthly cache OK).

**Citizen-science enrollment callouts (Wildlife card):**
- FrogWatch USA (Auburn chapter) — Amphibians monthsActive via frog calls Feb–Aug evenings.
- SE Bumble Bee Atlas (Xerces × GA DNR) — adopt a grid cell, May–Sep field season.
- NestWatch (Cornell) — seasonally surface during Birds-tab nesting windows.
- Project FeederWatch — winter Birds tab mode (Nov–Apr).
- iNaturalist Pickens County — link from each Amphibians species to local observation page.
- Hummingbirds at Home — surface seasonally when Ruby-throated arrives mid-April.

**Per-species deep-dive links (no integration burden, just URL fields):**
- Birds tab → eBird Pickens County bar chart per species (`ebird.org/species/[code]/US-GA-227`).
- Amphibians tab → SREL Herpetology species accounts (`srelherp.uga.edu/...`).
- Plants > Hydrangea card → Mt. Cuba wild hydrangea trial top-performers PDF.

**Programs/certifications worth pursuing (one-time actions, surface in Property card):**
- Homegrown National Park map registration (free) — adds property to national biodiversity map.
- GA Forestry free Forest Stewardship Plan (custom multi-resource plan via 1-800-GA-TREES).
- USFWS Partners for Fish and Wildlife site visit (free habitat-planning consult).
- Birds Georgia Wildlife Sanctuary certification ($110, 5-yr cert, mailable yard sign).
- NRCS EQIP / CSP cost-share (Pickens Co eligible).
- Conservation easement options (Mountain Conservation Trust GA — most aligned mandate).
- Appalachian Beginning Forest Farmer Coalition — strongest fit for shade-grown native NTFPs (ramps, ginseng, sochan, goldenseal) given the property's mature forest.

**Notes & caveats:**
- Lake Sequoyah is in Pickens Co at Tate Mountain Estates (NOT Habersham Co); 38 acres, ~2,800 ft, built ~1929. Likely HOA/private — verify before publishing fishing-regulation content.
- AmericanMeteor / IMO meteor shower data: no API. Manually transcribe ~10 major showers per year into static JSON, refresh annually.
- GA DNR weekly trout stocking: no public JSON API. Either scrape weekly into static cache or link as deep-dive only.
- Time and Date API ($99+): explicitly NOT recommended; compute sun/moon times locally instead.
- March 3, 2026 total lunar eclipse is visible from Georgia — featured-event candidate for the celestial card.

### Photos — birds, amphibians, fishing, plants (✓ Done; vehicles pending Paul's photos)
All four wildlife/plant categories render with a 44×44 thumbnail in the always-visible card header AND a hero photo (~500px) at the top of the expanded body, plus a small italic credit line linking back to Wikimedia Commons.

- **Birds:** 16 species, `images/birds/{id}.jpg`
- **Amphibians:** 12 species, `images/amphibians/{id}.jpg`
- **Fishing (Lake Sequoyah):** 3 species, `images/fishing/{id}.jpg`. Hero only (no thumbnail — fishing uses a tabbed species switcher rather than a row list)
- **Plants:** 13 plants, `images/plants/{id}.jpg`. **Caveat:** several entries are trademarked cultivars (Berry Box® Pyracomeles, Yuki Cherry Blossom® Deutzia, named Clematis hybrids, mixed Hosta, pond Iris). For those, the photo is a genus-level proxy from Commons — see `images/README.md` for the proxy mapping. The `plants.draft.json:qualityPhotosForFutureIntegration` tracker is the place to upgrade these to actual photos of the specimens in the garden.

Each item has a `photo` field (relative path) and `attribution` object (`source`, `author`, `license`, `url`) on the source JSON. Source images are 800px-wide JPEGs (looks sharp at the ~500px hero display on retina, also fine for the 44×44 thumb).

Tooling (unified across all categories):
- `tools/fetch-photos.py --category {birds|amphibians|fishing|plants}` — pulls lead images from Wikipedia/Commons API, writes `images/{cat}/_attribution.json`. Pass `--force` to refresh, or specific ids to refetch a subset. Per-category `PAGE_OVERRIDES` (Wikipedia title) and `FILE_OVERRIDES` (Commons file name) live in the `CATEGORIES` dict at the top of the script.
- `tools/wire-photos.py --category {…}` — merges attribution into the source JSON and re-inlines the corresponding `{CATEGORY}_DATA` constant in `viewer.html`. **Important:** these constants are the live runtime source (no JSON fetch for any of them), so the inline must be kept in sync.

The legacy `tools/fetch-bird-photos.py` and `tools/wire-bird-photos.py` scripts have been superseded — they still work, but new photo work should use the unified scripts.

CSS: `.bio-species-thumb` (44×44, rounded, `object-fit: cover`), `.bio-species-photo` (hero, max-width 500px, natural aspect), `.bio-photo-credit` (small gray italic, right-aligned under hero), and `.plant-thumb` (parallel to bio-species-thumb but in plant-card markup) live near the other relevant CSS rules. Photo `<img>` tags use `loading="lazy"` and `onerror="this.remove()"` for graceful degradation when a file is missing.

Single-file constraint: not violated — the repo already has `tools/`, `weather-history.json`, etc. outside `viewer.html`. The principle is *no build step*, which still holds.

**Next (when Paul provides photos):** vehicles renderer at `viewer.html:3836` currently shows `v.emoji` in `.vehicle-icon`; conditional swap to `<img>` is a one-liner. Drop locally-shot JPEGs into `images/vehicles/{id}.jpg`, no attribution needed.

### Sounds — bird and frog calls (✓ Done)
Vocal species render a small ▶ play button next to their thumbnail in the species row. Clicking plays a single-instance audio (one species at a time — clicking another stops the first). The expanded body shows an audio attribution credit below the photo credit.

- **Birds:** 16/16 species. Files in `sounds/birds/{id}.{mp3|ogg}` — mix of formats depending on what Commons stored.
- **Frogs/toads:** 4 species — Spring Peeper, Upland Chorus Frog, American Toad, Gray Treefrog. Files in `sounds/frogs/{id}.{ogg|wav|mp3}`.
- **Salamanders:** silent — no sound button rendered (correct behavior, not a coverage gap).
- **Amphibians "calling now" badge:** frogs/toads with `monthsActive` including the current month show a small green pill next to their name. Surfaces seasonal context without urgency.

**Coverage gaps (Wikimedia Commons doesn't have proper recordings under tried scientific names):** American Bullfrog, Green Frog, Fowler's Toad. Skipped silently — same treatment as salamanders. Not high-priority since the Spring Peeper / American Toad / Gray Treefrog chorus dominates the property soundscape anyway. To upgrade later, register a xeno-canto v3 API key (free) and extend `tools/fetch-sounds.py` to fall back to xeno-canto for these three.

**Browser support:** All recordings play in Safari/iOS. Commons-sourced Ogg Vorbis files are auto-transcoded to M4A AAC on download by `fetch-sounds.py` using macOS-native `afconvert` (no ffmpeg / brew needed). On non-macOS hosts, transcoding is skipped and the original .ogg is kept — those won't play in Safari/iOS but still work in Chrome/Firefox/Edge. Final mix on disk: 8 .mp3, 8 .m4a (transcoded), 1 .wav, all iOS-friendly.

Each item has a `sound` field (relative path) and `soundAttribution` object on the source JSON, written by `tools/wire-sounds.py`. License filter accepts CC-BY, CC-BY-SA, CC0, and Public Domain (this is a personal dashboard — NC-restricted licenses would also be fine if needed).

Tooling:
- `tools/fetch-sounds.py --category {birds|frogs}` — Commons audio search by scientific name, license-filtered, size-bounded (50KB–8MB to skip both snippets and field tapes), URL-derived extension. Re-runnable; passes `--force` to refresh, or specific ids.
- `tools/wire-sounds.py --category {birds|frogs}` — merges into JSON, re-inlines `BIRDS_DATA` / `AMPHIBIANS_DATA` const, prints a sanity-check sound-field count after re-inlining.

CSS: `.bio-sound-btn` (30px circular, green when playing), `.bio-calling-now` (small badge), `.bio-sound-credit` (parallel to `.bio-photo-credit`).
JS: single global `SoundPlayer` IIFE coordinates a single `Audio` instance — clicking another button stops the first. Audio uses `preload="none"` so the file isn't fetched until playback.

## Pending design improvements (prioritized)

1. ~~**Mobile dashboard strip** — 3-column grid wraps awkwardly at 390px~~ ✓ Done.
2. ~~**Body background** — subtle grain/noise texture~~ ✓ Done — layered SVG fractalNoise over the gradient.
3. ~~**Extend Crimson Text** — Card titles use serif~~ ✓ Done (was already in place; verified).
4. **Card expand animation** — Currently hard-toggles. Add CSS `grid-template-rows: 0fr → 1fr` or max-height transition.
5. ~~**"REFERENCE" section divider** — needed more visual weight~~ ✓ Done — serif italic Crimson Text label, fade-to-clear gradient lines.
6. ~~**Dashboard strip stat hierarchy** — values needed more visual weight~~ ✓ Done — 17px → 20px, weight 600 → 700, darker color.
7. ~~**Header breathing room** — 22px → 32px padding, h1 30px~~ ✓ Done.

## Active drafts (not yet promoted to live data)

These files are staging areas. Do **not** wire them to the viewer until the user says go.

- **`vehicles.draft.json`** (schema v3, 15 items) — proposes splitting flat array into `group: "vehicle" | "equipment"` and adds a per-item `maintenance` block (fuel, oil, sparkPlug, filters, consumables) with `confidence: verified | inferred | tbd` tags. New equipment added: Kobalt KM2040X-06 mower, Echo PB-7910T backpack blower, Echo PB-250LN handheld blower, Homelite UT33650A trimmer, Homelite gas blower/vac (model not stickered — likely UT09521 family). Husqvarna riding mower fully fleshed out from the on-unit replacement-parts sticker (Kawasaki FR691V, 54" deck, all part numbers verified). Husqvarna model number itself still TBD (sticker not yet found).
- **`plants.draft.json`** — five new plants identified: Berry Box® Pyracomeles (USPP35913, verified by Pike Nursery tag), Yuki Cherry Blossom® Deutzia (NCDX2, verified by tag), Clematis (genus high; cultivar uncertain), Hostas (genus high; cultivars uncertain), pond Iris (genus high; species likely Blue Flag). **Care calendars filled out for all 5** in proper plants.json schema (under `plantsForPromotion`) — ready to lift directly into `plants.json.plants[]`. The `promotionChecklist` block in the draft documents the exact lift-and-paste workflow. Also tracks `qualityPhotosForFutureIntegration` — quality reference photos flagged for the future "real photos in the dashboard" enhancement.

## Uncommitted work in progress

These edits are local-only — not yet committed or pushed:

- **Phase 5 station-aware alerts** in `viewer.html` — generateAlerts() refactored, per-alert source chips, dedup. Pending visual verification + commit.
- **Phase 6 archive scaffolding**: `weather-history.json` (5 days seeded) and `tools/record-daily-rollup.mjs` + `tools/README.md`. Pending decision on scheduling approach (launchd vs GitHub Action).

## Outstanding asks for Paul

1. **Husqvarna riding mower:** model sticker (under seat or rear fender) — need the specific Husqvarna SKU like TS354XD / YTH24K54 / GTH54LS.
2. **Homelite trimmer:** confirm UT33650A (straight shaft) vs UT33550A (curved shaft) — middle digit on EPA sticker is slightly ambiguous.
3. **Homelite blower/vac:** no model sticker found on the unit. Maintenance specs are inferred from the trimmer's engine family (HHCPS.0264AT). Acceptable for at-a-store reference.
4. **Annual: NASA SVS Dial-a-Moon visualization ID** — when SVS publishes the 2027 visualization (usually Dec/Jan), update the `DIAL_A_MOON_VIZ` constant in viewer.html (`year`, `parent` bucket, `id`). Find the new ID at svs.gsfc.nasa.gov/gallery/moonphase. Until refreshed, the moon hero hides cleanly once the year flips.

## Next steps after the drafts go live

- Viewer needs updating to render the new `vehicles.json` v3 with the `group` split (vehicle vs equipment) — likely two collapsible sub-sections inside the Vehicles & Equipment card, or two tabs.
- Viewer needs updating to render the new plants once their care calendars are filled in.
- Backfill maintenance blocks have already been written for all carried-over v2 items in the draft.

## Location constants

| Field | Value |
|---|---|
| Address | 282 Church Mountain Road, Jasper, GA 30143 |
| Coordinates | 34.5496°N, 84.3674°W (confirmed via Google Maps + Open-Meteo elevation API, May 2026; previous 34.52, -84.46 pointed near Jasper town center and was wrong) |
| Elevation | 2,959 ft (confirmed; 1,424 ft above KJZP baseline) |
| USDA Zone | 6b (elevation-adjusted); 7b official county |
| Last frost 50% | May 3 |
| Last frost 90% safe | May 24 |
| First frost 50% | October 17 |
| PWS | KGAJASPE279 (Weather Underground) |
| Sky quality | Bortle 3 (rural dark sky) |
