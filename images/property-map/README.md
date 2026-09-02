# Property map — multi-source imagery catalog

Starting-point imagery for the eventual property map view at 34.5496°N, 84.3674°W. Multiple data sources, each filling a different role.

## Files

### Aerial photography (current / near-current)

| File | Source | Zoom / span | Use |
|---|---|---|---|
| `aerial-esri-z19.jpg` | ESRI World Imagery | z19, ~620 ft across, 0.8 ft/px | Close-in: house + driveway |
| `aerial-esri-z18.jpg` | ESRI World Imagery | z18, ~1,240 ft across, 1.6 ft/px | Working scale: house, fairway, forest edge |
| `aerial-esri-z17.jpg` | ESRI World Imagery | z17, ~4,100 ft across, 3.2 ft/px | Wide context: property in relation to Lake Sequoyah and neighbors |
| `gep-2015-03-leafoff.png` | Google Earth Pro (user-supplied) | Mar 6, 2015 | **SUPERSEDED — historical only, not a basemap.** Was the v1 base; it is oblique, un-georeferenced, and licensed, which is what made the v1 polygons unsalvageable (see `tools/fetch-basemap.py`). The committed base is `base-naip-2022-01-leafoff.webp`. Kept because the leaf-off detail is still useful to *look* at. |

### NAIP historical time-lapse (`naip/`)

Seven USDA NAIP captures from 2010 to 2023, pulled via Microsoft Planetary Computer. ~1,200 ft across each. All ~1 m resolution. All leaf-on summer/fall **except 2022-01-10 which is true leaf-off winter** — that one is the standout.

| File | Date |
|---|---|
| `naip/naip-2010-08-31.png` | 2010-08-31 |
| `naip/naip-2013-10-25.png` | 2013-10-25 |
| `naip/naip-2015-09-15.png` | 2015-09-15 |
| `naip/naip-2017-10-20.png` | 2017-10-20 |
| `naip/naip-2019-10-04.png` | 2019-10-04 |
| `naip/naip-2022-01-10.png` | **2022-01-10 (leaf-off)** |
| `naip/naip-2023-10-07.png` | 2023-10-07 |
| `naip-timelapse-composite.jpg` | All 7 in one 4×2 grid | Side-by-side comparison view |

### Topographic / contour layers

| File | Source | Zoom / span | Use |
|---|---|---|---|
| `aerial-usgstopo-z16.jpg` | USGS Topographic basemap | z16, ~8,260 ft across | Property in context with road names, county line, contour lines (2940/2960/2980/3020 ft labeled), Sequoyah Lake + Clear Creek named, Church Mountain Rd labeled |
| `aerial-usgstopo-z15.jpg` | USGS Topographic basemap | z15, ~16,500 ft across | Wider topographic context, broader road network, additional named features (Eagles Rest Park, Burnt Mountain, Sequoyah Lake Dam) |
| `aerial-usgsshaded-z13.jpg` | USGS Shaded Relief | z13, ~66,000 ft across | Regional ridge-valley structure of the southern Appalachians at this elevation |
| `aerial-osm-z15.jpg` | OpenStreetMap | z15, ~16,500 ft across | Full road network with named roads (Saint Andrews Way, Lake Sequoyah Road, GA 136, Monument Road), county boundaries, Burnt Mountain (1,002 m / 3,288 ft) labeled |

## Sources documented

### ESRI World Imagery
- **URL**: `https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}`
- **Resolution**: up to z19 (~0.25 m/px) for our area
- **License**: Free for personal/non-commercial display
- **Coverage**: Sources from Maxar, USDA NAIP, regional providers. Mostly leaf-on. Current.

### NAIP via Microsoft Planetary Computer
- **STAC catalog**: `https://planetarycomputer.microsoft.com/api/stac/v1/search`
- **Item endpoint**: `https://planetarycomputer.microsoft.com/api/data/v1/item/bbox/{minx,miny,maxx,maxy}.png?collection=naip&item={id}&assets=image&asset_bidx=image%7C1%2C2%2C3&format=png&width={w}&height={h}`
- **Resolution**: ~1 m/px (most years) and 0.6 m/px (2019+)
- **License**: Public domain (US Federal aerial imagery)
- **Coverage**: Georgia is flown every 2-3 years. 7 captures from 2010 to 2023 visible at this point. No auth required.

### USGS National Map
- **Topo**: `https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}`
- **Shaded Relief**: `https://basemap.nationalmap.gov/arcgis/rest/services/USGSShadedReliefOnly/MapServer/tile/{z}/{y}/{x}`
- **Imagery (NAIP rebadged)**: `https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}` — 404s at z=18 for our area (gap in their tile cache)
- **License**: Public domain
- **Coverage**: Topo caps at z=16 in rural areas. Shaded relief caps lower (z=13 worked, z=14+ are inconsistent).

### OpenStreetMap
- **URL**: `https://tile.openstreetmap.org/{z}/{x}/{y}.png`
- **License**: ODbL — attribution required for public display
- **Coverage**: Wide. Best for road labels and POI names.

## Tools

```bash
# ESRI / USGS / OSM tile mosaics (existing)
python3 tools/fetch-aerial.py --zoom 18 --grid 3 --source ESRI
python3 tools/fetch-aerial.py --zoom 16 --grid 5 --source USGSTOPO
python3 tools/fetch-aerial.py --zoom 13 --grid 5 --source USGSSHADED
python3 tools/fetch-aerial.py --zoom 15 --grid 5 --source OSM

# NAIP historical time-lapse (Planetary Computer)
python3 tools/fetch-naip-timelapse.py --span-ft 1200

# Build the side-by-side composite from naip/ files
python3 tools/build-naip-composite.py
```

## Google Earth Pro — an editor, not a basemap

Added 2026-09-01. GE Pro is now the recommended surface for **drawing and correcting zone
geometry**, and is explicitly *not* a source for the committed base image.

**Why it works as an editor.** Since `zones.json` schema v2, vertices are real WGS84
`[lon, lat]`, independent of any basemap. GE Pro draws on a georeferenced globe, so what
comes back out is coordinates, not pixels — the 2015 failure (fractions of an oblique GEP
screenshot) cannot recur through this path. What it buys over `tools/area-trace.html`: the
historical imagery slider, so you can pick the least-shadowed capture instead of being stuck
with 2022-01-10's 32° winter sun; deeper zoom; and the measure tool.

**Why it is not a basemap.** GE Pro imagery is licensed and may not be redistributed from
this public repo — the same rule that disqualified Esri/Maxar (see `tools/fetch-basemap.py`).
A GE screenshot also carries no bbox, so it cannot be registered the way
`base-naip-2022-01-leafoff.bounds.json` registers NAIP. Look at it while tracing; ship NAIP.

**Round trip**

```bash
python3 tools/zones-to-kml.py --open          # exports/fernwood-zones.kml, opens in GE Pro
# ... trace in GE Pro, then right-click the folder > Save Place As... > .kml
python3 tools/kml-to-zones.py edited.kml                                  # dry run: what moved
python3 tools/kml-to-zones.py edited.kml --imagery "GE Pro, 2023-11-04" --write
```

The importer defaults to a dry run, requires `--imagery` before it will write, never deletes
a zone, refuses polygons with holes, and errors rather than reporting success on a KML that
holds zero polygons or coordinates off the property. Colors in the export are generated for
on-screen legibility and are never written back.

**Two things to hold onto while tracing**

1. **Reset tilt to nadir first** (View → Reset → Tilt, or press `u`). In a tilted 3-D view a
   click projects onto draped terrain; on a spur at 2,873 ft that lands the point downslope by
   meters. It looks correct on screen.
2. **Sharper is not more accurate.** GE resolves finer than NAIP's 0.6 m, but its
   georegistration is not guaranteed better than NAIP's ±6 m. Before trusting a retrace, put
   one unambiguous feature — a house corner, the driveway junction — in both frames and see how
   far apart they land. That offset is real, and it enters the record the moment sources are
   mixed. `zones.json` `_meta.accuracyHonesty` would need rewriting, not just relaxing.

**Still the better answer for the field zones.** The shadow complaint of 2026-08-31 is an
artifact of one capture. A canopy-height model derived from the 2018 GA statewide lidar (the
same product that fixed the elevation) draws the woods/field edge with no shadows and no
leaf-season dependence at all — it measures the trees instead of photographing them. That is
the strongest available source for `the-turf`, `the-meadow`, `the-green` and `lawn`, and
`lidar-hillshade-2018.png` shows the pull path already exists. Not built yet.

## Things found, things still to verify

**Confirmed in imagery (or Paul's read):**
- Property is at 34.5496°N, 84.3674°W
- House sits at the **northwest corner** of the fairway clearing, **facing south** (corrected from my initial misread)
- The fairway extends south/southeast from the house
- Forest interior wraps west, north, east
- A small **pond** sits between house and fairway, hidden by a tree canopy — not visible in any aerial source above; will require manual annotation
- Single gravel driveway approaching from the southwest
- ~0.3 mi north of Lake Sequoyah at ~2,960 ft elevation (matches `property.json`)

**Naming question resolved (Paul, 2026-05-19):**
- "Burnt Mountain Estates" and "Tate Mountain Estates" are different names for the same development at different points in time. OSM's modern label and USGS's historic label both refer to the same Tate-era development that the property sits inside. CLAUDE.md callouts remain anchored to the historic "Tate Mountain Estates" naming since that's the layered-history register the prose is in. If anything contradicts this read in future research, flag it.

**Property boundary** — not in any of these images. Paul doesn't have a clear boundary file yet; can add later from county GIS or deed plat.
