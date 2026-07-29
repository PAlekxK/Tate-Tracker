# Fernwood — backlog rationalization, UX lens

**Date:** 2026-07-29 · **Reviewer:** ux-expert · **Mode:** review (rationalization report)
**Review level:** flow / IA — the whole top-of-app input stack plus a system-wide type pass. Not micro-detail;
where I name a pixel it is because the pixel is the finding.
**Viewport judged:** 390 × 844 (mobile only). Desktop was not assessed and should not be inferred from this.
**Scope:** W8·a (input stack), W8·b (typography), A3's deferred UX findings, the tabs/IA question.
**Out of scope:** backend, the AI substrate, content voice (content-steward's lane), a11y implementation.

## 0 · User context

| | |
|---|---|
| **Primary user** | Mom. Reads with difficulty; named blocker is fear of being wrong; iPhone, intermittent sessions. |
| **Core jobs** | ① See what's happening on the place without committing to anything. ② Set something down when she notices it. ③ Get an answer to a question she has right now. ④ Be told her input mattered. |
| **Context of use** | Standing on the property or sitting with the phone; short sessions; 15 sessions / 30 days; opens the glance and rarely goes deeper (`card_expanded` 4× vs Paul's 47). |
| **Evidence tags** | `validated` — the fear statement (self-reported, n=1), the tabs ask (Paul-relayed, in person), the rainfall report, the Journal naming answer. `inferred` — that ambiguity between surfaces is *causing* the low answer rate. `assumption` — that a cleaner stack raises input volume. |
| **user_context_confidence** | **medium-high.** Rich behavioural + explicit evidence, but every engagement number in the record was measured through the noisy stack described below, which is the whole point of this run. |

### Established principles applied (library first, heuristics second)

From `~/.claude/design-principles/`, in the order they bind here:

| Principle | File | Where it lands |
|---|---|---|
| **Scope is communicated by where you tap, not auto-detected** | cross-project | The whole of §1 — five doors, no declared scope. |
| **Capture needs a declared scope; a scope-blind capture control can't stay AI-free** | fernwood *(candidate, 1 occurrence)* | **This review is its second occurrence** → propose promoting it out of candidate status. The composer's fused "log or ask" is the same failure at field level. |
| **A modeled value placed flush with a measured one borrows its credibility** | fernwood *(candidate, 1 occurrence)* | **UX-7 is its second occurrence** → propose promoting. Blue-as-state and blue-as-source is the same borrowing, done through hue instead of position. |
| **Source-hierarchy drives layout** · **Freshness sets altitude** | cross-project | UX-7, UX-8, and §2.3 rule 2 and rule 6. |
| **Typographic hierarchy by value** | cross-project | §2.2 is the enforcement mechanism this principle has been missing — it has never had a scale to be enforced against. |
| **Make every surface read at half-engagement** | fernwood | UX-8 (the labels that name the numbers stay small) and UX-9. |
| **A CTA's label must promise what the destination actually delivers** | cross-project | `Save & ask the Almanac` writes into a card now named **Journal** (renamed 2026-07-29 on her answer). Paul scoped the rename to the card deliberately, and the header tagline keeps "Almanac" — so this is **flagged, not recommended**: the word now has two referents on one screen, and "did she find the Journal" is measured through that. Worth a decision, not a fix. |
| **Prefer the platform's native control over an app reimplementation** | cross-project | UX-1 — respecting Safari's 16 px input rule is the cheapest form of this. |
| **A correct "no" still owes a next move** | cross-project | `Something's missing` opens the correction field but silently removes `＋ Add a note` and swaps the button row — the next move arrives, unannounced. Folded into UX-2's fix. |

Nielsen heuristics reached for where the library was silent: #1 visibility of system status (UX-3, UX-6), #4
consistency and standards (UX-8, UX-3), #6 recognition over recall (UX-5). Norman: signifiers (UX-11),
feedback (UX-4), and conceptual model (§1.2 — she has no model of why five boxes exist, because there isn't one
to have).

**Orienting principle applied throughout:** this is measurement hygiene. For every finding I state what signal it
currently corrupts and what it would measure cleanly afterwards. Findings that only make things prettier are
marked as such and ranked last.

---

## 1 · The input stack, traced at 390 × 844 (W8·a)

### 1.1 What is actually there

`.unified-input` spans **y = 184 → 1351 — 1,167 px, about 1.4 phone screens of consecutive asks before a single
thing about the place appears** (the dashboard strip starts below it; `viewer.html:5295` … `5370`, strip at
`5373`). Under the header, in DOM order:

| # | Surface | What it collects | Where it posts | How she tells it apart | **A tap on it is ambiguous between…** |
|---|---|---|---|---|---|
| 1 | **Ack ribbon** `#mom-queue-ack` → `.mom-ack-ribbon` (`9628`–`9756`) | a receipt (**Got it**), free text (**Write back**), a navigation intent (the underlined phrase inside the sentence) | `/api/feedback` as `q-ack-receipt` (sentiment `landed`) · or opens the ribbon panel with `section:"ack-reply"` | green container, ✓ lead mark, dated bold stamp | **"I read your message"** vs **"I agree with your guess."** `Got it` is a pale-green pill; 190 px lower `That's all of them` is a filled-green pill with a ✓. Both are green affirmatives. |
| 2 | **Composer** `.ui-input-row` (`5328`–`5364`) | free text + one photo **or** one audio; logs verbatim, then asks Guru | `/api/observations` + Guru | tan container, rounded field, two unlabelled 40×40 glyphs | **"log what I saw"** vs **"ask a question."** One box, one button, and the *placeholder itself is two asks in one string* — `"What did you see, or what would you like to know?"` (`5332`). |
| 3 | **Mama's Perspective** `#mom-queue` (`9788`–`9800`, card at `10040`–`10163`) | a 3-way answer, optionally a note, optionally a correction | `/api/feedback`, `context.type:"mom-queue"` | cream card, italic serif title above it | **"answer this question"** vs **"write something."** `＋ Add a note` is a dashed full-width control that reveals a second textarea; `Something's missing` silently swaps the button row for a single `Send` and hides `＋ Add a note`. |
| 4 | **Zone-walk launcher** (`9819`–`9823`) | voice, or text via the map's describe panel | `/api/zone-audio` · or `/api/feedback` with `section:"zone-describe"` | green-washed card, one forward action | **"start a walk"** vs **"another ask I can decline."** Renders unconditionally *underneath* an unanswered card. |
| 5 | **General-feedback tab** `FeedbackRibbon` (`10322`+, CSS `3980`) | free text | `/api/feedback` via `submitGeneralNote` | dark-green tab, fixed, `z-index:900` | **"tell Paul about the app"** vs **"the same box as #2."** It floats over the card at #3 (card region y 589–1326). |

**Five distinct free-text paths, all landing in the same room:** the composer textarea, *Write back*, *＋ Add a
note*, the *General feedback* tab, and the hidden `.mom-queue-correction` revealed by *Something's missing*.
Three of them (`.mom-queue-correction` 15 px Crimson on `#fffdf6` with a `#cdbf90` border, and
`.feedback-panel-input` 15.5 px Crimson on `#fffdf6` with a `#cdbf90` border) are **visually the same object**
appearing in two unrelated places.

**The asymmetry that is the whole problem:** the *record* can already tell these apart — every note carries
`context.section` (`9903`). **She cannot.** So we are collecting well-labelled data about a choice she was never
in a position to make. That is not a small distortion; it means "she used the general box" may only mean "that
was the box nearest her thumb."

### 1.2 What this currently corrupts, stated plainly

| Signal we steer on | What it can't distinguish today |
|---|---|
| `momack_acknowledged` vs `momqueue_answered:landed` | *"I read your note"* from *"your guess is right."* Same colour, same shape, 190 px apart. |
| composer usage | *"she logged an observation"* from *"she asked the Almanac."* Fused in one field, one button, one placeholder sentence. |
| `momqueue_answered` with `hasNote:false` | *"she had nothing to add"* from *"she typed something and the stepper deleted it"* (see UX-2) from *"she never found the note control."* |
| `launcher_offered` (60 in 30 d) | *"offered"* from *"rendered below an unanswered question she was still looking at."* |
| general-feedback volume | *"she chose the app-feedback channel"* from *"it was the box that was on screen."* |
| any tap in the stack | intent, from proximity — because nothing above the fold is labelled with what it is for. |

### 1.3 Evaluating Paul's two floated moves

**(i) "Possibly kill the click-to-expand line that opens a text box."**
There are two candidates, and they deserve opposite verdicts.

- **`＋ Add a note` on the confirm card — kill the *control*, keep the *capability*, and move it after the
  answer.** As it stands it is a dashed full-width button that looks like a drop zone, reveals a box 120 px
  below another box, and disappears when she taps `Not quite`. Worse, it is the only place in the app where
  typed words can be destroyed (UX-2). Move the invitation to the *ack step*: after she answers, the
  confirmation line offers "Anything to add?". That removes an affordance from the resting card, keeps the
  escape hatch for the highest-value input class (expertise she has that we never asked about), and — the
  measurement win — makes a note unambiguously *about the card she just answered*. **Do not delete the
  capability;** her richest contributions have all been free text.
- **The ack ribbon's inline underlined phrase (`ack-inline-link`, `9676`–`9688`) — keep it.** It opens a *card*,
  not a box, and it is the one place in the app where our message carries its own door. It is the fix that F7
  asked for and it shipped. Its only defect is that it lives inside a strip that also holds two pills, so a
  reader meets three tappable things with three different destinations. Fixing UX-3 (make the receipt not look
  like a decision) resolves that by subtraction.

**(ii) "Possibly give each input source its own card / labelled section."**
**Half right — and the half that's wrong would make things worse.** The Gestalt common-region literature is
clear that a container beats typographic distinction for separating adjacent things, and Fernwood's own reader
rule ("never a label doing all the work") points the same way. But she reads the glance and stops. Adding four
more cards to a 1,167 px pre-content stack spends the scarcest space in the app on making our asks more
architecturally impressive.

**So: structural separation yes, more containers no. Reduce to three doors, each with one job and a visible
name:**

| Door | Job | Where | Visible label |
|---|---|---|---|
| **To you** | our message + one reply | ack ribbon (stays at top) | dated stamp leads; one reply control |
| **From you, about the place** | log or ask | composer (stays at top) | a persistent label above the field, not a placeholder |
| **From you, about the app** | tell Paul | the edge tab | "Tell Paul" |

and **one ask at a time below the fold** (the confirm card), with the launcher rendering only when the queue is
empty. That is fewer surfaces than today, not more, and each one gains a name.

### 1.4 The target state, in one sentence

**Label the door, not the room.** Every surface that accepts input says, in visible text that does not vanish
when she types, *what it collects* and *who reads it* — and no two adjacent surfaces share a button shape or a
green fill. Everything else in this report is an instance of that.

---

## 2 · Typographic hierarchy (W8·b)

### 2.1 The finding under the finding

`viewer.html` contains roughly **700 `font-size` declarations across ~40 distinct pixel values from 7 px to
42 px**, in 0.5 px increments (9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5,
17, 17.5, 18, 18.5, 19, 19.5 …). That is not a scale with exceptions; it is a distribution. Every new surface
picks a size by eye, which is exactly why the rainfall card could invert the project's source hierarchy without
anyone deciding to. **The rainfall inversion was a symptom; the absence of a scale is the disease** — and a
spot-fix that does not install a scale guarantees the next surface re-creates it.

Compounding it: `body.text-lg` is a **hand-written allowlist**. Any class not on it is invisible to the
accessibility mode Mom is most likely to be using. There is no check for that, and eight rainfall classes are
still missing from it today.

### 2.2 The scale to install (7 steps, ~1.2 ratio, hard floor 12.5)

| Step | Base | A+ (`text-lg`) | Use |
|---|---|---|---|
| **Display** | 28 | 34 | the one number or word a card exists to show |
| **Title** | 22 | 26 | card titles, section heads |
| **Lead** | 19 | 23 | the single sentence per card that must read at arm's length (glance lines, card summaries) |
| **Body** | **16** | 19 | all prose, all serif guide text, **all text inputs** (also the iOS no-zoom floor — see UX-1) |
| **Secondary** | 14 | 17 | captions, hints, meta, button labels |
| **Label** | **12.5** | 15 | uppercase eyebrows, tags, chips, source badges |
| — | *nothing below 12.5 ships* | | |

Migration rule: round every existing value to the nearest step; where two adjacent elements land on the same
step and need separating, separate them with **weight or container**, never by inventing a 13.5.

### 2.3 The emphasis grammar (one channel, one meaning)

1. **Family = who is speaking.** Crimson serif = the place, the record, prose, her words. DM Sans = the app's
   chrome — labels, controls, numbers, chips. Never mix inside one line.
2. **Size = altitude.** Freshest / most local / most actionable is largest. A *measured* number is never smaller
   than a *modelled* one on the same card. (Already project doctrine; the scale is what makes it enforceable.)
3. **Weight = the noun under discussion.** 600 on the plant name in a prompt, on a dated stamp, on a notable
   figure. Never a whole line, never a whole sentence.
4. **Italic = editorial aside only** — framing, captions, hedges, empty states. **Italic never carries a number
   and never labels a control.**
5. **Uppercase + letter-spacing = a source or section eyebrow**, at Label size, never smaller.
6. **⭐ Hue = source. Fill and weight = salience.** Green family = measured here / ours. Blue family = modelled /
   regional. Tan = an input surface. Amber = an unverified read. **Hue must never encode "active" or "notable"**
   — that is what `.rain-active` does today (UX-7) and it is why blue is unreadable on that card.
7. **`✓` means exactly one thing: "this control is the affirmative choice."** It never means "we did something,"
   and it never decorates prose.

### 2.4 On Paul's "why is it a check mark?"

Because it is doing three jobs within ~350 px: a decorative lead on *our* message (`.ack-check`, 17 px green,
`3869`/`9632`), the affirmative glyph on *her* Yes control (`.gg-suggest-btn-yes::before`, `4282`), and a
trailing mark on the ack prose (`"Noted — your read's in the record. ✓"`, `10230`–`10232`). Read as
task-manager grammar because the first and third uses *are* task-manager grammar: they say **done**.

**Recommendation:** ✓ survives only on the control. Drop it from the ack prose (the sentence already says the
words). Replace the ribbon's lead mark with a **letter/note glyph** — the ribbon is a letter to her, and the
Mom-legibility rule wants an icon carrying part of the meaning, so removing the glyph entirely would cost more
than it saves. If Paul prefers no mark at all, let the bold dated stamp lead; that is defensible and quieter.

---

## 3 · Tiered findings

Effort: S ≤ 1 h · M ≤ half a day · L longer. Every row names the signal it cleans.

### TIER 1 · FIX NOW (nothing unblocks these; Mom-facing wording still passes Paul's gate)

| ID | Sev | Claim | Where | Cleans | Eff |
|---|---|---|---|---|---|
| **UX-1** | critical | **Every free-text field in the app is under 16 px, so iOS Safari zooms the viewport the moment she taps it** and leaves her at ~1.2× with the layout wider than the screen. `.ui-textarea` 14 px, `.mom-queue-correction` 15 px, `.feedback-panel-input` 15.5 px. This is a mobile-only defect and has never been on the board. | `3411`, `3951`, `4023` | Abandoned-typing looks identical to never-started-typing. A zoom-and-pinch tax sits on the only surfaces she uses. | S |
| **UX-2** | critical | **The carousel stepper silently destroys typed-but-unsent notes.** `‹ ›` sets `idx` and calls `render()`, which does `host.innerHTML = ""`; the textarea and its value are destroyed and never read. Same on `showAck`'s re-render. Her words are gone with no warning and no outbox. | `9604`, `10074`–`10090`, `10175`, `10190` | `hasNote:false` currently conflates "nothing to add," "never found the control," and "we deleted it." Also the only remaining silent-loss path in the loop, which `test-feedback-cycle.py` does not cover. | S–M |
| **UX-3** | important | **Two green affirmatives, 190 px apart, meaning different things.** `Got it` (`.ack-btn-primary`, pale green pill) vs `That's all of them` (`.gg-suggest-btn-yes`, filled green + ✓). Make the receipt visually *not a decision* — a quiet text link or neutral outline; reserve filled-green-plus-✓ for answers about the place. | `3904`, `4277`–`4282` | `momack_acknowledged` vs `momqueue_answered:landed`. Today the two most important taps in the app share a visual grammar. | S |
| **UX-4** | important | The ack's two controls are **30 px tall with 12.5 px labels** — the only sub-44 px targets in the stack, on the loop's first hard receipt signal. Take to 44 px / 14 px. | `3893`–`3899` | Receipt rate. A missed tap is recorded as no tap. | S |
| **UX-5** | important | **The composer has no visible label.** Its identity lives in a placeholder that disappears on the first keystroke — and that placeholder is two asks in one string. Add a persistent label above the field; reduce the placeholder to an example or drop it. | `5332`, `17194` | The box's identity survives typing. (Intent stays fused — see §6.) | S |
| **UX-6** | important | **`✓` carries three meanings in ~350 px.** Keep it only as the affirmative-control glyph; drop it from ack prose; give the ribbon a letter glyph or no glyph. | `3869`, `4282`, `10230` | Removes "done" grammar from a field journal, and stops a decorative mark from being read as a state. | S |
| **UX-7** | important | **Blue does two unrelated jobs on the rainfall card.** `.rain-active .rain-cell-value` renders her *own gauge's* headline figures navy `rgb(31,72,112)` as a "notable" state, while the *regional model* block is the same blue family (`.rain-ctx-amount` `rgb(26,58,90)`, `.rain-ctx-col-label` `rgb(90,138,170)`). A reader cannot tell whether blue means *notable* or *not from your gauge*. Fix at the encoding level: **hue = source only**; encode notable with fill + weight + a droplet glyph. | `1659`, `2237`, `2248` | Source hierarchy — the correctness rule this card exists to enforce. The 14× incident was a source-legibility failure; this is the same failure in a different channel. | S–M |
| **UX-8** | important | **Sub-12.5 px type persists, including in large-text mode.** `.rain-cell-label` 9 → 11, `.rain-byday-day` 9 → 11, `.rain-ctx-col-label` 9.5 → 11; **no `text-lg` rule at all** for `.rain-ctx-title` (10.5), `.rv-badge` (10), `.rv-pct` (9.5), `.rain-gauge-label` (10.5), `.rain-gauge-chip` (11.5), `.rain-byday-none` (11), `.garden-hero-rain-label` (9.5), `.garden-hero-rain-summary` (11.5 — the single most readable sentence on the block); and `.rain-local-note`'s rule is a **no-op** (16 → 16). Also `.icon-beta` at 7 px. Apply the §2.2 floor and complete the allowlist. | `1487`/`5202`, `1615`, `1622`, `1640`, `2212`, `2235`, `2258`, `2282`, `2302`, `2310`, `2322`, `2330`, `3671` | The *labels that say which number is which* are the part that stays small — which is precisely what made two numbers read as a contradiction in July. | M |
| **UX-9** | important | **Three blocks for one question.** "Mama's Perspective" (16 px italic serif — the largest type in the ask stack) + a 13 px framing line + the card. Fold both into the card as a small header. *(ux F5 move (b), re-derived — still holds.)* | `3850`–`3859`, `9788`–`9796` | Removes ~60 px of ask-weight above the fold and stops a section title outranking the question it introduces. | S |
| **UX-10** | important | **The edge tab floats over the confirm card** (`z-index:900`; measured 82 × 63 at left 308; card region y 589–1326). WCAG 2.2 SC 2.4.11 is the standard's name for this class. Hide it while `#mom-queue` is in the viewport (an IntersectionObserver is already in use for `observeViewed`), and keep the trimmed footprint. | `3980`, `4047`–`4056` | A card that is partly covered can be "viewed" and unanswerable at once — `momqueue_viewed` currently cannot tell those apart. | M |
| **UX-11** | nice | **Relabel the tab "General feedback" → "Tell Paul."** Disambiguates from the composer by *recipient*, which is the one distinction a reader with low literacy confidence can hold; also shorter, so less overlap. The aria-label already says this (`10336`); the visible label doesn't. ⚠ Paul chose "General feedback" on 2026-07-20 — this proposes a revision, his call. | `10338`–`10339` | "Which channel did she choose" becomes a real question rather than an artefact of proximity. | S |
| **UX-12** | nice | **Gate the launcher on an empty queue.** It renders unconditionally below an unanswered card. Demoted ≠ concurrent. | `9819`–`9823` | `launcher_offered` (60/30 d) starts meaning "she had a clear shot at it." | S |

### TIER 2 · CONFIRMED (an answer already in hand — build it)

| ID | Claim | Basis | Where | Cleans | Eff |
|---|---|---|---|---|---|
| **UX-13** | **Make the Journal reachable.** She asked to look back at her questions and she named the card. It is **8th of 13 cards** and has **no tile in the dashboard strip**. Add a Journal tile to the strip's second tier and move the card above the reference cards. | Her ask 7/26 + her Yes on `q-almanac-name` 7/29 | `5603`, `5396`–`5405` | Turns "she never looked back" from an unfalsifiable claim into a measurable one. | S |
| **UX-14** | **Rainfall range — month + year (W8·c).** Present as additional by-day-style rows inside the *same green gauge container*, not as a new panel, so the source grouping survives the extension. | Her direct ask 7/29 (`fb-946dp0qk-ms639ds6`); `weather-history.json` already local | `7304`–`7322` | — (feature; the container rule is what keeps UX-7 fixed) | S–M |
| **UX-15** | **Read `/api/feedback` broken down by `context.section`.** Every note already carries which door it came through; nothing reports it. This is the instrument for the entire measurement-hygiene argument. | Data already captured | `9903`, `tools/read-mom-feedback.py` | Makes "which surface does she actually use" answerable *without asking her*. | S |
| **UX-16** | **Move the ask host `#mom-queue` below the dashboard strip.** She meets, in order: what we owe her (ack), her own pen (composer), the place (strip + cards), and only then the asks. No surface added, no surface deleted. This is F5's move (c) — "lead with something that asks nothing" — achieved by reordering rather than by inventing a new block. | Her behaviour (glance-only, 4 expands) + the Weeds statement + F5 | `5369`, `5373` | Puts ~1,100 px of asks below the content they're competing with, so "did she scroll past the asks" and "did she see the place" stop being the same event. | M |

### TIER 3 · STEER (question not yet asked — each row carries its question and its capture path)

| ID | Claim | **The exact question** | **Capture path** | Eff |
|---|---|---|---|---|
| **UX-17** | **Her five categories omit the app's four most-used surfaces.** *vehicles · equipment · house systems · gardening · wildlife* contains no weather, no sky, no lake, no map, no Journal — and weather is the card the app leads with and the one she has engaged with most. Her list is not a nav-widget request; it is a statement that the app should be organised by **domain of stewardship** (things you maintain / things that live), which independently reproduces the Track A / Track B split. Before any restructure, the gap has to be closed. | *"Your list was vehicles, equipment, house systems, gardening and wildlife. Weather, the sky, the lake and the Journal aren't on it — should each of those stand on its own, or live under one of your five?"* Labels: **"They can stand on their own" / "Put them under mine" / "I'll think on it"**, `correctionPrompt`: *"Which would you put where?"* | New reflective card in `questions.json` (`_kind:"reflective"`, no `_foldTarget`), **queued behind `q-top-categories` — never two IA cards at once** → `POST /api/feedback` → `read-mom-feedback.py --pickup` → retired by hand (`active:false` + `resolvedAt`; it will hold the watermark until then, per the 2026-07-27 unprobeable rule). | S to ask |
| **UX-18** | **Tabs vs. reinforced cards is not yet an askable question — it is a telemetry question, and the read is pre-registrable.** Cards-as-doors shipped 2026-07-29 (`94d9302`) and has **zero** post-ship data. Asking her "do you want tabs" is a verdict-shaped question about our design, the class she declines. Resolve in the cheapest place first (telemetry → Paul → only then Mom, per `/mom-cycle`). | *No question to Mom yet.* Pre-registered behavioural read, window **2026-07-29 → 2026-08-12**, her device only, builder devices excluded: `card_expanded` **≥ 12 → the doors worked; do not restructure.** **≤ 5 → the doors did not work; the IA question becomes live.** 6–11 → extend one window. | `tools/read-mom-funnel.py` / `analyze-fernwood.py`, device-scoped with `excludeFromEngagement`; record the read in `.engineering/2026-07-22-mom-loop-first-run.md` as a dated run section. ⚠ Decode the deviceId's embedded timestamp rather than trusting a range-scoped `first-seen`, and remember Safari ITP can evict the id inside this window. | S to read |
| **UX-19** | **If UX-18 fires "restructure," the widget is still not automatically tabs.** At 390 px a five-tab bar carrying "house systems" cannot render legibly at 16 px, let alone at A+ (19 px). The cheap, reversible version of her ask is to **adopt her five categories as card *order and grouping*** — maintained things together, living things together — with a labelled group heading, before any new navigation component is built. | *(Only if UX-18 fires and UX-17 is answered)* — put the two orderings in front of her as a thing she can look at, not a thing she must judge: *"We've grouped the cards the way you described. Does this feel like the right order?"* | Same card mechanism; but prefer showing the reorder and reading `card_expanded` again over asking. | M–L to build |

---

## 4 · Kill list

| Row | Verdict | Why |
|---|---|---|
| **A2 · "Add-a-photo affordance on the confirm card"** | **KILL for now** (not permanently) | It adds a **sixth** input affordance to the exact surface this review exists to disambiguate, and its own row already says "validate with Mom first." Under the orienting principle, a finding that adds a surface must state its measurement cost: this one makes the confirm card's tap-intent *less* interpretable at the moment we are trying to make it more so. It is also gated on W6 (a photo is an identity key, and there is no instance model). Revisit after the stack is clean **and** W6 exists. |
| **W7's open question — "does a per-card *Add a note* earn its complexity?"** | **KILL as an askable row; it is not a question for Mom** | It is a verdict-shaped question about our own design — the one class she reliably declines — and it is answerable from data we already hold (`hasNote` across all offers, plus UX-15's section breakdown). Escalation ladder: telemetry → Paul → only then Mom. A row that asks Mom to grade our UI should not exist. **The design decision itself survives** as UX-2 + §1.3(i). |
| **W5's fallback option — "icon-only rest state that expands to the label on tap"** | **KILL** | Directly contradicts the Mom-legibility rule (meaning never arrives by icon alone) and solves a problem that has since shrunk by half — the tab is 82 px, not 150 px. UX-11's shorter *labelled* tab gets the same width back without the cost. |
| **`.rain-local-note` `text-lg` rule** (`5202`) | **KILL** — dead code | 16 px → 16 px. A rule that looks like accessibility coverage and provides none is worse than an absent rule, because it makes the allowlist audit read clean. |
| **`buildGeneral` / `expandGeneral` / `sendGeneral`** (`9833`–`9884`) | **KILL** — dead code | Retired 2026-07-20, kept "as the reference capture flow the ribbon mirrors." It is a second, unreachable definition of the general-note path — the parallel-source-of-truth pattern this project has been burned by repeatedly. The ribbon's own path is the reference now. *(Engineering's lane; flagged from here.)* |
| **"Ribbon → day-by-day deep link" (A3 · audit row ②)** | **RETIRE — already shipped** | See §5. |
| **"Rainfall type-scale inversion" (W8·b ①) as written** | **RETIRE the stated version; a narrower finding survives** | See §5 and UX-7 / UX-8. |

---

## 5 · Status corrections

⚠️ **I have no shell in this seat, so these are verified against `viewer.html` at HEAD (file:line, plus dated
in-code comments) and against live DOM measurements relayed by the coordinator — not against `git log`.**
Someone with a shell should confirm the commits.

| Backlog claim | Reality | Evidence |
|---|---|---|
| **W8·b ①** — *"the rainfall card renders regional ERA5 at 22 px and Mom's own station gauge at 13.5–14 px … deliberately NOT patched as a one-off on 2026-07-29"* | **STALE — the size inversion was fixed on 2026-07-26.** `.rain-ctx-amount` was reduced **22 → 15 px**; `.rain-cell-value` was raised **13.5 → 18 px**; live DOM confirms every gauge figure at 18 px / 600. Her data is now *larger* than the model's, not smaller. **What survives is a different, sharper finding:** blue encodes both "active" and "regional source" (UX-7). | `2242`–`2253` (comment: "22 → 15px (2026-07-26)"), `1646`–`1657` (comment: "13.5 → 18px (2026-07-26)"), `1659` |
| **W8·b ①** — *"`body.text-lg` has **zero** rainfall rules"* | **STALE — there are 8**, added 2026-07-26. The claim must be re-derived, and the re-derived version is narrower but still real: the *figures* grow, the *labels naming them* stay at 9–11.5 px, **eight** rainfall classes remain unlisted, and one of the eight rules is a no-op. | `5191`–`5202` |
| **A3 · audit row ② / F7** — *"the ribbon promises 'look back day by day' with no path to it"* | **SHIPPED.** The ribbon now supports `linkPhrase` + `linkCard`, renders the phrase as an inline control, fires `momack_followed`, calls `expandCard(target)` and scrolls it into view. Live data has it pointed at `card-weather` right now. | `9659`–`9691`, `9414`–`9425` |
| **W5** — *"the full label makes the tab ~150 px wide, so on a phone it covers ~40 % of one horizontal reading band"* | **STALE.** Measured **82 × 63 px** at left 308 in a 390 px viewport (~21 % of width) after the ≤480 px stacking rule. **The overlap complaint is still true** — `z-index:900` over the card at y 589–1326 — but the magnitude is half what the row says. | `4047`–`4056`, live DOM |
| **W5** — *"the note + general field are the same CSS class 120 px apart"* | **PARTLY STALE.** The in-carousel general foot-line was retired 2026-07-20, so that specific pair is gone. **A new confusable pair replaced it:** `.mom-queue-correction` and `.feedback-panel-input` are near-identical (same family, same background `#fffdf6`, same border `#cdbf90`, 15 vs 15.5 px) in two unrelated places. | `3948`–`3953`, `4020`–`4025` |
| **A3 · F5 move (a)** — *"serve only ONE ask at full weight"* still listed as open against `MAX_VISIBLE` | **PARTLY MOOT, and the row misreads its own mechanism.** The carousel already renders exactly **one** card at a time (`items[idx]`); `MAX_VISIBLE=5` governs the *pool*, not the screen — so Paul's "keep a queue of cards" call and the one-ask-at-full-weight principle do not actually conflict. **What is genuinely still open is co-presence:** card + launcher + floating tab on one screen (UX-10, UX-12). | `9783`–`9824` |
| **A4 · W8** — *"IDEATION — revisit once front-door has signal"* | **SUPERSEDED** by W8·a/W8·b and by this report. The front door has signal: it is zero from her device across 60 offers, and W8·d already demoted it. | `BACKLOG.md` W8 / W8·d |

---

## 6 · External research — and what each source changes

Each entry names the Fernwood row it moves. Where the literature disagrees with ratified Fernwood doctrine, the
conflict is stated rather than resolved silently.

| Source | What it says | Row it changes | Conflict with Fernwood doctrine? |
|---|---|---|---|
| **NN/g — "Placeholders in Form Fields Are Harmful"** ([nngroup.com](https://www.nngroup.com/articles/form-design-placeholders/)); W3C Low Vision TF placeholder research ([w3.org](https://www.w3.org/WAI/GL/low-vision-a11y-tf/wiki/Placeholder_Research)); Deque ([deque.com](https://www.deque.com/blog/accessible-forms-the-problem-with-placeholders/)) | Labels must sit **outside** the field and persist; placeholders are low-contrast, vanish on input, and are worst for short-term-memory, low-vision and cognitive-load users. | **UX-5** (composer label) and the whole of §1.3(ii). | **⚠️ YES — direct.** The composer's placeholder-as-invitation is a *locked* call (unified input, 2026-05-20; "discreet ≠ dormant," Layout A 2026-07-03). I am proposing a revision, not an override: **keep the warm invitation, move it above the field** so it survives typing. The doctrine it does *not* violate: "never a standing 'add data' button." A **label on a box that already exists is not a new affordance** — the defer-affordances rule constrains adding surfaces, not naming them. |
| **NN/g — "Accordion Icons: Which Signifiers Work Best?"** ([nngroup.com](https://www.nngroup.com/articles/accordion-icons/)) | The downward caret is the only signifier that reliably reads as "opens in place"; plus-icons test no better than nothing; users tap label and icon about equally, so **both must be live** and must not do different things. | **Validates the shipped cards-as-doors** (`94d9302`): caret + "Open" label + whole header as one `role="button"`. Also argues **against** the dashed `＋ Add a note` — a plus icon is the weakest signifier tested, and here it also changes the card's layout. | No conflict. Strengthens **UX-18**'s "give the doors a fair measurement window before restructuring." |
| **NN/g — "The Principle of Common Region"** ([nngroup.com](https://www.nngroup.com/articles/common-region/)) + Gestalt proximity literature | A visible boundary **overrides proximity**: items inside a container read as one group even when something else is nearer. | **§1.3(ii)** — this is the evidence for *structural* separation. But it also warns why **more containers isn't the answer**: a container groups, it doesn't explain. Each container still needs a name (UX-5, UX-11). | Aligns with the Mom rule (icon + size + colour + position, never a label alone) — the container is the "position" channel. |
| **Systematic review, age-friendly mobile app design, 132 studies, 2025** ([PMC12350549](https://pmc.ncbi.nlm.nih.gov/articles/PMC12350549/)) | Linear navigation paths, clear hierarchies, enlarged text and targets, high contrast, **adjustable display settings**, voice as a primary (not supplementary) alternative, error-tolerant interfaces. | **UX-4, UX-8** (targets and type floors); **UX-18** (the case for a *simple, linear* structure is real — which supports her tabs instinct in principle even before it supports it in evidence). Fernwood's A/A+ toggle and voice capture are already what this review would prescribe. | No conflict; Fernwood is ahead of the literature on voice and text-size, behind it on target sizes in the ack ribbon. |
| **Interface guidelines for low-literate users, literature review** ([ACM 3578837.3578842](https://dl.acm.org/doi/fullHtml/10.1145/3578837.3578842)) + Scottish Government digital, 2025 ([blogs.gov.scot](https://blogs.gov.scot/digital/2025/02/21/how-designing-for-low-english-literacy-empowers-everyone/)) + inclusive-platform study, 2025 ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2451958825000326)) | Plain vocabulary, simple sentence structure, **redundant coding** (icon *and* text), few options per screen, and consistent placement. | **UX-6** (a glyph should carry meaning, so replace ✓ rather than delete it), **UX-11** (a label a person would actually say out loud beats a category name), **UX-9/UX-16** (fewer competing blocks per screen). | No conflict — this *is* the Mom rule, independently derived. |
| **WCAG 2.2 SC 2.5.8 Target Size (Minimum)** — 24 × 24 CSS px floor, AA ([wcag22aa.org](https://wcag22aa.org/new-criteria/target-size/), [TestParty](https://testparty.ai/blog/wcag-target-guide)); Apple HIG 44 pt, Material 48 dp | 24 px is a legal floor, not a recommendation; platform guidance is nearly double. | **UX-4.** The 30 px ack buttons *pass* WCAG and *fail* the app's own standard (44–52 px everywhere else). Consistency, not compliance, is the argument. | No conflict. Worth naming: **passing 2.5.8 is not evidence of a usable target for this reader.** |
| **WCAG 2.2 SC 2.4.11 Focus Not Obscured** + FAB-overlap critique ([erikkroes.nl](https://www.erikkroes.nl/blog/floating-action-buttons-are-bad-and-what-to-do-instead-1/)) | Fixed overlays cover content and focus; on small viewports sticky elements eat a surprising share of the screen. | **UX-10.** Also **retro-validates** the 2026-07-20 decision to reject a chat-bubble FAB in favour of an edge bookmark — the residual overlap is the same defect at smaller scale, not a new one. | No conflict; the earlier ux call was right and is now under-executed rather than wrong. |
| **Modular type-scale practice, 2025** ([Cieden](https://cieden.com/book/sub-atomic/typography/establishing-a-type-scale), [Imperavi UI Typography](https://imperavi.com/books/ui-typography/principles/modular-scale/)) | Pick one ratio; in dense, content-oriented and dashboard-like UIs use a **low** ratio (1.2 Minor Third) rather than a dramatic one; 16 px body minimum on web, larger on mobile; the point of a scale is to remove the per-element decision. | **§2.2** — the 1.2 / 7-step scale, and the whole framing of W8·b as *install a system*, not *patch a card*. | No conflict; it names why the rainfall inversion happened at all. |
| **iOS Safari input-zoom behaviour** (form controls under 16 px trigger automatic zoom on focus — long-standing WebKit behaviour, unchanged through 2026) | Any `input`/`textarea` below 16 px zooms the viewport on focus. | **UX-1** — a mobile-only defect affecting **all three** text fields, invisible in every desktop review this project has ever run. | No conflict. It is the strongest single argument for the "MOBILE FIRST" instruction Paul gave. |

**A note on evidence class, per the orienting principle.** UX-13, UX-14, UX-17 rest on **explicit** input from
Mom. UX-9, UX-10, UX-12, UX-16, UX-18 rest on **behavioural** signal (`card_expanded` 4/30 d, launcher 0 taps
from her, the composer used unprompted). **UX-1, UX-2, UX-3, UX-4, UX-5, UX-6, UX-7, UX-8, UX-11 rest on
neither** — they are code-verified defects and design judgement, and I am marking them as the weaker evidence
class the brief requires me to mark. Their defence is not that she complained; it is that they are the noise
that makes her complaints hard to interpret.

---

## 7 · Sequencing

**Rule used:** anything that *cleans* the instrument outranks anything that *adds* to it; among cleaners, the
data-loss ones go first; among equals, the cheaper one goes first.

1. **UX-1, UX-2** — the two defects that can lose or tax her actual words. Both S/M, both mobile-only, neither
   on the board before today. *Nothing else in this list is worth measuring until these land.*
2. **UX-3, UX-4, UX-6** — the ack ribbon pass (one visit): the receipt stops looking like a decision, the
   targets reach 44 px, ✓ stops meaning three things. This is the single highest-leverage half-hour in the
   report because it repairs the loop's only hard receipt signal.
3. **UX-5, UX-11** — name the two doors ("about the place" / "tell Paul"). Paul-gated wording; ship together so
   she meets one coherent change, not two.
4. **UX-12, UX-10** — stop the launcher and the tab competing with the card that is asking her something.
5. **UX-15** — build the section-breakdown read. *Do this before step 6*, so the reorder in step 6 has a
   before-and-after.
6. **UX-16, UX-9** — the structural move: asks below the strip, title folded into the card. Take the
   before/after screenshot at 390 px.
7. **UX-13, UX-14** — her two confirmed asks (Journal reachable, rainfall range). These are the *give-back*
   half of the loop and should not slip behind the hygiene work indefinitely; if step 6 stalls, promote these.
8. **UX-7, UX-8** + install the §2.2 scale as the standing rule, and add **"does this surface have `text-lg`
   rules?"** to the landing checklist in `CLAUDE.md` — the same shape as `check-data-inline.py`. Without that
   line, UX-8 will regenerate on the next surface.
9. **UX-17** — serve the second IA card, but **only after `q-top-categories` is answered**.
10. **UX-18** — read the telemetry window on **2026-08-12**. Then, and only then, **UX-19**.

**Track A vs Track B, since the brief asks:** my lens says **Track A's input-stack hygiene outranks all of
Track B except the deadline-bearing items** (B1: GTI spare key / service — a real-world deadline beats
everything, and it is small). The reason is not that Mom's product matters more; it is that Track B's decisions
are made from Paul's own knowledge and are unaffected by measurement noise, whereas **every remaining Track A
decision is currently being made through a corrupted instrument**. Fixing the instrument is therefore the
highest-yield hour available in either track. After that, B6 (household systems) has an unusual claim: it is
the domain **she proposed herself, with its own IA** — it is Track-B-shaped work with Track-A-grade evidence
behind it, and it is one enum value.

---

## 8 · What I could not determine

| Question | What would settle it |
|---|---|
| Whether any note has ever been typed into `＋ Add a note` and lost to the stepper (UX-2). | Nothing records it — a lost draft leaves no trace anywhere. Fix first, instrument second: after UX-2, a `momqueue_note_started` event would make the funnel legible. Do not assume zero. |
| Whether `card_expanded` moves after cards-as-doors (`94d9302`). | The pre-registered read in **UX-18**, on 2026-08-12. |
| Whether the floating tab has ever obstructed a real tap of hers. | Unknowable from the record; UX-10 removes the possibility rather than measuring it. |
| Whether the composer's fused intent ("log" vs "ask") can be separated **without** re-opening the Save/Ask split Paul closed on 2026-07-13. | I don't think it can, and I am **not** proposing to re-open it — the log-first guarantee is correct and the second button was rightly killed. Deriving intent from her text would put AI on the capture path, which is forbidden. **So accept that intent is unmeasurable here**, and measure the *outcome* instead (did she read the reply / continue the thread) rather than the intent. Stated so nobody re-derives the split later as a "measurement fix." |
| Whether the git history matches these status corrections. | I have no shell in this seat. Confirm the 2026-07-26 rainfall commits before retiring the W8·b ① row. |
| Whether her five categories are a nav request or a taxonomy statement. | **UX-17**'s question. My read is taxonomy, and it is the more interesting answer, because it means her instinct and the repo's own Track A/B split agree. |

---

## Appendix — candidate principles (proposed, not applied)

Offered for Paul's confirm; nothing has been written to `~/.claude/design-principles/`.

**1. One channel, one meaning** — *cross-project candidate.*
> **Statement:** Each visual channel (hue, weight, size, container, glyph) encodes exactly one variable across a
> surface; when a second variable needs encoding, use a second channel, never a second value of the first.
> **Why:** Fernwood's rainfall card used blue for both "regional source" and "active/notable," which made the
> source hierarchy unreadable on the one card whose correctness the project had already been burned by. The
> same failure produced three meanings of `✓` in 350 px.
> **When it applies:** any surface carrying data from more than one source, or any surface where a control and
> a status share a palette.
> **Avoid:** state colours drawn from the same family as source colours; a glyph that decorates in one place and
> means something in another.

**2. Label the door, not the room** — *Fernwood, likely generalises.*
> **Statement:** Every surface that accepts input carries a persistent visible label naming what it collects and
> who reads it; no two adjacent input surfaces share a button shape or a fill colour.
> **Why:** five free-text paths in Fernwood post to one endpoint, distinguished in the record by
> `context.section` but not distinguishable by the person choosing between them.
> **When it applies:** whenever a second input affordance is added to a screen that already has one.
> **Avoid:** placeholders as the only label; a category name ("General feedback") where a recipient ("Tell
> Paul") would do.

**3. Install the scale before fixing the instance** — *cross-project candidate.*
> **Statement:** When a typographic defect is found, fix the type system, not the element; a spot fix in a
> project without a scale guarantees the next surface re-creates the defect.
> **Why:** ~700 `font-size` declarations across ~40 values is how a regional model came to outrank a measured
> gauge without anyone choosing that.
> **When it applies:** any hierarchy complaint on a project with more than a handful of surfaces.
