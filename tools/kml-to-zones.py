#!/usr/bin/env python3
"""Import zone polygons edited in Google Earth Pro back into zones.json.

WHY THIS EXISTS (2026-09-01)
  The return leg of tools/zones-to-kml.py. GE Pro polygons are real WGS84, so what
  comes back is coordinates — the record never depends on the picture Paul happened
  to be looking at. That is the whole v2 invariant, and this tool must not break it.

THE POSTURE: PROPOSE, THEN LET PAUL RULE
  zones.json is canonical and hand-authored. So this DEFAULTS TO A DRY RUN: it prints
  what would change — vertex counts, centroid shift in feet, area delta — and writes
  nothing. --write applies it, and --write REQUIRES --imagery, because a retrace whose
  imagery date is unrecorded cannot be reasoned about later (see _meta.accuracyHonesty).

WHAT IT REFUSES TO DO
  • Delete. A zone in zones.json that is absent from the KML is left ALONE and
    reported. Export a subset, edit it, bring it back — nothing else moves.
  • Guess. An unmatched polygon is reported, not invented into a zone, unless
    --allow-new says so explicitly.
  • Accept a polygon with holes. zones.json has no inner-boundary support, so
    silently dropping one would quietly shrink a zone. It errors instead.
  • Trust the container. A KML with zero polygons is an ERROR, not "0 zones
    updated" — a parser that reports success on the wrong document is the failure
    mode this repo has been bitten by. Coordinates outside the property envelope
    (the classic [lat, lon] swap) are an error too, not a shrug.
  • Touch styling, names, types, partOf, provenance or status. Vertices only.

USAGE
  python3 tools/kml-to-zones.py edited.kml
  python3 tools/kml-to-zones.py edited.kml --imagery "GE Pro, 2023-11-04 capture" --write
  python3 tools/kml-to-zones.py edited.kmz --only the-turf --imagery "..." --write
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parent.parent
ZONES = REPO / "zones.json"

KML_NS = {"k": "http://www.opengis.net/kml/2.2"}

# Property envelope. The anchor is 34.5496 N, -84.3674 W; +/-0.02 deg is ~1.4 mi,
# far wider than the property and far narrower than a wrong-place or swapped-axis
# mistake. This is the guard that catches [lat, lon] order, the documented footgun
# in this schema (_meta.vertexOrder).
LAT_MIN, LAT_MAX = 34.5296, 34.5696
LON_MIN, LON_MAX = -84.3874, -84.3474


# ---------------------------------------------------------------- geometry


def ring_area_m2(vertices: list[list[float]]) -> float:
    if len(vertices) < 3:
        return 0.0
    lat0 = math.radians(sum(v[1] for v in vertices) / len(vertices))
    mx, my = 111320.0 * math.cos(lat0), 110540.0
    pts = [(v[0] * mx, v[1] * my) for v in vertices]
    if pts[0] != pts[-1]:
        pts.append(pts[0])
    s = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:]))
    return abs(s) / 2.0


def centroid(vertices: list[list[float]]) -> tuple[float, float]:
    n = len(vertices)
    return sum(v[0] for v in vertices) / n, sum(v[1] for v in vertices) / n


def metres_between(a: tuple[float, float], b: tuple[float, float]) -> float:
    lat0 = math.radians((a[1] + b[1]) / 2)
    dx = (b[0] - a[0]) * 111320.0 * math.cos(lat0)
    dy = (b[1] - a[1]) * 110540.0
    return math.hypot(dx, dy)


def slug(name: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", name.lower())).strip("-")


# ---------------------------------------------------------------- parsing


def read_kml_bytes(path: Path) -> bytes:
    if path.suffix.lower() == ".kmz":
        with zipfile.ZipFile(path) as zf:
            names = [n for n in zf.namelist() if n.lower().endswith(".kml")]
            if not names:
                raise SystemExit(f"{path.name}: KMZ contains no .kml entry")
            preferred = [n for n in names if n.lower() == "doc.kml"]
            return zf.read(preferred[0] if preferred else names[0])
    return path.read_bytes()


def parse_polygons(path: Path) -> list[dict]:
    """Every Placemark carrying a Polygon, with its ring and identity hints."""
    try:
        root = ET.fromstring(read_kml_bytes(path))
    except ET.ParseError as exc:
        raise SystemExit(f"{path.name}: not valid XML — {exc}")

    out: list[dict] = []
    skipped: list[str] = []
    for pm in root.findall(".//k:Placemark", KML_NS):
        name_el = pm.find("k:name", KML_NS)
        name = (name_el.text or "").strip() if name_el is not None else ""

        polys = pm.findall(".//k:Polygon", KML_NS)
        if not polys:
            kind = "Point" if pm.find(".//k:Point", KML_NS) is not None else (
                "LineString" if pm.find(".//k:LineString", KML_NS) is not None else "no geometry")
            skipped.append(f"{name or '(unnamed)'} [{kind}]")
            continue
        if len(polys) > 1:
            raise SystemExit(
                f"'{name}': MultiGeometry with {len(polys)} polygons. zones.json holds one ring "
                f"per zone — split it into separate placemarks in GE Pro, or drop the extras."
            )

        poly = polys[0]
        if poly.find(".//k:innerBoundaryIs", KML_NS) is not None:
            raise SystemExit(
                f"'{name}': polygon has an inner boundary (a hole). zones.json has no hole "
                f"support, and importing it would silently enlarge the zone by the hole's area. "
                f"Remove the hole in GE Pro, or leave this zone out of the import."
            )

        coord_el = poly.find(".//k:outerBoundaryIs/k:LinearRing/k:coordinates", KML_NS)
        if coord_el is None or not (coord_el.text or "").strip():
            raise SystemExit(f"'{name}': polygon has no outer-boundary coordinates")

        ring: list[list[float]] = []
        for tup in (coord_el.text or "").replace("\n", " ").split():
            parts = tup.split(",")
            if len(parts) < 2:
                raise SystemExit(f"'{name}': malformed coordinate tuple {tup!r}")
            lon, lat = float(parts[0]), float(parts[1])  # KML is lon,lat[,alt] — alt dropped
            ring.append([lon, lat])

        ext = {}
        for d in pm.findall(".//k:Data", KML_NS):
            v = d.find("k:value", KML_NS)
            ext[d.get("name")] = (v.text or "").strip() if v is not None else ""

        out.append({"name": name, "ring": ring, "ext": ext})

    if skipped:
        print(f"  note: skipped {len(skipped)} non-polygon placemark(s): {', '.join(skipped[:6])}"
              + (" ..." if len(skipped) > 6 else ""))

    # Match the payload, not the container: a file we parsed cleanly but that holds
    # none of what we came for is a failure, never a quiet zero.
    if not out:
        raise SystemExit(
            f"{path.name}: parsed fine but contains ZERO polygons. Nothing was imported. "
            f"In GE Pro, save the FOLDER (right-click > Save Place As...), not the current view."
        )
    return out


def check_envelope(polys: list[dict]) -> None:
    bad = []
    for p in polys:
        for lon, lat in p["ring"]:
            if not (LON_MIN <= lon <= LON_MAX and LAT_MIN <= lat <= LAT_MAX):
                bad.append((p["name"], lon, lat))
                break
    if bad:
        first = bad[0]
        swapped = LAT_MIN <= first[1] <= LAT_MAX and LON_MIN <= first[2] <= LON_MAX
        hint = ("\n  Those look like [lat, lon] — KML coordinates are lon,lat. "
                "Check what wrote this file." if swapped else
                "\n  These coordinates are not on the property. Wrong file, or wrong place in GE Pro.")
        raise SystemExit(
            f"{len(bad)} polygon(s) fall outside the property envelope "
            f"({LAT_MIN}..{LAT_MAX} N, {LON_MIN}..{LON_MAX} W). First: "
            f"'{first[0]}' at lon={first[1]}, lat={first[2]}.{hint}"
        )


# ---------------------------------------------------------------- matching


def match_zones(polys: list[dict], zones: list[dict]) -> tuple[list[tuple], list[dict]]:
    by_id = {z["id"]: z for z in zones}
    by_name = {z["name"].strip().lower(): z for z in zones}
    by_slug = {slug(z["name"]): z for z in zones}

    matched, unmatched, claimed = [], [], set()
    for p in polys:
        zid = (p["ext"].get("zoneId") or "").strip()
        z, how = None, ""
        if zid and zid in by_id:
            z, how = by_id[zid], "zoneId"
        elif p["name"].strip().lower() in by_name:
            z, how = by_name[p["name"].strip().lower()], "name"
        elif slug(p["name"]) in by_slug:
            z, how = by_slug[slug(p["name"])], "slug"

        if z is None:
            unmatched.append(p)
            continue
        if z["id"] in claimed:
            raise SystemExit(
                f"two polygons both resolve to zone '{z['id']}' — refusing to guess. "
                f"Give them distinct names in GE Pro."
            )
        claimed.add(z["id"])
        matched.append((z, p, how))
    return matched, unmatched


def normalise_ring(ring: list[list[float]], keep_closed: bool) -> list[list[float]]:
    """KML always closes its rings; zones.json is mixed (4 closed, 19 open as of v3).
    Preserve whatever convention the zone already used rather than silently flipping it."""
    r = [list(v) for v in ring]
    while len(r) > 1 and r[0] == r[-1]:
        r.pop()
    if keep_closed:
        r.append(list(r[0]))
    return r


# ---------------------------------------------------------------- main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kml", type=Path, help="the .kml or .kmz saved out of Google Earth Pro")
    ap.add_argument("--write", action="store_true", help="apply the changes (default is a dry run)")
    ap.add_argument("--imagery", help="REQUIRED with --write: which imagery was traced, "
                                      "e.g. 'GE Pro historical, 2023-11-04'")
    ap.add_argument("--why", default="", help="one line on what this retrace was for")
    ap.add_argument("--by", default="paul-gep-trace", help="history attribution (default paul-gep-trace)")
    ap.add_argument("--only", help="comma-separated zone ids — ignore everything else in the KML")
    ap.add_argument("--allow-new", action="store_true", help="create zones for unmatched polygons")
    ap.add_argument("--min-shift-ft", type=float, default=0.0,
                    help="skip zones whose centroid moved less than this (default 0 = apply all)")
    args = ap.parse_args()

    if args.write and not args.imagery:
        raise SystemExit(
            "--write requires --imagery. Which capture did you trace against? A retrace with no "
            "imagery provenance can't be judged later — that is exactly what _meta.accuracyHonesty "
            "is about."
        )
    if not args.kml.exists():
        raise SystemExit(f"no such file: {args.kml}")

    doc = json.loads(ZONES.read_text(encoding="utf-8"))
    zones = doc["zones"]

    print(f"reading {args.kml.name}")
    polys = parse_polygons(args.kml)
    check_envelope(polys)
    print(f"  {len(polys)} polygon(s) parsed, all inside the property envelope")

    if args.only:
        want = {s.strip() for s in args.only.split(",")}
        polys = [p for p in polys
                 if (p["ext"].get("zoneId") or slug(p["name"])) in want or p["name"] in want]
        if not polys:
            raise SystemExit(f"--only matched nothing in {args.kml.name}")

    matched, unmatched = match_zones(polys, zones)

    changes, unchanged = [], []
    for z, p, how in matched:
        keep_closed = z["vertices"][0] == z["vertices"][-1]
        new = normalise_ring(p["ring"], keep_closed)
        if new == z["vertices"]:
            unchanged.append(z["id"])
            continue
        old_c, new_c = centroid(z["vertices"]), centroid(new)
        shift_ft = metres_between(old_c, new_c) * 3.28084
        a_old, a_new = ring_area_m2(z["vertices"]), ring_area_m2(new)
        changes.append({
            "zone": z, "new": new, "how": how, "shift_ft": shift_ft,
            "a_old": a_old, "a_new": a_new,
            "dv": len(new) - len(z["vertices"]),
        })

    if args.min_shift_ft > 0:
        held = [c for c in changes if c["shift_ft"] < args.min_shift_ft]
        changes = [c for c in changes if c["shift_ft"] >= args.min_shift_ft]
        if held:
            print(f"  holding {len(held)} zone(s) under --min-shift-ft {args.min_shift_ft}: "
                  f"{', '.join(c['zone']['id'] for c in held)}")

    # ---- report
    print()
    if changes:
        print(f"{'zone':<28} {'match':<7} {'verts':>11} {'centroid':>11} {'area':>22}")
        print("-" * 84)
        for c in sorted(changes, key=lambda c: -c["shift_ft"]):
            z = c["zone"]
            dpct = (c["a_new"] - c["a_old"]) / c["a_old"] * 100 if c["a_old"] else 0.0
            print(f"{z['id']:<28} {c['how']:<7} "
                  f"{len(z['vertices']):>4} -> {len(c['new']):<4} "
                  f"{c['shift_ft']:>9.1f}ft "
                  f"{c['a_old'] * 10.7639:>8,.0f} -> {c['a_new'] * 10.7639:<8,.0f} ft² "
                  f"({dpct:+.0f}%)")
    else:
        print("no geometry changes.")

    if unchanged:
        print(f"\nidentical, untouched ({len(unchanged)}): {', '.join(unchanged)}")
    if unmatched:
        print(f"\nunmatched polygons ({len(unmatched)}): "
              f"{', '.join(p['name'] or '(unnamed)' for p in unmatched)}")
        if not args.allow_new:
            print("  -> not imported. Re-export and edit in place, or pass --allow-new to create them.")
    absent = [z["id"] for z in zones if z["id"] not in {c["zone"]["id"] for c in changes}
              and z["id"] not in unchanged]
    if absent:
        print(f"\nin zones.json but not in this KML ({len(absent)}): {', '.join(absent)}")
        print("  -> left exactly as they are. Nothing is ever deleted by this tool.")

    new_zones = []
    if unmatched and args.allow_new:
        existing = {z["id"] for z in zones}
        for p in unmatched:
            zid = slug(p["name"]) or "unnamed"
            if zid in existing:
                raise SystemExit(f"--allow-new would collide with existing zone id '{zid}'")
            existing.add(zid)
            new_zones.append((zid, p))
        print(f"\nwould CREATE ({len(new_zones)}): {', '.join(z for z, _ in new_zones)}")

    if not args.write:
        print(f"\nDRY RUN — nothing written. Re-run with --write --imagery '<capture>' to apply.")
        return 0

    if not changes and not new_zones:
        print("\nnothing to write.")
        return 0

    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    for c in changes:
        z = c["zone"]
        n_before = len(z["vertices"])
        z["vertices"] = c["new"]
        z["updatedAt"] = now
        z["lastEditedBy"] = args.by
        z.setdefault("history", []).append({
            "at": now, "by": args.by, "action": "retraced",
            "details": {
                "source": f"Google Earth Pro KML ({args.kml.name})",
                "imagery": args.imagery,
                "matchedBy": c["how"],
                "vertexCountBefore": n_before,
                "vertexCountAfter": len(c["new"]),
                "centroidShiftFt": round(c["shift_ft"], 1),
                "areaBeforeFt2": round(c["a_old"] * 10.7639),
                "areaAfterFt2": round(c["a_new"] * 10.7639),
                "why": args.why or "retraced in Google Earth Pro",
                "caveat": "GE Pro imagery resolves finer than NAIP but its georegistration is "
                          "not guaranteed better. Mixing sources injects their relative offset "
                          "into the record — see _meta.accuracyHonesty.",
            },
        })

    for zid, p in new_zones:
        ring = normalise_ring(p["ring"], keep_closed=False)
        zones.append({
            "id": zid, "name": p["name"], "type": p["ext"].get("type") or "planted",
            "color": [122, 149, 104], "vertices": ring, "status": "draft",
            "createdAt": now, "createdBy": args.by, "updatedAt": now, "lastEditedBy": args.by,
            "history": [{"at": now, "by": args.by, "action": "created",
                         "details": {"source": f"Google Earth Pro KML ({args.kml.name})",
                                     "imagery": args.imagery, "vertexCount": len(ring),
                                     "why": args.why or "traced in Google Earth Pro"}}],
        })

    doc["_meta"]["lastBuilt"] = now[:10]
    doc["_meta"]["lastBuiltAt"] = now

    # Atomic, and byte-format-preserving so the git diff shows only what moved.
    payload = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=ZONES.parent,
                                     prefix=".zones.", suffix=".tmp", delete=False) as fh:
        fh.write(payload)
        tmp = Path(fh.name)
    json.loads(tmp.read_text(encoding="utf-8"))  # never leave a broken canon behind
    tmp.replace(ZONES)

    print(f"\nWROTE zones.json — {len(changes)} retraced"
          + (f", {len(new_zones)} created" if new_zones else "") + ".")
    print("  Review it before committing:  git diff --stat zones.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
