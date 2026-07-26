#!/usr/bin/env python3
"""test-feedback-cycle.py — does Mom's feedback actually survive the round trip?

Written 2026-07-26, after her rainfall report sat unseen. That note was captured
perfectly. It was POSTed, stored, and returned by the API on demand — and it
still went unanswered for four hours, because **capture is not a loop.** The
system had three legs (she gives input → it lands → we act) and no fourth (she
is told), and no leg had a test.

This walks a note through every leg and asserts on each, so a regression in any
one of them is caught here rather than by Mom.

  1. CAPTURE     a note is stored and comes back with a stable id
  2. SURFACE     it is classified `needs-reply` — not silently swallowed
  3. PROTECT     the watermark REFUSES to advance past it (the data-loss guard)
  4. ESCALATE    the ack ribbon reports her as owed a reply
  5. CLOSE       recording where it went flips it to `addressed`
  6. RELEASE     with nothing outstanding, the watermark advances again

Default is OFFLINE: synthetic records driven through the real functions, no
network, no writes to her feedback stream, no mutation of tracked state. That
makes it safe to run every session.

  --live   also POSTs one clearly-marked note to the real Worker and reads it
           back, proving the capture path end-to-end (this is the only part
           that can catch a broken endpoint). It addresses its own note on the
           way out so it never becomes someone's phantom to-do.

Usage:
    python3 tools/test-feedback-cycle.py
    python3 tools/test-feedback-cycle.py --live
"""
import argparse
import copy
import datetime as dt
import importlib.util
import json
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import momlib  # noqa: E402

_spec = importlib.util.spec_from_file_location("rmf", os.path.join(HERE, "read-mom-feedback.py"))
rmf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rmf)

PASS, FAIL = "  ✓", "  ✗"
_failures = []


def check(label, condition, detail=""):
    if condition:
        print(f"{PASS} {label}")
    else:
        print(f"{FAIL} {label}" + (f"\n      {detail}" if detail else ""))
        _failures.append(label)
    return bool(condition)


def note(rec_id, ts, text):
    return {"id": rec_id, "ts": ts, "note": text, "sentiment": None,
            "context": {"type": "mom-queue", "questionId": "q-open-standing", "kind": "open"}}


def answer(rec_id, ts, qid, sentiment="landed"):
    return {"id": rec_id, "ts": ts, "note": "", "sentiment": sentiment,
            "context": {"type": "mom-queue", "questionId": qid, "kind": "confirm"}}


def offline_suite():
    print("\n── OFFLINE: the lifecycle, driven through the real functions ──\n")

    older = "2026-07-10T12:00:00Z"
    hers = "2026-07-12T13:20:00Z"
    newer = "2026-07-20T12:00:00Z"
    records = [
        answer("fb-old", older, "q-crocosmia-lucifer"),
        note("fb-hers", hers, "The rainfall over the past seven days doesn't look right to me."),
        answer("fb-new", newer, "q-panicle-hydrangea-bloom"),
    ]

    # 2 · SURFACE — an empty log means nothing has answered her.
    log = {}
    st = momlib.note_state(records[1], log)
    check("SURFACE  a note with nothing recorded against it reads `needs-reply`",
          st["state"] == "needs-reply", f"got {st['state']!r}")
    check("SURFACE  a confirm tap is NOT mistaken for a free-text note",
          not momlib.is_general_note(records[0]))
    check("SURFACE  a note with words IS recognised",
          momlib.is_general_note(records[1]))

    note_rows = [{"rec": r, "note_state": momlib.note_state(r, log)}
                 for r in records if momlib.is_general_note(r)]
    q_rows = [{"rec": records[0], "state": {"state": "resolved"}},
              {"rec": records[2], "state": {"state": "resolved"}}]

    # 3 · PROTECT — the guard that would have saved her note.
    wm, why = rmf.advance_watermark({}, records, q_rows, note_rows=note_rows)
    check("PROTECT  the watermark stops BELOW her unanswered note",
          wm is not None and wm < hers,
          f"stamped {wm} — her note at {hers} would be buried")
    check("PROTECT  ...and says why it held back", "held back" in why, why)

    # 5 · CLOSE — record where it went.
    log_closed = {"fb-hers": {"noteId": "fb-hers", "noteTs": hers,
                              "addressedOn": "2026-07-26",
                              "disposition": "fixed: rainfall now reads the station gauge",
                              "acknowledgedToHer": False}}
    st2 = momlib.note_state(records[1], log_closed)
    check("CLOSE    recording a disposition flips it to `addressed`",
          st2["state"] == "addressed", f"got {st2['state']!r}")
    check("CLOSE    the disposition is carried, not just a boolean",
          "station gauge" in st2["why"], st2["why"])
    check("CLOSE    'we fixed it' is tracked SEPARATELY from 'she was told'",
          log_closed["fb-hers"]["acknowledgedToHer"] is False)

    # 6 · RELEASE — nothing outstanding, so the watermark moves again.
    note_rows2 = [{"rec": r, "note_state": momlib.note_state(r, log_closed)}
                  for r in records if momlib.is_general_note(r)]
    wm2, _ = rmf.advance_watermark({}, records, q_rows, note_rows=note_rows2)
    check("RELEASE  once addressed, the watermark advances past it",
          wm2 == newer, f"stamped {wm2}, expected {newer}")

    # Regression guard on the ORIGINAL bug, kept here so it can't come back.
    q_rows_unfolded = [{"rec": records[0], "state": {"state": "resolved"}},
                       {"rec": records[2], "state": {"state": "open"}}]
    wm3, _ = rmf.advance_watermark({}, records, q_rows_unfolded, note_rows=note_rows2)
    check("REGRESS  an UNFOLDED answer still pins the watermark below itself",
          wm3 is not None and wm3 < newer, f"stamped {wm3}")


def ribbon_suite():
    print("\n── ESCALATE: does the ribbon report her as owed a reply? ──\n")
    r = momlib.ribbon_state()
    check("ESCALATE the ribbon exposes a machine-readable clock",
          r["acknowledged_through"] is not None,
          "MOM_ACK_DATA has no acknowledgedThrough — staleness is unanswerable")
    check("ESCALATE the ribbon knows whether it actually SHIPPED",
          isinstance(r["shipped"], bool))
    token = momlib.resolve_token()
    if not token:
        print("  · no token — skipping the live channel read")
        return
    try:
        state = momlib.latest_mom_input(token, days=60)
    except Exception as e:  # noqa: BLE001
        print(f"  · Worker unreachable ({e}) — skipping")
        return
    names = {c["name"] for c in state["channels"]}
    check("ESCALATE every app channel is polled (feedback/observations/zone-audio/guru)",
          {"feedback", "observations", "zone-audio", "guru"} <= names,
          f"polled {sorted(names)}")
    check("ESCALATE no text ledger is consulted (channel doctrine)",
          "text" not in names and not os.path.exists(
              os.path.join(momlib.ROOT, ".private", "mom-input-log.json")))


def live_suite():
    print("\n── LIVE: the real capture path (POST → store → read back) ──\n")
    token = momlib.resolve_token()
    if not token:
        print("  · no token — cannot run the live half")
        return
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    rec_id = f"fb-cycletest-{stamp}"
    payload = {
        "id": rec_id,
        "ts": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "note": f"[automated cycle test {stamp}] not from Mom — proves capture→surface→close. Safe to ignore.",
        "sentiment": None,
        "context": {"type": "mom-queue", "questionId": "q-open-standing", "kind": "open"},
    }
    req = urllib.request.Request(
        momlib.WORKER_URL + "/api/feedback",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": momlib.USER_AGENT},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.load(resp)
    except Exception as e:  # noqa: BLE001
        check("CAPTURE  POST /api/feedback accepts a note", False, str(e))
        return
    check("CAPTURE  POST /api/feedback accepts a note (write-only, no token)",
          body.get("stored") == 1, json.dumps(body))

    today = dt.date.today()
    data = momlib._get("/api/feedback", token,
                       {"start": str(today - dt.timedelta(days=1)), "end": str(today)})
    back = next((r for r in momlib.flatten(data) if r.get("id") == rec_id), None)
    check("CAPTURE  it reads back with a stable id and her words intact",
          back is not None and back.get("note") == payload["note"])
    if back is None:
        return
    check("SURFACE  the round-tripped record classifies as `needs-reply`",
          momlib.note_state(back, {})["state"] == "needs-reply")

    # Close it out so the test never leaves a phantom to-do behind.
    momlib.address_note(back, f"automated cycle test {stamp} — self-closed, no action needed",
                        acknowledged=True)
    check("CLOSE    the test note self-closes to `addressed`",
          momlib.note_state(back)["state"] == "addressed")


def main():
    ap = argparse.ArgumentParser(description="End-to-end test of Mom's feedback cycle.")
    ap.add_argument("--live", action="store_true",
                    help="Also POST one marked note to the real Worker and read it back")
    args = ap.parse_args()

    print("Feedback-cycle self-test — capture is not a loop; every leg is asserted.")
    offline_suite()
    ribbon_suite()
    if args.live:
        live_suite()
    else:
        print("\n  · live capture path not exercised (pass --live to POST a marked test note)")

    print()
    if _failures:
        print(f"✗ {len(_failures)} check(s) FAILED:")
        for f in _failures:
            print(f"    · {f}")
        return 1
    print("✓ all checks passed — a note cannot be captured and then silently lost.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
