# Church Mountain Property Tracker

A self-contained property dashboard for **Fernwood, Jasper, GA 30143** (elevation 2,873 ft, USDA Zone 6b elevation-adjusted; 7b official).

Open `viewer.html` in any browser — no server, no build step, no account required.

---

## Features

### 🌤 Weather
- Live conditions fetched from [Open-Meteo](https://open-meteo.com) (free, no API key)
- 7-day forecast with highs/lows, precipitation, wind, UV index
- Rule-based alerts: freeze warnings, heat advisories, good outdoor work windows
- **Animated radar** — RainViewer tiles via Leaflet, centered on the property

### 🎣 Fishing Forecast
- Daily composite score (water temp · pressure trend · moon phase · wind · sky) with research-backed weights
- Per-species star ratings: Largemouth Bass, Smallmouth Bass, Spotted Bass, Rainbow Trout, Crappie, Bluegill, Catfish
- Solunar windows (major ±1 hr around moon transit; minor ±30 min around moonrise/set) computed live via SunCalc
- Barometric pressure trend from 6 hours of Open-Meteo hourly data
- Species-specific water temperature sweet spots calibrated to North Georgia mountain streams and ponds

### 🔭 Celestial Events
- Tonight's sky: cloud cover, moon phase + illumination %, astronomical dark window, Bortle 3 site quality estimate
- 14 upcoming events (May 2026 – Dec 2027) with Georgia-specific visibility ratings and moon-interference computed dynamically
- Expandable detail rows: peak rate, direction, altitude at 34.5°N, duration note, viewing tip
- Events include: Eta Aquariids, Venus-Jupiter conjunction, Milky Way season, partial solar eclipse (Aug 12 2026 ~15–25% coverage), Perseids (exceptional 2026 — new moon), partial lunar eclipse, Saturn opposition, Orionids, Leonids, Geminids, Quadrantids, and 2027 repeats

### 🌿 Plant Calendar & Care Guides
- 8 plants tracked: White Pine, Azalea, Hydrangea, Dogwood, Boxwood, Holly, Mountain Laurel, Japanese Maple
- Per-plant care calendars (prune, fertilize, water, propagate, inspect) with Zone 7b timing
- 3-month timeline view and full-year heat map
- Peak window flags and narrow-window alerts

### 🚗 Vehicles & Equipment
- Fleet of 9 vehicles/equipment items with status badges
- Includes restoration-in-progress and diagnosis-ongoing flags

### 🏡 Property Info
- Microclimate notes, soil types, elevation, aspect, watershed info

---

## Files

```
property-tracker/
├── viewer.html      ← the entire UI; open this in a browser
├── plants.json      ← plant database (schema v2)
├── fishing.json     ← fishing species + habitat data
├── property.json    ← property metadata
├── vehicles.json    ← fleet/equipment registry
└── weather.json     ← fallback static data (live fetch takes priority)
```

`viewer.html` is fully self-contained — all CSS, JS, and fallback data are inlined. The live weather and solunar calculations happen client-side at page load.

---

## Location

| Field | Value |
|---|---|
| Address | Fernwood, Jasper, GA 30143 |
| Coordinates | 34.5496°N, 84.3674°W |
| Elevation | 2,873 ft (measured from USGS 3DEP 1 m lidar, 2026-08-31) |
| USDA Zone | 7b |
| Last frost | Mid-April |
| First frost | Late October |
| Sky quality | Bortle 3 (rural dark sky) |

---

## Data sources

- **Weather & pressure** — [Open-Meteo](https://open-meteo.com) (free, no key, CORS-enabled)
- **Radar tiles** — [RainViewer](https://www.rainviewer.com/api.html) (free)
- **Astronomical calculations** — [SunCalc](https://github.com/mourner/suncalc) (MIT)
- **Map rendering** — [Leaflet.js](https://leafletjs.com) (BSD-2)
- All other data (plants, vehicles, celestial events) is hand-curated for this property
