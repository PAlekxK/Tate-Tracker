#!/usr/bin/env python3
"""check-jump-strip.py — does the jump strip still match the cards?

    python3 tools/check-jump-strip.py
    python3 tools/check-jump-strip.py --selftest

⭐ WHY `[paul-stated 2026-09-08]`: *"in general, the jump strips should match the cards. Right?"*
He said it after finding Sky & Stars rendering as a card with no shortcut to it.

⛔ THIS HAS NOW HAPPENED TWICE, in opposite directions, and neither was caught by anything:
  · `RELEASE_NOTES.md` 2026-09-07 — *"The Wildlife shortcut and the Wildlife tile had quietly gone
    missing. The card itself was always there, with all 83 of them in it."* A strip entry vanished.
  · Paul's QA walk 2026-09-08 — `card-celestial` renders and had no entry. A card gained no entry.
**Both are the same defect**: the strip is hand-authored HTML and the cards are hand-authored HTML,
and nothing ever compared them.

⛔ IT DOES NOT AUTO-DERIVE THE STRIP, DELIBERATELY. `measured`: 16 cards exist and 6 are in the
strip. Some of the other ten are almost certainly *inside* another card's territory — turf and weeds
under Gardening, fishing under Wildlife — and some are chrome (release notes, the place log). **Which
domains deserve a shortcut is a product judgement and it is Paul's**, so this tool FLAGS the gap and
never closes it. A strip auto-built from all 16 would be unusable and would read as a fix.
"""
import argparse, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "engine", "viewer.template.html")
CARD_RX = re.compile(r'class="main-card"\s+id="([\w-]+)"')
JUMP_RX = re.compile(r'data-jump="([\w-]+)"')
# Cards that are chrome or live inside another card's territory. ⛔ A ROSTER, so that adding a card
# forces a decision here rather than silently widening the strip or silently being ignored.
NOT_A_DESTINATION = {
    "card-release-notes": "the product's changelog — chrome, not a domain",
    "card-place-log":     "this place's changelog — chrome, not a domain",
    "card-references":    "a reference drawer, reached from the cards that cite it",
    "card-candidates":    "a review surface, not somewhere a person navigates to",
    "card-property":      "the place itself; the masthead already answers 'where am I'",
}


def check(template=None):
    """(missing, orphaned, cards, strip). Raises on an unreadable template."""
    with open(template or TEMPLATE, encoding="utf-8") as fh:
        t = fh.read()
    cards = CARD_RX.findall(t)
    strip = JUMP_RX.findall(t)
    if not cards or not strip:
        raise RuntimeError("parsed %d card(s) and %d strip entr(ies) — a broken parser is not a "
                           "clean strip" % (len(cards), len(strip)))
    missing = [c for c in cards if c not in strip and c not in NOT_A_DESTINATION]
    orphaned = [j for j in strip if j not in cards]      # a shortcut to a card that does not exist
    return missing, orphaned, cards, strip


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    if ap.parse_args().selftest:
        return selftest()
    try:
        missing, orphaned, cards, strip = check()
    except (OSError, RuntimeError) as e:
        print("⛔ jump strip UNCHECKABLE — %s" % e); return 2
    print("🧭 jump strip — %d card(s) · %d shortcut(s) · %d classed as not-a-destination"
          % (len(cards), len(strip), len(NOT_A_DESTINATION)))
    for o in orphaned:
        # ⛔ WORSE THAN A MISSING ENTRY: a shortcut that scrolls to nothing, which is what the
        # Reference-drawer entries did for weeks — "VISIBLY DOING NOTHING".
        print("   🔴 shortcut `%s` points at NO CARD — it would do nothing when tapped" % o)
    for m in missing:
        print("   ⚡ card `%s` renders and has no shortcut — reachable only by scrolling" % m)
    if not missing and not orphaned:
        print("   ✅ every card is either reachable from the strip or classed as not-a-destination")
    print("   ⛔ Flags only. WHICH domains deserve a shortcut is Paul's call, not this tool's.")
    return 1 if (missing or orphaned) else 0


def selftest():
    import tempfile
    fails = []

    def ck(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            fails.append(name)

    def write(body):
        f = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
        f.write(body); f.close(); return f.name

    good = write('<a data-jump="card-a"></a><div class="main-card" id="card-a">')
    m, o, _, _ = check(good)
    ck("M0 a matching strip and card set is clean", not m and not o)

    gap = write('<a data-jump="card-a"></a><div class="main-card" id="card-a">'
                '<div class="main-card" id="card-b">')
    m, o, _, _ = check(gap)
    ck("M1 a card with no shortcut is FLAGGED", m == ["card-b"] and not o)

    dead = write('<a data-jump="card-ghost"></a><div class="main-card" id="card-a">')
    m, o, _, _ = check(dead)
    ck("M2 a shortcut pointing at NO card is flagged — it would do nothing when tapped",
       o == ["card-ghost"])

    classed = write('<a data-jump="card-a"></a><div class="main-card" id="card-a">'
                    '<div class="main-card" id="card-release-notes">')
    m, _, _, _ = check(classed)
    ck("M3 a card classed not-a-destination is NOT flagged", not m)

    empty = write("<html>nothing here</html>")
    try:
        check(empty); ok = False
    except RuntimeError:
        ok = True
    ck("M4 parsing zero cards RAISES rather than reporting a clean strip", ok)
    print("\n%s selftest (%d failure(s))" % ("✅" if not fails else "🔴", len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
