#!/usr/bin/env python3
"""scan-mentions.py — the ANALYZE leg, done deterministically.

The audit's honest scorecard on 2026-07-26: recognition was automated across
every channel, but *analysis* existed only for the confirm tap (which is an
enum, so `question_state()` is the whole analysis). Her field notes, her Garden
Guru questions and her voice captures were recognized, timestamped, and then
read by a human or not at all.

**This is the analysis that needs no model.** It answers one question:

    Which things in the record has she been TALKING about —
    and of those, which ones does the record admit it is unsure of?

That intersection is the highest-value question the loop can ask, because it is
BOTH channels at once:
  · ANALYZE      — her free text becomes structured signal (which entities, how
                   often, how recently) without a model reading it for meaning.
  · GENERATE Qs  — an entity she raised herself, that canon marks `inferred`,
                   is a clarification gap she is ALREADY thinking about.

⭐ WHY THIS SHAPE AND NOT A HARVEST. `harvest-questions.py` seeds cards from OUR
uncertainty markers, sweeping canon for anything unconfirmed. BACKLOG A3 records
the structural critique: it is a verdict-ask factory — it can only ever produce
"is our guess right?", the one format her stated fear of being wrong blocks
(offered 35 → viewed 33 → tapped 1 → answered 1). This tool inverts the seed:
it starts from HER words and asks what she has already shown interest in. Same
mechanism, opposite direction, and it is the concrete form of Paul's standing
instruction to *"seed her cards from her last input instead."*

AI BOUNDARY — this is counting, not reading. Word-boundary string matching
against canon's own entity names. No model, no inference about meaning, no
sentiment, no summarising. It cannot paraphrase her and it never writes a card:
it prints candidates for Paul, and card wording reaches Mom so it stays
human-authored (CLAUDE.md "authored content"). Her verbatim text never leaves
the terminal — nothing here writes it to a tracked file.

It also advances the `observations` read clock, because displaying her notes to
a human IS the act of reading that channel.

Usage:
    python3 tools/scan-mentions.py
    python3 tools/scan-mentions.py --days 90
    python3 tools/scan-mentions.py --quiet     # only the clarification gaps
"""
import argparse
import datetime as dt
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402

# Canon files that describe THINGS ON THE PROPERTY she might mention.
SOURCES = [
    ("plants.json", "plants", "plant"),
    ("weeds.json", "weeds", "weed"),
    ("birds.json", "species", "bird"),
    ("mammals.json", "species", "mammal"),
    ("amphibians.json", "species", "amphibian"),
    ("snakes.json", "species", "snake"),
    ("lizards.json", "species", "lizard"),
    ("candidates.json", "candidates", "candidate"),
]

# Fields that carry an honesty marker we could ask her to settle.
UNSURE_PATHS = [
    ("variety", "confidence", "which variety it is"),
    ("bloom", "confidence", "when it actually blooms here"),
    (None, "confidence", "the identification itself"),
]

STOP = {"the", "and", "a", "of", "in", "it", "is", "to"}

# Head nouns too generic to match on alone. Without this, "Pitcher Plant" also
# matches the bare word "plant" and every field note about planting anything
# lights up the pitcher plant. The head-noun shortcut is only useful when the
# head noun is DISTINCTIVE ("stiltgrass", "laurel"), never when it's a category.
GENERIC_HEADS = {
    "plant", "plants", "flower", "flowers", "tree", "trees", "grass", "grasses",
    "bush", "bushes", "shrub", "shrubs", "weed", "weeds", "vine", "vines",
    "berry", "berries", "leaf", "leaves", "wood", "woods", "seed", "seeds",
    "bird", "birds", "snake", "snakes", "lizard", "lizards", "frog", "frogs",
    "salamander", "toad", "sedge", "rush", "iris", "fern", "ferns", "hybrid",
    "common", "eastern", "western", "northern", "southern", "american",
}


def entity_terms(e):
    """Every string a person might plausibly type for this entity."""
    terms = set()
    for key in ("name", "scientificName", "commonName"):
        v = e.get(key)
        if isinstance(v, str) and len(v) > 3:
            terms.add(v.strip())
    v = e.get("variety")
    if isinstance(v, dict) and isinstance(v.get("value"), str):
        terms.add(v["value"].strip().strip("'\""))
    # A two-word name also matches on its distinctive head noun ("Japanese
    # stiltgrass" → "stiltgrass"), which is how people actually talk.
    for t in list(terms):
        parts = [p for p in re.split(r"[\s'\"]+", t) if len(p) > 4 and p.lower() not in STOP]
        if len(parts) > 1 and parts[-1].lower() not in GENERIC_HEADS:
            terms.add(parts[-1])
    return {t for t in terms if len(t) > 3}


def unsure_about(e):
    """What canon admits it does not know about this entity."""
    out = []
    for block, field, human in UNSURE_PATHS:
        node = e.get(block) if block else e
        if not isinstance(node, dict):
            continue
        val = node.get(field)
        if isinstance(val, str) and val.lower() != "verified":
            askable = node.get("askable")
            out.append({"what": human, "confidence": val,
                        "askable": askable is not False,
                        "where": f"{block + '.' if block else ''}{field}"})
    return out


def load_canon():
    items = []
    for fname, key, kind in SOURCES:
        data = momlib.load_json(fname)
        for e in (data.get(key) or []):
            if not isinstance(e, dict) or not e.get("id"):
                continue
            items.append({"id": e["id"], "kind": kind, "file": fname,
                          "name": e.get("name") or e["id"],
                          "terms": entity_terms(e), "unsure": unsure_about(e)})
    return items


def gather_her_text(token, days):
    """Every place she writes free text. Returns [(source, ts, text)]."""
    out = []
    today = dt.date.today()
    # The Worker caps the feedback range; ask for at most 60 days there.
    fb_start = str(today - dt.timedelta(days=min(days, 60)))
    start, end = str(today - dt.timedelta(days=days)), str(today)
    try:
        data = momlib._get("/api/feedback", token, {"start": fb_start, "end": end})
        for r in momlib.flatten(data):
            if momlib.carries_words(r):
                out.append(("note", r.get("ts"), r.get("note")))
    except Exception as e:  # noqa: BLE001
        print(f"  (couldn't read /api/feedback: {e})", file=sys.stderr)
    try:
        data = momlib._get("/api/observations", token)
        for r in (data.get("observations") or []):
            body = (r.get("body") or "").strip()
            if body:
                out.append(("field note", r.get("createdAt") or r.get("date"), body))
    except Exception as e:  # noqa: BLE001
        print(f"  (couldn't read /api/observations: {e})", file=sys.stderr)
    # Voice captures, once transcribed. UNVERIFIED model reads — flagged as such
    # and never treated as her exact words.
    d = os.path.join(momlib.ROOT, ".private", "mom-zone-audio")
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".transcript.txt"):
                try:
                    with open(os.path.join(d, fn), encoding="utf-8") as f:
                        body = f.read().split("-" * 20)[-1].strip()
                    if body:
                        out.append(("voice ⚠️unverified", fn[:10], body))
                except OSError:
                    pass
    out.sort(key=lambda x: x[1] or "")
    return out


def find_mentions(canon, texts):
    hits = {}
    for source, ts, text in texts:
        low = " " + re.sub(r"[^a-z0-9']+", " ", (text or "").lower()) + " "
        for e in canon:
            for term in e["terms"]:
                t = re.sub(r"[^a-z0-9']+", " ", term.lower()).strip()
                if not t:
                    continue
                if re.search(r"(?<![a-z])" + re.escape(t) + r"e?s?(?![a-z])", low):
                    rec = hits.setdefault(e["id"], {"entity": e, "where": []})
                    rec["where"].append((source, ts, term))
                    break
    return hits


def main():
    ap = argparse.ArgumentParser(description="What has Mom been talking about, and what is canon unsure of?")
    ap.add_argument("--days", type=int, default=90)
    ap.add_argument("--quiet", action="store_true", help="Only the clarification gaps")
    args = ap.parse_args()

    token = momlib.resolve_token()
    if not token:
        print("error: no token.", file=sys.stderr)
        return 2

    canon = load_canon()
    texts = gather_her_text(token, args.days)
    if not texts:
        print("Nothing of hers in free text in this window.")
        return 0
    hits = find_mentions(canon, texts)

    gaps = {k: v for k, v in hits.items() if v["entity"]["unsure"]}
    settled = {k: v for k, v in hits.items() if not v["entity"]["unsure"]}

    print(f"\nScanned {len(texts)} piece(s) of her free text against "
          f"{len(canon)} canon entries.  (deterministic string match — no model)\n")

    if gaps:
        print("⭐ SHE RAISED IT, AND THE RECORD ADMITS IT'S UNSURE — ask HER, not the sweep")
        print("   (a card seeded from her own input, not from our uncertainty sweep)\n")
        for v in sorted(gaps.values(), key=lambda x: -len(x["where"])):
            e = v["entity"]
            print(f"  • {e['name']}  ({e['kind']} · {e['file']} `{e['id']}`)")
            for u in e["unsure"]:
                flag = "" if u["askable"] else "   [not marked askable]"
                print(f"      canon is unsure of: {u['what']}  ({u['where']} = {u['confidence']}){flag}")
            for src, ts, term in v["where"][:3]:
                print(f"      she wrote it in a {src} — {momlib.et_str(ts, with_time=False)} (matched \"{term}\")")
            print()
    else:
        print("  No overlap between what she's raised and what canon is unsure of.\n")

    if settled and not args.quiet:
        print("She has also mentioned (canon already settled — corroboration, no ask needed):")
        print("  " + ", ".join(sorted(v["entity"]["name"] for v in settled.values())) + "\n")

    unmatched = len(texts) - len({id(t) for t in texts if any(
        any(s[1] == t[1] for s in v["where"]) for v in hits.values())})
    if unmatched > 0 and not args.quiet:
        print(f"⚠️  {unmatched} piece(s) of her text matched NOTHING in canon.")
        print("   That is the interesting residue — it's where a thing the record")
        print("   doesn't know about yet would hide (moss was exactly this).")
        print("   This tool cannot read it for meaning by design. Read it yourself:")
        print("     python3 tools/read-mom-feedback.py\n")

    # Displaying her notes to a human IS reading this channel.
    newest = max((t[1] or "") for t in texts)
    if newest:
        momlib.mark_channel_read("observations", newest, by="scan-mentions.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
