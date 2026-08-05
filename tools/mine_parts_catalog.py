#!/usr/bin/env python3
"""Mine a parts catalogue's text extraction for parts that FIT ONE TRUCK.

The problem this exists to solve: `grep -i tailgate` on the LMC FD.88 text
returns 187 hits, and **most of them do not fit Bolores.** The catalogue covers
Ford Truck AND Bronco 1980-96, so the overwhelming majority of tailgate parts are
STYLESIDE / F-SERIES pickup tailgates — a completely different assembly from the
Bronco's power-window tailgate. A raw keyword count reads like a rich seam and is
mostly a different vehicle.

So the filter is the product, not the search. Two gates, both from the part row
itself:

  1. FITMENT — the application field must name BRONCO, or be universal (no
     vehicle named at all). A row naming F-SERIES / STYLESIDE / F100 / F150 and
     NOT Bronco is excluded and COUNTED, so the exclusion is visible rather than
     silent.
  2. YEAR — the model-year range must cover the truck's year. '80-86' is out;
     '87-96' is in. Ranges are 2-digit and never cross 1999 in this catalogue.

⚠️ WHAT THIS IS NOT: a fitment guarantee. It is a SHORTLIST that turns a 180-page
catalogue into a page of candidates. LMC's own application data is the authority
and it is abbreviated here to a few characters; the ⚠️ 2026-08-03 price warning
on this catalogue applies to every figure printed below (prices expired
2026-08-03 — part numbers and applications stay good, treat prices as
approximate). Confirm before ordering.

    python3 tools/mine_parts_catalog.py --topic tailgate
    python3 tools/mine_parts_catalog.py --list-topics
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CATALOG = REPO / "manuals" / "text" / "bronco-1989-lmc-catalog-fd88.txt"

TRUCK_YEAR = 89  # 1989 Bronco, built 10/88

# A part row: number, description, application+years, optional qty, price.
PART_RE = re.compile(
    r"(?P<num>\d{2}-\d{4}(?:-[A-Z]{1,2})?)\s+"
    r"(?P<rest>.+?)"
    r"(?P<price>\$[\d,]+\.\d{2})"
)
YEAR_RE = re.compile(r"\b(\d{2})-(\d{2})\b")

# Vehicles that are NOT this truck. Presence of one of these WITHOUT 'BRONCO'
# means the row is for a pickup and is excluded.
OTHER_VEHICLE = re.compile(r"\b(F-?SERIES|STYLESIDE|FLARESIDE|F100|F150|F250|F350|SHORTBED|LONGBED)\b", re.I)
BRONCO = re.compile(r"\bBRONCO\b", re.I)

TOPICS = {
    "tailgate":     [r"TAILGATE"],
    "tire-carrier": [r"TIRE CARRIER", r"SPARE TIRE"],
    "body-mount":   [r"BODY MOUNT", r"CAB MOUNT", r"RADIATOR CORE MOUNT"],
    "door-panel":   [r"DOOR PANEL", r"PANEL-DOOR", r"ARM REST", r"ARMREST"],
    "hinge":        [r"HINGE"],
    "carpet":       [r"CARPET", r"FLOOR MAT"],
    "weatherstrip": [r"WEATHERSTRIP", r"WEATHER STRIP", r"SEAL-DOOR", r"DOOR SEAL"],
    "glass":        [r"GLASS", r"WINDOW REGULATOR", r"WINDOW MOTOR"],
    "rocker":       [r"ROCKER PANEL", r"CAB CORNER", r"BEDSIDE", r"WHEEL ARCH", r"FENDER"],
}


def year_ok(text: str, year: int) -> bool | None:
    """True if a year range covers `year`; None if no range found (universal)."""
    spans = YEAR_RE.findall(text)
    if not spans:
        return None
    for lo, hi in spans:
        lo_i, hi_i = int(lo), int(hi)
        # 2-digit, all 1980-1996 in this catalogue; no century wrap to handle.
        if lo_i <= year <= hi_i:
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", default=str(CATALOG))
    ap.add_argument("--topic", action="append", help="topic key (repeatable); default = all")
    ap.add_argument("--year", type=int, default=TRUCK_YEAR)
    ap.add_argument("--list-topics", action="store_true")
    ap.add_argument("--show-excluded", action="store_true", help="also print the rows filtered out")
    args = ap.parse_args()

    if args.list_topics:
        for k, pats in TOPICS.items():
            print(f"  {k:<14} {', '.join(pats)}")
        return 0

    path = Path(args.catalog)
    if not path.exists():
        print(f"catalogue text not found: {path}", file=sys.stderr)
        return 2
    text = path.read_text(encoding="utf-8", errors="replace")

    topics = args.topic or list(TOPICS)
    print(f"mine_parts_catalog — {path.name}, fitment year 19{args.year}\n")

    grand_fit = grand_wrong_vehicle = grand_wrong_year = 0

    for topic in topics:
        if topic not in TOPICS:
            print(f"unknown topic: {topic}", file=sys.stderr)
            return 2
        pats = [re.compile(p, re.I) for p in TOPICS[topic]]

        fits, wrong_vehicle, wrong_year = [], [], []
        seen = set()

        for line in text.splitlines():
            if not any(p.search(line) for p in pats):
                continue
            for m in PART_RE.finditer(line):
                num, rest, price = m.group("num"), m.group("rest"), m.group("price")
                blob = f"{num} {rest}"
                if not any(p.search(blob) for p in pats):
                    continue  # keyword was elsewhere on a multi-column line
                if num in seen:
                    continue
                seen.add(num)
                desc = " ".join(rest.split())
                row = (num, desc, price)

                is_bronco = bool(BRONCO.search(rest))
                is_other = bool(OTHER_VEHICLE.search(rest))
                if is_other and not is_bronco:
                    wrong_vehicle.append(row)
                    continue
                yr = year_ok(rest, args.year)
                if yr is False:
                    wrong_year.append(row)
                    continue
                fits.append(row + (("universal/undated" if yr is None else ""),))

        grand_fit += len(fits)
        grand_wrong_vehicle += len(wrong_vehicle)
        grand_wrong_year += len(wrong_year)

        print(f"── {topic.upper()}  —  {len(fits)} candidate(s)")
        if not fits:
            print("     (none fit)")
        for num, desc, price, note in sorted(fits):
            flag = f"   [{note}]" if note else ""
            print(f"     {num:<12} {desc[:66]:<66} {price:>10}{flag}")
        print(f"     filtered out: {len(wrong_vehicle)} wrong vehicle · {len(wrong_year)} wrong year")
        if args.show_excluded:
            for num, desc, price in sorted(wrong_vehicle + wrong_year):
                print(f"       ✗ {num:<12} {desc[:60]}")
        print()

    total = grand_fit + grand_wrong_vehicle + grand_wrong_year
    print("── COVERAGE")
    print(f"   {total} keyword-matched part rows examined across {len(topics)} topic(s)")
    print(f"   {grand_fit} fit · {grand_wrong_vehicle} wrong vehicle · {grand_wrong_year} wrong year")
    print("   ⚠️ A SHORTLIST, NOT A FITMENT GUARANTEE — LMC's application data is the")
    print("      authority and is abbreviated to a few characters in this text. Prices")
    print("      expired 2026-08-03; part numbers and applications stay good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
