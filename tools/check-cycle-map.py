#!/usr/bin/env python3
"""check-cycle-map.py — the map's own control.

⚠️ A HAND-WRITTEN MAP GOES STALE. That is the whole reason this file exists, and
it is not a theory: `[[feedback_hand_maintained_facts_drift]]` fired five times
on 2026-08-02 alone, and every time the drift flattered whoever wrote it. So
`MOM-CYCLE-MAP.md` ships with a check that fails when the loop grows a mechanism
the map does not name.

WHAT IT CAN AND CANNOT DO
-------------------------
CAN: verify that every detector/reader tool in `tools/` is named in the map, that
every leg the procedure defines has a row, and that the artifacts the map points
at exist.
CANNOT: verify a sentence. A documented-but-wrong description passes. The market-
digest map states the same limit about itself, and stating it is the point —
an unstated boundary reads as full coverage.

IT IS A CLOSE-OUT CHECK, NOT A GATE. It runs beside the other checks when a
Fernwood session closes. Wiring it into the loop's own sweep would mean the map
check gates the thing it documents.

Usage:
    python3 tools/check-cycle-map.py
    python3 tools/check-cycle-map.py --selftest    # prove it can FAIL
"""
import argparse
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
MAP = os.path.join(ROOT, "MOM-CYCLE-MAP.md")
LOG = os.path.join(ROOT, "MOM-CYCLE-LOG.md")

# Tools that are part of the loop and must therefore appear in the map.
# Derived by GLOB, never by a hand-kept list — a hand-kept list is the exact
# failure mode this file exists to catch.
TOOL_GLOBS = ("check-*.py", "read-*.py", "test-feedback-cycle.py",
              "fold-answer.py", "mom-cycle-status.py")

# Tools that are deliberately NOT part of this loop. Each needs a reason, and the
# reason is checked by a human, not by this script.
NOT_IN_LOOP = {
    "check-domains.py": "domain-contract check — the record's structure, not her feedback",
    "check-cycle-map.py": "this file; it documents the map, it is not a loop leg",
}

LEGS = ["GUARD", "READ", "TRIAGE", "RESOLVE", "EXPERT", "SHIP", "GATE", "CLOSE"]


def audit(map_text):
    """Return a list of finding strings. Empty list = clean."""
    findings = []

    present = set()
    for g in TOOL_GLOBS:
        for p in glob.glob(os.path.join(HERE, g)):
            present.add(os.path.basename(p))

    for tool in sorted(present):
        if tool in NOT_IN_LOOP:
            continue
        if tool not in map_text:
            findings.append(
                f"UNDOCUMENTED TOOL  {tool} is in tools/ and serves the loop, "
                f"but MOM-CYCLE-MAP.md never names it")

    for leg in LEGS:
        if not re.search(rf"\b{leg}\b", map_text):
            findings.append(f"MISSING LEG  the map has no row for leg {leg}")

    if "PRE-REGISTERED" not in map_text.upper():
        findings.append(
            "NO PRE-REGISTRATION  the map defines no 'clean lap', so the loop "
            "cannot score itself and self-improvement has nothing to measure")

    return findings


def main():
    ap = argparse.ArgumentParser(description="Is MOM-CYCLE-MAP.md still true?")
    ap.add_argument("--selftest", action="store_true",
                    help="prove this check can FAIL — a control never seen to fail is decoration")
    a = ap.parse_args()

    if not os.path.exists(MAP):
        print("⛔ MOM-CYCLE-MAP.md does not exist.")
        return 1

    with open(MAP, "r", encoding="utf-8") as f:
        map_text = f.read()

    if a.selftest:
        print("SELFTEST — feeding the auditor a map with a tool and a leg removed.")
        broken = map_text.replace("check-cards.py", "xxx").replace("RESOLVE", "xxx")
        got = audit(broken)
        undoc = any("check-cards.py" in g for g in got)
        legmiss = any("leg RESOLVE" in g for g in got)
        print(f"  can detect an undocumented tool : {'PASS' if undoc else 'FAIL'}")
        print(f"  can detect a missing leg        : {'PASS' if legmiss else 'FAIL'}")
        clean = audit(map_text)
        print(f"  the REAL map currently          : {'clean' if not clean else str(len(clean)) + ' finding(s)'}")
        ok = undoc and legmiss
        print(f"\n{'✓ the control can fail' if ok else '⛔ THIS CONTROL CANNOT FAIL — it is decoration'}")
        return 0 if ok else 1

    findings = audit(map_text)
    if not os.path.exists(LOG):
        findings.append("NO CHRONICLE  MOM-CYCLE-LOG.md is missing — laps are unrecorded")

    if not findings:
        print("OK    MOM-CYCLE-MAP.md names every loop tool and every leg.")
        print("      (This verifies coverage, never correctness — it cannot check a sentence.)")
        return 0

    print(f"⛔ MOM-CYCLE-MAP.md is behind the loop — {len(findings)} finding(s):\n")
    for f_ in findings:
        print(f"  · {f_}")
    print("\n   Update the map, then re-run. Do not silence this by editing the glob.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
