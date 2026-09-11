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
import argparse, importlib.util, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")

# ⭐ THE COVERAGE LINE `[paul-ruled 2026-09-07]` — the disposition of the `second-viewport`
# pre-registration, and the retro's finding #2 in its general form.
# ⛔ WHY THIS EXISTS. Lap 2's gate printed **4 of 4** while the intersection of "can test a placed
# household" and "had undegraded data" was EMPTY. A verdict is not coverage. What the battery DID NOT
# reach has to be on the page next to the pass, or the pass reads as a claim about the whole product.
# ⭐ Viewport is the first entry because it is the one we know is a gap and can state exactly: every
# synthetic walk this loop has ever run was 414×848. Paul found a defect at laptop width on 2026-09-06
# that the phone battery missed, and the harness cannot reproduce it — so the honest move is to DECLARE
# the gap every lap rather than build a flag nobody has a confirmed user for. If a laptop defect bites
# again, this line is where it will already have been admitted.
# ⛔ READ, NEVER TYPED. The number comes out of the instrument itself, so it cannot drift away from
# what the walks actually did; an unreadable constant prints UNREADABLE and never a remembered value.
VIEWPORT_RX = re.compile(r"viewport:\s*\{\s*width:\s*(\d+)\s*,\s*height:\s*(\d+)")


def walk_viewport():
    """(width, height) every synthetic walk ran at, read from `journey-view.py`. None if unreadable."""
    try:
        with open(os.path.join(ROOT, "tools", "journey-view.py"), encoding="utf-8") as fh:
            m = VIEWPORT_RX.search(fh.read())
    except OSError:
        return None
    return (int(m.group(1)), int(m.group(2))) if m else None
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
                "countable": (None, "no transcript"), "no-failed-actions": (None, "no transcript"),
                "walked-in-qa": (None, "no transcript")}
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

    # ⛔ FAIL CLOSED ON A TRANSCRIPT THAT DOES NOT SAY. An older run predating the field cannot prove
    # where it happened, and "cannot prove" is not "passed" — that equivalence is the defect this
    # whole lap has been removing from other instruments.
    _origin = t.get("origin")
    if _origin is None:
        out["walked-in-qa"] = (False, "transcript records no origin — cannot prove where this ran")
    else:
        out["walked-in-qa"] = (_origin == "qa", "origin=%s" % _origin)

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
    # ⛔ WHOSE 429 WAS IT `[paul-ruled 2026-09-07, option A]`. This clause was named "the origin did
    # not 429" and implemented as ANY 429 in the walk's output — matching the CONTAINER, not the
    # PAYLOAD. The 429s were Open-Meteo's free tier throttling the browser (4 direct call sites in
    # the viewer); our own limiter never fired, its KV counters reading 4 and 14 against a cap of 20.
    # The classifier is IMPORTED from `walk-integrity`, not re-derived — one definition of "ours".
    try:
        _wi = importlib.util.spec_from_file_location("wi", os.path.join(ROOT, "tools", "walk-integrity.py"))
        _m = importlib.util.module_from_spec(_wi); _wi.loader.exec_module(_m)
        _ours, _theirs, _unattr = _m.rate_limits(t, run_dir)
    except Exception as e:
        _ours, _theirs, _unattr = [], [], 0
        out["not-rate-limited"] = (None, "cannot classify 429s: %s" % e)
    if "not-rate-limited" not in out:
        if _ours:
            out["not-rate-limited"] = (False, "OUR origin returned 429: %s" % _ours[0][:80])
        elif _unattr:
            # ⚠️ 429s recorded with no URL — predates the capture that would say whose. UNCHECKABLE,
            # never a pass: a gate reading unjudgeable as passing is the failure this gate exists to
            # end. Bounded — every walk after 2026-09-07 records the URL.
            out["not-rate-limited"] = (None, "%d 429(s) with no URL recorded — whose is UNCHECKABLE" % _unattr)
        elif _m.capture_failures(t, run_dir) is None and "rateLimited" not in t:
            out["not-rate-limited"] = (None, "the transcript predates the field — UNCHECKABLE, not clean")
        else:
            out["not-rate-limited"] = (True, "no 429 from our origin")
    if _theirs:
        # ⚠️ NOT COUNTABLE-BLOCKING, NEVER SILENT. A third-party throttle means this walk saw
        # DEGRADED DATA — forecast and ERA5 history come straight from Open-Meteo in the browser.
        out["third-party-throttled"] = (False, "⚠️ %d third-party 429(s) — DEGRADED WEATHER DATA in "
                                               "this walk: %s" % (len(_theirs), _theirs[0][:80]))

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
    ("not-rate-limited", "OUR OWN origin did not 429  (a third party's is a caveat, not a refusal)"),
    # ⛔⛔ WHERE THE WALK HAPPENED. Owed since 2026-09-07 as D3 and grep-zero until now: gate ① is the
    # QA gate, and it could be passed by four walks taken at `lab`. Nothing in the gate read the
    # origin the walker actually visited — `at-sha` proves WHICH BUILD, `watched` proves HOW, and
    # nothing proved WHERE. `measured` 2026-09-08: every transcript already carries `origin` and
    # `originUrl`; the gate simply never looked. A clause that exists in the record and in no check
    # is the shape this repo names "a capability the loop cannot reach".
    ("walked-in-qa", "the walk happened at the QA origin  (gate ① is the QA gate)"),
]


# ⭐ H4 (lap 7, L7-P2 + L7-P3 as ONE step [Q6, paul-ruled 2026-09-10]) — TWO ARTIFACT CONVENTIONS so two
# clauses can be READ rather than printed UNCHECKABLE forever:
#   content: `.content/walks/<sha7>-walk-read.md` — the copy a walk met was read by the voice's owner
#            (content-steward), one section per seat; the clause checks that an artifact EXISTS for this
#            sha and NAMES every seat on disk. ⛔ It checks that a read was WRITTEN, never that it was right.
#   ux:      `.ux-reviews/sweeps/<sha7>-ux-sweep.md` — the two-pass sweep filed at this candidate.
# Absent → UNCHECKABLE with the PATH named, never a silent omission and never a pass.
CONTENT_DIR = os.path.join(ROOT, ".content", "walks")
UX_DIR = os.path.join(ROOT, ".ux-reviews", "sweeps")


def content_clause(sha, seat_names, content_dir=None):
    """→ (state, detail). True only when the artifact exists for this sha and names every seat."""
    d = content_dir or CONTENT_DIR
    path = os.path.join(d, "%s-walk-read.md" % sha[:7])
    if not os.path.exists(path):
        return (None, "UNCHECKABLE — no content read filed at %s" % os.path.relpath(path, ROOT))
    body = open(path, encoding="utf-8").read()
    if sha[:7] not in body:
        return (False, "the artifact at %s does not name this sha" % os.path.relpath(path, ROOT))
    missing = [s_ for s_ in seat_names if not re.search(r"(^|\W)%s(\W|$)" % re.escape(s_), body)]
    if missing:
        return (False, "the content read names no section for seat(s): %s" % ", ".join(missing))
    return (True, os.path.relpath(path, ROOT))


def ux_clause(sha, ux_dir=None):
    d = ux_dir or UX_DIR
    path = os.path.join(d, "%s-ux-sweep.md" % sha[:7])
    if not os.path.exists(path):
        return (None, "UNCHECKABLE — no two-pass sweep filed at %s" % os.path.relpath(path, ROOT))
    body = open(path, encoding="utf-8").read()
    if sha[:7] not in body:
        return (False, "the sweep at %s does not name this sha" % os.path.relpath(path, ROOT))
    return (True, os.path.relpath(path, ROOT))


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
        tp = v.get("third-party-throttled")
        if tp:
            print("        %s" % tp[1])
        st, detail = v.get("instrumented", (None, "not evaluated"))
        print("        %s instrumented (reported, counted from lap 2) — %s" % ("✅" if st is True else ("🔴" if st is False else "⬜"), detail))

    print("\n  seats passing every clause: %d of %d" % (len(passing_seats), len(ss)))
    # ⛔ COUNTED, NEVER GRADED — this line states what the battery did not reach. It refuses nothing
    # and it must never gain a pass/fail, or it becomes a second gate nobody ruled on.
    vp = walk_viewport()
    print("  📐 coverage — %s" % (
        ("viewport %d×%d ONLY — no seat has ever walked at another width, and the harness cannot "
         "produce one (hardcoded in journey-view.py, no flag). ⛔ A pass here says NOTHING about "
         "laptop width." % vp) if vp else
        "viewport UNREADABLE — journey-view.py's constant could not be parsed, so what these walks "
        "covered is UNKNOWN, not assumed."))
    # ⛔ COVERAGE, STATED: J2 is UNWALKABLE at every build since the open door `[measured 2026-09-11, lap 7
    # battery]` — an unfinished record cannot exist without an estate (the profile write 404s without one),
    # founding replaced granting, so the door reads J2's fixture as J0; no transcript at any build has ever
    # recorded a walked J2. A pass here says nothing about a resumed-unfinished person until Paul rules
    # the re-scope-or-retire (coordination's recommendation: re-scope as "returning, founded nothing").
    print("  📐 coverage — J2 (returning-unfinished) is UNWALKABLE at every build since the open door: an unfinished "
          "record cannot exist without an estate; founding replaced granting; no transcript at any build has ever "
          "recorded a walked J2. Not covered here — awaiting Paul's re-scope-or-retire ruling.")
    # H4 (lap 7) — the two per-sha clauses, each read from its artifact convention
    cst, cdet = content_clause(sha, ss)
    ust, udet = ux_clause(sha)
    mark = lambda st: "✅" if st is True else ("🔴" if st is False else "⬜")
    print("  %s content read for this build (L7-P3: every walk read by the voice's owner) — %s" % (mark(cst), cdet))
    print("  %s UX sweep for this build (L7-P2: the two-pass sweep at this candidate) — %s" % (mark(ust), udet))

    if len(passing_seats) == len(ss) and ss:
        if cst is True and ust is True:
            print("\n✅ every seat passes, the content read is filed and the sweep is filed — gate ① PASSED at %s." % sha[:7])
            return 0
        print("\n🟡 every seat passes — but %s, so this is NOT a bare pass." % (
              "the content clause is %s and the UX clause is %s" % (
                  "unfiled" if cst is None else ("red" if cst is False else "green"),
                  "unfiled" if ust is None else ("red" if ust is False else "green"))))
        print("   Gate ① exits beat 2 only when both artifacts are filed at this sha (or a human confirms in their place).")
        # ⛔ EXIT CODE AGREES WITH STDOUT. This returned 0 here while the text refused, so a machine
        # caller (pages-deploy) would have read a pass. practice-steward, 2026-09-06. `--seats-only`
        # is the machine question "did every seat pass every seat clause at this sha" and answers 0;
        # the bare command keeps answering the whole gate.
        return 0 if seats_only else 1
    print("\n🔴 GATE ① NOT PASSED at %s. The synthetic loop has not been exited." % sha[:7])
    print("   Paul's rule: the build stays in the synthetic loop UNTIL IT NO LONGER FAILS.")
    return 1


def selftest():
    print("release-gate --selftest — can every clause FAIL?\n")
    import tempfile
    ok = True
    # ⛔ THE FIXTURE MUST MATCH WHAT THE WRITER EMITS. `journey-walk` records `httpFailures` (and a
    # declared `rateLimited`) since 2026-09-07; a base without them reads UNCHECKABLE, which is
    # correct behaviour and made M0 fail. A fixture that drifts from the writer is how a green clause
    # ends up unable to fire — the defect this whole clause exists because of.
    # ⭐ `origin` joined this fixture with the walked-in-qa clause (2026-09-08). M0 went red the
    # moment the clause landed, because a "fully clean run" that cannot say WHERE it happened is not
    # clean any more — which is the clause proving itself against the selftest's own baseline.
    base = {"buildBefore": "a" * 40, "buildAfter": "a" * 40, "watched": True, "origin": "qa",
            "stops": [{"stop": "01", "status": "walked"}], "failedActions": [],
            "rateLimited": False, "httpFailures": []}

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

        # ⛔ M4b/M4c/M4d · WHERE THE WALK HAPPENED. Gate ① is the QA gate and until 2026-09-08 it
        # could be passed by four walks taken at `lab` — `at-sha` proves which build, `watched` proves
        # how, and nothing proved where. Every transcript already carried `origin`; nothing read it.
        # ⭐ M4d is the one that matters: a transcript that does not SAY must fail, because "cannot
        # prove" is not "passed" — the equivalence this lap has been removing everywhere else.
        v = mk(os.path.join(tmp, "atlab"), dict(base, origin="lab"))
        bit = v["walked-in-qa"][0] is False
        print("  %s M4b a walk at LAB fails 'walked-in-qa' (gate ① is the QA gate)" % ("✅" if bit else "🔴")); ok &= bit

        v = mk(os.path.join(tmp, "atqa"), dict(base, origin="qa"))
        bit = v["walked-in-qa"][0] is True
        print("  %s M4c a walk at QA passes it" % ("✅" if bit else "🔴")); ok &= bit

        _noorigin = dict(base); _noorigin.pop("origin", None)
        v = mk(os.path.join(tmp, "noorigin"), _noorigin)
        bit = v["walked-in-qa"][0] is False
        print("  %s M4d a transcript that does not SAY fails it — cannot-prove is not passed" % ("✅" if bit else "🔴")); ok &= bit

        # ⛔ M7a/M7b · THE RATE-LIMIT CLAUSE, in the shape the writer really emits: run-level
        # `rateLimited`, per-stop `walked`. The old walk-integrity fixture hand-wrote a per-stop
        # `"rate-limited"` status that `journey-walk.py:423` cannot produce, which is why an
        # equivalent guard was green and unable to fire for the life of the harness.
        v = mk(os.path.join(tmp, "ours429"), dict(base, httpFailures=[
            {"status": 429, "url": "https://fernwood-qa.paul-kirschenbauer.workers.dev/api/feedback"}]))
        bit = v["not-rate-limited"][0] is False
        print("  %s M7a OUR OWN origin 429 fails the gate" % ("✅" if bit else "🔴")); ok &= bit

        v = mk(os.path.join(tmp, "theirs429"), dict(base, httpFailures=[
            {"status": 429, "url": "https://api.open-meteo.com/v1/forecast?lat=1"}]))
        bit = (v["not-rate-limited"][0] is True) and ("third-party-throttled" in v)
        print("  %s M7b a THIRD-PARTY 429 does NOT fail the gate and IS reported" % ("✅" if bit else "🔴")); ok &= bit

        v = mk(os.path.join(tmp, "no429"), dict(base, httpFailures=[]))
        bit = v["not-rate-limited"][0] is True and "third-party-throttled" not in v
        print("  %s M7b2 a walk with no 429 passes and raises no caveat" % ("✅" if bit else "🔴")); ok &= bit

        _legacy = dict(base, rateLimited=True); _legacy.pop("httpFailures")   # exactly a pre-2026-09-07 record
        v = mk(os.path.join(tmp, "untagged"), _legacy)
        bit = v["not-rate-limited"][0] is None
        print("  %s M7b3 a 429 with NO URL is UNCHECKABLE, never a pass and never a guess" % ("✅" if bit else "🔴")); ok &= bit

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

        # H4 (lap 7) — the two artifact clauses can FAIL, and absence is UNCHECKABLE, never a pass
        cdir = os.path.join(tmp, "content"); udir = os.path.join(tmp, "ux"); os.makedirs(cdir); os.makedirs(udir)
        st, _ = content_clause("a" * 40, ["mom", "owner"], cdir)
        bit = st is None
        print("  %s M8a no content read filed → UNCHECKABLE, never a pass" % ("✅" if bit else "🔴")); ok &= bit
        open(os.path.join(cdir, "aaaaaaa-walk-read.md"), "w").write("# read at bbbbbbb\n## mom\n## owner\n")
        st, _ = content_clause("a" * 40, ["mom", "owner"], cdir)
        bit = st is False
        print("  %s M8b a read filed under this sha that names ANOTHER sha → red" % ("✅" if bit else "🔴")); ok &= bit
        open(os.path.join(cdir, "aaaaaaa-walk-read.md"), "w").write("# read at aaaaaaa\n## mom\n")
        st, det = content_clause("a" * 40, ["mom", "owner"], cdir)
        bit = st is False and "owner" in det
        print("  %s M8c a read that names only SOME seats → red, naming the missing seat" % ("✅" if bit else "🔴")); ok &= bit
        open(os.path.join(cdir, "aaaaaaa-walk-read.md"), "w").write("# read at aaaaaaa\n## mom\n## owner\n")
        st, _ = content_clause("a" * 40, ["mom", "owner"], cdir)
        bit = st is True
        print("  %s M8d a read at this sha naming every seat → green" % ("✅" if bit else "🔴")); ok &= bit
        st, _ = ux_clause("a" * 40, udir)
        bit = st is None
        print("  %s M9a no sweep filed → UNCHECKABLE, never a pass" % ("✅" if bit else "🔴")); ok &= bit
        open(os.path.join(udir, "aaaaaaa-ux-sweep.md"), "w").write("two-pass sweep at aaaaaaa\n")
        st, _ = ux_clause("a" * 40, udir)
        bit = st is True
        print("  %s M9b a sweep filed at this sha → green" % ("✅" if bit else "🔴")); ok &= bit

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
