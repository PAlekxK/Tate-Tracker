#!/usr/bin/env python3
"""Merge insect photo attribution into insects.json AND re-inline INSECTS_DATA.

Usage:
    python3 tools/wire-insect-photos.py

The half that actually reaches the app. `fetch-insect-photos.py` only downloads
files and writes the attribution log; the `photos` array — and the re-inline that
makes it render — happen HERE. Photos on disk that were never wired are photos
nobody sees, which is the same failure the sound pipeline's own header warns about.

Writes per species:

    "photos": [
      {"src": "images/insects/<id>-1.jpg", "author": …, "license": …,
       "licenseUrl": …, "url": …, "observedOn": …, "place": …},
      … up to 3 …
    ]

⚠️ REFERENCE, NOT RECORD. Every entry is stamped `"reference": true`. Nothing in
insects.json has been confirmed at Fernwood — these are photographs of the species
taken somewhere else by someone else, and the card must never let a reader mistake
one for a picture of this property. `place`/`observedOn` are carried so the card
can say where it actually was taken, which is the honest version of a caption.
"""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VIEWER = os.path.join(ROOT, "viewer.html")
JSON_FILE = os.path.join(ROOT, "insects.json")
ATTR_FILE = os.path.join(ROOT, "images", "insects", "_attribution.json")
IMAGE_DIR_REL = "images/insects"


def main():
    with open(JSON_FILE) as f:
        data = json.load(f)
    with open(ATTR_FILE) as f:
        attribution = json.load(f)

    species = data["species"]
    updated = 0
    total_photos = 0
    short = []

    for item in species:
        sid = item["id"]
        entries = attribution.get(sid)
        if not entries:
            short.append((sid, 0))
            continue
        photos = []
        for n, a in enumerate(entries, start=1):
            src = f"{IMAGE_DIR_REL}/{sid}-{n}.jpg"
            if not os.path.exists(os.path.join(ROOT, src)):
                # The log claims a photo the disk does not have — say so rather
                # than wiring a src that renders as a broken image on Mom's phone.
                print(f"  ! {sid}: attribution lists photo {n} but {src} is missing")
                continue
            photos.append({
                "src": src,
                "author": a.get("author", "Unknown"),
                "license": a.get("license", ""),
                "licenseUrl": a.get("license_url", ""),
                "url": a.get("observation_url", ""),
                "observedOn": a.get("observed_on", ""),
                "place": a.get("place", ""),
                "reference": True,
            })
        if not photos:
            short.append((sid, 0))
            continue
        item["photos"] = photos
        # The collapsed row shows one thumb; keep the existing single-photo field
        # pointing at the first so renderInsectCard's `sp.photo` branch — shared
        # with every other Wildlife tab — keeps working unchanged.
        item["photo"] = photos[0]["src"]
        updated += 1
        total_photos += len(photos)
        if len(photos) < 3:
            short.append((sid, len(photos)))

    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Updated {updated}/{len(species)} species in insects.json ({total_photos} photos)")

    with open(VIEWER, encoding="utf-8") as f:
        html = f.read()
    pattern = re.compile(r"const INSECTS_DATA = \{.*?\};", re.DOTALL)
    if not pattern.search(html):
        raise SystemExit("Could not find `const INSECTS_DATA = {...};` in viewer.html")
    blob = "const INSECTS_DATA = " + json.dumps(data, ensure_ascii=False) + ";"
    html = pattern.sub(lambda _: blob, html, count=1)
    with open(VIEWER, "w", encoding="utf-8") as f:
        f.write(html)

    const = re.search(r"const INSECTS_DATA = (\{.*?\});", html, re.DOTALL)
    wired = const.group(1).count('"src": "images/insects/') if const else 0
    print(f"Re-inlined INSECTS_DATA into viewer.html (photo srcs wired: {wired})")

    if short:
        print(f"⚠️  fewer than 3 photos for {len(short)} species: "
              + ", ".join(f"{s}({n})" for s, n in short))


if __name__ == "__main__":
    main()
