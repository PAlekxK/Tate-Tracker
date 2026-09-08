# zones-derivability — the experiment code, landed so it can be re-run

Companion to `.engineering/2026-09-08-zones-derivability-EXPERIMENT.md`.

⚠️ **This lives here, not in `tools/`, on purpose.** The BUILD window owns `tools/*` this lap, and
**Z-9 rules the operator layer SCAFFOLDING with a known expiry** — this is measurement apparatus, not
a product surface. It earns a `tools/` home only if it survives contact with a second property.

⛔ **It was originally written to a session scratchpad**, and the EXPERIMENT file's own QA section
claimed it was *"re-runnable from the scratchpad."* **That was false the moment the session ended** —
the scratchpad is session-scoped. Landing it here is the fix. *(Same shape as the repo's standing
lesson: a capability the loop cannot reach by running its own procedure is not a capability it has.)*

## Run

```bash
cd .engineering/zones-derivability && python3 -c "
import sys; sys.path.insert(0,'.')
import geo, raster, field
print(geo.assert_same_frame('base-naip-2022-01-leafoff.bounds.json'))"
```

**PIL only.** `numpy`, `scipy`, `skimage`, `cv2`, `shapely`, `rasterio`, `gdal`, `pdal` are all
ABSENT from this environment (measured 2026-09-08) — that is the existing design, not a gap to fill.

## The three preconditions — if any stops passing, every number in the write-up is void

1. **Frame identity** — `geo.assert_same_frame()`. The lidar and all seven NAIP frames must share
   bounds byte-for-byte. It refuses rather than warns.
2. **Ramp direction** — the slope PNG is **RGB, a 491-colour ramp**. `field.slope_field()` inverts
   luminance so high = steep, and that direction is only valid because it was read empirically off
   the answer key (`the-bank`/`the-bluff` darkest, `the-meadow`/`the-turf` lightest).
3. **`house` rasterises to ~139 m²** (~1,500 sq ft). The georeferencing sanity check.

## Files

| | |
|---|---|
| `geo.py` | bounds, lon/lat→px, metres-per-pixel, shoelace area |
| `raster.py` | ramp decode, point-in-polygon, interior/boundary sampling (no shapely) |
| `field.py` | slope scalar field + break-of-slope gradient |
| `derivability.json` | per-zone TERRAIN percentiles (the §3 table) |
| `mowing.json` | per-zone per-frame TEXTURE percentiles (the §6 edge test that failed) |

Deterministic under `seed 20260908`.
