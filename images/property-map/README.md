# Property map — multi-source imagery catalog

Starting-point imagery for the eventual property map view at 34.5496°N, 84.3674°W. Multiple data sources, each filling a different role.

## Files

### Aerial photography (current / near-current)

| File | Source | Zoom / span | Use |
|---|---|---|---|
| `aerial-esri-z19.jpg` | ESRI World Imagery | z19, ~620 ft across, 0.8 ft/px | Close-in: house + driveway |
| `aerial-esri-z18.jpg` | ESRI World Imagery | z18, ~1,240 ft across, 1.6 ft/px | Working scale: house, fairway, forest edge |
| `aerial-esri-z17.jpg` | ESRI World Imagery | z17, ~4,100 ft across, 3.2 ft/px | Wide context: property in relation to Lake Sequoyah and neighbors |
| `gep-2015-03-leafoff.png` | Google Earth Pro (user-supplied) | Mar 6, 2015 | **True leaf-off winter capture, canonical base layer for the eventual map view.** Bare deciduous trees show fairway pattern, driveway, and forest density clearly. House labeled "282 Church Mountain Rd" with pin. |

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
