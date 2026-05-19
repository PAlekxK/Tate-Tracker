# Phase E — Conversational layer design questions

A field assistant Paul can talk to in plain language about Fernwood. Knows every plant, species, observation, soil note, frost date, microclimate quirk, and the live weather state. Built on top of the Phase D capture UX (already shipped).

This doc surfaces the open design questions so they can be decided before code is written. It does **not** answer them.

---

## What "good" looks like (from the original brief)

Paul: *"Here's a picture of my Azalea. What's wrong with it?"*

The assistant doesn't lapse into "Here are 5 tips for caring for your Azalea." It speaks as someone who knows *this* azalea on *this* property — soil pH, the south-facing slope, the white-pine canopy that filters afternoon sun, the lacebug pressure last August, the time Paul noted yellow margins in 2025 that turned out to be iron chlorosis.

Field-journal voice. Slow. Place-anchored. No bullet lists, no generic best-practices, no "consult a local expert."

---

## Open questions

### 1. Where does the chat surface live?

| Option | Pros | Cons |
|---|---|---|
| **A. Inside the Field Notes card** — chat appears below (or replaces) the capture textarea | Closest to current architecture; cards stay organized | Chat history scrolls inside a card; doesn't feel like the primary surface |
| **B. Top-of-page chat surface** — above all main cards | Implies "this is the front door"; matches the field-assistant framing | Reorganizes the whole layout; not all sessions need chat |
| **C. Dedicated tab / view** — toggle between "dashboard" and "ask" | Clean separation; each surface keeps its purpose | Two paths feels like productivity-app convention, against the field-journal tone |
| **D. Replace Field Notes entirely** — capture flows from the chat | Most ambitious; structured entries become chat side-effects | Highest risk; loses the "look back at past entries" affordance unless re-built |

**Bias toward:** A or B. C feels off-brand; D is too big for one phase.

### 2. Does the assistant initiate, or only respond?

Two stances:

**Reactive only** — assistant says nothing until Paul asks something. Predictable, low surface, never noise.

**Proactive — "today" register** — assistant offers a one-line opening when the dashboard loads ("the laurel's just about to open by the spring; the bats came back to the pond this week"). Already a partial overlap with the existing `today-line` Claude call.

Hybrid is possible: keep the today-line, no other proactive turns.

### 3. How is context delivered to Claude?

Two paths, both real:

**A. Stuff everything into the system prompt.**
- One large system prompt at session start containing the full schema of plants.json, birds.json, mammals.json, amphibians.json, snakes.json, lizards.json, fishing.json, property.json, plus the current weather state and recent observations.
- Pro: model has perfect recall every turn.
- Con: ~30-50 KB of context per turn (cached after the first turn — see prompt caching). Cost is reasonable. Limits the upper ceiling of context size as data grows.

**B. Tool-use.**
- Compact system prompt that says "you can call these tools." Tools: `get_plant(id)`, `list_plants_in_peak()`, `get_bird(id)`, `get_weather_current()`, `get_observations(category?, since?)`, `search_observations(query)`.
- Pro: scales with data growth; model fetches only what's needed.
- Con: more code to write and maintain; some turns now require multiple round trips.

**Bias toward:** B (tool-use) — better long-term shape. But could start with A as a smoke test before investing in tool-use plumbing.

### 4. Which model on which turn?

Cost-quality trade-off:

- **Haiku 4.5** — ~$0.001 per turn at this context size. Fast (~1-2s). Loses ground on long reasoning chains.
- **Sonnet 4.6** — ~$0.01 per turn. Slower (~3-5s). Stronger reasoning.
- **Opus 4.7** — ~$0.05 per turn. Slowest. Best at synthesis-heavy turns.

Routing options:
- All Haiku
- Haiku for short factual turns, Sonnet for synthesis ("what should I plant by the seep?")
- Haiku for everything except image input (Phase F), which would always be Sonnet+

**Bias toward:** Haiku as the default; Sonnet only when the model itself escalates ("this question needs more reasoning, give me the bigger model"). That's a self-routing pattern worth a prototype.

### 5. How is conversation state persisted?

Options:

**A. localStorage only.** Conversations live on the device that started them. Closing the tab = losing history.

**B. Cloudflare KV (alongside observations).** Conversations sync across devices. Adds storage growth.

**C. None — conversation is ephemeral per session.** No history at all. Each refresh starts fresh.

**Bias toward:** A or C. The journal IS the persistence layer (observations get written via the conversation as a side-effect, per the field-assistant framing). Chat history itself doesn't need to persist if the substantive outputs land as observations.

### 6. Does the conversation write observations?

The field-assistant framing says: yes, the structured journal becomes a side-effect of the conversation.

**Concrete pattern:**
- Paul says "I saw three goldfinches at the feeder this morning"
- Assistant: acknowledges, asks if he wants to record it, OR records it silently and confirms
- Either way, a new entry lands in the Field Notes list with category=`birds`, species=`American Goldfinch`

**Open questions:**
- Silent auto-save vs. explicit "save this as an entry?" prompt?
- What about turns that are clearly questions, not observations ("when does the laurel usually open?")? Don't save those.
- The classifier from Phase D could be reused — if the model thinks this turn is observation-shaped, save it.

### 7. How does the assistant handle uncertainty?

The field-journal voice doesn't bullshit. Two failure modes to avoid:

- **Generic best-practices fallback.** "Azaleas generally prefer acidic soil..." — wrong register, wrong scope.
- **Confident hallucination.** "Your azalea is showing iron chlorosis based on the photo" when it can't actually tell.

Rules to bake into the system prompt:
- When you don't know something specific about this property, say so plainly.
- When making an inference from limited evidence, name the uncertainty: "this looks like it could be lacebug damage — I'd want to see the underside of a leaf to be sure."
- Never recommend a treatment without referencing what's already on the property's care calendar.

### 8. How long is a "session"?

Two patterns:

**A. One session per page load.** Refreshing the page = fresh assistant. Simple.

**B. Persistent sessions across loads** (with localStorage history). Continuity across days.

Real talk: Paul will probably use this from his phone in the yard 80% of the time. Sessions there are short, focused, often image-driven. The continuity case ("I asked about the azalea two weeks ago, what did you say?") might matter sometimes but probably not as primary surface.

**Bias toward:** A.

### 9. What's the minimum viable demo?

To validate the direction before committing 2-3 sessions of build:

**MVP scope:**
- One chat surface (decide location per Q1)
- All-Haiku, no model routing
- System-prompt stuffing (no tool-use yet) — just plants.json + property.json + recent observations
- No image input (defer to Phase F)
- localStorage-only history (or none)
- No auto-save observations (manual via Phase D capture remains primary)

If MVP works qualitatively (the assistant sounds like it knows the property), invest in tool-use + observation write-back.

If MVP doesn't work, the rewrite path is much narrower.

---

## Things that are NOT open questions

- **Field-journal voice.** This is non-negotiable. Same voice rules as the rest of the site (see `[[project_tate_tracker_tone]]` and the Sand County Almanac touchstone).
- **Depth filter.** The assistant only references the property's curated scope (17 plants, 17 mammals, etc.), not regional completeness.
- **Worker auth.** Anything that calls Claude goes through the existing Worker with `X-Tate-Token`. No direct browser → Anthropic API calls.
- **Cost ceiling.** Stay under $5/month. Haiku at expected volume keeps this trivial; Sonnet routing changes the math.

---

## When you're ready to build

The first session of build work, in suggested order:

1. **Decide Q1 (surface placement) and Q9 (MVP scope) explicitly.** Write the decisions in this doc before opening code.
2. **Worker:** add `/api/chat` endpoint (similar shape to `/api/today-line` and `/api/classify` already shipped). System prompt + messages array + return assistant message. No tool-use in MVP.
3. **Client:** build the chat surface chosen in Q1. Send `{messages: [...]}` to `/api/chat`, append the response, scroll into view.
4. **Test:** ask the assistant 5-10 representative questions ("what plants are in peak right now," "should I be worried about the azalea leaves," "what bird is most likely calling at dusk in May") and check if the answers actually use the property's specific data.
5. **Iterate the system prompt until the voice and groundedness feel right.** This is the hardest part. Expect 4-8 iterations.

If MVP holds, the next session is tool-use + observation write-back. If MVP doesn't hold, the iteration above is where most of the work lives.

---

## Adjacent thread — observations as a knowledge layer (Phase G)

Raised by Paul on 2026-05-19 right after the capture-surface promotion: field notes shouldn't just be a log, they should feed back into the rest of the dashboard's surfaces and sharpen recommendations over time. ("You noted the laurel opening April 25 last year — watch for it now.")

This is a strict superset of what Q3 and Q6 already cover for the assistant — but it extends to non-chat surfaces (Plants peak, today-line, burn status, Wildlife). It is NOT the same as Phase E. Don't build it until E lands and the observation set is rich enough (~50+ entries) to be useful.

Design Phase E's context layer so it doesn't fight this future. Specifically: store observations in a shape that's queryable by other render functions later, not just by the assistant. The existing `observations.json` flat array is fine for now; if it needs indexing later, that's a separate phase.

## Related docs

- `STACK_TOUR.md` — the full stack reference (where the Worker lives, KV, auth model, etc.).
- `CLAUDE.md → Forward direction` — the Phase D/E/F brief + Phase G observations-as-knowledge-layer thread.
- Memory: `project_tate_tracker_tone.md` — field-journal voice rules.
- Memory: `feedback_tate_tracker_depth_filter.md` — only the property's actual scope, never regional completeness.
- Memory: `project_tate_tracker_observations_feedback_loop.md` — the Phase G thread captured in full.
