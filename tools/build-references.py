#!/usr/bin/env python3
"""
build-references.py — parse research-resources.md into references.json.

The markdown file is Paul's long-form research notebook (working voice,
includes "Dashboard integration idea" + "Depth tier" lines, prefatory
sections like "Top finds" + the two Quick reference tables). The JSON
output is the curated published shape — what the dashboard's Sources card
renders. Per the 2026-05-21 reference-card reviews:
  - Drop "Category N:" numbering, scope parentheticals; normalize "&" → "and"
  - Skip prefatory sections (Top finds, both Quick reference tables)
  - Skip Dashboard-integration + Depth-tier lines (operator/metadata, not voice)
  - Prefer "Why it's relevant here" as the framing line; fall back to "What it is"

Run from the repo root:
    python3 tools/build-references.py

Output: references.json at the repo root. Re-run when research-resources.md changes.
"""

import datetime as dt
import json
import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCE_MD = os.path.join(REPO_ROOT, "research-resources.md")
OUTPUT_JSON = os.path.join(REPO_ROOT, "references.json")

# Per content-steward's 2026-05-21 review: utilitarian-plain section labels.
CATEGORY_LABEL_REWRITES = {
    "Category 1: Extension & academia (Georgia-specific)": "Extension and academia",
    "Category 2: Native plants & habitat": "Native plants and habitat",
    "Category 3: Wildlife (state & federal)": "Wildlife — state and federal",
    "Category 4: Land, soil, water": "Land, soil, water",
    "Category 5: Fishing & aquatic (Lake Sequoyah / regional)": "Fishing and the lake",
    "Category 6: Climate, dark sky, homesteading-adjacent": "Climate, dark sky, homesteading",
    "Category 7: History & cultural heritage (local & regional)": "History and cultural heritage",
    "Category 8: Local events & day trips (within ~45 min)": "Events and day trips nearby",
}


def slugify(s):
    s = s.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[-\s]+", "-", s).strip("-")
    return s


def extract_url(value):
    """The URL field sometimes has multiple URLs (e.g. landing page + PDF).
    Take the first http(s) URL."""
    m = re.search(r"https?://\S+", value)
    if not m:
        return ""
    url = m.group(0)
    # Strip trailing punctuation that shouldn't be part of the URL
    while url and url[-1] in ".,;:)":
        url = url[:-1]
    return url


def parse():
    if not os.path.exists(SOURCE_MD):
        print(f"ERROR: {SOURCE_MD} not found", file=sys.stderr)
        sys.exit(1)

    with open(SOURCE_MD) as f:
        text = f.read()

    lines = text.splitlines()

    categories = []
    current_category = None
    current_entry = None
    current_field = None  # which **Field:** we're accumulating into
    field_buffer = []

    def flush_field():
        nonlocal current_field, field_buffer
        if current_field is None or current_entry is None:
            current_field = None
            field_buffer = []
            return
        value = " ".join(s.strip() for s in field_buffer).strip()
        current_entry[current_field] = value
        current_field = None
        field_buffer = []

    def flush_entry():
        nonlocal current_entry
        if current_entry is None:
            return
        flush_field()
        # Only keep entries that have at least one of url + framing
        framing = current_entry.get("why_relevant") or current_entry.get("what_it_is") or ""
        url = extract_url(current_entry.get("url", ""))
        if framing or url:
            categories[-1]["entries"].append({
                "title": current_entry["title"],
                "url": url,
                "framing": framing.strip(),
            })
        current_entry = None

    def flush_category():
        nonlocal current_category
        if current_category is None:
            return
        flush_entry()
        current_category = None

    for line in lines:
        # Category headers
        h2 = re.match(r"^##\s+(.+?)\s*$", line)
        if h2:
            heading = h2.group(1).strip()
            flush_category()
            if heading in CATEGORY_LABEL_REWRITES:
                label = CATEGORY_LABEL_REWRITES[heading]
                categories.append({
                    "id": slugify(label),
                    "label": label,
                    "entries": [],
                })
                current_category = label
            else:
                # Prefatory section ("Top finds", "Quick reference — ..."): skip
                current_category = None
            continue

        # Entry headers
        h3 = re.match(r"^###\s+(.+?)\s*$", line)
        if h3 and current_category:
            flush_entry()
            title = h3.group(1).strip()
            current_entry = {"title": title}
            continue

        # Field starts (e.g. "**URL:** https://...")
        field_match = re.match(r"^\*\*([^:]+):\*\*\s*(.*)$", line)
        if field_match and current_entry is not None:
            flush_field()
            field_name = field_match.group(1).strip().lower()
            field_value = field_match.group(2).strip()
            mapped = {
                "url": "url",
                "what it is": "what_it_is",
                "why it's relevant here": "why_relevant",
                "why it's relevant": "why_relevant",
            }.get(field_name)
            # Explicitly skip dashboard-integration + depth-tier per voice review
            if field_name in ("dashboard integration idea", "depth tier"):
                current_field = None
                field_buffer = []
                continue
            if mapped:
                current_field = mapped
                field_buffer = [field_value]
            else:
                current_field = None
                field_buffer = []
            continue

        # End-of-section markers
        if line.strip().startswith("---") and current_entry is not None:
            flush_entry()
            continue

        # Continuation lines inside an active field
        if current_field is not None and current_entry is not None:
            stripped = line.strip()
            if stripped and not stripped.startswith("**") and not stripped.startswith("#"):
                field_buffer.append(stripped)

    flush_category()

    total_entries = sum(len(c["entries"]) for c in categories)
    output = {
        "_meta": {
            "lastBuilt": dt.date.today().isoformat(),
            "source": "research-resources.md",
            "totalEntries": total_entries,
            "categoryCount": len(categories),
        },
        "categories": categories,
    }

    with open(OUTPUT_JSON, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote {OUTPUT_JSON}", file=sys.stderr)
    print(f"  {len(categories)} categories, {total_entries} entries total", file=sys.stderr)
    for c in categories:
        print(f"    {c['label']}: {len(c['entries'])} entries", file=sys.stderr)


if __name__ == "__main__":
    parse()
