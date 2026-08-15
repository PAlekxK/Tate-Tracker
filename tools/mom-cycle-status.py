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
the board were `d-avslqpyd-m72qxt1s-mpeuqnyg`, a device carrying
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
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

spec = importlib.util.spec_from_file_location("momlib", os.path.join(HERE, "momlib.py"))
momlib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(momlib)

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
    try:
        head = subprocess.run(["git", "log", "--oneline", "-1"], cwd=ROOT,
                              capture_output=True, text=True, timeout=20).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                               capture_output=True, text=True, timeout=20).stdout.strip()
        unpushed = subprocess.run(["git", "log", "--oneline", "origin/main..HEAD"], cwd=ROOT,
                                  capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        head, dirty, unpushed = "", "", ""
    sig["repo"] = {
        "source": "git",
        "head": head,
        "dirty_files": len([l for l in dirty.splitlines() if l.strip()]),
        "unpushed_commits": len([l for l in unpushed.splitlines() if l.strip()]),
    }
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
        "repo": {"head": "", "dirty_files": 0, "unpushed_commits": 0},
    }


def selftest():
    fails = []

    def check(label, got, want):
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
    print("✅ mom-cycle-status selftest — 14 assertions, incl. 3 negative controls.")
    return 0


STATE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "data", "cycle-state.json")


def write_state(at, state, needs_paul, unresolved, bench):
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
    }
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, STATE_PATH)                    # atomic; a torn read reads FIRED-less
    print(f"published {STATE_PATH} — state {state} · {why}")
    return 0


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

    if a.write_state:
        return write_state(at, state, needs_paul, unresolved, bench)

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
    if sig["repo"]["unpushed_commits"]:
        print(f"  🟡 {sig['repo']['unpushed_commits']} unpushed commit(s) — Pages serves "
              "viewer.html; a commit alone never reaches her.")
    if sig["repo"]["dirty_files"]:
        print(f"  🟡 {sig['repo']['dirty_files']} uncommitted file(s) in the working tree.")

    if (not needs_paul and not unresolved and sig["canon_surfaces"]["clean"]
            and not sig["repo"]["unpushed_commits"]):
        print("  🟢 Nothing is waiting on you.")
    print()
    return 1 if needs_paul else 0


if __name__ == "__main__":
    sys.exit(main())
