# Google Earth as a Fernwood data source — what it can do, and how to drive it

*Started 2026-09-01. Paul: "I think it's worth kind of documenting this process a little bit
as we go, and exploring all the capabilities that Google Earth offers like this."*

Two products, and they are not interchangeable:

| | **Earth Pro** (desktop) | **Earth Web** (`earth.google.com/web`) |
|---|---|---|
| KML import/export | ✅ full | ⚠️ import only, limited |
| Historical imagery | ✅ slider | ✅ slider, **and URL-addressable** |
| Drivable by Claude | ❌ native app, no automation hook | ✅ **via the Chrome extension** |
| Save image | ✅ high-res export | screenshot only |

**That last row is the finding.** Earth Pro cannot be automated from here — it is a native app,
and neither the Chrome extension nor Playwright can reach it. Earth Web can, through the
Claude-in-Chrome extension against Paul's own signed-in session. So Pro is where *he* works and
Web is where *we* can look together.

---

## ⭐ The unlock: the imagery date is addressable by URL

Earth Web encodes its state in a base64 protobuf `data=` parameter — and inside it, **the
imagery date is a plain ASCII `YYYY-MM-DD` string**, length-prefixed. So any capture can be
jumped to directly instead of clicking through a slider.

```python
import base64
def ge_url(date, lat=34.5496, lon=-84.3674, dist=600):
    """date: 'YYYY-MM-DD' (always 10 chars — the length prefix depends on it)"""
    payload = (b'\n\x16*\x10\x08\x01\x12\n' + date.encode() +
               b'\x18\x01B\x02\x08\x01:\x03\n\x010B\x02\x08\x00'
               b'J\r\x08\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x00')
    enc = base64.b64encode(payload).decode().replace('+','-').replace('/','_').rstrip('=')
    return f"https://earth.google.com/web/@{lat},{lon},875a,{dist}d,35y,0h,0t,0r/data={enc}"
```

URL camera params are `@lat,lon,altitude(a),distance(d),fov(y),heading(h),tilt(t),roll(r)`.
**Keep `0t` — tilt zero is nadir.** A tilted view projects clicks onto draped terrain, which is
the error that would silently corrupt any coordinate taken from it.

⚠️ `dist` values much above a few thousand metres reset the view to the whole globe and **drop
the date** — measured, `12000d` did exactly that. Stay in the hundreds-of-metres range.

---

## The historical archive over Fernwood

**Ticks on the timeline: 1985 · 1993 · 1999 · 2005 · 2006 · 2007 · 2008 · 2009 · 2010 · 2012 ·
2015 · 2017 · 2018 · 2019 · 2021 · 2025**, plus unlabelled dots between. That is roughly 16+
captures against NAIP's 7, and it reaches **25 years further back**.

Exact dates read off the header so far: `2025-11-05` · `2025-10-20` · `2021-11-27` ·
`2019-11-01` · `2018-04-12` · `2015-03-07`.

### ⭐ The March–April 2018 frame is the best view of this property that exists
Paul found it by dragging the slider; the arithmetic agrees it is the ceiling. At 34.55°N the
leaf-off window caps the noon sun near 55° at the equinox, so mid-March to mid-April is the only
time bare trees and a high sun coexist.

| frame | noon sun | shadow | leaf |
|---|---|---|---|
| NAIP 2022-01-10 *(what the zones were traced on)* | 33.4° | 1.52× | off |
| Esri WorldView-3 2022-02-12 | 41.2° | 1.14× | off |
| **GE, mid-March 2018** | **52.6°** | **0.76×** | **off** |
| **GE, 2018-04-12** *(a confirmed capture)* | **63.7°** | **0.49×** | off/early |

**Half to a third of the shadow**, and you can see the ground through the bare canopy. The
house, the driveway loop, the field, the second structure and the paths are all crisply readable.
Saved (display-only, gitignored) at `images/property-map/.local/gearth/ge-web-2018-leafoff.png`.

---

## ⚠️ Two ways this interface reads clean and is wrong

Both are the same failure class this repo keeps paying for — a plausible value from a
successful-looking operation.

**1. The attribution date LAGS the header.** The bottom-left "Data attribution" date shows the
*previously loaded* tile while the new one is still fetching. Measured: at header `Mar 15, 2018`
it read `older–4/9/2017`; after stepping to header `Mar 7, 2015` it read `older–4/12/2018` — the
frame before. **Read the header, and only once loading shows 100%.** Recording the attribution
line mid-load would put a false capture date into the record.

**2. `1985` renders 100% loaded and completely blank at property zoom.** Not an error, not a
spinner — a flat dark-green frame that looks like a successful load of empty ground. The tick
exists because 1985 has coverage *somewhere*, not here. Same shape as Esri's z20 "Map data not
yet available" grey square: **a status of "done" is not evidence that anything arrived.**

Corollary for Paul's "before the house" question: **Earth Web does not answer it.** The oldest
usable capture is well after the house existed. The 1971 USGS 1:24,000 topo sheet does answer it
— no building at the anchor — and USGS EarthExplorer single-frame aerials (1930s–1990s) remain
the only path to an actual *photograph* of that. See `LAND-SOURCES.md`.

---

## Capabilities seen but not yet used

- **Compare two years** — a built-in side-by-side change view (icon right of the timeline).
  Directly relevant to the regrading question: the lidar is 2018 and the western garden/patio
  were reshaped after it.
- **Gemini panel** — offers things like *"Find parcels above 2 acres."* Untested. ⚠️ Anything it
  returns is a model read, not a source: it would be a hypothesis under the standing verification
  rule, never a value for the record.
- **Measure tool**, **projects/KML import**, Street View pegman.
- Historical Imagery mode **disables 3D buildings** by design.

## Licensing — unchanged, and it governs everything above

Google imagery is **display-only and not redistributable**, same class as Esri. Captures land in
gitignored `.local/`, are never committed, never served from Pages, and never become
`zones.json._meta.baseImage`. The shipped basemap stays public-domain NAIP.

**Still open:** using the 2018 frame for actual tracing needs control-point registration against
the NAIP frame. That is buildable — the 2015 GEP failure was because that image was *oblique*,
not because Google frames cannot be registered. A nadir capture with known centre and camera
distance, fitted on features visible in both, would register fine.
