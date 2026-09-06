#!/usr/bin/env python3
"""release-gate.py — has GATE ① been passed for a candidate build?

    python3 tools/release-gate.py                 # gate the current HEAD
    python3 tools/release-gate.py --sha 2fc2b71   # gate a specific build
    python3 tools/release-gate.py --selftest      # prove every clause can FAIL

⭐ WHY THIS EXISTS `[paul-stated 2026-09-06]`. Paul defined the release loop:

    "we have a build, we run it through our synthetic testers UNTIL IT NO LONGER FAILS, and then I
     run it. If I spot a failure it goes back through that loop of synthetics until it no longer
     fails, then back to me — and that is a loop in and of itself. And then once I clear it, it is
     truly released."

and he defined the exit condition in the same breath: "all the synthetics have gone through it IN
CHROME, DOCUMENTED THEIR EXPERIENCES, and it's gated on my review and walk-through."

⛔ EVERY CLAUSE BELOW WAS ALREADY COMPUTED AND READ BY NO GATE. `journey-walk` has written `watched`
since the day `--watch` was added; `walk-integrity` has refused unread runs for longer than that.
Nothing asked them the question, so on 2026-09-06 a single headless QA battery was reported as
satisfying a gate that three of Paul's stated expectations had not met. The machinery was not
missing. The QUESTION was missing. This file is the question.

⚠️ IT IS PER-SHA, BECAUSE EVIDENCE EXPIRES WHEN THE BUILD MOVES `[paul-ruled 2026-09-06]`. A pass at
an older build is not a pass at this one — the rule caught the session that proposed it, which
reported four seats as having walked a sha they had never walked.

⛔ AND IT NEVER PRINTS A BARE PASS WHILE A CLAUSE IS UNCHECKABLE. A gate that cannot see one of its
own clauses and says PASS is worse than no gate.
"""
import argparse, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")
UNWRITTEN = "WALK-REPORT-UNWRITTEN"


def head_sha():
    r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def seats():
    """⭐ DERIVED from what exists on disk, never a typed roster — the control this project has now
    been bitten by four times (check-storage-keys 3x, household-export's --env list)."""
    if not os.path.isdir(WALKS):
        return []
    return sorted(d for d in os.listdir(WALKS) if os.path.isdir(os.path.join(WALKS, d)))


def runs_for(seat):
    d = os.path.join(WALKS, seat)
    return sorted(r for r in os.listdir(d) if os.path.isdir(os.path.join(d, r)))


def judge(run_dir, sha):
    """→ dict of clause -> (state, detail). state is True / False / None(=uncheckable)."""
    out = {}
    tpath = os.path.join(run_dir, "transcript.json")
    if not os.path.exists(tpath):
        return {"at-sha": (False, "no transcript"), "watched": (None, "no transcript"),
                "countable": (None, "no transcript"), "no-failed-actions": (None, "no transcript")}
    try:
        t = json.load(open(tpath, encoding="utf-8"))
    except Exception as e:
        return {"at-sha": (False, "unreadable transcript: %s" % e)}

    before, after = (t.get("buildBefore") or ""), (t.get("buildAfter") or "")
    at = bool(sha) and before.startswith(sha) and after.startswith(sha)
    # ⛔ A build that MOVED DURING the walk is not a walk of either sha.
    if before != after:
        out["at-sha"] = (False, "build moved mid-walk: %s → %s" % (before[:7], after[:7]))
    else:
        out["at-sha"] = (at, "%s" % (before[:7] or "unknown"))

    out["watched"] = (bool(t.get("watched")), "watched=%s" % t.get("watched"))

    rpath = os.path.join(run_dir, "REPORT.md")
    if not os.path.exists(rpath):
        out["countable"] = (False, "no REPORT.md")
    else:
        body = open(rpath, encoding="utf-8", errors="replace").read()
        out["countable"] = (UNWRITTEN not in body, "unread" if UNWRITTEN in body else "read")

    stops = t.get("stops") or []
    bad = [s for s in stops if s.get("status") not in ("walked", "skipped", "n/a")]
    failed = t.get("failedActions")
    if failed is None and not stops:
        out["no-failed-actions"] = (None, "no stops recorded")
    else:
        n = len(bad) + (len(failed) if isinstance(failed, list) else 0)
        out["no-failed-actions"] = (n == 0, "%d problem stop/action(s)" % n)

    if t.get("contaminated"):
        out["uncontaminated"] = (False, "run marked contaminated")
    return out


CLAUSES = [
    ("at-sha", "a run exists AT this build"),
    ("watched", "driven in visible Chrome  (\"gone through it in Chrome\")"),
    ("countable", "the seat READ its own walk  (\"documented their experiences\")"),
    ("no-failed-actions", "zero failed actions  (\"until it no longer fails\")"),
]


def report(sha):
    print("release gate ① — build %s\n" % (sha[:7] if sha else "UNKNOWN"))
    if not sha:
        print("🔴 UNCHECKABLE: no candidate sha. Refusing to gate nothing.")
        return 2
    ss = seats()
    if not ss:
        print("🔴 UNCHECKABLE: no seats found on disk — refusing to report on an empty roster.")
        return 2

    passing_seats, rows = [], []
    for seat in ss:
        best = None
        for run in runs_for(seat):
            v = judge(os.path.join(WALKS, seat, run), sha)
            if v.get("at-sha", (False, ""))[0]:
                # among runs at this sha, keep the best (most clauses true)
                score = sum(1 for k, _ in CLAUSES if v.get(k, (None,))[0] is True)
                if best is None or score > best[0]:
                    best = (score, run, v)
        rows.append((seat, best))
        if best and all(best[2].get(k, (None,))[0] is True for k, _ in CLAUSES):
            passing_seats.append(seat)

    for seat, best in rows:
        if not best:
            print("  🔴 %-11s no run at this build" % seat)
            continue
        _, run, v = best
        marks = []
        for key, _label in CLAUSES:
            st, detail = v.get(key, (None, "not evaluated"))
            marks.append("%s %s" % ("✅" if st is True else ("🔴" if st is False else "⬜"), key))
        print("  %-11s %s" % (seat, run))
        print("     " + "  ".join(marks))
        for key, label in CLAUSES:
            st, detail = v.get(key, (None, "not evaluated"))
            if st is not True:
                print("        %s %s — %s" % ("🔴" if st is False else "⬜", label, detail))

    print("\n  seats passing every clause: %d of %d" % (len(passing_seats), len(ss)))
    # ⬜ The UX sweep has no artifact convention yet. DECLARED, never silently omitted.
    print("  ⬜ UX sweep for this build — UNCHECKABLE: no artifact convention exists yet.")

    if len(passing_seats) == len(ss) and ss:
        print("\n🟡 every seat passes — but the UX clause is UNCHECKABLE, so this is NOT a bare pass.")
        print("   Gate ① exits beat 2 only when a human confirms the UX clause too.")
        return 0
    print("\n🔴 GATE ① NOT PASSED at %s. The synthetic loop has not been exited." % sha[:7])
    print("   Paul's rule: the build stays in the synthetic loop UNTIL IT NO LONGER FAILS.")
    return 1


def selftest():
    print("release-gate --selftest — can every clause FAIL?\n")
    import tempfile
    ok = True
    base = {"buildBefore": "a" * 40, "buildAfter": "a" * 40, "watched": True,
            "stops": [{"stop": "01", "status": "walked"}], "failedActions": []}

    def mk(d, tr, report_body="all good"):
        os.makedirs(d, exist_ok=True)
        json.dump(tr, open(os.path.join(d, "transcript.json"), "w"))
        open(os.path.join(d, "REPORT.md"), "w").write(report_body)
        return judge(d, "a" * 7)

    with tempfile.TemporaryDirectory() as tmp:
        v = mk(os.path.join(tmp, "good"), base)
        bit = all(v[k][0] is True for k, _ in CLAUSES)
        print("  %s M0 a fully clean run passes every clause" % ("✅" if bit else "🔴")); ok &= bit

        v = mk(os.path.join(tmp, "unwatched"), dict(base, watched=False))
        print("  %s M1 watched=False → 'watched' goes red" % ("✅" if v["watched"][0] is False else "🔴"))
        ok &= v["watched"][0] is False

        v = mk(os.path.join(tmp, "unread"), base, "…" + UNWRITTEN + "…")
        print("  %s M2 an unread REPORT.md → 'countable' goes red" % ("✅" if v["countable"][0] is False else "🔴"))
        ok &= v["countable"][0] is False

        v = mk(os.path.join(tmp, "failed"), dict(base, stops=[{"stop": "01", "status": "could-not"}]))
        print("  %s M3 a non-walked stop → 'no-failed-actions' goes red" % ("✅" if v["no-failed-actions"][0] is False else "🔴"))
        ok &= v["no-failed-actions"][0] is False

        v = mk(os.path.join(tmp, "othersha"), dict(base, buildBefore="b" * 40, buildAfter="b" * 40))
        print("  %s M4 a run at ANOTHER build → 'at-sha' goes red (evidence expires)" % ("✅" if v["at-sha"][0] is False else "🔴"))
        ok &= v["at-sha"][0] is False

        v = mk(os.path.join(tmp, "moved"), dict(base, buildAfter="c" * 40))
        bit = v["at-sha"][0] is False and "moved mid-walk" in v["at-sha"][1]
        print("  %s M5 the build MOVED mid-walk → not a walk of either sha" % ("✅" if bit else "🔴")); ok &= bit

        v = judge(os.path.join(tmp, "nothing"), "a" * 7)
        bit = v["watched"][0] is None
        print("  %s M6 a missing transcript reads UNCHECKABLE, never pass" % ("✅" if bit else "🔴")); ok &= bit

    print("\n%s selftest" % ("✅" if ok else "🔴"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sha", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return report((a.sha or head_sha())[:40])


if __name__ == "__main__":
    sys.exit(main())
