"""Ridge extraction — the derived EDGE candidates, as fragments.
Non-max suppression + threshold + connected components. Pure PIL."""
from collections import deque
import geo, field

def ridge_pixels(bp, bbox, pct_keep=0.06):
    x0,y0,x1,y1 = bbox
    vals=[]
    for y in range(y0,y1,2):
        for x in range(x0,x1,2): vals.append(bp[x,y])
    vals.sort()
    thr = vals[int(len(vals)*(1.0-pct_keep))]
    out=set()
    for y in range(y0+1,y1-1):
        for x in range(x0+1,x1-1):
            v=bp[x,y]
            if v < thr: continue
            # local maximum along at least one axis = a ridge crest, not a slab
            if ((v>=bp[x-1,y] and v>=bp[x+1,y]) or (v>=bp[x,y-1] and v>=bp[x,y+1]) or
                (v>=bp[x-1,y-1] and v>=bp[x+1,y+1]) or (v>=bp[x-1,y+1] and v>=bp[x+1,y-1])):
                out.add((x,y))
    return out, thr

def components(pxset, min_px=40):
    """8-connected components, filtered by length. A 12 px fragment is noise."""
    seen=set(); comps=[]
    for p in pxset:
        if p in seen: continue
        q=deque([p]); seen.add(p); comp=[]
        while q:
            x,y=q.popleft(); comp.append((x,y))
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    n=(x+dx,y+dy)
                    if n in pxset and n not in seen:
                        seen.add(n); q.append(n)
        if len(comp)>=min_px: comps.append(comp)
    return sorted(comps, key=len, reverse=True)

def extent_m(comp):
    xs=[p[0] for p in comp]; ys=[p[1] for p in comp]
    return (((max(xs)-min(xs))*geo.MPP_X)**2 + ((max(ys)-min(ys))*geo.MPP_Y)**2) ** 0.5
