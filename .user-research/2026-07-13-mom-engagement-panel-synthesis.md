# Mom engagement & feedback — panel synthesis + holistic backlog reassessment

**Assembled 2026-07-13 · STATUS: ⏸ HELD (do not build yet — Paul's call) · This is the single entry point.**

> Paul's ask (2026-07-13): a *holistic* current-state assessment of the whole Mom-feedback/engagement backlog,
> run with the UX expert + the expert team, under a hard reframe — **assume the discovery interview will never
> happen; the device + Mom's usage must generate the signal.** Then: flesh out a full brief, **hold execution**,
> put it in the backlog, and assemble + clearly link all sources. This doc does that.

---

## 1. The reframe (load-bearing)
The emailed discovery interview was sent 2026-05-29, refreshed 6/20 + 6/21, and **never returned**. That non-return
is itself a finding: a 30-minute out-of-band ask exceeds what Mom will do. **We stop waiting on it.** Every design
gate that read "we'll learn this from the T+30 interview" is now orphaned and must be answered by the device + her
usage instead. Goal: use her natural use as the signal to (a) let her give *rich* feedback, (b) draw richer
interaction, (c) keep her engaged, (d) enrich the local observation base — **without a single standing "give
feedback" control** (that's the trap the ⭐ star already fell into).

## 2. What already happened — the five-lens panel RAN and CONVERGED (2026-07-13)
A concurrent session (`session_01V9LgxRastqrkkQj6Mt44CE`, commit `0f3b0a1`) convened all five lenses on
"Mom's in-app feedback/confirmation queue." **Reviews only, no product code.** All five are linked in §6. The
convergence is strong and consistent:

| Lens | Verdict (one line) | File |
|---|---|---|
| **user-researcher** | SHIP-NARROWED: one contextual confirm probe, *not* a queue. "Container is the risk, confirm is the gold." | `.user-research/2026-07-13-mom-feedback-queue.md` |
| **ux-expert** | One question at a time in the guaranteed-seen top zone; no standing queue card/count; reuse `renderTodayGlance`/pills. | `.ux-reviews/2026-07-13-mom-feedback-queue.json` |
| **engineering-partner** | 90% already exists — extend the dormant `/api/feedback` + `zone-feedback` pickup + a fetched `questions.json`. Don't coin new endpoints or a queue UI. | `.engineering/2026-07-13-path-mom-feedback-queue.md` |
| **ai-advisor** | Capture stays **AI-free** — do NOT route confirms through Garden Guru (overrules "just log it with Guru"). AI only Paul-facing (authoring, later pickup-clustering). | `.ai-reviews/2026-07-13-mom-feedback-queue.md` |
| **content-steward** | Name it **"When you're out there"** — Paul quietly leaving things only she can settle. Third door "Haven't looked yet." Open feedback = one quiet foot-line, not co-equal. Honest loop microcopy. | `review/2026-07-13-mom-feedback-queue-voice.md` |

## 3. The synthesis — the converged recommendation
**v1 = ONE live contextual confirm, shipped as an instrumented prove-before-build probe.**
- **The probe:** the **crocosmia = 'Lucifer'?** question (real open owner-Paul item; the plant is blooming
  on-property now = the flywheel's fresh-signal hook). Rendered as a single calm line **on the crocosmia entry
  inside the Plants card** (her most-scanned surface) — no new badge, no counter, no "outstanding" language.
- **Three honest branches:** *Yes, that's it · No, it's different · Haven't looked yet* + optional verbatim note
  (deterministic, AI-free ObservationStore-style capture tagged to `plantId`). "Haven't looked yet"/"Not sure" is
  first-class — it's usable ground-truth. Attribute the uncertainty to Paul/the photo, never test her.
- **Capture is AI-free.** A fence carries only routing metadata; the record is her words. Guru is at most the
  *secondary* verbatim fold-back path, never the primary confirm channel.
- **Reuse, don't build:** answers ride the dormant `/api/feedback` (extend `context`, relax one validation line)
  or the `zone-feedback` pickup pattern; questions live in a committed **`questions.json`** *fetched at load* (zero
  drift-tax). No `/api/mom-feedback`, no merge/queue UI.
- **Placement is make-or-break** (ux + content + researcher all flag it): it must ride the one moment she can't
  miss. If the Plants-entry surface doesn't get enough `viewed`, move it to the top-of-app glance.
- **Instrument the funnel the star never had:** `confirm_offered → confirm_viewed → confirm_tapped →
  confirm_answered_with_note`. This distinguishes "never saw it" from "saw it and ignored it" — the exact
  ambiguity that made the star's zero uninterpretable.
- **Close the loop visibly + honestly:** her answer lands *with Paul* (say so warmly); do NOT claim the dashboard
  updated until Paul picks it up.
- **The gate (~2–3 weeks real exposure):** *Grow* = Mom answers ≥1 confirm (tap or note) on a day it was `viewed`
  → scale to the backlog. *Kill* = `offered`+`viewed` firing repeatedly with **zero `tapped`** → it's the next
  dead affordance; stop, don't build the queue. *Ambiguous* = high offered / low viewed → extend or reposition.

## 4. Holistic reassessment of the parked backlog (the panel mapped onto your 6 threads)
| Parked thread | Verdict | Why |
|---|---|---|
| **⭐ "this matters" star** | **KILL / retire** | 0 uses / 104 revisits. Wrong model — *revisit frequency IS her curation*; a star to also say "I value this" is redundant. |
| **🚩 meta-feedback / open feedback** | **DON'T BUILD** | The standing "leave feedback" box is the star all over again. If Mom has app-feedback she tells Paul out-of-band — and that's fine. Keep at most a single quiet foot-line. |
| **Seeded prompts** | **Deprecate** | 0 usage; a standing discoverable control she doesn't operate. |
| **"Prompt Mom for input" seed (weed, 7/13)** | **SUBSUMED** | This *is* the confirm feature — a weed/plant-ID ask is a contextual confirm. Retire the separate seed into this. |
| **Fairway / change-reactions** ("does the hub match the property?") | **DEFER** | Paul-want-shaped (validating his restructure) = leading-the-witness. Revisit only after confirms prove engagement, and phrase as an observable, not a design review. |
| **Save / Ask two-button split** | **STILL OPEN — separate thread** | Not covered by this panel (it's about the confirm surface). The revisit-hierarchy question (make Save primary, Ask quiet secondary vs the no-AI-capture principle) remains its own backlog item. |

## 5. What's genuinely still open (for when this un-holds)
1. **Paul's go/no-go to BUILD the v1 probe.** The design is done + converged; only the build decision is held.
2. **Build shape** (when un-held): follow the engineering path-eval (`.engineering/2026-07-13-path-mom-feedback-queue.md`)
   — extend `/api/feedback`, add fetched `questions.json`, render one confirm via the `renderTodayGlance` machinery,
   wire the offered→viewed→tapped funnel, content-steward final voice pass on the microcopy.
3. **The Save/Ask split** — its own small ux revisit, unrelated to the confirm feature.
4. **The four in-Mom's-head questions** a tap can't answer (Q1–Q4 in `2026-07-02-mom-behavior-interpretation.md`)
   — mental-model discovery the confirm can't do. Do NOT let the confirm feature claim to close the discovery thread.

## 6. Full source inventory (all linked)
**The five-lens panel (2026-07-13):**
- `.user-research/2026-07-13-mom-feedback-queue.md` · `.ux-reviews/2026-07-13-mom-feedback-queue.json`
- `.engineering/2026-07-13-path-mom-feedback-queue.md` · `.ai-reviews/2026-07-13-mom-feedback-queue.md`
- `review/2026-07-13-mom-feedback-queue-voice.md`

**Behavioral grounding (usage-as-signal — the reframe's evidence base):**
- `.user-research/2026-07-02-mom-behavior-interpretation.md` (reads usage as the discovery signal; the 4 open Qs)
- `.user-research/2026-07-02-garden-guru-conversation-analysis.md` (real KV turns + 40-day metrics)
- `.user-research/persona-mom.md` · `.user-research/jtbd-2026-05-27.md` · `.user-research/jtbd-talk-to-the-property.md`
- `.user-research/eval-garden-guru.md` (standing eval rubric)
- `.audit/2026-05-26-telemetry-rollup.md` (the ⭐-zero-usage / one-shot findings)

**The (now-retired) interview package — kept for the mental-model Qs it still frames:**
- `.user-research/2026-05-28-mom-discovery-interview-guide.md` · `-moderator-prompt.md` · `-reading-the-output.md`

**Shipped architecture this builds on:**
- `[[project_fernwood_almanac_save_model]]` (unified input, ⭐, Save/Ask, meta-feedback Path-E decision)
- `.ux-reviews/2026-05-20-unified-input-redesign.json` · `.engineering/2026-05-20-path-unified-input.md`
- `.engineering/2026-07-02-garden-guru-redesign-plan.md` (log-with-confidence, suggest-* fences)
- `PHASE_E_MVP.md`

**Governing principles / memory:**
- Fernwood `CLAUDE.md` → "The glance and the repository" section (glance → repository → loop flywheel)
- `[[feedback_no_ai_on_capture]]` · `[[feedback_defer_affordances_pending_signal]]` · `[[project_tate_tracker_tone]]`
- `[[project_fernwood_mom_reading_accessibility]]` · `[[project_tate_tracker_observations_feedback_loop]]`
- `[[feedback_agent_proposals_not_validated]]` (the panel's conclusions are proposals until Paul ratifies)

**Code the build touches (verified present):**
- `worker/worker.js` — dormant `/api/feedback` (~1799–1867) + live `zone-feedback` GET/pickup pattern
- `viewer.html` — `renderTodayGlance`/`computeLookFors` ("Worth noticing today" surface), `.tag.t-{type}` pills,
  the ⭐ star + seeded prompts + `MetricsCollector` (the funnel instrumentation extends this)

## 7. How to un-hold / kick off later
The design convening is **complete**; nothing needs re-running. To proceed, Paul decides **build the v1 crocosmia
confirm probe — yes/no.** If yes: hand `.engineering/2026-07-13-path-mom-feedback-queue.md` (build shape) +
`review/2026-07-13-mom-feedback-queue-voice.md` (voice) to the main session to implement, then run the ~2–3 week
gate. If a *fresh* expert pass is ever wanted (e.g. to design the Save/Ask revisit, or re-open change-reactions),
this doc is the brief — point the relevant agent(s) at §1–§4 + the §6 sources.
