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
import argparse, copy, datetime as dt, importlib.util, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "cycle", "release", "cycle-state.json")
LOG = os.path.join(ROOT, "cycle", "release", "CYCLE-LOG.md")


def momlib_module():
    spec = importlib.util.spec_from_file_location("momlib", os.path.join(ROOT, "tools", "momlib.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


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
    # ⭐⭐ J-c `[paul-ruled 2026-09-07]` — THE CHRONICLE IS THE SOURCE OF LAP STATE, not this JSON.
    # WHAT THIS REPLACED AND WHY: the line here read
    #     last = prior.get("last_lap") or {"lap": 1, "opened": "2026-09-06", "outcome": "open"}
    # — a DERIVED cache seeded from a hardcoded default and then carried forward from its own prior
    # copy, with no path back to what actually happened. It lost lap 2 and Paul's clear: on 2026-09-07
    # the chronicle recorded two closed laps while this file still read `lap: 1, cleared_sha: c821051`.
    # That is the second time this artifact has misreported the lap count.
    # ⛔ THE ASYMMETRY THAT MAKES THIS SAFE: the chronicle is where a human writes what happened, so it
    # is the only record that can be WRONG IN A WAY SOMEONE NOTICES. A cache that silently reverts is
    # wrong in a way nobody notices, which is the failure this ruling removes.
    # ⭐ `mom-cycle-status.py:661` already did exactly this; the release loop was the laggard.
    # ⚠️ `cleared_sha` is NOT derived from the chronicle and must not be. It is S4b — written only by
    # `--cleared <sha>` on Paul's word. The chronicle's heading mentions a sha in PROSE and parsing it
    # out would make a human gate machine-derivable, which is the one thing S2/S4b exist to prevent.
    lap_count, chron, anomalies = None, None, []
    try:
        _ml = momlib_module()
        lap_count, chron = _ml.lap_state(LOG)
        anomalies = _ml.lap_heading_anomalies(LOG)
    except Exception as exc:                       # noqa: BLE001
        lap_count = None                           # UNMEASURED, never 0
        anomalies = [(0, f"lap census unreadable: {type(exc).__name__}")]
    prior_last = prior.get("last_lap") or {}
    if chron:
        last = {"lap": chron["n"], "opened": chron["date"],
                "outcome": chron["outcome"] or "unknown", "closed_at": chron.get("closed_at")}
    else:
        last = {"lap": None, "opened": None, "outcome": "unknown"}
    cleared_sha = cleared or prior_last.get("cleared_sha")
    if cleared_sha and sha.startswith(cleared_sha):
        beat, owner, state, outcome = 5, "paul", "ARMED", "cleared"
    elif seats_pass:
        beat, owner, state, outcome = 3, "paul", "FIRED", "open"       # a human gate is open
    else:
        beat, owner, state, outcome = 2, "session", "FIRED", "open"
    # ⛔ `outcome` (computed just above) is about the CURRENT CANDIDATE; `last_lap.outcome` is about
    # the LAST LAP IN THE CHRONICLE. They are different questions and the old code conflated them by
    # overwriting one with the other — which is how this field came to publish `"cleared"`, a value
    # that is not in the CYCLE-SPINE's enum at all (noted at CYCLE-LOG.md:922). The chronicle's enum
    # (`closed` · `abandoned` · unmarked→`unknown`) now stands, and the candidate's story is carried
    # by `beat`/`state`, which is what those fields were always for.
    last = dict(last, **({"cleared_sha": cleared_sha} if cleared_sha else {}))
    return {
        "state": state,
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "generated_by": "tools/release-state.py",
        "candidate_sha": sha[:7],
        # ⛔ "of": 5 WAS FALSE AFTER A-1 `[process-audit D2, 2026-09-07]`. The map gained beats 0 and
        # 6-11 that night; this line kept publishing a five-beat loop, so `cycle-state.json` read
        # "beat 2 of 5" while the loop was sitting in the estate-manager beats — and
        # operating-layer's portfolio render recorded that false beat as verified.
        # ⭐ AND THE HONEST HALF, which is why `derivable` exists rather than just bumping the 5:
        # this tool derives from the GATE and GIT, and those can only ever speak to beats 2, 3 and 5.
        # Beats 0, 1 and 6-11 are human or session beats with no artifact to read, so a number here
        # is not evidence about them. Publishing `of: 11` alone would have swapped one false claim
        # for a vaguer one; naming what is derivable says which part of the count is measured.
        "beat": {"n": beat, "of": 11, "owner": owner,
                 "name": {2: "the synthetic loop", 3: "Paul walks it", 5: "Paul cleared it"}[beat],
                 "derivable": [2, 3, 5],
                 "_note": "beats 0, 1 and 6-11 are human or session beats this tool cannot observe; "
                          "`n` is only ever one of `derivable`. Read CYCLE-MAP.md for the full ladder."},
        "gate_1": {"seats_pass": seats_pass, "ux_clause": "UNCHECKABLE — no artifact convention",
                   "seats": seats},
        "lap_count": lap_count,
        "last_lap": last,
        # ⛔ Non-empty means a hand-typed heading did not parse and A LAP IS MISSING FROM THE COUNT.
        # Empty is not proof of completeness — only that nothing heading-shaped was rejected.
        "lap_heading_anomalies": [{"line": n, "text": t} for n, t in anomalies],
        # ⛔ DEEP-COPIED, NOT ALIASED. `prior.get("pre_registered")` hands back the SAME LIST OBJECT
        # the prior state holds, so anything that appends to the derived state also appends to
        # `prior` — and the `same` guard below then compares a list against itself, finds no
        # difference, and SKIPS THE WRITE. Measured 2026-09-07 the moment `--pre-register` was added:
        # it reported "✚ pre-registered: P1…P5" and wrote nothing, which is the worst shape a bug can
        # take — a success line over a no-op. Any future writer of this field would have hit it too.
        "pre_registered": copy.deepcopy(prior.get("pre_registered")) or [
            # ⛔ `disposition` IS THE SPINE'S ENUM — `open | answered | carried | dropped`
            # (CYCLE-SPINE.md:210), and `answered` requires non-empty `evidence`. Lap 3 wrote
            # "closed" and "retired" here, both off the enum — the same class as the
            # `outcome: "cleared"` bug fixed in the neighbouring field, in the same commit.
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
    # ⭐ D3 `[process-audit, 2026-09-07]`: this tool CARRIED `pre_registered[]` forward and could never
    # ADD to it, so a lap's own pre-registrations lived in prose in the retro and nothing existed to
    # discharge them against at close. Beat 0's exit requires DISPOSING the prior lap's — it never
    # required WRITING this lap's, and the gap is exactly the "amend before reset" half of
    # `[[feedback_retro_improvement_closes_a_cycle]]`, which is two-sided by ruling.
    ap.add_argument("--pre-register", metavar="FILE",
                    help="a JSON list of {id, question, ...} to ADD to pre_registered[]. "
                         "⛔ Refuses to overwrite an id that already exists — a disposition is "
                         "evidence and must never be silently replaced by a re-registration.")
    ap.add_argument("--sha", help="derive against this build instead of HEAD (the deployed, walked candidate when HEAD moved by a non-app commit)")
    a = ap.parse_args()
    prior = None
    try: prior = json.load(open(STATE, encoding="utf-8"))
    except (OSError, ValueError): pass
    # ⭐ THE CANDIDATE IS THE BUILD QA SERVES, NOT HEAD `[2026-09-07, the flex-point audit R3]`. Beat 1's
    # own exit condition is "a sha is deployed to QA and qa-build.json reports it"; deriving against HEAD
    # meant the commit that RECORDED lap 1's close re-fired the loop ("FIRED · beat 2 · candidate
    # b5ae109") while the file said cleared. HEAD is a candidate only once it is served.
    sha = a.sha
    note = None
    if not sha:
        try:
            spec = importlib.util.spec_from_file_location("jw", os.path.join(ROOT, "tools", "journey-walk.py"))
            jw = importlib.util.module_from_spec(spec); spec.loader.exec_module(jw)
            served = jw.served_sha("qa")
            head = subprocess.check_output(["git", "-C", ROOT, "rev-parse", "HEAD"], text=True).strip()
            if served:
                sha = served
                if not head.startswith(served[:7]):
                    note = "  (candidate = the build QA serves, %s; HEAD %s is not deployed — deploy to QA to make it the candidate)" % (served[:7], head[:7])
            else:
                note = "  (QA's served sha is unreadable — deriving against HEAD %s)" % head[:7]
        except Exception as e:
            note = "  (could not read QA's served sha: %s — deriving against HEAD)" % (str(e)[:60])
    st = derive(cleared=a.cleared, prior=prior, sha=sha)
    if a.pre_register:
        try:
            incoming = json.load(open(os.path.expanduser(a.pre_register), encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print("  ⛔ --pre-register: cannot read %s (%s)" % (a.pre_register, type(exc).__name__))
            return 1
        if not isinstance(incoming, list):
            print("  ⛔ --pre-register: the file must hold a JSON LIST of {id, question, ...}")
            return 1
        have = {q.get("id") for q in st["pre_registered"]}
        added, refused = [], []
        for q in incoming:
            qid = (q or {}).get("id")
            if not qid or not (q.get("question") or "").strip():
                refused.append("%r — every pre-registration needs an id AND a question" % qid)
                continue
            if qid in have:
                # ⛔ NEVER OVERWRITE. An existing entry may already carry a disposition and its
                # evidence; re-registering over it would erase the discharge and read as fresh.
                refused.append("%s — already present; refusing to overwrite (it may hold a disposition)" % qid)
                continue
            st["pre_registered"].append(dict(q, disposition=q.get("disposition") or "open",
                                             evidence=q.get("evidence")))
            have.add(qid); added.append(qid)
        for r in refused:
            print("  ⛔ %s" % r)
        print("  ✚ pre-registered: %s" % (", ".join(added) if added else "none"))
    print("release loop — %s · beat %d/%d (%s) · owner: %s · candidate %s · seats pass: %s"
          % (st["state"], st["beat"]["n"], st["beat"]["of"], st["beat"]["name"], st["beat"]["owner"],
             st["candidate_sha"], st["gate_1"]["seats_pass"]))
    if note: print(note)
    # ⭐ The loud half of J-c: a heading that did not parse means a lap silently vanished from the
    # count, so it prints at the top level rather than living only in the JSON nobody opens.
    for ln, txt in [(a["line"], a["text"]) for a in st.get("lap_heading_anomalies", [])]:
        print("  ⛔ CYCLE-LOG.md:%s — heading did not parse; THIS LAP IS MISSING FROM THE COUNT: %s" % (ln, txt[:90]))
    print("  laps closed in the chronicle: %s · last: lap %s (%s) %s"
          % (st.get("lap_count"), st["last_lap"].get("lap"), st["last_lap"].get("outcome"),
             ("cleared_sha " + st["last_lap"]["cleared_sha"]) if st["last_lap"].get("cleared_sha") else "(no cleared_sha)"))
    if a.write:
        # ⛔ A WRITE THAT CHANGES ONLY THE TIMESTAMP IS NOT A WRITE. Hooked to post-commit (R3), an
        # unconditional dump re-dirtied the tree after every commit and the seam gate never read clean.
        same = prior is not None and {k: v for k, v in prior.items() if k != "generated_at"} == {k: v for k, v in st.items() if k != "generated_at"}
        if same:
            print("  (state unchanged — not rewritten)")
        else:
            os.makedirs(os.path.dirname(STATE), exist_ok=True)
            # ⚠️ TRAILING NEWLINE, deliberately. Without it git reports "\\ No newline at end of
            # file" on every hooked rewrite, so the file reads as modified forever and the seam gate
            # never comes clean — the same symptom the timestamp guard above was written to cure,
            # arriving by a different route.
            with open(STATE, "w", encoding="utf-8") as fh:
                json.dump(st, fh, indent=1, ensure_ascii=False)
                fh.write("\n")
            print("  → %s" % os.path.relpath(STATE, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
