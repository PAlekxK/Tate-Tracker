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
ZONES = os.path.join(ROOT, "zones.json")

# Template bank — keyed by marker type. Deterministic; {placeholders} filled from
# the marker. Paul edits the drafted prompt for voice before it goes live.
#
# ⭐ REWRITTEN 2026-07-29 (content-steward's draft, Paul-approved). The old bloom
# string made OUR CLAIM the subject and closed on "Does that match what's out
# there?" — which asks her to grade our guess. That is verdict-class, the one
# format the 2026-07-26 audit found she declines, and the reason is her own:
# she hesitates because she is afraid of being wrong.
#
# Three things the new string changes:
#   · the PLANT becomes the subject of the sentence, not our claim;
#   · the hedge becomes THE RECORD'S OWN GAP ("we've never actually watched it
#     here") instead of a request for her verdict;
#   · "yet" presupposes it will flower, so "Not blooming" is a fact about the
#     season rather than a negative verdict on us.
#
# Fixed here, it corrects the 5 staged cards and every future one off the 20
# inferred bloom windows. It does NOT retroactively rewrite prompts already
# written into questions.json — the 2 live cards were hand-edited to match.
TEMPLATES = {
    # ⚠️ NOT SERVABLE AS-IS, BY DESIGN — see to_question()'s tripwire. A good
    # variety card needs an observable that differs per plant (colour, leaf,
    # seed-head); no generic string can produce one, and the old string's "Does
    # that match what's out there?" *sounded* finished, which is exactly how a
    # verdict card gets flipped live by accident.
    "variety": ("The **{name}**{where} — the record has it as **{variety}**, read off a photo "
                "and never checked on the ground.{note} "
                "⟨WRITE THE OBSERVABLE: what would she SEE that settles this — colour, leaf, "
                "seed-head? Then delete this bracket.⟩"),
    "bloom":   ("The **{name}**{where} — we have it down to flower around now, though we've "
                "never actually watched it here. **Is it in flower yet?**"),
}

# Button labels, Paul's wording (2026-07-29): "it's blooming, not blooming, or
# snooze card. Let's just use snooze card as a way to dismiss it, but it goes back
# into the queue for resurfacing later."
#
# The third button's MECHANISM already worked this way — notSure() stamps
# snoozed[id] = today and outstanding() filters on `!== today`, so the card
# returns the next day rather than being retired. This names the control after
# what it does.
#
# ⚠️ Recorded tension, Paul's call stands: the 7/26 doctrine chose STATE language
# ("I haven't looked") over action language on the reasoning that a state is
# unembarrassing to someone afraid of being wrong, and check-cards.py lints
# deferral-shaped labels ("Ask me later", "Skip", "Not now"). "Snooze card" is an
# action on the card rather than a state she is in, so it sits closer to that line
# — but it is also unambiguous about what happens next, which the state label was
# not, and Paul weighed simplicity for this reader as the higher good. It does not
# trip the lint. If the third button's tap rate drops, this is the variable to
# revisit first.
BLOOM_LABELS = {"yes": "It's blooming", "no": "Not blooming", "later": "Snooze card"}


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


def where_phrase(plant, zones_by_id):
    """" down at the pond" / " in the Western Garden" — or "" when we don't know.

    The cheap anchor fix (content-steward C7): it tells her WHICH plant we mean,
    which on an ID card matters more than voice. Most plants have no `zoneId`
    today, so most cards get nothing — and that is the honest outcome, not a
    degradation. Never invents a location.
    """
    zid = plant.get("zoneId")
    if not zid:
        return ""
    z = zones_by_id.get(zid) or {}
    nm = (z.get("name") or "").strip()
    if not nm:
        return ""
    return f" in the {nm}"


def harvest(plants, questions, today_mmdd, zones_by_id=None):
    zones_by_id = zones_by_id or {}
    covered = covered_ids(questions)
    cands = []
    for p in plants:
        pid = p.get("id")
        if not pid or pid in covered:
            continue
        name = short_name(p)
        where = where_phrase(p, zones_by_id)

        v = p.get("variety")
        if isinstance(v, dict) and v.get("value") and v.get("confidence") != "verified" and v.get("askable"):
            note = v.get("note")
            note_txt = f" ({note})" if note else ""
            cands.append({
                "type": "variety",
                "id": f"q-{pid}-variety",
                "entityId": pid,
                "prompt": TEMPLATES["variety"].format(
                    name=name, variety=v["value"], note=note_txt, where=where),
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
                    "prompt": TEMPLATES["bloom"].format(name=name, where=where),
                    "why": f"bloom is inferred + in-window now ({b.get('window','')})",
                    # Emitted EXPLICITLY so the JSON is self-describing. The viewer
                    # defaults a missing `later` to "I haven't looked", which meant
                    # the served card and the record disagreed about what her third
                    # option said — and a reader of questions.json concluded there
                    # was no third button at all. There was. Say it in the file.
                    "extra": {"labels": dict(BLOOM_LABELS)},
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

    # zones give the {where} anchor; absent file just means every card gets "".
    zones_by_id = {}
    try:
        zdata = json.load(open(ZONES, encoding="utf-8"))
        for z in (zdata.get("zones") or []):
            if isinstance(z, dict) and z.get("id"):
                zones_by_id[z["id"]] = z
    except (OSError, ValueError):
        pass

    cands = harvest(plants, questions, mmdd(today), zones_by_id)

    if not cands:
        print("No new candidates — every askable uncertainty is already covered or out of season.")
        return 0

    print(f"=== {len(cands)} candidate card(s) — your approval gates each (nothing is live) ===\n")
    for c in cands:
        print(f"[{c['type']}] {c['id']}   ({c['why']})")
        print(f"    {c['prompt']}\n")
        if "\u27e8" in c["prompt"]:
            print("    \u26a0\ufe0f  UNRESOLVED \u27e8\u2026\u27e9 — this prompt is a SKELETON, not a question.")
            print("        No generic string can name the observable that settles a variety;")
            print("        write what she would SEE, delete the bracket, then flip it live.")
            print("        check-cards.py fails on any served card still carrying one.\n")

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
