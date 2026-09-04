#!/usr/bin/env python3
"""zone-topology-report — what the zone geometry actually looks like. READ-ONLY.

⛔ THIS TOOL NEVER WRITES. No --fix, no --repair, no snap pass. It reports; a human rules.
   That is not caution, it is the record's own position — see CONTAINMENT below.

WHY IT EXISTS. Every number in `.plans/2026-09-04-map-region-smoothing-PLAN.md` was computed
by four throwaway scripts in a session scratchpad. The plan carried the NUMBERS and not the
METHOD, so none of its tables could be re-derived or challenged — and the scripts were minutes
from cleanup when the session that wrote them closed. Recovered and consolidated 2026-09-04.
The plan's §7 asks for exactly this tool; this is that, not new scope.

WHAT IT MEASURES
  --geometry     per-zone: vertex count, area, perimeter, segment lengths, sharp turns
  --pairs        zone-pair proximity: slivers, gaps, and vertex-to-VERTEX vs vertex-to-EDGE
  --snap         what a snap tolerance would actually collapse (union-find clustering)
  --smooth       Chaikin displacement and its AREA BIAS; Douglas-Peucker retention
  --containment  overlaps, and which of them declare `partOf`
  (no flag = all)

⭐ THE POSITIVE CONTROL. `_meta.schemaNotes` records that `the-green` tests **60%** inside
`the-turf`. This tool recomputes that pair on every run and fails loudly if its own method does
not reproduce the record's number. A measurement tool that has never been checked against a
known value is an opinion with a decimal point.

⛔ CONTAINMENT CANNOT BE SETTLED BY GEOMETRY, and the record says so first. `_meta.schemaNotes`
on the one declared `partOf` reads: *"Recorded because Paul stated the containment, NOT derived
from geometry: the-green's vertices test only 60% inside the-turf."* So an undeclared overlap is
one of {undeclared containment, a real overlap defect, trace slop} and no amount of arithmetic
separates them. The tool prints the candidates and stops. Geometry proposes; Paul rules.

⚠️ ACCURACY BUDGET. Vertices are WGS84 traced against a 0.6 m/px January NAIP frame with long
shadows; the record's stated budget is ±9.1 m. Median segment spacing is ~2.5 m. A boundary
sampled every 2.5 m with 9 m of error per sample is a random walk with a corner at every sample
— which is why "the vertices look ragged" is mostly instrument noise, not carelessness.
⛔ Therefore a snap tolerance is bounded by vertex SPACING, never by the accuracy budget:
snapping at ±9.1 m destroys the map. Run --snap and read the collapse before choosing one.
"""
import json, math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZONES = os.path.join(ROOT, "zones.json")
LAT0, MPD_LAT = 34.5496, 111132.0
MPD_LON = 111320.0 * math.cos(math.radians(LAT0))
CONTROL = ("the-green", "the-turf", 0.60, 0.02)   # id, container, expected fraction, tolerance


def load():
    Z = json.load(open(ZONES, encoding="utf-8"))
    zs = [z for z in Z["zones"] if z.get("vertices")]
    P = {z["id"]: [(v[0] * MPD_LON, v[1] * MPD_LAT) for v in z["vertices"]] for z in zs}
    return Z, zs, P


def segs(p):  return [(p[i], p[(i + 1) % len(p)]) for i in range(len(p))]
def area(p):  return abs(sum(p[i][0] * p[(i + 1) % len(p)][1] - p[(i + 1) % len(p)][0] * p[i][1]
                             for i in range(len(p)))) / 2
def perim(p): return sum(math.dist(*s) for s in segs(p))


def pt_seg(p, a, b):
    vx, vy = b[0] - a[0], b[1] - a[1]
    L = vx * vx + vy * vy
    if L == 0: return math.dist(p, a), 0.0
    t = max(0, min(1, ((p[0] - a[0]) * vx + (p[1] - a[1]) * vy) / L))
    return math.dist(p, (a[0] + t * vx, a[1] + t * vy)), t


def inside(pt, poly):
    x, y = pt; c = False; n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i - 1) % n]
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1): c = not c
    return c


def frac_inside(a, b):
    return sum(1 for p in a if inside(p, b)) / len(a)


def control(P):
    """Reproduce the record's own stated figure, or say the method has drifted."""
    a, b, want, tol = CONTROL
    if a not in P or b not in P:
        return None, f"⚠ control pair {a}/{b} not in the record — cannot self-check"
    got = frac_inside(P[a], P[b])
    ok = abs(got - want) <= tol
    return ok, (f"{'✅' if ok else '🔴'} positive control: {a} inside {b} = {got:.0%} "
                f"(record states {want:.0%})" + ("" if ok else "  ⛔ METHOD HAS DRIFTED — do not trust the rest"))


def r_geometry(zs, P):
    print("── PER-ZONE GEOMETRY")
    print(f"  {'id':30}{'n':>4}{'area m²':>10}{'perim m':>9}{'min':>7}{'med':>7}{'max':>7}{'sharp':>7}")
    allseg = []
    for z in zs:
        p = P[z["id"]]; sl = sorted(math.dist(*s) for s in segs(p)); allseg += sl
        sharp = 0
        for i in range(len(p)):
            a, b, c = p[(i - 1) % len(p)], p[i], p[(i + 1) % len(p)]
            v1 = (a[0] - b[0], a[1] - b[1]); v2 = (c[0] - b[0], c[1] - b[1])
            m1, m2 = math.hypot(*v1), math.hypot(*v2)
            if m1 and m2:
                cs = max(-1, min(1, (v1[0] * v2[0] + v1[1] * v2[1]) / (m1 * m2)))
                if 180 - math.degrees(math.acos(cs)) > 60: sharp += 1
        print(f"  {z['id']:30}{len(p):>4}{area(p):>10.0f}{perim(p):>9.1f}"
              f"{sl[0]:>7.2f}{sl[len(sl)//2]:>7.2f}{sl[-1]:>7.2f}{sharp:>7}")
    allseg.sort()
    print(f"\n  {len(allseg)} segments · median {allseg[len(allseg)//2]:.2f} m against a ±9.1 m budget")
    print("  ⚠ Sampling finer than the error is what makes a traced line look ragged.")


def r_pairs(zs, P):
    print("── ZONE-PAIR PROXIMITY  (⛔ a gap is not unclaimed ground)")
    ids = [z["id"] for z in zs]; rows = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            A, B = P[ids[i]], P[ids[j]]
            best, interior = 1e18, False
            for p in A:
                for k in range(len(B)):
                    d, t = pt_seg(p, B[k], B[(k + 1) % len(B)])
                    if d < best: best, interior = d, 0.05 < t < 0.95
            for p in B:
                for k in range(len(A)):
                    d, t = pt_seg(p, A[k], A[(k + 1) % len(A)])
                    if d < best: best, interior = d, 0.05 < t < 0.95
            if best < 3.0: rows.append((best, ids[i], ids[j], interior))
    rows.sort()
    ve = sum(1 for r in rows if r[3])
    for b, a, c, it in rows:
        print(f"  {b:6.2f} m  {a:26} {c:26} {'vertex-to-EDGE' if it else 'vertex-to-vertex'}")
    print(f"\n  {len(rows)} pair(s) under 3 m; {ve} are vertex-to-EDGE.")
    print("  ⛔ Vertex snapping cannot close a vertex-to-EDGE gap — that is why a snap pass under-delivers.")
    print("  ⛔ Which of these abut and which have a wall, a path or a strip of nothing between them")
    print("     is NOT derivable here [paul-stated 2026-09-04]. Geometry proposes; Paul rules.")


def r_snap(zs, P):
    print("── SNAP TOLERANCE — what it would actually collapse")
    items = [(zid, i, p[0], p[1]) for zid, pts in P.items() for i, p in enumerate(pts)]
    N = len(items)
    for tol in (0.25, 0.5, 1.0, 2.0, 3.0):
        parent = list(range(N))
        def find(a):
            while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
            return a
        for i in range(N):
            for j in range(i + 1, N):
                if abs(items[i][2] - items[j][2]) < tol and math.dist(items[i][2:], items[j][2:]) < tol:
                    ra, rb = find(i), find(j)
                    if ra != rb: parent[rb] = ra
        cl = {}
        for i in range(N): cl.setdefault(find(i), []).append(i)
        multi = [v for v in cl.values() if len(v) > 1]
        biggest = max((len(v) for v in multi), default=0)
        move = max((math.dist((sum(items[i][2] for i in v) / len(v),
                               sum(items[i][3] for i in v) / len(v)), items[i][2:])
                    for v in multi for i in v), default=0)
        print(f"  tol {tol:4.2f} m → {len(cl):3d} nodes from {N} vertices · "
              f"largest cluster {biggest:3d} · max point moved {move:5.2f} m")
    print("\n  ⛔ Tolerance is bounded by vertex SPACING (~0.5 m here), NOT by the ±9.1 m accuracy")
    print("     budget. The intuitive choice destroys the map — read the largest-cluster column.")


def r_smooth(zs, P):
    print("── SMOOTHING  (⛔ render-time only — never write this to the data)")
    def chaikin(p, it=2):
        for _ in range(it):
            out = []
            for i in range(len(p)):
                a, b = p[i], p[(i + 1) % len(p)]
                out.append((0.75 * a[0] + 0.25 * b[0], 0.75 * a[1] + 0.25 * b[1]))
                out.append((0.25 * a[0] + 0.75 * b[0], 0.25 * a[1] + 0.75 * b[1]))
            p = out
        return p
    alld, shrink = [], []
    for z in zs:
        p = P[z["id"]]; sm = chaikin(p)
        ds = [min(pt_seg(v, sm[i], sm[(i + 1) % len(sm)])[0] for i in range(len(sm))) for v in p]
        alld += ds
        a0, a1 = area(p), area(sm)
        shrink.append((z["id"], a0, a1, (a1 - a0) / a0 * 100 if a0 else 0))
    alld.sort()
    print(f"  displacement: median {alld[len(alld)//2]:.2f} m · p90 {alld[int(len(alld)*.9)]:.2f} m · "
          f"max {alld[-1]:.2f} m  (budget ±9.1 m)")
    print("\n  ⭐ AREA BIAS — the reason this must never be written to canon:")
    for zid, a0, a1, pct in sorted(shrink, key=lambda r: r[3])[:5]:
        print(f"    {zid:30} {a0:8.0f} → {a1:8.0f} m²  ({pct:+.1f}%)")
    print("  Chaikin is biased INWARD on small convex rings. Displacement stays inside the noise")
    print("  while AREA does not — so every distance check reads green while the smallest zones shrink.")


def r_containment(Z, zs, P):
    print("── CONTAINMENT / OVERLAP  ⛔ GEOMETRY CANNOT SETTLE THIS")
    declared = {z["id"]: z.get("partOf") for z in Z["zones"] if z.get("partOf")}
    print(f"  `partOf` declared on {len(declared)} zone(s): "
          f"{', '.join(f'{k}→{v}' for k, v in declared.items()) or '(none)'}")
    ids = [z["id"] for z in zs]; rows = []
    for a in ids:
        for b in ids:
            if a == b: continue
            f = frac_inside(P[a], P[b])
            if f >= 0.30:
                rows.append((f, a, b, area(P[a]), area(P[b]), declared.get(a) == b))
    rows.sort(reverse=True)
    if not rows:
        print("  no zone has ≥30% of its vertices inside another."); return
    print(f"\n  {'zone':28}{'inside':28}{'frac':>6}{'  areas m²':>14}   declared?")
    for f, a, b, aa, ab, dec in rows:
        flag = "✅ partOf" if dec else "⚠ UNDECLARED"
        note = ""
        if not dec and aa >= ab * 0.8:
            note = "   ← nearly same size; almost certainly NOT containment"
        print(f"  {a:28}{b:28}{f:>5.0%}{aa:>8.0f}/{ab:<6.0f} {flag}{note}")
    print("\n  ⛔ Each UNDECLARED row is one of: undeclared containment · a real overlap defect ·")
    print("     trace slop. Geometry cannot separate them, and the record agrees — the ONE declared")
    print("     partOf was recorded because Paul stated it, and tests only 60% by geometry.")
    print("  → These belong in a walk-the-ground conversation, not a repair script.")


def main():
    if not os.path.exists(ZONES):
        print(f"no zones.json at {ZONES}", file=sys.stderr); return 2
    Z, zs, P = load()
    want = set(a.lstrip("-") for a in sys.argv[1:]) or {"geometry", "pairs", "snap", "smooth", "containment"}
    print(f"── ZONE TOPOLOGY REPORT · {len(zs)} zone(s) · "
          f"{sum(len(v) for v in P.values())} vertices · READ-ONLY\n")
    ok, msg = control(P)
    print("  " + msg + "\n")
    if ok is False:
        return 1
    for name, fn in (("geometry", lambda: r_geometry(zs, P)), ("pairs", lambda: r_pairs(zs, P)),
                     ("snap", lambda: r_snap(zs, P)), ("smooth", lambda: r_smooth(zs, P)),
                     ("containment", lambda: r_containment(Z, zs, P))):
        if name in want:
            fn(); print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
