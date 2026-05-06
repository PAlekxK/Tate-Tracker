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

### Icon/emoji audit — collisions and poor fits
Several icons clash or don't represent their subject well. Goal: every icon should be the most semantically precise choice for its context — doesn't need to be cheerful, just accurate.

**Confirmed collisions:**
- Plants card 🌿 = Propagate action 🌿 — exact duplicate at two different UI levels

**Poor fits:**
- Vehicles card 🚗 — the fleet is an F-150, Bronco, two dirt bikes, a golf cart, chainsaws, and a riding mower. A sedan is the least representative item. Consider 🛻 or 🔧.
- Propagate 🌿, Fertilize 🌱, and Repot 🪴 form a cluster of similar green plant emojis used as sibling actions — they don't read as distinct at a glance. One or more should move to a non-plant metaphor (e.g. Fertilize could be a pellet/bag/chemical; Repot could be a shovel or vessel).
- Celestial events: 9 of 14 individual events share ☄️ (comet). Meteor showers, conjunctions, eclipses, and Milky Way season should each have a distinct emoji — they are different phenomena.

**Approach:** Audit all icons holistically — card level, care action level, and celestial event level — and choose the most precise, non-overlapping emoji for each. Emojis don't need to be cute; they need to be unambiguous.

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

### Wildlife photos — birds & amphibians (lower priority)
Explore adding actual photographs for each bird and amphibian species rather than emoji icons. Species are well-defined (all are North Georgia mountain species present on the property), so sourcing accurate photos is feasible — Wikimedia Commons and iNaturalist have permissively licensed images for all of them. Implementation consideration: photos would need to be either hosted externally (URL references in the JSON) or base64-inlined to keep the single-file constraint. Thumbnail treatment within the expandable species rows is the natural insertion point. Lower priority due to implementation complexity.

## Pending design improvements (prioritized)

1. ~~**Mobile dashboard strip** — 3-column grid wraps awkwardly at 390px~~ ✓ Done — now uses `repeat(auto-fit, minmax(150px, 1fr))`.
2. **Body background** — Add subtle grain/noise texture over the gradient for depth.
3. **Extend Crimson Text** — Card titles ("Weather", "Plants") should use the serif for typographic contrast vs DM Sans data labels.
4. **Card expand animation** — Currently hard-toggles. Add CSS `grid-template-rows: 0fr → 1fr` or max-height transition.
5. **"REFERENCE" section divider** — Plain uppercase text; should be a ruled line or carry more visual weight.
6. **Dashboard strip stat hierarchy** — Key numbers (temp, bird count) need more visual weight vs their labels.
7. **Header breathing room** — Increase top padding (22px → 32px) and h1 size (26px → 30px).

## Active drafts (not yet promoted to live data)

These files are staging areas. Do **not** wire them to the viewer until the user says go.

- **`vehicles.draft.json`** (schema v3, 15 items) — proposes splitting flat array into `group: "vehicle" | "equipment"` and adds a per-item `maintenance` block (fuel, oil, sparkPlug, filters, consumables) with `confidence: verified | inferred | tbd` tags. New equipment added: Kobalt KM2040X-06 mower, Echo PB-7910T backpack blower, Echo PB-250LN handheld blower, Homelite UT33650A trimmer, Homelite gas blower/vac (model not stickered — likely UT09521 family). Husqvarna riding mower fully fleshed out from the on-unit replacement-parts sticker (Kawasaki FR691V, 54" deck, all part numbers verified). Husqvarna model number itself still TBD (sticker not yet found).
- **`plants.draft.json`** — five new plants identified: Berry Box® Pyracomeles (USPP35913, verified by Pike Nursery tag), Yuki Cherry Blossom® Deutzia (NCDX2, verified by tag), Clematis (genus high; cultivar uncertain), Hostas (genus high; cultivars uncertain), pond Iris (genus high; species likely Blue Flag). Each entry needs a Zone 7b care calendar before promotion. Also tracks `qualityPhotosForFutureIntegration` — quality reference photos flagged for the future "real photos in the dashboard" enhancement.

## Uncommitted work in progress

These edits are local-only — not yet committed or pushed:

- **Phase 5 station-aware alerts** in `viewer.html` — generateAlerts() refactored, per-alert source chips, dedup. Pending visual verification + commit.
- **Phase 6 archive scaffolding**: `weather-history.json` (5 days seeded) and `tools/record-daily-rollup.mjs` + `tools/README.md`. Pending decision on scheduling approach (launchd vs GitHub Action).

## Outstanding asks for Paul

1. **Husqvarna riding mower:** model sticker (under seat or rear fender) — need the specific Husqvarna SKU like TS354XD / YTH24K54 / GTH54LS.
2. **Homelite trimmer:** confirm UT33650A (straight shaft) vs UT33550A (curved shaft) — middle digit on EPA sticker is slightly ambiguous.
3. **Homelite blower/vac:** no model sticker found on the unit. Maintenance specs are inferred from the trimmer's engine family (HHCPS.0264AT). Acceptable for at-a-store reference.

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
