#!/usr/bin/env python3
"""Fetch lead photos from Wikipedia/Wikimedia Commons for any species/item category.

Usage:
    python3 tools/fetch-photos.py --category birds
    python3 tools/fetch-photos.py --category amphibians
    python3 tools/fetch-photos.py --category fishing
    python3 tools/fetch-photos.py --category plants
    python3 tools/fetch-photos.py --category birds wild-turkey --force

For each item in the category's JSON, this script:
1. Calls the Wikipedia REST summary endpoint to find the lead image (preferring
   scientific name lookup with a common-name fallback).
2. Resolves the Commons file metadata (author, license, source URL).
3. Downloads a width-constrained JPEG to images/{category}/{id}.jpg.
4. Writes an attribution log to images/{category}/_attribution.json.

Re-runnable: skips files that already exist locally unless --force is passed.
"""
import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
THUMB_WIDTH = 800  # large enough to look sharp at the ~500px hero display on retina
USER_AGENT = "TateTracker-PhotoFetcher/1.0 (paul.kirschenbauer@gmail.com)"

# Per-category configuration. `species_path` is the dot-path inside the JSON
# where the list of items lives. `prefer` is the lookup order: "sci" tries the
# scientific name first then common name; "common" does the opposite.
CATEGORIES = {
    "birds": {
        "json_file": "birds.json",
        "species_path": "species",
        "image_dir": "images/birds",
        "prefer": "common",  # bird common names disambiguate cleanly on Wikipedia
        "page_overrides": {
            "wild-turkey": "Wild_turkey",
        },
        "file_overrides": {},
    },
    "amphibians": {
        "json_file": "amphibians.json",
        "species_path": "species",
        "image_dir": "images/amphibians",
        "prefer": "sci",  # amphibian common names ambiguate; scientific is safer
        "page_overrides": {},
        "file_overrides": {},
    },
    "fishing": {
        "json_file": "fishing.json",
        "species_path": "species",
        "image_dir": "images/fishing",
        "prefer": "common",
        "page_overrides": {},
        "file_overrides": {},
    },
    "plants": {
        "json_file": "plants.json",
        "species_path": "plants",
        "image_dir": "images/plants",
        "prefer": "sci",  # genus/species more reliable than cultivar trade names
        "page_overrides": {
            # Trademarked cultivars: fall back to genus-level Wikipedia pages.
            "pyracomeles-berry-box": "Pyracantha",  # ×Pyracomeles is a Pyracantha × Osteomeles hybrid; no dedicated WP article
            "deutzia-yuki-cherry-blossom": "Deutzia",
            "clematis": "Clematis",
            "hosta": "Hosta",
            "iris-pond": "Iris_versicolor",
            "azalea": "Rhododendron",  # azaleas are a subgenus of Rhododendron
            "hydrangea": "Hydrangea",
            "boxwood": "Buxus",
            "holly": "Ilex",
        },
        "file_overrides": {},
    },
    "snakes": {
        "json_file": "snakes.json",
        "species_path": "species",
        "image_dir": "images/snakes",
        "prefer": "sci",  # snake common names disambiguate poorly (e.g., "rat snake")
        "page_overrides": {
            # Eastern Rat Snake's accepted Wikipedia title uses the older binomial in some indexings
            "eastern-rat-snake": "Pantherophis_alleghaniensis",
            # Ringneck Snake article is under hyphenated form
            "ringneck-snake": "Ring-necked_snake",
            # Dekay's brown snake hyphenation matters on WP
            "dekays-brown-snake": "Storeria_dekayi",
        },
        "file_overrides": {},
    },
    "lizards": {
        "json_file": "lizards.json",
        "species_path": "species",
        "image_dir": "images/lizards",
        "prefer": "sci",
        "page_overrides": {},
        "file_overrides": {
            # WP article lead is a hand-held shot; this is a naturalistic in-situ photo by 2ndPeter (Flickr → Commons)
            "ground-skink": "File:Ground Skink (Scincella lateralis) - Flickr - 2ndPeter.jpg",
        },
    },
    "mammals": {
        "json_file": "mammals.json",
        "species_path": "species",
        "image_dir": "images/mammals",
        "prefer": "sci",  # scientific names unambiguous; common names mostly fine too but sci is the safer default
        "page_overrides": {
            # "bats" is order-level (species unconfirmed at property); use the WP article on Bats
            "bats": "Bat",
        },
        "file_overrides": {},
    },
}


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


class _TextStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def html_to_text(s):
    if not s:
        return ""
    p = _TextStripper()
    p.feed(s)
    return "".join(p.parts).strip()


def get_at_path(d, path):
    """Walk a dot path inside a dict (e.g., 'species' or 'sub.list')."""
    for part in path.split("."):
        d = d[part]
    return d


def candidate_titles(item, prefer):
    """Yield Wikipedia article titles to try, in order."""
    sci = item.get("scientificName", "")
    name = item.get("name", "")
    # Scientific names sometimes have qualifiers like "spp." or " (cultivar)" —
    # take just the first two words if it looks like a binomial.
    sci_words = sci.split()
    binomial = None
    if len(sci_words) >= 2 and sci_words[0][0].isupper():
        binomial = "_".join(sci_words[:2]).rstrip(".,;:")

    options = []
    if prefer == "sci":
        if binomial:
            options.append(binomial)
        if name:
            options.append(name.replace(" ", "_"))
    else:
        if name:
            options.append(name.replace(" ", "_"))
        if binomial:
            options.append(binomial)
    # De-dup while preserving order
    seen = set()
    for o in options:
        if o not in seen:
            seen.add(o)
            yield o


def find_commons_file(item, cfg):
    if item["id"] in cfg["file_overrides"]:
        return cfg["file_overrides"][item["id"]]

    titles = []
    if item["id"] in cfg["page_overrides"]:
        titles.append(cfg["page_overrides"][item["id"]])
    titles.extend(candidate_titles(item, cfg["prefer"]))

    last_err = None
    for title in titles:
        try:
            summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(title)}"
            summary = fetch_json(summary_url)
            img_url = (summary.get("originalimage") or summary.get("thumbnail") or {}).get("source")
            if not img_url:
                continue
            fname = urllib.parse.unquote(img_url.split("/")[-1])
            if img_url.startswith("https://upload.wikimedia.org/wikipedia/commons/thumb/"):
                fname = urllib.parse.unquote(img_url.split("/")[-2])
            fname = fname.split("?")[0]  # strip query strings (utm_source etc.) Wikipedia now appends to lead-image URLs
            return f"File:{fname}"
        except Exception as e:
            last_err = e
            continue
    if last_err:
        print(f"  (last lookup error: {last_err})")
    return None


def fetch_commons_meta(file_title):
    api = (
        "https://commons.wikimedia.org/w/api.php?action=query&format=json"
        f"&prop=imageinfo&iiprop=url%7Cextmetadata&iiurlwidth={THUMB_WIDTH}"
        f"&titles={urllib.parse.quote(file_title)}"
    )
    data = fetch_json(api)
    pages = data.get("query", {}).get("pages", {})
    for _, page in pages.items():
        ii_list = page.get("imageinfo")
        if not ii_list:
            return None
        ii = ii_list[0]
        em = ii.get("extmetadata", {})
        return {
            "thumburl": ii.get("thumburl"),
            "url": ii.get("url"),
            "descurl": ii.get("descriptionurl"),
            "artist": html_to_text(em.get("Artist", {}).get("value", "")) or "Unknown",
            "license": em.get("LicenseShortName", {}).get("value", ""),
            "license_url": em.get("LicenseUrl", {}).get("value", ""),
            "credit": html_to_text(em.get("Credit", {}).get("value", "")),
        }
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", required=True, choices=sorted(CATEGORIES.keys()))
    ap.add_argument("--force", action="store_true")
    ap.add_argument("ids", nargs="*", help="optional: limit to specific ids")
    args = ap.parse_args()

    cfg = CATEGORIES[args.category]
    json_path = os.path.join(ROOT, cfg["json_file"])
    img_dir = os.path.join(ROOT, cfg["image_dir"])
    attr_file = os.path.join(img_dir, "_attribution.json")

    os.makedirs(img_dir, exist_ok=True)
    with open(json_path) as f:
        data = json.load(f)
    items = get_at_path(data, cfg["species_path"])

    attribution = {}
    if os.path.exists(attr_file):
        with open(attr_file) as f:
            attribution = json.load(f)

    for item in items:
        sid = item["id"]
        if args.ids and sid not in args.ids:
            continue
        out = os.path.join(img_dir, f"{sid}.jpg")
        if os.path.exists(out) and not args.force:
            print(f"[skip] {sid} (already downloaded)")
            continue

        try:
            print(f"[fetch] {sid} — {item['name']}")
            file_title = find_commons_file(item, cfg)
            if not file_title:
                print(f"  ! no lead image found")
                continue
            meta = fetch_commons_meta(file_title)
            if not meta or not meta.get("thumburl"):
                print(f"  ! no metadata for {file_title}")
                continue
            print(f"  file: {file_title}")
            print(f"  artist: {meta['artist'][:60]}")
            print(f"  license: {meta['license']}")
            img_bytes = fetch_bytes(meta["thumburl"])
            with open(out, "wb") as f:
                f.write(img_bytes)
            attribution[sid] = {
                "file": file_title,
                "author": meta["artist"],
                "license": meta["license"],
                "license_url": meta["license_url"],
                "source_url": meta["descurl"],
                "credit": meta["credit"],
            }
            time.sleep(0.5)
        except Exception as e:
            print(f"  ! error: {e}")
            continue

    with open(attr_file, "w") as f:
        json.dump(attribution, f, indent=2, sort_keys=True)
    print(f"\nWrote {attr_file}")


if __name__ == "__main__":
    main()
