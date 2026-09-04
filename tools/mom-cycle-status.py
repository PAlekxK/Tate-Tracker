#!/usr/bin/env python3
"""mom-cycle-status.py — the Mom-feedback loop's GLANCEABLE STATUS SURFACE.

The awareness half of the definable loop (`MOM-CYCLE-MAP.md`). Paul reads the
loop's position HERE, not by parsing an agent's action stream.

WHY THIS EXISTS
---------------
`[paul-stated 2026-08-03]` every recurring AI workstream gets a definable loop,
and one of its five parts is *"a very intentional design to keep me aware and in
control"* — status that is READ, never narrated. Until 2026-08-04 this loop had
five detectors (check-mom-ack, check-cards, check-data-inline, check-digest-fresh,
read-mom-feedback) and no surface that said WHERE IN THE LOOP WE ARE. Five green
exit codes do not answer "is anything waiting on me."

⭐ NON-AI DOOR (`[paul-stated 2026-08-02]`). No model runs here. Every signal is
derived from canon on disk plus the Worker's own endpoints. If the only way to
learn whether Mom is owed a reply were to ask Claude, this loop would be broken.

WHAT IT WILL NOT DO
-------------------
It does not report a draft that exists only in a conversation. A return leg
sitting in an agent's chat window is not loop state — it is unshipped. What this
prints is what the RECORD owes her, which is the thing that can actually be
verified. `[the 7/26 lesson: capture is not a loop]`

⭐⭐ ARMED vs FIRED — the defect this board carried until 2026-08-12
--------------------------------------------------------------------
`MOM-CYCLE-MAP.md` § "What STARTS a lap" names three states that **must stay
tellable apart** — RESTING · ARMED · FIRED — and this board could not tell the
last two apart. It made two separate collapses, and both had to be undone:

**Collapse 1 — every arrival looked like her arrival.** The flags keyed on *input
landed*, never on *whose browser it landed from*, so Paul's own bench taps raised
the same 🔴 as Mom speaking. On 2026-08-10 the board read 🔴 RETURN LEG + 🔴 UNREAD
off a Guru turn whose own text says *"testing testing this is Paul… disregard this
data."* Measured again on 2026-08-12 and still true: all three arrivals lighting
the board were `d-‹p-7f3a2c›`, a device carrying
`excludeFromEngagement: true` in `tools/people.json` since 2026-07-28 — a
declaration the funnel had honoured for two weeks and this board had never read.

**Collapse 2 — "nobody has looked" was rendered as "she is owed a card."** The
board derived *the return leg is owed* from `check-mom-ack.py`'s exit code, which
is 1 for any finding. So R2b UNREAD and R1/R2 STALE landed on the same leg with
the same red. They are not the same: UNREAD is a five-minute read at leg 1, STALE
is a Mom-facing card at Paul's gate at leg 6. `check-mom-ack.py --json` now says
which rule fired, and this board routes them to different legs.

⛔ **AND THE FIX THAT WAS REFUSED, because it is the trap:** *do not assert
attribution.* Nothing here says a record IS Mom's — there is no "hers" bucket and
`split_arrivals` cannot produce one. A device Paul registered as his own is
`bench`; **everything else, including a record with no deviceId at all, is
`unresolved`** and keeps the board lit. Bench arrivals are SEPARATED AND NAMED on
screen, never dropped, because he shared his phone with Mom until 2026-07-28 and
a silent drop could discard hers. Separating a count you can still see is not the
same act as deleting a record you cannot.

Exit codes follow the sibling checks: 0 = nothing waiting, 1 = something is.

Usage:
    python3 tools/mom-cycle-status.py
    python3 tools/mom-cycle-status.py --json
    python3 tools/mom-cycle-status.py --selftest   # known-answer + negative controls
"""
import argparse
import datetime as dt
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

spec = importlib.util.spec_from_file_location("momlib", os.path.join(HERE, "momlib.py"))
momlib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(momlib)

# ⭐ ONE GUARD, NOT TWO. Leg 0's concurrent-session check is `guard-concurrent.py`
# and this board READS it rather than shelling out to git itself. It used to run
# its own `git log --oneline -1` — a second, divergent copy of the same check,
# and the copy that swallowed every failure into `head = ""` (see gather()).
_gspec = importlib.util.spec_from_file_location(
    "guard_concurrent", os.path.join(HERE, "guard-concurrent.py"))
guard = importlib.util.module_from_spec(_gspec)
_gspec.loader.exec_module(guard)

# The legs, in the order SKILL.md defines them. `gate` marks a leg that a run
# CANNOT cross on its own — the structural half of human-in-the-loop.
LEGS = [
    ("0", "GUARD",   False, "concurrent session / HEAD moved"),
    ("1", "READ",    False, "the deterministic sweep"),
    ("2", "TRIAGE",  False, "four classes, routed"),
    ("3", "RESOLVE", True,  "ambiguity ladder — tier 2 is Paul"),
    ("4", "EXPERT",  False, "one seat, escalate on trigger"),
    ("5", "SHIP",    False, "wins that never reach her"),
    ("6", "GATE",    True,  "the return leg, at Paul's gate"),
    ("7", "CLOSE",   False, "dispositions + watermark"),
]


def _run(tool, *args):
    """Run a sibling check, return (exit_code, stdout). Never raises."""
    try:
        p = subprocess.run(
            [sys.executable, os.path.join(HERE, tool), *args],
            capture_output=True, text=True, timeout=120, cwd=ROOT,
        )
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except Exception as e:
        return -1, f"{type(e).__name__}: {e}"


def gather():
    """Derive every signal. Each carries the SOURCE it came from — a signal with
    no named source is a rumour, and this loop has already paid for one."""
    sig = {}

    cards_rc, cards_out = _run("check-cards.py")
    sig["served_queue"] = {
        "source": "tools/check-cards.py",
        "clean": cards_rc == 0,
        "detail": [l.strip() for l in cards_out.splitlines() if "🔴" in l or "🟡" in l],
    }

    # ⭐ --json, not the exit code. The exit code is 1 for ANY finding, which is
    # what forced UNREAD and STALE onto the same leg (collapse 2, above).
    ack_rc, ack_out = _run("check-mom-ack.py", "--json")
    try:
        ack = json.loads(ack_out)
    except ValueError:
        ack = {"problems": ["UNPARSEABLE"], "unread": [], "offline": True}
    probs = set(ack.get("problems") or [])
    sig["return_leg"] = {
        "source": "tools/check-mom-ack.py --json",
        # The ribbon itself is behind her, or absent, or never shipped. THIS is the
        # leg-6 state — a Mom-facing card at Paul's gate.
        "owed": bool(probs & {"STALE", "NOT SHIPPED", "NO CLOCK", "UNPARSEABLE"}),
        "why": sorted(probs),
        # Something landed that nothing has read. A leg-1 state, and cheap.
        "unread": ack.get("unread") or [],
        "offline": bool(ack.get("offline")),
    }

    # ⭐ The ARMED/FIRED discriminator. Arrivals newer than each channel's read
    # mark, split by ORIGIN — never by person. See the module docstring.
    try:
        tok0 = momlib.resolve_token()
        sig["arrivals"] = {
            "source": "momlib.arrivals_by_origin (tools/people.json declarations)",
            **momlib.arrivals_by_origin(tok0),
        } if tok0 else {"source": "momlib.arrivals_by_origin", "channels": [],
                        "errors": ["no token"]}
    except Exception as e:  # noqa: BLE001
        sig["arrivals"] = {"source": "momlib.arrivals_by_origin", "channels": [],
                           "errors": [f"{type(e).__name__}: {e}"]}

    inline_rc, _ = _run("check-data-inline.py")
    digest_rc, _ = _run("check-digest-fresh.py")
    sig["canon_surfaces"] = {
        "source": "check-data-inline.py + check-digest-fresh.py",
        "clean": inline_rc == 0 and digest_rc == 0,
    }

    # Her newest input, and whether the record has answered through it.
    try:
        tok = momlib.resolve_token()
        state = momlib.load_read_state()
        sig["channels"] = {
            "source": ".private/channel-read-state.json",
            "read_through": {k: v.get("readThrough") for k, v in (state or {}).items()},
        }
    except Exception as e:
        sig["channels"] = {"source": ".private/channel-read-state.json", "error": str(e)}

    # Concurrency guard — Leg 0. A moving HEAD is the one signal that invalidates
    # everything below it, so it is derived first and printed loudest.
    #
    # ⭐ DELEGATED, not re-implemented (2026-08-31). This block used to run its own
    # three git commands inside a bare `except: head, dirty, unpushed = "", "", ""`
    # — so a repo the tool could not read rendered as a repo with an empty HEAD, 0
    # dirty files and 0 unpushed commits: a guard failure wearing a clean board.
    # `repo_state()` carries `ok`, and every consumer below fails closed on it.
    sig["repo"] = guard.repo_state(ROOT)
    return sig


def arrival_counts(sig):
    """(unresolved, bench) totals across every channel, newer than its read mark."""
    chans = (sig.get("arrivals") or {}).get("channels") or []
    return (sum(c["unresolved"]["count"] for c in chans),
            sum(c["bench"]["count"] for c in chans))


def position(sig):
    """Where the loop is standing, what STATE it is in, and whose move it is.

    Returns (leg, state, needs_paul). PURE — it reads `sig` and nothing else, so
    `--selftest` can drive it with fixtures instead of the network.

    Deliberately conservative, and the order is the argument:

    1. **The return leg outranks everything** — it is the only leg whose absence
       is invisible to Mom AND to Paul, and it is the leg that sat 8 days stale
       during her best week. Note this is now the RIBBON rules only; UNREAD no
       longer reaches leg 6.
    2. **A wrong served queue is a Mom-facing defect**, same gate.
    3. **FIRED** — an arrival nobody has read, from a browser Paul did not
       register as his own. This is the trigger the map defines, and it lands at
       leg 1 READ, not at leg 6: until someone looks, *nothing is known about
       whose it was*, and a board that jumps straight to "draft her a card" is
       asserting the very attribution this loop refuses to assert.
    4. Canon surfaces behind → leg 5.
    5. Otherwise ARMED — the healthy steady state, not an overdue lap.
    """
    if sig["return_leg"]["owed"] or not sig["served_queue"]["clean"]:
        return "6", "FIRED", True
    unresolved, _bench = arrival_counts(sig)
    if unresolved:
        return "1", "FIRED", False
    if not sig["canon_surfaces"]["clean"]:
        return "5", "ARMED", False
    return "7", "ARMED", False


# --------------------------------------------------------------- selftest
#
# ⭐ WHY THIS TOOL GETS ONE (W14's rule, applied to the board). The one artifact
# in this loop that makes a claim ABOUT A PERSON is the one that shipped without a
# control — and this board's claim is the strongest of them all: *she has spoken*
# or *she has not*. Every case below is a known answer, and three of them are
# NEGATIVE controls: they assert the board still goes red on inputs a careless
# exclusion would have swallowed.

_FIXTURE_BENCH = {"d-bench-1"}


def _sig(*, unresolved=0, bench=0, owed=False, queue_clean=True, canon_clean=True):
    """A minimal signal dict — the same shape `gather()` produces."""
    return {
        "served_queue": {"clean": queue_clean, "detail": []},
        "return_leg": {"owed": owed, "why": ["STALE"] if owed else [], "unread": [], "offline": False},
        "canon_surfaces": {"clean": canon_clean},
        "arrivals": {"channels": [{"name": "guru", "read_through": None,
                                   "bench": {"count": bench, "latest": "2026-08-09T00:00:00Z"},
                                   "unresolved": {"count": unresolved,
                                                  "latest": "2026-08-09T00:00:00Z"}}]},
        "repo": {"ok": True, "head": "", "head_sha": None, "error": None,
                 "dirty_files": 0, "unpushed_commits": 0},
    }


def selftest():
    fails = []
    ran = []

    def check(label, got, want):
        # ⚠️ COUNT THE ASSERTIONS, never state the number in prose. This line used
        # to end `"14 assertions, incl. 3 negative controls."` as a literal, and by
        # 2026-08-17 the suite held 31 — a green summary confidently under-reporting
        # its own coverage by more than half. Same shape as every stale-count
        # finding in this repo, sitting inside the check that exists to catch them.
        ran.append(label)
        if got != want:
            fails.append(f"{label}\n        got  {got}\n        want {want}")

    # ---- split_arrivals: the classifier, driven by fixtures ----
    recs = [
        {"deviceId": "d-bench-1", "updatedAt": "2026-08-09T10:00:00Z"},   # bench
        {"deviceId": "d-someone-else", "updatedAt": "2026-08-09T11:00:00Z"},  # unresolved
        {"updatedAt": "2026-08-09T12:00:00Z"},                            # NO device -> unresolved
        {"deviceId": "d-bench-1", "updatedAt": "2026-08-01T10:00:00Z"},    # older than cutoff
    ]
    s = momlib.split_arrivals(recs, ("updatedAt",), cutoff="2026-08-05T00:00:00Z",
                              bench_ids=_FIXTURE_BENCH)
    check("split: bench count", len(s["bench"]), 1)
    check("split: unresolved count", len(s["unresolved"]), 2)
    check("split: cutoff excluded the old bench record", s["bench"], ["2026-08-09T10:00:00Z"])

    # NEGATIVE CONTROL 1 — a record with NO deviceId must never be swallowed.
    s2 = momlib.split_arrivals([{"updatedAt": "2026-08-09T12:00:00Z"}], ("updatedAt",),
                               bench_ids=_FIXTURE_BENCH)
    check("no-device record is UNRESOLVED (fails open)",
          (len(s2["bench"]), len(s2["unresolved"])), (0, 1))

    # NEGATIVE CONTROL 2 — an unregistered device must never be swallowed.
    s3 = momlib.split_arrivals([{"deviceId": "d-brand-new", "updatedAt": "2026-08-09T12:00:00Z"}],
                               ("updatedAt",), bench_ids=_FIXTURE_BENCH)
    check("unregistered device is UNRESOLVED (fails open)",
          (len(s3["bench"]), len(s3["unresolved"])), (0, 1))

    # NEGATIVE CONTROL 3 — there is no path to a "hers" bucket.
    check("classifier has exactly two buckets, and neither is 'hers'",
          sorted(s.keys()), ["bench", "unresolved"])

    # ---- position(): the state machine ----
    # THE LIVE 2026-08-10 CASE. Three bench arrivals, nothing else. Before the fix
    # this read leg 6 / NEEDS YOU off Paul's own test taps.
    check("bench-only arrivals read ARMED at leg 7",
          position(_sig(bench=3)), ("7", "ARMED", False))
    # The same three arrivals from a browser nobody registered must FIRE — and at
    # leg 1 READ, not leg 6. Origin unresolved is not permission to go quiet.
    check("unresolved arrivals FIRE at leg 1, not leg 6",
          position(_sig(unresolved=3)), ("1", "FIRED", False))
    # Mixed: one unresolved among bench traffic still fires.
    check("one unresolved among bench traffic still fires",
          position(_sig(unresolved=1, bench=9)), ("1", "FIRED", False))
    # A genuinely stale ribbon is Paul's, at leg 6.
    check("a stale ribbon is leg 6 and NEEDS YOU",
          position(_sig(owed=True)), ("6", "FIRED", True))
    # A stale ribbon outranks unresolved arrivals.
    check("the return leg outranks an unread arrival",
          position(_sig(owed=True, unresolved=5)), ("6", "FIRED", True))
    # A wrong served queue is Mom-facing and keeps its gate.
    check("a dirty served queue is leg 6 and NEEDS YOU",
          position(_sig(queue_clean=False)), ("6", "FIRED", True))
    # Canon drift is ours, never a lap trigger.
    check("canon drift is leg 5 and stays ARMED",
          position(_sig(canon_clean=False)), ("5", "ARMED", False))
    # The resting state.
    check("nothing anywhere reads ARMED at leg 7",
          position(_sig()), ("7", "ARMED", False))

    # ── ENGAGEMENT AS A TRIGGER `[paul-approved 2026-08-17]` ─────────────────
    # Every signal proven in BOTH directions, plus its UNMEASURED case. The
    # stakes are the mirror of this board's original defect: that one could not
    # say she HAD spoken; this one must not say she was quiet when the event was
    # simply not being recorded yet.
    def _eng(**ev):
        unreadable = ev.pop("_unreadable", [])
        sess = ev.pop("_sessions", 0)
        return {"events": ev, "sessions": [{}] * sess, "unreadable_zeros": unreadable}

    def _named(raw, days=None):
        sigs, fired = engagement_signals(raw, days)
        return {s["name"]: s for s in sigs}, fired

    # C5 3b — the denominator follows the module set.
    sg, _ = engagement_signals(_eng(momqueue_viewed=5, momqueue_tapped=0), None, card_modules=False)
    sg = {x["name"]: x for x in sg}
    check("MODULES  no card-bearing module on → offers-passed is '—' and never fires",
          (sg["offers-passed"]["value"], sg["offers-passed"]["fired"]), ("—", False))
    sg, _ = engagement_signals(_eng(momqueue_viewed=5, momqueue_tapped=0), None, card_modules=None)
    sg = {x["name"]: x for x in sg}
    check("MODULES  unreadable module set → offers-passed is '?'", sg["offers-passed"]["value"], "?")
    check("MODULES  at Fernwood a card-bearing module IS on", _card_modules_on(), True)
    # C7 1b — answer-age follows the module set, and ON-but-empty still fires
    sg, _ = engagement_signals(_eng(), 22, card_modules=False); sg = {x["name"]: x for x in sg}
    check("C7 1b  a 22-day gap at an estate with no card-bearing module publishes '?' and never fires",
          (sg["answer-age"]["value"], sg["answer-age"]["fired"]), ("?", False))
    sg, _ = engagement_signals(_eng(), 22, card_modules=True); sg = {x["name"]: x for x in sg}
    check("C7 1b  the same gap where a card module is on (even with an empty plants.json) STILL fires",
          sg["answer-age"]["fired"], True)

    s, f = _named(_eng(momqueue_viewed=3, momqueue_tapped=0))
    check("3 offers seen and passed FIRES", s["offers-passed"]["fired"], True)
    check("...and it is named as the reason", "offers-passed" in f, True)
    s, _ = _named(_eng(momqueue_viewed=2, momqueue_tapped=0))
    check("NEAR MISS — 2 passed does not fire", s["offers-passed"]["fired"], False)
    s, _ = _named(_eng(momqueue_viewed=4, momqueue_tapped=4))
    check("offers she TAPPED are not passed offers", s["offers-passed"]["fired"], False)

    # ⭐ THE CONTROL THAT MATTERS MOST. An event not live for the whole window
    #   has an unreadable zero, and a 0 there would read as "she ignored it".
    s, f = _named(_eng(_unreadable=["momqueue_viewed"]))
    check("an UNMEASURED offer count publishes '?'", s["offers-passed"]["value"], "?")
    check("...and never fires on it", s["offers-passed"]["fired"], False)

    s, _ = _named(_eng(_sessions=3))
    check("3 quiet sessions FIRES", s["sessions-quiet"]["fired"], True)
    s, _ = _named(_eng(_sessions=2))
    check("NEAR MISS — 2 quiet sessions does not fire", s["sessions-quiet"]["fired"], False)

    # ⭐⭐ THE SAME-DAY LAP CONTROL (added 2026-09-01, after L1). `collect()`
    # filtered on `day < window_start` — two YYYY-MM-DD strings — so the window
    # covered the WHOLE DAY the lap is dated, and a lap that opened and closed on
    # one day counted its OWN trigger session. Mom lap 8 published FIRED with 0
    # unresolved arrivals the instant it closed, and `focus.py` then spilled four
    # Fernwood rows into Paul's queue as "cycle FIRED and unrun".
    # These legs assert the WINDOW, not the signals — the signals were always
    # right about what they were given.
    import importlib.util as _il
    _s = _il.spec_from_file_location("_eng_mod", os.path.join(HERE, "read-mom-engagement.py"))
    _e = _il.module_from_spec(_s); _s.loader.exec_module(_e)

    DAY, TS = "2026-09-01", "2026-09-01T16:48:11Z"
    _data = {"days": {DAY: [{"device": {"deviceId": "dev-hers"}, "events": [
        {"type": "session_start", "ts": "2026-09-01T15:10:00.000Z"},   # BEFORE the close
        {"type": "session_start", "ts": "2026-09-01T17:30:00.000Z"},   # AFTER the close
    ]}]}}
    hers = {"dev-hers"}

    mine, _o, _f = _e.collect(_data, hers, DAY, TS)
    check("⭐ an instant-bounded window EXCLUDES the lap's own trigger session",
          len(mine), 1)
    check("...and keeps what happened after the close", mine[0]["_ts"],
          "2026-09-01T17:30:00.000Z")

    # PAIRED: the legacy path must be byte-identical for laps with no instant —
    # a backfilled guess at when lap 3 closed would be a fabricated timestamp.
    mine_legacy, _o, _f = _e.collect(_data, hers, DAY, None)
    check("PAIRED — with NO instant, the day-granular behaviour is unchanged",
          len(mine_legacy), 2)

    # And an event with no ts at all must not be silently kept by the instant path.
    _noTs = {"days": {DAY: [{"device": {"deviceId": "dev-hers"},
                             "events": [{"type": "session_start"}]}]}}
    mine_nots, _o, _f = _e.collect(_noTs, hers, DAY, TS)
    check("an event with NO timestamp is excluded, never assumed in-window",
          len(mine_nots), 0)

    s, _ = _named(_eng(), days=21)
    check("a 21-day answer gap FIRES", s["answer-age"]["fired"], True)
    s, _ = _named(_eng(), days=20)
    check("NEAR MISS — 20 days does not fire", s["answer-age"]["fired"], False)
    s, _ = _named(_eng(), days=None)
    check("an unknown answer age is '?', not 0", s["answer-age"]["value"], "?")

    # A dead reader must not read as a quiet user.
    s, f = _named(None)
    check("an unreadable /api/metrics fires NOTHING", f, [])
    check("...and says so rather than publishing zeros",
          "UNMEASURED" in s["engagement"]["detail"], True)

    # The prose parser this borrows its answer-age from.
    check("the answer-age parser reads the real line shape",
          _AGE_RX.search("🌿 Mom-check — last checked today · her last answer "
                         "2026-08-03 (14d ago).").group(1), "14")
    check("...and yields nothing on a line without one",
          _AGE_RX.search("🌿 Mom-check — no answers from her in the last 30 days."), None)

    # ---- the declaration this all rests on is actually in people.json ----
    real = momlib.bench_device_ids()
    if not real:
        fails.append("bench_device_ids() is EMPTY — people.json has no "
                     "`excludeFromEngagement` device, so the board cannot separate "
                     "bench traffic at all.")
    if real & momlib.harness_device_ids():
        fails.append("a device is registered as BOTH bench and harness — the two "
                     "claims are different strengths and must not overlap.")

    if fails:
        print(f"❌ mom-cycle-status selftest: {len(fails)} failure(s)")
        for f in fails:
            print(f"   · {f}")
        return 1
    print(f"✅ mom-cycle-status selftest — {len(ran)} assertions "
          f"(arrival classifier · leg position · engagement trigger), "
          f"every fire paired with a near-miss that must not.")
    return 0


STATE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "data", "cycle-state.json")

# ── ENGAGEMENT AS A TRIGGER `[paul-approved 2026-08-17]` ─────────────────────
#
# CLAUDE.md has carried this as an OPEN QUESTION since 2026-08-15: *"Engagement is
# measured between cycles here, not promoted to a trigger — that is a live question
# for Paul, and not one a check may settle by existing."* He settled it on 08-17,
# after a pickup rendered this loop 🟢 ARMED / "nothing unread could be hers" on a
# window in which she had **4 sessions across 3 active days and viewed 3 of 4
# Perspective offers without tapping one**. Both readings were correct. Only one of
# them was on the board.
#
# ⭐ WHAT CHANGES AND WHAT DOES NOT. The arrival trigger is untouched — `position()`
# is still pure, still arrival-driven, still covered by its own 14 assertions. This
# is an ADDITIONAL gate that can raise ARMED → FIRED, with its own stated reason, so
# a lap fired by her *behaviour* never renders like one fired by her *words*. It can
# only ever raise the state; it can never quiet a FIRED loop.
#
# ⛔ AND IT ASSERTS NOTHING ABOUT HER. Every boundary the engagement reader states
# still binds: a deviceId is a browser bucket, not a person; an event whose first
# firing postdates the window is UNMEASURED and publishes "?", never 0. A signal
# that cannot be measured must never render as a quiet one — that is the whole
# failure this promotion exists to correct, and re-committing it here would be the
# same mistake wearing the new mechanism's clothes.
#
# The three thresholds below are AGENT-PROPOSED and ratified by Paul's pick of the
# option that previewed these exact numbers. They are the first cut, not doctrine —
# tune them from what the next laps show, and record the move in MOM-CYCLE-LOG.md.
VIEWED_NOT_TAKEN = 3    # Perspective offers she SAW and passed over
SESSIONS_QUIET = 3      # app sessions since the lap with no arrival at all
DAYS_SINCE_ANSWER = 21  # her last settled answer, in days


def _engagement_raw():
    """`read-mom-engagement.py --json`, or None. Never raises, never invents."""
    rc, out = _run("read-mom-engagement.py", "--json")
    if rc != 0 or not out:
        return None
    try:
        return json.loads(out)
    except (ValueError, TypeError):
        return None


_AGE_RX = re.compile(r"her last answer\s+\S+\s+\((\d+)d ago\)")


def _days_since_answer():
    """Days since her last settled answer, or None (→ UNMEASURED, never 0).

    ⚠️ THIS PARSES PROSE, and that is a stated weakness, not a hidden one.
    `read-mom-feedback.py` computes this and has no `--json`, so the choices were
    to parse its one line or to re-derive "which records are hers" here — and the
    second is worse than fragile, it is WRONG: this board asserts no attribution
    by design (there is no `hers` bucket; a record with no deviceId is
    `unresolved`). Re-deriving it would mint a second, quieter definition of a
    claim about a person, which is the one thing this loop refuses to do twice.
    So it reuses the tool that already makes the claim on the pickup surface.

    A parse miss returns None and the signal publishes "?" — the failure lands as
    UNMEASURED rather than as a confident zero. The durable fix is a `--json` on
    that tool; until then this is a borrowed reading, not a new source.
    """
    _rc, out = _run("read-mom-feedback.py", "--pickup")
    m = _AGE_RX.search(out or "")
    return int(m.group(1)) if m else None


def _card_modules_on(est=None):
    """C5 3b — does any module that can put a CARD in front of her read ON?
    True/False, or None when the module set is unreadable (→ `?`, never fires).
    Cards come only from `ENTITY_SOURCES` (the cardable domains), so this is
    'is any cardable domain enabled'."""
    on = momlib.enabled_domains(est)
    if on is None:
        return None
    return any(d in on for d in momlib.ENTITY_SOURCES)


def engagement_signals(raw, last_answer_days=None, today=None, card_modules=True):
    """Her BEHAVIOUR as trigger signals. PURE — fixtures drive it in the selftest.

    `card_modules` (C5 3b): whether any card-bearing module is ON at this estate —
    True (count offers), False (off-module offers LEAVE the denominator: a non-tap
    where there are no plants is not a signal about her), None (unreadable → `?`).

    Returns (signals, fired) — `fired` is the subset of names that went off.
    """
    if raw is None:
        return ([{"name": "engagement", "fired": False, "value": "?", "threshold": "—",
                  "detail": "UNMEASURED: could not read /api/metrics"}], [])

    ev = raw.get("events") or {}
    unreadable = set(raw.get("unreadable_zeros") or [])
    sigs = []

    # 1 · She saw the ask and passed over it. The one signal an ARRIVAL trigger can
    #     never produce: declining is invisible to a record that only logs answers.
    if card_modules is None:
        sigs.append({"name": "offers-passed", "fired": False, "value": "?",
                     "threshold": VIEWED_NOT_TAKEN,
                     "detail": "UNMEASURED: the estate's module set is unreadable"})
    elif card_modules is False:
        sigs.append({"name": "offers-passed", "fired": False, "value": "—",
                     "threshold": VIEWED_NOT_TAKEN,
                     "detail": "no card-bearing module is on at this estate — nothing was offered, so nothing was passed"})
    elif {"momqueue_viewed", "momqueue_tapped"} & unreadable:
        sigs.append({"name": "offers-passed", "fired": False, "value": "?",
                     "threshold": VIEWED_NOT_TAKEN,
                     "detail": "UNMEASURED: the event was not live for this whole window"})
    else:
        passed = max(0, ev.get("momqueue_viewed", 0) - ev.get("momqueue_tapped", 0))
        sigs.append({"name": "offers-passed", "fired": passed >= VIEWED_NOT_TAKEN,
                     "value": passed, "threshold": VIEWED_NOT_TAKEN,
                     "detail": "Perspective offers she SAW and did not tap"})

    # 2 · She is in the app and settling nothing. Deliberately NOT "she is absent" —
    #     absence is her prerogative and fires nothing.
    n_sessions = len(raw.get("sessions") or [])
    sigs.append({"name": "sessions-quiet", "fired": n_sessions >= SESSIONS_QUIET,
                 "value": n_sessions, "threshold": SESSIONS_QUIET,
                 "detail": "sessions since the lap — using it, settling nothing"})

    # 3 · The slow clock. A real gate: time passes whether or not anyone works it.
    #     C7 1b: an estate with NO card-bearing module has no contributor loop, so a
    #     silence there is not hers — publish `?`, the file's existing idiom.
    if card_modules is False:
        sigs.append({"name": "answer-age", "fired": False, "value": "?",
                     "threshold": DAYS_SINCE_ANSWER,
                     "detail": "UNMEASURED: no contributor loop at this estate (no card-bearing module is on)"})
    elif last_answer_days is None:
        sigs.append({"name": "answer-age", "fired": False, "value": "?",
                     "threshold": DAYS_SINCE_ANSWER,
                     "detail": "UNMEASURED: no dated answer on record"})
    else:
        sigs.append({"name": "answer-age", "fired": last_answer_days >= DAYS_SINCE_ANSWER,
                     "value": f"{last_answer_days}d", "threshold": f"{DAYS_SINCE_ANSWER}d",
                     "detail": "since her last settled answer"})

    return (sigs, [s["name"] for s in sigs if s["fired"]])


def write_state(at, state, needs_paul, unresolved, bench, signals=None, engagement=()):
    """Publish data/cycle-state.json, the portfolio-standard state artifact.

    WHY A FILE AND NOT A FLAG. The cross-project readers — operating-layer's
    cycle DISPATCH, focus.py's spill-back — must be able to learn this loop's
    state WITHOUT running this loop's code. That is the non-AI-door rule applied
    to a cycle: a state only obtainable by executing a project-local tool is a
    state no portfolio surface will ever show, and this board proved it. It has
    computed ARMED/FIRED correctly since 2026-08-12 and told nobody but the
    person who typed the command.

    Shape is fixed by the registry contract (`page.cycle.state`), matching
    private-financial-dashboard's publisher, the only other one:
        {state, generated_at, generated_by, why, next}
    `why` and `next` are prose for a human; `state` is the field machines read.

    generated_at is LOCAL wall-clock ISO, matching the existing publisher. A
    reader that treats a missing or unparseable artifact as RESTING would defeat
    the point, so the readers fail closed on both — see
    field_log.cycle_published_state.
    """
    if state == "FIRED":
        if needs_paul:
            why = f"leg {at} — the return leg is owed, or the served queue is wrong"
            nxt = "run /mom-cycle: the return leg is a Paul gate"
        else:
            why = (f"leg {at} — {unresolved} unresolved arrival(s) nobody has read yet")
            nxt = "run /mom-cycle beat 1 (READ) — until someone looks, whose it was is unknown"
    elif engagement:
        # Fired by BEHAVIOUR, not by an arrival — and it says so, because the two
        # mean different things and want different opening moves. An arrival says
        # *read what she sent*; this says *she saw the ask and passed over it*.
        why = (f"leg {at} — nothing unread, but her ENGAGEMENT fired: "
               + ", ".join(engagement))
        nxt = "run /mom-cycle — she is using the app and declining the asks; the ask design is the work"
    else:
        why = f"leg {at} — monitor live, nothing unread could be hers"
        if bench:
            why += f" ({bench} bench arrival(s), not hers)"
        nxt = None
    doc = {
        "state": state,
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "generated_by": "Tate-Tracker/tools/mom-cycle-status.py --write-state",
        "why": why,
        "next": nxt,
        "at_leg": at,
        "needs_paul": needs_paul,
        "unresolved_arrivals": unresolved,
        "signals": signals or [],
    }
    # ⭐ THE LAP CENSUS — added 2026-09-01 after a peer session measured that
    # `ecosystem-probe.py` returned UNKNOWN for this loop: it publishes neither
    # `lap_count` nor `last_lap`, so mom lap 7 CLOSED and lap 7 OPEN-AT-LEG-6 were
    # indistinguishable to every portfolio surface, and the closure rested entirely
    # on a `#` heading. That is the non-AI-door rule failing in the small: a fact
    # only a human reading prose can establish is a fact no machine can check.
    # ⛔ Read from an explicit ENUM (`momlib.lap_outcomes`), never from the
    # heading's prose — lap 5's heading said `🔓 OPEN AT LEG 6` for three days
    # after it closed, and lap 7's says "CLOSED, with leg 6 DELIBERATELY
    # UNCROSSED". A substring match would be wrong on both. An unmarked lap
    # publishes `unknown`, never a guess.
    try:
        lap_count, last_lap = momlib.lap_state()
        doc["lap_count"] = lap_count
        doc["last_lap"] = last_lap
    except Exception as exc:                       # noqa: BLE001
        doc["lap_count"] = None                    # UNMEASURED, never 0
        doc["last_lap"] = {"outcome": "unknown",
                           "outcome_note": f"lap census unreadable: {type(exc).__name__}"}
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, STATE_PATH)                    # atomic; a torn read reads FIRED-less
    print(f"published {STATE_PATH} — state {state} · {why}")
    return 0


def _print_engagement():
    """⭐ ARMED must never be read as 'she is not using the app' `[paul-stated 2026-08-15]`.

    This board says *"nothing unread could be hers"* — a true statement about the
    ARRIVAL record and a false one about the app. On 2026-08-15 it read 🟢 ARMED
    while her device had 3 sessions, 2 jump-strip taps and 2 card opens since lap 3.
    Paul: *"the false signal of her not responding to any of the cards means she's
    not using the app. But that's just because that's the only thing we're checking."*

    So the board carries the between-lap engagement line beside the arrival state.
    It is INFORMATIONAL — it does not move a leg, does not set FIRED, and does not
    change what triggers a lap. Best-effort by design: a failed read prints as a
    failed read, never as a zero, because a silent zero here is the exact defect.
    """
    try:
        _spec = importlib.util.spec_from_file_location(
            "engagement", os.path.join(HERE, "read-mom-engagement.py"))
        eng = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(eng)
        lap = eng.last_lap()
        hers = eng.her_devices()
        if not hers:
            return
        start = lap[1] if lap else None
        if not start:
            return
        # ⭐ Pass the close INSTANT through (2026-09-01). Without it the signals
        # count the whole day the lap is dated, so a lap that opened and closed
        # the same day counts its OWN trigger session and publishes FIRED the
        # moment it closes — which then spills rows into Paul's focus queue.
        start_ts = lap[2] if lap and len(lap) > 2 else None
        r = eng.build(start, hers, momlib.resolve_token(), start_ts)
    except Exception as exc:
        print(f"  ⚪️ between-lap engagement — could not read /api/metrics ({type(exc).__name__}).")
        print("       Unknown, NOT zero. python3 tools/read-mom-engagement.py")
        print()
        return

    n_s, n_d = len(r["sessions"]), len(r["active_days"])
    j = sum(r["journal"].get(k, 0) for k in ("field_note_saved", "entry_revisited",
                                             "conversation_turn"))
    icon = "📈" if n_s else "⚪️"
    print(f"  {icon} BETWEEN-LAP USE — since lap {lap[0]} ({lap[1]}): {n_s} session(s) on "
          f"{n_d} day(s),")
    print(f"       {sum(r['cards'].values())} card open(s), {j} journal interaction(s). "
          f"Her device bucket — not a")
    print(f"       claim about who held the phone, and not a trigger. Detail:")
    print("       python3 tools/read-mom-engagement.py")
    print()


def main():
    ap = argparse.ArgumentParser(description="Where is the Mom-feedback loop standing?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true",
                    help="Drive position() with known-answer fixtures and negative controls. "
                         "No network, no git, no Worker.")
    ap.add_argument("--write-state", action="store_true",
                    help="Publish data/cycle-state.json — the portfolio-standard state "
                         "artifact operating-layer's DISPATCH and focus.py's spill-back read. "
                         "This board already KNOWS the state; until now it only ever said so "
                         "to whoever ran it, so a FIRED loop was invisible to every reader "
                         "that was not a human at this terminal.")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    sig = gather()
    at, state, needs_paul = position(sig)
    unresolved, bench = arrival_counts(sig)

    # ⭐ ENGAGEMENT can RAISE the state, never lower it. `position()` stays the
    #   authority on an arrival-fired lap; this only reaches a loop it left ARMED.
    eng_sigs, eng_fired = engagement_signals(_engagement_raw(), _days_since_answer(),
                                             card_modules=_card_modules_on())
    if eng_fired and state != "FIRED":
        state = "FIRED"

    if a.write_state:
        return write_state(at, state, needs_paul, unresolved, bench,
                           signals=eng_sigs, engagement=eng_fired)

    if a.json:
        print(json.dumps({"at_leg": at, "state": state, "needs_paul": needs_paul,
                          "unresolved_arrivals": unresolved, "bench_arrivals": bench,
                          "signals": sig},
                         indent=2, ensure_ascii=False))
        return 1 if needs_paul or not sig["served_queue"]["clean"] else 0

    print()
    print("🌿 Mom-feedback loop — where we are")
    print("   map: MOM-CYCLE-MAP.md · chronicle: MOM-CYCLE-LOG.md · procedure: /mom-cycle")
    print()
    for num, name, is_gate, blurb in LEGS:
        here = "▶" if num == at else " "
        mark = " 👤" if is_gate else ""
        flag = ""
        if num == at and needs_paul:
            flag = "   🔴 NEEDS YOU"
        print(f"  {here} {num} · {name:<8}{mark:<3} {blurb}{flag}")
    print()

    # ⭐ The headline the map asks for. ARMED is the HEALTHY steady state — it is
    # not a lap that is overdue, and it must not look like one.
    if state == "ARMED":
        print("  🟢 ARMED — the monitor is running and nothing unread could be hers.")
        print("       The loop rests. HER input fires it — not a schedule, not this backlog.")
    else:
        print("  🔴 FIRED — something is waiting that is not ours to ignore.")
    print()

    _print_engagement()

    if not sig["served_queue"]["clean"]:
        print("  🔴 SERVED QUEUE — what she is being shown is wrong:")
        for d in sig["served_queue"]["detail"]:
            print(f"       {d}")
    if sig["return_leg"]["owed"]:
        print("  🔴 RETURN LEG — she has given something the ribbon does not cover.")
        print(f"       ({', '.join(sig['return_leg']['why'])})")
        print("       python3 tools/check-mom-ack.py --verbose")
    if unresolved:
        # ⛔ Deliberately NOT "Mom has said something." Unresolved means unresolved.
        print(f"  🔴 UNREAD, ORIGIN UNRESOLVED — {unresolved} arrival(s) from a browser")
        print("       nobody registered. It could be hers; nothing here can say. Go look:")
        for c in (sig.get("arrivals") or {}).get("channels") or []:
            if c["unresolved"]["count"]:
                print(f"       · {c['name']:<16} {c['unresolved']['count']} "
                      f"(newest {momlib.et_str(c['unresolved']['latest'])})")
    if bench:
        # Named, never hidden. A separated count you can still see is not a drop.
        print(f"  ⚙️  {bench} bench arrival(s) — devices YOU registered as your own")
        print("       (people.json `excludeFromEngagement`). Not counted as hers, and not")
        print("       evidence she is quiet either. Clear them once you've looked:")
        for c in (sig.get("arrivals") or {}).get("channels") or []:
            if c["bench"]["count"]:
                print(f"       · python3 tools/check-mom-ack.py --mark-read {c['name']}")
    if not sig["canon_surfaces"]["clean"]:
        print("  🟡 CANON SURFACES — viewer inlines or Guru's digest are behind canon.")
    # ⭐ LEG 0, FAIL CLOSED. A repo this board cannot read is not a quiet repo.
    if not sig["repo"]["ok"]:
        print("  🔴 LEG 0 GUARD — CANNOT READ THIS REPO'S STATE. Treat as UNSAFE.")
        print(f"       {sig['repo']['error']}")
        print("       Nothing below this line is trustworthy; a guard that cannot run")
        print("       must not report clear. python3 tools/guard-concurrent.py status")
    if sig["repo"]["unpushed_commits"]:
        print(f"  🟡 {sig['repo']['unpushed_commits']} unpushed commit(s) — Pages serves "
              "viewer.html; a commit alone never reaches her.")
        print("       Before pushing: python3 tools/guard-concurrent.py before-push")
    if sig["repo"]["dirty_files"]:
        print(f"  🟡 {sig['repo']['dirty_files']} uncommitted file(s) in the working tree.")

    if (not needs_paul and not unresolved and sig["canon_surfaces"]["clean"]
            and sig["repo"]["ok"] and sig["repo"]["unpushed_commits"] == 0):
        print("  🟢 Nothing is waiting on you.")
    print()
    return 1 if needs_paul or not sig["repo"]["ok"] else 0


if __name__ == "__main__":
    sys.exit(main())
