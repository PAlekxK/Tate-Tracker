---
type: journey
project: fernwood
journey_id: unified-field-assistant
last_updated: 2026-05-19
evidence_level: inferred
performer: [persona-paul-co-steward.md (mobile + desktop modes), persona-mom.md]
sources:
  - Tate-Tracker/PHASE_E_BRIEF.md (2026-05-19)
  - jtbd-talk-to-the-property.md
  - persona-mom.md, persona-paul-co-steward.md, jtbd-invest-time-well.md
---

# Journey — Three performers at the unified field-assistant surface

The unified surface replaces the Quick Capture textbox at the top of the Fernwood dashboard. The same physical surface serves three different journeys. Treating it as one journey would smear genuinely different needs together; treating each as its own card lets the design decisions (affordance, voice, latency, follow-up behavior) be made deliberately per mode.

These are **proto-journeys** — built from the existing personas and Paul's stated use modes in the brief, not from observed behavior. Phase E hasn't shipped. The emotional curves and friction points below should be re-evaluated against real session logs and Mom-direct conversation 30 days after launch.

---

## Journey 1 — Paul-mobile · on the property · voice-primary

The use mode the brief most explicitly calls out. Phone in one hand, often looking at something specific (a plant, a bird heard, a damaged leaf). Voice dictation is the primary input. Tolerance for any extra tap is low — Paul is doing something else with his other hand or his attention.

### Stages

| Stage | Action | Thought | Emotion (-2..+2) | Touchpoint | Friction |
|-------|--------|---------|------------------|------------|----------|
| Notice | Sees / hears something worth marking | "I should remember this" or "what is that?" | +1 | The property itself | None |
| Reach | Pulls phone, opens dashboard (or it's already open) | "I want this captured before I forget" | +1 | Phone home screen / browser | Page load latency; if Mom or Paul-desktop left it on another card the field-assistant surface may not be visible without a scroll |
| Tap-to-talk | Taps mic on unified surface | "Just let me talk" | +1 | Unified field-assistant surface | Mic permission prompt if it's the first time; UI must make the listening state unmistakable |
| Dictate | Speaks observation or question | "Saw a Ruby-throated at the feeder" / "what's that bird calling?" | +1 | Web Speech API → textarea | Dictation accuracy on bird names; the property's curated species list helps but mid-dictation correction is awkward on mobile |
| Send | Voice-stop or explicit send | "Done — go" | 0 | Send button or auto-send on silence | **Open architecture decision in the brief** — auto-send is faster but eliminates proofread; explicit send adds a tap but keeps control. Paul-mobile tilts auto-send. |
| Wait | ~1-3 seconds for classification or reply | "Did it hear me right?" | -1 | The surface, in-between state | This is the danger zone. Without a clear pending state, Paul wonders if it worked. The brief's "save success surfaced in unified surface" open question lives here. |
| Land | Observation appears in Field Notes card below, OR a reply renders in-surface, OR ambiguous follow-up appears | "Got it" / "Oh good, it knew" | +2 | Field Notes card + unified surface | If statement-path: Field Notes card is *below* the surface — Paul has to scroll down to see the entry land, which on mobile is friction. The brief flags this. |
| Continue or pocket | Either dictates the next turn or pockets the phone | "On to the next thing" | +1 | Same surface | If chat history clutters the surface for the next observation, Paul has to clear it or scroll past — depends on the unresolved "reply pane behavior" question |

### Pain points (Paul-mobile)
- `[inferred]` — **The save-success gap.** Statement-path entries land in a card the user can't see without scrolling. Within the unified surface itself, there's no inherent affordance that the save happened. This is *the* most acute mobile friction. Brief Q open.
- `[inferred]` — **Voice-stop ambiguity.** Auto-send vs. explicit send is a real trade-off. Auto-send is faster but unforgiving on dictation errors; explicit send is a tap that costs in the field. Default: lean auto-send with an undo affordance, but this needs UX-expert weigh-in.
- `[inferred]` — **Multi-turn coherence on the trail.** Paul says "saw a hummingbird at the feeder" then immediately "what was the first hummingbird date last year?" — the assistant should hold turn 1 as context. Brief Q5 says session-only; for Paul-mobile this is exactly right.

### Opportunities (Paul-mobile)
- `[inferred]` — A persistent compact "last action" affordance in the unified surface ("Saved · Field Notes ↓") that lets Paul confirm the entry landed without scrolling. Survives 1 turn, then clears.
- `[inferred]` — Voice-mode visual cue that's high-contrast enough to read in outdoor sunlight. Mic pulse is fine indoors; sunlight makes subtle UI states invisible.
- `[inferred]` — Treat the question-path mobile use as a *spot answer* design: short reply (one paragraph max), no embedded lists or expandable sections. Anything longer breaks the field-mode flow.

### Emotional curve summary (Paul-mobile)
Starts positive (the noticing itself is the good moment), dips during the wait state (uncertainty about whether the dictation registered), recovers strongly on land if the affordance is clear. The whole journey should resolve in under 5 seconds elapsed wall-clock to feel right.

---

## Journey 2 — Paul-desktop · at his desk, in Atlanta · question-primary

The planning / researching mode. Paul is at his desk between visits to the property, sitting with the dashboard open, asking the kinds of questions that surface his appreciation-of-place job (research threads on Cherokee history, native keystones, hemlock restoration) alongside spot stewardship questions ("what should I do for the azaleas this month?").

### Stages

| Stage | Action | Thought | Emotion (-2..+2) | Touchpoint | Friction |
|-------|--------|---------|------------------|------------|----------|
| Settle | Opens dashboard at desk, possibly with research context in another tab | "Let me catch up with the property" | +1 | Browser, full desktop | None |
| Browse first | Glances at dashboard strip and cards, may not engage the assistant immediately | "What's happening this week?" | +1 | Dashboard strip, today-line, main cards | Surface competition — the assistant is one option among several. If the dashboard already answered the question via cards, no chat happens. |
| Question forms | Types a question — usually fuller-shaped than mobile ("what should I be thinking about for the azaleas this month?") | "I want to think this through" | +1 | Unified surface, keyboard input | None — desktop typing is fast and accurate |
| Read reply | One paragraph (or possibly two), in-voice, property-specific | "Good, that's grounded — yes that's our azalea, that's our slope" | +2 | Reply pane in unified surface | If reply drifts into generic advice or breaks voice, sharp negative; the field-journal register is doing real work here for Paul-the-builder-user too |
| Follow up | Asks a follow-up ("and the white one?") | "Continue the thread" | +1 | Same surface, multi-turn | Multi-turn coherence is the value here; brief Q5 (session-only) is correct for desktop too |
| Integrate | May copy something out into research notes, or trigger a planned task | "This is going into the plan" | +1 | External (notes app, calendar) or just internal memory | The assistant isn't doing this part — but design implication: the reply should be quotable / copyable cleanly |
| End | Closes browser tab or moves to another card | "Useful, back to work" | +1 | — | None |

### Pain points (Paul-desktop)
- `[inferred]` — **Voice drift on longer replies.** A two-paragraph reply at desktop has more room to slip out of register than the one-sentence mobile reply. The longer the assistant talks, the harder it is to stay in Sand County Almanac voice. This is content-steward territory but a real UX risk too.
- `[inferred]` — **Generic advice creep on research-leaning questions.** "What should I think about for native keystones?" is the kind of question that Claude is very willing to answer generically. The depth filter has to bite hard here. If it doesn't, Paul-the-builder-user is the first one to notice — and the trust hit propagates.
- `[inferred]` — **Where does the conversation go after the surface clears on refresh?** Brief Q5 says no persistence. For desktop's research mode, this may be too strict — Paul mid-research-thread loses the chain on refresh. But persisting changes the surface's identity from "always-fresh field surface" to "chat history with saved sessions," which is a different product. Worth flagging, not changing in v1.

### Opportunities (Paul-desktop)
- `[inferred]` — Treat the desktop reply as the "long-form" voice — closest to the dashboard's existing prose. The reply pane is where the dual-frame identity (`project_tate_tracker_tone.md`) gets its biggest workout per turn.
- `[inferred]` — Lean into the cited-context affordance — if the assistant's reply references a specific plant from `plants.json`, a clickable affordance to the plant's expanded view in the Plants card would close a loop the dashboard's IA can't close from the cards themselves.

### Emotional curve summary (Paul-desktop)
Higher baseline, less dramatic curve. The risk isn't acute friction; it's a slow erosion if voice or specificity drift. Validation has to be qualitative — does the assistant *feel* like it knows the property after 20 turns over a week? Or has it shaded toward generic helpful-AI?

---

## Journey 3 — Mom · bed with coffee, or kitchen / porch · read-mostly, ask-rarely

The most open journey of the three. **Whether Mom uses the assistant at all (vs. only the dashboard's read-only cards) is the brief's flagged open question.** The journey below is the *aspirational* version — what happens if she does engage. The honest read in the research memo below addresses the should-she-or-shouldn't-she question separately.

### Stages

| Stage | Action | Thought | Emotion (-2..+2) | Touchpoint | Friction |
|-------|--------|---------|------------------|------------|----------|
| Wake / wind down | Reaches for phone with coffee or before sleep | "What's happening at the property" | +1 | Phone, in bed | None — this is the leisure-reading mode confirmed by Paul 2026-05-11 |
| Open dashboard | Loads the page | "Let's see" | +1 | Dashboard | None — page-load is the existing UX |
| Glance the strip and today-line | Reads the dashboard strip, the today-line italic banner, maybe scrolls to a card | "Mmm, hummingbirds arriving — and yes I saw one yesterday" | +2 | Dashboard strip, today-line, cards | None — this is the validated existing pattern |
| Notice the assistant surface | Sees the unified field-assistant box at the top | "What's this for?" | 0 | Unified surface | **The make-or-break friction.** If the empty state copy reads as obligation ("Type a question..."), she scrolls past. If it reads as invitation in-voice ("Ask the property anything, or just note what you see"), she may engage. Microcopy here is doing enormous work — content-steward's territory, but a research-finding: this is *the* affordance that decides whether she's a performer of this journey or not. |
| Either engage or skip | If engage: types a question. If skip: continues to cards as usual. | "Let me ask…" / "Not today" | +1 if engage, 0 if skip | Unified surface or cards below | The skip path is not a failure — the cards still work. The engage path has to pay off the curiosity-cost. |
| **If engage** — read reply | Reply appears in voice, short, anchored | "Oh — yes, that's our laurel" | +2 if voice holds; -2 if it slips into generic advice | Unified surface reply | Voice is the load-bearing variable. The reply has to read like the rest of the dashboard. |
| **If engage** — done | Doesn't follow up; this is one-question-and-done leisure mode | "That was nice" | +1 | — | None — but the assistant shouldn't prompt for a follow-up. Pull, not push. |
| Move on | Continues reading or closes phone | "On to the morning" | +1 | — | None |

### Pain points (Mom)
- `[inferred]` — **The empty state is the whole game.** For Paul, the empty-state copy is microcopy; for Mom it's the gate. If she doesn't read the empty state as an invitation in her language, she never becomes a user of this surface. Brief explicitly flags microcopy in content-steward's section.
- `[inferred]` — **Voice and tone matter more here than functionality.** Mom is unlikely to push the assistant on accuracy or stress-test it. She'll engage if it feels like the rest of the dashboard, and disengage quietly if it doesn't. The failure mode is silent.
- `[validated, inline]` — **Cold/clinical voice on an uncertain-Mom question.** This is a distinct failure from generic voice drift. Even when the assistant stays in field-journal register, a purely observational reply lands as detached when Mom's question carries trepidation about doing right by the property. The fix is a tonal flex toward acknowledgment of shared stewardship — not reassurance, not chatbot-cute warmth, but recognition that the reader is figuring this out alongside the journal. (Source: Paul direct 2026-05-20, Garden Guru rubric interview Q6: *"a mentor that also cares about the well-being and beauty of all the plants and everything else we have at the property and even our equipment is what will make a real difference of connection."*)
- `[inferred]` — **No prompts, no follow-ups, no "did this help?" affordances.** The bed/coffee context is leisure mode. Any UI that asks her to engage further pushes against the pull. The assistant should be sticky only on her initiative.
- `[assumption]` — **Not knowing what to say.** A natural-language input box presupposes the user has a formed question. For a bed-with-coffee glance, the user may have *curiosity* but no formed question. Affordance opportunity: see Opportunities below.

### Opportunities (Mom)
- `[inferred]` — **Seeded prompts as scaffolding, not as a menu.** A small set of 2-3 example questions visible under the empty state — *in the assistant's voice* — could lower the "what do I say?" barrier. *"What's blooming this week?" / "What bird is most likely calling now?" / "What should I be watching for?"* — short, in-voice, evocative of the kinds of asking the assistant rewards. The risk is that this looks like a chatbot suggestion chip; the mitigation is voice and restraint.
- `[inferred]` — **Read-mostly is a valid path; design for it explicitly.** The unified surface should look beautiful when *not* being interacted with — the empty state is most of what most users see most of the time. Treating that as an aesthetic surface, not a dormant input, fits the dual-frame identity.
- `[inferred]` — **The first successful engagement is the moment that decides Mom's adoption.** A great answer to her first question gets her to ask a second next week. A generic or off-voice answer means she doesn't try again. This is a research finding the team should know: the assistant has one shot per Mom-user.

### Emotional curve summary (Mom)
Mostly flat-positive (the existing dashboard pattern). The assistant adds a possible spike up (great answer in voice) or a possible quiet drop-out (off-voice answer means she stops trying, doesn't tell anyone). The asymmetry of upside vs. downside is the key research signal.

**Reframed 2026-05-20 (Q11):** the journey's outcome ladder is **dashboard-opened-regularly (pass) → Guru-tried-once (gradient up) → Guru-becomes-pattern (gradient up further)**. *Failure is dashboard-not-opened, full stop.* Mom never engaging the assistant but continuing to open the dashboard is success, not gradient failure. The journey above should not be read as binary pass/fail on Mom-engages-Guru.

---

## Where the journeys overlap

- **The unified surface is shared.** Same physical input, same voice rules, same routing logic. This is the brief's central design choice and it's right — splitting the surface per persona would be over-engineering.
- **All three performers benefit from voice that holds.** A Sand County Almanac register that survives multi-turn is the load-bearing constraint, and it serves all three.
- **All three depend on the depth-filter holding.** No invented plants, no generic advice. This is non-negotiable across modes.
- **Statement-path is identical across modes** — observation in, classified entry out, Field Notes card updated. Mom is unlikely to use statement-path much, but if she does (say, she sees something on the porch and dictates it), it should feel identical.

## Where the journeys diverge

- **Latency tolerance.** Paul-mobile needs <2s perceived response or the field-mode flow breaks. Paul-desktop tolerates 3-5s. Mom tolerates almost anything because she's reading at leisure — but a long wait without a clear pending state will make her *not* engage next time.
- **Reply length and shape.** Paul-mobile wants one-line answers. Paul-desktop wants paragraphs. Mom wants whatever feels like the rest of the dashboard — generally short, prose-shaped, never list-shaped.
- **Engagement intent.** Paul-mobile is task-shaped (capture this, ID that). Paul-desktop is research-shaped (think this through). Mom is browse-shaped (what's happening). The same surface has to serve all three without feeling like it's optimized for any one.
- **The cost of failure.** Paul-mobile shrugs at a bad answer (he'll try again or check the card). Paul-desktop notices voice drift and may surface it as a content-steward issue. Mom silently stops engaging. The silence is the most expensive failure mode.

---

## Evidence log

- `2026-05-19: [inferred] — Tate-Tracker/PHASE_E_BRIEF.md — three use modes (Paul-mobile, Paul-desktop, Mom) are Paul-named in the brief; the journey-level differentiation between them is the user-researcher's read.`
- `2026-05-19: [inferred] — persona-mom.md + persona-paul-co-steward.md — performer details are inherited from the existing personas; this journey extends them into Phase E specifics.`
- `2026-05-11: [validated, inherited] — Paul direct, via persona-mom.md — bed/coffee leisure-reading is a real Mom use mode; the journey 3 framing builds on that confirmed context.`

---

## Open questions (real-user validation pending)

- **Does Mom ever transition from glance-mode to ask-mode?** The whole journey 3 engagement path is currently aspirational. Worker logs and direct conversation post-launch will tell.
- **What's the actual ratio of statement-path to question-path turns?** Brief assumes a healthy mix; in practice Paul-mobile may be 80% statements, Paul-desktop 80% questions, Mom 95% silent. The surface design should hold for all of those.
- **Is the multi-turn coherence Paul wants on desktop the same as what Mom would want?** Hers may be effectively zero (one-and-done). Worth not over-investing in cross-turn cleverness if it doesn't serve her.
- **Does the latency budget hold once Worker + Haiku + render are real?** Brief targets <3s average. If real-world latency lands at 4-5s, Paul-mobile journey degrades hardest.
