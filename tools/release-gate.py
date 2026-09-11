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


# ═══ T1 · THE UNIT BECOMES THE CELL — `(journey, lens)` ═══════════════════════════════════════════
#
# ⛔ THE DEFECT THIS REPLACES, measured and on the record (cycle/release/lap-8-T0-before-image.md):
# `seats()` listed DIRECTORY NAMES, and `report()` kept one best run per seat. At `87c7aae` that
# printed five rows — every one `no-failed-actions` ✅ — while SEVENTEEN other runs at that sha were
# not shown at all, holding 12 failed actions across 7 runs. The verdict was a function of which
# journey the battery happened to walk first. A run folder's name is the STORAGE LAYOUT; it is not a
# decision anyone made.
#
# ⭐ WHICH FIELD DEFINES A CELL, AND WHY — the choice this function makes, stated because the two
# candidates DISAGREE on 68% of the recorded corpus and the disagreement is systematic, not noise.
# `measured` at lap 8's open: 283 transcripts · 59 carry BOTH `journey` and `journeyEntered` · 40 of
# those 59 DISAGREE — walked=J0/door=J5 ×23, walked=J8/door=J3 ×17.
#
#   `journey`        = what the harness SET OUT TO WALK   ← ⭐ this one defines the cell
#   `journeyEntered` = what the DOOR SAID the record was on arrival
#
# It is not a tie-break between two near-equal readings. It is a choice between the test and the
# fixture's state, and three things settle it:
#   1. A CELL IS A UNIT OF TEST COVERAGE. A declared cell list (T3) says "we will walk J8 under the
#      successor lens." What is committed to is the WALK. The door's answer is an INPUT to that walk.
#   2. THE ENTRY STATE ALREADY HAS A HOME, and it is not this one — T10 gives every journey a
#      declared `arrivalState` and T14 records the state the run actually ran in. Keying the cell on
#      the door would put entry state in two places and make neither authoritative.
#   3. ⛔ KEYING ON THE DOOR COLLAPSES DISTINCT TESTS. At `87c7aae` all 17 J8 walks entered J3, so
#      grouping on `journeyEntered` makes lifecycle and returning indistinguishable and the matrix
#      could never show that J8 was walked at all. That is this row's own defect one level up: a cell
#      that hides what was actually tested.
# ⭐ And the door's answer is NOT discarded — it is recorded beside the cell and a disagreement is
# PRINTED (`report()`), because a walk whose arrival contradicts its own premise is a finding, not a
# grouping detail to be resolved silently.

J1_LEGACY = "J1-legacy"
JRET_LEGACY = "J-returning-legacy"


def journey_of(t):
    """→ (journey, source) where source is `recorded` | `door-measured` | `backfilled`.

    ⛔ NEVER RETURNS A BARE `J2` OR `J4` BY INFERENCE. The 09-10 plan's backfill rule keyed the
    returning population on a token suffixed `-neverminted` — a property of a CREDENTIAL THE
    TRANSCRIPT NEVER RECORDED. `measured`: of 224 transcripts with no `journey`, 220 carry no
    `arrival`, no `entryState` and no token at all, and the non-fresh population spans the re-point
    of `journey_returning` from J2 to J3 at `7496196`. So J2, J3 and J4 are INDISTINGUISHABLE on this
    corpus and a rule that picked one would mint exactly the fiction the CREDENTIAL ruling exposed.
    The honest bucket is `J-returning-legacy` and it is never counted toward a declared cell.
    """
    j = t.get("journey")
    if j:
        return j, "recorded"
    for k in ("journeyEntered", "arrival", "entryState"):
        v = t.get(k)
        if isinstance(v, str) and v:
            return v, "door-measured"          # the door's own measured answer, taken exactly
    return (J1_LEGACY if t.get("fresh") is True else JRET_LEGACY), "backfilled"


def is_legacy(journey):
    """A backfilled cell can satisfy NO declared cell — it is evidence, never coverage (T3/M10c)."""
    return journey in (J1_LEGACY, JRET_LEGACY)


def unit_of(run_dir):
    """→ (journey, lens). `lens` is the transcript's own when present, else the DIRECTORY NAME —
    which is what it has always been, so nothing that predates the split loses its identity."""
    seat = os.path.basename(os.path.dirname(run_dir))
    tpath = os.path.join(run_dir, "transcript.json")
    if not os.path.exists(tpath):
        return None
    try:
        t = json.load(open(tpath, encoding="utf-8"))
    except Exception:
        return None
    j, _src = journey_of(t)
    return (j, t.get("lens") or seat)


def units(sha):
    """⭐ DERIVED from the runs that exist AT THIS SHA, never a typed roster — `seats()`'s own
    discipline, carried over deliberately. T3 unions this with the DECLARED cell list so a declared
    cell with no run prints UNWALKED instead of vanishing."""
    out = set()
    for seat in seats():
        for run in runs_for(seat):
            d = os.path.join(WALKS, seat, run)
            u = unit_of(d)
            if u and judge(d, sha).get("at-sha", (False,))[0]:
                out.add(u)
    return sorted(out)


# ═══ T2 · `instrumented` RE-KEYED TO THE JOURNEY ══════════════════════════════════════════════════
#
# ⛔ THE DEFECT: `instrumented` passed on `n > 0` for every run alike. `strict`'s J0 is the REFUSAL
# walk, and a refused founder never reaches the app — so its `instrumented` was 🔴 FOREVER BY
# CONSTRUCTION. A permanent red that is CORRECT BEHAVIOUR and a real instrumentation failure printed
# identically, which is the same `cannot-prove == failed` equivalence this gate has spent the whole
# lap removing from itself.
# ⚠️ `instrumented` STAYS OUT OF `CLAUSES` — advisory, not gating. Promoting it is a change to the
# release condition and is not in the eight rulings. Re-keying what it SAYS is in lane; changing what
# it BLOCKS is not.

def expects_app_events(journey):
    """→ True | False | None. Read from the journey's own declaration in `journey-walk.JOURNEYS`.

    ⛔ NONE UNTIL T10 LANDS, AND THAT IS DELIBERATE. T10 is the step that adds `expectsAppEvents` to
    every `JOURNEYS` entry; this step lands before it. Until then a journey declares no profile and
    the clause reads ⬜ UNCHECKABLE **with the reason named** — which already removes the false red,
    because a permanent 🔴 and a real failure no longer print the same. It is never guessed: a
    profile inferred from a journey id would be exactly the typed roster `units()` refuses to be.
    """
    if not journey:
        return None
    try:
        spec = importlib.util.spec_from_file_location("jw", os.path.join(ROOT, "tools", "journey-walk.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        entry = (getattr(m, "JOURNEYS", {}) or {}).get(journey)
    except Exception:
        return None
    if not isinstance(entry, dict) or "expectsAppEvents" not in entry:
        return None
    return bool(entry["expectsAppEvents"])


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
        # ⛔ RAW COUNT, so the supersession line does NOT re-derive it or parse it back out of the
        # detail string. One definition of "how many problems", used by both readers.
        out["_problems"] = (n, "raw count — not a clause, never printed as one")

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
    # ⭐ T2 — re-keyed to the JOURNEY's own declared profile. See `expects_app_events()` above for why
    # a missing profile reads UNCHECKABLE rather than being guessed.
    cpath = os.path.join(run_dir, "capture.json")
    _journey, _jsrc = journey_of(t)
    _expects = expects_app_events(_journey)
    if os.path.exists(cpath):
        try:
            c = json.load(open(cpath, encoding="utf-8"))
            n = int(((c.get("app") or {}).get("events")) or 0)
            if _expects is True:
                out["instrumented"] = (n > 0, "%d app event(s) landed — %s expects app events" % (n, _journey))
            elif _expects is False:
                # ⛔ THE REFUSAL CASE. A journey that declares it reaches no app is CORRECT with zero
                # events, and must stop printing as a failure.
                out["instrumented"] = (n == 0, "%d app event(s) — %s expects NONE (a refusal walk "
                                               "never reaches the app)" % (n, _journey))
            else:
                out["instrumented"] = (None, "%d app event(s) landed, but %s declares no "
                                             "expectsAppEvents profile (T10 not yet landed) — "
                                             "UNCHECKABLE, not a failure" % (n, _journey))
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


# ═══ T3 · THE DECLARED CELL LIST, THE MATRIX, AND UNWALKED-BY-NAME ════════════════════════════════
#
# ⛔ ABSENCE INDISTINGUISHABLE FROM A PASS is the defect this step removes. Until now a cell nobody
# walked simply did not appear, and a reader could not tell "we walked it and it was fine" from "no
# one has ever walked it." ⭐ EMPTY CELLS ARE THE COVERAGE CLAIM, NOT DECORATION.
#
# ⛔⛔ NO SCHEDULER, NO SELECTION ENGINE, NO BUDGET — the audit's boundary, verbatim and binding:
# the classifier may answer "which journeys can REACH what changed", a derivable fact about routes.
# It may NEVER answer "which journeys are WORTH running" — that is a value judgement and it is
# Paul's, at beat 6, in the declared cell list. ⭐ THIS STEP PRINTS; IT NEVER PICKS.
# ITS OWN FALSIFIER: the moment this code needs a weight, a score, a budget or a priority to produce
# its answer, it has crossed the line and it stops.
#
# ⛔ THIS STEP DOES NOT FILE A CELL LIST, AND THAT IS DELIBERATE. `declaredBy: paul` is a record of
# HIS act at beat 6. A build window writing that field would be minting a declaration nobody made —
# the same class as inferring a J2 from a token the transcript never held. With no list filed the
# gate reads UNCHECKABLE WITH THE PATH NAMED (M12c), which is the true state of lap 8 today.
CELLS_DIR = os.path.join(ROOT, "cycle", "release", "cells")


def _journey_library():
    """→ (JOURNEY_IDS, JOURNEYS, NAMED_UNBUILT). Imported, never re-typed —
    `release-state.py:171` already reaches journey-walk this way."""
    try:
        spec = importlib.util.spec_from_file_location("jw", os.path.join(ROOT, "tools", "journey-walk.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        return (list(getattr(m, "JOURNEY_IDS", []) or []),
                dict(getattr(m, "JOURNEYS", {}) or {}),
                dict(getattr(m, "NAMED_UNBUILT", {}) or {}))
    except Exception:
        return [], {}, {}


def read_cells(cells_dir=None):
    """→ (spec, problem). The lap is the HIGHEST-numbered `lap-<N>.json` present — derived from what
    exists, never a number typed here. `spec` is None whenever the list cannot be honoured, and
    `problem` always says why; ⛔ neither is ever a silent pass."""
    d = cells_dir or CELLS_DIR
    if not os.path.isdir(d):
        return None, "no cell list filed — expected %s/lap-<N>.json" % os.path.relpath(d, ROOT)
    files = sorted(f for f in os.listdir(d) if re.fullmatch(r"lap-\d+\.json", f))
    if not files:
        return None, "no cell list filed — expected %s/lap-<N>.json" % os.path.relpath(d, ROOT)
    newest = max(files, key=lambda f: int(re.findall(r"\d+", f)[0]))
    path = os.path.join(d, newest)
    try:
        spec = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        return None, "%s is unreadable: %s" % (newest, e)
    cells = spec.get("cells")
    if not isinstance(cells, list) or not cells:
        return None, "%s declares no cells" % newest
    # ⛔ M12b — A CELL LIST IS NOT A PLACE TO INVENT JOURNEYS. An id the library does not know is
    # REFUSED BY NAME, because a declaration the harness cannot walk is a coverage claim nobody
    # can honour, and it would print UNWALKED forever while looking like a fixture problem.
    ids, _J, named = _journey_library()
    known = set(ids) | set(named)
    if known:
        for c in cells:
            j = (c or {}).get("journey")
            if j not in known:
                return None, ("%s declares journey %r, which is absent from journey-walk's "
                              "JOURNEY_IDS and NAMED_UNBUILT — refusing" % (newest, j))
    spec["_file"] = newest
    return spec, None


def cell_last_walked(sha_any=True):
    """→ {(journey, lens): (newest mtime, source)} across ALL shas. A git-free read of run directory
    mtimes — used only to say WHICH CELL HAS GONE LONGEST UNWALKED. ⛔ It ranks by age and by
    nothing else; it is not a scheduler and it must never gain a second sort key.

    ⛔⛔ `source` IS LOAD-BEARING AND WAS NOT HERE ON THE FIRST DRAFT. `journey_of()` falls back to
    the DOOR's answer for a transcript that declared no journey, so four runs land in cells J1/J2/J3
    purely because the door read them that way. Printing those as *"last walked"* put a line saying
    `(J2, handover) last walked 2026-09-10` DIRECTLY ABOVE the standing paragraph that says no
    transcript at any build has ever recorded a walked J2 — two claims on one screen, one of them
    false, and the false one was this function's. A door reading is evidence about the RECORD's
    state at arrival; it is not a walk, and the two may never render the same."""
    out = {}
    for seat in seats():
        for run in runs_for(seat):
            d = os.path.join(WALKS, seat, run)
            u = unit_of(d)
            if not u or is_legacy(u[0]):
                continue
            try:
                t = json.load(open(os.path.join(d, "transcript.json"), encoding="utf-8"))
                mt = os.path.getmtime(os.path.join(d, "transcript.json"))
            except Exception:
                continue
            _j, src = journey_of(t)
            if u not in out or mt > out[u][0]:
                out[u] = (mt, src)
    return out


# ═══ T3b · THE LENS'S READ TIER — DECLARED, RECORDED, AND CHECKED ═════════════════════════════════
#
# MODEL-POLICY §3(B). Before this, Fernwood's release-evidence tier was set by `~/.claude/settings.json`
# — outside the repo, changed for unrelated reasons, read by no Fernwood check. The tier is now
# DECLARED in `cycle/release/lenses.json` [paul-ruled, P7: Opus 5] and the gate refuses to COUNT a
# read whose recorded tier is absent or does not match.
#
# ⚠️⚠️ A DETECTOR, NOT A PREVENTER — in those words, because the policy requires them and because an
# OVERSTATED BOUNDARY IS WORSE THAN AN UNSTATED ONE. Nothing here can force a driving session to
# spawn a lens at the declared tier; a spawn takes its model from an agent file or inherits the
# session's. This refuses to COUNT a mismatched read. Weaker than a hook, stronger than a sentence
# in a document.
#
# ⛔ AND IT IS SELF-ARMING RATHER THAN RED-ON-DAY-ONE, which is the T1 lesson applied: NOTHING WRITES
# A TIER INTO A RUN YET. If the clause refused every read with no recorded tier, all 283 historical
# runs would go uncountable at once and the gate would red everywhere — "a red that is an artefact of
# a migration reads exactly like a red that is a finding." So the arming condition is DERIVED FROM
# THE CORPUS, never from a flag someone must remember to flip: if NO run at this sha records a tier,
# the writer does not exist and every read reads ⬜ UNCHECKABLE with the reason named. The moment ANY
# run records one, the writer exists — and a run that omits it is then a real gap and REFUSES.
LENSES_FILE = os.path.join(ROOT, "cycle", "release", "lenses.json")


def declared_tiers(path=None):
    """→ ({lens: tier}, problem). ⛔ Never invents a roster — an absent file means UNCHECKABLE."""
    p = path or LENSES_FILE
    if not os.path.exists(p):
        return {}, "no tier declaration filed — expected %s" % os.path.relpath(p, ROOT)
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        return {}, "%s is unreadable: %s" % (os.path.basename(p), e)
    lenses = d.get("lenses")
    if not isinstance(lenses, dict) or not lenses:
        return {}, "%s declares no lenses" % os.path.basename(p)
    return {k: (v or {}).get("tier") for k, v in lenses.items()}, None


def recorded_tier(run_dir):
    """→ the tier this run says it was READ at, or None. Read from the run's own record, so nothing
    but that record can supply it — `check-arrival-dispositions.py`'s rule, applied to a tier."""
    for name in ("read.json", "capture.json", "transcript.json"):
        fp = os.path.join(run_dir, name)
        if not os.path.exists(fp):
            continue
        try:
            d = json.load(open(fp, encoding="utf-8"))
        except Exception:
            continue
        for key in ("readTier", "read_tier", "tier"):
            v = d.get(key) if isinstance(d, dict) else None
            if isinstance(v, str) and v:
                return v
        r = d.get("read") if isinstance(d, dict) else None
        if isinstance(r, dict) and isinstance(r.get("tier"), str) and r["tier"]:
            return r["tier"]
    return None


def tier_writer_exists(sha):
    """⭐ DERIVED ARMING. True once ANY run at this sha records a tier — i.e. once something in the
    stack actually writes one. Never a flag; a flag is a thing someone must remember to flip."""
    for seat in seats():
        for run in runs_for(seat):
            d = os.path.join(WALKS, seat, run)
            if judge(d, sha).get("at-sha", (False,))[0] and recorded_tier(d):
                return True
    return False


# ═══ T17 · THE IDENTICAL-FAILURE READ — is the HARNESS lying, or is the PRODUCT broken? ════════════
#
# ⛔ THE EVIDENCE IT EXISTS ON, measured: at `87c7aae`, FIVE of five lenses walking J8 failed the
# SAME assertion — `expect:.hh-utility` — with ZERO page errors. Eleven of battery C's twenty-two
# walks were spent on a fault the FIRST walk had already shown. Nothing read that signature, so the
# battery kept paying for the same finding.
#
# ⭐ THE INFERENCE, and its limit: when every lens on one journey fails the SAME action and the page
# raised no error, the thing they share is the ACTION LIST, not the product. A product fault reaches
# different lenses differently, and usually leaves a page error behind. ⛔ It is a SUSPICION, printed
# as one — "fix the action list, not the product" is advice, not a verdict.
#
# ⚠️⚠️ IT PRINTS; IT DOES NOT STOP THE BATTERY. Stopping is the pilot-walk clause in beat 8 and that
# is Paul's. This builds the signature that rule keys on and acquires no authority of its own.
#
# ⛔⛔ IT READS `failedActions[]`, NOT `steps[].ok`. The plan specifies `steps[].ok`; THAT FIELD DOES
# NOT EXIST — 0 of 283 transcripts carry a `steps` key, `journey-walk.py` contains the string zero
# times, and no stop carries an `ok`. Built against it this detector would find zero identical
# failures FOREVER and print silence: a permanent false-green in the one control whose entire job is
# catching a harness that is lying.
# ⭐ A CONFIDENT WRONG PREDICATE AND A CORRECT ONE PRINT THE SAME WAY: A NUMBER. The only thing that
# separated them here was reading the schema instead of trusting the field name. `release-gate.py`
# already reads `failedActions` in `judge()`, so the corrected predicate is this file's own.
#
# ⛔ SECURITY R6-B — it may read `journey · buildBefore/After · lens · origin · failedActions ·
# pageErrors` AND NOTHING ELSE, and it compares on a NORMALISED KEY: verb + selector, everything
# after the first `=` dropped. A typed action therefore contributes `type:#line1` and never its
# value, so a planted address cannot reach the output.

def normalise_action_key(failure):
    """→ `verb:selector` for a failed-action string, value dropped. ⛔ None when no action can be
    read — UNKNOWN, never a bucket that silently merges unlike failures into a false signature."""
    if not isinstance(failure, str) or not failure.strip():
        return None
    m = re.search(r"'([^']+)'", failure)
    act = m.group(1) if m else failure.strip().split(" ")[0]
    act = act.strip()
    if not act:
        return None
    return act.partition("=")[0]            # ⛔ everything after the first `=` is a VALUE


def suspect_harness(sha):
    """→ [(journey, key, lenses, total_lenses, env)] where EVERY lens that walked that journey at
    this sha failed the same normalised action, with zero page errors across all of them.

    ⚠️ N OF N, not "several". Four of five failing is a finding about the product or about one lens;
    only unanimity points at the thing they all share. ⛔ A single-lens journey can never trigger it:
    1-of-1 is unanimous and means nothing, so it is excluded by name rather than by accident."""
    by_journey = {}
    for seat in seats():
        for run in runs_for(seat):
            d = os.path.join(WALKS, seat, run)
            tp = os.path.join(d, "transcript.json")
            if not os.path.exists(tp):
                continue
            try:
                t = json.load(open(tp, encoding="utf-8"))
            except Exception:
                continue
            b, a = (t.get("buildBefore") or ""), (t.get("buildAfter") or "")
            if not (sha and b.startswith(sha) and b == a):
                continue
            j = journey_of(t)[0]
            lens = t.get("lens") or seat
            env = t.get("origin")
            keys = {normalise_action_key(f) for f in (t.get("failedActions") or [])}
            keys.discard(None)
            by_journey.setdefault((j, env), []).append(
                (lens, keys, len(t.get("pageErrors") or [])))

    out = []
    for (j, env), runs in sorted(by_journey.items(), key=lambda kv: str(kv[0])):
        lenses = {r[0] for r in runs}
        if len(lenses) < 2:
            continue                         # 1-of-1 is unanimous and says nothing
        counts = {}
        for lens, keys, _pe in runs:
            for k in keys:
                counts.setdefault(k, set()).add(lens)
        for k, who in sorted(counts.items()):
            if who != lenses:
                continue                     # not unanimous
            # ⛔ A PAGE ERROR ANYWHERE AMONG THEM MAKES IT A PRODUCT FAULT, not a harness one.
            if any(pe for lens, keys, pe in runs if k in keys and pe):
                continue
            out.append((j, k, sorted(who), len(lenses), env))
    return out


# ═══ T5 · ONE DEFINITION OF "WHICH CELLS WERE TESTED AT THIS SHA" ═════════════════════════════════
# ⛔ EXTRACTED BECAUSE release-state.py HELD A SECOND COPY. It re-implemented the best-run loop —
# same tie-break, same scoring, keyed on the SEAT — so the state file and the gate could disagree
# about the same sha and nothing would say so. `class: engine · must-not-diverge` names exactly this:
# ONE definition of "this candidate was tested". release-state now calls this rather than keeping an
# opinion of its own, the same way this file imports `rate_limits` from walk-integrity.
def cells_at(sha):
    """→ (rows, passing_cells, cells). `rows` is [(unit, best, n_runs, problems, superseded)] where
    best is (score, run, clauses, seat) or None. ⛔ The tie-break is `score > best[0]` and stays that
    way: within one cell two runs are a retry [paul-ruled 2026-09-11]."""
    cells = {}
    for seat in seats():
        for run in runs_for(seat):
            d = os.path.join(WALKS, seat, run)
            v = judge(d, sha)
            if not v.get("at-sha", (False, ""))[0]:
                continue
            u = unit_of(d)
            if u is None:
                continue
            cells.setdefault(u, []).append((run, seat, v))

    passing_cells, rows = [], []
    for u in sorted(cells):
        entries = sorted(cells[u], key=lambda e: e[0])        # chronological, so "retry" means later
        best = None
        for run, seat, v in entries:
            score = sum(1 for k, _ in CLAUSES if v.get(k, (None,))[0] is True)
            if best is None or score > best[0]:               # ⛔ UNCHANGED tie-break
                best = (score, run, v, seat)
        n_runs = len(entries)
        problems = sum((e[2].get("_problems", (0,))[0] or 0) for e in entries)
        superseded = bool(best) and (best[2].get("_problems", (0,))[0] or 0) == 0 and problems > 0
        rows.append((u, best, n_runs, problems, superseded))
        if best and all(best[2].get(k, (None,))[0] is True for k, _ in CLAUSES):
            passing_cells.append(u)
    return rows, passing_cells, cells


def report(sha, seats_only=False):
    print("release gate ① — build %s\n" % (sha[:7] if sha else "UNKNOWN"))
    if not sha:
        print("🔴 UNCHECKABLE: no candidate sha. Refusing to gate nothing.")
        return 2
    ss = seats()
    if not ss:
        print("🔴 UNCHECKABLE: no seats found on disk — refusing to report on an empty roster.")
        return 2

    # ⭐ T1 — THE ROSTER IS NOW CELLS, NOT DIRECTORIES. Every run at this sha is placed in its
    # `(journey, lens)` cell; the best run wins the cell's row, exactly as it used to win the seat's.
    # ⛔ THE TIE-BREAK IS UNCHANGED — `score > best[0]`, so ties keep the EARLIEST run — and that is
    # correct once the key is right. `[paul-ruled 2026-09-11]` a clean retry SUPERSEDES a failing run
    # at the same sha: within one cell, two runs are genuinely a retry, and a retry is how "run it
    # until it no longer fails" exits. The defect was never the comparison; it was the key.
    # ⭐ AND THE SUPERSESSION IS PRINTED ON THE GATE'S FACE — his ruling's second half, and a BUILD
    # REQUIREMENT, not merely a falsifier: a cell that needed a retry may never render like a cell
    # that passed first time. Without that print, T1 moves the unit without moving the legibility and
    # the failed actions are merely hidden in a new place.
    rows, passing_cells, cells = cells_at(sha)

    _tier_armed = tier_writer_exists(sha)
    for u, best, n_runs, problems, superseded in rows:
        label = "(%s, %s)" % u
        if not best:
            print("  🔴 %-26s no run at this build" % label)
            continue
        _, run, v, seat = best
        allgreen = all(v.get(k, (None,))[0] is True for k, _ in CLAUSES)
        # ⭐ THE SUPERSESSION LINE — Paul's ruling, on the face.
        tail = "%d run%s" % (n_runs, "" if n_runs == 1 else "s")
        # ⛔ THE NOUN FOLLOWS THE CLAUSE. `no-failed-actions` counts NON-WALKED STOPS **plus**
        # `failedActions[]` entries, so this quantity is "problem stop/action(s)", not "failed
        # actions" — the two differ (at `87c7aae`, 12 failed actions but 22 problems). Paul's
        # illustrative wording said "failed action"; the gate prints what it actually counted,
        # because a count without its predicate is this repo's most-repeated defect and it would be
        # absurd to re-commit it inside the line that exists to make a failure legible.
        if superseded:
            tail += " · %d problem stop/action%s, PASSING ON RETRY" % (problems, "" if problems == 1 else "s")
        elif problems:
            tail += " · %d problem stop/action%s" % (problems, "" if problems == 1 else "s")
        print("  %s %-26s %s  ·  %s%s" % ("✅" if allgreen else "🔴", label, run, tail,
                                          "" if is_legacy(u[0]) else ""))
        if is_legacy(u[0]):
            print("       ⬜ BACKFILLED cell — satisfies no declared cell; evidence, never coverage.")
        # ⚠️ the door's own answer, kept beside the cell and printed only when it DISAGREES.
        try:
            _t = json.load(open(os.path.join(WALKS, seat, run, "transcript.json"), encoding="utf-8"))
            _door = _t.get("journeyEntered")
            if _door and _t.get("journey") and _door != _t.get("journey"):
                print("       ⚠️ the door said %s; this walk walked %s — recorded, not resolved."
                      % (_door, _t.get("journey")))
        except Exception:
            pass
        marks = []
        for key, _label in CLAUSES:
            st, detail = v.get(key, (None, "not evaluated"))
            marks.append("%s %s" % ("✅" if st is True else ("🔴" if st is False else "⬜"), key))
        print("     " + "  ".join(marks))
        for key, label in CLAUSES:
            st, detail = v.get(key, (None, "not evaluated"))
            if st is not True:
                print("        %s %s — %s" % ("🔴" if st is False else "⬜", label, detail))
        # ── T3b · the READ TIER, checked against the declaration ──────────────────────────────
        _tiers, _tprob = declared_tiers()
        _rt = recorded_tier(os.path.join(WALKS, seat, run))
        _want = _tiers.get(u[1]) if _tiers else None
        if _tprob:
            print("        ⬜ read tier — UNCHECKABLE: %s" % _tprob)
        elif _rt and _want and _rt != _want:
            print("        🔴 READ TIER MISMATCH — this read records %r, %s declares %r. NOT COUNTED."
                  % (_rt, os.path.basename(LENSES_FILE), _want))
        elif _rt and _want:
            print("        ✅ read tier %r matches the declaration" % _rt)
        elif _rt and not _want:
            print("        🔴 READ TIER %r recorded for lens %r, which the declaration does not name "
                  "— NOT COUNTED (a lens with no declared tier cannot be checked against one)."
                  % (_rt, u[1]))
        elif _tier_armed:
            print("        🔴 NO READ TIER RECORDED — other runs at this build record one, so the "
                  "writer exists and this run omitted it. NOT COUNTED.")
        else:
            print("        ⬜ read tier — UNCHECKABLE: nothing in the stack writes a tier into a run "
                  "yet, so no run at this build records one. Declared %r; unverified."
                  % (_want or "—"))
        tp = v.get("third-party-throttled")
        if tp:
            print("        %s" % tp[1])
        st, detail = v.get("instrumented", (None, "not evaluated"))
        print("        %s instrumented (reported, counted from lap 2) — %s" % ("✅" if st is True else ("🔴" if st is False else "⬜"), detail))

    # ⭐ THE UNIT IS NAMED IN THE COUNT. "seats passing" was the sentence that made the 87c7aae
    # verdict readable as five clean walks; the count now says what it actually counted.
    _declared = [u for u in sorted(cells) if not is_legacy(u[0])]
    _legacy_n = len(cells) - len(_declared)
    print("\n  CELLS passing every clause: %d of %d   (a cell is a (journey, lens) pair)"
          % (len(passing_cells), len(cells)))
    if _legacy_n:
        print("  ⬜ %d of the %d cells %s BACKFILLED legacy — evidence, never coverage."
              % (_legacy_n, len(cells), "is" if _legacy_n == 1 else "are"))
    # ═══ T3 · THE MATRIX AND THE COVERAGE CLAIM ══════════════════════════════════════════════════
    spec, problem = read_cells()
    declared, unwalked = [], []
    if spec:
        declared = [((c or {}).get("journey"), (c or {}).get("lens")) for c in spec["cells"]]
        print("\n  ── MATRIX · declared cells from %s (lap %s, declaredBy %s) ──"
              % (spec["_file"], spec.get("lap", "?"), spec.get("declaredBy", "?")))
        width = max([len("(%s, %s)" % d) for d in declared] + [12])
        print("     %-*s  %s" % (width, "cell", "  ".join(k for k, _ in CLAUSES)))
        for d in declared:
            walked = next((r for r in rows if r[0] == d), None)
            label = "(%s, %s)" % d
            if not walked or not walked[1]:
                # ⛔ EMPTY CELLS ARE THE COVERAGE CLAIM. A declared cell with no run at this sha is
                # UNWALKED BY NAME and the gate REFUSES — absence never reads as a pass.
                print("     %-*s  %s  ⛔ UNWALKED at this build" % (width, label,
                      "  ".join("·".center(len(k)) for k, _ in CLAUSES)))
                unwalked.append(d)
                continue
            v = walked[1][2]
            marks = "  ".join(("✅" if v.get(k, (None,))[0] is True else
                               ("🔴" if v.get(k, (None,))[0] is False else "⬜")).center(len(k))
                              for k, _ in CLAUSES)
            print("     %-*s  %s" % (width, label, marks))
        extra = [u for u, b, n, pr, sup in rows if u not in declared and not is_legacy(u[0])]
        if extra:
            print("     ⬜ walked but NOT DECLARED: %s — evidence, and not a coverage claim "
                  "anyone made." % " · ".join("(%s, %s)" % u for u in extra))
    else:
        # ⛔ M12c — UNCHECKABLE WITH THE PATH NAMED, never a pass. The H4 convention exactly.
        print("\n  ⬜ MATRIX UNCHECKABLE — %s" % problem)
        print("     A cell list is declared by Paul at beat 6; this gate reads it and never writes it.")

    # ── STANDING COVERAGE HOLES — journeys the library knows and NO run has ever walked ───────────
    # ⭐ DERIVED, never a typed roster. The plan names "J1 · J5 · J7" in prose; J7 is absent from
    # JOURNEY_IDS entirely, so typing that trio here would assert a journey the harness does not
    # have. The set is computed, and an id named in a plan but missing from the library prints as
    # its own finding rather than silently not appearing.
    ids, _J, named = _journey_library()
    # ⛔ ONLY A RECORDED JOURNEY COUNTS AS WALKED. A door-measured cell proves the door read a
    # record that way, never that a walk went through that journey.
    ever = {u[0] for u, (mt, src) in cell_last_walked().items() if src == "recorded"}
    holes = [j for j in sorted(set(ids) | set(named)) if j not in ever]
    if holes:
        print("\n  ── STANDING UNWALKED — no run at ANY build has ever walked these ──")
        for j in holes:
            blocker = ""
            if j in named:
                nd = named[j]
                blocker = str(nd.get("needs", "")) if isinstance(nd, dict) else str(nd)
            print("     ⛔ %-4s %s" % (j, ("BLOCKER: " + blocker) if blocker else
                                       "declared in JOURNEYS; no walk on record"))
    # ⭐ THE LONGEST-UNWALKED READ — three lines, ranked by age and by NOTHING ELSE.
    lw = cell_last_walked()
    if lw:
        import datetime as _dt
        oldest = sorted(lw.items(), key=lambda kv: kv[1][0])[:3]
        print("\n  ── LONGEST UNWALKED (any build) ──")
        for u, (mt, src) in oldest:
            when = _dt.datetime.fromtimestamp(mt).strftime("%Y-%m-%d")
            if src == "recorded":
                print("     %-26s last walked %s" % ("(%s, %s)" % u, when))
            else:
                print("     %-26s ⬜ %s %s — NO WALK EVER DECLARED THIS JOURNEY; the door read a "
                      "record that way. Not a walk." % ("(%s, %s)" % u, src, when))

    # ── T17 · SUSPECT HARNESS ─────────────────────────────────────────────────────────────────────
    for j, key, who, total, env in suspect_harness(sha):
        print("\n  ⛔ SUSPECT HARNESS — FIX THE ACTION LIST, NOT THE PRODUCT")
        print("     %s of %s lenses walking %s at %s failed the SAME action, with ZERO page errors:"
              % (len(who), total, j, env or "an unrecorded env"))
        print("       %s" % key)
        print("       lenses: %s" % " · ".join(who))
        print("     ⚠️ A SUSPICION, NOT A VERDICT, and it stops nothing — when every lens on one "
              "journey fails the same action and the page raised no error, the thing they SHARE is "
              "the action list. A product fault reaches different lenses differently and usually "
              "leaves a page error behind. Read the first failing walk before spending the rest.")

    _retries = [u for u, b, n, pr, sup in rows if sup]
    if _retries:
        print("  ⚠️ %d cell(s) passed ONLY ON RETRY: %s — a retry exits the loop, and this line is "
              "why it can never look like a clean first pass." % (len(_retries),
              " · ".join("(%s, %s)" % u for u in _retries)))
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
    # ═══ J2 — RULED, SO THE GATE STOPS ASKING ════════════════════════════════════════════════════
    #
    # ⛔ THIS LINE USED TO SOLICIT A DECISION THAT HAD ALREADY BEEN MADE. It read:
    #   ~~"J2 is UNWALKABLE at every build since the open door … no transcript at any build has ever
    #     recorded a walked J2. Not covered here — awaiting Paul's re-scope-or-retire ruling."~~
    # TWO of its clauses were false by the time this step was written, and each failed differently:
    #
    # 1. ⛔ "no transcript at any build has ever recorded a walked J2" — FALSE, measured. Two runs
    #    record journey=J2/journeyDeclared=J2/journeyEntered=J2 at build 196e146 (an ancestor of
    #    HEAD), NINE STOPS ALL WALKED, ZERO PROBLEMS, with stop ids U01-arrive…U09-the-place —
    #    `journey_resuming`'s OWN purpose-built list, end to end. The claim was filed as
    #    "[measured, lap 7 battery]" and read the same way twice; BOTH readings were scoped to the
    #    battery's candidate shas, and 196e146 is not one of them. A count correct about its own
    #    scope, published as "at any build".
    # 2. ⛔ "awaiting Paul's re-scope-or-retire ruling" — FALSE. He RULED it at 10:05 EDT on
    #    2026-09-11, before this window opened: CYCLE-LOG.md § lap 8, "J2 (L8-P6) → re-scoped to
    #    'returning, founded nothing', NOT retired; the cell list may name it".
    #
    # ⭐ THE RULING IS NOT REOPENED BY THE FIRST CORRECTION — IT IS BETTER SUPPORTED. Paul declined to
    # retire J2 while believing it untestable; the record shows it walked clean, twice, through its
    # own procedure. Same direction, stronger evidence.
    # ⭐ AND THIS IS WHY THE LINE CHANGES NOW WHEN T3's INSTRUCTION SAID CARRY IT VERBATIM: that
    # instruction was conditioned on the question being UNRULED. It is ruled. A RULED ITEM IS STRUCK
    # WHERE IT WAS ASKED, NEVER ONLY WHERE IT WAS ANSWERED — otherwise the gate keeps asking Paul
    # for a decision he has already given, which is the exact failure this project found in a seat's
    # "what Paul must still rule" list three hours earlier.
    _j2runs = []
    for _seat in seats():
        for _run in runs_for(_seat):
            try:
                _t = json.load(open(os.path.join(WALKS, _seat, _run, "transcript.json"), encoding="utf-8"))
            except Exception:
                continue
            if _t.get("journey") == "J2":
                _bad = [x for x in (_t.get("stops") or []) if x.get("status") not in ("walked", "skipped", "n/a")]
                _j2runs.append((_seat, _run, (_t.get("buildBefore") or "")[:7],
                                len(_t.get("stops") or []), len(_bad) + len(_t.get("failedActions") or [])))
    print("  📐 coverage — J2 · RULED 2026-09-11: re-scoped to \"returning, founded nothing\", NOT "
          "retired; the cell list may name it. [paul-ruled, CYCLE-LOG.md § lap 8]")
    if _j2runs:
        _clean = [r for r in _j2runs if r[4] == 0]
        print("     ✅ and it HAS been walked — %d run(s) on record, %d clean: %s"
              % (len(_j2runs), len(_clean),
                 " · ".join("%s at %s (%d stops, %d problems)" % (r[1], r[2], r[3], r[4]) for r in _j2runs)))
    else:
        print("     ⬜ no run on record has walked it — UNWALKED, not unwalkable.")
    print("     ⚠️ OPEN, and it is a MEASUREMENT rather than a judgement: is J2 walkable AT HEAD? "
          "Its fixture is provisioned per run because the walk finishes the record it arrived on, so "
          "\"was walked\" and \"can be walked\" are different claims. Beat 8's to take, not this gate's.")
    _tiers, _tprob = declared_tiers()
    if _tprob:
        print("  ⬜ read tier — UNCHECKABLE: %s" % _tprob)
    else:
        print("  📐 read tier — declared in %s for %d lens(es). ⚠️ A DETECTOR, NOT A PREVENTER: "
              "nothing can force a session to spawn a lens at the declared tier; this gate refuses "
              "to COUNT a read whose recorded tier is absent or mismatched.%s"
              % (os.path.relpath(LENSES_FILE, ROOT), len(_tiers),
                 "" if _tier_armed else " Nothing writes a tier into a run yet, so every read at "
                 "this build is UNVERIFIED rather than verified."))
    # H4 (lap 7) — the two per-sha clauses, each read from its artifact convention
    cst, cdet = content_clause(sha, ss)
    ust, udet = ux_clause(sha)
    mark = lambda st: "✅" if st is True else ("🔴" if st is False else "⬜")
    print("  %s content read for this build (L7-P3: every walk read by the voice's owner) — %s" % (mark(cst), cdet))
    print("  %s UX sweep for this build (L7-P2: the two-pass sweep at this candidate) — %s" % (mark(ust), udet))

    # ⛔ M12a — A DECLARED CELL WITH NO RUN REFUSES. This is the 09-10 plan's falsifier ④, the
    # negative control: a gate that has only ever been seen to pass has proven nothing.
    if unwalked:
        print("\n🔴 GATE ① NOT PASSED at %s — %d DECLARED CELL(S) UNWALKED at this build: %s"
              % (sha[:7], len(unwalked), " · ".join("(%s, %s)" % u for u in unwalked)))
        print("   A cell nobody walked is not a cell that passed. Walk them, or amend the "
              "declaration — the gate will not infer which you meant.")
        return 1
    if len(passing_cells) == len(cells) and cells:
        if cst is True and ust is True:
            print("\n✅ every CELL passes, the content read is filed and the sweep is filed — gate ① PASSED at %s." % sha[:7])
            return 0
        print("\n🟡 every CELL passes — but %s, so this is NOT a bare pass." % (
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
    # ⚠️ ONE declaration for the whole function — several clause blocks below swap these to point at
    # a temporary corpus, and Python allows only one `global` per name per function body.
    global WALKS, CELLS_DIR, LENSES_FILE
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

    # ═══ T1 · M10a/b/c — THE UNIT, THE BACKFILL, AND WHAT A BACKFILLED CELL MAY NOT DO ═══════════
    with tempfile.TemporaryDirectory() as tmp:
        W = os.path.join(tmp, "walks"); os.makedirs(W)
        _saved = WALKS
        try:
            WALKS = W

            def mkrun(seat, run, **over):
                d = os.path.join(W, seat, run); os.makedirs(d, exist_ok=True)
                json.dump(dict(base, **over), open(os.path.join(d, "transcript.json"), "w"))
                open(os.path.join(d, "REPORT.md"), "w").write("all good")
                return d

            # M10a — ONE SEAT, TWO JOURNEYS, ONE SHA. The `87c7aae` SHAPE, synthesised.
            # ⚠️ The shape is real; the LABEL "(the 87c7aae shape)" in the plan is wrong and struck —
            # at `87c7aae` every failure has a later clean run in its own cell, so the real corpus
            # PASSES. Here the failing J8 has NO retry, which is what makes it able to go red.
            mkrun("mom", "R1", journey="J0", lens="mom")
            mkrun("mom", "R2", journey="J8", lens="mom", failedActions=["click:#x"])
            cs = {}
            for seat in seats():
                for run in runs_for(seat):
                    d = os.path.join(W, seat, run)
                    u = unit_of(d)
                    if u:
                        cs.setdefault(u, []).append(judge(d, "a" * 7))
            bit = len(cs) == 2 and ("J0", "mom") in cs and ("J8", "mom") in cs
            print("  %s M10a one seat walking two journeys at one sha → TWO cells, not one"
                  % ("✅" if bit else "🔴")); ok &= bit
            bit = cs[("J8", "mom")][0]["no-failed-actions"][0] is False and \
                  cs[("J0", "mom")][0]["no-failed-actions"][0] is True
            print("  %s M10a' … and the failing journey goes RED while the clean one stays green "
                  "(under the old seat key the clean run hid it)" % ("✅" if bit else "🔴")); ok &= bit

            # M10b — THE BACKFILL. ⛔ A bare `J1` or `J2` must FAIL this clause.
            j, src = journey_of(dict(base, fresh=True))
            b1 = (j == "J1-legacy" and src == "backfilled")
            j, src = journey_of(dict(base, fresh=False))
            b2 = (j == "J-returning-legacy" and src == "backfilled")
            j, src = journey_of(dict(base, fresh=False, journeyEntered="J3"))
            b3 = (j == "J3" and src == "door-measured")
            j, src = journey_of(dict(base, journey="J8", journeyEntered="J3"))
            b4 = (j == "J8" and src == "recorded")
            print("  %s M10b backfill: fresh→J1-legacy · not-fresh→J-returning-legacy · door→its own "
                  "answer · recorded wins" % ("✅" if (b1 and b2 and b3 and b4) else "🔴"))
            ok &= (b1 and b2 and b3 and b4)
            bit = journey_of(dict(base, fresh=False))[0] not in ("J2", "J4")
            print("  %s M10b' a bare J2/J4 is NEVER inferred — three journeys collapse into one "
                  "unreadable bucket and the record must not pretend otherwise" % ("✅" if bit else "🔴"))
            ok &= bit

            # M10c — a backfilled cell can satisfy NO declared cell.
            bit = is_legacy("J1-legacy") and is_legacy("J-returning-legacy") and not is_legacy("J3")
            print("  %s M10c a BACKFILLED cell is excluded from declared-cell coverage"
                  % ("✅" if bit else "🔴")); ok &= bit

            # ═══ T2 · M11a/b — `instrumented` RE-KEYED ════════════════════════════════════════════
            d = mkrun("strict", "R1", journey="J0", lens="strict")
            json.dump({"app": {"events": 0}}, open(os.path.join(d, "capture.json"), "w"))
            st, det = judge(d, "a" * 7)["instrumented"]
            bit = st is None and "UNCHECKABLE" in det and "T10" in det
            print("  %s M11a with NO declared profile, zero events reads ⬜ UNCHECKABLE naming the "
                  "reason — never the 🔴-forever it used to print" % ("✅" if bit else "🔴")); ok &= bit

            d2 = mkrun("strict", "R2", journey="J0", lens="strict")
            open(os.path.join(d2, "capture.json"), "w").write("{not json")
            st, _ = judge(d2, "a" * 7)["instrumented"]
            bit = st is None
            print("  %s M11b an unreadable capture.json still reads ⬜ on any profile"
                  % ("✅" if bit else "🔴")); ok &= bit
        finally:
            WALKS = _saved

    # ═══ T3 · M12a/b/c — THE DECLARED CELL LIST ═══════════════════════════════════════════════════
    with tempfile.TemporaryDirectory() as tmp:
        cd = os.path.join(tmp, "cells"); os.makedirs(cd)

        # M12c — no list filed → UNCHECKABLE WITH THE PATH NAMED, never a pass. (H4's convention.)
        spec, prob = read_cells(cd)
        bit = spec is None and "lap-<N>.json" in (prob or "")
        print("  %s M12c no cell list filed → UNCHECKABLE with the path named, never a pass"
              % ("✅" if bit else "🔴")); ok &= bit

        # M12b — an id the journey library does not know is REFUSED BY NAME.
        json.dump({"lap": 8, "cells": [{"journey": "J0", "lens": "mom"},
                                       {"journey": "J99", "lens": "mom"}], "declaredBy": "paul"},
                  open(os.path.join(cd, "lap-8.json"), "w"))
        spec, prob = read_cells(cd)
        bit = spec is None and "J99" in (prob or "")
        print("  %s M12b a cell naming a journey absent from the library is REFUSED, naming the id "
              "(a cell list is not a place to invent journeys)" % ("✅" if bit else "🔴")); ok &= bit

        # M12b' — the highest-numbered lap file wins, derived, never a number typed in the tool.
        json.dump({"lap": 8, "cells": [{"journey": "J0", "lens": "mom"}], "declaredBy": "paul"},
                  open(os.path.join(cd, "lap-8.json"), "w"))
        json.dump({"lap": 9, "cells": [{"journey": "J3", "lens": "mom"}], "declaredBy": "paul"},
                  open(os.path.join(cd, "lap-9.json"), "w"))
        spec, _ = read_cells(cd)
        bit = spec is not None and spec.get("lap") == 9
        print("  %s M12b' the lap is DERIVED from the highest-numbered file, never typed"
              % ("✅" if bit else "🔴")); ok &= bit

        # M12d — an empty cells[] is refused, not read as "nothing declared, therefore fine".
        json.dump({"lap": 10, "cells": [], "declaredBy": "paul"},
                  open(os.path.join(cd, "lap-10.json"), "w"))
        spec, prob = read_cells(cd)
        bit = spec is None and "no cells" in (prob or "")
        print("  %s M12d a list declaring ZERO cells is refused — an empty claim is not coverage"
              % ("✅" if bit else "🔴")); ok &= bit

    # M12a — a declared cell with no run must REFUSE. Proven on the real `report()` path, because
    # this is the 09-10 plan's falsifier ④ and a clause that only tests a helper proves nothing
    # about the gate's exit code.
    import io, contextlib
    with tempfile.TemporaryDirectory() as tmp:
        W = os.path.join(tmp, "walks"); os.makedirs(os.path.join(W, "mom", "R1"))
        json.dump(dict(base, journey="J0", lens="mom"),
                  open(os.path.join(W, "mom", "R1", "transcript.json"), "w"))
        open(os.path.join(W, "mom", "R1", "REPORT.md"), "w").write("all good")
        cd = os.path.join(tmp, "cells"); os.makedirs(cd)
        json.dump({"lap": 8, "declaredBy": "paul",
                   "cells": [{"journey": "J0", "lens": "mom"}, {"journey": "J3", "lens": "mom"}]},
                  open(os.path.join(cd, "lap-8.json"), "w"))
        _sw, _sc = WALKS, CELLS_DIR
        try:
            WALKS, CELLS_DIR = W, cd
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = report("a" * 40)
            out = buf.getvalue()
            bit = rc != 0 and "UNWALKED" in out and "(J3, mom)" in out
            print("  %s M12a a DECLARED cell with no run prints UNWALKED by name and the gate "
                  "REFUSES (falsifier ④, the negative control)" % ("✅" if bit else "🔴")); ok &= bit
            bit = "(J0, mom)" in out
            print("  %s M12a' … while the declared cell that WAS walked still prints its marks"
                  % ("✅" if bit else "🔴")); ok &= bit
        finally:
            WALKS, CELLS_DIR = _sw, _sc

    # ═══ T17 · M23 — THE IDENTICAL-FAILURE READ, AND THE THREE WAYS IT MUST NOT FIRE ════════════
    with tempfile.TemporaryDirectory() as tmp:
        W = os.path.join(tmp, "walks")
        _sw = WALKS
        try:
            WALKS = W

            def mkw(lens, fails, pe=0, journey="J8"):
                d = os.path.join(W, lens, "R1"); os.makedirs(d, exist_ok=True)
                json.dump(dict(base, journey=journey, lens=lens, failedActions=fails,
                               pageErrors=["PAGEERROR: x"] * pe),
                          open(os.path.join(d, "transcript.json"), "w"))
                open(os.path.join(d, "REPORT.md"), "w").write("all good")

            FIVE = ["mom", "wide-eyed", "strict", "owner", "handover"]
            for L in FIVE:
                mkw(L, ["'expect:.hh-utility' — expect: not visible — .hh-utility"])
            r = suspect_harness("a" * 7)
            bit = len(r) == 1 and r[0][1] == "expect:.hh-utility" and r[0][3] == 5
            print("  %s M23a five lenses, one journey, the SAME failure, zero page errors → SUSPECT"
                  % ("✅" if bit else "🔴")); ok &= bit

            for L in FIVE:
                mkw(L, ["'expect:.x-%s' — expect: not visible" % L])
            bit = suspect_harness("a" * 7) == []
            print("  %s M23b five DIFFERENT failures → not suspect (that is five findings)"
                  % ("✅" if bit else "🔴")); ok &= bit

            for L in FIVE:
                mkw(L, ["'expect:.hh-utility' — expect: not visible"], pe=1)
            bit = suspect_harness("a" * 7) == []
            print("  %s M23c identical failures WITH page errors → not suspect (a product fault)"
                  % ("✅" if bit else "🔴")); ok &= bit

            # ⛔ FOUR OF FIVE IS NOT UNANIMOUS — it is a finding about the product or about one lens.
            for L in FIVE[:4]:
                mkw(L, ["'expect:.hh-utility' — expect: not visible"])
            mkw(FIVE[4], [])
            bit = suspect_harness("a" * 7) == []
            print("  %s M23d FOUR of five → not suspect; only unanimity points at what they share"
                  % ("✅" if bit else "🔴")); ok &= bit

            # ⛔ A SINGLE-LENS JOURNEY IS UNANIMOUS BY CONSTRUCTION AND MEANS NOTHING.
            import shutil as _sh
            _sh.rmtree(W); os.makedirs(W)
            mkw("mom", ["'expect:.hh-utility' — expect: not visible"])
            bit = suspect_harness("a" * 7) == []
            print("  %s M23e ONE lens alone never triggers it — 1-of-1 is unanimous and says nothing"
                  % ("✅" if bit else "🔴")); ok &= bit
        finally:
            WALKS = _sw

    # ⛔ R6-B — A PLANTED VALUE MUST NOT REACH THE OUTPUT. The key is verb + selector, everything
    # after the first `=` dropped, so a typed action contributes its FIELD and never its content.
    _planted = normalise_action_key("'type:#line1=282 Church Mountain Road' — could not do")
    bit = _planted == "type:#line1" and "Church" not in _planted
    print("  %s M23f a planted address in a failed action yields only the SELECTOR"
          % ("✅" if bit else "🔴")); ok &= bit
    bit = normalise_action_key("") is None and normalise_action_key(None) is None
    print("  %s M23g an unreadable failure is None, never a bucket unlike failures merge into"
          % ("✅" if bit else "🔴")); ok &= bit

    # ═══ T3b · M13a-e — THE READ TIER. ⚠️ The plan labels these M12d, which T3 already used for
    # "a list declaring zero cells is refused"; renaming a proven clause to match a label would be
    # churn, so they are M13*. Flagged rather than silently renumbered.
    with tempfile.TemporaryDirectory() as tmp:
        lf = os.path.join(tmp, "lenses.json")
        _sl = LENSES_FILE
        try:
            LENSES_FILE = os.path.join(tmp, "absent.json")
            t, prob = declared_tiers()
            bit = t == {} and "no tier declaration filed" in (prob or "")
            print("  %s M13a no tier declaration → UNCHECKABLE with the path, never a pass"
                  % ("✅" if bit else "🔴")); ok &= bit

            json.dump({"lenses": {"mom": {"tier": "opus"}}}, open(lf, "w"))
            LENSES_FILE = lf
            t, prob = declared_tiers()
            bit = prob is None and t.get("mom") == "opus"
            print("  %s M13b a filed declaration reads its tiers" % ("✅" if bit else "🔴")); ok &= bit

            W = os.path.join(tmp, "walks"); os.makedirs(os.path.join(W, "mom", "R1"))
            rd = os.path.join(W, "mom", "R1")
            json.dump(dict(base, journey="J0", lens="mom"), open(os.path.join(rd, "transcript.json"), "w"))
            open(os.path.join(rd, "REPORT.md"), "w").write("all good")
            bit = recorded_tier(rd) is None
            print("  %s M13c a run recording no tier reads None (never a guessed default)"
                  % ("✅" if bit else "🔴")); ok &= bit

            json.dump(dict(base, journey="J0", lens="mom", readTier="sonnet"),
                      open(os.path.join(rd, "transcript.json"), "w"))
            bit = recorded_tier(rd) == "sonnet"
            print("  %s M13d a recorded tier is read from the run's OWN record"
                  % ("✅" if bit else "🔴")); ok &= bit

            # ⭐ M13e — THE SELF-ARMING PROPERTY, which is the whole reason this clause cannot red
            # the historical corpus on day one. Proven both ways.
            _sw = WALKS
            try:
                WALKS = W
                armed_with = tier_writer_exists("a" * 7)
                json.dump(dict(base, journey="J0", lens="mom"), open(os.path.join(rd, "transcript.json"), "w"))
                armed_without = tier_writer_exists("a" * 7)
            finally:
                WALKS = _sw
            bit = armed_with is True and armed_without is False
            print("  %s M13e the clause SELF-ARMS from the corpus — dormant while nothing writes a "
                  "tier, armed the moment any run does (never a flag someone must flip)"
                  % ("✅" if bit else "🔴")); ok &= bit
        finally:
            LENSES_FILE = _sl

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
