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


# ⛔ TWO CREDENTIAL CLASSES, TWO HEADERS, AND THIS TOOL USED TO KNOW ONLY ONE.
# `worker.js:787` reads a GRANT from `X-Grant` and says in its own comment "never X-Tate-Token —
# seat discipline 2"; `X-Tate-Token` is the MASTER token (`authOk`, `worker.js:334`), which is
# strictly more powerful and is the thing `PRODUCT-ENGINE.md:15` is retiring. Meanwhile
# `grant-mint.py:295-304` writes its token as JSON — `{"<person>@<estate>": token}` or
# `{"X-Grant": token}` — while this function took the first non-comment LINE.
# So a grant token dropped into one of these files would have been read as a JSON blob and sent
# under the master's header: three mismatches, and the failure arrives as a bare 401 that says
# nothing about which of the three it was.
# ⭐ The fix is to READ THE FILE'S SHAPE and send the header that matches it. A JSON object is a
# grant → `X-Grant`; a bare line is the master → `X-Tate-Token`. The class is REPORTED, so a 401 can
# be read against what was actually presented.
def token_for(env):
    name = TOKENS.get(env)
    if not name:
        return None, None, "no token file is declared for env %r" % env
    p = os.path.join(PRIVATE, name)
    rel = os.path.relpath(p, ROOT)
    if not os.path.exists(p):
        # ⚠️ NOT "cannot be read" ANY MORE — that became false on 2026-09-07. `watch-feedback.py`
        # reads the same store through local wrangler auth and needs no token at all, so a message
        # saying the environment is unreadable would send a reader looking for a credential that
        # nothing requires. An honest UNREADABLE names the door that IS open.
        return None, None, ("%s does not exist — this tool cannot read %s. `python3 "
                            "tools/watch-feedback.py --env %s` reads the same store with no token."
                            % (rel, env, env))
    raw = open(p, encoding="utf-8").read()
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError:
        obj = None
    if isinstance(obj, dict):
        vals = [v for v in obj.values() if isinstance(v, str) and v.strip()]
        if not vals:
            return None, None, "%s is a JSON object with no token value in it" % rel
        if len(vals) > 1:
            # Refusing beats guessing: picking one of several credentials silently is how a tool
            # ends up presenting a credential nobody meant it to present.
            return None, None, ("%s holds %d credentials; this tool will not choose between them"
                                % (rel, len(vals)))
        return vals[0], "grant", None
    for line in raw.splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            return line, "master", None
    return None, None, "%s is empty" % rel


def fetch(env, days):
    tok, klass, why = token_for(env)
    if not tok:
        return None, why
    header = "X-Grant" if klass == "grant" else "X-Tate-Token"
    end = dt.date.today()
    start = end - dt.timedelta(days=max(1, days) - 1)
    url = "%s/api/feedback?start=%s&end=%s" % (WORKERS[env], start.isoformat(), end.isoformat())
    req = urllib.request.Request(url, headers={header: tok, "User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as f:
            return json.loads(f.read()), None
    except urllib.error.HTTPError as e:
        return None, ("the store answered %s — %s was presented as %s and it may not open this "
                      "environment" % (e.code, klass, header))
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


# ⭐ RUN IDENTITY, AND WHICH RUN IS CURRENT `[paul-stated 2026-09-06]`: "if we find a critical error
# that requires a rerun of a synthetic, the aborted or failed or unsatisfactory run should not be
# kept in memory… we would always be only committing the data from the FINAL SUCCESSFUL run. So it
# would supersede everything else. We're keeping all the feedback and runs as we go."
#
# ⛔ THE PROBLEM THAT MAKES THIS NECESSARY, MEASURED before it was built: est-qa0001 held 18 place
# names across 7 distinct values, with nothing saying which was current — because "keep the last
# good run" had nothing to group BY. A row carried estate, person, time and env, and no ATTEMPT.
#
# ⭐ THE JOIN: a synthetic walk passes `?syn=<runId>` where runId IS its own run folder, so a stored
# `sessionId` equals `.private/synthetic-walks/<role>/<runId>/`. No inference, no fuzzy matching.
#
# ⛔ AND "CURRENT" IS NOT "NEWEST". The aborted run is usually the last one — that is exactly Paul's
# case. So current = the newest run this seat has that WALK-INTEGRITY WILL COUNT, which already
# refuses a walk with a failed stop, a build that moved mid-walk, or no written report. A run that
# fell over cannot become the authority by being late.
# ⚠️ Paul's judgment overrides it: `.private/current-runs.json` mapping role -> runId wins where
# present, because "some of that will come down to my human judgment of what's good enough."
def walk_runs(root=ROOT):
    """runId -> {role, countable}. Read from the walk corpus; nothing is restated here."""
    import glob as _g, importlib.util as _ilu
    spec = _ilu.spec_from_file_location("wi", os.path.join(root, "tools", "walk-integrity.py"))
    wi = _ilu.module_from_spec(spec); spec.loader.exec_module(wi)
    out = {}
    for d in _g.glob(os.path.join(root, ".private", "synthetic-walks", "*", "*")):
        if not os.path.isdir(d):
            continue
        v = wi.verdict(d)
        out[os.path.basename(d)] = {"role": v["seat"], "countable": not v["refusals"],
                                    "refusals": [k for k, _ in v["refusals"]]}
    return out


def current_runs(runs, root=ROOT):
    """role -> the runId whose data is authoritative."""
    override = {}
    p = os.path.join(root, ".private", "current-runs.json")
    if os.path.exists(p):
        try:
            override = json.load(open(p, encoding="utf-8")) or {}
        except ValueError:
            override = {}
    best = {}
    for rid, meta in sorted(runs.items()):
        if meta["countable"]:
            best[meta["role"]] = rid          # sorted ascending, so the last countable wins
    best.update({k: v for k, v in override.items() if isinstance(v, str)})
    return best


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
    runs = walk_runs()
    cur = current_runs(runs)
    cur_ids = set(cur.values())

    def standing(r):
        sid = r.get("sessionId")
        if not sid:
            return "no-run"          # pre-dates run identity; cannot be superseded or trusted
        meta = runs.get(sid)
        if not meta:
            return "unlinked"        # a run id we have no walk for — a person, or a lost transcript
        if sid in cur_ids:
            return "current"
        # ⛔ SUPERSEDED AND PENDING ARE NOT THE SAME THING, and calling both "superseded" reads as
        # "something replaced this" when the truth is often the opposite. A run NEWER than the
        # authoritative one has not been beaten — it has not yet been READ. Its data is real and
        # waiting; the seat that walked it has not written the experiential half, so walk-integrity
        # will not count it and it cannot claim authority.
        # ⭐ That is the property worth keeping: DATA DOES NOT BECOME AUTHORITATIVE UNTIL SOMEONE
        # HAS READ THE RUN THAT PRODUCED IT. Saying "pending" keeps that legible; saying
        # "superseded" would quietly turn an unread run into a discarded one.
        authoritative = cur.get(meta["role"])
        if authoritative and sid > authoritative:
            return "pending"
        return "superseded"

    counts = collections.Counter(provenance(r) for r in rows)
    st = collections.Counter(standing(r) for r in rows)
    print("read-onboarding — env %s · last %d day(s) · %d answer(s)" % (env, days, len(rows)))
    print("   provenance: %d real · %d synthetic · %d unknown"
          % (counts.get("real", 0), counts.get("synthetic", 0), counts.get("unknown", 0)))
    print("   standing:   %d current · %d pending (walked, not yet read) · %d superseded · "
          "%d unlinked · %d pre-date run identity"
          % (st.get("current", 0), st.get("pending", 0), st.get("superseded", 0),
             st.get("unlinked", 0), st.get("no-run", 0)))
    if cur:
        print("   authoritative run per seat: %s"
              % ", ".join("%s=%s" % (k, v) for k, v in sorted(cur.items())))
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
        print("   %s  %-4s %-10s %-22s %s" % (r.get("_date"), provenance(r)[:4],
                                                    standing(r)[:10], kind(r)[:22], a[:70]))
    return 0


def selftest():
    fails = []

    def check(name, ok, why=""):
        print("  %s %-50s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    tok, klass, why = token_for("home")
    check("an env with no token file reads UNREADABLE", tok is None and bool(why),
          "production has no token here and must not read as 'no answers'")
    # ⚠️ The message must not claim the environment is unreadable FULL STOP — a reader that needs
    # no token exists since 2026-09-07, and sending someone to hunt a credential nothing requires
    # is a wrong answer wearing an honest one's clothes.
    check("and it names the door that IS open", "watch-feedback.py" in (why or ""),
          "the UNREADABLE message sends a reader looking for a credential nothing needs")

    # ⛔ THE CREDENTIAL CLASS DECIDES THE HEADER. A grant goes in `X-Grant` and the master in
    # `X-Tate-Token` (`worker.js:787` — "never X-Tate-Token"), and grant-mint writes JSON while a
    # master token is a bare line. Presenting one under the other's header fails as a bare 401.
    import tempfile as _tf
    global PRIVATE
    _real_private = PRIVATE
    PRIVATE = _tf.mkdtemp()
    try:
        with open(os.path.join(PRIVATE, TOKENS["qa"]), "w") as f:
            f.write('{"p-x@est-qa0001": "GRANTTOKEN"}\n')
        t, k, w = token_for("qa")
        check("a JSON credential file is read as a GRANT", (t, k, w) == ("GRANTTOKEN", "grant", None),
              "read %r as %r" % (t, k))
        with open(os.path.join(PRIVATE, TOKENS["qa"]), "w") as f:
            f.write("# a comment\nMASTERTOKEN\n")
        t, k, w = token_for("qa")
        check("a bare-line credential file is read as the MASTER", (t, k, w) == ("MASTERTOKEN", "master", None))
        with open(os.path.join(PRIVATE, TOKENS["qa"]), "w") as f:
            f.write('{"a": "one", "b": "two"}\n')
        t, k, w = token_for("qa")
        check("a file holding two credentials is REFUSED, never guessed at",
              t is None and "will not choose" in (w or ""))
        with open(os.path.join(PRIVATE, TOKENS["qa"]), "w") as f:
            f.write("   \n# only a comment\n")
        t, k, w = token_for("qa")
        check("an empty credential file reads UNREADABLE, not as a token", t is None and bool(w))
    finally:
        PRIVATE = _real_private

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

    # ⭐ SUPERSEDING — the property Paul actually asked for, asserted rather than assumed.
    runs = {"2026-09-06T100000": {"role": "mom", "countable": True, "refusals": []},
            "2026-09-06T110000": {"role": "mom", "countable": False, "refusals": ["stops-did-not-complete"]},
            "2026-09-06T090000": {"role": "owner", "countable": True, "refusals": []}}
    cur = current_runs(runs, root="/nonexistent")     # no override file
    check("the newest COUNTABLE run is authoritative", cur.get("mom") == "2026-09-06T100000",
          "got %r — a run that fell over became the authority by being late, which is Paul's exact case"
          % cur.get("mom"))
    check("each seat has its own authority", cur.get("owner") == "2026-09-06T090000")
    check("a seat with no countable run has NO authority", "strict" not in cur,
          "an unproven seat must not silently claim one")
    check("PENDING and SUPERSEDED are distinguishable",
          "2026-09-06T120000" > "2026-09-06T100000" and "2026-09-06T090000" < "2026-09-06T100000",
          "run ids must sort chronologically or newer-vs-older cannot be told apart")
    print("\n%s selftest: %d failure(s)" % ("✅" if not fails else "🔴", len(fails)))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description="read what people said while setting their place up")
    ap.add_argument("--env", choices=sorted(WORKERS), default="qa")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--current", action="store_true",
                    help="only rows from the authoritative run of each seat — what the estate "
                         "actually claims, with superseded attempts left in the trail")
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
    if a.current:
        cur_ids = set(current_runs(walk_runs()).values())
        # ⛔ A ROW WITH NO RUN ID IS DROPPED HERE, DELIBERATELY. It cannot be shown to be current,
        # and --current is the view that answers "what does this estate actually claim". Including
        # the unattributable would make the answer look complete while resting on rows nothing can
        # supersede — the flattering direction.
        rows = [r for r in rows if r.get("sessionId") in cur_ids]
    return report(rows, a.env, a.days)


if __name__ == "__main__":
    sys.exit(main())
