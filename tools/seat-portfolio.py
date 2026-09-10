#!/usr/bin/env python3
"""seat-portfolio.py — ARE THESE THE RIGHT SEATS? A standing assessment of the reading roster.

    python3 tools/seat-portfolio.py
    python3 tools/seat-portfolio.py --selftest

⭐ THE ASK `[paul-stated 2026-09-10]`: "as we have these seats that review the various journeys,
there should be a standing assessment of whether those seats make sense, whether they tie in
together… and we should have hypotheses about demographics that we're testing as we go."

⛔ IT ASKS A DIFFERENT QUESTION FROM EVERY OTHER CHECK IN THIS REPO. `release-gate` asks did each
seat pass; `walk-integrity` asks may this run be counted. This asks *are these the right seats* —
do they cover the space, where do they overlap, and what is nobody sitting in.

⭐⭐ THE METHOD IS ALREADY IN THE ROSTER, AND IT IS WHY THIS IS DERIVED RATHER THAN INVENTED.
`synthetic-identity.py` records that `handover` was added because it was "one of the eleven things
the ranking screen offers and it was the ONLY one no seat had ever ranked." That is the assessment
Paul is asking to make standing: take a space that already exists, find the uncovered cell, name it.
So the space here is `INTERESTS` — READ from `onboarding/index.html`, never restated — because it is
the product's own profile axis and it has already produced one seat.
⛔ NOT A DEMOGRAPHIC TAXONOMY. Inventing one would mint categories nobody has evidence for, and the
eleven are what a real person is actually shown and asked to rank.

⛔ A SEAT IS A SHAPE, NOT A PERSON — the roster's own constraint, and it binds this file too.
Nothing here proposes a seat modelled on a real neighbour, and an uncovered cell is a HYPOTHESIS
with a falsifier, never a persona presented as fact. `.user-research/persona-mom.md` is the model:
`evidence_level: contested`, with a retraction banner naming a source it withdrew.

⚠️ AND THE FIRST HONEST OUTPUT MAY BE THAT THE PORTFOLIO CANNOT BE ASSESSED YET. The roster mixes
axes: `handover` is a JOURNEY wearing a lens's clothes, `mom` is a POSTURE, `strict`'s distinguishing
feature is its PO box, which is a FIXTURE. A coverage reading over a list whose members are different
kinds of thing is a reading about the list, not about the coverage. This file says so out loud rather
than assessing past it.
"""
import argparse, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def interests(root=ROOT):
    """The modules a person is actually shown and asked to rank — READ from the page that shows them.

    ⛔ DERIVED, NEVER RESTATED. A typed copy of this list is a second definition of what the product
    offers, and it would go stale the first time a module is added — at which point this file would
    report full coverage of a space that had grown."""
    p = os.path.join(root, "onboarding", "index.html")
    src = open(p, encoding="utf-8").read()
    m = re.search(r"var INTERESTS = \[(.*?)\n  \];", src, re.S)
    if not m:
        return []
    return [(i, l) for i, l in re.findall(r'\{\s*id:\s*"([^"]+)",\s*label:\s*"([^"]+)"', m.group(1))]


def seats(root=ROOT):
    """(role, posture, ranked, place) per seat — posture from the roles register, the rest from the
    seat's own answers. A seat with no answers file has no fixture and is named as such."""
    import importlib.util as _i
    p = os.path.join(root, "tools", "synthetic-identity.py")
    s = _i.spec_from_file_location("si", p); si = _i.module_from_spec(s); s.loader.exec_module(si)
    out = []
    for role, v in sorted(si.ROLES.items()):
        ap = os.path.join(root, ".private", "walk-answers", "%s.json" % role)
        try:
            a = json.load(open(ap, encoding="utf-8"))
        except (OSError, ValueError):
            a = None
        out.append((role, (v or {}).get("note") or "", (a or {}).get("interests") or [],
                    (a or {}).get("place")))
    return out


def assess(root=ROOT):
    # ⛔ THE SPACE IS READ FIRST AND REFUSED FIRST. Reading the roster before knowing there is a
    # space to assess it against would make an unreadable space fail as a crash rather than as
    # UNCHECKABLE — a distinction this repo's exit codes carry deliberately.
    ints = interests(root)
    lines, hypotheses = [], []
    if not ints:
        return ["⛔ UNCHECKABLE — the ranking options could not be read from onboarding/index.html, "
                "so there is no space to assess coverage against."], [], 3
    ss = seats(root)
    ids = [i for i, _ in ints]
    lines.append("  the space: %d module(s) a person is shown and asked to rank" % len(ints))
    lines.append("")
    covered = {}
    for role, note, ranked, place in ss:
        for r in ranked:
            covered.setdefault(r, []).append(role)
        lines.append("  %-11s ranks %-38s %s"
                     % (role, ", ".join(ranked) or "⛔ nothing", "" if ranked else "(no answers file)"))
    lines.append("")
    # ── COVERAGE. The uncovered cell is the whole method — it is what produced `handover`.
    for i, label in ints:
        who = covered.get(i) or []
        lines.append("  %-14s %-32s %s" % (i, label,
                                           ", ".join(who) if who else "⛔ NO SEAT RANKS IT"))
        if not who:
            # ⭐ `other` IS NOT A FALSE POSITIVE, and special-casing it away would lose the best cell
            # on the board. CLAUDE.md already names this shape from the other direction — the
            # onboarding sweep's own note is that "what's missing" is "the only line where someone
            # can name a need we never anticipated." A seat that ranks it walks the product as
            # somebody whose want is not on the list, and no seat ever has.
            extra = (" ⭐ AND IT IS THE CATCH-ALL: nothing in the battery has ever walked the "
                     "product as somebody whose want is not on the list." if i == "other" else "")
            hypotheses.append(
                ("uncovered", i,
                 "no seat ranks %r, so nothing in the battery reads the product as somebody who "
                 "wants it. HYPOTHESIS: a reader who ranks it would meet something the others do "
                 "not. FALSIFIER: give an existing seat this module and the battery surfaces "
                 "nothing new — then the cell did not need a seat.%s" % (label, extra)))
    # ⛔ AND THE OVERLAP, which is the other half of "do they tie in together".
    for i, who in sorted(covered.items()):
        if len(who) >= 4:
            hypotheses.append(
                ("crowded", i,
                 "%d of %d seats rank it (%s). HYPOTHESIS: the marginal seat here reads what an "
                 "earlier one already read. FALSIFIER: their reports on this module diverge — then "
                 "the crowding is real coverage, not redundancy."
                 % (len(who), len(ss), ", ".join(who))))
    # ── ⭐⭐ THE AXIS READING, and it is measurable rather than argued for exactly one seat.
    lines.append("")
    for role, note, ranked, place in ss:
        tell = []
        if role in ids:
            # ⭐ A SEAT NAMED AFTER A MODULE IS A JOURNEY, NOT A LENS. `handover` is both a seat and
            # one of the eleven things a person can rank — it names a PATH THROUGH THE PRODUCT, not a
            # way of reading one. It is filed in the roles dict because the roles dict is the only
            # list there is, and it is the cleanest three-axis evidence in the repo.
            tell.append("JOURNEY — it shares a name with a module a person can rank")
        if not note:
            tell.append("no posture declared")
        if tell:
            hypotheses.append(("axis", role, " · ".join(tell)))
    return lines, hypotheses, (1 if hypotheses else 0)


def report(out=print):
    lines, hypotheses, rc = assess()
    out("seat portfolio — are these the right seats?  ⛔ hypotheses, never findings\n")
    for l in lines:
        out(l)
    if not hypotheses:
        out("\n✅ every module has a reader and no seat is misfiled.")
        return rc
    out("\n⛔ %d hypothesis/es — each carries its own falsifier:" % len(hypotheses))
    for kind, what, why in hypotheses:
        out("  · %-10s %-14s %s" % (kind, what, why))
    out("\n⚠️⚠️ READ THE AXIS ROWS FIRST, AND READ THE COVERAGE ROWS AS PROVISIONAL UNTIL THEY CLEAR.")
    out("   The roster mixes kinds of thing — a posture, a fixture and a journey in one list — so a")
    out("   coverage reading over it is a reading about the LIST, not about the coverage. Separating")
    out("   the three axes is the journey library's work, not this file's.")
    out("⛔ A seat is a SHAPE, not a person. Nothing here proposes one modelled on anybody real, and")
    out("   an uncovered cell is a hypothesis to test, never a persona to adopt.")
    return rc


def selftest():
    fails = []

    def check(name, ok, why=""):
        print("  %s %-56s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    ints = interests()
    # ⛔⛔ THIS CLAUSE PINNED A COPY STRING AND WENT RED WHEN ANOTHER LANE DID CORRECT WORK.
    # `[corrected 2026-09-10 at close-out]` It asserted `("handover", "Handing it all over") in ints`
    # — the id AND its label. `onboarding-ask-b3` then rewrote the interests ask so each option names
    # an ACTIVITY (`4439010`), and the label became "Getting it ready to hand over". The module never
    # moved: 11 modules still read, `handover` still among them. The only thing that broke was my
    # copy of somebody else's words.
    # ⭐ A TEST THAT FAILS WHEN ANOTHER LANE DOES ITS JOB IS A TEST THAT GETS MUTED, and the next
    # reader cannot tell a muted clause from a satisfied one. The ID is the identity and is this
    # file's business; the LABEL is authored content that is SUPPOSED to change, and pinning it made
    # this file a silent veto over a surface it does not own.
    # ⚠️ Same family as the anti-regression clause that went false six hours after it was written:
    # pin a clause to the thing it cares about, never to a detail that merely happened to be true.
    ids = {k for k, _ in ints}
    check("the module space is READ from the page that shows it",
          len(ints) >= 8 and "handover" in ids and all(k and v for k, v in ints),
          "read %d module(s): %r" % (len(ints), ints[:3]))
    check("every seat in the roles register is assessed",
          {r for r, _, _, _ in seats()} and len(seats()) >= 4, "")
    # ⛔ THE CLAUSE THAT MAKES THE AXIS FINDING REPRODUCIBLE rather than a remembered opinion.
    _, hyp, _ = assess()
    check("a seat sharing a name with a module is flagged as a JOURNEY",
          any(k == "axis" and w == "handover" for k, w, _ in hyp),
          "handover is both a seat and a rankable module and nothing said so")
    check("every hypothesis carries a falsifier or is an axis row",
          all(("FALSIFIER" in why or kind == "axis") for kind, _, why in hyp),
          "a hypothesis was emitted with no way to be wrong")
    # ⛔ NEVER GREEN BY ABSENCE: an unreadable space is UNCHECKABLE, not full coverage.
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "onboarding"))
        open(os.path.join(d, "onboarding", "index.html"), "w").write("<html></html>")
        _, _, rc = assess(d)
        check("an unreadable module space is UNCHECKABLE (3), never full coverage", rc == 3, "rc=%r" % rc)
    print("\n%s selftest: %d/5" % ("✅" if not fails else "🔴", 5 - len(fails)))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    return selftest() if ap.parse_args().selftest else report()


if __name__ == "__main__":
    sys.exit(main())
