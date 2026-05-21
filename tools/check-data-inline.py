#!/usr/bin/env python3
"""
check-data-inline.py — verify that the *_DATA constants inlined in viewer.html
match their source JSON files.

The viewer reads PLANTS_DATA / MAMMALS_DATA / BIRDS_DATA / etc. as inlined
constants. The corresponding plants.json / mammals.json / birds.json files are
the source of truth. They MUST agree on the species set; if they drift, the
dashboard can render stale data (or worse, render a "ghost" entry that exists
in JSON but not in the inlined fallback, or vice versa).

This script:
- Reads each source JSON.
- Greps the matching const out of viewer.html.
- Compares the species id-sets + the count.
- Reports any drift with file paths + the missing/extra ids.

Exit code 0 → all in sync. Exit code 1 → drift detected.

Background — why this matters (2026-05-21 incident):
- Phase F Option C auto-promote committed plants.json + viewer.html + photo
  in 3 separate commits.
- A rebase conflict on viewer.html, resolved with `git checkout --theirs`
  during rebase (wrong direction — `--theirs` is incoming commits in rebase,
  not upstream), silently dropped the auto-promote's PLANTS_DATA re-inline.
- plants.json (commit A) still had the new entry; viewer.html (commit B
  dropped) lost it. Drift invisible until Playwright check tried to find
  the entry in PLANTS_DATA and failed.

Run before any commit that touches viewer.html or any *_DATA-source JSON,
and after any merge/rebase involving the auto-promote commits.

Usage:
    python3 tools/check-data-inline.py
    python3 tools/check-data-inline.py --fix    # re-inline missing/drifted consts via wire-photos.py
"""

import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VIEWER = os.path.join(ROOT, "viewer.html")

# Map (source JSON, inlined const name, species path).
# Mirrors the KIND_TARGETS in worker/worker.js + the CATEGORIES in
# tools/wire-photos.py. If you add a new species category, update all three.
SOURCES = [
    ("plants.json",     "PLANTS_DATA",     "plants",  "plants"),
    ("mammals.json",    "MAMMALS_DATA",    "species", "mammals"),
    ("birds.json",      "BIRDS_DATA",      "species", "birds"),
    ("amphibians.json", "AMPHIBIANS_DATA", "species", "amphibians"),
    ("snakes.json",     "SNAKES_DATA",     "species", "snakes"),
    ("lizards.json",    "LIZARDS_DATA",    "species", "lizards"),
    ("fishing.json",    "FISHING_DATA",    "species", "fishing"),
]


def get_inlined_const(html, const_name):
    """Extract the JSON literal assigned to `const <const_name> = {...};`."""
    pattern = re.compile(r"const " + re.escape(const_name) + r"\s*=\s*(\{.*?\});", re.DOTALL)
    m = pattern.search(html)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return {"_parse_error": str(e), "_excerpt": m.group(1)[:200]}


def species_ids(data, species_path):
    """Walk species_path into the data dict; return set of ids."""
    if not isinstance(data, dict):
        return set()
    node = data
    for part in species_path.split("."):
        if not isinstance(node, dict) or part not in node:
            return set()
        node = node[part]
    if not isinstance(node, list):
        return set()
    return {item.get("id") for item in node if isinstance(item, dict) and item.get("id")}


def check_all():
    if not os.path.isfile(VIEWER):
        print(f"ERROR: viewer.html not found at {VIEWER}", file=sys.stderr)
        return 2
    with open(VIEWER, "r", encoding="utf-8") as f:
        html = f.read()

    any_drift = False
    drift_categories = []
    for json_file, const_name, species_path, category in SOURCES:
        json_path = os.path.join(ROOT, json_file)
        if not os.path.isfile(json_path):
            print(f"  SKIP {const_name}: source JSON missing at {json_path}")
            continue
        with open(json_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        json_ids = species_ids(json_data, species_path)

        inlined = get_inlined_const(html, const_name)
        if inlined is None:
            print(f"  WARN {const_name}: const not found in viewer.html — source has {len(json_ids)} entries.")
            any_drift = True
            drift_categories.append(category)
            continue
        if isinstance(inlined, dict) and "_parse_error" in inlined:
            print(f"  ERROR {const_name}: inlined JSON failed to parse — {inlined['_parse_error']}")
            print(f"    Excerpt: {inlined['_excerpt']}")
            any_drift = True
            drift_categories.append(category)
            continue
        inlined_ids = species_ids(inlined, species_path)

        missing_in_inlined = json_ids - inlined_ids
        extra_in_inlined = inlined_ids - json_ids
        if missing_in_inlined or extra_in_inlined:
            any_drift = True
            drift_categories.append(category)
            print(f"  DRIFT {const_name}: source({len(json_ids)}) ≠ inlined({len(inlined_ids)})")
            if missing_in_inlined:
                print(f"    - missing from inlined PLANTS_DATA: {sorted(missing_in_inlined)}")
            if extra_in_inlined:
                print(f"    - extra in inlined (not in JSON): {sorted(extra_in_inlined)}")
        else:
            print(f"  OK    {const_name}: {len(json_ids)} entries, in sync.")

    if any_drift:
        print()
        print(f"DRIFT detected in {len(drift_categories)} categor{'y' if len(drift_categories) == 1 else 'ies'}: {', '.join(drift_categories)}")
        return 1, drift_categories
    return 0, []


def fix(drift_categories):
    """Run wire-photos.py for each drifted category to re-inline the const."""
    wire_script = os.path.join(ROOT, "tools", "wire-photos.py")
    if not os.path.isfile(wire_script):
        print(f"ERROR: wire-photos.py not found at {wire_script}", file=sys.stderr)
        return 2
    for cat in drift_categories:
        print(f"\n[fix] Re-inlining {cat}...")
        result = subprocess.run(
            ["python3", wire_script, "--category", cat],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"  FAILED: {result.stderr.strip()}")
            return 3
        print(f"  {result.stdout.strip()}")
    print()
    print("[fix] Re-running check to verify...")
    exit_code, _ = check_all()
    return exit_code


def main():
    ap = argparse.ArgumentParser(description="Verify inlined *_DATA consts match source JSONs.")
    ap.add_argument("--fix", action="store_true", help="If drift is detected, re-inline via wire-photos.py")
    args = ap.parse_args()

    exit_code, drift_categories = check_all()
    if exit_code == 0:
        print("\nAll data consts in sync with source JSONs.")
        return 0
    if not args.fix:
        print("\nRun with --fix to auto-re-inline the drifted constants.")
        return exit_code
    return fix(drift_categories)


if __name__ == "__main__":
    sys.exit(main())
