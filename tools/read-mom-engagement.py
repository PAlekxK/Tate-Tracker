#!/usr/bin/env python3
"""read-mom-engagement.py — what she DID in the app, since the last lap.

`[paul-stated 2026-08-15]`: *"I want us to not limit our signal for Mom's feedback
to the cards and whether she's responded or not, we should also have a clear view
of her logins, clicks, etc. — especially since the last cycle. e.g. she's logged in
6 times since the last cycle, interacted x times with the journal."*

WHY THIS EXISTS — the loop's definition of "signal from Mom" was ARRIVALS ONLY
-----------------------------------------------------------------------------
Every detector in this cycle keys on something LANDING in a record: a confirm
answer, a free-text note, a zone recording, a Guru turn. `mom-cycle-status.py`
says so in its own words — *"nothing unread could be hers."* That is a true
statement about the answer record and a **false one about the app**.

Measured 2026-08-15, with the board reading 🟢 ARMED and nothing waiting: since
lap 3 closed (08-14) her device had **3 sessions across 2 days, 2 jump-strip taps
and 2 card opens** — the first jump-strip taps ever recorded from it. None of that
is an arrival, so none of it could reach any leg of the loop. **A quiet answer
record is not a quiet user**, and the loop could not tell those apart.

The data was never missing. `/api/metrics` has been collecting it for months and
`analyze-fernwood.py` already computes most of it. What was missing is a read
scoped to **her, since the last lap** — the window Paul actually reasons in.

WHAT THIS IS NOT
----------------
⛔ **It does not assert attribution.** `tools/people.json` maps one deviceId to
Mom, established from CONTENT she demonstrably authored — that is the only
evidence class this project accepts, and it is still a **browser bucket, not a
person**. Every heading here says *her device*. If someone else picks up that
phone, this tool has no way to know and does not pretend to.

⛔ **It does not narrate.** Counts only, no story over two data points
(ai-advisor 2026-07-17). At this n a sentence about what she "prefers" is
fiction wearing a number.

⛔ **It is not a verdict.** `read-mom-funnel.py` owns the pre-registered
GROW/HOLD/KILL call on the zone journey. This is the wider behavioural read that
sits underneath it, and it deliberately scores nothing.

⭐ **AND A ZERO IS ONLY READABLE IF THE EVENT WAS LIVE BEFORE THE WINDOW OPENED.**
The 2026-08-04 lesson, applied here rather than restated: an event first fired
after this window began cannot produce a meaningful zero inside it, so those are
listed separately instead of printing as behaviour. See `check-telemetry.py`.

Usage:
    python3 tools/read-mom-engagement.py               # since the last closed lap
    python3 tools/read-mom-engagement.py --pickup      # one line, for session-start
    python3 tools/read-mom-engagement.py --since 2026-08-01
    python3 tools/read-mom-engagement.py --json
"""
import argparse
import datetime as dt
import importlib.util
import json
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
spec = importlib.util.spec_from_file_location("momlib", os.path.join(HERE, "momlib.py"))
momlib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(momlib)

CYCLE_LOG = os.path.join(ROOT, "MOM-CYCLE-LOG.md")
PEOPLE = os.path.join(HERE, "people.json")

# `## Lap 3 — 2026-08-14 · ✅ CLOSED — …`. Interlap notes deliberately do NOT match:
# a lap boundary is what Paul means by "the last cycle," and a note saying no lap ran
# is the opposite of one.
LAP_RX = re.compile(r"^##\s+Lap\s+(\d+)\s+[—-]\s+(\d{4}-\d{2}-\d{2})", re.M)

# The Almanac's DOM id never followed its rename — same list analyze-fernwood.py reads.
ALMANAC_CARD_IDS = ("card-fieldnotes", "card-almanac", "fieldnotes", "almanac")

# What "interacted with the journal" means, named explicitly so the number is
# checkable rather than a vibe. Guru turns are counted apart from written notes:
# asking a question and recording an observation are different acts.
JOURNAL_EVENTS = {
    "field_note_saved":     "notes saved",
    "entry_revisited":      "entries revisited",
    "entry_starred":        "entries starred",
    "conversation_started": "Guru conversations",
    "conversation_turn":    "Guru turns",
    "input_focused":        "composer opened",
    "input_abandoned":      "composer abandoned",
}

# The asks she is shown, each as offered → viewed → taken. A funnel row with no
# offered count is the failure `jumpstrip_viewed` was added to close: without a
# denominator, "she never tapped" and "it was never on screen" print the same.
ASKS = [
    ("Mama's Perspective queue", "momqueue_offered", "momqueue_viewed",
     ("momqueue_tapped", "momqueue_answered")),
    ("acknowledgment ribbon",    "momack_shown",     None,
     ("momack_tapped", "momack_followed")),
    ("front-door launcher",      "launcher_offered", "launcher_viewed",
     ("launcher_tapped", "launcher_dismissed")),
    ("jump strip",               "jumpstrip_viewed", None,  ("jumpstrip_tapped",)),
    ("plant-check prompt",       "plant_check_prompt_offered", None, ()),
    ("look-for prompt",          "lookfor_offered",  None,  ("lookfor_tapped",)),
]

LOOKBACK_DAYS = 60   # for "was this event ever live BEFORE the window?"


def last_lap():
    """(lap number, YYYY-MM-DD) of the most recent lap in the chronicle, or None."""
    try:
        with open(CYCLE_LOG, encoding="utf-8") as f:
            laps = LAP_RX.findall(f.read())
    except OSError:
        return None
    if not laps:
        return None
    return max(laps, key=lambda p: p[1])


def her_devices():
    """Device ids people.json maps to Mom. A bucket, never a claim about a person."""
    try:
        with open(PEOPLE, encoding="utf-8") as f:
            people = json.load(f).get("people") or []
    except (OSError, ValueError):
        return []
    return [d for p in people if p.get("name") == "mom" for d in (p.get("deviceIds") or [])]


def collect(data, hers, window_start):
    """Split /api/metrics into her events and everyone else's, keeping both.

    `first_seen` spans the whole LOOKBACK (that is what makes a zero readable);
    `mine` and `others` are both clamped to the WINDOW, so the two counts printed
    beside each other cover the same days. They did not on the first cut, and an
    other-devices figure silently spanning 60 days beside a 2-day one of hers is
    exactly the kind of mismatched denominator this loop keeps getting caught by.
    """
    mine, others, first_seen = [], 0, {}
    for day, batches in (data.get("days") or {}).items():
        for b in batches or []:
            dev = (b.get("device") or {}).get("deviceId")
            for e in (b.get("events") or []):
                t = e.get("type")
                ts = e.get("ts") or day
                if t and (t not in first_seen or ts < first_seen[t]):
                    first_seen[t] = ts
                if day < window_start:
                    continue
                if dev in hers:
                    mine.append(dict(e, _ts=ts, _day=day))
                else:
                    others += 1
    return mine, others, first_seen


def sessions_of(events):
    """[(startTs, durationSec|None)] — a 'login' here is an app open, nothing more."""
    starts, durations = {}, {}
    for e in events:
        sid = e.get("sessionId") or e.get("_ts")
        if e.get("type") == "session_start":
            starts.setdefault(sid, e["_ts"])
        elif e.get("type") == "session_end":
            durations[sid] = e.get("durationSec")
    return sorted((ts, durations.get(sid)) for sid, ts in starts.items())


def build(window_start, hers, token):
    end_d = dt.date.today() + dt.timedelta(days=1)
    # The Worker caps a metrics range at 90 days and answers 400 — not an empty
    # result — past it. Clamp here so a wide `--since` degrades to a shorter
    # lookback (which only weakens the zero-readability flag) instead of failing
    # the whole read. A tool that returns nothing looks exactly like no activity.
    lookback_d = max(dt.date.fromisoformat(window_start) - dt.timedelta(days=LOOKBACK_DAYS),
                     end_d - dt.timedelta(days=89))
    data = momlib._get("/api/metrics", token,
                       {"start": lookback_d.isoformat(), "end": end_d.isoformat()})

    mine, others, first_seen = collect(data, hers, window_start)

    ev = Counter(e["type"] for e in mine if e.get("type"))
    cards = Counter()
    sections = Counter()
    # ⭐ HOW DEEP DID SHE GO (added 2026-08-24, mom-cycle lap 5).
    # `card_expanded` is depth 1. Two signals go deeper and NEITHER was printed
    # by any tool: `subtab_switched` (depth 2 — which of the six wildlife rooms,
    # which plants view) was read only by analyze-fernwood.py and read with the
    # WRONG FIELD NAMES so its branch was dead; `detail_opened` (depth 3 — an
    # individual species) shipped lap 3 specifically to see inside cards and was
    # read by **zero** tools, reachable only via --json.
    #
    # It matters because every "no evidence she goes deep" claim in this repo —
    # including the ones sizing the nested-width work — was standing on signals
    # nobody printed. An unprinted signal and an absent one are the same zero to
    # a reader, which is this project's oldest recurring failure.
    subtabs = Counter()
    details = Counter()
    for e in mine:
        if e["type"] == "card_expanded":
            cards[(e.get("cardId") or "?", e.get("via") or "?")] += 1
        elif e["type"] == "card_section_viewed":
            sections[e.get("cardId") or "?"] += 1
        elif e["type"] == "subtab_switched":
            subtabs[(e.get("card") or "?", e.get("subtab") or "?")] += 1
        elif e["type"] == "detail_opened":
            details[(e.get("kind") or "?", e.get("id") or "?")] += 1

    # Events whose FIRST EVER firing (any device) postdates the window — their zeros
    # inside it are unmeasured, not behavioural.
    unreadable = sorted(t for t, ts in first_seen.items() if ts[:10] >= window_start)

    return {
        "window_start": window_start,
        "sessions": sessions_of(mine),
        "active_days": sorted({e["_day"] for e in mine}),
        "events": ev,
        "cards": cards,
        "sections": sections,
        "subtabs": subtabs,
        "details": details,
        "journal": {k: ev.get(k, 0) for k in JOURNAL_EVENTS},
        "almanac_opens": sum(n for (c, _), n in cards.items() if c in ALMANAC_CARD_IDS),
        "other_device_events": others,
        "unreadable_zeros": unreadable,
        "total_events": sum(ev.values()),
    }


def report(r, lap):
    n_s, n_d = len(r["sessions"]), len(r["active_days"])
    since = f"lap {lap[0]} ({lap[1]})" if lap else r["window_start"]
    print(f"🌿 Mom engagement — since {since}")
    print(f"   her device per tools/people.json — a browser bucket, not a person.\n"
          f"   {r['other_device_events']} event(s) from every other device are not counted here.\n")

    print(f"  SESSIONS — an app open (there is no login)")
    print(f"    {n_s} session(s) across {n_d} active day(s)")
    for ts, dur in r["sessions"]:
        d = f"{int(dur)}s" if dur is not None else "—"
        print(f"      {momlib.et_str(ts)}   {d}")
    if not n_s:
        print("      none")

    print(f"\n  WHAT SHE OPENED — {sum(r['cards'].values())} card open(s)")
    for (card, via), n in r["cards"].most_common():
        print(f"      {card:22} {n}   (via {via})")
    if not r["cards"]:
        print("      none")
    if r["sections"]:
        print("    scrolled into view: "
              + ", ".join(f"{c} {n}" for c, n in r["sections"].most_common()))

    # ⭐ HOW DEEP — the two signals nothing printed until 2026-08-24. Depth 1 is
    # the card open above; these are 2 and 3. A zero here is reported as a zero
    # and dated by the unreadable-zeros block below, never left as a blank.
    print(f"\n  HOW DEEP SHE WENT — past the card face")
    print(f"    depth 2 · a room inside a card (subtab_switched) — {sum(r['subtabs'].values())}")
    for (card, tab), n in r["subtabs"].most_common():
        print(f"      {card} → {tab:20} {n}")
    if not r["subtabs"]:
        print("      none in this window")
    print(f"    depth 3 · one individual opened (detail_opened) — {sum(r['details'].values())}")
    for (kind, ident), n in r["details"].most_common(8):
        print(f"      {kind}: {ident:22} {n}")
    if not r["details"]:
        print("      none in this window")

    print(f"\n  THE JOURNAL — {r['almanac_opens']} card open(s)")
    for k, label in JOURNAL_EVENTS.items():
        n = r["journal"].get(k, 0)
        if n:
            print(f"      {label:22} {n}")
    if not any(r["journal"].values()):
        print("      no journal interaction in this window")

    print("\n  THE ASKS — offered → viewed → taken")
    for label, offered, viewed, taken in ASKS:
        o = r["events"].get(offered, 0)
        v = r["events"].get(viewed, 0) if viewed else None
        parts = [f"{o} offered"]
        if viewed:
            parts.append(f"{v} viewed")
        for t in taken:
            parts.append(f"{r['events'].get(t, 0)} {t.split('_', 1)[1]}")
        print(f"      {label:26} " + " → ".join(parts))

    if r["unreadable_zeros"]:
        print("\n  ⚠️ FIRST EVER FIRED INSIDE THIS WINDOW — a zero on these is UNMEASURED,")
        print("     not 'it did not happen'. They were not live for the whole window.")
        for t in r["unreadable_zeros"]:
            print(f"      · {t}")

    print("\n  Read this beside — never instead of — the answer record:")
    print("     read-mom-feedback.py (what she settled) · read-mom-funnel.py (the zone-journey verdict)")
    print("  It scores nothing and asserts nothing about a person. Counts only.")


def main():
    ap = argparse.ArgumentParser(description="What Mom's device DID, since the last lap.")
    ap.add_argument("--since", help="YYYY-MM-DD; overrides the lap boundary")
    ap.add_argument("--pickup", action="store_true", help="one line, for the session-start block")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    lap = last_lap()
    window_start = a.since or (lap[1] if lap else
                               (dt.date.today() - dt.timedelta(days=14)).isoformat())
    # An explicit --since is NOT the lap boundary, and every heading below reads off
    # `lap`. Labelling a hand-picked window "since lap 3" would put the wrong
    # denominator on a real number — the failure mode this whole file is about.
    if a.since:
        lap = None

    hers = her_devices()
    if not hers:
        print("⛔ tools/people.json maps no device to Mom — nothing to read.", file=sys.stderr)
        return 1

    tok = momlib.resolve_token()
    if not tok:
        print("⛔ no token (FERNWOOD_TOKEN or .private/fernwood-token).", file=sys.stderr)
        return 1

    try:
        r = build(window_start, hers, tok)
    except Exception as exc:                       # network/API — say so, never print a silent zero
        print(f"⛔ could not read /api/metrics: {exc}", file=sys.stderr)
        return 1

    if a.json:
        out = dict(r)
        out["events"] = dict(r["events"])
        out["cards"] = {f"{c}|{v}": n for (c, v), n in r["cards"].items()}
        out["sections"] = dict(r["sections"])
        out["lap"] = lap
        print(json.dumps(out, indent=2))
        return 0

    if a.pickup:
        # ALWAYS one line, quiet windows included — the counter rule. A silent watcher
        # and a dead one must never print the same thing.
        since = f"lap {lap[0]}" if lap else f"since {window_start}"
        j = sum(r["journal"].get(k, 0) for k in ("field_note_saved", "entry_revisited",
                                                 "conversation_turn"))
        print(f"📈 Her app use — {len(r['sessions'])} session(s) / {len(r['active_days'])} day(s) "
              f"since {since} · {sum(r['cards'].values())} card open(s) · {j} journal interaction(s)"
              f"   [device bucket, not a person]")
        return 0

    report(r, lap)
    return 0


if __name__ == "__main__":
    sys.exit(main())
