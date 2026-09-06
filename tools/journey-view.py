#!/usr/bin/env python3
"""journey-view.py — open a link and describe what is on the screen. Nothing else.

    python3 tools/journey-view.py "<url>"
    python3 tools/journey-view.py "<url>" --do "click:#go1" --do "type:#a1=123 Main St"

Built for the RECEIVING side of a journey walk: a reader who was handed a link and has to get
somewhere with it. It reports what a person would see — the visible words, the fields, the buttons —
and never what the code is doing.

Actions replay from a fresh browser every time, so a run is reproducible and the order you pass them
in is the order they happen. Cloudflare Access is handled internally with a host-scoped cookie; you
do not need a credential and there is nothing here for you to configure.
"""
import tempfile, uuid, argparse, glob, json, os, subprocess, sys, urllib.request, http.cookiejar

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)


def access_cookie(url):
    """A CF_Authorization cookie, scoped to this host only (never a header that rides everywhere)."""
    try:
        tok = json.load(open(os.path.join(ROOT, ".private", "cf-access-service-token.json")))
    except OSError:
        return None
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = urllib.request.Request(url, headers={
        "CF-Access-Client-Id": tok["CF_ACCESS_CLIENT_ID"],
        "CF-Access-Client-Secret": tok["CF_ACCESS_CLIENT_SECRET"],
        "User-Agent": "Mozilla/5.0"})
    try:
        op.open(req, timeout=30)
    except Exception:
        return None
    for c in cj:
        if c.name == "CF_Authorization":
            return {"name": c.name, "value": c.value, "domain": c.domain, "path": "/"}
    return None


NODE = r"""
const { chromium } = require('playwright');
const cfg = JSON.parse(process.argv[2]);
(async () => {
  const b = await chromium.launch();
  // ⭐ deviceScaleFactor 3 — HER DEVICE'S RESOLUTION, not a third of it. Every pixel review to date
  // read a 1x raster (36KB where 172KB was available), so hairline rules, sub-pixel misalignment and
  // small-type legibility were all being judged from an image that had thrown them away. isMobile +
  // hasTouch also make the page behave as a phone rather than a narrow desktop.
  // ⛔ AND THE FLOOR THAT WASN'T: real Chrome cannot be RESIZED below ~606px by hand, but a
  // CDP-driven Chrome has no such floor. The instrument was never choosing between her width and a
  // real browser — measured 2026-09-05, real Chrome 152 and bundled Chromium render this page
  // identically (same font stack, same h1 width, same height).
  const ctx = await b.newContext({
    viewport: { width: 414, height: 848 },
    deviceScaleFactor: 3, isMobile: true, hasTouch: true,
  });
  ctx.setDefaultTimeout(8000);
  if (cfg.cookie) await ctx.addCookies([Object.assign({}, cfg.cookie, { secure: true, httpOnly: true })]);
  const page = await ctx.newPage();
  // A screenshot's entire meaning is its geometry. Recording it here means a later reader can tell
  // what the image is EVIDENCE OF, instead of assuming the standard it was supposed to meet.
  const out = { steps: [], console: [],
                geometry: { width: 414, height: 848, deviceScaleFactor: 3, isMobile: true } };
  // A walk that cannot say WHY a write failed cannot attribute it later. Errors only —
  // a full console dump buries the one line that matters.
  page.on('console', (m) => { if (m.type() === 'error') out.console.push(m.text().slice(0, 300)); });
  page.on('pageerror', (e) => out.console.push('PAGEERROR: ' + String(e).slice(0, 300)));
  try {
    await page.goto(cfg.url, { waitUntil: 'load', timeout: 45000 });
    await page.waitForTimeout(1200);
    for (const act of cfg.actions) {
      try {
        // ⭐ `goto:` CROSSES THE HANDOFF. Every stop until now ended at the last onboarding screen, so
        // the seam between onboarding and the estate view — the thing the whole journey builds toward
        // — was walked by nobody, and whatever a brand-new person sees on the other side was untested.
        // Same browser context, so localStorage survives the navigation exactly as it does for her.
        if (act.startsWith('goto:')) { await page.goto(act.slice(5), { waitUntil: 'load', timeout: 45000 }); await page.waitForTimeout(1200); }
        else if (act.startsWith('click:')) { await page.click(act.slice(6)); }
        else if (act.startsWith('type:')) {
          const rest = act.slice(5); const i = rest.indexOf('=');
          await page.fill(rest.slice(0, i), rest.slice(i + 1));
        }
        await page.waitForTimeout(700);
        out.steps.push({ action: act, ok: true });
      } catch (e) { out.steps.push({ action: act, ok: false, error: String(e.message).split('\n')[0] }); }
    }
    out.screen = await page.evaluate(() => {
      const vis = (el) => { if (!el) return false; const r = el.getBoundingClientRect();
        const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.display !== 'none' && cs.visibility !== 'hidden'; };
      const text = [];
      // ⛔ `.trouble` and [role=alert] ARE IN THIS LIST DELIBERATELY. The set was tag-only until
      // 2026-09-05, and an error message written into a bare <div> was therefore invisible to
      // every walk — the harness reported a screen with no error while the screen plainly showed
      // one. A journey walk exists to catch exactly that copy, so the instrument was blind in the
      // one place it most needed to see.
      document.querySelectorAll('h1,h2,h3,p,label,li,strong,em,span,.trouble,[role="alert"]').forEach((n) => {
        if (!vis(n)) return;
        if (n.querySelector('h1,h2,h3,p,label,li')) return;      // keep leaves only
        const t = (n.innerText || '').replace(/\s+/g, ' ').trim();
        if (t && !text.includes(t)) text.push(t);
      });
      const fields = [...document.querySelectorAll('input,textarea,select')].filter(vis).map((f) => ({
        id: f.id, label: (document.querySelector('label[for="' + f.id + '"]') || {}).innerText || null,
        placeholder: f.placeholder || null, value: f.value || null }));
      const buttons = [...document.querySelectorAll('button,a')].filter(vis).map((b) => ({
        id: b.id || null, text: (b.innerText || '').trim(), href: b.getAttribute('href') || null }));
      return { title: document.title, url: location.href, text, fields, buttons };
    });
    // ⛔ TWO FRAMES, AND THE SECOND IS THE ONE THAT CAN JUDGE THE FOLD. A full-page capture is
    // STITCHED, which (a) hides where the viewport actually ends, so a reviewer cannot say what is
    // above the fold, and (b) manufactures a phantom: `background-attachment: fixed` seams into a
    // horizontal band that the vision seat correctly identified as an artifact only after nearly
    // filing it as a layout break. The viewport frame has neither problem and costs one screenshot.
    // ⭐ ux-expert, 2026-09-05: this — not a real-Chrome swap — is what the fold findings needed.
    // Chrome cannot go below ~606px, and at that width TWO of tonight's real bugs disappear
    // entirely, because their mechanism is text wrapping at 414px.
    await page.screenshot({ path: cfg.shot, fullPage: true });
    await page.screenshot({ path: cfg.shot.replace(/\.png$/, '.fold.png'), fullPage: false });
  } catch (e) { out.error = String(e.message).split('\n')[0]; }
  await b.close();
  console.log(JSON.stringify(out, null, 2));
})();
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--do", action="append", default=[], help='"click:#id" or "type:#id=text"')
    # ⛔ A PER-PROCESS DEFAULT, NOT A SHARED ONE. It was "/tmp/journey-view.png" for every caller, so
    # parallel walkers overwrote each other's screenshots — and on 2026-09-05 a primed walker read a
    # DIFFERENT walker's rendered screen and correctly reported itself contaminated. Priming leaks and
    # cannot be un-leaked; a shared write path in the harness is how it leaks silently. A fixture must
    # assert its own destination.
    ap.add_argument("--shot", default=os.path.join(
        tempfile.gettempdir(), "journey-view-%d-%s.png" % (os.getpid(), uuid.uuid4().hex[:6])))
    a = ap.parse_args()

    mods = glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/playwright"))
    if not mods:
        raise SystemExit("journey-view: no browser available")
    env = dict(os.environ); env["NODE_PATH"] = os.path.dirname(mods[0])
    js = "/tmp/.journey-view.js"
    open(js, "w").write(NODE)
    cfg = {"url": a.url, "actions": a.do, "shot": a.shot, "cookie": access_cookie(a.url)}
    p = subprocess.run(["node", js, json.dumps(cfg)], capture_output=True, text=True, env=env, timeout=300)
    if p.returncode != 0 or not p.stdout.strip():
        raise SystemExit("journey-view: could not open that link\n" + (p.stderr or "")[-800:])
    r = json.loads(p.stdout)

    if r.get("error"):
        print("Could not open the link: %s" % r["error"]); return 2
    for s in r["steps"]:
        if not s["ok"]:
            print("  ⚠️  could not do %r — %s" % (s["action"], s.get("error")))
    sc = r["screen"]
    print("PAGE TITLE: %s" % sc["title"])
    if r.get("console"):
        print("CONSOLE ERRORS (the page's own diagnostics — why a write failed, not just that it did):")
        for c in r["console"][:8]:
            print("   " + c)
    print("ON SCREEN:")
    for t in sc["text"]:
        print("   %s" % t)
    if sc["fields"]:
        print("FIELDS YOU CAN FILL IN:")
        for f in sc["fields"]:
            print("   %s — label=%r placeholder=%r current=%r" % (f["id"], f["label"], f["placeholder"], f["value"]))
    if sc["buttons"]:
        print("BUTTONS / LINKS:")
        for b in sc["buttons"]:
            print("   %s%s%s" % (b["text"] or "(no text)",
                                 " [#%s]" % b["id"] if b["id"] else "",
                                 " → %s" % b["href"] if b["href"] else ""))
    print("SCREENSHOT: %s" % a.shot)
    return 0


if __name__ == "__main__":
    sys.exit(main())
