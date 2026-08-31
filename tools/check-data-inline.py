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
- Compares the species id-sets + the count (STRUCTURE drift).
- Deep-compares the full parsed structures (CONTENT drift) — so an edit to an
  existing entry's fields (flip a confidence, correct a variety, edit a note)
  is caught, not just added/removed entries. Parsed compare, never text: the
  inline is minified and the source is indent=2, so a text diff would
  false-positive on formatting every run.
- Reports any drift with file paths + the missing/extra ids or differing paths.

Exit code 0 → all in sync. Exit code 1 → drift detected.

Content-blindness fix (2026-07-14): the check previously reduced each entry to
its `id` and diffed id-sets only — so a field edit to an entry whose id didn't
change read as "in sync," and `--fix` was a no-op. That is exactly the mutation
every Mama's-Perspective fold produces, so silent dashboard staleness was the
default. Now the check deep-compares content and `--fix` re-inlines the whole
const via the side-effect-free tools/reinline.py.

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
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reinline  # noqa: E402  — shared side-effect-free re-inline path

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VIEWER = os.path.join(ROOT, "viewer.html")

# Map (source JSON, inlined const name, species path).
# Mirrors the KIND_TARGETS in worker/worker.js + the CATEGORIES in
# tools/wire-photos.py. If you add a new species category, update all three.
SOURCES = [
    ("plants.json",     "PLANTS_DATA",     "plants",   "plants"),
    ("mammals.json",    "MAMMALS_DATA",    "species",  "mammals"),
    ("birds.json",      "BIRDS_DATA",      "species",  "birds"),
    ("amphibians.json", "AMPHIBIANS_DATA", "species",  "amphibians"),
    ("snakes.json",     "SNAKES_DATA",     "species",  "snakes"),
    ("lizards.json",    "LIZARDS_DATA",    "species",  "lizards"),
    ("fishing.json",    "FISHING_DATA",    "species",  "fishing"),
    ("vehicles.json",   "VEHICLES_DATA",   "vehicles", "vehicles"),
    # Added 2026-07-16: ZONES_DATA was the only re-inlined const with no drift alarm.
    # It matters more than most now — since schema v2 its _meta carries the BASEMAP
    # GEOREFERENCE (bounds + image dimensions), so a stale inline doesn't just show
    # old data, it projects every zone against the wrong picture.
    ("zones.json",      "ZONES_DATA",      "zones",    "zones"),
    # Added 2026-07-20 with the Weeds card — inferred weed reads, settled via Mom.
    ("weeds.json",      "WEEDS_DATA",      "weeds",    "weeds"),
    # Added 2026-08-31 (ux-sweep follow-up): TURF_DATA was the one re-inlined
    # const the checker could not see — a turf.json edit would silently never ship.
    ("turf.json",       "TURF_DATA",       "sources",  "turf"),

    # Added 2026-08-15 with the Insect Sounds tab. Nothing fetches insects.json at
    # runtime, so this const IS the app for that domain — the usual case, not the
    # exception (17 of 21 JSONs work this way).
    ("insects.json",    "INSECTS_DATA",    "species",  "insects"),
]

# Cap on how many differing paths to print per const (keep output legible).
MAX_DIFFS_SHOWN = 12


def _short(v):
    """One-line, length-capped repr of a value for drift output."""
    s = json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v
    s = s.replace("\n", " ")
    return s if len(s) <= 80 else s[:77] + "…"


def deep_diff(inlined, source, path=""):
    """Yield (path, inlined_value, source_value) where the two parsed structures
    differ. Order-sensitive for lists (re-inline preserves source order). Ints and
    floats that are numerically equal are treated as equal."""
    diffs = []
    if isinstance(inlined, bool) or isinstance(source, bool):
        if inlined is not source:
            diffs.append((path or "(root)", inlined, source))
        return diffs
    if isinstance(inlined, (int, float)) and isinstance(source, (int, float)):
        if inlined != source:
            diffs.append((path or "(root)", inlined, source))
        return diffs
    if type(inlined) is not type(source):
        diffs.append((path or "(root)", inlined, source))
        return diffs
    if isinstance(inlined, dict):
        for k in sorted(set(inlined) | set(source), key=str):
            kp = f"{path}.{k}" if path else k
            if k not in inlined:
                diffs.append((kp, "(absent in inlined)", source[k]))
            elif k not in source:
                diffs.append((kp, inlined[k], "(absent in source)"))
            else:
                diffs.extend(deep_diff(inlined[k], source[k], kp))
    elif isinstance(inlined, list):
        if len(inlined) != len(source):
            diffs.append((f"{path}[length]", len(inlined), len(source)))
        for i in range(min(len(inlined), len(source))):
            diffs.extend(deep_diff(inlined[i], source[i], f"{path}[{i}]"))
    else:
        if inlined != source:
            diffs.append((path or "(root)", inlined, source))
    return diffs


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
            print(f"  DRIFT {const_name}: source({len(json_ids)}) ≠ inlined({len(inlined_ids)}) — STRUCTURE")
            if missing_in_inlined:
                print(f"    - missing from inlined {const_name}: {sorted(missing_in_inlined)}")
            if extra_in_inlined:
                print(f"    - extra in inlined (not in JSON): {sorted(extra_in_inlined)}")
            continue
        # Same entry set — now check CONTENT (the drift the id-set compare is blind to).
        content_diffs = deep_diff(inlined, json_data)
        if content_diffs:
            any_drift = True
            drift_categories.append(category)
            print(f"  DRIFT {const_name}: {len(content_diffs)} field(s) differ — CONTENT (inlined ≠ source)")
            for p, iv, sv in content_diffs[:MAX_DIFFS_SHOWN]:
                print(f"    - {p}:  inlined={_short(iv)}  →  source={_short(sv)}")
            if len(content_diffs) > MAX_DIFFS_SHOWN:
                print(f"    … and {len(content_diffs) - MAX_DIFFS_SHOWN} more")
        else:
            print(f"  OK    {const_name}: {len(json_ids)} entries, content in sync.")

    if any_drift:
        print()
        print(f"DRIFT detected in {len(drift_categories)} categor{'y' if len(drift_categories) == 1 else 'ies'}: {', '.join(drift_categories)}")
        return 1, drift_categories
    return 0, []


def fix(drift_categories):
    """Re-inline each drifted category's const directly from its source JSON via
    the side-effect-free reinline module (no attribution merge, no source rewrite,
    unlike wire-photos.py). This repairs CONTENT drift, which the old wire-photos
    path never reached because it was only ever called on structure drift."""
    const_by_category = {cat: (jf, cn) for jf, cn, _sp, cat in SOURCES}
    for cat in drift_categories:
        jf, const_name = const_by_category[cat]
        json_path = os.path.join(ROOT, jf)
        print(f"\n[fix] Re-inlining {const_name} from {jf} …")
        reinline.reinline_from_source(VIEWER, const_name, json_path)
        print("  done.")
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
