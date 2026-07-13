# ai-advisor review — Mom's in-app feedback / confirmation queue

**Date:** 2026-07-13 · Slug: `mom-feedback-queue` · Lens: ai-advisor (role-of-AI, capture discipline, cost, deterministic-vs-learned split)

## Bottom line

**Ship the capture path with ZERO LLM in it.** The queue is a deterministic surface — confirm chips (Yes / Not quite / No) + a plain text box — that writes Mom's verbatim words to the existing KV substrate. Do **not** route confirmation through Garden Guru. Paul's "may just be as simple as logging it with the Garden Guru" is the one instinct I'd overrule, and the reasons are principled, not stylistic.

AI has exactly two legitimate seats here, both off the capture path and both **Paul-facing, not Mom-facing**:
1. **Authoring** — Paul + Claude (in the terminal, as they already work) phrase a flagged item into a warm Mom-question. This is not new machinery; it's Paul doing what he does. No per-interaction cost, no new system.
2. **Pickup** — eventually, summarizing/clustering her answers for Paul. Legitimate ask-path, but **premature for v1**. At the volume this will run at, the raw `zone-feedback` GET list is the right tool. Defer the LLM until volume actually hurts (it won't for a long time).

That's it. Everything else that touches Mom stays deterministic.

---

## 1. Why capture must stay AI-free here — and why this case is *stronger* than the general rule

`[[feedback_no_ai_on_capture]]` already settles the default. But this feature is a sharper instance than the plant-log or vehicle-note flows, because **the payload is ground-truth adjudication of a factual claim we ourselves raised.**

The queue items are things like:
- "Is this crocosmia actually 'Lucifer'?"
- "Is the white mophead 'Annabelle'?"
- "Does the hydrangea hub-and-roster match what's on the property?"

These are the *exact* input the flywheel exists to harvest — "the one input only someone at the property can give." Mom's answer is the authoritative correction to *our* provisional guess. An LLM sitting between her mouth and the record is not a convenience here; it is a **corruption risk on the highest-value data in the system.**

Concrete failure mode. Suppose the crocosmia confirm is routed through Guru and Mom types:

> "no it's the orange one, not that lucifer one — smaller than lucifer"

A model asked to "log her confirmation" will be tempted to *resolve* that into a tidy structured claim — `{ cultivar: "not Lucifer", confidence: "user-denied" }` — and in doing so quietly discards the load-bearing detail ("the orange one," "smaller than lucifer") that is the actual clue to the real ID. Worse, a model can round a hedge into a decision: "confirmed NOT Lucifer" when she was merely unsure. **The paraphrase doesn't just add noise; it can invert the ground-truth.** That is the precise thing the property's whole trust model is built to prevent (measured vs. modeled must stay visually and semantically distinct — a confidently-wrong record is worse than an honestly-unsure one).

The fence pattern *does* protect against this — but only because the deterministic layer logs the human's raw string and the AI's prose never becomes the record. Which raises the real question:

## 2. Is there anything for the fence to *do* here? No.

The fence ("the fence is the bridge") exists to solve one specific problem: **detecting intent inside an open-ended conversation.** Guru reads free text, notices "oh — she's recording an observation about a plant we tend," and emits a routing hint so the client can offer a deterministic log. The AI's job is *classification of ambiguous input*.

In this feature there is **no ambiguous input to classify.** Paul flagged the crocosmia. The intent — "get Mom's ground-truth on the crocosmia cultivar" — is known *a priori*, authored into the queue item. There is nothing to detect. The confirm chip can be rendered deterministically straight from the queue record (`{question, targetEntity, kind}`), and her answer captured verbatim, with no model in the loop at any point.

So "log it with the Garden Guru" would mean **fabricating a conversational wrapper around a question we already have in structured form** — spending a Worker round-trip, ~76K tokens of digest, latency on Mom's LTE-in-bed connection, and a paraphrase-risk surface, to reproduce a chip the client can draw for free and offline. That's not reuse of the fence machinery; it's mis-application of it. The fence is the right tool when intent is emergent. Here intent is declared.

**Recommendation: the queue is its own deterministic surface. No `/api/chat` call anywhere in the confirm path.** Reuse `zone-feedback`'s "user captures → status:pending → Paul reads the GET" shape (the proven "thesis ratification" precedent Paul himself pointed at), extended with a `questionId` / `kind` so answers bind back to the item that prompted them. Her free-text answer is stored as-is, same boundary as observation bodies.

## 3. Tone does not require an LLM

The anticipated ux/eng counter is: "but Guru gives it the warm field-journal voice; a bare chip feels like a form." I reject the premise that warmth needs inference. `computeLookFors()` already proves it — a **deterministic template bank** produces calm, in-voice, hyper-local copy ("Worth noticing this week…") with zero model calls, zero cost, and zero paraphrase risk. The queue should do the same: Paul authors the question string (with Claude's help, offline), and it renders verbatim in a `.tag.t-{type}` surface. The voice is authored, not generated. That's *more* reliable than an LLM, not less — an authored line can't drift, hallucinate, or round a hedge.

## 4. Where AI *is* clean — both Paul-side, both ask-path

**Authoring (yes, but it's not a feature).** Turning "confirm crocosmia cultivar" into a warm, specific, answerable Mom-question is genuinely helped by Claude — phrasing, disambiguation, not-leading-the-witness. But this happens in Paul's terminal, as part of him maintaining the queue, exactly like he drafts everything else with Claude today. It needs **no new AI machinery, no Worker endpoint, no cost model.** Build the authoring UX as "Paul appends a question record"; the fact that Paul used Claude to word it is invisible to the system. Don't over-engineer a "question drafter" endpoint.

**Pickup / synthesis (yes — but later).** Clustering her answers, flagging "she contradicted our canon here," summarizing a week of reactions for Paul — this is a legitimate ask-path, Paul-facing use with no capture-corruption risk (it reads already-captured verbatim records; it never *becomes* the record). But at v1 volume — a handful of confirms trickling in — an LLM rollup is solving a problem that doesn't exist. The `zone-feedback` GET returns a short list Paul reads in ten seconds. **Defer AI summarization until the answer volume is genuinely more than Paul wants to eyeball** (mirror the `analyze-fernwood.py` posture: the data accrues in KV regardless; add the rollup when it earns itself). When it does earn itself, keep it read-only over the stored verbatim strings and footnote it as model-generated, never let it overwrite the raw answers.

## 5. Cost

Per-turn Garden Guru cost (Haiku 4.5, `claude-haiku-4-5-20251001`, ~76K-token digest, `cache_control: ephemeral`, `max_tokens: 600`):

| Path | Rough cost per interaction |
|---|---|
| Deterministic confirm chip | **$0.00** |
| Guru turn, warm cache (digest already cached) | ~$0.008–0.012 (76K cache-read @ ~$0.10/M + ~600 out @ $5/M) |
| Guru turn, cold cache (first turn / cache expired) | ~$0.08–0.10 (76K cache-write @ ~$1.25/M) |

In absolute dollars, routing a dozen confirms through Guru is cents — not a budget problem. **The cost argument is not "it's expensive"; it's "it's non-zero for something that should be exactly zero, and it drags in latency + a network dependency + a failure mode + a paraphrase surface for no functional gain."** A confirm chip works offline, instantly, and can't fail halfway. Every one of those properties matters more for Mom-in-bed-on-LTE than the cents do. Spend LLM tokens where inference adds value (photo ID, open Q&A); a known-question confirmation is not that place.

## 6. "Reach her where she is" — the pull/push line, drawn precisely

Mom's documented behavior: satisfied one-shot user who **opens the app, asks once, leaves for claude.ai.** She does *open the app* — that's the moment we have. The passive queue rides it correctly: it's *there* when she opens, glance-able, ignorable. That is pull.

What would be **push, and is out of bounds:**
- A notification / email nudge to answer the queue — violates pull-not-push and calm-not-naggy, and email is the heavyweight loop we're explicitly trying to retire.
- Guru **proactively** surfacing the queue mid-conversation, unprompted — push, and it hijacks a session she started for her own reason.

The one **AI-adjacent path that stays on the pull side**, and the only place I'd let a model near this feature Mom-facing: at the **natural end of a conversation *she* initiated**, a single calm chip — "Paul wondered about the crocosmia — got a sec?" — reusing the `suggest-followup` fence mechanics (AI routes, client renders a deterministic chip, tap opens the deterministic confirm; her answer still captured verbatim). She's already engaged, so it's pull-adjacent, and it "reaches her where she is" by riding the one moment she's actually in Guru.

But I would **not ship this in v1.** It's an amplifier for a queue we haven't yet shown gets *any* use. Given the zero-usage graveyard (star: 0/104 revisits; seeded prompts: 0; 5-turn cap: never fired), the honest sequence is: ship the deterministic passive queue, instrument it (`momq_offered` / `momq_answered` on device `d-14nyhnjz`), and **only** add the end-of-conversation Guru hook if the passive surface shows a pulse. AI cannot manufacture engagement; adding it up front just puts cost behind a possibly-dead affordance.

## 7. What I would explicitly NOT do with AI here

1. **No `/api/chat` call in the confirm/capture path.** Ever. Not for framing, not for "logging," not for tone.
2. **No AI paraphrase, summarization, or structuring of Mom's answer at capture time.** Store her verbatim string. Structuring (if any) is a *later*, Paul-side, read-only pass over the raw record — never a rewrite of it.
3. **No new "question drafter" LLM endpoint.** Authoring is Paul-in-terminal; it needs no productized AI.
4. **No AI-mediated push** (notification, proactive Guru interjection). Pull only.
5. **No AI rollup of answers in v1.** The `zone-feedback` GET list is enough; add synthesis only when volume forces it.
6. **Don't reuse the fence just because it's elegant.** It solves intent-detection; this feature has no intent to detect.

## 8. The 2–3 decisions this hinges on

1. **Is the queue a deterministic surface or a Guru surface?** → Deterministic. (Intent is pre-declared, so the fence has no job; and the payload is factual ground-truth where paraphrase is a correctness bug, not a style nit.)
2. **Does warmth require an LLM?** → No. Authored template copy (the `computeLookFors` precedent) is warmer *and* safer than generated copy for a fixed question set.
3. **When does AI earn a seat?** → Only on the Paul-facing pickup side, only when answer volume exceeds a glance, and only read-only over verbatim records. And, as a v2 *amplifier*, a pull-side end-of-Guru-conversation chip — gated on the passive queue showing usage first.

## 9. Anticipated disagreements with the other lenses

- **vs. engineering-partner:** likely reaches for the fence machinery because it's built, tested, and elegant. My pushback: elegant, but mis-fit. The fence exists to classify ambiguous free text; here the question is structured and known in advance, so a fence adds a Worker round-trip + digest cost + a failure mode to render a chip the client already has all the data for. Reuse the `zone-feedback` KV shape, not the fence.
- **vs. ux-expert:** likely wants Guru to conversationally "frame" each item for warmth/continuity. My pushback: tone is authored, not inferred — deterministic templates give identical warmth for free and can't drift or round a hedge. If ux wants a *conversational* entry point, that's the v2 pull-side end-of-conversation hook, not LLM-in-the-capture-loop.
- **vs. user-researcher:** I expect strong alignment — research will likely warn the passive queue is a zero-usage candidate. I agree, and I'd add the ai-specific corollary: **AI does not rescue an unused affordance; it just puts cost and paraphrase risk behind it.** So the sequencing (deterministic v1 → instrument → only then consider the thin Guru amplifier) is a shared conclusion.
- **vs. content-steward:** probably aligned — authored copy is exactly their domain, and "the record is her words" is a voice principle as much as an AI one. Possible friction only on who owns the question-string wording (steward vs. Paul-with-Claude); trivially resolved.

---

*One-line summary for the orchestrator: capture stays 100% deterministic (confirm chip + verbatim text box over the `zone-feedback` KV pattern); AI only on the Paul-facing authoring (informal, no machinery) and — later, when volume earns it — read-only pickup synthesis; the fence has no job here because intent is pre-declared, and warmth comes from authored templates, not inference.*
