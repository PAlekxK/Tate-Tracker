#!/usr/bin/env python3
"""Fetch lead photos for each bird species from Wikipedia/Wikimedia Commons.

For each species in birds.json, this script:
1. Calls the Wikipedia REST summary endpoint to find the lead image
2. Resolves the Commons file metadata (author, license, source URL)
3. Downloads a width-constrained JPEG to images/birds/{id}.jpg
4. Writes an attribution log to images/birds/_attribution.json

Re-runnable: skips files that already exist locally unless --force is passed.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BIRDS_JSON = os.path.join(ROOT, "birds.json")
IMG_DIR = os.path.join(ROOT, "images", "birds")
ATTR_FILE = os.path.join(IMG_DIR, "_attribution.json")
THUMB_WIDTH = 500
USER_AGENT = "TateTracker-PhotoFetcher/1.0 (paul.kirschenbauer@gmail.com)"

# Manual overrides for species where the auto-pulled lead image is poor or
# misidentified. Maps species id → Wikipedia page title to use for lookup.
PAGE_OVERRIDES = {
    # Wikipedia disambiguates "Wild_Turkey" — the species page is lowercase.
    "wild-turkey": "Wild_turkey",
}

# Force-pick a specific Commons file (skip the Wikipedia summary lookup) when
# the lead image on the Wikipedia article isn't great. Maps species id → File: name.
FILE_OVERRIDES = {
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


def page_title_for(species):
    if species["id"] in PAGE_OVERRIDES:
        return PAGE_OVERRIDES[species["id"]]
    # Default: use the common name with underscores.
    return species["name"].replace(" ", "_")


def find_commons_file(species):
    """Return the bare 'File:Foo.jpg' Commons title for the species lead image."""
    if species["id"] in FILE_OVERRIDES:
        return FILE_OVERRIDES[species["id"]]
    title = page_title_for(species)
    summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(title)}"
    summary = fetch_json(summary_url)
    img_url = (summary.get("originalimage") or summary.get("thumbnail") or {}).get("source")
    if not img_url:
        return None
    # URL form: https://upload.wikimedia.org/wikipedia/commons/X/YY/Filename.jpg
    # Extract just the filename (last path segment).
    fname = urllib.parse.unquote(img_url.split("/")[-1])
    # If the URL was a thumbnail, the filename is preceded by ".../thumb/X/YY/Filename.jpg/NNNpx-Filename.jpg".
    # In that case the second-to-last segment is the real file.
    if img_url.startswith("https://upload.wikimedia.org/wikipedia/commons/thumb/"):
        fname = urllib.parse.unquote(img_url.split("/")[-2])
    return f"File:{fname}"


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
    force = "--force" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    os.makedirs(IMG_DIR, exist_ok=True)
    with open(BIRDS_JSON) as f:
        birds = json.load(f)
    attribution = {}
    if os.path.exists(ATTR_FILE):
        with open(ATTR_FILE) as f:
            attribution = json.load(f)

    for sp in birds["species"]:
        sid = sp["id"]
        if only and sid not in only:
            continue
        out = os.path.join(IMG_DIR, f"{sid}.jpg")
        if os.path.exists(out) and not force:
            print(f"[skip] {sid} (already downloaded)")
            continue

        try:
            print(f"[fetch] {sid} — {sp['name']}")
            file_title = find_commons_file(sp)
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
            time.sleep(0.5)  # polite to Wikimedia
        except Exception as e:
            print(f"  ! error: {e}")
            continue

    with open(ATTR_FILE, "w") as f:
        json.dump(attribution, f, indent=2, sort_keys=True)
    print(f"\nWrote {ATTR_FILE}")


if __name__ == "__main__":
    main()
