#!/usr/bin/env python3
"""Render USGS historical topographic sheets, cropped to the property.

WHY (2026-09-01, Paul): "It would just be cool to see any image of the area that's
available... I don't think people will or can expect to zoom in on an old photo like
that. But there is value just in seeing that cool old view."

Right, and that framing is what makes the old sheets worth having. The 1888 and 1911
Ellijay sheets are 1:125,000 - the property is a dot and there is no house on them.
They are not evidence about the property; they are a picture of this mountain before
anyone built here. The 1971 Amicalola sheet is 1:24,000, which is the first scale that
draws individual buildings.

THE GEOREFERENCING, AND WHY IT NEEDED WORK
  These are TerraGo GeoPDFs. They carry no ISO-32000 /Measure dictionary, so nothing
  standard reads them - the georeferencing is in a private /LGIDict holding a /CTM, a
  /Neatline, and a /Registration list of (pdfX, pdfY, projX, projY) control points.
  Those coordinates are POLYCONIC METRES on Clarke 1866, not lat/lon, so locating the
  property means running the forward Polyconic projection and fitting to the control
  points. That is what this does, and it is why gdal is not required.

⚠️ DATUM. These sheets are NAD27. The property anchor is WGS84. The NAD27->WGS84 shift
   in north Georgia is roughly 20-40 m and is NOT applied here - correcting it properly
   needs NADCON grids. At 1:24,000 that is about a millimetre on the sheet; at 1:125,000
   it is invisible. It is stated because an uncorrected datum that nobody mentions is how
   a "cool old view" quietly becomes a positional claim. These crops are for LOOKING.
   Nothing traced on them may enter zones.json.

LICENSE: public domain (US federal work). The rendered crops are redistributable. The
source PDFs are large and regenerable, so they stay in .local/ and are gitignored.
"""
from __future__ import annotations

import argparse, json, math, re, subprocess, sys, urllib.parse, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOCAL = REPO / "images/property-map/.local/topo"
OUT = REPO / "images/property-map/historical"
LAT, LON = 34.5496, -84.3674

A = 6378206.4          # Clarke 1866 semi-major (NAD27)
ES = 0.00676865799729  # Clarke 1866 eccentricity squared


def meridional_arc(phi: float) -> float:
    e2 = ES
    return A * ((1 - e2/4 - 3*e2**2/64 - 5*e2**3/256) * phi
                - (3*e2/8 + 3*e2**2/32 + 45*e2**3/1024) * math.sin(2*phi)
                + (15*e2**2/256 + 45*e2**3/1024) * math.sin(4*phi)
                - (35*e2**3/3072) * math.sin(6*phi))


def polyconic_forward(lat_deg: float, lon_deg: float, lon0_deg: float, lat0_deg: float = 0.0):
    """American Polyconic. Snyder, Map Projections - A Working Manual, pp. 129-130."""
    phi, lam = math.radians(lat_deg), math.radians(lon_deg)
    lam0 = math.radians(lon0_deg)
    M0 = meridional_arc(math.radians(lat0_deg))
    if abs(phi) < 1e-12:
        return A * (lam - lam0), -M0
    N = A / math.sqrt(1 - ES * math.sin(phi) ** 2)
    E = (lam - lam0) * math.sin(phi)
    cot = 1.0 / math.tan(phi)
    return N * cot * math.sin(E), meridional_arc(phi) - M0 + N * cot * (1 - math.cos(E))


def read_lgidict(pdf: Path):
    """Pull the /CTM, /Registration and central meridian out of the TerraGo GeoPDF.

    The CTM is the authority: a 6-element PDF-user-space -> projected-metres affine,
    present on every sheet. /Registration control points are NOT reliable to fit against
    — the 1888 Ellijay sheet carries exactly two, both at pdfX=0, which is a degenerate
    vertical line and cannot determine a 2-D transform. So the CTM does the work and the
    control points, where there are enough of them, only VERIFY it.
    """
    qdf = pdf.with_suffix(".qdf.pdf")
    if not qdf.exists():
        subprocess.run(["qpdf", "--qdf", "--object-streams=disable", str(pdf), str(qdf)],
                       check=True, capture_output=True)
    raw = qdf.read_bytes().decode("latin-1")

    cm = re.search(r"/CentralMeridian\s*\((-?[\d.]+)\)", raw)
    if not cm:
        raise SystemExit(f"{pdf.name}: no /CentralMeridian — not a TerraGo GeoPDF?")
    lon0 = float(cm.group(1))

    i = raw.find("/CTM")
    if i < 0:
        raise SystemExit(f"{pdf.name}: no /CTM")
    ctm = [float(g) for g in re.findall(r"\((-?[\d.eE+-]+)\)", raw[i:i + 400])[:6]]
    if len(ctm) != 6:
        raise SystemExit(f"{pdf.name}: could not read a 6-element /CTM")

    pts = []
    j = raw.find("/Registration")
    if j >= 0:
        for m in re.finditer(r"\[\s*\((-?[\d.eE+-]+)\)\s*\((-?[\d.eE+-]+)\)\s*"
                             r"\((-?[\d.eE+-]+)\)\s*\((-?[\d.eE+-]+)\)\s*\]",
                             raw[j:j + 12000]):
            pts.append(tuple(float(g) for g in m.groups()))
    return lon0, ctm, pts


def ctm_inverse(ctm, X, Y):
    """projected metres -> PDF user space. CTM is [a b c d e f]:
         X = a*x + c*y + e ;  Y = b*x + d*y + f"""
    a, b, c, d, e, f = ctm
    det = a * d - b * c
    if abs(det) < 1e-30:
        raise SystemExit("degenerate /CTM")
    dx, dy = X - e, Y - f
    return (d * dx - c * dy) / det, (-b * dx + a * dy) / det


def verify_ctm(ctm, pts):
    """Assert the CTM against the sheet's own control points. A transform that reads
    plausibly and places things wrongly is the failure this repo keeps paying for, so
    where the sheet supplies checkpoints they are actually checked."""
    if len(pts) < 2:
        return None
    worst = 0.0
    for px, py, X, Y in pts:
        a, b, c, d, e, f = ctm
        worst = max(worst, math.hypot(a*px + c*py + e - X, b*px + d*py + f - Y))
    return worst


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--span-ft", type=float, default=6000, help="ground width of the crop")
    args = ap.parse_args()

    try:
        from PIL import Image
    except ImportError:
        raise SystemExit("needs Pillow")
    Image.MAX_IMAGE_PIXELS = None
    OUT.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(f for f in LOCAL.glob("topo-*.pdf") if not f.name.endswith(".qdf.pdf"))
    if not pdfs:
        raise SystemExit(f"no sheets in {LOCAL} — run the downloader first")

    manifest = []
    for pdf in pdfs:
        year = pdf.stem.split("-")[1]
        lon0, ctm, pts = read_lgidict(pdf)
        resid = verify_ctm(ctm, pts)
        if resid is not None and resid > 5.0:
            raise SystemExit(f"{pdf.name}: /CTM disagrees with its own control points by "
                             f"{resid:.1f} m — refusing to crop against a transform that "
                             f"fails the sheet's own check.")
        px_, py_ = polyconic_forward(LAT, LON, lon0)
        ptx, pty = ctm_inverse(ctm, px_, py_)

        # PDF units are points (1/72"). Scale from the control points' own geometry:
        # metres of ground per PDF point, measured, not assumed.
        mpp = math.hypot(ctm[0], ctm[1])   # metres of ground per PDF point, from the CTM
        span_m = args.span_ft * 0.3048
        half_pt = (span_m / mpp) / 2

        scale = args.dpi / 72.0
        png = LOCAL / f"{pdf.stem}-{args.dpi}.png"
        if not png.exists():
            print(f"  rendering {pdf.name} at {args.dpi} dpi ...")
            subprocess.run(["pdftoppm", "-r", str(args.dpi), "-png", "-singlefile",
                            str(pdf), str(png.with_suffix(""))], check=True, capture_output=True)
        im = Image.open(png).convert("RGB")

        # pdftoppm origin is top-left; PDF user space is bottom-left.
        cx = ptx * scale
        cy = im.height - pty * scale
        h = half_pt * scale
        box = (int(cx-h), int(cy-h), int(cx+h), int(cy+h))
        inside = 0 <= cx < im.width and 0 <= cy < im.height
        crop = im.crop(box)

        outp = OUT / f"topo-{year}-property.png"
        crop.resize((900, 900), Image.LANCZOS).save(outp)
        rtxt = f"CTM check {resid:.2f} m ({len(pts)} pts)" if resid is not None else "no checkpoints"
        print(f"  {year}: lon0={lon0}  {rtxt}  "
              f"{mpp:.1f} m/pt  property at pdf({ptx:.0f},{pty:.0f}) "
              f"{'IN SHEET' if inside else '⚠️ OUTSIDE SHEET'}  -> {outp.name}")
        manifest.append({"year": int(year), "sheet": pdf.name, "centralMeridian": lon0,
                         "controlPoints": len(pts),
                         "ctmCheckMetres": (round(resid, 3) if resid is not None else None),
                         "metresPerPdfPoint": round(mpp, 2), "propertyInSheet": inside,
                         "cropSpanFt": args.span_ft, "output": outp.name})

    (OUT / "manifest.json").write_text(json.dumps({
        "purpose": "USGS historical topographic sheets cropped to the property. FOR LOOKING.",
        "license": "public domain (US federal work) — these crops are redistributable",
        "datumCaveat": "Sheets are NAD27; the anchor is WGS84. The 20-40 m north-Georgia "
                       "shift is NOT applied (needs NADCON grids). Nothing traced on these "
                       "may enter zones.json.",
        "georeferencing": "TerraGo /LGIDict /CTM (PDF user space → Polyconic metres, "
                          "Clarke 1866), inverted; the property is placed by the forward "
                          "Polyconic projection. Verified against /Registration control "
                          "points where the sheet supplies enough. No gdal required.",
        "sheets": manifest,
    }, indent=2) + "\n")
    print(f"\n  manifest -> {(OUT/'manifest.json').relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
