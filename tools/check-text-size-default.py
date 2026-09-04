#!/usr/bin/env python3
"""check-text-size-default.py — C6 1b/1c's rendered assertions, as an exit code.
    python3 tools/check-text-size-default.py <url-or-path> [--expect lg|normal]
Two fresh browser contexts at HER conditions (414 × 848), every /api/* request blocked so the page
proves itself with no Worker:
  1. NO stored preference → body carries `.text-lg` iff the expected default is "lg"; the metrics buffer
     holds exactly one `text_size_served` with {size:<default>, stored:false}; and `tateTracker.textSize`
     is STILL ABSENT afterwards — nothing is written to storage on a default (the decision block's rule 1:
     stamping the default would forge a choice).
  2. `tateTracker.textSize = "normal"` stored → body renders A (no `.text-lg`) and `text_size_served` reads
     {size:"normal", stored:true} — the stored key wins, which is the proof her configured device behaves
     as yesterday whatever the served default becomes.
Exit 0 all assertions hold · 1 an assertion failed · 2 the page never rendered / the walk could not run.
`--expect` defaults to the value in instance/fernwood.json (read, not retyped). Browser discovery is
qa-walk.py's: the Playwright the MCP server cached under ~/.npm/_npx, no install.
"""
import argparse, glob, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import qa_access
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
NODE = r"""
const [url, expect] = process.argv.slice(-2);
const { chromium } = require('playwright');
(async () => {
  const exe = process.env.QA_WALK_CHROMIUM || null;
  const browser = await chromium.launch(exe ? { executablePath: exe } : {});
  const out = { url, expect, contexts: [] };
  async function walk(label, init) {
    const ctx = await browser.newContext({ viewport: { width: 414, height: 848 }, extraHTTPHeaders: JSON.parse(process.env.QA_ACCESS_HEADERS || '{}') });
    await ctx.route('**/api/**', r => r.abort());
    if (init) await ctx.addInitScript(init);
    const page = await ctx.newPage();
    const errors = []; page.on('pageerror', e => errors.push(String(e.message).slice(0, 160)));
    const rec = { label, ok: false, errors };
    try {
      await page.goto(url, { waitUntil: 'load', timeout: 60000 });
      await page.waitForTimeout(800);
      Object.assign(rec, await page.evaluate(() => {
        let buf = []; try { buf = JSON.parse(localStorage.getItem('tateTracker.metrics.v1') || '[]'); } catch (e) {}
        const served = buf.filter(e => e.type === 'text_size_served').map(e => ({ size: e.size, stored: e.stored }));
        let storedKey = null; try { storedKey = localStorage.getItem('tateTracker.textSize'); } catch (e) {}
        return { rendered: document.querySelectorAll('.main-card').length > 0, textLg: document.body.classList.contains('text-lg'),
                 served, storedKey };
      }));
      rec.ok = true;
    } catch (e) { rec.error = String(e.message).slice(0, 200); }
    await ctx.close(); out.contexts.push(rec);
  }
  await walk('fresh', null);
  await walk('stored-normal', "try { localStorage.setItem('tateTracker.textSize', 'normal'); } catch (e) {}");
  await browser.close();
  console.log(JSON.stringify(out));
})().catch(e => { console.log(JSON.stringify({ fatal: String(e.message) })); process.exit(2); });
"""

def find_playwright():
    hits = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/playwright/package.json")), key=os.path.getmtime)
    return os.path.dirname(os.path.dirname(hits[-1])) if hits else None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("url"); ap.add_argument("--expect", choices=("lg", "normal")); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    expect = a.expect or json.load(open(os.path.join(ROOT, "instance", "fernwood.json")))["display"]["defaultTextSize"]
    url = a.url if "://" in a.url else "file://" + os.path.abspath(a.url)
    nm = find_playwright()
    if not nm: print("⛔ no Playwright under ~/.npm/_npx — run any Playwright MCP session once"); return 2
    env = dict(os.environ, NODE_PATH=nm, QA_ACCESS_HEADERS=json.dumps(qa_access.headers(url)))
    exes = sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/*.app/Contents/MacOS/*")), key=os.path.getmtime)
    if exes: env["QA_WALK_CHROMIUM"] = exes[-1]
    r = subprocess.run(["node", "-e", NODE, "--", url, expect], capture_output=True, text=True, env=env, timeout=240)
    line = [l for l in r.stdout.strip().split("\n") if l.startswith("{")]
    if not line: print("⛔ walk produced no verdict\n" + r.stderr[-800:]); return 2
    out = json.loads(line[-1])
    if a.json: print(json.dumps(out, indent=1)); 
    if "fatal" in out: print("⛔ " + out["fatal"]); return 2
    fresh, stored = out["contexts"]
    fails = []
    for c in (fresh, stored):
        if not c["ok"] or not c.get("rendered"): print("⛔ %s: page never rendered a .main-card (%s)" % (c["label"], c.get("error", "no error text"))); return 2
        if c["errors"]: fails.append("%s: uncaught script errors: %s" % (c["label"], c["errors"]))
    want_lg = expect == "lg"
    if fresh["textLg"] != want_lg: fails.append("fresh: body.text-lg=%s, expected %s (default %s)" % (fresh["textLg"], want_lg, expect))
    if fresh["served"] != [{"size": expect, "stored": False}]: fails.append("fresh: text_size_served=%s, expected one {size:%s, stored:false}" % (fresh["served"], expect))
    if fresh["storedKey"] is not None: fails.append("fresh: tateTracker.textSize=%r was WRITTEN on a default — a forged choice" % fresh["storedKey"])
    if stored["textLg"]: fails.append("stored-normal: body carries .text-lg — the stored key did not win")
    if stored["served"] != [{"size": "normal", "stored": True}]: fails.append("stored-normal: text_size_served=%s, expected one {size:normal, stored:true}" % stored["served"])
    print("check-text-size-default · %s · expect %s" % (url, expect))
    print("  fresh:         text-lg=%s served=%s stored-key=%r" % (fresh["textLg"], fresh["served"], fresh["storedKey"]))
    print("  stored-normal: text-lg=%s served=%s" % (stored["textLg"], stored["served"]))
    for f in fails: print("  🔴 " + f)
    print("  %s" % ("✅ the served default is %s and a stored choice still wins" % expect if not fails else "🔴 %d assertion(s) failed" % len(fails)))
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
