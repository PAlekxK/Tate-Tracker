"""Raster decode + polygon sampling, PIL only."""
import os
from PIL import Image
import geo

def load_rgb(name):
    return Image.open(os.path.join(geo.MAPS, name)).convert("RGB")

def ramp_scalar(rgb):
    """The slope PNG is a COLOUR ramp (491 colours), not grayscale. All three
    channels move together along it, so luminance is a monotonic proxy for
    position on the ramp. Direction (which end is steep) is established
    empirically, never assumed."""
    r,g,b = rgb
    return 0.299*r + 0.587*g + 0.114*b

def point_in_poly(x, y, poly):
    """Ray casting. No shapely in this environment."""
    inside = False
    n = len(poly)
    for i in range(n):
        x1,y1 = poly[i]; x2,y2 = poly[(i+1) % n]
        if (y1 > y) != (y2 > y):
            xint = (x2-x1)*(y-y1)/(y2-y1) + x1
            if x < xint: inside = not inside
    return inside

def interior_px(poly, step=1):
    xs=[p[0] for p in poly]; ys=[p[1] for p in poly]
    x0,x1 = int(min(xs)), int(max(xs))+1
    y0,y1 = int(min(ys)), int(max(ys))+1
    out=[]
    for y in range(max(0,y0), min(geo.H,y1), step):
        for x in range(max(0,x0), min(geo.W,x1), step):
            if point_in_poly(x+0.5, y+0.5, poly): out.append((x,y))
    return out

def boundary_px(poly, spacing=1.0):
    """Walk the polygon edges, sampling every `spacing` pixels."""
    out=[]
    n=len(poly)
    for i in range(n):
        x1,y1 = poly[i]; x2,y2 = poly[(i+1)%n]
        d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
        steps = max(1, int(d/spacing))
        for s in range(steps):
            t = s/steps
            out.append((x1+(x2-x1)*t, y1+(y2-y1)*t))
    return out
