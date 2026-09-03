#!/usr/bin/env python3
"""True local sundown at Fernwood, from a 1-arcsec SRTM DEM.

Builds the terrain skyline (max angular elevation per azimuth) around the
observer, then solves when the sun's upper limb actually clears/leaves that
skyline -- and compares it to the flat-horizon sunset the dashboard uses today.
"""
import math, struct, json, sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402 — canon values derive, never re-typed (C5 4a)

TILE = "N34W085.hgt"
N = 3601                      # 1-arcsec tile
TILE_LAT0, TILE_LON0 = 34, -85   # SW corner

R_EARTH = 6371000.0
K_REFRACT = 0.13
R_EFF = R_EARTH / (1.0 - K_REFRACT)
SEMIDIAM = 0.267
REFRACT_H = 0.567

with open(TILE, "rb") as f:
    RAW = f.read()

def elev_at(lat, lon):
    """Bilinear-sampled elevation (m) from the SRTM tile."""
    y = (lat - TILE_LAT0) * (N - 1)
    x = (lon - TILE_LON0) * (N - 1)
    if not (0 <= x < N-1 and 0 <= y < N-1):
        return None
    x0, y0 = int(x), int(y)
    fx, fy = x - x0, y - y0
    def raw(px, py):
        row = (N - 1) - py             # tile rows run north -> south
        off = (row * N + px) * 2
        v = struct.unpack_from(">h", RAW, off)[0]
        return None if v == -32768 else float(v)
    v00, v10 = raw(x0, y0), raw(x0+1, y0)
    v01, v11 = raw(x0, y0+1), raw(x0+1, y0+1)
    if None in (v00, v10, v01, v11):
        return None
    return (v00*(1-fx)*(1-fy) + v10*fx*(1-fy) + v01*(1-fx)*fy + v11*fx*fy)

def dest_point(lat, lon, az_deg, dist_m):
    d = dist_m / R_EARTH
    az = math.radians(az_deg)
    p1, l1 = math.radians(lat), math.radians(lon)
    p2 = math.asin(math.sin(p1)*math.cos(d) + math.cos(p1)*math.sin(d)*math.cos(az))
    l2 = l1 + math.atan2(math.sin(az)*math.sin(d)*math.cos(p1),
                         math.cos(d) - math.sin(p1)*math.sin(p2))
    return math.degrees(p2), math.degrees(l2)

def build_skyline(lat, lon, eye_height_m=1.7, az_step=1.0, max_km=30.0):
    """Max terrain angular elevation (deg) per azimuth, 30 m sampling near in."""
    h0 = elev_at(lat, lon)
    if h0 is None:
        raise SystemExit("observer outside tile")
    h0 += eye_height_m
    # sample step grows with distance: 30 m close in, coarser far out
    dists = []
    d = 30.0
    while d < max_km * 1000:
        dists.append(d)
        d += 30.0 if d < 3000 else (60.0 if d < 10000 else 150.0)
    prof = {}
    for i in range(int(360 / az_step)):
        az = i * az_step
        best_ang, best_d, best_h = -90.0, None, None
        for dd in dists:
            la, lo = dest_point(lat, lon, az, dd)
            h = elev_at(la, lo)
            if h is None:
                continue
            drop = (dd * dd) / (2.0 * R_EFF)
            ang = math.degrees(math.atan2(h - h0 - drop, dd))
            if ang > best_ang:
                best_ang, best_d, best_h = ang, dd, h
        prof[az] = {"angle": best_ang, "dist": best_d, "elev": best_h}
    return prof, h0 - eye_height_m

# ---------- NOAA solar position ----------
def julian_day(y, m, d, hour_utc):
    if m <= 2:
        y -= 1; m += 12
    a = y // 100
    b = 2 - a + a // 4
    return (math.floor(365.25*(y+4716)) + math.floor(30.6001*(m+1))
            + d + b - 1524.5 + hour_utc/24.0)

def sun_pos(lat, lon, y, mo, dy, hour_utc):
    jd = julian_day(y, mo, dy, hour_utc)
    t = (jd - 2451545.0) / 36525.0
    L0 = (280.46646 + t*(36000.76983 + t*0.0003032)) % 360
    M = 357.52911 + t*(35999.05029 - 0.0001537*t)
    Mr = math.radians(M)
    ecc = 0.016708634 - t*(0.000042037 + 0.0000001267*t)
    C = (math.sin(Mr)*(1.914602 - t*(0.004817 + 0.000014*t))
         + math.sin(2*Mr)*(0.019993 - 0.000101*t) + math.sin(3*Mr)*0.000289)
    true_long = L0 + C
    omega = 125.04 - 1934.136*t
    app_long = true_long - 0.00569 - 0.00478*math.sin(math.radians(omega))
    e0 = 23 + (26 + (21.448 - t*(46.815 + t*(0.00059 - t*0.001813)))/60)/60
    e = e0 + 0.00256*math.cos(math.radians(omega))
    lam, er = math.radians(app_long), math.radians(e)
    decl = math.asin(math.sin(er)*math.sin(lam))
    yv = math.tan(er/2)**2
    L0r = math.radians(L0)
    eot = 4*math.degrees(yv*math.sin(2*L0r) - 2*ecc*math.sin(Mr)
                         + 4*ecc*yv*math.sin(Mr)*math.cos(2*L0r)
                         - 0.5*yv*yv*math.sin(4*L0r)
                         - 1.25*ecc*ecc*math.sin(2*Mr))
    tst = (hour_utc*60 + eot + 4*lon) % 1440
    ha = tst/4 - 180
    if ha < -180: ha += 360
    har, latr = math.radians(ha), math.radians(lat)
    cz = math.sin(latr)*math.sin(decl) + math.cos(latr)*math.cos(decl)*math.cos(har)
    zen = math.acos(max(-1.0, min(1.0, cz)))
    alt = 90 - math.degrees(zen)
    den = math.cos(latr)*math.sin(zen)
    if abs(den) < 1e-9:
        az = 180.0
    else:
        ca = max(-1.0, min(1.0, (math.sin(latr)*math.cos(zen) - math.sin(decl))/den))
        a = math.degrees(math.acos(ca))
        # NOAA convention, degrees clockwise from north
        az = (a + 180) % 360 if ha > 0 else (540 - a) % 360
    return alt, az

def sky_at(prof, az, az_step=1.0):
    lo = (math.floor(az/az_step)*az_step) % 360
    hi = (lo + az_step) % 360
    f = ((az - lo) % 360) / az_step
    return prof[lo]["angle"]*(1-f) + prof[hi]["angle"]*f

def sundown(lat, lon, prof, y, mo, dy, tz_h, terrain=True, az_step=1.0):
    """Local-clock minute the upper limb vanishes; scans PM at 0.25-min steps."""
    prev = None
    m = 11*60*4
    while m < 23*60*4:
        minute = m/4.0
        alt, az = sun_pos(lat, lon, y, mo, dy, minute/60.0 - tz_h)
        ridge = sky_at(prof, az, az_step) if terrain else 0.0
        gap = alt - (ridge - SEMIDIAM - REFRACT_H)
        if prev is not None and prev[1] > 0 >= gap:
            return minute, az, ridge
        prev = (minute, gap)
        m += 1
    return None

def sunup(lat, lon, prof, y, mo, dy, tz_h, terrain=True, az_step=1.0):
    """Local-clock minute the upper limb first clears the skyline (AM)."""
    prev = None
    m = 3*60*4
    while m < 13*60*4:
        minute = m/4.0
        alt, az = sun_pos(lat, lon, y, mo, dy, minute/60.0 - tz_h)
        ridge = sky_at(prof, az, az_step) if terrain else 0.0
        gap = alt - (ridge - SEMIDIAM - REFRACT_H)
        if prev is not None and prev[1] <= 0 < gap:
            return minute, az, ridge
        prev = (minute, gap)
        m += 1
    return None

def hhmm(m):
    return f"{int(m)//60:02d}:{int(round(m))%60:02d}"

if __name__ == "__main__":
    SITES = {
        "House (Fernwood)": (momlib.config("location.coordinates.latitude"), momlib.config("location.coordinates.longitude")),
    }
    if len(sys.argv) > 2:
        SITES = {sys.argv[3] if len(sys.argv) > 3 else "site":
                 (float(sys.argv[1]), float(sys.argv[2]))}

    for name, (lat, lon) in SITES.items():
        prof, gnd = build_skyline(lat, lon)
        print(f"\n=== {name} ===")
        print(f"DEM ground elevation: {gnd:.0f} m / {gnd*3.28084:.0f} ft")
        json.dump({str(k): v for k, v in prof.items()},
                  open(f"skyline_{name.split()[0].lower()}.json", "w"))

        dirs = ["N","NNE","NE","ENE","E","ESE","SE","SSE",
                "S","SSW","SW","WSW","W","WNW","NW","NNW"]
        print("\nSkyline, 10-degree summary (ridge angle above true horizontal):")
        print(f"{'Az':>4} {'dir':>4} {'ridge°':>7} {'km':>6} {'ridge_ft':>9}")
        for az in range(0, 360, 10):
            p = prof[float(az)]
            d = dirs[int((az+11.25)//22.5) % 16]
            km = p["dist"]/1000 if p["dist"] else 0
            ft = p["elev"]*3.28084 if p["elev"] else 0
            print(f"{az:4d} {d:>4} {p['angle']:7.2f} {km:6.2f} {ft:9.0f}")

        print("\nDUSK — true local sundown vs. the flat-horizon sunset the app uses:")
        print(f"{'date':>12} {'app_sunset':>11} {'true_down':>10} {'delta_min':>10} "
              f"{'sun_az':>7} {'ridge':>7}")
        DATES = [(1,15,"Jan 15"), (2,15,"Feb 15"), (3,20,"Mar 20"),
                 (4,15,"Apr 15"), (5,15,"May 15"), (6,21,"Jun 21"),
                 (7,23,"Jul 23"), (8,15,"Aug 15"), (9,22,"Sep 22"),
                 (10,15,"Oct 15"), (11,15,"Nov 15"), (12,21,"Dec 21")]
        for (mo, dy, label) in DATES:
            tz = -5.0 if mo in (1,2,12) or (mo == 11 and dy > 5) else -4.0
            flat = sundown(lat, lon, prof, 2026, mo, dy, tz, terrain=False)
            terr = sundown(lat, lon, prof, 2026, mo, dy, tz, terrain=True)
            if not flat or not terr:
                continue
            print(f"{label:>12} {hhmm(flat[0]):>11} {hhmm(terr[0]):>10} "
                  f"{terr[0]-flat[0]:+10.1f} {terr[1]:7.1f} {terr[2]:6.2f}d")

        print("\nDAWN — true local sunup vs. the flat-horizon sunrise the app uses:")
        print(f"{'date':>12} {'app_sunrise':>12} {'true_up':>10} {'delta_min':>10} "
              f"{'sun_az':>7} {'ridge':>7}")
        for (mo, dy, label) in DATES:
            tz = -5.0 if mo in (1,2,12) or (mo == 11 and dy > 5) else -4.0
            flat = sunup(lat, lon, prof, 2026, mo, dy, tz, terrain=False)
            terr = sunup(lat, lon, prof, 2026, mo, dy, tz, terrain=True)
            if not flat or not terr:
                continue
            print(f"{label:>12} {hhmm(flat[0]):>12} {hhmm(terr[0]):>10} "
                  f"{terr[0]-flat[0]:+10.1f} {terr[1]:7.1f} {terr[2]:6.2f}d")
