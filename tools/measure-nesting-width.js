// measure-nesting-width.js — DOES THE NESTING EAT THE WIDTH?
// ============================================================================
// The measurement `BACKLOG.md` § "🔴 OPEN — does the nesting eat the width?"
// demanded before anyone is allowed to propose a fix. Paul raised it twice —
// 2026-08-15 (*"cards within cards and nested drop downs is eating up margins
// and width of the page… this is true across our card schema"*) and again
// 2026-08-24, naming the concrete path: **Wildlife → Insects → one insect**,
// where each door you open leaves the text a narrower column than the last.
//
// The backlog row's own conditions, transcribed so this file can be read alone:
//   · compute the USED content width at every nesting depth
//   · at a REAL viewport, never inferred from the CSS
//   · in BOTH text modes (A and A+)
//   · and it is only worth acting on if it reproduces on ≥2 domains besides
//     the insect card, since the claim is schema-wide
//
// ⭐ WHY THIS MEASURES ROWS AND NOT JUST PIXELS
// --------------------------------------------
// "The column is 84px narrower" is not a user-visible fact. What Mom meets is
// *"more rows than necessary"* — Paul's words, both times. So every text-bearing
// leaf is measured twice: as it renders where it sits, and re-flowed at the
// width its own top-level card has. The difference in LINE BOXES is the cost,
// in the only unit anyone experiences. A level that spends 14px and costs zero
// extra rows is not a defect; a level that spends 8px and pushes a heading onto
// a second line is.
//
// ⭐ IT IS CLASS-AGNOSTIC ON PURPOSE
// ---------------------------------
// It walks the real ancestor chain of real text and names whatever it finds,
// rather than looking for `.main-card → section → info box → disclosure`. The
// claim under test is that this is SCHEMA-WIDE — a probe that only knows the
// four levels someone already wrote down cannot discover a fifth, and would
// have reported "four levels, as expected" on a tree that grew one.
//
// ⛔ WHAT IT DOES NOT DO
// ---------------------
// It reads layout. It clicks doors open to reach nested content and it writes
// nothing: no POST, no canon, no localStorage beyond what opening a card does
// on its own. It is safe against the LOCAL server. Do not point it at the live
// site — not because it would write, but because `people.json` attribution is
// the thing that would get muddied, and a layout number never needs her origin.
//
// HOW TO RUN
// ----------
//   cd ~/Developer/Tate-Tracker && python3 -m http.server 8765
//   lsof -nP -iTCP:8765 -sTCP:LISTEN     # verify the PID, never a curl 200
//
//   ⚠️ HER VIEWPORT IS 414×848, NOT 390 (`BACKLOG.md`, lap 4 2026-08-19 — 51
//   metric batches at 414×848). Every layout check in this repo before that row
//   was sized to 390, which is NARROWER and therefore conservative — nothing
//   already verified is invalidated, but no check had ever measured the 24px she
//   actually has. 414 is canonical here; 390 is kept as the stress case.
//   Both sizes are named in the VIEWPORTS register below — add a size there,
//   never as a literal, so the next reader learns where a number came from.
//
//   ⚠️ WINDOW RESIZE SILENTLY DOES NOT TAKE in an automation tab (recorded on
//   the `Fernwood :: Rainfall A+ overflow fix` anchor item, 2026-08-14). Render
//   viewer.html in an IFRAME of the target width instead — same origin, so
//   `@media (max-width:480px)` resolves against the FRAME and the numbers are
//   real. `measureNestingWidth.inFrame()` below does exactly that; do not
//   re-discover the wall.
//
//   open http://localhost:8765/         # any same-origin page will do
//   paste this file into the console, then:
//     await measureNestingWidth.run()               // 414 and 390, A and A+
//     await measureNestingWidth.run({widths:[414]}) // one width
//
//   The two that return a VERDICT rather than a table — run BOTH, read them
//   apart. `clean` means no HIGH.
//     await measureNestingWidth.herConditions()     // 414×848 × A+ — the gate
//     await measureNestingWidth.stressConditions()  // 390×848 × A+ — narrower
//
//   And one that is deliberately NOT in any sweep and NOT a gate — see
//   § LANDSCAPE at the foot of this file before you read anything into it:
//     await measureNestingWidth.landscapeConditions()   // 896×414
//
// Record the result in MOM-CYCLE-LOG.md for the lap, and — if it reproduces —
// in the BACKLOG row that commissioned it.
// ============================================================================

(function () {
  "use strict";

  // The domains to walk. Insects is Paul's named exemplar (the deepest tree in
  // the app); the others are here because the row requires the finding to
  // reproduce on at least two more before it may be called schema-wide.
  // Each entry: [label, card id, optional sub-door opener run inside the card].
  const DOMAINS = [
    ["Wildlife → Insects → one insect", "card-wildlife", openInsect],
    ["Vehicles → one vehicle → specs", "card-vehicles", openVehicleSpecs],
    ["Equipment → one machine", "card-equipment", openFirstDisclosure],
    ["Plants → one plant", "card-plants", openFirstDisclosure],
    ["Household → one system", "card-household", openFirstDisclosure],
    ["Weather", "card-weather", null],
  ];

  // ⭐ THE VIEWPORT REGISTER — one place that names a size and says WHERE IT
  // CAME FROM. Before this existed the numbers were literals scattered through
  // defaults, and "390" read as a considered choice when it was inherited from
  // an exhibit stylesheet nobody had revisited.
  //
  //   CANONICAL — 414×848. HERS, measured: 51 `/api/metrics` device batches at
  //     `414x848` (lap 4, 2026-08-19). This is the size every default resolves
  //     to. Height matters as much as width here: the pre-glance stack measures
  //     1,712px, which is ~2 viewports of 848 and a different story at any other
  //     height, so a check that sets width and lets height float is measuring a
  //     phone nobody owns.
  //   STRESS — 390×848. NOT hers and never was: it came from the
  //     `/design-options` exhibit convention (`compare.html`: `width:min(390px,
  //     88vw)`). It is KEPT, deliberately, because it is 24px NARROWER — every
  //     check this repo ran before lap 4 ran here, so dropping it would retire
  //     the only width the entire test history is expressed in, and would trade
  //     one blind spot for another. It is a stress case, not a target device.
  //   LANDSCAPE — 896×414. OBSERVED ONCE (a single batch, same lap). Defined so
  //     it can be RUN, and deliberately in NO default sweep — see § LANDSCAPE
  //     below for why one batch does not earn a standing case.
  //
  // ⚠️ Nothing between 390 and 414 is a breakpoint: `viewer.html`'s only
  // width media queries are `max-width: 480px` and `max-width: 540px`, so both
  // widths resolve to the SAME CSS branch. That makes a 390-vs-414 divergence
  // less likely — it does NOT make it impossible, because the gap shows up in
  // fluid arithmetic (`calc(100% - 24px)`, flex wrap points, ellipsis boxes),
  // which is exactly where this repo's known width defects have lived.
  const VIEWPORTS = {
    canonical: { w: 414, h: 848, label: "hers (measured, 51 batches)" },
    stress:    { w: 390, h: 848, label: "stress (narrower; the pre-lap-4 convention)" },
    landscape: { w: 896, h: 414, label: "landscape (observed once — not a default)" },
  };

  // A leaf must carry enough of its OWN text to wrap. Short labels ("Aug 9",
  // "Yes") cannot demonstrate a row cost at any width, and counting them would
  // dilute the finding with elements that were never going to wrap.
  const MIN_TEXT = 45;

  // The two thresholds of the ROW TAX RULE. First cut, deliberately stated as
  // tunable rather than derived — the repo's ratified posture for a new visual
  // rule is that it must be a claim someone can CHECK, not that its constant is
  // already right. Tune from what runs show; changing them is a design decision
  // and belongs in the chronicle.
  const LIMIT_ROW_TAX = 1.25;   // Clause A — extra line boxes vs. reflow at card width
  const LIMIT_CHROME = 0.15;    // Clause B — chrome as a share of card content width

  const px = (v) => Math.round(v * 10) / 10;

  function ownText(el) {
    let n = 0;
    for (const c of el.childNodes) if (c.nodeType === 3) n += c.textContent.trim().length;
    return n;
  }

  // The content box: what the text actually gets, after this element's own
  // padding and border are taken out.
  //
  // ⚠️ NOT `clientWidth` — it is **0 for every non-replaced inline box**, so the
  // first run of this tool reported `narrowest: 0` on three of six domains and
  // would have been read as "the column collapses to nothing." It does not; the
  // probe was measuring a property inline elements do not have. Caught before
  // any number left the harness. Same shape as the standing rule in
  // [[reference_match_payload_not_container]] — the wrong box returns a
  // plausible number rather than an error.
  //
  // `getBoundingClientRect()` gives a real border box for inline and block
  // alike; padding and border come off it the same way. An inline leaf's rect
  // is nonetheless the TEXT extent, not the column it may wrap in — which is
  // why `isBlockish()` below keeps inlines out of the leaf set entirely and
  // attributes their text to the block container that actually governs the wrap.
  function contentWidth(el, cs) {
    return el.getBoundingClientRect().width -
           parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight) -
           parseFloat(cs.borderLeftWidth) - parseFloat(cs.borderRightWidth);
  }

  // Only a block container decides where a line breaks. A `<span>` or an `<a>`
  // is carried by whatever block holds it, so measuring it as its own column
  // would price a level that does not exist.
  function isBlockish(cs) {
    return /^(block|flow-root|list-item|flex|grid|table|table-cell|table-row|inline-block)$/.test(cs.display);
  }

  // What THIS level spends horizontally — the number that is claimed to
  // compound down the tree. Margin counts: it narrows the child just as surely
  // as padding does, and a level that pays its cost in margin would otherwise
  // read as free.
  function spend(cs) {
    return parseFloat(cs.paddingLeft) + parseFloat(cs.paddingRight) +
           parseFloat(cs.borderLeftWidth) + parseFloat(cs.borderRightWidth) +
           Math.max(0, parseFloat(cs.marginLeft)) + Math.max(0, parseFloat(cs.marginRight));
  }

  // Line boxes actually painted, via the text's own client rects. This is the
  // rendered truth — not a division of characters by an estimated glyph width.
  function lineCount(el) {
    const r = document.createRange();
    r.selectNodeContents(el);
    const rects = [...r.getClientRects()].filter((x) => x.width > 0 && x.height > 0);
    if (!rects.length) return 0;
    const tops = new Set(rects.map((x) => Math.round(x.top * 2) / 2));
    return tops.size;
  }

  // Re-flow the SAME text at the width its top-level card has, to price the
  // nesting in rows. The clone is measured off-screen with the element's own
  // computed typography copied across, so only the width differs.
  function linesAtWidth(el, width, doc) {
    const cs = doc.defaultView.getComputedStyle(el);
    const host = doc.createElement("div");
    host.style.cssText =
      "position:absolute;left:-99999px;top:0;visibility:hidden;" +
      "width:" + width + "px;box-sizing:content-box;padding:0;border:0;margin:0;";
    const clone = el.cloneNode(true);
    for (const p of ["fontFamily", "fontSize", "fontWeight", "fontStyle", "lineHeight",
                     "letterSpacing", "wordSpacing", "textTransform", "whiteSpace",
                     "textIndent", "hyphens", "wordBreak", "overflowWrap"]) {
      clone.style[p] = cs[p];
    }
    clone.style.width = width + "px";
    clone.style.padding = "0"; clone.style.border = "0"; clone.style.margin = "0";
    clone.style.maxWidth = "none";
    host.appendChild(clone);
    doc.body.appendChild(host);
    const n = lineCount(clone);
    host.remove();
    return n;
  }

  // ── door openers ────────────────────────────────────────────────────────
  // Each returns a promise. A door that is absent returns null rather than
  // throwing — an absent door is a finding to report, not a crash. (The same
  // rule telemetry-walk.js follows for ELEMENT ABSENT.)

  const wait = (ms) => new Promise((r) => setTimeout(r, ms));

  async function clickIn(root, sel, test) {
    const els = [...root.querySelectorAll(sel)];
    const el = test ? els.find(test) : els[0];
    if (!el) return null;
    el.click();
    await wait(120);
    return el;
  }

  async function openInsect(card, doc) {
    // Wildlife carries a tab row; Insects is one tab, then a species opens.
    await clickIn(card, ".wildlife-tab", (e) => /insect/i.test(e.textContent || ""));
    const opened = await clickIn(card, ".bio-species-list .bio-species-row, .bio-species-list > *[onclick], .bio-species-name");
    if (!opened) await clickIn(card, ".bio-species-list *");
    await wait(150);
    return true;
  }

  async function openVehicleSpecs(card) {
    await clickIn(card, ".vehicle-specs-toggle");
    await wait(120);
    return true;
  }

  async function openFirstDisclosure(card) {
    // Whatever this domain calls its second level. Tried in order of how the
    // schema has actually grown, and it stops at the first one that exists.
    for (const sel of [".ref-category-header", ".ref-drawer-toggle", ".prop-panel-title",
                       ".wblock-header", "details > summary", "[aria-expanded]"]) {
      const el = await clickIn(card, sel);
      if (el) return true;
    }
    return false;
  }

  // ── the walk ────────────────────────────────────────────────────────────

  async function measureDoc(doc, label, viewportW) {
    // Carried in the result so a reader can see the mode was VERIFIED applied
    // rather than merely requested — the contamination above was invisible
    // until something printed it.
    const out = {
      viewport: viewportW,
      mode: label,
      textLgApplied: doc.body.classList.contains("text-lg"),
      rootFontSize: doc.defaultView.getComputedStyle(doc.body).fontSize,
      domains: [],
    };

    for (const [name, cardId, opener] of DOMAINS) {
      const card = doc.getElementById(cardId);
      if (!card) { out.domains.push({ domain: name, status: "CARD ABSENT" }); continue; }

      // Open the card itself the way the app opens it, so nothing depends on
      // this script knowing the expansion mechanism.
      const header = card.querySelector(".main-card-header");
      if (header && !card.classList.contains("expanded")) { header.click(); await wait(200); }

      let doorNote = "card only";
      if (opener) {
        try { doorNote = (await opener(card, doc)) ? "nested door opened" : "NESTED DOOR ABSENT"; }
        catch (e) { doorNote = "opener failed: " + e.message; }
        await wait(150);
      }

      const cardCs = doc.defaultView.getComputedStyle(card);
      const cardContent = contentWidth(card, cardCs);

      // Every text-bearing leaf inside the open card.
      const leaves = [...card.querySelectorAll("*")].filter((el) => {
        if (ownText(el) < MIN_TEXT) return false;
        const cs = doc.defaultView.getComputedStyle(el);
        if (cs.display === "none" || cs.visibility === "hidden") return false;
        if (!isBlockish(cs)) return false;   // see contentWidth() — inlines do not own a column
        return el.getBoundingClientRect().width > 0;
      });

      const rows = [];
      for (const leaf of leaves) {
        const cs = doc.defaultView.getComputedStyle(leaf);
        const w = contentWidth(leaf, cs);
        const here = lineCount(leaf);
        const atCard = linesAtWidth(leaf, cardContent, doc);

        // The ancestor ledger: what each level between the card and this text
        // spends, named by whatever it actually is.
        const chain = [];
        let n = leaf;
        while (n && n !== card) {
          const ncs = doc.defaultView.getComputedStyle(n);
          chain.push({
            tag: n.tagName.toLowerCase(),
            cls: (n.className && String(n.className).split(/\s+/)[0]) || "",
            spend: px(spend(ncs)),
            content: px(contentWidth(n, ncs)),
          });
          n = n.parentElement;
        }
        chain.reverse();

        // ── THE ROW TAX RULE (ux-expert seat, lap 5) ────────────────────────
        // Clause A — the VERDICT: no text leaf may cost more than 25% extra line
        //   boxes versus the same text reflowed at its own card's width.
        // Clause B — the DIAGNOSIS: chrome between `.main-card-body` and the leaf
        //   may spend at most 15% of the card's content width.
        //
        // A width FLOOR was tried first and thrown away: "no wrapped column below
        // 60% of its card" does not flag `vehicle-notes`, which sits at 68% and is
        // the worst row cost in the app. The tax has no such blind spot, it is
        // stated in the unit Paul reported twice ("more rows than necessary"), it
        // is scale-invariant (proved by this tool's own A/A+ table), and it
        // AUTO-EXEMPTS short values — a spec cell reading "10W-30" scores 1.00 and
        // can never flag, so the rule needs no exemption list.
        const rowTax = atCard > 0 ? here / atCard : 1;
        const chromeSpend = cardContent - w;
        rows.push({
          text: leaf.textContent.trim().slice(0, 60),
          depth: chain.length,
          width: px(w),
          pctOfViewport: px((w / viewportW) * 100),
          linesHere: here,
          linesAtCardWidth: atCard,
          extraRows: here - atCard,
          rowTax: Math.round(rowTax * 100) / 100,
          chromePct: px((chromeSpend / cardContent) * 100),
          failsA: rowTax > LIMIT_ROW_TAX,
          failsB: chromeSpend / cardContent > LIMIT_CHROME,
          chain,
        });
      }

      // Sorted by the TAX, not by depth or narrowness. The first version sorted
      // by extra rows then width, which buried `vehicle-notes` — the worst
      // offender — among deeper, narrower, cheaper columns. A report that ranks
      // by the wrong key makes its own finding hard to see.
      rows.sort((a, b) => b.rowTax - a.rowTax || b.extraRows - a.extraRows);

      out.domains.push({
        domain: name,
        door: doorNote,
        cardContentWidth: px(cardContent),
        leaves: rows.length,
        deepest: rows.length ? Math.max(...rows.map((r) => r.depth)) : 0,
        narrowest: rows.length ? Math.min(...rows.map((r) => r.width)) : null,
        extraRowsTotal: rows.reduce((s, r) => s + Math.max(0, r.extraRows), 0),
        leavesCostingRows: rows.filter((r) => r.extraRows > 0).length,
        maxRowTax: rows.length ? Math.max(...rows.map((r) => r.rowTax)) : 1,
        breachesA: rows.filter((r) => r.failsA).length,
        breachesB: rows.filter((r) => r.failsB).length,
        worst: rows.slice(0, 6),
      });
    }
    return out;
  }

  // Render viewer.html in a frame of the target width. Same origin, so the
  // media queries resolve against the FRAME — which is the whole point.
  //
  // ⚠️ HEIGHT IS A PARAMETER, not a constant. It was hardcoded to 848 — right
  // for both portrait cases and therefore invisible as an assumption, but it
  // made the observed LANDSCAPE size (896×414) literally inexpressible: you
  // could ask for an 896-wide frame and still get an 848-tall one, i.e. a
  // viewport no device has. Defaults to the canonical height so every existing
  // caller is byte-for-byte unchanged.
  async function inFrame(width, textMode, fn, height) {
    const h = height || VIEWPORTS.canonical.h;
    const f = document.createElement("iframe");
    f.style.cssText = "width:" + width + "px;height:" + h + "px;border:0;position:fixed;left:0;top:0;z-index:99999;background:#fff";
    // ⭐⭐ RESOLVE THE FRAME URL AGAINST THIS PAGE, NEVER FROM THE ROOT
    // (2026-09-01). This read `"/viewer.html"` — a root-absolute path. That
    // resolves locally (`localhost:8765/viewer.html`) and **404s on GitHub
    // Pages**, where the site is served from `/Tate-Tracker/`. So on the LIVE
    // site this harness loaded GitHub's 404 page and measured THAT: the first
    // live run of the new QA leg reported 8 confident HIGH findings about
    // `container`, `h1`, `p` and `a` — GitHub's 404 markup, not Fernwood's.
    //
    // ⛔ This is `match the payload, not the container` inside the instrument
    // that is supposed to catch it, and CLAUDE.md GATES A RELEASE on
    // `herConditions()`. A gate that reads a different document and returns a
    // plausible number is worse than no gate.
    f.src = new URL("viewer.html", document.baseURI).href;
    document.body.appendChild(f);
    await new Promise((r) => { f.onload = r; });
    // The app hydrates after load; give it room, then confirm a card exists.
    let hydrated = false;
    for (let i = 0; i < 40; i++) {
      if (f.contentDocument.querySelector(".main-card")) { hydrated = true; break; }
      await wait(250);
    }
    // ⛔ AND FAIL LOUDLY IF IT NEVER ARRIVED. The old loop `break`s on success
    // and then PROCEEDS ANYWAY on failure — which is precisely how a 404 got
    // measured and scored. Silent-vs-loud is a property of the CONSUMER: this
    // one gates a release, so it must throw rather than report.
    if (!hydrated) {
      const title = (f.contentDocument && f.contentDocument.title) || "(no title)";
      f.remove();
      throw new Error(
        "measure-nesting-width: the frame never rendered a .main-card — it loaded " +
        f.src + " and got \"" + title + "\". NOTHING was measured. " +
        "(On GitHub Pages the app lives under /Tate-Tracker/; serve locally with " +
        "`python3 -m http.server 8765` or run this from the app's own origin.)");
    }
    const doc = f.contentDocument;

    // ⚠️ SET THE MODE EXPLICITLY IN BOTH DIRECTIONS, AND CLEAR THE STORED
    // PREFERENCE FIRST. The first version only ADDED `text-lg` for A+ and did
    // nothing for A — so the A+ frame wrote `tateTracker.textSize` to
    // localStorage, every later frame in the same profile restored it, and the
    // "A" runs were silently A+. Both columns of the A/A+ table reported
    // `hasClass: true`. Caught by probing the class instead of trusting the
    // argument; nothing was reported from the contaminated pass.
    //
    // Key read off viewer.html:20240, NOT guessed — telemetry-walk.js pays for
    // the same lesson in its DAY_KEYS block: a reset that clears a misspelled
    // key silently does nothing and the harness looks fine.
    try { f.contentWindow.localStorage.removeItem("tateTracker.textSize"); } catch (e) {}
    doc.body.classList.toggle("text-lg", textMode === "A+");
    await wait(250);
    const applied = doc.body.classList.contains("text-lg");
    if (applied !== (textMode === "A+")) {
      throw new Error("text mode did not take: asked " + textMode + ", body.text-lg=" + applied);
    }
    let res;
    try { res = await fn(doc, f.contentWindow.innerWidth || width); }
    finally { f.remove(); }
    return res;
  }

  async function run(opts) {
    opts = opts || {};
    // Canonical FIRST, stress second — the order is the message. Whoever reads
    // the console reads hers before the one that is merely conservative.
    const widths = opts.widths || [VIEWPORTS.canonical.w, VIEWPORTS.stress.w];
    const modes = opts.modes || ["A", "A+"];
    const all = [];
    for (const w of widths) {
      for (const m of modes) {
        const label = w + "px · " + m;
        const r = await inFrame(w, m, (doc, vw) => measureDoc(doc, label, vw));
        all.push(r);
        console.log("── " + label);
        console.table(r.domains.map((d) => ({
          domain: d.domain,
          door: d.door,
          card: d.cardContentWidth,
          narrowest: d.narrowest,
          deepest: d.deepest,
          "leaves costing rows": d.leavesCostingRows + "/" + d.leaves,
          "extra rows": d.extraRowsTotal,
        })));
      }
    }
    window.__nestingWidth = all;
    console.log("full detail in window.__nestingWidth");
    return all;
  }

  // ── THE GATE ────────────────────────────────────────────────────────────
  // `run()` REPORTS; this VERDICTS. The difference is the whole point of the
  // rule: a report is read once by whoever ran it, and a threshold that nothing
  // enforces is a preference. Returns {clean, breaches[]} and logs a verdict.
  //
  // Honest boundary, stated so it does not read as full coverage: it checks the
  // six domains in DOMAINS at the widths given, and only text leaves carrying
  // MIN_TEXT characters of their own. A surface not walked is not cleared.
  async function gate(opts) {
    opts = opts || {};
    const all = await run({ widths: opts.widths || [VIEWPORTS.canonical.w], modes: opts.modes || ["A"] });
    const breaches = [];
    for (const r of all) {
      for (const d of r.domains) {
        for (const leaf of (d.worst || [])) {
          if (leaf.failsA || leaf.failsB) {
            breaches.push({
              mode: r.mode, domain: d.domain, text: leaf.text,
              rowTax: leaf.rowTax, chromePct: leaf.chromePct,
              clause: (leaf.failsA ? "A" : "") + (leaf.failsB ? "B" : ""),
            });
          }
        }
      }
    }
    const clean = breaches.length === 0;
    console.log(clean
      ? "✓ ROW TAX RULE: clean across " + all.length + " mode(s) — no leaf over "
        + LIMIT_ROW_TAX + "x rows or " + (LIMIT_CHROME * 100) + "% chrome"
      : "⛔ ROW TAX RULE: " + breaches.length + " breach(es)");
    if (!clean) console.table(breaches);
    console.log("   checked: " + DOMAINS.length + " domain(s). A surface not walked is NOT cleared.");
    return { clean, breaches, limits: { rowTax: LIMIT_ROW_TAX, chrome: LIMIT_CHROME } };
  }

  // ── THE PAIR AUDIT ──────────────────────────────────────────────────────
  // `[paul-stated 2026-08-24]`: *"we should challenge ourselves … we're not
  // inventing a new rule, but we're retaining a cohesive look throughout all the
  // different hierarchies — setting up rules over time for how to handle this
  // nesting."*
  //
  // So before any pair row is restyled, this reports what the app ALREADY does.
  // A rule that describes six existing treatments and corrects the outliers is a
  // rule; a rule invented for one row is a preference with a citation.
  //
  // A "pair row" = an element whose children are exactly a short LABEL and one
  // CONTENT node. It finds them structurally rather than from a class list, so a
  // pair nobody wrote down still shows up.
  function pairAudit(doc, cardIds) {
    const out = [];
    for (const id of cardIds) {
      const card = doc.getElementById(id);
      if (!card) continue;
      for (const el of card.querySelectorAll("*")) {
        const kids = [...el.children];
        if (kids.length !== 2) continue;
        const cs = doc.defaultView.getComputedStyle(el);
        if (cs.display === "none") continue;
        const [a, b] = kids;
        const at = (a.textContent || "").trim();
        const bt = (b.textContent || "").trim();
        if (!at || !bt) continue;
        // A label is short and is the FIRST child. Content is the longer one.
        if (at.length > 40 || bt.length < at.length) continue;
        // ...and BOTH must be leaf-ish text, or this matches whole containers
        // whose first child merely happens to be short. The first run of this
        // audit reported `.vehicle` as a "pair" with 99,257 characters of
        // content, which is the tell.
        if (a.children.length || b.children.length) continue;

        const ar = a.getBoundingClientRect();
        const br = b.getBoundingClientRect();
        if (!br.width || !ar.width) continue;

        // ⚠️ LAYOUT IS DECIDED BY GEOMETRY, NOT BY COMPUTED `display`.
        // The first version tested `getComputedStyle(child).display === "block"`
        // — but **flex items are BLOCKIFIED**, so every child of a flex row
        // reports `block` and the whole audit read "stacked", including
        // `.chorus-now-item`, which is the one row we already know is
        // side-by-side. A plausible answer, not an error: the same shape as
        // `clientWidth` on inlines earlier in this file.
        // Side-by-side ⟺ the two boxes share a horizontal band and do not
        // overlap horizontally. That is true regardless of how it was achieved
        // (flex, grid, float, table cell).
        const sharesBand = ar.top < br.bottom - 1 && br.top < ar.bottom - 1;
        const disjointX = ar.right <= br.left + 1 || br.right <= ar.left + 1;
        const stacked = !(sharesBand && disjointX);
        const bw = br.width;
        out.push({
          cls: (el.className && String(el.className).split(/\s+/)[0]) || el.tagName.toLowerCase(),
          label: at.slice(0, 22),
          contentChars: bt.length,
          contentWidth: px(bw),
          layout: stacked ? "stacked" : "side-by-side",
          contentLines: lineCount(b),
          // The discriminator the rule turns on: does the CONTENT wrap where it sits?
          wraps: lineCount(b) > 1,
        });
      }
    }
    // One row per class — these repeat many times over and the class is the unit
    // a rule can actually act on.
    const byCls = new Map();
    for (const r of out) {
      const prev = byCls.get(r.cls);
      if (!prev || r.contentChars > prev.contentChars) byCls.set(r.cls, r);
      const cur = byCls.get(r.cls);
      cur.n = (prev ? prev.n : 0) + 1;
    }
    return [...byCls.values()].sort((x, y) => y.contentChars - x.contentChars);
  }

  async function pairs(opts) {
    opts = opts || {};
    const ids = opts.cards || DOMAINS.map((d) => d[1]);
    return await inFrame(opts.width || VIEWPORTS.canonical.w, opts.mode || "A", async (doc) => {
      // open every card and its nested door so the pairs actually render
      for (const [, id, opener] of DOMAINS) {
        const card = doc.getElementById(id);
        if (!card) continue;
        const h = card.querySelector(".main-card-header");
        if (h && !card.classList.contains("expanded")) { h.click(); await wait(180); }
        if (opener) { try { await opener(card, doc); } catch (e) {} }
      }
      await wait(250);
      const rows = pairAudit(doc, ids);
      console.table(rows);
      return rows;
    });
  }

  // ── THE TOKEN AUDIT ─────────────────────────────────────────────────────
  // `[paul-stated 2026-08-24]`: *"what about colour scheme and so on? Is that
  // consistent as well? Text, font, size?"* — the same cohesion question as the
  // pair rule, asked of type and colour instead of layout.
  //
  // Same method, deliberately: inventory what the RENDERED app actually uses,
  // rank by how often, and let the long tail name itself. A design system is not
  // what the stylesheet declares — it is what survives to the screen.
  //
  // ⚠️ It counts ELEMENTS THAT PAINT TEXT, not CSS rules. A rule that never
  // matches anything cannot bother a reader, and a rule that matches 200 nodes
  // is 200 times as load-bearing as one that matches one. Counting declarations
  // would flatter tidiness and miss what people see.
  function tokenAudit(doc) {
    const fonts = new Map(), sizes = new Map(), colors = new Map(), families = new Map();
    const bump = (m, k, el) => {
      if (!m.has(k)) m.set(k, { n: 0, sample: "", where: new Set() });
      const r = m.get(k);
      r.n++;
      if (!r.sample) r.sample = (el.textContent || "").trim().slice(0, 34);
      const cls = (el.className && String(el.className).split(/\s+/)[0]) || el.tagName.toLowerCase();
      if (r.where.size < 5) r.where.add(cls);
    };
    for (const el of doc.querySelectorAll("*")) {
      if (ownText(el) < 2) continue;                 // only nodes that paint their own text
      const cs = doc.defaultView.getComputedStyle(el);
      if (cs.display === "none" || cs.visibility === "hidden") continue;
      if (!el.getBoundingClientRect().width) continue;
      bump(sizes, cs.fontSize, el);
      bump(colors, cs.color.replace(/\s+/g, ""), el);
      bump(families, (cs.fontFamily.split(",")[0] || "").replace(/["']/g, ""), el);
      bump(fonts, cs.fontSize + " / " + cs.fontWeight, el);
    }
    const fmt = (m) => [...m.entries()]
      .map(([k, v]) => ({ value: k, n: v.n, where: [...v.where].join(", "), sample: v.sample }))
      .sort((a, b) => b.n - a.n);
    return { sizes: fmt(sizes), colors: fmt(colors), families: fmt(families), sizeWeight: fmt(fonts) };
  }

  async function tokens(opts) {
    opts = opts || {};
    return await inFrame(opts.width || VIEWPORTS.canonical.w, opts.mode || "A", async (doc) => {
      for (const [, id, opener] of DOMAINS) {
        const card = doc.getElementById(id);
        if (!card) continue;
        const h = card.querySelector(".main-card-header");
        if (h && !card.classList.contains("expanded")) { h.click(); await wait(180); }
        if (opener) { try { await opener(card, doc); } catch (e) {} }
      }
      await wait(300);
      return tokenAudit(doc);
    });
  }

  // ── HER CONDITIONS — the pre-release pass ───────────────────────────────
  // `[paul-stated 2026-08-24]`: *"if she's being served at A+ and at 414 — if
  // that's what she's seeing, you need to run a full check on that pretty much
  // right now, or at least build that in before we do the final release. This
  // lap and every lap thereafter, that should kind of be the default."*
  //
  // ⚠️ WHY THIS DID NOT EXIST, WHICH IS THE POINT. Every layout check in this
  // repo has been run at **390 × A**. Neither number was ever hers:
  //   · 390 came from the /design-options exhibit convention. Her device reports
  //     **414×848** (51 metric batches, lap 4). 390 is NARROWER, so old checks
  //     are conservative and nothing verified is invalidated — but no check had
  //     ever measured the 24px she actually has.
  //   · A was assumed because she has never fired the A/A+ toggle (0 of 37
  //     events, all Paul's). But `text_size_served` reports **{size:"lg",
  //     stored:true}** on her device (2026-08-20, 2026-08-24) — she is SERVED
  //     A+. "Never toggled" and "is on A" are different claims and this repo
  //     had been using the first as evidence for the second.
  // So the combination she actually meets — 414 × A+ — is the one combination
  // that had never been checked. This runs it, and it is meant to run before
  // every release, not once.
  //
  // Honest boundary: it checks the six domains in DOMAINS, one file, one engine.
  // A surface not walked is not cleared, and a real phone can still differ.
  async function herConditions(opts) {
    opts = opts || {};
    const W = opts.width || VIEWPORTS.canonical.w,
          H = opts.height || VIEWPORTS.canonical.h,
          MODE = opts.mode || "A+";
    return await inFrame(W, MODE, async (doc, vw) => {
      for (const [, id, opener] of DOMAINS) {
        const card = doc.getElementById(id);
        if (!card) continue;
        const h = card.querySelector(".main-card-header");
        if (h && !card.classList.contains("expanded")) { h.click(); await wait(180); }
        if (opener) { try { await opener(card, doc); } catch (e) {} }
      }
      await wait(350);

      const findings = [];
      const add = (sev, kind, detail) => findings.push({ sev, kind, detail });

      // 1 · The page itself must not scroll sideways.
      if (doc.documentElement.scrollWidth > W + 1) {
        add("HIGH", "page overflows horizontally",
            doc.documentElement.scrollWidth + "px in a " + W + "px viewport");
      }

      // 2 · Nothing may stick out past the viewport — EXCEPT inside a deliberate
      // horizontal scroller.
      // ⚠️ The first run of this check reported **235 HIGH findings** and ~200 of
      // them were the hourly and 7-day forecast strips, which sit inside
      // `.hourly-strip` / `.forecast-strip` at `overflow-x: auto`. A side-scroller
      // extending past the viewport is the design, not a defect. A check that
      // cries wolf 200 times is worse than no check — it trains its reader to
      // skim, which is the same failure the padded focus queue was written to fix.
      const inScroller = (el) => {
        let n = el.parentElement;
        while (n && n !== doc.body) {
          const cs = doc.defaultView.getComputedStyle(n);
          if (/auto|scroll/.test(cs.overflowX)) return true;
          n = n.parentElement;
        }
        return false;
      };
      for (const el of doc.querySelectorAll("*")) {
        const r = el.getBoundingClientRect();
        if (!r.width) continue;
        if (r.right > W + 1.5 && !inScroller(el)) {
          const cls = (el.className && String(el.className).split(/\s+/)[0]) || el.tagName.toLowerCase();
          add("HIGH", "element past the right edge",
              cls + " ends at " + Math.round(r.right) + "px");
        }
      }

      // 3 · CLIPPING. `.main-card-body` uses `max-height: 8000px` with
      // `overflow: hidden` — at A+ everything grows, so a long card can cross
      // that ceiling and lose its tail SILENTLY: no scrollbar, no error, no
      // visual tell. Same class as the 1MB cliff this repo has hit twice.
      for (const el of doc.querySelectorAll(".main-card-body, .vehicle-specs-panel, [style*='max-height']")) {
        const cs = doc.defaultView.getComputedStyle(el);
        if (cs.overflow !== "hidden" && cs.overflowY !== "hidden") continue;
        const cap = parseFloat(cs.maxHeight);
        if (!isFinite(cap)) continue;
        // ⚠️ A COLLAPSED card is not a clipped card. `clientHeight === 0` means
        // the card is shut, and its content is hidden ON PURPOSE — that is what
        // a collapsed accordion IS. The first run flagged all eight closed cards
        // as "content CLIPPED and hidden"; the one card actually open measured
        // 2337 == 2337, no clipping at all. Only judge what is rendered.
        if (el.clientHeight === 0) continue;
        if (el.scrollHeight > el.clientHeight + 2) {
          const cls = (el.className && String(el.className).split(/\s+/)[0]) || el.tagName.toLowerCase();
          add("HIGH", "content CLIPPED and hidden",
              cls + ": " + el.scrollHeight + "px of content in " + el.clientHeight + "px, overflow hidden");
        } else if (cap && el.scrollHeight > cap * 0.85) {
          add("MED", "approaching a max-height ceiling",
              Math.round(el.scrollHeight) + "px against a " + Math.round(cap) + "px cap");
        }
      }

      // 4 · Tap targets, at HER size. The 08-01 sweep ran at 390.
      const seen = new Set();
      for (const el of doc.querySelectorAll("button, a, [role='button'], [onclick], .tap44")) {
        const r = el.getBoundingClientRect();
        if (!r.width || !r.height) continue;
        const cs = doc.defaultView.getComputedStyle(el);
        if (cs.display === "none" || cs.visibility === "hidden") continue;
        // ⚠️ READ THE ::after BOX. The 2026-08-01 sweep gave a dozen small
        // controls a 44px hit area via a centered transparent `::after`
        // (viewer.html:176-190) — paint and layout deliberately untouched. That
        // area is invisible to `getBoundingClientRect`, so a check that reads
        // only the element's own box reports every one of them as a defect and
        // asks someone to re-fix work that is already done. `.tap44` is the
        // marker; the pseudo-element is the truth.
        const minH = parseFloat(cs.minHeight) || 0;
        const after = doc.defaultView.getComputedStyle(el, "::after");
        const afterH = parseFloat(after && after.height) || 0;
        if (Math.max(r.height, minH, afterH) >= 43.5) continue;
        const cls = (el.className && String(el.className).split(/\s+/)[0]) || el.tagName.toLowerCase();
        if (seen.has(cls)) continue;
        seen.add(cls);
        add("LOW", "tap target under 44px",
            cls + " " + Math.round(r.width) + "×" + Math.round(r.height));
      }

      // 5 · The row tax, at her conditions.
      const measured = await measureDoc(doc, W + "px · " + MODE, vw);
      for (const d of measured.domains) {
        for (const leaf of (d.worst || [])) {
          if (leaf.failsA) {
            add("MED", "row tax breach",
                d.domain.split(" ")[0] + ": " + leaf.rowTax + "× rows — \"" + leaf.text.slice(0, 34) + "\"");
          }
        }
      }

      const order = { HIGH: 0, MED: 1, LOW: 2 };
      findings.sort((a, b) => order[a.sev] - order[b.sev]);
      const counts = findings.reduce((m, f) => (m[f.sev] = (m[f.sev] || 0) + 1, m), {});
      console.log("── HER CONDITIONS: " + W + "×" + H + " × " + MODE +
                  "  ·  " + (opts.caseName || "canonical") +
                  "  ·  textLgApplied=" + doc.body.classList.contains("text-lg"));
      console.table(findings.slice(0, 40));
      return {
        width: W, height: H, mode: MODE, case: opts.caseName || "canonical",
        textLgApplied: doc.body.classList.contains("text-lg"),
        counts, findings,
        clean: !findings.some((f) => f.sev === "HIGH"),
      };
    }, H);
  }

  // ── THE STRESS CASE, WITH A NAME ────────────────────────────────────────
  // `herConditions()` runs the size she HAS. This runs the 24px-narrower size
  // every check in this repo used before lap 4.
  //
  // ⭐ WHY THIS FUNCTION EXISTS AT ALL. 390 was already retained in `run()`'s
  // default widths — but `run()` REPORTS and only `herConditions()` VERDICTS,
  // and leg 6e of `MOM-CYCLE-MAP.md` gates a release on `herConditions()`
  // returning clean. So the stress width had a place in the reporting layer and
  // NO entry point in the deciding layer: at release time, nothing ran it. That
  // is the same shape as keeping a test file and deleting its caller. Now the
  // stress case is a function you can name, run, and fail on.
  //
  // It is deliberately NOT folded into `herConditions()` as a second width. A
  // gate that returns one verdict over two viewports cannot say WHICH one broke,
  // and a stress breach and a hers breach do not deserve the same response: a
  // HIGH at 414 is shipping to Mom, a HIGH at 390 alone is a robustness finding.
  // Run both, read them separately.
  async function stressConditions(opts) {
    opts = opts || {};
    return await herConditions(Object.assign({
      width: VIEWPORTS.stress.w,
      height: VIEWPORTS.stress.h,
      caseName: "stress",
    }, opts));
  }

  // ── § LANDSCAPE — 896×414 ───────────────────────────────────────────────
  // ⚠️ RECOMMENDATION, NOT A RULING. The lap-4 metrics show **one** batch at
  // `896x414` against **51** at `414x848`. One batch is a phone that got turned
  // sideways, not a usage pattern, and it cannot distinguish "she reads in
  // landscape" from "it was face-up on the table while she carried it."
  //
  // So the posture is: DEFINED and RUNNABLE (`landscapeConditions()`), in NO
  // default sweep, and NOT a release gate. Promote it to a standing case only on
  // evidence about HER — the same bar the A+ default was held to and walked back
  // on: a session of real length in landscape, or her saying she turns it.
  //
  // Cheap now, and worth knowing once: at 896 wide the app is ABOVE both of its
  // width breakpoints (`max-width: 480px` / `540px`), so landscape renders a CSS
  // branch her portrait sessions never touch — it is not "the same layout, wider."
  // And 414 tall is half the vertical room, against a pre-glance stack already
  // measured at 1,712px. If it is ever gated, that is the finding to expect.
  async function landscapeConditions(opts) {
    opts = opts || {};
    return await herConditions(Object.assign({
      width: VIEWPORTS.landscape.w,
      height: VIEWPORTS.landscape.h,
      caseName: "landscape",
    }, opts));
  }

  window.measureNestingWidth = {
    run, gate, pairs, tokens,
    herConditions, stressConditions, landscapeConditions,
    inFrame, measureDoc, DOMAINS, VIEWPORTS,
  };
})();
