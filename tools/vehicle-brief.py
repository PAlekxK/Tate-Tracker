#!/usr/bin/env python3
"""
vehicle-brief.py — BEAT 0 for any fleet/maintenance work.

Resolve a loose spoken name ("the 200 blue thunder", "mom's bike", "the bronco")
to exactly one machine in vehicles.json, then print everything a session needs
BEFORE it starts diagnosing: specs, provenance warnings, open mechanical items,
live restoration queue, recent service history, techniques — and, the part this
tool exists for, a PROVENANCE CHECK on every manual attached to that machine.

⭐ WHY IT EXISTS (2026-08-30, `paul-stated`).
A session diagnosed Blue Thunder's starting fault out of
`manuals/text/dr200s-2017-service.txt` and told Paul to kick-start a bike that has
no kickstarter. The manual's own line 3 reads "SUZUKI DR200SE" — a different model.
`manuals/INDEX.md` already titled it correctly, behind a 🟡 marker. It was read past.

The lesson is what shaped this tool: **careful reading of the wrong document produces
confident wrong answers.** The session DID cross-check spec tables and quote line
numbers. So a beat 0 defined as "familiarise yourself with the vehicle" would not have
caught it — only a mechanical comparison would. Hence:

  THE FILENAME IS THE CONTAINER. THE MANUAL'S OWN FOREWORD IS THE PAYLOAD.

`--check` compares the model designator a manual NAMES IN ITS OWN TEXT against the
model the vehicle card claims, and flags a mismatch. That is [[reference_match_payload_not_container]]
implemented as a check rather than remembered as a rule.

STATED LIMITS — do not oversell this (it converts a wrong answer into a flagged
uncertainty; it does not produce a right one):
  · It cannot tell you WHICH specs actually differ between two sibling models. It
    raises the risk; a human resolves it against a correct source.
  · It reads EXTRACTED text, so a sparse or image-only scan may name no model at
    all. That reports as UNKNOWN, never as a pass — a document that could not be
    checked must never look like one that passed.
  · It does not judge applicability. INDEX.md's confidence marker is reprinted, never
    re-derived.

Reuses `manuals-search.py`'s INDEX parser and longest-prefix resolver rather than
re-deriving them — one source, N readers.

USAGE
  python3 tools/vehicle-brief.py "the 200 blue thunder"
  python3 tools/vehicle-brief.py bronco --full      # full service history
  python3 tools/vehicle-brief.py --check            # provenance sweep, WHOLE fleet
  python3 tools/vehicle-brief.py --list
  python3 tools/vehicle-brief.py --selftest

EXIT  0 clean · 1 a human is needed (provenance flag, or an ambiguous name) · 2 usage
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.dirname(HERE)
TEXT_DIR = os.path.join(REPO, "manuals", "text")

try:
    from importlib.machinery import SourceFileLoader
    _ms = SourceFileLoader("manuals_search",
                           os.path.join(HERE, "manuals-search.py")).load_module()
    load_index, load_vehicles, resolve_machine = (
        _ms.load_index, _ms.load_vehicles, _ms.resolve_machine)
except Exception as e:                                    # pragma: no cover
    sys.exit(f"vehicle-brief: cannot reuse manuals-search.py ({e}). "
             "That file is the one authority on INDEX parsing; fix it rather than "
             "re-deriving the logic here.")

# A model designator: letters, then digits, optionally more. DR200SE, DR-Z400S,
# YTH24V54, F150, G22A, BST31SS. Deliberately loose — precision comes from
# comparing against the vehicle's OWN tokens, not from this pattern being clever.
_MODEL = re.compile(r"\b[A-Z][A-Z\-]{0,6}\d{2,4}[A-Z0-9\-]{0,6}\b")
_STOP = {"MANUAL", "SECTION", "PAGE", "SUZUKI", "FORD", "YAMAHA", "HUSQVARNA",
         "ECHO", "STIHL", "KOBALT", "GENERAC", "HOMELITE", "EPA", "USA", "VIN"}
FOREWORD_LINES = 40


def norm(s):
    return re.sub(r"[^A-Z0-9]", "", (s or "").upper())


def vehicle_tokens(v):
    """Model designators the CARD claims, from name/trim/id — normalised."""
    out = set()
    for field in (v.get("name"), v.get("trim"), v.get("nickname")):
        for m in _MODEL.finditer((field or "").upper()):
            if m.group() not in _STOP:
                out.add(norm(m.group()))
    # the id's model half, e.g. "dr200s-2017" -> DR200S
    head = (v.get("id") or "").split("-")[0]
    if re.search(r"\d", head):
        out.add(norm(head))
    return {t for t in out if len(t) >= 3}


def foreword_models(stem):
    """Model designators the DOCUMENT names in its own opening lines."""
    path = os.path.join(TEXT_DIR, stem + ".txt")
    if not os.path.exists(path):
        return None, ""
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            head = [next(fh, "") for _ in range(FOREWORD_LINES)]
    except Exception:
        return None, ""
    blob = "".join(head)
    found = {norm(m.group()) for m in _MODEL.finditer(blob.upper())
             if m.group() not in _STOP}
    return {t for t in found if len(t) >= 3}, blob


def classify(card_tokens, doc_tokens):
    """MATCH · MISMATCH · UNKNOWN.

    MISMATCH is deliberately narrow: the document names something that is a
    NEAR-MISS of the card's model — one is a prefix of the other but they are not
    equal (DR200S vs DR200SE). A document naming an unrelated part number is not a
    mismatch, and calling it one would train the reader to skim the flag.
    """
    if not doc_tokens:
        return "UNKNOWN", None
    if card_tokens & doc_tokens:
        return "MATCH", None
    for c in card_tokens:
        for d in doc_tokens:
            if d.startswith(c) or c.startswith(d):
                return "MISMATCH", d
    # THIRD TIER, added 2026-08-30 on the sweep's first run. The document DOES name
    # models and NONE of them relates to this card. That is not "unknown" — it is a
    # different-document smell, and folding it into UNKNOWN hid the corpus's own
    # known-bad case (husqvarna-mower-yth24v54, a YTH24V54 tractor manual filed
    # against a confirmed Z254F). Kept OUT of MISMATCH deliberately: a manual that
    # merely quotes part numbers would otherwise inflate the count that must stay
    # trustworthy. Reported, never graded.
    if card_tokens:
        return "NO-OVERLAP", "/".join(sorted(doc_tokens)[:3])
    return "UNKNOWN", None


def manuals_for(vid, vehicles):
    if not os.path.isdir(TEXT_DIR):
        return []
    return sorted(s[:-4] for s in os.listdir(TEXT_DIR) if s.endswith(".txt")
                  and resolve_machine(s[:-4], vehicles) == vid)


def check_manuals(v, vehicles, idx):
    """-> list of (stem, verdict, named, confidence, doc_title)"""
    card = vehicle_tokens(v)
    rows = []
    for stem in manuals_for(v["id"], vehicles):
        doc_tokens, _ = foreword_models(stem)
        if doc_tokens is None:
            rows.append((stem, "NO-TEXT", None, idx.get(stem, {}).get("confidence", ""),
                         idx.get(stem, {}).get("doc", "")))
            continue
        verdict, named = classify(card, doc_tokens)
        rows.append((stem, verdict, named, idx.get(stem, {}).get("confidence", ""),
                     idx.get(stem, {}).get("doc", "")))
    return rows


# ─────────────────────────── name resolution ───────────────────────────
def score(query, v):
    """Token overlap against everything the machine is called."""
    q = [t for t in re.split(r"[^a-z0-9]+", query.lower()) if t]
    hay = " ".join(str(v.get(k) or "") for k in
                   ("id", "name", "nickname", "trim", "category", "doorLabel")).lower()
    hay_t = set(re.split(r"[^a-z0-9]+", hay))
    s = 0
    for t in q:
        if t in hay_t:
            s += 3                      # whole-token hit
        elif len(t) >= 3 and t in hay:
            s += 2                      # substring ("200" inside "dr200s")
    if norm(query) and norm(query) == norm(v.get("nickname")):
        s += 10
    return s


def resolve(query, vehicles):
    ranked = sorted(((score(query, v), v) for v in vehicles.values()),
                    key=lambda p: (-p[0], p[1]["id"]))
    ranked = [(s, v) for s, v in ranked if s > 0]
    return ranked


# ─────────────────────────────── render ────────────────────────────────
def bar(t):
    print(f"\n\033[1m{t}\033[0m" if sys.stdout.isatty() else f"\n{t}")
    print("─" * min(len(t), 78))


def brief(v, vehicles, idx, full=False):
    flagged = False
    name = f"{(v.get('emoji') or '').strip()} {v.get('name')}".strip()
    nick = v.get("nickname")
    print(f"\n{name}" + (f'  —  "{nick}"' if nick else ""))
    print(f"id: {v['id']} · {v.get('category','?')} · status: {v.get('status','?')}")

    for k, val in v.items():
        if k.startswith("_") and "warn" in k.lower():
            flagged = True
            print(f"\n🚨 {k}\n   " + "\n   ".join(_wrap(str(val), 74)))

    bar("SPECS")
    for k, val in (v.get("specs") or {}).items():
        print(f"  {k:16s} {val}")

    bar("MANUALS — provenance check")
    rows = check_manuals(v, vehicles, idx)
    if not rows:
        print("  (no manual on disk for this machine)")
    for stem, verdict, named, conf, doc in rows:
        mark = {"MATCH": "✓", "MISMATCH": "🔴", "NO-OVERLAP": "🟠",
                "UNKNOWN": "❓", "NO-TEXT": "❓"}[verdict]
        print(f"  {mark} {stem}  [{conf or '—'}]  {doc[:52]}")
        if verdict == "MISMATCH":
            flagged = True
            print(f"      🔴 THE DOCUMENT NAMES **{named}**, THE VEHICLE IS "
                  f"**{'/'.join(sorted(vehicle_tokens(v))) or '?'}**.")
            print("      Treat every value taken from it as `inferred`, not `verified`.")
        elif verdict == "NO-OVERLAP":
            flagged = True
            print(f"      🟠 its opening pages name {named} and NOTHING matching this"
                  " machine — check it is the right document at all.")
        elif verdict in ("UNKNOWN", "NO-TEXT"):
            print("      ❓ its opening pages name no model we can match — NOT a pass.")

    for key, title in (("openMechanicalItems", "OPEN MECHANICAL ITEMS"),):
        block = v.get(key)
        if block:
            items = block.get("items", block) if isinstance(block, dict) else block
            bar(f"{title} ({len(items)})")
            for it in items:
                print(f"  • {it.get('item')}")
                if it.get("status"):
                    print("      " + "\n      ".join(_wrap(it["status"], 72)[:2]))
                if it.get("check"):
                    print("      check: " + _wrap(it["check"], 66)[0])

    live = [r for r in (v.get("restoration") or []) if r.get("status") != "done"]
    if live:
        bar(f"RESTORATION — live ({len(live)} of {len(v.get('restoration') or [])})")
        for r in live:
            print(f"  • [{r.get('status','?')}] {r.get('item')}")

    sh = v.get("serviceHistory") or []
    if sh:
        show = sh if full else sh[:4]
        bar(f"SERVICE HISTORY — {len(show)} of {len(sh)}"
            + ("" if full else "  (--full for all)"))
        for e in show:
            print(f"  {e.get('date','?')}  {e.get('summary','')[:88]}")

    tq = v.get("techniques") or []
    if tq:
        bar(f"TECHNIQUES ({len(tq)})")
        for t in tq:
            print(f"  • {t.get('name')}")

    return flagged


def _wrap(s, w):
    out, line = [], ""
    for word in str(s).split():
        if len(line) + len(word) + 1 > w:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out or [""]


# ─────────────────────────────── selftest ──────────────────────────────
def selftest():
    """Both directions, against the real corpus. A check proven only to FAIL is
    not proven; the positive control is the half that is usually skipped."""
    vehicles, idx = load_vehicles(), load_index()
    ok = True

    def check(nm, cond):
        nonlocal ok
        print(("  ✓ " if cond else "  ✗ ") + nm)
        ok = ok and bool(cond)

    check("vehicles.json loaded (>10 machines)", len(vehicles) > 10)
    check("INDEX.md parsed (>15 rows)", len(idx) > 15)

    # POSITIVE CONTROL — the exact failure this tool was built for MUST fire.
    dr = vehicles.get("dr200s-2017")
    rows = {r[0]: r for r in check_manuals(dr, vehicles, idx)} if dr else {}
    r = rows.get("dr200s-2017-service")
    check("POSITIVE: dr200s-2017-service flags MISMATCH", r and r[1] == "MISMATCH")
    check("POSITIVE: and it names DR200SE as what the doc claims",
          r and r[2] == "DR200SE")

    # NEGATIVE CONTROL — a correctly-held manual must NOT fire, or a pass is free.
    dz = vehicles.get("drz400s-2001")
    rz = {x[0]: x for x in check_manuals(dz, vehicles, idx)} if dz else {}
    q = rz.get("drz400s-2001-service")
    check("NEGATIVE: drz400s-2001-service does NOT flag", q and q[1] == "MATCH")

    # POSITIVE CONTROL 2 — the corpus's other known-bad document, which the
    # near-miss rule alone could not see (wholly different model name).
    hq = vehicles.get("husqvarna-mower")
    rh = {x[0]: x for x in check_manuals(hq, vehicles, idx)} if hq else {}
    check("POSITIVE: the wrong-chassis Husqvarna manual is flagged (NO-OVERLAP)",
          any(x[1] == "NO-OVERLAP" for x in rh.values()))

    # classify() unit checks — the near-miss rule is the whole discriminator
    check("classify: exact match -> MATCH",
          classify({"DR200S"}, {"DR200S"})[0] == "MATCH")
    check("classify: near-miss  -> MISMATCH",
          classify({"DR200S"}, {"DR200SE"})[0] == "MISMATCH")
    check("classify: unrelated  -> NO-OVERLAP (never MISMATCH)",
          classify({"DR200S"}, {"BST31SS"})[0] == "NO-OVERLAP")
    check("classify: no tokens  -> UNKNOWN (silence is never a pass)",
          classify({"DR200S"}, set())[0] == "UNKNOWN")

    # resolution — loose speech must land, and ambiguity must stay visible
    ranked = resolve("the 200 blue thunder", vehicles)
    check("resolve: 'the 200 blue thunder' -> dr200s-2017",
          ranked and ranked[0][1]["id"] == "dr200s-2017")
    check("resolve: a nonsense name resolves to NOTHING",
          not resolve("zzzzqqq", vehicles))

    print("\n" + ("selftest PASSED" if ok else "selftest FAILED"))
    return 0 if ok else 1


def sweep(vehicles, idx):
    """Whole-fleet provenance sweep. Prints its own denominator."""
    bad = nov = unk = checked = 0
    print("MANUAL PROVENANCE SWEEP — every machine, every document\n")
    for v in vehicles.values():
        for stem, verdict, named, conf, doc in check_manuals(v, vehicles, idx):
            checked += 1
            if verdict == "MISMATCH":
                bad += 1
                print(f"  🔴 {stem}  [{conf or '—'}]")
                print(f"       names {named} · card is {v.get('name')}")
            elif verdict == "NO-OVERLAP":
                nov += 1
                print(f"  🟠 {stem}  [{conf or '—'}]")
                print(f"       names {named} · nothing matching {v.get('name')}")
            elif verdict in ("UNKNOWN", "NO-TEXT"):
                unk += 1
    print(f"\n  {checked} document(s) checked across {len(vehicles)} machine(s): "
          f"{bad} MISMATCH · {nov} NO-OVERLAP · {unk} unverifiable · "
          f"{checked-bad-nov-unk} match.")
    print("  ❓ unverifiable = the extracted text names no model we can match. "
          "That is NOT a pass —\n     a sparse scan and a correct document look "
          "identical to this check.")
    return 1 if (bad or nov) else 0


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("query", nargs="*", help="loose name of the machine")
    ap.add_argument("--full", action="store_true", help="full service history")
    ap.add_argument("--check", action="store_true", help="fleet-wide provenance sweep")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    vehicles, idx = load_vehicles(), load_index()
    if not vehicles:
        sys.exit("vehicle-brief: vehicles.json unreadable")
    if a.check:
        return sweep(vehicles, idx)
    if a.list or not a.query:
        for v in vehicles.values():
            print(f"  {v['id']:30s} {(v.get('nickname') or ''):16s} {v.get('name')}")
        return 0

    q = " ".join(a.query)
    ranked = resolve(q, vehicles)
    if not ranked:
        print(f'✗ "{q}" matches no machine in the fleet. `--list` shows all of them.')
        return 1
    top, rest = ranked[0], ranked[1:4]
    if len(ranked) > 1 and ranked[1][0] == top[0]:
        print(f'⚠ "{q}" is AMBIGUOUS — {len([r for r in ranked if r[0]==top[0]])} '
              "machines score equally. Name one:")
        for s, v in ranked:
            if s == top[0]:
                print(f"    {v['id']}  {v.get('nickname') or v.get('name')}")
        return 1

    flagged = brief(top[1], vehicles, idx, full=a.full)
    if rest:
        print("\nalso considered, and rejected: "
              + ", ".join(f"{v['id']}({s})" for s, v in rest))
    print(f"resolved from: \"{q}\"  →  {top[1]['id']}  (score {top[0]})")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
