#!/usr/bin/env python3
"""Merge attribution log into a category JSON AND re-inline its data const in viewer.html.

Usage:
    python3 tools/wire-photos.py --category birds
    python3 tools/wire-photos.py --category amphibians
    python3 tools/wire-photos.py --category fishing
    python3 tools/wire-photos.py --category plants

For the chosen category, this script:
1. Reads images/{category}/_attribution.json and the source JSON file
2. Adds `photo` (relative path) + `attribution` (source/author/license/url) to each item
3. Writes back the JSON
4. Re-inlines the corresponding `const {CATEGORY}_DATA = {...};` line in viewer.html
   (data is loaded at runtime from the inlined const, not fetched, so this must stay in sync)
"""
import argparse
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VIEWER = os.path.join(ROOT, "viewer.html")

CATEGORIES = {
    "birds":      {"json_file": "birds.json",      "data_const": "BIRDS_DATA",      "species_path": "species", "image_dir": "images/birds"},
    "amphibians": {"json_file": "amphibians.json", "data_const": "AMPHIBIANS_DATA", "species_path": "species", "image_dir": "images/amphibians"},
    "fishing":    {"json_file": "fishing.json",    "data_const": "FISHING_DATA",    "species_path": "species", "image_dir": "images/fishing"},
    "plants":     {"json_file": "plants.json",     "data_const": "PLANTS_DATA",     "species_path": "plants",  "image_dir": "images/plants"},
    "snakes":     {"json_file": "snakes.json",     "data_const": "SNAKES_DATA",     "species_path": "species", "image_dir": "images/snakes"},
    "lizards":    {"json_file": "lizards.json",    "data_const": "LIZARDS_DATA",    "species_path": "species", "image_dir": "images/lizards"},
    "mammals":    {"json_file": "mammals.json",    "data_const": "MAMMALS_DATA",    "species_path": "species", "image_dir": "images/mammals"},
}


def get_at_path(d, path):
    for part in path.split("."):
        d = d[part]
    return d


def merge_attribution(cfg):
    json_path = os.path.join(ROOT, cfg["json_file"])
    attr_file = os.path.join(ROOT, cfg["image_dir"], "_attribution.json")
    img_dir_rel = cfg["image_dir"]

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
        item["photo"] = f"{img_dir_rel}/{sid}.jpg"
        item["attribution"] = {
            "source": "Wikimedia Commons",
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
    print(f"Re-inlined {const_name} into {VIEWER}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", required=True, choices=sorted(CATEGORIES.keys()))
    args = ap.parse_args()
    cfg = CATEGORIES[args.category]
    data = merge_attribution(cfg)
    reinline_into_viewer(cfg, data)


if __name__ == "__main__":
    main()
