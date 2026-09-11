#!/usr/bin/env python3
"""check-place-values.py — does one household's build carry ANOTHER household's VALUES?

    python3 tools/check-place-values.py                 # build every neutral instance and scan it
    python3 tools/check-place-values.py --instance instance/paul.json
    python3 tools/check-place-values.py --page /tmp/some-build.html
    python3 tools/check-place-values.py --selftest

⭐⭐ WHY THIS EXISTS, AND WHY `check-estate-neutral.py` DOES NOT COVER IT. CLAUDE.md already records
the failure in its own words:

  > EVEN RUN CORRECTLY IT IS NOT COVERAGE FOR A DATA LEAK. On 09-07 Fernwood's own gauge record —
  > 123 days, 30.83", "OUR GAUGE" — rendered at households in Roswell, Dahlonega and Bangor, and
  > this check read ✅ 311 needles / rendered=0 against the very origin four seats walked.
  > **IT TESTS FOR NAMES.** That leak was NUMBERS AND POSSESSIVE PRONOUNS.

⛔ It happened again, and bigger. Measured 2026-09-10: `SUN_HORIZON_DATA` was a **33,860-byte
literal in the engine** — Fernwood's coordinates, DEM elevation, skyline angles and a year of its
sun times — shipping inside the PUBLIC build of every other household. `check-estate-neutral` was
green throughout, because not one of those bytes is a NAME.

**So this is the sibling check, and its whole subject is VALUES.** `[paul-ruled 2026-09-10]`: *"we
don't want all the populated Fernwood data in all the other households either."*

## Three things it does differently

1. **It scans a BUILT HOUSEHOLD EXPORT**, not the shipped static pages. `check-estate-neutral`'s
   `_shipped_pages()` drops `viewer.html` on purpose (the tracked copy is Fernwood's and is supposed
   to name Fernwood) — so the app itself was never scanned by the bare form. This BUILDS each
   neutral instance and scans that, which is the artifact a stranger actually downloads.
2. **Needles are READ FROM CANON, never typed** — the same rule `check-estate-neutral` runs on for
   species. A coordinate this tool did not derive is a coordinate it cannot miss having.
3. **It separates a LEAK from DISCLOSURE.** A value in code or data is 🔴 — it is live, it can
   render, and it is another household's fact. The same value in a comment is 🟠 — inert, but it is
   still shipped to every household and readable by anyone with View Source.

⛔ IT IS NOT A REPLACEMENT. Names still matter and `check-estate-neutral` still owns them. Run both:
one asks *"does this page name another household"*, this one asks *"does it carry another
household's facts."* Neither answers the other's question.

EXIT: 0 clean · 1 a VALUE leaked into code or data · 2 disclosure only (comments) · 3 UNCHECKABLE.
"""
import argparse, importlib.util, json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ⚠️ TWO TYPED LISTS, DECLARED AS SUCH, AND THE SPLIT BETWEEN THEM IS THE WHOLE POINT. Prose cannot
# be derived from canon — no field holds "our gauge". But the first version treated all possessive
# prose as a leak and buried a REAL one under 23 false alarms, which is how a detector stops being
# read.
#
# 🔴 PLACE_PROSE — sentences that describe ONE property and render at any household. `[measured
# 2026-09-10]` the engine renders, to everyone: "how much of that is the mountain and how much is
# the gauge's sheltered spot by the pond." A household in Bangor has no pond. TWO COMMENTS IN THIS
# SAME FILE already name this exact string as the problem and it was never fixed — which is why it
# needs a check and not another comment.
PLACE_PROSE = [r"the gauge's sheltered spot by the pond", r"sheltered spot by the pond",
               r"how much is the gauge", r"is the mountain and how much"]
# 🟡 POSSESSIVE — first-person framing. LEGITIMATE when it means the household being rendered: "Day
# by day at our gauge" is true for whoever owns the gauge. It is a REVIEW signal, never a verdict —
# the danger is another estate's NUMBERS rendering underneath it, which is a different control
# (the station declaration) and not this one.
POSSESSIVE = [r"our gauge", r"our pond", r"our spur", r"our station", r"our own gauge"]


def canon_needles():
    """Every place-specific VALUE Fernwood's canon states, derived — never restated here."""
    out = {}

    def add(label, val, kind):
        if val is None or val == "":
            return
        out.setdefault(label, (str(val), kind))

    try:
        prop = json.load(open(os.path.join(ROOT, "property.json"), encoding="utf-8"))
    except OSError:
        raise SystemExit("check-place-values: ⛔ UNCHECKABLE — property.json is unreadable, so the "
                         "needles cannot be derived. Never green by absence.")
    p = prop.get("property") or {}
    for k in ("address", "city", "zip", "county", "name"):
        add("property.%s" % k, p.get(k), "text")
    loc = prop.get("location") or {}
    c = loc.get("coordinates") or {}
    for k, lab in (("latitude", "lat"), ("longitude", "lon")):
        v = c.get(k)
        if v is None:
            continue
        s = str(v)
        add("coord.%s" % lab, s, "number")
        # a truncated coordinate is the same disclosure — 4dp is ~11 m
        m = re.match(r"(-?\d+\.\d{4})", s)
        if m:
            add("coord.%s.4dp" % lab, m.group(1), "number")
    el = (loc.get("elevation") or {})
    for k in ("estimated_ft", "measured_ft", "demElev_ft"):
        v = el.get(k)
        if v is None:
            continue
        n = int(float(v))
        add("elev.%s" % k, str(n), "number")
        add("elev.%s.comma" % k, "{:,}".format(n), "number")
    res = prop.get("resources") or {}
    st = res.get("nearestWeatherStation") or {}
    add("station.id", st.get("id"), "text")
    try:
        fish = json.load(open(os.path.join(ROOT, "fishing.json"), encoding="utf-8"))
        add("water.name", (fish.get("_meta") or {}).get("water") or fish.get("water"), "text")
    except OSError:
        pass
    for i, pat in enumerate(PLACE_PROSE):
        out["prose.%d" % i] = (pat, "regex")
    for i, pat in enumerate(POSSESSIVE):
        out["possessive.%d" % i] = (pat, "regex")
    return out


def tier(h):
    """🔴 leak · 🟡 review · 🟠 disclosure. A comment is disclosure whatever it says; in live code,
    a VALUE or place-PROSE is a leak and a bare possessive is a question for a human."""
    if h["where"] == "comment":
        return "disclosure"
    if h["needle"].startswith("possessive."):
        return "review"
    return "leak"


COMMENT_LINE = re.compile(r"^\s*(//|/\*|\*)")


def comment_spans(text):
    """[(start, end)] of every /* … */ block and // … EOL run, scanned once.

    ⛔ THE FIRST VERSION WAS LINE-LOCAL AND IT OVER-REPORTED BY ~5×. A wrapped block comment's
    CONTINUATION lines start with neither `//` nor `*`, so every needle on one was filed as live
    code. A detector that cries wolf on 48 hits when 3 are real is a detector nobody runs twice —
    the over-report direction is safe for a MISS, never for a habit.
    ⚠️ Still deliberately crude: it does not parse strings, so a `//` inside a quoted literal can
    open a phantom comment. That errs toward calling a hit a COMMENT, so the guard below keeps the
    line-local test as well and takes the STRICTER of the two.
    """
    spans, i, n = [], 0, len(text)
    while i < n:
        b = text.find("/*", i)
        l = text.find("//", i)
        if b < 0 and l < 0:
            break
        if b >= 0 and (l < 0 or b < l):
            e = text.find("*/", b + 2)
            e = n if e < 0 else e + 2
            spans.append((b, e)); i = e
        else:
            # a scheme's `//` is not a comment
            if text[max(0, l - 6):l].endswith(("http:", "https:", "ws:", "wss:")):
                i = l + 2; continue
            e = text.find("\n", l)
            e = n if e < 0 else e
            spans.append((l, e)); i = e
    return spans


def in_span(spans, pos):
    lo, hi = 0, len(spans) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        s, e = spans[mid]
        if pos < s: hi = mid - 1
        elif pos >= e: lo = mid + 1
        else: return True
    return False


def classify(text, pos, spans=None):
    """comment | code. Uses the whole-file comment map when given one, and falls back to the
    line-local test — a hit is CODE unless both agree it is not."""
    ls = text.rfind("\n", 0, pos) + 1
    le = text.find("\n", pos)
    line = text[ls:le if le > 0 else len(text)]
    before = line[:pos - ls]
    line_local_comment = bool(COMMENT_LINE.match(line)) or (
        "//" in before and not ("http://" in before or "https://" in before))
    # ⛔ WHEN THE SPAN MAP EXISTS IT IS THE ANSWER, and OR-ing the line-local test on top of it was
    # a bug its own selftest caught: `/* a */ var y = <needle>;` starts with `/*`, so the line-local
    # test called live code a comment — the ONE direction this tool must never err in.
    if spans is not None:
        return "comment" if in_span(spans, pos) else "code"
    return "comment" if line_local_comment else "code"


def scan(text, needles):
    spans = comment_spans(text)
    hits = []
    for label, (val, kind) in needles.items():
        rx = re.compile(val, re.I) if kind == "regex" else re.compile(re.escape(val), re.I)
        for m in rx.finditer(text):
            hits.append({"needle": label, "value": m.group(0), "kind": kind,
                         "where": classify(text, m.start(), spans),
                         "line": text[:m.start()].count("\n") + 1})
    return hits


def build_instance(inst_path):
    out = tempfile.NamedTemporaryFile(suffix=".html", delete=False).name
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build-viewer.py"),
                        "--instance", inst_path, "--out", out],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        tail = (r.stderr or r.stdout or "").strip().splitlines()
        raise RuntimeError((tail[-1] if tail else "build failed")[:160])
    return out


def neutral_instances():
    out = []
    for f in sorted(os.listdir(os.path.join(ROOT, "instance"))):
        if not f.endswith(".json"):
            continue
        p = os.path.join(ROOT, "instance", f)
        try:
            d = json.load(open(p, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if d.get("canon") == "..":       # Fernwood's own build is SUPPOSED to name Fernwood
            continue
        out.append(p)
    return out


def report(name, hits):
    leak = [h for h in hits if tier(h) == "leak"]
    rev = [h for h in hits if tier(h) == "review"]
    comm = [h for h in hits if tier(h) == "disclosure"]
    mark = "🔴" if leak else ("🟡" if rev else ("🟠" if comm else "✅"))
    print("   %s %-22s %d leak · %d review · %d disclosure" % (mark, name, len(leak), len(rev), len(comm)))
    for h in leak[:8]:
        print("        🔴 L%-6d %-18s %r" % (h["line"], h["needle"], h["value"][:44]))
    seen_r = set()
    for h in rev:
        if h["needle"] in seen_r: continue
        seen_r.add(h["needle"])
        print("        🟡 L%-6d %-18s %r — prose; true if it means THIS household"
              % (h["line"], h["needle"], h["value"][:30]))
    seen = set()
    for h in comm:
        if h["needle"] in seen:
            continue
        seen.add(h["needle"])
        n = sum(1 for x in comm if x["needle"] == h["needle"])
        print("        🟠 %-18s ×%-3d e.g. L%d" % (h["needle"], n, h["line"]))
    return len(leak), len(rev), len(comm)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--instance"); ap.add_argument("--page"); ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    needles = canon_needles()
    print("🔎 place-VALUES in a household build — %d needle(s) derived from canon "
          "(%d typed possessive)\n" % (len(needles), len(POSSESSIVE)))

    targets = []
    if a.page:
        targets = [(os.path.basename(a.page), a.page, False)]
    else:
        for p in ([a.instance] if a.instance else neutral_instances()):
            try:
                targets.append((os.path.basename(p), build_instance(p), True))
            except Exception as e:
                print("   ⛔ %-22s UNCHECKABLE — could not build: %s" % (os.path.basename(p), e))
                targets.append((os.path.basename(p), None, True))

    total_code, total_rev, total_comm, unchecked = 0, 0, 0, 0
    for name, path, temp in targets:
        if not path:
            unchecked += 1
            continue
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError as e:
            print("   ⛔ %-22s UNCHECKABLE — %s" % (name, e)); unchecked += 1; continue
        c, rv, m = report(name, scan(text, needles))
        total_code += c; total_rev += rv; total_comm += m
        if temp:
            os.unlink(path)

    print()
    if unchecked:
        print("⛔ %d target(s) UNCHECKABLE — that is not 'clean'." % unchecked)
        return 3
    if total_code:
        print("🔴 %d place-VALUE(s) live in code or data of a household build. This is the class "
              "`check-estate-neutral` cannot see." % total_code)
        return 1
    if total_rev:
        print("🟡 %d possessive(s) in live prose — REVIEW, not a verdict. True where it means the "
              "household being rendered." % total_rev)
    if total_comm:
        print("🟠 %d disclosure(s) — comments only. Inert, but shipped to every household and "
              "readable with View Source." % total_comm)
    if total_rev or total_comm:
        return 2
    print("✅ no household build carries another household's values.")
    return 0


def selftest():
    ok, bad = 0, []
    n = {"coord.lat": ("34.5496", "number"), "possessive.0": (r"our gauge", "regex")}
    def check(cond, why):
        # ⛔ `ok += 1 if c else bad.append(...)` raises TypeError on the FAILING branch, so the first
        # real failure destroys the run instead of being reported. Measured on this very file.
        nonlocal_ok[0] += 1 if cond else 0
        if not cond: bad.append(why)
    nonlocal_ok = [0]
    check(scan("var x = 34.5496;", n)[0]["where"] == "code", "code hit misread")
    # ⭐ the regression that motivated the rewrite: a WRAPPED block comment's continuation line
    wrapped = "/* a long note that runs\n   past 34.5496 onto the next line */\n"
    check(scan(wrapped, n)[0]["where"] == "comment", "block-comment continuation read as code")
    check(scan("/* a */ var y = 34.5496;", n)[0]["where"] == "code", "code after a closed block read as comment")
    check(scan("// computed at 34.5496 once", n)[0]["where"] == "comment", "comment hit misread")
    check(scan("/* x\n  * 34.5496 in a block comment */", n)[0]["where"] == "comment", "block comment misread")
    check(scan('const u = "https://x/34.5496";', n)[0]["where"] == "code", "a url:// was read as a comment")
    check(len(scan("OUR GAUGE and our gauge", n)) == 2, "case-insensitive possessive missed")
    check(scan("nothing here", n) == [], "phantom hit")
    # a derived needle set must never be silently empty
    try:
        got = canon_needles()
        check(any(k.startswith("coord.") for k in got), "no coordinate needle derived from canon")
        check(any(k.startswith("elev.") for k in got), "no elevation needle derived from canon")
    except SystemExit:
        bad.append("canon unreadable during selftest")
    ok = nonlocal_ok[0]
    print("selftest: %d passed, %d failed" % (ok, len(bad)))
    for b in bad: print("   🔴", b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
