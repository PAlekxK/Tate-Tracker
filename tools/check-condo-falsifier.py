#!/usr/bin/env python3
"""check-condo-falsifier.py — can the engine render a PLANTLESS estate without a fork?

C7 step 2 / C4 step 5c. The "no garden" falsifier: build a second instance (the condo paper
model, sited in the private sibling) with the SAME engine, and prove nothing under engine/
had to change. If it cannot render, the engine/instance line is drawn wrong — stop,
re-classify, no repo moves (C4 5c's FAIL branch). A guard added under engine/ DURING the run
to make it render is a FAIL recorded as one, not a fix.

  python3 tools/check-condo-falsifier.py            # the full run — REFUSES until every precondition holds
  python3 tools/check-condo-falsifier.py --pre-read # the mechanical half that CAN run today (2b), labelled as such
  python3 tools/check-condo-falsifier.py --selftest

PRECONDITIONS (2a) — the harness refuses, exit 2, naming the first unmet one:
  · engine/ is tracked and non-empty        (C4 5b)   — otherwise "the diff under engine/ is empty" is vacuously true
  · tools/build-viewer.py exists            (C4 5b)
  · momlib.enabled_domains exists           (C5 3a)   — the module switch; without it "no Plants tile" is not testable
  · the condo instance exists in the sibling (C7 1a)

WHAT --pre-read PROVES, and what it does not: it builds the condo with declared absences,
asserts no unfilled placeholder, asserts engine/ unchanged before/after, and greps the built
file for Fernwood identity strings OUTSIDE the inlined consts. It does NOT assert the Plants
tile is absent — that is C5 3b's consumer behaviour and stays a named gap until it lands. The
2c boot read (414 × A+) is a Playwright step recorded in the plan, not run here.
"""
import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SIBLING = os.path.expanduser("~/Developer/fernwood-private")
CONDO = os.path.join(SIBLING, "instance-condo", "instance.json")
SCRATCH = os.environ.get("CONDO_SCRATCH", os.path.join(ROOT, ".private", "condo-falsifier"))
sys.path.insert(0, HERE)

# Fernwood identity strings that must NOT appear in the condo build outside the inlined consts
# (the seat's §1 list, as a grep set). Consts are stripped before the grep — they are instance
# data by construction and the condo's are empty/its own.
FERNWOOD_STRINGS = ["2,873", "2873 ft", "Jasper", "Church Mountain", "Tate Mountain", "Lake Sequoyah",
                    "Pickens", "Cherokee", "Bortle 3", "KJZP", "34.5496", "84.3674", "Blue Ridge", "Fernwood"]


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, cwd=ROOT)


def preconditions():
    unmet = []
    n = sh("git", "ls-files", "engine/").stdout.strip().split("\n")
    if not n or n == [""]:
        unmet.append("engine/ is empty or untracked (C4 5b)")
    if not os.path.exists(os.path.join(HERE, "build-viewer.py")):
        unmet.append("tools/build-viewer.py does not exist (C4 5b)")
    try:
        import momlib
        if not hasattr(momlib, "enabled_domains"):
            unmet.append("momlib.enabled_domains does not exist (C5 3a — the module switch)")
    except Exception as e:  # noqa: BLE001
        unmet.append("momlib import failed: %s" % e)
    if not os.path.exists(CONDO):
        unmet.append("the condo instance does not exist at %s (C7 1a)" % CONDO)
    return unmet


def strip_consts(html):
    return re.sub(r"^(?:const|let) [A-Z_]+_DATA = .*?;$", "", html, flags=re.M)


def engine_state():
    return (sh("git", "status", "--porcelain", "--", "engine/").stdout,
            sh("git", "diff", "--stat", "--", "engine/").stdout)


def pre_read():
    print("condo falsifier — PRE-READ (2b only; 2c/2d wait on C5 3a/3b)\n")
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + detail) if detail and not cond else ""))

    unmet = preconditions()
    hard = [u for u in unmet if "C5 3a" not in u]
    if hard:
        print("⛔ precondition unmet: %s" % hard[0]); return 2
    print("  · precondition deliberately waived for the pre-read: %s" % "; ".join(u for u in unmet if "C5 3a" in u))
    tracked = sh("git", "ls-files", "engine/").stdout.strip().split("\n")
    check("engine/ is tracked and non-empty (%d file(s)) — the diff below is not vacuous" % len(tracked), len(tracked) > 0)
    before = engine_state()
    os.makedirs(SCRATCH, exist_ok=True)
    out = os.path.join(SCRATCH, "condo.html")
    r = sh(sys.executable, os.path.join(HERE, "build-viewer.py"), "--instance", CONDO, "--out", out)
    check("build-viewer.py --instance <condo> exits 0", r.returncode == 0, (r.stdout + r.stderr)[-300:])
    if r.returncode != 0:
        return 1
    html = open(out, encoding="utf-8").read()
    check("no unfilled placeholder in the built file", "{{" not in html)
    after = engine_state()
    check("engine/ unchanged for the whole run (status + diff --stat identical before/after)", before == after and before[0] == "")
    outside = strip_consts(html)
    hits = {s: outside.count(s) for s in FERNWOOD_STRINGS if s in outside}
    check("Fernwood identity strings outside the inlined consts: 0 (%d string(s) checked)" % len(FERNWOOD_STRINGS),
          not hits, json.dumps(hits))
    if hits:
        print("       ↳ these are ENGINE-half literals naming the founding instance — the seat's P5/config-derivation finding, now measured on a second estate")
    absent = [c for c in re.findall(r'^(?:const|let) ([A-Z_]+_DATA) = \{"_meta": \{"declaredAbsent": true\}', html, re.M)]
    print("  · declared-absent consts in the build: %d — %s" % (len(absent), ", ".join(absent)))
    print("  · built: %s (%s bytes)" % (out, "{:,}".format(len(html))))
    print("\n  NOT proven here: the Plants tile absent (C5 3b) · the 414 × A+ boot read (2c, Playwright) · digest/signals (2d).")
    print("%s" % ("\n✅ pre-read holds — the engine BUILDS a plantless estate with no engine change." if ok else "\n🔴 pre-read failed — read the line above before touching engine/."))
    return 0 if ok else 1


def full():
    unmet = preconditions()
    if unmet:
        print("⛔ precondition unmet: %s" % unmet[0])
        for u in unmet[1:]:
            print("   also: %s" % u)
        print("   The falsifier does not run partially in full mode; use --pre-read for the mechanical half.")
        return 2
    print("all preconditions hold — the full run is not implemented yet (2c/2d land with C5 3a/3b)")
    return 1


def selftest():
    print("check-condo-falsifier selftest\n")
    ok = True
    unmet = preconditions()
    c5 = [u for u in unmet if "C5 3a" in u]
    print("  %s on today's tree the full run REFUSES on the C5 3a precondition (exit 2), never passes" % ("✅" if c5 else "🔴"))
    ok &= bool(c5)
    html = 'const PLANTS_DATA = {"x": "Jasper"};\n<h1>Fernwood</h1>\n'
    s = strip_consts(html)
    ok2 = "Jasper" not in s and "Fernwood" in s
    print("  %s the identity grep ignores inlined consts and sees the engine half" % ("✅" if ok2 else "🔴")); ok &= ok2
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pre-read", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.pre_read:
        return pre_read()
    return full()


if __name__ == "__main__":
    sys.exit(main())
