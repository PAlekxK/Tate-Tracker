#!/usr/bin/env python3
"""anchors.py — are the HIGHEST-CONFIDENCE objects on a property DOWNLOADS rather than derivations?

    python3 anchors.py            # fetch (G0, keyless, stdlib+PIL), measure vs the answer key, render
    python3 anchors.py --offline  # re-measure from the cached JSON beside this file

Measured 2026-09-10 (zones assessment). Two free sources, no key, no install:
  · Microsoft Global ML Building Footprints — one level-9 quadkey tile (~11 MB) filtered to the bbox
  · OpenStreetMap via Overpass — highway=service/driveway ways in the bbox
Against Fernwood's 23 hand-traced zones (the answer key, [paul-stamped 2026-09-08]).

⛔ Answer-key only. n=1 property. Nothing here writes zones.json, and nothing reaches an origin.
"""
import csv, gzip, io, json, math, os, sys, urllib.parse, urllib.request
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
UA = {"User-Agent": "Fernwood/1.0 (+zones research)"}
BOUNDS = json.load(open(os.path.join(ROOT, "images/property-map/base-naip-2022-01-leafoff.bounds.json")))
B = BOUNDS["bounds"]; W = BOUNDS["pixelWidth"]; H = BOUNDS["pixelHeight"]
LAT0, LON0 = BOUNDS["propertyAnchor"]["lat"], BOUNDS["propertyAnchor"]["lon"]
MX = 111320 * math.cos(math.radians(LAT0)); MY = 110540

def m(lon, lat): return ((lon - LON0) * MX, (lat - LAT0) * MY)
def px(lon, lat): return ((lon - B["west"]) / (B["east"] - B["west"]) * W, (B["north"] - lat) / (B["north"] - B["south"]) * H)

def quadkey(lat, lon, z):
    s = math.sin(math.radians(lat)); x = (lon + 180) / 360; y = 0.5 - math.log((1 + s) / (1 - s)) / (4 * math.pi)
    n = 2 ** z; tx = int(x * n); ty = int(y * n); qk = ""
    for i in range(z, 0, -1):
        d = 0; mask = 1 << (i - 1)
        if tx & mask: d += 1
        if ty & mask: d += 2
        qk += str(d)
    return qk

def fetch_ms_footprints():
    """One quadkey tile of the global dataset, filtered to our bbox. ⚠️ Positive control: the tile row
    must exist for this quadkey, and the tile must parse as GeoJSON lines — an empty result is only
    'no buildings' if both held."""
    qk = quadkey(LAT0, LON0, 9)
    idx = urllib.request.urlopen(urllib.request.Request(
        "https://minedbuildings.z5.web.core.windows.net/global-buildings/dataset-links.csv", headers=UA), timeout=60).read().decode()
    rows = [r for r in csv.DictReader(io.StringIO(idx)) if r.get("QuadKey") == qk and r.get("Location") == "UnitedStates"]
    if not rows: raise SystemExit(f"UNVERIFIED: no dataset row for quadkey {qk}")
    data = urllib.request.urlopen(urllib.request.Request(rows[0]["Url"], headers=UA), timeout=180).read()
    raw = gzip.decompress(data).decode() if data[:2] == b"\x1f\x8b" else data.decode()
    hits = []
    for line in raw.splitlines():
        g = json.loads(line)
        if any(B["west"] <= x <= B["east"] and B["south"] <= y <= B["north"] for x, y in g["geometry"]["coordinates"][0]):
            hits.append(g)
    return hits

def fetch_osm():
    q = f'[out:json][timeout:25];(way["highway"]({B["south"]-0.003},{B["west"]-0.003},{B["north"]+0.003},{B["east"]+0.003}););out geom;'
    req = urllib.request.Request("https://overpass-api.de/api/interpreter", data=urllib.parse.urlencode({"data": q}).encode(), headers=UA)
    return json.loads(urllib.request.urlopen(req, timeout=60).read())

def polymask(poly):
    im = Image.new("1", (W, H), 0); ImageDraw.Draw(im).polygon([px(*p) for p in poly], fill=1); return im

def iou(a, b):
    A = list(a.getdata()); Bb = list(b.getdata())
    inter = sum(1 for p, q in zip(A, Bb) if p and q); union = sum(1 for p, q in zip(A, Bb) if p or q)
    return inter / union if union else 0.0

def main():
    offline = "--offline" in sys.argv
    if offline:
        ms = json.load(open(os.path.join(HERE, "anchors-ms-footprints.json")))
        osm = json.load(open(os.path.join(HERE, "anchors-osm-highways.json")))
    else:
        ms = fetch_ms_footprints(); json.dump(ms, open(os.path.join(HERE, "anchors-ms-footprints.json"), "w"))
        osm = fetch_osm(); json.dump(osm, open(os.path.join(HERE, "anchors-osm-highways.json"), "w"))
    Z = json.load(open(os.path.join(ROOT, "zones.json")))["zones"]
    house = [z for z in Z if z["id"] == "house"][0]["vertices"]
    hm = polymask(house)
    print(f"buildings in bbox: {len(ms)}")
    best = (0, None)
    for f in ms:
        poly = f["geometry"]["coordinates"][0]; v = iou(hm, polymask(poly))
        cx = sum(p[0] for p in poly) / len(poly); cy = sum(p[1] for p in poly) / len(poly); ox, oy = m(cx, cy)
        print(f"  footprint {ox:+5.0f} m E {oy:+5.0f} m N of anchor · IoU vs traced house {v:.2f} · height {f['properties'].get('height')}")
        if v > best[0]: best = (v, f)
    service = [e for e in osm["elements"] if e.get("tags", {}).get("highway") == "service"]
    # ⭐ THE SPINE IS THE DRIVEWAY NETWORK CONNECTED TO THE HOUSE, not every service way in the bbox —
    # neighbours' drives down by the road are in the bbox too (measured: 6 ways, 3 are ours).
    # Connectivity = a shared node coordinate. Seed = the way whose nearest node is closest to the house.
    def nodes(e): return {(round(p["lon"], 7), round(p["lat"], 7)) for p in e["geometry"]}
    def near(e): return min(math.hypot(*m(p["lon"], p["lat"])) for p in e["geometry"])
    seed = min(service, key=near)
    drive = [seed]; grown = True
    while grown:
        grown = False
        for e in service:
            if e in drive: continue
            if any(nodes(e) & nodes(d) for d in drive): drive.append(e); grown = True
    print(f"OSM service/driveway ways in bbox: {len(service)} · connected to the house: {len(drive)} (seed way {seed['id']}, {near(seed):.0f} m from the house)")
    segs = []
    for e in drive:
        pts = [m(p["lon"], p["lat"]) for p in e["geometry"]]
        dmin = min(math.hypot(x, y) for x, y in pts)
        print(f"  way {e['id']} {e['tags']} nodes={len(pts)} nearest-to-house={dmin:.0f} m")
        segs += [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    def dseg(p, a, b):
        ax, ay = a; bx, by = b; qx, qy = p; dx, dy = bx - ax, by - ay
        t = max(0, min(1, ((qx - ax) * dx + (qy - ay) * dy) / (dx * dx + dy * dy or 1)))
        return math.hypot(qx - (ax + t * dx), qy - (ay + t * dy))
    worst = 0
    for z in Z:
        d = min(min(dseg(m(*v), a, b) for a, b in segs) for v in z["vertices"]); worst = max(worst, d)
    print(f"every zone's nearest vertex is within {worst:.0f} m of the driveway network")
    # frame arithmetic — house + driveways + margin
    spine = [m(*p) for p in best[1]["geometry"]["coordinates"][0]] + [m(p["lon"], p["lat"]) for e in drive for p in e["geometry"]]
    sx = [p[0] for p in spine]; sy = [p[1] for p in spine]
    for margin in (20, 30, 40):
        fw, fe, fs, fn = min(sx) - margin, max(sx) + margin, min(sy) - margin, max(sy) + margin
        inside = sum(1 for z in Z if all(fw <= m(*v)[0] <= fe and fs <= m(*v)[1] <= fn for v in z["vertices"]))
        print(f"spine bbox +{margin} m contains {inside}/23 zones; frame {fe-fw:.0f} x {fn-fs:.0f} m")
    half = (B["east"] - B["west"]) * MX / 2
    out = sum(1 for x, y in spine if abs(x) > half or abs(y) > half)
    print(f"spine vertices OUTSIDE the hand-pulled {2*half:.0f} m frame: {out}/{len(spine)}")
    # exhibit
    base = Image.open(os.path.join(ROOT, "images/property-map/base-naip-2022-01-leafoff.png")).convert("RGB")
    d = ImageDraw.Draw(base, "RGBA")
    for z in Z: d.polygon([px(*p) for p in z["vertices"]], outline=(255, 255, 255, 220), width=2)
    for e in drive: d.line([px(p["lon"], p["lat"]) for p in e["geometry"]], fill=(255, 220, 0, 255), width=5)
    for f in ms: d.polygon([px(*p) for p in f["geometry"]["coordinates"][0]], outline=(0, 255, 80, 255), fill=(0, 255, 80, 70), width=3)
    fw, fe, fs, fn = min(sx) - 30, max(sx) + 30, min(sy) - 30, max(sy) + 30
    pm = lambda x, y: px(LON0 + x / MX, LAT0 + y / MY)
    d.rectangle([pm(fw, fn), pm(fe, fs)], outline=(255, 60, 60, 255), width=4)
    d.rectangle([2, 2, W - 3, H - 3], outline=(120, 120, 255, 255), width=3)
    try: fnt = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30)
    except Exception: fnt = None
    y = 20
    for t in ["Fernwood — free downloads vs the hand-traced answer key (2022-01 NAIP leaf-off)",
              "green = Microsoft building footprints (G0, stdlib)   yellow = OSM driveways (G0)",
              "white = the 23 traced zones   red = house+driveway bbox +30 m   blue = the 459 m frame pulled by hand"]:
        d.rectangle([10, y - 6, 10 + d.textlength(t, font=fnt) + 12, y + 36], fill=(0, 0, 0, 160)); d.text((16, y), t, fill=(255, 255, 255, 255), font=fnt); y += 44
    base.save(os.path.join(HERE, "frame-anchors.png"), optimize=True)
    print("wrote frame-anchors.png")

if __name__ == "__main__":
    main()
