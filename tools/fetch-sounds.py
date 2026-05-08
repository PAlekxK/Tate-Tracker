#!/usr/bin/env python3
"""Fetch reference audio recordings from Wikimedia Commons for vocal species.

Usage:
    python3 tools/fetch-sounds.py --category birds
    python3 tools/fetch-sounds.py --category frogs
    python3 tools/fetch-sounds.py --category birds pileated-woodpecker --force

For each vocal species in the category's JSON, this script:
1. Searches Commons for `{scientificName} filetype:audio` (namespace 6).
2. Fetches imageinfo for each candidate, picks the first CC-licensed file
   in a reasonable size range (skips tiny test snippets and huge field tapes).
3. Downloads the original file (mp3 or ogg) to sounds/{cat}/{id}.{ext}.
4. Writes an attribution log to sounds/{cat}/_attribution.json.

Salamanders are skipped automatically — they don't vocalize.
"""
import argparse
import json
import os
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
USER_AGENT = "TateTracker-SoundFetcher/1.0 (paul.kirschenbauer@gmail.com)"

MIN_BYTES = 50_000      # skip tiny snippets
MAX_BYTES = 8_000_000   # skip huge field tapes — dashboard wants short reference clips
ACCEPTED_LICENSE_PREFIXES = ("CC", "Public domain", "PDM")

# When the species' Latin binomial doesn't surface a usable recording, try these
# Wikipedia-page-style fallbacks. Most species don't need overrides.
SPECIES_OVERRIDES = {
    # Fowler's Toad — Commons also indexes under older synonym "Bufo fowleri"
    "fowlers-toad": ["Bufo fowleri", "Anaxyrus fowleri call"],
}

CATEGORIES = {
    "birds": {
        "json_file": "birds.json",
        "species_path": "species",
        "sound_dir": "sounds/birds",
        "is_vocal": lambda item: True,  # all birds vocalize
    },
    "frogs": {
        # We pull from amphibians.json but only fetch sounds for frogs/toads;
        # salamanders are silent.
        "json_file": "amphibians.json",
        "species_path": "species",
        "sound_dir": "sounds/frogs",
        "is_vocal": lambda item: "salamander" not in item["name"].lower(),
    },
}


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as r:
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
    for part in path.split("."):
        d = d[part]
    return d


def search_audio_candidates(query, limit=8):
    q = urllib.parse.quote(f"{query} filetype:audio")
    url = (
        f"https://commons.wikimedia.org/w/api.php?action=query&format=json"
        f"&list=search&srsearch={q}&srnamespace=6&srlimit={limit}"
    )
    data = fetch_json(url)
    return [hit["title"] for hit in data.get("query", {}).get("search", [])]


def fetch_commons_meta(file_title):
    api = (
        "https://commons.wikimedia.org/w/api.php?action=query&format=json"
        "&prop=imageinfo&iiprop=url%7Csize%7Cextmetadata&iilimit=1"
        f"&titles={urllib.parse.quote(file_title)}"
    )
    data = fetch_json(api)
    for _, page in data.get("query", {}).get("pages", {}).items():
        ii_list = page.get("imageinfo")
        if not ii_list:
            return None
        ii = ii_list[0]
        em = ii.get("extmetadata", {})
        return {
            "url": ii.get("url"),
            "descurl": ii.get("descriptionurl"),
            "size": ii.get("size", 0),
            "mime": ii.get("mime", ""),
            "artist": html_to_text(em.get("Artist", {}).get("value", "")) or "Unknown",
            "license": em.get("LicenseShortName", {}).get("value", ""),
            "license_url": em.get("LicenseUrl", {}).get("value", ""),
        }
    return None


def license_ok(lic):
    if not lic:
        return False
    return any(lic.startswith(p) for p in ACCEPTED_LICENSE_PREFIXES) or "Public domain" in lic


def pick_best(meta_candidates):
    """Pick the first CC-licensed candidate within size bounds."""
    for title, meta in meta_candidates:
        if not meta:
            continue
        if not license_ok(meta["license"]):
            continue
        if meta["size"] < MIN_BYTES or meta["size"] > MAX_BYTES:
            continue
        return title, meta
    # Fallback: same constraints minus the size cap (still license-filtered).
    for title, meta in meta_candidates:
        if meta and license_ok(meta["license"]):
            return title, meta
    return None, None


def find_audio(item, cfg):
    queries = []
    sci = item.get("scientificName", "")
    if sci:
        queries.append(sci)
    queries.extend(SPECIES_OVERRIDES.get(item["id"], []))
    queries.append(item.get("name", ""))

    seen_titles = set()
    candidates = []  # list of (title, meta)
    for q in queries:
        if not q:
            continue
        try:
            titles = search_audio_candidates(q)
        except Exception as e:
            print(f"  ! search error for '{q}': {e}")
            continue
        for t in titles:
            if t in seen_titles:
                continue
            seen_titles.add(t)
            try:
                meta = fetch_commons_meta(t)
            except Exception as e:
                print(f"  ! meta error for {t}: {e}")
                meta = None
            candidates.append((t, meta))
            time.sleep(0.15)
        # Try to short-circuit early if the binomial query already gave usable hits
        title, meta = pick_best(candidates)
        if title:
            return title, meta
    return pick_best(candidates)


def file_extension(meta):
    # The URL extension is authoritative — Commons sometimes returns a MIME
    # that doesn't match the actual file format (e.g. audio/mpeg on an .ogg).
    # Strip query string before matching: API URLs come with ?utm_source=...
    url = (meta or {}).get("url", "").lower().split("?", 1)[0]
    for ext in ("mp3", "ogg", "wav", "flac", "oga", "opus"):
        if url.endswith("." + ext):
            return "ogg" if ext in ("oga",) else ext
    mime = (meta or {}).get("mime", "")
    if "ogg" in mime:
        return "ogg"
    if "mpeg" in mime or "mp3" in mime:
        return "mp3"
    if "wav" in mime:
        return "wav"
    return "mp3"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", required=True, choices=sorted(CATEGORIES.keys()))
    ap.add_argument("--force", action="store_true")
    ap.add_argument("ids", nargs="*", help="optional: limit to specific ids")
    args = ap.parse_args()

    cfg = CATEGORIES[args.category]
    json_path = os.path.join(ROOT, cfg["json_file"])
    sound_dir = os.path.join(ROOT, cfg["sound_dir"])
    attr_file = os.path.join(sound_dir, "_attribution.json")

    os.makedirs(sound_dir, exist_ok=True)
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
        if not cfg["is_vocal"](item):
            print(f"[skip] {sid} (silent species)")
            continue

        # Skip if any audio file already exists for this id (mp3, ogg, wav)
        existing = None
        for ext in ("mp3", "ogg", "wav"):
            p = os.path.join(sound_dir, f"{sid}.{ext}")
            if os.path.exists(p):
                existing = p
                break
        if existing and not args.force:
            print(f"[skip] {sid} (already downloaded: {os.path.basename(existing)})")
            continue

        try:
            print(f"[fetch] {sid} — {item['name']}")
            file_title, meta = find_audio(item, cfg)
            if not file_title or not meta:
                print(f"  ! no usable recording found")
                continue
            ext = file_extension(meta)
            out = os.path.join(sound_dir, f"{sid}.{ext}")
            print(f"  file: {file_title}")
            print(f"  artist: {meta['artist'][:60]}")
            print(f"  license: {meta['license']}")
            print(f"  size: {meta['size']:,} bytes ({ext})")
            audio_bytes = fetch_bytes(meta["url"])
            with open(out, "wb") as f:
                f.write(audio_bytes)
            attribution[sid] = {
                "file": file_title,
                "ext": ext,
                "author": meta["artist"],
                "license": meta["license"],
                "license_url": meta["license_url"],
                "source_url": meta["descurl"],
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
