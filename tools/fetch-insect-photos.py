#!/usr/bin/env python3
"""Fetch THREE reference photos per singing insect, from iNaturalist research-grade records.

Usage:
    python3 tools/fetch-insect-photos.py
    python3 tools/fetch-insect-photos.py snowy-tree-cricket --force

Why this is its own tool instead of a category in fetch-photos.py
----------------------------------------------------------------
`fetch-photos.py` pulls the Wikipedia lead image and returns exactly ONE photo,
matched by page title. Both halves of that are wrong for this domain:

1. **One photo cannot be checked.** On 2026-08-15 the sound pipeline downloaded a
   juvenile Australian magpie as the Morning Cicada, because *Gymnorhina tibicen*
   and *Neotibicen tibicen* share an epithet. That was catchable only because the
   FILENAME said magpie. A wrong cricket photo says nothing — it is a small brown
   insect that looks like every other small brown insect, and neither Paul nor an
   agent can eyeball a Carolina Ground Cricket against a Jumping Bush Cricket.
   Three photos from three INDEPENDENT observers is the hedge: if one is an
   outlier, it reads as an outlier next to the other two, and the reader can see
   that for themselves rather than trusting us.
2. **Title matching is the weak link.** iNaturalist research-grade means two or
   more humans agreed on the identification against the specimen, which is a far
   stronger claim than a filename containing a genus. We take the lower hit rate.

Licensing: photo-level license only (an observation may be CC-BY while a photo on
it is CC-BY-NC). NC is fine for this personal, non-commercial dashboard.

⚠️ These are REFERENCE images, never property records. Nothing in insects.json has
been confirmed at Fernwood, so no insect photo may ever claim to have been taken
here — `wire-insect-photos.py` stamps every one of them accordingly.
"""
import argparse
import json
import os
import shutil
import subprocess
import time
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMAGE_DIR = os.path.join(ROOT, "images", "insects")
JSON_FILE = os.path.join(ROOT, "insects.json")

PHOTOS_PER_SPECIES = 3
# 800px matches fetch-photos.py's THUMB_WIDTH — the house size. Deliberately NOT
# smaller: these render three-across in the expanded card, and Paul's constraint
# was that size discipline must not make them too small to actually see. 800px
# stays sharp when displayed at ~200px on a retina screen.
TARGET_WIDTH = 800
JPEG_QUALITY = "high"

ACCEPTED_LICENSES = ("cc0", "cc-by", "cc-by-sa", "cc-by-nc", "cc-by-nc-sa")
LICENSE_LABELS = {
    "cc0": "CC0 1.0", "cc-by": "CC BY 4.0", "cc-by-sa": "CC BY-SA 4.0",
    "cc-by-nc": "CC BY-NC 4.0", "cc-by-nc-sa": "CC BY-NC-SA 4.0",
}
LICENSE_URLS = {
    "cc0": "https://creativecommons.org/publicdomain/zero/1.0/",
    "cc-by": "https://creativecommons.org/licenses/by/4.0/",
    "cc-by-sa": "https://creativecommons.org/licenses/by-sa/4.0/",
    "cc-by-nc": "https://creativecommons.org/licenses/by-nc/4.0/",
    "cc-by-nc-sa": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
}

USER_AGENT = "TateTracker-InsectPhotoFetcher/1.0 (paul.kirschenbauer@gmail.com)"


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def big_url(photo_url):
    """iNaturalist serves size variants by filename segment; 'square' is the default."""
    for size in ("square", "small", "medium"):
        if f"/{size}." in photo_url:
            return photo_url.replace(f"/{size}.", "/large.")
    return photo_url


def downscale(path):
    """Normalise to JPEG and cap width at TARGET_WIDTH via macOS sips.

    The format coercion is not cosmetic. iNaturalist serves some originals as PNG
    under a .jpg-looking URL, and a photographic PNG at 800px is ~10× the bytes of
    the same image as JPEG — measured: oblong-winged-katydid-1 came down 623 KB →
    56 KB with no visible change. Browsers sniff the real type and render it either
    way, so this costs nothing and would otherwise be invisible bloat.
    """
    if not shutil.which("sips"):
        return
    subprocess.run(
        ["sips", "-s", "format", "jpeg", "--resampleWidth", str(TARGET_WIDTH),
         "-s", "formatOptions", JPEG_QUALITY, path, "--out", path],
        check=False, capture_output=True,
    )


def find_photos(item):
    """Up to PHOTOS_PER_SPECIES CC photos, each from a DIFFERENT observer.

    Distinct observers matter more than distinct observations: two photos from one
    person carry one identification judgement, so they hedge nothing.
    """
    sci = item.get("scientificName", "")
    if not sci:
        return []
    url = (
        f"https://api.inaturalist.org/v1/observations?taxon_name={urllib.parse.quote(sci)}"
        f"&photos=true&quality_grade=research&per_page=60&order_by=votes"
    )
    try:
        data = fetch_json(url)
    except Exception as e:
        print(f"  ! iNaturalist error: {e}")
        return []

    picked, seen_users = [], set()
    for obs in data.get("results", []):
        user = (obs.get("user") or {}).get("login") or "?"
        if user in seen_users:
            continue
        for photo in obs.get("photos", []):
            lic = (photo.get("license_code") or "").lower()
            if lic not in ACCEPTED_LICENSES or not photo.get("url"):
                continue
            seen_users.add(user)
            picked.append({
                "url": big_url(photo["url"]),
                "author": (obs.get("user") or {}).get("name") or user,
                "license": LICENSE_LABELS.get(lic, lic.upper()),
                "license_url": LICENSE_URLS.get(lic, ""),
                "observation_url": f"https://www.inaturalist.org/observations/{obs.get('id')}",
                "observed_on": obs.get("observed_on") or "",
                "place": (obs.get("place_guess") or "").strip(),
            })
            break
        if len(picked) >= PHOTOS_PER_SPECIES:
            break
    return picked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("ids", nargs="*", help="optional: limit to specific species ids")
    args = ap.parse_args()

    os.makedirs(IMAGE_DIR, exist_ok=True)
    with open(JSON_FILE) as f:
        species = json.load(f)["species"]

    attr_file = os.path.join(IMAGE_DIR, "_attribution.json")
    attribution = {}
    if os.path.exists(attr_file):
        with open(attr_file) as f:
            attribution = json.load(f)

    short = []
    for item in species:
        sid = item["id"]
        if args.ids and sid not in args.ids:
            continue
        existing = [p for p in range(1, PHOTOS_PER_SPECIES + 1)
                    if os.path.exists(os.path.join(IMAGE_DIR, f"{sid}-{p}.jpg"))]
        if len(existing) == PHOTOS_PER_SPECIES and not args.force:
            print(f"[skip] {sid} (already has {PHOTOS_PER_SPECIES})")
            continue

        print(f"[fetch] {sid} — {item['name']}")
        photos = find_photos(item)
        if not photos:
            print("  ! no CC research-grade photos found")
            short.append((sid, 0))
            continue

        saved = []
        for n, p in enumerate(photos, start=1):
            out = os.path.join(IMAGE_DIR, f"{sid}-{n}.jpg")
            try:
                with open(out, "wb") as f:
                    f.write(fetch_bytes(p["url"]))
                downscale(out)
                kb = os.path.getsize(out) // 1024
                print(f"  {n}. {p['author'][:28]:<28} {p['license']:<16} {kb} KB")
                saved.append({k: v for k, v in p.items() if k != "url"})
            except Exception as e:
                print(f"  ! photo {n} failed: {e}")
        if saved:
            attribution[sid] = saved
        if len(saved) < PHOTOS_PER_SPECIES:
            short.append((sid, len(saved)))
        time.sleep(0.4)

    with open(attr_file, "w") as f:
        json.dump(attribution, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write("\n")
    print(f"\nWrote {attr_file}")
    if short:
        # Never silently under-deliver: the whole point of three is the cross-check,
        # so a species that got fewer is a REPORTED gap, not a quiet one.
        print(f"⚠️  fewer than {PHOTOS_PER_SPECIES} photos for {len(short)} species:")
        for sid, n in short:
            print(f"     {sid}: {n}")


if __name__ == "__main__":
    main()
