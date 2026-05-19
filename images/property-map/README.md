# Property map — aerial imagery

Starting-point aerial images of the Fernwood property (34.5496°N, 84.3674°W) for the eventual property-map view. Pulled from public ESRI World Imagery tiles via `tools/fetch-aerial.py`.

## Files

| File | Zoom | Coverage | Resolution | Use |
|---|---|---|---|---|
| `aerial-esri-z17.jpg` | 17 | ~4,100 ft across (5×5 tiles) | 3.2 ft/px | Wide context — shows Lake Sequoyah, neighboring properties, the road network |
| `aerial-esri-z18.jpg` | 18 | ~1,240 ft across (3×3 tiles) | 1.6 ft/px | Working scale — the house, fairway clearing, surrounding forest edge |
| `aerial-esri-z19.jpg` | 19 | ~620 ft across (3×3 tiles) | 0.8 ft/px | Close-in — house and immediate surroundings |

Each image has a small red crosshair marking the property's exact lat/lon.

## Source

ESRI World Imagery tile service (`server.arcgisonline.com/ArcGIS/rest/services/World_Imagery`). Publicly accessible XYZ tiles, sourced from Maxar / USDA NAIP / regional providers. Personal/non-commercial use is fine; we display these on a personal property dashboard, not redistribute the source tiles.

USGS NAIP attempted but doesn't have coverage at z18 for this rural Blue Ridge location (404).

## To regenerate or refresh

```bash
python3 tools/fetch-aerial.py --zoom 18 --grid 3 --source ESRI
python3 tools/fetch-aerial.py --zoom 19 --grid 3 --source ESRI
python3 tools/fetch-aerial.py --zoom 17 --grid 5 --source ESRI
```

The script lives at `tools/fetch-aerial.py`. Property coordinates are hardcoded; edit `PROPERTY_LAT` and `PROPERTY_LON` at the top to point elsewhere.

## Quality notes

- Looks like late winter / early spring capture — fairway clearing shows the old golf-course furrow pattern; deciduous trees in the lower elevation strips look mostly bare. The dense forest blocks at z17 look greener (could be a different acquisition date stitched together).
- Limited control over historical-imagery selection from this tile service. For a leaf-off / winter capture or a more recent year, Google Earth Pro's historical-imagery slider is the better source — drop a higher-quality export into this directory as `aerial-v2.jpg` (or similar) and we'll work from that instead.

## What I see in the imagery (Claude's read, 2026-05-19)

At z19 (closest):
- House visible at lower-center — small structure with what looks like a dark roof and a vehicle parked next to it
- Circular driveway/turnaround wrapping the south side of the house
- A driveway extending south from the house
- The bulk of the image (everything north and east of the house) is the south-facing fairway clearing mentioned in property.json — the rows of bare deciduous saplings in a diagonal pattern suggest old golf-course furrows now in successional growth
- Forest interior wraps around the west, north, and east edges (faintly visible at this zoom; clearer at z18)

At z18 (working scale):
- The fairway clearing is fully visible — the property sits at its south-southwest corner
- Dense forest interior to the west, north, and east
- A sandy/light-colored path snakes south from the property, likely the driveway to the road network
- A second clearing or feature in the lower-right corner

At z17 (wide context):
- Lake Sequoyah is the green water body in the lower-right — about 0.3 mi from the property as expected from property.json
- The dam is visible at the bottom-center of the lake
- A road runs across the dam
- A scatter of neighboring houses around the south and east of the lake (the broader Tate Mountain Estates community)
- The property sits north of the lake on rising ground — the wider forest block extends west and north
- The fairway is one of several clearings visible in the area — adjacent properties have their own clearings, paths, and driveway loops

If anything I just described is wrong, that's the most useful feedback — it tells me my mental model of the property doesn't match the ground truth, and I should recalibrate before any zone-naming work.
