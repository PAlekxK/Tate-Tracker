#!/usr/bin/env python3
"""Georeference a Google Earth Web capture using Earth's OWN cursor lat/lon readout.

WHY (2026-09-01). Paul found the best view of this property that exists: Google Earth's
2018-04-12 capture — leaf-off at a ~64 deg sun, against the 2022-01-10 NAIP frame the
zones were actually traced on at 33.4 deg. Roughly a third of the shadow. A screen
capture carries no bounds, so it cannot become a layer until it is registered.

⚠️ THIS IS THE THING THAT DESTROYED THE v1 ZONES — AND THE DIFFERENCE IS THE WHOLE POINT.
The 2015 base was a Google Earth screenshot, and polygons stored fractions OF THAT JPEG.
The record then said where a zone APPEARED IN A PICTURE, not where it IS; swap the picture
and every polygon moved. That is not what happens here. This tool SOLVES the image's
bounds and writes them to a sidecar. Vertices stay real WGS84 and are never touched. The
failure in 2015 was the coordinate system, not the source.

HOW — and why it is not correlation
  A first version matched the capture against the NAIP frame by normalised cross-
  correlation. It scored 0.21 and got WORSE at higher resolution — the signature of a
  model mismatch, not noise. Earth Web renders a PERSPECTIVE camera over real terrain, so
  a single scale+translation cannot fit: across the four control points below Earth
  reported ground elevations of 827-898 m, a 71 m spread inside one frame.

  So instead of guessing, ask Earth. Hovering the cursor makes it print the lat/lon under
  that pixel, terrain included. Four corners give an exact projective homography
  (8 unknowns, 8 equations) that models the perspective properly. This is Google's own
  answer for where each pixel lands, not an inference of ours.

⚠️ WHAT IT STILL CANNOT DO
  A homography is exact for a PLANE. This ground is not one. Between the control points
  the fit is good; over a knoll or a steep bank it will drift, most where relief departs
  furthest from the plane through those four corners. So: use this layer to SEE an edge
  the January frame buries in shadow. It is not a survey, and it does not supersede
  zones.json _meta.accuracyHonesty. Check anything traced here against a NAIP frame.

LICENSE: Google imagery, display-only. Output stays in gitignored .local/.
"""
from __future__ import annotations

import argparse, json, math, sys
from pathlib import Path
from PIL import Image

REPO = Path(__file__).resolve().parent.parent
REF_BND = REPO / "images/property-map/base-naip-2022-01-leafoff.bounds.json"


def dms(s: str) -> float:
    p = s.split()
    v = float(p[0]) + float(p[1]) / 60 + float(p[2]) / 3600
    return -v if p[3].upper() in ("W", "S") else v


def solve(M: list[list[float]], b: list[float]) -> list[float]:
    """Gaussian elimination with partial pivoting."""
    n = len(b)
    A = [row[:] + [b[i]] for i, row in enumerate(M)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(A[r][c]))
        if abs(A[p][c]) < 1e-14:
            raise SystemExit("singular system — control points are degenerate (collinear?)")
        A[c], A[p] = A[p], A[c]
        for r in range(n):
            if r != c:
                f = A[r][c] / A[c][c]
                for k in range(c, n + 1):
                    A[r][k] -= f * A[c][k]
    return [A[i][n] / A[i][i] for i in range(n)]


def homography(src, dst):
    """8-parameter projective map src(x,y) -> dst(u,v). Needs exactly 4 point pairs."""
    M, b = [], []
    for (x, y), (u, v) in zip(src, dst):
        M.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u)
        M.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
    h = solve(M, b) + [1.0]
    return h


def apply_h(h, x, y):
    d = h[6] * x + h[7] * y + h[8]
    return (h[0] * x + h[1] * y + h[2]) / d, (h[3] * x + h[4] * y + h[5]) / d


def invert_h(h):
    a, b_, c, d, e, f, g, i, j = h
    A = [[a, b_, c], [d, e, f], [g, i, j]]
    det = (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
    if abs(det) < 1e-30:
        raise SystemExit("non-invertible homography")
    inv = [[0]*3 for _ in range(3)]
    for r in range(3):
        for cc in range(3):
            m = [[A[rr][ccc] for ccc in range(3) if ccc != r] for rr in range(3) if rr != cc]
            cof = m[0][0]*m[1][1] - m[0][1]*m[1][0]
            inv[r][cc] = ((-1) ** (r + cc)) * cof / det
    return [inv[0][0], inv[0][1], inv[0][2], inv[1][0], inv[1][1], inv[1][2],
            inv[2][0], inv[2][1], inv[2][2]]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("points", type=Path, help="the .points.json beside the capture")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()

    spec = json.loads(args.points.read_text())
    cap_path = args.points.parent / spec["capture"]
    cap = Image.open(cap_path).convert("RGB")
    cx0, cy0, cx1, cy1 = spec["cropCssRegion"]
    sx = cap.width / (cx1 - cx0)     # device px per CSS px
    sy = cap.height / (cy1 - cy0)

    pts = spec["points"]
    if len(pts) != 4:
        raise SystemExit("need exactly 4 control points for an exact homography")
    src = [((p["cssX"] - cx0) * sx, (p["cssY"] - cy0) * sy) for p in pts]
    dst = [(dms(p["lonDMS"]), dms(p["latDMS"])) for p in pts]

    h = homography(src, dst)
    resid = max(math.hypot(apply_h(h, *s)[0] - d[0], apply_h(h, *s)[1] - d[1])
                for s, d in zip(src, dst))
    print(f"capture    {cap_path.name} {cap.size}   date {spec['captureDate']}")
    print(f"homography exact-fit residual {resid*111320:.4f} m at the control points "
          f"(exact by construction — this only proves the solve)")

    elevs = [p["elevM"] for p in pts]
    print(f"           terrain across the frame: {min(elevs)}-{max(elevs)} m "
          f"({max(elevs)-min(elevs)} m spread) — why a flat fit could not work")

    bnd = json.loads(REF_BND.read_text())["bounds"]
    hi = invert_h(h)

    # ⭐ NATIVE RESOLUTION, OWN BOUNDS — and this is the whole point of a zoomed capture.
    # Resampling a 0.17 m/px zoom onto the shared 1500 px frame would put it back at
    # ~0.5 m/px and throw away exactly the detail it was taken for. Paul found this the
    # hard way: "the resolution still gets really poor when I zoom in." So the output
    # keeps the capture's own pixel count and carries its own bounds; the tracing tool
    # positions it from those. Perspective is still removed — the warp is onto an
    # axis-aligned lat/lon grid — so it stays a drop-in overlay, just a sharper one.
    corners = [apply_h(h, 0, 0), apply_h(h, cap.width, 0),
               apply_h(h, 0, cap.height), apply_h(h, cap.width, cap.height)]
    own = {"west": min(c[0] for c in corners), "east": max(c[0] for c in corners),
           "south": min(c[1] for c in corners), "north": max(c[1] for c in corners)}
    W, H = cap.width, cap.height
    bnd = own
    out = Image.new("RGB", (W, H), (16, 18, 16))
    op, ip = out.load(), cap.load()
    inside = 0
    for py in range(H):
        lat = bnd["north"] - (py + 0.5) / H * (bnd["north"] - bnd["south"])
        for px in range(W):
            lon = bnd["west"] + (px + 0.5) / W * (bnd["east"] - bnd["west"])
            ix, iy = apply_h(hi, lon, lat)
            xi, yi = int(ix), int(iy)
            if 0 <= xi < cap.width and 0 <= yi < cap.height:
                op[px, py] = ip[xi, yi]
                inside += 1
    ref_b = json.loads(REF_BND.read_text())["bounds"]
    fw = ref_b["east"] - ref_b["west"]; fh = ref_b["north"] - ref_b["south"]
    cw = min(own["east"], ref_b["east"]) - max(own["west"], ref_b["west"])
    chh = min(own["north"], ref_b["north"]) - max(own["south"], ref_b["south"])
    cov = max(0.0, cw) * max(0.0, chh) / (fw * fh)
    span_m = (own["east"] - own["west"]) * 111320 * math.cos(math.radians(34.5496))
    print(f"native     {W}x{H} px over {span_m:.0f} m  ->  {span_m/W:.3f} m/px "
          f"({0.6/(span_m/W):.1f}x NAIP)")
    print(f"coverage   {cov*100:.1f}% of the traced frame — it is a WINDOW, positioned by "
          f"its own bounds, not stretched to the frame")

    out_path = args.out or (args.points.parent / f"trace-gearth-{spec['captureDate']}.png")
    out.save(out_path)
    print(f"saved      {out_path}")

    # metres per pixel of the SOURCE, measured through the solved homography
    lon0, lat0 = apply_h(h, 0, cap.height / 2)
    lon1, _ = apply_h(h, cap.width, cap.height / 2)
    mpp = abs(lon1 - lon0) * 111320 * math.cos(math.radians(lat0)) / cap.width

    side = out_path.with_suffix(".bounds.json")
    side.write_text(json.dumps({
        "image": out_path.name,
        "source": "Google Earth Web screen capture",
        "captureDate": spec["captureDate"],
        "dateProvenance": spec["dateSource"],
        "license": "⛔ Google imagery — display only, NOT redistributable. Gitignored on "
                   "purpose. Never commit, never serve from Pages, never set as "
                   "zones.json _meta.baseImage. The committed basemap stays NAIP.",
        "registration": {
            "method": "projective homography from 4 control points read off Google Earth's "
                      "OWN cursor lat/lon readout at this exact camera",
            "whyNotCorrelation": "an NCC fit against the NAIP leaf-off frame scored 0.21 and "
                                 "DEGRADED at higher resolution — Earth Web is a perspective "
                                 "camera over real terrain, and a scale+translation cannot "
                                 "model it. Earth reported 827-898 m of ground elevation "
                                 "across these four points.",
            "sourceMetresPerPixel": round(mpp, 4),
            "frameCoverage": round(cov, 3),
        },
        "accuracyCaveat": "A homography is exact for a PLANE and this ground is not one. The "
                          "fit is good between the control points and drifts where relief "
                          "departs from the plane through them. FOR SEEING an edge the "
                          "January frame buries in shadow — not a survey. Does not supersede "
                          "zones.json _meta.accuracyHonesty; check traces against NAIP.",
        "controlPoints": pts,
        "bounds": own,
        "pixelWidth": W, "pixelHeight": H,
        "registeredTo": "warped to an axis-aligned lat/lon grid at NATIVE resolution, carrying "
                        "its OWN bounds. NOT stretched to the NAIP frame — doing that would "
                        "resample a 0.1-0.2 m/px zoom back down to ~0.5 m/px and discard the "
                        "detail the capture exists for. The tracing tool positions it from "
                        "these bounds.",
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"saved      {side}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
