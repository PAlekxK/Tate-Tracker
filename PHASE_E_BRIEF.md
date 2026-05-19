# Phase E — Unified Field Assistant — Feature Brief

**Author:** Claude + Paul · **Date:** 2026-05-19 · **Status:** Draft for expert review · **Repo:** `Tate-Tracker` (project name: Fernwood)

---

## Summary in one paragraph

Replace the dashboard's current Quick Capture surface (a textarea + mic for one-shot observations) with a **unified conversational surface** that handles both observation capture AND back-and-forth chat. The user types or dictates anything into a single top-of-page surface; Claude Haiku classifies the intent and routes:
- **Statement** ("saw a hummingbird at the feeder") → save as a Field Notes observation with inferred category + species
- **Question** ("what plants are in peak right now?") → conversational reply grounded in the property's actual data
- **Ambiguous** → save and ask a one-line follow-up

The assistant has the full property context baked into its system prompt (plants, birds, mammals, amphibians, snakes, lizards, fishing, property notes, recent observations, live weather). It speaks in the field-journal voice that the rest of the dashboard uses, references *this* property specifically, never produces generic best-practices advice.

---

## Why this exists

**Original brief (Paul, 2026-05-18):** *"What I actually want is a field assistant — a conversational interface that already knows this property in depth (every plant, every species, every past observation, the soils, the elevation, the frost dates, the lake) and that I can talk to in plain language, including photo input ('here's a picture of my Azalea. What's wrong with it?'). The structured journal becomes a side effect of the conversation, not the primary surface."*

This is a deliberate product shift. The dashboard today is a calendar + reference: it tells you what *is* happening on the property, organized by data type (Plants card, Wildlife card, Weather card). The field assistant inverts that — instead of you navigating cards to find information, you ask the property and it responds.

The Field Notes capture surface that shipped in Phase D (2026-05-19) was the structured-form version of this vision. Phase E replaces the form with a conversation. The structured-data backbone stays (entries still land in `observations.json` with category + species fields) but the interface to it becomes natural language.

---

## Who uses this

**Primary user — Paul.** Owner-steward of the property. Consulting background, learning-by-building, not a developer by trade. Two distinct use modes:
- **Mobile, in the field.** Phone in one hand, looking at something specific. Voice dictation is the primary input. Wants to capture observations fast and ask spot questions ("what's that bird I just heard?").
- **Desktop, at home.** Sitting with the dashboard, planning, reviewing, asking broader questions ("what should I be doing for the azaleas this month?").

**Secondary user — Paul's mother.** Co-steward; less technical comfort. Daily-glance use to see what's happening at the property. Existing dashboard is already tuned for her glance pattern (the "looking out at the land, not a to-do list" framing in `project_tate_tracker_tone.md` was partly informed by her). For Phase E: the assistant should be approachable enough that she could ask it a question without coaching.

---

## Where it lives in the dashboard

Replaces the current Quick Capture surface at the top of the page, just below the dashboard strip and above the main cards. Same visual footprint, expanded behavior. The existing Field Notes main card (which displays past observations) stays — it's the browse surface; the new unified surface is the input/conversation surface.

Visual placement, top of page:

```
Header (Fernwood · Almanac subtitle · address)
Dashboard strip (Weather / Plants / Wildlife / Sky / Vehicles / Place)
────────
[ Unified field-assistant surface — type or dictate anything ]
────────
Main cards (Weather, Plants, Wildlife, Sky & Stars, Place, Field Notes, Vehicles)
```

---

## What it does (user-visible)

### Statement path (observation save)

1. Paul types or dictates a statement
2. Hits "send" (or voice-stop)
3. Entry appears in the Field Notes card list with a brief "saved" affordance in the unified surface
4. Within ~1-2s, the category chip + species line populate (via the existing `/api/classify` endpoint that already ships)
5. Unified surface clears, ready for the next turn

### Question path (conversational reply)

1. Paul types or dictates a question
2. Hits "send"
3. Assistant's reply appears below the input (in-surface or in a small chat pane that builds)
4. Reply is anchored in *this* property's specific data — plant names, species lists, observation history, current weather
5. Unified surface keeps the conversation visible for follow-up; clears on page refresh (no persistence in v1)

### Ambiguous path

1. Input is unclear ("hummingbird at the feeder")
2. Assistant saves as observation AND offers a one-line follow-up ("Saved that — was it the Ruby-throated, or do you want to talk through the ID?")
3. Paul either confirms / answers the follow-up or moves on

### Error / uncertainty path

- Assistant says so plainly when it doesn't know something specific about this property
- When inferring from limited evidence, names the uncertainty ("looks like it could be lacebug damage — I'd want to see the underside of a leaf to be sure")
- Never recommends a treatment without referencing the plant's existing care calendar in `plants.json`

---

## How it works (system-visible)

### High-level flow per turn

```
1. User types/dictates → unified surface
2. Client POSTs to Worker /api/chat with: {body, sessionContext, propertyContext}
3. Worker calls Claude Haiku with system prompt + conversation messages
4. Claude returns {intent: "statement"|"question"|"ambiguous", reply?, observation?}
5. Client routes:
   - statement → save observation via existing /api/classify path
   - question → render reply in the surface
   - ambiguous → both
```

### Architecture decisions resolved from the 2026-05-19 walkthrough

| Question | Resolved | Rationale |
|---|---|---|
| Q1 Where the surface lives | Top of page, unified | Paul's choice; matches the "field assistant" framing |
| Q3 Context delivery | System-prompt stuffing for v1 | ~30 KB property JSON; prompt caching makes it cheap after turn 1; migrate to tool-use if data grows or queries diverge |
| Q4 Model routing | Haiku 4.5 only | Phase D classifier proven good at intent + species inference; reserve Sonnet/Opus for Phase F image input |
| Q5 Persistence | Session-only (no history across loads) | The journal IS the persistence layer; substantive outputs land as observations |
| Q2 Proactive vs reactive | Reactive only in chat; keep existing `/api/today-line` for proactive | Don't add a second proactive channel |
| Q7 Uncertainty rules | Baked into system prompt | See "Constraints to honor" |
| Q8 Session length | One per page load | Pairs with Q5 |

### Architecture decisions still open (for expert review)

| Question | Why open |
|---|---|
| Q6 Intent routing approach | Most consequential remaining call. Three patterns: (A) classify first then act, (B) always conversational, save on demand, (C) always save, optionally also reply. My lean: A. UX expert + AI advisor should pressure-test this. |
| **How is "save success" surfaced in the unified surface?** | If we clear the textarea on save, the user has no in-surface evidence the save happened. If we don't clear, the surface gets cluttered. Phase D had this same issue and we didn't solve it — relied on the Field Notes card down below. Need a deliberate UX call. |
| **How does the reply pane behave across turns?** | Single growing chat pane? Last-turn-only? Collapsible history? Affects layout, scroll behavior, mobile usability. |
| **Voice-mode flow** | Mic dictation transcribes into the textarea. On voice-stop, do we auto-send, or wait for explicit send? Auto-send is faster but eliminates the proofread step. |
| **Multi-turn coherence** | If turn 2 is "what about the white one?" — does the assistant remember turn 1 was about the azalea? Session-only history (Q5) means yes, but for how many turns until context length forces truncation? |
| **Mom's path** | Does she use the same unified surface, or does the field assistant need a different mode for her? My instinct: same surface, same voice; the field-journal register is already her register. But worth validating. |

---

## Constraints to honor (non-negotiable)

These are settled and should not be expert-debated unless an expert sees a real reason to reopen them.

- **Field-journal voice.** Sand County Almanac register; observational, slow, place-anchored; never directive. See `project_tate_tracker_tone.md` memory and the existing prose throughout the dashboard.
- **Depth filter.** Assistant references only the property's curated scope (the 17 plants, 17 mammals, 16 birds, 12 amphibians, etc. that are actually on the property), not regional completeness. See `feedback_tate_tracker_depth_filter.md`.
- **Worker auth.** All Claude API calls flow through the existing Cloudflare Worker with the `X-Tate-Token` header. No direct browser → Anthropic calls. The `ANTHROPIC_API_KEY` is a Worker secret.
- **Cost ceiling.** Total monthly Claude API spend should stay under $5/month. Haiku at expected volume (a few dozen turns/day) is trivially below that.
- **Never invent property facts.** Don't claim a plant is on the property if `plants.json` doesn't list it. Don't claim an observation happened if `observations.json` doesn't have it.

---

## Out of scope (deferred to later phases)

- **Phase F — Image input.** Photo upload + Claude vision endpoint. Paul wants this ("here's a picture of my Azalea, what's wrong with it?") but it's a separate phase. Don't design around it; design so it's additive later.
- **Phase G — Observations as a knowledge layer.** Field notes feeding back into other dashboard surfaces (Plants peak this week, today-line, Wildlife arriving). Captured in `project_tate_tracker_observations_feedback_loop.md`. Phase E creates the substrate (richer observation data); Phase G consumes it.
- **Persistent multi-device conversation history.** Phase E is session-only; cross-device chat history is a v2 if it turns out to matter.
- **Property map zone awareness.** The map view thread is paused (see `images/property-map/zones.md`). When map zones are stable, the assistant could route questions like "what's planted near the pond" through zone IDs. Out of scope for Phase E v1.

---

## Success criteria — what "this works" looks like

**Behavioral:**
- Paul can dictate "saw a Ruby-throated at the feeder" while walking the property and have it land in the journal correctly classified within ~2 seconds, no manual taps after voice-stop.
- Paul can ask "what's in peak this week?" and get a one-paragraph reply that names the actual plants in peak right now, with no generic horticulture advice.
- The assistant can answer "what bird is most likely calling at dusk in May?" by referencing the property's bird list, not a generic field guide.
- When Paul asks something the assistant doesn't know specifically about *this* property, it says so plainly and offers what it does know.

**Cost / performance:**
- Average turn latency under 3 seconds (Haiku response + render)
- Average cost per turn under $0.005 (Haiku + ~30KB cached property context)
- No cold-start cost worse than a single Claude API call

**Voice:**
- A blind read of 10 conversational replies should be indistinguishable from the existing dashboard prose in register — observational, slow, place-anchored.
- No "Here are 5 tips..." style outputs in any turn.

---

## What I need from each expert

When this brief gets routed to the team of experts, here's what I'd ask each to focus on:

**ux-expert:**
- Pressure-test the intent-routing UX (Q6). Is mode confusion a real risk? What affordances tell the user what mode they're in?
- Save-success feedback in a unified surface — what's the minimum visible cue that doesn't clutter?
- Multi-turn chat layout on mobile (390px wide) — single pane vs. distinct messages
- The "Mom's path" question — does the unified surface work for a less-technical co-user?
- Accessibility — voice dictation + screen-reader compatibility

**ai-advisor:**
- Intent routing approach — A vs B vs C in Q6. What pattern is Claude reliably good at?
- System-prompt stuffing vs tool-use trade-off — what's the real ceiling on stuffing?
- Prompt caching strategy — what stays in the cached prefix vs the per-turn payload
- Multi-turn coherence — context-window management, when to truncate, what to preserve
- Voice/role definition for the assistant — concrete patterns for the field-journal register
- Failure modes specific to AI agents in this kind of role (hallucination of plant facts, over-confident species ID, etc.)

**user-researcher:**
- Jobs the unified surface does for each persona (Paul mobile, Paul desktop, Mom)
- Where the personas diverge in needs / mental models
- Top scenarios where intent ambiguity is likely (what does Paul actually type?)
- Whether the "field assistant" framing matches how Paul thinks of it, or whether there's a more natural framing
- Validation paths — how do we know after launch whether this is doing the job

**engineering-partner:**
- Worker endpoint shape — should `/api/chat` be its own endpoint or unified with `/api/classify`?
- Latency budget — Haiku turn + roundtrip vs. perception threshold
- Cost modeling — turns/day × prompt size × cache hit rate
- Error paths — what happens when the Worker is offline, Claude returns malformed JSON, conversation hits context limit
- How session state lives in the client — single JS object? localStorage? Just DOM?
- Migration path from system-prompt stuffing to tool-use (when does it become worth it)

**content-steward — primary lens: the assistant's conversational voice.** The way the assistant TALKS is a first-class design dimension, not a polish-pass concern. Paul's flagged this explicitly: the chatbot's tone is content-steward's central job here.

- **The assistant's voice end-to-end.** What's the register across multi-turn conversational interactions? Does the Sand County Almanac voice hold up when Claude has to be *helpful* (give information, offer a partial ID, explain a constraint)? Where does the field-journal frame strain, and what's the right adjustment? Concrete prose patterns the system prompt can lock in.
- **Conversational copy patterns** for each path — statement save confirmation, question reply opening, ambiguous follow-up. What does each pattern sound like in this voice, and how do we keep the same voice across all three?
- **Voice patterns for uncertainty** — "I'm not sure but…" vs "looks like it could be…" vs other registers. The depth filter says the assistant should name uncertainty rather than bluff; how does it do so without sounding evasive?
- **How error states are voiced** (Worker offline, classifier failure, low confidence) — without breaking the field-journal frame.
- **Microcopy for the empty state** ("type or dictate anything…" or whatever fits the voice better).
- **Naming pass on the surface itself.** "Field Notes" + "Quick Capture" both feel structural; a name that fits the assistant's identity might serve the conversational register better. (Open thread from earlier today: the "Property card" naming question — the same instinct may apply here.)

---

## Open question for Paul before expert review

- Anything I've described that doesn't match your mental model of what this should be?
- Any constraint I've listed as "non-negotiable" that you'd want to revisit?
- Anything in "Out of scope" that you actually want pulled into Phase E v1?
- The "Mom's path" question — is she actually going to use the assistant, or is the assistant for Paul and Mom keeps using the dashboard's read-only surfaces?

Reply on those (or just say "good, send it out") and I'll spawn the five experts in parallel.
