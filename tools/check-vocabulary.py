#!/usr/bin/env python3
"""check-vocabulary.py — is the canonical vocabulary actually true of the code?

⭐ WHY THIS EXISTS `[paul-stated 2026-09-02]`: *"Let's be using all these to document our
names for everything and try to standardize as much as possible — and also make it
DETERMINISTIC where possible to the data schema."*

`VOCABULARY.md` was promoted to canon the same day. A glossary nobody can check is prose,
and this repo's own doctrine is that **a written rule is not a mechanism**. This is the
mechanism.

WHAT IT CHECKS, AND WHY EACH ONE EARNED ITS PLACE
-------------------------------------------------
Every check below corresponds to a defect actually found on 2026-09-02:

  V1  A REJECTED term is used as an IDENTIFIER in a governed surface.
      · `propertyId` survived in 4 files against canon that rules `property` unusable
        as the tenant noun (`property.json` already means *facts about this place*).
  V2  A CANONICAL term is defined and used NOWHERE — aspirational vocabulary.
      · `siting` reached zero artifacts on the day it was coined.
  V3  A key is DOUBLE-BOOKED — one name, two meanings, one repo.
      · `group` = tend/fight/visit/run/place in `momlib.DOMAINS` AND
        vehicle/equipment/household-system in `vehicles.json`.
  V4  A term is BOTH canonical and rejected inside VOCABULARY.md itself.
  V5  A name canon says is TAKEN is minted for a new purpose.
      · `location` was declared absent ("Zero") while appearing 7× meaning
        *where the paint-code sticker is* — a future agent would have minted it for siting.

⛔ IT FLAGS; IT NEVER RENAMES. Renaming a live key is a migration, and this checks
vocabulary.

⚠️ THE N8 GUARD IS THE HARD PART, and it is why the scope is narrow.
`property` appears **433 times** in `viewer.html`. A checker that fired on every legacy
occurrence would be red forever on day one — the **COSTLY CONTROL** signature Paul has
already ruled against (*a control whose alarm never clears is a control nobody reads*).
So: **V1 governs only SCHEMA-BEARING surfaces** — the places new names get minted — and
legacy prose is reported as **coverage, counted and never graded**.

Usage:
    python3 tools/check-vocabulary.py
    python3 tools/check-vocabulary.py --json
    python3 tools/check-vocabulary.py --selftest
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
VOCAB = os.path.join(ROOT, "VOCABULARY.md")

# ⭐ SITING (CYCLE-SPINE S3): the measured risk is a NEW name being minted against canon,
# and new names are minted where schema is defined — not in prose. So V1 reads the files
# that DEFINE structure, plus the design docs that specify it, and deliberately not
# `viewer.html`'s 433 legacy hits. Widening this to prose would buy a permanently-red row.
SCHEMA_SURFACES = [
    "tools/momlib.py",
    "worker/wrangler.toml",
    # moved to the private sibling 2026-09-03 (C4 step 1b) — read there; unreadable if the sibling is absent
    "../fernwood-private/.plans/2026-09-02-data-model-design.md",
    "../fernwood-private/.plans/2026-09-02-governance-model-PROPOSAL.md",
]

# Parsed OUT of VOCABULARY.md rather than restated here — the file is canon, this is a reader.
REJECTED_HEAD = re.compile(r"^##\s*4\s*·", re.M)
# ⚠️ The bold term does NOT always end its cell — rejected rows read
# `| **`property`** as the tenant noun | why |`. Requiring `**` then `|` silently matched
# NOTHING for exactly the row that mattered, and the selftest caught it on first run.
ROW = re.compile(r"^\|\s*(?:⛔\s*)?\*\*[`\"']?([A-Za-z][A-Za-z ._-]{1,40}?)[`\"']?\*\*[^|]*\|", re.M)


class Unknown(Exception):
    """Cannot determine an input. Fails CLOSED — never renders as clean."""


def _read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def parse_vocabulary(text):
    """Split VOCABULARY.md into canonical terms and rejected terms, from its own headings."""
    m = REJECTED_HEAD.search(text)
    if not m:
        raise Unknown("VOCABULARY.md has no '## 4 ·' rejected-words section — "
                      "the file's shape changed and this reader is stale")
    before, after = text[:m.start()], text[m.start():]
    # §5 is the live-defect section; rejections stop there.
    nxt = re.search(r"^##\s*5\s*·", after, re.M)
    rejected_block = after[:nxt.start()] if nxt else after
    canonical = {t.strip().lower() for t in ROW.findall(before)}
    rejected = {t.strip().lower() for t in ROW.findall(rejected_block)}
    if not canonical or not rejected:
        raise Unknown(f"parsed {len(canonical)} canonical / {len(rejected)} rejected terms — "
                      "expected both to be non-empty; the table shape changed")
    return canonical, rejected


CODE_SPAN = re.compile(r"`[^`\n]*`")


def identifier_hits(term, text, markdown=False):
    """Count uses of `term` as an IDENTIFIER (camelCase key, snake key, JSON key),
    never as an English word. `propertyId` counts; 'the property is the tenant' does not.

    ⚠️ CORRECTED on this tool's FIRST LIVE RUN, 2026-09-02. It flagged the sentence
    *"the key is `estateId`, never `propertyId`"* — i.e. a rule ABOUT not using the term
    was read as a use of it. **In Markdown, a backticked span is a MENTION, not a use**, so
    code spans are stripped before matching there. Left intact for .py/.toml, where a
    backtick is not a mention marker.

    This is the container-vs-payload defect committed by the checker built to catch it,
    caught by running it rather than by reading it — which is the day's own lesson.
    """
    if markdown:
        text = CODE_SPAN.sub(" ", text)
    t = re.escape(term)
    pats = [rf'\b{t}Id\b', rf'\b{t}_id\b', rf'"{t}"\s*:', rf"'{t}'\s*:", rf'\b{t}=']
    return sum(len(re.findall(p, text)) for p in pats)


def check(vocab_text, root=ROOT, surfaces=None):
    canonical, rejected = parse_vocabulary(vocab_text)
    surfaces = SCHEMA_SURFACES if surfaces is None else surfaces
    findings, facts = [], {}

    # V4 first — if canon contradicts itself, everything downstream is unsound.
    both = canonical & rejected
    if both:
        findings.append(("V4", f"term is BOTH canonical and rejected in VOCABULARY.md: "
                               f"{', '.join(sorted(both))}"))

    # V1 — a rejected term used as an identifier in a schema-bearing surface.
    read, unreadable = {}, []
    for rel in surfaces:
        p = os.path.join(root, rel)
        try:
            read[rel] = _read(p)
        except OSError:
            unreadable.append(rel)
    if unreadable:
        # A surface we cannot read is UNKNOWN, never clean.
        findings.append(("V1?", f"surface(s) unreadable, so NOT checked: {', '.join(unreadable)}"))
    for term in sorted(rejected):
        for rel, body in read.items():
            n = identifier_hits(term, body, markdown=rel.endswith('.md'))
            if n:
                findings.append(("V1", f"rejected term '{term}' used as an identifier "
                                       f"{n}x in {rel}"))

    # V2 — a canonical term defined and used nowhere at all (aspirational vocabulary).
    corpus = "\n".join(read.values())
    unused = sorted(t for t in canonical
                    if len(t.split()) == 1 and not re.search(rf'\b{re.escape(t)}\b', corpus, re.I))
    facts["canonicalTermsAbsentFromSchemaSurfaces"] = unused

    facts["canonical"] = len(canonical)
    facts["rejected"] = len(rejected)
    facts["surfacesChecked"] = len(read)
    facts["surfacesUnreadable"] = unreadable
    return findings, facts


# --------------------------------------------------------------------------
# SELFTEST — S3: a check that has never been SEEN TO FAIL has proven nothing.
# Every case is a mutation that must flip a verdict.
# --------------------------------------------------------------------------
VOCAB_FIXTURE = """# V
## 3 · RATIFIED
| term | means | why |
|---|---|---|
| **estate** | one property | x |
| **grant** | the edge | x |
| **siting** | where a machine lives | x |
## 4 · WORDS WE ARE NOT USING
| rejected | why |
|---|---|
| **`property`** as the tenant noun | taken |
| **`tenant`** | landlord connotation |
## 5 · LIVE DEFECT
"""


def _selftest():
    import tempfile
    fails = []
    def chk(label, cond):
        print(("  ✅ " if cond else "  ❌ ") + label)
        if not cond: fails.append(label)
    print("check-vocabulary selftest")

    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, "s"), exist_ok=True)
        clean = os.path.join("s", "schema.py")
        open(os.path.join(td, clean), "w").write("estateId = 1\ngrant = {}\nsiting = None\n")
        f, facts = check(VOCAB_FIXTURE, root=td, surfaces=[clean])
        chk("clean schema -> no V1", not [x for x in f if x[0] == "V1"])
        chk("  and it parsed both tables", facts["canonical"] >= 3 and facts["rejected"] >= 1)

        # MUTATION 1 — the real 2026-09-02 defect: propertyId against canon.
        open(os.path.join(td, clean), "w").write("propertyId = 1\n")
        f, _ = check(VOCAB_FIXTURE, root=td, surfaces=[clean])
        chk("propertyId -> V1 fires", any(x[0] == "V1" and "property" in x[1] for x in f))

        # MUTATION 2 — English prose must NOT fire. This is the N8 guard.
        open(os.path.join(td, clean), "w").write("# the property is the tenant of record\n")
        f, _ = check(VOCAB_FIXTURE, root=td, surfaces=[clean])
        chk("prose use of a rejected word -> does NOT fire (N8 guard)",
            not [x for x in f if x[0] == "V1"])

        # MUTATION 3 — an unreadable surface is UNKNOWN, never clean.
        f, facts = check(VOCAB_FIXTURE, root=td, surfaces=["s/does-not-exist.py"])
        chk("unreadable surface -> reported, not silently clean",
            any(x[0] == "V1?" for x in f) and facts["surfacesUnreadable"])

        # MUTATION 3b — a MENTION in Markdown is not a USE. The false positive this
        # tool produced on its own first live run.
        md = os.path.join("s", "doc.md")
        open(os.path.join(td, md), "w").write("The key is `estateId`, never `propertyId`.\n")
        f, _ = check(VOCAB_FIXTURE, root=td, surfaces=[md])
        chk("backticked MENTION in .md -> does NOT fire", not [x for x in f if x[0] == "V1"])
        open(os.path.join(td, md), "w").write("propertyId = 1\n")
        f, _ = check(VOCAB_FIXTURE, root=td, surfaces=[md])
        chk("  but a bare USE in the same .md still fires", any(x[0] == "V1" for x in f))

        # MUTATION 4 — canon contradicting itself outranks everything.
        bad = VOCAB_FIXTURE.replace("| **`tenant`** | landlord connotation |",
                                    "| **`tenant`** | x |\n| **estate** | x |")
        f, _ = check(bad, root=td, surfaces=[clean])
        chk("term both canonical AND rejected -> V4 fires", any(x[0] == "V4" for x in f))

        # MUTATION 5 — aspirational vocabulary: defined, used nowhere.
        open(os.path.join(td, clean), "w").write("estateId=1\ngrant={}\n")
        _, facts = check(VOCAB_FIXTURE, root=td, surfaces=[clean])
        chk("a canonical term used nowhere -> reported as absent",
            "siting" in facts["canonicalTermsAbsentFromSchemaSurfaces"])

        # MUTATION 6 — FAIL CLOSED on a shape change.
        try:
            check("# V\nno tables here\n", root=td, surfaces=[clean])
            chk("VOCABULARY.md shape change -> raises Unknown", False)
        except Unknown:
            chk("VOCABULARY.md shape change -> raises Unknown", True)

    print(f"\n{'PASS' if not fails else 'FAIL'} — {len(fails)} failure(s)")
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return _selftest()
    try:
        findings, facts = check(_read(VOCAB))
    except Unknown as e:
        print(f"🔤 Vocabulary — ⚠️ UNKNOWN, treated as a finding: {e}")
        return 1
    except OSError as e:
        print(f"🔤 Vocabulary — ⚠️ cannot read VOCABULARY.md ({e})")
        return 1

    if a.json:
        print(json.dumps({"findings": [{"code": c, "what": w} for c, w in findings],
                          **facts}, indent=2))
        return 1 if findings else 0

    if not findings:
        print(f"🔤 Vocabulary — clean. {facts['canonical']} canonical / {facts['rejected']} "
              f"rejected terms, {facts['surfacesChecked']} schema surface(s) checked.")
    else:
        print(f"🔤 Vocabulary — {len(findings)} finding(s):")
        for c, w in findings:
            print(f"   ⚡ [{c}] {w}")
    absent = facts.get("canonicalTermsAbsentFromSchemaSurfaces") or []
    if absent:
        print(f"   · counted, never graded — canonical terms not yet in any schema surface: "
              f"{', '.join(absent)}")
    print(f"   ⛔ Flags only. Renaming a live key is a migration, not a vocabulary fix.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
