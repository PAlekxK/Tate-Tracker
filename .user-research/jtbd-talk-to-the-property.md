---
type: jtbd
project: fernwood
job_id: talk-to-the-property
last_updated: 2026-05-19
evidence_level: inferred
sources:
  - Tate-Tracker/PHASE_E_BRIEF.md (2026-05-19)
  - Tate-Tracker/CLAUDE.md "Forward direction — toward a field assistant"
  - Paul direct quote inside the brief: "What I actually want is a field assistant…" (2026-05-18)
  - persona-mom.md, persona-paul-co-steward.md, jtbd-invest-time-well.md
  - ~/.claude/agent-foundations/_about-paul.md (Fernwood user context)
---

# When I notice or wonder something about *this* place, I want to ask the property in plain language and have it answer — or just speak it once and have the journal hold it — so noticing and knowing stop being two separate acts.

This is a **new, layered job** Phase E introduces on top of the existing joint job (`jtbd-invest-time-well.md`). The underlying motive — invest finite time well on a place that matters — hasn't changed. What changes is the *interaction shape*: today the dashboard answers questions you didn't quite ask by laying out cards; the assistant lets you ask the question you actually have, in the words you'd actually use, and either get an answer or have the moment captured.

The two jobs sit in a stack, not in competition:
- **Outer job (unchanged):** invest time well on a place that matters.
- **Inner job (new):** collapse the gap between *noticing* (or wondering) and *knowing* (or remembering).

If the inner job lands well, the outer job gets stronger. If the inner job feels like another surface to navigate, the outer job is weakened by the friction.

---

## Forces

### Push (pain in current state — what's wrong with the dashboard as it stands)

- `[inferred]` — **The dashboard answers by layout, not by question.** Today you find what's in peak by opening the Plants card and switching to "This Month." You find a bird call by tabbing through Wildlife and reading. The path from "I wonder…" to "the answer" is several clicks and a fair bit of scanning. For Paul-mobile in the field this is genuinely awkward; for Mom in bed with coffee it's a small but real friction that may be the difference between "I'll look" and "I'll just enjoy the morning."
- `[inferred]` — **Capture and recall are two different surfaces.** Phase D shipped a unified capture box, but capture and *asking about what you captured* still live apart. "Did I see a Ruby-throated at the feeder this time last year?" requires opening Field Notes and scrolling. The structured journal is a good substrate but a clumsy reader.
- `[inferred]` — **The depth of context already in the dashboard is invisible at the surface.** Bortle 3 sky, 2,959 ft elevation, May 24 last frost, Hayesville soil, the specific 17 plants on the property — that context informs every card but isn't directly *interrogable*. A user has to know which card encodes which fact. The assistant flips that: the user states the question, the property answers from its own self-knowledge.
- `[validated, inline]` — Paul, 2026-05-18, in the original brief inside `CLAUDE.md`: *"What I actually want is a field assistant — a conversational interface that already knows this property in depth… and that I can talk to in plain language… The structured journal becomes a side effect of the conversation, not the primary surface."* This is Paul naming the push directly.

### Pull (attraction to the new solution)

- `[inferred]` — **One surface, in their own words.** The unified field-assistant box accepts whatever shape the user's thought has — observation, question, half-formed musing — and routes intelligently. The user doesn't have to know which card holds the answer, or whether what they have is a statement or a query. Reduces "where do I go?" to zero.
- `[inferred]` — **Voice + mobile = a true field tool.** Voice dictation already shipped in Phase D. Phase E makes that voice channel two-way: dictate an observation, get a question back, dictate the answer. For Paul standing on the trail looking at something specific, this is qualitatively different from a form modal.
- `[inferred]` — **Property-specific answers, not generic horticulture.** The constraint to never lapse into "here are 5 tips for caring for your azalea" — to always reference *this* azalea, on *this* property, in *this* zone, at *this* elevation — is a real differentiator from anything Mom or Paul could get from a Google search or a generic gardening app. The pull isn't conversational AI in the abstract; it's *this property* being conversational.
- `[validated, inline]` — **For Mom: a property-aware version of the Claude+photos workflow she's already doing.** Mom is already using Claude with image input for plant/wildlife ID and building up context "specific to where our home is and the wildlife and weather there" — that workflow is her "difference maker." Garden Guru's wedge over Claude (for her specifically) is deeper pre-loaded property context, persistent personal library across sessions, and Fernwood-specific UI surfaces tied to the plant cards / wildlife / weather she already references. Without image input (Phase F), Garden Guru is strictly worse than Claude for her stated workflow. (Source: Paul direct 2026-05-20, Garden Guru rubric interview Q4.)
- `[inferred]` — **Memory as ambient depth.** Phase G (observations as a knowledge layer) is the long arc — the assistant grows more useful as the journal accumulates. The pull of Phase E partly is the seed it plants for Phase G: every observation becomes future context. The user senses this even if they don't articulate it ("I noticed something last spring around now…").

### Anxieties (worries holding them back)

- `[inferred]` — **The assistant will get something wrong about the property.** Inventing a plant that isn't there, mis-IDing a bird that *is* on the curated list, citing a frost date that's not the property-calibrated one — any of these breaks the trust that the assistant *knows this place*. The depth filter and "never invent property facts" constraints in the brief address this, but the anxiety remains: a single confident-wrong answer is more damaging here than ten useful ones are valuable.
- `[inferred]` — **The voice will break.** The field-journal register is load-bearing for the project's identity. If the assistant slips into productivity-app voice ("Here are 3 things to do for your azaleas this week!") in the middle of an otherwise good conversation, the dual-frame identity (`project_tate_tracker_tone.md`) erodes turn by turn. This is more acute for Mom — she's the make-or-break user, and the voice is partly what earns the app's place in her morning routine.
- `[validated, inline]` — **For Mom: a voice that's correct but cold.** A distinct failure mode from "voice will break." Even when the assistant stays in the field-journal register, a purely observational reply lands as detached when Mom's question carries trepidation about doing right by the property. She has named the fix: *"a mentor that also cares about the well-being and beauty of all the plants and everything else we have at the property and even our equipment."* Not reassurance, not chatbot-cute warmth, but acknowledgment that the reader is figuring this out alongside the journal. Addressed in the 2026-05-20 charter principle [Acknowledge the shared work — for uncertain readers]. (Source: Paul direct 2026-05-20, Garden Guru rubric interview Q6.)
- `[inferred]` — **The conversation will feel like an obligation.** A chat surface that keeps growing, or that "remembers" too much across turns, or that prompts follow-ups in a way that feels like it wants you to engage further — slides toward chore. Especially dangerous given anxiety #1 in the parent JTBD ("the app itself becomes a chore"). The new conversational layer multiplies that risk.
- `[inferred]` — **For Paul: building a feature that's brilliant for him and confusing for Mom.** The builder-user bias (cross-project pattern; see `tate-tracker.md`) is more dangerous here than usual. A natural-language interface is *Paul's* native idiom — he's a strategy consultant who reasons in language. It's not necessarily Mom's. Designing Phase E without separating the two use modes is a structural risk.
- `[assumption]` — **For Mom specifically: not knowing what to say.** A blank conversational box is an open prompt — and a low-attention bed-with-coffee user may simply not know what the right input shape is. The empty-state copy and the affordance design matter disproportionately for her.

### Habits / inertia (what makes change hard)

- `[inferred]` — **The dashboard already works.** Phase A through Phase C2 shipped a card-based reference that does the appreciation half of the joint job well. Mom may already have a working pattern (open the dashboard, glance, close). Phase E has to be additive enough to that pattern that it doesn't displace what's working.
- `[inferred]` — **Voice dictation is still new.** Paul shipped it in Phase D on 2026-05-19; there isn't a year of muscle memory. The conversational layer is being introduced before the capture layer has settled. There's a real chance that Paul-mobile patterns will form *during* Phase E, not before — meaning Phase E partly *creates* the habit it has to fit into.
- `[inferred]` — **Conversational AI has its own UX baggage.** Both users have likely used ChatGPT, Siri, or similar. They bring expectations from those — including the bad ones (rambly replies, hallucinations, generic advice). The assistant has to defeat those expectations early to be trusted.

---

## Performers

Three performers, one job — but the *shape* of how they perform it differs enough that journey-level treatment matters. See `journey-unified-field-assistant.md`.

- **Paul-mobile** — on the property, phone in hand, voice-primary. Highest tolerance for terse turns, lowest tolerance for latency or multi-tap flows. Statement-path traffic dominates; question-path is spot-ID and quick lookups ("what's that bird I just heard?").
- **Paul-desktop** — at his desk in Atlanta, planning or researching. Question-path dominates; statements are rarer and more deliberate. Tolerance for longer replies and follow-up exchanges is high. The mode that looks most like a "chat" in the conventional sense.
- **Mom** — bed/coffee or kitchen/porch, phone. Lowest tolerance for any sense of obligation; highest sensitivity to voice/tone. The performer the assistant has to earn its place with. Whether she uses the assistant at all (vs. continues using the dashboard's read-only surfaces) is the open question of Phase E. See `journey-unified-field-assistant.md` and the research memo accompanying these artifacts.

[See persona-mom.md and persona-paul-co-steward.md for full performer profiles.]

---

## Evidence log

- `2026-05-20: [validated, inline] — Paul direct, Garden Guru rubric interview Q4 — Mom is a Claude power-user already doing the photos-for-ID + context-building workflow. Garden Guru without image input (Phase F) is strictly worse than what she already has. Wedge over Claude = deeper pre-loaded property context + persistent personal library + Fernwood-specific UI tied to cards she already references.`
- `2026-05-20: [validated, inline] — Paul direct, Garden Guru rubric interview Q6 — distinct anxiety surfaced: voice that is correct but cold. Mom's trepidation about doing things wrong means a purely observational reply lands detached. Charter principle added 2026-05-20: "Acknowledge the shared work — for uncertain readers."`
- `2026-05-20: [validated, inline] — Paul direct, Garden Guru rubric interview Q11 — dashboard engagement = load-bearing metric; Guru engagement = gradient. Reshapes the "Mom column" of any evaluation rubric.`
- `2026-05-19: [validated, inline] — Paul direct in PHASE_E_BRIEF.md and CLAUDE.md, "Forward direction" section — Paul explicitly named the field-assistant vision and the structured-journal-as-side-effect framing. This is the seed claim for the entire JTBD.`
- `2026-05-19: [inferred] — Brief + dashboard architecture — the dashboard-answers-by-layout push force is visible structurally; the dashboard's card-based information architecture is real and the new surface is positioned as an inversion.`
- `2026-05-19: [inferred] — persona-mom.md + persona-paul-co-steward.md — the three performers and their distinct shapes of the job are extrapolated from the existing personas; tag is inferred because the Phase E use modes themselves haven't been observed yet (nothing has shipped).`
- `2026-05-11: [validated, inherited] — Paul direct, via jtbd-invest-time-well — the parent job ("invest time well") and the anxiety that the app itself becomes a chore. Inherited here because Phase E sits inside that parent job.`

---

## Open questions (real-user validation pending)

- **Does Mom ever ask the assistant a question, or does she only read?** This is the core "Mom's path" open question from the brief. The split would be visible in Worker logs within ~30 days post-launch (sessions originating from her device that hit `/api/chat` vs. only loading the dashboard).
- **Which path is Paul's dominant traffic — statement or question?** Brief assumes a healthy mix; in practice one may dominate, which has implications for the surface's affordance hierarchy (is it primarily a capture box that also answers, or primarily a chat that also captures?).
- **Does the assistant feel different enough from "another AI chatbot" to defeat the ChatGPT-baggage expectation?** Validation path is qualitative: ask Paul and Mom independently after ~2 weeks of use, "what does it remind you of?" Hoped-for answer: not ChatGPT, not Siri — something more like "asking the property."
- **Do the three performers' jobs actually diverge enough to warrant three journey treatments, or is the differentiation smaller in practice?** Worth re-examining after a month of mixed-mode use.
