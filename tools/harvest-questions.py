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

⭐ DOMAIN-AGNOSTIC since 2026-08-02 (M1). It no longer knows any field names. It
asks `momlib.markers(record, dtype)` "does this record admit a guess?" over every
domain the manifest marks `cardable`, and the MARKER PATH picks the template.
Adding a domain is a declaration in `momlib.DOMAINS` — not an edit in here.

*Why that mattered:* the BACKLOG called this "the one remaining plants-only site,"
which understated it. It did not merely read plants.json — it hardcoded the
`variety` and `bloom` field SHAPES, so repointing it at weeds.json would have
returned ZERO. Three weeds sat marked `confidence: inferred` +
`status: needs-confirmation` — explicitly raising their hands, in a vocabulary
this file could not hear.

Markers harvested (all must be Mom-answerable FROM THE GROUND — observable, never
taxonomic):
  • variety   — `variety.confidence` != verified AND askable
                → skeleton only; a human must write the observable (see TEMPLATES)
  • bloom     — `bloom.confidence` == inferred AND its window is ACTIVE RIGHT NOW
                (so "is it in flower?" is answerable today)
  • identity  — a record-level `confidence` that is not verified, in any domain
                → uses the record's OWN `momConfirm.confirmBy` as the observable,
                  which is why this one needs no human to finish it

Already-covered markers are skipped, in BOTH directions — card→record via
`entityRef`, and record→card via `momConfirm.questionId`. Reading only the first
re-drafts crabgrass; see covered_ids().

Usage:
    python3 tools/harvest-questions.py                 # dry run — print candidates
    python3 tools/harvest-questions.py --append-drafts # file them as active:false drafts
    python3 tools/harvest-questions.py --today 2026-07-14  # override "now" (testing)
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
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
    # ⭐ NEW 2026-08-02 — the shape that made non-plant domains harvestable at all.
    # A weed's uncertainty is its IDENTITY, and the record already names the thing
    # that settles it in `momConfirm.confirmBy` ("counting five leaflets on a leaf
    # (poison ivy has three)"). So unlike `variety`, this template does NOT need a
    # human to write the observable — the domain that admits the guess also states
    # how to check it. That pairing is why weeds could be wired and plants' variety
    # still cannot: the marker and the observable live together.
    "identity": ("The **{name}**{where} — we picked it out of a photo and have never "
                 "checked it on the ground. **{confirm_by}**"),
}

# Which template a marker path calls for. The harvester reads THIS instead of
# knowing field names, which is what makes it domain-agnostic: a new domain
# declares its marker path in momlib.DOMAINS and lands here, not in the loop.
MARKER_TEMPLATE = {
    "variety.confidence": "variety",
    "bloom.confidence": "bloom",
    "confidence": "identity",
}

# A confirmBy that names a season is describing something that may not exist
# today. Flagged, never suppressed — the prose is not machine-readable, so a
# human decides. (wild-violet's is "the little purple flowers next spring".)
SEASONAL_PROSE = ("spring", "summer", "fall", "autumn", "winter", "next year",
                  "late season", "early season")

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


def covered_ids(questions, records_by_type=None):
    """Entity ids that already have a question (active OR resolved) — skip these.

    Two directions, because the link is not reliably bidirectional. `entityRef`
    points card → record; a weed's `momConfirm.questionId` points record → card.
    **Reading only the first would have re-drafted crabgrass**: its card
    `q-fairway-grass-seedheads` carries `entityRef: plant/fairway-meadow` (the
    meadow the seed-heads are IN), while the crabgrass record names that same card
    as its own confirmation. Both statements are true and neither is wrong — they
    just anchor to different things — so a harvester that trusts one direction
    silently duplicates a question Mom is already being asked.
    """
    ids = {ref["id"] for q in questions
           if (ref := (q.get("entityRef") or {})).get("id")}
    known = {q.get("id") for q in questions}
    for recs in (records_by_type or {}).values():
        for r in recs:
            qid = ((r.get("momConfirm") or {}).get("questionId"))
            if qid and qid in known and r.get("id"):
                ids.add(r["id"])
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


def harvest(records_by_type, questions, today_mmdd, zones_by_id=None):
    """Draft candidates from EVERY cardable domain's own uncertainty markers.

    ⭐ REWRITTEN 2026-08-02 (M1). The old loop walked `plants` and hardcoded the
    `variety` and `bloom` field shapes, which is why the BACKLOG's "plants-only
    site" understated the problem: repointing it at weeds.json would have found
    ZERO, because weeds admit a guess top-level and it could only read the nested
    plant shape. Three weeds were sitting explicitly marked
    `confidence: inferred` + `status: needs-confirmation` — raising their hands in
    a vocabulary this file could not hear.

    It now asks `momlib.markers()` "does this record admit a guess?" and lets the
    marker path pick a template. Adding a domain is a declaration in
    `momlib.DOMAINS`, not an edit here.
    """
    zones_by_id = zones_by_id or {}
    covered = covered_ids(questions, records_by_type)
    cands = []
    for dtype, records in sorted(records_by_type.items()):
        for rec in records:
            rid = rec.get("id")
            if not rid or rid in covered:
                continue
            name = short_name(rec)
            where = where_phrase(rec, zones_by_id)

            for mk in momlib.markers(rec, dtype):
                if not mk["askable"]:
                    continue
                kind = MARKER_TEMPLATE.get(mk["path"])
                if not kind:
                    continue          # a marker with no template is not yet askable
                owner, warn, extra = mk["owner"], None, {}

                if kind == "bloom":
                    dates = owner.get("dates")
                    if not isinstance(dates, list) or not any(
                            range_active(r, today_mmdd) for r in dates):
                        continue      # out of window — "is it in flower?" is unanswerable
                    prompt = TEMPLATES["bloom"].format(name=name, where=where)
                    why = f"bloom is {mk['confidence']} + in-window now ({owner.get('window','')})"
                    # Emitted EXPLICITLY so the JSON is self-describing. The viewer
                    # defaults a missing `later` to "I haven't looked", which meant
                    # the served card and the record disagreed about what her third
                    # option said — and a reader of questions.json concluded there
                    # was no third button at all. There was. Say it in the file.
                    extra = {"labels": dict(BLOOM_LABELS)}
                elif kind == "variety":
                    if not owner.get("value"):
                        continue
                    note = owner.get("note")
                    prompt = TEMPLATES["variety"].format(
                        name=name, variety=owner["value"],
                        note=f" ({note})" if note else "", where=where)
                    why = f"variety '{owner['value']}' is {mk['confidence']} + askable"
                    # a "no" on an ID owes the real name; keeps the variety-confirm voice
                    extra = {"correctionPrompt": "What is it, then? (optional)"}
                else:  # identity — the record names its own observable
                    confirm_by = ((rec.get("momConfirm") or {}).get("confirmBy") or "").strip()
                    if not confirm_by:
                        continue      # no observable = no honest question to ask
                    prompt = TEMPLATES["identity"].format(
                        name=name, where=where,
                        confirm_by=confirm_by[0].upper() + confirm_by[1:] + "?")
                    why = f"{dtype} identity is {mk['confidence']} + {rec.get('status','askable')}"
                    if any(w in confirm_by.lower() for w in SEASONAL_PROSE):
                        warn = (f"its confirmBy names a SEASON — \"{confirm_by}\" — so the "
                                f"observable may not exist today. Check before serving.")
                    extra = {"correctionPrompt": "What is it, then? (optional)"}

                cands.append({
                    "type": kind, "domain": dtype,
                    "id": f"q-{rid}-{kind}" if kind != "identity" else f"q-weed-{rid}",
                    "entityId": rid, "prompt": prompt, "why": why,
                    "warn": warn, "extra": extra,
                })
    return cands


def to_question(cand, created):
    """Shape a candidate into a questions.json entry (drafted, NOT live)."""
    q = {
        "id": cand["id"],
        "kind": "confirm",
        "answerMode": "yesno",
        "prompt": cand["prompt"],
        "entityRef": {"type": cand["domain"], "id": cand["entityId"]},
        "createdAt": created,
        "active": False,
        "_source": "harvest",
        # The fold target is the CONFIDENCE FLAG the answer would flip, which for
        # an identity card is the record's own top-level `confidence` — the same
        # key momlib.FOLD_FIELDS already knows. Never the template name.
        "_foldTarget": "confidence" if cand["type"] == "identity" else cand["type"],
        "_draftNote": "Drafted by harvest-questions.py from a canon uncertainty marker. Edit the prompt for voice, then set active:true to serve it.",
    }
    q.update(cand.get("extra") or {})  # per-type labels / correctionPrompt
    return q


def load_records():
    """Every domain the manifest marks cardable — not a hardcoded file list.

    ⭐ EXTRACTED 2026-08-02, and the extraction is the fix. M1 changed `harvest()`'s
    first argument from a plants LIST to a domain-keyed DICT and updated the only
    caller it could see — this file's own `main()`. `mom-queue-watch.py` was still
    passing `plants`, so both scheduled runs after M1 died on
    `'list' object has no attribute 'values'` and Mom's loop went quiet while
    looking merely idle.

    The obvious patch — build `{"plant": plants}` at the call site — would have
    restored the count and silently re-created the bug M1 existed to kill: a
    second producer that can only see plants, blind to the three askable weeds.
    So the loader is ONE function both callers import, for the same reason
    `momlib.question_state()` is one function: three copies of a `_load()` shim
    and three definitions of "pending" already cost this repo a real wrong claim.
    """
    records_by_type = {}
    for dtype, dom in momlib.DOMAINS.items():
        if not dom.cardable:
            continue
        got = momlib.load_json(dom.file).get(dom.key)
        if isinstance(got, list):
            records_by_type[dtype] = [r for r in got if isinstance(r, dict)]
    return records_by_type


def main():
    ap = argparse.ArgumentParser(description="Harvest candidate Mama's-Perspective cards from canon uncertainty.")
    ap.add_argument("--today", default=str(dt.date.today()), help="YYYY-MM-DD override for the in-bloom filter")
    ap.add_argument("--append-drafts", action="store_true", help="Append candidates to questions.json as active:false drafts")
    args = ap.parse_args()

    today = dt.date.fromisoformat(args.today)
    records_by_type = load_records()
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

    cands = harvest(records_by_type, questions, mmdd(today), zones_by_id)

    if not cands:
        print("No new candidates — every askable uncertainty is already covered or out of season.")
        return 0

    print(f"=== {len(cands)} candidate card(s) — your approval gates each (nothing is live) ===\n")
    for c in cands:
        print(f"[{c['domain']}·{c['type']}] {c['id']}   ({c['why']})")
        print(f"    {c['prompt']}\n")
        if c.get("warn"):
            print(f"    \u26a0\ufe0f  {c['warn']}\n")
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
