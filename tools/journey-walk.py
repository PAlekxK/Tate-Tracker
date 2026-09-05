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
    url = {"qa": "https://fernwood-qa.pages.dev", "lab": "https://fernwood-lab.pages.dev"}[env]
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


def view(url, actions, shot):
    cmd = [sys.executable, os.path.join(ROOT, "tools", "journey-view.py"), url, "--shot", shot]
    for a in actions:
        cmd += ["--do", a]
    t0 = dt.datetime.now()
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    return {"actions": actions, "seconds": round((dt.datetime.now() - t0).total_seconds(), 1),
            "screen": r.stdout, "error": r.stderr[-400:] if r.returncode else None}


# The journey as a sequence of STOPS. Each stop is what the walker has done so far — replayed from
# the start, so every stop is independently reproducible and a failure at stop 4 does not hide stop 3.
def stops(fresh, answers):
    a = answers
    signup = ([] if not fresh else [
        "type:#uname=" + a["username"], "type:#uword=" + a["password"], "type:#uword2=" + a["password"],
        "type:#uemail=" + a["email"], "click:#go0"])
    return [
        ("01-arrive", []),
        # ⛔ None, NOT []. This read `signup[:-1] if fresh else []`, so on the arrive-with-a-token
        # path the account stop got an EMPTY action list — it re-rendered the arrival screen and
        # recorded itself COMPLETE. A stop named "account" that never visits the account screen and
        # reports success is a false green, and it is why s0 looked covered while nothing walked it.
        # None means "not reachable in this mode" and the runner refuses to score it.
        ("02-account", signup[:-1] if fresh else None),
        ("03-named", signup + ["type:#pname=" + a["place"], "click:#go1"]),
        ("04-address", signup + ["type:#pname=" + a["place"], "click:#go1",
                                 "type:#a1=" + a["line1"], "type:#city=" + a["city"],
                                 "type:#state=" + a["state"], "type:#zip=" + a["zip"]]),
        ("05-submitted", signup + ["type:#pname=" + a["place"], "click:#go1",
                                   "type:#a1=" + a["line1"], "type:#city=" + a["city"],
                                   "type:#state=" + a["state"], "type:#zip=" + a["zip"], "click:#go2"]),
        ("06-confirm", signup + ["type:#pname=" + a["place"], "click:#go1",
                                 "type:#a1=" + a["line1"], "type:#city=" + a["city"],
                                 "type:#state=" + a["state"], "type:#zip=" + a["zip"],
                                 "click:#go2", "click:#go3"]),
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--role", required=True)
    ap.add_argument("--fresh", action="store_true", help="sign up in-flow rather than arriving with a token")
    ap.add_argument("--answers", help="JSON file of what this walker types; defaults to the role's own")
    # ⭐ GATE 1 RUNS ON QA `[paul-approved 2026-09-05]`. The origin was HARDCODED to lab, so every
    # gate-1 walk ran in gate 2's environment while the cascade said otherwise — and nothing could
    # report the mismatch because there was no parameter to disagree with. QA is the default because
    # it is the only origin with its own estate (est-qa0001) AND a CI-maintained build stamp; lab is
    # hand-deployed and cannot say which build it is serving. Lab stays REACHABLE (Paul walks it at
    # gate 2) but you have to ask for it, and the transcript records which you asked for.
    ap.add_argument("--origin", choices=["qa", "lab"], default="qa",
                    help="which origin to walk (default qa — gate 1). lab is gate 2, Paul's seat.")
    a = ap.parse_args()

    v = refresh(a.role, a.origin) if not a.fresh else identity(a.role, a.origin)
    base = {"qa":  "https://fernwood-qa.pages.dev/onboarding/",
            "lab": "https://fernwood-lab.pages.dev/onboarding/"}[a.origin]
    url = base if a.fresh else base + "?g=" + (v.get("token") or "")

    ans = {"username": v["username"], "password": v["word"], "email": v["email"],
           "place": "A place", "line1": "1 Example Road", "city": "Jasper", "state": "GA", "zip": "30143"}
    if a.answers:
        ans.update(json.load(open(a.answers, encoding="utf-8")))

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
              "answers": {k: ("<password>" if k == "password" else x) for k, x in ans.items()},
              "stops": []}
    for name, actions in stops(a.fresh, ans):
        if actions is None:
            # Unreachable is a RESULT, and it is not a pass. It is recorded so a reader of the
            # transcript can see the screen went unvisited instead of inferring it was fine.
            record["stops"].append({"stop": name, "status": "not-reachable",
                                    "why": "arrived with a token; this stop exists only on the --fresh signup path"})
            print("  %-14s   ---   NOT REACHABLE on this path — re-run with --fresh to walk it" % name)
            continue
        got = view(url, actions, os.path.join(d, name + ".png"))
        record["stops"].append(dict(got, stop=name, status="walked"))
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
