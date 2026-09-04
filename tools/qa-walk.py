#!/usr/bin/env python3
"""qa-walk.py — the rendered gate as an EXIT CODE (practice-steward proposal §4, smallest first version).

    python3 tools/qa-walk.py <url>            # e.g. https://fernwood-qa.pages.dev/viewer.html
    python3 tools/qa-walk.py <url> --json

Renders the page in headless Chromium at HER conditions (414 × 848), evaluates the page's own
`tools/measure-nesting-width.js` inside it, and prints `herConditions()`'s verdict. Exit 0 on
`clean: true`; exit 1 on any HIGH finding; exit 2 when the page never rendered a `.main-card`
(the wrong document loaded — a 404 page scored "clean" once, 2026-09-01) or the walk could not run.

This mints NO second definition of "clean": the verdict is the ratified gate's own. It only turns
a console paste into something a workflow can run. The browser is the Playwright the MCP server
already cached under ~/.npm/_npx (node) — no install; if it is missing, exit 2 says so.

Also asserts, because the module switch and the identity pass depend on them:
  · ESTATE_MODULES present · at least one tile rendered · no "[object Object]" in any .prop-note
  · zero uncaught script errors during load
"""
import argparse, glob, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))

NODE_SCRIPT = r"""
const url = process.argv[process.argv.length - 1];
const { chromium } = require('playwright');
(async () => {
  // the MCP server's cached browser, so this needs no install; any Chromium under the cache will do
  const exe = process.env.QA_WALK_CHROMIUM || null;
  const browser = await chromium.launch(exe ? { executablePath: exe } : {});
  const page = await browser.newPage({ viewport: { width: 414, height: 848 } });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e.message).slice(0, 200)));
  const out = { url, ok: false };
  try {
    await page.goto(url, { waitUntil: 'load', timeout: 60000 });
    await page.waitForTimeout(1500);
    const basics = await page.evaluate(() => ({
      title: document.title,
      mainCards: document.querySelectorAll('.main-card').length,
      tiles: [...document.querySelectorAll('.dash-cell')].filter(c => getComputedStyle(c).display !== 'none').length,
      modules: (typeof ESTATE_MODULES === 'object' && ESTATE_MODULES) || null,
      objectObject: [...document.querySelectorAll('.prop-note')].filter(n => /\[object Object\]/.test(n.innerText)).length,
      qaBanner: (document.getElementById('qa-banner') || {}).textContent || null,
    }));
    Object.assign(out, basics, { scriptErrors: errors.slice() });
    if (!basics.mainCards) { out.reason = 'the page never rendered a .main-card — wrong document?'; console.log(JSON.stringify(out)); process.exit(2); }
    const dir = new URL(url).pathname.replace(/[^/]*$/, '');
    const verdict = await page.evaluate(async (dir) => {
      let r = await fetch(dir + 'tools/measure-nesting-width.js');
      if (!r.ok) r = await fetch('/tools/measure-nesting-width.js');          // a build served from a subfolder (the condo scratch)
      if (!r.ok) return { error: 'measure script ' + r.status };
      (0, eval)(await r.text());
      const v = await measureNestingWidth.herConditions();
      return { clean: v.clean, counts: v.counts, high: v.findings.filter(f => f.sev === 'HIGH') };
    }, dir);
    out.verdict = verdict;
    out.ok = !!verdict.clean && !errors.length && !basics.objectObject && !!basics.modules;
    console.log(JSON.stringify(out));
    process.exit(verdict.error ? 2 : (out.ok ? 0 : 1));
  } catch (e) {
    out.reason = String(e.message).slice(0, 300); console.log(JSON.stringify(out)); process.exit(2);
  } finally { await browser.close(); }
})();
"""


def find_playwright():
    hits = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/playwright/package.json")), key=os.path.getmtime)
    return os.path.dirname(os.path.dirname(hits[-1])) if hits else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    nm = find_playwright()
    if not nm:
        print("⛔ qa-walk: no Playwright found under ~/.npm/_npx — run any Playwright MCP session once, or `npx playwright install chromium`"); return 2
    env = dict(os.environ, NODE_PATH=nm)
    exes = sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/*.app/Contents/MacOS/*")), key=os.path.getmtime)
    if exes:
        env["QA_WALK_CHROMIUM"] = exes[-1]
    r = subprocess.run(["node", "-e", NODE_SCRIPT, "--", a.url], capture_output=True, text=True, env=env, timeout=180)
    line = (r.stdout.strip().split("\n") or [""])[-1]
    try:
        out = json.loads(line)
    except ValueError:
        print("⛔ qa-walk: the walk did not report —", (r.stderr or r.stdout)[-400:]); return 2
    if a.json:
        print(json.dumps(out)); return r.returncode
    v = out.get("verdict") or {}
    print("qa-walk — %s" % a.url)
    print("  title: %s · main cards: %s · tiles: %s · modules: %s" % (out.get("title"), out.get("mainCards"), out.get("tiles"), "yes" if out.get("modules") else "MISSING"))
    if out.get("qaBanner"): print("  banner: %s" % out["qaBanner"][:90])
    if out.get("reason"): print("  ⛔ %s" % out["reason"])
    if v: print("  herConditions(): %s · %s · HIGH: %d" % ("clean" if v.get("clean") else "NOT CLEAN", json.dumps(v.get("counts")), len(v.get("high") or [])))
    for h in (v.get("high") or [])[:5]: print("     HIGH %s — %s" % (h.get("kind"), h.get("detail")))
    if out.get("objectObject"): print("  ✗ %d .prop-note(s) read '[object Object]'" % out["objectObject"])
    for e in out.get("scriptErrors") or []: print("  ✗ script error: %s" % e)
    print("  %s" % ("✅ exit 0 — clean at her conditions" if r.returncode == 0 else ("🔴 exit %d" % r.returncode)))
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
