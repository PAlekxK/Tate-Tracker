---
type: interview-guide
project: fernwood
guide_id: 2026-05-28-mom-discovery
last_updated: 2026-06-20
participant: Mom (likely device d-14nyhnjz, 27 sessions over 6 days through 2026-05-27)
moderator: Claude voice mode (claude.ai), running on Mom's laptop
artifact_under_study: Fernwood (palekxk.github.io/Tate-Tracker/), used on Mom's phone
session_length_target: 25–35 minutes
delivery_path: Paul emails Mom the wrapper + paste-in prompt; she self-serves; she emails Paul the transcript afterward
sources:
  - .user-research/persona-mom.md (validated, updated 2026-05-27)
  - .user-research/jtbd-talk-to-the-property.md
  - .user-research/jtbd-2026-05-27.md (six telemetry-grounded jobs + four unserved candidates)
  - .user-research/journey-unified-field-assistant.md
  - .user-research/eval-garden-guru.md
  - .audit/2026-05-26-telemetry-rollup.md (telemetry that informs hypotheses — NOT to be shared with Mom)
  - ~/.claude/projects/-Users-paulkirschenbauer/memory/project_fernwood_mom_interview_format.md (locked methodology)
  - ~/.claude/projects/-Users-paulkirschenbauer/memory/project_fernwood_mom_reading_accessibility.md
  - Teresa Torres — Continuous Discovery Habits (story-based interviewing posture)
  - Rob Fitzpatrick — The Mom Test (past behavior over hypothetical opinions)
---

# Mom discovery interview — moderator's playbook

This is the durable research artifact behind the 2026-05-28 self-serve discovery session. The moderator prompt (`2026-05-28-mom-moderator-prompt.md`) is the operationalized version of this guide; the email draft (`2026-05-28-mom-email-draft.md`) is the wrapper Mom receives.

## Why this interview exists

Paul's model of Mom-as-user has been built mostly from his side of the conversation. He's been pointing her to things, populating entries, and inferring her use cases from the building side of the relationship. Six days of telemetry (2026-05-20..2026-05-27) made adoption no longer hypothetical — she's using Fernwood ~4.5 sessions/day — but the *why* layer is still inferred. This interview is the why.

**The session is honest discovery. It is NOT validation of Paul's roadmap.** Two headline questions answered through Mom's own narration of her actual usage:

1. **How is Fernwood useful to you today?** — past behavior, in her words.
2. **How can we continue making it more useful?** — forward-look, surfaced after discovery, not before.

The shape is proto-persona / user-portrait, not feature-test. It feeds prioritization downstream (see `reading-the-output.md`).

## Posture (non-negotiable)

- **Open questions, story-prompting.** Torres-style: *"Tell me about the last time you opened Fernwood"* — not *"do you find the Plants card useful?"* Past behavior, not opinions of features.
- **Silence is OK.** The moderator should not fill space. If Mom pauses, wait.
- **"Tell me more about that"** is the workhorse follow-up. Use it liberally; it costs nothing and surfaces depth.
- **Do NOT help her.** If Mom gets stuck — can't find something, doesn't know what a thing does, taps the wrong place — the moderator notes the friction and asks her to describe what she's seeing. Friction is data. Helping erases it.
- **The moderator is naive about what's on the phone screen.** Voice mode has no eyes on Fernwood. Everything the moderator knows comes from Mom narrating aloud what she sees and does. Ask her to describe her screen.
- **Mom-Test discipline.** No "would you like a feature that does X?" — Rob Fitzpatrick's rule applies; that question generates polite-yes answers that don't predict behavior. Always anchor in concrete past moments.
- **No coaching on the app.** The moderator does not say "you could tap the star to save that" or "Garden Guru is the one with the leaf icon." The moderator is doing research, not onboarding.

## The four-phase structure

Roughly proportional to a 25–35 minute session. Phases are guideposts, not gates — the moderator should let Mom dwell where there's signal and move on where there isn't.

### Phase 1 — Discovery (≈ 10–12 min): her use, in her words

The most important phase. Surface how she actually uses Fernwood today, before the walk-through narrows attention to the app's surfaces.

**Opening question (after warm-up):**
- *"Tell me about the last time you opened Fernwood. What were you doing? Where were you? What did you look at?"*

**Story-prompting follow-ups (use the ones that fit the answer):**
- *"What made you open it that time?"*
- *"What were you hoping to find?"*
- *"Tell me more about what you did next."*
- *"Was that a typical time, or was it different from how you usually open it?"*
- *"Walk me through a different time you opened it recently — maybe yesterday or this morning."*

**Then widen to pattern:**
- *"If you think about the last week or two, when do you find yourself reaching for Fernwood?"*
- *"Are there times of day when you tend to open it?"*
- *"Tell me about a moment recently when Fernwood was useful — anything come to mind?"*
- *"And a moment when it wasn't — when you opened it and put it down without doing much?"*

**What to listen for** (Paul-facing, not for the moderator to share with Mom):
- Bed/coffee/morning vs. on-porch vs. on-property — anchoring to the inferred trigger contexts from the persona.
- Stewardship-shaped use ("I needed to know when to prune") vs. appreciation-shaped use ("I just wanted to see what was blooming").
- Specific cards she names unprompted (Plants, Weather, Wildlife, Celestial, Property, Almanac, Worth Considering, Sources).
- Whether she narrates by card or by question ("I opened it because I wondered…") — tells us whether the IA is by-layout or by-question in her head.
- Whether she names anything about reading, glasses, text size, contrast — surfacing the accessibility constraint via her own framing.

**Don'ts:**
- Don't ask "do you use Garden Guru?" — surfaces a feature she may not remember by name. Wait for her to name it.
- Don't ask "is the dashboard helpful?" — leading and yes-prone.
- Don't ask "what feature is your favorite?" — invites politeness, not behavior.

### Phase 2 — Observation (≈ 8–10 min): walk through Fernwood as she actually uses it

Now hand the floor to her phone. The moderator's job is to listen to her narrate what she's doing, and to probe where there's friction.

**Transition prompt:**
- *"Could you pick up your phone and open Fernwood the way you normally would? As you go, describe what you're looking at, where your eyes land first, what you'd usually tap or scroll to."*

**While she's walking through:**
- *"Tell me what you're seeing right now."*
- *"What did you just do? What made you do that?"*
- *"What does that mean to you?"* (when she lands on a label, icon, or chip whose meaning isn't obvious)
- *"Is this what you'd normally look at first, or are you doing this because we're talking?"* (good calibration question — surfaces whether the walkthrough is artificial)

**If she pauses on something:**
- *"What are you noticing right now?"*
- *"What would you do next?"*

**If she expresses confusion or hesitation:**
- *"Tell me what's happening for you right now."*
- DO NOT EXPLAIN THE APP. Note the moment and ask her to keep narrating.

**What to listen for:**
- Where her eyes land first vs. what she actually taps.
- Cards she scrolls past without engaging.
- Whether she expands cards or skims headlines.
- Whether she ever references entries she's looked at before (the "revisit-as-curation" pattern from telemetry).
- Whether she notices, mentions, or uses the star (⭐) on entries. Zero stars in 55 revisits last week — does she see it? Does she ignore it? Has she even noticed it?
- Whether she notices the A/A+ text-size toggle. Telemetry shows she's used it 12 times. Hearing her describe *why* would be high signal.
- Whether she narrates by what she sees ("the green section") or by what she's looking for ("I want to know about the bird").

### Phase 3 — Scenarios (≈ 5–8 min): lightweight prompted tasks

Only after discovery and observation. Scenarios test her ability to do specific things; if we lead with them, we measure her ability to navigate Paul's mental model, not her own. The scenarios are deliberately *light-touch* and grounded in things telemetry shows she does or hasn't done.

**Pick 2–3, not all of them. Pick the ones that haven't already come up in Phase 1 or 2.**

**Scenario A — revisit something familiar:**
- *"Think about something you read in Fernwood recently — an entry, a plant, a wildlife note — that you found interesting. Can you find it again?"*
- Listen for: does she scroll, search, use a filter, go to the Almanac, or give up? Does she ever consider the star? Does the path feel natural or fumbled?

**Scenario B — encounter the unknown:**
- *"Imagine you just walked past something on the property — a plant or a bird — and you don't know what it is. Show me what you'd do."*
- Listen for: does she reach for Garden Guru? Does she reach for Claude (her existing workflow per Q4 of the eval rubric)? Does she look for a photo affordance? What does she expect to happen next?
- **Split follow-up (only if she reaches a likely-identification) — does the add-impulse appear, and on which path?** *"Say it tells you what it is. Then what — is there anything you'd want to do with that, or are you just glad to know?"* Stay quiet and let her answer; do NOT suggest "add it" or name any affordance. If she narrates a "show it a photo" reach, that's the **photo path** (already validated). If she narrates "ask it in words," that's the **text path** (the open question). The thing we're listening for is whether *"and put it in my app/the record"* is a move she reaches for **unprompted** — on either path.

**Scenario C — what's coming up:**
- *"If you wanted to know what to look for at Fernwood this week — what's blooming, what birds are around — how would you find out?"*
- Listen for: which card does she try first? Does the "this month" Plants view come to mind? Does she look for a forward-looking surface that doesn't exist (Job 7 from the 2026-05-27 JTBD rollup)?

**Critical rule for all scenarios:** if she gets stuck, the moderator does not help. The moderator asks *"what's happening right now?"* and lets her keep working, give up, or try something else. The give-up moment is data.

### Phase 4 — Forward-look (≈ 5–7 min): what's missing, what she wishes for

Last, not first — because forward-look questions are most reliable when they're anchored in concrete past moments she's already surfaced.

**Lead questions:**
- *"Think about the last time you wanted something from Fernwood and didn't find it. What were you looking for?"*
- *"Is there anything you've found yourself wishing the app did, that it doesn't?"*
- *"Is there anything Paul has told you about that you haven't tried, or that you tried once and didn't come back to?"*

**Past-behavior probe — the add-impulse, split by path (only if it didn't already surface in Scenario B):**
These two are deliberately *paired and separate*. Photo-add is already something Mom has done (it's in the telemetry); words-add has never been observed. Asking them apart keeps us from hearing a "sure" to one and crediting it to the other. Both are past-behavior, both non-leading — ask, then wait.
- *(photo path — the known one)* *"Tell me about a time you took a photo of something on the property to figure out what it was. Once you knew what it was, what did you do next?"*
- *(text path — the open one)* *"Now tell me about a time you just asked — in words, no picture — about a plant, and it turned out to be something not already in your app. Did you want to do anything with it, or were you happy just knowing the answer?"*
- Listen for whether *"put it in the app / make it part of the record"* shows up on its own, and crucially **which path it rides in on.** A "I just wanted to know" on the text path is as useful a finding as a "yes" — it would tell us the words-add affordance isn't wanted, and save building it.

**Closing question (load-bearing — this is the meta-feedback validation gate from PHASE_E_MVP):**
- *"When you've been using Fernwood and something didn't feel right — the app itself, not the property — what have you done with that? Mentioned it to Paul? Let it go? Something else?"*
- Phrased to capture the behavior wherever it happens (in-app, text, in-person) without leading her toward a "yes, I'd type it into the app" answer. The transcript will distinguish in-app vs out-of-band on its own.

**Soft close:**
- *"Anything else you've been thinking about with Fernwood that we haven't talked about?"*
- *"Thanks. That's everything I wanted to cover. Anything you want to say to Paul before we wrap up?"*

## Key research questions this interview should answer

These are the questions Paul will read the transcript looking for answers to. The moderator does NOT ask these directly — they surface (or don't) through the story-based questions above.

1. **What is Mom actually hiring Fernwood to do?** Validation or refinement of the six jobs in `jtbd-2026-05-27.md`. Which ones did she narrate? Which didn't surface? Are any of the four unserved jobs (Jobs 7–10) ones she names herself?
2. **Does the star affordance exist for her?** Three candidate explanations in the persona (invisible / wrong-model / redundant). One of these should be more consistent with the transcript than the others.
3. **What's the actual shape of her Garden Guru use?** All her conversations are 2-turn per telemetry. Are two turns enough, or does she not know multi-turn is possible, or does she want to but doesn't?
4. **What does the bed/coffee context look like in her words?** The trigger context is `inferred` not `validated`. Her own description either grounds it or reframes it.
5. **Where is the friction?** Walk-through and scenarios surface the moments she fumbles. Each one is a design opportunity.
6. **Does she experience the app as field journal, or as something else?** The dual-frame identity is load-bearing for the project. Hearing her in her own voice tells us whether the tonal work is landing.
7. **Has she ever wanted to send Paul meta-feedback through the app?** The validation gate for the 🚩 affordance decision. A "no, I just text him" answer is itself a useful finding.
8. **Does the add-impulse exist for her — and on which path?** The 2026-06-20 three-expert review (`.engineering/2026-06-20-path-text-path-add.md`, `.ux-reviews/2026-06-20-text-path-add-affordance.json`) found photo-add `validated` but text-add an `assumption` (a Paul-want, no Mom-signal). Scenario B's split follow-up and the Phase-4 paired questions test whether "add it to the record" is a move she reaches for unprompted, and whether it rides in on a *photo* (known) or *words* (open). A clean "I just wanted to know" on the words path falsifies the text-add hypothesis and saves a build.

## Things the moderator should explicitly NOT do

- Ask leading questions ("the Garden Guru feature is pretty cool, right?").
- Pitch features ("did you know you can save entries with a star?").
- Explain the app's mental model ("the Almanac is where everything you save goes").
- Help her find things ("try tapping the green section at the top").
- Test her recall ("can you remember the name of the plant Paul promoted last week?").
- Treat any phrase as final ("got it, moving on") — instead probe one layer deeper with "tell me more."
- Race through phases. If she's still in Phase 1 at 20 minutes and the signal is rich, stay there.
- Pretend to know what's on her phone. The moderator has no eyes on the screen.

## Telemetry-informed hypotheses (Paul-facing, NOT in the moderator prompt)

The moderator should not enter the session with hypotheses to confirm — Mom-Test discipline. These are listed here for Paul's reading of the transcript afterward.

- **H1:** The star is invisible OR conceptually wrong. Distinguishing signal: does she ever mention saving, marking, or coming back to specific entries? Does she narrate the star icon as visual noise, or not mention it at all?
- **H2:** Two-turn ceiling is "answers are good enough." Distinguishing signal: she describes Garden Guru as quick, helpful, done. Vs. "I would have asked more but…" which would point to discoverability or use-mode mismatch.
- **H3:** Bed/coffee is real. Distinguishing signal: she describes the trigger context unprompted, in those terms or close.
- **H4:** Photo-ID is the killer Garden Guru use case. Distinguishing signal: when scenario B (encounter the unknown) lands, does she reach for Garden Guru, or for her existing Claude workflow?
- **H5:** Forward-looking ("what should I look for this week") is an unserved job (Job 7). Distinguishing signal: she narrates a moment of "I wish I'd known X was about to bloom" or similar.
- **H6:** Year-over-year memory is a Mom-want, not just a Paul-want (Job 8). Distinguishing signal: she narrates wondering when something happened last year.
- **H7:** The add-impulse is photo-anchored, not conversational. Distinguishing signal: on the Phase-4 paired questions, "add it to the record" surfaces on the *photo* story but not the *words* story — or doesn't surface at all. A words-path "yes" (unprompted) would be the first signal the text-add affordance is wanted; a words-path "I just wanted to know" falsifies it.

## Session protocol — operational

- **Setup:** Mom on her laptop in claude.ai voice mode; Fernwood (`palekxk.github.io/Tate-Tracker/`) on her phone.
- **Kickoff:** Mom pastes the moderator prompt from Paul's email into Claude. Claude reads it, confirms its role aloud, and starts.
- **No screen-share, no recording-on-phone.** The interview is voice-only on the laptop. Mom narrates her phone aloud; voice mode transcribes.
- **Output at session end:** Claude saves a full transcript and a structured findings summary (see moderator prompt for the schema). Mom emails the transcript file to Paul.
- **No Paul in the room.** This is self-serve. Mom does it when she has time and energy; transcript comes back when it comes back.

## What success looks like for this interview

- A transcript of 25–35 minutes with Mom doing most of the talking.
- At least two concrete past-behavior stories surfaced (the "last time you opened it" question, plus at least one more).
- At least one moment of friction or fumble during the walkthrough — a place where her path didn't match the app's mental model.
- At least one forward-looking wish in her own words.
- A clear answer (yes or no, with context) to the meta-feedback question.

If we don't get those, the issue is most likely the moderator missed a probe; iterate on the prompt and try again.

## Evidence log

- `2026-06-20: [revised] — Split the add-impulse question into paired photo-path / text-path past-behavior probes (Scenario B follow-up + Phase 4), added research Q8 + H7. Driven by the three-expert review of a proposed text-path plant-add affordance (.engineering/2026-06-20-path-text-path-add.md, .ux-reviews/2026-06-20-text-path-add-affordance.json): photo-add validated, text-add an assumption. The interview is the gate before building.`
- `2026-05-28: [planned] — Interview guide drafted by user-researcher agent. To be operationalized via moderator prompt and Mom-facing email.`
- `2026-05-27: [validated] — .audit/2026-05-26-telemetry-rollup.md — first real-usage telemetry that grounds this interview. Hypotheses H1–H6 derive from this rollup.`
- `2026-05-27: [validated] — jtbd-2026-05-27.md — six jobs validated by telemetry, four unserved jobs inferred. This interview tests the inferred jobs.`
- `2026-05-22: [validated] — Paul direct — Mom reads with difficulty without glasses. Behaviorally confirmed by 12 text_size_changed events on her device.`
- `2026-05-20: [validated, inline] — Paul direct, eval-garden-guru Q11 — dashboard engagement is load-bearing, Guru engagement is gradient.`
- `2026-05-11: [inferred] — Paul direct — bed/coffee / wind-down posture for Mom's use.`

## Open questions

- Does Mom's laptop reliably support claude.ai voice mode? Worth Paul checking before sending. If not, fallback is text-mode interview (slower but workable) — note in the email.
- Is 25–35 minutes the right session length for Mom? Could be too long for one sitting. The structure tolerates a stopping point at the end of Phase 2 if she's tired; Phases 3–4 can resume.
- Does Claude voice mode reliably output a full transcript and a structured findings block in one session, or do we need to ask explicitly for the transcript at the end? The moderator prompt assumes the latter (explicit ask).
