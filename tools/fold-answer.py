#!/usr/bin/env python3
"""fold-answer.py — assisted one-tap fold for Mama's Perspective.

The other half of the loop from read-mom-feedback.py: it takes what Mom has
SETTLED and folds it into canon, with Paul as the confirmer. For each answered
question still open (active:true) it drafts the exact plants.json edit, shows the
before→after, and — only on your yes — applies it, re-inlines PLANTS_DATA, retires
the question (active:false + a resolution line), and (optionally) rebuilds the
digest and deploys. Nothing is written to canon without your approval; the capture
side stays untouched.

What it can auto-draft:
  • variety + "Looks right" (landed) → variety.confidence inferred→verified
  • bloom   + "It's out"   (landed) → bloom.confidence   inferred→verified
A "Not quite" (missed) prints her correction for you to hand-apply (an ID change
is a judgment call, not a mechanical flip). Reflective cards (no _foldTarget) are
her preference, not canon — reported, never folded.

Token: FERNWOOD_TOKEN env or .private/fernwood-token (same as read-mom-feedback.py).

Usage:
    python3 tools/fold-answer.py                 # interactive: review + approve each
    python3 tools/fold-answer.py --deploy         # also rebuild digest + deploy after
    python3 tools/fold-answer.py --dry-run        # show what it WOULD do, change nothing
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
VIEWER = os.path.join(ROOT, "viewer.html")
PLANTS = os.path.join(ROOT, "plants.json")
QUESTIONS = os.path.join(ROOT, "questions.json")

sys.path.insert(0, HERE)
import reinline  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


rmf = _load("rmf", os.path.join(HERE, "read-mom-feedback.py"))

MONTHS = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def latest_answers(token):
    """questionId -> latest mom-queue answer record (definitive answers only)."""
    today = dt.date.today()
    start = str(today - dt.timedelta(days=60))  # Worker caps the feedback range (~90d); stay under
    data = rmf._get("/api/feedback", token, {"start": start, "end": str(today)})
    latest = {}
    for r in rmf.flatten(data):  # oldest-first
        ctx = r.get("context") or {}
        if ctx.get("type") == "mom-queue" and ctx.get("questionId") and r.get("sentiment") in rmf.DEFINITIVE:
            latest[ctx["questionId"]] = r  # later overwrites earlier
    return latest


def find_plant(plants, pid):
    for p in plants:
        if p.get("id") == pid:
            return p
    return None


def draft_edit(question, plant, answer):
    """Return (field_path, old, new, apply_fn) or (None, reason, None, None) if not auto-foldable."""
    target = question.get("_foldTarget")
    sentiment = answer.get("sentiment")
    when = (answer.get("ts") or "")[:7]  # YYYY-MM
    label_month = ""
    if len(when) == 7:
        y, m = when.split("-")
        label_month = f"{MONTHS[int(m)]} {y}"

    if sentiment == "missed":
        note = answer.get("note") or "(no detail given)"
        return (None, f'she answered "Not quite": {note} — correct by hand (an ID change is a judgment call)', None, None)

    if target == "variety" and isinstance(plant.get("variety"), dict):
        v = plant["variety"]
        old = v.get("confidence")
        if old == "verified":
            return (None, "variety already verified", None, None)

        def apply():
            v["confidence"] = "verified"
            v["askable"] = False
            v["verifiedOn"] = when or dt.date.today().strftime("%Y-%m")
            v["source"] = f"confirmed on the ground{', ' + label_month if label_month else ''}"
        return (f"{plant['id']}.variety.confidence", old, "verified", apply)

    if target == "bloom" and isinstance(plant.get("bloom"), dict):
        b = plant["bloom"]
        old = b.get("confidence")
        if old == "verified":
            return (None, "bloom already verified", None, None)

        def apply():
            b["confidence"] = "verified"
        return (f"{plant['id']}.bloom.confidence", old, "verified", apply)

    return (None, f"no auto-fold rule for _foldTarget={target!r}", None, None)


def main():
    ap = argparse.ArgumentParser(description="Fold Mom's settled answers into canon (with approval).")
    ap.add_argument("--deploy", action="store_true", help="Rebuild digest + deploy the Worker after applying")
    ap.add_argument("--dry-run", action="store_true", help="Show what would change; write nothing")
    ap.add_argument("--yes", action="store_true", help="Skip the per-edit prompt (auto-approve every auto-foldable edit)")
    args = ap.parse_args()

    token = rmf.resolve_token()
    if not token:
        print("error: no token (set FERNWOOD_TOKEN or .private/fernwood-token).", file=sys.stderr)
        return 2

    qdata = json.load(open(QUESTIONS, encoding="utf-8"))
    questions = qdata["questions"]
    pdata = json.load(open(PLANTS, encoding="utf-8"))
    plants = pdata["plants"]
    by_id = {q["id"]: q for q in questions}

    answers = latest_answers(token)
    # Foldable = answered + question still open (active:true) + has a fold target.
    todo = [(qid, a) for qid, a in answers.items()
            if qid in by_id and by_id[qid].get("active") is True]

    if not todo:
        print("Nothing to fold — no open question has a fresh Yes/No answer.")
        return 0

    applied = 0
    manual = []
    for qid, answer in todo:
        q = by_id[qid]
        plant = find_plant(plants, (q.get("entityRef") or {}).get("id"))
        if q.get("_foldTarget") is None:
            manual.append((qid, "reflective/preference — not a canon fold; note it for yourself"))
            continue
        if plant is None:
            manual.append((qid, f"entity {(q.get('entityRef') or {}).get('id')!r} not found in plants.json"))
            continue

        path, old, new, apply = draft_edit(q, plant, answer)
        prompt_txt = rmf.strip_md(q.get("prompt", ""))[:70]
        if apply is None:
            manual.append((qid, old))  # `old` holds the reason here
            continue

        print(f"\n● {qid}   ({prompt_txt}…)")
        print(f"    canon edit: {path}:  {old!r} → {new!r}")
        print(f"    then: retire the card (active:false) + resolution line")
        if args.dry_run:
            continue
        ok = args.yes or input("    apply? [y/N] ").strip().lower() == "y"
        if not ok:
            print("    skipped.")
            continue

        apply()
        q["active"] = False
        q["resolvedAt"] = dt.date.today().isoformat()
        q["resolution"] = f"Mom confirmed '{rmf.CONFIRM_LABEL.get(answer.get('sentiment'), answer.get('sentiment'))}' " \
                          f"{(answer.get('ts') or '')[:10]}; folded into plants.json ({path} → verified)."
        applied += 1
        print("    ✓ staged")

    if manual:
        print("\n--- Needs your hand (not auto-folded) ---")
        for qid, why in manual:
            print(f"  • {qid}: {why}")

    if args.dry_run:
        print("\nDry run — nothing written.")
        return 0

    if applied:
        # Write canon + questions, then re-inline PLANTS_DATA via the shared path.
        json.dump(pdata, open(PLANTS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        open(PLANTS, "a", encoding="utf-8").write("\n")
        json.dump(qdata, open(QUESTIONS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        open(QUESTIONS, "a", encoding="utf-8").write("\n")
        reinline.reinline_from_source(VIEWER, "PLANTS_DATA", PLANTS)
        print(f"\n✓ Folded {applied} answer(s): plants.json + PLANTS_DATA + questions.json updated.")

        # Advance the read watermark so these stop showing as 'new' in --pickup.
        subprocess.run([sys.executable, os.path.join(HERE, "read-mom-feedback.py"), "--mark-reviewed"],
                       cwd=ROOT, env={**os.environ, "FERNWOOD_TOKEN": token})

        if args.deploy:
            print("\n[deploy] rebuilding digest + deploying Worker …")
            subprocess.run([os.path.join(HERE, "deploy-worker.sh")], cwd=ROOT)
        else:
            print("\nNext: rebuild the Guru digest + deploy so it serves the confirmed data:")
            print("      python3 tools/build-digest.py && ./tools/deploy-worker.sh   (or re-run with --deploy)")
        print("Then commit: git add -A && git commit && git push")
    else:
        print("\nNothing applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
