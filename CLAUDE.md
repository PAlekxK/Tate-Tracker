# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project purpose & tone

Fernwood is a **personal property reference dashboard** for 282 Church Mountain Road, Jasper, GA 30143 — a rural mountain property at 2,959 ft elevation in the Blue Ridge, within Tate Mountain Estates. "Fernwood" is the property's name; "Tate Mountain Estates" is the surrounding 1920s mountain development, separate from the nearby town of Tate. It is hyper-personalized, not a generic app.

**Project rename history:** Originally "Tate Tracker" (named for Col. Sam Tate / Tate Mountain Estates); renamed to "Fernwood" on 2026-05-19 to name the actual property rather than the surrounding development. Repo path, GitHub repo, Worker URL, localStorage keys, and most internal var names retain `tate-tracker` / `tateTracker` for now — those are infrastructure-level identifiers, not user-facing, and renaming them carries data-migration risk (existing observations). Rename them only if a clear reason emerges.

**Tone is everything here.** This is a fun, evocative reference tool — a field journal, not a task manager. Language like "17 actions due" or "3 alerts" is wrong for this project. Prefer "What's happening in May" or "Worth checking this month." The dashboard should feel like looking out at the land, not a to-do list with deadlines.

## How to run

Open `viewer.html` directly in a browser — no build step, no server, no install. For Playwright testing or CORS-sensitive API testing, serve locally:

```bash
cd /Users/paulkirschenbauer/Documents/Claude/Projects/Tate-Tracker
python3 -m http.server 8765
# then open http://localhost:8765/viewer.html
```

## Architecture

`viewer.html` is a single ~4,600-line self-contained file: all CSS, JS, and inlined JSON data live in one file. There is no build system, no module bundler, no framework. The JSON files (`plants.json`, `fishing.json`, etc.) are the source of truth for data — they are fetched at page load and the inlined copies in `viewer.html` serve as fallback. When updating data, edit the JSON files and re-inline them.

### Data layer

All domain data is loaded as JS constants from inlined JSON at the top of the script section (~line 1550):

- `PLANTS_DATA` — 17 plants with per-plant care calendars (schema v3). Care entries have `months[]`, `peakWindow`, `narrow` (boolean for timing-critical windows), and optional `subcategories[]`.
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

### ~~Phase 5 — station-aware alert engine~~ ✓ Done (live)
`generateAlerts()` produces both station-driven and forecast-driven alerts. Station alerts: heavy/steady/light rain in progress, saturated soils, hot now, freezing now, high gusts now, pressure dropping fast, station battery low. Forecast alerts: freeze tonight, hard freeze, heat stretch, good seeding window, heavy rain/storms coming, damaging/gusty winds, excellent outdoor work day. Each alert renders a per-alert source chip (📡 Station / ☁️ Forecast) — green for station, blue for forecast. Dedup logic via `stationCovers.{cold,heat,rain,wind}` flags: forecast "Heavy Rain Today" suppressed when station's already firing an in-progress rain alert; forecast wind suppressed when station gust alert active; same pattern for cold/heat. Sort: severity tier first, station before forecast within tier. Source-chip render path completed and live 2026-05-13.

### Phase 6 — long-term archive — fully wired ✓ (accumulating)
- New `weather-history.json` at repo root holds daily rollups (min/max/avg for temp, humidity, wind, rain, pressure, solar, UV, indoor sensors).
- New `tools/record-daily-rollup.mjs` — Node 18+ script (zero deps) that fetches Ambient Weather, builds a daily rollup, and merges it into `weather-history.json`. Idempotent — re-running on a day already recorded replaces it. See `tools/README.md` for usage.
- Already backfilled: 5 days (May 2 partial, May 3, May 4, May 5, May 6 partial).
- **GitHub Action live as of 2026-05-13** at `.github/workflows/record-weather.yml` — runs every 6 hours plus a "finalize previous day" pass. Bot commits any updates back to `main`, which triggers a Pages redeploy automatically. Both required secrets (`AMBIENT_APP_KEY`, `AMBIENT_API_KEY`) are configured in repo settings. The local launchd alternative is documented in `tools/SCHEDULING.md` but the GitHub Action is the chosen path.
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
- Property card → "Tate Mountain Estates" historical note. Lake Sequoyah at Tate Mountain Estates (~0.3 mi from Fernwood — the property is effectively *in* Tate Mountain Estates) was built by Col. Sam Tate around 1929. **Distance correction logged 2026-05-18:** prior `~6.2 mi from the property` figure was a misread of research-resources.md's "6.2 mi from Jasper [town]" — the property's Jasper mailing address is rural and the property sits adjacent to the lake.
- ~~Wildlife card → "Endemic fish of the Etowah" subtitle~~ **Deferred / probably drop (2026-05-13).** Paul's ground-truth: he has spent significant time in the streams on the property and has never observed these species. Habitat is downstream of the property's 2,959 ft headwater elevation — mainstem Etowah near Dawsonville and larger named tributaries (Long Swamp, Talking Rock). Saying they're on or near the property over-implies proximity; the data was "in the watershed somewhere," not "in the streams you walk." Keep the species in the research file as regional context; don't promote to a dashboard callout without clearer property relevance.
- Property card → "Bortle 3 — Stephen C. Foster SP (Bortle 2) is GA's only IDA-certified site" reference for sky-quality calibration.
- Plants card → keystone genera for Blue Ridge ecoregion (oak ~400+ Lepidoptera, willow, cherry, blueberry, goldenrod) sourced from NWF Keystone Plants by Ecoregion.
- Property card → seasonally-conditional burn-ban banner (May 1–Sep 30 = state ban active; rest of year = permit required via gatrees.org).

**History & cultural heritage callouts (Cat 7) — ✓ Shipped 2026-05-19.**
- Property card → "The original Appalachian Trail" callout (Mount Oglethorpe terminus 1937-1958) ✓
- Property card → "A Unionist county" callout (Union flag over Pickens courthouse, Company D of 1st GA Infantry to Union Army) ✓
- Property card → "On Cherokee land" callout expanded with Sanderstown, Taloney/Carmel Mission, Federal Road ford, Fort Newman stockade ✓
- Property card → "Tate Mountain Estates" callout expanded to fold in Lake Sequoyah naming + Connahaynee Lodge timeline + bankruptcy + 1946 fire ✓
- Property card → "Worked marble, eight hundred AD" callout (Native marble workings + Georgia Marble Co. + ~60% of DC monuments) ✓

**Rare & restorative plants callouts (Cat 2) — ✓ Shipped 2026-05-19.**
- Property card → "Natural Community" row in Location & Elevation panel: "Mesic Cove / Montane Oak mosaic" ✓
- Property card → Habitat certifications mini-list in Local Resources panel (Birds Georgia / GNPS / Homegrown National Park) ✓
- Plants card → "On this slope" section appended below tab views with four callouts:
  - "Rare species worth looking for" (rich-cove special-concern species) ✓
  - "This slope was once chestnut canopy" (historical-ecology + TACF Restoration Chestnut 1.0) ✓
  - "Hemlocks at this elevation" (HWA threat + treatment protocol + survival data) ✓
  - "Sourcing" (ethical-provenance nurseries + UGA SBG/GNPI recommended-nurseries PDF) ✓
- Conditional "Hemlock check-in" reminder during HWA peak windows — **still pending** (deferred; needs conditional-rendering plumbing). The educational content lives in the "Hemlocks at this elevation" callout for now.

**Places to visit nearby (Cat 7 day-trips seed list, added 2026-05-19):**
- **Georgia Marble Company / Village of Tate marker** (Georgia Historical Society, 1999) at Tate Cemetery on GA-53 — primary-source historical marker ~5 min from the property.
- **Tate House** — Col. Sam Tate's 1921-1926 marble residence, now operating as a wedding venue.
- **Eagles Rest Park / Mount Oglethorpe summit** — original AT southern terminus.
- **Pickens Historical Society sites** (Jasper): Old Jail (1906), Mountain Heritage Cabin, Nelson-Simmons-Trippe House.
- **Hwy 136 bridge at Talking Rock Ford** — Federal Road crossing site near the Sanderstown / Carmel Mission / Fort Newman area.
- **Pickens County Courthouse** (Jasper, 1949) — built with Tate marble; site of the famous "Union flag" episode.

### Local events / day-trips calendar integration (Cat 8, scoped 2026-05-19)

**Scope:** Recurring annual events within ~45 min drive of the property — Pickens (Jasper, Tate, Talking Rock), Gilmer (Ellijay), Fannin (Blue Ridge), Lumpkin (Dahlonega). ~15-20 confirmed events spanning festivals, markets, holiday events, rodeo, outdoor adventures.

**Feed availability verdict (probed 2026-05-19):**
- No source within day-trip distance publishes an iCal/ICS/RSS feed.
- Visit Pickens GA's community calendar uses the QEM (Quick Event Manager) WordPress plugin — no iCal endpoint by default. Confirmed via probes of `/events/?ical=1` (404) and `/community-calendar/?ical=1` (HTML).
- Explore Georgia's state calendar is bot-protected (HTTP 403 on automated fetches).
- Facebook Events no longer reliably expose public iCal.
- Individual event sites (Marble Festival, Apple Festival, JeepFest, Bear on the Square, etc.) are single-event static pages.

**Architecture decision:** Manually-curated `events.json` at the project root. Annual review cadence; spot-check 30 days before each event for date confirmation. The trade-off vs. live feeds: lower freshness, but full editorial control over which events surface and how they're framed.

**Schema (initial draft in `events.json`):**
- `_meta`: `lastUpdated`, `scope`, `refreshCadence`
- `events[]`: `id`, `name`, `location`, `county`, `driveMin`, `dates` (specific YYYY-MM-DD range when known), `pattern` (e.g., "First weekend of October" — fallback for years when dates aren't yet confirmed), `type` (tags), `url`, `notes` (1-2 sentences in field-journal voice)

**Dashboard integration plan (deferred, not built yet):**
- Add an Events card to viewer.html, between Wildlife and Plants.
- Renderer sorts by upcoming `dates`; falls back to `pattern` when `dates` is in the past or missing.
- Surface the 3 next upcoming events on the Property card as a chip strip ("Next nearby — Marble Festival Oct 3-4 · Heritage Days Oct 17-18 · Apple Festival Oct 10-11").
- "Why it matters here" links from history-anchored events (Marble Festival, Heritage Days, Tate Day) back to the Cat 7 Property card historical content.

**Annual maintenance ritual:**
- Each January, refresh the `dates` field for the upcoming year by visiting each event's primary URL (listed in Cat 8 of research-resources.md).
- Mid-year: spot-check any event 30 days out for cancellation/date-shift.

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
- ~~NOAA NCEI 1991–2020 normals for "May normal high/low" subtitle~~ **Dropped 2026-05-18.** `fetchClimateNormals()` already computes 30-year normals from Open-Meteo's archive API client-side (no token needed) — covers the same use case at the property coordinates without the NCEI signup or proxy hop.

**Citizen-science enrollment callouts (Wildlife card) — shipped then deactivated 2026-05-13.**

Original shipment included FrogWatch USA (Amphibians, Feb–Aug), NestWatch (Birds, Apr–Aug), Project FeederWatch (Birds, Nov–Apr), and iNaturalist Pickens County (both tabs, year-round). Hummingbirds at Home was dropped from MVP (Audubon program deprecated). SE Bumble Bee Atlas was deferred to the Plants card.

**Deactivated same-day** at Paul's request — pending review of whether to surface programs that involve uploading observations to external services. The implementation is preserved as dormant scaffolding:
- `citizenScience` arrays remain in `birds.json` and `amphibians.json`
- `renderCitizenSciencePanel()` function and `.bio-take-part-*` CSS classes remain in `viewer.html`
- The two render calls in `renderBirds()` and `renderAmphibians()` are commented out with a clear marker

Re-enabling later is a two-line uncomment. If the decision is to drop permanently, delete the CSS / function / data arrays then.

**Per-species deep-dive links (no integration burden, just URL fields):**
- ~~Birds tab → eBird Pickens County bar chart per species~~ ✓ Done 2026-05-13. `ebirdCode` field added to all 16 birds.json species; renderer surfaces a `📊 eBird · Pickens Co.` chip on each species detail. Codes validated against the eBird taxonomy API.
- ~~Amphibians tab → SREL Herpetology species accounts~~ ✓ Done 2026-05-13. `srelUrl` field added to 11 of 12 amphibians.json species; renderer surfaces a `📚 SREL Herpetology` chip when present. The slug pattern is WordPress-style (`/frogs-and-toads/{slug}/` or `/salamanders/{slug}/`) and SREL's slug doesn't always match the common-name kebab-case (e.g., Green Frog → `green-bronze-frog`, American Bullfrog → `bullfrog`). **Red-backed Salamander has no SREL page** — see Outstanding asks #7 for species-ID question.
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
- **Plants:** 17 plants, `images/plants/{id}.jpg`. **Caveat:** several entries are trademarked cultivars (Berry Box® Pyracomeles, Yuki Cherry Blossom® Deutzia, named Clematis hybrids, mixed Hosta, pond Iris, Summer Cascade® Wisteria, Elpis Clematis, DreamCloud® Hydrangea). For those, the photo is a genus-level proxy from Commons — see `images/README.md` for the proxy mapping. The `plants.draft.json:qualityPhotosForFutureIntegration` tracker is the place to upgrade these to actual photos of the specimens in the garden.

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

## Elevation calibration

**Property is 2,959 ft, not 1,750 ft.** The original data was written with a stale assumption (1,750 ft, derived from Lake Sequoyah's ~2,800 ft mistakenly attributed to the property). `property.json` is the source of truth: 2,959 ft confirmed via Open-Meteo elevation API at coordinates 34.5496°N, 84.3674°W (May 2026), 1,424 ft above KJZP baseline (1,535 ft).

Cleanup completed 2026-05-13 across `plants.json`, viewer.html's inlined `PLANTS_DATA`, and README.md:
- Numeric `elevation_ft`, "~1,750 ft" prose references, hardiness zone (7a → 6b), and KJZP delta strings all corrected.
- Frost-date `_meta` (`lastFrost_50pct`, `lastFrost_90pctSafe`, `firstFrost_50pct`) shifted from April 30 / May 21 / October 20 → May 3 / May 24 / October 17 to match `property.json` `atPropertyElevation`.
- Schema notes / data sources updated from "+7 days spring / -7 days fall" to "+10 days spring / -10 days fall."
- All `peakWindow` and `currentSeasonNote` dates in the **8 original plants** (white-pine, azalea, hydrangea, dogwood, boxwood, holly, mountain-laurel, japanese-maple) shifted +3 days for Jan–Jul dates / -3 days for Aug–Dec dates. The 5 plants promoted from `plants.draft.json` (pyracomeles, deutzia, clematis, hosta, iris-pond) were authored at 2,959 ft and needed no shift.

**Known imprecisions:** the +3/-3 shift relies on lapse-rate math (7 days per 1,000 ft); Paul's direct phenological observation is more authoritative if anything reads obviously off. Some descriptive prose still uses vague phrases ("mid-May to early June," "early summer") that weren't shifted — those are approximate to begin with and should be tightened only if a specific entry reads wrong on the ground.

## ~~Next major pass — holistic UX + copy review~~ ✓ Done 2026-05-18

The holistic review ran on 2026-05-18 with three parallel agents (ux-expert, content-steward, user-researcher). Artifacts at `review/2026-05-18/` — `ux-findings.md`, `copy-findings.md`, `future-ideas.md`, `existing-wildlife-audit.md`, `property-card-content.md`, `plant-guide-drafts.md`, and `SYNTHESIS.md` (the consolidated punch list with phase plan and resolved-questions log).

**Shipped on 2026-05-18:**
- **Wildlife audit** — 48 species through the depth filter, zero deletions, 8 prose softenings + Lake Sequoyah distance fix (~6.2 mi misread → 0.3 mi corrected; property is effectively *in* Tate Mountain Estates).
- **Phase 1 mechanical cleanup** (12 items) — dropped wildlife traffic-light glyphs, ~20 meta-chip emojis, Sky & Stars decorative glyphs, celestial star ratings, fishing verdict emojis, ✓ checkmark on Plants empty state, ⚠ on snake safety panel, in-page "Reference" divider; recolored `.maint-conf-tbd` (red → gray) and peak-window chips (yellow → green); softened `.alert.severe` chrome (red → warm amber).
- **Phase 2 voice rewrites** (6 items) — alert subsystem (~17 NWS-bulletin titles → observational + body softening + dropped all-caps), fishing verdict text ("Lake is sluggish — fish all deep, cold, and slow"), header subtitle (*"An Appalachian Almanac for 282 Church Mountain Road"* — Sand County Almanac touchstone), 4 empty-state copy rewrites, Vehicles card summary + Crimson-italic intro, all 17 plant `guide` first sentences anchored in this property, `currentSeasonNote` opener variety across 13 plants.
- **Phase 4.1 Property card upgrade** — Crimson-italic Sand County Almanac-register lead paragraph at top, plus six surface-fact callouts (Tate Mountain Estates, On Cherokee land, A Bortle 3 sky, Keystone plants, Outdoor burning, Homegrown National Park).
- **Phase 4.2 Mammals tab** — new tab in the Wildlife card with 17 curated species (white-tailed deer, eastern gray squirrel, chipmunk, cottontail, groundhog, raccoon, opossum, striped skunk, red fox, gray fox, coyote, black bear, bobcat, river otter, beaver, southern flying squirrel, bats). Schema mirrors `birds.json`. Renderer parallels existing wildlife tabs.
- **Phase A week-tier surfacing** (locked-sequence start) — header date softened from uppercase letter-spaced productivity chrome to journal-voice serif italic with week-tier prefix ("Mid May · Monday, May 18"). Plants dash tile gets a "Peak this week" callout for plants whose any `peakWindow` contains today; Wildlife dash tile gets "Arriving this week" / "Leaving this week" callouts derived from bird `arrivalWindow` / `departureWindow` (matched against the first/last edge token only, so a Late-April arrival doesn't keep saying "arriving" in mid-May). Render-layer helpers (`weekTier`, `parseShortDateRange`, `parseSeasonalEdge`) live near the top of the script block.
- **Phase B Field Notes write surface** — new "Field Notes" main card between Property and Vehicles, with a journal-voice intro, write-entry button, list of past observations sorted newest-first, and per-entry delete. Write modal collects date (defaults to today), category (10 choices including the 7 wildlife/plants tabs + weather/property/other), optional species picker (auto-populated from the matching `*_DATA` constant), and body text. **Voice dictation** via Web Speech API (`webkitSpeechRecognition` on iOS Safari; standard `SpeechRecognition` elsewhere) — mic button bottom-right of textarea, pulses red while listening, transcript streams in as interim text and commits on each phrase boundary. Storage is `localStorage` under `tateTracker.observations.v1` (~5MB quota; photos deliberately not in v1). Cross-card "Recent observations" surfacing is Phase B v2.
- **Phase C1 cross-device sync** — a small Cloudflare Worker (`worker/worker.js` + `wrangler.toml` + `README.md`) backs Field Notes observations with KV storage so entries follow Paul between phone, tablet, and laptop. Endpoints: `GET/POST /api/observations`, `DELETE /api/observations/:id`, plus an auth-free `/health` for setup verification. All `/api/*` calls require an `X-Tate-Token` header matching a `SHARED_TOKEN` Worker secret. Client side has a new `ObservationStore` IIFE that tries the Worker and falls back to localStorage (the original Phase B cache), with optimistic local writes so the UI feels instant. Sync status surfaces in two places: a small pill on the Field Notes card header ("Synced" / "Local only" / "Sync error") and an in-body banner with a "Sync settings" button. The settings modal collects the Worker URL and shared token, calls `/health` and `/api/observations` to verify auth, then saves the config to localStorage under `tateTracker.sync.v1`. On first successful refresh after configuring sync, any local-only entries get uploaded to the Worker — so entries Paul wrote pre-sync don't disappear. Cost: $0 at expected volume (Workers + KV free tier). Live Worker URL: `https://tate-tracker.paul-kirschenbauer.workers.dev`.
- **Phase C2 worker-backed features** — three new endpoints on the same Worker:
  - `GET /api/airnow?lat=&lon=` — AirNow current AQI (15-min KV cache). Dashboard surfaces an AQI chip on the Weather card summary using the chip color scale (good/moderate/UFSG/unhealthy/very-unhealthy).
  - `GET /api/drought?fips=` — US Drought Monitor severity by county FIPS (6-hr cache). Dashboard appends a "Drought status" callout to the Property card immediately after "Outdoor burning, by season."
  - `POST /api/today-line` — Claude Haiku 4.5 synthesis of the day, anchored in current weather + plants in peak + birds arriving/leaving + lake state. Cached 24h by date (one Claude call per day, ~$0.01/day). Surfaces as a journal-voice italic banner under the header subtitle.
  - Secrets required (each fails gracefully with 503 → dashboard hides the feature): `AIRNOW_API_KEY` (airnowapi.org), `ANTHROPIC_API_KEY` (console.anthropic.com). NCEI normals endpoint dropped — `fetchClimateNormals()` already computes 1991-2020 normals from Open-Meteo archive client-side, no token needed.
  - Client side: `WorkerAPI` IIFE shares config with `ObservationStore`. Three fetchers (`fetchAirNowAQI`, `fetchDroughtStatus`, `fetchTodayLine`) run after the existing weather fetchers and degrade silently when the Worker isn't configured or a secret is missing. `gatherTodayState()` snapshots the dashboard state into a compact JSON brief for the Claude prompt.

**Decisions locked from the 2026-05-18 walk-through** (full table in SYNTHESIS.md):
- Dual-frame identity: voice = field journal; form = Appalachian Almanac. Touchstone = Aldo Leopold's *A Sand County Almanac*. See [[project_tate_tracker_tone]].
- Depth filter for all coverage decisions: only what Paul realistically observes on this property. See [[feedback_tate_tracker_depth_filter]].
- Server proxy: green-lit and shipped (Cloudflare Worker handles AirNow / Drought Monitor / AI today-line; NCEI normals dropped — Open-Meteo archive covers that client-side).

## Pending design improvements (prioritized)

1. ~~**Mobile dashboard strip** — 3-column grid wraps awkwardly at 390px~~ ✓ Done.
2. ~~**Body background** — subtle grain/noise texture~~ ✓ Done — layered SVG fractalNoise over the gradient.
3. ~~**Extend Crimson Text** — Card titles use serif~~ ✓ Done (was already in place; verified).
4. ~~**Card expand animation**~~ ✓ Done — `.main-card-body` uses a max-height + opacity transition with cubic-bezier(0.4, 0, 0.2, 1). Sub-card expanders (`.bio-species-body`, `.plant-body`, `.care-block-body`) still hard-toggle; left as-is — they sit inside an already-animating parent and a second nested animation read worse in testing.
5. ~~**"REFERENCE" section divider** — needed more visual weight~~ ✓ Done — serif italic Crimson Text label, fade-to-clear gradient lines.
6. ~~**Dashboard strip stat hierarchy** — values needed more visual weight~~ ✓ Done — 17px → 20px, weight 600 → 700, darker color.
7. ~~**Header breathing room** — 22px → 32px padding, h1 30px~~ ✓ Done.

## Active drafts (not yet promoted to live data)

These files are staging areas. Do **not** wire them to the viewer until the user says go.

- ~~**`vehicles.draft.json`**~~ **Promotion complete 2026-05-13.** v3 schema (group split + per-item maintenance blocks) is fully live in `vehicles.json` and the inlined `VEHICLES_DATA` in viewer.html. Renderer at `renderVehicles()` filters into Vehicles (7) and Equipment (8) headers with counts; each item renders a maintenance toggle showing `value` + `confidence` chip (`verified` | `inferred` | `tbd`). The draft file itself is now a working-doc archive — `openQuestions` (Husqvarna SKU, Homelite trimmer model, Homelite blower/vac model) still tracked there and in "Outstanding asks for Paul" below.
- ~~**`plants.draft.json`**~~ **Promotion complete 2026-05-13.** All 5 plants (Berry Box® Pyracomeles, Yuki Cherry Blossom® Deutzia, Clematis, Hostas, pond Iris) are live in `plants.json.plants[]` and inlined in viewer.html's `PLANTS_DATA` constant. Verified renders at that point: 13 plants total. **Subsequent additions (2026-05-16):** butterfly weed, Summer Cascade® wisteria, Elpis clematis, and DreamCloud® hydrangea — bringing live `plants.json` to 17 entries. The `plantsForPromotion` and `promotionChecklist` blocks have been removed from the draft; `qualityPhotosForFutureIntegration` remains as the active tracking list for upgrading proxy photos to in-garden specimen shots.

## Uncommitted work in progress

(None — all sections currently in sync with the remote.)

## Forward direction — toward a field assistant (Phases D / E / F)

**Raised by Paul mid-C2 on 2026-05-18.** The Field Notes card I built in Phase B is a structured log. What Paul actually wants is a *field assistant* — a conversational interface that already knows this property in depth (every plant, every species, every past observation, the soils, the elevation, the frost dates, the lake) and that he can talk to in plain language, including photo input ("here's a picture of my Azalea. What's wrong with it?"). The structured journal becomes a side effect of the conversation, not the primary surface.

This is a real product shift. The current Field Notes UI (form modal with category/species pickers) is a stepping stone, not the destination. The path:

| Phase | Scope | Status |
|---|---|---|
| **D — Capture UX rebuild** | Replace the Field Notes modal with a single always-visible text box + mic at the top of the card. Drop the category and species pickers from the user-facing form entirely. Timestamp captured automatically. A `POST /api/classify` Claude call assigns category/speciesId behind the scenes after save. | ✓ Shipped 2026-05-19 (commit 783e72c). Worker `/api/classify` endpoint live; inline composer + async classify wired; fuzzy species matching against curated *_DATA. |
| **E — Conversational layer** | Multi-turn chat with the full property context as the system prompt — `plants.json`, `birds.json`, `mammals.json`, `amphibians.json`, `snakes.json`, `lizards.json`, `fishing.json`, `property.json`, the active observations, and the current weather state. Use Claude tool-use so the model can look up specific records on demand rather than stuffing everything into context every turn. | Scoping doc at `PHASE_E_DESIGN.md` (2026-05-19) — open questions surfaced, no implementation yet. |
| **F — Image input** | Photo upload on the chat surface (mobile-first — camera roll + capture). Use Claude's vision endpoint. Decide whether images persist with their associated entry (visual journal) or are transient Q&A inputs only. | Not started. |

**Constraints to honor:**
- The depth filter still applies: the assistant references only the property's actual scope (the 17 curated plants, 17 mammals, etc.), not regional completeness.
- Field-journal voice in both directions — the assistant doesn't lapse into "Here are 5 tips for caring for your Azalea." It speaks as someone who knows *this* azalea on *this* property.
- All API costs flow through the existing Worker with the existing `X-Tate-Token` auth. Per-call cost matters because conversations are multi-turn; consider Haiku for routine turns and reserve Sonnet/Opus for image-vision or long-context queries.

**Phase G — observations as a knowledge layer (direction raised 2026-05-19):** Field notes shouldn't just live as a structured log; they should feed back into other dashboard surfaces and sharpen recommendations over time. Concrete examples: Plants card "You noted the laurel opening April 25 last year — watch for it now"; Wildlife "Your first hummingbird last spring was April 18"; today-line grounded in recent observations not just live state; conversational assistant (Phase E) referencing past notes every turn. Don't build until Phase E lands and the observation set is rich enough (~50+ entries) to be useful. Voice rule: when a callout cites a past observation, it should sound like memory ("you noted X last year") not like a database row. See memory `project_tate_tracker_observations_feedback_loop.md` for the full thread.

**Plants to consider planting (direction raised 2026-05-19):** A curated reference for native species, protected/at-risk plants worth fostering, and anything that supports the local ecology — distinct from `plants.json` which tracks what's *already* on the property. Initial framing + seed entries in `plants-to-consider.md` at the repo root. Pulls heavily from existing research-resources.md Cat 2 (chestnut + hemlock restoration, rich-cove special-concern flora, GPCA partner network, Mt. Cuba Center trial reports for native cultivars, ethical-provenance nursery list). When this thread becomes active: decide on structured schema (mirror plants.json) vs free-form markdown, and start populating zone-affinity hints once map zones are stable. Connects naturally to the map view (zone affinity per candidate), Phase E (assistant can answer "what could I plant near the pond"), and Phase G (observations that find a species already present can promote it from "considering" to "found").

**Property map view (direction raised 2026-05-19):** A spatial surface — currently everything is by-time (calendars, peak windows, months). Paul wants a map of the property with sections/numbers/icons showing roughly where plants live. Explicit scope note from him: *doesn't need to be down to exact coordinates, but at least groups of plants in different little areas of the property.* Zone-level granularity is enough.

This is structurally different from existing surfaces because it introduces a spatial axis. It connects to several existing threads but doesn't depend on any of them:
- Microclimate aspects (south-southwest / north-northeast / east / west) on the Property card already imply zones — those could be the seed zone vocabulary.
- Each plant could gain a `location` or `zoneId` field on `plants.json` pointing to one of the named zones.
- Wildlife habitat zones could overlay later (fairway edge, forest interior, pond, near-spring) — the `habitatContext` field in `mammals.json` and `birds.json` already names some of these informally.
- Field-note observations could carry an optional zone in Phase G, turning the map into "where on the property has X been seen."

Open questions for when the thread becomes active:
- **Zone vocabulary** — what zones does Paul actually think in? Candidates: front fairway, pond edge, north-side slope, east-side plantings, the house perimeter, the spring drainage, deep woods. Needs his naming pass before any code.
- **Map base** — aerial photo from Google Earth (photographic), hand-drawn diagram (Sand County Almanac aesthetic, but commissioning art), or stylized SVG zones with no base image (lightest). Probably the SVG-zone path for v1; revisit later.
- **Interaction model** — click a zone → list the plants in it (and later, wildlife seen + observations made there); click a plant → highlight its zone; hover for preview.
- **Where it lives** — new tab in the Plants card, or new main card, or appended to Property card. Map view feels heavyweight enough for its own card.
- **Scope of overlays** — plants only (v1), or plants + wildlife habitat + observations from the start?

Don't start building until Paul has done a zone-naming pass. The hardest part of this thread isn't the SVG or the renderer — it's deciding what zones the property has and how they correspond to where plants actually live.

## Deferred for Paul

~~**Code & logic walkthrough.**~~ ✓ Done 2026-05-19. `STACK_TOUR.md` at repo root covers the entire stack (GitHub Pages, viewer.html single-file pattern, JSON inline pattern, Cloudflare Worker + KV + secrets, dashboard ↔ Worker auth, localStorage cache+fallback, Web Speech API, weather-history GitHub Action, deployment paths, cost summary, glossary). Survives chat scrollback.

## Outstanding asks for Paul

1. **Husqvarna riding mower:** model sticker (under seat or rear fender) — need the specific Husqvarna SKU like TS354XD / YTH24K54 / GTH54LS.
2. **Homelite trimmer:** confirm UT33650A (straight shaft) vs UT33550A (curved shaft) — middle digit on EPA sticker is slightly ambiguous.
3. **Homelite blower/vac:** no model sticker found on the unit. Maintenance specs are inferred from the trimmer's engine family (HHCPS.0264AT). Acceptable for at-a-store reference.
4. **Annual: NASA SVS Dial-a-Moon visualization ID** — when SVS publishes the 2027 visualization (usually Dec/Jan), update the `DIAL_A_MOON_VIZ` constant in viewer.html (`year`, `parent` bucket, `id`). Find the new ID at svs.gsfc.nasa.gov/gallery/moonphase. Until refreshed, the moon hero hides cleanly once the year flips.
5. ~~**Push the weather-history GitHub Action workflow + add repo secrets**~~ ✓ Done 2026-05-13. Workflow live at `.github/workflows/record-weather.yml`; both `AMBIENT_APP_KEY` and `AMBIENT_API_KEY` configured as repo secrets. First scheduled run will fire at the next 6-hour cron mark (UTC 18:00 / 00:00 / 06:00 / 12:00).
6. ~~**Rotate the GitHub fine-grained PAT used 2026-05-13.**~~ ✓ Done 2026-05-13. Old token regenerated, new value saved in password manager, old value confirmed dead (HTTP 401).
7. ~~**Verify the red-backed salamander species identification.**~~ Conservative relabel applied 2026-05-13: the entry (id `red-backed-salamander` retained for stable image paths) is now `Woodland Salamander (Plethodon sp.)` with a `taxonomicNote` field explaining the candidate species at this elevation (P. serratus most plausible; P. cinereus unlikely at the southwestern edge of its range; Southern Appalachian Salamander complex also possible). SREL link points to their salamanders index page rather than a specific species. **Still useful for Paul to do, just not blocking:** if you ID a specimen in person, update `amphibians.json` to the correct species name + scientific name and swap `srelUrl` to the specific species page.

## Next steps after the drafts go live

Both drafts (plants + vehicles) have been promoted to live data as of 2026-05-13. Viewer renderers were already group-split-aware for vehicles and schema-compatible for plants — no further renderer work needed for these promotions.

Remaining draft-related follow-ups:
- Resolve the 3 vehicles "Outstanding asks for Paul" entries (Husqvarna sticker, Homelite trimmer model digit, Homelite blower/vac model) — currently `confidence: tbd` in maintenance blocks; once resolved, update `vehicles.json` + re-inline `VEHICLES_DATA`.
- `plants.draft.json.qualityPhotosForFutureIntegration` tracks specimen photos to swap in for the genus-level proxies on the 5 newly promoted plants.

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
