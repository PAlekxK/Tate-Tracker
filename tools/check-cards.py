#!/usr/bin/env python3
"""check-cards.py — is what Mom is being SHOWN right now actually correct?

The fourth sibling of check-data-inline / check-digest-fresh / check-mom-ack,
same contract: read-only, exit 0 = say nothing, exit 1 = surface it.

WHY THIS EXISTS (2026-07-26). The loop had a check for the ribbon
(`check-mom-ack.py`) and a check for the fold punch-list
(`read-mom-feedback.py`) — and **nothing at all that verified the queue she is
actually served.** The gap produced two failures in one day:

  1. A backlog row asserted a concrete defect in `q-clematis-variety` that had
     been fixed FIVE MINUTES EARLIER. The row was written from prose, not from
     `questions.json`, and then quoted as fact for the rest of the session.
  2. Asked whether Mom had answered two specific cards, the honest answer
     required four ad-hoc commands across three sources — the feedback API, the
     card file, and canon — reassembled by hand. Anything reassembled by hand
     gets reassembled differently next time.

The class is the one this whole loop keeps re-learning: **a claim about state
that isn't derived from state is a guess with a citation.** This tool derives.

WHAT IT CROSS-CHECKS — three sources that must agree:
    questions.json   what we are SERVING her (active)
    /api/feedback    what she has ANSWERED
    canon            what the record now SAYS (plants.json / weeds.json)

Contradictions it catches, none of which any other check sees:
  🔴 SERVED + ALREADY ANSWERED     a fresh device would re-ask what she settled
  🔴 SERVED + CANON VERIFIED       stale-premised: asking for something we know
  🔴 ANSWERED + CANON UNSETTLED    her answer never reached the record
  🟡 RETIRED + CANON UNSETTLED     resolution claims a fold canon can't confirm
  🟡 ANSWER ON A NEVER-SERVED DRAFT  how did she answer a card we never served?
  🟡 LABEL DEFECTS                 an A-or-B prompt on yes/no labels; a
                                   deferral-shaped "later" ("Ask me later")
                                   instead of a state ("I haven't looked")

That last one is here because it is exactly the defect the stale row named: it
is mechanically checkable, it reaches Mom, and it silently regressed on 3 of 5
live cards while the two flagship cards were fixed.

Usage:
    python3 tools/check-cards.py             # session-start check
    python3 tools/check-cards.py --verbose   # print the full card table
"""
import argparse
import datetime as dt
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402

RED, AMBER, GREEN, DIM = "🔴", "🟡", "🟢", "·"

# An A-or-B prompt needs A-or-B labels. Generic yes/no on a "which is it?"
# question means her real answer only fits in an optional free-text box.
AB_PROMPT = re.compile(r"\bor is it\b|\bwhich (one|of)\b|\bA or B\b|\bor a\b.*\?", re.I)
GENERIC_YES = {"yes", "yes it is", "looks right", "that's right", "correct"}
DEFERRAL_LATER = {"ask me later", "later", "remind me", "skip", "not now"}


def latest_answers(token, days=88):
    """questionId -> latest DEFINITIVE answer record."""
    today = dt.date.today()
    try:
        data = momlib._get("/api/feedback", token,
                           {"start": str(today - dt.timedelta(days=min(days, 88))),
                            "end": str(today)})
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(f"could not read /api/feedback: {e}")
    out = {}
    for r in momlib.flatten(data):
        if momlib.is_instrumentation(r):
            continue
        ctx = r.get("context") or {}
        qid = ctx.get("questionId")
        if qid and r.get("sentiment") in momlib.DEFINITIVE:
            out[qid] = r  # oldest-first, so this keeps the latest
    return out


def label_findings(q):
    """Mechanical defects in what the buttons actually say."""
    out = []
    labels = q.get("labels") or {}
    prompt = momlib.strip_md(q.get("prompt") or "")
    yes = (labels.get("yes") or "").strip()
    later = (labels.get("later") or "").strip()

    if AB_PROMPT.search(prompt) and yes.lower() in GENERIC_YES:
        out.append("an A-or-B question on generic yes/no labels — \"no\" cannot say WHICH")
    if later and later.lower() in DEFERRAL_LATER:
        out.append(f"\"later\" is a deferral ({later!r}), not a state she can be in "
                   f"— prefer \"I haven't looked\"")
    # A free-text card (kind:"open") is a note box, not a yes/no — it has no
    # buttons by design. Flagging it was a false positive on this tool's first
    # run; a check that cries wolf gets ignored, which is the failure it exists
    # to prevent.
    if q.get("active") is True and not labels and q.get("kind") != "open":
        out.append("served with NO labels — falls back to generic yes/no")
    return out


def main():
    ap = argparse.ArgumentParser(description="Does the served card queue match reality?")
    ap.add_argument("--verbose", action="store_true", help="Print every card, not just problems")
    ap.add_argument("--days", type=int, default=88)
    args = ap.parse_args()

    token = momlib.resolve_token()
    if not token:
        print("· check-cards: no token; skipping (local half has nothing to check)", file=sys.stderr)
        return 0
    try:
        answers = latest_answers(token, args.days)
    except RuntimeError as e:
        print(f"· check-cards: {e} — skipping (offline is not a failure)", file=sys.stderr)
        return 0

    questions = (momlib.load_json("questions.json").get("questions") or [])
    c = momlib.canon()
    problems, rows = [], []

    for q in questions:
        qid = q.get("id")
        st = momlib.question_state(q, c)
        ans = answers.get(qid)
        served = q.get("active") is True
        flags = []

        if served and ans:
            flags.append((RED, "SERVED but she ALREADY ANSWERED it "
                               f"({momlib.et_str(ans.get('ts'), False)}) — a fresh device re-asks her"))
        if served and st["state"] == "settled-in-canon":
            flags.append((RED, f"SERVED but canon is already verified — {st['why']}"))
        if ans and st["state"] == "open":
            flags.append((RED, f"she ANSWERED it but canon is still unsettled — {st['why']}"))
        if st["state"] == "resolved" and q.get("_foldTarget"):
            ok, info = momlib.probe_target(q, c)
            if ok and str(info["value"]).lower() != "verified":
                flags.append((AMBER, f"retired as folded, but {info['where']} = "
                                     f"{info['value']!r} — the resolution asserts a fold canon can't confirm"))
        if ans and st["state"] == "draft":
            flags.append((AMBER, "she answered a card that was never served (active:false, no resolvedAt)"))
        for f in label_findings(q):
            # A defect on a card she is SERVED reaches her now; the same defect
            # on an unserved draft is a trap to disarm before it ships.
            flags.append((AMBER if served else DIM, f + ("" if served else "  [draft — not served yet]")))

        rows.append((qid, served, bool(ans), st["state"], flags))
        problems.extend((qid, lvl, msg) for lvl, msg in flags)

    served_n = sum(1 for r in rows if r[1])
    answered_n = sum(1 for r in rows if r[2])

    if not problems and not args.verbose:
        return 0

    print(f"\n🃏 Mama's Perspective — the served queue vs. reality")
    print(f"   {len(rows)} card(s) · {served_n} being served · {answered_n} answered "
          f"· cross-checked against questions.json + /api/feedback + canon\n")

    if args.verbose:
        print(f"   {'card':42s} {'served':7s} {'answered':9s} canon-state")
        for qid, served, answered, state, _ in rows:
            print(f"   {qid:42s} {'yes' if served else '—':7s} "
                  f"{'yes' if answered else '—':9s} {state}")
        print()

    if problems:
        print("   Contradictions:")
        for qid, lvl, msg in problems:
            print(f"     {lvl} {qid}")
            print(f"        {msg}")
        print()
        print("   ↳ Card wording reaches Mom — human-confirmed before anything ships.")
        return 1

    print(f"   {GREEN} No contradictions: nothing served is already answered or already settled,\n"
          f"      every answer reached the record, and no label defects.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
