#!/usr/bin/env python3
"""Merge attribution log into birds.json AND re-inline BIRDS_DATA in viewer.html.

Reads images/birds/_attribution.json and birds.json, merges, writes back.
Then updates the inlined `const BIRDS_DATA = {...};` line in viewer.html so
the page sees the new data. (BIRDS_DATA is not fetched at runtime — the
inlined constant is the live source.)

Safe to re-run; adds/updates fields for any species that has a downloaded photo.
"""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BIRDS_JSON = os.path.join(ROOT, "birds.json")
VIEWER = os.path.join(ROOT, "viewer.html")
ATTR_FILE = os.path.join(ROOT, "images", "birds", "_attribution.json")
IMG_DIR_REL = "images/birds"


def merge_attribution_into_birds():
    with open(BIRDS_JSON) as f:
        birds = json.load(f)
    with open(ATTR_FILE) as f:
        attribution = json.load(f)

    updated = 0
    for sp in birds["species"]:
        sid = sp["id"]
        if sid not in attribution:
            continue
        a = attribution[sid]
        sp["photo"] = f"{IMG_DIR_REL}/{sid}.jpg"
        sp["attribution"] = {
            "source": "Wikimedia Commons",
            "author": a["author"],
            "license": a["license"],
            "url": a["source_url"],
        }
        updated += 1

    with open(BIRDS_JSON, "w") as f:
        json.dump(birds, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Updated {updated}/{len(birds['species'])} species in birds.json")
    return birds


def reinline_into_viewer(birds):
    with open(VIEWER, "r", encoding="utf-8") as f:
        html = f.read()

    # Match the entire `const BIRDS_DATA = {...};` line. The JSON is on one line.
    pattern = re.compile(r"const BIRDS_DATA = \{.*?\};", re.DOTALL)
    if not pattern.search(html):
        raise SystemExit("Could not find `const BIRDS_DATA = {...};` in viewer.html")

    new_blob = "const BIRDS_DATA = " + json.dumps(birds, ensure_ascii=False) + ";"
    new_html = pattern.sub(lambda _: new_blob, html, count=1)

    with open(VIEWER, "w", encoding="utf-8") as f:
        f.write(new_html)
    try:  # C4 5b: the engine template follows every direct edit of viewer.html
        import reinline; reinline.sync_template(VIEWER)
    except Exception as e:  # noqa: BLE001
        print("⚠️ template sync failed (run tools/build-viewer.py --extract):", e)
    print(f"Re-inlined BIRDS_DATA into {VIEWER}")


def main():
    birds = merge_attribution_into_birds()
    reinline_into_viewer(birds)


if __name__ == "__main__":
    main()
