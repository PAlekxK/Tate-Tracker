---
type: behavioral-analysis
project: fernwood
artifact_id: gg-conversation-analysis-2026-07-02
date: 2026-07-02
evidence_level: verified (conversation content) + inferred (device→person)
source: Cloudflare KV OBSERVATIONS namespace — all 16 conversation:<uuid> records + 32 metrics days (2026-05-20 → 2026-07-02), pulled live via wrangler
supersedes_partial: .audit/2026-05-26-telemetry-rollup.md (extends its window 5/26 → 7/2 and reads actual turn CONTENT, which the rollup did not)
purpose: Ground the Garden Guru conversational redesign in real usage instead of inferred signals. Commissioned by Paul 2026-07-02.
---

# Garden Guru — conversation-stretch analysis (through 2026-07-02)

Pulled the **actual turn content** of every Garden Guru conversation (not just event
counts) plus the full metrics window. This is the behavioral spine for the redesign
around three asks: (1) let people ask **follow-up questions**, (2) let them **attach
photos mid-conversation**, (3) let them **add a plant directly from Garden Guru**.

The data settles two of the three asks with direct evidence rather than inference.

---

## Headline findings

### 1. Follow-ups: demand is real; the **affordance** is the blocker — now proven, not inferred. `[verified]`
- **15 of 16 conversations are exactly one user turn.** Only ONE conversation in the
  entire history ever reached a second turn.
- The 2026-05-26 rollup read this same shape (all 2-turn, `conversation_capped: 0`) as
  *"the 5-turn cap is mechanism without need."* **That conclusion is backwards.** The
  event data cannot distinguish "didn't want to follow up" from "couldn't find how."
  Paul's lived experience — you can't find a way to continue after a reply — says it's
  the latter. The one time a user *did* get a second turn, they used it substantively
  (see below). People aren't one-and-done because they're satisfied; they're one-and-done
  because the UI dead-ends them.
- **The plumbing already supports follow-ups.** Worker `/api/chat` is multi-turn; the
  frontend `GardenGuru` controller already holds `turns[]`, exposes `followupsRemaining`
  (cap = 6 = 1 + 5 follow-ups), and `askWithImage()` works on any turn. The gap is the
  **view layer not re-presenting the input after a reply.** This is a surfacing fix, not
  a build.

### 2. Add-a-plant from conversation: demand is real, AND today's refusal quietly becomes Paul's manual work. `[verified]`
The single follow-up in the whole corpus (2026-05-28) was a user explicitly asking to
add a plant to the journal:

> **Q1:** "Is there advice on how to encourage a creeping fig to climb a wall instead of spreading out in front of the wall"
> **Guru:** "Creeping fig isn't one of the seventeen plants we tend here… I can't speak to its care from the property's experience. That said — if you're working with one elsewhere —…"
> **Q2 (the only follow-up ever recorded):** **"Please add creeping fig vine to our journal and I am attempting to make it climb a masonry wall"**
> **Guru:** **"Not something I can do from here — the journal tracks what we know from direct observation… Creeping fig would need to be planted, observed through a full season or two…"**

Then **Paul added creeping fig to `plants.json` by hand three weeks later (2026-06-20/21).**
So: a real user asked Guru to add a plant → Guru refused → the work fell to Paul offline.
That is the exact loop the redesign should close.

**Nuance the panel must hold:** Guru's refusal is *principled* under the depth-filter /
observations-as-knowledge rules (don't fabricate property knowledge for a plant not yet
observed here). The failure isn't the stance — it's that the flow **dead-ends** instead of
**capturing the intent** ("noted: you're trying creeping fig on the masonry wall — worth
documenting after a season").

### 3. The most recent conversation (TODAY, 2026-07-02) is the whole redesign in one utterance. `[verified]`
From the likely-Mom device, with a photo attached:

> "We're seeing some apparent **die back of our Lily pads** so I attached a photo wanted to
> go ahead and **log that** and see **what could be driving that**… maybe this is just normal
> but wanted to **log it. See what we can do to help the plant** and… have it **populate our
> field** [notes]."

This is a **three-intent utterance in one breath**: *capture/log* + *diagnose* + *get care
advice* — with a photo, about an **already-known** plant. Guru gave an excellent diagnostic
reply (thickening canopy + shifted July sun angle reducing pond light) and closed with
"Worth logging the observation." **But it could only talk** — the observation she asked to
log went nowhere in-app, and **this became Paul's manual `INQUIRIES.md` entry the same day**
(commit `b0d728f`, "resolve pond water-lily yellowing"). Second time in the corpus that a
real capture-and-log intent hit a wall and became Paul's offline chore.

Note this is a **different capture intent than species-promotion**: she doesn't want to add
a new *species* (lily pads are already known) — she wants to record a **seasonal field
observation** on an existing plant. The current photo→`suggest-species`→promote pipeline
does not serve this.

### 4. "Mom" is a committed daily user, active today — the transcript gate can be released. `[inferred, strong]`
- Device `d-14nyhnjz` (iPhone, 393×793): **active 27 of the last ~40 days, through today
  2026-07-02**, 1,045 total events (by far the most of any device), **22 `text_size_changed`
  events** (the A/A+ accessibility toggle shipped specifically for Mom-without-glasses — no
  other device uses it), photos attached, one species promoted. Her questions are warm and
  possessive ("What's this purple flower in **our** garden?", "**our** Lily pads").
- `tools/people.json` currently guesses this device is "probably Paul's old iPhone before a
  Safari clear." **That guess looks wrong** — 27 days of sustained use through today plus
  heavy accessibility-toggle use reads as Mom, not a cleared-and-abandoned device.
- **Implication for the project:** we've been waiting on Mom's discovery transcript since
  2026-05-29 to unblock these decisions. **Her behavior is the transcript.** She is trying
  to use Garden Guru, repeatedly, right now.

---

## Turn-depth distribution (the follow-up question, whole corpus)
| user turns | # conversations |
|---|---|
| 1 | **15** |
| 2 | **1** (the creeping-fig add-to-journal, above) |
| 3+ | 0 |
| conversations with ≥1 image | 4 |
| `conversation_capped` events, all time | **0** |

## Device engagement (full window, 32 metric-days, 2026-05-20 → 2026-07-02)
| device | class | active span (days) | conv started | img attached | promoted | text-size toggle | read |
|---|---|---|---|---|---|---|---|
| `d-14nyhnjz` | iPhone 393×793 | 5/21→**7/02** (27) | 4 | 3 | 1 | **22** | **likely Mom** — daily, accessibility, today |
| `d-szqlt0h7` | iPhone 414×848 | 5/21→6/27 (16) | 7 | 2 | 1 | 0 | 2nd active field user (Paul's 2nd device? co-steward?) — most conversations, stewardship-voiced |
| `d-avslqpyd` | desktop 1512×827 | 5/21→6/07 (7) | 1 | 0 | 0 | 0 | Paul (mapped laptop) — the sarracenia planning question |
| `d-fxeb35uh` | iPhone 393×665 | 5/21→5/27 (2) | 0 | 0 | 0 | 0 | Paul (mapped iPhone) — no Guru use |
| `unknown` | desktop 1512×827 | 5/20→5/21 (2) | 4 | 0 | 0 | 0 | pre-deviceId early tests (the 4 text-only 5/20 Qs) |

## Every question asked (chronological) — the real demand curve
- 5/20 "What's blooming on the property this week?"
- 5/20 "Is there poison ivy on the property?"
- 5/20 "Just saw a black bear at the salt lick."
- 5/20 "There's a brown bird at the feeder with a streaked chest — what is it?"
- 5/21 📷 "What is this?"
- 5/21 📷 "Can you I'd this plant?"
- 5/22 📷 "Just saw a black bear with cubs"
- 5/22 "Is it a good time to fertilize my Rhododendron and Mount Laurel"
- 5/22 📷 "What's this purple flower in our garden?"
- 5/24 "When is the best time to move a native azalea"
- 5/28 "…encourage a creeping fig to climb a wall…" → **"Please add creeping fig vine to our journal…"** (only follow-up)
- 6/02 "I got two sarracenias for the pond. One we will leave in over winter…" (Paul, laptop)
- 6/13 "Which of the plants in our landscape would benefit from ash from the fireplace"
- 6/18 "Creeping fig" (terse — likely a re-check after Paul added it)
- 6/27 "Is it terrible to put a nail into a tree to hang up something"
- 7/02 📷 "…die back of our Lily pads… log that… see what could be driving that… populate our field [notes]" (today)

The questions are overwhelmingly **property-stewardship** shaped (fertilize timing, transplant
timing, amendments, ID, "is this normal / what do I do") — exactly the Q5 wedge the eval rubric
predicted. None are idle chat. Several are natural multi-turn openers that got no second turn.

---

## What the data resolves vs. what still needs Mom
**Resolved by behavior (stop waiting):**
- People want follow-ups (the affordance is the blocker). ✓
- People want to add/log to the journal from a conversation (twice, → Paul manual work). ✓
- Mom is an active, committed user (not the churn risk the eval feared). ✓
- Photo-in-conversation is already used and wanted; the open need is photo + *log an
  observation on an existing plant*, distinct from species-promotion. ✓

**Still genuinely needs Mom (candidate verification questions):**
- When she asked one question and stopped — did she *have* a follow-up in mind and not find
  where, or was she satisfied? (Confirms finding #1's mechanism directly.)
- Today's lily-pad ask: did she believe it *got logged*? What did she expect "log it" to do?
- The two-intent blur (log vs. ask): does she experience "tell the journal" and "ask the
  guru" as one action or two? (Bears on whether capture and ask should share one box —
  and collides with the standing "no AI on the capture path" rule.)
- Does she know follow-ups/photos-in-thread aren't possible, or has she never tried?

---

## Forensic note for engineering
Today's lily-pad conversation record stores the user turn as **text-only** (no image block)
even though `image_attached` fired (967 KB, `conversationId: null`, 8 s before the
conversation got its id) and Guru's reply clearly *saw* the photo (it describes the leaf
margins accurately). So the image reached the model but the **persisted KV record dropped
the image block** — worth confirming whether that's the intended lean-storage behavior
(`leanTurnForStorage` strips blobs) or a bug that loses the photo from the saved thread.
