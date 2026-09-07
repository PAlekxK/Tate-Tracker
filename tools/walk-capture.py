#!/usr/bin/env python3
"""walk-capture.py — did a synthetic walk's events LAND on the capture side?

    python3 tools/walk-capture.py --env qa --run 2026-09-06T204303            # print
    python3 tools/walk-capture.py --env qa --run 2026-09-06T204303 --write <run dir>   # capture.json
    python3 tools/walk-capture.py --selftest

⭐ WHY `[paul-stated 2026-09-06]`: "for everything that we do and see and observe that we're capturing
on the user side, there needs to also be as much as possible instrumentation on our side, on the
capture side… the one thing we can't do is go back in time and recapture data from real users."
A walk records what the product SHOWED (transcript.json) and what the walker FELT (REPORT.md). This
is the third record: what the product TOLD US ABOUT ITSELF while it happened. A stop that produced
no capture-side event is a stop a real person would walk invisibly.

WHAT IT READS. GET /api/metrics for the walk's UTC day, filtered to batches whose device block
carries `synthetic == <run id>` — the id onboarding stores when a walk arrives on `?syn=<run>`, and
the viewer's collector stamps on every batch. ⛔ ONBOARDING'S OWN EVENTS (`/api/onboarding-metrics`)
ARE WRITE-ONLY — the Worker has no GET for them (measured 2026-09-06, worker.js:3296), so this tool
reports that half as UNREADABLE rather than as zero. → engineering-partner.

⛔ NEVER GREEN BY ABSENCE. No token, no store, a Worker error → UNREADABLE (exit 3), never "0 events".
"""
import argparse, datetime as dt, json, os, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRIVATE = os.path.join(ROOT, ".private")
WORKERS = {"qa": "https://fernwood-qa.paul-kirschenbauer.workers.dev",
           "lab": "https://fernwood-lab.paul-kirschenbauer.workers.dev",
           "home": "https://fernwood-home.paul-kirschenbauer.workers.dev"}
TOKENS = {"qa": "fernwood-token-qa", "lab": "fernwood-token-lab", "home": "fernwood-token-home"}


def token_for(env):
    p = os.path.join(PRIVATE, TOKENS.get(env, ""))
    try:
        for line in open(p, encoding="utf-8"):     # same shape as read-onboarding: first non-comment line
            line = line.strip()
            if line and not line.startswith("#"):
                return line
    except OSError:
        pass
    return None


def fetch_batches(env, day):
    tok = token_for(env)
    if not tok:
        raise SystemExit("walk-capture: UNREADABLE — no token file for env %r (%s)" % (env, TOKENS.get(env)))
    url = "%s/api/metrics?start=%s&end=%s" % (WORKERS[env], day, day)
    req = urllib.request.Request(url, headers={"X-Tate-Token": tok, "User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as f:
            data = json.loads(f.read())
    except (urllib.error.URLError, ValueError, OSError) as e:
        raise SystemExit("walk-capture: UNREADABLE — %s" % e)
    # The Worker answers {"range": {...}, "days": {"YYYY-MM-DD": [batch, ...]}} — a MAP of days.
    # The first cut of this reader looked for a list and read zero on a day that held the walks'
    # own batches (measured 2026-09-06: three rounds reported 0 while the store said otherwise).
    if isinstance(data, dict) and isinstance(data.get("days"), dict):
        data = [b for lst in data["days"].values() if isinstance(lst, list) for b in lst]
    elif isinstance(data, dict):
        for k in ("batches", "items", "days"):
            if isinstance(data.get(k), list):
                data = data[k]
                break
    out = []
    for x in (data if isinstance(data, list) else []):
        if isinstance(x, dict) and isinstance(x.get("batches"), list):
            out.extend(x["batches"])
        elif isinstance(x, dict) and "events" in x:
            out.append(x)
    return out


def summarise(batches, run):
    """→ {'app': {events, types, via}, 'onboarding': 'UNREADABLE'}"""
    mine = [b for b in batches if ((b.get("device") or {}).get("synthetic") == run)]
    events = [e for b in mine for e in (b.get("events") or [])]
    types = {}
    for e in events:
        types[e.get("type") or "?"] = types.get(e.get("type") or "?", 0) + 1
    return {"run": run,
            "app": {"batches": len(mine), "events": len(events), "types": types,
                    "via": sorted({b.get("via") or "?" for b in mine})},
            "onboarding": "UNREADABLE — /api/onboarding-metrics has no GET (worker.js:3296)"}


def selftest():
    ok = True
    batches = [{"via": "grant", "device": {"synthetic": "R1"}, "events": [{"type": "session_start"}, {"type": "card_expanded"}]},
               {"via": "master", "device": {"synthetic": None}, "events": [{"type": "session_start"}]},
               {"via": "grant", "device": {"synthetic": "R2"}, "events": [{"type": "session_start"}]}]
    s = summarise(batches, "R1")
    bit = s["app"]["events"] == 2 and s["app"]["types"] == {"session_start": 1, "card_expanded": 1}
    print("  %s M0 only the run's own batches are counted" % ("✅" if bit else "🔴")); ok &= bit
    s = summarise(batches, "R9")
    bit = s["app"]["events"] == 0 and s["app"]["batches"] == 0
    print("  %s M1 an unknown run reads zero, not someone else's events" % ("✅" if bit else "🔴")); ok &= bit
    bit = "UNREADABLE" in summarise([], "R1")["onboarding"]
    print("  %s M2 the write-only half reports UNREADABLE, never zero" % ("✅" if bit else "🔴")); ok &= bit
    print("%s selftest" % ("✅" if ok else "🔴"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", choices=sorted(WORKERS), default="qa")
    ap.add_argument("--run", help="the walk's run id, e.g. 2026-09-06T204303")
    ap.add_argument("--day", help="UTC day to read (default: derived from the run id, plus the next day)")
    ap.add_argument("--write", help="run folder to write capture.json into")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.run:
        raise SystemExit("walk-capture: --run is required")
    # A run id is LOCAL time; the Worker keys by UTC day, so read the run's day and the next.
    day0 = dt.date.fromisoformat(a.day or a.run[:10])
    batches = []
    for d in (day0, day0 + dt.timedelta(days=1)):
        batches += fetch_batches(a.env, d.isoformat())
    s = summarise(batches, a.run)
    s["readAt"] = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    s["env"] = a.env
    print("walk-capture — %s @ %s" % (a.run, a.env))
    print("  app events for this run: %d in %d batch(es) via %s" % (s["app"]["events"], s["app"]["batches"], ",".join(s["app"]["via"]) or "-"))
    for t, n in sorted(s["app"]["types"].items()):
        print("     %-22s %d" % (t, n))
    print("  onboarding events: %s" % s["onboarding"])
    if a.write:
        with open(os.path.join(a.write, "capture.json"), "w", encoding="utf-8") as f:
            json.dump(s, f, indent=1)
        print("  → capture.json written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
