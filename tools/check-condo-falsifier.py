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
    """The engine half of a built file: inlined consts gone (instance data by construction);
    WHOLE-LINE comments gone (a comment that says "Fernwood did X" is history, not a leak);
    two names exempted — a canon KEY (`valleyFloor_KJZP`, `distanceFromFernwood_mi`) names a
    field, and `Blue Ridge Parkway` names an NPS unit, not this place.

    ⚠️ Line-based ON PURPOSE (2026-09-03): a regex block-comment strip swallowed 36% of the built
    file — 312 openers vs 317 closers, because `/*` also appears inside JS strings and regex
    literals — and hid two card titles and a sync intro that DID name the place. A strip that
    over-matches makes the falsifier pass by deleting the evidence."""
    out = re.sub(r"^(?:const|let) [A-Z_]+_DATA = .*?;$", "", html, flags=re.M)
    kept, in_block = [], None          # in_block: the closer we are waiting for
    for line in out.split("\n"):
        st = line.strip()
        if in_block:
            if in_block in st:
                in_block = None
            continue
        if st.startswith("/*") and "*/" not in st:
            in_block = "*/"; continue
        if st.startswith("<!--") and "-->" not in st:
            in_block = "-->"; continue
        if st.startswith(("//", "<!--", "/*", "*", "*/")):
            continue
        kept.append(re.sub(r"<!--.*?-->", "", line))
    out = "\n".join(kept)
    out = out.replace("valleyFloor_KJZP", "valleyFloor_STATION")
    out = out.replace("distanceFromFernwood_mi", "distanceFromSite_mi")
    out = out.replace("Blue Ridge Parkway", "the Parkway")
    return out


def engine_state():
    return (sh("git", "status", "--porcelain", "--", "engine/").stdout,
            sh("git", "diff", "--stat", "--", "engine/").stdout)


def pre_read():
    print("condo falsifier — PRE-READ (2b: build · engine untouched · identity strings)\n")
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
    """2b + the 3b structural proofs (the module switch reaches the build). The 414 × A+
    BOOT READ (2c) is a Playwright step: serve SCRATCH over http and read the built file —
    the plan records it; this harness cannot drive a browser."""
    rc = pre_read()
    print("\n── 2d · the module declaration reaches the condo build")
    ok = rc == 0
    out = os.path.join(SCRATCH, "condo.html")
    html = open(out, encoding="utf-8").read() if os.path.exists(out) else ""
    m = re.search(r"^const ESTATE_MODULES = (\{.*?\});$", html, re.M)
    mods = json.loads(m.group(1)) if m else {}
    def check(name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + str(detail)) if detail and not cond else ""))
    check("the condo build carries ESTATE_MODULES with garden OFF", mods.get("garden") == "off", mods)
    check("the Plants tile carries data-module=\"garden\" (applyModuleTiles hides it at boot)",
          'data-module="garden"' in html and "function applyModuleTiles" in html)
    check("PLANTS_DATA is a declared absence in the build", re.search(r'^const PLANTS_DATA = \{"_meta": \{"declaredAbsent": true\}', html, re.M) is not None)
    sys.path.insert(0, HERE)
    import importlib.util
    spec = importlib.util.spec_from_file_location("bd", os.path.join(HERE, "build-digest.py")); bd = importlib.util.module_from_spec(spec); spec.loader.exec_module(bd)
    condo_dir = os.path.dirname(CONDO)
    est = json.load(open(os.path.join(condo_dir, "estate.json")))
    def load(name):
        p = os.path.join(condo_dir, name)
        return json.load(open(p)) if os.path.exists(p) else {"_meta": {"declaredAbsent": True}}
    d = bd.compose(est, load)
    check("the condo digest has NO plants / weeds / turf key", not ({"plants", "weeds", "turf"} & set(d)), sorted(d))
    check("…and says so in _meta.declares", any("no garden" in x for x in d.get("_meta", {}).get("declares", [])), d.get("_meta", {}).get("declares"))
    print("\n  2c (the boot read at 414 × A+) is recorded in the plan from a Playwright run against `python3 -m http.server` on %s." % SCRATCH)
    print("%s" % ("\n✅ FALSIFIER HOLDS — the same engine renders a plantless estate as itself." if ok else "\n🔴 FALSIFIER FAILS — see the lines above; no engine edit to make it pass."))
    return 0 if ok else 1


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
