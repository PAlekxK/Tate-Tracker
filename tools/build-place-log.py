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


def _load(name, canon=None):
    """Read one canon file FROM THE HOUSEHOLD BEING BUILT — never from the repo root.

    ⛔⛔ THE BUG THIS SIGNATURE EXISTS TO PREVENT, and it shipped for about an hour on 2026-09-07.
    `canon` defaulted to the repo root, which is FERNWOOD'S canon. So building QA's app inlined
    Fernwood's zone names, its three vehicles, "Church Mountain" and "Appalachian Almanac" into a
    stranger's build — and this file's own docstring said it derived from "the household's own dated
    records", which is the sentence that made it look safe.
    ⭐ SIXTH INSTANCE OF ONE ASSUMPTION. The lap-2 retro named the pattern and gave the search string:
    *a comment saying "this is safe because…" whose premise is about Fernwood.* This was written the
    same evening that retro was read. It was caught only because `qa` was added to HOUSEHOLD minutes
    later and the neutrality falsifier ran on a QA build for the first time; the deploy REFUSED and
    nothing reached the origin.
    """
    try:
        with open(os.path.join(canon or ROOT, name), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        # ⛔ A source we cannot read contributes NOTHING and says so to the caller via `missing`.
        # It must never contribute a zero that reads like "nothing happened here".
        return None


def derive(sources=None, canon=None):
    """[(date, kind, text)] newest first, plus the sources that could not be read.

    ⛔ `canon` is the household being built. An instance whose canon holds none of these files
    derives an EMPTY log, which is the correct answer for a household with no history — never
    another household's history.
    """
    s = sources or {}
    missing, out = [], []

    veh = s.get("vehicles", _load("vehicles.json", canon))
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

    q = s.get("questions", _load("questions.json", canon))
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

    z = s.get("zones", _load("zones.json", canon))
    if z is None:
        missing.append("zones.json")
    else:
        for zone in (z.get("zones") or []):
            d = (zone.get("createdAt") or zone.get("namedAt") or "")[:10]
            if d:
                out.append((d, "place", "named “%s”" % zone.get("name", "a place")))

    out.sort(key=lambda r: r[0], reverse=True)
    return out, missing


# ⭐ MODELLED ON THE PRODUCT LOG'S OWN SHAPE, NOT COPIED `[paul-stated 2026-09-07]`: *"we already have
# a decent changelog template in Mom's version of Fernwood, so let's not copy and paste, but we can
# model after that a little bit."*
#
# RELEASE_NOTES entries are `{date, title, bullets[]}` and render as a date + a title, then a bulleted
# list. The first version of this log emitted one flat `{date, kind, text}` row per event, which put
# twenty-three near-identical lines on screen and read as a dump rather than a record.
#
# ⛔ THE TITLE IS DERIVED FROM COUNTS, NEVER COMPOSED. A day is summarised by what KIND of thing
# happened and how many — "Six places named" — because a generated sentence about someone's own
# property is the one thing on this path that could sound like it was written about them rather than
# from their record. Counting is honest; narrating is not, and there is no AI on this path.
KIND_WORDS = {
    "place":   ("place named", "places named"),
    "fleet":   ("service entry", "service entries"),
    "settled": ("question you answered", "questions you answered"),
}


def group(rows, limit_days=12):
    """[(date, title, bullets)] — one entry per DAY, mirroring the product log's shape."""
    days = {}
    for d, k, t in rows:
        days.setdefault(d, []).append((k, t))
    out = []
    for d in sorted(days, reverse=True)[:limit_days]:
        items = days[d]
        counts = {}
        for k, _t in items:
            counts[k] = counts.get(k, 0) + 1
        parts = []
        for k in ("place", "fleet", "settled"):
            n = counts.get(k)
            if n:
                one, many = KIND_WORDS[k]
                parts.append("%d %s" % (n, one if n == 1 else many))
        title = " · ".join(parts).capitalize() if parts else "Changes here"
        out.append({"date": d, "title": title, "bullets": [t for _k, t in items]})
    return out


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
        print(json.dumps(group(rows, a.limit), ensure_ascii=False))
        return 0
    entries = group(rows, a.limit)
    print("🏡 place log — %d event(s) across %d day(s); showing %d"
          % (len(rows), len({r[0] for r in rows}), len(entries)))
    for e in entries:
        print("   %s — %s" % (e["date"], e["title"]))
        for b in e["bullets"][:4]:
            print("      • %s" % str(b)[:80])
        if len(e["bullets"]) > 4:
            print("      • … and %d more" % (len(e["bullets"]) - 4))
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
    g = group(rows)
    ck("M5 grouped by DAY, newest first, mirroring the product log's {date,title,bullets}",
       len(g) == 4 and [e["date"] for e in g] == sorted([e["date"] for e in g], reverse=True)
       and all({"date", "title", "bullets"} <= set(e) for e in g))
    multi = group([("2026-01-01", "place", "a"), ("2026-01-01", "place", "b"),
                   ("2026-01-01", "fleet", "c")])
    ck("M6 a day's title COUNTS what happened and never narrates it",
       multi[0]["title"] == "2 places named · 1 service entry" and len(multi[0]["bullets"]) == 3)
    ck("M1 newest first", [r[0] for r in rows] == sorted([r[0] for r in rows], reverse=True))
    ck("M2 an undated row is dropped, never dated 'today'",
       not derive({"vehicles": {"vehicles": [{"name": "x", "serviceHistory": [{"what": "y"}]}]},
                   "questions": {"questions": []}, "zones": {"zones": []}})[0])

    rows2, missing2 = derive({"vehicles": None, "questions": {"questions": []}, "zones": {"zones": []}})
    ck("M3 an UNREADABLE source is NAMED, not counted as empty",
       missing2 == ["vehicles.json"] and not rows2)

    rows3, _ = derive({"vehicles": {"vehicles": []}, "questions": {"questions": []}, "zones": {"zones": []}})
    ck("M4 a brand-new household derives ZERO and that is not an error", rows3 == [])

    # ⛔ THE LEG THAT WOULD HAVE CAUGHT THE TENANCY LEAK. A canon directory holding none of these
    # files must derive NOTHING — not the repo root's Fernwood data. This is the sixth instance of
    # "correct code whose premise was about Fernwood", so it gets an assertion, not a comment.
    import tempfile
    empty = tempfile.mkdtemp()
    rows4, missing4 = derive(canon=empty)
    ck("M7 a canon with no records derives ZERO — never the repo root's household",
       rows4 == [] and sorted(missing4) == ["questions.json", "vehicles.json", "zones.json"])
    print("\n%s selftest (%d failure(s))" % ("✅" if not fails else "🔴", len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
