#!/usr/bin/env python3
"""place-claims.py — the PLACE-CLAIM register: shared engine prose that speaks of a place, classified and ratcheted.
    python3 tools/place-claims.py            # sync: every place-claiming SHARED sentence in the ledger gets a row (new → unclassified); report
    python3 tools/place-claims.py --check    # exit 1 if any row is unclassified, or if the count still rendering at the condo GREW past the baseline
    python3 tools/place-claims.py --list     # the rows, for Paul's read

[paul-stated 2026-09-04 ~5:00 AM ET]: "that should be part of this document we're building that tracks what's unique and
deterministically updated and linked to what for each location. We need to be sure that the condo doesn't have references
to, like, chestnut canopy — that's not necessarily true. Let's figure out a way to track this and approach it systematically."

INPUT  .private/condo-falsifier/uniqueness-ledger.json — `tools/uniqueness-ledger.py` over the Fernwood build and the condo
       build (its `shared` list: sentences BOTH render). A sentence is a PLACE CLAIM when it carries a place word (slope,
       ridge, the lake, this place, the house, mountain, canopy, here …) — the same predicate the ledger prints.
REGISTER engine/place-claims.json (TRACKED): one row per claim, keyed by a stable hash of the sentence:
       class ∈ unclassified · engine-neutral (fine anywhere: "here" means wherever you are) · instance-prose (move into
       that estate's canon) · reword (engine copy that must stop naming a place). `note` is the reason. The classes are
       Paul's or the content steward's to set; this tool never sets one.
THE RATCHET: `baseline.renderingAtCondo` is the count of instance-prose/reword rows the condo STILL renders. --check is red if
       it grew — a new place claim reached the engine — and green when it falls. It starts at today's truth (47-ish), which
       is a truthful red on the moves, not on the tool: the moves ride the migration; the ratchet keeps them from multiplying.
"""
import argparse, hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(ROOT, ".private", "condo-falsifier", "uniqueness-ledger.json")
REGISTER = os.path.join(ROOT, "engine", "place-claims.json")
PLACE = re.compile(r"\b(slope|property|this place|the lake|the house|ridge|mountain|here|canopy|the porch|the valley|thermal belt|the pond|the creek|the woods|the road|the driveway|the panel|the garage|the yard|the lawn|the beds|on this|our (?:land|slope|ridge|lake|house|woods))\b", re.I)
CLASSES = ("unclassified", "engine-neutral", "instance-prose", "reword")

def key(s): return hashlib.sha1(s.strip().encode("utf-8")).hexdigest()[:10]

def load_register():
    if os.path.exists(REGISTER):
        return json.load(open(REGISTER, encoding="utf-8"))
    return {"_meta": {"purpose": "Place claims in SHARED engine prose — see tools/place-claims.py", "declared": "2026-09-04"}, "baseline": {"renderingAtCondo": None, "setOn": None}, "claims": {}}

def suspects():
    if not os.path.exists(LEDGER):
        raise SystemExit("⛔ no ledger at %s — run tools/uniqueness-ledger.py <fernwood> <condo> --out %s first" % (LEDGER, LEDGER))
    led = json.load(open(LEDGER, encoding="utf-8"))
    return sorted({s.strip() for s in led.get("shared", []) if PLACE.search(s)})

def sync(reg, sus):
    new = 0
    for s in sus:
        k = key(s)
        if k not in reg["claims"]:
            reg["claims"][k] = {"text": s, "class": "unclassified", "note": "", "firstSeen": __import__("datetime").date.today().isoformat()}; new += 1
    for k, row in reg["claims"].items():
        row["rendersAtCondo"] = row["text"] in set(sus)
    return new

def save(reg):
    reg["claims"] = dict(sorted(reg["claims"].items(), key=lambda kv: kv[1]["text"].lower()))
    json.dump(reg, open(REGISTER, "w", encoding="utf-8"), indent=1, ensure_ascii=False); open(REGISTER, "a").write("\n")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    reg = load_register(); sus = suspects(); new = sync(reg, sus)
    rows = reg["claims"]
    bad_class = [r for r in rows.values() if r["class"] not in CLASSES]
    uncl = [r for r in rows.values() if r["class"] == "unclassified"]
    moving = [r for r in rows.values() if r["class"] in ("instance-prose", "reword") and r["rendersAtCondo"]]
    still = len([r for r in rows.values() if r["rendersAtCondo"] and r["class"] != "engine-neutral"])
    base = reg["baseline"]["renderingAtCondo"]
    if base is None:
        reg["baseline"] = {"renderingAtCondo": still, "setOn": __import__("datetime").date.today().isoformat()}; base = still
    if not a.check:
        save(reg)
    print("place-claims — %d claim(s) in shared prose · %d new · %d unclassified · %d classed to move and still at the condo · baseline %d (set %s)"
          % (len(rows), new, len(uncl), len(moving), base, reg["baseline"]["setOn"]))
    if a.list:
        for r in rows.values():
            print("  %-15s %s %s" % (r["class"], "●" if r["rendersAtCondo"] else "○", r["text"][:150]))
    if a.check:
        rc = 0
        if bad_class: print("🔴 %d row(s) carry a class outside %s" % (len(bad_class), CLASSES)); rc = 1
        if uncl: print("🔴 %d place claim(s) UNCLASSIFIED — Paul or the content steward classes them; the tool will not" % len(uncl)); rc = 1
        if still > base: print("🔴 RATCHET: %d non-neutral place claim(s) render at the condo, baseline %d — a NEW place claim reached shared engine prose" % (still, base)); rc = 1
        if rc == 0: print("✅ every place claim is classed; %d still render at the condo (baseline %d) — falls only" % (still, base))
        return rc
    return 0

if __name__ == "__main__":
    sys.exit(main())
