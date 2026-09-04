#!/usr/bin/env python3
"""check-config-derivation.py — the path-keyed lint for INSTANCE VALUES TYPED INTO ENGINE CODE (C5 4b).

The founding leak: `FROST_MONTH, FROST_DAY = 10, 17` in fleet_probe.py, typed beside a
property.json that says "October 17" — and when canon moved (Oct 20 → Oct 17) the tool did
not follow. This lint keys on the CANONICAL PATH, not the file: each roster row names the
canon value, how a leaked copy would look (its detector), where the value is ALLOWED to
appear (canon itself, built outputs, georeference records — each with a reason), and every
other hit is a finding.

Three detector kinds:
  literal        the value's spelling(s) as substrings           (34.5496 · 2873 / 2,873)
  type-changed   the value re-typed in another type              ("October 17" → `10, 17`)
  absent-consumer a canon value NOBODY reads — counted, never failed (firstFallRiskBegins)

BLIND SPOTS, stated: a value the lint cannot see — a COMPUTED copy (`2873/1000*7`, a
lapse-rate derivation, a rounded 34.55), a value split across lines, or a spelling not in the
row. This is a substring lint over text; it names the leaks it can name.

    python3 tools/check-config-derivation.py             # exit 1 on any un-allowed hit
    python3 tools/check-config-derivation.py --selftest  # plant / clear / allowed-is-silent
"""
import argparse, ast, fnmatch, io, json, os, re, subprocess, sys, tempfile, tokenize

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import momlib  # noqa: E402

SCAN_GLOBS = ("*.py", "*.js", "*.mjs", "*.html", "*.json", "*.toml", "*.yml", "*.sh")
SKIP_DIRS = {".git", "node_modules", ".playwright-mcp"}

# (canonical path, detector kind, patterns, {allowed location glob: reason})
ROSTER = [
    ("location.coordinates.latitude", "literal", (r"34\.5496(?!\d)",), {
        "property.json":                       "canon — the value's home",
        "images/property-map/*.bounds.json":   "georeference records: a raster's own anchor, measured against the property",
        "birds.json": "domain _meta records the place the range was inferred for", "amphibians.json": "domain _meta",
        "insects.json": "domain _meta", "lizards.json": "domain _meta", "mammals.json": "domain _meta", "snakes.json": "domain _meta",
        "sun-horizon.json":                    "DERIVED output of gen-sun-horizon.py (which now derives the anchor from canon)",
        "viewer.html":                         "BUILT output — PROPERTY_DATA is inlined by build-viewer / reinline",
        "engine/viewer.template.html":         "the template carries {{DATA:PROPERTY_DATA}}; a hit here means the row left the roster",
        "worker/digest.json":                  "BUILT output of build-digest.py",
        "tools/check-condo-falsifier.py":      "a DETECTOR string — the falsifier looks for this value to prove it is absent",
        "tools/area-trace.html":               "a traced bounds record (34.5496736 — a finer coordinate that happens to contain the substring)",
        ".plans/*.json": "records", ".ux-reviews/*.json": "records", ".engineering/*": "records", ".user-research/*": "records",
    }),
    ("location.elevation.estimated_ft", "literal", (r"\b2,?873\b",), {
        "property.json": "canon", "references.json": "canon prose naming the site's elevation (content, not config)",
        "plants.json": "canon prose", "plants.draft.json": "canon prose", "candidates.json": "canon prose", "turf.json": "canon prose",
        "birds.json": "domain _meta", "amphibians.json": "domain _meta", "insects.json": "domain _meta", "lizards.json": "domain _meta",
        "mammals.json": "domain _meta", "snakes.json": "domain _meta",
        "images/property-map/*.bounds.json": "georeference records",
        "viewer.html": "BUILT output", "engine/viewer.template.html": "PROPERTY_DATA placeholder; other hits are prose in engine markup — see P-note",
        "worker/digest.json": "BUILT output",
        "tools/check-condo-falsifier.py": "a DETECTOR string",
        "tools/guru-facts.py": "SELFTEST FIXTURES — strings the derived regexes are tested against; the rows derive, and the file's own AST check fails on a typed number outside the selftest",
        "tools/guru-probe.py": "SELFTEST FIXTURES for the inverted grader",
        ".plans/*.json": "records", ".ux-reviews/*.json": "records", ".engineering/*": "records", ".user-research/*": "records",
    }),
    # C6 1c — the SERVED text-size default is instance config (instance/<estate>.json display.defaultTextSize),
    # filled into the template's DEFAULT_SIZE. A typed `DEFAULT_SIZE = "lg"` under engine/ or tools/ is a fork.
    ("instance.display.defaultTextSize", "literal", (r'DEFAULT_SIZE\s*=\s*"(?:lg|normal)"',), {
        "viewer.html":                         "BUILT output — build-viewer.py fills {{DISPLAY:defaultTextSize}}",
        "tools/check-config-derivation.py":    "the DETECTOR string",
        ".plans/*": "records", ".engineering/*": "records", ".ux-reviews/*": "records", ".user-research/*": "records",
    }),
    ("property.address", "literal", (r"282 Church Mountain",), {
        "property.json": "canon", "viewer.html": "BUILT output (header address line + PROPERTY_DATA)", "worker/digest.json": "BUILT output",
        "birds.json": "domain _meta records the place", "amphibians.json": "domain _meta", "insects.json": "domain _meta", "lizards.json": "domain _meta",
        "mammals.json": "domain _meta", "snakes.json": "domain _meta", "fishing.json": "domain _meta", "plants.json": "domain _meta", "weeds.json": "domain _meta",
        "vehicles.json": "canon prose (an order record names the ship-to address) — content, not config",
        "questions.json": "canon prose (a card's resolution note) — content, not config",
        "engine/viewer.template.html": "PROPERTY_DATA placeholder; a hit here means the identity block stopped deriving",
        "tools/check-condo-falsifier.py": "a DETECTOR string",
        ".plans/*.json": "records", ".ux-reviews/*.json": "records", ".engineering/*": "records", ".user-research/*": "records",
    }),
    ("(deployment) AMBIENT_MAC — the station", "literal", (r"\b[0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5}\b",), {   # 2026-09-04: a MAC-SHAPED pattern, never the value — the MAC is a Worker SECRET now; any MAC in the tree is a leak
        "worker/wrangler.toml": "the ONE place the station lives — a [vars] entry per environment (C5 7c retired the code default)",
    }),
    ("frostDates.atPropertyElevation.firstFall_50pct", "type-changed", (r"\b10,\s*17\b",), {
        "property.json": "canon (as 'October 17')",
    }),
    ("frostDates.atPropertyElevation.firstFallRiskBegins", "absent-consumer", (r"firstFallRiskBegins",), {}),
]


def _files(root):
    """TRACKED files only when root is a git checkout (`.private/` is gitignored and
    holds scratch copies of the app); a plain walk otherwise (the selftest's temp dir)."""
    r = subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        for rel in r.stdout.split("\n"):
            if rel and any(fnmatch.fnmatch(os.path.basename(rel), g) for g in SCAN_GLOBS):
                yield rel
        return
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if any(fnmatch.fnmatch(fn, g) for g in SCAN_GLOBS):
                yield os.path.relpath(os.path.join(dp, fn), root)


def _strip_prose(rel, text):
    """For .py files, blank COMMENTS and DOCSTRINGS before matching — a comment that
    says "this used to be 10, 17" is not a leak; a code string still is. Other files
    are matched as-is (a leak in a JS prompt string is exactly what the lint is for)."""
    if not rel.endswith(".py"):
        return text
    lines = text.split("\n")
    import warnings
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and node.body:
                first = node.body[0]
                if isinstance(first, ast.Expr) and isinstance(getattr(first, "value", None), ast.Constant) and isinstance(first.value.value, str):
                    for ln in range(first.lineno - 1, first.end_lineno):
                        lines[ln] = ""
        for tok in tokenize.generate_tokens(io.StringIO(text).readline):
            if tok.type == tokenize.COMMENT:
                ln = tok.start[0] - 1
                lines[ln] = lines[ln][:tok.start[1]]
    except (SyntaxError, tokenize.TokenError):
        pass
    return "\n".join(lines)


def _allowed(rel, allowed):
    for g, why in allowed.items():
        if fnmatch.fnmatch(rel, g) or rel == g:
            return why
    return None


def scan(root):
    """→ (findings, notes, allowed_hits). A finding = (path, file, line, text)."""
    findings, notes, allowed_hits = [], [], []
    files = list(_files(root))
    texts = {}
    for rel in files:
        try:
            with open(os.path.join(root, rel), encoding="utf-8", errors="replace") as fh:
                texts[rel] = _strip_prose(rel, fh.read())
        except OSError:
            continue
    for path, kind, patterns, allowed in ROSTER:
        rx = re.compile("|".join(patterns))
        hits = [(rel, i + 1, line.strip()[:110]) for rel, t in texts.items()
                for i, line in enumerate(t.split("\n")) if rx.search(line)]
        if kind == "absent-consumer":
            readers = [h for h in hits if h[0] != "property.json" and not h[0].startswith(("viewer.html", "engine/", "worker/digest.json", "tools/check-config-derivation.py"))]
            notes.append("%s: %d reader(s) outside canon and built outputs%s" % (
                path, len(readers), " — a canon value nobody consumes" if not readers else ": " + ", ".join(sorted({r[0] for r in readers}))))
            continue
        for rel, ln, text in hits:
            if rel == "tools/check-config-derivation.py":
                continue
            why = _allowed(rel, allowed)
            if why is None:
                findings.append((path, rel, ln, text))
            else:
                allowed_hits.append((path, rel, why))
    return findings, notes, allowed_hits


def main(root=ROOT, quiet=False):
    findings, notes, allowed_hits = scan(root)
    if not quiet:
        print("config derivation — %d roster row(s); %d allowed hit(s) in %d location(s)\n" % (
            len(ROSTER), len(allowed_hits), len({a[1] for a in allowed_hits})))
        for n in notes:
            print("  · %s" % n)
        leaks = [a for a in allowed_hits if "KNOWN LEAK" in a[2]]
        for path, rel, why in sorted(set(leaks)):
            print("  ⚠️  %s in %s — %s" % (path, rel, why))
        if findings:
            print("\n── %d TYPED INSTANCE VALUE(S) in engine code" % len(findings))
            for path, rel, ln, text in findings:
                print("  ✗ %s  ←  %s:%d  %s" % (path, rel, ln, text))
            print("\n  fix: derive it — momlib.config(%r) — or add an allowed location WITH a reason." % findings[0][0])
        else:
            print("\n── every canon value the roster names appears only where it is allowed.")
    return 1 if findings else 0


def selftest():
    ok = True
    def check(name, cond, detail=""):
        nonlocal ok; ok &= bool(cond)
        print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + str(detail)) if detail and not cond else ""))
    print("check-config-derivation selftest\n")
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "tools")); os.makedirs(os.path.join(d, "images", "property-map"))
        open(os.path.join(d, "property.json"), "w").write('{"frostDates": {"atPropertyElevation": {"firstFall_50pct": "October 17"}}}')
        f, _, _ = scan(d)
        check("a clean tree has no findings", f == [], f)
        tool = os.path.join(d, "tools", "scratch_probe.py")
        open(tool, "w").write("FROST_MONTH, FROST_DAY = 10, 17\n")
        f, _, _ = scan(d)
        check("PLANT `FROST_MONTH, FROST_DAY = 10, 17` in a tool → FIRES (type-changed)",
              any(x[0].endswith("firstFall_50pct") and x[1] == "tools/scratch_probe.py" for x in f), f)
        open(tool, "w").write("FROST_MONTH, FROST_DAY = momlib.parse_month_day(momlib.config('frostDates.atPropertyElevation.firstFall_50pct'))\n")
        f, _, _ = scan(d)
        check("derive it → CLEARS", f == [], f)
        open(os.path.join(d, "images", "property-map", "x.bounds.json"), "w").write('{"anchor": 34.5496}')
        f, _, _ = scan(d)
        check("`34.5496` in an ALLOWED location (a bounds record) → silent", f == [], f)
        open(tool, "w").write("LAT = 34.5496\n")
        f, _, _ = scan(d)
        check("`34.5496` typed in a tool → FIRES (literal)", any(x[1] == "tools/scratch_probe.py" for x in f), f)
        open(tool, "w").write("ELEV_FT = 2873\n")
        f, _, _ = scan(d)
        check("`2873` typed in a tool → FIRES", any(x[0].endswith("estimated_ft") for x in f), f)
        os.makedirs(os.path.join(d, "engine"), exist_ok=True)
        eng = os.path.join(d, "engine", "scratch.template.html")
        open(eng, "w").write('<script>\n  const DEFAULT_SIZE = "lg";\n</script>\n')
        f, _, _ = scan(d)
        check("PLANT `DEFAULT_SIZE = \"lg\"` under engine/ → FIRES (C6 1c: the served default is instance config)",
              any(x[0] == "instance.display.defaultTextSize" and x[1].startswith("engine/") for x in f), f)
        open(eng, "w").write('<script>\n  const DEFAULT_SIZE = "{{DISPLAY:defaultTextSize}}";\n</script>\n')
        f, _, _ = scan(d)
        check("the placeholder in its place → CLEARS", not any(x[0] == "instance.display.defaultTextSize" for x in f), f)
        open(tool, "w").write("x = 2873/1000*7  # a computed copy\n")
        f, _, _ = scan(d)
        check("BLIND SPOT, stated not hidden: a computed copy still contains the literal here, but `2.873` or a lapse-rate result would not — documented in the docstring",
              "BLIND SPOTS" in open(__file__).read())
    r = main(quiet=True)
    check("the live tree is clean today (every hit allowed with a reason)", r == 0, "run without --selftest to see the findings")
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true", help="{count} of un-allowed hits — check-engine-manifest's P4 reads it")
    a = ap.parse_args()
    if a.json:
        f, _, _ = scan(ROOT); print(json.dumps({"count": len(f), "findings": [{"path": x[0], "file": x[1], "line": x[2]} for x in f]})); sys.exit(0)
    sys.exit(selftest() if a.selftest else main())
