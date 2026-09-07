#!/usr/bin/env python3
"""release-state.py — the release loop's STATE ARTIFACT (S1), derived, never typed.

    python3 tools/release-state.py            # print
    python3 tools/release-state.py --write    # cycle/release/cycle-state.json
    python3 tools/release-state.py --sha <candidate> --write   # when HEAD moved by a non-app commit
                                              # after the candidate was deployed and walked (round 10)

⭐ WHY `[practice-steward, 2026-09-06, §D]`: the loop had a map and a gate and no state — nothing a
board could read, nothing that said which beat the lap was on or whose it was. Every value here is
DERIVED from the gate, the run folders and git at the moment of writing; a hand-typed count beside a
tool that computes it is the CYCLE-SPINE's own recorded failure mode. S2 is `beat.owner`: when it
reads "paul", a human gate is open and no session may pretend to pass it. S4b is `cleared_sha`,
written only by `--cleared <sha>` on Paul's word, never derived.
"""
import argparse, datetime as dt, importlib.util, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "cycle", "release", "cycle-state.json")


def gate_module():
    spec = importlib.util.spec_from_file_location("rg", os.path.join(ROOT, "tools", "release-gate.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def derive(cleared=None, prior=None, sha=None):
    rg = gate_module()
    if sha:
        sha = subprocess.check_output(["git", "-C", ROOT, "rev-parse", sha], text=True).strip()
    else:
        sha = rg.head_sha()
    seats = {}
    for seat in rg.seats():
        best = None
        for run in rg.runs_for(seat):
            v = rg.judge(os.path.join(rg.WALKS, seat, run), sha[:40])
            if v.get("at-sha", (False, ""))[0]:
                score = sum(1 for k, _ in rg.CLAUSES if v.get(k, (None,))[0] is True)
                if best is None or score > best[0]:
                    best = (score, run, v)
        if best:
            _, run, v = best
            seats[seat] = {"run": run, **{k: v.get(k, (None, ""))[0] for k in [c for c, _ in rg.CLAUSES] + ["instrumented"]}}
        else:
            seats[seat] = {"run": None}
    seats_pass = bool(seats) and all(all(s.get(k) is True for k, _ in rg.CLAUSES) for s in seats.values())
    prior = prior or {}
    last = prior.get("last_lap") or {"lap": 1, "opened": "2026-09-06", "outcome": "open"}
    cleared_sha = cleared or last.get("cleared_sha")
    if cleared_sha and sha.startswith(cleared_sha):
        beat, owner, state, outcome = 5, "paul", "ARMED", "cleared"
    elif seats_pass:
        beat, owner, state, outcome = 3, "paul", "FIRED", "open"       # a human gate is open
    else:
        beat, owner, state, outcome = 2, "session", "FIRED", "open"
    last = dict(last, outcome=outcome, **({"cleared_sha": cleared_sha} if cleared_sha else {}))
    return {
        "state": state,
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "generated_by": "tools/release-state.py",
        "candidate_sha": sha[:7],
        "beat": {"n": beat, "of": 5, "owner": owner,
                 "name": {2: "the synthetic loop", 3: "Paul walks it", 5: "Paul cleared it"}[beat]},
        "gate_1": {"seats_pass": seats_pass, "ux_clause": "UNCHECKABLE — no artifact convention",
                   "seats": seats},
        "last_lap": last,
        "pre_registered": prior.get("pre_registered") or [
            {"id": "instrumented-counted", "question": "at the lap-1 candidate sha, does every seat's capture.json show ≥1 app event via grant?",
             "disposition": "open", "evidence": None},
            {"id": "second-viewport", "question": "does a laptop-width walk find what 414 hides (Paul found one on 2026-09-06)?",
             "disposition": "open", "evidence": None},
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--cleared", help="Paul cleared this sha (his word, typed by a session on his say-so)")
    ap.add_argument("--sha", help="derive against this build instead of HEAD (the deployed, walked candidate when HEAD moved by a non-app commit)")
    a = ap.parse_args()
    prior = None
    try: prior = json.load(open(STATE, encoding="utf-8"))
    except (OSError, ValueError): pass
    st = derive(cleared=a.cleared, prior=prior, sha=a.sha)
    print("release loop — %s · beat %d/%d (%s) · owner: %s · candidate %s · seats pass: %s"
          % (st["state"], st["beat"]["n"], st["beat"]["of"], st["beat"]["name"], st["beat"]["owner"],
             st["candidate_sha"], st["gate_1"]["seats_pass"]))
    if a.write:
        os.makedirs(os.path.dirname(STATE), exist_ok=True)
        json.dump(st, open(STATE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print("  → %s" % os.path.relpath(STATE, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
