#!/usr/bin/env python3
"""
Fetch and stitch aerial tiles for the property from ESRI World Imagery.

Usage:
    python3 tools/fetch-aerial.py [--zoom Z] [--grid N] [--source ESRI|OSM]

Defaults: zoom 18, 3x3 grid, ESRI World Imagery (publicly available aerial).

Tile source: https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery
Public access; personal/non-commercial use is fine. The tiles are sourced from
Maxar, USDA NAIP, and regional providers depending on coverage.

Property anchor: 34.5496 N, 84.3674 W (from property.json).
"""
import math
import os
import sys
import time
import urllib.request
import urllib.error
from io import BytesIO
from PIL import Image, ImageDraw

PROPERTY_LAT = 34.5496
PROPERTY_LON = -84.3674
TILE_SIZE = 256

SOURCES = {
    "ESRI": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    "USGS": "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}",
    "USGSTOPO": "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}",
    "USGSSHADED": "https://basemap.nationalmap.gov/arcgis/rest/services/USGSShadedReliefOnly/MapServer/tile/{z}/{y}/{x}",
    "OSM": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
}

HEADERS = {"User-Agent": "Fernwood-Dashboard/1.0 (paul.kirschenbauer@gmail.com) tile-fetch"}


def latlon_to_tile(lat, lon, z):
    """Web Mercator tile coords for given lat/lon at zoom z."""
    lat_rad = math.radians(lat)
    n = 2.0 ** z
    xtile = (lon + 180.0) / 360.0 * n
    ytile = (1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n
    return xtile, ytile


def fetch_tile(template, z, x, y, tries=3, delay=0.5):
    url = template.format(z=z, x=x, y=y)
    req = urllib.request.Request(url, headers=HEADERS)
    last_err = None
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
            if len(data) < 100:
                raise RuntimeError(f"tiny response ({len(data)} bytes)")
            return Image.open(BytesIO(data)).convert("RGB")
        except (urllib.error.URLError, urllib.error.HTTPError, RuntimeError) as e:
            last_err = e
            time.sleep(delay * (attempt + 1))
    raise RuntimeError(f"failed {url}: {last_err}")


def build_mosaic(lat, lon, zoom, grid, source="ESRI", marker=True):
    """Build a (grid x grid) mosaic of tiles around the lat/lon at zoom z."""
    template = SOURCES[source]
    cx, cy = latlon_to_tile(lat, lon, zoom)
    cx_int, cy_int = int(cx), int(cy)
    half = grid // 2
    # Fractional center within the center tile (for crosshair placement)
    frac_x = cx - cx_int
    frac_y = cy - cy_int

    out = Image.new("RGB", (TILE_SIZE * grid, TILE_SIZE * grid))
    for dy in range(-half, half + 1):
        for dx in range(-half, half + 1):
            x = cx_int + dx
            y = cy_int + dy
            tile = fetch_tile(template, zoom, x, y)
            px = (dx + half) * TILE_SIZE
            py = (dy + half) * TILE_SIZE
            out.paste(tile, (px, py))

    # Draw a small crosshair at the property's pixel position.
    #
    # marker=False for anything destined to be a MAP BASE. A baked-in crosshair is
    # chrome: it can't be turned off later, it sits on top of the exact area the
    # zones get drawn over, and it re-commits the mistake the 2015 Google Earth
    # screenshot made (notification + HUD + pin welded into the imagery). Keep the
    # marker for scouting/reference pulls, where "where is the house" is the point.
    center_px = int((half + frac_x) * TILE_SIZE)
    center_py = int((half + frac_y) * TILE_SIZE)
    if marker:
        draw = ImageDraw.Draw(out)
        r = 10
        draw.ellipse([center_px - r, center_py - r, center_px + r, center_py + r], outline="red", width=2)
        draw.line([center_px - r * 2, center_py, center_px + r * 2, center_py], fill="red", width=1)
        draw.line([center_px, center_py - r * 2, center_px, center_py + r * 2], fill="red", width=1)
    return out, (center_px, center_py)


def estimate_ground_resolution(lat, zoom):
    """Approximate meters per pixel for Web Mercator at this latitude/zoom."""
    return 156543.03 * math.cos(math.radians(lat)) / (2 ** zoom)


def main():
    args = {"zoom": 18, "grid": 3, "source": "ESRI", "marker": True, "out": None}
    for i, a in enumerate(sys.argv[1:]):
        if a == "--zoom" and i + 1 < len(sys.argv) - 1:
            args["zoom"] = int(sys.argv[i + 2])
        elif a == "--grid" and i + 1 < len(sys.argv) - 1:
            args["grid"] = int(sys.argv[i + 2])
        elif a == "--source" and i + 1 < len(sys.argv) - 1:
            args["source"] = sys.argv[i + 2].upper()
        elif a == "--no-marker":
            args["marker"] = False          # map bases must carry no chrome
        elif a == "--out" and i + 1 < len(sys.argv) - 1:
            args["out"] = sys.argv[i + 2]

    zoom = args["zoom"]
    grid = args["grid"]
    source = args["source"]
    if source not in SOURCES:
        print(f"Unknown source {source}. Use ESRI or USGS.", file=sys.stderr)
        sys.exit(1)
    if grid % 2 == 0:
        print("Grid must be odd (e.g. 3, 5, 7) so the property is centered.", file=sys.stderr)
        sys.exit(1)

    mpp = estimate_ground_resolution(PROPERTY_LAT, zoom)
    width = grid * TILE_SIZE
    span_m = width * mpp
    span_ft = span_m * 3.28084
    print(f"Fetching {source} zoom={zoom} grid={grid}x{grid}")
    print(f"  approx ground resolution: {mpp:.2f} m/px = {mpp * 3.28084:.2f} ft/px")
    print(f"  image size: {width}x{width} px = ~{span_ft:.0f} ft across")

    mosaic, center = build_mosaic(PROPERTY_LAT, PROPERTY_LON, zoom, grid, source=source, marker=args["marker"])
    out_path = args["out"] or f"images/property-map/aerial-{source.lower()}-z{zoom}.jpg"
    mosaic.save(out_path, "JPEG", quality=90, optimize=True)
    sz = os.path.getsize(out_path)
    print(f"  saved {out_path} ({sz/1024:.0f} KB) — property marked at ({center[0]}, {center[1]})")


if __name__ == "__main__":
    main()
