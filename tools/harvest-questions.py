#!/usr/bin/env python3
"""harvest-questions.py — deterministic reseed for Mama's Perspective.

Reads the canon's OWN honest-uncertainty markers — the places the data already
admits it's guessing — and drafts candidate confirm-cards for the one person who
can settle them from the ground. It NEVER writes a live card: candidates print
for Paul to approve (his locked gate), or `--append-drafts` files them into
questions.json as active:false so he flips the ones he wants. No AI: selection is
a deterministic filter over structured markers; phrasing is a fixed template bank
(Paul edits for voice). This is the "AI on the ask path, capture AI-free" line —
harvest is neither; it's mechanical selection from a human-authored uncertainty.

Markers harvested (all must be Mom-answerable FROM THE GROUND — observable, never
taxonomic):
  • variety   — plant.variety with confidence != 'verified' AND askable == true
                → "we read it as X off a photo — does that match?"
  • bloom     — plant.bloom with confidence == 'inferred' AND its window is
                ACTIVE RIGHT NOW (so "is it in flower?" is answerable today)
                → "should be in flower about now — does that match?"

Already-covered markers are skipped: an entity with an active OR resolved question
in questions.json is not re-drafted (don't re-ask what she's settled or is being
asked).

Usage:
    python3 tools/harvest-questions.py                 # dry run — print candidates
    python3 tools/harvest-questions.py --append-drafts # file them as active:false drafts
    python3 tools/harvest-questions.py --today 2026-07-14  # override "now" (testing)
"""
import argparse
import datetime as dt
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PLANTS = os.path.join(ROOT, "plants.json")
QUESTIONS = os.path.join(ROOT, "questions.json")

# Template bank — keyed by marker type. Deterministic; {placeholders} filled from
# the marker. Paul edits the drafted prompt for voice before it goes live.
TEMPLATES = {
    "variety": "The {name} — we read it as **{variety}** off a photo, but that's a guess.{note} Does that match what's out there?",
    "bloom":   "The **{name}** should be in flower about now — but that's a guess off the book, not something we've actually watched. Does that match what's out there?",
}


def mmdd(d):
    return f"{d.month:02d}-{d.day:02d}"


def range_active(rng, today_mmdd):
    """Year-wrap-aware: is today_mmdd within {start,end} (MM-DD)? Mirrors the
    viewer's mmddRangeActive."""
    s, e = rng.get("start"), rng.get("end")
    if not s or not e:
        return False
    if s <= e:
        return s <= today_mmdd <= e
    return today_mmdd >= s or today_mmdd <= e  # wraps the year end


def covered_ids(questions):
    """Entity ids that already have a question (active OR resolved) — skip these."""
    ids = set()
    for q in questions:
        ref = (q.get("entityRef") or {})
        if ref.get("id"):
            ids.add(ref["id"])
    return ids


def short_name(plant):
    """A friendlier card name than the full scientific-ish name."""
    n = plant.get("name") or plant.get("id")
    # "Clematis (large-flowered hybrid)" -> "Clematis"
    return n.split(" (")[0].strip()


def harvest(plants, questions, today_mmdd):
    covered = covered_ids(questions)
    cands = []
    for p in plants:
        pid = p.get("id")
        if not pid or pid in covered:
            continue
        name = short_name(p)

        v = p.get("variety")
        if isinstance(v, dict) and v.get("value") and v.get("confidence") != "verified" and v.get("askable"):
            note = v.get("note")
            note_txt = f" ({note})" if note else ""
            cands.append({
                "type": "variety",
                "id": f"q-{pid}-variety",
                "entityId": pid,
                "prompt": TEMPLATES["variety"].format(name=name, variety=v["value"], note=note_txt),
                "why": f"variety '{v['value']}' is {v.get('confidence','?')} + askable",
                # a "no" on an ID owes the real name; keeps the variety-confirm voice
                "extra": {"correctionPrompt": "What is it, then? (optional)"},
            })

        b = p.get("bloom")
        if isinstance(b, dict) and b.get("confidence") == "inferred" and isinstance(b.get("dates"), list):
            if any(range_active(r, today_mmdd) for r in b["dates"]):
                cands.append({
                    "type": "bloom",
                    "id": f"q-{pid}-bloom",
                    "entityId": pid,
                    "prompt": TEMPLATES["bloom"].format(name=name),
                    "why": f"bloom is inferred + in-window now ({b.get('window','')})",
                    # "It's out / Not yet" reads in one glance for a bloom question
                    "extra": {"labels": {"yes": "It's out", "no": "Not yet"}},
                })
    return cands


def to_question(cand, created):
    """Shape a candidate into a questions.json entry (drafted, NOT live)."""
    q = {
        "id": cand["id"],
        "kind": "confirm",
        "answerMode": "yesno",
        "prompt": cand["prompt"],
        "entityRef": {"type": "plant", "id": cand["entityId"]},
        "createdAt": created,
        "active": False,
        "_source": "harvest",
        "_foldTarget": cand["type"],
        "_draftNote": "Drafted by harvest-questions.py from a canon uncertainty marker. Edit the prompt for voice, then set active:true to serve it.",
    }
    q.update(cand.get("extra") or {})  # per-type labels / correctionPrompt
    return q


def main():
    ap = argparse.ArgumentParser(description="Harvest candidate Mama's-Perspective cards from canon uncertainty.")
    ap.add_argument("--today", default=str(dt.date.today()), help="YYYY-MM-DD override for the in-bloom filter")
    ap.add_argument("--append-drafts", action="store_true", help="Append candidates to questions.json as active:false drafts")
    args = ap.parse_args()

    today = dt.date.fromisoformat(args.today)
    plants = json.load(open(PLANTS, encoding="utf-8")).get("plants", [])
    qdata = json.load(open(QUESTIONS, encoding="utf-8"))
    questions = qdata.get("questions", [])

    cands = harvest(plants, questions, mmdd(today))

    if not cands:
        print("No new candidates — every askable uncertainty is already covered or out of season.")
        return 0

    print(f"=== {len(cands)} candidate card(s) — your approval gates each (nothing is live) ===\n")
    for c in cands:
        print(f"[{c['type']}] {c['id']}   ({c['why']})")
        print(f"    {c['prompt']}\n")

    existing_ids = {q.get("id") for q in questions}
    fresh = [c for c in cands if c["id"] not in existing_ids]

    if args.append_drafts:
        for c in fresh:
            questions.append(to_question(c, str(today)))
        qdata["questions"] = questions
        with open(QUESTIONS, "w", encoding="utf-8") as f:
            json.dump(qdata, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"Filed {len(fresh)} draft(s) into questions.json as active:false.")
        print("Review/edit each prompt, then set active:true on the ones you want served.")
    else:
        print("Dry run. Re-run with --append-drafts to file these as active:false drafts for your review,")
        print("or hand-copy the ones you want. (Already-drafted ids are skipped on append.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
