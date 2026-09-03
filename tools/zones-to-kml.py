#!/usr/bin/env python3
"""Export zones.json to a KML that Google Earth Pro can open, edit, and save back.

WHY THIS EXISTS (2026-09-01)
  Since schema v2, zone vertices are real WGS84 [lon, lat] — independent of any
  basemap. That is what makes an external editor possible at all: Google Earth Pro
  draws polygons on a georeferenced globe, so what comes back OUT is coordinates,
  not pixels. The 2015 failure (fractions of an oblique GEP screenshot) cannot
  recur through this path.

  What GE Pro buys over tools/area-trace.html: the historical imagery slider (pick
  the least-shadowed capture instead of being stuck with 2022-01-10's 32-degree
  sun), deeper zoom, and the measure tool.

WHAT THIS IS NOT
  Not a basemap swap. GE Pro imagery is licensed and may not be committed to this
  public repo — the same rule that disqualified Esri/Maxar in fetch-basemap.py.
  Look at it in GE Pro; ship NAIP.

  Colors here are a VIEW concern, generated per-zone so adjacent zones are
  distinguishable while tracing. They are NOT round-tripped — kml-to-zones.py
  ignores styling entirely and never writes a color back.

TRACING DISCIPLINE (read before you drag a vertex)
  • RESET TILT TO NADIR first (View -> Reset -> Tilt, or press `u`). In a tilted 3-D
    view a click projects onto draped terrain; on a spur at 2,873 ft that displaces
    the recorded point downslope by meters. Silent error — it looks correct on screen.
  • Sharper is not more accurate. GE resolves finer than NAIP's 0.6 m, but its
    georegistration is not guaranteed better than NAIP's +/-6 m. Before trusting a
    retrace, put one unambiguous feature (a house corner, the driveway junction) in
    both frames and see how far apart they land. That offset is real and it enters
    the data the moment sources are mixed.
  • Record WHICH imagery date you traced against — kml-to-zones.py requires it.

USAGE
  python3 tools/zones-to-kml.py                       # -> exports/fernwood-zones.kml
  python3 tools/zones-to-kml.py --out ~/Desktop/z.kml
  python3 tools/zones-to-kml.py --only the-turf,the-meadow,the-green
  python3 tools/zones-to-kml.py --open                # export, then open in GE Pro
"""
from __future__ import annotations

import argparse
import colorsys
import hashlib
import json
import math
import os
import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402 — canon values derive, never re-typed (C5 4a)

REPO = Path(__file__).resolve().parent.parent
ZONES = REPO / "zones.json"
DEFAULT_OUT = REPO / "exports" / "fernwood-zones.kml"

# Property anchor (property.json, confirmed via Google Maps May 2026).
ANCHOR_LAT = momlib.config("location.coordinates.latitude")
ANCHOR_LON = momlib.config("location.coordinates.longitude")

TYPE_ORDER = ["turf", "planted", "structure"]


def load_zones() -> dict:
    with ZONES.open(encoding="utf-8") as fh:
        return json.load(fh)


def hue_for(zone_id: str) -> tuple[int, int, int]:
    """Deterministic, well-spread RGB per zone id, so neighbours differ on screen."""
    h = int(hashlib.sha1(zone_id.encode("utf-8")).hexdigest()[:8], 16)
    hue = (h % 997) / 997.0
    r, g, b = colorsys.hsv_to_rgb(hue, 0.78, 0.98)
    return int(r * 255), int(g * 255), int(b * 255)


def kml_color(rgb: tuple[int, int, int], alpha: int) -> str:
    """KML wants aabbggrr — alpha, blue, green, red. Reversed from RGB hex."""
    r, g, b = rgb
    return f"{alpha:02x}{b:02x}{g:02x}{r:02x}"


def ring_area_m2(vertices: list[list[float]]) -> float:
    """Shoelace on a local equirectangular projection at the property latitude.

    At this scale the projection error is far below the imagery's own (same
    reasoning as zones.json _meta.boundsNote). Good enough to report a delta.
    """
    if len(vertices) < 3:
        return 0.0
    lat0 = math.radians(sum(v[1] for v in vertices) / len(vertices))
    mx = 111320.0 * math.cos(lat0)
    my = 110540.0
    pts = [(v[0] * mx, v[1] * my) for v in vertices]
    if pts[0] != pts[-1]:
        pts.append(pts[0])
    s = 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0


def closed_ring(vertices: list[list[float]]) -> list[list[float]]:
    """KML LinearRings MUST repeat the first coordinate as the last."""
    ring = [list(v) for v in vertices]
    if ring and ring[0] != ring[-1]:
        ring.append(list(ring[0]))
    return ring


def placemark(zone: dict) -> str:
    zid = zone["id"]
    rgb = hue_for(zid)
    ring = closed_ring(zone["vertices"])
    coords = " ".join(f"{lon:.7f},{lat:.7f},0" for lon, lat in ring)
    area = ring_area_m2(zone["vertices"])

    desc_rows = [
        ("zoneId", zid),
        ("type", zone.get("type", "")),
        ("status", zone.get("status", "")),
        ("partOf", zone.get("partOf") or "—"),
        ("vertices", str(len(zone["vertices"]))),
        ("area", f"{area:,.0f} m² ({area * 10.7639:,.0f} ft²)"),
    ]
    if zone.get("provenance"):
        desc_rows.append(("provenance", zone["provenance"]))
    desc = "<![CDATA[<table>" + "".join(
        f"<tr><td><b>{k}</b></td><td>{escape(str(v))}</td></tr>" for k, v in desc_rows
    ) + "</table>]]>"

    return f"""    <Placemark id="zone-{escape(zid)}">
      <name>{escape(zone.get('name', zid))}</name>
      <description>{desc}</description>
      <styleUrl>#style-{escape(zid)}</styleUrl>
      <ExtendedData>
        <Data name="zoneId"><value>{escape(zid)}</value></Data>
        <Data name="type"><value>{escape(zone.get('type', ''))}</value></Data>
        <Data name="status"><value>{escape(zone.get('status', ''))}</value></Data>
        <Data name="partOf"><value>{escape(zone.get('partOf') or '')}</value></Data>
        <Data name="ringWasClosed"><value>{'1' if zone['vertices'][0] == zone['vertices'][-1] else '0'}</value></Data>
      </ExtendedData>
      <Polygon>
        <tessellate>1</tessellate>
        <altitudeMode>clampToGround</altitudeMode>
        <outerBoundaryIs><LinearRing><coordinates>{coords}</coordinates></LinearRing></outerBoundaryIs>
      </Polygon>
    </Placemark>"""


def style(zid: str) -> str:
    rgb = hue_for(zid)
    return f"""    <Style id="style-{escape(zid)}">
      <LineStyle><color>{kml_color(rgb, 0xFF)}</color><width>2.4</width></LineStyle>
      <PolyStyle><color>{kml_color(rgb, 0x33)}</color><fill>1</fill><outline>1</outline></PolyStyle>
      <LabelStyle><scale>0.8</scale></LabelStyle>
    </Style>"""


def build_kml(doc: dict, only: set[str] | None) -> tuple[str, list[dict]]:
    meta = doc["_meta"]
    zones = [z for z in doc["zones"] if not only or z["id"] in only]
    if not zones:
        raise SystemExit("no zones selected — check --only")

    by_type: dict[str, list[dict]] = {}
    for z in zones:
        by_type.setdefault(z.get("type") or "untyped", []).append(z)

    folders = []
    for t in TYPE_ORDER + sorted(k for k in by_type if k not in TYPE_ORDER):
        if t not in by_type:
            continue
        marks = "\n".join(placemark(z) for z in sorted(by_type[t], key=lambda z: z["name"]))
        folders.append(
            f"""  <Folder>
    <name>{escape(t)} ({len(by_type[t])})</name>
    <open>1</open>
{marks}
  </Folder>"""
        )

    styles = "\n".join(style(z["id"]) for z in sorted(zones, key=lambda z: z["id"]))
    header_note = (
        "Fernwood zones exported from zones.json schema v"
        f"{meta.get('schemaVersion')} (built {meta.get('lastBuilt')}). "
        "RESET TILT TO NADIR before tracing (View > Reset > Tilt, or press u) — a tilted "
        "click projects onto draped terrain and lands downslope. Note which imagery date "
        "you traced against; the importer requires it. "
        "Colors are generated for legibility and are NOT part of the record."
    )

    kml = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
  <name>Fernwood zones ({len(zones)})</name>
  <description>{escape(header_note)}</description>
  <open>1</open>
  <LookAt>
    <longitude>{ANCHOR_LON}</longitude>
    <latitude>{ANCHOR_LAT}</latitude>
    <altitude>0</altitude>
    <heading>0</heading>
    <tilt>0</tilt>
    <range>420</range>
    <altitudeMode>relativeToGround</altitudeMode>
  </LookAt>
{styles}
{chr(10).join(folders)}
</Document>
</kml>
"""
    return kml, zones


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT, help=f"output .kml (default {DEFAULT_OUT})")
    ap.add_argument("--only", help="comma-separated zone ids to export")
    ap.add_argument("--open", action="store_true", help="open the result (Google Earth Pro if installed)")
    args = ap.parse_args()

    doc = load_zones()
    only = {s.strip() for s in args.only.split(",")} if args.only else None
    if only:
        known = {z["id"] for z in doc["zones"]}
        missing = only - known
        if missing:
            raise SystemExit(f"unknown zone id(s): {', '.join(sorted(missing))}")

    kml, zones = build_kml(doc, only)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(kml, encoding="utf-8")

    total = sum(ring_area_m2(z["vertices"]) for z in zones)
    print(f"wrote {args.out}")
    print(f"  {len(zones)} zone(s), {sum(len(z['vertices']) for z in zones)} vertices, "
          f"{total:,.0f} m² total ({total / 4046.86:.1f} acres)")
    closed = sum(1 for z in zones if z["vertices"][0] == z["vertices"][-1])
    print(f"  ring convention in the record: {closed} closed / {len(zones) - closed} open "
          f"(preserved on re-import)")
    print("\n  In Google Earth Pro: File > Open, then RESET TILT (press u) before tracing.")
    print("  Edit vertices, then right-click the 'Fernwood zones' folder > Save Place As... > .kml")
    print("  Bring it back with: python3 tools/kml-to-zones.py <file.kml> --imagery '<date/source>'")

    if args.open:
        gep = "/Applications/Google Earth Pro.app"
        if os.path.isdir(gep):
            subprocess.run(["open", "-a", gep, str(args.out)], check=False)
        else:
            print("\n  (Google Earth Pro not found at /Applications — opening with the default handler)")
            subprocess.run(["open", str(args.out)], check=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
