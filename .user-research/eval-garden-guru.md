---
type: evaluation-rubric
project: fernwood
artifact_id: eval-garden-guru
last_updated: 2026-05-20
evidence_level: inferred
scope: Garden Guru as it stands after the Phase D classify-on-save removal — two-track design (Quick Capture for write, Garden Guru for ask). NOT Phase E in isolation; NOT the full field-assistant direction with image input + Phase G memory. Phase F is benched as of 2026-05-20 but surfaces here as the killer use case worth re-examining.
sources:
  - Paul interview 2026-05-20 (Q1–Q12, "decoding what good looks like for Garden Guru")
  - Tate-Tracker/CLAUDE.md (Phase D/E status, no-AI-on-capture pivot, metrics-capture punch list, unified-input UX punch list)
  - jtbd-talk-to-the-property.md
  - journey-unified-field-assistant.md
  - persona-mom.md, persona-paul-co-steward.md
  - jtbd-invest-time-well.md
  - ~/.claude/projects/-Users-paulkirschenbauer/memory/feedback_no_ai_on_capture.md (referenced)
  - ~/.claude/projects/-Users-paulkirschenbauer/memory/project_tate_tracker_tone.md
---

# Garden Guru — Evaluation Rubric

A decoding of "what good looks like" for Garden Guru across the three performers (Paul-mobile, Paul-desktop, Mom). The shape is deliberately concrete: per performer, what does a *win* look like, what does a *miss* look like, what does *silent failure* look like (the most expensive category — see Q11), and what would it take to move the column from `inferred` to `validated`.

This is a working instrument, not a scorecard. It gets used three ways:

1. **Smoke-test scoring** — after Paul's E2E test, score each performer's behavior against the column.
2. **Design path-eval input** — the "close the loop" column points to the metrics-capture work the engineering-partner agent picks up. Until that ships, every win/miss judgment is observation-of-one, not measurement.
3. **Hard-fail tripwire** — the miss column includes Q8b/Q8c hard-fail flags. If either fires once in real usage, that's not a "score lower" — that's a system-prompt-iteration trigger.

---

## Operating principles (cross-performer)

These hold across all three columns. They're the depth-filter and voice non-negotiables expressed as eval criteria.

- `[validated, inline]` — **Property-specific over generic, always.** Paul Q9: *"offering suggestions for plant care that are valid at Jasper's elevation because of a lazy lookup rather than adjusting everything to be sure it's very accurate to our elevation."* Any answer that could have been written by a generic gardening app — and was, given that Fernwood-specific context was available — is a hard fail. The LLM-gravity-toward-Jasper-1535ft-defaults is the specific failure mode to watch.
- `[validated, inline]` — **Never invent plants on the property.** Paul Q8b. Q7 refinement: real-plant ID (something you point at and ask "what is this?") is fine; "I see your laurel is blooming" when there's no laurel in `plants.json` is a hard fail.
- `[validated, inline]` — **Wildlife ID is permitted even outside the curated list.** Paul Q7. Refines the depth filter — for wildlife the filter is "don't claim it's been observed here unless it has," not "refuse to identify."
- `[inferred]` — **Voice holds across the turn.** Field-journal register (Sand County Almanac touchstone). Drift toward productivity-app voice ("Here are 3 things you should do this week!") is a miss but Q8a-iterate, not Q8b/c-hard-fail.
- `[validated, inline]` — **Friendly mentor, not detached observer, when the user is uncertain.** Paul Q6: Mom needs *"acknowledgment that we're trying to do the right thing"* — Guru as *"friendly and understanding and a mentor that also cares about the well-being and beauty of all the plants and everything else we have at the property and even our equipment."* This sits in tension with the dashboard's observer voice — see Contradictions section below.

---

## Performer 1 — Paul-mobile (on the property, phone in hand)

The use mode where Paul is asking about something he can see and Mom can't (or vice versa — he wants to capture for her).

### Win signals `[inferred]`

- **Pre-loaded context is the whole moat.** Q2 — Paul nails it on the first try when *"you can pull this up without providing all the context… and just pick up the phone and ask what is this. And there's immediately, not only an understanding of the context of where the picture is taken… but also specifically, all feedback is immediately matched to Fernwood."* A win turn doesn't require Paul to say "I'm at Fernwood, elevation 2,959 ft, mountain laurel context" — it just answers as if Guru already knows.
- **One-shot answers, not paragraphs.** Mobile-on-trail tolerance for length is low. A two-sentence reply that's right beats a five-sentence reply that's right.
- **Property-anchored, even on generic-sounding asks.** Paul asks "what should I do for the azaleas this month?" — a win cites our specific azalea entries, our frost date, our soil, our elevation. Not "azaleas generally prefer..."
- **Capture-then-ask flow works.** The 2026-05-16 Butterfly Weed loop (real Claude conversation at Tate → ID → species landed in `plants.json`) is the canonical win pattern. Garden Guru without image input today can't ID the unknown specimen on-property — but it can take Paul's description and either ID or honestly say it doesn't know.

### Miss signals `[inferred]`

- **Generic horticulture creep on a property-specific question.** Q8c HARD FAIL. Paul asks about *his* azaleas and gets advice that would work in Jasper-town at 1,535 ft. Hardest to detect because the answer "sounds" right and the elevation-mismatch is invisible without checking.
- **Latency over ~3 seconds with no clear pending state.** On LTE, with the ~57K-token system prompt, this is a real risk. Mobile flow breaks at 5s.
- **Surface ambiguity — Paul tries to log an observation via Garden Guru.** If the unified-input UX lands (see Q10), routing is explicit via button. Until then, the current two-card layout (Quick Capture + Garden Guru) does the routing — but it puts the burden on Paul to pick the right surface. A miss here is conceptual confusion, not Guru's fault.
- **Mention of plants/equipment that aren't actually at Fernwood.** Q8b HARD FAIL.

### Silent failure modes `[inferred]`

- **Paul stops opening Guru in the field and reverts to the Q3 baseline.** *"take a picture and then go back to the desk and figure it out later."* If on-property Guru sessions trend toward zero post-novelty (~30 days), the killer use case from Q1 isn't being served. **This is the dominant silent failure for Paul-mobile.** It would not show up as a complaint — Paul just stops invoking it.
- **Paul opens Guru, asks once, gets a passable-but-generic answer, accepts it.** No hard-fail tripwire fires, but the moat (Q2 pre-loaded context) wasn't deployed. Trust drifts down by half a degree per such turn until Guru feels indistinguishable from Claude in the regular app.
- **Phase F absence becomes a quiet daily friction.** Paul keeps wanting to send a photo, can't, settles for description, gets a less-confident answer. He doesn't complain — but the killer use case from Q1/Q3 stays unbuilt. (See Contradiction #3 below.)

### Close-the-loop to `validated`

- **Engineering-partner: metrics-capture path.** Punch-list item from 2026-05-20 (`CLAUDE.md`). For Paul-mobile specifically, what we need: per-conversation device-type (phone/tablet/desktop) detection logged to KV; geolocation-or-network heuristic for on-property vs off (optional — LTE-network signal might be enough, or a soft "I'm at the property" toggle); session frequency over time post-launch. **Without this, every win/miss judgment here is anecdotal.**
- **Direct Paul-debrief after 2 weeks of mixed use:** "In the last two weeks, how many times did you reach for Guru on the property and not? Which times did it feel like the moat (Q2)? Which times did it feel like a Claude session you could have run anywhere?"
- **Hard-fail incident log.** Every Q8b (invented plant) or Q8c (generic when property-specific was knowable) instance gets logged with the conversation ID, the system prompt version, and the iteration response. **One hard-fail per month is the limit before the system prompt is the bug.**

---

## Performer 2 — Paul-desktop (Atlanta, planning/researching)

The mode that looks most like a conventional chat: keyboard, longer turns, research-shaped questions. Q1 doesn't put this mode in the foreground — Paul says use is *"generally at the property"* — but Paul-desktop is still a real performer, especially for the appreciation/research half of the joint job.

### Win signals `[inferred]`

- **Multi-turn coherence holds.** Paul asks about the laurel, follows up with "and the one near the spring," Guru tracks. Multi-turn is where desktop shines vs. mobile.
- **Reply can be paragraph-shaped without slipping voice.** Desktop tolerates 2-3 sentence answers. The Sand County Almanac register is hardest to hold at length — when it holds, that's a win.
- **Citations are linkable / referenceable.** When Guru says "the chestnut callout in the Plants card touches on this," a desktop win means Paul can act on that reference — even if the link itself isn't yet built, the reply doesn't leave him guessing about provenance.
- **The research-mode question gets a property-anchored answer.** "What should I think about for native keystones?" gets answered through Fernwood's specific oak/willow/cherry context, not generic NWF lists. The depth filter has to bite harder on desktop because the questions are more abstract and the LLM is more tempted to drift generic.

### Miss signals `[inferred]`

- **Generic-horticulture creep.** Q8c HARD FAIL. Same as Paul-mobile but more dangerous here because the question is more abstract and the failure is harder to spot. The two-paragraph "here are some great native keystones for Blue Ridge gardens" reply that doesn't anchor in *our* oaks is exactly the trap.
- **Voice drift at length.** Q8a iterate-not-hard-fail, but the longer the reply, the more frequent. Desktop is where the system prompt earns its keep.
- **Loss of conversation chain on refresh.** Phase E shipped session-only persistence; for desktop research mode this may be too strict (see journey doc, open question). Not a current miss-signal because it's a known limitation, but a known opportunity.

### Silent failure modes `[inferred]`

- **Paul-builder-user notices voice drift Mom wouldn't, but doesn't flag it.** He's already iterated heavily on the system prompt; if he stops iterating because "it's good enough," but it's actually mid-drift, the asset erodes invisibly. **The check: is Paul still iterating `GARDEN_GURU_SYSTEM` monthly?** If yes, healthy. If no, suspect.
- **Desktop becomes the only mode that works well, and mobile/Mom modes don't get equal attention.** Builder-user bias (cross-project pattern; see also persona-paul-co-steward.md anti-persona). Desktop is Paul's native idiom — if Guru is great there and only OK elsewhere, the eval shows a green light overall while Mom silently doesn't engage.

### Close-the-loop to `validated`

- **Engineering-partner: metrics-capture.** Same path as Paul-mobile. The differential signal that matters here: are Paul's desktop sessions trending toward research-shaped multi-turn (3+ turns) or one-shot question-answer? Multi-turn = the value-add is landing; one-shot = Claude-equivalent.
- **System prompt iteration log.** Track every `GARDEN_GURU_SYSTEM` edit with date + reason. The cadence is the health metric.

---

## Performer 3 — Mom (bed with coffee, kitchen, porch)

Q4–Q6 and Q11 land here. **The most important performer for whether the project succeeds — and the one where the eval gets sharpest because Q11 reshapes what "Guru engagement" even means for her.**

### Win signals `[inferred]`

- **The dashboard gets opened regularly.** Q11 — *"if she uses the dashboard but doesn't use the guru, that's still a success."* **Dashboard engagement is the load-bearing metric for Mom, period.** Guru engagement is gradient, not gate. This is the sharpest reframe in the rubric.
- **When Guru *is* engaged, the question is the Q5 question or a close cousin.** *"specifics for fertilizing a given plant"* — the property-specific stewardship lookup. A win is one well-placed question per week, answered in voice, with the wedge over Claude visible: *"when it pulls in the weather forecast, when it pulls in the history and everything else that we have fed into the Fernwood tracker."*
- **The reply feels like the rest of the dashboard.** Voice consistency is the load-bearing variable for Mom. If she can't tell whether she's reading a card or a Guru reply, that's a win.
- **Acknowledgment of effort, not correction of error.** Q6 — when Mom asks something with trepidation, Guru leads with mentor-warmth, not detached observation. **This is in tension with the dashboard's observer voice** — see Contradictions.
- **The personal library accumulates.** Q4/Q5 — over time, Guru knows Mom's preferences (*"what tools to use, what brands she uses… how she operates and gets things done"*) and Fernwood's history *together*. A win at 3 months is that the personal-library accumulation is visible — Guru references something Mom said two weeks ago.

### Miss signals `[inferred]`

- **Mom stops opening the dashboard.** Q11 — *"it's a failure either way if she doesn't open the dashboard."* This is THE failure signal, and it's not Guru-specific — Guru could be perfect and the dashboard could still lose her.
- **Cold/clinical voice when Mom is uncertain.** Q6 miss. Not Q8b/c hard-fail, but the silent-disengagement risk is acute. Mom doesn't push back — she just doesn't ask again.
- **A blank-textbox empty state with no scaffolding.** Q10 / Mom-journey analysis — bed-with-coffee mode doesn't have a formed question. If Guru's empty state requires one, Mom skips. (Note: the current shipped Garden Guru has more affordance than this, but the unified-input UX redesign (Q10) needs to preserve scaffolding for her.)
- **Push behavior — Guru prompts Mom to engage further.** Reminders are OK *if* batched and roll-up-style (Q5 extension); follow-up prompts in-conversation are not. Pull, not push, for her.

### Silent failure modes `[inferred]`

- **The dominant Mom silent failure: she opens it once or twice, then quietly stops.** No complaint, no signal — just absence. **This is the single most important signal to instrument, and the metrics-capture work is what makes it visible.**
- **She uses the dashboard but never tries Guru.** Per Q11 this is "still a success" — but it's also a missed opportunity that's invisible without the engagement metrics. Worth knowing-but-not-treating-as-failure.
- **Strictly-worse-than-Claude path.** Q4 — Mom already uses Claude with image input for plant ID. **Garden Guru without Phase F is, for Mom's stated workflow, strictly worse than what she has today.** If Mom keeps using Claude for plant ID and never uses Guru, that's not Guru failing in isolation — it's the product not landing in her existing workflow. **This is the Phase F re-examination trigger.** (See Contradiction #3.)

### Close-the-loop to `validated`

- **Engineering-partner: metrics-capture — Mom dashboard opens above all else.** The single most important signal in the whole rubric: dashboard sessions originating from Mom's device, daily/weekly, over a 90-day window post-instrumentation. Privacy-respecting, family-only — already scoped in CLAUDE.md punch list.
- **Direct conversation with Mom after 30 days of metrics.** Mom-Test-style: what did she actually do, what did she reach for, when did she last open it and what for. Not hypotheticals. (This is the standing artifact-validation gap from the README — closing it is the single biggest move toward `validated` across the whole research set.)
- **Mom's Q5 wedge claim test:** ask her after a month, "when you wanted to know about fertilizing the [plant], where did you go?" If Guru: validated. If Claude or Google: the wedge isn't landing.
- **Voice/mentor calibration test (Q6):** show Mom 3 sample Guru replies — observer-voiced, mentor-voiced, and current-Guru-voiced — without telling her which. Ask which she'd want to read. Closes the voice-tension question (see Contradiction #1).

---

## Hard-fail tripwires (cross-performer)

Per Q8, two things are hard-fail; one is iterate-not-fail.

| Behavior | Tier | Response |
|---|---|---|
| **Q8a — Voice drift** | Iterate | Edit `GARDEN_GURU_SYSTEM`. Track date + reason. Monthly cadence = healthy. |
| **Q8b — Invents a plant on the property** | HARD FAIL | Immediate system-prompt iteration. Log to hard-fail incident log. >1/month = system prompt is the bug. |
| **Q8c — Generic horticulture when property-specific was knowable** | HARD FAIL | Same as Q8b. Harder to detect — see "Silent failure" sections. |

Hard-fail incident log location (proposed): `Tate-Tracker/.engineering/garden-guru-hard-fails.md` — engineering-partner sets up.

---

## Evidence log

- `2026-05-20: [validated, inline] — Paul interview Q1–Q12, "Decoding what good looks like for Garden Guru."` All Q-cited claims trace to this conversation.
- `2026-05-20: [validated, inline] — Paul Q11 — "if she uses the dashboard but doesn't use the guru, that's still a success. And it's a failure either way if she doesn't open the dashboard."` Reframes Mom's column.
- `2026-05-20: [validated, inline] — Paul Q4 — Mom already uses Claude with photos for plant ID at Fernwood. Garden Guru without Phase F is strictly worse than her existing workflow for that use case.` Reframes Phase F's bench status.
- `2026-05-20: [validated, inline] — Paul Q2 — pre-loaded Fernwood context is the moat over Google/ChatGPT.` Anchor for win-signal definition across all performers.
- `2026-05-20: [validated, inline] — Paul Q9 — Jasper-elevation lazy-lookup is the canonical Q8c example.` Specific failure mode for hard-fail detection.
- `2026-05-20: [inferred] — Paul Q10 — unified-input UX proposal (one minimalist textbox + 2 buttons) is distinct from both the as-shipped two-card layout and the Phase E synthesis intent-routing surface.` Tagged inferred because the design hasn't been path-eval'd or shipped.
- `2026-05-19: [validated, inherited] — Phase E MVP shipped (commit 3c8236c); GARDEN_GURU_SYSTEM live; Worker /api/chat + cost log + conversation persistence to KV.` Baseline state.
- `2026-05-20: [validated, inherited] — Paul direct (no-AI-on-capture memory) — classify-on-save call slated for removal; capture path becomes pure-text log.` Scope-defining decision.

---

## Open questions (real-user validation pending)

- **All `inferred` win/miss signals.** Until metrics-capture ships, this rubric is a hypothesis. The whole "close the loop" column exists to track what would convert each.
- **Voice tension between observer (dashboard) and mentor (Mom's Guru need).** See Contradiction #1 below — proposed but not yet resolved.
- **Phase F's bench status.** Q4 makes the killer-use-case argument loudly. Whether to un-bench is a Paul + ai-advisor + engineering-partner decision; this rubric only flags it.
- **Hard-fail incident frequency.** No baseline yet — first hard-fail incident sets the watermark.
- **Whether Mom's existing Claude+photos workflow becomes Garden Guru's user-story-1 (un-bench Phase F) or remains "Mom uses Claude for ID, dashboard for everything else" (live with the wedge limitation).** This is the most important strategic question this rubric surfaces.
