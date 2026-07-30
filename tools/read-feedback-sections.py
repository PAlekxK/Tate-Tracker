#!/usr/bin/env python3
"""Which DOOR did she come through? — /api/feedback grouped by context.section.

BACKLOG Track A1 · W8·a, Tier 2 #5. Paul's orienting principle (2026-07-29) says
the confusing input stack is contaminating the instrument we steer by: we cannot
distinguish *she declined* from *she never understood which thing she was
answering*. `context.section` is the field that tells them apart — it records
which surface a record was authored on.

⚠️ READ THIS BEFORE CITING ANY NUMBER THIS TOOL PRINTS.

The backlog row said "every note already carries which door it came through —
nobody has ever read it that way." Half of that was true. Nobody had read it.
But the notes did NOT carry it: on 2026-07-29 a survey of all 14 records found
`section` set on exactly 2 (both `ack-receipt`), because only one of five
`postFeedback` call sites ever passed it. The field was a schema slot four
producers left empty.

So this tool keeps THREE things apart that a naive group-by would merge into one
"unknown" bucket:

  · UNINSTRUMENTED — authored before stamping landed, when the door was simply
    not recorded. This is OUR gap. It is NOT a signal about her, and must never
    be read as a decline, a bounce, or a preference. It is unrecoverable: the
    door was never written down, so these records are permanently unattributable
    to a surface.
  · `unspecified` — authored AFTER stamping by a producer that came through
    postFeedback without naming its door. The helper's floor writes this rather
    than omitting the field, so the gap is visible instead of invisible. A
    finding: go stamp that surface.
  · FLOOR BYPASSED — authored after stamping with no section at all, meaning
    something POSTs to /api/feedback around postFeedback entirely. A code defect,
    reported separately from both of the above.

Merging those would have printed "12 unknown" on 7/29 — reading as though she had
used some mystery surface a dozen times, when in truth we had simply never
written the door down. An honestly-unsure instrument beats a confidently-wrong
one: the doctrine the app itself runs on, and the same failure mode as the
phantom punch-list (2026-07-26) and the backwards device map (fixed 2026-07-28).

Never prints her note text. Sections, counts and timestamps only — this repo is
public, and the verbatim stays in the Worker.

Usage:
    python3 tools/read-feedback-sections.py                # last 90 days
    python3 tools/read-feedback-sections.py --days 30
    python3 tools/read-feedback-sections.py --since 2026-07-30   # stamped era only
    python3 tools/read-feedback-sections.py --json
"""

import argparse
import collections
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402

# The instant every producer began stamping its door — a full TIMESTAMP, not a
# date. A date was tried first and was wrong the same hour: Mom answered a card
# at 8:54 AM ET on 2026-07-29 and the stamping shipped that evening, so a
# date-granular cutoff filed her two morning records as "post-stamping producer
# that forgot its door" — inventing a code defect out of correct behaviour.
#
# Deliberately set a little AFTER the push. Records in the gap read as
# uninstrumented, which is the safe direction: this tool must never claim
# instrumentation it does not have.
STAMPING_LANDED = "2026-07-30T02:10:00Z"
STAMPING_LANDED_HUMAN = "2026-07-29, evening ET"

# What each door IS, in Mom's terms — so a section name in the output does not
# require reading viewer.html to interpret.
DOORS = {
    "card-answer":   "tapped an answer on a confirm card (Looks right / Not quite)",
    "card-notsure":  "chose 'I haven't looked' on a confirm card, and typed something",
    "queue-general": "wrote in the open standing card at the foot of the queue",
    "ribbon":        "wrote in the general feedback panel, no scope given",
    "ack-reply":     "wrote back from the acknowledgment ribbon ('Write back')",
    "ack-receipt":   "tapped 'Got it' on the acknowledgment ribbon",
    "unspecified":   "⚠️ a LIVE producer that did not name its door — go stamp it",
}


def fetch(token, start, end):
    """Walk the range in <=85-day windows (the Worker caps a query at 90)."""
    recs = []
    cur = start
    while cur <= end:
        stop = min(cur + dt.timedelta(days=85), end)
        data = momlib._get("/api/feedback", token,
                           {"start": cur.isoformat(), "end": stop.isoformat()})
        recs += momlib.flatten(data)
        cur = stop + dt.timedelta(days=1)
    return recs


def classify(rec):
    """-> (section, instrumented). `section` is None when no door was recorded.

    `instrumented` compares full instants, not dates — see STAMPING_LANDED.
    """
    ctx = rec.get("context") or {}
    sec = ctx.get("section")
    a = momlib.parse_ts(rec.get("ts") or "")
    b = momlib.parse_ts(STAMPING_LANDED)
    instrumented = bool(a and b and a >= b)
    return (sec or None), instrumented


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=90, help="how far back (default 90)")
    ap.add_argument("--since", help="ISO date; overrides --days")
    ap.add_argument("--json", action="store_true", help="machine-readable")
    args = ap.parse_args()

    token = momlib.resolve_token()
    if not token:
        print("error: no token (.private/fernwood-token).", file=sys.stderr)
        return 2

    today = dt.date.fromisoformat(momlib.et_now().date().isoformat()) \
        if hasattr(momlib, "et_now") else dt.datetime.now(dt.timezone.utc).date()
    start = dt.date.fromisoformat(args.since) if args.since \
        else today - dt.timedelta(days=args.days)

    try:
        recs = fetch(token, start, today)
    except Exception as e:  # noqa: BLE001
        print(f"error: could not read /api/feedback ({e})", file=sys.stderr)
        return 2

    stamped = collections.Counter()
    stamped_latest = {}
    unstamped = 0
    unstamped_latest = None
    bypassed = 0          # post-stamping AND no section — a real code defect
    bypassed_latest = None
    for r in recs:
        sec, instrumented = classify(r)
        ts = r.get("ts") or ""
        if sec is None:
            # Two very different kinds of nothing, kept apart on purpose.
            if instrumented:
                # postFeedback's floor writes "unspecified" rather than omitting,
                # so a record with NO section at all, authored after stamping,
                # means something wrote to /api/feedback around that helper.
                bypassed += 1
                if not bypassed_latest or ts > bypassed_latest:
                    bypassed_latest = ts
            else:
                unstamped += 1
                if not unstamped_latest or ts > unstamped_latest:
                    unstamped_latest = ts
            continue
        stamped[sec] += 1
        if sec not in stamped_latest or ts > stamped_latest[sec]:
            stamped_latest[sec] = ts

    if args.json:
        print(json.dumps({
            "range": {"start": start.isoformat(), "end": today.isoformat()},
            "stampingLanded": STAMPING_LANDED,
            "total": len(recs),
            "instrumented": {
                "bySection": dict(stamped),
                "latestBySection": stamped_latest,
            },
            "uninstrumented": {
                "count": unstamped,
                "latest": unstamped_latest,
                "meaning": "door not recorded — OUR gap, not a signal about her",
            },
            "floorBypassed": {
                "count": bypassed,
                "latest": bypassed_latest,
                "meaning": "post-stamping with no section at all — a code defect",
            },
        }, indent=2, ensure_ascii=False))
        return 0

    print(f"\n🚪 Which door she came through — {start} → {today}")
    print(f"   {len(recs)} feedback record(s)\n")

    if stamped:
        total = sum(stamped.values())
        print(f"── Instrumented ({total}) — the door IS in the record ──\n")
        for sec, n in stamped.most_common():
            desc = DOORS.get(sec, "unrecognised section — new surface, or a typo")
            when = momlib.et_str(stamped_latest.get(sec)) if stamped_latest.get(sec) else "—"
            print(f"  {n:4d}  {sec:15s} {desc}")
            print(f"        last: {when}")
        print()
    else:
        print("── Instrumented (0) ──\n")
        print("  Nothing yet. Every record in range predates door-stamping, so this\n"
              "  tool cannot yet tell a decline from a misunderstanding. That is the\n"
              "  finding — not a result. Come back once she has used the app since\n"
              f"  {STAMPING_LANDED_HUMAN}.\n")

    if bypassed:
        print(f"── ⚠️  FLOOR BYPASSED ({bypassed}) — fix this ──\n")
        print("  Authored AFTER stamping, carrying no section at all. postFeedback")
        print("  writes \"unspecified\" rather than omitting the field, so these did not")
        print("  come through it — something is POSTing to /api/feedback around the")
        print("  one helper that stamps. That is a code defect, not a data gap.")
        print(f"  Most recent: {momlib.et_str(bypassed_latest) if bypassed_latest else '—'}\n")

    if unstamped:
        print(f"── Uninstrumented ({unstamped}) — door NOT recorded ──\n")
        print(f"  Authored before stamping landed ({STAMPING_LANDED_HUMAN}), when only")
        print("  1 of 5 producers named its door. This is OUR instrumentation gap.")
        print("  ⚠️  It is NOT a decline, a bounce, or a preference. Do not read it as")
        print("      anything about her. It cannot be recovered — the door was never")
        print("      written down — so these records are permanently unattributable")
        print("      to a surface.")
        print(f"  Most recent: {momlib.et_str(unstamped_latest) if unstamped_latest else '—'}\n")

    if stamped and unstamped:
        pct = 100.0 * sum(stamped.values()) / len(recs)
        print(f"── Coverage: {pct:.0f}% of records in range carry a door ──")
        print("   Any share computed across the whole range mixes an instrumented")
        print("   era with an uninstrumented one. Use --since 2026-07-30 for a clean")
        print("   denominator.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
