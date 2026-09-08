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
    rows, bad, unchosen_row = [], [], None
    for c in p["colors"]:
        on_white, as_ink = ratio(c["hex"], WHITE), ratio(c["hex"], GROUND)
        worst = min(on_white, as_ink)
        rows.append((c, on_white, as_ink, worst))
        if worst < AAA:
            bad.append((c, worst))
    if p["default"] not in [c["id"] for c in p["colors"]]:
        bad.append(({"id": p["default"], "name": "(default)"}, 0.0))

    # ⭐ `unchosen` IS CHECKED LIKE A MEMBER AND COUNTED AS NONE (2026-09-08). It is what an
    # unconfigured build paints before anyone picks — a different fact from `default`, which is the
    # pre-selected SWATCH in the picker. Overloading one key would either fail the member assertion
    # above or leave a false line in this file. ⚠️ It is checked because this file's own `_contrast`
    # note refuses stored ratios on the grounds that a hand-kept fact rots; a stored HEX with no
    # check is the same defect one step earlier. Absent is a FAILURE, not a skip: build-viewer reads
    # this key for every estate that declares no colour, so an unreadable one has households wearing
    # nothing — and until today it had them wearing Fernwood's green.
    _u = (p.get("unchosen") or {}).get("hex")
    if not _u:
        bad.append(({"id": "unchosen", "name": "(unchosen — MISSING)"}, 0.0))
    else:
        _w, _i = ratio(_u, WHITE), ratio(_u, GROUND)
        unchosen_row = (_u, _w, _i, min(_w, _i))
        if min(_w, _i) < AAA:
            bad.append(({"id": "unchosen", "name": "(unchosen)"}, min(_w, _i)))

    if not a.check:
        print("estate accent palette — %d colours, ratios recomputed from the hex\n" % len(rows))
        print("  %-9s %-8s %-10s %-10s %s" % ("id", "hex", "on white", "as ink", "level"))
        for c, w, i, worst in rows:
            print("  %-9s %-8s %-10.2f %-10.2f %s%s" % (
                c["id"], c["hex"], w, i,
                "AAA" if worst >= AAA else ("AA" if worst >= AA else "⛔ FAILS"),
                "   ← default" if c["id"] == p["default"] else ""))
        if unchosen_row:
            _h, _w, _i, _worst = unchosen_row
            print("  %-9s %-8s %-10.2f %-10.2f %s   ← unchosen (not a choice; what a fresh estate wears)"
                  % ("unchosen", _h, _w, _i, "AAA" if _worst >= AAA else ("AA" if _worst >= AA else "⛔ FAILS")))
        else:
            print("  unchosen  ⛔ MISSING — build-viewer has nothing to paint an unchosen estate with")
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
