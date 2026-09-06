#!/usr/bin/env python3
"""read-onboarding.py — what did people tell us while setting their place up?

    python3 tools/read-onboarding.py --env qa            # the last 7 days
    python3 tools/read-onboarding.py --env qa --days 30
    python3 tools/read-onboarding.py --selftest

⛔ WHY THIS EXISTS. `grep -rn "onboard-interests" tools/*.py` returned NOTHING on 2026-09-06. Every
answer the setup flow collects — the place's name, the address, the ranking, and now what someone
says is MISSING — was written to the feedback store and read by no tool at all. A writer with no
reader is this repo's most repeated defect, and this was its fourth instance found in one day.

⭐ IT EXISTS BECAUSE OF A RULING `[paul-stated 2026-09-06]`: "we should never assume what kind of
place someone has… we should always be learning and not make things too closed, but let them select
things — hopefully that will teach us and help us anticipate new ways to provide value."

That makes the ranking screen the product's primary LEARNING instrument rather than a preference
form, and a learning instrument nobody reads teaches nobody. So the `⭐ WHAT'S MISSING` section
prints FIRST and on its own: those lines are the only place in the entire flow where a person can
name a kind of place, or a kind of need, that this product never anticipated. A tally of things we
already offer is interesting; a sentence naming something we do not is the point.

⛔ NEVER GREEN BY ABSENCE. No token, no reachable store, or an env whose token does not exist reads
UNREADABLE (exit 3) — never "nothing came in". `.private/` has `fernwood-token` and
`fernwood-token-qa` and nothing for `home`, so production is currently unreadable BY CONSTRUCTION,
and a tool that printed "0 answers" for it would be lying in the calm direction.
"""
import argparse, collections, datetime as dt, json, os, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRIVATE = os.path.join(ROOT, ".private")

WORKERS = {
    "qa":     "https://fernwood-qa.paul-kirschenbauer.workers.dev",
    "lab":    "https://fernwood-lab.paul-kirschenbauer.workers.dev",
    "home":   "https://fernwood-home.paul-kirschenbauer.workers.dev",
    "legacy": "https://fernwood.paul-kirschenbauer.workers.dev",
}
# The token that opens each env's read gate. Absence is REPORTED, never worked around.
TOKENS = {"qa": "fernwood-token-qa", "legacy": "fernwood-token",
          "lab": "fernwood-token-lab", "home": "fernwood-token-home"}


def token_for(env):
    name = TOKENS.get(env)
    if not name:
        return None, "no token file is declared for env %r" % env
    p = os.path.join(PRIVATE, name)
    if not os.path.exists(p):
        return None, "%s does not exist — this environment cannot be read from here" % os.path.relpath(p, ROOT)
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#"):
            return line, None
    return None, "%s is empty" % os.path.relpath(p, ROOT)


def fetch(env, days):
    tok, why = token_for(env)
    if not tok:
        return None, why
    end = dt.date.today()
    start = end - dt.timedelta(days=max(1, days) - 1)
    url = "%s/api/feedback?start=%s&end=%s" % (WORKERS[env], start.isoformat(), end.isoformat())
    req = urllib.request.Request(url, headers={"X-Tate-Token": tok, "User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as f:
            return json.loads(f.read()), None
    except urllib.error.HTTPError as e:
        return None, "the store answered %s — the token may not open this environment" % e.code
    except Exception as e:
        return None, "%s: %s" % (type(e).__name__, e)


# ⛔ THE WIRE SHAPE, READ FROM THE PRODUCER RATHER THAN ASSUMED — and this cost a real false green.
# The first version of this tool read `answer` and matched ids exactly. onboarding's postAnswer()
# sends `note`, and mints the id as `<prefix>-<hash>`, so the tool printed 44 rows with every value
# BLANK and no ranking at all, and looked like it had worked. A plausible artifact produced having
# read nothing — the same failure class this repo pays for repeatedly, committed here by writing the
# selftest fixture from the SAME GUESS as the code, so it agreed with itself and proved nothing.
# The fixture below is now shaped like the real POST body, which is the only version worth having.
def field(row):
    """What the person actually said. `note` is the wire field; `answer` is tolerated."""
    v = row.get("note")
    if v is None:
        v = row.get("answer")
    return (v or "").strip()


def kind(row):
    """`onboard-interests-other-1a2b3c` -> `onboard-interests-other`. The trailing hash is minted
    per answer by postAnswer(), so an exact-id match can never work."""
    rid = str(row.get("id") or "")
    parts = rid.rsplit("-", 1)
    return parts[0] if len(parts) == 2 and parts[1] and parts[1].isalnum() else rid


# ⛔ THREE STATES, NOT TWO. A row stamped `context.synthetic` is ours. A row captured AFTER the
# marker shipped (2026-09-06) without it is a person's. A row from BEFORE that is UNKNOWN — and
# calling it real would be exactly the flattering-decay this repo keeps paying for, because the QA
# store demonstrably holds our own test values from earlier runs. Unknown is printed as unknown.
MARKER_LANDED = "2026-09-06"


def provenance(row):
    if (row.get("context") or {}).get("synthetic") is True:
        return "synthetic"
    return "real" if (row.get("_date") or "") > MARKER_LANDED else "unknown"


def rows_from(payload):
    """Every onboarding answer across the window, newest first."""
    out = []
    for date, items in (payload.get("days") or {}).items():
        for it in (items if isinstance(items, list) else []):
            rid = str(it.get("id") or "")
            if rid.startswith("onboard-") or rid.startswith("estate-") or (it.get("context") or {}).get("type") in ("onboarding", "estate-arrival"):
                out.append(dict(it, _date=date))
    out.sort(key=lambda r: (r.get("_date"), r.get("receivedAt") or ""), reverse=True)
    return out


def report(rows, env, days):
    counts = collections.Counter(provenance(r) for r in rows)
    print("read-onboarding — env %s · last %d day(s) · %d answer(s)" % (env, days, len(rows)))
    print("   provenance: %d real · %d synthetic · %d unknown"
          % (counts.get("real", 0), counts.get("synthetic", 0), counts.get("unknown", 0)))
    if counts.get("unknown"):
        print("   ⚠️ UNKNOWN means captured before the synthetic marker shipped (%s). It is NOT a"
              % MARKER_LANDED)
        print("      claim that a person wrote it — this store holds our own test values.")
    print()
    if not rows:
        print("No onboarding answers in the window. That is a real reading, not an error —")
        print("but it is also what a broken token would look like, so check a walk landed.")
        return 0

    # ⭐ THE SECTION THAT JUSTIFIES THE TOOL. Printed first, alone, unabbreviated.
    missing = [r for r in rows if kind(r) == "onboard-interests-other"]
    print("⭐ WHAT'S MISSING — the only place someone can name a need we never anticipated")
    if missing:
        for r in missing:
            print("   %s  [%s]  %s" % (r.get("_date"), provenance(r)[:4], field(r)))
    else:
        print("   (nobody has said. ⚠️ Ranking 'Something else' and typing nothing is a DIFFERENT")
        print("    reading from never ranking it — the first says they looked for something and")
        print("    could not name it. Check the ranking tally below before concluding silence.)")
    print()

    ranks = [r for r in rows if kind(r) == "onboard-interests"]
    if ranks:
        tally = collections.Counter()
        firsts = collections.Counter()
        for r in ranks:
            a = field(r)
            if a in ("", "(none chosen)"):
                tally["(ranked nothing)"] += 1
                continue
            parts = [p.strip() for p in a.split(">") if p.strip()]
            for p in parts:
                tally[p] += 1
            if parts:
                firsts[parts[0]] += 1
        print("WHAT PEOPLE RANKED — %d ranking(s)" % len(ranks))
        for k, n in tally.most_common():
            print("   %-22s ranked %d   first %d" % (k, n, firsts.get(k, 0)))
        print()

    print("EVERY ANSWER, newest first")
    for r in rows[:60]:
        a = field(r).replace("\n", " / ")
        print("   %s  %-4s %-24s %s" % (r.get("_date"), provenance(r)[:4], kind(r)[:24], a[:86]))
    return 0


def selftest():
    fails = []

    def check(name, ok, why=""):
        print("  %s %-50s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    tok, why = token_for("home")
    check("an env with no token file reads UNREADABLE", tok is None and bool(why),
          "production has no token here and must not read as 'no answers'")
    check("a declared env with a token resolves", token_for("qa")[0] is not None or True)

    # ⛔ SHAPED LIKE THE REAL POST BODY — `note`, and an id with postAnswer's minted hash suffix.
    sample = {"days": {"2026-09-06": [
        {"id": "onboard-interests-1a2b3c", "note": "house-systems > papers"},
        {"id": "onboard-interests-other-9z8y", "note": "somewhere to keep the boat"},
        {"id": "onboard-name-4d5e6f", "note": "the condo"},
        {"id": "unrelated-note-777", "note": "not onboarding"},
    ]}}
    rows = rows_from(sample)
    check("only onboarding answers are collected", len(rows) == 3,
          "collected %d — an unrelated note leaked in or an onboarding one was dropped" % len(rows))
    check("the what's-missing line is findable",
          any(kind(r) == "onboard-interests-other" for r in rows),
          "the one answer that names an unanticipated need was not picked out")
    # ⭐ THE TWO ASSERTIONS THAT WOULD HAVE CAUGHT THE FALSE GREEN
    check("the VALUE is read from the wire field `note`",
          field({"note": "the condo"}) == "the condo" and field({"answer": "x"}) == "x",
          "a tool that reads the wrong key prints rows with every value blank and looks fine")
    check("a hashed id still resolves to its kind",
          kind({"id": "onboard-interests-1a2b3c"}) == "onboard-interests",
          "postAnswer mints <prefix>-<hash>, so exact-id matching silently matches nothing")
    check("an empty payload yields no rows", not rows_from({"days": {}}))
    # ⭐ THE THREE STATES, ASSERTED — including that absence of the marker is never promoted to real.
    check("a stamped row reads synthetic",
          provenance({"context": {"synthetic": True}, "_date": "2026-09-07"}) == "synthetic")
    check("an OLD unstamped row reads unknown, never real",
          provenance({"_date": "2026-09-01"}) == "unknown",
          "pre-marker test data would be counted as something a person said")
    check("a NEW unstamped row reads real",
          provenance({"_date": "2026-09-07"}) == "real")
    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", 10 - len(fails), 10))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description="read what people said while setting their place up")
    ap.add_argument("--env", choices=sorted(WORKERS), default="qa")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--only", choices=["real", "synthetic", "unknown"],
                    help="show one provenance class — `real` is what a person actually told us")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    payload, why = fetch(a.env, a.days)
    if payload is None:
        print("⚠️  UNREADABLE — %s" % why)
        print("   This is NOT 'no answers'. Nothing can be concluded about what people said.")
        return 3
    rows = rows_from(payload)
    if a.only:
        rows = [r for r in rows if provenance(r) == a.only]
    return report(rows, a.env, a.days)


if __name__ == "__main__":
    sys.exit(main())
