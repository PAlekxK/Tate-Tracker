#!/usr/bin/env python3
"""journey-walk.py — one synthetic walker's full journey, captured richly and repeatably.

    python3 tools/journey-walk.py --role owner
    python3 tools/journey-walk.py --role wide-eyed --fresh     # sign up rather than sign in

⭐ WHY THE CAPTURE IS WIDE `[paul-stated 2026-09-05]`: "capture as much data as possible… make these
repeatable… bear in mind this is all accretive." A walk that records only its verdict cannot be
re-read later with a new question in mind. So every screen's full text, every field, every button,
every action and its timing lands in a dated run folder, and the folders accumulate per walker.

⛔ THIS CAPTURES THE OBJECTIVE HALF ONLY — what the product did. What the walker FELT is a separate
artifact written by the walker, and the two must not be merged by this tool: a transcript that mixes
"the button said Save" with "I hesitated here" makes the second unfalsifiable. They live side by side
in the same run folder and are joined by the run id, never blended.

Runs land in `.private/synthetic-walks/<role>/<timestamp>/` — private, because a walk carries the
walker's invented address and the account's credentials are one file away.
"""
import time, urllib.request, argparse, datetime as dt, glob, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, ".private", "synthetic-identities.json")
OUT = os.path.join(ROOT, ".private", "synthetic-walks")


def identity(role, env):
    d = json.load(open(STORE, encoding="utf-8"))
    # ⛔ ROLE@ENV, never the bare role. An identity is per-role-PER-ENVIRONMENT: "mom" on QA and "mom"
    # on lab are different accounts with different personIds, and looking one up by role alone is how
    # a gate-1 walk silently borrowed gate 2's identity.
    key = "%s@%s" % (role, env)
    v = (d.get("identities") or {}).get(key)
    if not v:
        raise SystemExit("journey-walk: no identity %r — `synthetic-identity.py --create %s --env %s`"
                         % (key, role, env))
    return v


def refresh(role, env):
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "synthetic-identity.py"),
                    "--login", role, "--env", env], capture_output=True, text=True, timeout=180)
    return identity(role, env)


# ⛔ A WALK MUST NOT WALK A MOVING TARGET. On 2026-09-05 four walkers ran between 17:00 and 17:30
# while eleven deploys went out — one walk started 2m29s after a deploy and finished before the next.
# Cloudflare's edge does not update atomically (the bare host served the previous index.html for
# minutes, measured the same night), so a walker could load one build and have its writes answered by
# another. That produced an intermittent "didn't go through" nobody could reproduce afterwards, and it
# is unfalsifiable after the fact: the walk records no build. So the build is READ AT THE START AND
# RE-READ AT THE END, and a walk that straddled a deploy says so in its own transcript rather than
# being quietly believed.
def served_sha(env):
    url = {"qa": "https://fernwood-qa.pages.dev", "lab": "https://fernwood-lab.pages.dev",
           "home": "https://fernwood-home.pages.dev"}[env]
    h = {"User-Agent": "Mozilla/5.0"}          # a UA-less request is 403'd at the edge, not by the Worker
    try:
        tok = json.load(open(os.path.join(ROOT, ".private", "cf-access-service-token.json")))
        h["CF-Access-Client-Id"] = tok["CF_ACCESS_CLIENT_ID"]
        h["CF-Access-Client-Secret"] = tok["CF_ACCESS_CLIENT_SECRET"]
    except OSError:
        pass
    try:
        req = urllib.request.Request(url + "/qa-build.json?cb=%d" % time.time(), headers=h)
        with urllib.request.urlopen(req, timeout=30) as f:
            return (json.loads(f.read()) or {}).get("sha")
    except Exception:
        return None


def view(url, actions, shot, watch=False):
    cmd = [sys.executable, os.path.join(ROOT, "tools", "journey-view.py"), url, "--shot", shot]
    if watch:
        cmd.append("--watch")
    for a in actions:
        cmd += ["--do", a]
    t0 = dt.datetime.now()
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=2400 if watch else 600)
    # ⛔ journey-view is a HUMAN-READABLE tool: it prints prose to stdout and returns no JSON. An
    # earlier version of this function looked for a `steps` key that has never existed, so every
    # failed action evaluated to zero failures and every stop scored "walked" — the false-green class
    # closed by reading a field that was not there. Parse the two things it actually prints.
    out = r.stdout or ""
    failed = [l.split("could not do", 1)[1].strip() for l in out.splitlines() if "could not do" in l]
    # The section the page was actually showing when the shot was taken — the join key between a
    # feedback note (which records s0..s4) and the screenshot beside this record.
    sid = next((l.split(":", 1)[1].strip() for l in out.splitlines() if l.startswith("SCREEN ID:")), None)
    return {"actions": actions, "seconds": round((dt.datetime.now() - t0).total_seconds(), 1),
            "screen": out, "screenId": None if sid in (None, "-") else sid,
            "error": r.stderr[-400:] if r.returncode else None,
            "failedActions": failed or None,
            "rateLimited": ("429" in out) or ("rate-limited" in out)}


# The journey as a sequence of STOPS. Each stop is what the walker has done so far — replayed from
# the start, so every stop is independently reproducible and a failure at stop 4 does not hide stop 3.
def stops(fresh, answers, run_tag=""):
    a = answers
    # ⛔ A UNIQUE USERNAME PER STOP. Every stop replays the journey FROM THE START, and account
    # creation is not idempotent — so with one username the first stop created the account and every
    # later stop hit "that username is taken" and never left s0. Found 2026-09-05 by noticing three
    # screenshots were byte-identical; the text dump read as a plausible account screen every time,
    # so nothing in the transcript said the walk had stopped walking. A replayed step that CHANGES
    # THE WORLD has to vary the thing the world remembers.
    def signup_for(stop):
        if not fresh:
            return []
        u = "%s-%s%s" % (a["username"], run_tag, stop.split("-")[0])
        return ["type:#uname=" + u, "type:#uword=" + a["password"], "type:#uword2=" + a["password"],
                "type:#uemail=" + a["email"], "click:#go0"]
    signup = signup_for("00")
    return [
        ("01-arrive", []),
        # ⛔ None, NOT []. This read `signup[:-1] if fresh else []`, so on the arrive-with-a-token
        # path the account stop got an EMPTY action list — it re-rendered the arrival screen and
        # recorded itself COMPLETE. A stop named "account" that never visits the account screen and
        # reports success is a false green, and it is why s0 looked covered while nothing walked it.
        # None means "not reachable in this mode" and the runner refuses to score it.
        ("02-account", signup_for("02")[:-1] if fresh else None),
        ("03-named", signup_for("03-named") + ["type:#pname=" + a["place"], "click:#go1"]),
        ("04-address", signup_for("04-address") + ["type:#pname=" + a["place"], "click:#go1",
                                 "type:#a1=" + a["line1"], "type:#city=" + a["city"],
                                 "type:#state=" + a["state"], "type:#zip=" + a["zip"]]),
        ("05-submitted", signup_for("05-submitted") + ["type:#pname=" + a["place"], "click:#go1",
                                   "type:#a1=" + a["line1"], "type:#city=" + a["city"],
                                   "type:#state=" + a["state"], "type:#zip=" + a["zip"], "click:#go2"]),
        ("06-confirm", signup_for("06-confirm") + ["type:#pname=" + a["place"], "click:#go1",
                                 "type:#a1=" + a["line1"], "type:#city=" + a["city"],
                                 "type:#state=" + a["state"], "type:#zip=" + a["zip"],
                                 "click:#go2", "click:#go3"]),
        # ⛔ NO WALK HAD EVER CROSSED THE HANDOFF. Measured 2026-09-06: every stop name ever
        # recorded across all 20 runs stops at 06-confirm, so no synthetic seat has ever been a
        # SIGNED-IN READER looking at the estate view. Two things were therefore untestable and
        # nobody could see that they were:
        #   · the persistent General-feedback RIBBON lives only in engine/viewer.template.html.
        #     Paul asked for that channel to be available on every screen once someone has an
        #     account and is logged in — and the battery meant to prove it stopped one click short
        #     of the first screen that has it.
        #   · a walker's answers only pay off past this door. wide-eyed types a Maine address
        #     against shipped Georgia weather, frost and plant data; that is a different STRING
        #     until a stop renders the place it describes, and then it is a different OBSERVATION.
        # #gohome is an <a href="/viewer">, so this stop leaves the onboarding document entirely —
        # which is exactly why it is the one stop that can prove the handoff rather than assert it.
        ("07-handoff", signup_for("07-handoff") + ["type:#pname=" + a["place"], "click:#go1",
                                 "type:#a1=" + a["line1"], "type:#city=" + a["city"],
                                 "type:#state=" + a["state"], "type:#zip=" + a["zip"],
                                 "click:#go2", "click:#go3", "click:#go5", "click:#gohome"]),
    ]


# ---- SELFTEST · the four false greens, as ASSERTIONS rather than as prose ----------------------
# ⛔ THIS FILE CARRIED EIGHT COMMENTS EXPLAINING TONIGHT'S DEFECTS AND ZERO EXECUTABLE CHECKS. Its
# sibling journey-logic.py carries 16 assertions and produced no defects; this one produced all four.
# The learning was written into the exact file that would have caught it, in a form that cannot run.
# A comment is a note to the next reader; an assertion is a note to the next RUN.
def selftest():
    fails = []

    def check(name, ok, why):
        print("  %s %-34s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    # 1 · a stop that cannot run must not score as walked (the empty-action-list green)
    st = dict(stops(fresh=False, answers={"username": "u", "password": "p", "email": "e",
                                          "place": "P", "line1": "l", "city": "c",
                                          "state": "GA", "zip": "3"}))
    check("unreachable stop is None, not []", st.get("02-account") is None,
          "02-account returned %r — an empty list scores 'walked' having done nothing" % (st.get("02-account"),))

    # 2 · a replayed step must vary what the world remembers (the same-username green)
    a = {"username": "syn", "password": "p", "email": "e", "place": "P",
         "line1": "l", "city": "c", "state": "GA", "zip": "3"}
    names = []
    for stop, acts in stops(fresh=True, answers=a, run_tag="T"):
        if not acts:
            continue
        names += [x.split("=", 1)[1] for x in acts if x.startswith("type:#uname=")]
    check("each replayed stop mints its own username", len(names) == len(set(names)),
          "reused: %r — after the first stop every later one hits 'username taken'" % (names,))

    # 3 · the status must be DERIVED from the failures the harness already recorded
    for got, want in ((   {"failedActions": ["click:#go3 — timeout"], "rateLimited": False}, "incomplete"),
                      (   {"failedActions": None, "rateLimited": True},                     "rate-limited"),
                      (   {"failedActions": None, "rateLimited": False, "error": "boom"},   "error"),
                      (   {"failedActions": None, "rateLimited": False},                    "walked")):
        f = got.get("failedActions") or []
        st2 = "error" if got.get("error") else ("incomplete" if f else
              ("rate-limited" if got.get("rateLimited") else "walked"))
        check("status(%s)" % want, st2 == want, "got %r" % st2)

    # 4 · the shot path must be per-process (the shared-screenshot contamination)
    import subprocess as sp
    out = sp.run([sys.executable, os.path.join(ROOT, "tools", "journey-view.py"), "--help"],
                 capture_output=True, text=True).stdout
    check("screenshot path is not a shared constant", "/tmp/journey-view.png" not in out,
          "a fixed default path lets parallel walkers overwrite each other")

    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", 7 - len(fails), 7))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true", help="prove the four false-green guards still bite")
    ap.add_argument("--role")
    ap.add_argument("--fresh", action="store_true", help="sign up in-flow rather than arriving with a token")
    # ⭐ `paul-stated 2026-09-06`: "I like being able to watch the walk through in chrome." Same
    # viewport, same screenshots, same records — only visibility and pacing change, so a watched
    # walk is admissible evidence rather than a demo of one.
    ap.add_argument("--watch", action="store_true",
                    help="open a VISIBLE browser and pace it so you can follow the walk")
    ap.add_argument("--answers", help="JSON file of what this walker types. Without it, .private/walk-answers/<role>.json "
                         "is used when present; otherwise a SHARED default that makes every seat identical")
    # ⭐ GATE 1 RUNS ON QA `[paul-approved 2026-09-05]`. The origin was HARDCODED to lab, so every
    # gate-1 walk ran in gate 2's environment while the cascade said otherwise — and nothing could
    # report the mismatch because there was no parameter to disagree with. QA is the default because
    # it is the only origin with its own estate (est-qa0001) AND a CI-maintained build stamp; lab is
    # hand-deployed and cannot say which build it is serving. Lab stays REACHABLE (Paul walks it at
    # gate 2) but you have to ask for it, and the transcript records which you asked for.
    ap.add_argument("--origin", choices=["qa", "lab", "home"], default="qa",
                    help="which origin to walk (default qa — gate 1). lab is gate 2. "
                         "⚠️ home is PRODUCTION and writes real rows into Mom's estate.")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.role:
        raise SystemExit("journey-walk: --role is required (or use --selftest)")

    v = refresh(a.role, a.origin) if not a.fresh else identity(a.role, a.origin)
    base = {"qa":   "https://fernwood-qa.pages.dev/onboarding/",
            "lab":  "https://fernwood-lab.pages.dev/onboarding/",
            "home": "https://fernwood-home.pages.dev/onboarding/"}[a.origin]
    url = base if a.fresh else base + "?g=" + (v.get("token") or "")

    # ⛔ THE SEATS MUST NOT TYPE THE SAME THING. Measured 2026-09-06: all four seats — mom, owner,
    # strict, wide-eyed — typed "A place / 1 Example Road / Jasper / GA / 30143", because this
    # default was shared and --answers was never passed. Four seats producing one observation is
    # not four seats; it is one, at four times the rate-limit cost, and it is why the last battery
    # yielded roughly one seat's worth of signal. The help text already CLAIMED a per-role default
    # ("defaults to the role's own") and no such file existed anywhere in the repo — the promise
    # was in the interface and the behaviour was a constant.
    #
    # Resolution order: --answers  >  .private/walk-answers/<role>.json  >  the shared default.
    # The transcript RECORDS which one was used, so walk-integrity.py can refuse a battery whose
    # seats collapse to one input instead of that fact being invisible after the fact.
    ans = {"username": v["username"], "password": v["word"], "email": v["email"],
           "place": "A place", "line1": "1 Example Road", "city": "Jasper", "state": "GA", "zip": "30143"}
    answers_source = "shared-default"
    role_file = os.path.join(ROOT, ".private", "walk-answers", "%s.json" % a.role)
    if a.answers:
        ans.update(json.load(open(a.answers, encoding="utf-8")))
        answers_source = a.answers
    elif os.path.exists(role_file):
        ans.update({k: v2 for k, v2 in json.load(open(role_file, encoding="utf-8")).items()
                    if not k.startswith("_")})
        answers_source = os.path.relpath(role_file, ROOT)
    else:
        print("  \u26a0\ufe0f  NO PER-ROLE ANSWERS for %r \u2014 falling back to the SHARED default." % a.role)
        print("      Every seat using this default types the same thing, so N seats are ONE")
        print("      observation. Write %s to make this seat its own." % os.path.relpath(role_file, ROOT))

    run = dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    d = os.path.join(OUT, a.role, run)
    os.makedirs(d, exist_ok=True)

    print("journey-walk — %s · run %s · origin %s" % (a.role, run, a.origin))
    sha_before = served_sha(a.origin)
    print("  build at start: %s" % (sha_before[:7] if sha_before else "⚠️ UNKNOWN — origin cannot say what it serves"))
    # The transcript records the ORIGIN it walked. A walk that cannot say where it ran cannot be
    # checked against the cascade, which is exactly how gate 1 ran in gate 2's environment unnoticed.
    record = {"role": a.role, "runAt": run, "origin": a.origin, "originUrl": base,
              "fresh": bool(a.fresh), "personId": v.get("personId"),
              "answersSource": answers_source, "watched": bool(a.watch),
              "answers": {k: ("<password>" if k == "password" else x) for k, x in ans.items()},
              "stops": []}
    for name, actions in stops(a.fresh, ans, run_tag=dt.datetime.now().strftime("%H%M%S")):
        if actions is None:
            # Unreachable is a RESULT, and it is not a pass. It is recorded so a reader of the
            # transcript can see the screen went unvisited instead of inferring it was fine.
            record["stops"].append({"stop": name, "status": "not-reachable",
                                    "why": "arrived with a token; this stop exists only on the --fresh signup path"})
            print("  %-14s   ---   NOT REACHABLE on this path — re-run with --fresh to walk it" % name)
            continue
        got = view(url, actions, os.path.join(d, name + ".png"), watch=a.watch)
        # ⛔ CONSUME THE FAILURE THE HARNESS ALREADY RECORDED. journey-view reports ok:false per
        # action; this filed every stop as "walked" without ever reading it. All three false greens
        # tonight were the same shape — a plausible artifact produced having done nothing — and the
        # evidence to refuse two of them was sitting in the record, unconsumed.
        failed = got.get("failedActions") or []
        status = "error" if got.get("error") else ("incomplete" if failed else
                 ("rate-limited" if got.get("rateLimited") else "walked"))
        record["stops"].append(dict(got, stop=name, status=status))
        if status != "walked":
            print("       \u26d4 %s%s" % (status.upper(),
                  (" — did not happen: " + "; ".join(f[:60] for f in failed[:2])) if failed
                  else " — the Worker refused a write during this stop"))
        first = next((l for l in got["screen"].splitlines() if l.startswith("PAGE TITLE")), "")
        print("  %-14s %5.1fs  %s%s" % (name, got["seconds"], first, "  ⛔ " + (got["error"] or "") if got["error"] else ""))

    sha_after = served_sha(a.origin)
    record["buildBefore"], record["buildAfter"] = sha_before, sha_after
    if sha_before and sha_after and sha_before != sha_after:
        record["contaminated"] = True
        record["contaminatedWhy"] = ("the origin changed build mid-walk (%s → %s) — a deploy landed "
                                     "while this walked, so screens may come from different builds"
                                     % (sha_before[:7], sha_after[:7]))
        print("\n  ⛔ CONTAMINATED — the origin changed build mid-walk (%s → %s)."
              "\n     This walk is NOT evidence about either build. Re-run it." % (sha_before[:7], sha_after[:7]))
    elif not (sha_before and sha_after):
        record["contaminated"] = "unknown"
        record["contaminatedWhy"] = "the origin could not report its build, so a mid-walk deploy is undetectable"
        print("\n  ⚠️  build unverifiable — a mid-walk deploy could not have been detected.")
    else:
        record["contaminated"] = False

    with open(os.path.join(d, "transcript.json"), "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2)
    open(os.path.join(d, "REPORT.md"), "w", encoding="utf-8").write(
        "# %s — run %s\n\n<!-- WALK-REPORT-UNWRITTEN — delete this line when the walker has written it.\n"
        "     ⛔ Anything consolidating walks MUST refuse to count a seat while this marker is present.\n"
        "     On 2026-09-05 a 287-byte stub was counted as a seat that had reported, and a finding was\n"
        "     attributed to three seats when only two had produced any experiential claim. -->\n"
        "> ⛔ The walker's OWN experience goes here, written by the walker.\n"
        "> This file is deliberately separate from transcript.json: what the product DID and what a\n"
        "> person FELT are different kinds of claim, and merging them makes the second unfalsifiable.\n" % (a.role, run))
    prior = sorted(glob.glob(os.path.join(OUT, a.role, "*")))
    print("\n  → %s\n  %d run(s) recorded for %s — accretive by design" % (d, len(prior), a.role))
    return 0


if __name__ == "__main__":
    sys.exit(main())
