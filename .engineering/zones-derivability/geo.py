"""Shared georeferencing + raster decode for the zone-derivation experiment.
PIL only — no numpy/scipy/shapely in this environment (verified 2026-09-08)."""
import json, math, os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MAPS = os.path.join(REPO, "images/property-map")

def load_bounds(name):
    with open(os.path.join(MAPS, name)) as f:
        return json.load(f)

# The lidar + NAIP frames are byte-identical in bounds (verified, not trusted).
B = load_bounds("lidar-hillshade-2018.bounds.json")
BB = B["bounds"]; W = B["pixelWidth"]; H = B["pixelHeight"]
LAT0 = (BB["north"] + BB["south"]) / 2.0

def assert_same_frame(other):
    o = load_bounds(other)
    assert o["bounds"] == BB and o["pixelWidth"] == W and o["pixelHeight"] == H, \
        "FRAME MISMATCH with %s — refusing to overlay" % other
    return True

def lonlat_to_px(lon, lat):
    """EPSG:4326 linear render — the API rendered the exact bbox, so this is a
    straight linear map, not a projection."""
    x = (lon - BB["west"]) / (BB["east"] - BB["west"]) * W
    y = (BB["north"] - lat) / (BB["north"] - BB["south"]) * H
    return x, y

# metres per pixel, at this latitude
M_PER_DEG_LAT = 111132.92 - 559.82*math.cos(2*math.radians(LAT0)) + 1.175*math.cos(4*math.radians(LAT0))
M_PER_DEG_LON = 111412.84*math.cos(math.radians(LAT0)) - 93.5*math.cos(3*math.radians(LAT0))
MPP_X = (BB["east"]-BB["west"]) * M_PER_DEG_LON / W
MPP_Y = (BB["north"]-BB["south"]) * M_PER_DEG_LAT / H

def zones():
    with open(os.path.join(REPO, "zones.json")) as f:
        return json.load(f)["zones"]

def poly_px(z):
    return [lonlat_to_px(lon, lat) for lon, lat in z["vertices"]]

def shoelace_m2(pts_px):
    a = 0.0
    for i in range(len(pts_px)):
        x1,y1 = pts_px[i]; x2,y2 = pts_px[(i+1) % len(pts_px)]
        a += x1*y2 - x2*y1
    return abs(a)/2.0 * MPP_X * MPP_Y
