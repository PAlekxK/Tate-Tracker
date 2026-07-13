---
type: research-review
project: fernwood
artifact_id: mom-feedback-queue-2026-07-13
date: 2026-07-13
discipline: user-researcher
evidence_level: grounded in 40-day behavior read + 6-day telemetry rollup + persona
recommendation: SHIP-NARROWED (a single contextual confirm as a signal probe; NOT the full queue)
sources:
  - .user-research/2026-07-02-mom-behavior-interpretation.md
  - .user-research/2026-07-02-garden-guru-conversation-analysis.md
  - .user-research/persona-mom.md
  - .user-research/2026-05-28-mom-discovery-interview-guide.md
  - .user-research/2026-05-28-reading-the-output.md
  - CLAUDE.md (governing glance/repository/loop principle; Outstanding-for-Paul backlog)
---

# Mom's in-app feedback / confirmation queue — user-research review

## Bottom line up front

**Ship, but not the queue.** Ship **one real confirm question, on one real plant, in the surface Mom already scans, instrumented as a go/no-go gate.** The full three-feed queue (confirms + change-reactions + open feedback) is not yet warranted by evidence, and its default shape — "a digestible queue of what's outstanding for her" — is the exact silhouette of the affordances that have gone to zero on this project. Prove she'll answer one contextual confirm before building the machine that serves them in bulk.

This is not caution for its own sake. It's the same discipline the project has already applied correctly twice: photo-add was validated before text-add was gated (`.engineering/2026-06-20-path-text-path-add.md`), and the discovery interview was set up as *the gate* before building. A confirm probe is the cheapest possible version of that same gate.

---

## The evidence, read straight

### What Mom actually does (validated)
- **Durable daily user.** Active 27 of ~40 days through 7/02, scanning cards — `card_section_viewed` is ~57% of her events. Plants and Weather are her most-opened cards. The dashboard glance carries her job.
- **She engages affordances that sit on a path she's already walking.** The A/A+ text-size toggle (22 events, the *only* device that touches it), attaching photos to Garden Guru, asking stewardship questions, promoting a species. When an affordance is on the road she's already on, she uses it.
- **Her "input" behavior is conversational, not curatorial.** Every time Mom has tried to *give* the property something — add creeping fig (5/28), log the lily-pad dieback (7/02) — she did it *through Garden Guru, in her own words*, mid-question. Both attempts dead-ended and became Paul's manual work. She has never once expressed input through a passive dashboard control.

### What Mom demonstrably ignores (validated)
- **The star: 0 uses across 55 revisits on her device (0/104 all-devices).**
- **Seeded prompts: 0.**
- **The 5-turn cap: never fired.**

The instructive part is *why* these went to zero, because the reasons are not identical and they draw the line for this feature:
- The **star** is zero because it's a **standing, discoverable control she has to notice and choose to operate** — and because revisit already *is* her curation (tapping a star to also say "I value this" is redundant). Wrong model, not just invisible.
- The **single-turn ceiling** turned out **not** to be disposition — the one follow-up in the whole corpus was her *trying to continue* and hitting a dead-ending UI. "Doesn't follow up" ≠ "doesn't want to."

**The synthesis that governs this review:** Mom does not fail to engage because she's passive. She fails to engage with **standing affordances that wait to be discovered on a surface she's not already using for that purpose.** She *does* engage when the affordance rides her existing path — the card scan, or the Garden Guru turn. A "queue" is, by construction, a standing affordance that waits to be discovered. That is the trap. The confirms themselves are gold; the *queue container* is the risk.

---

## Confronting the tension the brief names

**"Is a passive queue Mom should react to realistic, given she opens the app rarely and doesn't explore?"**

No — not as a queue. Three reasons, all from the evidence:

1. **A queue is a list, and a list is a to-do surface.** The persona's hardest line is the anti-persona: not the productivity user who wants checklists and things-to-clear. "3 items outstanding for you" is "3 alerts" wearing a cardigan. It reads as being managed, which the persona says will *close* the app, not open it.
2. **A standing container has to be discovered.** She scans Plants and Weather. A new "For you / Outstanding" card or tab is one more thing to find, and the star proves she doesn't hunt for controls. The confirm has to be *where her eyes already land*, not in a room she has to walk into.
3. **She opens the app in a low-attention, one-handed, no-glasses, bed/coffee posture.** The realistic interaction budget is *one tap on one thing she happens to be looking at* — not "work through a list."

**So how should the mechanism reach her?** Ride the two paths she already walks, in priority order:

- **Primary — contextual, inline, one at a time, on the plant it's about.** When Mom opens the Plants card (her most-used surface) and the crocosmia entry is in view, the question about the crocosmia rides *there*, on that entry, as a single calm line with a tap: *"Paul isn't sure of the variety here — does 'Lucifer' match what's planted, or is it something else?"* She's already looking at the crocosmia. The question costs her nothing to find. This is the "Worth noticing today" pattern (`computeLookFors`/`renderTodayGlance`) applied to confirms — a proven surface she's shown to look at, reusing `.tag.t-{type}` pills per constraint.
- **Secondary / fold-back — Garden Guru.** Her *proven* input channel. If she'd rather tell it in words, the confirm can also be answerable via a Guru fence (the `suggest-*` pattern), logging her verbatim answer. This is where she already tries to log and confirm, so it's a natural catch-basin — but it requires her to *open Guru*, a deeper act than glancing at a card, so it's the second road, not the first.

**What NOT to use to reach her:**
- **A push notification** is the anti-trigger by name in the persona ("a notification telling her something is 'due'… will close the app, not open it"). Do not notify.
- **Piggybacking on claude.ai** is where she goes for depth, but it's her personal Claude with no write-back path into Fernwood canon. Interesting long-term, out of scope for anything we control. Reject for v1.

---

## The smallest thing that generates real signal (the actual recommendation)

Before building any queue, ship **exactly one confirm**, and let it answer the only question that matters: *will Mom answer a contextual confirm at all?*

**The probe (v1 MVP):**
- Take **one** live, real backlog confirm — the **crocosmia = 'Lucifer'?** question is perfect (real, binary-ish, currently a residual owner-Paul item, and the plant is blooming on-property *right now* so it's freshly relevant — the flywheel's "fresh localized signal" hook).
- Render it as a single calm line **on the crocosmia entry inside the Plants card**, styled with existing pills, no new badge pattern, no counter, no "outstanding" language.
- Three honest branches (see phrasing below): a tap for each of *matches / it's something else / not sure*, plus an optional "add a note" that opens the **deterministic, AI-free verbatim capture** path (ObservationStore pattern, `fnSaveNoteOnVehicle` analog tagged to `plantId`).
- Her answer writes to a lean KV queue Paul reads later — reuse the **`zone-feedback` GET pattern** (user captures → `status: pending` → Paul picks up), *not* a new endpoint. The `/api/feedback` substrate also works; either is fine, don't build a third.
- Instrument the **full funnel**: `confirm_offered` (it was rendered) → `confirm_viewed` (the Plants card / entry was actually expanded while the confirm was present) → `confirm_tapped` → `confirm_answered_with_note`.

That offered→viewed→tapped funnel is the whole point. It's the instrumentation the star never had: it distinguishes **"she never saw it"** from **"she saw it and ignored it"** — the exact ambiguity that made the star's zero uninterpretable for weeks. This time we'll *know* which failure (or success) we're looking at.

**Why one and not three-or-four:** if the first contextual confirm gets a genuine answer, the mechanism is validated and you scale it to the rest of the backlog for near-zero marginal cost. If it gets a clean offered-but-never-tapped zero across ~2–3 weeks of real exposure, you have saved yourself from building — and asking Mom to live alongside — the next star. One probe is decisive either way; three feeds is a bet placed before the table's been read.

---

## Research-instrument quality: how to phrase a confirm so the answer is usable

Each confirm is a one-item survey with N=1 and no interviewer to repair a bad question. Apply the Mom-Test rules the interview guide already established:

1. **Offer the deflating branch as openly as the confirming one.** "Is this crocosmia 'Lucifer'?" leads — yes is the easy, agreeable tap, and an agreeable tap from a warm mother-to-son relationship is near-worthless as ground-truth. Phrase it three-way: **matches / it's a different variety / not sure.** "Not sure" must be a first-class, no-shame answer, because *"not sure"* is itself true, usable ground-truth (it tells Paul the ID can't be closed from Mom's knowledge and needs the plant tag).
2. **Ask about the thing in front of her, never a hypothetical.** She's looking at the actual crocosmia. Good. Never ask "would you like a feature that…".
3. **Attribute the uncertainty to Paul/the app, not to her.** "*Paul read this from a photo and isn't certain*" frames it as helping close *his* open question, not testing *her* knowledge. Lowers the stakes, raises honesty.
4. **A bare tap is low-fidelity — know that going in.** A "matches" tap doesn't tell you whether she *knows* it's Lucifer or just agreed. That's the ceiling of a tap-only confirm, and it's an acceptable ceiling for closing photo-read IDs — but for anything where *why* matters, the optional verbatim note is where the real signal lives. Design the note as invited, never required (required text kills the bed-posture interaction).
5. **One confirm visible at a time.** Never stack them. Two questions on one card is a list, and a list is the thing we're avoiding.

**Worked example (hand to content-steward for final voice):**
> *On the crocosmia entry:* "Paul read this as 'Lucifer' from a photo and wasn't sure. Does that match what's actually planted here?"
> Taps: **Yes, that's it** · **No, it's different** · **Not sure** · *(add a note ›)*

---

## How the emailed interview maps into this — gained and lost

Worth stating plainly: **the heavyweight emailed interview never came back.** Sent 2026-05-29, refreshed 6/20 and 6/21, still awaited in the 7/13 CLAUDE.md. That is itself a finding: **the out-of-band, separate-sitting, 30-minute ask exceeded what Mom will do.** It is direct evidence *for* moving feedback into her existing app cadence, where the activation energy is one tap during a session she was already going to have.

But the queue does **not** replace the interview — it replaces one slice of it:

**Gained by the in-app confirm:**
- Rides her real cadence instead of demanding a separate ritual she hasn't performed in six weeks.
- Contextual — the question sits on the actual plant, so she answers from what's in front of her, not from memory.
- Incremental and fresh — answers arrive as she opens the app, timed to when the plant is in season.
- Closes the loop *visibly* (the flywheel requirement): when she confirms 'Lucifer', that has to *show up* — the entry updates, the uncertainty flag clears. She must see her word land, or it's extractive.

**Lost, and not recoverable in a queue:**
- **No probing or follow-up.** A confirm answers only what we already knew to ask. It cannot chase an ambiguous answer or ask "why."
- **No open discovery.** The interview's highest value was surfacing jobs *she didn't know to mention* (Job 7 look-ahead, the lily-pad log-a-seasonal-change job). A confirm can't discover a new job; it can only close a known one.
- **The four in-her-head questions still need a live conversation.** Q1–Q4 in `2026-07-02-mom-behavior-interpretation.md` (did she have a follow-up in mind? what did she think "log it" did? tell-vs-ask? has she tried to continue?) are about *what's happening in her head at the moment of use* — a tap can't answer any of them. **Do not let the confirm feature close the discovery-interview thread.** They serve different jobs; the confirm handles factual ground-truth, the interview handles mental-model discovery.

**Mapping rule:** route to the confirm queue only items that are **binary/factual and property-observable** ("is this Lucifer?", "did the panicle hydrangea bloom yet?"). Keep everything requiring *why*, *how it felt*, or *what she'd want* for a live conversation.

---

## The three feeds, ranked by evidence

The brief proposes three feeds merging into one queue. They are not equal:

1. **Plant-ID / ground-truth confirms — SHIP (as the probe).** Highest evidence. Real recurring backlog (Outstanding-for-Paul is full of them), flywheel-aligned ("the one input only someone at the property can give"), binary, contextual, low-friction. This is the whole justified feature.

2. **Change-reactions ("does the hydrangea hub match the property?") — DEFER.** Weaker on three counts: (a) it asks her to react to *Paul's reorganization* in the abstract, holding a change in mind rather than looking at a thing — higher cognitive load, wrong for bed posture; (b) it's **Paul-want-shaped** — Paul wants validation that his restructure landed, which is the leading-the-witness trap the interview guide explicitly warns against (recall Scenario D / Job 10 were cut for exactly this); (c) release notes are already the "changes we shipped" surface and get near-zero attention. Revisit only *after* confirms prove engagement, and even then phrase as an observable ("does the property have a paniculata hydrangea like this one?") not a design review ("do you like the new hub?").

3. **Open general feedback — DON'T BUILD.** This is the 🚩 meta-feedback channel whose validation gate the interview was supposed to close and never did. The standing "leave feedback" box is the textbook zero-usage affordance — a discoverable control on a surface she doesn't visit for that purpose, i.e. the star all over again. The `reading-the-output` doc's own middle branch is the likely truth: if Mom has feedback, she tells Paul out-of-band (text/call/in person), and *that's fine*. Do not build in-app infrastructure for a behavior that happens over the phone. Kill or hold indefinitely.

---

## Success and kill metrics

**The gate (v1 probe, ~2–3 week window of real exposure):**
- **Grow / validated:** Mom (`d-14nyhnjz`) answers ≥1 confirm — tap *or* note — on a day the confirm was `viewed`. Even one genuine "not sure" counts; it's usable ground-truth and proves the interaction is in her repertoire. → Scale to the rest of the backlog; reconsider feed #2.
- **Kill:** `confirm_offered` and `confirm_viewed` both firing repeatedly (she opened the Plants card with the confirm present, multiple sessions) with **zero `confirm_tapped`** across ~2–3 weeks. That is the star's fingerprint: seen and declined. → It's the next dead affordance. Stop; do not build the queue; the backlog stays Paul's manual work or waits for a live conversation.
- **Ambiguous (don't over-read):** high `offered`, low `viewed` — she just didn't open the crocosmia entry / it wasn't in season / she wasn't in the app much. Not a rejection; extend the window or move the confirm to a higher-traffic entry. The funnel is designed precisely so we can tell this from a real decline.

**Guardrail (health, not success):** if answers come in but skew almost entirely "matches" with no notes and no "not sure," treat that as *possible agreeableness artifact*, not clean validation — sanity-check a couple against the ground truth (plant tags) before trusting the mechanism for canon-affecting confirms.

---

## Anticipated disagreements with the other lenses

- **ux-expert** will likely want the unified *queue surface* for coherence — one place all outstanding items live. I'll push back: a standing queue card/tab is the discoverable-container trap; the evidence says contextual-inline-on-the-entry beats a dedicated surface for this user. Where we'll agree: reuse "Worth noticing today"/`renderTodayGlance` machinery and existing pills. Where we may still differ: I want strictly **one confirm visible at a time**, never a rendered list, even if ux wants to show "2 more."
- **engineering-partner** will want to build the general data model once — `questions.json` + merged feed + pickup endpoint. I agree the *storage substrate* should be lean and forward-compatible (reuse `zone-feedback` or `/api/feedback` KV; a small `forMom`/`momConfirm` field on the plant entry is fine), but I'll argue hard against building the **merge/queue UI** before the probe returns. Model can be general; the surface must be one question.
- **ai-advisor** may argue for routing confirms through Garden Guru as primary, since that's her *proven* input channel. It's a genuinely strong alternative and I'd name it as the co-leading option — with one caveat: opening Guru is a deeper act than glancing at a card, and card-scan is her higher-traffic surface, so I lean contextual-on-card as *primary* and Guru as the verbatim fold-back path. Full agreement on: capture stays AI-free, the fence carries only metadata, the record is her words.
- **content-steward** — likely agreement on voice; the one place I'll hold firm even against warmth is preserving the **"not sure" / deflating branch** and the Paul-attributed framing. A confirm that's too warm-and-agreeable produces unusable ground-truth. Signal integrity beats coziness here.

---

## Evidence log
- `2026-07-13: [validated] — Zero-usage affordances (star 0/55 revisits, seeded prompts 0, cap never fired) are all standing/discoverable controls on surfaces not walked for that purpose; contrasted with used affordances (text-size toggle, photo-attach, Guru asks) which ride her existing path. Basis for the "container is the risk, confirm is the gold" split.`
- `2026-07-13: [validated] — Every Mom input attempt (creeping fig 5/28, lily-pad 7/02) was conversational via Garden Guru, never via a passive control; both dead-ended into Paul's manual work. Supports contextual/Guru delivery over a queue container.`
- `2026-07-13: [inferred, strong] — The emailed discovery interview never returned (sent 5/29, refreshed 6/20 + 6/21, still awaited 7/13). Direct evidence the heavyweight out-of-band ask exceeds Mom's willingness; supports in-cadence in-app capture.`
- `2026-07-13: [design-decision] — Recommend SHIP-NARROWED: one contextual confirm (crocosmia='Lucifer'?) as an instrumented go/no-go probe; defer change-reactions; do not build open feedback. Kill metric = offered+viewed firing with zero tapped over ~2–3 weeks.`
</content>
</invoke>
