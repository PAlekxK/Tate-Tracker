#!/usr/bin/env python3
"""mom-queue-watch.py — the scheduled nudge for Mama's Perspective.

Runs unattended (via a launchd timer), READ-ONLY: it never folds, never writes a
card, never dirties the repo. It just answers "is there anything worth a 2-minute
approval session?" and pings Paul when the answer changes to yes — so he never has
to wonder whether Mom has answered.

⭐ WIDENED 2026-07-26 — it now watches "unacknowledged INPUT," not just "a fold
is waiting." The old trigger was `answered + active:True`, i.e. a confirm-card
answer. That is why this watcher was **completely silent on 2026-07-26**, the
richest feedback day the project has had: Mom asked Garden Guru two real
questions, reported a display problem, proposed a whole new domain and shared a
moss technique — and answered zero cards. A watcher keyed to the one channel her
stated fear of being wrong blocks will stay quiet exactly when it matters most.

So it pings on either of two things:
  1. she answered an OPEN card (a fold is waiting), or
  2. input landed through ANY app channel that the acknowledgment ribbon does
     not cover yet — the same computation `check-mom-ack.py` runs, imported,
     not reimplemented.

The ping also reports how many fresh cards the harvester could draft, so Paul can
reseed while he's in there.

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
import momlib  # noqa: E402


def _load(name, path):
    """Import a hyphenated tool by path. Still needed for harvest-questions.py;
    the copy that used to load read-mom-feedback.py is gone — its shared helpers
    now live in momlib (rule of three, 2026-07-26)."""
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
    """⛔ DELIBERATELY UNCONFIGURED — Paul's call 2026-08-02. Do not "fix" this.

    `.private/gmail-app-password` does not exist, so this always returns False
    and every ping logs `(email=skipped)`. That was raised as a gap — pings land
    only on a Mac nobody may be looking at — and Paul chose NOT to wire it:
    *"that's something we may wanna revisit in the future, but for now I don't
    wanna hear about it anymore… I don't wanna go through all the steps."*

    What replaced it is cheaper and needs no secret: `read-mom-feedback.py
    --pickup` now prints a **Mom-check counter on every run**, including quiet
    ones, so any session touching this repo sees how long it has been since
    anyone looked. Push notification traded for a pull reminder, on purpose.
    Leave the code path in place — it works the moment the file appears.
    """
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

    rmf = momlib  # the shared helpers used to be reached through read-mom-feedback.py
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

    # --- the widened half: input the ribbon doesn't cover yet ---
    # Same computation check-mom-ack.py runs, imported rather than reimplemented,
    # so "acknowledged" can only ever mean one thing across the two tools.
    ribbon = momlib.ribbon_state()
    ack = ribbon["acknowledged_through"]
    try:
        inputs = momlib.latest_mom_input(token, days=60)
    except Exception:  # noqa: BLE001
        inputs = {"latest": None, "channels": [], "errors": []}
    uncovered = momlib.channels_since(inputs, ack)
    uncovered_ts = max((c["latest"] for c in uncovered), default=None)

    state = read_state()
    pinged = set(state.get("pingedAnswerIds", []))
    new_answers = answered_open - pinged
    # Ping once per newly-arrived uncovered input, not every run.
    last_uncovered = state.get("lastUncoveredPingedTs") or ""
    new_uncovered = bool(uncovered_ts and uncovered_ts > last_uncovered)

    if not new_answers and not new_uncovered and not args.force:
        # Nothing new. Keep state's answered set current (so a re-answer of a
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
    if uncovered:
        chans = ", ".join(c["name"] for c in uncovered)
        parts.append(f"input the ribbon hasn't answered ({chans})")
    if k:
        parts.append(f"{k} new card(s) to approve")
    if not parts:
        parts.append("nothing pending (forced ping)")
    summary = "; ".join(parts) + "."

    body_lines = [summary, ""]
    if uncovered:
        body_lines += [
            "Input landed that the acknowledgment ribbon doesn't cover:",
            f"  ribbon covers through : {momlib.et_str(ack) if ack else '(no clock set)'}",
        ]
        for c in uncovered:
            body_lines.append(f"  · {c['name']:14s} {momlib.et_str(c['latest'])}")
        body_lines += [
            "  (attribution is NOT asserted — if that was your own tap, clear it with",
            "   python3 tools/check-mom-ack.py --acknowledged-through <ts>)",
            "",
        ]
    body_lines += [
        "When you have a minute, open a Fernwood session and run:",
        "  python3 tools/check-mom-ack.py                (is she owed a line?)",
        "  python3 tools/read-mom-feedback.py            (see her answers)",
        "  python3 tools/fold-answer.py --deploy         (fold them into canon)",
        "  python3 tools/harvest-questions.py            (draft new cards to approve)",
    ]
    body = "\n".join(body_lines) + "\n"

    notify_macos(title, summary)
    emailed = notify_email(title + " — " + summary, body)

    state["pingedAnswerIds"] = sorted(answered_open)
    if uncovered_ts:
        state["lastUncoveredPingedTs"] = uncovered_ts
    state["lastRun"] = today.isoformat()
    state["lastPingAt"] = dt.datetime.now().astimezone().isoformat()
    write_state(state)
    print(f"pinged: {summary}  (email={'sent' if emailed else 'skipped'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
