#!/usr/bin/env python3
"""lane-watch — is each lane alive, and is it writing where it said it would?

Not a watcher. A CALLER for two doors that already exist:
  * `claude agents --json`  -> pid, cwd, kind, status per live session
  * `git log <base>..HEAD --name-only` -> what each lane actually wrote

Why it exists: the practice-steward audit (2026-09-04, M2/M3) found that a lane
which finished quietly and one that died at a 3am permission prompt produced the
identical ledger row, and that nothing detected a missing gate report -- while
the data to tell them apart was already on disk. Paul then asked for a periodic
check "to be sure they're not stuck or drifting". This is that check.

OWNS is parsed from each contract's `## OWNS` section rather than restated here.
A second copy of the ownership list is how the contract and the check start
disagreeing about what a lane owns.

Exit 0 always: this reports, it never gates.
"""
import json, re, subprocess, sys, os, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
BASE = sys.argv[1] if len(sys.argv) > 1 else "2e65319"   # the contracts commit
STALL_MIN = 12

def sh(*a, cwd=REPO):
    return subprocess.run(a, cwd=cwd, capture_output=True, text=True).stdout

def owns():
    """lane slug -> [path globs], read from the contract's own OWNS section."""
    out = {}
    for fn in sorted(os.listdir(HERE)):
        if not fn.startswith("lane-") or not fn.endswith(".md"):
            continue
        body = open(os.path.join(HERE, fn)).read()
        m = re.search(r"^## OWNS.*?$(.*?)^## ", body, re.S | re.M)
        if not m:
            continue
        paths = re.findall(r"`([^`]+)`", m.group(1))
        keep = [p.replace("~/Developer/Tate-Tracker/", "").strip()
                for p in paths if "/" in p or p.endswith(".md") or p.endswith(".html")]
        out[fn[:-3]] = keep
    return out

def live():
    try:
        rows = json.loads(sh("claude", "agents", "--json") or "[]")
    except Exception:
        return []
    return [r for r in rows
            if r.get("kind") == "interactive" and r.get("cwd", "").endswith("Tate-Tracker")]

def main():
    O = owns()
    print(f"── LANE WATCH · {time.strftime('%-I:%M %p')} · base {BASE}\n")

    sessions = live()
    print(f"LIVE ({len(sessions)} interactive session(s) in this repo)")
    if not sessions:
        print("  ⚠ none — every lane has exited. A lane that exited before reporting its gate")
        print("    is indistinguishable from one that finished; check the commits below.")
    for r in sessions:
        st = r.get("status", "?")
        age = int((time.time() * 1000 - r.get("startedAt", 0)) / 60000)
        flag = {"busy": "  ", "idle": "· ", "waiting": "⚠ "}.get(st, "? ")
        note = ""
        if st == "waiting":
            note = "  ← BLOCKED on a prompt nobody can see; it will sit here forever"
        print(f"  {flag}{r.get('name','?'):<22} {st:<8} {age:>4}m{note}")

    # what actually got written since the base
    files = [f for f in sh("git", "log", f"{BASE}..HEAD", "--name-only",
                           "--pretty=format:").split("\n") if f.strip()]
    seen, claimed = sorted(set(files)), set()
    print(f"\nWRITES since {BASE} ({len(seen)} distinct path(s))")
    for lane, paths in sorted(O.items()):
        hits = [f for f in seen if any(f == p or f.startswith(p.rstrip('/') + '/')
                                       or os.path.basename(p) == os.path.basename(f)
                                       for p in paths)]
        claimed |= set(hits)
        print(f"  {lane:<26} {len(hits)} in-OWNS")
    stray = [f for f in seen if f not in claimed]
    if stray:
        print(f"\n  ⚠ {len(stray)} path(s) matched NO lane's OWNS — hub writes, or drift:")
        for f in stray:
            who = sh("git", "log", "-1", "--pretty=format:%h %s", f"{BASE}..HEAD", "--", f)
            print(f"      {f}\n         {who[:96]}")
        print("      ⚠ This cannot tell a hub write from a lane's drift. It names the commit;")
        print("        you read it. A checker that guessed would be worse than one that asks.")

    # stall: busy a long time with nothing landed
    print()
    for r in sessions:
        if r.get("status") == "busy":
            age = int((time.time() * 1000 - r.get("startedAt", 0)) / 60000)
            if age > STALL_MIN and not seen:
                print(f"  ⚠ {r.get('name')} busy {age}m with nothing committed — possible stall")
    print("  (status is a claim about right now; a lane can be 'busy' rendering its last message.)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
