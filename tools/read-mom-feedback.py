#!/usr/bin/env python3
"""Read Mom's confirm-queue answers ("Mama's Perspective") and print them
legibly for Paul's pickup.

Answers are captured deterministically by the viewer (her tap + her verbatim
words — no AI) and POSTed to the Worker's /api/feedback with
context.{type:"mom-queue", questionId, kind}. This tool fetches that range,
keeps only the mom-queue records, and joins questionId -> prompt/entityRef from
the local questions.json so the output reads like a person, not raw JSON.

What it does beyond a raw dump:
  • NEW-since-last-seen — a local watermark (.private/mom-feedback-state.json)
    marks which answers have landed since you last reviewed. `--mark-reviewed`
    advances the watermark once you've acted on them.
  • Ready-to-fold punch-list — for each confirm, it drafts the concrete canon
    edit (flip plants.json <id> confidence inferred->verified, or correct it to
    what she said). It NEVER writes canon itself — promotion stays your hand
    (AI/automation on the surface path; the human confirms canon).
  • `--pickup` — a quiet one-screen mode for the Fernwood session-start ritual:
    prints a short "Mama's Perspective — N new" block, or nothing at all when
    there's nothing new (calm, no-noise, matches the app's tone).

Note: the viewer now reconciles answered questions against the Worker on load
(MomQueue.syncServerAnswers), so a Yes/No answer stops being served on ANY of
Mom's devices automatically — setting `active:false` in questions.json is now
just housekeeping, no longer required to keep from re-asking her.

Auth token (matches the Worker's SHARED_TOKEN), resolved in order:
    1. FERNWOOD_TOKEN environment variable
    2. .private/fernwood-token  (gitignored; first non-comment, non-blank line)

Env:
    FERNWOOD_WORKER_URL   defaults to the production Worker URL
    FERNWOOD_TOKEN        optional if .private/fernwood-token exists

Usage:
    python3 tools/read-mom-feedback.py                    # last 30 days, NEW flagged
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
import urllib.parse
import urllib.request

DEFAULT_WORKER_URL = "https://tate-tracker.paul-kirschenbauer.workers.dev"
WORKER_URL = os.environ.get("FERNWOOD_WORKER_URL", DEFAULT_WORKER_URL).rstrip("/")
HTTP_TIMEOUT_SEC = 30
USER_AGENT = "FernwoodMomFeedback/2.0 (+tools/read-mom-feedback.py)"

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.join(_HERE, "..")
TOKEN_FILE = os.path.join(_REPO, ".private", "fernwood-token")
STATE_FILE = os.path.join(_REPO, ".private", "mom-feedback-state.json")

# Display mapping: storage keeps the reused landed/so_so/missed enum; a confirm
# reads Yes / No / Not sure to a person.
CONFIRM_LABEL = {"landed": "Yes", "missed": "No", "so_so": "Not sure", None: "—"}
REACT_LABEL = {"landed": "looks right", "so_so": "so-so", "missed": "not right", None: "—"}
# Sentiments that are a DEFINITIVE answer (mirror the viewer: only these durably
# dismiss a question; so_so is a same-day "not sure" that comes back).
DEFINITIVE = ("landed", "missed")


def resolve_token():
    tok = os.environ.get("FERNWOOD_TOKEN", "").strip()
    if tok:
        return tok
    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s and not s.startswith("#"):
                    return s
    except FileNotFoundError:
        pass
    return ""


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


def _get(path, token, params=None):
    url = WORKER_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "X-Tate-Token": token,
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SEC) as resp:
        return json.load(resp)


def load_questions():
    """questionId -> question dict, from the repo's questions.json (if present)."""
    path = os.path.join(_REPO, "questions.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {q["id"]: q for q in data.get("questions", []) if isinstance(q, dict) and q.get("id")}
    except FileNotFoundError:
        return {}
    except Exception as e:  # noqa: BLE001
        print(f"warning: could not read questions.json ({e})", file=sys.stderr)
        return {}


def strip_md(text):
    return (text or "").replace("**", "")


def fold_suggestion(q, sentiment, note):
    """Draft the concrete canon edit for a confirm answer. Read-only — a
    suggestion for Paul, never an automatic write."""
    ref = (q or {}).get("entityRef") or {}
    target = ref.get("id") or "(unmapped)"
    kind = ref.get("type") or "entity"
    loc = f"{kind}s.json `{target}`" if target != "(unmapped)" else "the mapped entry"
    if sentiment == "landed":
        return f"flip {loc} confidence inferred→verified (lock the variety she confirmed)"
    if sentiment == "missed":
        if note:
            return f'correct {loc} — she says: "{note}"'
        return f"re-check {loc} — she marked it not-right (no detail); may want to ask her"
    return None


def flatten(data):
    """{days:{date:[records]}} -> flat list, oldest first (records carry ts)."""
    records = []
    for day in sorted((data.get("days") or {}).keys()):
        for rec in data["days"][day]:
            if isinstance(rec, dict):
                records.append(rec)
    records.sort(key=lambda r: r.get("ts") or "")
    return records


def is_new(rec, watermark):
    ts = rec.get("ts") or ""
    return bool(ts) and (not watermark or ts > watermark)


def render_full(mom, other, questions, watermark, show_all):
    """The detailed listing (default mode)."""
    if not mom:
        print("No answers from Mama's Perspective in this range.")
    else:
        new_count = sum(1 for r in mom if is_new(r, watermark))
        header = f"=== Mama's Perspective — {len(mom)} answer(s)"
        header += f", {new_count} new ===" if new_count else " ==="
        print("\n" + header + "\n")
        fold = []
        for r in mom:
            ctx = r.get("context") or {}
            qid = ctx.get("questionId", "?")
            kind = ctx.get("kind", "?")
            q = questions.get(qid)
            prompt = strip_md(q["prompt"]) if q else "(question not in current questions.json)"
            active = "" if (q and q.get("active") is not False) else "  [retired in questions.json]"
            sentiment = r.get("sentiment")
            if kind == "confirm":
                verdict = CONFIRM_LABEL.get(sentiment, sentiment or "—")
            elif kind == "react":
                verdict = REACT_LABEL.get(sentiment, sentiment or "—")
            else:
                verdict = sentiment or "note"
            when = (r.get("ts") or "")[:10]
            note = r.get("note") or ""
            newtag = "🆕 " if is_new(r, watermark) else "   "
            print(f"{newtag}Q ({kind} · {qid}){active}\n     {prompt}")
            line = f"     → Mom [{verdict}]"
            if note:
                line += f': "{note}"'
            if when:
                line += f"   ({when})"
            print(line + "\n")
            if kind == "confirm" and sentiment in DEFINITIVE:
                sug = fold_suggestion(q, sentiment, note)
                if sug:
                    fold.append((qid, sug))

        if fold:
            print("--- Ready to fold into canon (your call — nothing is auto-written) ---")
            for qid, sug in fold:
                print(f"  • {qid}: {sug}")
            print()

    if show_all and other:
        print(f"=== Other feedback records — {len(other)} ===\n")
        for r in other:
            when = (r.get("ts") or "")[:10]
            ctx = r.get("context") or {}
            print(f"  [{ctx.get('type','general')}] {r.get('sentiment') or '—'}"
                  + (f' — "{r.get("note")}"' if r.get("note") else "") + f"   ({when})")


def render_pickup(mom, questions, watermark):
    """Quiet session-start block: only what's NEW; nothing at all if none.
    Returns the number of new answers (so the caller/exit can stay quiet)."""
    new = [r for r in mom if is_new(r, watermark)]
    if not new:
        return 0
    print(f"🌿 Mama's Perspective — {len(new)} new answer(s) since you last looked:")
    for r in new:
        ctx = r.get("context") or {}
        qid = ctx.get("questionId", "?")
        q = questions.get(qid)
        subj = strip_md(q["prompt"])[:60] + "…" if q else qid
        sentiment = r.get("sentiment")
        verdict = CONFIRM_LABEL.get(sentiment, sentiment or "—")
        note = r.get("note") or ""
        line = f"  • [{verdict}] {subj}"
        if note:
            line += f'  —  "{note}"'
        print(line)
        sug = fold_suggestion(q, sentiment, note)
        if sug and sentiment in DEFINITIVE:
            print(f"      ↳ {sug}")
    print("  (run `python3 tools/read-mom-feedback.py --mark-reviewed` once you've folded these in)")
    return len(new)


def main():
    ap = argparse.ArgumentParser(description="Read Mom's Mama's-Perspective answers.")
    today = dt.date.today()
    ap.add_argument("--start", default=str(today - dt.timedelta(days=30)), help="YYYY-MM-DD (default: 30 days ago)")
    ap.add_argument("--end", default=str(today), help="YYYY-MM-DD (default: today)")
    ap.add_argument("--all", action="store_true", help="Include non-mom-queue feedback records too")
    ap.add_argument("--pickup", action="store_true", help="Quiet session-start mode: only what's new; silent if nothing new")
    ap.add_argument("--mark-reviewed", action="store_true", help="Stamp all shown answers as seen (advance the watermark to now)")
    args = ap.parse_args()

    token = resolve_token()
    if not token:
        msg = ("error: no token. Set FERNWOOD_TOKEN, or put it in .private/fernwood-token "
               "(matches the Worker's SHARED_TOKEN).")
        # In --pickup mode, stay silent-ish so a missing token never noises up every pickup.
        print(msg, file=sys.stderr)
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

    if args.pickup:
        render_pickup(mom, questions, watermark)
    else:
        render_full(mom, other, questions, watermark, args.all)

    if args.mark_reviewed and mom:
        newest = max((r.get("ts") or "") for r in mom)
        if newest:
            state["lastReviewedTs"] = newest
            state["lastReviewedAt"] = dt.datetime.now().astimezone().isoformat()
            save_state(state)
            print(f"\n✓ Watermark advanced — {len(mom)} answer(s) marked reviewed (through {newest[:10]}).",
                  file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
