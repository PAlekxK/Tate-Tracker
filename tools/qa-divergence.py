#!/usr/bin/env python3
"""qa-divergence.py — what QA has that the live Fernwood (Mom's page) does not, measured from git.
    python3 tools/qa-divergence.py            # the ledger: commits on origin/staging not on origin/main, by surface class
    python3 tools/qa-divergence.py --json
    python3 tools/qa-divergence.py --check    # exit 1 if any SURFACE divergence is not named in a plan stage-note

[paul-stated 2026-09-04 ~1:25 AM ET]: "this is where we start to potentially diverge from the live Fernwood mom
sees … we need to make additions in a way that's trackable." Prod's viewer is origin/main (GitHub Pages builds it);
QA's is origin/staging (Pages + the fernwood-qa Worker). So the divergence IS `origin/main..origin/staging`, and this
tool reads it rather than anyone remembering it. Each commit is classed by the files it touches:
  SURFACE   viewer.html · engine/ · instance/ · a rostered canon JSON   → what she would SEE change at the migration
  WORKER    worker/                                                      → engine behind the page (prod-eligible by cherry-pick)
  TOOLING   tools/ · .github/ · docs/plans/records                       → nothing she sees
`--check` asks that every SURFACE commit's short sha OR the first 40 chars of its subject appears in some plan's `- stage-note:` line (subjects survive rebase; shas do not) — the addition is
recorded where the plan lives, or the run is red. It fetches first so the answer is about the remotes, not this clone.
"""
import argparse, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
SURFACE = re.compile(r"^(viewer\.html|engine/|instance/|property\.json|plants\.json|weeds\.json|turf\.json|zones\.json|vehicles\.json|birds\.json|mammals\.json|amphibians\.json|snakes\.json|lizards\.json|insects\.json|fishing\.json|candidates\.json|references\.json|sources\.json|estate\.json|RELEASE_NOTES\.md|images/|sounds/)")
WORKER = re.compile(r"^worker/")

def git(*a):
    return subprocess.run(["git", "-C", ROOT] + list(a), capture_output=True, text=True).stdout

def classify(files):
    if any(SURFACE.match(f) for f in files): return "SURFACE"
    if any(WORKER.match(f) for f in files): return "WORKER"
    return "TOOLING"

def ledger(fetch=True):
    if fetch:
        subprocess.run(["git", "-C", ROOT, "fetch", "-q", "origin", "main", "staging"], capture_output=True)
    shas = [l for l in git("log", "--format=%h", "origin/main..origin/staging").split("\n") if l]
    rows = []
    for h in shas:
        subject = git("log", "-1", "--format=%s", h).strip()
        when = git("log", "-1", "--date=format-local:%Y-%m-%d %H:%M", "--format=%ad", h).strip()
        files = [f for f in git("show", "--name-only", "--format=", h).split("\n") if f]
        rows.append({"sha": h, "when": when, "class": classify(files), "files": files, "subject": subject})
    notes = ""
    for fn in sorted(os.listdir(os.path.join(ROOT, ".plans"))):
        if fn.endswith("-PLAN.md"):
            notes += "".join(l for l in open(os.path.join(ROOT, ".plans", fn), encoding="utf-8") if l.startswith("- stage-note:"))
    for r in rows:
        # a sha MOVES under rebase (measured 2026-09-04: 5d7760f became e1e608a after two integrations of the other
        # session's main); the subject does not. A stage-note records EITHER — quoting the subject's first 40 chars is
        # the rebase-proof way.
        r["recorded"] = r["sha"] in notes or r["subject"][:40] in notes
    return rows

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--json", action="store_true"); ap.add_argument("--check", action="store_true"); ap.add_argument("--no-fetch", action="store_true")
    a = ap.parse_args()
    rows = ledger(fetch=not a.no_fetch)
    if a.json:
        print(json.dumps(rows, indent=1)); return 0
    by = {}
    for r in rows: by.setdefault(r["class"], []).append(r)
    print("QA ⟂ live Fernwood — origin/main..origin/staging: %d commit(s) she does not have" % len(rows))
    for cls in ("SURFACE", "WORKER", "TOOLING"):
        rs = by.get(cls, [])
        if not rs: continue
        print("\n  %s (%d)%s" % (cls, len(rs), " — what she would SEE change" if cls == "SURFACE" else ""))
        for r in rs:
            print("   %s %s %s  %s" % ("✅" if r["recorded"] or cls != "SURFACE" else "🔴", r["sha"], r["when"], r["subject"][:110]))
            if cls == "SURFACE":
                print("        files: " + ", ".join(f for f in r["files"] if SURFACE.match(f))[:160])
    unrec = [r for r in rows if r["class"] == "SURFACE" and not r["recorded"]]
    if a.check and unrec:
        print("\n🔴 %d SURFACE commit(s) on QA are not named in any plan stage-note — record the addition where its plan lives" % len(unrec)); return 1
    if not rows:
        print("  (none — QA and the live page are the same commit)")
    print("\n%s" % ("✅ every SURFACE divergence is recorded in a plan" if not unrec else "⚠️ %d SURFACE commit(s) unrecorded (run --check to gate)" % len(unrec)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
