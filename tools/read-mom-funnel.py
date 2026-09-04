#!/usr/bin/env python3
"""read-mom-funnel.py — read the Mom-engagement funnel from /api/metrics.

Makes the zone-journey + confirm-queue signals LEGIBLE. The front-door voice walk
(shipped 2026-07-17) fires a funnel of structural events; this reads them back and
computes the H1-H5 hypotheses + a deterministic GROW/HOLD/KILL verdict on
pre-registered counts. READ-ONLY: never writes canon, never dirties the repo.

Deliberately NOT an AI narrative (ai-advisor 2026-07-17: at low n, script the
verdict, don't narrate a story over two data points). It prints raw counts; Paul
reads them and makes the call. Design + thresholds:
`.user-research/2026-07-17-zone-journey-panel-synthesis.md` (the H1-H5 register).

Events consumed (MetricsCollector -> /api/metrics; each event is
{type, ts, sessionId, ...fields}, deviceId on the enclosing batch.device):
  Front-door walk : launcher_offered / launcher_viewed / launcher_tapped (mints flowId),
                    flow_zone_picked (flowId, zoneId), flow_closed (flowId, completed, saveResult)
  Capture         : zone_audio_started / zone_audio_saved (zoneId, durationMs, flowId?),
                    zone_tapped (the map path)
  Confirm queue   : momqueue_offered / momqueue_viewed / momqueue_tapped / momqueue_answered
A zone_audio_saved WITHOUT a flowId = an organic map capture (not via the card) -> H1.

Caveats it prints, never hides:
  - Attribution (rewritten 2026-07-28, CLEAN SLATE). Two things used to make a deviceId
    unusable as a person, and both are closed: Paul shared his phone with Mom (ended by
    his decision 2026-07-28), and people.json had the mapping BACKWARDS — his builder
    device was recorded as Mom's, so his own app-opens were counted as her engagement.
    Corrected against authored content: every one of Mom's four real inputs is on
    d-szqlt0h7. Builder devices are now dropped deterministically via people.json
    `excludeFromEngagement`, not via the localStorage flag, which had to be re-set on
    every browser and therefore never was. The exclusion count prints on every run.
    ⚠ Nothing before 2026-07-28 is comparable to what comes after — do not splice them.
  - The "non-gimme answer" half of GROW lives in the ANSWER content (/api/feedback,
    read by read-mom-feedback.py), not the funnel. This tool reports engagement +
    returns; combine with read-mom-feedback for the full Grow call.

Token: FERNWOOD_TOKEN env or .private/fernwood-token (same as the other tools).

Usage:
    python3 tools/read-mom-funnel.py                     # full scorecard, ship-date -> today
    python3 tools/read-mom-funnel.py --pickup            # one line; silent if no data (session-start)
    python3 tools/read-mom-funnel.py --json
    python3 tools/read-mom-funnel.py --start 2026-07-17 --end 2026-08-14
    python3 tools/read-mom-funnel.py --notify --state-file <path>   # for the launchd watcher
"""
import argparse
import datetime as dt
import importlib.util
import json
import os
import subprocess
import sys


def _register_people():
    """The people register WITH device ids — merged by momlib from the private sibling
    (C5 8a, 2026-09-03). The public tools/people.json no longer carries ids; a direct read
    would exclude nobody and map nobody, silently."""
    import importlib.util, os as _os
    spec = importlib.util.spec_from_file_location("momlib", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "momlib.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m._people()[0]


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

# The front-door voice walk shipped 2026-07-17 — the 4-week time-box starts here.
# ⭐ TIME-BOX ANCHORED TO HER FIRST CONFIRM (Paul, 2026-07-28).
#
# 2026-07-13 is the day Mom answered her first confirm card (crocosmia 'Lucifer', then the
# white mophead) — the first act in the record that is unambiguously hers. The box starts
# there and counts only what SHE does.
#
# Why this is the right anchor, and why an earlier reset here was wrong: the contamination
# was never about DATES, it was about DEVICES. tools/people.json had Paul's builder device
# recorded as Mom's, so his app-opens were counted as her engagement — that is what produced
# "0 launcher taps in nine days" and "declined 33 of 33," neither of which reproduces. The
# deterministic `excludeFromEngagement` drop below is the actual fix. Restarting the clock at
# 2026-07-28 (the first attempt) ALSO threw away her genuine 07-13 and 07-19 confirms to
# escape contamination the exclusion already removes — over-correction, and it would have
# left the box measuring from zero while real signal sat just behind it.
#
# ⚠ One honest caveat on the early edge: until 2026-07-16 every write path gated on
# per-device pairing, so an UNPAIRED device wrote nothing at all. Her confirms landed, so her
# device was paired — but any activity from an unpaired device of hers in 07-13..07-16 is
# simply absent. That biases this window toward UNDER-counting her, never over-counting.
TIMEBOX_START = "2026-07-13"          # her first confirm answer
TIMEBOX_START_SHIPDATE = "2026-07-17"  # front-door ship date; historical reference only
TIMEBOX_WEEKS = 4


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def iter_events(data):
    """Yield (event, deviceId, date) from the /api/metrics {days:{date:[batch,...]}} shape.
    Event date is taken from event.ts when present (true event time), else the day key."""
    days = (data or {}).get("days") or {}
    for day, batches in days.items():
        if not isinstance(batches, list):
            continue
        for batch in batches:
            if not isinstance(batch, dict):
                continue
            did = ((batch.get("device") or {}).get("deviceId")) or "unknown"
            for ev in (batch.get("events") or []):
                if not isinstance(ev, dict) or not ev.get("type"):
                    continue
                d = day
                ts = ev.get("ts")
                if isinstance(ts, str) and len(ts) >= 10:
                    d = ts[:10]
                yield ev, did, d


def compute(events):
    """events: list of (ev, deviceId, date). Returns the scorecard dict."""
    by_type = {}
    for ev, did, d in events:
        by_type.setdefault(ev["type"], []).append((ev, did, d))

    def n(t):
        return len(by_type.get(t, []))

    # ---- front-door funnel ----
    offered, viewed, tapped = n("launcher_offered"), n("launcher_viewed"), n("launcher_tapped")
    picked = n("flow_zone_picked")

    saved = by_type.get("zone_audio_saved", [])
    saved_via_card = [s for s in saved if (s[0].get("flowId"))]
    saved_organic = [s for s in saved if not s[0].get("flowId")]

    # captures per flow (H2: one-zone vs sweep) — group card-path saves by flowId
    per_flow = {}
    for ev, did, d in saved_via_card:
        per_flow.setdefault(ev.get("flowId"), []).append(ev)
    zones_per_flow = sorted((len(v) for v in per_flow.values()), reverse=True)

    durations = [ev.get("durationMs") for ev, _, _ in saved if isinstance(ev.get("durationMs"), (int, float))]

    # H3: of flows that tapped in, how many produced a saved capture
    tapped_flows = {ev.get("flowId") for ev, _, _ in by_type.get("launcher_tapped", []) if ev.get("flowId")}
    flows_with_save = set(per_flow.keys())
    completed_flows = len(tapped_flows & flows_with_save)

    # H5: distinct calendar days a device produced a saved capture (>=2 => a later-day return)
    days_by_device = {}
    for ev, did, d in saved:
        days_by_device.setdefault(did, set()).add(d)
    returners = {did: sorted(ds) for did, ds in days_by_device.items() if len(ds) >= 2}

    # ---- confirm queue (Mama's Perspective) ----
    mq = {k: n("momqueue_" + k) for k in ("offered", "viewed", "tapped", "answered")}

    # ---- the jump strip ("the tabs across the top") ----
    # ⭐ ADDED 2026-08-04, and the gap it closes is the point. The strip shipped
    # 08-02 with TAPS-ONLY instrumentation — the only major control in the app
    # without an impression event, while momqueue and launcher both have
    # offered/viewed/tapped. So when Mom told Paul she had "seen the tabs at the
    # top and liked them", that was literally unmeasurable, and a zero tap count
    # could not be told apart from a zero VIEW count. `jumpstrip_viewed` (fires
    # once per session at 50% visibility) is the denominator.
    #
    # ⚠️ READ THE SPLIT HONESTLY, BOTH WAYS:
    #   viewed 0            → we cannot say anything. Not evidence against it.
    #   viewed > 0, tapped 0 → she sees it and does not use it. THAT is a finding,
    #                          and it is the first time this funnel can produce it.
    # ⚠️ AND THE LINE IS NOT POOLABLE. The strip was rebuilt 2026-08-04 around her
    # own five categories, with bigger type and real 44px targets replacing a row
    # whose overlapping hit bands stole taps. Counts before and after that commit
    # measure different controls — do not sum across it.
    strip = {"viewed": n("jumpstrip_viewed"), "tapped": n("jumpstrip_tapped")}
    # The first-ever firing travels WITH the count, so no reader has to take a zero
    # on trust. An event that has never fired makes its zero uninformative.
    for k in ("viewed", "tapped"):
        stamps = sorted(e.get("ts") for e, _dv, _dy in by_type.get("jumpstrip_" + k, []) if e.get("ts"))
        strip["first_" + k] = stamps[0] if stamps else None
    strip["targets"] = {}
    for ev, _did, _d in by_type.get("jumpstrip_tapped", []):
        t = ev.get("target") or "?"
        strip["targets"][t] = strip["targets"].get(t, 0) + 1

    # ---- deterministic verdict (raw counts; no narrative) ----
    # KILL  = offered a lot, never tapped (dead affordance).
    # GROW* = a real capture AND a later-day return (the funnel half of Grow; the
    #         non-gimme-answer half is in read-mom-feedback).
    # HOLD  = everything between (honest default at low n).
    total_saves = len(saved)
    if (offered >= 8 or mq["offered"] >= 8) and tapped == 0 and mq["tapped"] == 0:
        verdict = "KILL-candidate (offered, never tapped — dead affordance)"
    elif total_saves >= 1 and returners:
        verdict = "GROW-candidate (a capture AND a later-day return) — confirm the answer was non-gimme via read-mom-feedback.py"
    else:
        verdict = "HOLD (not enough signal — n is low; one episode is not validation)"

    return {
        "front_door": {
            "offered": offered, "viewed": viewed, "tapped": tapped,
            "zone_picked": picked,
            "saved_total": total_saves,
            "saved_via_card": len(saved_via_card), "saved_organic": len(saved_organic),
            "completed_flows_tapped_to_saved": completed_flows,
            "tapped_flows": len(tapped_flows),
        },
        "H1_invitation_required": {
            "via_card": len(saved_via_card), "organic": len(saved_organic),
            "read": "card >> organic supports H1 (she needs the invitation)"
        },
        "H2_one_zone_vs_sweep": {
            "captures_per_flow": zones_per_flow,
            "read": "mostly 1 (occasional 2) => one-zone; routine 4-5 => sweep-appetite is real"
        },
        "H3_gate_lifts_completion": {
            "tapped_flows": len(tapped_flows), "completed": completed_flows,
            "rate": round(completed_flows / len(tapped_flows), 2) if tapped_flows else None
        },
        "H5_later_day_return": {
            "returning_devices": len(returners), "detail": returners,
            "read": "a device saving on >=2 distinct days = a return (proxy — shared device)"
        },
        "duration_ms": {
            "count": len(durations),
            "median": sorted(durations)[len(durations) // 2] if durations else None,
        },
        "confirm_queue": mq,
        "jump_strip": strip,
        "per_device_saves": {did: sorted(ds) for did, ds in days_by_device.items()},
        "verdict": verdict,
        "totals": {"saves": total_saves, "launcher_taps": tapped, "confirm_answers": mq["answered"]},
    }


def scorecard_text(sc, start, end):
    fd = sc["front_door"]
    lines = []
    lines.append(f"Mom-engagement funnel  ·  {start} → {end}")
    lines.append("=" * 52)
    # Print the denominator on every run. A tool that quietly excludes nothing reads exactly
    # like a tool that correctly excluded everything — that ambiguity is what let builder
    # testing masquerade as Mom's engagement for 26 days (clean slate 2026-07-28).
    exc = sc.get("_excluded") or {}
    if exc.get("devices"):
        lines.append(f"  [excluding {len(exc['devices'])} builder device(s); "
                     f"{exc['events_dropped']} event(s) dropped]")
    else:
        lines.append("  [⚠ NO device exclusion applied — builder testing may be inflating this]")
    for did in (exc.get("unmapped_devices") or []):
        lines.append(f"  [⚠ UNMAPPED device counted as Mom: {did} — if it is yours, "
                     f"add it to people.json paul.deviceIds]")
    lines.append("FRONT-DOOR WALK (zone journey)")
    lines.append(f"  offered {fd['offered']} → viewed {fd['viewed']} → tapped {fd['tapped']} "
                 f"→ zone-picked {fd['zone_picked']} → SAVED {fd['saved_total']}")
    lines.append(f"  saves via the card: {fd['saved_via_card']}   organic (map): {fd['saved_organic']}   [H1]")
    h3 = sc["H3_gate_lifts_completion"]
    lines.append(f"  tap→save completion: {h3['completed']}/{h3['tapped_flows']}"
                 + (f" ({int(h3['rate']*100)}%)" if h3["rate"] is not None else "") + "   [H3]")
    cpf = sc["H2_one_zone_vs_sweep"]["captures_per_flow"]
    lines.append(f"  zones per walk: {cpf or '—'}   [H2: 1s=one-zone, 4-5s=sweep-appetite]")
    dm = sc["duration_ms"]
    lines.append(f"  recordings: {dm['count']}   median length: "
                 + (f"{round(dm['median']/1000,1)}s" if dm["median"] else "—"))
    h5 = sc["H5_later_day_return"]
    lines.append(f"  later-day returns: {h5['returning_devices']} device(s)   [H5 — the Grow keystone]")
    if h5["detail"]:
        for did, days in h5["detail"].items():
            lines.append(f"    · {did[:16]}…: {', '.join(days)}")
    js = sc.get("jump_strip") or {"viewed": 0, "tapped": 0, "targets": {}}
    print("THE TABS ACROSS THE TOP (jump strip)")
    if not js["viewed"] and not js["tapped"]:
        print("  no data — impression tracking shipped 2026-08-04; before that only taps existed,")
        print("  so an empty reading here means UNMEASURED, never 'she did not look'.")
    else:
        print(f"  viewed {js['viewed']} → tapped {js['tapped']}")
        if js["viewed"] and not js["tapped"]:
            print("  ⚠️ SEEN BUT NOT USED — the one reading this funnel could never produce before.")
        for t, c in sorted(js.get("targets", {}).items(), key=lambda kv: -kv[1]):
            print(f"     {c:3d}  {t}")
    print(f"  first tap ever seen : {js.get('first_tapped') or 'NONE — any tap-zero here is UNMEASURED'}")
    print(f"  first view ever seen: {js.get('first_viewed') or 'NONE — impressions still unmeasured'}")
    print("  ⚠️ do NOT pool across 2026-08-04 — the strip was rebuilt (her categories, 44px targets).")
    print()

    mq = sc["confirm_queue"]
    lines.append("")
    lines.append("CONFIRM QUEUE (Mama's Perspective)")
    lines.append(f"  offered {mq['offered']} → viewed {mq['viewed']} → tapped {mq['tapped']} "
                 f"→ answered {mq['answered']}")
    lines.append("")
    lines.append(f"VERDICT: {sc['verdict']}")
    lines.append("  (funnel only — combine with read-mom-feedback.py for the non-gimme-answer half;")
    lines.append("   builder devices excluded by deviceId; phone-sharing ended 2026-07-28, so")
    lines.append("   a stray Paul-on-her-phone session before that date is possible but unflagged.)")
    return "\n".join(lines)


def notify_macos(title, body):
    try:
        subprocess.run(
            ["osascript", "-e",
             f"display notification {json.dumps(body)} with title {json.dumps(title)}"],
            check=False, capture_output=True, timeout=15)
    except Exception:
        pass


ROTATION_THRESHOLD = 3          # distinct offered-days at the head slot without an answer

# Event first-fired dates. A stint predating one of these publishes "?", never 0 —
# the same rule mom-cycle-status.py follows. UNMEASURED is not zero.
INSTRUMENTATION = {
    "momqueue_offered": "2026-07-13",
    "momqueue_answered": "2026-07-13",
    "momqueue_viewed": "2026-07-19",
    "momqueue_tapped": "2026-07-19",
    "momqueue_tapped.choice": "2026-08-27",   # which control she pressed
}


def rotation_rows(events, excluded, qs_by_id, season_of):
    """Per-card head-slot exposure. REPORT ONLY — it computes, it never writes.

    THE UNIT IS A DISTINCT OFFERED-DAY AT THE HEAD SLOT, not a raw offer.
    `q-weed-stiltgrass` has 13 offers across far fewer days; a render fires an
    offer and she opens the app repeatedly in a day. 13 offers is not 13 decisions.

    TWO PRE-CONDITIONS, and the first is the one that matters:
     ① UNANSWERABLE != DECLINED. A day the card was out-of-season does not count.
        q-clematis-variety is the worked example — 7 offers, 7 views, 0 taps, and
        the honest reading is NOT "she is bored of this card", it is "we asked her
        to read a flower colour on a vine that had no flowers". A naive
        no-response-after-N rule gets that card right for the wrong reason and
        writes the wrong reason into a record that outlives the reasoning.
     ② HEAD-SLOT ONLY. A card accrues a day only on a day it actually fired
        momqueue_offered. No exposure, no evidence, no aging — this is what stops
        the cards she has never seen from silently aging off.
    """
    import collections as _c
    days = _c.defaultdict(set)
    offers = _c.Counter()
    taps = _c.defaultdict(_c.Counter)
    answered_on = {}
    her_sessions = set()
    positions = _c.Counter()

    for ev, dev, date in events:
        if dev in excluded:
            continue
        t_ = ev.get("type", "")
        if t_ == "session_start":   # verified present: 148 in window. Do not add a
            #                          second name here without checking it fires.
            her_sessions.add(date)
        if not t_.startswith("momqueue_"):
            continue
        qid = ev.get("questionId")
        if not qid:
            continue
        if t_ == "momqueue_offered":
            pos = ev.get("position")
            positions[pos] += 1
            # position is None for pre-instrumentation events; those were the
            # single rendered card too, so they count as head.
            if pos in (0, None):
                days[qid].add(date)
                offers[qid] += 1
        elif t_ == "momqueue_tapped":
            taps[qid][ev.get("choice") or "unrecorded"] += 1
        elif t_ == "momqueue_answered":
            answered_on[qid] = min(answered_on.get(qid, date), date)

    rows = []
    for qid, dayset in days.items():
        q = qs_by_id.get(qid) or {}
        # ① drop days the card could not be answered on
        countable = sorted(d for d in dayset if season_of(qid, d) in ("in-season", "season-free", "unknown"))
        dropped = len(dayset) - len(countable)
        rows.append({
            "questionId": qid,
            "offeredDays": len(countable),
            "daysDroppedUnanswerable": dropped,
            "offers": offers[qid],
            "taps": dict(taps[qid]),
            "answeredOn": answered_on.get(qid),
            "live": q.get("active") is True,
            "firstDay": min(dayset) if dayset else None,
            "lastDay": max(dayset) if dayset else None,
            "due": (q.get("active") is True
                    and qid not in answered_on
                    and len(countable) >= ROTATION_THRESHOLD),
        })
    rows.sort(key=lambda r: (-r["offeredDays"], r["questionId"]))
    return rows, positions, len(her_sessions)


def rotation_text(rows, positions, n_session_days, bench_ready):
    out = []
    out.append(f"CARD ROTATION — head-slot exposure  ·  threshold {ROTATION_THRESHOLD} offered-days")
    out.append("")
    head = sum(v for k, v in positions.items() if k in (0, None))
    deep = sum(v for k, v in positions.items() if k not in (0, None))
    out.append(f"  she was offered a card {head + deep} time(s): {head} at the HEAD slot, {deep} deeper in the queue.")
    if deep == 0 and head:
        out.append("  ⭐ SHE HAS NEVER SEEN A CARD PAST THE HEAD. 'Another question ›' has never been")
        out.append("     tapped on her device, so every card below the first has had ZERO exposure —")
        out.append("     that is not zero response, and the two must never be read the same way.")
    out.append("")
    out.append(f"  {'questionId':<40}{'days':>6}{'offers':>8}  {'answered':<12}taps")
    for r in rows:
        mark = "⚡" if r["due"] else ("✓" if r["answeredOn"] else " ")
        tap = ", ".join(f"{k}×{v}" for k, v in sorted(r["taps"].items())) or "—"
        ans = r["answeredOn"] or "—"
        out.append(f"{mark} {r['questionId']:<40}{r['offeredDays']:>6}{r['offers']:>8}  {ans:<12}{tap}")
        if r["daysDroppedUnanswerable"]:
            out.append(f"    ↳ {r['daysDroppedUnanswerable']} day(s) NOT counted — the card was unanswerable then "
                       f"(out of season). Unanswerable is not declined.")
    due = [r for r in rows if r["due"]]
    out.append("")
    if not due:
        out.append("  nothing is due to rotate.")
    else:
        for r in due:
            out.append(f"  ⚡ {r['questionId']} is DUE to rotate "
                       f"({r['offeredDays']} offered-days, {r['firstDay']} → {r['lastDay']}, no answer)")
            if bench_ready:
                out.append(f"     replacement available on the bench: {', '.join(bench_ready)}")
            else:
                # This is the supply signal, and it costs Mom nothing.
                out.append("     ⛔ NOTHING APPROVED ON THE BENCH TO REPLACE IT — so do not rotate.")
                out.append("        Rotating with no swap shrinks her queue below cap, which violates")
                out.append("        five-stays-five outright. This is a SUPPLY signal for Paul, not a")
                out.append("        card problem: clear one with rationalize-bench.py --approve <id>.")
    out.append("")
    out.append("  REPORT ONLY — this writes nothing. Rotation becomes a write only after")
    out.append("  three clean laps (see .user-research/2026-08-27-card-rotation.md §1.4).")
    out.append("")
    out.append("  INSTRUMENTATION (a stint predating an event is UNMEASURED, never 0):")
    for k, v in INSTRUMENTATION.items():
        out.append(f"    {k:<28} first available {v}")
    out.append(f"  Her active days in window: {n_session_days}. Rotation runs on HER cadence —")
    out.append("  a quiet stretch produces no aging, because she has declined nothing.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Read the Mom-engagement funnel (read-only).")
    ap.add_argument("--start", default=TIMEBOX_START, help="YYYY-MM-DD (default: front-door ship date)")
    ap.add_argument("--end", default=None, help="YYYY-MM-DD (default: today)")
    ap.add_argument("--pickup", action="store_true", help="One line; silent if no funnel data yet")
    ap.add_argument("--json", action="store_true", help="Emit the scorecard as JSON")
    ap.add_argument("--rotation", action="store_true",
                    help="Head-slot exposure per card + what is due to rotate (report only)")
    ap.add_argument("--write-log", action="store_true",
                    help="with --rotation: write data/card-rotation-log.json (the RECORD, not a verdict)")
    ap.add_argument("--notify", action="store_true", help="macOS notification when the verdict-state advances")
    ap.add_argument("--state-file", default=os.path.join(ROOT, ".private", "mom-funnel-watch-state.json"))
    args = ap.parse_args()

    end = args.end or dt.date.today().isoformat()

    rmf = _load("rmf", os.path.join(HERE, "read-mom-feedback.py"))
    token = rmf.resolve_token()
    if not token:
        if not args.pickup:
            print("No token (FERNWOOD_TOKEN / .private/fernwood-token) — can't read metrics.", file=sys.stderr)
        return 0

    try:
        data = rmf._get("/api/metrics", token, {"start": args.start, "end": end})
    except Exception as e:  # offline / Worker down — a watcher must not crash-loop
        if not args.pickup:
            print(f"Couldn't read /api/metrics: {e}", file=sys.stderr)
        return 0

    events = list(iter_events(data))

    if args.rotation:
        excluded = set()
        try:
            for person in _register_people():
                if person.get("excludeFromEngagement"):
                    excluded.update(person.get("deviceIds") or [])
                    if person.get("deviceId"):
                        excluded.add(person["deviceId"])
        except Exception as e:
            print(f"⛔ cannot read people.json ({e}) — refusing to report numbers that")
            print("   would silently include the builder's own devices.")
            return 2

        ml = _load("momlib", os.path.join(HERE, "momlib.py"))
        qdoc = json.load(open(os.path.join(ROOT, "questions.json")))
        qs = qdoc["questions"] if isinstance(qdoc, dict) else qdoc
        by_id = {q.get("id"): q for q in qs}
        canon = ml.canon()

        def season_of(qid, daystr):
            q = by_id.get(qid)
            if not q:
                return "unknown"
            try:
                return ml.in_season(q, canon, dt.date.fromisoformat(daystr))["verdict"]
            except Exception:
                return "unknown"

        bench_ready = []
        for q in qs:
            if q.get("active") is not True and q.get("approvedForServe"):
                v = season_of(q.get("id"), end)
                if v in ("in-season", "season-free"):
                    bench_ready.append(q["id"])

        rows, positions, nsess = rotation_rows(events, excluded, by_id, season_of)
        print(rotation_text(rows, positions, nsess, bench_ready))

        if args.write_log:
            # THE RECORD, not the verdict. It states what was offered and what came
            # back; it never says what that MEANS. The verdict is dated, human-authored
            # and lives in MOM-CYCLE-LOG.md — see §2.2 of the research file.
            #
            # ⚠ `rotated` and `answered` are different outcomes and MUST NOT MERGE.
            #   A rotated card is UNANSWERED, not handled: no resolvedAt is written
            #   anywhere by this path, and it must never release the feedback
            #   watermark. If rotation ever writes a resolution, a real question of
            #   hers disappears silently — the worst failure class in this repo.
            log_path = os.path.join(ROOT, "data", "card-rotation-log.json")
            stints = []
            for r in rows:
                q = by_id.get(r["questionId"]) or {}
                if r["answeredOn"]:
                    outcome = "answered"
                elif q.get("_seasonHold") or q.get("benchedAt"):
                    outcome = "season-hold"
                elif q.get("resolvedAt") or q.get("resolution"):
                    outcome = "retired"
                elif r["due"]:
                    outcome = "due-to-rotate"
                elif q.get("active") is True:
                    outcome = "open"
                else:
                    outcome = "superseded"
                pre = r["firstDay"] and r["firstDay"] < INSTRUMENTATION["momqueue_tapped"]
                stints.append({
                    "questionId": r["questionId"],
                    "class": q.get("kind"),
                    "answerCost": q.get("answerCost", "?"),
                    "seededFrom": q.get("seededFrom") or ("our-uncertainty-marker"
                                                          if q.get("_source") == "harvest" else "?"),
                    "enteredHeadAt": r["firstDay"],
                    "leftHeadAt": r["answeredOn"] or (None if q.get("active") is True else r["lastDay"]),
                    "offeredDays": r["offeredDays"],
                    "daysDroppedUnanswerable": r["daysDroppedUnanswerable"],
                    "offers": r["offers"],
                    # "?" not 0 — the count is UNMEASURED for stints predating the event.
                    "taps": r["taps"] if not pre else "?",
                    "herActiveDaysInWindow": nsess,
                    "outcome": outcome,
                    "seasonVerdictAtExit": season_of(r["questionId"], end),
                    "replacedBy": None,
                    "windowNote": ("stint predates momqueue_tapped (2026-07-19); tap counts "
                                   "are UNMEASURED, not zero" if pre else None),
                })
            doc = {
                "_meta": {
                    "purpose": "One row per head-slot STINT. THE RECORD, never the verdict — "
                               "it says what was offered and what came back, never what it means. "
                               "Verdicts are dated and human-authored in MOM-CYCLE-LOG.md.",
                    "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
                    "generated_by": "tools/read-mom-funnel.py --rotation --write-log",
                    "window": {"start": args.start, "end": end},
                    "rotationThreshold": ROTATION_THRESHOLD,
                    "outcomeValues": ["answered", "rotated", "due-to-rotate", "season-hold",
                                      "retired", "superseded", "edited", "open"],
                    "warning": "`rotated` != `answered`. A rotated card is UNANSWERED. "
                               "Nothing here may release the feedback watermark.",
                },
                "_instrumentation": INSTRUMENTATION,
                "_caveats": [
                    "A deviceId is a browser bucket, not a person.",
                    "Counts are single-digit; a pattern here is a reason to look, not a finding.",
                    "She has never tapped past the head slot, so cards below position 0 have "
                    "ZERO EXPOSURE — which is not zero response.",
                ],
                "stints": stints,
            }
            with open(log_path, "w", encoding="utf-8") as fh:
                json.dump(doc, fh, indent=2, ensure_ascii=False)
                fh.write("\n")
            print(f"\n✓ wrote {log_path} — {len(stints)} stint(s)")
        return 0

    # ⭐ 2026-07-28 — EXCLUDE THE BUILDER'S OWN DEVICES DETERMINISTICALLY.
    # The old design relied on a localStorage flag (tateTracker.metricsExclude, viewer.html)
    # being set on every browser Paul ever tested from. It never was, so his app-opens were
    # counted as engagement — and because people.json ALSO had the device mapping backwards,
    # they were counted as MOM's. That produced the two figures that drove real decisions
    # ("0 taps", "33/33 declines"), neither of which reproduces. A flag that must be re-set
    # per browser is a flag that will be missed; the map is the durable place for this.
    excluded = set()
    try:
        for person in _register_people():
            if person.get("excludeFromEngagement"):
                excluded.update(person.get("deviceIds") or [])
    except Exception:
        excluded = set()   # absent/broken map -> exclude nothing, and say so below
    dropped = [t for t in events if t[1] in excluded]
    if excluded:
        events = [t for t in events if t[1] not in excluded]

    # Any device in neither list is UNMAPPED, and silence about it is the failure mode that
    # started all this. An unmapped device is either a new device of Mom's (its events belong
    # in the numbers) or another browser of Paul's (they must not be) — and nothing here can
    # tell which, so the tool NAMES it and lets Paul answer instead of quietly picking.
    known = set(excluded)
    try:
        for person in _register_people():
            known.update(person.get("deviceIds") or [])
    except Exception:
        pass
    unmapped = sorted({t[1] for t in events if t[1] not in known and t[1] != "unknown"})

    sc = compute(events)
    sc["_excluded"] = {"devices": sorted(excluded), "events_dropped": len(dropped),
                       "unmapped_devices": unmapped,
                       "note": ("builder devices excluded via people.json excludeFromEngagement"
                                if excluded else
                                "NO device exclusion applied — people.json unreadable or no "
                                "device is flagged excludeFromEngagement. Builder testing may "
                                "be inflating these numbers.")}
    tot = sc["totals"]

    # Days into the time-box (for context on how much signal to expect)
    try:
        started = dt.date.fromisoformat(args.start)
        day_n = (dt.date.fromisoformat(end) - started).days + 1
        weeks_left = max(0, TIMEBOX_WEEKS - (day_n / 7.0))
    except ValueError:
        day_n, weeks_left = None, None

    if args.pickup:
        if not events:
            return 0  # silent — no signal yet, matches the calm session-start tone
        print(f"Mom funnel: {tot['saves']} capture(s), {tot['launcher_taps']} launcher tap(s), "
              f"{tot['confirm_answers']} confirm answer(s) — {sc['verdict'].split('(')[0].strip()}")
        return 0

    if args.json:
        print(json.dumps(sc, ensure_ascii=False, indent=2))
        return 0

    if args.notify:
        # Fire once per verdict-state advance (dead → tapped → captured → returned).
        state = {}
        try:
            state = json.load(open(args.state_file, encoding="utf-8"))
        except (FileNotFoundError, ValueError):
            pass
        stage = ("returned" if sc["H5_later_day_return"]["returning_devices"] else
                 "captured" if tot["saves"] else
                 "tapped" if tot["launcher_taps"] or sc["confirm_queue"]["tapped"] else
                 "quiet")
        order = {"quiet": 0, "tapped": 1, "captured": 2, "returned": 3}
        prev = state.get("stage", "quiet")
        if order.get(stage, 0) > order.get(prev, 0):
            notify_macos("Fernwood — Mom is engaging",
                         f"{stage}: {tot['saves']} capture(s), {tot['launcher_taps']} tap(s). Run read-mom-funnel.py.")
        state["stage"] = stage
        state["lastRun"] = end
        os.makedirs(os.path.dirname(args.state_file), exist_ok=True)
        json.dump(state, open(args.state_file, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(scorecard_text(sc, args.start, end))
    if day_n is not None:
        print(f"\n(day {day_n} of the {TIMEBOX_WEEKS}-week time-box — ~{weeks_left:.1f} weeks left)")
    if not events:
        print("\nNo funnel events yet — nothing has been recorded on the live surface. "
              "Expected until Mom (or a test on a non-excluded device) hits the front door.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
