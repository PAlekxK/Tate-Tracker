#!/usr/bin/env python3
"""clean-zones.py — the 23 hand-traced Fernwood zones, cleaned into a GAP-FREE, NON-OVERLAPPING set.

    <venv with shapely>/bin/python clean-zones.py            # read zones.json, write zones.cleaned.json + report + exhibit
    ... clean-zones.py --gap 1.0 --simplify 0.35             # tune the two tolerances (metres)

Ruled: Z-13 `[paul-stated 2026-09-10]` — "clean them up visually a little bit so there's no gaps and they
just kind of look better. More cohesive shapes not depending too much on just those vertices I clicked …
go ahead and clean it up as best you can automatically and nothing should overlap … let me know of any
questions." The cleaned set is the PRELOAD for Mom's estate and the new ANSWER KEY.

⛔ WRITES ONLY BESIDE ITSELF. Never `zones.json` (canon; replaced only on Paul's go, through the window that
   owns the write). Output: zones.cleaned.json · clean-report.json · clean-exhibit.jpg.

WHAT IT DOES, in order — every step is TOPOLOGICAL, none is cosmetic (plan §5b: cosmetic smoothing was
shipped 09-04 and measured as "not meaningfully better"; the viewer already rounds at render time):
  0. project WGS84 → local metres (equirectangular about the zone centroid; the property is 400 m across,
     so the error is millimetres)
  1. SIMPLIFY each trace (Douglas-Peucker, topology-preserving) — drops the jitter of close clicks
  2. HOUSE ← the Microsoft building footprint (IoU 0.76 vs the trace, centroid 1.5 m; assessment §1a).
     ⚠️ A ROOF OUTLINE, not walls — flagged as a QUESTION on the exhibit, not asserted
  3. OVERLAPS → zero, with ONE exception: the declared `partOf` (the-green in the-turf) is Paul's own
     statement, so the parent is extended to enclose the child fully and stays WHOLE (the schema has no
     holes; the viewer draws the child on top). Undeclared overlaps: the SMALLER zone keeps its shape, the
     LARGER yields — a small bed traced over a big field is the bed's claim, not the field's. Under 3 m² it is
     trace slop and is removed silently (noted in the report); 3 m² and over is a QUESTION on the exhibit.
  4b. NAMED PAIRS in CLOSE_PAIRS (and --close-pair A:B) are closed whatever the width — by ruling, cited beside the list.
  4. GAPS: a morphological CLOSING of the whole set (buffer out, buffer in, --gap/2 each way) finds every
     sliver narrower than --gap between zones, and every notch that narrow in an outline. Each sliver goes to
     the LARGEST zone it touches (the field absorbs; the bed keeps its trace); after the union the neighbours
     share an edge exactly. Gaps WIDER than --gap are left alone — "a gap is not unclaimed ground".
  5. TIDY: parts under 2 m² dropped, holes under 2 m² filled, a final light simplify (0.10 m) and a final
     snap so shared edges stay shared. Every zone comes out as ONE polygon (or the report says which did not).

WHAT IT CANNOT DO — stated so the reader does not rely on it for these:
  · it cannot say whether two abutting zones share a wall, a path, or a strip of nothing [paul-stated 09-04];
    it closes every sub-tolerance gap because Paul ruled that default on 09-10
  · it cannot tell containment from trace slop; the one declared partOf is honoured, the four undeclared
    overlaps are RESOLVED BY A RULE and FLAGGED, never adjudicated
  · it cannot make a boundary MORE ACCURATE — only the house moves to evidence; everything else is the trace,
    tidied. A cleaned line is not a located line (plan §8·7: nothing here is a ±30 ft record presented as a locate)
"""
import argparse, json, math, os, sys, datetime
from shapely.geometry import Polygon, MultiPolygon, shape, mapping
from shapely.ops import unary_union, snap
from shapely.validation import make_valid

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ZONES = os.path.join(ROOT, "zones.json")
MS = os.path.join(HERE, "anchors-ms-footprints.json")
OUT_JSON = os.path.join(HERE, "zones.cleaned.json")
OUT_REPORT = os.path.join(HERE, "clean-report.json")
OUT_PNG = os.path.join(HERE, "clean-exhibit.jpg")

# Pairs closed BY RULING regardless of width. The bank ↔ eastern woodlands gap (4.8 m) was the one gap the
# 1 m rule left; ux-expert: on an otherwise gapless map the only readable meaning of a hole is "something is
# missing here" — close it or name it. Paul, 2026-09-10: "Yes." The ground between them goes to the larger.
CLOSE_PAIRS = [("the-bank", "eastern-woodlands")]

# ---------- projection ----------
def make_proj(lon0, lat0):
    mlat = 111132.92 - 559.82 * math.cos(2 * math.radians(lat0)) + 1.175 * math.cos(4 * math.radians(lat0))
    mlon = 111412.84 * math.cos(math.radians(lat0)) - 93.5 * math.cos(3 * math.radians(lat0))
    fwd = lambda lon, lat: ((lon - lon0) * mlon, (lat - lat0) * mlat)
    inv = lambda x, y: (lon0 + x / mlon, lat0 + y / mlat)
    return fwd, inv

def to_poly(coords, fwd):
    p = Polygon([fwd(lon, lat) for lon, lat in coords])
    return biggest(make_valid(p))

def biggest(g):
    """One polygon per zone. Returns (polygon, dropped_area_m2)."""
    if g.geom_type == "Polygon":
        return g
    parts = [p for p in getattr(g, "geoms", []) if p.geom_type == "Polygon"]
    if not parts:
        return Polygon()
    return max(parts, key=lambda p: p.area)

def keep_largest(p, k, flags):
    """One polygon per zone; anything sliced off is dropped and, if it mattered, flagged."""
    if p.is_empty or p.geom_type == "Polygon":
        return p
    parts = sorted([q for q in p.geoms if q.geom_type == "Polygon"], key=lambda q: q.area, reverse=True)
    if not parts:
        return Polygon()
    lost = sum(q.area for q in parts[1:])
    if lost >= 2.0:
        flags.append({"kind": "question", "zone": k, "text": f"{k}: an operation sliced off {lost:.0f} m² in {len(parts)-1} piece(s); the largest piece is kept. Look at it."})
    return parts[0]

def tidy(p, min_part=2.0, min_hole=2.0):
    if p.is_empty:
        return p
    p = make_valid(p)
    parts = [p] if p.geom_type == "Polygon" else [q for q in p.geoms if q.geom_type == "Polygon"]
    parts = [q for q in parts if q.area >= min_part] or ([max(parts, key=lambda q: q.area)] if parts else [])
    out = []
    for q in parts:
        holes = [h for h in q.interiors if Polygon(h).area >= min_hole]
        out.append(Polygon(q.exterior, holes))
    return out[0] if len(out) == 1 else MultiPolygon(out)

def ring_coords(p, inv, nd=7):
    ext = [list(map(lambda v: round(v, nd), inv(x, y))) for x, y in list(p.exterior.coords)[:-1]]
    holes = [[list(map(lambda v: round(v, nd), inv(x, y))) for x, y in list(h.coords)[:-1]] for h in p.interiors]
    return ext, holes

# ---------- measurement ----------
def slivers(polys, tol, declared=()):
    """Narrow unclaimed ground between zones: morphological CLOSING of the whole set minus the set.
    Anything narrower than 2*tol between two zones (or a notch that narrow in an outline) shows up here."""
    U = unary_union([p for p in polys.values() if not p.is_empty])
    C = U.buffer(tol, join_style="mitre").buffer(-tol, join_style="mitre")
    S = C.difference(U)
    parts = [S] if S.geom_type == "Polygon" else [q for q in getattr(S, "geoms", []) if q.geom_type == "Polygon"]
    return [q for q in parts if q.area > 0.02]

def pair_stats(polys, tol, declared=()):
    ids = list(polys)
    overlap = 0.0; overlaps = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = polys[ids[i]], polys[ids[j]]
            if a.is_empty or b.is_empty or (ids[i], ids[j]) in declared or (ids[j], ids[i]) in declared:
                continue
            inter = a.intersection(b).area
            if inter > 0.01:
                overlap += inter; overlaps.append((ids[i], ids[j], round(inter, 2)))
    sl = slivers(polys, tol)
    return {"overlap_m2": round(overlap, 1), "overlap_pairs": overlaps,
            "sliver_m2": round(sum(q.area for q in sl), 1), "sliver_count": len(sl)}

# ---------- main ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gap", type=float, default=1.0, help="close gaps narrower than this (m)")
    ap.add_argument("--simplify", type=float, default=0.35, help="Douglas-Peucker tolerance on the raw trace (m)")
    ap.add_argument("--no-house", action="store_true", help="keep the traced house instead of the footprint")
    ap.add_argument("--close-pair", action="append", default=[], metavar="A:B", help="also close the gap between these two zones, whatever its width (repeatable)")
    args = ap.parse_args()

    data = json.load(open(ZONES))
    Z = data["zones"]
    lon0 = sum(v[0] for z in Z for v in z["vertices"]) / sum(len(z["vertices"]) for z in Z)
    lat0 = sum(v[1] for z in Z for v in z["vertices"]) / sum(len(z["vertices"]) for z in Z)
    fwd, inv = make_proj(lon0, lat0)

    raw = {z["id"]: to_poly(z["vertices"], fwd) for z in Z}
    order = [z["id"] for z in Z]
    parent = {z["id"]: z.get("partOf") for z in Z if z.get("partOf")}
    flags = []
    declared = {(c, p) for c, p in parent.items()}
    before = pair_stats(raw, args.gap / 2, declared)

    # 1 · simplify
    P = {k: biggest(make_valid(v.simplify(args.simplify, preserve_topology=True))) for k, v in raw.items()}

    # 2 · house ← footprint
    if not args.no_house and os.path.exists(MS):
        feats = json.load(open(MS))
        cands = [biggest(make_valid(shape(f["geometry"]))) for f in feats]
        cands = [Polygon([fwd(x, y) for x, y in c.exterior.coords]) for c in cands]
        h = P["house"]
        best = max(cands, key=lambda c: c.intersection(h).area / c.union(h).area)
        iou = best.intersection(h).area / best.union(h).area
        if iou >= 0.6:
            P["house"] = best.simplify(0.15, preserve_topology=True)
            flags.append({"kind": "question", "zone": "house",
                          "text": f"house replaced by the Microsoft building footprint (IoU {iou:.2f} vs your trace, "
                                  f"{best.area:.0f} m² vs {h.area:.0f} m²). A roof outline — porch/deck not included. Keep it, or your trace?"})
        else:
            flags.append({"kind": "note", "zone": "house", "text": f"footprint IoU {iou:.2f} < 0.6 — traced house kept"})

    # 3 · overlaps → zero
    def resolve_overlaps():
        changed = True; passes = 0
        while changed and passes < 6:
            changed = False; passes += 1
            for i in range(len(order)):
                for j in range(i + 1, len(order)):
                    a, b = order[i], order[j]
                    if P[a].is_empty or P[b].is_empty:
                        continue
                    inter = P[a].intersection(P[b]).area
                    if inter <= 0.005:
                        continue
                    if parent.get(a) == b or parent.get(b) == a:
                        child, par = (a, b) if parent.get(a) == b else (b, a)
                        # declared containment: the parent absorbs the child fully and stays whole (the schema has no holes;
                        # the viewer draws the child on top). This is the ONE overlap that survives, by Paul's own declaration.
                        if not P[child].within(P[par].buffer(0.01)):
                            P[par] = tidy(P[par].union(P[child]))
                            flags.append({"kind": "note", "zone": child, "text": f"{child} is declared partOf {par}: {par} extended to enclose it fully (was {inter:.0f} m² inside)"})
                        continue
                    else:
                        small, large = (a, b) if P[a].area <= P[b].area else (b, a)
                        P[large] = keep_largest(tidy(P[large].difference(P[small])), large, flags)
                        if inter >= 3.0:
                            flags.append({"kind": "question", "zone": large,
                                          "text": f"{large} overlapped {small} by {inter:.0f} m²; the smaller ({small}) kept its shape and {large} yielded. Right way round?"})
                        else:
                            flags.append({"kind": "note", "zone": large, "text": f"{large}/{small}: {inter:.1f} m² of trace slop removed from {large}"})
                    changed = True
    resolve_overlaps()

    # 4 · close gaps: every sliver narrower than --gap between zones (and any notch that narrow in an outline)
    #     goes to the LARGEST zone it touches — the field absorbs, the bed keeps its trace
    def close_gaps():
        for _ in range(3):
            sl = slivers(P, args.gap / 2)
            if not sl:
                break
            for q in sl:
                nb = [k for k in order if not P[k].is_empty and P[k].distance(q) < 0.02]
                if not nb:
                    continue
                large = max(nb, key=lambda k: P[k].area)
                others = unary_union([P[k] for k in order if k != large and not P[k].is_empty])
                q2 = q.buffer(0.03, join_style="mitre").difference(others)   # a hair of overlap so the union FUSES
                P[large] = keep_largest(tidy(P[large].union(q2)), large, flags)
    close_gaps()

    # 4b · named pairs closed by ruling, whatever the width: the lens within reach of BOTH, touching both, minus everyone else
    def close_pair(a, b):
        A, B = P[a], P[b]
        d = A.distance(B)
        if d == 0:
            return
        # the ground between the two FACING stretches of boundary: hull of every vertex of each within reach of the other
        from shapely.geometry import MultiPoint
        from shapely.ops import nearest_points
        reach = d + 2.0
        pts = [c for c in A.exterior.coords if B.distance(Polygon([c, c, c]).centroid) <= reach] + \
              [c for c in B.exterior.coords if A.distance(Polygon([c, c, c]).centroid) <= reach]
        pts += [(q.x, q.y) for q in nearest_points(A, B)]
        g = MultiPoint(pts).convex_hull.difference(A).difference(B)
        parts = [g] if g.geom_type == "Polygon" else [q for q in getattr(g, "geoms", []) if q.geom_type == "Polygon"]
        parts = [q for q in parts if q.distance(A) < 0.02 and q.distance(B) < 0.02]
        if not parts:
            flags.append({"kind": "question", "zone": a, "text": f"{a} ↔ {b}: asked to close a {d:.1f} m gap but no ground lies between them that touches both"}); return
        large = a if A.area >= B.area else b
        others = unary_union([P[k] for k in order if k not in (a, b) and not P[k].is_empty])
        sliver = unary_union(parts).buffer(0.03, join_style="mitre").difference(others)
        P[large] = keep_largest(tidy(P[large].union(sliver)), large, flags)
        flags.append({"kind": "note", "zone": large, "text": f"{a} ↔ {b}: {d:.1f} m gap closed by ruling; {sliver.area:.0f} m² went to {large}"})
    for a, b in CLOSE_PAIRS + [tuple(x.split(":")) for x in args.close_pair]:
        close_pair(a, b)
    resolve_overlaps()

    # 5 · tidy + final snap so shared edges are shared
    for k in order:
        P[k] = tidy(P[k])
    for _ in range(2):
        for i in range(len(order)):
            for j in range(len(order)):
                if i != j and not P[order[i]].is_empty and not P[order[j]].is_empty and P[order[i]].distance(P[order[j]]) < 0.15:
                    P[order[i]] = tidy(snap(P[order[i]], P[order[j]], 0.15))
    for k in order:
        P[k] = keep_largest(tidy(make_valid(P[k].simplify(0.10, preserve_topology=True))), k, flags)
    resolve_overlaps()
    close_gaps()
    resolve_overlaps()
    for k in order:
        P[k] = keep_largest(P[k], k, flags)

    after = pair_stats(P, args.gap / 2, declared)
    seen = set(); flags[:] = [f for f in flags if not (f["text"] in seen or seen.add(f["text"]))]

    # ---------- write candidate ----------
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    out = json.loads(json.dumps(data))
    per = []
    for z in out["zones"]:
        k = z["id"]; p = P[k]
        p1 = p if p.geom_type == "Polygon" else max(p.geoms, key=lambda q: q.area)
        ext, holes = ring_coords(p1, inv)
        a0, a1 = raw[k].area, p1.area
        z["vertices"] = ext
        if holes:
            z["holes"] = holes
        z["status"] = "draft"
        z["updatedAt"] = now
        z["lastEditedBy"] = "clean-zones.py"
        z.setdefault("history", []).append({"at": now, "by": "clean-zones.py", "action": "cleaned",
            "details": {"ruling": "Z-13 [paul-stated 2026-09-10]", "vertexCount": len(ext),
                        "areaBefore_m2": round(a0, 1), "areaAfter_m2": round(a1, 1),
                        "method": f"simplify {args.simplify} m · overlaps→0 · gaps<{args.gap} m closed · house←footprint"}})
        per.append({"id": k, "verts_before": len(raw[k].exterior.coords) - 1, "verts_after": len(ext),
                    "area_before": round(a0, 1), "area_after": round(a1, 1), "delta_pct": round((a1 - a0) / a0 * 100, 1) if a0 else None,
                    "holes": len(holes)})
    out["_meta"]["cleaned"] = {"at": now, "by": "clean-zones.py", "ruling": "Z-13", "from": "zones.json @ working tree",
                               "note": "CANDIDATE — not canon until Paul's go. holes[] is new and optional: rings cut out of a parent for a declared partOf child."}
    json.dump(out, open(OUT_JSON, "w"), indent=1)

    report = {"at": now, "params": vars(args), "before": before, "after": after, "zones": per, "flags": flags,
              "totals": {"verts_before": sum(x["verts_before"] for x in per), "verts_after": sum(x["verts_after"] for x in per),
                         "area_before": round(sum(x["area_before"] for x in per), 1), "area_after": round(sum(x["area_after"] for x in per), 1)}}
    json.dump(report, open(OUT_REPORT, "w"), indent=1)

    # ---------- console ----------
    print(f"zones: {len(order)} · vertices {report['totals']['verts_before']} → {report['totals']['verts_after']}"
          f" · area {report['totals']['area_before']:.0f} → {report['totals']['area_after']:.0f} m²")
    print(f"overlap (undeclared)  {before['overlap_m2']:>7.1f} m² in {len(before['overlap_pairs'])} pairs → {after['overlap_m2']:.1f} m² in {len(after['overlap_pairs'])} pairs")
    print(f"slivers <{args.gap} m wide  {before['sliver_m2']:>6.1f} m² in {before['sliver_count']} pieces → {after['sliver_m2']:.1f} m² in {after['sliver_count']} pieces")
    for x in per:
        if abs(x["delta_pct"] or 0) >= 8:
            print(f"  ⚠ {x['id']:30s} area {x['area_before']:>7.1f} → {x['area_after']:>7.1f} m² ({x['delta_pct']:+.0f}%)")
    print(f"{len(flags)} flag(s):")
    for f in flags:
        print(f"  {'❓' if f['kind']=='question' else '·'} {f['text']}")
    print(f"wrote {os.path.basename(OUT_JSON)} · {os.path.basename(OUT_REPORT)}")

    # ---------- exhibit ----------
    try:
        render(raw, P, flags, inv, args)
    except Exception as e:  # the numbers stand even if the picture fails
        print(f"exhibit not rendered: {e}", file=sys.stderr)

def render(raw, P, flags, inv, args):
    from PIL import Image, ImageDraw, ImageFont
    bounds = json.load(open(os.path.join(ROOT, "images/property-map/base-naip-2022-01-leafoff.bounds.json")))
    B = bounds["bounds"]; W = bounds["pixelWidth"]; H = bounds["pixelHeight"]
    base = Image.open(os.path.join(ROOT, "images/property-map/base-naip-2022-01-leafoff.png")).convert("RGB")
    px = lambda lon, lat: ((lon - B["west"]) / (B["east"] - B["west"]) * W, (B["north"] - lat) / (B["north"] - B["south"]) * H)
    try: fnt = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 26); small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    except Exception: fnt = small = None

    def frame(polys, margin, width):
        """crop the base to these polygons + margin, scaled to `width` px; returns (image, metre→pixel fn)"""
        xs = [x for p in polys for x, y in p.exterior.coords]; ys = [y for p in polys for x, y in p.exterior.coords]
        lonlat = [inv(x, y) for x, y in [(min(xs) - margin, min(ys) - margin), (max(xs) + margin, max(ys) + margin)]]
        (x0, y1), (x1, y0) = px(*lonlat[0]), px(*lonlat[1])
        x0, y0, x1, y1 = int(max(0, x0)), int(max(0, y0)), int(min(W, x1)), int(min(H, y1))
        crop = base.crop((x0, y0, x1, y1)); scale = width / crop.width
        crop = crop.resize((width, int(crop.height * scale)), Image.LANCZOS)
        def pp(x, y):
            lon, lat = inv(x, y); X, Y = px(lon, lat)
            return ((X - x0) * scale, (Y - y0) * scale)
        return crop, pp

    def panel(crop, pp, polys, title, colour, show_flags=False, lw=3):
        im = crop.copy(); d = ImageDraw.Draw(im, "RGBA")
        for k, p in polys.items():
            parts = [p] if p.geom_type == "Polygon" else list(p.geoms)
            for q in parts:
                if q.is_empty: continue
                d.polygon([pp(*c) for c in q.exterior.coords], fill=colour + (55,), outline=colour + (255,), width=lw)
            c = p.representative_point()
            d.text(pp(c.x, c.y), k, fill=(255, 255, 255, 230), font=small, anchor="mm")
        if show_flags:
            n = 1
            for f in flags:
                if f["kind"] != "question": continue
                p = polys.get(f["zone"])
                if p is None or p.is_empty: continue
                c = p.representative_point(); X, Y = pp(c.x, c.y)
                d.ellipse([X - 18, Y - 18 - 24, X + 18, Y + 18 - 24], fill=(255, 60, 60, 230)); d.text((X, Y - 24), str(n), fill="white", font=fnt, anchor="mm"); n += 1
        d.rectangle([8, 8, 8 + d.textlength(title, font=fnt) + 16, 48], fill=(0, 0, 0, 170)); d.text((16, 14), title, fill="white", font=fnt)
        return im

    wide, ppw = frame(list(raw.values()), 25, 1400)
    core_ids = [k for k in raw if raw[k].area < 400]          # the built core: everything but the fields
    core, ppc = frame([raw[k] for k in core_ids], 8, 1400)
    a = panel(wide, ppw, raw, "BEFORE — the 23 as traced (zones.json)", (255, 255, 255))
    b = panel(wide, ppw, P, f"AFTER — cleaned candidate (gaps<{args.gap} m closed · no overlaps · house=footprint)", (120, 255, 140), show_flags=True)
    c = panel(core, ppc, raw, "BEFORE — the built core, zoomed", (255, 255, 255), lw=4)
    e = panel(core, ppc, P, "AFTER — the built core, zoomed", (120, 255, 140), show_flags=True, lw=4)
    qs = [f for f in flags if f["kind"] == "question"]
    legend_h = 40 + 30 * len(qs)
    out = Image.new("RGB", (a.width * 2 + 20, a.height + c.height + 20 + legend_h), (20, 20, 20))
    out.paste(a, (0, 0)); out.paste(b, (a.width + 20, 0))
    out.paste(c, (0, a.height + 20)); out.paste(e, (a.width + 20, a.height + 20))
    d = ImageDraw.Draw(out)
    y = a.height + c.height + 30
    for i, f in enumerate(qs, 1):
        d.text((12, y), f"{i}. {f['text']}", fill=(255, 220, 220), font=small); y += 30
    out.save(OUT_PNG, quality=88, optimize=True)
    print(f"wrote {os.path.basename(OUT_PNG)}")

if __name__ == "__main__":
    sys.exit(main())
