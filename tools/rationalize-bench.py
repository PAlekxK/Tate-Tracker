#!/usr/bin/env python3
"""rationalize-bench.py — the bench pass: what should be in front of Mom today?

Built 2026-07-31 (Paul's design, settled in BACKLOG A3 "THE BENCH").

THE PROBLEM THIS SOLVES. `outstanding()` in viewer.html filters active-and-
unanswered and then `.slice(0, MAX_VISIBLE)`. That much already works: answer a
card and the next one in declaration order becomes visible on its own. What did
NOT exist was everything upstream of it —

  1. a BENCH that can reach the queue at all. `outstanding()` filters
     `active !== false`, so a drafted card can never promote itself. That wall
     is Paul's confirm gate and it is correct; what was missing is a way to
     open it deliberately, in batch, rather than by hand-editing JSON.
  2. any RE-RANKING. `questions.json._ordering` states the priority axis in
     prose and nothing applied it.
  3. any re-check of FRESHNESS. `harvest-questions.py` computes "is the window
     open now?" when it drafts a card and never again — so a card's freshness
     was measured once, at birth. See momlib.in_season() for the three live
     instances that motivated this.

PAUL'S TWO DESIGN CALLS (2026-07-31), which this implements literally:

  ① THE CLEAR GATE IS PAUL. A card reaches Mom only after he approves it. The
    approval moves EARLIER rather than away: he clears a batch here, and
    promotion into the visible five is mechanical afterwards. So `--apply`
    will promote ONLY cards carrying an `approvedForServe` stamp, and this
    tool never writes that stamp except under `--approve`, one id at a time,
    run by a human. Multiple supply streams feed the bench (harvest-created,
    surfaced from her own feedback, hand-slotted) and each will grow its own
    approval rules; this gate is the floor under all of them.

  ② FIVE STAYS FIVE, AND VARIETY IS A HARD CONSTRAINT. Paul overruled a
    proposal to hold the visible set below the cap. His reasoning changes the
    algorithm: the five are not a workload, they are a SAMPLE OF WHAT SHE CAN
    INFLUENCE — "keep the variety so that mom can always flip through them and
    get a broad sense of everything that we're asking for and that she can
    influence." So diversity is a FILTER over the ranked list, not a
    tiebreaker. A pure information-value sort would happily stack all five
    slots with bloom cards: that scores well and says exactly the wrong thing.

AI BOUNDARY. This tool reads canon, dates and card metadata. It never reads
Mom's words, never writes a prompt, and never invents a card. Promotion makes
an ALREADY-PAUL-APPROVED card visible; that is scheduling, not authoring.

Run it inside `/mom-cycle`'s rationalization pass, or any time before a reseed.

    python3 tools/rationalize-bench.py                  # report only (default)
    python3 tools/rationalize-bench.py --approve <id>   # Paul clears one card
    python3 tools/rationalize-bench.py --apply          # promote to fill the five
    python3 tools/rationalize-bench.py --bench <id> --because "…"  # take one OFF her surface
    python3 tools/rationalize-bench.py --date 2026-08-01  # ask about another day
"""
import argparse
import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402

QUESTIONS = os.path.join(momlib.ROOT, "questions.json")

# The cap is DERIVED from the viewer, never re-declared here. A second copy of
# MAX_VISIBLE is precisely the kind of duplicate definition momlib exists to
# prevent — and this one would drift silently, because both numbers would look
# equally authoritative.
MAX_VISIBLE_RE = re.compile(r"const\s+MAX_VISIBLE\s*=\s*(\d+)")

# Diversity classes. Derived from fields the cards already carry; nothing new is
# stamped on a card to make this work. `_kind: reflective` is authored by hand,
# `_foldTarget` is set by the harvest — so both are honest signals rather than
# labels invented for this tool.
def card_class(q):
    if q.get("kind") == "open":
        return "standing"
    if q.get("_kind") == "reflective":
        return "preference"
    target = q.get("_foldTarget")
    if target == "bloom":
        return "observation-bloom"
    if target in ("variety", "confidence"):
        return "observation-id"
    return "other"


# No single class may take more than this many of the visible slots while a
# card of another class is available. Two of five leaves room for at least
# three different kinds of ask on screen at once, which is the "broad sense"
# Paul asked for. Fail-open: if nothing else is available the slot is filled
# anyway and the report says so — an empty slot serves her worse than a
# repeated class, and silently under-filling would be the kind of invisible
# policy this repo keeps getting bitten by.
CLASS_CAP = 2

# Priority, per questions.json._ordering: an answer that unblocks a BUILD
# outranks one that fills a canon gap, which outranks a verdict on our own
# guess; preference cards last (no canon target, so no fold path).
CLASS_RANK = {
    "observation-id": 0,     # a gap in canon only she can close
    "observation-bloom": 1,  # a gap in canon, but time-boxed
    "preference": 2,         # no fold path
    "standing": 3,           # the always-on foot-line, never in the sliced five
    "other": 2,
}


def max_visible():
    try:
        with open(momlib.VIEWER, encoding="utf-8") as fh:
            m = MAX_VISIBLE_RE.search(fh.read())
        if m:
            return int(m.group(1)), None
    except OSError as exc:
        return 5, f"could not read viewer.html ({exc}) — assuming 5"
    return 5, "MAX_VISIBLE not found in viewer.html — assuming 5"


def load_questions():
    with open(QUESTIONS, encoding="utf-8") as fh:
        return json.load(fh)


def save_questions(doc):
    # ensure_ascii=False: these files carry em-dashes and curly quotes, and
    # escaping them turns a readable diff into noise.
    with open(QUESTIONS, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def classify(q):
    """visible-eligible | bench | draft | resolved — the SERVE-side state.

    Deliberately NOT a second opinion on momlib.question_state(), which answers
    the CANON-side question ("has this been folded?"). This one answers "may it
    be served?" They are different questions and conflating them is what made
    `active:false` mean three incompatible things.
    """
    if q.get("resolvedAt") or q.get("resolution"):
        return "resolved"
    if q.get("active") is True:
        return "live"
    if q.get("approvedForServe"):
        return "bench"
    return "draft"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true",
                    help="promote approved bench cards to fill the visible set")
    ap.add_argument("--bench", metavar="ID", action="append", default=[],
                    help="take a LIVE card off her surface and back to the bench "
                         "(seasonal hold; requires --because)")
    ap.add_argument("--because", metavar="TEXT",
                    help="why the card is coming off her surface — required by --bench")
    ap.add_argument("--approve", metavar="ID", action="append", default=[],
                    help="stamp Paul's clear-gate on a card (repeatable)")
    ap.add_argument("--date", metavar="YYYY-MM-DD",
                    help="evaluate seasonality for another day (default: today, ET)")
    args = ap.parse_args()

    today = (dt.date.fromisoformat(args.date) if args.date
             else dt.datetime.now(momlib.ET or dt.timezone.utc).date())
    cap, cap_note = max_visible()
    doc = load_questions()
    qs = doc["questions"]
    c = momlib.canon()

    # ---- the INVERSE of the gate -----------------------------------------
    # ⭐ WHY THIS VERB EXISTS (added 2026-08-27, lap 6). `--approve` had no
    #    opposite. A card could be promoted by tool and could only be REMOVED by
    #    hand-editing questions.json — the exact act Leg 7 names as the reason
    #    retirement got skipped ("q-top-categories was answered 08-03 and STILL
    #    BEING SERVED 08-04"). So the tool could name `q-butterfly-weed-bloom` as
    #    ⛔ OUT OF SEASON every single day for 12 days and do nothing about it.
    #    A check that can only ever report is half a control.
    #
    #    BENCH IS NOT RETIRE, and they must not collapse:
    #      · retire  = she answered it; it is settled; it never comes back.
    #                  Lives in read-mom-feedback.py --retire, which REFUSES on a
    #                  card she has not answered. Correct, and it refused here.
    #      · bench   = nobody answered anything. The card is fine; the WORLD moved
    #                  out from under it. It comes back when its window reopens.
    #    Benching keeps `approvedForServe`, so the card lands on the bench rather
    #    than back in the draft pile, and the FILL step already holds out-of-season
    #    bench cards back — so it re-promotes itself, in season, with no human.
    if args.bench:
        if not args.because:
            print("⛔ REFUSED: --bench requires --because.")
            print("   Taking a card off her surface is a decision about what she is asked;")
            print("   no machine can check the reason, so it has to be written down.")
            return 2
        by_id = {q.get("id"): q for q in qs}
        benched = []
        for qid in args.bench:
            q = by_id.get(qid)
            if q is None:
                print(f"✗ no card `{qid}`")
                return 2
            st = classify(q)
            if st == "resolved":
                print(f"✗ `{qid}` is retired — it is not on her surface to take off")
                return 2
            if st != "live":
                print(f"✗ `{qid}` is `{st}`, not live — nothing to bench")
                return 2
            if not q.get("approvedForServe"):
                # It was live, so it WAS cleared — just before this tool existed
                # (2026-07-31) or by hand. Record that honestly rather than
                # stamping today's date as if Paul cleared it today.
                q["approvedForServe"] = "pre-tool"
                q["_approvedForServeNote"] = (
                    "Set when the card was benched: it was live, so it had been cleared, "
                    "but carried no stamp — it predates rationalize-bench.py (2026-07-31). "
                    "NOT a record that Paul approved it on this date.")
            q["active"] = False
            q["benchedAt"] = today.isoformat()
            q["_benchedBecause"] = args.because
            benched.append(qid)
        save_questions(doc)
        print(f"✓ benched ({today}): {', '.join(benched)}")
        print(f"  because: {args.because}")
        print("  They are off her surface and ON THE BENCH — --apply will re-promote")
        print("  them once their window reopens. Re-run check-cards.py, then commit.")
        return 0

    # ---- Paul's gate ------------------------------------------------------
    if args.approve:
        by_id = {q.get("id"): q for q in qs}
        stamped = []
        for qid in args.approve:
            q = by_id.get(qid)
            if q is None:
                print(f"✗ no card `{qid}`")
                return 2
            if classify(q) == "resolved":
                print(f"✗ `{qid}` is retired — approving it would re-serve a settled card")
                return 2
            q["approvedForServe"] = today.isoformat()
            stamped.append(qid)
        save_questions(doc)
        print(f"✓ cleared to serve ({today}): {', '.join(stamped)}")
        print("  They are on the bench now, not in front of her — run --apply to promote.")
        return 0

    # ---- state ------------------------------------------------------------
    state, season = {}, {}
    for q in qs:
        state[q["id"]] = classify(q)
        season[q["id"]] = momlib.in_season(q, c, today)

    live = [q for q in qs if state[q["id"]] == "live"
            and q.get("kind") in ("confirm",)]     # the sliced queue is confirms only
    bench = [q for q in qs if state[q["id"]] == "bench"]
    drafts = [q for q in qs if state[q["id"]] == "draft"]

    print(f"bench pass — {today} (ET) · visible cap {cap}"
          + (f"  ⚠ {cap_note}" if cap_note else ""))

    # ---- 1. STALE ON HER SURFACE RIGHT NOW --------------------------------
    bad_live = [q for q in live
                if season[q["id"]]["verdict"] in ("out-of-season", "review", "dangling")]
    print(f"\n── SERVED NOW ({len(live)} confirm cards live, {min(len(live), cap)} visible)")
    if not bad_live:
        print("   every live card's observable exists today.")
    for q in bad_live:
        s = season[q["id"]]
        mark = {"out-of-season": "⛔ OUT OF SEASON",
                "dangling": "🔴 BROKEN POINTER",
                "review": "⚠ REVIEW"}[s["verdict"]]
        print(f"   {mark}  {q['id']}")
        print(f"      {s['why']}")
        if s["next_open"]:
            print(f"      next window opens {s['next_open']}")

    # ---- 2. cards about to turn over --------------------------------------
    tomorrow = today + dt.timedelta(days=1)
    turning = []
    for q in live + bench:
        a, b = season[q["id"]]["verdict"], momlib.in_season(q, c, tomorrow)["verdict"]
        if a != b:
            turning.append((q["id"], state[q["id"]], a, b))
    if turning:
        print(f"\n── TURNS OVER TOMORROW ({tomorrow})")
        for qid, st, a, b in turning:
            print(f"   {qid}  [{st}]  {a} → {b}")

    # ---- 3. the bench ------------------------------------------------------
    print(f"\n── BENCH ({len(bench)} approved, ready to promote)")
    for q in sorted(bench, key=lambda q: CLASS_RANK[card_class(q)]):
        s = season[q["id"]]
        flag = "" if s["verdict"] in ("in-season", "season-free") else f"  ← {s['verdict']}"
        print(f"   {q['id']:<44} {card_class(q):<18}{flag}")
    if not bench:
        print("   (none — nothing has been cleared to serve)")

    print(f"\n── AWAITING PAUL'S CLEAR GATE ({len(drafts)} drafted, never approved)")
    for q in sorted(drafts, key=lambda q: CLASS_RANK[card_class(q)]):
        s = season[q["id"]]
        flag = "" if s["verdict"] in ("in-season", "season-free") else f"  ← {s['verdict']}"
        print(f"   {q['id']:<44} {card_class(q):<18}{flag}")
        print(f"      approve with: --approve {q['id']}")

    # ---- 4. fill the visible set ------------------------------------------
    open_slots = cap - len(live)
    print(f"\n── FILL  ({len(live)} live / cap {cap} → {max(0, open_slots)} open slot(s))")

    # NOTE: no early `return` below, deliberately. Every path must reach the
    # COVERAGE block — a run that exits before printing its own denominator
    # reads exactly like a run that found nothing wrong, which is the failure
    # mode this repo has a standing rule against. (Caught 2026-07-31, on this
    # tool's first run: the full-queue path skipped coverage entirely.)
    eligible = [q for q in bench
                if season[q["id"]]["verdict"] in ("in-season", "season-free")]
    blocked = [q for q in bench if q not in eligible]
    if blocked:
        print(f"   {len(blocked)} bench card(s) held back as out-of-season: "
              + ", ".join(q["id"] for q in blocked))

    picked = []
    if open_slots <= 0:
        print("   the visible set is full; nothing to promote.")
    elif not eligible:
        print("   nothing eligible to promote"
              + (" (the bench is empty)." if not bench else " — see the held-back list above."))
    else:
        picked = fill(live, eligible, open_slots)

    _coverage(qs, state, season, live, bench, drafts)
    if args.apply and picked:
        ids = {q["id"] for q in picked}
        for q in qs:
            if q["id"] in ids:
                q["active"] = True
                q["promotedAt"] = today.isoformat()
        save_questions(doc)
        print(f"\n✓ promoted {len(ids)} card(s). Re-run check-cards.py, then commit.")
    elif picked:
        print("\n   (report only — re-run with --apply to promote)")
    return 0


def fill(live, eligible, open_slots):
    """Pick which bench cards take the open slots, variety enforced."""
    counts = {}
    for q in live:
        counts[card_class(q)] = counts.get(card_class(q), 0) + 1

    ranked = sorted(eligible, key=lambda q: (CLASS_RANK[card_class(q)], q["id"]))
    picked, deferred_by_diversity = [], []
    for q in ranked:
        if len(picked) >= open_slots:
            break
        k = card_class(q)
        if counts.get(k, 0) >= CLASS_CAP:
            deferred_by_diversity.append(q)
            continue
        picked.append(q)
        counts[k] = counts.get(k, 0) + 1

    # Fail-open: an empty slot serves her worse than a repeated class.
    if len(picked) < open_slots and deferred_by_diversity:
        for q in deferred_by_diversity:
            if len(picked) >= open_slots:
                break
            print(f"   ⚠ diversity cap relaxed for {q['id']} — no other class available")
            picked.append(q)

    for q in picked:
        print(f"   → promote {q['id']:<44} {card_class(q)}")
    held = [q["id"] for q in deferred_by_diversity if q not in picked]
    if held:
        print("   held for variety (would over-fill one class): " + ", ".join(held))
    return picked


def _coverage(qs, state, season, live, bench, drafts):
    # ---- denominator -------------------------------------------------------
    # This repo's standing rule: a tool must report what it could NOT check, or
    # a clean run is indistinguishable from a clean world.
    unknown = [q["id"] for q in qs if state[q["id"]] != "resolved"
               and season[q["id"]]["verdict"] == "unknown"]
    review = [q["id"] for q in qs if state[q["id"]] != "resolved"
              and season[q["id"]]["verdict"] == "review"]
    print("\n── COVERAGE (what this run could NOT decide)")
    print(f"   {len(qs)} cards · {len(live)} live · {len(bench)} bench · "
          f"{len(drafts)} awaiting approval · "
          f"{sum(1 for q in qs if state[q['id']] == 'resolved')} retired")
    print(f"   season-checked deterministically: "
          f"{sum(1 for q in qs if season[q['id']]['verdict'] in ('in-season','out-of-season','season-free'))}"
          f" of {len(qs)}")
    if review:
        print(f"   ⚠ {len(review)} by HEURISTIC, needing a human: {', '.join(review)}")
        print("     (flower wording on a card whose _foldTarget is not `bloom` — the tool")
        print("      raises these and never decides them)")
    if unknown:
        print(f"   ? {len(unknown)} bloom card(s) with no windows in canon: {', '.join(unknown)}")
    dangling = [q["id"] for q in qs if state[q["id"]] != "resolved"
                and season[q["id"]]["verdict"] == "dangling"]
    if dangling:
        print(f"   🔴 {len(dangling)} card(s) with a BROKEN entityRef — fix the pointer "
              f"before trusting any verdict about them: {', '.join(dangling)}")
    print("   NOT CHECKED BY ANY TIER: whether a card that is in season and in canon")
    print("   is a question worth asking her. Seasonality is not relevance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
