#!/usr/bin/env python3
"""check-estate-neutral.py — does the arrival surface leak ANOTHER household into a new one?

    python3 tools/check-estate-neutral.py              # check estate/index.html on disk
    python3 tools/check-estate-neutral.py --url <u>    # check what an origin actually SERVES
    python3 tools/check-estate-neutral.py --selftest   # prove the needles still bite

⛔ THE FINDING THIS EXISTS FOR (ux-expert, 2026-09-06, ranked above every other finding in its
review). The tempting way to build a "buildout in progress" view is `viewer.html` with the cards
hidden. That re-ships the tenancy leak through six surfaces card-hiding does not touch — the
masthead suffix, the jump strip, Garden Guru's digest, the acknowledgment ribbon, the release notes
and the weather station. Each one names Fernwood, or Jasper, or the Blue Ridge, or a species that
grows at 2,873 ft in north Georgia, to a reader who lives in Bangor, Maine.

⭐ ITS FALSIFIER, WHICH IS THE POINT: load the surface a brand-new estate is served and grep it for
every token that belongs to ONE household. Zero hits, or it is not shipped. That is mechanical, it
needs no judgement, and it answers "is this actually neutral?" without asking anyone — the
non-AI-door rule applied to a tenancy claim.

⚠️ THE NEEDLES ARE READ FROM CANON, NEVER RESTATED. A hand-typed list of species would drift the
first time a plant is added, and a check that quietly stops covering new canon is worse than none.
The fixed tokens are the place's identity; the species come from the canon files themselves.

⛔ NEVER GREEN BY ABSENCE. No page, or no needles, is UNCHECKABLE (exit 3) and never a pass — the
same posture as check-public-build.py. A check that reports clean because it found nothing to look
for is the failure mode this repo pays for most often.
"""
import argparse, glob, json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ⛔ THIS SCANNED ONE FILE. Fixed 2026-09-06 — the FIFTH instance of this shape in one day
# (check-storage-keys three times, household-export's --env list, now this). The checker that exists
# to prove a household origin names no other household read `estate/index.html` and nothing else,
# while `pages-deploy.py` shipped five other files to that origin. It missed a street address in a
# comment on `onboarding/index.html`, the page a stranger actually lands on.
# ⭐ DERIVED FROM WHAT IS ACTUALLY SHIPPED, never a typed path: the roster is pages-deploy's own
# HOUSEHOLD_ALLOW — one roster, two readers, the arrangement this file already uses for its needles.
def _shipped_pages():
    import importlib.util as _ilu
    try:
        spec = _ilu.spec_from_file_location("pd", os.path.join(ROOT, "tools", "pages-deploy.py"))
        pd = _ilu.module_from_spec(spec); spec.loader.exec_module(pd)
        allow = [a for a in pd.HOUSEHOLD_ALLOW if a.endswith((".html", ".md"))]
        # ⛔ `index.html` IS NOT SHIPPED AS WRITTEN — `pages-deploy.py` OVERWRITES it in the export
        # with a generated "My Home" redirect, precisely because the tracked one points at
        # viewer.html. Scanning the repo file therefore reports a leak that cannot reach a reader:
        # measured 2026-09-06, the file says `<title>Fernwood</title>` while the origin serves
        # `<title>My Home</title>`. ⭐ Excluded WITH ITS REASON rather than allow-listed as a token —
        # the file is out of scope, the string is not forgiven. Use `--url` to check the real origin,
        # which is the only surface that can answer for a generated file.
        # ⛔ TWO SHIPPED FILES ARE GENERATED AT DEPLOY AND ARE NOT WHAT THE REPO HOLDS:
        #   index.html   — pages-deploy OVERWRITES it with a "My Home" redirect.
        #   viewer.html  — pages-deploy REBUILDS it from `instance/<env>.json`, so a household
        #                  origin serves ITS OWN app. The tracked file is FERNWOOD'S build and is
        #                  supposed to name Fernwood; scanning it reports 309 tokens that no
        #                  household can reach.
        # ⭐ EXCLUDED WITH THEIR REASON, never allow-listed as tokens: the FILES are out of scope
        # for a static scan, the STRINGS are not forgiven. The only honest check for a generated
        # file is the ORIGIN — `--url https://<host>/viewer.html` — or the built artifact itself,
        # `--page /tmp/<neutral build>`. Both are used; neither is optional.
        allow = [a for a in allow if a not in ("index.html", "viewer.html")]
    except Exception:
        allow = []
    out = [os.path.join(ROOT, *a.split("/")) for a in allow]
    return [p for p in out if os.path.exists(p)]


PAGES = _shipped_pages()
# ⚠️ A derivation that finds nothing must be VISIBLE, never a silent fallback to the old single file.
PAGE = PAGES[0] if PAGES else os.path.join(ROOT, "estate", "index.html")

# The place's own identity — what makes Fernwood Fernwood rather than a property app.
FIXED = ["Fernwood", "Jasper", "Church Mountain", "Blue Ridge", "Cherokee", "Tate Mountain",
         "Lake Sequoyah", "2,873", "2873", "Sequoyah", "Appalachian Almanac"]

# Canon files whose records name living things that grow at ONE address.
CANON = ["plants.json", "weeds.json", "birds.json", "mammals.json", "amphibians.json",
         "fish.json", "lizards.json", "snakes.json", "insects.json", "vehicles.json"]


def species_needles(root=ROOT):
    """Every name and scientificName in canon. Read, never restated."""
    out = set()
    for fn in CANON:
        p = os.path.join(root, fn)
        if not os.path.exists(p):
            continue
        try:
            data = json.load(open(p, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        stack = [data]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                for k, v in node.items():
                    if k in ("name", "scientificName", "nickname") and isinstance(v, str):
                        v = v.strip()
                        # Short or generic words would false-positive on ordinary prose.
                        if len(v) >= 5 and " " in v or len(v) >= 8:
                            out.add(v)
                    else:
                        stack.append(v)
            elif isinstance(node, list):
                stack.extend(node)
    return sorted(out)


def hits_in(text, needles):
    """→ [(needle, line_no, excerpt)] — case-insensitive, whole-token where it matters."""
    found = []
    lines = text.splitlines()
    low = [l.lower() for l in lines]
    for n in needles:
        nl = n.lower()
        for i, l in enumerate(low):
            if nl in l:
                found.append((n, i + 1, lines[i].strip()[:100]))
                break          # one witness per needle is enough to fail
    return found


def strip_comments(html):
    """⛔ A NEEDLE INSIDE AN HTML COMMENT IS NOT SERVED TO A READER — and this file's own header
    explains the defect by NAMING Fernwood, Jasper and the Blue Ridge. Checking raw bytes would
    make the explanation of the leak indistinguishable from the leak, so the check would fail on a
    page that is correct and the honest fix would be to delete the reasoning. Comments are stripped
    before matching, and script/style content is kept, because those DO reach the reader."""
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    # ⛔ AND URLs/HOSTNAMES ARE INFRASTRUCTURE, NOT A HOUSEHOLD'S IDENTITY. The Worker endpoints are
    # literally named `fernwood-qa`/`fernwood-home` — CLAUDE.md is explicit that the repo path,
    # GitHub repo and Worker URL "are infrastructure-level identifiers, not user-facing." A reader
    # never sees them; renaming them is a data-migration risk taken for no reader's benefit.
    # ⚠️ THIS IS A CONTEXTUAL EXCLUSION, NOT AN ALLOW-LIST, and the difference is the whole point:
    # it removes a PLACE a needle may appear (inside a URL), never a needle. "Fernwood" rendered in
    # a heading still fails, which the selftest asserts in both directions.
    html = re.sub(r"https?://[^\s\"'<>)]+", " ", html)
    # ⛔ AND A JS LINE COMMENT REACHES A READER EXACTLY AS MUCH AS AN HTML ONE — which is to say not
    # at all. Excluding one and not the other would be arbitrary: both are explanation in source,
    # neither renders. ⚠️ ORDER MATTERS — URLs are stripped FIRST, so the `//` in `https://` is
    # already gone and cannot be mistaken for the start of a comment. A needle in executable code,
    # including a string literal, is still checked; the selftest asserts that direction too.
    html = re.sub(r"(?m)//.*$", " ", html)
    # ⛔ AND CSS BLOCK COMMENTS. Found 2026-09-06 running a household export: onboarding's stylesheet
    # explains, in /* */, why it does NOT use Fernwood's green — and the check read that explanation
    # as the leak. Same rule as the other two: it does not reach a reader, so it is not checked.
    return re.sub(r"/\*.*?\*/", " ", html, flags=re.S)


def load(url=None, page=PAGE):
    if url:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        try:
            import qa_access
            for k, v in (qa_access.headers(url) or {}).items():
                req.add_header(k, v)
        except Exception:
            pass
        with urllib.request.urlopen(req, timeout=30) as f:
            return f.read().decode("utf-8", "replace")
    return open(page, encoding="utf-8").read()


def selftest():
    fails = []

    def check(name, ok, why=""):
        print("  %s %-52s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    needles = FIXED + species_needles()
    check("needles are READ from canon, not restated", len(needles) > len(FIXED),
          "only the %d fixed tokens — canon contributed nothing, so new species go unchecked" % len(FIXED))

    # ⭐ SEEN TO FAIL: the exact thing ux-expert warned about — the Fernwood viewer with cards hidden.
    leaky = "<html><body><h1>Fernwood</h1><p>282 Church Mountain Road, Jasper</p></body></html>"
    check("a page carrying the Fernwood masthead FAILS", len(hits_in(strip_comments(leaky), needles)) >= 2,
          "the leak this tool exists to catch went undetected")

    clean = "<html><body><h1>My Home</h1><p>87 Quarry Hill Rd, Bangor, ME</p></body></html>"
    check("a genuinely neutral page passes", not hits_in(strip_comments(clean), needles),
          "false positive on a page that names no household")

    commented = "<html><!-- explains the Fernwood leak in Jasper --><body><h1>My Home</h1></body></html>"
    check("a needle inside an HTML COMMENT does not fail the page",
          not hits_in(strip_comments(commented), needles),
          "the explanation of the defect is being read as the defect")

    # A needle in a SCRIPT does reach the reader and must still fail.
    scripted = '<html><body><script>var t = "Fernwood";</script></body></html>'
    check("a needle inside <script> still FAILS", hits_in(strip_comments(scripted), needles),
          "script content reaches the reader and must be checked")

    urlonly = '<html><body><script>var W = "https://fernwood-qa.paul-kirschenbauer.workers.dev";</script></body></html>'
    check("a needle only inside a URL does not fail the page", not hits_in(strip_comments(urlonly), needles),
          "an infrastructure hostname is being read as a household leak")

    # ⭐ THE OTHER DIRECTION, which is what stops the exclusion becoming a hole.
    both = '<html><body><h1>Fernwood</h1><script>var W="https://fernwood-qa.workers.dev";</script></body></html>'
    check("a VISIBLE needle still fails even beside a URL", hits_in(strip_comments(both), needles),
          "the URL exclusion swallowed a real leak in a heading")

    jscomment = '<html><body><script>// explains the Fernwood leak\nvar x = 1;</script></body></html>'
    check("a needle in a JS // comment does not fail the page",
          not hits_in(strip_comments(jscomment), needles),
          "source explanation is being read as rendered content")

    css = '<html><style>/* not Fernwood green, deliberately */</style><body><h1>My Home</h1></body></html>'
    check("a needle in a CSS /* */ comment does not fail the page",
          not hits_in(strip_comments(css), needles),
          "a stylesheet's own reasoning is being read as rendered content")

    check("an EMPTY needle list is uncheckable, never a pass", not hits_in(clean, []),
          "no needles must never render as clean")

    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", 10 - len(fails), 10))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description="the arrival surface must name no other household")
    ap.add_argument("--url", help="check what an origin actually serves (default: the file on disk)")
    ap.add_argument("--page", default=PAGE)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    needles = FIXED + species_needles()
    if len(needles) <= len(FIXED):
        print("⚠️  UNCHECKABLE — canon contributed no species needles (looked for %s in %s)."
              % (", ".join(CANON[:3]) + " …", ROOT))
        print("   A check that covers only the fixed tokens is not the check that was asked for.")
        return 3
    try:
        html = load(a.url, a.page)
    except (OSError, ValueError) as e:
        print("⚠️  UNCHECKABLE — could not read the surface: %s" % e)
        return 3

    # ⭐ SWEEP EVERY SHIPPED PAGE, not just the first. A --page or --url names ONE surface
    # deliberately; the default is the whole set a household origin actually serves.
    targets = [(a.url, None)] if a.url else (
        [(None, a.page)] if a.page != PAGE else [(None, p) for p in PAGES])
    if not targets:
        print("⚠️  UNCHECKABLE — no shipped pages derived from pages-deploy's allow-list.")
        return 3

    total, worst = 0, 0
    print("check-estate-neutral — %d surface(s) · %d needle(s)\n" % (len(targets), len(needles)))
    for url, page in targets:
        try:
            body = load(url, page) if url else load(None, page)
        except (OSError, ValueError) as e:
            print("  ⚠️  UNCHECKABLE  %s — %s" % (url or page, e)); worst = max(worst, 3); continue
        where = url or os.path.relpath(page, ROOT)
        # ⛔ COMMENTS ARE STRIPPED FOR THE RENDERED CHECK, AND SCANNED SEPARATELY. A comment renders
        # nothing but SHIPS in the source a stranger can read — measured 2026-09-06, a street address
        # sat in a JS comment on the onboarding page and passed every check for exactly this reason.
        rendered = hits_in(strip_comments(body), needles)
        in_source = hits_in(body, needles)
        only_comment = [h for h in in_source if h not in rendered]
        mark = "🔴" if rendered else ("⚠️ " if only_comment else "✅")
        print("  %s %-30s %7d bytes  rendered=%d  in-comments=%d"
              % (mark, where, len(body), len(rendered), len(only_comment)))
        for n, line, excerpt in rendered[:6]:
            print("       🔴 %-24s line %-5d %s" % (repr(n), line, excerpt))
        for n, line, excerpt in only_comment[:4]:
            print("       ⚠️  %-24s line %-5d (comment — renders nothing, ships anyway)" % (repr(n), line))
        total += len(rendered)
        worst = max(worst, 1 if rendered else 0)

    if worst == 0:
        # ⛔ NEVER A BARE ✅. The old line read *"every shipped surface names no other household"* —
        # a WHOLE-SURFACE claim from a scan that deliberately excludes `viewer.html` (see
        # `_shipped_pages`), which is the generated file and the one a real leak was found in on
        # 2026-09-07: Fernwood's own rain gauge, "0.01\" past 7d here" and "at OUR gauge", served to
        # a household in Bangor, Maine.
        #
        # ⭐ THE FAILURE THAT MADE THIS NECESSARY WAS READING A GREEN RATHER THAN A SCOPE `[lane-F,
        # 2026-09-07, on its own mistake]`. The scope was already stated — in a comment, in capitals,
        # with the word "optional" in it — and the bare form is what CLAUDE.md's session-start block
        # prints, so the green most sessions ever see says nothing about the viewer. A tick that
        # looks like coverage is worse than no tick.
        #
        # ⚠️ OUTPUT ONLY. Exit codes are untouched: `pages-deploy.py:246` imports this module's
        # NEEDLES and walks the export itself, so nothing that gates a deploy changes here.
        scanned = ", ".join((u if u else os.path.relpath(pg, ROOT)) for u, pg in targets)
        print("\n✅ NO OTHER HOUSEHOLD IS NAMED IN WHAT THIS RUN SCANNED — and that is not the whole surface.")
        print("   scanned (%d): %s" % (len(targets), scanned))
        if not a.url:
            print("   ⛔ NOT scanned: `viewer.html` — generated per instance, excluded by design, and")
            print("      the file the 2026-09-07 leak was in. This run says NOTHING about it.")
            print("      Complete it, and neither is optional:")
            print("        python3 tools/check-estate-neutral.py --url https://<origin>/viewer.html")
            print("        python3 tools/check-estate-neutral.py --page /tmp/<neutral build>")
        print("   ⚠️ AND IT TESTS FOR NAMES. Measured 2026-09-07: a household's own gauge readings and")
        print("      first-person-plural prose (\"at OUR gauge\", \"0.01\" past 7d here\") passed 311")
        print("      needles with rendered=0. Numbers and pronouns are outside this roster.")
        return 0
    if total:
        print("\n🔴 %d household-specific token(s) REACH THE READER." % total)
        print("A brand-new estate is being shown another household's place. This is the tenancy leak")
        print("wearing a different surface — fix the surface, do not add the token to an allow-list.")
    return worst


if __name__ == "__main__":
    sys.exit(main())
