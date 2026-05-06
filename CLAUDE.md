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
| `renderFishing()` | Composite fishing score + per-species breakdown |
| `renderProperty()` | Property profile card |
| `renderPlantList()` | By Species view (calls `renderPlantCard` per plant) |
| `renderThisMonthPlants()` | This Month view grouped by care type |
| `renderTimeline()` | 3 Month view |
| `renderCalendarBody()` + `renderCalendarLegend()` | Full Year heatmap |
| `renderBirds()` / `renderAmphibians()` | Wildlife tabs |

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

### Tone — review urgency language throughout
Several strings read like a task manager rather than a field journal. Audit and soften:
- "17 actions due" → something like "17 things happening this month"
- "3 need attention" (vehicles) → "3 to keep an eye on"
- "3 alerts" (weather) → review whether "alerts" is the right word or if a gentler framing fits

## Pending design improvements (prioritized)

1. **Mobile dashboard strip** — 3-column grid wraps awkwardly at 390px; needs single-column fallback or shorter text.
2. **Body background** — Add subtle grain/noise texture over the gradient for depth.
3. **Extend Crimson Text** — Card titles ("Weather", "Plants") should use the serif for typographic contrast vs DM Sans data labels.
4. **Card expand animation** — Currently hard-toggles. Add CSS `grid-template-rows: 0fr → 1fr` or max-height transition.
5. **"REFERENCE" section divider** — Plain uppercase text; should be a ruled line or carry more visual weight.
6. **Dashboard strip stat hierarchy** — Key numbers (temp, bird count) need more visual weight vs their labels.
7. **Header breathing room** — Increase top padding (22px → 32px) and h1 size (26px → 30px).

## Location constants

| Field | Value |
|---|---|
| Address | 282 Church Mountain Road, Jasper, GA 30143 |
| Coordinates | 34.52°N, 84.46°W |
| Elevation | 2,959 ft (confirmed; 1,424 ft above KJZP baseline) |
| USDA Zone | 6b (elevation-adjusted); 7b official county |
| Last frost 50% | May 3 |
| Last frost 90% safe | May 24 |
| First frost 50% | October 17 |
| PWS | KGAJASPE279 (Weather Underground) |
| Sky quality | Bortle 3 (rural dark sky) |
