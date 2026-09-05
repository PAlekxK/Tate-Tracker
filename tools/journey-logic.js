// journey-logic.js — the bare-logic path table for the onboarding journey, forced state by state.
// Driven by tools/journey-logic.py; never run directly. Config arrives as JSON on argv[2].
//
// The document under test is ALWAYS served by interception, so a run is byte-exact and leaves no
// residue. The Worker's responses are controlled per path. The identity marker is DERIVED by the
// Python side from the working tree and passed in — no marker is typed here.
const { chromium } = require('playwright');
const cfg = JSON.parse(process.argv[2]);

const ORIGIN = cfg.origin;                 // e.g. https://fernwood-qa.pages.dev
const DOC_URL = ORIGIN + cfg.docPath;      // e.g. /onboarding/

// ── helpers ────────────────────────────────────────────────────────────────
const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, X-Grant, X-Tate-Token',
  'Access-Control-Max-Age': '600',
};
const results = [];
function record(id, name, ok, detail, extra) {
  results.push(Object.assign({ id, name, ok: !!ok, detail: detail || '' }, extra || {}));
}

// Build a context whose document request is fulfilled with `body`, and whose Worker calls are
// answered by `api` (a map of substring -> {status, json} | 'abort' | 'live').
async function openPage(browser, { body, api, storage, url, host }) {
  const ctx = await browser.newContext({ viewport: { width: 414, height: 848 } });
  ctx.setDefaultTimeout(5000);
  const target = url || DOC_URL;
  const posts = [];
  await ctx.route('**/*', async (route) => {
    const u = route.request().url();
    // the document itself (and anything on the Pages origin that is not an API call)
    if (u.startsWith(target.split('?')[0]) || u === target) {
      return route.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body });
    }
    for (const key of Object.keys(api || {})) {
      if (u.includes(key)) {
        const rule = api[key];
        if (rule === 'abort') return route.abort('failed');
        // The page lives on *.pages.dev and calls the Worker on *.workers.dev — CROSS-ORIGIN. Both
        // `X-Grant` and `Content-Type: application/json` are non-simple, so the browser sends a
        // preflight first. A fulfilled response without CORS headers is BLOCKED by the browser, the
        // fetch rejects, and the page takes its offline branch — i.e. every path silently resolves to
        // s-nolink and the runner reports the product broken when it is the harness that is.
        if (route.request().method() === 'OPTIONS') {
          return route.fulfill({ status: 204, headers: CORS, body: '' });
        }
        if (route.request().method() === 'POST') {
          try { posts.push({ url: u, body: JSON.parse(route.request().postData() || '{}') }); }
          catch (e) { posts.push({ url: u, body: null }); }
        }
        return route.fulfill({ status: rule.status,
                               headers: Object.assign({ 'Content-Type': 'application/json' }, CORS),
                               body: JSON.stringify(rule.json === undefined ? {} : rule.json) });
      }
    }
    // anything else on the page (there should be none — the page makes no third-party request)
    return route.fulfill({ status: 404, body: '' });
  });
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', (e) => errors.push(String(e && e.message || e)));
  page.__errors = errors;
  if (storage) {
    // seed localStorage on the right origin before the document runs
    await page.addInitScript((s) => {
      try { for (const k of Object.keys(s)) localStorage.setItem(k, s[k]); } catch (e) {}
    }, storage);
  }
  await page.goto(target, { waitUntil: 'load', timeout: 45000 });
  await page.waitForTimeout(cfg.settleMs || 900);
  page.__posts = posts;
  page.__ctx = ctx;
  return page;
}

// which of the six screens is visible
async function visible(page) {
  return page.evaluate((ids) => {
    const shown = ids.filter((id) => {
      const el = document.getElementById(id);
      return el && !el.hidden;
    });
    return shown;
  }, cfg.screens);
}
async function nolinkHTML(page) {
  return page.evaluate(() => {
    const el = document.getElementById('s-nolink');
    return el ? el.innerHTML.replace(/\s+/g, ' ').trim() : null;
  });
}

// ── the run ────────────────────────────────────────────────────────────────
(async () => {
  const exe = process.env.QA_WALK_CHROMIUM || null;
  const browser = await chromium.launch(exe ? { executablePath: exe } : {});
  const DOC = cfg.docBody;
  const OK_WHOAMI = { status: 200, json: { personId: 'p-qa-fixture-a', estateId: 'est-qa0001', capability: 'member' } };
  const NOT_FOUND = { status: 404, json: { error: 'not found' } };
  const api = (whoami, feedback) => {
    const m = {};
    if (whoami) m['/api/grant/whoami'] = whoami;
    if (feedback) m['/api/feedback'] = feedback;
    return m;
  };

  try {
    // ─── PATH 13 FIRST — document identity. If the runner cannot tell the product from a
    // 200-status page that is not the product, nothing else it reports means anything.
    {
      const p = await openPage(browser, { body: cfg.loginBytes, api: api(OK_WHOAMI) });
      const title = await p.title();
      const ids = await p.evaluate((s) => s.map((id) => !!document.getElementById(id)), cfg.screens);
      const isProduct = title === cfg.identity.title && ids.every(Boolean);
      record(13, 'wrong document (Access login, HTTP 200) is REFUSED', !isProduct,
             isProduct ? 'the runner accepted a non-product page' : `saw title="${title}"`);
      await p.__ctx.close();
    }

    // ⛔ THE GATE: if the document under test is not the product, STOP. Asserting paths 1-12 against
    // a page that has none of the elements is not a red run — it is a runner interrogating the wrong
    // document, which is the exact confusion path 13 exists to prevent. (It also hangs: every
    // fill()/click() waits out its timeout on a selector that will never appear.)
    {
      const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI) });
      const title = await p.title();
      const ids = await p.evaluate((s) => s.map((id) => !!document.getElementById(id)), cfg.screens);
      await p.__ctx.close();
      if (!(title === cfg.identity.title && ids.every(Boolean))) {
        record(0, 'the document under test IS the product', false,
               `served title="${title}" but the tree says "${cfg.identity.title}" — paths 1-12 not run`);
        await browser.close();
        console.log(JSON.stringify({ results, abortedOnIdentity: true }, null, 2));
        return;
      }
    }

    // ─── PATH 1 — the link carries the credential, and the credential leaves the address bar
    {
      const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI), url: DOC_URL + '?g=' + cfg.grant });
      const shown = await visible(p);
      const search = await p.evaluate(() => location.search);
      const stored = await p.evaluate(() => localStorage.getItem('fw-grant'));
      record(1, 'valid ?g on a known host → s1, ?g stripped, and nothing thrown',
             shown.join() === 's1' && !/[?&]g=/.test(search) && stored === cfg.grant && p.__errors.length === 0,
             `screen=${shown.join()||'none'} search="${search}" stored=${stored ? 'yes' : 'no'} scriptErrors=${JSON.stringify(p.__errors)}`);
      await p.__ctx.close();
    }

    // ─── PATH 2 — no credential at all
    let nolink2 = null;
    {
      const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI) });
      const shown = await visible(p);
      nolink2 = await nolinkHTML(p);
      record(2, 'no g, empty storage → s-nolink', shown.join() === 's-nolink', `screen=${shown.join()||'none'}`);
      await p.__ctx.close();
    }

    // ─── PATH 3 — an unknown/revoked credential must look IDENTICAL to path 2
    {
      const p = await openPage(browser, { body: DOC, api: api(NOT_FOUND), url: DOC_URL + '?g=bogus-not-a-grant' });
      const shown = await visible(p);
      const html = await nolinkHTML(p);
      record(3, 'unknown/revoked grant → s-nolink, byte-identical to path 2',
             shown.join() === 's-nolink' && html === nolink2,
             shown.join() !== 's-nolink' ? `screen=${shown.join()||'none'}`
               : (html === nolink2 ? 'identical' : 'COPY DIFFERS from path 2 — the failure screen leaks which case it was'));
      await p.__ctx.close();
    }

    // ─── PATH 4 — offline is NOT a bad link and must not be dressed as one
    {
      const p = await openPage(browser, { body: DOC, api: api('abort'), url: DOC_URL + '?g=' + cfg.grant });
      const shown = await visible(p);
      const html = await nolinkHTML(p);
      const differs = html !== nolink2;
      const saysConn = /connection|wi-?fi/i.test(html || '');
      // ⛔ 'the offline copy appeared' is satisfied by the very catastrophe it must exclude: when
      // step() threw on every call (09-05), EVERY path showed this copy and this row went green.
      // A genuine offline must ALSO be quiet — no script fault behind it.
      const quiet = p.__errors.length === 0;
      record(4, 'whoami unreachable → the OFFLINE copy, and NOTHING was thrown behind it',
             shown.join() === 's-nolink' && differs && saysConn && quiet,
             `screen=${shown.join()||'none'} differsFromBadLink=${differs} mentionsConnection=${saysConn} scriptErrors=${JSON.stringify(p.__errors)}`);
      await p.__ctx.close();
    }

    // ─── PATH 5 — an unknown Pages host must fail closed (WORKER resolves null)
    {
      const bogusOrigin = 'https://fernwood-not-a-real-label.pages.dev';
      const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI),
                                          url: bogusOrigin + cfg.docPath + '?g=' + cfg.grant });
      const shown = await visible(p);
      record(5, 'unknown Pages host → s-nolink (WORKER null, fail-closed)',
             shown.join() === 's-nolink', `screen=${shown.join()||'none'}`);
      await p.__ctx.close();
    }

    // ─── PATH 6 — the resume table, including the deliberate 3 → s4
    for (const [step, want] of [['2', 's2'], ['3', 's4'], ['4', 's4']]) {
      const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI),
                                          storage: { 'fw-grant': cfg.grant, 'fw-onboard-step': step } });
      const shown = await visible(p);
      record(6, `resume: fw-onboard-step=${step} → ${want}`, shown.join() === want,
             `screen=${shown.join()||'none'}`);
      await p.__ctx.close();
    }

    // ─── PATH 7 — a missing required field names WHAT is missing and never scolds
    {
      const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI, { status: 200, json: { stored: 1 } }),
                                          storage: { 'fw-grant': cfg.grant, 'fw-onboard-step': '2' } });
      await p.fill('#a1', '123 Example Rd');          // city, state, zip deliberately left empty
      await p.click('#go2');
      await p.waitForTimeout(300);
      const shown = await visible(p);
      const trouble = await p.evaluate(() => {
        const t = document.getElementById('trouble');
        return { hidden: t.hidden, text: (t.textContent || '').trim() };
      });
      const focused = await p.evaluate(() => document.activeElement && document.activeElement.id);
      const names = /city/i.test(trouble.text) && /state/i.test(trouble.text) && /ZIP/i.test(trouble.text);
      record(7, 'submit with gaps → stays on s2, names what is missing, focuses the first gap',
             shown.join() === 's2' && !trouble.hidden && names && focused === 'city',
             `screen=${shown.join()||'none'} trouble="${trouble.text}" focus=${focused}`);
      await p.__ctx.close();
    }

    // ─── PATHS 8 + 9 — the fingerprint, across THREE fresh sessions.
    // Replay must dedup to the SAME id; a correction must produce a DIFFERENT one. Doing this in one
    // page means clicking #go2 while it is still disabled with "Saving…" — a harness fault, not a
    // finding — so each submit gets its own context, which is also the realistic shape (she comes
    // back later and fixes it).
    {
      const submit = async (line1, feedbackJson) => {
        const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI, { status: 200, json: feedbackJson }),
                                            storage: { 'fw-grant': cfg.grant, 'fw-onboard-step': '2' } });
        await p.fill('#a1', line1); await p.fill('#city', 'Jasper');
        await p.fill('#state', 'GA'); await p.fill('#zip', '30143');
        await p.click('#go2');
        await p.waitForTimeout(500);
        const shown = await visible(p);
        const posts = p.__posts.filter((x) => x.url.includes('/api/feedback'));
        const id = posts.length ? posts[posts.length - 1].body && posts[posts.length - 1].body.id : null;
        const errs = p.__errors.slice();
        await p.__ctx.close();
        return { shown: shown.join(), id, errs };
      };

      const first  = await submit('123 Example Rd', { stored: 1 });
      const replay = await submit('123 Example Rd', { stored: 0, duplicate: true });
      const fixed  = await submit('456 Corrected Ave', { stored: 1 });

      record(8, 'replay of identical text → {stored:0,duplicate:true} accepted → s3, same record id',
             replay.shown === 's3' && replay.id !== null && replay.id === first.id,
             `screen=${replay.shown||'none'} firstId=${first.id} replayId=${replay.id}`);

      record(9, 'a CORRECTED address produces a DIFFERENT record id (not a silent no-op)',
             fixed.id !== null && first.id !== null && fixed.id !== first.id && fixed.shown === 's3',
             `firstId=${first.id} correctedId=${fixed.id} screen=${fixed.shown||'none'}`);
    }

    // ─── PATH 10 — a 200 is not proof of a write
    {
      const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI, { status: 200, json: { stored: 0 } }),
                                          storage: { 'fw-grant': cfg.grant, 'fw-onboard-step': '2' } });
      await p.fill('#a1', '789 Nowhere Ln'); await p.fill('#city', 'Jasper'); await p.fill('#state', 'GA'); await p.fill('#zip', '30143');
      await p.click('#go2'); await p.waitForTimeout(500);
      const shown = await visible(p);
      const st = await p.evaluate(() => ({
        troubleHidden: document.getElementById('trouble').hidden,
        troubleText: (document.getElementById('trouble').textContent || '').trim(),
        disabled: document.getElementById('go2').disabled,
      }));
      record(10, '{stored:0} without duplicate → stays on s2, retry copy, button re-enabled',
             shown.join() === 's2' && !st.troubleHidden && !st.disabled,
             `screen=${shown.join()||'none'} buttonDisabled=${st.disabled} trouble="${st.troubleText.slice(0, 60)}"`);
      await p.__ctx.close();
    }

    // ─── PATH 11 — storage cleared AFTER the link was consumed. The link stripped ?g, so there is no way back.
    {
      const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI), url: DOC_URL + '?g=' + cfg.grant });
      await p.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
      await p.reload({ waitUntil: 'load' });
      await p.waitForTimeout(cfg.settleMs || 900);
      const shown = await visible(p);
      const html = await nolinkHTML(p);
      record(11, 'storage cleared after the link was consumed → resolves to a STATED outcome',
             shown.join() === 's-nolink', `screen=${shown.join()||'none'} copy="${(html||'').slice(0,70)}"`,
             { stated: 's-nolink (the bad-link screen)', note: 'what the RIGHT outcome is, is a content call — not asserted here' });
      await p.__ctx.close();
    }

    // ─── PATH 12 — a new device, link re-tapped
    {
      const p = await openPage(browser, { body: DOC, api: api(OK_WHOAMI), url: DOC_URL + '?g=' + cfg.grant });
      const shown = await visible(p);
      record(12, 'new device, original link re-tapped → s1', shown.join() === 's1', `screen=${shown.join()||'none'}`);
      await p.__ctx.close();
    }
  } catch (e) {
    record(0, 'runner fault', false, String(e && e.message || e));
  }

  await browser.close();
  console.log(JSON.stringify({ results }, null, 2));
})();
