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
  - Shared device: Paul shares his phone with Mom (people.json attribution invalid),
    so a per-deviceId "return" is a proxy, not proof it was Mom. Per-device breakdown
    is shown so Paul can eyeball. Set localStorage tateTracker.metricsExclude="1" on
    Paul's own test device to keep builder-testing out of the numbers.
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

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

# The front-door voice walk shipped 2026-07-17 — the 4-week time-box starts here.
TIMEBOX_START = "2026-07-17"
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
        "per_device_saves": {did: sorted(ds) for did, ds in days_by_device.items()},
        "verdict": verdict,
        "totals": {"saves": total_saves, "launcher_taps": tapped, "confirm_answers": mq["answered"]},
    }


def scorecard_text(sc, start, end):
    fd = sc["front_door"]
    lines = []
    lines.append(f"Mom-engagement funnel  ·  {start} → {end}")
    lines.append("=" * 52)
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
    mq = sc["confirm_queue"]
    lines.append("")
    lines.append("CONFIRM QUEUE (Mama's Perspective)")
    lines.append(f"  offered {mq['offered']} → viewed {mq['viewed']} → tapped {mq['tapped']} "
                 f"→ answered {mq['answered']}")
    lines.append("")
    lines.append(f"VERDICT: {sc['verdict']}")
    lines.append("  (funnel only — combine with read-mom-feedback.py for the non-gimme-answer half;")
    lines.append("   shared device means a 'return' is a proxy, not proof it was Mom.)")
    return "\n".join(lines)


def notify_macos(title, body):
    try:
        subprocess.run(
            ["osascript", "-e",
             f"display notification {json.dumps(body)} with title {json.dumps(title)}"],
            check=False, capture_output=True, timeout=15)
    except Exception:
        pass


def main():
    ap = argparse.ArgumentParser(description="Read the Mom-engagement funnel (read-only).")
    ap.add_argument("--start", default=TIMEBOX_START, help="YYYY-MM-DD (default: front-door ship date)")
    ap.add_argument("--end", default=None, help="YYYY-MM-DD (default: today)")
    ap.add_argument("--pickup", action="store_true", help="One line; silent if no funnel data yet")
    ap.add_argument("--json", action="store_true", help="Emit the scorecard as JSON")
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
    sc = compute(events)
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
