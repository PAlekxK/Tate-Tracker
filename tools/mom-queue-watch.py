#!/usr/bin/env python3
"""mom-queue-watch.py — the scheduled nudge for Mama's Perspective.

Runs unattended (via a launchd timer), READ-ONLY: it never folds, never writes a
card, never dirties the repo. It just answers "is there anything worth a 2-minute
approval session?" and pings Paul when the answer changes to yes — so he never has
to wonder whether Mom has answered.

Triggers a ping when Mom has answered an OPEN question we haven't pinged about yet
(a fold is waiting). The ping also reports how many fresh cards the harvester could
draft, so Paul can reseed while he's in there.

Pings via (either/both, best-effort):
  • macOS notification  — always attempted (zero setup)
  • email to Paul       — only if .private/gmail-app-password exists (one-time
                          Gmail app-password; from/to = the address below)

State (so it pings once per new answer, not every run): .private/mom-queue-watch-state.json
Token: FERNWOOD_TOKEN env or .private/fernwood-token (same as the other tools).

Usage:
    python3 tools/mom-queue-watch.py            # the scheduled run
    python3 tools/mom-queue-watch.py --force    # ping even if nothing new (test)
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
PLANTS = os.path.join(ROOT, "plants.json")
QUESTIONS = os.path.join(ROOT, "questions.json")
STATE = os.path.join(ROOT, ".private", "mom-queue-watch-state.json")
APP_PW_FILE = os.path.join(ROOT, ".private", "gmail-app-password")
EMAIL_ADDR = "paul.kirschenbauer@gmail.com"

sys.path.insert(0, HERE)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def read_state():
    try:
        return json.load(open(STATE, encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return {}


def write_state(s):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    json.dump(s, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def notify_macos(title, body):
    try:
        subprocess.run(
            ["osascript", "-e", f"display notification {json.dumps(body)} with title {json.dumps(title)}"],
            check=False, capture_output=True, timeout=15,
        )
    except Exception:
        pass


def notify_email(subject, body):
    try:
        with open(APP_PW_FILE, encoding="utf-8") as f:
            app_pw = next((ln.strip() for ln in f if ln.strip() and not ln.startswith("#")), "")
    except FileNotFoundError:
        return False
    if not app_pw:
        return False
    try:
        import smtplib
        from email.message import EmailMessage
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDR
        msg["To"] = EMAIL_ADDR
        msg.set_content(body)
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as s:
            s.starttls()
            s.login(EMAIL_ADDR, app_pw)
            s.send_message(msg)
        return True
    except Exception as e:  # noqa: BLE001
        # A cron job must never crash-loop on a bad password / offline; log to stderr only.
        print(f"[mom-queue-watch] email failed: {e}", file=sys.stderr)
        return False


def main():
    ap = argparse.ArgumentParser(description="Scheduled nudge for Mama's Perspective (read-only).")
    ap.add_argument("--force", action="store_true", help="Ping even if nothing is new (for testing)")
    args = ap.parse_args()

    rmf = _load("rmf", os.path.join(HERE, "read-mom-feedback.py"))
    harvestmod = _load("harvestmod", os.path.join(HERE, "harvest-questions.py"))

    token = rmf.resolve_token()
    if not token:
        return 0  # unattended: stay silent, no token = nothing to do

    qdata = json.load(open(QUESTIONS, encoding="utf-8"))
    questions = qdata["questions"]
    plants = json.load(open(PLANTS, encoding="utf-8"))["plants"]
    by_id = {q["id"]: q for q in questions}

    # Answers to still-OPEN questions = folds waiting for Paul.
    today = dt.date.today()
    try:
        data = rmf._get("/api/feedback", token, {"start": str(today - dt.timedelta(days=60)), "end": str(today)})
    except Exception:
        return 0  # offline / Worker down — quietly try again next run
    answered_open = set()
    for r in rmf.flatten(data):
        ctx = r.get("context") or {}
        qid = ctx.get("questionId")
        if ctx.get("type") == "mom-queue" and qid and r.get("sentiment") in rmf.DEFINITIVE:
            q = by_id.get(qid)
            if q and q.get("active") is True:
                answered_open.add(qid)

    # Fresh cards the harvester could draft (read-only count).
    candidates = harvestmod.harvest(plants, questions, harvestmod.mmdd(today))
    existing = {q["id"] for q in questions}
    fresh_cards = [c for c in candidates if c["id"] not in existing]

    state = read_state()
    pinged = set(state.get("pingedAnswerIds", []))
    new_answers = answered_open - pinged

    if not new_answers and not args.force:
        # Nothing new to fold. Keep state's answered set current (so a re-answer of a
        # newly-reopened question can re-trigger), but don't ping.
        state["pingedAnswerIds"] = sorted(answered_open)
        state["lastRun"] = today.isoformat()
        write_state(state)
        return 0

    n = len(answered_open)
    k = len(fresh_cards)
    title = "Fernwood — Mama's Perspective"
    parts = []
    if n:
        parts.append(f"Mom answered {n} — ready to fold")
    if k:
        parts.append(f"{k} new card(s) to approve")
    if not parts:
        parts.append("nothing pending (forced ping)")
    summary = "; ".join(parts) + "."
    body = (summary + "\n\nWhen you have a minute, open a Fernwood session and run:\n"
            "  python3 tools/read-mom-feedback.py            (see her answers)\n"
            "  python3 tools/fold-answer.py --deploy         (fold them into canon)\n"
            "  python3 tools/harvest-questions.py            (draft new cards to approve)\n")

    notify_macos(title, summary)
    emailed = notify_email(title + " — " + summary, body)

    state["pingedAnswerIds"] = sorted(answered_open)
    state["lastRun"] = today.isoformat()
    state["lastPingAt"] = dt.datetime.now().astimezone().isoformat()
    write_state(state)
    print(f"pinged: {summary}  (email={'sent' if emailed else 'skipped'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
