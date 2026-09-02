#!/usr/bin/env python3
"""check-backlog-drift.py — is a backlog rationalization owed?

⭐ WHY THIS EXISTS `[paul-stated 2026-09-02]`: the five-seat rationalization Paul
commissioned on 2026-07-28 **ran on 2026-07-29** and was applied (`a6c89a8`). It was a
ONE-OFF he had to commission by hand. Nothing made it recur, so nothing did.

Measured the day this was written, 35 days later:

  · `BACKLOG.md`  **575 -> 2,421 lines** (4.2x) across **129 commits**
  · **21 new H2 sections** wedged between the "one true list" and the tracks it ranks
  · the pointer head sits at line 19; its **TIER 1 table sits at line 753** — 734 lines apart

⭐ THAT LAST NUMBER IS THE DEFECT, AND IT IS NOT FILE SIZE. The 07-29 head declares
*"This is a POINTER list, not a second tracker... read this for what now."* A reader who
obeys that instruction now reads 734 lines of later accretion before reaching what-now.
The rationalization was commissioned to kill **"the two colliding ▶️ NEXT tables."** The
same defect has re-grown by append, in the file's own reading order.

WHY IT IS A TRIGGER, NOT A BEAT — AND WHY IT IS NOT IN THE MOM CYCLE
-------------------------------------------------------------------
⛔ **A rationalization beat must never become a lap trigger.** `MOM-CYCLE-MAP.md` is
explicit: *"The loop rests. HER INPUT is what fires it. Not a schedule, not a backlog."*
Hanging rationalization off the mom cycle's close would make grooming a shared artifact
wait on Mom's cadence — and `BACKLOG.md` is not Track A's file. It carries Track A, Track
B and Track C, and since 2026-09-01 it is written by **two** loops (mom + fleet). A beat
inside either one is scoped wrong in both directions.

So this is the SAME SHAPE as `check-ux-sweep.py`, deliberately and by reuse rather than
invention: an accumulation trigger that sits in `CLAUDE.md`'s session-start block, is read
at every Fernwood pickup (**not** at every lap), FLAGS and never runs anything, and fires
on measured accretion rather than on a calendar. It adds no loop, no state and no beat.

⛔ IT FLAGS; IT DOES NOT REORDER. A non-AI door: "is a rationalization owed?" is
answerable without invoking a model, and the reordering itself stays Paul-gated exactly
as the 07-29 run was.

⚠️ THE CLOCK IS READ FROM EVIDENCE, NEVER FROM A HAND-WRITTEN LINE. A count typed beside
a tool that computes the same count is the CYCLE-SPINE enactment amendment's own recorded
failure mode. The last rationalization is discovered from `.plans/` and from BACKLOG.md's
own `(rationalized YYYY-MM-DD)` marker, newest wins — which also means **applying** a
rationalization resets this clock as a side effect of doing the work, not as a chore.

Usage:
    python3 tools/check-backlog-drift.py
    python3 tools/check-backlog-drift.py --json
    python3 tools/check-backlog-drift.py --selftest
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
BACKLOG = os.path.join(ROOT, "BACKLOG.md")
PLANS = os.path.join(ROOT, ".plans")

DATE_PAT = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

# --- The three structural anchors this check is SITED on -------------------
# SITING (CYCLE-SPINE S3): the measured risk is that the ranked pointer list gets
# BURIED by append-only accretion — not that the file gets long. A long decision
# record is correct and wanted; a ranking a reader cannot reach is not. So the
# check is sited on the DISTANCE from the pointer head to its own first tier, and
# on what accumulates between them. It is deliberately NOT sited on line count,
# which was never the defect and would fire on healthy growth.
HEAD_PAT = re.compile(r"^#\s*(?:▶️|▶)\s*NEXT\b", re.M)
TIER_PAT = re.compile(r"^##\s*.*\bTIER\s*1\b", re.M | re.I)
# ⭐ The TIER 1/2/3 headings are H2s living INSIDE the live region — they ARE the ranked
# list, not accretion piled on top of it. Counting them was this checker's own first
# defect, caught by its selftest before it ever ran for real: it inflated every reading
# by a constant 3 and would have reported a freshly-rationalized file as carrying three
# sections of drift. Container-vs-payload again — "is an H2 above the tracks" was standing
# in for "is something a rationalization has not yet ranked".
TIER_ANY_PAT = re.compile(r"^##\s*.*\bTIER\s*\d", re.M | re.I)
TRACKS_PAT = re.compile(r"^#\s*TRACK\s+A\b", re.M | re.I)
H2_PAT = re.compile(r"^##\s+")
# A section whose heading already says the work is finished. Reported as a FACT for
# whoever runs the rationalization — never a firing signal. (S3 posture: counted,
# never graded. A control whose alarm is permanently on is a control nobody reads.)
CLOSED_PAT = re.compile(r"✅|SHIPPED|FIXED|CLOSED|KILLED|SUPERSEDED", re.I)

# Where the head marker records the last applied run: "(rationalized 2026-07-29)"
MARKER_PAT = re.compile(r"rationalized\s+(\d{4}-\d{2}-\d{2})", re.I)
# A .plans/ artifact from a rationalization run.
PLAN_PAT = re.compile(r"rationaliz", re.I)

# Thresholds — a FIRST CUT, agent-proposed, NOT ratified. Same posture as
# check-ux-sweep.py's limits and the engagement signals: tune from what runs show
# and record the move in MOM-CYCLE-LOG.md.
LIMIT_DAYS = 30          # a rationalization older than a month over an active file
LIMIT_SECTIONS = 12      # new H2s wedged above the tracks since the last run
LIMIT_HEAD_GAP = 400     # lines between the pointer head and its own TIER 1


class Unknown(Exception):
    """The check cannot determine an input. Fails CLOSED — never renders as rested."""


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def last_rationalization(backlog_text, plans_dir=PLANS):
    """Newest evidence of an applied rationalization, from TWO independent sources.

    Both are containers for the same claim, so neither is trusted alone: the head
    marker can be edited without a run, and a .plans/ file can exist for a run that
    was never applied. Taking the NEWEST is the fail-closed direction for a clock
    (it under-reports how stale we are, never over-reports).
    """
    found = []
    m = MARKER_PAT.search(backlog_text)
    if m:
        y, mo, d = m.group(1).split("-")
        found.append((dt.date(int(y), int(mo), int(d)), f"BACKLOG.md head marker ({m.group(1)})"))
    if os.path.isdir(plans_dir):
        for name in os.listdir(plans_dir):
            if not PLAN_PAT.search(name):
                continue
            dm = DATE_PAT.search(name)
            if dm:
                found.append((dt.date(*map(int, dm.groups())), f".plans/{name}"))
    if not found:
        raise Unknown("no rationalization has ever been recorded "
                      "(no head marker, no .plans/ artifact)")
    return max(found, key=lambda t: t[0])


def measure(backlog_text):
    """Structural facts about the file, as line numbers. Raises Unknown if an anchor
    is missing — a moved/renamed anchor must be LOUD, not silently read as zero drift."""
    lines = backlog_text.splitlines()
    head = HEAD_PAT.search(backlog_text)
    tier = TIER_PAT.search(backlog_text)
    tracks = TRACKS_PAT.search(backlog_text)
    if not head:
        raise Unknown("no '▶️ NEXT' pointer head found — the rationalized list is gone or renamed")
    if not tier:
        raise Unknown("no 'TIER 1' heading found — the ranked list is gone or renamed")

    def lineno(match):
        return backlog_text[:match.start()].count("\n") + 1

    head_ln, tier_ln = lineno(head), lineno(tier)
    tracks_ln = lineno(tracks) if tracks else len(lines) + 1

    # The "live region": everything between the pointer head and the tracks. This is
    # what a reader crosses before reaching the decision record.
    region = [(i + 1, l) for i, l in enumerate(lines) if head_ln < i + 1 < tracks_ln]
    h2s = [(n, l) for n, l in region
           if H2_PAT.match(l) and not TIER_ANY_PAT.match(l)]
    closed = [(n, l) for n, l in h2s if CLOSED_PAT.search(l)]
    return {
        "lines": len(lines),
        "headLine": head_ln,
        "tierLine": tier_ln,
        "tracksLine": tracks_ln if tracks else None,
        "headGap": tier_ln - head_ln,
        "sectionsAboveTracks": len(h2s),
        "closedSectionsInLiveRegion": len(closed),
    }


def sections_added_since(since):
    """H2 count in the live region added since `since`, by diffing against that date's
    BACKLOG.md in git. Returns None when git cannot answer (reported, never assumed 0)."""
    try:
        out = subprocess.run(
            ["git", "-C", ROOT, "rev-list", "-1", f"--before={since.isoformat()} 23:59:59", "HEAD"],
            capture_output=True, text=True, timeout=20)
        sha = out.stdout.strip()
        if not sha:
            return None
        old = subprocess.run(["git", "-C", ROOT, "show", f"{sha}:BACKLOG.md"],
                             capture_output=True, text=True, timeout=20)
        if old.returncode != 0 or not old.stdout:
            return None
        return measure(old.stdout)["sectionsAboveTracks"]
    except (OSError, ValueError, subprocess.SubprocessError, Unknown):
        return None


def commits_since(since):
    try:
        out = subprocess.run(
            ["git", "-C", ROOT, "log", "--oneline", f"--since={since.isoformat()}",
             "--", "BACKLOG.md"], capture_output=True, text=True, timeout=20)
        return len([l for l in out.stdout.splitlines() if l.strip()])
    except (OSError, subprocess.SubprocessError):
        return None


def evaluate(backlog_text, today=None, plans_dir=PLANS, git=True):
    today = today or dt.date.today()
    when, source = last_rationalization(backlog_text, plans_dir)
    m = measure(backlog_text)
    days = (today - when).days
    before = sections_added_since(when) if git else None
    added = (m["sectionsAboveTracks"] - before) if before is not None else None

    fired = []
    if days >= LIMIT_DAYS:
        fired.append(f"{days}d since the last rationalization (limit {LIMIT_DAYS})")
    if added is not None and added >= LIMIT_SECTIONS:
        fired.append(f"{added} new sections wedged above the tracks (limit {LIMIT_SECTIONS})")
    elif added is None and m["sectionsAboveTracks"] >= LIMIT_SECTIONS:
        fired.append(f"{m['sectionsAboveTracks']} sections above the tracks, "
                     f"growth unmeasurable from git (limit {LIMIT_SECTIONS})")
    if m["headGap"] >= LIMIT_HEAD_GAP:
        fired.append(f"the ranked list is {m['headGap']} lines below its own head "
                     f"(limit {LIMIT_HEAD_GAP}) — line {m['headLine']} -> {m['tierLine']}")

    return {
        "owed": bool(fired), "fired": fired,
        "lastRationalization": when.isoformat(), "source": source, "days": days,
        "sectionsAddedSince": added, "backlogCommitsSince": commits_since(when) if git else None,
        **m,
    }


# --------------------------------------------------------------------------
# SELFTEST — S3 requires a check SEEN TO FAIL. Each case is a MUTATION that must
# flip a verdict; a checker that only ever passes has proven nothing about itself.
# --------------------------------------------------------------------------
HEALTHY = """# Fernwood — backlog

# ▶️ NEXT — the one true list (rationalized {date})

## 🔥 TIER 1 · FIX NOW
- a row

# TRACK A — Mom's field journal
## A1 · something
"""


def _selftest():
    today = dt.date(2026, 9, 2)
    fails = []

    def check(label, cond):
        print(("  ✅ " if cond else "  ❌ ") + label)
        if not cond:
            fails.append(label)

    print("check-backlog-drift selftest")

    # 1 · A tight, freshly-rationalized file is RESTED.
    r = evaluate(HEALTHY.format(date="2026-09-01"), today=today, plans_dir="/nonexistent", git=False)
    check("healthy + fresh marker -> not owed", r["owed"] is False)

    # 2 · MUTATION: age the marker past the day limit. Must fire, and only on days.
    r = evaluate(HEALTHY.format(date="2026-06-01"), today=today, plans_dir="/nonexistent", git=False)
    check("aged marker -> owed", r["owed"] is True)
    check("aged marker fires the DAYS signal", any("since the last" in f for f in r["fired"]))
    check("aged marker does NOT fire head-gap", not any("below its own head" in f for f in r["fired"]))

    # 3 · MUTATION: bury the ranked list under accretion, marker still fresh.
    #     This is the real 2026-09-02 defect, reproduced in miniature.
    buried = HEALTHY.format(date="2026-09-01").replace(
        "## 🔥 TIER 1", "\n".join(f"## 📌 appended section {i}" for i in range(30))
        + "\n" + "\n".join("filler" for _ in range(500)) + "\n## 🔥 TIER 1")
    r = evaluate(buried, today=today, plans_dir="/nonexistent", git=False)
    check("buried list + fresh marker -> owed", r["owed"] is True)
    check("buried list fires HEAD-GAP", any("below its own head" in f for f in r["fired"]))
    check("buried list fires the SECTION count too", any("above the tracks" in f for f in r["fired"]))
    check("buried list does NOT fire days", not any("since the last" in f for f in r["fired"]))

    # 4 · MUTATION: sections BELOW the tracks header must not be counted. A decision
    #     record is allowed to be long — that is the whole point of the split.
    below = HEALTHY.format(date="2026-09-01") + "\n".join(
        f"## A{i} · a decision-record row" for i in range(40))
    r = evaluate(below, today=today, plans_dir="/nonexistent", git=False)
    check("40 sections BELOW the tracks -> still not owed", r["owed"] is False)
    check("  and they are not counted in the live region", r["sectionsAboveTracks"] == 0)

    # 4b · MUTATION: the TIER headings themselves are the ranked list, never accretion.
    tiers = HEALTHY.format(date="2026-09-01").replace(
        "## 🔥 TIER 1 · FIX NOW", "## 🔥 TIER 1 · FIX NOW\n## ✅ TIER 2 · CONFIRMED\n## 🧭 TIER 3 · STEER")
    r = evaluate(tiers, today=today, plans_dir="/nonexistent", git=False)
    check("TIER 1/2/3 headings are not counted as drift", r["sectionsAboveTracks"] == 0)

    # 5 · FAIL CLOSED: no evidence of any rationalization at all.
    try:
        evaluate("# Fernwood\n# ▶️ NEXT\n## TIER 1\n", today=today, plans_dir="/nonexistent", git=False)
        check("no marker anywhere -> raises Unknown", False)
    except Unknown:
        check("no marker anywhere -> raises Unknown", True)

    # 6 · FAIL CLOSED: the anchors moved. Must be LOUD, never silently zero drift.
    for label, text in (("head", "# Fernwood\n## TIER 1 · x\n"),
                        ("tier", "# ▶️ NEXT — (rationalized 2026-09-01)\n")):
        try:
            evaluate(text, today=today, plans_dir="/nonexistent", git=False)
            check(f"missing {label} anchor -> raises Unknown", False)
        except Unknown:
            check(f"missing {label} anchor -> raises Unknown", True)

    # 7 · The closed-section count is a FACT, not a firing signal.
    shipped = HEALTHY.format(date="2026-09-01").replace(
        "## 🔥 TIER 1", "\n".join(f"## ✅ SHIPPED thing {i}" for i in range(20)) + "\n## 🔥 TIER 1")
    r = evaluate(shipped, today=today, plans_dir="/nonexistent", git=False)
    check("20 SHIPPED sections are COUNTED", r["closedSectionsInLiveRegion"] == 20)
    check("  and do not by themselves fire anything",
          not any("shipped" in f.lower() for f in r["fired"]))

    print(f"\n{'PASS' if not fails else 'FAIL'} — {len(fails)} failure(s)")
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return _selftest()

    try:
        r = evaluate(_read(BACKLOG))
    except Unknown as e:
        if args.json:
            print(json.dumps({"owed": True, "unknown": str(e)}, indent=2))
        else:
            print(f"📋 Backlog rationalization — ⚠️ UNKNOWN, treated as OWED: {e}")
        return 1
    except OSError as e:
        print(f"📋 Backlog rationalization — ⚠️ cannot read BACKLOG.md ({e})")
        return 1

    if args.json:
        print(json.dumps(r, indent=2))
        return 1 if r["owed"] else 0

    if not r["owed"]:
        print(f"📋 Backlog rationalization — rested. Last {r['lastRationalization']} "
              f"({r['days']}d) · {r['sectionsAboveTracks']} sections above the tracks · "
              f"ranked list {r['headGap']} lines below its head.")
        return 0

    print(f"📋 Backlog rationalization is OWED — last run {r['lastRationalization']} "
          f"({r['days']}d ago, per {r['source']}).")
    for f in r["fired"]:
        print(f"   ⚡ {f}")
    print(f"   · BACKLOG.md is {r['lines']} lines; {r['closedSectionsInLiveRegion']} of "
          f"{r['sectionsAboveTracks']} sections above the tracks already read as finished")
    if r["backlogCommitsSince"] is not None:
        print(f"   · {r['backlogCommitsSince']} commits to BACKLOG.md since that run")
    print("   Run:  a rationalization pass — PROPOSE the reordering as a diff, do not apply it")
    print("   ⚠️ This does NOT fire a mom lap. The loop still rests on HER input")
    print("      (MOM-CYCLE-MAP.md § What STARTS a lap). This is a file-grooming trigger,")
    print("      read at pickup, and BACKLOG.md is written by two loops, not one.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
