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

LITERAL_RE = re.compile(r'["\'`](tateTracker\.[A-Za-z0-9_.]+)["\'`]')
ROSTER_RE = re.compile(r'const STORAGE_KEYS = Object\.freeze\(\{(.*?)\}\);', re.S)


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
    unused = sorted(k for k in roster if k not in used)
    if not quiet:
        print("storage keys — %d rostered · %d distinct literals in use" % (len(roster), len(used)))
        if unused:
            print("  · rostered but no usage literal outside the roster: %s" % ", ".join(unused))
            print("    (not a failure — a key can be read through the roster object; it is a prompt to look)")
    if unrostered:
        print("  🔴 %d key(s) in use and NOT in STORAGE_KEYS:" % len(unrostered))
        for k, ln in sorted(unrostered.items(), key=lambda kv: kv[1]):
            print("       · %-52s first at viewer.html:%d" % (k, ln))
        print("     Add each to the roster (with its one-line purpose). A key the migration does")
        print("     not know about is a key she loses at the origin move.")
        return 1
    if not quiet:
        print("  ✅ every browser-storage literal is rostered.")
    return 0


def selftest(src):
    print("check-storage-keys selftest\n")
    ok = True
    rc = check(src, quiet=True)
    ok &= rc == 0
    print("  %s the live file passes (exit %d)" % ("✅" if rc == 0 else "🔴", rc))
    planted = src.replace("</script>", 'localStorage.getItem("tateTracker.plantedNineteenth.v1");\n</script>', 1)
    rc = check(planted, quiet=True)
    ok &= rc == 1
    print("  %s a planted, unrostered 19th key FAILS (exit %d)" % ("✅" if rc == 1 else "🔴", rc))
    rc = check(src.replace("const STORAGE_KEYS = Object.freeze({", "const STORAGE_KEYS_ = Object.freeze({", 1), quiet=True)
    ok &= rc == 2
    print("  %s a missing roster fails CLOSED (exit %d)" % ("✅" if rc == 2 else "🔴", rc))
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    with open(VIEWER, encoding="utf-8") as f:
        src = f.read()
    return selftest(src) if args.selftest else check(src)


if __name__ == "__main__":
    sys.exit(main())
