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
import argparse, datetime as dt, glob, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, ".private", "synthetic-identities.json")
OUT = os.path.join(ROOT, ".private", "synthetic-walks")


def identity(role):
    d = json.load(open(STORE, encoding="utf-8"))
    v = (d.get("identities") or {}).get(role)
    if not v:
        raise SystemExit("journey-walk: no identity %r — `synthetic-identity.py --create %s`" % (role, role))
    return v


def refresh(role):
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "synthetic-identity.py"), "--login", role],
                   capture_output=True, text=True, timeout=180)
    return identity(role)


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
    a = ap.parse_args()

    v = refresh(a.role) if not a.fresh else identity(a.role)
    base = "https://fernwood-lab.pages.dev/onboarding/"
    url = base if a.fresh else base + "?g=" + (v.get("token") or "")

    ans = {"username": v["username"], "password": v["word"], "email": v["email"],
           "place": "A place", "line1": "1 Example Road", "city": "Jasper", "state": "GA", "zip": "30143"}
    if a.answers:
        ans.update(json.load(open(a.answers, encoding="utf-8")))

    run = dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    d = os.path.join(OUT, a.role, run)
    os.makedirs(d, exist_ok=True)

    print("journey-walk — %s · run %s" % (a.role, run))
    record = {"role": a.role, "runAt": run, "fresh": bool(a.fresh), "personId": v.get("personId"),
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
