#!/usr/bin/env python3
"""palette.py — the estate accent palette, and the check that no member is unreadable.

    python3 tools/palette.py            # show the palette with recomputed contrast
    python3 tools/palette.py --check    # exit 1 if any member fails AAA. Ratios are DERIVED.

⛔ NOT named check-*.py deliberately: `check-cycle-map.py` globs that prefix and requires every
match to be named in MOM-CYCLE-MAP.md, and a palette guard is not a leg of the mom cycle. Naming it
there would forge a loop step that does not exist.

WHY THIS EXISTS: `--accent` is a button fill under WHITE text and also link ink on a near-white
ground, so a light accent is unreadable twice over — and the reader this was built for has
documented difficulty reading. A palette is exactly the kind of list someone extends later with a
colour they liked. This refuses that.
"""
import argparse, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(ROOT, "engine", "palette.json")
WHITE, GROUND = "#ffffff", "#fbfcfd"
# 20px at weight 500 is NORMAL text under WCAG, not large — so the bar is 4.5 (AA) / 7.0 (AAA),
# never the 3.0 that large text would allow.
AA, AAA = 4.5, 7.0


def _lum(h):
    h = h.lstrip("#")
    ch = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    ch = [(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4) for v in ch]
    return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]


def ratio(a, b):
    la, lb = _lum(a), _lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    p = json.load(open(FILE, encoding="utf-8"))
    rows, bad = [], []
    for c in p["colors"]:
        on_white, as_ink = ratio(c["hex"], WHITE), ratio(c["hex"], GROUND)
        worst = min(on_white, as_ink)
        rows.append((c, on_white, as_ink, worst))
        if worst < AAA:
            bad.append((c, worst))
    if p["default"] not in [c["id"] for c in p["colors"]]:
        bad.append(({"id": p["default"], "name": "(default)"}, 0.0))

    if not a.check:
        print("estate accent palette — %d colours, ratios recomputed from the hex\n" % len(rows))
        print("  %-9s %-8s %-10s %-10s %s" % ("id", "hex", "on white", "as ink", "level"))
        for c, w, i, worst in rows:
            print("  %-9s %-8s %-10.2f %-10.2f %s%s" % (
                c["id"], c["hex"], w, i,
                "AAA" if worst >= AAA else ("AA" if worst >= AA else "⛔ FAILS"),
                "   ← default" if c["id"] == p["default"] else ""))
        band = max(r[3] for r in rows) - min(r[3] for r in rows)
        print("\n  lightness band spread: %.2f  (ux-expert kept its recommended five within 0.64;" % band)
        print("  a wider band means one estate's affirmative reads weaker than another's)")
        return 0

    if bad:
        for c, worst in bad:
            print("🔴 palette: %s (%s) worst contrast %.2f — below AAA %.1f" % (c["name"], c.get("hex", "?"), worst, AAA))
        return 1
    print("✅ palette: %d colours, every one AAA against white text and as ink" % len(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
