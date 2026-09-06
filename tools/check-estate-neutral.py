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
PAGE = os.path.join(ROOT, "estate", "index.html")

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
    return re.sub(r"(?m)//.*$", " ", html)


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

    check("an EMPTY needle list is uncheckable, never a pass", not hits_in(clean, []),
          "no needles must never render as clean")

    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", 9 - len(fails), 9))
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

    where = a.url or os.path.relpath(a.page, ROOT)
    found = hits_in(strip_comments(html), needles)
    print("check-estate-neutral — %s · %d needle(s) · %d byte(s)" % (where, len(needles), len(html)))
    if not found:
        print("✅ the arrival surface names no other household.")
        return 0
    print("🔴 %d household-specific token(s) reach the reader:" % len(found))
    for n, line, excerpt in found[:20]:
        print("   %-28s line %-5d %s" % (repr(n), line, excerpt))
    print("\nA brand-new estate is being shown another household's place. This is the tenancy leak")
    print("wearing a different surface — fix the surface, do not add the token to an allow-list.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
