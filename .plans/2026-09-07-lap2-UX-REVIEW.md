# Lap 2 → lap 3 · UX review of Paul's production walk (F2 · settings · the place card)

- row: C7-R1 (settled by Paul, this review reviews his resolution) · C7-R2 · C7-R3 · 19b · 19c · lap-3 capture F2
- objective: O3 — the engine renders any household (inherited from C7's row; not re-derived here). The card-architecture half also bears on O5.
- kind: review
- seats: `ux-expert`, one seat, one pass. **No walk.** Source read only.
- ready: agent-proposed 2026-09-07 — Paul rules
- gate: ⛔ NOTHING HERE EXECUTES. Every finding is a proposal; nothing is built, nothing is committed, no copy reaching a person is approved. Two findings (F13, F14) **recommend against** work Paul described wanting — they are arguments, not vetoes.

---

## 0 · What I read, and the sha I did NOT read

⚠️ **Read this before quoting a line number.** I read the **working tree** at `~/Developer/Tate-Tracker`. The lap-2 handover records `HEAD → 4a3a61b` and `production → 1e2748d`. **Paul walked `1e2748d`.** So the file I describe already contains the two-defect fix that production does not, and at least one thing he saw on screen (the owner-guard/`isFinite` pair) is not in the code below. Every line number here is against the working tree, not against his walk.

I did not load the live origin. This is a **source review, not a walk** — do not count it toward `release-gate`, `walk-integrity`, or the two-pass `/ux-sweep` clock (a single-seat consult explicitly does not reset that clock, per `CLAUDE.md`).

Files read: `estate/index.html` · `homes/index.html` · `settings/place/index.html` · `settings/account/index.html` · `viewer.html` (jump strip 6535–6542; dash strip 6654–6706; card headers 6711–7044; card expand 7887–7979; `expandCard` 17664–17704; `renderDashboardStrip` 18446–18700; `renderEmptyCards` / `renderAskNext` / `renderHouseholdFirstScreen` 18150–18445; field-note auto-open 20820–20877; jump-strip wiring 22841–22900) · `BACKLOG.md` C7-R1/R2/R3/R5 + rows 19/19b/19c/20 · `.plans/2026-09-07-lap3-paul-feedback-CAPTURE.md` · `.plans/2026-09-07-lap2-CLOSE-HANDOVER.md`.

Principles applied: cross-project `form-and-restraint.md`, `honest-surfaces.md`, `ordering-and-layout.md`; `fernwood.md`; the governing glance/repository principle and standing rules 1–5 in `CLAUDE.md`.

## 1 · User context

| | |
|---|---|
| **primary user** | Paul, as a **first-time household owner** — Grant Park condo, account `pkirsch`, not Fernwood, not administrator. Secondary and binding: **Mom as a cold start** (`[paul-ruled 2026-09-06]` — she meets these screens too), 414 × 848, A+, one-handed, half-engaged. |
| **jobs to be done** | (1) *See that the thing I just told it took.* (2) *Find out whether there is anything here for me yet.* (3) *Change one of the few things I gave it, without re-doing setup.* |
| **context of use** | Phone, evening, minutes after finishing onboarding; the app is near-empty **by design**, and the reader knows it. The reader has entered ~6 values and nothing else exists. |
| **assumptions** | That Paul's walk is representative of an owner's first session (his own report). That the household is placed (coordinates present) for F14 — **capture F5 says his account has none**, so the unplaced branch is the live one for him tonight. |
| **confidence** | **medium.** The owner persona is Paul's own reported walk (strong); the A+/414 conditions and the 0-for-35 ask behaviour are Mom's measured record, imported (`[validated]` for her, `inferred` for a new owner). |

---

# PART A — the Settings surface and the "what you told me" area

Paul: *"pretty bare bones — it would be good for the UX team to look at best practices, how we can make those look a little more clean."*

**The diagnosis first, in one line:** these pages are not under-decorated — they are **unaddressed**. Every one of them opens on a form control with no statement of what the page is about, and the three most prominent typographic elements on each screen are 13px uppercase tracked micro-labels. That combination is what "bare bones" describes. The fix is not ornament; per *Ornament earns its place* and *Content and function first, form follows*, it is to give the page a subject and let type carry the ordering (*Ordering first, then type in service of it*).

---

### F7 · The settings page never names the home it is settings for
**severity: nice-to-have** (→ important the day a second home exists) · **reader: owner, and Mom on a shared device**

`settings/place/index.html:89` — `<h1>Settings</h1>`. The reader leaves a page whose masthead is **"Grant Park Condo"** and arrives at one that says **"Settings"** and could belong to anything. The only thing carrying *which home* is the accent colour — and this page's second card exists to **change that colour**, so the sole identity signal mutates while the reader edits it.

`estate/index.html`'s own comment states the standing job (*VOCABULARY §3b — the top bar always answers "where am I"*). This page breaks it. `settings/account/` does not have the problem: it is honestly titled **"Your account"**, and that asymmetry is the tell.

**Principle**: *Ordering first, then type in service of it* — the h1 is the top of the ordering and it is spending its weight on the least valuable word on the screen. Nielsen #1, visibility of system status.

**Smallest change**: h1 becomes the home's name (already in `fw-onboard-name`, already read at `:164`); "Settings" moves to the utility line beside "‹ Back", which is where it already sits in the reader's mental model because that is the word they tapped. Zero new elements.

---

### F8 · The uppercase micro-labels ARE the "bare bones"
**severity: nice-to-have** · **reader: both, and hardest on the A+ reader**

Four sites, one rule: `settings/place:59` · `settings/account:64` · `estate:123` (`.row .label`) — `font-size:.82rem; letter-spacing:.02em; text-transform:uppercase; color:var(--ink-soft)`.

At 414 × A+ that renders **WHAT YOU CALL THIS HOME · ITS COLOUR · HOW TO REACH YOU · YOUR COLOUR · USERNAME · WHERE IT IS · WHAT I'LL BUILD FIRST** — seven all-caps grey strings across three screens, each the *loudest structural element on its card* and each the *least valuable string on it*. This is F8 from the 2026-05-11 zoom-out review verbatim ("9px uppercase tracked labels read as CMS-admin chrome rather than journal voice"), re-imported onto a new set of pages that were built after the principle was written.

The value beneath each label is 16px regular ink. So the hierarchy is **inverted**: the question is shouting and the reader's own answer is whispering. On the estate card that is worse than a style problem — the whole page is a receipt, and the receipt's subject is her words.

**Principle**: *Ordering first, then type in service of it* (Avoid clause, verbatim: "All caps + tracking on a label whose function is 'quietly name this tile'") + Fernwood *Tone-coherence across all chrome*.

**Smallest change**: drop `text-transform` and `letter-spacing`; label goes to `.92rem`, `--ink-soft`, weight 500, sentence case. The value goes to `1.05rem` ink (the `.value` class on the account page already does this — `:66`). One CSS block per file, no markup. This single change is most of what "look a little more clean" is asking for.

---

### F9 · Colour previews live but saves on Save — the screen shows a state the record does not hold
**severity: important** · **reader: both**

`settings/place:188–194` — tapping a swatch sets `--accent` immediately (correct: the `wide-eyed` seat asked for exactly this). But the write happens only in the Save handler (`:200–225`). So between tap and Save the masthead, the page ground, the hairlines and the swatch ring **all show a colour that is not the reader's colour**. Tap Back and every one of them silently reverts — the reader made a choice, watched it take, and it did not take.

Same shape on `settings/account:178–182`. This is the mildest member of the family this project has already broken twice (*capture must not lie*); it loses a preference rather than words, which is why it is important and not critical.

**Principle**: *Save-success at the surface, not at the destination* (cross-project) + Nielsen #1. Note the file's own good instinct at `:214` — "LOCAL ONLY AFTER THE SERVER HAS IT" — which correctly guards the cache and does not guard the **pixels**.

**Smallest change, and I recommend the cut over the addition**: **a swatch tap saves itself.** It is a single-tap idempotent choice with a live preview and no compose step; it does not need a commit ceremony, and the existing failure line (`#trouble`) covers the POST failing. `Save` then owns only the text field, which genuinely does need a commit. Two commit models on one page is the **platform's own** model (*Prefer the platform's native control over an app reimplementation* — iOS Settings: a picker commits, a text field needs Done), so it borrows familiarity rather than inventing.
*Alternative if Paul wants one commit for the page*: keep Save and make it sticky-at-the-fold once anything changes. That is more chrome for the same outcome; I'd take the cut.

---

### F10 · Two colour pickers, one storage fallback — the account page rings a colour the reader never chose
**severity: important** · **reader: both. This is a re-opened defect.**

`settings/account:154` — `var chosen = read(K_PROFILE) || read("fw-accent")`. The fallback is well-intentioned (its comment: "NO SECOND COLOUR NOBODY CHOSE") and it produces the defect it names, one step later:

1. Reader changes the **home's** colour in place settings → `fw-accent` = Clay.
2. Reader opens **account** settings → "YOUR COLOUR" opens with **Clay ringed and bolded**, `aria-current="true"`.
3. The reader has now been told they chose a personal colour. They chose a *home's* colour. The page states a preference back to them that they never expressed.

That is the exact `mom` seat finding from 2026-09-06 — *"carries its own separate colour picker that I don't recall ever choosing"* — fixed for the Stone default and reintroduced through the fallback. And it is **already ruled on**: BACKLOG row 19c, *"Do not build two colour pickers before answering [which colour wins at an estate] — that is how one concept becomes two forever."*

**Principle**: *A value's provenance and freshness must be shown as honestly as the value itself* (a value inherited from another field, rendered identically to a chosen one, is a provenance lie) + Fernwood standing rule 5's caveat (changeable must be **true**).

**Smallest change**: **cut the account colour picker from pass 1.** At one home it controls the shelf, a surface the reader crosses in under a second, and it manufactures a second colour concept before the precedence rule exists. Row 19c already says not to build it. If Paul wants it kept, the minimum honest version is: no ring, and the note reads "Not set — your homes list uses your home's colour for now."

---

### F11 · Three CTAs on the estate card promise an edit and deliver a note box
**severity: important** · **reader: owner (this is what Paul tapped)**

`estate:373 · 395 · 430` — **"That's not right ›"** · **"Change that ›"** · **"Change the order ›"**. All three call `openFb(r.label)` (`:452`) and open a textarea addressed to Paul. Three different labels, three different promised edits, one message box.

The file knows: `:446` — *"THE EDIT ROUTE IS A NOTE, NOT A TRIP BACK THROUGH THE FLOW."* The reasoning is sound; the **labels never updated to match**. This is the ratified *A CTA's label must promise what the destination actually delivers* — the second-occurrence case that promoted it (a generic "Add to Calendar" over a single-provider URL) is structurally identical.

**And one of the three can now be honest for free.** `/settings/account/` exists and holds contact preference. **"Change that ›" on the "How to reach you" row should be `href="/settings/account/"`.** Row 19c predicted exactly this ("Estate settings is the destination those links were always waiting for") and half the destination has shipped.

**Smallest change**: contact row → link to `/settings/account/`. The other two keep the note box and say what it does — **"Tell me what it should say ›"** — until their destinations exist. One href, two strings.

---

### F12 · "What I'll build first" is the app's voice inside a list of the reader's answers
**severity: nice-to-have** · **reader: both**

`estate:417`. Three consecutive rows read: **Where it is** (about the place) · **How to reach you** (about the reader) · **What I'll build first** (about *us*). Three registers in three rows, in the app's most-trusted playback. It is also a forward promise with no release condition, sitting in a list of settled facts — and the row's own comment already fought this once, adding the "(an idea — not built yet)" marker to individual items because a caveat had gone missing.

**Principle**: Fernwood *Tone-coherence across all chrome* ("Letting a single tile/card use a different voice register than its neighbours").

**Smallest change**: the label becomes the reader's side of it — **"What matters most to you"** — and the derived order is what makes it a receipt rather than an echo (which the file's own comment at `:399` says is the point of the row). The build promise, if wanted, moves to the one line that already carries it: the banner.

---

### What I am NOT proposing for Settings, and why

- **No standing explanatory paragraph on either page.** The 2026-08-04 removal of Mama's Perspective's framing line is the precedent — *"it said the same thing on every visit, which is the definition of furniture."* F7 + F8 give the page a subject **using strings that are already there**. That is the restraint-consistent answer and it is most of the win.
- **No accordions, no sections, no gear glyphs.** The file's own cut-list (`settings/place:20–24`) is right and I would not reopen it.
- **No progress/completeness meter** ("2 of 6 things set up"). It would be an honest number that makes an empty-by-design app read as an unfinished chore.

---

# PART B — the two navigation surfaces (capture F2, BACKLOG C7-R1)

## B0 · Paul's resolution is right, and the code already agrees with him

His resolution — keep the jump strip at the top, collapse the summary menu's intelligence into the cards, re-analyse what a closed card shows — is not a build-from-scratch. **The slot he is asking for already exists and is already dynamic.**

Measured in `viewer.html`:

| layer | what it is | count |
|---|---|---|
| jump strip (`nav.jump-strip`, 6535) | emoji + word, scroll + expand. **No content.** | 6 links |
| dash strip (6654–6706) | label + a multi-row dynamic tease block. Weather renders up to **5 rows**. | 8 cells (6 tier-A + 2 tier-B) |
| card headers (6711+) | icon + title + **`.main-card-summary`** + Open/Close pill | 16 summary elements |

`.main-card-summary` is **already written dynamically** for weather (9364), plants (14423), wildlife (19567), celestial (16875), fishing (`data-record-prose`), turf (15163), weeds (15236), field notes (20711), candidates (15311), release notes (15475), calendar (15545). It is **static furniture** for vehicles (14734), equipment, household systems, reference (6990) and property (7002).

So Paul's "put the intelligence in the cards" is: **delete the middle layer, move five tease blocks into slots that already exist, and decide what the five static ones say.** That is the shape of the work, and it is smaller than it sounds.

---

### F1 · The weather glance is computed twice, by two cascades, into two copies of one slot
**severity: important** · **reader: both** · **this is the strongest argument FOR Paul's collapse**

- **Closed card** (`weather-summary`, 9364): `generateGardenerInsight().observation` + a rounded temperature + an AQI chip appended later (20029).
- **Dash cell** (`dash-weather-sub`, 18469–18526): weather-code glyph + temperature + condition word + H/L + a station-vs-grid 7-day rain figure + up to **3** `generateAlerts()` rows + a "+N more".

Same input set. Same output slot — *"what the weather card says without opening it."* Two independent cascades, and the file's own comment at 9358 names the hazard while creating a second instance of it one screen away: *"The wrong fix is to fork the generator so the header gets its own sentence: that recreates the two-compute-paths bug this card has now hit three times."*

**Principle**: Fernwood **One engine, one verdict**, and specifically its `[paul-ratified 2026-08-02]` sharpening clause — *"The tell is not a shared call — it is a shared INPUT SET plus a shared output slot."* The clause's own occurrence trail names `generateGardenerInsight` vs `generateAlerts` as occurrence 3. **This is occurrence 4 of the same pair, now spanning two surfaces rather than one card.** And the principle states its own remedy for exactly this case: *"If a fourth appears, the answer is not another reconciliation layer — it is that the two functions should have been one."*

**Smallest change**: it is Paul's change. Collapsing the tiles removes the second slot, which removes the second engine by construction rather than by maintenance.

⚠️ **What the collapse must not silently drop.** The dash cell today carries three things the card summary does not: the **station-vs-grid rain figure** (the number Mom disbelieved on 2026-07-26 and was right about, by 14×), the **alerts**, and the **H/L**. If the tiles go and the card summary stays one sentence, that measured-rain line disappears from every closed-state surface. Decide it deliberately (F3 §1 proposes where it lands); do not let it fall out of a deletion.

---

### F2 · Where "what matters today" should live — the question his resolution leaves open
**severity: important** · **reader: both** · **recommendation, not a survey**

Distributing summaries into every collapsed card keeps the **summarising** and drops the **ranking**, because ranking requires a place where items *compete*, and the collapse removes every such place. The capture file lists three candidates. **I recommend none of them**, and two are ruled out by principles already ratified:

- **(a) a state marker / dot on the jump strip — OUT.** Fernwood's *Glyphs follow the journal voice* forbids it by name: *"Ops-dashboard / monitoring glyphs in any surface — traffic-light dots, severity chips, status pills."* A notification dot on a nav item is PagerDuty grammar. It also fails *Icons earn their place* test 2 — a dot says *something* without saying *what*, so it costs a tap to resolve — and at A+ on a 6-item horizontal strip it is the "under 12px, degrades to a coloured speck" case.
- **(b) dynamic card ORDER — OUT, and this one would undo two ratified decisions at once.** Cross-project, `paul-ratified`: ***"A menu's order is a PLACE; a worklist's order is a RANKING — never let one set the other."*** The strip is the index; its tell is "a row that moves when an unrelated item closes." Worse, the strip's order **is Mom's own five categories in her own order** (`[confirmed by her 2026-08-03]`), and page order was reordered *to match the strip* on 2026-08-04 because *"a nav whose order fights the page is disorienting."* Ranking the cards by relevance breaks the strip↔page correspondence **and** reorders her list — which that same comment calls "the same act as rewording 'household systems'."
- **(c) accept the loss — honest, and it costs the thing Paul called the layer's whole purpose.** Thirteen closed cards each carrying a line is a *scan*, not a *read*, and it fails Fernwood's *Make every surface read at half-engagement* (the essential read in 1.5 seconds).

**⭐ My recommendation — (d): one synthesis LINE where the tile grid is today.**

One or two sentences directly under the jump strip, naming only what is **unusual today**, each phrase linked to the card that holds it. Not a menu. Not a marker. Not an order. One or two lines where nine tiles are now.

Why this one:

1. **It is the ratified principle for exactly this surface.** *Lead with the synthesis, not the rows* — "state the conclusion the surface already computes at the top, as its own layer above the detail, rather than leaving the reader to re-assemble the gestalt from the rows." The dash strip is the textbook anti-pattern that principle names: it compresses rows spatially and calls the result a synthesis. Paul's instinct (*"highlights the most relevant information"*) **is** that principle; it was implemented as tiles.
2. **The index stays an index.** Strip order never moves, so the ratified menu/worklist rule holds and Mom's measured strip-first navigation is untouched.
3. **The mechanism already exists and is already ratified.** `MOM_ACK_DATA.links = [{phrase, card}]` — many phrases, each linked to where the reader can see it, *and a phrase no longer in the message is skipped rather than rendered as a dead control* (standing rule 2). That is precisely the behaviour a ranking line needs. **Reuse the vocabulary before adding a state.**
4. **It satisfies the governing empty ruling natively.** A day with nothing notable renders **no line at all** — a sentence can be absent; a tile grid can only leave a hole.
5. **It restores exactly one place where things compete**, at the smallest size the product can spend.

**Constraints on it, and they are load-bearing:**
- ⛔ **Cap at 2 phrases.** The alerts array already does 3-plus-"+N more"; that is a list, not a synthesis.
- ⛔ **Every phrase is a PROJECTION of a card's own summary resolver, never a new claim** — or F1 is re-created at a third altitude.
- ⛔ It reaches a person, so the copy is **human-confirmed before it ships** (AI boundary: authored content).
- ⚠️ It must not become a fourth layer. The falsifier: *if the line ever says something no card summary says, it has become a fifth engine.*

---

### F3 · What a CLOSED card should display, per card type
**severity: important** · **reader: both**

One grammar for every card, three slots, no exceptions:

**`[identity square] [Title] · [state line] · [Open]`**

The state line is **one line**, written by the card's **own** resolver, and the rules go by card type:

**1 · Live / measured domains — Weather, Fishing, Sky.**
The current verdict in the domain's own words, with the measured value leading and the modelled word following in the same sentence (*Source-hierarchy drives layout*; *keep measured signals visually distinct from modelled ones*). One line. Everything the dash cell renders in five rows moves inside — the card is one tap away and *the card holds* (**Strip teases, card holds**; with the strip gone, that principle's "tease" job transfers to the closed header and its "card is self-contained" clause is unchanged).
*Weather is the one card permitted a second line, and only when an alert exists, and only the highest-ranked one.* The station-vs-grid rain figure belongs **inside** the card, at the top of the open body, beside the rest of the rainfall panel — that is where it can carry its own provenance, which a one-line header cannot.

**2 · Seasonal / roster domains — Plants, Wildlife, Weeds, Turf, Insects.**
Name **what changed or what is at peak**, never a census. *"Three at their peak — hydrangea, deutzia, clematis"*, not *"0 plants · a quiet Sep here."* If nothing is at peak, the month's character (*"Pruning and inspecting this September"*). If neither is true, **no line.**

**3 · Reference / holding domains — Vehicles, Equipment, Household Systems, Reference, Property.**
These are the third of the card set Paul's resolution leaves genuinely open, and today they carry static prose (*"The machines we keep — and what each one needs"*, *"The back pages — specs, sources, and records"*, *"Land · Sky · History"*) which says the same thing on every visit — the 2026-08-04 definition of furniture. Two honest options; **I recommend the second where it is available**:
  - (i) **No line.** Title only. Honest, and the card still reads as a door.
  - (ii) **The domain's most recent dated CHANGE** — *"Last touched: Bolores, RetroSound, Aug 9"* — derived from `serviceHistory` (which already carries stable `id`s and dates). It is dynamic, true, and it is the **only** thing about a reference card that can ever be new.
  Recommend (ii) where a dated record exists, (i) where it does not. Never both, never static prose.

**4 · The reader's own domain — Almanac / Field notes.** Count + newest. It already does this (20718). Keep — this is the one card where a count *is* the read.

**5 · Empty modules.** Already ruled: hidden entirely for a household (18265). Keep. But **the implementation carries two vocabularies for one state in one function**: 18287 writes `"Nothing here yet."` onto the face, 18240 blanks it for the reader's #1. Under the ruling, normalise to **absence** — *"Nothing here yet."* is a line whose content is that there is no line.

**6 · The unplaced place card.** See F14; it is currently force-open (route 5 in F5), which is the app conceding its closed line cannot carry the message.

**The rule underneath all six, stated once:**
> A closed card's line is written by that card's own resolver. **A resolver with nothing to say returns null, and a null renders no element** — not a dash, not an ellipsis, not a placeholder, not "Nothing here yet."

---

### F4 · Loading is not empty — the one place I argue against a literal reading of the ruling
**severity: important** · **reader: both**

`renderUnplacedSummaries()` (18380) rewrites **every** `.summary-loading` to `"Nothing here yet."` — deliberately, and for a good reason the `owner` seat found (five present-tense ellipses beside honest dashes tipped the page from *new* to *failed to load*).

But that normalisation runs the wrong way under the new grammar. **A card still fetching and a card with nothing to say are different states, and the reader acts on them differently** — the estate page learned this exact lesson three weeks ago and encoded it (`estate:464` — *"THREE EMPTY STATES, NOT ONE"*: no credential · fetching · genuinely empty).

**Recommendation**: the empty rule gets exactly one carve-out. **Absence** for nothing-to-say; **a stated line** for fetching; and the two must never render the same. The `!SITE_PLACED` case that motivated `renderUnplacedSummaries` is not "loading" at all — it is *permanently* nothing-to-say, so under the new rule it correctly becomes **absence**, and the function goes away rather than growing.

---

### F5 · ⚠️ THE ROUTES — enumerated, because a zero here has already produced a wrong finding
**severity: important** · **reader: whoever reads the next telemetry number**

Every writer of `.expanded` on a `.main-card`, measured in the working tree:

| # | site | route | tracks `card_expanded`? | calls `syncCardHeaderState`? |
|---|---|---|---|---|
| 1 | `toggle()` 7965 | header click + Enter/Space | ✅ `via:"header"` | ✅ |
| 2 | `expandCard()` 17688 | see call sites below | ✅ `via:<source>` | ✅ |
| 3 | `renderEmptyCards()` **18239** | auto-opens the reader's **#1 ranked empty module**, every load | ❌ | ❌ |
| 4 | `renderAskNext()` **18193** | card born `class="main-card ask-next expanded"` | ❌ | ❌ |
| 5 | `renderHouseholdFirstScreen()` **18430** | auto-opens the **place card** when `!SITE_PLACED`, every load | ❌ | ❌ |
| 6 | `fnSaveInlineEntry` 20826 | auto-opens field notes on save | ❌ | ✅ |
| 7 | `fnSaveObservationOnPlant` 20871 | auto-opens field notes on save | ❌ | ✅ |

Plus a **different component** that shares the class name: `.plant` rows (14725 → CSS 2270/2273), toggled by their own header handler, no telemetry.

`expandCard` call sites, measured: **13** — 8 dash cells (6657 · 6661 · 6665 · 6669 · 6673 · 6685 · 6697 · 6701) · 3 ack-ribbon links (12500 · 12529 · 12603) · 1 Almanac history link (17735) · 1 jump-strip handler (22874, dynamic over 6 anchors). Counting the strip's anchors individually, that is **18 distinct user-facing routes** through `expandCard`.

**Three things follow, and all three bear on lap 3:**

1. **`viewer.html:7891` is stale.** It says *"`.expanded` is added in four places"* and it is **seven**; 17669 says *"14 call sites"* and I count **13**. Both comments were true when written and three later writers did not update them. This is the same shape as the defect the 2026-08-14 fix closed — an exhaustive claim in a comment that nothing enforces.
2. **Two of the three new writers skip `syncCardHeaderState`**, which is the one thing 7890 exists to prevent. So on the reader's **#1 ranked card** (route 3) and a household's **place card** (route 5), the pill reads **"Open"** on a card that is already open — *a control that misreports its own state*, which the comment itself calls "worse than the unlabelled chevron it replaced."
3. **⭐ Two cards have no closed state to design.** Routes 3 and 5 force those cards open at first paint, on every load, for exactly the reader Paul is designing for. **A household's place card is never seen closed.** So the "what does a closed card show" work must first rule on whether force-open survives — and if it does, those two cards need their **open first line** designed instead, which is a different question.

⛔ **Standing constraint for anything downstream:** any claim about open/closed behaviour must name which of the seven routes it counted. Only routes 1 and 2 emit `card_expanded`; routes 3–7 open cards silently, and routes 3 and 5 fire without a tap, so they can never appear in an open-rate denominator at all.

*Footnote, not a finding: `renderAskNext()` (18183) returns at `:18186` for a household and at `:18188` for everything else, so as written it can never build its card. Route 4 is presently unreachable. Flagging so nobody counts an ask-next card in the household's card inventory; the fix is an engineering call, not mine.*

---

### F6 · The one tile row that cannot move into a card header
**severity: important** · **reader: both** · **the highest-risk item in Paul's resolution**

`dash-plants-sub` (18538–18589) renders a **"Worth a look"** prompt whose tap is wired by `wirePlantCheckPrompt` to the **composer**, not to the card — deliberately (`:18535`, Paul's call 2026-07-14). It is the only dash-cell row whose tap does something a card summary cannot do, and it is the **loop's invitation** — strand 3 of the governing glance/repository principle, the flywheel, the thing that makes the glance an exchange rather than an extraction.

It cannot survive as-is inside a `.main-card-header`, because that header's whole job is one thing: open the card. A nested tap target with a different destination inside a header that is itself a `role="button"` is an affordance collision and an accessibility one.

**Smallest change**: **split it.** The closed card's line *states* it, flatly and without a control — *"Worth a look · the clematis"*. The **tap-to-note** affordance moves to the first row of the **open** plants card body, where the composer route makes sense and where a second target is legal. One target per closed header is what makes the whole collapse safe.

---

### F15 · Five vocabularies for "nothing on this card's face"
**severity: important** · **reader: both**

Measured on one screen today: `—` (6771 · 6785 · 6799) · `"Nothing here yet."` (18287 · 18382) · `"Listening for the station…"` (6659 · 6716) · `"Getting the weather…"` (9370 · 18459) · `""` (18240). Five strings, one meaning-space, and the `owner` seat already reported that the mix is what tipped the page from *new* to *broken*.

The card-collapse work is the moment to settle it, because it touches every one of these sites anyway.

**Smallest change**: three states and three only, per F3 + F4 — **absence** (nothing to say) · **one fetching line, identical everywhere** (still coming) · **the real line**. Enforceable as a walk assertion: *no `.main-card-summary` renders a bare dash, an empty string, or more than one distinct fetching string per build.*

---

# PART C — the place card and the promise (capture F3 + F4)

### F13 · The ribbon + "OK sounds good" **relocates the promise** — recommend against
**severity: important** · **reader: both, and it spends Mom's one learned grammar** · **this is a recommend-against, not a veto**

Paul's (4) asks whether the acknowledgment-ribbon + feedback-box pattern should carry *"we're working out your weather and what grows here from the address you gave me,"* with a lightweight "OK sounds good."

**It relocates the promise, and it pays for the move with the ribbon's credibility.** Three grounds, all from rulings already made:

1. **The ribbon's ratified job is ATTRIBUTION, not information** `[paul-stated 2026-08-04]`: *"we DO have a changelog / release notes elsewhere in the app. So this card is about we heard you — we actioned these things because of you."* Two of that ruling's three binding consequences are violated head-on. Consequence 2: *"Every line traces to something she gave. A change she did not cause does not belong on this card."* A line saying *we are still working on your weather* traces to nothing she gave and names no change. Consequence 1: *"It refreshes on HER events, never on ours. It goes quiet when she does."* A promise-in-progress refreshes on **our** cadence — which that ruling names, verbatim, as the failure mode: *"a changelog wearing the ribbon's clothes."*
2. **The "OK sounds good" ack makes it worse, not lighter.** The measured record: **0 of 10** on the acknowledgment ribbon, **0 of 35** on confirm cards, **0** on the look-for prompt, against **5 of 5** on the affordance that simply moves her. This would be an eleventh ask whose entire payload is *acknowledge that we have not done something yet* — it gives nothing and asks for a tap. Fernwood candidate, *Give before you ask — a surface that only extracts gets ignored.* And a tapped "OK sounds good" is a **recorded consent to wait with no release condition**, which is the risk Paul's own reframing already carries a warning about in the lap-2 handover.
3. **The promise does not need a better container. It needs to stop being a promise.** The handover records the delivery state exactly: the weather half is **delivered and verified**; the "what grows there" half is delivered to **nobody** — frost date, zone, growing season all zero across 7 runs, *"no surface behind the door, not even an empty one."* Wrapping a half-true sentence in a more trusted container does not change its truth value; it raises the price of it being false.

---

### F14 · Replace the promise with a receipt, delete the undeliverable half, and let the card carry what the address actually yields
**severity: important** · **reader: owner (Paul tonight), and Mom at her condo)**

The live sentence, `viewer.html:18428`: *"We're working out your weather and what grows here from this address — it lands on this card as it comes in."*

**Split it by delivery, and drop the half that has none.**

- **The weather half is delivered.** For a placed household there is a 7-day forecast, an hourly strip, a rainfall panel and eight dated sky events — the handover says the door card was *underselling* exactly this. So say it in the **past tense, as a fact**: *"Weather and sky are already in, from this address."* That is a receipt. The estate door card already learned this move (`estate:324`) and the app card has not caught up.
- **The "what grows here" half has no delivery, so it does not appear at all.** This is the governing ruling — *better to not display something than display something that's empty* — applied to a **sentence** rather than a container. A promise with no delivery is the emptiest thing on a screen, and it is worse than an empty box because a box does not ask to be believed.
- **Then Paul's (3) is the content answer.** The card should be about **what the address yields**: town and county, elevation, sunrise/sunset, the weather it already has, and — later — the neighbourhood and what is on locally. ⚠️ Two things bound the "later": **C7-R5** records that the events block already renders **Pickens-County events at the condo** and sits at the *bottom* of the location card, violating freshness-sets-altitude; and the capture file records that the condo's outward-facing family (events, neighbourhood) is *"captured, not built — a new ingestion class and a third path through the AI boundary that needs a ruling first."* So the honest interim is: **the card carries what geocoding already returned, and no forward claim.** Events wait for the ruling; they do not get pre-announced.
- **If a "we're building this" line is wanted anywhere**, it belongs in **Recent updates / release notes** — the surface whose ratified job it is, and the very surface the 08-04 ribbon ruling cites as the reason the ribbon must not do it.
- ⚠️ **A box-number household is a separate branch and is already right** (`:18426`) — it says plainly what cannot be done. Do not fold it into the placed copy.

**Falsifier for F13 + F14 together**: *no surface in the product states a future capability with no delivery date.* A sentence that fails it either moves to the past tense or is deleted.

---

## Open questions for Paul

1. **Does force-open survive?** Routes 3 and 5 (F5) mean the reader's #1 card and the household place card are never seen closed. If they stay force-open, they need their **open** first line designed, not their closed one.
2. **F3 §3** — for Vehicles / Equipment / Household Systems / Reference / Property: **no line**, or **last dated change**? I recommend last-dated-change where a record exists.
3. **Colour precedence** (row 19c) is still unruled, and F10's fix is a cut that presumes the answer is "later." Confirm the cut, or rule the precedence.
4. **The synthesis line (F2 §d)** — 1 phrase or 2? And does it live above the cards permanently, or only when it has something to say? (I recommend: only when it has something.)
5. **Is the 7-day station rain figure allowed to leave the closed-state surfaces entirely** (F1 ⚠️)? It is the number Mom disbelieved and was right about.

## Follow-up research suggested

- Once the tiles are gone, the strip's `jumpstrip_viewed` denominator changes meaning — the strip becomes the *only* thing above the cards. Re-baseline before any strip-usage claim. ⚠️ And the capture file's own warning stands: `MOM-CYCLE-LOG.md:1816` vs `:1115` may be a live contradiction; the 100%-by-strip figure is **not quotable** until re-measured.
- A one-question read for Mom, if a card ever surfaces one: *does the closed line tell you enough to decide whether to open it?* That is the only success test for the whole F3 grammar.

## Principles proposed — ⚠️ NOT filed, Paul words them or they die

Per standing rule: one occurrence = candidate; nothing enters the library without his wording.

1. **`[cross-project candidate]` Distributing a synthesis destroys its ranking.**
   *Statement*: pushing a summary down into the things it summarised keeps the summarising and loses the ranking, because ranking needs a place where items compete. If ranking mattered, preserve exactly one such place — as small as it can be, and derived from the same engines as the distributed summaries.
   *Why*: Fernwood lap 3 — the resolution that correctly removes a redundant middle layer also silently removes the only surface where "what matters today" could exist. Sharpens *Lead with the synthesis, not the rows* from "put the conclusion on top" to "and do not let a de-duplication pass delete it."

2. **`[cross-project candidate]` A promise with no delivery does not get to borrow a receipt's credibility.**
   *Statement*: a surface whose job is to confirm what happened may not carry a forward-looking claim. Move the claim to the changelog, put it in the past tense, or delete it — never re-house it somewhere more trusted.
   *Why*: F13. Generalises the 2026-08-04 ribbon ruling from *this ribbon* to *any receipt surface*.

3. **`[fernwood candidate]` A closed card's line is written by its own resolver; a resolver with nothing to say returns null.**
   *Statement*: null renders no element. Absence, one fetching line, or the real line — three states, never a dash, an empty string or a placeholder. The one carve-out is that fetching and nothing-to-say must never print the same.
   *Why*: F3 + F4 + F15 — operationalises Paul's already-made empty ruling, and adds the loading distinction the ruling does not carry.
