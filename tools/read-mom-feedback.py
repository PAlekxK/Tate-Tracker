#!/usr/bin/env python3
"""Read Mom's confirm-queue answers ("Mama's Perspective") and print what is
actually waiting for Paul.

Answers are captured deterministically by the viewer (her tap + her verbatim
words — no AI) and POSTed to the Worker's /api/feedback with
context.{type:"mom-queue", questionId, kind}. This tool fetches that range,
keeps the mom-queue records, and joins questionId -> the local questions.json so
the output reads like a person, not raw JSON.

⭐ THE PUNCH-LIST IS DERIVED FROM CANON, NOT FROM THE ANSWER RECORD (2026-07-26).
Until today this tool printed every answered confirm under "Ready to fold into
canon" regardless of whether it had already been folded. On 2026-07-26 that
reported three of Mom's answers as pending when all three had been in canon for
days — and the phantom propagated into BACKLOG.md, a user-researcher brief and
three agent reports before anyone checked. The fix is the one in
[[Derive a gate's pending-count; don't list it]]: ask the live state of the
FOLD TARGET, never the existence of an answer. `momlib.question_state()` is now
the single definition; this tool renders it.

Output is four buckets, and only the first is a to-do:
    Ready to fold          — the card is live and canon still says `inferred`
    Retire the card        — canon is already settled; the card is asking for
                             something we know (a stale-premised card)
    Already settled        — folded and retired; shown so you can see it landed
    Can't verify           — no generic probe can see this fold (the 'Annabelle'
                             fold went into the hydrangea ROSTER). Printed as an
                             ASSERTION, labelled as one. An honestly-unsure tool
                             beats a confidently-wrong one — the same doctrine
                             the app itself runs on.

What it does beyond a raw dump:
  • NEW-since-last-seen — a local watermark (.private/mom-feedback-state.json).
    `--mark-reviewed` advances it, but NEVER past an answer that is still
    actionable (see advance_watermark) — that clamp is the fix for the one path
    in this cycle that could silently lose her input.
  • It NEVER writes canon. Promotion stays Paul's hand.
  • `--pickup` — a quiet one-screen mode for the session-start ritual: prints
    only what needs him, or nothing at all (calm, no-noise, matches the app).

Token: FERNWOOD_TOKEN env or .private/fernwood-token (the Worker's SHARED_TOKEN).

Usage:
    python3 tools/read-mom-feedback.py                    # full listing + buckets
    python3 tools/read-mom-feedback.py --pickup           # quiet session-start block
    python3 tools/read-mom-feedback.py --mark-reviewed    # ...then stamp them seen
    python3 tools/read-mom-feedback.py --start 2026-07-01 --end 2026-07-31
    python3 tools/read-mom-feedback.py --all              # include non-mom-queue too
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402

# Re-exported so the tools that `_load()` this file by path keep working.
CONFIRM_LABEL = momlib.CONFIRM_LABEL
REACT_LABEL = momlib.REACT_LABEL
DEFINITIVE = momlib.DEFINITIVE
resolve_token = momlib.resolve_token
_get = momlib._get
flatten = momlib.flatten
strip_md = momlib.strip_md

STATE_FILE = os.path.join(momlib.ROOT, ".private", "mom-feedback-state.json")

# A card in one of these states still wants something from Paul. The watermark
# must never advance past one of them.
ACTIONABLE = ("open", "settled-in-canon", "draft", "unprobeable")

BUCKET_TITLES = [
    ("open", "Ready to fold — canon still says inferred"),
    ("settled-in-canon", "Card is open but canon already settled — retire the card"),
    ("draft", "⚠️  Answer against a card that was never served — check what happened"),
    ("unprobeable", "Can't verify automatically — check by hand"),
    ("resolved", "Already settled — nothing to do"),
]


def load_state():
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, ValueError):
        return {}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def load_questions():
    """questionId -> question dict, from the repo's questions.json (if present)."""
    data = momlib.load_json("questions.json")
    return {q["id"]: q for q in (data.get("questions") or [])
            if isinstance(q, dict) and q.get("id")}


def is_new(rec, watermark):
    ts = rec.get("ts") or ""
    return bool(ts) and (not watermark or ts > watermark)


# ------------------------------------------------------------- the punch-list

def fold_suggestion(q, state, sentiment, note):
    """The concrete next action for one answered card — templated by what the
    card actually folds. It used to say "lock the variety she confirmed" for a
    BLOOM card (run-1 finding #3); the wording now follows `_foldTarget`."""
    probe = state.get("probe") or {}
    where = probe.get("where") or "the mapped entry"
    target = q.get("_foldTarget")
    subject = {"variety": "the variety she confirmed",
               "bloom": "the bloom window she confirmed",
               "confidence": "the identification she confirmed"}.get(target, "what she confirmed")

    if sentiment == "missed":
        if note:
            return f'correct {where} — she says: "{note}"  (an ID change is a judgment call, not a flip)'
        return f"re-check {where} — she marked it not-right and left no detail; worth asking her"
    if state["state"] == "open":
        return f"flip {where}: {probe.get('value','inferred')} → verified  (lock {subject})"
    if state["state"] == "settled-in-canon":
        return (f"{where} is ALREADY verified — the card is stale-premised. "
                f"Retire it (active:false + resolvedAt), don't re-ask her.")
    return None


def classify(mom_records, questions, c):
    """Latest definitive answer per card, joined to its DERIVED state.

    Returns a list of dicts oldest-first, and a dict keyed by bucket."""
    latest = {}
    for r in mom_records:  # oldest-first, so later overwrites earlier
        ctx = r.get("context") or {}
        qid = ctx.get("questionId")
        if qid and r.get("sentiment") in DEFINITIVE:
            latest[qid] = r

    rows = []
    for qid, rec in latest.items():
        q = questions.get(qid)
        if q is None:
            rows.append({"qid": qid, "q": None, "rec": rec,
                         "state": {"state": "unprobeable", "probe": None,
                                   "why": "questionId is not in the current questions.json"},
                         "suggestion": None})
            continue
        st = momlib.question_state(q, c)
        rows.append({"qid": qid, "q": q, "rec": rec, "state": st,
                     "suggestion": fold_suggestion(q, st, rec.get("sentiment"), rec.get("note") or "")})
    rows.sort(key=lambda x: x["rec"].get("ts") or "")

    buckets = {name: [] for name, _ in BUCKET_TITLES}
    for row in rows:
        buckets.setdefault(row["state"]["state"], []).append(row)
    return rows, buckets


def render_buckets(buckets, verbose=True):
    """Print the four buckets. Returns the count of rows that need Paul."""
    todo = 0
    for name, title in BUCKET_TITLES:
        rows = buckets.get(name) or []
        if name in ACTIONABLE:
            todo += len(rows)
        if not rows:
            if verbose and name == "open":
                print(f"{title}\n  • (none)\n")
            continue
        print(title)
        for row in rows:
            qid, st = row["qid"], row["state"]
            when = momlib.et_str(row["rec"].get("ts"), with_time=False)
            if name == "resolved":
                print(f"  • {qid:42s} {st['why']}")
            elif name == "unprobeable":
                # An ASSERTION, labelled as one — never a probe that lies.
                claim = st["why"]
                print(f"  • {qid:42s} {claim}")
                if row["q"] and row["q"].get("resolution"):
                    print(f"    {'':42s} asserted resolution: {strip_md(row['q']['resolution'])}")
            else:
                print(f"  • {qid:42s} (answered {when})")
                if row["suggestion"]:
                    print(f"    ↳ {row['suggestion']}")
        print()
    return todo


# --------------------------------------------------------------- watermark

def advance_watermark(state, mom_records, rows, through=None):
    """Move the read watermark forward WITHOUT ever stepping over an answer that
    still needs Paul.

    THE BUG THIS FIXES (the only data-loss-shaped path in the cycle): the old
    `--mark-reviewed` stamped `max(ts)` across every record in view, and
    `fold-answer.py` called it after folding SOME of them. Fold one card and an
    unrelated, unfolded answer stopped being "new" — permanently. Her input was
    still in the Worker, but nothing would ever surface it again.

    So the ceiling is the OLDEST still-actionable answer: we advance to the
    newest timestamp strictly below it. Everything actionable keeps showing up.
    """
    all_ts = sorted(t for t in ((r.get("ts") or "") for r in mom_records) if t)
    if not all_ts:
        return None, "no answers in range"

    actionable = sorted(
        (r["rec"].get("ts") or "") for r in rows if r["state"]["state"] in ACTIONABLE
    )
    actionable = [t for t in actionable if t]
    ceiling = actionable[0] if actionable else None

    candidates = [t for t in all_ts if (ceiling is None or t < ceiling)]
    if through:
        candidates = [t for t in candidates if t <= through]
    if not candidates:
        why = (f"the oldest answer still needing you ({momlib.et_str(ceiling, False)}) "
               f"is the oldest in range — nothing to stamp")
        return None, why

    new_wm = max(candidates)
    old_wm = state.get("lastReviewedTs") or ""
    if old_wm and new_wm <= old_wm:
        return None, "watermark already at or past that point"
    held = ""
    if ceiling:
        held = (f"; held back at {momlib.et_str(ceiling, False)} so "
                f"{len(actionable)} answer(s) still needing you stay visible")
    return new_wm, f"advanced to {momlib.et_str(new_wm, False)}{held}"


# ----------------------------------------------------------------- rendering

def render_full(mom, other, questions, watermark, show_all, rows, buckets):
    if not mom:
        print("No answers from Mama's Perspective in this range.")
    else:
        new_count = sum(1 for r in mom if is_new(r, watermark))
        header = f"=== Mama's Perspective — {len(mom)} answer(s)"
        header += f", {new_count} new ===" if new_count else " ==="
        print("\n" + header + "\n")
        for r in mom:
            ctx = r.get("context") or {}
            qid = ctx.get("questionId", "?")
            kind = ctx.get("kind", "?")
            q = questions.get(qid)
            prompt = strip_md(q["prompt"]) if q else "(question not in current questions.json)"
            sentiment = r.get("sentiment")
            if kind == "confirm":
                verdict = CONFIRM_LABEL.get(sentiment, sentiment or "—")
            elif kind == "react":
                verdict = REACT_LABEL.get(sentiment, sentiment or "—")
            else:
                verdict = sentiment or "note"
            tag = ""
            if q is not None:
                st = momlib.question_state(q).get("state")
                tag = {"resolved": "  [folded + retired]", "draft": "  [⚠️ never-served draft]",
                       "settled-in-canon": "  [canon already settled]"}.get(st, "")
            note = r.get("note") or ""
            newtag = "🆕 " if is_new(r, watermark) else "   "
            print(f"{newtag}Q ({kind} · {qid}){tag}\n     {prompt}")
            line = f"     → Mom [{verdict}]"
            if note:
                line += f': "{note}"'
            line += f"   ({momlib.et_str(r.get('ts'))})"
            print(line + "\n")

        print("--- What's actually waiting (derived from canon — nothing is auto-written) ---\n")
        render_buckets(buckets)

    if show_all and other:
        print(f"=== Other feedback records — {len(other)} ===\n")
        for r in other:
            ctx = r.get("context") or {}
            print(f"  [{ctx.get('type','general')}] {r.get('sentiment') or '—'}"
                  + (f' — "{r.get("note")}"' if r.get("note") else "")
                  + f"   ({momlib.et_str(r.get('ts'), with_time=False)})")


def render_pickup(mom, questions, watermark, rows, buckets):
    """Quiet session-start block. Two reasons to speak: something NEW arrived,
    or something is genuinely waiting to be folded. Otherwise: silence."""
    new = [r for r in mom if is_new(r, watermark)]
    waiting = [r for r in rows if r["state"]["state"] in ("open", "settled-in-canon", "draft")]
    if not new and not waiting:
        return 0

    if new:
        print(f"🌿 Mama's Perspective — {len(new)} new answer(s) since you last looked:")
        for r in new:
            ctx = r.get("context") or {}
            qid = ctx.get("questionId", "?")
            q = questions.get(qid)
            subj = strip_md(q["prompt"])[:60] + "…" if q else qid
            verdict = CONFIRM_LABEL.get(r.get("sentiment"), r.get("sentiment") or "—")
            note = r.get("note") or ""
            print(f"  • [{verdict}] {subj}" + (f'  —  "{note}"' if note else ""))
        print()

    if waiting:
        print("🌿 Mama's Perspective — waiting on you:")
        for row in waiting:
            print(f"  • {row['qid']}")
            if row["suggestion"]:
                print(f"      ↳ {row['suggestion']}")
        print("  (fold with `python3 tools/fold-answer.py`)")
    return len(new) or len(waiting)


def main():
    ap = argparse.ArgumentParser(description="Read Mom's Mama's-Perspective answers.")
    today = dt.date.today()
    ap.add_argument("--start", default=str(today - dt.timedelta(days=30)), help="YYYY-MM-DD (default: 30 days ago)")
    ap.add_argument("--end", default=str(today), help="YYYY-MM-DD (default: today)")
    ap.add_argument("--all", action="store_true", help="Include non-mom-queue feedback records too")
    ap.add_argument("--pickup", action="store_true", help="Quiet session-start mode: only what needs you; silent otherwise")
    ap.add_argument("--mark-reviewed", action="store_true",
                    help="Stamp reviewed answers as seen (never past one that still needs you)")
    ap.add_argument("--mark-reviewed-through", metavar="TS", default=None,
                    help="Stamp only up to this ISO timestamp (used by fold-answer.py for exactly what it folded)")
    args = ap.parse_args()

    token = resolve_token()
    if not token:
        print("error: no token. Set FERNWOOD_TOKEN, or put it in .private/fernwood-token "
              "(matches the Worker's SHARED_TOKEN).", file=sys.stderr)
        return 2

    if not args.pickup:
        print(f"Reading feedback {args.start} → {args.end} …", file=sys.stderr)
    try:
        data = _get("/api/feedback", token, {"start": args.start, "end": args.end})
    except Exception as e:  # noqa: BLE001
        print(f"error: fetch failed: {e}", file=sys.stderr)
        return 1

    questions = load_questions()
    state = load_state()
    watermark = state.get("lastReviewedTs") or ""

    records = flatten(data)
    mom = [r for r in records if (r.get("context") or {}).get("type") == "mom-queue"]
    other = [r for r in records if (r.get("context") or {}).get("type") != "mom-queue"]

    c = momlib.canon()
    rows, buckets = classify(mom, questions, c)

    if args.pickup:
        render_pickup(mom, questions, watermark, rows, buckets)
    else:
        render_full(mom, other, questions, watermark, args.all, rows, buckets)

    if (args.mark_reviewed or args.mark_reviewed_through) and mom:
        new_wm, why = advance_watermark(state, mom, rows, through=args.mark_reviewed_through)
        if new_wm:
            state["lastReviewedTs"] = new_wm
            state["lastReviewedAt"] = dt.datetime.now().astimezone().isoformat()
            save_state(state)
            print(f"\n✓ Watermark {why}.", file=sys.stderr)
        else:
            print(f"\n· Watermark unchanged — {why}.", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
