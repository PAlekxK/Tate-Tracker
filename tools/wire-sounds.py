#!/usr/bin/env python3
"""Merge audio attribution into a category JSON AND re-inline its data const.

Usage:
    python3 tools/wire-sounds.py --category birds
    python3 tools/wire-sounds.py --category frogs

For the chosen category, this script:
1. Reads sounds/{cat}/_attribution.json and the source JSON file
2. Adds `sound` (relative path) + `soundAttribution` (source/author/license/url) per item
3. Writes back the JSON
4. Re-inlines the corresponding `const {CATEGORY}_DATA = {...};` line in viewer.html

Notes:
- Frogs share amphibians.json with salamanders. Salamanders never get a sound
  field (silent species). The script only writes the sound field for items that
  appear in the attribution log.
- After re-inlining, prints how many `"sound":` fields ended up in viewer.html
  for the relevant data const, so wiring failures are loud.
"""
import argparse
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VIEWER = os.path.join(ROOT, "viewer.html")

CATEGORIES = {
    "birds": {
        "json_file": "birds.json",
        "data_const": "BIRDS_DATA",
        "species_path": "species",
        "sound_dir": "sounds/birds",
    },
    "frogs": {
        "json_file": "amphibians.json",
        "data_const": "AMPHIBIANS_DATA",
        "species_path": "species",
        "sound_dir": "sounds/frogs",
    },
    "mammals": {
        "json_file": "mammals.json",
        "data_const": "MAMMALS_DATA",
        "species_path": "species",
        "sound_dir": "sounds/mammals",
    },
    # Added 2026-08-15 with the Insect Sounds tab. This is the half that actually
    # reaches the app: fetch-sounds.py only downloads files and writes the
    # attribution log — the `sound` field, and the re-inline that makes it render,
    # happen HERE. A category present in fetch-sounds but missing here downloads
    # audio that nothing ever plays.
    "insects": {
        "json_file": "insects.json",
        "data_const": "INSECTS_DATA",
        "species_path": "species",
        "sound_dir": "sounds/insects",
    },
}


def get_at_path(d, path):
    for part in path.split("."):
        d = d[part]
    return d


def merge_attribution(cfg):
    json_path = os.path.join(ROOT, cfg["json_file"])
    attr_file = os.path.join(ROOT, cfg["sound_dir"], "_attribution.json")
    sound_dir_rel = cfg["sound_dir"]

    with open(json_path) as f:
        data = json.load(f)
    with open(attr_file) as f:
        attribution = json.load(f)

    items = get_at_path(data, cfg["species_path"])
    updated = 0
    for item in items:
        sid = item["id"]
        if sid not in attribution:
            continue
        a = attribution[sid]
        ext = a.get("ext", "mp3")
        item["sound"] = f"{sound_dir_rel}/{sid}.{ext}"
        item["soundAttribution"] = {
            "source": a.get("source", "Wikimedia Commons"),
            "author": a["author"],
            "license": a["license"],
            "url": a["source_url"],
        }
        updated += 1

    with open(json_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Updated {updated}/{len(items)} items in {cfg['json_file']}")
    return data


def reinline_into_viewer(cfg, data):
    with open(VIEWER, "r", encoding="utf-8") as f:
        html = f.read()

    const_name = cfg["data_const"]
    pattern = re.compile(rf"const {const_name} = \{{.*?\}};", re.DOTALL)
    if not pattern.search(html):
        raise SystemExit(f"Could not find `const {const_name} = {{...}};` in viewer.html")

    new_blob = f"const {const_name} = " + json.dumps(data, ensure_ascii=False) + ";"
    new_html = pattern.sub(lambda _: new_blob, html, count=1)

    with open(VIEWER, "w", encoding="utf-8") as f:
        f.write(new_html)

    # Sanity check: count sound fields inside the rewritten const
    const_match = re.search(rf"const {const_name} = (\{{.*?\}});", new_html, re.DOTALL)
    sound_count = 0
    if const_match:
        sound_count = const_match.group(1).count('"sound":')
    print(f"Re-inlined {const_name} into viewer.html (sound fields wired: {sound_count})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", required=True, choices=sorted(CATEGORIES.keys()))
    args = ap.parse_args()
    cfg = CATEGORIES[args.category]
    data = merge_attribution(cfg)
    reinline_into_viewer(cfg, data)


if __name__ == "__main__":
    main()
