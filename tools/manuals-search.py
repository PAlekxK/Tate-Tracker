#!/usr/bin/env python3
"""manuals-search.py — search the whole fleet's manuals without invoking a model.

    python3 tools/manuals-search.py "spark plug gap"
    python3 tools/manuals-search.py --machine bronco "body mount"
    python3 tools/manuals-search.py --list
    python3 tools/manuals-search.py --selftest

WHY THIS EXISTS
---------------
`feedback_non_ai_door` (Paul, 2026-08-02): *anything deterministic must be reachable
without invoking a model.* Its falsifier, almost word for word from the backlog row:
**if the only way to learn what your manual says is to ask Guru, this is broken.**

The corpus has been greppable since 2026-07-08. `grep -rin` works and will keep working.
What it does not do is the whole reason this file exists:

  1. **It does not tell you WHICH MACHINE a hit belongs to.** `drz400s-2001-service.txt`
     is a filename, not an answer. You wanted the DR-Z400.
  2. **It does not rank.** A 1,341-page owner's manual and a 7-page quick-reference card
     return hits in directory order, so the useful one is wherever the alphabet put it.
  3. **It does not span filenames.** Searching "bronco" finds the word *inside* documents
     and misses the document that IS the Bronco's.

⛔ WHAT THIS IS NOT — and the backlog row exists to prevent exactly this confusion:
**this is not Guru retrieval.** That is a separate, still-PARKED build (§A6), deliberately
held for the expert team, and two findings already constrain it — retrieval solves volume,
not confusability, and a test harness is its real prerequisite because probing /api/chat
forges a Mom-input signal. Building this and calling it progress on that would be the
failure the row was written to prevent. They share a substrate and nothing else.

WHAT IT CANNOT DO, stated rather than implied
---------------------------------------------
  · It searches EXTRACTED TEXT. `pdftotext` on a scanned manual yields sparse, sometimes
    garbled output — `dr200s-2017-service` is flagged in INDEX.md as exactly that. A miss
    here is not proof the manual is silent; it may be proof the scan is poor.
  · It matches literal words (and regex with --re). It has no synonyms: "gap" will not
    find "clearance", and nothing here will tell you it didn't.
  · Applicability is a JUDGEMENT it does not make. It prints INDEX.md's confidence marker
    beside every hit — 🟡 and ⚠️ mean the document may not describe your unit. The known
    live case: `husqvarna-mower-yth24v54` is the WRONG CHASSIS manual on disk (a YTH24V54
    tractor, not the confirmed Z254F). Its engine specs still hold; its deck-belt part
    numbers do not. The tool surfaces that; it cannot decide it for you.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TEXT = os.path.join(REPO, "manuals", "text")
INDEX = os.path.join(REPO, "manuals", "INDEX.md")
VEHICLES = os.path.join(REPO, "vehicles.json")

# INDEX.md rows: | `id` | Document | Pages | Match | Source |
_ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|")
_CONF = re.compile(r"(✅|🟡|⚠️)")


def load_index():
    """stem -> {doc, pages, confidence, note}. The INDEX is the authority on what a
    document IS and how well it matches; this tool never re-derives that judgement."""
    out = {}
    if not os.path.exists(INDEX):
        return out
    with open(INDEX, encoding="utf-8") as fh:
        for line in fh:
            m = _ROW.match(line)
            if not m:
                continue
            stem, doc, pages, match = m.groups()
            conf = _CONF.search(match)
            out[stem] = {
                "doc": re.sub(r"\*\*", "", doc).strip(),
                "pages": pages.strip(),
                "confidence": conf.group(1) if conf else "",
                "note": _CONF.sub("", match).strip(" .·"),
            }
    return out


def load_vehicles():
    try:
        v = json.load(open(VEHICLES, encoding="utf-8"))
    except Exception:
        return {}
    items = v if isinstance(v, list) else (v.get("vehicles") or v.get("items") or [])
    return {i["id"]: i for i in items if isinstance(i, dict) and i.get("id")}


def resolve_machine(stem, vehicles):
    """Which machine does this document belong to?

    INDEX.md states the convention — filename = the vehicles.json id, plus a
    -parts/-service/-engine suffix for secondary docs. But three files break a naive
    suffix strip (`bronco-1989-lmc-catalog-fd88`, `g22a-2005-ax2`,
    `husqvarna-mower-yth24v54`), so match the LONGEST vehicle id that prefixes the stem.
    Longest wins so `g22a-2005-ax2` cannot resolve to a shorter unrelated id.
    """
    best = None
    for vid in vehicles:
        if stem == vid or stem.startswith(vid + "-"):
            if best is None or len(vid) > len(best):
                best = vid
    return best


def machine_label(stem, vehicles, idx):
    vid = resolve_machine(stem, vehicles)
    if vid:
        v = vehicles[vid]
        emoji = (v.get("emoji") or "").strip()
        return f"{emoji + ' ' if emoji else ''}{v.get('name') or vid}"
    # Not an orphan-tolerant tool: an unresolved doc is reported AS unresolved rather
    # than quietly labelled by its filename, which would read like an answer.
    return f"(unmatched document · {stem})"


def search(term, machine=None, use_re=False, context=90, limit=40):
    idx, vehicles = load_index(), load_vehicles()
    if not os.path.isdir(TEXT):
        print(f"⛔ no manuals corpus at {TEXT}")
        return 2
    try:
        rx = re.compile(term if use_re else re.escape(term), re.I)
    except re.error as exc:
        print(f"⛔ bad regex: {exc}")
        return 2

    per_doc = []
    for fn in sorted(os.listdir(TEXT)):
        if not fn.endswith(".txt"):
            continue
        stem = fn[:-4]
        label = machine_label(stem, vehicles, idx)
        if machine and machine.lower() not in (stem + " " + label).lower():
            continue
        try:
            body = open(os.path.join(TEXT, fn), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        hits = []
        for m in rx.finditer(body):
            s = max(0, m.start() - context // 2)
            snip = " ".join(body[s:m.end() + context // 2].split())
            hits.append(snip)
        # Filename hits answer "which document IS this machine's" — the case plain grep
        # over file CONTENTS structurally cannot serve.
        name_hit = bool(rx.search(stem) or rx.search(label))
        if hits or name_hit:
            per_doc.append((stem, label, idx.get(stem, {}), hits, name_hit))

    if not per_doc:
        print(f'no hits for "{term}"' + (f" in {machine}" if machine else ""))
        print("  ⚠️ A miss is not proof the manual is silent. This searches EXTRACTED text —")
        print("     scanned manuals extract sparsely — and it has no synonyms.")
        return 1

    # Rank: filename/machine matches first (they answer a different, usually better
    # question), then by hit count. Hit count is a crude relevance signal and is stated
    # as such rather than dressed up as a score.
    per_doc.sort(key=lambda r: (not r[4], -len(r[3]), r[0]))

    shown = 0
    print(f'MANUALS — "{term}"' + (f"  · machine filter: {machine}" if machine else "") + "\n")
    for stem, label, meta, hits, name_hit in per_doc:
        conf = meta.get("confidence", "")
        doc = meta.get("doc", "(not in INDEX.md)")
        print(f"  {label}   {conf}")
        print(f"    {doc}")
        if meta.get("note"):
            # Only a non-✅ note is a CAVEAT. On a ✅ row the note is reassuring
            # ("covers 2001"), and dressing it as a warning trains the reader to
            # ignore the warnings that matter.
            mark = "⚠️" if conf in ("🟡", "⚠️") else "·"
            print(f"    {mark} {meta['note'][:140]}")
        if name_hit and not hits:
            print("    ← matched this DOCUMENT's name, not its text")
        for h in hits[:5]:
            print(f"      · {h[:200]}")
            shown += 1
            if shown >= limit:
                break
        if len(hits) > 5:
            print(f"      … {len(hits) - 5} more hit(s) in this document")
        print(f"    file: manuals/text/{stem}.txt")
        print()
        if shown >= limit:
            print(f"  (stopped at {limit} snippets — narrow with --machine)")
            break

    total = sum(len(h) for _, _, _, h, _ in per_doc)
    print(f"  {total} hit(s) across {len(per_doc)} document(s) of "
          f"{len([f for f in os.listdir(TEXT) if f.endswith('.txt')])} in the corpus.")
    print("  ⚠️ 🟡/⚠️ marks come from manuals/INDEX.md and mean the document may not describe "
          "your exact unit. Applicability is yours to judge.")
    return 0


def list_corpus():
    idx, vehicles = load_index(), load_vehicles()
    files = sorted(f for f in os.listdir(TEXT) if f.endswith(".txt"))
    print(f"MANUALS CORPUS — {len(files)} document(s)\n")
    unresolved = []
    for fn in files:
        stem = fn[:-4]
        label = machine_label(stem, vehicles, idx)
        meta = idx.get(stem, {})
        if label.startswith("(unmatched"):
            unresolved.append(stem)
        print(f"  {meta.get('confidence',' ')} {label:34} {stem}")
        if meta.get("doc"):
            print(f"      {meta['doc'][:110]}")
    print()
    missing_idx = [f[:-4] for f in files if f[:-4] not in idx]
    if missing_idx:
        print(f"  ⚠️ {len(missing_idx)} document(s) not in INDEX.md: {', '.join(missing_idx)}")
    if unresolved:
        print(f"  ⚠️ {len(unresolved)} document(s) resolve to no vehicles.json id: "
              f"{', '.join(unresolved)}")
    if not missing_idx and not unresolved:
        print("  ✓ every document maps to a machine and carries an INDEX.md row.")
    return 0


def selftest():
    """Prove the three things plain grep cannot do, and prove they can FAIL."""
    fails = []

    def check(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            fails.append(name)

    vehicles, idx = load_vehicles(), load_index()
    files = [f[:-4] for f in os.listdir(TEXT) if f.endswith(".txt")]

    # 1 — every document resolves to a machine. This is the claim the tool's whole value
    # rests on, and the three awkward filenames are why it is asserted rather than assumed.
    unresolved = [s for s in files if resolve_machine(s, vehicles) is None]
    check("every manual resolves to a vehicles.json machine", not unresolved)
    if unresolved:
        print(f"        unresolved: {', '.join(unresolved)}")

    # 2 — longest-prefix, not first-match. The bug this prevents: `g22a-2005-ax2`
    # resolving to `g22a-2005` is CORRECT, but a shorter accidental prefix would not be.
    check("g22a-2005-ax2 resolves to the g22a-2005 machine",
          resolve_machine("g22a-2005-ax2", vehicles) == "g22a-2005")
    check("bronco catalog resolves to the bronco",
          resolve_machine("bronco-1989-lmc-catalog-fd88", vehicles) == "bronco-1989")

    # 3 — a negative control. A stem belonging to nothing must resolve to NOTHING, or
    # the checks above pass for free and prove nothing.
    check("an unknown stem resolves to no machine (control)",
          resolve_machine("not-a-real-machine-xyz", vehicles) is None)

    # 4 — INDEX.md parsed at all, and confidence actually read.
    check("INDEX.md rows parsed", len(idx) >= 15)
    check("a 🟡/⚠️ confidence marker is read from INDEX.md",
          any(v.get("confidence") in ("🟡", "⚠️") for v in idx.values()))

    # 5 — the known-bad document is surfaced as such rather than silently trusted.
    husq = idx.get("husqvarna-mower-yth24v54", {})
    check("the wrong-chassis Husqvarna manual carries a non-✅ marker",
          husq.get("confidence") in ("🟡", "⚠️"))

    print(f"\n{'FAILED: ' + ', '.join(fails) if fails else 'all checks passed'}")
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(
        description="Search the fleet's manuals corpus. No model involved.")
    ap.add_argument("term", nargs="?", help="text to find (literal unless --re)")
    ap.add_argument("--machine", help="restrict to one machine (substring of id or name)")
    ap.add_argument("--re", action="store_true", dest="use_re", help="treat term as a regex")
    ap.add_argument("--list", action="store_true", help="list the corpus and its coverage")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.list:
        return list_corpus()
    if not a.term:
        ap.print_help()
        return 2
    return search(a.term, machine=a.machine, use_re=a.use_re)


if __name__ == "__main__":
    sys.exit(main())
