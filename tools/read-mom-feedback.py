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
                             the app itself runs on. It is also the ONE bucket
                             that cannot clear itself, so every place it appears
                             names the action that clears it — retire the card —
                             or it holds the watermark indefinitely.

What it does beyond a raw dump:
  • NEW-since-last-seen — a local watermark (.private/mom-feedback-state.json).
    `--mark-reviewed` advances it, but NEVER past an answer that is still
    actionable (see advance_watermark) — that clamp is the fix for the one path
    in this cycle that could silently lose her input.
  • It NEVER writes canon. Promotion stays Paul's hand.
  • `--pickup` — a quiet one-screen mode for the session-start ritual: prints
    only what needs him, or nothing at all (calm, no-noise, matches the app).

⭐⭐ THE COUNTER READS EVERY CHANNEL, NOT JUST THIS ONE (M1, `paul-stated`
2026-09-01): *"The feedback reader definitely needs to look in observations
slash guru. Anywhere where we can get feedback, the feedback reader needs to
look."*

Measured the moment it mattered. At 11:12 AM ET Mom authored four acts — a
request to add the refrigerator, plus three specs — through the Guru. Minutes
later this tool printed `her last answer 2026-08-20 (12d ago)` and nothing else.
**Green. Twelve days quiet. While a live request sat unread.** This file reads
`/api/feedback`; `observations`, `guru` and `zone-audio` were structurally
invisible to it — and this line is the door the session-start ritual actually
renders for *"is anything pending from Mom?"*.

So `render_counter` now carries a SECOND line derived from
`momlib.undispositioned_arrivals()` — the same definition
`check-arrival-dispositions.py` reads, not a second one. Three properties it
must keep:
  · **The answer-age clause names its own scope.** It says "her last CARD
    answer", because that is all it ever measured. A number that cannot see a
    channel must not be phrased as though it can.
  · **An unreachable channel prints UNMEASURED, never 0.** A fetch failure that
    degrades to a green line is the exact defect this fixes, wearing a different
    hat — `[[reference_match_payload_not_container]]`.
  · **It asserts no attribution.** `owed_to_mom` (unresolved) and `bench-unheard`
    (a device Paul registered as his) are counted and printed apart, because a
    bench arrival still needs a look but is not a debt to Mom.

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
#
# ⚠️ `unprobeable` is the one with no SELF-clearing path (audit finding, 2026-07-26).
# The other three leave this set on their own once canon moves — a fold flips
# `inferred`→`verified`, a retire sets `resolvedAt`. `unprobeable` means no probe
# can ever see the fold, so canon can never answer "was this handled?": the card
# sits at the watermark ceiling until a HUMAN retires it. A reflective card
# (`_kind:reflective`, no `_foldTarget` by design — momlib.probe_target) is the
# permanent case. It stays ACTIONABLE — burying her preference would be the
# silent-loss bug this clamp exists to prevent — so the fix is to NAME the
# clearing action everywhere it surfaces, which is what fold_suggestion(),
# render_buckets(), render_pickup() and advance_watermark() now do.
ACTIONABLE = ("open", "settled-in-canon", "draft", "unprobeable")

# The one action that releases an `unprobeable` card. Written once, printed
# wherever the card shows, so the escape hatch is never a thing you had to
# already know.
RETIRE_ACTION = ("retire the card (`active:false` + `resolvedAt` in questions.json) "
                 "once you've handled it — until then it holds the watermark and "
                 "every later answer keeps reading as new")

NOTE_BUCKET_TITLES = [
    ("needs-reply", "💬 She told us something and nothing has answered it yet"),
    ("addressed", "💬 Notes already addressed"),
]

BUCKET_TITLES = [
    ("open", "Ready to fold — canon still says inferred"),
    ("settled-in-canon", "Card is open but canon already settled — retire the card"),
    ("draft", "⚠️  Answer against a card that was never served — check what happened"),
    # "check by hand" read as *inspect* and left the clearing action undiscoverable,
    # so these pinned the watermark indefinitely. The title now says what to DO.
    ("unprobeable", "Can't verify automatically — handle by hand, then RETIRE the card"),
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


def _days_since(iso):
    """Whole days between an ISO timestamp and now. None if unparseable."""
    if not iso:
        return None
    try:
        then = dt.datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
    except ValueError:
        return None
    if then.tzinfo is None:
        then = then.astimezone()
    return max(0, (dt.datetime.now().astimezone() - then).days)


def render_counter(state, mom, window_days):
    """ONE line, printed at EVERY pickup — including the quiet ones.

    Paul's call 2026-08-02, replacing the unconfigured email path on
    mom-queue-watch: *"anytime we work within the Fernwood repository, we should
    check and have, like, a counter that tells us when's the last time — a
    reminder to nudge us to check for Mom's feedback. That's just simpler than
    trying to do something super automated."*

    Why a counter and not silence: a quiet watcher and a dead one look
    IDENTICAL in a log, and `--pickup` was silent on the happy path — so
    "nothing new" and "nobody has looked in nine days" printed the same thing
    (nothing). The counter is the cheap instrument that tells those apart, and
    it costs one line. It measures the gap between sessions that actually
    looked, which is why the stamp is written on every run.
    """
    since_check = _days_since(state.get("lastCheckedAt"))
    if since_check is None:
        when = "never checked before (first run — the counter starts today)"
    elif since_check == 0:
        when = "last checked today"
    elif since_check == 1:
        when = "last checked yesterday"
    else:
        when = f"last checked {since_check} days ago"

    # ⚠️ SCOPED WORDING IS LOAD-BEARING (M1, 2026-09-01). This value is derived
    # from /api/feedback alone, so it may only speak about CARD answers. It once
    # read "her last answer 12d ago" over a live Guru request — true of what it
    # measured, and false as the sentence a reader took away.
    newest = max((r.get("ts") or "") for r in mom) if mom else ""
    if newest:
        d = _days_since(newest)
        hers = (f"her last card answer {momlib.et_str(newest, with_time=False)}"
                + (f" ({d}d ago)" if d is not None else ""))
    else:
        hers = f"no card answers from her in the last {window_days} days"

    # Loud only when the gap is real. A nudge that fires every day is furniture.
    flag = "⚠️ " if (since_check is not None and since_check >= 7) else ""
    print(f"{flag}🌿 Mom-check — {when} · {hers}.")


CHANNEL_LABEL = {
    "feedback": "cards",
    "observations": "observations",
    "guru": "Guru",
    "zone-audio": "voice",
}


def render_channels(token, days=60):
    """The SECOND counter line: what is waiting on EVERY channel she can reach.

    This is the M1 fix. `render_counter` above can only ever speak about
    /api/feedback; this speaks about all of them, and it is deliberately built
    on `momlib.undispositioned_arrivals()` rather than a fresh sweep — one
    definition of "nobody has looked at this yet", N readers. A second, quieter
    definition living here is how the two boards would come to disagree.

    Returns the number of arrivals owed to Mom (for the caller's exit posture).
    """
    try:
        res = momlib.undispositioned_arrivals(token, days=days)
    except Exception as e:  # noqa: BLE001
        # Never degrade to a green line. An unreadable sweep is a LOUD unknown.
        print(f"⚠️  🗂  channels UNMEASURED — the arrival sweep failed ({e}). "
              f"This line cannot say the channels are quiet; it can only say it did not look.")
        return None

    items, errors = res.get("items") or [], res.get("errors") or []

    owed, bench = {}, {}
    for it in items:
        bucket = owed if it.get("owed_to_mom") else bench
        bucket[it["channel"]] = bucket.get(it["channel"], 0) + 1

    def _fmt(counts):
        return ", ".join(f"{n} {CHANNEL_LABEL.get(ch, ch)}"
                         for ch, n in sorted(counts.items(), key=lambda kv: -kv[1]))

    parts = []
    if owed:
        parts.append(f"{sum(owed.values())} undispositioned ({_fmt(owed)})")
    if bench:
        parts.append(f"{sum(bench.values())} bench-unheard ({_fmt(bench)})")

    if parts:
        print(f"⚠️  🗂  channels — {' · '.join(parts)}. "
              f"Each needs its OWN disposition: "
              f"python3 tools/check-arrival-dispositions.py")
    elif errors:
        pass  # the errors line below is the whole story; don't also print green
    else:
        print("🗂  channels — every arrival on cards, observations, Guru and "
              "voice carries a disposition.")

    if errors:
        # A channel we could not reach is UNMEASURED. Printing nothing here is
        # what let a green line stand over an unreachable channel.
        print(f"⚠️  🗂  UNMEASURED: {', '.join(sorted(errors))} — "
              f"could not be read, so this line does not cover "
              f"{'it' if len(errors) == 1 else 'them'}.")

    return sum(owed.values())


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

    # An unprobeable card can never clear itself — say so, and say what does.
    # Checked FIRST because there is no `where` to correct and no flag to flip:
    # the generic "correct <the mapped entry>" line below would be a probe that
    # lies, which is the one thing this tool refuses to do.
    if state["state"] == "unprobeable":
        lead = ("she gave you a preference here, never a canon fold"
                if q.get("_kind") == "reflective"
                else "no generic probe can see this fold")
        note_part = f'  she says: "{note}"' if note else ""
        return f"{lead} — {RETIRE_ACTION}.{note_part}"
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


def classify_notes(records):
    """Her free-text notes, with the one thing they never had: a state.

    A note is `needs-reply` until someone records where it went. That state is
    ACTIONABLE, so the watermark can never bury an unanswered note again — which
    is exactly what happened to her 2026-07-26 rainfall report.
    """
    log = momlib.load_feedback_log()
    rows = []
    for r in records:
        if not momlib.is_general_note(r):
            continue
        rows.append({"rec": r, "note_state": momlib.note_state(r, log)})
    rows.sort(key=lambda x: x["rec"].get("ts") or "")
    buckets = {name: [] for name, _ in NOTE_BUCKET_TITLES}
    for row in rows:
        buckets.setdefault(row["note_state"]["state"], []).append(row)
    return rows, buckets


def render_note_buckets(note_buckets):
    for name, title in NOTE_BUCKET_TITLES:
        rows = note_buckets.get(name) or []
        if not rows:
            continue
        print(title)
        for row in rows:
            rec = row["rec"]
            when = momlib.et_str(rec.get("ts"))
            text = (rec.get("note") or "").strip().replace("\n", " ")
            if name == "needs-reply":
                print(f"  • {rec.get('id')}   ({when})")
                print(f"    \"{text[:180]}{'…' if len(text) > 180 else ''}\"")
                print(f"    ↳ once you've acted, record where it went:")
                print(f"        python3 tools/read-mom-feedback.py --address {rec.get('id')} \\")
                print(f"            --as \"filed as BACKLOG <row> / fixed in <commit>\"")
            else:
                print(f"  • {rec.get('id'):24s} {row['note_state']['why']}")
        print()


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
                if row["suggestion"]:
                    print(f"    ↳ {row['suggestion']}")
            else:
                print(f"  • {qid:42s} (answered {when})")
                if row["suggestion"]:
                    print(f"    ↳ {row['suggestion']}")
        print()
    return todo


# --------------------------------------------------------------- watermark

def advance_watermark(state, mom_records, rows, through=None, note_rows=None):
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

    # (ts, what it is, its state) so the held-back message can NAME the card
    # holding the ceiling — otherwise an `unprobeable` card that can never clear
    # itself looks identical to a fold you simply haven't done yet.
    actionable = [(r["rec"].get("ts") or "", r.get("qid") or "?", r["state"]["state"])
                  for r in rows if r["state"]["state"] in ACTIONABLE]
    # An unanswered free-text note is actionable too. Without this, a note with
    # no probeable target — her rainfall bug report — ages out silently.
    actionable += [(r["rec"].get("ts") or "", r["rec"].get("id") or "?", "needs-reply")
                   for r in (note_rows or []) if r["note_state"]["state"] == "needs-reply"]
    actionable = sorted(t for t in actionable if t[0])
    holder = actionable[0] if actionable else None
    ceiling = holder[0] if holder else None

    candidates = [t for t in all_ts if (ceiling is None or t < ceiling)]
    if through:
        candidates = [t for t in candidates if t <= through]
    if not candidates:
        why = (f"the oldest answer still needing you ({holder[1]}, "
               f"{momlib.et_str(ceiling, False)}) is the oldest in range — nothing to stamp")
        if holder[2] == "unprobeable":
            why += f"; it can NEVER clear itself — {RETIRE_ACTION}"
        return None, why

    new_wm = max(candidates)
    old_wm = state.get("lastReviewedTs") or ""
    if old_wm and new_wm <= old_wm:
        return None, "watermark already at or past that point"
    held = ""
    if ceiling:
        held = (f"; held back at {momlib.et_str(ceiling, False)} by {holder[1]} so "
                f"{len(actionable)} answer(s) still needing you stay visible")
        if holder[2] == "unprobeable":
            held += (f" — {holder[1]} can NEVER clear itself (nothing in canon can "
                     f"confirm it); {RETIRE_ACTION}")
    return new_wm, f"advanced to {momlib.et_str(new_wm, False)}{held}"


# ----------------------------------------------------------------- rendering

def render_full(mom, other, questions, watermark, show_all, rows, buckets, note_buckets):
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
        render_note_buckets(note_buckets)

    if show_all and other:
        print(f"=== Other feedback records — {len(other)} ===\n")
        for r in other:
            ctx = r.get("context") or {}
            print(f"  [{ctx.get('type','general')}] {r.get('sentiment') or '—'}"
                  + (f' — "{r.get("note")}"' if r.get("note") else "")
                  + f"   ({momlib.et_str(r.get('ts'), with_time=False)})")


def render_pickup(mom, questions, watermark, rows, buckets, note_buckets):
    """Quiet session-start block. Three reasons to speak: something NEW arrived,
    something is waiting to be folded, or she said something nobody has answered.
    Otherwise: silence."""
    new = [r for r in mom if is_new(r, watermark)]
    waiting = [r for r in rows if r["state"]["state"] in ("open", "settled-in-canon", "draft")]
    # `unprobeable` was ACTIONABLE — it held the watermark — and yet it was the one
    # actionable state this quiet mode never mentioned. So the card doing the
    # holding was invisible in the block Paul actually reads, and the only symptom
    # was every older answer re-reading as new, forever, with no stated cause.
    pinning = [r for r in rows if r["state"]["state"] == "unprobeable"]
    unanswered = note_buckets.get("needs-reply") or []
    if not new and not waiting and not pinning and not unanswered:
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
        print()

    if pinning:
        print("🌿 Mama's Perspective — holding the read watermark (nothing can confirm these):")
        for row in pinning:
            print(f"  • {row['qid']}   {row['state']['why']}")
            if row["suggestion"]:
                print(f"      ↳ {row['suggestion']}")
        print()

    if unanswered:
        print(f"💬 She told us {len(unanswered)} thing(s) nothing has answered yet:")
        for row in unanswered:
            rec = row["rec"]
            text = (rec.get("note") or "").strip().replace("\n", " ")
            print(f"  • ({momlib.et_str(rec.get('ts'), with_time=False)}) \"{text[:110]}"
                  f"{'…' if len(text) > 110 else ''}\"")
        print("  (see the full text + how to close it: `python3 tools/read-mom-feedback.py`)")
    return len(new) or len(waiting) or len(pinning) or len(unanswered)


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
    ap.add_argument("--address", metavar="NOTE_ID", default=None,
                    help="Record that one of her free-text notes has been acted on")
    ap.add_argument("--as", dest="disposition", metavar="WHERE", default=None,
                    help="Where it went, e.g. 'filed as BACKLOG A1 rainfall row; fixed in abc1234'")
    ap.add_argument("--retire", metavar="QUESTION_ID", default=None,
                    help="Retire a card she has ALREADY ANSWERED (active:false + resolvedAt). "
                         "Needs --because '<what was incorporated>'.")
    ap.add_argument("--because", metavar="WHAT", default=None,
                    help="For --retire: what her answer actually changed. The incorporation "
                         "attestation — no machine can check it, so a human states it.")
    ap.add_argument("--acknowledged", action="store_true",
                    help="Mark that the ribbon has told HER about it (not just that we fixed it)")
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
    # Self-test traffic and "Got it" receipts are the system talking about
    # itself. They stay in the stream but must never read as a person waiting.
    records = [r for r in records if not momlib.is_instrumentation(r)]
    mom = [r for r in records if (r.get("context") or {}).get("type") == "mom-queue"]
    other = [r for r in records if (r.get("context") or {}).get("type") != "mom-queue"]

    c = momlib.canon()
    rows, buckets = classify(mom, questions, c)
    note_rows, note_buckets = classify_notes(records)

    if args.retire:
        # ⭐ RETIREMENT IS A STEP, NOT A CHORE `[paul-stated 2026-08-04]`: "if that's
        # the question card that you already asked or answered, we should definitely
        # retire that. That should be automatic part of the process, after we check
        # that we've incorporated the feedback."
        #
        # Until now retiring meant hand-editing questions.json, which is precisely
        # why it got skipped — `q-top-categories` was answered 08-03 and was still
        # being SERVED to her a day later, so a fresh device would have re-asked her
        # a question she had already answered, and (being reflective/unprobeable) it
        # pinned the feedback watermark the whole time.
        #
        # ⚠️ WHAT STAYS HUMAN, AND WHY IT CANNOT BE AUTOMATED AWAY. A reflective card
        # has no `_foldTarget` by design, so canon can NEVER say "handled" for it —
        # that is the 2026-07-27 unprobeable rule. So the detector is deterministic
        # (check-cards.py already flags served-but-answered) and the ACTION is one
        # command, but the judgement "did we actually incorporate what she said?"
        # is `--because`, typed by a person. Retiring first would claim we acted on
        # a preference we had not: HANDLED, THEN RETIRED, in that order.
        qs = momlib.load_json("questions.json")
        items = qs.get("questions") if isinstance(qs, dict) else qs
        q = next((x for x in items if x.get("id") == args.retire), None)
        if q is None:
            print(f"error: no question with id {args.retire!r} in questions.json", file=sys.stderr)
            return 2
        if not args.because:
            print("error: --retire needs --because \"<what her answer changed>\". A card retired "
                  "with no stated incorporation is indistinguishable from one quietly dropped.",
                  file=sys.stderr)
            return 2
        answered = [r for r in mom
                    if (r.get("context") or {}).get("questionId") == args.retire]
        if not answered:
            print(f"⛔ REFUSED: she has not answered {args.retire!r} in {args.start} → {args.end}.\n"
                  f"   Retiring an UNANSWERED card silently removes a question she never got to.\n"
                  f"   Widen --start if the answer is older, or leave it serving.", file=sys.stderr)
            return 2
        if not q.get("active", True):
            print(f"· {args.retire} is already retired (resolvedAt {q.get('resolvedAt')}). Nothing to do.")
            return 0
        when = answered[-1].get("ts")
        q["active"] = False
        q["resolvedAt"] = str(dt.date.today())
        q["_note"] = (q.get("_note", "") +
                      f" RETIRED {q['resolvedAt']} — answered {momlib.et_str(when)}. "
                      f"Incorporated: {' '.join(args.because.split())}").strip()
        momlib.save_json("questions.json", qs) if hasattr(momlib, "save_json") else None
        if not hasattr(momlib, "save_json"):
            with open(os.path.join(momlib.ROOT, "questions.json"), "w", encoding="utf-8") as f:
                json.dump(qs, f, indent=2, ensure_ascii=False)
                f.write("\n")
        print(f"✓ {args.retire} retired ({q['resolvedAt']}).")
        print(f"  incorporated: {args.because}")
        print("  This also RELEASES the feedback watermark if this card was holding it —")
        print("  re-run `--pickup` to confirm, and re-run check-cards.py to confirm she is")
        print("  no longer being served something she already answered.")
        return 0

    if args.address:
        rec = next((r for r in records if r.get("id") == args.address), None)
        if rec is None:
            print(f"error: no feedback record with id {args.address!r} in {args.start} → {args.end}. "
                  f"Widen --start if it's older.", file=sys.stderr)
            return 2
        if not args.disposition:
            print("error: --address needs --as \"<where it went>\". Record the action, not her words.",
                  file=sys.stderr)
            return 2
        entry = momlib.address_note(rec, args.disposition, acknowledged=args.acknowledged)
        print(f"✓ {rec['id']} recorded as addressed ({entry['addressedOn']}): {entry['disposition']}")
        if not args.acknowledged:
            print("  Note: this records that WE acted, not that SHE knows. If the ribbon hasn't")
            print("  told her yet, she still doesn't know she was heard — re-run with --acknowledged")
            print("  once MOM_ACK_DATA names it.")
        return 0

    if args.pickup:
        # The counter prints FIRST and ALWAYS — before the conditional block, so
        # a quiet day still produces a line. Stamped after rendering so the line
        # reports the gap since the PREVIOUS look, not zero.
        try:
            window_days = (dt.date.fromisoformat(args.end) - dt.date.fromisoformat(args.start)).days
        except ValueError:
            window_days = 30
        render_counter(state, mom, window_days)
        # M1: the counter above sees ONE channel. This sees all of them, and it
        # runs on the quiet path too — a channel is only watched if something
        # looks at it on the days nothing happened.
        render_channels(token)
        render_pickup(mom, questions, watermark, rows, buckets, note_buckets)
        state["lastCheckedAt"] = dt.datetime.now().astimezone().isoformat()
        save_state(state)
    else:
        render_full(mom, other, questions, watermark, args.all, rows, buckets, note_buckets)

    # Surfacing her records to a human IS the act of reading this channel, so
    # this tool — and only a tool that actually displays them — advances the
    # feedback channel's read mark. check-mom-ack.py can then refuse to go green
    # on a channel nothing has read.
    if records:
        newest_shown = max((r.get("ts") or "") for r in records)
        if newest_shown:
            momlib.mark_channel_read("feedback", newest_shown, by="read-mom-feedback.py")

    if (args.mark_reviewed or args.mark_reviewed_through) and mom:
        new_wm, why = advance_watermark(state, mom, rows, through=args.mark_reviewed_through,
                                        note_rows=note_rows)
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
