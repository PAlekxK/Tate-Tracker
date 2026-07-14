# Handoff: mom-confirm-probe
<!-- generated 2026-07-13 ~8:5x PM ET · source: Tate-Tracker@3db19dfbc770a862f003a04d37b125f7d9f11558 · RECEIVER: verify shas vs HEAD before trusting any status below; if HEAD moved, reconcile from git + the pickup-point, not from this brief -->

## 1. Mission
Build **v1 of the Mom in-app contextual-confirm probe** — ONE live confirm ("is this crocosmia 'Lucifer'?"), AI-free capture, instrumented, shipped as a prove-before-build probe. Paul greenlit the build 2026-07-13. This is NOT the full "queue" — one question, deterministic, no standing container.

## 2. Read first (point, don't re-derive)
1. `.user-research/2026-07-13-mom-engagement-panel-synthesis.md` — **§3 (the converged recommendation) + §4 (what's KILL/DEFER) + §5 (still-open) + §6 (sources).** This is the master brief; start here.
2. `.engineering/2026-07-13-path-mom-feedback-queue.md` — **THE build shape.** Data model, the dormant `/api/feedback` extension (worker.js ~1799–1867), the `zone-feedback` pickup pattern, `questions.json` (fetched not inlined), what to refuse to add. Follow this for the backend.
3. `review/2026-07-13-mom-feedback-queue-voice.md` — final microcopy/voice ("When you're out there"; Paul-attributed framing; the three honest branches; honest loop-close wording).
4. `.ux-reviews/2026-07-13-mom-feedback-queue.json` — `v1_mvp_scope` + `explicitly_not_doing` (the UI shape + the chip family to reuse).

## 3. Next steps (ordered)
1. Read the four above (esp. eng path-eval for the exact endpoint/record shape).
2. **Backend:** add a committed `questions.json` (fetched at load, NOT inlined) holding the single crocosmia confirm; wire answers to the **dormant `/api/feedback`** (extend `context`, relax the one validation line the eng doc names) OR the `zone-feedback` pickup pattern — eng doc picks. Answer record = `status: pending` for Paul. **Do NOT coin a new `/api/mom-feedback` endpoint; do NOT build a merge/queue UI.**
3. **Frontend:** render ONE confirm, deterministically (model on `renderTodayGlance`/`computeLookFors` in viewer.html), reusing `.tag.t-{type}` pills / the `gg-suggest` chip family — **no new badge, no counter, no "outstanding"/list language.** Three branches: **Looks right · Not quite · Not sure** ("Not quite" pre-warms the composer for a verbatim correction). Optional verbatim note = the AI-free ObservationStore path (analog of `fnSaveNoteOnVehicle`, tagged `plantId`).
4. **Instrument the funnel** (extend `MetricsCollector`): `confirm_offered → confirm_viewed → confirm_tapped → confirm_answered_with_note`. This is the whole point — it distinguishes "never saw it" from "saw and ignored" (the ambiguity that made the ⭐ star's zero uninterpretable).
5. **Loop-close honestly:** her answer lands *with Paul* (say so warmly); do **NOT** write microcopy claiming the dashboard updated (it doesn't until Paul picks it up).
6. Ship: commit → `git pull --rebase` (weather bot) → push → `bash tools/deploy-worker.sh` → phone-verify (Safari-kill). If you touch `plants.json`, run `python3 tools/check-data-inline.py`. Release note (field-journal voice).
7. **Arm the ~2–3 week gate** and record it: *Grow* = Mom (`d-14nyhnjz`) answers ≥1 confirm (tap or note) on a day it was `viewed` → scale to the backlog. *Kill* = `offered`+`viewed` firing repeatedly with **zero `tapped`** → it's the next dead affordance, stop. *Ambiguous* = high offered / low viewed → reposition/extend.

## 4. State & pointers
- **Repo:** `~/Developer/Tate-Tracker` @ `3db19df` (clean at handoff). Public repo → GH Pages; Worker `tate-tracker.paul-kirschenbauer.workers.dev`.
- **Code the build touches:** `worker/worker.js` — dormant `/api/feedback` (~1799–1867), live `zone-feedback` GET/pickup. `viewer.html` — `renderTodayGlance`/`computeLookFors`, `.tag.t-{type}` / `gg-suggest` chips, `MetricsCollector`, the unified-input section.
- **The confirm subject:** crocosmia = 'Lucifer'? — a real open owner-Paul item (photo-read ID, blooming on-property now = the flywheel's fresh-signal hook).
- **No uncommitted work** to carry; everything is at HEAD.

## 5. Guardrails
- **Capture stays AI-FREE. Do NOT route the confirm through Garden Guru** — ai-advisor explicitly overruled that instinct (the payload is ground-truth adjudication of a claim we raised). The fence carries only metadata; the record is Mom's verbatim words.
- **ONE confirm at a time. Never a rendered list/queue/card/count.** Two questions on one surface = a to-do list = the thing we're avoiding.
- **Placement must be guaranteed-seen** and Mom-legible (icon+size+color+position, not label text; she reads in bed, no glasses).
- **"Not sure"/"Haven't looked yet" is first-class** — it's usable ground-truth. Attribute the uncertainty to Paul/the photo, never test her.
- Panel output = **expert proposals until Paul ratifies** ([[feedback_agent_proposals_not_validated]]); Paul greenlit the *build*, but check specific copy/placement calls with him if they feel load-bearing.

## 6. Done when
One crocosmia confirm renders in a guaranteed-seen spot, its three branches + optional verbatim note write Mom's answer (AI-free) to KV as `pending` for Paul, the `offered→viewed→tapped→answered` funnel is instrumented, the loop-close microcopy is honest, it's committed + pushed + Worker-deployed + phone-verified, and the ~2–3 week grow/kill gate is armed with metrics accruing. A cold reader can check each without judgment.

## 7. Un-sealed judgment (not yet on disk — resolve early)
- **The placement fork (the one real open design decision):** ux-expert says a **"From Paul" strip at the top of the unified-input section** (top-of-app, always-seen); user-researcher says **on the crocosmia entry inside the Plants card** (contextual, on the thing). Both are "guaranteed-seen"; they disagree on which. The synthesis leaned card-contextual-primary with a top-of-app fallback if `viewed` is low. **Pick one for v1 with Paul; instrument so you can tell if it's being seen.** This choice is make-or-break (every lens flagged placement as the thing that kills or saves it).
- **Endpoint choice** (`/api/feedback` extend vs `zone-feedback` reuse) — eng path-eval leans `/api/feedback`; either is fine, don't build a third. Read the eng doc's reasoning before deciding.
- **Naming + framing — Paul LOCKED it (2026-07-13). This OVERRIDES the content-steward + ai-advisor "Paul-attributed" framing.**
  - **Name: "Mama's Perspective"** (3rd-person section title, warm family-journal register).
  - **Framing = Mom ↔ app direct, NOT Paul-in-the-loop.** Paul's exact reasoning: *"we're already talking about it in person, so I'd rather it just be between her and the app when she's using it."* The goal is **driving Mom's engagement** — the app is HER space to record her read of the place, not a messaging channel to Paul. So: **do NOT foreground Paul** in the copy ("Paul isn't sure / your answer goes to Paul" → out). The panel's Paul-attribution was for answer-honesty; that job now shifts to a **"what's your read? — no wrong answer, 'not sure' is fine"** register, which "Mama's Perspective" carries naturally.
  - **Loop-close (still honest):** frame her answer as *added to the property's record / her perspective, noted* — do NOT claim the dashboard instantly updated (it doesn't until Paul folds it in), and do NOT frame it as "sent to Paul." Paul still picks up the `pending` answers on the backend; that just isn't surfaced to her.
  - Keep the three honest branches (Looks right · Not quite · Not sure). Content-steward does the final voice pass on THIS direction.

## 8. Trust status (per item)
- **Build is Paul-authorized (2026-07-13)** — GO. — *human-cleared.*
- The **converged design** (one confirm, AI-free, no queue, kill metric) — *strong 5-lens expert convergence, but proposals until Paul ratifies specific copy/placement.* Treat as the plan; confirm load-bearing UI calls with Paul.
- The **crocosmia='Lucifer' ID itself** — *model-flagged photo-read, NOT cleared* (that's precisely why it's the confirm subject; do not treat it as fact).
