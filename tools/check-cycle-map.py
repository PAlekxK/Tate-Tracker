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
              "fold-answer.py", "mom-cycle-status.py",
              # ⭐ `.js` ADDED 2026-08-24 (mom-cycle lap 5) — THE CONTROL HAD A
              # HOLE THE EXACT SHAPE OF THE THING IT GUARDS AGAINST.
              # Every glob above ends in `.py`, so a loop tool written in
              # JavaScript was invisible to it. `telemetry-walk.js` — Leg 6b's
              # walk, whose own header says "A leg of the mom-cycle, not a
              # calendar item" `[paul-stated 2026-08-08]` — is named NOWHERE in
              # MOM-CYCLE-MAP.md, and this check reported OK for 16 days.
              # A control that cannot see half the toolbox reports clean about
              # the half it can see, which reads as clean about all of it.
              # Globbed, not enumerated: a hand-kept list is the failure this
              # file exists to catch, and it had grown one in the file
              # extension.
              "*.js")

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

    # TRAJECTORY — every lap must record what it DECIDED and what that supersedes.
    # `[paul-stated 2026-08-04]`: "my intention is to help make sure that there's a
    # trajectory throughout these cycles, and not necessarily pinging back between two
    # different states without any self-awareness from cycle to cycle."
    #
    # Oscillation is the failure; volume is not. A loop that changes one thing five times
    # toward one end is healthy — a loop that flips the same thing twice WITHOUT NOTICING
    # is not, and the tell is the not-noticing. That cannot be a habit (this stack's own
    # rule: name the mechanism or drop the claim), so it is a required record shape:
    # a reversal becomes queryable instead of remembered.
    #
    # ⚠️ THIS CHECKS SHAPE, NOT TRAJECTORY. It cannot tell a principled reversal from a
    # flip-flop — it only guarantees the data a human (or a later detector) would need.
    # An actual oscillation detector needs >= 2 laps of history and does not exist yet.
    log_path = os.path.join(ROOT, "MOM-CYCLE-LOG.md")
    if os.path.exists(log_path):
        with open(log_path, encoding="utf-8") as f:
            log_text = f.read()
        laps = re.split(r"^## Lap ", log_text, flags=re.M)[1:]
        for lap in laps:
            title = lap.splitlines()[0].strip() if lap.splitlines() else "?"
            if not re.search(r"^###\s*Decisions\b", lap, flags=re.M):
                findings.append(
                    f"NO DECISIONS BLOCK  lap '{title}' records no Decisions section — "
                    f"what it changed and what that supersedes is unqueryable, so a later "
                    f"lap cannot tell a trajectory from a flip-flop")

    # ⭐ MAP ↔ PROCEDURE AGREEMENT (added 2026-08-04, the same day it broke).
    # The map is the DEFINITION; `~/.claude/skills/mom-cycle/SKILL.md` is the
    # PROCEDURE an agent actually loads when someone types /mom-cycle. On the day
    # the map gained three amendments the procedure gained none, and for hours it
    # still said "one seat by default" while the map said the opposite — so a lap
    # run from the Skill would have executed the OLD loop while the map documented
    # the new one.
    #
    # ⚠️ THEY LIVE IN DIFFERENT REPOS (`~/.claude` vs this one), which is precisely
    # how a scoped close-out updates one and not the other. Nothing structural stops
    # them drifting; this check is the only thing that does.
    #
    # It compares VOCABULARY, not prose — every amended leg name the map introduces
    # must appear somewhere in the procedure. It cannot tell whether the procedure
    # describes them CORRECTLY, and says so rather than implying coverage.
    skill = os.path.expanduser("~/.claude/skills/mom-cycle/SKILL.md")
    if os.path.exists(skill):
        with open(skill, encoding="utf-8") as f:
            proc = f.read()
        for token, why in (("PREVIEW", "leg 6a"), ("TELEMETRY", "leg 6b"),
                           ("PROXY", "leg 6c"), ("--retire", "leg 7's one-command retirement")):
            if token in map_text and token not in proc:
                findings.append(
                    f"MAP/PROCEDURE DRIFT  the map defines {token} ({why}) and "
                    f"SKILL.md never mentions it — an agent running /mom-cycle would "
                    f"execute a loop the map does not describe")
        # Check the FRONTMATTER description separately — it is what an agent reads
        # first and what the skill listing shows, and it drifted independently of
        # the body on 2026-08-04. Prose that QUOTES the superseded rule (a banner, a
        # `supersedes "…"` note) is legitimate history, so match the stale CLAIM in
        # the description rather than the phrase anywhere in the file.
        desc = next((l for l in proc.splitlines() if l.startswith("description:")), "")
        if "one expert seat" in desc:
            findings.append(
                "MAP/PROCEDURE DRIFT  SKILL.md's frontmatter description still promises "
                "'one expert seat' while the map carries an amended Leg 4 sequence — and "
                "the description is what the skill listing shows")
        leg4 = next((l for l in proc.splitlines() if l.startswith("## Leg 4")), "")
        if leg4 and "AMENDED" not in map_text.upper():
            pass
        elif leg4 and "SCOPED" not in leg4.upper() and "SEQUENCE" not in leg4.upper():
            findings.append(
                "MAP/PROCEDURE DRIFT  SKILL.md's Leg 4 heading does not describe a sequence "
                "while the map's Leg 4 is amended to one")
    else:
        findings.append(f"NO PROCEDURE  {skill} is missing — the map defines a loop nothing runs")

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
