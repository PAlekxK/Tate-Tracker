#!/usr/bin/env python3
"""build-place-log.py — WHAT CHANGED AT THIS PLACE, derived from the place's own record.

    python3 tools/build-place-log.py                 # print what it derives
    python3 tools/build-place-log.py --json          # the payload the build inlines
    python3 tools/build-place-log.py --selftest

⭐ WHY TWO CHANGELOGS `[paul-ruled 2026-09-07]`: *"we've got a changelog for each property as well as
at the accounts / application generator level."*

⛔ THE COLLISION THIS SPLITS. `RELEASE_NOTES.md` is the PRODUCT's changelog and its own heading reads
**"What's changed at Fernwood lately."** It is shipped into every household. At Bob's house that
sentence is false, and at Mom's condo it will be. One file was answering two different questions:

| question | whose log |
|---|---|
| *"why does the app look different?"* | the **product** log — authored by Paul, same for everyone |
| *"did my thing land? what happened here?"* | ⭐ the **place** log — DERIVED, different at every household |

⭐ **DERIVED, NEVER AUTHORED, and that is the whole design.** A place log somebody has to write is a
place log that goes stale the first busy week. This reads the household's own dated records — the
ones already kept for other reasons — so it cannot drift from what actually happened.

⛔ **IT IS NOT AN ACKNOWLEDGMENT AND MUST NOT BECOME ONE.** The ribbon says *we heard you*; this says
*here is what changed*. `CLAUDE.md` is explicit that the ribbon exists because a changelog lives
elsewhere in the app — this is that elsewhere, for the half the product log never covered.

⚠️ **AN EMPTY LOG IS THE CORRECT OUTPUT FOR A NEW HOUSEHOLD** and must read as *nothing has happened
here yet*, never as *broken*. Fernwood has years of record; Paul's condo is hours old. `measured
2026-09-07`: Fernwood derives ~89 entries, a fresh household derives 0.

⛔⛔ Z-ACK ADJACENCY — READ BEFORE RENDERING THIS ANYWHERE MOM CAN SEE IT. `measured 2026-09-07`:
13 of Fernwood's 89 derived entries are **her zone namings**. Paul ruled Z-ACK CLOSED — *"don't worry
about the acknowledgment to Mom, I'll take care of it in person"* — and explicitly: **do not design a
ribbon, a card, a message or a surface to thank her for the 23 zones.**

This log is a dated factual record, not a thank-you, and it is derived rather than composed. But a
card that lists *"named 'The Turf' · named 'The Meadow' · …"* back to the person who named them sits
close enough to that ruling that **it is Paul's call, not a build decision.** In practice the frozen
estate takes no deploys, so nothing reaches her today — but the constraint is written here rather
than discovered later.

⛔ NO AI ON THIS PATH. Every line is a deterministic restatement of a dated row that already exists.
"""
import argparse, json, os, sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name):
    try:
        with open(os.path.join(ROOT, name), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        # ⛔ A source we cannot read contributes NOTHING and says so to the caller via `missing`.
        # It must never contribute a zero that reads like "nothing happened here".
        return None


def derive(sources=None):
    """[(date, kind, text)] newest first, plus the sources that could not be read."""
    s = sources or {}
    missing, out = [], []

    veh = s.get("vehicles", _load("vehicles.json"))
    if veh is None:
        missing.append("vehicles.json")
    else:
        for v in (veh.get("vehicles") or veh.get("items") or []):
            label = v.get("name") or v.get("id") or "a vehicle"
            for e in (v.get("serviceHistory") or []):
                d = (e.get("date") or "")[:10]
                what = e.get("what") or e.get("summary") or e.get("note") or "service"
                if d:
                    out.append((d, "fleet", "%s — %s" % (label, what)))

    q = s.get("questions", _load("questions.json"))
    if q is None:
        missing.append("questions.json")
    else:
        for x in (q.get("questions") if isinstance(q, dict) else q) or []:
            if not isinstance(x, dict):
                continue
            d = (x.get("resolvedAt") or "")[:10]
            if d:
                # ⭐ THE LINE THAT MATTERS MOST — a question the household ANSWERED, and what it
                # settled. This is the loop closing where a person can see it.
                out.append((d, "settled", x.get("resolution") or x.get("prompt") or x.get("id")))

    z = s.get("zones", _load("zones.json"))
    if z is None:
        missing.append("zones.json")
    else:
        for zone in (z.get("zones") or []):
            d = (zone.get("createdAt") or zone.get("namedAt") or "")[:10]
            if d:
                out.append((d, "place", "named “%s”" % zone.get("name", "a place")))

    out.sort(key=lambda r: r[0], reverse=True)
    return out, missing


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--limit", type=int, default=12, help="how many the card shows")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    rows, missing = derive()
    if a.json:
        print(json.dumps([{"date": d, "kind": k, "text": t} for d, k, t in rows[:a.limit]],
                         ensure_ascii=False))
        return 0
    print("🏡 place log — %d dated entr%s derived" % (len(rows), "y" if len(rows) == 1 else "ies"))
    for d, k, t in rows[:a.limit]:
        print("   %s  %-8s %s" % (d, k, str(t)[:88]))
    if len(rows) > a.limit:
        print("   … and %d older" % (len(rows) - a.limit))
    if missing:
        # ⛔ NAMED, never silently skipped: "we could not read it" and "it held nothing" are
        # different sentences and this repo has paid for conflating them.
        print("   ⛔ UNREADABLE, so its entries are MISSING rather than absent: %s" % ", ".join(missing))
    if not rows:
        print("   ⬜ nothing has happened here yet — the correct output for a new household, "
              "and it must render as that rather than as an error")
    return 0


def selftest():
    fails = []

    def ck(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            fails.append(name)

    S = {"vehicles": {"vehicles": [{"name": "Bolores", "serviceHistory": [
             {"date": "2026-05-01", "what": "new battery"},
             {"date": "2026-07-04", "what": "oil"}]}]},
         "questions": {"questions": [{"id": "q1", "resolvedAt": "2026-06-02", "resolution": "Annabelle"}]},
         "zones": {"zones": [{"name": "the fairway", "createdAt": "2026-04-01"}]}}
    rows, missing = derive(S)
    ck("M0 derives from every source", len(rows) == 4 and not missing)
    ck("M1 newest first", [r[0] for r in rows] == sorted([r[0] for r in rows], reverse=True))
    ck("M2 an undated row is dropped, never dated 'today'",
       not derive({"vehicles": {"vehicles": [{"name": "x", "serviceHistory": [{"what": "y"}]}]},
                   "questions": {"questions": []}, "zones": {"zones": []}})[0])

    rows2, missing2 = derive({"vehicles": None, "questions": {"questions": []}, "zones": {"zones": []}})
    ck("M3 an UNREADABLE source is NAMED, not counted as empty",
       missing2 == ["vehicles.json"] and not rows2)

    rows3, _ = derive({"vehicles": {"vehicles": []}, "questions": {"questions": []}, "zones": {"zones": []}})
    ck("M4 a brand-new household derives ZERO and that is not an error", rows3 == [])
    print("\n%s selftest (%d failure(s))" % ("✅" if not fails else "🔴", len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
