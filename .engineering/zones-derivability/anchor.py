"""ANCHOR step — the operator points, the machine proposes the extent.

This is 'we draw, they confirm' with the labour split correctly: a human supplies
the SEED (a click inside a place they can see), the machine supplies the BOUNDARY.
Pure PIL — no numpy/scipy/skimage in this environment.
"""
from collections import deque
from PIL import Image
import geo, raster

# The slope PNG is a 0-30 deg colour ramp. Luminance 245 ~ 0 deg, 93 = clipped at 30.
RAMP_HI, RAMP_LO, RAMP_MAXDEG = 245.0, 93.0, 30.0

def degrees_field():
    """Slope in DEGREES, clipped at 30. Direction verified empirically (see README)."""
    im = Image.open(geo.MAPS + "/lidar-slope-2018.png").convert("L")
    px = im.load()
    return px

def deg(px, x, y):
    l = px[x, y]
    return max(0.0, min(RAMP_MAXDEG, RAMP_MAXDEG * (RAMP_HI - l) / (RAMP_HI - RAMP_LO)))

def grow(px, seed, tol_deg=6.0, max_px=400000, bbox=None):
    """Flood-grow from a seed while slope stays within tol of the seed's own slope.
    A place like a house pad or a parking cut is FLAT and rimmed; the grow stops at
    the rim by itself. Returns the pixel set, or None if it ran away."""
    sx, sy = int(seed[0]), int(seed[1])
    base = deg(px, sx, sy)
    seen = set()
    q = deque([(sx, sy)])
    seen.add((sx, sy))
    x0, y0, x1, y1 = bbox or (0, 0, geo.W, geo.H)
    while q:
        x, y = q.popleft()
        if len(seen) > max_px:
            return None                      # ⛔ ran away — REFUSE, never return a guess
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx, ny = x+dx, y+dy
            if (nx, ny) in seen: continue
            if not (x0 <= nx < x1 and y0 <= ny < y1): continue
            if abs(deg(px, nx, ny) - base) <= tol_deg:
                seen.add((nx, ny))
                q.append((nx, ny))
    return seen

def rasterize(poly):
    return set(raster.interior_px(poly))

def iou(a, b):
    if not a or not b: return 0.0
    return len(a & b) / float(len(a | b))

def outline(pxset):
    """Boundary pixels: in the set, with a 4-neighbour outside it."""
    return {(x,y) for (x,y) in pxset
            if not all((x+dx, y+dy) in pxset for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)))}

def barrier_grow(bp, seed, barrier, max_px=400000, bbox=None):
    """Grow from a seed but REFUSE to cross a break. A rim is a BARRIER, not a value
    to track — this is the watershed formulation, and it is the one that matches the
    physics of a pad, a cut or a terrace."""
    sx, sy = int(seed[0]), int(seed[1])
    if bp[sx, sy] >= barrier: return None      # seeded on a ridge — nonsense
    seen = {(sx, sy)}
    q = deque([(sx, sy)])
    x0, y0, x1, y1 = bbox or (0, 0, geo.W, geo.H)
    while q:
        x, y = q.popleft()
        if len(seen) > max_px: return None      # ⛔ leaked — REFUSE
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx, ny = x+dx, y+dy
            if (nx, ny) in seen: continue
            if not (x0 <= nx < x1 and y0 <= ny < y1): continue
            if bp[nx, ny] < barrier:
                seen.add((nx, ny)); q.append((nx, ny))
    return seen
