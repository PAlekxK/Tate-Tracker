---
type: synthesis-note
project: fernwood
note_id: 2026-05-28-reading-the-output
last_updated: 2026-05-28
audience: Paul (post-interview synthesis)
companion_artifacts:
  - .user-research/2026-05-28-mom-discovery-interview-guide.md
  - .user-research/2026-05-28-mom-moderator-prompt.md
  - .user-research/persona-mom.md
  - .user-research/jtbd-2026-05-27.md
---

# Reading the output — short guide

When Mom emails the transcript back, this is what to do with it. Goal: extract durable signal, fold it back into the persona / JTBD artifacts, and feed Phase E / prioritization decisions. Roughly an hour of work, ideally in one sitting.

## Before you read

- **Resist the urge to skim for "did she like X."** That's not what's there. The signal is in *what she did*, *what she said in her own words*, and *where she got stuck* — not in feature-level approval.
- **Read the verbatim transcript first, the structured summary second.** Claude's summary is a starting frame, not a substitute. Her own words carry the work.
- **Have `persona-mom.md` and `jtbd-2026-05-27.md` open as you read.** You'll be folding signal into them.

## What to look for (in priority order)

### 1. The six telemetry-grounded jobs — confirmed or refined?

The jobs in `jtbd-2026-05-27.md` (jobs 1–6) are based on telemetry — what she does, not what she says. The transcript adds the *why*.

For each job, ask:
- Did she narrate this job in her own words? (Promotes evidence from `validated by telemetry` to `validated by behavior + statement`.)
- Did she narrate it in a different shape than the telemetry implied? (Refinement — update the JTBD card.)
- Did she not mention it at all? (Worth noting — the job may still be real but not top-of-mind.)

### 2. The three star hypotheses — which one survived?

H1 from the interview guide. Persona open question. The transcript should distinguish:
- **Invisible.** She doesn't mention the star, doesn't see it during walk-through, scrolls past entries without noticing the icon. → UX iteration on visibility.
- **Wrong-model.** She mentions the star, but talks about entries as things she reads, not things she marks. The concept of curation-by-marking is foreign. → Kill the star or replace with passive surfacing (e.g., "you came back to this 4 times").
- **Redundant.** She says something like "I just come back to ones I want to read again." → Star is conceptually wrong; revisit-as-curation is the actual model.

Whichever one fits, the decision on the star follows naturally. If signal is ambiguous, hold the call and watch the next telemetry rollup.

### 3. The 2-turn Garden Guru ceiling — which one?

H2. The transcript should distinguish:
- **"Answers are good enough."** Guru is working as intended for her use mode. No iteration needed.
- **"Wanted to ask more but didn't know how."** Discoverability issue on the multi-turn affordance.
- **Mismatch.** Her job-to-be-done with Guru is one-shot Q&A, not conversation. → Reshape Garden Guru toward one-shot Q&A; don't keep building multi-turn affordances.

### 4. The bed/coffee trigger — does it hold?

H3. If she narrates the trigger context unprompted (in bed, with coffee, in the morning, winding down at night), promote that line in `persona-mom.md` from `inferred` to `validated`. If she describes a different trigger context (on the porch, at the kitchen table, before going outside) — update the persona to match. If she describes both, even better.

### 5. The unserved jobs (7–10) — which surfaced from her side?

For each of jobs 7–10 in `jtbd-2026-05-27.md`:
- Did she narrate something that maps to this job? (Promotes the job from `inferred` to `validated` with her quote as the inline source.)
- Did she narrate something close but different? (Reshape the job.)
- Did she not mention it? (Job stays `inferred`; prioritize lower unless other signal surfaces.)

Job 7 (know-what-to-look-for) and Job 8 (year-over-year) are the highest-leverage if validated. Job 9 (browse past conversations) is structurally real but may be a Paul-want, not a Mom-want — watch for "no, I just ask it again" or similar. Job 10 (share-this) is the easiest to over-build; treat any signal here as weak.

### 6. Friction points — every single one is a design opportunity

From the structured summary's "friction points" section, and also from your reading of the transcript. For each one:
- Is it a UX issue (label, affordance, layout)? → Hand to ux-expert.
- Is it a voice/tone issue (something read wrong, felt wrong)? → Hand to content-steward.
- Is it a conceptual issue (she didn't understand what something is for)? → User-researcher (me) revisits the JTBD or anti-persona.
- Is it an accessibility issue (couldn't read, couldn't tap)? → Direct fix; high priority given the make-or-break framing.

Don't try to fix anything immediately. The synthesis pass is to *catalog*, not to act. Acting comes from prioritization.

### 7. The meta-feedback closing question — the actual answer

The validation gate for the 🚩 affordance from `project_fernwood_almanac_save_model.md`. Three possible shapes:
- **"Yes, I typed something and saved it as an entry, then told you later."** → Path E (current state) works. No 🚩 needed.
- **"Yes, I texted you about it / called you / told you in person."** → Path E doesn't work *for in-app meta-feedback* but the function is being served outside the app. Decision: leave Path E (Mom uses out-of-band channels for this; that's fine) or build 🚩 to bring it in-app. The ux-expert risk flag still holds: 🚩 may be a feature for a behavior that doesn't happen in-app.
- **"No, never thought about it."** → Path E forever. Kill the 🚩 backlog item.

Whichever answer she gives, update `project_fernwood_almanac_save_model.md` with the resolution.

## What to fold back into which artifacts

After reading, update the following:

| Artifact | What to add |
|---|---|
| `persona-mom.md` | New `validated` claims from her own words. Update Open Questions — close ones the interview answered; open new ones it raised. Update Evidence log with a `2026-05-28` entry pointing at the transcript file. |
| `jtbd-2026-05-27.md` | Per-job: did the transcript validate, refine, or leave the job? For jobs 7–10: any promotions from `inferred` to `validated`? Update Evidence log. |
| `jtbd-talk-to-the-property.md` | Per Phase E open question at bottom of file: did the transcript settle any of them? |
| `journey-unified-field-assistant.md` | Mom journey (Journey 3) — friction points + pain points refined by her actual walk-through. Update emotional curve if surprising. |
| `eval-garden-guru.md` | If she gave language for any of the Q1–Q12 rubric dimensions, fold it in. |
| Auto-memory `project_fernwood_almanac_save_model.md` | Meta-feedback channel decision settled (or not). |
| Auto-memory `project_fernwood_mom_interview_format.md` | Note that the first session ran; what worked, what didn't, what to change for the next session. |

## What NOT to do with the output

- **Don't propose feature changes from this transcript alone.** The synthesis is durable signal; the feature decisions come from synthesis + prioritization across multiple inputs. Sit with the findings for a day before acting.
- **Don't share Mom's verbatim transcript with other agents without redacting.** It's family material. Quotes within research artifacts are fine; the full transcript stays in `.user-research/` and is `.gitignore`d if it isn't already.
- **Don't fold her words into the JTBD as `validated` if they're actually `inferred` from indirect signal.** If she said "I open it in the morning sometimes" — that's `validated` for "sometimes in the morning." It's not `validated` for "bed-and-coffee daily ritual" unless she said that.
- **Don't treat one interview as the final word.** This is N=1. It's the strongest signal we have, but the next session (per the pencils-down handoff plan, focused on a different surface) will refine.

## Cross-project pattern check

After folding into Fernwood artifacts, take 5 minutes to check `~/.claude/user-research/cross-project.md` and `~/.claude/user-research/fernwood.md`. If anything in the transcript generalizes (e.g., "Mom uses tech like an adult who has things to do, not like a beginner" — a pattern that might apply across Paul's audiences), propose an addition. Per the user-researcher methodology: always propose, never silently update.

## What "good" looks like

A successful synthesis pass produces:
- ~5–10 line updates across the persona / JTBD / journey artifacts.
- A clear answer on the star (kill / move / replace / wait).
- A clear answer on the 2-turn Guru ceiling (working / discoverability / mismatch).
- A clear answer on the meta-feedback gate (Path E forever / build 🚩 / out-of-band).
- A short list of 2–4 friction points worth handing to ux-expert or content-steward.
- One or two updates to Open Questions across the artifacts — old ones closed, new ones added.
- A short reflection on the interview process itself: did it surface signal, or was the moderator too constrained, or too loose?

If the output doesn't carry any of that, the interview likely missed — iterate on the moderator prompt and try again on a different focus area (per the pencils-down handoff: the next session can focus on Garden Guru specifically, or the property map specifically).
