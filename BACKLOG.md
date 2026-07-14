# Fernwood — consolidated backlog

**This is the single source of truth for Fernwood backlog statuses.** Consolidated 2026-07-13
from the backlog fragments that had scattered across CLAUDE.md's many sections, the memory files,
and the design docs — and whose statuses had begun to conflict. When those disagree with this file,
**this file wins** (and the stale source should be fixed to point here).

The dated **"Pickup point"** sections in CLAUDE.md are a *historical log* of what happened each
session — keep them for the trail, but do **not** read them as current status. Read status here.

**Status taxonomy:**
- **SHIPPED** — live in production (GH Pages + Worker).
- **ACTIVE** — being worked right now, or a live measurement phase.
- **DEFERRED** — decided-not-now; each carries the **gate** that would unblock it.
- **IDEATION** — raised, not yet designed or decided.
- **KILLED / SUPERSEDED** — abandoned or folded into something else.

---

## ▶ NEXT — building now (decided 2026-07-13)

**Collapse Save / Ask → ONE button: "Log to Fernwood Almanac" (log-first, then Garden Guru).**
Paul's call, 2026-07-13. The unified input's two buttons become one. On tap it (1) writes her
**verbatim** entry to the almanac **first**, deterministically and AI-free — always succeeds, instant —
then (2) fires Garden Guru as a second step for the answer + follow-up opportunity. The log never
*depends* on the AI, so a Guru refusal / timeout / dead-signal can't eat the entry (this closes the
7/3 failure that turned Mom away on both the ask and the log).

- **Why decided now:** cost was the only suspected blocker and it's negligible — Haiku 4.5 at
  $1/$5 per MTok, ~a penny per warm turn / ~$0.10 cold-cache first turn, **~$5/mo measured**. The real
  reason two buttons existed was capture *reliability* + verbatim integrity, not cost — and log-first
  preserves both while giving Paul the single-button, always-logged, follow-up-enabled UX.
- **Build shape:** merge the two handlers in the unified-input section; Save's deterministic write runs
  first, then hands off to the Guru path. **Do NOT** route the log *through* Guru (that reopens the
  "did it save?" problem). Preserves [[feedback_no_ai_on_capture]] — the capture stays deterministic;
  AI is the second, best-effort step on the ask side.
- **Guardrail:** if Guru fails after the log lands, tell her calmly the note is saved but the answer
  didn't come through — never imply the note was lost.

## ACTIVE

| Item | What it is | Gate / next |
|---|---|---|
| **Save / Ask → one button** | See ▶ NEXT above — decided, building now. | In progress. |
| **Mama's Perspective — validation gate** | The shipped Mom confirm-queue is now in its ~2–3 week live-exposure test. | **Grow** = Mom answers ≥1 confirm on a day it was `viewed` → scale the queue. **Kill** = `offered`+`viewed` firing with **zero `tapped`** → it's the next dead affordance, stop. **Ambiguous** = high `offered` / low `viewed` → reposition/extend. Watch `momqueue_offered/viewed/tapped/answered`. |
| **Vehicle records — rest of the fleet** | Extend the shipped GTI service-records pipeline to the Bronco's bigger paper pile, then others. | Agent-can-drive. |
| **Bronco door-panel repair** | Paul's stated "next big project"; guide + verified buy-list ready, panel is out of the truck. | Physical work, owner: Paul. |

---

## DEFERRED (with the gate that unblocks each)

| Item | What it is | Gate |
|---|---|---|
| **Property map — zone-naming completeness pass** | The interactive zone map is **shipped** (lives at the top of the Property card, pan/zoom, tap/confirm). What's left is naming/populating the remaining zones + per-candidate `zoneAffinity`. | Paul's zone-naming pass. *(NB: the map surface itself is SHIPPED — the old "paused, don't build" note is stale.)* |
| **Phase G — observations as a knowledge layer** | Field notes feed other surfaces ("you noted the laurel opening April 25 last year — watch for it now"); the loop/flywheel's non-assistant surfaces. | Phase E proven **and** observation set ~50+ entries. |
| **"is it open yet?" bloom ground-truth loop** | Invite + fold back ground-truth on bloom timing (the flywheel's concrete trigger). | Part of the loop; Mama's Perspective now carries the first bloom confirm (panicle hydrangea). |
| **Bloom in "Worth noticing today" glance** | Surface bloom state in the top glance. | After de-crowding the "Peak this week" area. |
| **Phase H — audio identification** | Bird/sound ID; built end-to-end then hidden (👂 button `hidden`). | A mature free/single-vendor audio-ID path **and** a Mom-usage signal. |
| **Tool-use migration** | Move Garden Guru off system-prompt digest-stuffing to tool-use. | digest >80K **or** observations >50. ⚠️ **digest is ~80K now — at the ceiling.** This is the closest-to-triggering deferred item. |
| **Streaming responses** | Stream Guru replies (~30 lines client). | If turns feel laggy on LTE. |
| **Conversation browse UI** | UI to browse KV-stored conversations. | v2 want. |
| **Durable photo-in-note** | Persist photos in saved notes (stripped for iOS quota). | Needs own scoping; mirror the audio_ref server-blob pattern. |
| **Off-machine backup target (R2 vs Google Drive)** | The only unbuilt piece of service-records durability. | Paul's decision; Apple Photos is the interim second copy. |
| **Guru re-inline verification (root-cause fix)** | Make the promote flow verify its own re-inline commit landed (the Lizard's-Tail silent-drift failure mode). | Open root-cause; drift-check tools are the interim guard. |
| **Per-vehicle mileage/hours + last-service anchors** | Add anchors to all 15 assets. | Needs Paul's odometer/service readings. |
| **Tiguan / F-150 profile enrichment** | Fill the near-empty vehicle profiles. | Needs Paul's history input. |
| **Plants-to-consider gaps** | GFC 2026-27 seedling catalog (~Jul 1), UGA nursery list refresh, TACF, HRI, Mt. Cuba genera. | Time/source-gated. |
| **Citizen-science scaffolding** | Dormant code in viewer.html. | Paul's call: re-enable / drop / leave dormant. |
| **Guru-machines deferred bits** | On-card per-vehicle input; "which one?" disambiguation chip; notes-lister CLI. | ask-then-log made them unneeded; revisit on signal. |
| **Fairway / change-reactions confirm** | "Does the hub match the property?" reaction-to-a-change question (the Mama's Perspective schema already supports `kind: react`). | After confirms prove engagement; phrase as an observable, not a design review. |
| **Batch document-mining playbook** | Generalize the triage→characterize→verify→fold receipt-mining pattern cross-project. | Until a 2nd project needs it. |
| **Expert-proposed principles (candidates)** | "reuse the mechanism, not the semantics"; "match structure to the reader's unit of meaning"; "widen the ask → implied the log". | Paul demote/keep call. |

---

## IDEATION (raised, not designed)

| Item | What it is |
|---|---|
| **Automate the Fernwood Worker deploy** | `wrangler deploy` is currently Paul-only (auto-mode's classifier blocks the agent), so every digest refresh / endpoint change stalls on him. **Leading candidate:** a GitHub Action deploy-on-push to main with a `CLOUDFLARE_API_TOKEN` secret — CI does the deploy, not the agent, sidestepping the classifier (the repo already runs Actions via `record-weather.yml`, so the pattern's proven). Guardrail: trigger only on `worker/` or digest changes; keep the `/health` check. Alternatives: allowlist the wrangler command, or a git post-push hook. Captured in `~/.claude/handoff/captures-inbox.md`. Owner: Paul (deprioritized starting now). |
| **Photo-library vehicle/repair-photo miner** | Mine the ~50K-photo library for per-vehicle machine + teardown shots; propose-then-confirm. **NB:** since prototyped — now its own project (`~/Developer/photo-miner/`, memory `project_photo_miner`). Effectively ACTIVE there, not a Fernwood-repo item. |

---

## KILLED / SUPERSEDED

| Item | Resolution |
|---|---|
| **⭐ "this matters" star** | KILL — 0 uses / 104 revisits; revisit frequency *is* her curation. (Still in code; retire on next touch.) |
| **Seeded prompts** | Deprecate — 0 usage; a standing control she doesn't operate. |
| **🚩 open-feedback / standing "leave feedback" box** | DON'T BUILD — "the star all over again." General feedback lives as the one quiet foot-line in Mama's Perspective + out-of-band to Paul. |
| **Emailed Mom discovery interview** | DEAD — sent 5/29, refreshed 6/20+6/21, never returned; device + usage replaces it (the reframe behind Mama's Perspective). |
| **"prompt Mom for input" weed seed** | SUBSUMED into Mama's Perspective. |
| **Comprehensive UI/UX overhaul** | Dropped — let evidence commission targeted passes, not a speculative overhaul. |
| **Phase D classify-on-save** | Removed (kept dormant) — no-AI-on-capture principle. |
| **Classifier for machine-spec routing** | Rejected — the fused real message argues against routing. |
| **Weather Underground PWS (KGAJASPE279)** | Killed as a data source — the on-site Ambient Weather station is the sole source. Don't reintroduce. |
| **Two-box architecture (separate Field Notes + Garden Guru)** | Superseded by the unified input surface. |
| **Name "When you're out there"** | Superseded → **"Mama's Perspective"** (Paul's steer). |
| **Text-path plant-add (standing button)** | Don't ship — Paul-want, no Mom-signal; if ever built, funnel back to the photo path. |

---

## SHIPPED (for reference — the built base these build on)

Mama's Perspective (Mom confirm queue, 2026-07-13) · Unified input (Save/Ask + auto-save, 5/20) ·
The Almanac card (5/21) · Garden Guru Phase E conversational layer (5/19) + redesign Phases 1–3 (7/02) +
into-the-machines (7/07) · Phase D capture rebuild (5/19) · Phase F image input → auto-promote (5/21) ·
Concept A "Today + Reference Drawer" / computeLookFors (7/05) · structured `peakDates` (7/06) ·
Fishing granular + dynamic, own card (7/06) · Plants bloom-time + Hydrangea hub (7/12) ·
**Property zone map** in the Property card (interactive, 5/28) · Vehicles "what she needs" restoration
list (6/12) + "what she's had done" service-records pipeline (7/09) + per-step tap-to-call contacts (6/28) +
registration reminders (7/11) + manuals corpus (7/08) · Metrics capture (5/20) · analyze-fernwood.py (5/21) ·
Sources card (5/21) · Worth Considering candidates card (5/26) · drift-check tools + deploy-worker.sh ·
cross-device zone sync fix (5/28) · storage-quota / sanitize-at-boundary fix (5/26) · Mom no-glasses a11y.

---

## Reconciliation notes (what was conflicting — resolved 2026-07-13)

- **Mama's Perspective shipped, but three "authoritative" docs still said HELD / not-a-queue.** Paul steered
  the panel's "single confirm probe" into a navigable, continuously-populatable **queue** and it shipped the
  same day (git `a888ebb`). The CLAUDE.md top Mom-backlog section, the panel synthesis "master brief," and the
  `project_fernwood_prompt_mom_input` memory all still described the held design. **Ground truth = code +
  RELEASE_NOTES + git HEAD.** CLAUDE.md + the memory index have been updated to SHIPPED; the dated design docs
  are left as historical point-in-time artifacts.
- **Property map** — code check confirmed it's SHIPPED (live in the Property card), not "paused." Only a
  zone-naming completeness pass remains (DEFERRED above).
- **Photo-library miner** — CLAUDE.md said "not started"; it was since prototyped and moved to its own repo
  (`~/Developer/photo-miner/`). Tracked there now, not as a Fernwood-repo backlog item.
