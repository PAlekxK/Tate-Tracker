#!/usr/bin/env python3
"""Read Mom's confirm-queue answers ("When you're out there") and print them
legibly for Paul's pickup.

Answers are captured deterministically by the viewer (her tap + her verbatim
words — no AI) and POSTed to the Worker's /api/feedback with
context.{type:"mom-queue", questionId, kind}. This tool fetches that range,
keeps only the mom-queue records, and joins questionId -> prompt from the
local questions.json so the output reads like a person, not raw JSON.

Pickup loop: read an answer here -> act on it (edit plants.json, flip the
plant's `confidence` inferred -> verified, commit) -> set that question
`active: false` (or delete the row) in questions.json so it stops being asked.
Confirmed IDs are promoted to canon BY HAND — nothing here auto-writes canon.

Env:
    FERNWOOD_WORKER_URL   defaults to the production Worker URL
    FERNWOOD_TOKEN        required; matches the Worker's SHARED_TOKEN

Usage:
    FERNWOOD_TOKEN=... python3 tools/read-mom-feedback.py                 # last 30 days
    FERNWOOD_TOKEN=... python3 tools/read-mom-feedback.py --start 2026-07-01 --end 2026-07-31
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
TOKEN = os.environ.get("FERNWOOD_TOKEN", "")
HTTP_TIMEOUT_SEC = 30
USER_AGENT = "FernwoodMomFeedback/1.0 (+tools/read-mom-feedback.py)"

# Display mapping: storage keeps the reused landed/so_so/missed enum; a confirm
# reads Yes / No / Not sure to a person.
CONFIRM_LABEL = {"landed": "Yes", "missed": "No", "so_so": "Not sure", None: "—"}
REACT_LABEL = {"landed": "looks right", "so_so": "so-so", "missed": "not right", None: "—"}


def _get(path, params=None):
    url = WORKER_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "X-Tate-Token": TOKEN,
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SEC) as resp:
        return json.load(resp)


def load_questions():
    """questionId -> question dict, from the repo's questions.json (if present)."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "..", "questions.json")
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


def main():
    ap = argparse.ArgumentParser(description="Read Mom's confirm-queue answers.")
    today = dt.date.today()
    ap.add_argument("--start", default=str(today - dt.timedelta(days=30)), help="YYYY-MM-DD (default: 30 days ago)")
    ap.add_argument("--end", default=str(today), help="YYYY-MM-DD (default: today)")
    ap.add_argument("--all", action="store_true", help="Include non-mom-queue feedback records too")
    args = ap.parse_args()

    if not TOKEN:
        print("error: FERNWOOD_TOKEN is required (matches the Worker's SHARED_TOKEN).", file=sys.stderr)
        return 2

    print(f"Reading feedback {args.start} → {args.end} …", file=sys.stderr)
    try:
        data = _get("/api/feedback", {"start": args.start, "end": args.end})
    except Exception as e:  # noqa: BLE001
        print(f"error: fetch failed: {e}", file=sys.stderr)
        return 1

    questions = load_questions()

    # Flatten the {days: {date: [records]}} shape, newest first.
    records = []
    for day in sorted(data.get("days", {}).keys()):
        for rec in data["days"][day]:
            if isinstance(rec, dict):
                records.append(rec)

    mom = [r for r in records if (r.get("context") or {}).get("type") == "mom-queue"]
    other = [r for r in records if (r.get("context") or {}).get("type") != "mom-queue"]

    if not mom:
        print("No answers from the confirm queue in this range.")
    else:
        print(f"\n=== From the confirm queue — {len(mom)} answer(s) ===\n")
        for r in mom:
            ctx = r.get("context") or {}
            qid = ctx.get("questionId", "?")
            kind = ctx.get("kind", "?")
            q = questions.get(qid)
            prompt = strip_md(q["prompt"]) if q else "(question not in current questions.json)"
            active = "" if (q and q.get("active") is not False) else "  [already retired in questions.json]"
            sentiment = r.get("sentiment")
            if kind == "confirm":
                verdict = CONFIRM_LABEL.get(sentiment, sentiment or "—")
            elif kind == "react":
                verdict = REACT_LABEL.get(sentiment, sentiment or "—")
            else:
                verdict = sentiment or "note"
            when = (r.get("ts") or "")[:10]
            note = r.get("note") or ""
            print(f"Q ({kind} · {qid}){active}\n  {prompt}")
            line = f"  → Mom [{verdict}]"
            if note:
                line += f': "{note}"'
            if when:
                line += f"   ({when})"
            print(line + "\n")

    if args.all and other:
        print(f"=== Other feedback records — {len(other)} ===\n")
        for r in other:
            when = (r.get("ts") or "")[:10]
            ctx = r.get("context") or {}
            print(f"  [{ctx.get('type','general')}] {r.get('sentiment') or '—'}"
                  + (f' — "{r.get("note")}"' if r.get("note") else "") + f"   ({when})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
