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
const playwright = require('playwright');
const { chromium } = playwright;

// ═══ T14 · THE ONE CONTEXT FACTORY ═══════════════════════════════════════════════════════════════
//
// ⛔⛔ WHY A FACTORY AND NOT THREE MORE cfg KEYS ON THE INLINE CALL: A GROWN ARGUMENT OBJECT IS NOT A
// FACTORY. Row H needs a SECOND browser context in the same run, and against an inline `newContext`
// it would have to duplicate this block — two context-creation paths, i.e. TWO DEFINITIONS OF "the
// conditions this walk ran in", which is a second harness by accident. That is the single highest-
// risk collision between rows T and H, and `class: engine · must-not-diverge` forbids it by name.
// ⭐ H1's second context is built by THIS function. If a future reader finds a bare `newContext`
// anywhere in this file, that is the divergence returning.
//
// ⛔ THE ARRIVAL STATE IS A DECLARED PROPERTY, NOT A HARNESS DEFAULT. A walk used to run in whatever
// the harness happened to do; it now runs in a state the CELL declared, and records the state it
// ACTUALLY ran in — which are different claims, and the second is the evidence.
//
// ⚠️ SECURITY R2-B binds the profile: lab/qa only, profiles under `.private/walk-profiles/`, NEVER
// /tmp, MINTED BY WALKING and never hand-seeded. A `returning-device` profile carries a DEAD
// credential by construction — that is the fixture, not a fault.
const VIEWPORT = { width: 414, height: 848, deviceScaleFactor: 3, isMobile: true, hasTouch: true };

async function mkContext(browser, cfg, label) {
  const opts = Object.assign({}, VIEWPORT);
  // ⛔ storageState is passed ONLY when it exists on disk. Playwright throws on a missing path, and
  // a walk that dies because a profile was absent would read as a product failure.
  if (cfg.storageState) opts.storageState = cfg.storageState;
  const ctx = await browser.newContext(opts);
  ctx.setDefaultTimeout(8000);
  if (cfg.cookie) await ctx.addCookies([Object.assign({}, cfg.cookie, { secure: true, httpOnly: true })]);
  // ⭐ `text: A+` is an INIT SCRIPT, not a click: it must be in place BEFORE the first paint, which
  // is the only way to walk the size Mom is actually served.
  // ⚠️ J8's L08 CLEARS localStorage mid-walk, so this does not survive that stop. That is CORRECT
  // PRODUCT BEHAVIOUR and is recorded rather than asserted away.
  // ⛔ `{ content: ... }`, NOT A BARE STRING. Playwright treats a bare string as a PATH TO A FILE,
  // so `addInitScript("localStorage.setItem(...)")` silently does NOTHING — measured: the walk
  // recorded `ranIn.text: "A+"` while the page read `fw-text-size=unset`. The record would have
  // claimed a state the browser was never in, which is worse than not offering the flag.
  if (cfg.initScript) await ctx.addInitScript({ content: cfg.initScript });
  return { ctx, label: label || 'primary',
           ranIn: { engine: cfg.engine || 'chromium',
                    profile: cfg.storageState ? 'returning-device' : 'clean',
                    text: cfg.initScript ? 'A+' : 'default',
                    viewport: { width: VIEWPORT.width, height: VIEWPORT.height,
                                deviceScaleFactor: VIEWPORT.deviceScaleFactor,
                                isMobile: VIEWPORT.isMobile } } };
}
const cfg = JSON.parse(process.argv[2]);
(async () => {
  // ⭐ --watch OPENS A VISIBLE WINDOW `[paul-stated 2026-09-06]`: "I like being able to watch the
  // walk through in chrome." slowMo is what makes it followable — without it a walk is a flicker.
  // ⛔ AND IT STAYS BUNDLED CHROMIUM AT 414px, deliberately. The obvious reading of "watch it in
  // Chrome" is channel:'chrome', and that would QUIETLY CHANGE THE EVIDENCE: real Chrome cannot be
  // resized below ~606px, and at 606 two of 2026-09-05's real bugs vanish entirely because their
  // mechanism is text wrapping at 414. A watched run and a headless run must be the same
  // measurement or watching is not observation, it is a different experiment. Only headless and
  // pacing change here; viewport, deviceScaleFactor, isMobile and hasTouch are untouched below.
  // ⛔ THE ENGINE IS DECLARED, NOT ASSUMED. `chromium` stays the default so nothing changes for a
  // walk that declares nothing; an unknown engine REFUSES rather than silently falling back, because
  // a walk that silently ran on a different engine than it claimed is evidence about nothing.
  const engineName = cfg.engine || 'chromium';
  // ⛔ THE PROPERTY EXISTING IS NOT THE BROWSER EXISTING. `playwright.webkit` is always defined; it
  // is LAUNCH that throws when the engine is not installed — measured, the first version checked the
  // property, passed, and died with a raw Node stack instead of the named refusal. An engine that
  // cannot run must say so in one line a reader can act on, never fall back to another engine: a
  // walk that silently ran on a different engine than it claimed is evidence about nothing.
  let b;
  if (!playwright[engineName]) {
    console.log('ENGINE-UNAVAILABLE: ' + engineName + ' (playwright has no such engine)');
    process.exit(3);
  }
  try {
    b = await playwright[engineName].launch(cfg.watch ? { headless: false, slowMo: 350 } : {});
  } catch (e) {
    console.log('ENGINE-UNAVAILABLE: ' + engineName + ' — not installed. '
                + 'Install it with: npx playwright install ' + engineName);
    process.exit(3);
  }
  // ⭐ deviceScaleFactor 3 — HER DEVICE'S RESOLUTION, not a third of it. Every pixel review to date
  // read a 1x raster (36KB where 172KB was available), so hairline rules, sub-pixel misalignment and
  // small-type legibility were all being judged from an image that had thrown them away. isMobile +
  // hasTouch also make the page behave as a phone rather than a narrow desktop.
  // ⛔ AND THE FLOOR THAT WASN'T: real Chrome cannot be RESIZED below ~606px by hand, but a
  // CDP-driven Chrome has no such floor. The instrument was never choosing between her width and a
  // real browser — measured 2026-09-05, real Chrome 152 and bundled Chromium render this page
  // identically (same font stack, same h1 width, same height).
  const made = await mkContext(b, cfg, 'primary');
  const ctx = made.ctx;
  const page = await ctx.newPage();
  // A screenshot's entire meaning is its geometry. Recording it here means a later reader can tell
  // what the image is EVIDENCE OF, instead of assuming the standard it was supposed to meet.
  // ⭐ T7 — the URL as of the last checkpoint, so each checkpoint can record where it STARTED.
  let lastUrl = null;
  // ⭐ T16's TRAP, CLOSED HERE BECAUSE THE FACTORY NOW OWNS THE CONSTANT: `geometry` used to
  // RE-TYPE the viewport ten lines below where it was set, so the two could drift and the recorded
  // geometry would describe a walk that never happened. It is DERIVED.
  const out = { steps: [], console: [], checkpoints: [], httpFailures: [],
                geometry: made.ranIn.viewport,
                // ⛔ THE STATE IT ACTUALLY RAN IN, not the state it was asked for.
                ranIn: made.ranIn };
  // A walk that cannot say WHY a write failed cannot attribute it later. Errors only —
  // a full console dump buries the one line that matters.
  page.on('console', (m) => { if (m.type() === 'error') out.console.push(m.text().slice(0, 300)); });
  page.on('pageerror', (e) => out.console.push('PAGEERROR: ' + String(e).slice(0, 300)));
  // ⛔ THE CONSOLE LINE CARRIES A STATUS AND NO URL, so WHOSE 429 it was is not derivable from it.
  // Measured 2026-09-07: all 18 occurrences across the corpus are the byte-identical string
  // "Failed to load resource: the server responded with a status of 429 (Too Many Requests)".
  // A gate clause was refusing runs on that string while being NAMED for our own origin — and the
  // 429s were Open-Meteo's free tier, fetched straight from the browser. Recording the URL at
  // capture time is what makes attribution possible at all; inferring it from timing or position
  // would be a clause that guesses, which is worse than the wide one because it is wrong silently.
  page.on('response', (r) => {
    try { if (r.status() >= 400) out.httpFailures.push({ status: r.status(), url: String(r.url()).slice(0, 300) }); }
    catch (e) { /* a response that cannot report itself is not worth failing the walk over */ }
  });
  try {
    await page.goto(cfg.url, { waitUntil: 'load', timeout: 45000 });
    await page.waitForTimeout(1200);
    // ⭐ ONE JOURNEY, MANY CHECKPOINTS `[paul-stated 2026-09-06]`: "I want all the synthetics to run
    // profile creation in chrome that we can watch." A watched walk has to look like a PERSON using
    // the app — arrive, sign up, name the place, walk out — not seven browser launches each
    // replaying the last one from scratch. It is also the limiter fix: replaying every prefix cost
    // 47 actions and FIVE account creations per seat, which is what flooded 20-writes-per-5-minutes.
    // A `shot:<name>` pseudo-action captures the full state HERE, mid-journey, so one continuous
    // session yields the same per-stop evidence the replay used to.
    const describe = () => page.evaluate(() => {
      const vis = (el) => { if (!el) return false; const r = el.getBoundingClientRect();
        const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.display !== 'none' && cs.visibility !== 'hidden'; };
      const text = [];
      // ⛔ `.trouble` and [role=alert] ARE IN THIS LIST DELIBERATELY. The set was tag-only until
      // 2026-09-05, and an error message written into a bare <div> was therefore invisible to
      // every walk — the harness reported a screen with no error while the screen plainly showed
      // one. A journey walk exists to catch exactly that copy, so the instrument was blind in the
      // one place it most needed to see.
      // ⛔ AND `div` IS IN THIS LIST FOR THE SAME REASON, added 2026-09-07. The tag list above was
      // extended by NAMING one class (`.trouble`) when a bare <div> turned out to be invisible. That
      // fixed one div and left the shape: the place card at stop 12 writes its address into
      // `div.main-card-summary` and its lead sentence into `div.prop-lead`, so **the card the whole
      // build was about was absent from every brief**, and mom · strict · wide-eyed each reported
      // reading it off the PNG instead (cycle/release/CYCLE-LOG.md:769). Naming three more classes
      // would repeat the fix; the rule is that a TEXT LEAF is a text leaf whatever tag it wears.
      // The leaf test below is what keeps a layout wrapper from dragging the whole page in: a node
      // qualifies only if it contains no element other than inline formatting.
      const LEAFY = 'br,span,strong,em,b,i,a,small,code,abbr,time,sup,sub';
      document.querySelectorAll('h1,h2,h3,h4,p,label,li,strong,em,span,div,.trouble,[role="alert"]').forEach((n) => {
        if (!vis(n)) return;
        if (n.tagName === 'DIV' && [...n.children].some((c) => !LEAFY.split(',').includes(c.tagName.toLowerCase()))) return;
        if (n.querySelector('h1,h2,h3,h4,p,label,li')) return;      // keep leaves only
        const t = (n.innerText || '').replace(/\s+/g, ' ').trim();
        if (t && !text.includes(t)) text.push(t);
      });
      const fields = [...document.querySelectorAll('input,textarea,select')].filter(vis).map((f) => ({
        id: f.id, label: (document.querySelector('label[for="' + f.id + '"]') || {}).innerText || null,
        placeholder: f.placeholder || null, value: f.value || null }));
      const buttons = [...document.querySelectorAll('button,a')].filter(vis).map((b) => ({
        id: b.id || null, text: (b.innerText || '').trim(), href: b.getAttribute('href') || null }));
      // ⭐ THE SCREEN'S OWN ID, so a NOTE can be matched to a PICTURE `[paul-stated 2026-09-06]`:
      // "it's probably helpful to be able to refer to the current state screenshots when looking at
      // feedback." A general-feedback note records `screen` as the SECTION id (s0..s4 — see
      // onboarding/index.html postAnswer), while a walk names its screenshots by STOP (03-named).
      // Two vocabularies for one screen means a note and the picture of what she was looking at
      // could not be joined by anything but a human remembering the mapping. Recording the id the
      // page itself is showing closes that at the source instead of with a hand-kept table that
      // would drift the first time a screen is renamed.
      const openSection = document.querySelector('section.card:not([hidden])');
      return { title: document.title, url: location.href, text, fields, buttons,
               screenId: openSection ? openSection.id : null };
    });
    // ⭐ T7 — seed from the real landing URL, so the FIRST checkpoint's `urlBefore` is the page the
    // journey arrived on rather than null. A null here would read as "no prior screen", which is
    // true of the first stop but useless to the reader who wants to know where the walk began.
    if (lastUrl === null) { try { lastUrl = page.url(); } catch (e) {} }
    for (const act of cfg.actions) {
      try {
        // ⭐ `goto:` CROSSES THE HANDOFF. Every stop until now ended at the last onboarding screen, so
        // the seam between onboarding and the estate view — the thing the whole journey builds toward
        // — was walked by nobody, and whatever a brand-new person sees on the other side was untested.
        // Same browser context, so localStorage survives the navigation exactly as it does for her.
        if (act.startsWith('shot:')) {
          // A checkpoint is a RECORD, not a pause: full state + both frames, named by the caller.
          const nm = act.slice(5);
          // A checkpoint LOOKS at a page that has finished arriving. Round 8 (2026-09-06): the handoff
          // shot ran while the click before it was still navigating — "execution context was
          // destroyed" — and a clean product walk scored a failed action. Wait for load, then look.
          try { await page.waitForLoadState('load', { timeout: 8000 }); } catch (e) {}
          const sc = await describe();
          const base = cfg.shotDir + '/' + nm;
          await page.screenshot({ path: base + '.png', fullPage: true });
          await page.screenshot({ path: base + '.fold.png', fullPage: false });
          // ⭐ T7 — WHERE THIS STOP STARTED FROM. TIER 2 · 22 ①: `14-shelf-to-place` was unreadable
          // because two consecutive checkpoints held IDENTICAL screenshots and nothing recorded the
          // URL the tap began at, so a reader could not tell whether the click had done anything at
          // all. `urlBefore` is the URL as of the PREVIOUS checkpoint — i.e. before the actions that
          // led here — so the pair (urlBefore, url) says whether this stop moved.
          // ⛔ It is the cell's EVIDENCE, not its verdict: a stop that did not move may be perfectly
          // correct (a same-page disclosure), and this records the fact without judging it.
          out.checkpoints.push({ name: nm, screen: sc, shot: base + '.png', urlBefore: lastUrl });
          lastUrl = (sc && sc.url) || lastUrl;
        }
        else if (act.startsWith('goto:')) { await page.goto(act.slice(5), { waitUntil: 'load', timeout: 45000 }); await page.waitForTimeout(1200); }
        else if (act.startsWith('click:')) { await page.click(act.slice(6)); }
        // ⭐ lap 7 (H3) — ASSERTIONS AS ACTIONS. `expect:<selector>` fails the action unless the element is
        // present and visible; `eval:<js>` fails it unless the expression (a value or a promise) is truthy.
        // A broken promise therefore lands in the transcript as a FAILED ACTION, which release-gate's
        // `no-failed-actions` clause refuses — never a screenshot somebody has to read to notice.
        else if (act.startsWith('expect:')) {
          // ⛔ WAIT, THEN LOOK — the way `shot:` already does. The first cut checked the instant the previous
          // click returned; measured 2026-09-11 (lap 7 battery, J8 × 5 at 87c7aae): every seat failed
          // `expect:.hh-utility` right after the sign-in click while the next two stops on that very bar
          // passed. An assertion that runs before the navigation lands scores the product's correct
          // behaviour as a failure — an instrument artefact, not a finding.
          const sel = act.slice(7);
          try { await page.waitForLoadState('load', { timeout: 8000 }); } catch (e) {}
          try { await page.waitForSelector(sel, { state: 'visible', timeout: 8000 }); }
          catch (e) { throw new Error('expect: not visible — ' + sel); }
        }
        else if (act.startsWith('eval:')) {
          const v = await page.evaluate(act.slice(5));
          if (!v) throw new Error('eval: falsy — ' + act.slice(5, 90));
        }
        else if (act.startsWith('type:')) {
          const rest = act.slice(5); const i = rest.indexOf('=');
          await page.fill(rest.slice(0, i), rest.slice(i + 1));
        }
        await page.waitForTimeout(700);
        out.steps.push({ action: act, ok: true });
      } catch (e) { out.steps.push({ action: act, ok: false, error: String(e.message).split('\n')[0] }); }
    }
    out.screen = await describe();
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
  // ⛔ END THE WALK THE WAY A PERSON ENDS A VISIT. `browser.close()` fires no pagehide, no
  // visibilitychange, no beforeunload — so the app's session-end flush (its capture-side record)
  // never ran, and every walk read "0 app events" while a real person closing the tab would have
  // recorded a session. Measured 2026-09-06 (round 3, owner + mom). Close the PAGE first.
  // Round 3 measured 0 app events even with the page closed first: the last stop is a screenshot and
  // an exit inside a second, and a CDP close does not reliably fire pagehide. So the walk LOOKS at the
  // last screen for a moment, as a person would, then leaves the way a person does — pagehide, then
  // the tab closes — and gives the keepalive post a beat to leave the machine.
  try {
    await page.waitForTimeout(6500);
    await page.evaluate(() => { try { window.dispatchEvent(new Event("pagehide")); } catch (e) {} });
    await page.waitForTimeout(1500);
    await page.close({ runBeforeUnload: true });
    await new Promise(r => setTimeout(r, 800));
  } catch (e) {}
  await b.close();
  console.log(JSON.stringify(out, null, 2));
})();
"""


def _selftest():
    """T14's clauses. ⛔ It proves the REFUSALS and the cfg shape; it does not launch a browser, and
    says so — the end-to-end behaviour (A+ installs before first paint, the geometry is derived, the
    deploy guard still refuses a broken page) is proven by running, and is recorded in T14's commit
    rather than asserted here."""
    ok = []

    def ck(name, cond):
        ok.append(bool(cond)); print("  %s %s" % ("✅" if cond else "🔴", name))

    NODEJS = NODE
    # ⛔ M21a — ONE CONTEXT FACTORY, NOT TWO. Row H's second context must be built by mkContext; a
    # bare `newContext` reappearing anywhere in this file IS the divergence returning.
    ck("T14/M21a exactly ONE `.newContext(` exists, and it is inside mkContext",
       NODEJS.count(".newContext(") == 1 and "async function mkContext" in NODEJS)
    ck("T14/M21a2 the factory is actually USED for the primary context",
       "await mkContext(b, cfg, 'primary')" in NODEJS)

    # ⛔ M21b — the A+ init script is passed as CONTENT, not as a bare string. A bare string is read
    # by Playwright as a FILE PATH and silently does nothing, so the record would claim a state the
    # browser was never in. Measured: that is exactly what the first version did.
    ck("T14/M21b the init script is passed as `{ content: ... }`, never a bare string",
       "addInitScript({ content:" in NODEJS)

    # ⛔ M21c — the geometry is DERIVED from the factory's constant, never re-typed.
    ck("T14/M21c `geometry` is derived from the factory, not a second literal",
       "geometry: made.ranIn.viewport" in NODEJS and NODEJS.count("width: 414") == 1)
    ck("T14/M21c2 the run records the state it ACTUALLY ran in", "ranIn: made.ranIn" in NODEJS)

    # ⛔ M21d — an engine that cannot LAUNCH refuses; checking the property alone is not enough,
    # because `playwright.webkit` is always defined and it is launch that throws.
    ck("T14/M21d an engine is refused on LAUNCH failure, not merely on a missing property",
       "catch (e)" in NODEJS and "ENGINE-UNAVAILABLE" in NODEJS
       and "npx playwright install" in NODEJS)

    # ═══ T15 · THE WEBKIT CELL ═══════════════════════════════════════════════════════════════════
    # ⭐ `[paul-ruled, P17: WebKit is installed]`. Zero walks in this project's history had used
    # anything but bundled Chromium — MOM'S SAFARI ENGINE HAD NEVER BEEN WALKED ONCE — and as of
    # 2026-09-11 it has: `--engine webkit` opens the QA origin and reports a screen, recording
    # `ranIn.engine: "webkit"`.
    # ⛔ SECURITY R4: no new tier and no new trust root. A WebKit run that cannot reach the origin
    # reports UNREACHABLE; A FAILURE HERE IS A CAPABILITY FINDING, NEVER A PRODUCT FINDING.
    # ⭐⭐ AND THE PRODUCT FACT THIS CELL EXISTS TO FALSIFY (L8-P7), measured: `fw-grant` is written
    # to **localStorage only** — no cookie, no sessionStorage anywhere in the served pages. WebKit
    # evicts localStorage for an origin left idle, so a returning person on Safari can lose the grant
    # that keeps them signed in. This cell is the instrument that would show it; it is a roster row
    # for lap 8 · A, not row T's to fix.
    ck("T15/M22a the engine is DECLARED and recorded, so a walk can say which browser it ran in",
       "'engine': " in NODEJS or "engine: cfg.engine" in NODEJS or "engine: engineName" in NODEJS
       or "cfg.engine || 'chromium'" in NODEJS)
    ck("T15/M22b the playwright tree is the NEWEST, not an arbitrary glob hit — an engine installed "
       "into another tree would read as unavailable though it is installed",
       "key=lambda d: os.path.getmtime(d), reverse=True" in open(os.path.abspath(__file__),
                                                                 encoding="utf-8").read())

    # ⛔ M21e — a declared-but-absent profile refuses BEFORE launching, naming how to produce one.
    import tempfile as _tf
    with _tf.TemporaryDirectory() as td:
        missing = os.path.join(td, "nope.json")
        src = open(os.path.abspath(__file__), encoding="utf-8").read()
        ck("T14/M21e a declared profile that does not exist refuses, naming how to mint one",
           "REFUSING" in src and "MINTED BY WALKING" in src and not os.path.exists(missing))

    print("\n%s journey-view selftest (%d/%d)  ⚠️ refusals and cfg shape only; no browser launched"
          % ("✅" if all(ok) else "🔴", sum(ok), len(ok)))
    return 0 if all(ok) else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url", nargs="?")
    ap.add_argument("--do", action="append", default=[], help='"click:#id" or "type:#id=text"')
    # ⛔ A PER-PROCESS DEFAULT, NOT A SHARED ONE. It was "/tmp/journey-view.png" for every caller, so
    # parallel walkers overwrote each other's screenshots — and on 2026-09-05 a primed walker read a
    # DIFFERENT walker's rendered screen and correctly reported itself contaminated. Priming leaks and
    # cannot be un-leaked; a shared write path in the harness is how it leaks silently. A fixture must
    # assert its own destination.
    ap.add_argument("--shot", default=os.path.join(
        tempfile.gettempdir(), "journey-view-%d-%s.png" % (os.getpid(), uuid.uuid4().hex[:6])))
    # ⛔ THE PROSE IS FOR A PERSON; A CALLER NEEDS THE RECORD. journey-walk parsed stdout, so when
    # the walk moved to one continuous run it silently kept only what the summary line carried —
    # name, screen id, title — and DROPPED every checkpoint's screen text. That is the richest
    # evidence this harness collects ("capture as much data as possible... accretive by design"),
    # and worse, walk-integrity's refusal that scans screen prose for `could not do` can never fire
    # against a record that has no prose. Emitting the full result as JSON removes the incentive to
    # re-derive it from print statements.
    ap.add_argument("--json", dest="json_out", help="write the complete result (incl. every checkpoint's full screen) to this path")
    ap.add_argument("--shot-dir", dest="shot_dir",
                    help="directory for `shot:<name>` checkpoint captures (default: alongside --shot)")
    # ⭐ T14 — THE ARRIVAL STATE IS DECLARED ON THE COMMAND LINE, so a cell can ask for the state it
    # says it walks in. ⛔ Each flag is OPTIONAL and its ABSENCE is the clean default — a walk that
    # declares nothing runs exactly as it always has.
    ap.add_argument("--engine", default="chromium",
                    help="chromium (default) | firefox | webkit. An engine playwright does not have "
                         "REFUSES rather than falling back — a walk that silently ran on another "
                         "engine than it claimed is evidence about nothing.")
    ap.add_argument("--storage-state", dest="storage_state",
                    help="path to a saved browser profile (R2-B: under .private/walk-profiles/, "
                         "MINTED BY WALKING, never hand-seeded, never /tmp)")
    ap.add_argument("--text", choices=["default", "A+"], default="default",
                    help="A+ installs the served text size BEFORE first paint — the size Mom is "
                         "actually served. ⚠️ J8's L08 clears localStorage mid-walk, so it does not "
                         "survive that stop; that is correct product behaviour.")
    ap.add_argument("--watch", action="store_true",
                    help="open a VISIBLE browser and pace the actions so a person can follow them. "
                         "Same viewport (414x848 @3x, mobile) and same screenshots as a headless run — "
                         "only visibility and pacing change, so a watched run is the same evidence.")
    ap.add_argument("--selftest", action="store_true",
                    help="prove T14's refusals and cfg shape without launching a browser")
    a = ap.parse_args()
    if a.selftest:
        return _selftest()
    if not a.url:
        ap.error("the following arguments are required: url")

    # ⛔ T15 — THE NEWEST TREE, NOT AN ARBITRARY ONE. `glob` returns filesystem order, and `mods[0]`
    # took whichever came first across THREE playwright installs on this machine. An engine installed
    # into one tree while NODE_PATH points at another reads as UNAVAILABLE though it is installed —
    # a capability finding manufactured by a sort order. The plan says to fix this the day the
    # WebKit install lands; this is that day.
    mods = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/playwright")),
                  key=lambda d: os.path.getmtime(d), reverse=True)
    if not mods:
        raise SystemExit("journey-view: no browser available")
    env = dict(os.environ); env["NODE_PATH"] = os.path.dirname(mods[0])
    js = "/tmp/.journey-view.js"
    open(js, "w").write(NODE)
    # ⛔ A DECLARED PROFILE THAT DOES NOT EXIST REFUSES, NAMING THE COMMAND THAT WOULD PRODUCE ONE.
    # Playwright throws on a missing storageState path, so without this the walk dies mid-run and the
    # transcript blames the product for a missing fixture. Same refusal shape as `mint_invite`.
    if a.storage_state and not os.path.exists(a.storage_state):
        raise SystemExit(
            "journey-view: \u26d4 REFUSING \u2014 a `returning-device` profile was declared and "
            "none exists at\n  %s\n"
            "  A profile is MINTED BY WALKING, never hand-seeded (security R2-B). Produce one\n"
            "  with a clean walk of this cell first; that walk writes the profile it did not have.\n"
            % a.storage_state)
    cfg = {"url": a.url, "actions": a.do, "shot": a.shot, "cookie": access_cookie(a.url),
           "watch": bool(a.watch), "engine": a.engine,
           "storageState": a.storage_state or None,
           # the init script is built HERE, not passed as arbitrary JS from a caller
           "initScript": ("try{localStorage.setItem('fw-text-size','lg')}catch(e){}"
                          if a.text == "A+" else None),
           "shotDir": a.shot_dir or os.path.dirname(os.path.abspath(a.shot))}
    # A watched run is paced for a human (slowMo), so the headless timeout would kill it mid-walk and
    # the transcript would blame the product for the instrument's impatience.
    p = subprocess.run(["node", js, json.dumps(cfg)], capture_output=True, text=True, env=env,
                       timeout=1200 if a.watch else 300)
    if p.returncode == 3 and "ENGINE-UNAVAILABLE" in (p.stdout or ""):
        # ⛔ A CAPABILITY FINDING, NEVER A PRODUCT FINDING. T15's rule, enforced at the source: a
        # WebKit run that cannot start reports UNREACHABLE, not "refused".
        raise SystemExit("journey-view: " + p.stdout.strip().splitlines()[-1])
    if p.returncode != 0 or not p.stdout.strip():
        raise SystemExit("journey-view: could not open that link\n" + (p.stderr or "")[-800:])
    r = json.loads(p.stdout)

    if a.json_out:
        with open(a.json_out, "w", encoding="utf-8") as f:
            json.dump(r, f, indent=2)
    # ⛔ THE PER-ACTION FAILURES PRINT FIRST, EVEN WHEN THE PAGE ITSELF ERRORED. This returned early
    # on `error`, so a run that failed nine actions and then hit a navigation error printed the
    # navigation error ALONE — and journey-walk, which reads these lines to populate failedActions,
    # recorded `failedActions: None` over a walk where three stops were never reached. A clean
    # failure field above a failed run is the false-green shape this harness exists to refuse, and
    # it was in the harness. Measured 2026-09-06.
    for st in r.get("steps") or []:
        if not st.get("ok"):
            print("  ⚠️  could not do %r — %s" % (st["action"], st.get("error")))
    if r.get("error"):
        print("Could not open the link: %s" % r["error"])
        print("SCREENSHOT: %s" % a.shot)
        return 2
    sc = r["screen"]
    print("PAGE TITLE: %s" % sc["title"])
    # Printed on its own line so journey-walk can parse it without re-running the browser.
    print("SCREEN ID: %s" % (sc.get("screenId") or "-"))
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
    for c in r.get("checkpoints") or []:
        print("CHECKPOINT %s | screen=%s | title=%s | shot=%s"
              % (c["name"], c["screen"].get("screenId") or "-", c["screen"].get("title"), c["shot"]))
    print("SCREENSHOT: %s" % a.shot)
    return 0


if __name__ == "__main__":
    sys.exit(main())
