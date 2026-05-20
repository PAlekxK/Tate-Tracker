# Unified Input Surface — Path Evaluation

**Date:** 2026-05-20
**Subject:** Engineering path-eval for the Q10 unified-input UX redesign — replace the two-card composer layout (Quick Capture `#quick-capture` + Garden Guru `#garden-guru`) with a single minimalist textbox + two explicit-path buttons ("Record an observation" / "Ask Garden Guru"), positioned beneath the 6 main dashboard cards.
**Reviewer mode:** path-evaluation
**Scope:** Engineering lane only. ux-expert is running the parallel UX path-eval. This eval owns code, cost, complexity, deploy/rollback. UX semantics — what the surface should look like, what the empty state says, where it should sit visually — is ux-expert's lane; this eval calls out where engineering touches UX decisions but doesn't try to make them.

---

## Context recap (load-bearing — informs every recommendation below)

- **The two existing surfaces.** `#quick-capture` at `viewer.html:2748-2759` (Field Notes inline composer — textarea + mic + Save). `#garden-guru` at `viewer.html:2761-2777` (Garden Guru composer + inline conversation history — counter, conversation div, textarea + mic + reset + ask). Both sit *above* the 6 main cards (Weather, Plants, Wildlife, Sky & Stars, Fernwood, Vehicles + the Field Notes browse card at position 6 between Fernwood and Vehicles — that's actually 7 main cards, not 6, post-Phase B).
- **Composer mechanics are already factored.** `createVoiceCapture({textareaId, micBtnId, hintId})` factory at `viewer.html:8630-8739` is the *only* meaningful piece of code currently shared between the two surfaces. Two instances exist: `VoiceCapture` (FN, line 8741) and `GuruVoice` (GG, line 8747). Nothing else is factored — the save handler `fnSaveInlineEntry()` and the ask handler `GardenGuru.ask()` are unrelated code paths.
- **Two state owners.** `ObservationStore` (IIFE at 8233-8365) owns observations + sync config + status. `GardenGuru` (IIFE at 8820-8884) owns `conversationId`, `turns`, `isWaiting`, listeners. Both expose `onChange()`. Neither knows about the other.
- **Render contracts.** `renderFieldNotes()` (8450) writes to `#fieldnotes-body` (inside the FN main card). `renderGardenGuru()` (8924) writes inside `#garden-guru` itself — the GG card *is* both composer and history view. There's no `renderGardenGuruHistory()` separate from the composer; they're one block.
- **Where layouts live.** Card order is purely DOM order under `.content-wrap` (2746). No layout system, no grid container around the cards, no template loop. To move the composers beneath the cards = literal cut-and-paste of `<section>` blocks in viewer.html.
- **Wiring posture.** Both composers are static markup, wired once in IIFEs (`wireFieldNotes` 8754, `wireGardenGuru` 8983). They're never re-rendered or replaced — only their inner state/textareas update. That's a feature: it means moving the surface around the DOM doesn't break the wiring as long as IDs stay stable.
- **Data on disk.** Observations live in `localStorage["tateTracker.observations.v1"]` + Worker KV (via `ObservationStore`). Conversations live in Worker KV under `conversation:<uuid>` keys (see `worker.js:387`). Neither set of data is touched by the markup we're replacing — the data layer is independent.
- **Calibration.** Family-internal, Mom-as-make-or-break, Phase E shipped 24h ago, the only smoke test that's happened is Paul's. This is the largest UX change since Phase E, and Phase E itself is unproven. That informs the deploy posture below — heavily.
- **Cross-cutting principle observed.** [[Capture path stays pure; batch and amortize]] (fernwood.md, 2026-05-20). The capture button must NOT trigger a Claude call. The "Record an observation" path is pure-text log, classify-on-save is being removed per the no-AI-on-capture pivot (CLAUDE.md note on Phase D pivot). The Ask path is the only one that triggers `/api/chat`. Two buttons = two intent surfaces = the principle holds.

---

## TL;DR recommendation

**Path C (Hybrid: hide the two existing composers, keep both cards, add a unified entry surface as the sole composer).** Position it beneath the 6 main cards as the proposal stipulates. Feature-flag it via `localStorage["tateTracker.ui.unifiedInput.v1"]` so Paul can toggle on his devices while Mom continues to see the shipped layout until Paul has confidence.

**The bet:** the *expensive* parts of the current code (`ObservationStore`, `GardenGuru` state machine, `createVoiceCapture` factory, `fnSaveInlineEntry`, `GardenGuru.ask`, `renderFieldNotes`, `renderGardenGuru`) are exactly the parts that should NOT be rebuilt. They're load-bearing, tested in deployment, and own non-trivial state. The *cheap* parts (two `<section>` blocks of static markup, the wiring IIFEs that bind IDs to handlers) are the parts that need to change. Path C preserves the expensive code unchanged and isolates the change to markup + a thin router that translates "user clicked Record" → `fnSaveInlineEntry()` and "user clicked Ask" → `GardenGuru.ask(text)`.

**Strongest reason for it:** zero migration risk on observation/conversation data. Both stores keep working unchanged. If Path C ships and breaks, the rollback is a single feature-flag flip — the old surfaces still render correctly because we didn't tear them out.

**Strongest argument against it:** the Garden Guru conversation history needs *somewhere* to render, and the cleanest place is still the GG card body, which means the GG card stays visible above the 6 cards (or wherever it ends up post-relocation). The unified surface beneath the cards becomes the entry point, but the conversation reply renders into the existing `#gg-conversation` div elsewhere on the page. That's a real cognitive split — the user types beneath the cards, the reply appears in a card above. ux-expert should weigh in on whether that split is OK or whether we need to relocate the reply rendering too. (Engineering-side cost of relocating the reply: low-medium — see Section 5.)

**Cost:** ~1 evening of focused work for Path C. ~2-3 evenings for Path A. Feature flag adds ~30 min.

**Deploy:** ship behind a localStorage feature flag, toggle on Paul's devices, leave Mom on the current layout for at least 2 weeks of side-by-side, then promote to default once Paul has confidence and the metrics-capture instrument is live to validate Mom's behavior on the new surface.

Why not the alternatives:

- **Path A (full rebuild)** — the most "honest" architecturally, but the cost is high and the gain over Path C is mostly aesthetic. Rebuilding `ObservationStore`-equivalent and `GardenGuru`-equivalent inside a unified composer object means re-deriving the cap-tracking, the optimistic-write pattern, the sync status reporting, and the conversation-listener wiring. That code already works. Re-deriving it is exactly the kind of churn that introduces bugs in things that aren't actually broken.
- **Path B (wrapper consolidation, keep both composers + add a third)** — two composers means two text states means duplication-of-truth on pending input. The proposal explicitly removes the two-card layout; Path B keeps it. Doesn't match the UX intent.
- **Path D (composer factory: one composer object, two instances)** — surfaced below. Worth knowing about as a "graduation path" — if Path C ships and the unified surface proves it carries weight, the right next move is to extract a `createComposer({mode, onSubmit, ...})` factory that subsumes both surfaces. But not as v1. AHA-aligned — duplication is fine until the abstraction proves itself.

Detailed comparison below.

---

## Section 1 — The realistic paths

### Path A: Full rebuild

**What it is.** Tear out `#quick-capture` (2748-2759) and `#garden-guru` (2761-2777) markup. Tear out `fnSaveInlineEntry()` (8532), `renderGardenGuru()` (8924), `wireFieldNotes` IIFE (8754), `wireGardenGuru` IIFE (8983), and the inline conversation-history rendering inside `#garden-guru`. Build a new `UnifiedComposer` module from scratch. Decide where the conversation history renders (probably a new `#gg-history` div, possibly inside what was the Field Notes main card body or as a sibling above the unified composer). Decide where the FN list of past observations renders (probably stays in the Field Notes main card, unchanged).

The two existing main cards (`#card-fieldnotes` at 2931, no separate GG card — GG is a `<section>` not a `.main-card`) still exist for their *display* role:
- Field Notes card shows the list of saved observations (unchanged).
- ...but Garden Guru *doesn't have a main card today*. It's a `<section class="garden-guru">` that owns both the composer and the conversation history. Tearing it out means deciding what becomes of `#gg-conversation` — does it go into a new card? Stay inline somewhere?

**Files touched.** `viewer.html` only (the single-file constraint holds — no other code knows about these surfaces). Markup: 2748-2777 deleted, new unified composer inserted post-cards (post-`#card-vehicles` ending ~3000). JS: 8528-8573 (save), 8741-8784 (wiring + voice instances for FN), 8815-9015 (entire GardenGuru module + render + wire) all rewritten or substantially edited. Net: ~250 lines of rebuild work in one file.

**Trade-off:**

| Dimension | Read |
|---|---|
| Complexity | High. Re-derives state machines that already work. |
| Code touched | ~300 lines refactored/rewritten across 4 distinct modules. |
| Framework-idiom | Neutral — the existing pattern is "static markup + IIFE wires once + IIFE updates DOM." A rebuild would use the same pattern, just composed differently. |
| Future-features extensibility | High *if* designed for a third intent (image upload for Phase F, or "Save to research library"). But you're paying for that extensibility before you know if you need it. |
| Future-Paul-with-Claude maintainability | Lower than expected. The current code is two clearly-named modules with separate concerns. A unified module that *internally* routes by intent is denser; Claude has to navigate one big module instead of two small ones. AHA-aligned this isn't a win. |
| Learning value | Moderate. Re-deriving the state shape teaches the shape; but Paul already learned it building Phase D and E. |
| Deployment risk | High. Touching `GardenGuru` state machine is touching the thing Phase E just shipped. Same week — too soon. |
| Cost | ~2-3 focused evenings. |

**When you'd pick this anyway:** if the rebuild lets you cleanly add Phase F (image input) at the same time. Image upload is genuinely a third intent (not "ask" or "capture" but "ask-with-image" or "capture-with-image"), and a from-scratch composer can model that without retrofitting two surfaces. *But Phase F is benched, and re-benching the rebuild on Phase F's strategic decision is putting the cart before the horse.*

### Path B: Wrapper consolidation (keep two existing composers, add a third unified entry)

**What it is.** Don't touch `#quick-capture` or `#garden-guru`. Add a new `<section id="unified-input">` beneath `#card-vehicles`. Its two buttons route input to the existing handlers — "Record" stuffs text into `#fn-capture-textarea` and clicks `#fn-capture-save`; "Ask" stuffs text into `#gg-textarea` and clicks `#gg-ask-btn`.

**Verdict: don't.** The proposal explicitly replaces the two-card layout; Path B keeps it. Two composers visible at once means two textareas with potentially different content, two mics, two sources of state-of-truth for pending input. Either you hide the old composers (which is Path C, not Path B) or you don't (which is incoherent with the UX proposal).

Naming it here so it's not silently missing from the option space. Don't pick it.

### Path C: Hybrid (hide the two existing composers, route to existing handlers, keep the cards)

**What it is.** Two changes only:

1. **Markup.** Add `<section id="unified-input">` beneath `#card-vehicles` (~viewer.html line 3000-ish, the bottom of the cards stack). Hide `#quick-capture` and `#garden-guru` via `.unified-input-active` body class controlled by the feature flag.

2. **Routing.** A thin `UnifiedInput` IIFE that owns the new surface's textarea + mic + two buttons + intent state ("idle" / "leaning-capture" / "leaning-ask"). On Record click, it copies the text into `#fn-capture-textarea` and calls `fnSaveInlineEntry()`. On Ask click, it copies the text into `#gg-textarea` and calls `GardenGuru.ask(text)`. The existing handlers do the rest unchanged.

The Field Notes main card still renders the list of saved observations (unchanged). The Garden Guru conversation history *still renders inside `#garden-guru`* — but `#garden-guru` is now hidden by the feature flag, which is a problem.

**Resolving the GG history problem.** Three sub-options (this is the real engineering decision inside Path C):

- **C1:** Leave `#garden-guru` visible but strip its composer (hide just the input row + buttons; show only the header counter + conversation history). The card becomes a *read-only conversation display* above the cards.
- **C2:** Hide `#garden-guru` entirely and re-host `#gg-conversation` *inside* the new unified-input section below the cards. Reply appears immediately above the input row. This is the cleanest UX — type, ask, reply appears right there.
- **C3:** Hide `#garden-guru` entirely and re-host `#gg-conversation` inside a *new* `.main-card` for Garden Guru between Fernwood and Field Notes. Conversation history gets a proper main-card home, expand/collapse like the other cards.

**Recommended: C2.** It's the closest to the proposal's intent (one surface, one mental model, reply lands next to the input). Cost: low — `renderGardenGuru()` already targets `#gg-conversation` by ID; you just need to move that `<div>` to a new location in the DOM. The renderer doesn't care where the div lives.

**Files touched.** `viewer.html` only.

- Markup additions (~50 new lines): the unified-input section + CSS.
- Markup edits: `#garden-guru` wrapped in feature-flagged hidden state (~5 lines).
- New JS module `UnifiedInput` (~80 lines): textarea + mic (via existing `createVoiceCapture` factory) + two buttons + intent state + dispatch.
- Existing modules: zero edits to `ObservationStore`, `GardenGuru`, `fnSaveInlineEntry`, `renderGardenGuru`, `renderFieldNotes`. The two existing wiring IIFEs (`wireFieldNotes`, `wireGardenGuru`) keep running but bind to elements that are now `display: none` — harmless.

**Trade-off:**

| Dimension | Read |
|---|---|
| Complexity | Low-moderate. New module + flag, no state-machine rewrites. |
| Code touched | ~150 lines added, ~10 lines edited. Existing modules untouched. |
| Framework-idiom | Matches the project's pattern exactly — static markup + IIFE wires once + ID-keyed updates. |
| Future-features extensibility | Lower than Path A. Adding Phase F image upload still requires either extending the existing GG composer (which is hidden but functional) OR teaching `UnifiedInput` about a third intent. Either is fine. |
| Future-Paul-with-Claude maintainability | Higher than Path A. Two clear modules + a thin router; Claude can navigate "find where Record-an-observation does its work" in one hop (`UnifiedInput.onRecord` → `fnSaveInlineEntry`). |
| Learning value | Lower than Path A but more honest — teaches the pattern Paul will use repeatedly: "introduce a new surface that delegates to existing handlers, don't rebuild handlers." |
| Deployment risk | Low. Feature flag means a rollback is a localStorage flip. Existing surfaces still wire correctly even when hidden. |
| Cost | ~1 focused evening, plus ~30 min for the flag, plus iteration time on layout/CSS. |

**The argument against C** I want to name plainly: it's a *layered* solution, not a *clean* one. You're shipping a UI that delegates to two underlying modules but pretends to be one. If the UX proposal stabilizes and the unified surface proves it carries weight permanently, Path C is the kind of architecture you eventually want to consolidate into Path A or Path D anyway. Path C is "the right v1, with a clear graduation path." That's a feature, not a bug, at hobbyist stakes — but worth being honest about.

### Path D: Composer factory (extracted shared module, single source of truth for composer mechanics)

**What it is.** Extract a `createComposer({mode, placeholder, onSubmit, voiceId, ...})` factory that builds a textarea + mic + submit button as a reusable unit. Use it twice: once for the unified surface, once for any future surface (chat reply textarea, image upload form, anything). The two existing composers also get refactored to use it, eventually.

**Verdict: don't ship this as v1.** This is the Path A endgame plus the AHA principle violation. You'd be writing the abstraction before you have a third call site that proves the abstraction. The current `createVoiceCapture` factory is already the "shared piece worth sharing" — voice dictation is genuinely the same across surfaces. The rest of the composer (textarea styles, submit button shape, intent state) is plausibly different per surface and hasn't proven it wants consolidation yet.

**When you'd pick this:** after Path C ships and a *fourth* composer-shaped surface appears (image upload form, research-library save dialog, anything). Then the factory pays for itself. Until then, pre-factoring is the wrong move.

Naming this path so it's not silently absent — and so the graduation story is explicit. Path C now; Path D someday; never Path A unless Phase F changes the calculus.

---

## Section 2 — Relocating the surface beneath the 6 cards

**Cheap.** The cards are sibling `<div class="main-card">` elements under `.content-wrap` (viewer.html:2746). There's no grid container, no template loop, no order-controlled-by-JS. To put the unified input below the cards, you put the `<section id="unified-input">` after `</div>` of `#card-vehicles` (~line 3000).

**Caveat — `#card-fieldnotes` sits between `#card-property` and `#card-vehicles`** (lines 2931-2944). It's the *seventh* card visually, not the sixth. The "beneath the 6 main cards" phrasing in the proposal is approximately right but Paul should know that the existing card stack is 7 deep, not 6 — the Field Notes card was added in Phase B and shipped as a peer main card. Either:

- (a) The unified input goes beneath all 7 cards (likely intent — "beneath the dashboard"), or
- (b) The Field Notes card relocates or is folded into the unified input's footprint.

I read the proposal as (a). Confirm with ux-expert / Paul before placing.

**Layout/CSS work to expect.** The current `.quick-capture` and `.garden-guru` blocks have ~18px bottom margin and sit *above* the cards as a visual primer. Moving the unified equivalent below the cards changes its visual weight — it becomes a footer rather than a header. The CSS for the new section can borrow heavily from `.garden-guru` (lines 2167-2303), which already has the right register (soft cream background, serif italic label, restrained chrome) for a Mom-friendly composer. Expect ~30 min of CSS iteration to land the visual weight right; that's ux-expert's lane.

**Mobile reflow.** No special handling needed. The unified composer is a single `<section>` with a textarea + buttons; standard flex layout handles iPhone 13 / iPad in portrait without ceremony. The existing composers already work on iOS Safari with Web Speech API; the unified one inherits that for free via the same `createVoiceCapture` factory.

---

## Section 3 — Composer mechanics reuse

**The good news.** The shared piece is already factored: `createVoiceCapture({textareaId, micBtnId, hintId})` at viewer.html:8630-8739. It takes IDs (not DOM nodes), it owns its own state via closure, and it's already used twice. A third instance for the unified surface is a 5-line addition:

```
const UnifiedVoice = createVoiceCapture({
  textareaId: "ui-textarea",
  micBtnId: "ui-mic-btn",
  hintId: "ui-mic-hint",
});
```

**What's NOT shared today.** Textarea styles (`.fn-capture-textarea` vs `.gg-textarea` — different colors, different sizing), submit button styles (`.fn-capture-save` vs `.gg-ask-btn` — different gradients, different copy), and the submit handlers (`fnSaveInlineEntry` vs `GardenGuru.ask`). For Path C, none of these need to be consolidated. The unified surface gets its own CSS (new `.unified-input`-prefixed classes) and its two buttons each route to one of the two existing handlers.

**Suggestion (defer until after Path C ships).** Once the unified surface is the only composer the user interacts with, the styling on `.fn-capture-textarea` and `.gg-textarea` becomes dead — those elements are `display: none` under the feature flag. A follow-up cleanup pass deletes the dead CSS. Track this as Path C's debt — `// FOLLOWUP: dead styles when unified-input is default` comment, removed in the next cleanup pass.

**The mic button intent.** Worth flagging for ux-expert: today's two mics carry different implicit intent (the FN mic says "I'm logging an observation"; the GG mic says "I'm asking a question"). The unified mic is *intent-less* until the user picks Record or Ask. That's a UX decision (does dictation start before intent is picked? are both buttons disabled until text exists?) but it has an engineering implication — the `createVoiceCapture` factory doesn't care about intent, so the engineering is identical regardless of how ux-expert resolves it. The factory remains the right abstraction.

---

## Section 4 — State ownership in the unified surface

These are the four state questions the proposal raises, with my answers:

**Who owns pending input text (before user picks a path)?** A new `UnifiedInput` IIFE — owns the textarea value via standard `<textarea>` DOM state, no JS-side mirror needed. The textarea IS the state. On submit (Record or Ask), the IIFE reads `textareaEl.value`, dispatches to the appropriate handler, then clears the textarea.

**Who owns mode/intent state ("typing-mode-undecided" / "typing-as-capture" / "typing-as-ask")?** The proposal as written has no "leaning" state — the user types freely and explicitly picks a path. That's the simplest engineering shape: no intent state at all, both buttons are equally available, the buttons themselves are the routing decision. **My recommendation: ship that simplest shape first.** If ux-expert wants per-button hover/active styling to indicate which intent is being chosen, that's CSS-only. If they want a "leaning" state that visually previews intent before commit (e.g., textarea border changes color as you hover Record vs Ask), that's a JS state — but it's also feature creep and shouldn't gate v1.

**Who owns reply rendering?** Per recommendation C2 above: `#gg-conversation` div moves into the unified-input section (above the input row). `renderGardenGuru()` keeps targeting it by ID — no renderer changes needed. The reply lands directly above where the user typed, which is the right place visually.

**Who owns the conversation cap counter ("5 follow-ups left")?** Same div motion as `#gg-conversation` — `#gg-counter` moves with it. Or hide it during compose-mode and show it only after a conversation starts. ux-expert call; both are easy.

---

## Section 5 — Migration safety (observations + conversations)

**Verdict: no data migration is required.** The data layer is fully independent of the markup we're changing:

- `localStorage["tateTracker.observations.v1"]` — touched only by `ObservationStore` (8233-8365). The unified surface routes Record-an-observation to `fnSaveInlineEntry()`, which calls `ObservationStore.save()`, which writes to the same key. Nothing changes.
- Worker KV `observations:*` — touched only by `ObservationStore.callWorker()`. Same handler, same Worker endpoint. Nothing changes.
- Worker KV `conversation:<uuid>` — touched only by `GardenGuru.ask()` (which POSTs to `/api/chat`) and the Worker itself. The unified surface routes Ask to `GardenGuru.ask(text)`, same handler. Nothing changes.
- `localStorage["tateTracker.sync.v1"]`, `tateTracker.lastSync.v1` — touched only by `ObservationStore`. Nothing changes.

**Path A would have to migrate.** If you rebuilt `GardenGuru` from scratch (e.g., to merge it into a unified composer object), the existing in-memory conversation state would be lost on the deploy. KV-side conversations persist regardless — but the in-memory `turns` array of any conversation in progress at deploy time is gone. Low impact (Phase E ships fresh sessions with no persistence to localStorage anyway — the on-page conversation evaporates on refresh today) but worth naming. Path C avoids this entirely.

**The one migration consideration in Path C.** The feature flag itself. When Paul flips `tateTracker.ui.unifiedInput.v1 = true` on his phone, the old composers go `display: none` and the unified one appears. Any text in the old composers' textareas at flag-flip time is orphaned (it's still in the DOM, just hidden). Edge case: Paul has Field Notes textarea half-filled with a dictation in progress, flips the flag, loses the text. Acceptable at hobbyist stakes — the flag is dev-only until promotion. If/when the flag becomes user-facing, gate it on "no in-flight text" or copy the text across at flip-time. Don't ship that complexity in v1.

---

## Section 6 — Deploy posture and rollback

Phase E shipped 24 hours ago. The single E2E smoke test that's happened is Paul opening the GG card and asking a question. Mom hasn't touched it. The Garden Guru evaluation rubric is freshly written and unvalidated. This is *not* a moment to ship a major UX change as the default for everyone.

**Recommended deploy posture:**

1. **Feature-flag the unified surface via `localStorage["tateTracker.ui.unifiedInput.v1"]`.** When true, body gets `.unified-input-active` class; CSS hides `#quick-capture` and `#garden-guru`'s composer surfaces and shows `#unified-input`. When unset/false (default), the shipped layout renders unchanged. **Mom and brother see the current dashboard. Paul sees the new one on whatever devices he flips the flag on.**

2. **Paul flips the flag on his phone first.** Use the property in the field for ~3-5 sessions. Real-life feedback before laptop/desktop testing — that's the dominant Paul-mobile use mode the rubric identifies (Performer 1).

3. **After Paul is satisfied on phone, flip on laptop.** Test the desktop research-mode (Performer 2) shape.

4. **Wait until metrics-capture instrument lands** (from the 2026-05-20 metrics-capture path-eval) before promoting to default. Without metrics, you can't tell whether Mom's behavior changes after the layout change — the whole point of the redesign is supposed to make engagement more legible, and shipping it blind defeats that.

5. **Promote by inverting the flag.** Once confident, change the default from "off" to "on" and add `localStorage["tateTracker.ui.unifiedInput.disable.v1"]` as the inverse opt-out for rollback. The two-flag pattern (positive enable initially, negative disable post-promotion) keeps the door open for anyone — Mom included — to fall back to the shipped layout if the new one breaks for them.

6. **Cleanup pass at ~30 days post-promotion.** If no one's flipped the disable flag and metrics show engagement holding or improving, delete the dead `#quick-capture` + `#garden-guru` composer markup and the dead CSS. Path C becomes Path A-equivalent at that point, the right way: code consolidation following evidence, not preceding it.

**Rollback plan.** Three layers:

- **Per-device user rollback:** Paul flips the flag off in his browser console: `localStorage.removeItem("tateTracker.ui.unifiedInput.v1")` and refreshes. Mom never had it on; she's unaffected.
- **Codebase rollback during pre-promotion:** delete the unified-input markup + IIFE; revert single commit. Existing surfaces still work because Path C didn't touch them.
- **Codebase rollback post-promotion:** flip the default back to off; ship a small commit. Old markup still exists (until 30-day cleanup pass), so the old layout renders correctly. After the 30-day cleanup, rollback would require restoring deleted markup — at that point, "rollback" is more accurately "design v3," which is fine.

**The one thing you can't easily rollback.** If during Paul's testing of the new surface, Mom happens to see his phone or hears him talking about it and forms an opinion ("oh, the new one") before the metrics-capture instrument tells you whether her actual behavior is changing. That's a UX research validity issue, not a deploy issue — flag it to user-researcher if it becomes relevant.

---

## Section 7 — What I'd want Paul to weigh in on before implementation

Strategic / cross-lane questions where this path-eval calls the shape but doesn't have authority to decide:

1. **The "6 vs 7 main cards" reading of the proposal.** Confirm whether the unified surface goes beneath ALL existing cards (including Field Notes) or whether Field Notes card relocates as part of this redesign. (Engineering doesn't care, but the answer changes the markup placement.)
2. **C2 vs C1 vs C3 for the GG conversation history.** I recommended C2 (reply renders in the new section, above the input). ux-expert should weigh whether the reply-near-input intent matches the surface's intended use mode. If they prefer C3 (reply gets its own main card), engineering cost stays low.
3. **Feature-flag delivery for the activation.** Paul flips it in browser DevTools? Or do we add a tiny UI affordance (e.g., a `?ui=unified` query param) so Paul can flip on his iPhone without dev tools? Tiny additional complexity — but I'd add the query-param path if Paul's smoke testing will happen primarily on phone (which the rubric says it will).
4. **Phase F's strategic decision.** If un-benching Phase F (image input) is on the table near-term, the unified-input redesign and the image-input add land are sibling features and might want to be scoped together. That's an ai-advisor + Paul decision; this eval flags it without trying to resolve it.
5. **Whether to fold this into the metrics-capture sprint.** Both path-evals shipped today. Both touch the same single file. Shipping them as one coordinated pass means one round of regression-testing, one Mom-facing layout update, one deploy. Shipping them separately means two rounds, two deploys, lower per-change blast radius. My instinct: ship metrics-capture FIRST (it's invisible to the user), let it run for a week to establish a pre-change baseline, then ship unified-input behind a flag. Sequencing matters here for the analysis: without a pre-change baseline, post-change engagement deltas are unattributable.

---

## Appendix — Principles applied / surfaced

- **[[Capture path stays pure; batch and amortize]]** (fernwood.md, 2026-05-20) — honored. The Record button calls `fnSaveInlineEntry()` which writes to `ObservationStore`, no AI involved. The Ask button is the only path to `/api/chat`.
- **[[Storage mirrors existing shape; analysis lives in tools/]]** (fernwood.md, 2026-05-20) — not directly applicable (no new storage), but the spirit holds: don't invent new state when existing state covers the case. `ObservationStore` and `GardenGuru` stay as-is.
- **AHA (Avoid Hasty Abstractions)** — drove the "don't ship Path D as v1" recommendation. The third call site for a hypothetical composer factory doesn't exist yet. Wait for it.
- **Modular, not literal microservices** (engineering-partner foundation) — drove the "thin router that delegates to existing handlers" shape of Path C. Small composable pieces, single-responsibility modules, no premature consolidation.
- **AI-aware maintainability** (engineering-partner foundation) — drove the "keep two named modules instead of one big module" preference. Claude can navigate `ObservationStore` and `GardenGuru` as named objects in one hop each. A unified `UnifiedComposer` module that internally routes would be denser to navigate.

**Principles to propose** (Mode 3 candidates from this eval — not silently adding, flagging for Paul):

- **Feature-flag layered UX changes against the hardest-to-redo user.** When a UX change risks the make-or-break user's engagement and the change is reversible, default the change OFF for everyone and flip ON only on dev devices until measurable confidence accrues. The opposite — "ship to everyone immediately because rollback is easy" — is the wrong calibration when one user is load-bearing. (Surfaced 2026-05-20 in unified-input path-eval; candidate for `fernwood.md` since it's project-specific to Mom-as-make-or-break. Generalizes if any future project also has a load-bearing single user.)
- **Markup change vs. state-machine change is the right axis for "is this safe to ship."** Markup edits in a single-file static-HTML project are nearly always safe; state-machine edits are nearly always risky. When evaluating a refactor, look for the cut that isolates markup-only changes from state changes — that cut is where the deploy boundary belongs. (Surfaced 2026-05-20; candidate for cross-project.md if it shows up in a Bolo Boys path-eval as well, since the static-HTML pattern is shared.)
