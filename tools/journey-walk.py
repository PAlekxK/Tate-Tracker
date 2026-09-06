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


def view(url, actions, shot, watch=False, shot_dir=None):
    cmd = [sys.executable, os.path.join(ROOT, "tools", "journey-view.py"), url, "--shot", shot]
    if shot_dir:
        cmd += ["--shot-dir", shot_dir, "--json", os.path.join(shot_dir, "_view.json")]
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
    # journey-view prints one CHECKPOINT line per `shot:` — name | screen | title | shot path.
    # Prefer the structured result — it carries every checkpoint's FULL screen. The stdout parse
    # below is the fallback for a direct call with no --shot-dir, and it is lossy by construction.
    cps = []
    if shot_dir:
        try:
            full = json.load(open(os.path.join(shot_dir, "_view.json"), encoding="utf-8"))
            for c in full.get("checkpoints") or []:
                sc = c.get("screen") or {}
                cps.append({"stop": c.get("name"), "screen": sc.get("screenId"),
                            "title": sc.get("title"), "shot": c.get("shot"),
                            "text": sc.get("text") or [], "fields": sc.get("fields") or [],
                            "buttons": sc.get("buttons") or [], "url": sc.get("url")})
        except (OSError, ValueError):
            cps = []
    for l in ([] if cps else out.splitlines()):
        if not l.startswith("CHECKPOINT "):
            continue
        parts = [x.strip() for x in l[len("CHECKPOINT "):].split("|")]
        d = {"stop": parts[0]}
        for x in parts[1:]:
            k, _, v = x.partition("=")
            d[k.strip()] = v.strip()
        cps.append(d)
    return {"actions": actions, "seconds": round((dt.datetime.now() - t0).total_seconds(), 1),
            "screen": out, "screenId": None if sid in (None, "-") else sid,
            "checkpoints": cps,
            "error": r.stderr[-400:] if r.returncode else None,
            "failedActions": failed or None,
            "rateLimited": ("429" in out) or ("rate-limited" in out)}


# ⭐ ONE CONTINUOUS JOURNEY, CHECKPOINTED — replaces the replay-every-prefix design
# `[paul-stated 2026-09-06]`: "I want all the synthetics to run profile creation in chrome that we
# can watch." Two things were wrong with replaying, and they were the same thing:
#
#   · IT COST FIVE ACCOUNTS PER SEAT. Every stop re-ran signup from scratch, and since account
#     creation is not idempotent each stop had to mint a fresh username. Measured on the 09-05
#     production runs: 47 actions and 5 account creations per walk, 13 walks. That — not four
#     seats — is what flooded a limiter of 20 writes per IP per 5 minutes.
#   · IT IS NOT WHAT A PERSON DOES. A real reader arrives once and walks forward. Replaying each
#     prefix tests a journey nobody takes, and watching it looks like a machine restarting rather
#     than someone using the app.
#
# A `shot:<name>` checkpoint records the full screen mid-journey, so ONE session still yields the
# same per-stop evidence — same names, same screenshots, same screen text.
#
# ⚠️ THE TRADE, STATED: a failure now CASCADES. If naming the place fails, nothing after it runs.
# That is the honest behaviour — a reader who cannot name her place never reaches the address
# screen either — but it means a late stop's absence is no longer independent evidence that the
# late stop is broken. walk-integrity refuses a run with incomplete stops for exactly this reason.
STOP_NAMES = ["01-arrive", "02-account", "03-named", "04-address",
              "05-submitted", "06-confirm", "07-handoff"]


def journey(fresh, answers):
    """The whole walk as ONE action list. `shot:<name>` marks where a stop is recorded."""
    a = answers
    acts = ["shot:01-arrive"]
    if fresh:
        acts += ["type:#uname=" + a["username"], "type:#uword=" + a["password"],
                 "type:#uword2=" + a["password"], "type:#uemail=" + a["email"],
                 "shot:02-account", "click:#go0"]
    else:
        # Arriving on a token skips the account screen. It is recorded as NOT REACHABLE rather than
        # silently missing — a stop that never happened must not read like one that passed.
        acts += ["shot:02-account"]
    acts += ["type:#pname=" + a["place"], "click:#go1", "shot:03-named",
             "type:#a1=" + a["line1"], "type:#city=" + a["city"],
             "type:#state=" + a["state"], "type:#zip=" + a["zip"], "shot:04-address",
             "click:#go2", "shot:05-submitted",
             "click:#go3", "shot:06-confirm",
             "click:#go5", "click:#gohome", "shot:07-handoff"]
    return acts


# ---- SELFTEST · the four false greens, as ASSERTIONS rather than as prose ----------------------
# ⛔ THIS FILE CARRIED EIGHT COMMENTS EXPLAINING TONIGHT'S DEFECTS AND ZERO EXECUTABLE CHECKS. Its
# sibling journey-logic.py carries 16 assertions and produced no defects; this one produced all four.
# The learning was written into the exact file that would have caught it, in a form that cannot run.
# A comment is a note to the next reader; an assertion is a note to the next RUN.
def selftest():
    fails = []

    def check(name, ok, why):
        print("  %s %-44s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    A = {"username": "syn", "password": "p", "email": "e@x.com", "place": "P",
         "line1": "l", "city": "c", "state": "GA", "zip": "3"}

    # 1 · ⭐ THE LIMITER FIX, AS AN ASSERTION. The replay design minted a username per stop and so
    #     created FIVE accounts per seat; that is what flooded 20-per-5-minutes. One journey, one
    #     account. If this ever regresses, the battery starts DOSing the target again silently.
    fresh = journey(fresh=True, answers=A)
    signups = [x for x in fresh if x.startswith("type:#uname=")]
    check("a fresh journey creates exactly ONE account", len(signups) == 1,
          "found %d signup(s) — every extra one is a real account and a real write" % len(signups))

    # 2 · arriving on a token must create none at all
    tok = journey(fresh=False, answers=A)
    check("a token arrival creates NO account",
          not [x for x in tok if x.startswith("type:#uname=")], "a signup leaked into the token path")

    # 3 · every declared stop must actually be captured, or a stop silently stops existing
    shots = [x[5:] for x in fresh if x.startswith("shot:")]
    check("every STOP_NAME is checkpointed", shots == STOP_NAMES,
          "declared %r but the journey shoots %r" % (STOP_NAMES, shots))

    # 4 · ⭐ THE HANDOFF IS WALKED. No walk had ever crossed it before 2026-09-06 — every stop name
    #     ever recorded stopped at 06-confirm — so the estate view, and the feedback ribbon that
    #     lives only there, had been walked by nobody.
    check("the journey crosses the handoff", "click:#gohome" in fresh,
          "nothing clicks #gohome, so no seat is ever a signed-in reader")

    # 5 · the status derivation the old harness lacked, which scored every stop 'walked'
    for got, want in ((   {"failedActions": ["click:#go3 — timeout"], "rateLimited": False}, "incomplete"),
                      (   {"failedActions": None, "rateLimited": True},                     "rate-limited"),
                      (   {"failedActions": None, "rateLimited": False, "error": "boom"},   "error"),
                      (   {"failedActions": None, "rateLimited": False},                    "walked")):
        f = got.get("failedActions") or []
        st = "error" if got.get("error") else ("incomplete" if f else
             ("rate-limited" if got.get("rateLimited") else "walked"))
        check("status(%s)" % want, st == want, "got %r" % st)

    # 6 · the shared-screenshot contamination
    import subprocess as sp
    out = sp.run([sys.executable, os.path.join(ROOT, "tools", "journey-view.py"), "--help"],
                 capture_output=True, text=True).stdout
    check("screenshot path is not a shared constant", "/tmp/journey-view.png" not in out,
          "a fixed default path lets parallel walkers overwrite each other")

    # 7 · the cost of a walk, asserted rather than assumed
    writes = len([x for x in fresh if x.startswith("click:#go")])
    check("a fresh walk spends few enough writes to stay under the limiter", writes <= 6,
          "%d submit clicks — the cap is 20 writes per IP per 5 min, shared by 4 seats" % writes)

    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", 10 - len(fails), 10))
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

    # ⛔ BOTH PATHS REFRESH. The fresh path used the STORED token, which is a grant row that may
    # long since have gone — and a dead grant is indistinguishable from no grant, so the walk would
    # meet `invite-required` and read as a product failure rather than a stale fixture. Logging in
    # first guarantees the invite the walker arrives on is live at the moment she uses it.
    v = refresh(a.role, a.origin)
    base = {"qa":   "https://fernwood-qa.pages.dev/onboarding/",
            "lab":  "https://fernwood-lab.pages.dev/onboarding/",
            "home": "https://fernwood-home.pages.dev/onboarding/"}[a.origin]
    # ⛔ FRESH MUST ARRIVE ON AN INVITE TOO. This read `base if a.fresh`, i.e. no grant at all —
    # and since c111417 (2026-09-05 23:31) /api/account answers `invite-required` 403 without one:
    # "the capability now comes from the invite and never from the applicant." No fresh walk has
    # run since that commit, so the harness has been unable to create a profile for a day and
    # nothing said so. The fresh/token distinction is NOT whether she holds a grant — an invited
    # person always does — it is whether she CREATES an account or arrives already having one.
    url = base + "?g=" + (v.get("token") or "")

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
    # ⛔ A REPLAYED-WORLD STEP MUST VARY WHAT THE WORLD REMEMBERS. Account creation is not
    # idempotent, so a second fresh run for the same seat would hit "that username is taken" and
    # never leave s0 — the 2026-09-05 defect, which the old design solved per STOP and this one
    # still needs per RUN. Only the fresh path uniquifies: a token arrival signs in as the
    # identity that already exists and must keep its real username.
    run_tag = dt.datetime.now().strftime("%H%M%S")
    ans = {"username": (v["username"] + "-" + run_tag) if a.fresh else v["username"],
           "password": v["word"], "email": v["email"],
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
    acts = journey(a.fresh, ans)
    print("  one continuous journey — %d actions, %d checkpoints, %s"
          % (len([x for x in acts if not x.startswith("shot:")]), len(STOP_NAMES),
             "ONE account created" if a.fresh else "arriving on a token (no account created)"))
    got = view(url, acts, os.path.join(d, "final.png"), watch=a.watch, shot_dir=d)
    failed_all = got.get("failedActions") or []
    seen = {c["stop"]: c for c in got.get("checkpoints") or []}

    for name in STOP_NAMES:
        if name == "02-account" and not a.fresh:
            record["stops"].append({"stop": name, "status": "not-reachable",
                                    "why": "arrived with a token; this stop exists only on the --fresh signup path"})
            print("  %-14s   ---   NOT REACHABLE on this path — re-run with --fresh to walk it" % name)
            continue
        cp = seen.get(name)
        if not cp:
            # ⛔ A CHECKPOINT THAT NEVER FIRED IS A STOP THE WALKER NEVER REACHED. In the continuous
            # design this is the normal shape of a failure — the journey stopped earlier — so it is
            # recorded as its own status rather than omitted, because an absent stop and a passed
            # stop must never render the same.
            record["stops"].append({"stop": name, "status": "not-reached",
                                    "why": "the journey did not get this far; see the earlier failure"})
            print("  %-14s   ---   ⛔ NOT REACHED" % name)
            continue
        record["stops"].append({"stop": name, "status": "walked", "screenId": cp.get("screen"),
                                "title": cp.get("title"), "shot": cp.get("shot"),
                                "url": cp.get("url"),
                                # the full screen, kept per stop — this is what a later reader
                                # re-reads with a new question in mind, and what the integrity
                                # check scans for a stop that reports success over a failure.
                                "screen": cp.get("text") or [], "fields": cp.get("fields") or [],
                                "buttons": cp.get("buttons") or []})
        print("  %-14s  screen=%-4s %s" % (name, cp.get("screen") or "-", cp.get("title") or ""))

    # The failures belong to the JOURNEY, not to a stop — one session, one action stream.
    if failed_all:
        record["failedActions"] = failed_all
        print("\n  ⛔ %d action(s) did not happen:" % len(failed_all))
        for f in failed_all[:4]:
            print("       %s" % f[:110])
    if got.get("rateLimited"):
        record["rateLimited"] = True
        print("  ⛔ RATE-LIMITED during this walk — the Worker refused a write")
    if got.get("error"):
        record["error"] = got["error"]

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
