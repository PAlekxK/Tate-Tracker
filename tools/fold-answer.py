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
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
VIEWER = os.path.join(ROOT, "viewer.html")
QUESTIONS = os.path.join(ROOT, "questions.json")

sys.path.insert(0, HERE)
import reinline  # noqa: E402
import momlib  # noqa: E402

rmf = momlib  # historical alias — this file used to import read-mom-feedback.py by path

# entityRef.type -> where the record lives. This file used to carry its own
# copy of that map — plants-only at first, so the three live WEED cards silently
# degraded to "entity not found in plants.json" (2026-07-26), and then a
# hand-kept duplicate afterwards. It now reads momlib's ONE declaration
# (2026-07-27); add a new domain THERE, never here.
FOLD_SOURCES = momlib.ENTITY_SOURCES

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


def find_entity(entities, eid):
    for e in entities:
        if e.get("id") == eid:
            return e
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

    # Top-level `confidence` — the weeds shape. Her "yes, that's stiltgrass"
    # settles the ID we read off a photo, so the honesty markers both move.
    if target == "confidence" and plant.get("confidence") is not None:
        old = plant.get("confidence")
        if old == "verified":
            return (None, "identification already verified", None, None)

        def apply():
            plant["confidence"] = "verified"
            if plant.get("status") == "needs-confirmation":
                plant["status"] = "confirmed"
            plant["verifiedOn"] = when or dt.date.today().strftime("%Y-%m")
            plant["source"] = f"confirmed on the ground{', ' + label_month if label_month else ''}"
        return (f"{plant['id']}.confidence", old, "verified", apply)

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
    by_id = {q["id"]: q for q in questions}

    # Load every entity source a card could point at (plants, weeds), keeping
    # each parsed doc so we write back only the ones we actually touched.
    docs = {}
    for etype in FOLD_SOURCES:
        try:
            docs[etype] = json.load(open(momlib.entity_path(etype), encoding="utf-8"))
        except FileNotFoundError:
            docs[etype] = None
    touched = set()

    answers = latest_answers(token)
    # Foldable = answered + question still open (active:true) + has a fold target.
    todo = [(qid, a) for qid, a in answers.items()
            if qid in by_id and by_id[qid].get("active") is True]

    if not todo:
        print("Nothing to fold — no open question has a fresh Yes/No answer.")
        return 0

    applied = 0
    folded_ts = []       # ts of exactly what we folded — the watermark's ceiling
    manual = []
    for qid, answer in todo:
        q = by_id[qid]
        ref = q.get("entityRef") or {}
        etype, eid = ref.get("type"), ref.get("id")
        if q.get("_foldTarget") is None:
            manual.append((qid, "reflective/preference — not a canon fold; note it for yourself"))
            continue
        if etype not in FOLD_SOURCES or docs.get(etype) is None:
            manual.append((qid, f"no source file mapped for entityRef.type={etype!r}"))
            continue
        src = FOLD_SOURCES[etype]
        plant = find_entity(docs[etype].get(src.key) or [], eid)
        if plant is None:
            manual.append((qid, f"entity {eid!r} not found in {src.file}"))
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
        touched.add(etype)
        q["active"] = False
        q["resolvedAt"] = dt.date.today().isoformat()
        q["resolution"] = f"Mom confirmed '{rmf.CONFIRM_LABEL.get(answer.get('sentiment'), answer.get('sentiment'))}' " \
                          f"{momlib.et_str(answer.get('ts'), with_time=False)}; " \
                          f"folded into {src.file} ({path} → verified)."
        if answer.get("ts"):
            folded_ts.append(answer["ts"])
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
        # Write back ONLY the canon files we touched, then re-inline each one's
        # const via the shared side-effect-free path.
        written = []
        for etype in sorted(touched):
            src = FOLD_SOURCES[etype]
            path_json = momlib.entity_path(etype)
            json.dump(docs[etype], open(path_json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            open(path_json, "a", encoding="utf-8").write("\n")
            reinline.reinline_from_source(VIEWER, src.const, path_json)
            written.append(f"{src.file} + {src.const}")
        json.dump(qdata, open(QUESTIONS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        open(QUESTIONS, "a", encoding="utf-8").write("\n")
        print(f"\n✓ Folded {applied} answer(s): {', '.join(written)} + questions.json updated.")

        # Advance the read watermark — but ONLY through what we actually folded.
        #
        # ⚠️ This call used to be a bare `--mark-reviewed`, which stamped the max
        # timestamp across EVERY record in view. Folding one card therefore made
        # an unrelated, unfolded answer of Mom's stop being "new" — permanently.
        # It was the only silent-data-loss path in the cycle. `--mark-reviewed-
        # through` bounds the stamp to these answers, and read-mom-feedback.py
        # additionally clamps below anything still needing Paul.
        cmd = [sys.executable, os.path.join(HERE, "read-mom-feedback.py")]
        if folded_ts:
            cmd += ["--mark-reviewed-through", max(folded_ts)]
        else:
            cmd += ["--mark-reviewed"]
        subprocess.run(cmd, cwd=ROOT, env={**os.environ, "FERNWOOD_TOKEN": token},
                       stdout=subprocess.DEVNULL)

        # A fold is by definition new acknowledged-through material: she settled
        # something, so the ribbon owes her a line naming it. The tool computes
        # THAT she is owed one; the words stay Paul's (AI-boundary, CLAUDE.md).
        print("\n🎗  The acknowledgment ribbon now owes her a line — she just settled something.")
        print("    Name what she actually gave, in her words, then commit AND PUSH")
        print("    (Pages serves viewer.html; a commit alone never reaches her):")
        print("      1. edit MOM_ACK_DATA.message + acknowledgedThrough in viewer.html")
        print(f"      2. python3 tools/check-mom-ack.py    (verifies it covers her latest input)")

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
