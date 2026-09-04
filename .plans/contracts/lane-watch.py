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

def status():
    """lane slug -> its declared STATUS line, read from the contract.

    Added 2026-09-04 after lane A asked the question this tool could not answer:
    once a lane's tab closes, its absence from the live list is indistinguishable
    from a lane that vanished mid-work. A watcher that cannot tell "finished"
    from "disappeared" reports a clean run and a dead one identically -- the same
    quiet-failure shape this project already names three times. The contract
    declares it; nothing is inferred from absence.
    """
    out = {}
    for fn in sorted(os.listdir(HERE)):
        if fn.startswith("lane-") and fn.endswith(".md"):
            m = re.search(r"^## STATUS:\s*(.+)$", open(os.path.join(HERE, fn)).read(), re.M)
            out[fn[:-3]] = m.group(1).strip() if m else "UNDECLARED"
    return out


def live():
    try:
        rows = json.loads(sh("claude", "agents", "--json") or "[]")
    except Exception:
        return []
    here = [r for r in rows if r.get("kind") == "interactive"
            and os.path.abspath(r.get("cwd", "")) == REPO]
    # A lane whose OWNS are in another repo runs with a different cwd and is invisible
    # above. The WRITES panel already says so; the LIVE panel used to imply completeness.
    other = [r for r in rows if r.get("kind") == "interactive"
             and os.path.abspath(r.get("cwd", "")) != REPO]
    return here, other

def main():
    O = owns()
    print(f"── LANE WATCH · {time.strftime('%-I:%M %p')} · base {BASE}\n")

    sessions, elsewhere = live()
    print(f"LIVE ({len(sessions)} interactive session(s) with cwd = this repo)")
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
    # closed vs vanished — the distinction absence alone cannot make
    S = status()
    names = " ".join(r.get("name", "") for r in sessions)
    print("\nDECLARED STATUS (from each contract; absence is never inferred)")
    for lane, v in sorted(S.items()):
        if v.startswith("CLOSED"):
            print(f"  ✓ {lane:<26} {v}")
        elif v == "UNDECLARED":
            print(f"  ⚠ {lane:<26} no ## STATUS line — the watcher cannot judge its absence")
        else:
            print(f"  · {lane:<26} {v}")
    open_lanes = [l for l, v in S.items() if not v.startswith("CLOSED") and v != "UNDECLARED"]
    if open_lanes and len(sessions) < len(open_lanes):
        print(f"  ⚠ {len(open_lanes)} lane(s) declared OPEN but only {len(sessions)} live session(s) —")
        print("    at least one is VANISHED, not closed. Check before assuming it finished.")
    elif open_lanes:
        print(f"  · {len(open_lanes)} open, {len(sessions)} live — ⚠ COUNTS MATCH, WHICH IS NOT A PAIRING.")
        print("    ⛔ This compares NUMBERS, not identities: a lane that died while an unrelated")
        print("       session opened in this repo balances the count and reads exactly like health.")
        print("       Nothing here binds a session to a lane — that needs a slug exported at spawn.")
        print("       Read the names above against the open lanes yourself.")
    if elsewhere:
        print(f"  · {len(elsewhere)} interactive session(s) in OTHER repos — not judged here:")
        for r in elsewhere[:4]:
            print(f"      {r.get('name','?'):<24} {os.path.basename(r.get('cwd',''))}")
        print("    A lane whose OWNS are in another repo (lane A was) runs with a different cwd.")

    files = [f for f in sh("git", "log", f"{BASE}..HEAD", "--name-only",
                           "--pretty=format:").split("\n") if f.strip()]
    seen, claimed = sorted(set(files)), set()
    print(f"\nWRITES since {BASE} ({len(seen)} distinct path(s))")
    for lane, paths in sorted(O.items()):
        hits = [f for f in seen if any(f == p or f.startswith(p.rstrip('/') + '/')
                                       or os.path.basename(p) == os.path.basename(f)
                                       for p in paths)]
        claimed |= set(hits)
        # A lane whose OWNS live in another repo cannot be judged from this git log.
        # Printing "0" for it reads as "did nothing", which is the flattering direction.
        outside = [p for p in paths if p.startswith("~") or p.startswith("/")]
        if outside and not hits:
            print(f"  {lane:<26} n/a — OWNS are outside this repo ({outside[0]}); not visible here")
        else:
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
