#!/usr/bin/env python3
"""mom-cycle-status.py — the Mom-feedback loop's GLANCEABLE STATUS SURFACE.

The awareness half of the definable loop (`MOM-CYCLE-MAP.md`). Paul reads the
loop's position HERE, not by parsing an agent's action stream.

WHY THIS EXISTS
---------------
`[paul-stated 2026-08-03]` every recurring AI workstream gets a definable loop,
and one of its five parts is *"a very intentional design to keep me aware and in
control"* — status that is READ, never narrated. Until 2026-08-04 this loop had
five detectors (check-mom-ack, check-cards, check-data-inline, check-digest-fresh,
read-mom-feedback) and no surface that said WHERE IN THE LOOP WE ARE. Five green
exit codes do not answer "is anything waiting on me."

⭐ NON-AI DOOR (`[paul-stated 2026-08-02]`). No model runs here. Every signal is
derived from canon on disk plus the Worker's own endpoints. If the only way to
learn whether Mom is owed a reply were to ask Claude, this loop would be broken.

WHAT IT WILL NOT DO
-------------------
It does not report a draft that exists only in a conversation. A return leg
sitting in an agent's chat window is not loop state — it is unshipped. What this
prints is what the RECORD owes her, which is the thing that can actually be
verified. `[the 7/26 lesson: capture is not a loop]`

Exit codes follow the sibling checks: 0 = nothing waiting, 1 = something is.

Usage:
    python3 tools/mom-cycle-status.py
    python3 tools/mom-cycle-status.py --json
"""
import argparse
import datetime as dt
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

spec = importlib.util.spec_from_file_location("momlib", os.path.join(HERE, "momlib.py"))
momlib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(momlib)

# The legs, in the order SKILL.md defines them. `gate` marks a leg that a run
# CANNOT cross on its own — the structural half of human-in-the-loop.
LEGS = [
    ("0", "GUARD",   False, "concurrent session / HEAD moved"),
    ("1", "READ",    False, "the deterministic sweep"),
    ("2", "TRIAGE",  False, "four classes, routed"),
    ("3", "RESOLVE", True,  "ambiguity ladder — tier 2 is Paul"),
    ("4", "EXPERT",  False, "one seat, escalate on trigger"),
    ("5", "SHIP",    False, "wins that never reach her"),
    ("6", "GATE",    True,  "the return leg, at Paul's gate"),
    ("7", "CLOSE",   False, "dispositions + watermark"),
]


def _run(tool, *args):
    """Run a sibling check, return (exit_code, stdout). Never raises."""
    try:
        p = subprocess.run(
            [sys.executable, os.path.join(HERE, tool), *args],
            capture_output=True, text=True, timeout=120, cwd=ROOT,
        )
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except Exception as e:
        return -1, f"{type(e).__name__}: {e}"


def gather():
    """Derive every signal. Each carries the SOURCE it came from — a signal with
    no named source is a rumour, and this loop has already paid for one."""
    sig = {}

    cards_rc, cards_out = _run("check-cards.py")
    sig["served_queue"] = {
        "source": "tools/check-cards.py",
        "clean": cards_rc == 0,
        "detail": [l.strip() for l in cards_out.splitlines() if "🔴" in l or "🟡" in l],
    }

    ack_rc, ack_out = _run("check-mom-ack.py")
    sig["return_leg"] = {
        "source": "tools/check-mom-ack.py",
        "owed": ack_rc != 0,
        "unread": "R2b" in ack_out and "🔴" in ack_out,
    }

    inline_rc, _ = _run("check-data-inline.py")
    digest_rc, _ = _run("check-digest-fresh.py")
    sig["canon_surfaces"] = {
        "source": "check-data-inline.py + check-digest-fresh.py",
        "clean": inline_rc == 0 and digest_rc == 0,
    }

    # Her newest input, and whether the record has answered through it.
    try:
        tok = momlib.resolve_token()
        state = momlib.load_read_state()
        sig["channels"] = {
            "source": ".private/channel-read-state.json",
            "read_through": {k: v.get("readThrough") for k, v in (state or {}).items()},
        }
    except Exception as e:
        sig["channels"] = {"source": ".private/channel-read-state.json", "error": str(e)}

    # Concurrency guard — Leg 0. A moving HEAD is the one signal that invalidates
    # everything below it, so it is derived first and printed loudest.
    try:
        head = subprocess.run(["git", "log", "--oneline", "-1"], cwd=ROOT,
                              capture_output=True, text=True, timeout=20).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                               capture_output=True, text=True, timeout=20).stdout.strip()
        unpushed = subprocess.run(["git", "log", "--oneline", "origin/main..HEAD"], cwd=ROOT,
                                  capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        head, dirty, unpushed = "", "", ""
    sig["repo"] = {
        "source": "git",
        "head": head,
        "dirty_files": len([l for l in dirty.splitlines() if l.strip()]),
        "unpushed_commits": len([l for l in unpushed.splitlines() if l.strip()]),
    }
    return sig


def position(sig):
    """Where the loop is standing, and whether it is Paul's move.

    Deliberately conservative: the return leg outranks everything, because it is
    the only leg whose absence is invisible to Mom AND to Paul. It is the leg
    that sat 8 days stale during her best week."""
    if sig["return_leg"]["owed"] or not sig["served_queue"]["clean"]:
        return "6", True
    if not sig["canon_surfaces"]["clean"]:
        return "5", False
    return "7", False


def main():
    ap = argparse.ArgumentParser(description="Where is the Mom-feedback loop standing?")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    sig = gather()
    at, needs_paul = position(sig)

    if a.json:
        print(json.dumps({"at_leg": at, "needs_paul": needs_paul, "signals": sig},
                         indent=2, ensure_ascii=False))
        return 1 if needs_paul or not sig["served_queue"]["clean"] else 0

    print()
    print("🌿 Mom-feedback loop — where we are")
    print("   map: MOM-CYCLE-MAP.md · chronicle: MOM-CYCLE-LOG.md · procedure: /mom-cycle")
    print()
    for num, name, is_gate, blurb in LEGS:
        here = "▶" if num == at else " "
        mark = " 👤" if is_gate else ""
        flag = ""
        if num == at and needs_paul:
            flag = "   🔴 NEEDS YOU"
        print(f"  {here} {num} · {name:<8}{mark:<3} {blurb}{flag}")
    print()

    if not sig["served_queue"]["clean"]:
        print("  🔴 SERVED QUEUE — what she is being shown is wrong:")
        for d in sig["served_queue"]["detail"]:
            print(f"       {d}")
    if sig["return_leg"]["owed"]:
        print("  🔴 RETURN LEG — she has given something the ribbon does not cover.")
        print("       python3 tools/check-mom-ack.py --verbose")
    if sig["return_leg"]["unread"]:
        print("  🔴 UNREAD — a channel has input nothing has actually read.")
    if not sig["canon_surfaces"]["clean"]:
        print("  🟡 CANON SURFACES — viewer inlines or Guru's digest are behind canon.")
    if sig["repo"]["unpushed_commits"]:
        print(f"  🟡 {sig['repo']['unpushed_commits']} unpushed commit(s) — Pages serves "
              "viewer.html; a commit alone never reaches her.")
    if sig["repo"]["dirty_files"]:
        print(f"  🟡 {sig['repo']['dirty_files']} uncommitted file(s) in the working tree.")

    if not needs_paul and sig["canon_surfaces"]["clean"] and not sig["repo"]["unpushed_commits"]:
        print("  🟢 Nothing is waiting on you.")
    print()
    return 1 if needs_paul else 0


if __name__ == "__main__":
    sys.exit(main())
