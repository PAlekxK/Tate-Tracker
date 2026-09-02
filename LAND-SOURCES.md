# Land sources — what public data exists about this plot, and where to go back to

*Started 2026-09-01. Paul: "what other surveys and information data generally just about that
plot of land in the surrounding area is available? And what are the databases we can revisit?"*

**Anchor: 34.5496°N, −84.3674°W · 282 Church Mountain Rd, Jasper GA 30143 · Pickens County.**

Two tiers, and the difference is load-bearing. **VERIFIED** means a query was actually run
against that service at these coordinates on the date shown and it returned data about *this*
property. **LEAD** means the source is known to exist and plausibly covers this land, and
nobody has checked. A registry that blurs the two is how a lead becomes a fact by being
written down twice.

---

## VERIFIED — queried at these coordinates, returned data

### Aerial imagery — USDA NAIP (public domain, redistributable)
Seven captures, 2010→2023, **all pulled to one byte-identical frame** so they are drop-in
layers in `tools/area-trace.html`. Sun angle and shadow ratio are recorded per frame because
they decide whether an edge is traceable.

| capture | GSD | noon sun | shadow | leaf |
|---|---|---|---|---|
| 2010-08-31 | 1.0 m | 63.6° | 0.50× | on |
| 2013-10-25 | 1.0 m | 42.3° | 1.10× | on |
| 2015-09-15 | 1.0 m | 57.7° | 0.63× | on |
| 2017-10-20 | 1.0 m | 44.1° | 1.03× | on |
| 2019-10-04 | 0.6 m | 50.1° | 0.84× | on |
| **2022-01-10** | 0.6 m | **33.4°** | **1.52×** | **OFF** |
| 2023-10-07 | 0.6 m | 48.9° | 0.87× | on |

⭐ **Exactly one is leaf-off, and it is the lowest sun of all seven.** That is not bad luck, it
is geometry: at 34.55°N the leaf-off window (Dec–early Apr) caps the noon sun near 55° at the
equinox, and sun above 60° only ever falls on full canopy. **The frame with bare trees AND an
overhead sun does not exist here.** Pick per zone instead: October for open ground, January to
see under canopy.

`tools/fetch-basemap.py --item <STAC id> --slug <name>` · STAC search on Microsoft Planetary
Computer, collection `naip`, intersecting the anchor.

### Esri World Imagery — WorldView-3 (⛔ display only, NOT redistributable)
**MEASURED 2026-09-01:** WV03, captured **2022-02-12**, 0.31 m source, **stated accuracy
8.47 m**. Leaf-off at ~41° sun — better than the NAIP leaf-off frame on season, sun *and*
detail. The catch is placement: 8.47 m is **worse** than NAIP's ±6 m. Sharper ≠ better placed.

⚠️ **z19 (0.246 m/px) is the ceiling here.** z20 and z21 return an HTTP 200 carrying a valid
PNG of a grey square reading *"Map data not yet available."* A status-code check calls that
success. `tools/fetch-trace-hires.py` inspects pixels and refuses.

Lands in gitignored `.local/`. Never commit, never serve, never `zones.json._meta.baseImage`.

### USGS 3DEP lidar — GA_Statewide_2018_B18_DRRA (public domain)
1 m DEM, flown 2018. Already the source of the property's **measured 2,873 ft** elevation, and
of `lidar-hillshade-2018.png` / `lidar-slope-2018.png`, both registered to the NAIP frame.
Lidar is an **active sensor: no sun, therefore no shadows** — the one product immune to the
whole shadow problem above.
⚠️ Its temporal caveat is already recorded: the western garden and patio were reshaped with
heavy equipment *after* 2018, so lidar/ground disagreement there means **work done since**, not
a bad trace.

**Not yet built:** a canopy-height model (DSM − DTM) from this same flight would draw the
woods/field edge with no shadows and no leaf-season dependence at all — measuring the trees
rather than photographing them. Strongest available source for `the-turf`, `the-meadow`,
`the-green`, `lawn`.

### USGS Historical Topographic Maps (public domain)
**17 sheets covering this land, back to 1888.** Three pulled and cropped by
`tools/fetch-historical-topo.py` → `images/property-map/historical/`.

| year | scale | what it shows |
|---|---|---|
| 1888 | 1:125,000 | Ellijay sheet. Contour and drainage only. No development at the property. |
| 1911 | 1:125,000 | Ellijay. Roads and buildings appear to the southeast; the property itself still empty. |
| **1971** | **1:24,000** | Amicalola. First scale that draws individual buildings — **and there is none at the anchor.** Lake Sequoyah, Burnt Mtn Church, the cemetery and BM 2792 all named. |

Also available and not yet pulled: 1892, 1898, 1911 (×3 more states), 1955, 1958 (×3), 1961,
1963, 1981, plus modern US Topo 2011 / 2014 / 2017 / 2020 / 2024.

⚙️ **Georeferencing note.** These are TerraGo GeoPDFs with no ISO-32000 `/Measure` dictionary,
so nothing standard reads them. The transform lives in a private `/LGIDict` `/CTM` mapping PDF
user space to **Polyconic metres on Clarke 1866**. The tool inverts that and runs the forward
Polyconic to place the anchor — no gdal needed — then **verifies the CTM against the sheet's own
`/Registration` control points** (0.00 m residual on all three; the 1888 sheet has only 2 points,
both on a vertical line, which is why fitting to control points fails and the CTM does the work).
⚠️ Sheets are **NAD27**, the anchor is WGS84; the 20–40 m north-Georgia shift is **not** applied.
For looking, not for tracing.

### USGS Watershed Boundary Dataset — the full hierarchy
```
South Atlantic-Gulf Region  →  Alabama  →  Coosa-Tallapoosa
  →  Coosawattee (HUC8)  →  Cartecay River (HUC10)
    →  Turkey Creek-Clear Creek (HUC12)
```
`hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer/identify`

### FEMA National Flood Hazard Layer
**Zone X — "area of minimal flood hazard."** One intersecting feature.
`hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query`

### Already in this repo from earlier work
NOAA 1991–2020 climate normals (KJZP) · USDA Web Soil Survey series candidates (**inferred,
never tested — waits on the W9 soil test**) · Almanac frost dates · the on-site Ambient Weather
station, which is the only *measured* record of this exact spot.

### Google Earth Web — historical archive back to 1985 (⛔ display only)
~16+ captures against NAIP's 7, reaching 25 years further back. **The imagery date is
URL-addressable**, so any capture is directly reachable and the archive is scriptable.
⭐ The **March–April 2018** frame is the best view of this property that exists: leaf-off at a
52–64° sun, roughly a third the shadow of the frame the zones were traced on.
⚠️ Two documented traps — the attribution date **lags** the header while tiles load, and the
1985 tick renders **100% loaded and completely blank** here.
Full write-up, the URL recipe, and the untested capabilities: **`GOOGLE-EARTH-NOTES.md`**.

---

## LEADS — plausible, not yet checked. Do not cite as fact.

- **USGS EarthExplorer — Aerial Photo Single Frames / NHAP / NAPP.** Scanned historical aerial
  photography, 1930s–1990s, public domain. This is the real path to *seeing* the land before the
  house, as a photograph rather than a map. Needs an EarthExplorer M2M login, and frames are raw
  (not orthorectified), so each would need control-point registration.
- **Pickens County GIS / qPublic.** Parcel boundary, deed reference, sales history, building
  footprint and year built, assessed value. **The property boundary is still missing from every
  source in this repo** — this is where it lives.
- **1832 Cherokee Land Lottery (Georgia Archives).** This land was Cherokee territory until 1832
  and was distributed by lottery, not federal patent — so BLM GLO records will *not* cover it.
  Original land-lot number and grantee would be here.
- **USFWS National Wetlands Inventory** — would classify the pond.
- **Georgia DNR Natural Heritage / protected species.**
- **Georgia Geologic Survey bedrock mapping.**
- **USDA Soil Data Access (SDA).** The programmatic version of Web Soil Survey. Needs a POST
  with a SQL body; my GET probe returned 400 — that is my probe being wrong, not the service.
- **EPA WATERS / 303(d)** — stream quality for Clear Creek.
- **Library of Congress historical map collection** — Georgia county and railroad maps.

---

## How to come back to this

```bash
python3 tools/fetch-basemap.py --item <naip stac id> --slug <name>   # any NAIP capture, same frame
python3 tools/fetch-trace-hires.py                                   # Esri z19, local only
python3 tools/fetch-historical-topo.py --span-ft 6000                # topo crops + manifest
python3 tools/zones-to-kml.py --open                                 # zones into Google Earth Pro
```

⚠️ **Every frame these produce shares one georeference**, which is the whole point: a new source
is a *registration*, never a redraw, because `zones.json` stores real WGS84 (schema v2). The one
thing that must never happen is a basemap becoming the coordinate system again.
