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


def is_seat(path):
    """A seat is a directory holding at least one RUN — a subfolder with a transcript.json.
    ⛔ Measured 2026-09-06: `wide-eyed-2026-09-05-first/` holds one retrospective REPORT.md and no
    run. Counted as a seat, it could never pass, so the gate could never go green and nothing said
    why. A retained record is evidence (the two-classes ruling keeps it); it is not a seat."""
    if not os.path.isdir(path):
        return False
    return any(os.path.exists(os.path.join(path, r, "transcript.json"))
               for r in os.listdir(path) if os.path.isdir(os.path.join(path, r)))


def seats():
    """⭐ DERIVED from what exists on disk, never a typed roster — the control this project has now
    been bitten by four times (check-storage-keys 3x, household-export's --env list)."""
    if not os.path.isdir(WALKS):
        return []
    return sorted(d for d in os.listdir(WALKS) if is_seat(os.path.join(WALKS, d)))


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
        # ⛔ THE MARKER MUST BE DISCUSSABLE IN THE DOCUMENT IT GOVERNS — a bare substring match
        # scored a report that QUOTES the marker while explaining it as unwritten (found
        # 2026-09-07). Occurrences inside `backticks` or on a `>` blockquote line are a seat TALKING
        # ABOUT the marker, not the placeholder. Same fix as `walk-integrity.py`.
        import re as _re
        _clean = _re.sub(r"`[^`]*`", "", body)
        _clean = "\n".join(l for l in _clean.splitlines() if not l.lstrip().startswith(">"))
        out["countable"] = (UNWRITTEN not in _clean, "unread" if UNWRITTEN in _clean else "read")

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

    # ⛔ THE GATE READ NO RATE-LIMIT SIGNAL AT ALL, and this is the instrument that certifies a build
    # for production. Measured 2026-09-07 at `34cb103`: 3 of 4 seats carried `rateLimited: True`
    # while every stop read `walked`, so all four clauses above were satisfiable and the gate would
    # have passed three contaminated walks. `walk-integrity.py` owns the refusal; this reads the same
    # field rather than minting a second opinion about it.
    # ⚠️ RUN-LEVEL, because that is the level the record supports: `_view.json`'s console carries the
    # 429 lines with no timestamps and no interleaving with the CHECKPOINT lines, so which stop was
    # hit is not derivable.
    out["not-rate-limited"] = (not t.get("rateLimited"),
                               "the origin returned 429 during this walk" if t.get("rateLimited")
                               else "no 429 recorded")

    # ⭐ `instrumented` `[paul-stated 2026-09-06]`: "for everything that we do and see and observe that
    # we're capturing on the user side, there needs to also be as much as possible instrumentation on
    # our side, on the capture side." Read from capture.json, written by journey-walk at walk time.
    # ⚠️ REPORTED THIS LAP, COUNTED FROM LAP 2 (pre-registered in CYCLE-LOG.md): the grant-carried flush
    # first ships at the lap-1 candidate, so a run before it reads ⬜, never a false red or a false green.
    cpath = os.path.join(run_dir, "capture.json")
    if os.path.exists(cpath):
        try:
            c = json.load(open(cpath, encoding="utf-8"))
            n = int(((c.get("app") or {}).get("events")) or 0)
            out["instrumented"] = (n > 0, "%d app event(s) landed for this run" % n)
        except Exception as e:
            out["instrumented"] = (None, "unreadable capture.json: %s" % e)
    else:
        out["instrumented"] = (None, "no capture.json — walked before the capture read existed")
    return out


CLAUSES = [
    ("at-sha", "a run exists AT this build"),
    ("watched", "driven in visible Chrome  (\"gone through it in Chrome\")"),
    ("countable", "the seat READ its own walk  (\"documented their experiences\")"),
    ("no-failed-actions", "zero failed actions  (\"until it no longer fails\")"),
    ("not-rate-limited", "the origin did not 429 during the walk  (a throttled walk is not a walk)"),
]


def report(sha, seats_only=False):
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
        st, detail = v.get("instrumented", (None, "not evaluated"))
        print("        %s instrumented (reported, counted from lap 2) — %s" % ("✅" if st is True else ("🔴" if st is False else "⬜"), detail))

    print("\n  seats passing every clause: %d of %d" % (len(passing_seats), len(ss)))
    # ⬜ The UX sweep has no artifact convention yet. DECLARED, never silently omitted.
    print("  ⬜ UX sweep for this build — UNCHECKABLE: no artifact convention exists yet.")

    if len(passing_seats) == len(ss) and ss:
        print("\n🟡 every seat passes — but the UX clause is UNCHECKABLE, so this is NOT a bare pass.")
        print("   Gate ① exits beat 2 only when a human confirms the UX clause too.")
        # ⛔ EXIT CODE AGREES WITH STDOUT. This returned 0 here while the text refused, so a machine
        # caller (pages-deploy) would have read a pass. practice-steward, 2026-09-06. `--seats-only`
        # is the machine question "did every seat pass every seat clause at this sha" and answers 0;
        # the bare command keeps answering the whole gate, which is not yet passable by a machine.
        return 0 if seats_only else 1
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

        # ⛔ M7a/M7b · THE RATE-LIMIT CLAUSE, in the shape the writer really emits: run-level
        # `rateLimited`, per-stop `walked`. The old walk-integrity fixture hand-wrote a per-stop
        # `"rate-limited"` status that `journey-walk.py:423` cannot produce, which is why an
        # equivalent guard was green and unable to fire for the life of the harness.
        v = mk(os.path.join(tmp, "ratelimited"), dict(base, rateLimited=True))
        bit = v["not-rate-limited"][0] is False
        print("  %s M7a a run the origin 429'd fails the gate (run-level, as recorded)" % ("✅" if bit else "🔴")); ok &= bit
        v = mk(os.path.join(tmp, "notlimited"), dict(base, rateLimited=False))
        bit = v["not-rate-limited"][0] is True
        print("  %s M7b a run with no 429 passes that clause" % ("✅" if bit else "🔴")); ok &= bit

        # M7c · the marker must be discussable in the report it governs
        v = mk(os.path.join(tmp, "quotesmarker"), base,
               "I checked my report no longer says `" + UNWRITTEN + "`.")
        bit = v["countable"][0] is True
        print("  %s M7c a report QUOTING the unwritten-marker is not scored unread" % ("✅" if bit else "🔴")); ok &= bit

        v = mk(os.path.join(tmp, "moved"), dict(base, buildAfter="c" * 40))
        bit = v["at-sha"][0] is False and "moved mid-walk" in v["at-sha"][1]
        print("  %s M5 the build MOVED mid-walk → not a walk of either sha" % ("✅" if bit else "🔴")); ok &= bit

        v = judge(os.path.join(tmp, "nothing"), "a" * 7)
        bit = v["watched"][0] is None
        print("  %s M6 a missing transcript reads UNCHECKABLE, never pass" % ("✅" if bit else "🔴")); ok &= bit

        # M7 — a folder with a REPORT.md and no run is a retained record, not a seat.
        os.makedirs(os.path.join(tmp, "seatlike", "2026-01-01T000000"), exist_ok=True)
        open(os.path.join(tmp, "seatlike", "2026-01-01T000000", "transcript.json"), "w").write("{}")
        os.makedirs(os.path.join(tmp, "record-only"), exist_ok=True)
        open(os.path.join(tmp, "record-only", "REPORT.md"), "w").write("second-hand")
        bit = is_seat(os.path.join(tmp, "seatlike")) and not is_seat(os.path.join(tmp, "record-only"))
        print("  %s M7 a record-only folder is NOT a seat; a folder with a run is" % ("✅" if bit else "🔴")); ok &= bit

    print("\n%s selftest" % ("✅" if ok else "🔴"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sha", default=None)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--seats-only", action="store_true",
                    help="exit 0 when every seat passes every seat clause at the sha (the UX clause still prints as uncheckable)")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return report((a.sha or head_sha())[:40], seats_only=a.seats_only)


if __name__ == "__main__":
    sys.exit(main())
