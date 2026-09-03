#!/usr/bin/env python3
"""
Fetch NAIP aerial imagery for the property across all available years from
Microsoft's Planetary Computer. No auth needed.

NAIP = USDA National Agriculture Imagery Program. 0.6-1m resolution, typically
leaf-on summer/fall captures, every 2-3 years per state since ~2003.

Builds a year-by-year time-lapse for the property at a configurable bbox.

Usage:
    python3 tools/fetch-naip-timelapse.py [--span-ft N]

Default span: 1200 ft across (similar to the ESRI z18 working scale).
"""
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402 — canon values derive, never re-typed (C5 4a)

PROPERTY_LAT = momlib.config("location.coordinates.latitude")
PROPERTY_LON = momlib.config("location.coordinates.longitude")

STAC_URL = "https://planetarycomputer.microsoft.com/api/stac/v1/search"
DATA_BASE = "https://planetarycomputer.microsoft.com/api/data/v1/item/bbox/{bbox}.png"

HEADERS = {"User-Agent": "Fernwood-Dashboard/1.0 NAIP-timelapse-fetcher"}


def bbox_for_span(lat, lon, span_ft):
    """Return (minx, miny, maxx, maxy) bbox in EPSG:4326 covering ~span_ft across at lat."""
    span_m = span_ft * 0.3048
    # 1 deg lat ≈ 111,000 m. 1 deg lon ≈ 111,000 m * cos(lat)
    dlat = span_m / 111000.0
    dlon = span_m / (111000.0 * math.cos(math.radians(lat)))
    return (lon - dlon / 2, lat - dlat / 2, lon + dlon / 2, lat + dlat / 2)


def search_naip(lat, lon):
    req_body = json.dumps({
        "collections": ["naip"],
        "intersects": {"type": "Point", "coordinates": [lon, lat]},
        "limit": 100,
    }).encode("utf-8")
    req = urllib.request.Request(
        STAC_URL,
        data=req_body,
        headers={**HEADERS, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    features = data.get("features", [])
    # Sort by datetime ascending
    features.sort(key=lambda f: f["properties"].get("datetime", ""))
    return features


def fetch_crop(item_id, bbox, width=900, height=900, out_path="/tmp/naip.png"):
    minx, miny, maxx, maxy = bbox
    bbox_str = f"{minx},{miny},{maxx},{maxy}"
    params = {
        "collection": "naip",
        "item": item_id,
        "assets": "image",
        "asset_bidx": "image|1,2,3",
        "format": "png",
        "width": str(width),
        "height": str(height),
    }
    url = DATA_BASE.format(bbox=bbox_str) + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        # Probably a JSON error response
        sys.stderr.write(f"  WARN: non-PNG response ({len(data)} bytes) — {data[:200]!r}\n")
        return False
    with open(out_path, "wb") as f:
        f.write(data)
    return True


def main():
    span_ft = 1200
    for i, a in enumerate(sys.argv[1:]):
        if a == "--span-ft" and i + 1 < len(sys.argv) - 1:
            span_ft = int(sys.argv[i + 2])

    bbox = bbox_for_span(PROPERTY_LAT, PROPERTY_LON, span_ft)
    print(f"Searching NAIP catalog at {PROPERTY_LAT}, {PROPERTY_LON}")
    print(f"bbox span: {span_ft} ft = ({bbox[0]:.6f}, {bbox[1]:.6f}, {bbox[2]:.6f}, {bbox[3]:.6f})")

    out_dir = "images/property-map/naip"
    os.makedirs(out_dir, exist_ok=True)

    features = search_naip(PROPERTY_LAT, PROPERTY_LON)
    print(f"\nFound {len(features)} NAIP scenes:")
    for f in features:
        dt = f["properties"].get("datetime", "?")
        item_id = f["id"]
        date_str = dt[:10]
        out_path = os.path.join(out_dir, f"naip-{date_str}.png")
        print(f"  {date_str}  {item_id}")
        ok = fetch_crop(item_id, bbox, width=900, height=900, out_path=out_path)
        if ok:
            sz = os.path.getsize(out_path) / 1024
            print(f"    saved {out_path} ({sz:.0f} KB)")
        else:
            print(f"    FAILED")
        time.sleep(0.3)  # polite throttle


if __name__ == "__main__":
    main()
