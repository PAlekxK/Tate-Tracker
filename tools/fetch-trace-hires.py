#!/usr/bin/env python3
"""Fetch a HIGH-RESOLUTION tracing frame for area-trace.html. Local only, never committed.

WHY THIS EXISTS (2026-09-01)
  Paul, comparing the tracing tool to Google Earth Pro: "It seems like the zoom in
  Google Earth Pro is better." It is, and here is the arithmetic.

  The NAIP base is rendered 1500 px across a 458 m frame = 0.306 m/px, from a source
  whose native posting is 0.600 m/px. It is ALREADY 2x oversampled. Asking for more
  pixels of NAIP returns more pixels and not one bit more information — the detail is
  not in the source to begin with.

  GE Pro looks sharper because it serves Maxar-class imagery, not NAIP. Esri World
  Imagery is the same class and the same ceiling: MEASURED 2026-09-01, z19 = 0.246 m/px
  is real imagery over this property and z20 returns Esri's "Map data not yet available"
  placeholder — an HTTP 200 carrying a valid PNG of a grey square. So z19 is the ceiling,
  and it is 2.4x NAIP's native detail.

THE LICENSING LINE, AND IT IS THE WHOLE REASON THIS IS A SEPARATE TOOL
  Esri World Imagery is free for personal, non-commercial DISPLAY. It may NOT be
  redistributed — which is exactly why fetch-basemap.py disqualified it as a committed
  base image and pulls public-domain NAIP instead. Nothing about that has changed.

  What is different here is the destination. This writes to images/property-map/.local/,
  which is gitignored: it never enters a commit, never reaches GitHub Pages, never ships
  in Mom's app. It is a local tracing aid on Paul's own machine, the same posture as
  .private/. The committed basemap stays NAIP.

  ⛔ Do not commit the output. Do not set it as zones.json _meta.baseImage. Do not
  reference it from viewer.html.

WHAT IT DOES NOT BUY
  Not accuracy. Esri's georegistration is not guaranteed better than NAIP's +/-6 m, so a
  sharper picture can be confidently mis-placed. It buys the ability to SEE an edge, not
  the right to trust where the frame puts it. zones.json _meta.accuracyHonesty still holds.

USAGE
  python3 tools/fetch-trace-hires.py               # z19, matched to the NAIP frame
  python3 tools/fetch-trace-hires.py --px 2400     # oversample for smoother on-screen zoom
"""
from __future__ import annotations

import argparse
import io
import json
import math
import sys
import urllib.request
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("needs Pillow:  python3 -m pip install Pillow")

REPO = Path(__file__).resolve().parent.parent
FRAME = REPO / "images/property-map/base-naip-2022-01-leafoff.bounds.json"
OUT_DIR = REPO / "images/property-map/.local"

TILE = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
UA = {"User-Agent": "Fernwood-Dashboard/1.0 trace-hires"}
TILE_PX = 256


def merc_y(lat: float) -> float:
    """Web-Mercator y in [0,1] from the north pole down."""
    s = math.sin(math.radians(lat))
    return 0.5 - math.log((1 + s) / (1 - s)) / (4 * math.pi)


def merc_x(lon: float) -> float:
    return (lon + 180.0) / 360.0


def fetch_tile(z: int, x: int, y: int) -> Image.Image:
    req = urllib.request.Request(TILE.format(z=z, x=x, y=y), headers=UA)
    with urllib.request.urlopen(req, timeout=45) as r:
        data = r.read()
    im = Image.open(io.BytesIO(data)).convert("RGB")
    if im.size != (TILE_PX, TILE_PX):
        raise SystemExit(f"tile {z}/{x}/{y}: unexpected size {im.size}")
    return im


def looks_like_nodata(im: Image.Image) -> bool:
    """Esri answers a too-deep zoom with HTTP 200 and a grey 'Map data not yet
    available' PNG. A status code cannot tell you that; the pixels can."""
    g = im.convert("L")
    lo, hi = g.getextrema()
    return (hi - lo) < 40


def source_metadata(lat, lon):
    """Ask Esri WHAT it is actually serving here — sensor, capture date, stated accuracy.

    Without this the frame is an anonymous picture. It matters twice over: a capture date
    tells you whether the ground predates the regrading Paul did with heavy equipment, and
    the stated horizontal accuracy is the number that decides whether 'sharper' also means
    'better placed'. MEASURED 2026-09-01 over this property: WorldView-3, 2022-02-12,
    0.31 m resolution, 8.47 m accuracy — sharper than NAIP and placed LESS precisely
    than NAIP's +/-6 m. Both halves matter and only one of them is flattering.
    """
    import urllib.parse
    d = 0.0008
    url = ("https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/"
           "MapServer/identify?" + urllib.parse.urlencode({
               "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint", "sr": "4326",
               "layers": "all", "tolerance": "2", "returnGeometry": "false",
               "mapExtent": f"{lon-d},{lat-d},{lon+d},{lat+d}",
               "imageDisplay": "600,600,96", "f": "json"}))
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
            j = json.load(r)
        for it in j.get("results", []):
            a = it.get("attributes", {})
            date = a.get("SRC_DATE2")
            if date and date != "Null":
                return {
                    "sensor": a.get("DESCRIPTION"),
                    "captureDate": a.get("DATE (YYYYMMDD)"),
                    "captureDateReadable": date,
                    "sourceResolutionM": a.get("RESOLUTION (M)"),
                    "statedAccuracyM": a.get("ACCURACY (M)"),
                }
    except Exception as e:
        sys.stderr.write(f"  (Esri identify unavailable: {e})\n")
    return {}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--zoom", type=int, default=19, help="Esri zoom (19 is the measured ceiling here)")
    ap.add_argument("--px", type=int, default=0, help="output size; default = native for the zoom")
    args = ap.parse_args()

    b = json.loads(FRAME.read_text())["bounds"]
    meta = source_metadata((b["north"] + b["south"]) / 2, (b["east"] + b["west"]) / 2)
    if meta:
        print(f"source     {meta.get('sensor')} captured {meta.get('captureDateReadable')} "
              f"· {meta.get('sourceResolutionM')} m · stated accuracy {meta.get('statedAccuracyM')} m")
    W, S, E, N = b["west"], b["south"], b["east"], b["north"]
    z, n = args.zoom, 2 ** args.zoom

    lat_mid = (N + S) / 2
    span_m = (E - W) * 111320 * math.cos(math.radians(lat_mid))
    native_res = 156543.03392 * math.cos(math.radians(lat_mid)) / n
    px = args.px or int(round(span_m / native_res))

    print(f"frame      {span_m:.1f} m across   bounds W {W:.7f} E {E:.7f} S {S:.7f} N {N:.7f}")
    print(f"esri z{z}    {native_res:.3f} m/px native  ->  output {px}x{px} = {span_m/px:.3f} m/px")
    print(f"vs NAIP    0.600 m/px native  ->  {0.600/native_res:.1f}x the detail")

    x0, x1 = int(merc_x(W) * n), int(merc_x(E) * n)
    y0, y1 = int(merc_y(N) * n), int(merc_y(S) * n)
    cols, rows = x1 - x0 + 1, y1 - y0 + 1
    print(f"tiles      {cols}x{rows} = {cols*rows}")

    mosaic = Image.new("RGB", (cols * TILE_PX, rows * TILE_PX))
    nodata = 0
    for j, ty in enumerate(range(y0, y1 + 1)):
        for i, tx in enumerate(range(x0, x1 + 1)):
            im = fetch_tile(z, tx, ty)
            if looks_like_nodata(im):
                nodata += 1
            mosaic.paste(im, (i * TILE_PX, j * TILE_PX))
        print(f"  row {j+1}/{rows}", end="\r", flush=True)
    print(" " * 30, end="\r")

    # Match the payload, not the container: every tile was HTTP 200. If most of them
    # are Esri's grey placeholder, this zoom has no imagery and the output would be a
    # blank frame that renders perfectly.
    if nodata > cols * rows * 0.5:
        raise SystemExit(
            f"{nodata}/{cols*rows} tiles are Esri's 'Map data not yet available' placeholder "
            f"at z{z}. There is no imagery here at this zoom — try --zoom {z-1}."
        )
    if nodata:
        print(f"  note: {nodata}/{cols*rows} tiles were placeholders (frame edge)")

    # Resample the Mercator mosaic onto the frame's EPSG:4326 bbox. x is linear in both,
    # so it is one scale; y is NOT — latitude maps non-linearly into Mercator — so each
    # output row is placed by its own latitude. Over 458 m the difference is sub-centimetre,
    # far below the imagery's own error, but doing it right costs nothing and means the
    # output registers to the SAME bounds as every NAIP frame: a drop-in swap.
    mx0, mx1 = merc_x(W) * n * TILE_PX, merc_x(E) * n * TILE_PX
    ox0 = x0 * TILE_PX
    src_left, src_right = mx0 - ox0, mx1 - ox0

    out = Image.new("RGB", (px, px))
    oy0 = y0 * TILE_PX
    for row in range(px):
        lat_t = N - (N - S) * (row + 0.5) / px
        sy = merc_y(lat_t) * n * TILE_PX - oy0
        strip = mosaic.resize((px, 1), Image.LANCZOS,
                              box=(src_left, max(0, sy - 0.5), src_right, min(mosaic.height, sy + 0.5)))
        out.paste(strip, (0, row))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    png = OUT_DIR / f"trace-esri-z{z}.png"
    out.save(png)
    print(f"saved      {png.relative_to(REPO)}  ({png.stat().st_size/1024/1024:.1f} MB)")

    side = OUT_DIR / f"trace-esri-z{z}.bounds.json"
    side.write_text(json.dumps({
        "image": png.name,
        "source": "Esri World Imagery (Maxar/Airbus class) via ArcGIS Online tiles",
        "zoom": z,
        "nativeMetresPerPixel": round(native_res, 3),
        "renderedMetresPerPixel": round(span_m / px, 3),
        "license": "⛔ NOT redistributable. Free for personal, non-commercial DISPLAY only. "
                   "This file is gitignored on purpose — it must never be committed, served "
                   "from Pages, or set as zones.json _meta.baseImage. The committed basemap "
                   "stays public-domain NAIP (tools/fetch-basemap.py).",
        "purpose": "Local tracing aid for tools/area-trace.html. Detail, not authority.",
        "accuracyCaveat": "Sharper than NAIP; NOT known to be better georegistered. Esri's "
                          "placement is not guaranteed inside NAIP's +/-6 m. Use it to SEE an "
                          "edge, not to trust where the frame puts it. zones.json "
                          "_meta.accuracyHonesty still governs.",
        "zoomCeiling": f"MEASURED 2026-09-01: z{z+1} returns Esri's 'Map data not yet "
                       f"available' grey placeholder over this property, as an HTTP 200 with a "
                       f"valid PNG. z{z} is the real ceiling here.",
        "bounds": {"west": W, "south": S, "east": E, "north": N},
        "registeredTo": "IDENTICAL bounds to base-naip-* — drop-in layer, no re-registration",
        "pixelWidth": px, "pixelHeight": px,
        "sourceMetadata": meta,
        "seasonFinding": (
            "MEASURED, and it is the whole reason this frame is worth having: Esri serves a "
            "2026-02-12 WorldView-3 capture here, which is LEAF-OFF at a noon sun near 41 deg. "
            "The NAIP leaf-off frame is 2022-01-10 at 33.4 deg. So this is leaf-off AND a higher "
            "sun AND twice the detail — the closest thing that exists to the frame Paul asked "
            "for. What it gives up is placement: 8.47 m stated accuracy against NAIP's 6 m."
        ) if meta.get("captureDate", "").startswith(("202202", "202201", "202212", "202303")) else None,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"saved      {side.relative_to(REPO)}")
    print("\n⛔ gitignored by design. Local tracing detail only — the shipped basemap stays NAIP.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
