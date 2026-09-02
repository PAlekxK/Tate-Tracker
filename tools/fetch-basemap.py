#!/usr/bin/env python3
"""
Fetch ONE NAIP capture as the property map's base image, and write the bounds
alongside it.

Why this exists (2026-07-16). The old base was a Google Earth Pro *screenshot*:
oblique 3-D, a macOS notification baked into the sky, the GE HUD, and an address
pin. Worse, it had no georeference at all — zone vertices were stored as fractions
OF THAT JPEG, so the record didn't say where the Pond Area *is*, only where it
*appears in a picture*. Delete the picture and the data means nothing.

NAIP is the right source for this repo specifically:
  - PUBLIC DOMAIN (US federal work) — legally redistributable in a public repo.
    Esri/Maxar World Imagery is sharper (31cm) but may NOT be redistributed; it may
    only be displayed live. That disqualifies it as a committed base image.
  - This quarter-quad (m_3408430_sw) has a LEAF-OFF capture: 2022-01-10. Leaf-off is
    what makes the fairway edge, the driveway loop and the clearings traceable —
    under leaf-on canopy you'd be drawing boundaries you can't see.
  - 60cm, ±6m @ 95% (~20ft). Honest about what it is.

THE BOUNDS ARE THE POINT. The API renders an exact EPSG:4326 bbox, so the returned
image maps linearly to lat/lon. Writing that bbox next to the image is what lets zone
vertices be stored as real coordinates — and therefore what lets a future basemap
(a newer NAIP, or Paul's own drone ortho) be swapped by re-registering rather than
redrawing. This is the whole reason the 2015 polygons were unsalvageable.

Usage:
    python3 tools/fetch-basemap.py [--item ID] [--span-ft N] [--px N] [--slug NAME]
"""
import datetime
import json
import math
import os
import sys
import urllib.parse
import urllib.request

PROPERTY_LAT = 34.5496
PROPERTY_LON = -84.3674

# The leaf-off capture over this quarter-quad. NAIP aims for growing season, so a
# leaf-off frame is luck, not policy — 2022-01-10 is the one this quad has.
DEFAULT_ITEM = "ga_m_3408430_sw_16_060_20220110"
DEFAULT_DATE = "2022-01-10"

STAC_ITEM = "https://planetarycomputer.microsoft.com/api/stac/v1/collections/naip/items/{item}"
DATA_BASE = "https://planetarycomputer.microsoft.com/api/data/v1/item/bbox/{bbox}.png"
HEADERS = {"User-Agent": "Fernwood-Dashboard/1.0 basemap-fetch"}


def bbox_for_span(lat, lon, span_ft):
    """A bbox ~span_ft on a side (in METRES on the ground) centred on the property.

    dlat != dlon in degrees, so the image's x and y scales differ. That is fine and
    expected — the renderer maps each axis linearly against its own bound. What must
    never happen is assuming one degrees-per-pixel for both axes.
    """
    span_m = span_ft * 0.3048
    dlat = span_m / 111000.0
    dlon = span_m / (111000.0 * math.cos(math.radians(lat)))
    return (lon - dlon / 2, lat - dlat / 2, lon + dlon / 2, lat + dlat / 2)


def fetch_crop(item_id, bbox, px, out_path):
    minx, miny, maxx, maxy = bbox
    params = {
        "collection": "naip",
        "item": item_id,
        "assets": "image",
        "asset_bidx": "image|1,2,3",
        "format": "png",
        "width": str(px),
        "height": str(px),
    }
    url = DATA_BASE.format(bbox=f"{minx},{miny},{maxx},{maxy}") + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = resp.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        sys.stderr.write(f"non-PNG response ({len(data)} bytes): {data[:200]!r}\n")
        return False
    with open(out_path, "wb") as f:
        f.write(data)
    return True


def item_meta(item_id):
    """Pull the STAC item so the recorded provenance is the catalog's, not ours."""
    try:
        req = urllib.request.Request(STAC_ITEM.format(item=item_id), headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            it = json.loads(resp.read())
        p = it.get("properties", {})
        return {"datetime": p.get("datetime"), "gsd": p.get("gsd")}
    except Exception as e:
        sys.stderr.write(f"  (STAC metadata unavailable: {e})\n")
        return {}


def sun_and_season(capture_date):
    """Noon sun altitude and leaf state for a capture — the two numbers that decide
    whether an edge is traceable, and neither was recorded before 2026-09-01.

    Shadow length is height / tan(altitude), so a low sun does not dim the frame,
    it BURIES the ground next to anything vertical. At 34.55N these two wants are in
    direct conflict: the leaf-off window (Dec-early Apr) caps the noon sun near 55
    degrees at the equinox, and sun above 60 degrees only happens under full canopy.
    There is no capture that has both. Recording both numbers is what lets a tracer
    pick the right frame per zone instead of hunting for one that cannot exist.
    """
    try:
        d = datetime.date.fromisoformat(capture_date[:10])
    except Exception:
        return {}
    doy = d.timetuple().tm_yday
    dec = 23.44 * math.sin(math.radians(360 / 365 * (doy - 81)))
    alt = 90 - PROPERTY_LAT + dec
    # Leaf state at ~2,873 ft in the Blue Ridge: leaf-out runs late here, and drop is
    # complete by early December. April and November are genuinely mixed, so they are
    # labelled transitional rather than guessed either way.
    m = d.month
    season = ("leaf-off" if m in (12, 1, 2, 3) else
              "leaf-on" if m in (5, 6, 7, 8, 9, 10) else
              "transitional")
    return {
        "season": season,
        "seasonBasis": "month at ~2,873 ft Blue Ridge; Apr/Nov are mixed and read transitional",
        "noonSunAltitudeDeg": round(alt, 1),
        "shadowLengthPerUnitHeight": round(1 / math.tan(math.radians(alt)), 2),
        "shadowNote": "shadow = height / tan(altitude). Higher is better for tracing edges.",
    }


def main():
    item, span_ft, px, slug = DEFAULT_ITEM, 1500, 1500, "naip-2022-01-leafoff"
    a = sys.argv[1:]
    for i, tok in enumerate(a):
        if tok == "--item" and i + 1 < len(a): item = a[i + 1]
        elif tok == "--span-ft" and i + 1 < len(a): span_ft = int(a[i + 1])
        elif tok == "--px" and i + 1 < len(a): px = int(a[i + 1])
        elif tok == "--slug" and i + 1 < len(a): slug = a[i + 1]

    bbox = bbox_for_span(PROPERTY_LAT, PROPERTY_LON, span_ft)
    out_dir = "images/property-map"
    png = os.path.join(out_dir, f"base-{slug}.png")

    print(f"item     {item}")
    print(f"span     {span_ft} ft  ({span_ft * 0.3048:.0f} m)")
    print(f"px       {px}x{px}  → {span_ft / px:.2f} ft/px rendered")
    print(f"bbox     W {bbox[0]:.7f}  S {bbox[1]:.7f}  E {bbox[2]:.7f}  N {bbox[3]:.7f}")

    if not fetch_crop(item, bbox, px, png):
        sys.exit(1)
    print(f"saved    {png} ({os.path.getsize(png)/1024:.0f} KB)")

    meta = item_meta(item)
    bounds = {
        "image": os.path.basename(png),
        "source": "USDA NAIP via Microsoft Planetary Computer",
        "license": "public domain (US federal work) — redistributable",
        "stacItem": item,
        "captureDate": (meta.get("datetime") or DEFAULT_DATE)[:10],
        "gsdMeters": meta.get("gsd"),
        "projection": "EPSG:4326 linear (the API renders the exact bbox)",
        "declaredAccuracy": "+/-6 m @ 95% (NAIP contract spec) — ~20 ft",
        "bounds": {"west": bbox[0], "south": bbox[1], "east": bbox[2], "north": bbox[3]},
        "pixelWidth": px,
        "pixelHeight": px,
        "propertyAnchor": {"lat": PROPERTY_LAT, "lon": PROPERTY_LON},
    }
    bounds.update(sun_and_season(bounds["captureDate"]))
    side = os.path.join(out_dir, f"base-{slug}.bounds.json")
    with open(side, "w") as f:
        json.dump(bounds, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"saved    {side}")
    print("\nThe bounds file is the georeference. Zone vertices are stored as lat/lon")
    print("against it, so a future basemap is a re-registration, not a redraw.")


if __name__ == "__main__":
    main()
