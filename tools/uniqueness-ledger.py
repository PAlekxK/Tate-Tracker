#!/usr/bin/env python3
"""uniqueness-ledger.py — what two rendered estates SHARE and what is UNIQUE to each (paul-asked 2026-09-03).

    python3 tools/uniqueness-ledger.py <urlA> <urlB> [--out ledger.json] [--top 40]

Renders both pages headless at 414×848 (the cached Playwright, like qa-walk.py), takes every visible
text node, splits into sentences, and buckets them:
  SHARED    identical sentences on both pages — boilerplate candidates: engine prose that names no place.
            Right for a control label; WRONG for a sentence about "this slope" that reads the same at a condo.
  UNIQUE-A / UNIQUE-B   sentences only one estate renders — the instance speaking.
It also reports the accent colours in use (CSS custom properties on :root + the header background), so
"down to the theme colour" has a measurement: two estates with identical colours share a theme they did
not choose. Paul: "track what's dynamic and unique and where there's boilerplate text that may just be
left over and not part of our official vocabulary — having two properties compare over time will help."
"""
import argparse, glob, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import qa_access

HERE = os.path.dirname(os.path.abspath(__file__))
NODE = r"""
const [a, b] = process.argv.slice(-2);
const { chromium } = require('playwright');
(async () => {
  const exe = process.env.QA_WALK_CHROMIUM || null;
  const browser = await chromium.launch(exe ? { executablePath: exe } : {});
  const out = {};
  for (const url of [a, b]) {
    const page = await browser.newPage({ viewport: { width: 414, height: 848 }, extraHTTPHeaders: JSON.parse(process.env.QA_ACCESS_HEADERS || '{}') });
    await page.goto(url, { waitUntil: 'load', timeout: 60000 }); await page.waitForTimeout(2500);
    out[url] = await page.evaluate(() => {
      const texts = []; const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      let n; while ((n = w.nextNode())) { const el = n.parentElement; if (!el || ['SCRIPT','STYLE','NOSCRIPT'].includes(el.tagName)) continue;
        const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
        const t = n.textContent.replace(/\s+/g, ' ').trim(); if (t.length > 1) texts.push(t); }
      const root = getComputedStyle(document.documentElement); const vars = {};
      for (const sheet of document.styleSheets) { try { for (const r of sheet.cssRules) { if (r.selectorText === ':root' && r.style) for (const p of r.style) if (p.startsWith('--')) vars[p] = r.style.getPropertyValue(p).trim(); } } catch (e) {} }
      const header = document.querySelector('.header'); const strip = document.querySelector('.dash-strip');
      return { title: document.title, texts, theme: { vars, headerBg: header ? getComputedStyle(header).backgroundImage || getComputedStyle(header).backgroundColor : null, stripBg: strip ? getComputedStyle(strip).backgroundImage : null } };
    });
    await page.close();
  }
  await browser.close(); console.log(JSON.stringify(out));
})();
"""


def sentences(texts):
    out = set()
    for t in texts:
        for s in re.split(r"(?<=[.!?])\s+", t):
            s = s.strip()
            if len(s) >= 12 and re.search(r"[A-Za-z]{3}", s):
                out.add(s)
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--out"); ap.add_argument("--top", type=int, default=40)
    args = ap.parse_args()
    hits = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/playwright/package.json")), key=os.path.getmtime)
    if not hits: print("⛔ no Playwright under ~/.npm/_npx"); return 2
    env = dict(os.environ, NODE_PATH=os.path.dirname(os.path.dirname(hits[-1])), QA_ACCESS_HEADERS=json.dumps(qa_access.headers(args.a) or qa_access.headers(args.b)))
    exes = sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/*.app/Contents/MacOS/*")), key=os.path.getmtime)
    if exes: env["QA_WALK_CHROMIUM"] = exes[-1]
    r = subprocess.run(["node", "-e", NODE, "--", args.a, args.b], capture_output=True, text=True, env=env, timeout=300)
    try:
        data = json.loads(r.stdout.strip().split("\n")[-1])
    except Exception:  # noqa: BLE001
        print("⛔ the walk did not report —", (r.stderr or r.stdout)[-400:]); return 2
    A, B = data[args.a], data[args.b]
    sa, sb = sentences(A["texts"]), sentences(B["texts"])
    shared, ua, ub = sorted(sa & sb), sorted(sa - sb), sorted(sb - sa)
    theme_same = A["theme"] == B["theme"]
    ledger = {"a": {"url": args.a, "title": A["title"], "sentences": len(sa)}, "b": {"url": args.b, "title": B["title"], "sentences": len(sb)},
              "shared": shared, "uniqueA": ua, "uniqueB": ub, "themeIdentical": theme_same, "themeA": A["theme"], "themeB": B["theme"]}
    if args.out:
        json.dump(ledger, open(args.out, "w"), indent=1, ensure_ascii=False)
    print("uniqueness ledger — %s (%d sentences) vs %s (%d sentences)" % (A["title"], len(sa), B["title"], len(sb)))
    print("  SHARED %d · UNIQUE to %s %d · UNIQUE to %s %d" % (len(shared), A["title"], len(ua), B["title"], len(ub)))
    print("  THEME: %s — %s" % ("IDENTICAL" if theme_same else "differs", "two estates wearing one colour scheme neither chose (identity.theme is the backlog item)" if theme_same else "the instances diverge"))
    place_words = re.compile(r"\b(slope|property|this place|the lake|the house|ridge|mountain|here)\b", re.I)
    suspect = [s for s in shared if place_words.search(s)]
    print("\n  SHARED sentences that speak of a PLACE (boilerplate that should probably be instance prose or gone) — %d:" % len(suspect))
    for s in suspect[:args.top]: print("    · %s" % s[:150])
    print("\n  a sample of other shared sentences (%d total):" % len(shared))
    for s in [x for x in shared if x not in suspect][:12]: print("    · %s" % s[:120])
    if args.out: print("\n  full ledger → %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
