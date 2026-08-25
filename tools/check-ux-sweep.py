#!/usr/bin/env python3
"""check-ux-sweep.py — is a holistic UX sweep owed?

⭐ WHY THIS EXISTS `[paul-stated 2026-08-24]`: *"We had talked at one point about a
UX review. That UX review should have a pass of kind of fresh eyes, and then a pass
that has our principles and all these rules we're coming up with fed into that
informed pass. So let's also double check that that's kind of a part of our natural
release cycle."*

**It was not.** `/ux-sweep` existed, was correctly built, and its informed pass
already reads every design-principles file — so the rules written today feed it for
free. But it was referenced NOWHERE in the loop: not in `CLAUDE.md`'s session-start
block, not as a leg in `MOM-CYCLE-MAP.md`, not in the `/mom-cycle` procedure. It was
a skill Paul had to remember to invoke.

Measured the day this was written: **21 days, 38 commits to viewer.html and 4 closed
laps** since the last two-pass run (the 2026-08-03 pilot). Nothing said so.

That is the third instance of one failure shape found in a single day:
  · `telemetry-walk.js` served the loop for 16 days while the map never named it;
  · weather-history completeness lived outside the loop entirely;
  · and this.
**A capability the loop cannot reach by running its own procedure is not a
capability the loop has.**

WHY IT IS A TRIGGER, NOT A PER-LAP BEAT
---------------------------------------
A sweep is two agents and a full browse. Running it every lap would spend real
attention on a surface that has not moved, and this project's own doctrine says
loops rest and fire on a signal rather than on a cadence. The skill's own guidance
agrees: *"after a burst of accumulated changes — not per-fix."* So this counts the
burst and says when it is big enough.

⛔ IT FLAGS; IT DOES NOT RUN ANYTHING. Deliberately a non-AI door: the answer to
"is a sweep owed?" is readable without invoking a model.

Usage:
    python3 tools/check-ux-sweep.py
    python3 tools/check-ux-sweep.py --json
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
REVIEWS = os.path.join(ROOT, ".ux-reviews")

# A TWO-PASS run files under one of these. Single-seat reviews (a `ux-expert`
# consult on one surface, like this lap's nesting review) are NOT sweeps and must
# not reset the clock — they are exactly the single-fix work a sweep exists to
# zoom out from. Naming convention going forward: `YYYY-MM-DD-ux-sweep.md`.
SWEEP_PAT = re.compile(r"(ux-sweep|two-pass)", re.I)
DATE_PAT = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

# Thresholds — a FIRST CUT, agent-proposed, not ratified. Tune from what runs show
# and record the move in MOM-CYCLE-LOG.md, the same posture as the row-tax limits
# and the engagement signals.
LIMIT_DAYS = 21
LIMIT_COMMITS = 20      # commits touching the one file Mom actually loads
LIMIT_LAPS = 3


def last_sweep():
    if not os.path.isdir(REVIEWS):
        return None, "no .ux-reviews/ directory"
    best = None
    for name in os.listdir(REVIEWS):
        if not SWEEP_PAT.search(name):
            continue
        m = DATE_PAT.search(name)
        if not m:
            continue
        d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        if best is None or d > best[0]:
            best = (d, name)
    if best is None:
        return None, "no two-pass run has ever been filed"
    return best, None


def git_count(since):
    try:
        out = subprocess.run(
            ["git", "-C", ROOT, "log", "--oneline", f"--since={since}", "--", "viewer.html"],
            capture_output=True, text=True, timeout=20)
        return len([l for l in out.stdout.splitlines() if l.strip()])
    except Exception:
        return None


def laps_since(since):
    log = os.path.join(ROOT, "MOM-CYCLE-LOG.md")
    if not os.path.exists(log):
        return None
    n = 0
    with open(log, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("## Lap "):
                m = DATE_PAT.search(line)
                if m:
                    d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                    if d > since:
                        n += 1
    return n


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    best, why = last_sweep()
    today = dt.date.today()

    if best is None:
        payload = {"owed": True, "reason": why, "lastSweep": None}
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(f"🔍 UX sweep — OWED: {why}.")
            print("   /ux-sweep  (pass 1 fresh eyes · pass 2 adjudicates against the principle libraries)")
        return 1

    d, name = best
    days = (today - d).days
    commits = git_count(d.isoformat())
    laps = laps_since(d)

    fired = []
    if days >= LIMIT_DAYS:
        fired.append(f"{days}d since the last sweep (limit {LIMIT_DAYS})")
    if commits is not None and commits >= LIMIT_COMMITS:
        fired.append(f"{commits} commits to viewer.html (limit {LIMIT_COMMITS})")
    if laps is not None and laps >= LIMIT_LAPS:
        fired.append(f"{laps} laps closed (limit {LIMIT_LAPS})")

    payload = {
        "owed": bool(fired), "lastSweep": d.isoformat(), "lastSweepFile": name,
        "days": days, "viewerCommits": commits, "lapsClosed": laps, "fired": fired,
    }
    if args.json:
        print(json.dumps(payload, indent=2))
        return 1 if fired else 0

    if not fired:
        print(f"🔍 UX sweep — rested. Last {d.isoformat()} ({days}d) · "
              f"{commits} viewer commits · {laps} laps.")
        return 0

    print(f"🔍 UX sweep is OWED — last two-pass run {d.isoformat()} ({days}d ago).")
    for f in fired:
        print(f"   ⚡ {f}")
    print("   Run:  /ux-sweep")
    print("   Pass 1 browses un-primed; pass 2 adjudicates every finding against")
    print("   ~/.claude/design-principles/ — so today's rules feed it automatically.")
    print("   ⚠️ A single-seat review does NOT reset this clock. Only a two-pass run does.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
