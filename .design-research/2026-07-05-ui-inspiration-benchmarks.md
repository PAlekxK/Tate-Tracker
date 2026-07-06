# Fernwood — UI Inspiration & Benchmark Research

**Date:** 2026-07-05
**Author:** ux-expert (Paul's standing UX expert)
**Purpose:** Raw discussion material for a working session on evolving Fernwood's interface beyond the 11-card accordion stack. This is **inspiration, not a build spec.** Every idea is grounded in the project's non-negotiables (field-journal identity, Mom's no-glasses read, single static HTML / vanilla JS, restraint).
**Status:** Working material — not committed, not a decision.

**Evidence base for the "Mom" reads below.** Grounded in observed telemetry/logs, not a pending interview. From the 2026-07-02 conversation analysis: Mom (device `d-14nyhnjz`) is a **satisfied one-shot asker** — asks a question, gets a good answer, stops — whose real unmet gap was **logging-with-confidence** ("I hoped it was logged but wasn't sure"). From the main session's fresh 35-day KV metrics analysis (5/20 → 7/5), which I cite rather than re-derive:
- **Highly active: 29 of 35 days, 91 sessions.**
- **The dominant behavior has no designed surface.** In **51 of 91 sessions she expands zero cards** — she scrolls the collapsed 11-card stack as a *glanceable status board* and leaves. The thing she does most is read 11 collapsed headers; there is no surface built for that glance.
- **When she does expand, the ranking is telling:** The Almanac (field notes + Guru chat) is her #1 destination (15 expansions), then Plants (7), Worth considering (6), Wildlife (5), Weather (5). **Celestial and Recent updates are near-dead (2 each).**
- **The 7/2 conversational redesign is working:** composer focus jumped (33 of 39 all-time input-focus events came after 6/20), genuine multi-turn conversations now happen (a 4-turn and two 2-turn since 7/3, where before every conversation was one-shot), and the new add-a-plant flow was used on 7/4.
- **Accessibility + spatial signals:** she used the A/A+ text-size toggle 22 times (no-glasses read confirmed), and the map-zone prototype drew real use from her in May (34 zone taps).

Three of these directly reshape the recommendations below: the 51/91 zero-expand finding *is* the overwhelm problem, measured — her main job (the glance) is unserved; the expansion ranking tells us what's living (Almanac/Plants/Wildlife/Weather/Worth-considering) vs. dead weight on her daily surface (Celestial, Recent updates); and the composer being her #1 destination is real evidence *for* the familiarity/chat-first bet, not just a hypothesis.

**Paul's familiarity hypothesis (now a first-class research angle).** Paul's articulated bet: the best accessibility strategy for Mom isn't just big-type-and-icons — it's **familiarity**. Mom is already a fluent iPhone user and a Claude-plus-photos power user; the interface she operates most confidently is the **chat composer** (Claude/ChatGPT). So a serious candidate is to make Fernwood's front door *feel like the chat surface she already knows*, with the structured content wrapped around it. Section 2 adds a dedicated gallery angle for this; Section 3 adds a dedicated candidate direction (F) and gives it an honest read against the field-journal identity and the no-AI-on-capture principle.

---

## 1. TL;DR — the strongest transferable ideas

0. **Serve the glance — it's her actual job, and it has no home.** The telemetry headline: in **51 of 91 sessions Mom expands zero cards** — she scrolls the collapsed stack as a status board and leaves. Everything below flows from this. The single highest-value move is a **today-first "look-fors" front page** (Direction G): 2–4 specific, seasonal, place-anchored things worth *noticing* on the property this week, in field-journal voice, each inviting a report-back to Garden Guru that logs an observation and makes next week's prompts sharper. It serves her measured behavior, pairs with her #1 destination (the composer), and builds a proprietary observation moat over time.

1. **Split living from reference (two-tier).** The app is already straining toward this. Five cards are *alive* (change with the season/weather: Weather, Plants, Wildlife, Sky, Almanac); six are *reference* (consulted occasionally: Property, Vehicles, Sources, Recent updates, Worth considering — and the teaser strip). Put the reference cards behind one drawer. This is the lowest-cost, highest-leverage move on the table and needs almost no data re-architecture.

2. **Make *time* the primary axis, category the secondary lens.** Fernwood's soul is seasonal and cyclical (Leopold's *Sand County Almanac* is literally organized month-by-month), but its structure is category-first. The single most identity-true evolution is a "July at Fernwood" front that folds the seasonal picks together, with the category cards demoted to a "by subject" way to browse. The data already carries `months[]` fields — the substrate exists.

3. **Compose a "Today at Fernwood" front page — a narrative glance before any cards.** Apple Weather's "Right now…" sentence and every national-park homepage do the same thing: a composed, human first read *before* the modules. One evocative paragraph of what's happening on the land right now, then the cards. This is "looking out at the land," rendered.

4. **Rank the cards by value — kill the 11-equal-tiles flatness.** Right now every card is the same width, weight, and visual tier. Eleven things shouting equally quietly still produces overwhelm. Size, weight, and position should encode which cards are alive vs. reference. (This is your own cross-project principle — *Typographic hierarchy by value* — applied at the card level instead of the text level.) The telemetry gives you the ranking for free: Almanac / Plants / Wildlife / Weather / Worth-considering earn the daily surface; Celestial and Recent updates (2 expansions each in 35 days) should drop to the reference shelf.

5. **Every living module deserves a glanceable preview.** The teaser strip only previews 4 of 11 cards, so the "strip teases, card holds" contract is broken for most of the app. Either extend the preview to every living module, or fold the previews into the front-page narrative so the glance is complete.

6. **Familiarity may beat novelty — the front door Mom already trusts is a chat composer.** Every chat-first product (Claude, ChatGPT, Perplexity) converges on the same shape: a single composer as the front door, with history/library/content wrapped *around* it. The useful design pattern underneath is **"chat as engine, document as dashboard"** — the conversation is the ask-engine, the structured content stays the reference. Fernwood could lead with the surface Mom operates most fluently *and* keep the almanac as the durable record. This is the highest-upside / highest-tension idea in the doc — it collides with "no AI on the capture path" and with what a field journal should *feel* like. Direction F works that tension honestly.

---

## 2. The gallery

Grouped by angle. Every URL below was fetched or confirmed to resolve on 2026-07-05. Where a site is a JS app that didn't yield full text to the fetcher, I say so.

### Nature / place / almanac genre

**Alan's Almanac** — https://alans-almanac.co.uk/
A one-person British seasonal almanac. The entire top-level navigation is the **twelve months** — the year *is* the site map. Each month opens to "seasonal events, dates, activities, food and nature," and a second, thematic axis ("The Year on the Farm," "Seasonal Recipes," "Allotment tasks") lets you cut the same content by topic instead of by time. Evocative seasonal photography sets mood per month.
- **Steal this:** Time as the primary navigation axis, with category as a *secondary* lens over the same content — exactly the inversion Fernwood should consider. Landing on "the current month" means the user never has to choose where to go; the season chose for them.
- **Leave this:** It's a browse-a-static-guide model with no live data and no personalization. Fernwood is *this* property with live weather and a real plant list — the month view has to be generated from Fernwood's own data, not authored prose per month.

**The Old Farmer's Almanac / Farmers' Almanac** — https://www.almanac.com/ (bot-blocks scrapers; resolves in a browser) · https://www.farmersalmanac.com/
The canonical genre reference. Front page composes many modules — today's weather, moon phase, planting-by-the-moon, sky-this-week, folklore — into a "what matters today" digest rather than a menu of sections. A logged-in **Garden Planner journal** lets users record activities.
- **Steal this:** The "front page as today's digest" pattern — the homepage answers "what's going on right now" before it offers navigation. And the moon/sky/planting rhythm is proof that a seasonal-cyclical frame can carry genuine data density without feeling like a dashboard.
- **Leave this:** Both sites are dense, ad-supported, and visually busy — they violate Paul's restraint value badly. Take the *IA idea* (today-first digest), not the visual execution.

**Merlin Bird ID (Cornell Lab)** — https://apps.apple.com/us/app/merlin-bird-id-by-cornell-lab/id773457673
Cornell's field-guide app. The detail worth stealing: **seasonal bar charts for any location "at a glance"** — a small horizontal strip showing a species' abundance across the twelve months, so you instantly see "this bird is here now / gone by August."
- **Steal this:** A tiny **phenology sparkline** — one row, twelve cells, "now" highlighted — is a Mom-legible way to render *when* something happens without any prose. It could sit on every plant/bird/celestial row ("blooming now / peaks in 3 weeks / done") and carries meaning by position and fill, not label text.
- **Leave this:** Merlin's four-mode home (Photo / Sound / Step-by-step / Explore) is a tool launcher for an active identification task — the opposite of Fernwood's leisure-read. Don't import the mode-picker home.

**Phenology wheel** (genre concept) — templates at https://www.montananaturalist.org/blog-post/make-your-own-phenology-wheel/
The analog nature-journal artifact: a circle divided into twelve months, you draw/note what you observe in each wedge. Deeply on-brand for the Leopold identity.
- **Steal this:** As an *orienting motif* — a circular year-wheel showing where "now" sits in Fernwood's cycle is a beautiful, identity-true way to say "here's where we are in the year" at a glance.
- **Leave this:** As *navigation* it fails Mom hard — small radial tap targets, requires reading tiny month labels. Use it as an ornament that orients, not a control that routes (see Direction E and the risk note).

### Best-in-class weather + data apps (calm data density)

**Apple Weather (2024+ redesign)** — concept, see https://ios.gadgethacks.com/how-to/apples-weather-app-just-got-13-new-features-and-changes-latest-iphone-software-update-0385607/
The redesign leads each city with a **"Right now…" narrative** and surfaces the "feels like" temperature *only when it meaningfully differs* from the actual — i.e., the interface stays quiet until a number earns its place.
- **Steal this:** Two things. (1) The narrative-sentence lead — "64° and partly cloudy, saturated ground from yesterday's rain" reads like a journal, not a readout (you already do this on the Weather tile per *Make every surface read at half-engagement* — extend it to a whole front page). (2) **Conditional surfacing** — a data point appears *only when it matters*. Fernwood's frost/drought callouts already lean this way; generalize it: the front page shows a plant only when it's *doing* something this week.
- **Leave this:** Apple's animated backgrounds and depth effects are GPU-heavy spectacle — cite the *conditional-surfacing idea*, skip the WebGL.

**Merry Sky** — https://merrysky.net/ (resolves; a PWA, so the fetcher only saw the title — view in a browser)
"Weather, uncluttered." A pared-back, single-scroll forecast with a clean hourly timeline. Frequently cited as a calm alternative to ad-heavy weather apps.
- **Steal this:** The single-column, generously-spaced, no-chrome calm — proof that one scroll of well-ranked data reads as serene, not sparse. Fernwood's single-column instinct is *right*; the problem is the number of equal-weight cards, not the column.
- **Leave this:** It's mono-purpose (weather only). Fernwood's challenge is many modules, which Merry Sky never has to solve.

**(Not Boring) Weather** — https://apps.apple.com/us/app/not-boring-weather/id1531063436 · **Hello Weather** · **Weawow** — https://play.google.com/store/apps/details?id=com.weawow
Three calm-weather benchmarks. (Not Boring) proves personality and restraint can coexist (playful, but never busy). Hello Weather is the "no news, no ads, just the forecast in cards" glance standard. Weawow leads with a full-bleed **photograph** of real weather to set mood before any data.
- **Steal this:** From Weawow — a single evocative *image of the property/season* as the emotional lead of the front page does more for the field-journal feel than any amount of chrome. From Hello Weather — the "Right now" glance discipline.
- **Leave this:** (Not Boring)'s skinnable-icon novelty and Weawow's stock-photo globalism are off-identity — Fernwood's image should be *this land*, not a beautiful anywhere.

### Editorial & narrative design

**The Pudding** — https://pudding.cool/
Data-journalism studio. Two relevant lessons. Its **homepage is a numbered magazine index** — thumbnail + bold lowercase headline + one-line tagline, filterable by "Our Faves / Popular." Its house philosophy is explicit: *"restraint beats spectacle — not every section needs animation; let the data carry the weight."*
- **Steal this:** (1) The magazine-index feel for a "browse the estate" view — image + headline + one-line pull is more inviting than an accordion label. (2) The restraint credo, verbatim — it's Paul's own value in a working studio's words.
- **Leave this:** Pudding is a publication of discrete finished essays; Fernwood is a living reference. Don't adopt the "issues and archive" framing — Fernwood isn't published in editions.

**Scrollytelling (Pudding's technique)** — https://pudding.cool/process/responsive-scrollytelling/
Content reveals/changes as you scroll a single narrative, no clicking. The pacing rule they preach: "short and sweet — a few steps to grab the user, then out."
- **Steal this:** For a "walk through the seasons" or property-tour feature, letting the land reveal itself on scroll (spring → summer → fall on one page) is more Leopold than a tabbed control. A *light* touch — content fading in as it enters view.
- **Leave this:** Full scrolljacking is disorienting and an accessibility hazard for Mom (hijacked scroll defeats muscle memory). If used at all, keep it to gentle fade-in-on-enter, never pinned/hijacked scroll.

### Dashboard / IA patterns for many-module products

**NPS Unigrid & the parks design system** — heritage: https://en.wikipedia.org/wiki/Unigrids · system origins: https://www.figma.com/blog/made-in-figma-the-national-park-service-goes-from-paper-to-pixels/
Massimo Vignelli's 1977 Unigrid — a single modular grid that standardized every park brochure — won a Presidential Design Award for *"reducing routine decisions so that effort can be concentrated on quality."* The modern nps.gov design system descends from it.
- **Steal this:** The core philosophy — **one modular grid so every module looks like family, and the design stops making per-card decisions.** Fernwood's cards are already near-consistent; formalizing a single card grammar (one header shape, one type scale, one preview shape) is what lets you *add* modules without adding chaos. Consistency is the antidote to "too many cards feeling overwhelming."
- **Leave this:** Unigrid's Helvetica-modernist coolness is the wrong *tone* for a warm Appalachian journal. Borrow the systematic discipline, keep your Crimson-Text warmth.

**Great Smoky Mountains NP homepage** — https://www.nps.gov/grsm/index.htm
The nearest real-world analog to Fernwood's problem: a *place* with a large amount of information. Its structure is instructive: a seasonal hero image, a one-line "what this place is," then **two clear primary buttons** ("Plan your visit" / "About the park"), and — critically — **operational info (alerts, closures) is a separate calm card, deliberately split from the inspirational content.** Below, thematic cards (wildlife, scenic spots, heritage) in a 2–3 column grid.
- **Steal this:** (1) The **inspirational/operational split** — Fernwood's living seasonal cards (inspirational) and its reference cards (Vehicles, Sources = operational) should not sit at the same visual tier. This validates Direction C directly. (2) Just two primary entry points above a calmer grid — radical reduction of top-level choices.
- **Leave this:** The park page is built for *first-time visitors planning a trip*; Fernwood's daily user is a returning reader who wants "what's new on my land today," not "plan your visit." The hero-CTA model is too transactional — adapt the *split*, not the CTAs.

**Bento grids** — gallery: https://bentogrids.com/
The modular-tile layout (varied tile sizes, size encodes importance). The genuinely useful IA idea underneath the trend: **signal at the grid level, detail on drill-down** — the tile shows the headline number/state, the tap opens the full data (how Linear and Datadog handle density).
- **Steal this:** Size-encodes-importance is the cure for the 11-equal-cards flatness. A composed layout where Weather + This-Month's-Plants get large tiles and Sources gets a small one instantly communicates hierarchy — no labels required, which is a *Mom win*.
- **Leave this:** ⚠️ **Biggest tone risk in this whole document.** Bento is the visual grammar of SaaS/ops dashboards — KPI tiles, status chips, metric cards. Dropped into Fernwood carelessly it would import the exact "monitoring dashboard" register your *Glyphs follow the journal voice* and *Caution as noticing* principles exist to keep out. If you go bento, it must be warm, asymmetric, and journal-voiced — never a grid of metrics.

### Chat-first / assistant-first interfaces (familiarity as accessibility)

This is the angle Paul's hypothesis points at: apps where a **conversational surface is the front door** to a content-rich product — not a widget buried in a card. The recurring lesson across all of them: the composer is the primary object, and everything else (history, library, sources, structured content) is scaffolding arranged *around* it.

**Claude & ChatGPT mobile apps** — https://claude.ai/ · https://chatgpt.com/
The interface Mom already operates fluently. The IA is worth studying precisely *because* it's the thing she trusts: a minimalist chat screen is the whole home; a hamburger/sidebar holds conversation **history** and **Projects**; **search + memory** let past conversations resurface. Claude's follow-up module is especially relevant — when a question is broad it **asks a clarifying question and offers tappable predefined answers**, so the user checks a box instead of typing.
- **Steal this:** (1) The composer-as-home model — one obvious thing to do on arrival, no navigation decision. (2) **Tappable predefined answers** as a low-typing input — a Mom-legible way to steer a conversation without a keyboard, and a natural home for Fernwood's seeded prompts. (3) History/library lives *beside* the composer, not instead of it — the structured almanac and the chat can coexist.
- **Leave this:** A blank chat screen is a cold open — it says "ask me anything" and answers nothing until you type. Fernwood's whole value is the *unprompted* seasonal read ("here's what's happening on the land"). A pure chat home would throw that away. The composer can be the front door, but it must open *onto* the land's current state, not onto emptiness.

**Perplexity** — https://www.perplexity.ai/
The "answer engine as homepage." One composer; the response is a **synthesized answer at the top with its sources attached**, not a list of links. It shows intermediate progress (so waiting feels productive) and uses **expandable sections** to drill from summary into detail.
- **Steal this:** Answer-then-sources maps cleanly onto Fernwood's own good habit — Garden Guru should answer in this-property voice and *cite the almanac/plant record it drew from*. And the expandable summary→detail is progressive disclosure done conversationally.
- **Leave this:** Perplexity is a pure lookup tool with no identity and no "at rest" state — it exists to be queried and is blank otherwise. Fernwood is a *place you visit*, not a query box. Take the answer-with-provenance shape, not the blank-until-asked posture.

**Arc Search "Browse for me" / Spotlight-style launchers** — https://arc.net/ (pattern reference) · (Spotlight = the iOS pull-down search Mom already uses)
Two precedents for "ask-first" front doors, one AI-native and one pre-AI. Arc Search collapses search + read into a single ask; Spotlight is the OS-level "type what you want and it appears" launcher every iPhone user already has muscle memory for.
- **Steal this:** The **launcher mental model** — a single input that routes you to the right thing is deeply familiar and requires zero learning. If Fernwood ever adds a "jump to anything" input, model it on Spotlight (a pattern Mom already owns), not a bespoke nav.
- **Leave this:** Launchers are for *goal-directed retrieval* ("take me to X"). Mom's dominant mode is leisure-browse, not retrieval — she doesn't arrive knowing what she wants. A launcher-first home optimizes the wrong trigger rhythm (your own *Home is shaped by the dominant trigger rhythm* candidate principle).

**"Chat as engine, document as dashboard"** (pattern) — described at https://medium.com/@tselvaraj/build-a-perplexity-like-user-interface-for-your-private-data-1930bf0f7e72
An emerging design principle for AI + structured-content apps: **decouple the thinking surface (chat) from the durable artifact (the document/dashboard).** The document stays primary and directly editable; the chat is one way to act on it, not a replacement for it.
- **Steal this:** This is the cleanest resolution of Fernwood's tension. The **almanac is the document/dashboard** (durable, deterministic, the reader's own words); **Garden Guru is the engine** (an ask-layer that reads and appends to it). Framing it this way lets the composer be prominent *without* dissolving the field journal into a chat log — the journal is still the object; chat is just one door into it.
- **Leave this:** Nothing to reject — this is more a reconciling frame than a site. It's the principle that keeps Direction F honest.

### Prompted-observation / citizen-science (the "noticing" prompt)

The genre that has already solved Paul's newest idea: systems that surface a *small, specific, place-anchored thing to notice right now* — and turn the user's noticing into logged data. This is the design heritage behind the "look-fors flywheel" (Direction G).

**Nature's Notebook (USA National Phenology Network)** — https://www.usanpn.org/nn
The gold-standard phenology citizen-science program. Observers record *the timing of life-cycle events* — when a specific plant flowers, fruits, drops leaves — and the program runs **campaigns** that prompt people to watch for a particular species-event in season. The whole model is: prompt someone to notice one specific phenophase → they report it → it accretes into a long-term dataset.
- **Steal this:** The exact loop Fernwood wants — *a place-anchored, seasonally-timed prompt to notice one specific thing*, and the report feeding a growing record. This is the citizen-science proof that "watch for the first buds on the smooth hydrangea this week" is a real, motivating interaction, and that the observation it produces has compounding value (your repo's Phase G direction, validated by a national program).
- **Leave this:** Nature's Notebook is *systematic protocol* science — rigid phenophase definitions, standardized reporting forms. Fernwood's version must stay a warm invitation ("worth a look"), not a data-entry protocol. Take the loop, not the clipboard.

**Seek by iNaturalist** — https://www.inaturalist.org/pages/seek_app
The family-friendly, gamified sibling of iNaturalist. Its core surface shows **"organisms commonly found near you right now,"** drawn from millions of local observations, and nudges you to go find them (badges, seasonal challenges).
- **Steal this:** The **"likely near you now" list** as a discovery prompt — a small, curated, place-and-season-filtered set of things to go look for. Fernwood already knows its ~17 plants + wildlife + their months; generating "here's what's worth noticing this week on *this* property" is the same move, made hyper-local.
- **Leave this:** The gamification (badges, streaks, challenges) is exactly the achievement/urgency register the field-journal identity forbids. No badges, no streaks, no "you're on a 5-day noticing streak!" Keep the noticing intrinsic, never gamified.

**Planta / Gardenize** (plant-care apps) — https://apps.apple.com/us/app/gardenize-plant-care-gardening/id1118448120
The mainstream personalized-plant-care category. Both generate a per-plant schedule from your collection + location/climate and surface "what to do" — water, fertilize, prune, repot — as **reminders and tasks**.
- **Steal this:** The *derivation* is right — personalized, location-and-season-aware, per-plant care timing generated from a plant list. Fernwood has richer inputs (per-plant `peakWindow`, `narrow` timing windows, on-site weather station) to do this *better* than a generic app.
- **Leave this:** ⚠️ The **register is the anti-pattern** — reminders, tasks, checkboxes, "due" framing. This is precisely the task-manager idiom Fernwood exists to reject. Same underlying data, opposite voice: not "Prune the hydrangea (due)" but "the smooth hydrangea's first buds may be showing this week — worth a look." The gap between these two sentences *is* the Fernwood identity.

### Personal / "digital garden" sites (evergreen vs. growing content)

**Maggie Appleton's Garden** — https://maggieappleton.com/garden/
The reference digital garden. Notes are tagged by **growth stage — Seedling / Budding / Evergreen** — signaling maturity, and cross-cut by 30+ topics and by content *type* (Essay / Note / Pattern / Smidgeon). Timestamps ("almost 2 years ago") give freshness awareness without hiding evergreen material.
- **Steal this:** The **maturity/liveness tier as a first-class organizing device.** Fernwood's version isn't seedling/evergreen — it's **living vs. reference.** The garden proves you can hold "always-changing" and "stable-reference" content in one calm space by *tiering* it, which is the backbone of Direction C. Also: the "Smidgeon" (tiny observation) as its own type maps neatly to Almanac field notes.
- **Leave this:** The 30-topic filter grid is a power-user browse tool — far too much choice for Mom's glance. The tiering idea ports; the dense filter UI does not.

---

## 3. Candidate directions for Fernwood

Seven distinct evolution paths. **The telemetry moved my recommendation.** The 51-of-91 zero-expand finding means Mom's dominant job — the glance — has no designed home, and that is *the* overwhelm problem, measured. So the headline recommendation is now **Direction G (a today-first "look-fors" front page)**, which serves the glance directly, pairs naturally with the composer (her #1 destination), and demotes the dead-weight cards the telemetry exposed. **Direction C (two-tier split)** is still the cheap enabling move underneath it. A and B are identity-forward structural options; D and E are flagged; F (chat-first) is the biggest and most tension-laden bet. G is essentially a disciplined synthesis of A + C + F + the observation flywheel — read it last, but weight it first.

### Direction C — Two-tier: a living page + a reference drawer *(recommended first move)*
**Concept:** Formalize the split the app is already straining toward. Tier 1, always visible: the ~5 *living* cards that change with season/weather (Weather, Plants, Wildlife, Sky & Stars, The Almanac). Tier 2, behind one collapsed entry ("The Ledger" / "Reference" / "About the estate"): the ~6 *reference* cards (Fernwood/Property, Vehicles & Equipment, Sources, Recent updates, Worth considering). Mom's daily glance now meets 5 living cards, not 11 flat ones.
**Informed by:** Maggie Appleton's living/evergreen tiering; NPS Great Smoky's inspirational/operational split; Farmers' Almanac today-first digest.
**Honors the identity:** An almanac has a *body* (the seasonal read) and an *appendix* (the reference tables). This is that structure, exactly. Nothing about it reads as task-manager.
**Mom-accessibility read:** Strong. Fewer, larger, all-seasonal cards on the daily surface; the reference material stops competing for her attention. Routing to the drawer is one obvious labeled entry, not a hidden gesture.
**Implementation weight (no-build vanilla):** **Low.** Mostly reordering existing cards into two DOM groups with one collapsible divider between them. No data re-architecture, no new render pipeline. A weekend.
**Main risk:** Drawing the boundary. "Worth considering" is semi-living (seasonal plant sales), and "Property/Fernwood" is the identity anchor — you may want it visible even though it's reference. Decide the boundary deliberately; don't let it default.

### Direction A — "Today at Fernwood" front page, cards demoted to a shelf below
**Concept:** The landing surface becomes a single composed **narrative glance** — one evocative image of the land + a short paragraph of what's happening *right now* (weather sentence + what's blooming/calling this week + what's in the sky tonight), generated from the live data you already have. The 11 cards live *below* that front page (or behind it), as the reference shelf you consult when the glance makes you curious.
**Informed by:** Apple Weather's "Right now…" narrative + conditional surfacing; national-park hero-then-modules; Weawow's image-led calm; the Farmers' Almanac today digest.
**Honors the identity:** This is the most literal expression of "looking out at the land" — you open Fernwood and it *tells you what's happening*, in journal voice, before it shows you any machinery.
**Mom-accessibility read:** Excellent — one large, high-contrast narrative is the easiest possible read at half-engagement. She may never need to scroll to a card at all; the front page *is* the product for her.
**Implementation weight:** **Medium.** You have all the raw material (tile summaries, alerts, plant-care-this-month logic). The work is a new composing function that assembles a few live sentences + picks the 2–3 things "doing something this week," plus sourcing one seasonal property image. The cards stay as-is underneath.
**Main risk:** The front page becomes a new dumping ground — every card lobbies to be on it and it bloats back into overwhelm. Needs an editorial rule: *the front shows only what is doing something right now.* Also, the image must be *this land* and must not go stale (your *Static visuals lie on dynamic surfaces* principle — a fixed hero on a "today" surface is a trap; rotate it by season at least).

### Direction B — The almanac spine: month/season as the primary axis
**Concept:** Invert the structure. Top level becomes **time** — "July at Fernwood" — folding the cross-cutting seasonal picks together (what's blooming, what's calling, what's in the sky, what the turf needs) into one monthly read. The category cards (Plants, Wildlife, Sky) become a *secondary* "by subject" lens over the same data. Landing defaults to the current month.
**Informed by:** Alan's Almanac (month-as-navigation); Leopold's month-structured *Sand County Almanac*; Merlin's seasonal bar charts; the phenology wheel.
**Honors the identity:** The deepest of all directions. The cultural touchstone is *literally* a month-by-month almanac. Time-first *is* the field-journal worldview — calm, cyclical, seasonal.
**Mom-accessibility read:** Strong *if and only if* the current month is the default landing and she never has to pick a month. It fails the moment it asks her to navigate a month-picker. Land on "now"; make browsing other months a deliberate secondary act.
**Implementation weight:** **Medium-high.** The data substrate exists (`months[]`, `peakWindow`, `monthsPresent` are already on plants/birds/etc.), so a "what's happening in month N" query is feasible without new data. The work is a new monthly-composition renderer that slices across all the category datasets — real, but not a rewrite.
**Main risk:** Not everything is seasonal. Vehicles, Sources, Property, Recent updates have no natural home on a month axis and would need a separate shelf anyway — meaning B likely has to be *combined with C* (month-first living tier + a reference drawer for the aseasonal cards). That's fine, but it means B isn't standalone.

### Direction D — Bento front for the living tier
**Concept:** Replace the single-column accordion (at least for the living cards) with a composed, asymmetric **bento grid** where tile size encodes importance and seasonality: Weather + This-Month's-Plants get large tiles, quieter modules get small ones. Signal on the tile, drill-down on tap.
**Informed by:** Bento grids; Linear/Datadog signal-then-drill-down; NPS thematic card grid; your own *Typographic hierarchy by value* applied at card scale.
**Honors the identity:** *Only if disciplined.* A warm, asymmetric, serif-headed, journal-voiced grid can work. A tidy grid of equal metric tiles cannot.
**Mom-accessibility read:** **Mixed.** Upside: size-coding communicates hierarchy with zero label-reading, and big tiles are easy targets. Downside: grids tempt small tiles with small labels, and two-across on a phone is the practical ceiling before things get tiny. If pursued: 2 columns max on mobile, size-code aggressively, no tile smaller than a comfortable thumb.
**Implementation weight:** **Medium.** CSS Grid over the existing cards is easy; the harder part is changing the interaction from accordion-expand-in-place to tap-to-open (a detail view or modal), since a grid can't gracefully expand a tile inline.
**Main risk:** ⚠️ **Tone.** Bento is the native visual language of ops dashboards. This direction carries the highest risk of importing the monitoring-panel register your Fernwood principles exist to keep out. If the grid ever starts to feel like a control room, it has failed — no matter how well it solves the density problem.

### Direction E — Seasonal year-wheel as an orienting motif *(additive, not structural)*
**Concept:** A circular year-wheel at the top of the front page showing where "now" sits in the property's annual cycle — a small, beautiful "you are here in the year" device that can *also* deep-link into the month view (Direction B).
**Informed by:** Phenology wheel; circular/perpetual calendars; the analog nature-journal aesthetic.
**Honors the identity:** Very strongly on the visceral/reflective layer — it's the most Sand-County-Almanac object in this whole document.
**Mom-accessibility read:** **Risky as a control** (small radial targets, month labels too small to read without glasses). Safe and lovely as an *ornament that orients* — it tells her "we're deep in summer" by the position of a marker, which she reads by angle, not text.
**Implementation weight:** **Medium** (hand-rolled SVG, some math). Not hard, but real.
**Main risk:** It fails your own *Ornament earns its place* rule if it's pretty but doesn't do navigation work. Decide up front whether it's (a) a functional control into the month view, or (b) an orienting decoration — and if (b), it has to earn its space by genuinely improving the "where are we in the year" read, not just by being charming. Don't ship it as jewelry.

### Direction F — Chat-first almanac: one composer, everything logged, cards demoted *(the big bet on familiarity)*
**Concept:** Collapse the two current actions ("Save" = deterministic AI-free log; "Ask Garden Guru" = AI conversation) into a **single chat-style composer** as the front door. Everything the reader types (or dictates, or photographs) is logged to The Almanac verbatim; the assistant layers a response on top. The 11 cards demote to two things: what the assistant surfaces when asked, and a browse-shelf for deliberate reference. Front door = the surface Mom already operates most fluently.

**Informed by:** Claude/ChatGPT composer-as-home; Perplexity answer-with-sources; the "chat as engine, document as dashboard" frame; Paul's familiarity hypothesis.

**Honors the identity — with real strain.** A field journal *is* a place where you write down what you saw, which a composer models well. But a field journal is also a place of **quiet** — you can note "first trillium open by the spring" and have it simply *be recorded*, not answered. A chat surface's implicit promise is that every message gets a reply. That promise fights the journal's stillness.

**The live design question, worked honestly (the two-button → one-composer tension):**
- **No-AI-on-capture can survive the collapse — *if* built carefully.** The principle is protected as long as the reader's verbatim words are always written deterministically to the store, and the AI reply is a *separate layer on top*, never a rewrite of or precondition for the log. That's architecturally the same guarantee the current "Save" path gives; a one-composer surface can preserve it. So the principle is not an automatic veto.
- **But three real costs come with "every note gets answered":**
  1. **Noise.** If Mom just wants to *log* ("mowed the fairway today"), an AI reply is an uninvited interruption of a quiet act. Every note getting answered can make the journal feel chatty and needy — the opposite of the field-journal calm. What does the app do when she wants to say something to *no one*?
  2. **Cost & latency.** Every logged note becomes a model call — per-note spend and a wait on rural signal, for entries that today are instant and free. On weak property signal, a laggy or failed reply turns a 1-second log into a stall.
  3. **The meaning of silence.** Today, two buttons make intent explicit: Save = "just record this," Ask = "I want an answer." Collapse them and you lose the reader's ability to *say which one they meant*. You'd have to re-introduce that intent some other way (auto-detecting "is this a question?" — which your *Scope is communicated by where you tap, not auto-detected* candidate principle warns against — or a quieter signal like a trailing "?").
- **The most honest reconciliation** is probably not a literal single button, but a **chat-*shaped* composer that keeps a legible two-intent commit** — exactly what the Fernwood principle *Borrow the native composer's field grammar; decline single-send only where a protected intent-split lives* already prescribes. Lead with the familiar hero composer (which delivers ~90% of the "feels like Claude" familiarity win), and keep the twin word-led commit ("Save to journal" / "Ask the Guru") so silence stays meaningful and capture stays free. That captures the familiarity upside while refusing the one move that breaks the journal's quiet.

**Mom-accessibility read:** The strongest *familiarity* argument in the document — she already runs this exact interaction pattern daily on Claude. Two cautions from the telemetry, though: she's a **satisfied one-shot asker**, so a chat-first home optimized for multi-turn conversation would be building for a behavior she doesn't exhibit; and her observed unmet gap is **logging-with-confidence**, which argues the highest-value chat-first work is a *crisp, unmissable "logged ✓" confirmation* on the capture path — not more conversation. Familiarity should be spent on making the *log* feel certain, not on maximizing chat.

**Implementation weight:** **Medium** if it's the chat-shaped-composer reconciliation (you largely have this — it's an evolution of the existing unified input toward a more composer-like skin + demoting cards). **High** if it's a true single-composer rebuild with auto-save-plus-reply on every entry (new cost model, new confirmation model, new home).

**Main risk:** Spending the familiarity dividend in the wrong place — turning a calm seasonal journal into a chatbot that answers things nobody asked, adding cost and latency to the one path (capture) that is currently instant and free, and losing the meaning of silence. The upside is real; the failure mode is a field journal that won't stop talking.

### Direction G — Today-first "look-fors" front page + observation flywheel *(headline recommendation, telemetry-led)*
**Concept:** Give Mom's dominant behavior — the glance — a real home. At the very top, above everything, a small set (2–4) of **specific, seasonal, place-anchored "look-fors"** in field-journal voice: not the whole month's plant list, but *this week's* few things genuinely worth noticing on *this* property, derived from per-plant care calendars (`peakWindow`, `narrow` windows), the season, and on-site weather. Below the look-fors, the **chat composer** (her #1 engagement destination). Below that, the 11 cards demoted to a reference shelf (behind the Direction-C split). Each look-for is phrased as an invitation, and **invites her to report back to Garden Guru** — pull, not push.

Example look-for: *"The first buds may be showing on the smooth hydrangea this week — worth a look."* → tapping it opens the composer pre-warmed to let her tell Guru what she saw → the observation logs to the Almanac.

**The flywheel (why this compounds):** prompt → she looks → she tells Guru what she saw → observation logged deterministically → **future prompts get sharper** ("you noted the first buds on April 25 last year — watch for them now"). Each turn of the loop makes Fernwood's proprietary observation layer (the repo's Phase G direction) richer and the prompts more *this-property-specific* — the opposite of a generic gardening app, and a genuine moat only *this* property's data can build.

**Informed by:** Nature's Notebook (prompt-to-notice → report → long-term record — the flywheel, proven); Seek's "likely near you now" list; Apple Weather's narrative-lead + conditional surfacing (only show what's doing something); national-park "current conditions" card; and Fernwood's own shipped patterns (the 7/2 `suggest-log` fence already logs the reader's verbatim words — the report-back half of the loop is *built*).

**Honors the identity:** Deeply — if and only if the look-fors stay *noticing*, never *tasks*. "Worth a look" not "Prune (due)." This is the exact line the Planta/Gardenize contrast draws, and the line your *Caution as noticing, not warning* and anti-task-manager principles already patrol. Done right, it's the most literal possible expression of "looking out at the land": you open Fernwood and it quietly points at two or three things happening right now.

**Mom-accessibility read:** The strongest fit in the entire document. It serves her measured dominant behavior (glance-and-leave, 51/91 sessions) with a designed surface instead of 11 collapsed headers; it's a *short* read (2–4 items, large type) ideal for half-engagement; and it routes into the composer she already uses most. The report-back also directly addresses her one known gap — logging-with-confidence — by making the log a natural, invited act with a visible "noted ✓."

**Implementation weight:** **Medium.** The report-back machinery exists (the `suggest-log` → verbatim-log → "Noted ✓" path shipped 7/2). The new work is the **look-for generator**: a deterministic function that ranks "what's worth noticing this week" from the per-plant `months[]`/`peakWindow`/`narrow` fields + current date + weather, and phrases 2–4 in journal voice. Keep the *selection* deterministic (capture/surface path stays AI-free); the phrasing can be pre-written per care-event template so no model call is needed for the daily glance. That respects "no AI on the capture path" and keeps the glance instant and free.

**Main risk:** Two. (1) **Register drift** — the moment a look-for reads as a chore ("time to prune"), it becomes the task manager the project forbids; the voice discipline has to hold on every generated line. (2) **Empty weeks** — some weeks genuinely have little happening; the surface must degrade gracefully into a quiet seasonal observation ("a quiet stretch — the ferns are just holding steady") rather than manufacturing urgency or showing an empty box (your *labeled-but-empty section* candidate principle). Silence is allowed; a broken-looking empty slot is not.

---

## 4. What works / what doesn't in the current 11-card stack

### Genuinely good — keep these
- **The single-column, calm, one-thing-at-a-time layout.** Merry Sky and Hello Weather prove this is the *right* instinct for a serene, Mom-legible read. The column is not the problem — don't throw it out chasing a grid.
- **The field-journal voice discipline** across copy, and increasingly across chrome (per your principles library). This is genuinely rare and hard-won. Every direction above must protect it.
- **The "strip teases, card holds" contract** is a sound, already-principled model — the strip earns the tap, the card stands alone.
- **Card icons as identity carriers** (the plant-care lexicon especially). A working visual vocabulary that speaks in the right register.

### Straining — this is where the overwhelm lives
- **The glance — her single most common behavior — has no designed surface.** Measured: 51 of 91 sessions expand zero cards. She's using the collapsed 11-card stack as a status board it was never designed to be, reading 11 headers to do a job the app doesn't actually serve. This is the overwhelm, quantified — and the clearest mandate in the whole review (→ Direction G).
- **Dead weight sits on the daily surface.** Celestial and Recent updates drew 2 expansions each across 35 days, yet occupy the same daily real estate as The Almanac (15) and Plants (7). The telemetry names the reference tier for you.
- **Eleven equal-weight cards = no hierarchy.** Everything is the same width, weight, and tier. Eleven things whispering at the same volume is still a wall of noise. *This is the core problem*, and it's a violation of your own *Typographic hierarchy by value* principle — just applied at the card level instead of the text level. The cards need value-ranking.
- **Reference cards sit at the same tier as living cards.** Sources, Recent updates, Vehicles, Property, Worth considering are consulted occasionally — but they take up the same daily real estate as Weather and Plants, diluting the seasonal read Mom comes for. (This is the split NPS makes and the app doesn't.)
- **No temporal axis.** The app's entire soul is seasonal and cyclical, yet its structure is category-first with time buried *inside* each card. Time — the thing an almanac is *about* — is the missing primary organizing principle.
- **The preview contract only covers 4 of 11 cards.** The teaser strip previews Weather, Plants, Wildlife, Vehicles — so 7 cards (including living ones like Sky & Stars and The Almanac) have no glanceable lead. "Strip teases, card holds" is quietly broken for most of the app; a user has to open a card blind to know if it's worth opening.
- **Scroll depth.** Eleven accordions means the thing Mom wants can be eight scrolls down, with no map of what's below. Vertical distance is friction she pays every visit.

---

## Sources
- [Alan's Almanac](https://alans-almanac.co.uk/)
- [The Old Farmer's Almanac](https://www.almanac.com/) · [Farmers' Almanac](https://www.farmersalmanac.com/)
- [Merlin Bird ID (Cornell Lab)](https://apps.apple.com/us/app/merlin-bird-id-by-cornell-lab/id773457673)
- [Make Your Own Phenology Wheel (Montana Natural History Center)](https://www.montananaturalist.org/blog-post/make-your-own-phenology-wheel/)
- [Apple Weather redesign features (Gadget Hacks)](https://ios.gadgethacks.com/how-to/apples-weather-app-just-got-13-new-features-and-changes-latest-iphone-software-update-0385607/)
- [Merry Sky](https://merrysky.net/)
- [(Not Boring) Weather](https://apps.apple.com/us/app/not-boring-weather/id1531063436)
- [Weawow](https://play.google.com/store/apps/details?id=com.weawow)
- [The Pudding](https://pudding.cool/) · [Responsive scrollytelling (The Pudding)](https://pudding.cool/process/responsive-scrollytelling/)
- [Unigrids (Wikipedia)](https://en.wikipedia.org/wiki/Unigrids) · [NPS goes from paper to pixels (Figma Blog)](https://www.figma.com/blog/made-in-figma-the-national-park-service-goes-from-paper-to-pixels/)
- [Great Smoky Mountains National Park](https://www.nps.gov/grsm/index.htm)
- [Bento Grids gallery](https://bentogrids.com/)
- [The Garden of Maggie Appleton](https://maggieappleton.com/garden/)
- [Claude](https://claude.ai/) · [ChatGPT](https://chatgpt.com/) · [Perplexity](https://www.perplexity.ai/) · [Arc](https://arc.net/)
- ["Chat as engine, document as dashboard" pattern (Medium)](https://medium.com/@tselvaraj/build-a-perplexity-like-user-interface-for-your-private-data-1930bf0f7e72)
- [Nature's Notebook (USA National Phenology Network)](https://www.usanpn.org/nn) · [Seek by iNaturalist](https://www.inaturalist.org/pages/seek_app)
- [Gardenize plant-care app](https://apps.apple.com/us/app/gardenize-plant-care-gardening/id1118448120)
