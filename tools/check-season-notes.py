#!/usr/bin/env python3
"""check-season-notes.py — audit the month-keyed `seasonNotes` prose (schema v7).

WHY THIS EXISTS
---------------
178 authored prose lines across 36 plants render on Mom's surface, one per plant
per month. The standing item asked PAUL to read all 178 and spot-check them,
which sat undone for a week — it reads as a slog because it was scoped as one.

Two facts reshape the job, and this tool is built on them:

  1. **Only the current month is ever on screen.** `renderPlantCard` reads
     `plant.seasonNotes[String(currentMonth)]` and nothing else, so the live set
     is one month's worth (August: 24), never 178. Use `--month` for that view.
  2. **The authoring rule forbids date claims outright** — a note may never say
     "now" or assert a day-range, because a month is coarser than a 1–2 week
     window. So the notes are deliberately unfalsifiable by TIMING. What is left
     to be wrong about is narrower: a claim that contradicts the plant's own
     canon, or that breaks the authoring rule itself.

That narrower thing is machine-checkable against data already in the repo, which
means all 178 can be audited without anyone reading them.

POSTURE — IT FLAGS, IT NEVER FIXES
----------------------------------
Every content check here is a HEURISTIC over prose: it matches vocabulary, not
meaning. A note may legitimately mention flowers out of season ("long before the
flowers", "once the petals drop"). So findings are REVIEW items for a human, the
same fail-open posture `rationalize-bench.py` uses and for the same reason:
wrongly hiding a finding loses it silently; wrongly showing one costs a line in a
report someone reads. Nothing in this tool writes to canon.

Exit 0 = nothing to look at. Exit 1 = findings (same contract as the other
check-* tools, so it can join the session-start block).
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
ABBR = [m[:3] for m in MONTHS]

# Vocabulary that implies the plant is IN FLOWER as you read it. Anticipatory and
# retrospective framings are handled by SOFTENERS below, not by trimming this.
BLOOM_WORDS = re.compile(
    r"\b(bloom(?:s|ing)?|flower(?:s|ing)?|blossom(?:s|ing)?|petals?|in\s+flower|catkins?)\b",
    re.I)

# A note may reference a bloom it is NOT claiming is happening now. Two distinct
# framings do that, and both defuse a bloom-month finding:
#   TEMPORAL — the bloom is placed before/after the month being described.
#   HABIT    — the sentence describes the plant's flowering HABIT ("flowers on old
#              wood", "you'll get leaves instead of flowers", "the flower buds"),
#              which is a fact about the species, not a claim about today. This
#              class was the single largest source of false positives on the first
#              run: 6 of 6 BLOOM-MONTH hits were habit language.
SOFTENERS = re.compile(
    r"\b(before|after|once|by\s+the\s+time|until|last\s+year|next\s+(?:year|spring|summer)|"
    r"has\s+finished|are\s+done|long\s+gone|spent|faded|"
    r"on\s+(?:both\s+)?(?:old|new)\s+(?:and\s+new\s+)?wood|instead\s+of|flower\s+buds?|costs?\s+(?:next|the))\b", re.I)

# Care vocabulary → the `care` key it implies.
# ⚠️ "cutting" alone is NOT propagation — "cutting an overgrown holly hard" and
# "hard cutting costs the big flush" are both PRUNING. Taking cuttings needs the
# plural or an explicit verb. Three of six CARE-MONTH false positives were this.
CARE_WORDS = {
    "prune": re.compile(r"\b(prune|pruning|prun(?:ed|es)|cut\s+back|cutting\b|deadhead(?:ing|ed)?|shear(?:ing|ed)?)\b", re.I),
    "fertilize": re.compile(r"\b(fertiliz(?:e|ing|ed|er)|feed(?:ing)?\b|top-?dress)\b", re.I),
    "propagate": re.compile(r"\b(propagat(?:e|ing|ion)|cuttings\b|take\s+a\s+cutting|divid(?:e|ing)|layer(?:ing)?)\b", re.I),
    "repot": re.compile(r"\b(re-?pot(?:ting|ted)?|transplant(?:ing|ed)?)\b", re.I),
}

# A note that tells you NOT to do a thing this month is correct authoring, not a
# contradiction — "hold off on heavy pruning until it hardens" in a non-prune month
# is the record working. Two more false positives came from missing this.
CARE_NEGATION = re.compile(
    r"\b(hold\s+off|don'?t|do\s+not|avoid|wait|too\s+early|too\s+late|not\s+the\s+time|"
    r"the\s+window\s+comes|resist)\b", re.I)

# The v7 authoring rule, as patterns. A month is coarser than a 1–2 week window,
# so any of these is wrong for part of the month the note renders in.
DATE_ASSERTIONS = [
    (re.compile(r"\bright\s+about\s+now\b", re.I), 'says "right about now"'),
    (re.compile(r"\bany\s+day\s+now\b", re.I), 'says "any day now"'),
    (re.compile(r"\b(?:this|next|last)\s+week\b", re.I), "names a week"),
    (re.compile(r"\bin\s+the\s+next\s+few\s+days\b", re.I), "names a few days"),
    (re.compile(r"\b(?:" + "|".join(ABBR) + r")[a-z]*\.?\s+\d{1,2}\b"), "names a month-and-day"),
    (re.compile(r"\b\d{1,2}\s*[–—-]\s*\d{1,2}\b"), "names a day range"),
    (re.compile(r"\b(?:early|mid|late)[-\s]+(?:" + "|".join(ABBR) + r")[a-z]*\b", re.I),
     "names a part of a named month (the rule allows \"late in the month\", not \"late April\")"),
]

# "now" gets its own rule, read STRICTLY from the authoring constraint: a note
# "must never assert a date, a day-range, or 'now / right about now' FOR ANYTHING
# THAT HAS peakDates." The clause is conditional and the first run ignored it,
# flagging seven notes where "now" simply means "during this month" and is true
# all month ("anything cut now costs next spring's blooms"). It is only a
# violation when the sentence pairs "now" with the timed observable — the bloom.
NOW_WORD = re.compile(r"(?<!by\s)\bnow\b", re.I)

# A dated historical record may name a date — "Mom confirmed it in flower here in
# mid-July 2026" is the rule's own worked example of what IS allowed.
DATED_RECORD = re.compile(r"\b(19|20)\d{2}\b")


def load_plants():
    with open(os.path.join(ROOT, "plants.json"), encoding="utf-8") as f:
        data = json.load(f)
    return data.get("plants") or []


def bloom_months(plant):
    """0-indexed months any bloom window touches. None = the record has no bloom
    at all, which is different from an empty window and is reported differently."""
    bloom = plant.get("bloom")
    if not isinstance(bloom, dict):
        return None
    months = set()
    for d in bloom.get("dates") or []:
        try:
            s, e = int(str(d["start"])[:2]), int(str(d["end"])[:2])
        except (KeyError, ValueError, TypeError):
            continue
        m = s
        while True:                      # inclusive, wrapping across the year end
            months.add(m - 1)
            if m == e:
                break
            m = m % 12 + 1
    return months


def care_months(plant, key):
    """0-indexed months for a care type, folding in its subcategories."""
    entry = (plant.get("care") or {}).get(key)
    if not isinstance(entry, dict):
        return set()
    months = set(entry.get("months") or [])
    for sub in entry.get("subcategories") or []:
        months |= set(sub.get("months") or [])
    return months


def audit(plants, only_month=None):
    findings, stats = [], {"notes": 0, "plants": 0, "with_provenance": 0, "by_month": {}}

    for plant in plants:
        notes = plant.get("seasonNotes")
        if not isinstance(notes, dict) or not notes:
            continue
        stats["plants"] += 1
        bm = bloom_months(plant)
        seen_text = {}

        for key, text in sorted(notes.items(), key=lambda kv: str(kv[0])):
            # STRUCTURE — a bad key or an empty note is a defect, not a judgment call.
            try:
                m = int(key)
                assert 0 <= m <= 11
            except (ValueError, AssertionError):
                findings.append((plant["id"], key, "STRUCTURE",
                                 f"month key {key!r} is not 0–11"))
                continue
            if only_month is not None and m != only_month:
                continue
            stats["notes"] += 1
            stats["by_month"][m] = stats["by_month"].get(m, 0) + 1
            if isinstance(text, dict):          # a future per-note {value, confidence}
                if text.get("confidence"):
                    stats["with_provenance"] += 1
                text = text.get("value") or ""
            if not str(text).strip():
                findings.append((plant["id"], m, "STRUCTURE", "note is empty"))
                continue
            text = str(text)

            # STRUCTURE — the same sentence on two months is copy-paste drift, and
            # it defeats the whole point of month-keying.
            if text in seen_text:
                findings.append((plant["id"], m, "DUPLICATE",
                                 f"identical text to month {seen_text[text]}"))
            seen_text[text] = m

            # RULE — the v7 authoring constraints, which have never had a linter
            # despite BACKLOG claiming "lint-enforced at authoring".
            # A dated historical record is exempt from ALL of these, not just from
            # the self-naming check — that asymmetry was a bug on the first run.
            dated = bool(DATED_RECORD.search(text))
            if not dated:
                for pat, why in DATE_ASSERTIONS:
                    if pat.search(text):
                        findings.append((plant["id"], m, "DATE-CLAIM",
                                         f"{why} — {snippet(text, pat)}"))
                        break
                # "now" only violates the rule when it is attached to the timed
                # observable — see NOW_WORD. Otherwise it means "this month".
                if NOW_WORD.search(text) and BLOOM_WORDS.search(text) and bm:
                    findings.append((plant["id"], m, "DATE-CLAIM",
                                     f'says "now" about a bloom that has dated windows — '
                                     f"{snippet(text, NOW_WORD)}"))
            # A month may name ITSELF only inside a dated historical record.
            own = re.compile(r"\b" + MONTHS[m] + r"\b", re.I)
            if own.search(text) and not dated:
                findings.append((plant["id"], m, "SELF-NAMING",
                                 f'names its own month — {snippet(text, own)}'))

            # CANON — does the prose contradict this plant's own record?
            if BLOOM_WORDS.search(text) and not SOFTENERS.search(text):
                if bm is None:
                    findings.append((plant["id"], m, "BLOOM-NO-RECORD",
                                     f"talks about flowering but the record has no `bloom` — "
                                     f"{snippet(text, BLOOM_WORDS)}"))
                elif m not in bm:
                    window = ", ".join(MONTHS[x][:3] for x in sorted(bm)) or "none"
                    findings.append((plant["id"], m, "BLOOM-MONTH",
                                     f"reads as in-flower but bloom months are [{window}] — "
                                     f"{snippet(text, BLOOM_WORDS)}"))
            for care_key, pat in CARE_WORDS.items():
                if pat.search(text) and not CARE_NEGATION.search(text):
                    cm = care_months(plant, care_key)
                    if cm and m not in cm:
                        window = ", ".join(MONTHS[x][:3] for x in sorted(cm))
                        findings.append((plant["id"], m, f"CARE-MONTH:{care_key}",
                                         f"mentions {care_key} but care.{care_key} months are "
                                         f"[{window}] — {snippet(text, pat)}"))
    return findings, stats


def snippet(text, pat, width=64):
    m = pat.search(text)
    if not m:
        return text[:width].strip() + ("…" if len(text) > width else "")
    a = max(0, m.start() - width // 2)
    b = min(len(text), m.end() + width // 2)
    return ("…" if a else "") + text[a:b].strip() + ("…" if b < len(text) else "")


def main():
    ap = argparse.ArgumentParser(description="Audit month-keyed seasonNotes against the plants' own canon.")
    ap.add_argument("--month", type=int, default=None, metavar="N",
                    help="0-indexed month to audit alone (the Tier-2 view: what is ACTUALLY on screen)")
    ap.add_argument("--quiet", action="store_true", help="findings only; no coverage table")
    args = ap.parse_args()

    if args.month is not None and not 0 <= args.month <= 11:
        print("error: --month is 0-indexed (0=Jan … 11=Dec)", file=sys.stderr)
        return 2

    plants = load_plants()
    findings, stats = audit(plants, only_month=args.month)

    scope = f" for {MONTHS[args.month]}" if args.month is not None else ""
    print(f"season-notes audit{scope} — {stats['notes']} note(s) across {stats['plants']} plant(s)\n")

    if findings:
        print(f"── REVIEW — {len(findings)} finding(s). These are HEURISTIC reads of prose:")
        print("   a human decides. Nothing here has been changed.\n")
        by_kind = {}
        for pid, m, kind, why in findings:
            by_kind.setdefault(kind.split(":")[0], []).append((pid, m, kind, why))
        for kind in sorted(by_kind):
            print(f"  {kind}")
            for pid, m, full, why in by_kind[kind]:
                mon = MONTHS[m][:3] if isinstance(m, int) else m
                print(f"    · {pid:<38} {mon}  {why}")
            print()
    else:
        print("── no contradictions found against the plants' own bloom and care months.\n")

    if not args.quiet and args.month is None:
        print("── COVERAGE (only the CURRENT month ever renders — this is the real unit of review)")
        for m in range(12):
            n = stats["by_month"].get(m, 0)
            bar = "█" * n
            print(f"    {MONTHS[m][:3]}  {n:>3}  {bar}")
        print()

    # PROVENANCE — the standing finding this tool exists partly to keep visible.
    if stats["with_provenance"] == 0 and stats["notes"]:
        print("── ⚠️ PROVENANCE GAP (standing, not a per-note finding)")
        print(f"    0 of {stats['notes']} notes carry any confidence marker. These are")
        print("    AI-authored prose lines rendering on Mom's surface, in a project whose")
        print("    stated rule is that honesty markers are mandatory, not decorative —")
        print("    variety, bloom and every maintenance value carry one. A schema move to")
        print("    per-note {value, confidence} is Paul's call; this tool already reads")
        print("    that shape if it ever lands.\n")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
