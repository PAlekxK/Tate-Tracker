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

_URL = re.compile(r"https?://")

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


def laundering(v):
    """Card values whose `source` is a LINK rather than a held document.

    ⭐ Added 2026-08-30 `[paul-stated]`, alongside the FIELD-NOTES quarantine. Tier A
    means "the file is in `_assets/` and anyone can check it without asking us" — a
    URL is not a held document. It decays (11 of 27 Bronco bookmarks were once
    unretrievable), it is unarchived, and it is the shape a third-party claim takes
    on its way INTO the record.

    THE DANGER IS MIGRATION, NOT ERROR, and this repo has measured it: the Bronco's
    `_chatgptProvenanceWarning` records FOUR wrong card values traced to two ChatGPT
    threads, one wearing a false "read off the actual sidewalls" provenance. It never
    arrived labelled as junk — it was summarised into a note and later sat in
    vehicles.json looking manual-sourced. A habit does not catch that. A scan does.

    ⚠️ SCOPE, stated: `manual.url` is EXEMPT and deliberately so — that field's whole
    job is to hold a link to the readable manual, and flagging it would be the
    permanently-on alarm this stack keeps warning about. Only `maintenance.*.source`
    and serviceHistory citations are scanned, because those are the fields that carry
    the authority of a fact.
    """
    out = []
    for k, m in (v.get("maintenance") or {}).items():
        if isinstance(m, dict) and _URL.search(str(m.get("source") or "")):
            out.append(("maintenance." + k, str(m.get("source"))[:70]))
    for e in v.get("serviceHistory") or []:
        blob = " ".join(str(e.get(f) or "") for f in ("summary", "source", "shop"))
        if _URL.search(blob):
            out.append(("serviceHistory:" + str(e.get("id"))[:34], blob[:70]))
    return out


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
# ⛔ IDENTITY FIELDS ARE STRINGS. Do not add one here without checking its type
#    across the WHOLE fleet — see the 2026-09-01 defect note in _haystack().
#
# ⭐ STRONG vs WEAK is the discriminator. What a machine IS CALLED (id / name /
# nickname) is identity. What it is LIKE (trim / category / a document field) is
# description, and description is where a symptom sentence collides: 'start' is
# a substring of the CS-352's trim "i-30 Starter", which is not evidence that
# Paul is talking about a chainsaw.
STRONG_FIELDS = ("id", "name", "nickname")
WEAK_FIELDS = ("trim", "category", "doorLabel")
NAME_FIELDS = STRONG_FIELDS + WEAK_FIELDS

# ⭐ Function words carry NO identity and must never score. Paul dictates, so a
# real query is a run-on sentence that is mostly these.
STOPWORDS = frozenset("""
a an the this that these those it its is was were be been being am are
and or but nor so if then than as at by for from in into of off on onto out
over under up down to too with without again just really very much more most
not no nothing never only also well like kind sort pretty
i me my mine we us our you your he him his she her they them their
have has had do does did done get got go goes going went come came
try tried trying turn turned sound sounded seem seems
what which who when where why how
""".split())

# ⚠️ A stopword that IS part of a machine's real name, declared with its reason.
# A CLOSED SET, deliberately: an UNDECLARED collision fails --selftest loudly,
# so silencing a real name can only ever be a recorded judgment, never a drift.
# (Same posture as the closed-set `state` fix in fleet_probe.py, lap 1 beat 7.)
STOPWORD_COLLISIONS = {
    "turn": "husqvarna-mower 'Zero-Turn' — but 'turn over' is how anyone "
            "describes cranking an engine. 'zero' still carries that machine.",
    "i":    "chainsaw-cs352 trim 'i-30 Starter' — a bare 'I' is the speaker, "
            "not the saw. 'cs352' and 'echo' still carry that machine.",
}


def _haystack(v):
    """What the machine is CALLED (strong) and what it is LIKE (weak).

    Returns (strong, weak, skipped) — STRINGS ONLY.

    ⛔ 2026-09-01 DEFECT, found at fleet lap 2 beat 0 on the first real sentence
    Paul ever gave this tool. The haystack was built with
    `str(v.get(k) or "")`, and `doorLabel` is a **dict on exactly one of 22
    machines** (the Bronco). Python stringified that dict into 1,557 characters
    of English prose — 'summary', 'confidence', 'verified — paul read every
    field off the label photo', a file path, whole sentences. That one record
    then out-scored the entire fleet on any dictated query, because ordinary
    words ('the', 'and', 'a', 'to', 'of', 'not', 'is') were matching a **repr**,
    not a name. Paul's update scored bronco-1989 **61** and dr200s-2017 **2**;
    the correct machine placed last of eight.

    `str()` on a container returns a plausible value instead of raising, which
    is why nothing caught it: **match the payload, not the container.** A
    non-string identity field is SKIPPED and REPORTED, never stringified.
    """
    strong, weak, skipped = [], [], []
    for group, sink in ((STRONG_FIELDS, strong), (WEAK_FIELDS, weak)):
        for k in group:
            val = v.get(k)
            if val is None:
                continue
            if isinstance(val, str):
                sink.append(val)
            else:
                skipped.append((k, type(val).__name__))
    return " ".join(strong).lower(), " ".join(weak).lower(), skipped


def _toks(s):
    return {t for t in re.split(r"[^a-z0-9]+", s) if t}


# A model YEAR is identity when spoken whole ("the 2017 Suzuki") and pure noise
# when matched inside ("the 200" must not match the 2001 in drz400s-2001, nor
# the 2006 in f150-2006). So years are whole-token-matchable but never
# substring-matchable — found 2026-09-01 when "the 200" tied THREE machines.
YEAR_RE = re.compile(r"^(19|20)\d{2}$")


def _substring_hay(hay):
    return " ".join(t for t in re.split(r"[^a-z0-9]+", hay)
                    if t and not YEAR_RE.match(t))


def score(query, v):
    """Token overlap against everything the machine is called.

    Function words are dropped BEFORE scoring. What remains is graded by where
    it lands and by what KIND of token it is:

      6  a whole-word hit on id/name/nickname          ("bolores", "thunder")
      6  a DIGIT-BEARING substring hit on those        ("200" inside "dr200s")
      2  a whole-word hit on trim/category
      1  any other substring hit                       (weak by construction)

    ⭐ Digits are identity. In loose speech the model designation is the one
    reliable signal — Paul says "the 200", not "the Suzuki DR200S" — so a
    digit-bearing token is graded as strongly as a name. Plain alpha substrings
    are graded to 1 precisely because that is where symptom vocabulary lands.
    """
    q = [t for t in re.split(r"[^a-z0-9]+", query.lower())
         if t and t not in STOPWORDS]
    strong, weak, _ = _haystack(v)
    strong_t, weak_t = _toks(strong), _toks(weak)
    strong_sub, weak_sub = _substring_hay(strong), _substring_hay(weak)
    s = 0
    for t in q:
        if t in strong_t:
            s += 6
        elif len(t) >= 3 and t in strong_sub:
            s += 6 if any(c.isdigit() for c in t) else 1
        elif t in weak_t:
            s += 2
        elif len(t) >= 3 and t in weak_sub:
            s += 1
    if norm(query) and norm(query) == norm(v.get("nickname")):
        s += 10
    return s


# ⚠️ PROVISIONAL — first cut, same posture as every threshold in CYCLE-MAP.md.
# Half a strong hit of daylight is the minimum to declare a winner.
RESOLVE_MARGIN = 3


# ⚠️ PROVISIONAL. A single weak substring hit is not identity evidence: "it
# won't start" scored 1 against the CS-352's "i-30 Starter" and would otherwise
# have been served as a confident answer, because a LONE match is never a tie.
MIN_SCORE = 2


def resolve(query, vehicles):
    ranked = sorted(((score(query, v), v) for v in vehicles.values()),
                    key=lambda p: (-p[0], p[1]["id"]))
    return [(s, v) for s, v in ranked if s >= MIN_SCORE]


def too_close(ranked):
    """True when the top match is not clearly ahead — the caller must REFUSE.

    ⭐ Replaces an EXACT-TIE test, which could only ever catch a dead heat. The
    2026-09-01 defect scored 61 vs 2, so it was never a tie — it was
    confidently wrong, and a confidently-wrong resolver is exactly what this
    loop was founded to prevent. A refusal is the honest output of a resolver
    that cannot see daylight.
    """
    if len(ranked) < 2:
        return False
    return ranked[0][0] - ranked[1][0] < RESOLVE_MARGIN


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

    lnd = laundering(v)
    if lnd:
        flagged = True
        bar("⚠️ SOURCED TO A LINK, NOT A HELD DOCUMENT")
        for field, src in lnd:
            print(f"  🟣 {field}\n      {src}")
        print("  A card value's source must be a document we hold or a physical read.\n"
              "  A link is tier C — see cycle/fleet/FIELD-NOTES.md.")

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

    # ⭐ REGRESSION, 2026-09-01 — PAUL'S ACTUAL DICTATED SENTENCE, verbatim.
    # The old test above passes only because the machine's NAME is in the query.
    # This is what he really said, and it contains no name at all. It resolved
    # to bronco-1989 (61) over dr200s-2017 (2). Both halves are asserted: the
    # right machine must WIN, and the wrong one must not merely lose — it must
    # score ZERO, because every point it had was an English function word.
    PAULS_UPDATE = ("after charging the 200 for a good amount and then left it "
                    "overnight and tried to start it and it would not start the "
                    "battery kind of dimmed and it sounded like I was trying to "
                    "turn over and then I tried it again and again and it just "
                    "wound up clicking so it really seems like the battery is "
                    "draining or doesn't have a charge")
    pr = resolve(PAULS_UPDATE, vehicles)
    check("POSITIVE: Paul's dictated update -> dr200s-2017",
          pr and pr[0][1]["id"] == "dr200s-2017")
    check("PAIRED NEAR-MISS: it is NOT bronco-1989",
          not (pr and pr[0][1]["id"] == "bronco-1989"))
    check("PAIRED NEAR-MISS: bronco-1989 scores 0 on it (the noise is gone)",
          score(PAULS_UPDATE, vehicles["bronco-1989"]) == 0)

    # ⛔ the container bug itself — a dict identity field must be SKIPPED, and
    # no machine's haystack may ever contain a Python repr.
    bs, bw, bskip = _haystack(vehicles["bronco-1989"])
    check("haystack: bronco doorLabel (dict) is SKIPPED, not stringified",
          ("doorLabel", "dict") in bskip)
    check("haystack: and its prose never reaches the haystack",
          "summary" not in (bs + bw) and "{" not in (bs + bw))
    check("haystack: NO machine in the fleet leaks a repr",
          not any("{" in (h[0] + h[1]) or "'" in (h[0] + h[1])
                  for h in (_haystack(v) for v in vehicles.values())))

    # too_close — paired, because a gate proven only to open is not proven
    check("too_close: a clear winner is NOT refused",
          not too_close([(61, {}), (2, {})]))
    check("too_close: a 1-point gap IS refused (an exact tie is not the only risk)",
          too_close([(3, {}), (2, {})]))
    check("too_close: an exact tie is still refused",
          too_close([(5, {}), (5, {})]))
    check("too_close: a lone match is never refused",
          not too_close([(2, {})]))

    # a query of pure filler must resolve to NOTHING, never to a machine
    check("resolve: filler-only speech resolves to NOTHING",
          not resolve("and then it just would not do it again", vehicles))

    # ⭐ the model-year trap — "the 200" is inside 2001, 2005 AND 2006.
    r200 = resolve("the 200", vehicles)
    check("POSITIVE: 'the 200' -> dr200s-2017 alone (years are not substrings)",
          r200 and r200[0][1]["id"] == "dr200s-2017" and len(r200) == 1)
    check("PAIRED: 'the 400' -> drz400s-2001, the OTHER bike",
          (lambda r: bool(r) and r[0][1]["id"] == "drz400s-2001")(
              resolve("the 400", vehicles)))
    check("PAIRED: a year spoken WHOLE still scores ('the 2017 suzuki')",
          (lambda r: bool(r) and r[0][1]["id"] == "dr200s-2017")(
              resolve("the 2017 suzuki", vehicles)))

    # MIN_SCORE — a lone weak hit must refuse, because a lone match is never a tie
    check("resolve: 'it won't start' resolves to NOTHING (1 pt is not identity)",
          not resolve("it won't start", vehicles))
    check("PAIRED: a real weak-field hit still lands ('the truck')",
          bool(resolve("the truck", vehicles)))

    # ⭐ STOPWORDS must never swallow a real name. Fleet-safe, asserted.
    name_toks = set()
    for v in vehicles.values():
        for k in ("id", "name", "nickname", "trim", "category"):
            val = v.get(k)
            if isinstance(val, str):
                name_toks |= {t for t in re.split(r"[^a-z0-9]+", val.lower()) if t}
    collide = name_toks & STOPWORDS
    undeclared = collide - set(STOPWORD_COLLISIONS)
    check(f"STOPWORDS: every name collision is DECLARED with a reason "
          f"(undeclared: {sorted(undeclared)})", not undeclared)
    check("STOPWORDS: no DECLARED collision is stale (each is a real name token)",
          set(STOPWORD_COLLISIONS) <= collide)
    check("STOPWORDS: every declared collision carries a non-empty reason",
          all(isinstance(r, str) and len(r) > 20
              for r in STOPWORD_COLLISIONS.values()))

    # the link-as-source guard, both ways + the exemption + the live denominator
    check("laundering: a maintenance source that IS a URL gets flagged",
          bool(laundering({"maintenance": {"oil": {"source": "https://forum.example/t/1"}}})))
    check("laundering: a held-document source is NOT flagged",
          not laundering({"maintenance": {"oil": {"source": "manuals/text/x.txt p.4-2"}}}))
    check("laundering: manual.url is EXEMPT — holding a link is that field's job",
          not laundering({"manual": {"url": "https://manua.ls/suzuki/dr200s"}}))
    check("laundering: serviceHistory citations are scanned too",
          bool(laundering({"serviceHistory": [{"id": "sr-1",
                                               "summary": "per https://forum.example"}]})))
    check("laundering: the real fleet is clean TODAY (guard fitted before the problem)",
          sum(len(laundering(v)) for v in vehicles.values()) == 0)

    print("\n" + ("selftest PASSED" if ok else "selftest FAILED"))
    return 0 if ok else 1


def sweep(vehicles, idx):
    """Whole-fleet provenance sweep. Prints its own denominator."""
    bad = nov = unk = checked = lnd_n = 0
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
    for v in vehicles.values():
        for field, src in laundering(v):
            lnd_n += 1
            print(f"  🟣 {v['id']} · {field} is sourced to a LINK, not a held document")
    print(f"\n  card values sourced to a link: {lnd_n} "
          f"(scanned maintenance.*.source + serviceHistory across "
          f"{len(vehicles)} machines; manual.url exempt by design)")
    print(f"  {checked} document(s) checked across {len(vehicles)} machine(s): "
          f"{bad} MISMATCH · {nov} NO-OVERLAP · {unk} unverifiable · "
          f"{checked-bad-nov-unk} match.")
    print("  ❓ unverifiable = the extracted text names no model we can match. "
          "That is NOT a pass —\n     a sparse scan and a correct document look "
          "identical to this check.")
    return 1 if (bad or nov or lnd_n) else 0


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
    if too_close(ranked):
        near = [(s, v) for s, v in ranked if top[0] - s < RESOLVE_MARGIN]
        print(f'⚠ "{q}" is AMBIGUOUS — {len(near)} machines are within '
              f"{RESOLVE_MARGIN} points of each other. Name one:")
        for s, v in near:
            print(f"    {s:4d}  {v['id']}  {v.get('nickname') or v.get('name')}")
        return 1

    flagged = brief(top[1], vehicles, idx, full=a.full)
    if rest:
        print("\nalso considered, and rejected: "
              + ", ".join(f"{v['id']}({s})" for s, v in rest))
    print(f"resolved from: \"{q}\"  →  {top[1]['id']}  (score {top[0]})")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
