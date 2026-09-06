#!/usr/bin/env python3
"""check-storage-keys.py — every browser-storage key the viewer touches is in the roster.

C4 step 2b (.plans/2026-09-03-c4-environments-PLAN.md). Storage is per ORIGIN. The
origin move (custom domain) strands every `tateTracker.*` key on her phone unless a
one-time migration carries it, and a migration can only carry keys it knows about.
So `viewer.html` declares `STORAGE_KEYS` once, and this check scans the whole file for
`"tateTracker.` literals and FAILS on any that the roster does not name — the same
shape as check-live.py's FETCH_RE drift guard: a hand-kept list rots the moment someone
adds a key, and the guard is what stops it rotting silently.

  python3 tools/check-storage-keys.py            # exit 0 = every literal is rostered
  python3 tools/check-storage-keys.py --selftest # plants a 19th key in memory; must FAIL

It flags; it never edits. Exit 1 lists the unrostered keys and the line each first appears on.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIEWER = os.path.join(ROOT, "viewer.html")
# ⛔ THIS CHECK WAS GREEN OVER A SURFACE IT DOES NOT SCAN. It read viewer.html ONLY, and matched
# literals shaped `tateTracker.*` — so the eight `fw-*` keys in onboarding/ and estate/ were
# invisible to it TWICE OVER (wrong file, wrong prefix) and it printed ✅ anyway. Found by
# engineering-partner 2026-09-06, after this session had run it three times and read its green as
# covering keys it had just added.
# ⚠️ Those are precisely the keys that now travel to a SECOND HOUSEHOLD's origin, and this file's
# own reason for existing is "a key the origin-move migration does not know about is a key she
# loses". It was blind in exactly the place it was written to see.
# ⭐ onboarding/index.html is the canonical DECLARER — `var K_x = "fw-…"` — so the declarations are
# the roster and nothing new has to be hand-maintained. estate/ may only READ what onboarding
# declares; a key it reads that nothing writes is the near-miss this leg exists to catch.
ONBOARDING = os.path.join(ROOT, "onboarding", "index.html")
# ⛔ DISCOVERED, NOT LISTED — and this is the second time today the same blind spot bit. The leg was
# added this morning naming onboarding/ and estate/ by hand; `homes/` shipped hours later and was
# invisible to it, exactly as the ten fw-* keys had been invisible to the viewer-only scan it was
# added to fix. A named list of surfaces is a roster that rots the next time a surface is added, so
# the household surfaces are now FOUND: every index.html outside the build artefacts.
def household_surfaces(root=ROOT):
    import glob as _g
    out = []
    # ⛔ RECURSIVE, AND THAT WAS THE THIRD MISS OF THE DAY. A one-level glob found onboarding/,
    # estate/ and homes/ and silently skipped settings/place/ and settings/account/ — built minutes
    # after it. The morning's version scanned only viewer.html; the noon version named two files by
    # hand; this one looked one directory deep. Each fix was correct about the instance it was
    # written for and wrong about the shape, which is why the depth is now unbounded.
    for d in sorted(_g.glob(os.path.join(root, "**", "index.html"), recursive=True)):
        rel = os.path.relpath(d, root)
        if rel.split(os.sep)[0] in ("node_modules", "engine", "tools", "guides", "worker"):
            continue
        out.append(d)
    return out
FW_DECL_RE = re.compile(r'var\s+K_[A-Z]+\s*=\s*["\'`](fw-[A-Za-z0-9_.-]+)["\'`]')
FW_LIT_RE = re.compile(r'["\'`](fw-[A-Za-z0-9_.-]+)["\'`]')

LITERAL_RE = re.compile(r'["\'`](tateTracker\.[A-Za-z0-9_.]+)["\'`]')
ROSTER_RE = re.compile(r'const STORAGE_KEYS = Object\.freeze\(\{(.*?)\}\);', re.S)
# C4 2b — the roster names which keys hold PER-ESTATE state; every usage of one of those literals must pass through
# estateKey(), which inserts ESTATE_ID. A bare use is the exact defect (her answers at one estate shown at another).
PER_ESTATE_RE = re.compile(r'const STORAGE_KEYS_PER_ESTATE = Object\.freeze\(\[(.*?)\]\);', re.S)
NAME_RE = re.compile(r'^\s*([A-Za-z0-9_]+):\s*["\'`](tateTracker\.[A-Za-z0-9_.]+)["\'`]', re.M)


def roster_and_literals(src):
    m = ROSTER_RE.search(src)
    if not m:
        return None, None, None
    roster = set(LITERAL_RE.findall(m.group(1)))
    # literals OUTSIDE the roster block, with the first line each appears on
    before, after = src[:m.start()], src[m.end():]
    seen = {}
    for chunk, offset in ((before, 0), (after, src[:m.end()].count("\n"))):
        for mm in LITERAL_RE.finditer(chunk):
            key = mm.group(1)
            if key not in seen:
                seen[key] = offset + chunk[:mm.start()].count("\n") + 1
    return roster, seen, m


def check(src, quiet=False):
    roster, used, _ = roster_and_literals(src)
    if roster is None:
        print("⛔ STORAGE_KEYS roster not found in viewer.html — the guard has nothing to guard.")
        return 2
    unrostered = {k: ln for k, ln in used.items() if k not in roster}
    # per-estate keys: every usage literal outside the roster must be wrapped as estateKey("…")
    bare = {}
    pm = PER_ESTATE_RE.search(src)
    if pm:
        names = set(re.findall(r'["\'`]([A-Za-z0-9_]+)["\'`]', pm.group(1)))
        by_name = dict(NAME_RE.findall(_.group(1))) if (_ := ROSTER_RE.search(src)) else {}
        outside = src[:_.start()] + src[_.end():]
        for name in sorted(names):
            lit = by_name.get(name)
            if not lit:
                bare[name] = "named in STORAGE_KEYS_PER_ESTATE but not in STORAGE_KEYS"; continue
            for mm in re.finditer(r'["\'`]' + re.escape(lit) + r'["\'`]', outside):
                pre = outside[max(0, mm.start() - 12):mm.start()]
                if not pre.endswith("estateKey("):
                    bare[lit] = "used bare (not estateKey(…)) at viewer.html:%d" % (outside[:mm.start()].count("\n") + 1 + (1 if mm.start() >= _.start() else 0))
    unused = sorted(k for k in roster if k not in used)
    declared, hh = check_household_keys()
    if not quiet:
        print("household keys — %d declared, %d surface(s) scanned"
              % (len(declared), len(household_surfaces())))
        for problem in hh:
            print("  🔴 " + problem)
        if not hh and declared:
            print("  ✅ every fw-* key both surfaces touch is declared by onboarding.")
        print()
        print("storage keys — %d rostered · %d distinct literals in use" % (len(roster), len(used)))
        if unused:
            print("  · rostered but no usage literal outside the roster: %s" % ", ".join(unused))
            print("    (not a failure — a key can be read through the roster object; it is a prompt to look)")
    if not quiet and pm:
        print("  · %d per-estate key(s) declared (STORAGE_KEYS_PER_ESTATE); every use wrapped in estateKey(): %s" % (len(re.findall(r'["\'`]([A-Za-z0-9_]+)["\'`]', pm.group(1))), "no" if bare else "yes"))
    if bare:
        print("  🔴 per-estate key(s) used BARE — her answers at one estate would show at another:")
        for k, why in bare.items():
            print("       · %-52s %s" % (k, why))
        if not unrostered:
            return 1
    if unrostered:
        print("  🔴 %d key(s) in use and NOT in STORAGE_KEYS:" % len(unrostered))
        for k, ln in sorted(unrostered.items(), key=lambda kv: kv[1]):
            print("       · %-52s first at viewer.html:%d" % (k, ln))
        print("     Add each to the roster (with its one-line purpose). A key the migration does")
        print("     not know about is a key she loses at the origin move.")
        return 1
    if not quiet:
        print("  ✅ every browser-storage literal is rostered.")
    # ⛔ A CHECK THAT PRINTS RED AND EXITS 0 IS NOT A CHECK. The household leg was added and
    # mutation-tested the same hour: it correctly printed 🔴 for a key `estate/` reads that
    # onboarding never declares — and returned 0, so every caller would have read it as clean. That
    # is the exact shape practice-steward flagged in check-backlog-ready this morning (123 flags,
    # exit 0), reproduced within the hour by the session that had just read the finding.
    if hh:
        return 1
    return 0


def selftest(src):
    print("check-storage-keys selftest\n")
    ok = True
    rc = check(src, quiet=True)
    ok &= rc == 0
    print("  %s the live file passes (exit %d)" % ("✅" if rc == 0 else "🔴", rc))
    bare = src.replace("</script>", 'localStorage.getItem("tateTracker.momQueue.answered.v1");\n</script>', 1)
    rc = check(bare, quiet=True)
    ok &= rc == 1
    print("  %s a BARE use of a per-estate key FAILS (exit %d)" % ("✅" if rc == 1 else "🔴", rc))
    planted = src.replace("</script>", 'localStorage.getItem("tateTracker.plantedNineteenth.v1");\n</script>', 1)
    rc = check(planted, quiet=True)
    ok &= rc == 1
    print("  %s a planted, unrostered 19th key FAILS (exit %d)" % ("✅" if rc == 1 else "🔴", rc))
    rc = check(src.replace("const STORAGE_KEYS = Object.freeze({", "const STORAGE_KEYS_ = Object.freeze({", 1), quiet=True)
    ok &= rc == 2
    print("  %s a missing roster fails CLOSED (exit %d)" % ("✅" if rc == 2 else "🔴", rc))
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


def check_household_keys():
    """→ (declared, problems). The onboarding flow's own keys, which viewer.html never sees."""
    problems = []
    try:
        onb = open(ONBOARDING, encoding="utf-8").read()
        surfaces = [(os.path.relpath(f, ROOT), open(f, encoding="utf-8").read())
                    for f in household_surfaces()]
    except OSError as e:
        return set(), ["UNCHECKABLE — %s" % e]
    if not surfaces:
        return set(), ["UNCHECKABLE — no household surfaces found; a scan that finds nothing "
                       "must never read as clean"]
    declared = set(FW_DECL_RE.findall(onb))
    if not declared:
        return set(), ["UNCHECKABLE — no `var K_x = \"fw-…\"` declarations found in onboarding; "
                       "the roster is derived from them, so finding none is not a pass"]
    for name, src in surfaces:
        for lit in sorted(set(FW_LIT_RE.findall(src))):
            if lit not in declared:
                problems.append("%s uses %r, which onboarding never declares" % (name, lit))
        # ⛔ AND EVERY K_* IDENTIFIER MUST BE DECLARED IN THE FILE THAT USES IT. A key can be
        # correctly rostered and still crash: on 2026-09-06 estate/ referenced `K_RANK`, which only
        # onboarding declares, inside a promise — so it threw a ReferenceError that its own .catch()
        # swallowed, and the reconcile silently did nothing. The literal was rostered; the NAME was
        # not in scope. Second undefined-name defect of the day (the first hoisted a `describe`
        # helper below the loop that used it), which is enough to be a shape rather than bad luck.
        # ⚠️ Comments are stripped first — a constant named while EXPLAINING something is not a use.
        body = re.sub(r"<!--.*?-->", " ", src, flags=re.S)
        body = re.sub(r"(?m)//.*$", " ", body)
        body = re.sub(r"/\*.*?\*/", " ", body, flags=re.S)
        here = set(re.findall(r'\bvar\s+(K_[A-Z_]+)\s*=', body)) | set(
            re.findall(r',\s*(K_[A-Z_]+)\s*=', body))
        for ident in sorted(set(re.findall(r'\b(K_[A-Z_]+)\b', body))):
            if ident not in here:
                problems.append("%s references %s, which it never declares — a ReferenceError a "
                                "surrounding .catch() will hide" % (name, ident))
    return declared, problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    with open(VIEWER, encoding="utf-8") as f:
        src = f.read()
    return selftest(src) if args.selftest else check(src)


if __name__ == "__main__":
    sys.exit(main())
