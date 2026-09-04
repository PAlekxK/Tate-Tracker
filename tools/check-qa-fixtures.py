#!/usr/bin/env python3
"""check-qa-fixtures.py — a QA-only value is marked INLINE and must never reach a ref destined for Mom's page.
    python3 tools/check-qa-fixtures.py                          # list the `_qaFixture` markers in instance/*.json at HEAD
    python3 tools/check-qa-fixtures.py --check --ref origin/main
    python3 tools/check-qa-fixtures.py --check --ref HEAD --branch main   # CI form: enforces only when the branch is main/prod
Engineering seat, 2026-09-04 (.engineering/2026-09-04-qa-instance-overlay.md, re-answer under the freeze): `staging` is
main-in-waiting, so a QA-only value is declared NEXT TO ITSELF — `"vault": {"rooms": ["qa-contacts"], "_qaFixture": "C6 5c
retires this"}` — and the migration checklist is "remove every `_qaFixture`, rebuild, QA verifies, fast-forward". This check
is the grep: any `_qaFixture` key in an instance file at a main/prod ref is red. A value that will one day be TRUE at
Fernwood (the A+ default, identity.theme) is a staged prod change and carries NO marker.
"""
import argparse, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
MARK = "_qaFixture"

def files_at(ref):
    r = subprocess.run(["git", "-C", ROOT, "ls-tree", "--name-only", ref, "instance/"], capture_output=True, text=True)
    return [f for f in r.stdout.split() if f.endswith(".json")]

def markers(obj, path=""):
    out = []
    if isinstance(obj, dict):
        if MARK in obj: out.append((path or "<root>", obj[MARK]))
        for k, v in obj.items(): out += markers(v, (path + "." + k) if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj): out += markers(v, "%s[%d]" % (path, i))
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); ap.add_argument("--ref", default="HEAD"); ap.add_argument("--branch", default=None)
    a = ap.parse_args()
    found = []
    for f in files_at(a.ref):
        r = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (a.ref, f)], capture_output=True, text=True)
        if r.returncode: continue
        try: found += [(f, p, why) for p, why in markers(json.loads(r.stdout))]
        except ValueError: print("⛔ %s at %s is not JSON" % (f, a.ref)); return 3
    print("qa-fixtures at %s — %d `%s` marker(s)" % (a.ref, len(found), MARK))
    for f, p, why in found: print("  %s %s · %s" % (f, p, why))
    if not a.check: return 0
    if a.branch and a.branch not in ("main", "prod"): print("  (branch %s: fixtures allowed here)" % a.branch); return 0
    if found: print("🔴 %d QA fixture(s) in an instance file at %s — remove every `%s` before the migration push" % (len(found), a.ref, MARK)); return 1
    print("✅ no QA fixture marker at %s" % a.ref); return 0

if __name__ == "__main__":
    sys.exit(main())
