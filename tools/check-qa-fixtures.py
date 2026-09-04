#!/usr/bin/env python3
"""check-qa-fixtures.py — a QA fixture value must never reach a ref destined for Mom's page.
    python3 tools/check-qa-fixtures.py                      # list the register
    python3 tools/check-qa-fixtures.py --check --ref origin/main   # red if any row's qaValue is present at that ref
    python3 tools/check-qa-fixtures.py --check --ref HEAD --branch main   # CI form: only enforces when the branch is main
Engineering seat, 2026-09-04 (.engineering/2026-09-04-qa-instance-overlay.md): the divergence mechanism is the `staging`
branch; QA-only values are committed straight into the instance file there; this register names each one and this check
catches a merge, a cherry-pick and the migration with one predicate. Fails CLOSED on a missing register.
"""
import argparse, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
REG = os.path.join(HERE, "qa-fixtures.json")

def at(ref, file, path):
    r = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (ref, file)], capture_output=True, text=True)
    if r.returncode: return ("<missing file>",)
    cur = json.loads(r.stdout)
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur: return ("<missing key>",)
        cur = cur[part]
    return (cur,)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); ap.add_argument("--ref", default="origin/main"); ap.add_argument("--branch", default=None)
    a = ap.parse_args()
    if not os.path.exists(REG): print("⛔ tools/qa-fixtures.json is missing — failing closed"); return 3
    rows = json.load(open(REG))["rows"]
    enforce = not a.branch or a.branch in ("main", "prod")
    print("qa-fixtures — %d registered QA-only value(s)%s" % (len(rows), "" if a.check else ""))
    for r in rows: print("  %s %s  qa=%r prod=%r  · %s · retired by %s" % (r["file"], r["path"], r["qaValue"], r["prodValue"], r["why"], r["retiredBy"]))
    if not a.check: return 0
    if not enforce: print("  (branch %s: fixtures allowed here)" % a.branch); return 0
    bad = [r for r in rows if at(a.ref, r["file"], r["path"])[0] == r["qaValue"]]
    if bad:
        print("🔴 %d QA fixture value(s) present at %s — a fixture is about to reach Mom's page: %s" % (len(bad), a.ref, ", ".join("%s:%s" % (r["file"], r["path"]) for r in bad))); return 1
    print("✅ no QA fixture value at %s" % a.ref); return 0

if __name__ == "__main__":
    sys.exit(main())
