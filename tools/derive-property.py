#!/usr/bin/env python3
"""derive-property.py — turn an onboarding ADDRESS into a household's starting property record.

    python3 tools/derive-property.py --address "1 Example Road, Dahlonega, GA 30533" --estate bob
    python3 tools/derive-property.py --address "…" --json          # print, write nothing
    python3 tools/derive-property.py --selftest

⭐ WHY THIS EXISTS — **A0**, and building the Journal proved it is step 0 and not step 7
`[paul-ruled 2026-09-10]`: the Journal *"should work from virtual first light even if it has a very
limited database compared to the legacy Fernwood."*

`build-digest.py` refuses a record with no place in it —

    property.json holds neither an address nor an elevation
    — refusing to derive a core with no place in it

— and it is right to. **A Journal with no place is not a small Journal, it is a Journal about
nothing.** So a household's FIRST canon is derived from the one thing onboarding already asks for.
`instance/neutral-canon/property.json` has declared this contract from the day it was written:
*"the SHAPE a household property record has, with no household in it. Every value is filled from
what the person tells us at onboarding, never typed here."* Nothing had ever filled it.

⛔⛔ **IT REFUSES TO WRITE ANYWHERE GIT TRACKS, AND THAT IS THE POINT.** A filled property record
carries a person's HOME ADDRESS, and this repo is **public** (`PAlekxK/Tate-Tracker`) with
`instance/` tracked. Fernwood's address is public because Paul published it; **nobody else's is ours
to publish.** A household's canon lives in `.private/` and, from A1, in that estate's KV — never on
tracked disk. This tool checks `git ls-files` before it writes and refuses rather than trusting a
path convention.

⭐ EVERY DERIVED VALUE IS `inferred`, WITH ITS SOURCE. None of this is ground truth: it is what a
public dataset says about a coordinate. That is exactly the honest-uncertainty state the confirm-card
loop exists to convert into `verified` — a new household's Journal saying *"I think you're at about
1,420 ft — is that right?"* is the product working, not a limitation.

⛔ THREE OUTCOMES PER FIELD, NEVER TWO (`geocodeAddress`'s own rule): a value · a REFUSAL (a PO box
has no coordinate, ever) · a MISS with its reason. A miss is reported and left ABSENT. **It is never
defaulted, and there is never a default coordinate.**

EXIT: 0 a place was derived · 2 nothing usable (no address AND no elevation — `build-digest` would
refuse it anyway) · 3 UNREADABLE (the network, not the address).
"""
import argparse, json, os, subprocess, sys, urllib.parse, urllib.request
import datetime as dt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Fernwood/1.0 (+household property derivation)"}
PO_BOX_HINTS = ("po box", "p.o. box", "p o box", "post office box")


def _get(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


# ---- the derivers. Each returns (value|None, note). None is a MISS and says why. ----------------
def derive_geocode(oneline, get=_get):
    """Census — the SAME service `worker.js:GEOCODERS.census` uses.

    ⚠️ Duplicated deliberately, not shared: that one is JS inside a Worker, this is Python in a
    tool. One SERVICE, two readers — the repo's one-source-N-readers rule holds on the service, and
    a shared HTTP client across those two runtimes would be the more expensive coupling.
    """
    if any(h in oneline.lower() for h in PO_BOX_HINTS):
        return None, "refused: a PO box names no place on the ground"
    url = ("https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress?address="
           + urllib.parse.quote(oneline) + "&benchmark=Public_AR_Current&vintage=Current_Current&format=json")
    d = get(url)
    m = ((d.get("result") or {}).get("addressMatches") or [])
    if not m:
        return None, "miss: the census geocoder matched no address"
    m = m[0]
    c = m.get("coordinates") or {}
    try:
        lat, lon = float(c["y"]), float(c["x"])
    except (KeyError, TypeError, ValueError):
        return None, "miss: a match with no usable coordinate"
    cty = ((m.get("geographies") or {}).get("Counties") or [{}])[0]
    return {"latitude": lat, "longitude": lon,
            "matchedAddress": m.get("matchedAddress"),
            "county": cty.get("NAME"),
            "countyFips": ((cty.get("STATE") or "") + (cty.get("COUNTY") or "")) or None}, "census"


def derive_elevation(lat, lon, get=_get):
    """USGS 3DEP via EPQS — the SAME source Fernwood's own 2,873 ft was measured from.

    ⛔ NOT Open-Meteo. CLAUDE.md records why in as many words: its ~90 m global model *"reads 86 ft
    high on this spur"*, and a number from it had been stamped `confirmed` for months. Using the
    weaker source here would seed every new household with the error this project already paid to
    find once.
    """
    url = ("https://epqs.nationalmap.gov/v1/json?x=%s&y=%s&units=Feet&wkid=4326&includeDate=false"
           % (lon, lat))
    try:
        d = get(url)
    except Exception as e:
        return None, "miss: EPQS unreachable (%s)" % str(e)[:60]
    v = d.get("value")
    try:
        ft = round(float(v))
    except (TypeError, ValueError):
        return None, "miss: EPQS returned no value"
    # EPQS answers -1000000 for a point it has no data for. A sentinel is a MISS, never an elevation.
    if ft < -1000:
        return None, "miss: EPQS has no coverage at this point"
    return ft, "usgs-3dep-epqs"


def derive_zone(zipcode, get=_get):
    """USDA plant-hardiness zone from the ZIP. Coarse by construction — a ZIP is not a spur."""
    if not zipcode:
        return None, "miss: no zip to ask with"
    try:
        d = get("https://phzmapi.org/%s.json" % str(zipcode)[:5])
    except Exception as e:
        return None, "miss: hardiness service unreachable (%s)" % str(e)[:60]
    z = d.get("zone")
    return (z, "phzmapi") if z else (None, "miss: no zone returned")


# ---- assembly -----------------------------------------------------------------------------------
def neutral_shape():
    with open(os.path.join(ROOT, "instance", "neutral-canon", "property.json"), encoding="utf-8") as fh:
        return json.load(fh)


def derive(address, parts=None, get=_get):
    """The whole record plus a per-field provenance report. Pure apart from `get`."""
    parts = parts or {}
    prop = neutral_shape()
    prop["_meta"] = {"derivedAt": dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
                                   .isoformat().replace("+00:00", "Z"),
                     "derivedFrom": "onboarding address",
                     "rule": "every value here is INFERRED from a public dataset — not one of it is "
                             "ground truth, and the confirm loop is what turns it into verified"}
    report = []

    geo, note = derive_geocode(address, get)
    report.append(("coordinates", bool(geo), note))
    if geo:
        prop["property"]["address"] = geo.get("matchedAddress") or address
        if geo.get("county"):
            prop["property"]["county"] = geo["county"]
        prop["location"] = {"coordinates": {"latitude": geo["latitude"], "longitude": geo["longitude"],
                                            "confidence": "inferred", "source": "census"}}
        if geo.get("countyFips"):
            prop["location"]["countyFips"] = geo["countyFips"]
    for k in ("city", "state", "zip"):
        if parts.get(k):
            prop["property"][k] = parts[k]

    if geo:
        ft, note = derive_elevation(geo["latitude"], geo["longitude"], get)
        report.append(("elevation", ft is not None, note))
        if ft is not None:
            prop["location"].setdefault("elevation", {})
            prop["location"]["elevation"] = {"estimated_ft": ft, "confidence": "inferred",
                                             "source": "USGS 3DEP (EPQS)"}
    else:
        report.append(("elevation", False, "skipped: no coordinate to ask at"))

    z, note = derive_zone(parts.get("zip"), get)
    report.append(("hardiness", z is not None, note))
    if z:
        prop["hardiness"] = {"officialZone": z, "confidence": "inferred", "source": "phzmapi (by ZIP)"}

    # ⛔ FROST DATES ARE DELIBERATELY NOT DERIVED, and their absence is the honest answer.
    # Fernwood's own frost dates are a LAPSE-RATE ADJUSTMENT of a named baseline station
    # (+10 days spring / -10 days fall against KJZP), which needs a per-location baseline this tool
    # has no source for. Inventing them from a hardiness zone would put three confident-looking
    # dates into a household's record on the strength of a ZIP code. An absent frost date renders
    # as nothing; a wrong one tells someone when to plant.
    report.append(("frostDates", False, "not derived — needs a baseline station; absent beats invented"))
    return prop, report


def refuse_if_tracked(path):
    """⛔ The guard that matters. A filled property carries a home address and this repo is PUBLIC."""
    rel = os.path.relpath(os.path.abspath(path), ROOT)
    if rel.startswith(".."):
        return
    r = subprocess.run(["git", "ls-files", "--error-unmatch", rel], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode == 0:
        raise SystemExit("derive-property: ⛔ REFUSING to write %s — git tracks it and this repo is "
                         "PUBLIC. A household's address does not go in a public repo. Write to "
                         ".private/ (or publish to that estate's KV)." % rel)
    if rel.split(os.sep)[0] == "instance":
        raise SystemExit("derive-property: ⛔ REFUSING to write under instance/ — it is tracked, and a "
                         "filled property record is not neutral instance config.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--address", help="one-line address as the person gave it")
    ap.add_argument("--estate", help="name it belongs to (decides the default private out-path)")
    ap.add_argument("--city"); ap.add_argument("--state"); ap.add_argument("--zip")
    ap.add_argument("--out", help="where to write; defaults under .private/derived/")
    ap.add_argument("--json", action="store_true", help="print the record, write nothing")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.address:
        print("derive-property: --address is required"); return 2

    try:
        prop, report = derive(a.address, {"city": a.city, "state": a.state, "zip": a.zip})
    except Exception as e:
        print("⛔ UNREADABLE — %s" % str(e)[:200]); return 3

    print("📍 derived a starting place\n")
    for field, ok, note in report:
        print("   %s %-12s %s" % ("✅" if ok else "⬜", field, note))
    have_addr = bool(prop["property"].get("address"))
    have_elev = (prop.get("location") or {}).get("elevation", {}).get("estimated_ft") is not None
    print()
    if not have_addr and not have_elev:
        print("🔴 neither an address nor an elevation — `build-digest` would refuse this record, and so do I.")
        return 2

    if a.json:
        print(json.dumps(prop, indent=1)); return 0
    out = a.out or os.path.join(ROOT, ".private", "derived",
                                "%s-property.json" % (a.estate or "unnamed"))
    refuse_if_tracked(out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fd = os.open(out, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as fh:
        json.dump(prop, fh, indent=1)
    print("✅ written to %s (mode 600, untracked)" % os.path.relpath(out, ROOT))
    print("⚠️  every value is INFERRED. The confirm loop is what makes any of it verified.")
    return 0


def selftest():
    """Offline. Proves each outcome, including the ones that must REFUSE."""
    ok, bad = 0, []

    def fake(payloads):
        def get(url, timeout=25):
            for frag, val in payloads.items():
                if frag in url:
                    if isinstance(val, Exception): raise val
                    return val
            raise RuntimeError("no fixture for " + url[:40])
        return get

    census_hit = {"result": {"addressMatches": [{"coordinates": {"x": -84.0, "y": 34.5},
                   "matchedAddress": "1 EXAMPLE RD, DAHLONEGA, GA, 30533",
                   "geographies": {"Counties": [{"NAME": "Lumpkin", "STATE": "13", "COUNTY": "187"}]}}]}}
    g = fake({"geocoder": census_hit, "epqs": {"value": "1420.5"}, "phzmapi": {"zone": "7b"}})
    p, r = derive("1 Example Road", {"zip": "30533"}, g)
    ok += 1 if p["location"]["elevation"]["estimated_ft"] == 1420 else bad.append("elevation not rounded/derived")
    ok += 1 if p["location"]["elevation"]["confidence"] == "inferred" else bad.append("elevation not marked inferred")
    ok += 1 if p["property"]["county"] == "Lumpkin" else bad.append("county not carried")
    ok += 1 if p["hardiness"]["officialZone"] == "7b" else bad.append("zone not carried")
    ok += 1 if dict((f, o) for f, o, _ in r)["frostDates"] is False else bad.append("frost dates were invented")

    # a PO box is REFUSED, not missed
    p2, r2 = derive("PO Box 12, Jasper GA", {}, g)
    note = [n for f, o, n in r2 if f == "coordinates"][0]
    ok += 1 if note.startswith("refused") else bad.append("a PO box was not refused")
    ok += 1 if not p2["property"]["address"] else bad.append("a refused geocode still wrote an address")

    # an EPQS sentinel is a MISS, never an elevation
    g2 = fake({"geocoder": census_hit, "epqs": {"value": "-1000000"}, "phzmapi": {"zone": "7b"}})
    p3, r3 = derive("1 Example Road", {"zip": "30533"}, g2)
    ok += 1 if "elevation" not in p3.get("location", {}) else bad.append("a sentinel became an elevation")

    # a dead elevation service does not kill the derivation
    g3 = fake({"geocoder": census_hit, "epqs": RuntimeError("boom"), "phzmapi": {"zone": "7b"}})
    p4, r4 = derive("1 Example Road", {"zip": "30533"}, g3)
    ok += 1 if p4["property"]["address"] and "elevation" not in p4.get("location", {}) else bad.append("an outage lost the whole record")

    # the tracked-path guard must REFUSE
    try:
        refuse_if_tracked(os.path.join(ROOT, "instance", "fernwood.json")); bad.append("a tracked path was not refused")
    except SystemExit:
        ok += 1
    try:
        refuse_if_tracked(os.path.join(ROOT, ".private", "derived", "x.json")); ok += 1
    except SystemExit:
        bad.append("an untracked private path was wrongly refused")

    print("selftest: %d passed, %d failed" % (ok, len(bad)))
    for b in bad: print("   🔴", b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
