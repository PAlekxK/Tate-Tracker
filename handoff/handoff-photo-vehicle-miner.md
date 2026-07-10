# Handoff: photo-vehicle-miner
<!-- generated 2026-07-10 (ET) · sources: Tate-Tracker@4afb812 · RECEIVER: verify shas vs HEAD before trusting any status below; an AI/subagent FLAGS, never CLEARS -->

## 1. Mission (one line)
Run Paul's **photo-library vehicle/repair-photo miner** idea through the expert team → produce a scoped, decision-ready recommendation + MVP plan (research/scope only; do NOT build).

## 2. Read first (point, don't paste)
- `~/Developer/Tate-Tracker/CLAUDE.md` → the **"🔭 Backlog idea (raised 2026-07-09) — photo-library vehicle/repair-photo miner"** bullet inside the `## Pickup point — last session ended 2026-07-09` section. That bullet IS the spec; this brief operationalizes it.
- Memory: `project_vehicle_service_records` (the shipped document pipeline this is the *photo* sibling of — same propose-then-confirm discipline), `project_photo_library_overhaul` (the ~50K-asset Apple Photos library + its SSOT `photos-project/README.md`), `project_bolores_visual_archive` (a PAUSED Bronco visual-archive effort — check for reusable scaffolding/decisions before designing fresh), `feedback_no_ai_on_capture` (capture stays AI-free; AI on the ask path).
- Precedent to mirror: how the 2026-07-09 GTI service-records trial ran its expert panel (eng-partner + ai-advisor + ux-expert in parallel, grounded, then synthesized) — same shape here.

## 3. Next steps (ordered)
1. **Spin up the expert panel in parallel** (Agent tool), each grounded in §2, on the SAME question — "how should we build a tool that surfaces + proposes per-vehicle photos (the machines AND Paul's repair/teardown shots) from a ~50K Apple Photos library, seeded from albums?":
   - **engineering-partner** (path-eval): matching/architecture — album-seed + EXIF (date/geo) + burst/filename clustering as the deterministic spine; where proposals + confirmations are stored; how it plugs into the vehicle cards + the narrative "book"; reuse of osxphotos (already installed) + the `.private/` store pattern.
   - **ai-advisor** (consult): the **deterministic-vs-learned split** and the "we can train it" mechanism specifically — what's pure-deterministic (album membership, EXIF, clustering), what needs a learned visual-match layer (is-this-the-GTI vs the Bronco vs a dirt bike), on-device (e.g. Photos' own ML / a local model) vs API vision, and how a *train-from-Paul's-confirmations* loop works while keeping AI on the ask path (propose-then-confirm, never auto-file).
   - **ux-expert** (review): how proposals surface for Paul's confirm (a review/triage surface — batch accept/reject per vehicle), Mom-irrelevant here (Paul-facing), field-journal tone.
   - **(optional) user-researcher**: only if the panel wants Paul's actual foraging behavior modeled — likely skip for v1.
2. **Synthesize** the three into ONE recommendation: the deterministic MVP (what ships first, no ML), the trainable layer (when/if), the storage + card/book integration, and the 2–3 decisions that are genuinely Paul's.
3. **Present to Paul** as a scoped plan (draft-then-confirm) — do not start building.
4. **Update the backlog bullet** in Tate-Tracker/CLAUDE.md with the outcome (scoped / decisions-open), and the `project_vehicle_service_records` memory's photo-miner note. Commit.

## 4. State & pointers
- **Seed albums (Apple Photos):** the **Bolores/Bronco** album, and a **new dirt-bikes album Paul just started**. These are the training/seed anchors.
- **Library:** ~50K assets (see `project_photo_library_overhaul`). **osxphotos** is installed (`uv tool`; `~/.local/bin/osxphotos`) — the deterministic capture tool.
- **Repo:** `~/Developer/Tate-Tracker` (canonical post-2026-07-09 recovery; NOT `~/Documents/Claude`). Vehicle cards = `vehicles.json` → `viewer.html`. Private store pattern = `.private/service-records/` (gitignored).
- The narrative "book" of work-done is the downstream consumer of the surfaced repair photos.

## 5. Guardrails
- **Scope/research ONLY — do not build.** Output is a plan for Paul's confirm.
- **Propose-then-confirm; AI on the ask path; capture stays deterministic** (`feedback_no_ai_on_capture`). Never auto-file/move/delete library assets — surface proposals, Paul confirms.
- **Read-only against the actual Photos library** during scoping (osxphotos exports copies; never mutate the library).
- Check `project_bolores_visual_archive` for prior decisions BEFORE proposing a fresh design (it's a paused sibling — don't reinvent).
- Deterministic-first: pressure-test how far album-seed + EXIF + clustering gets before any ML is justified.

## 6. Done when
A synthesized expert recommendation + MVP plan (deterministic layer, trainable layer, storage, card/book integration, Paul-owned decisions) has been presented to Paul, and the backlog bullet + memory updated with the outcome. No code written.

## 7. Un-sealed judgment (open reads, not yet on disk)
- Hunch: the **deterministic layer alone** (album membership as ground-truth seeds + EXIF date/geo + burst clustering + "shot at the property/garage" geofence) likely captures most of the value before any learned model — worth the panel testing that hypothesis first, so "we can train it" stays a phase 2, not a prerequisite.
- The **repair/teardown shots** are the high-value, hard part (they're close-ups of parts, not whole-car — visual match to "which vehicle" is weak; EXIF-time-clustering to a known service *date/event* may be the stronger signal — e.g. "shot the same week as the Autohaus water-pump job"). Flag this to ai-advisor + eng-partner.
- Apple Photos already runs on-device ML (scene/object) — worth asking whether osxphotos can read any of that (labels/faces/computed albums) as a free deterministic-ish signal.

## 8. Trust status (per open item)
- Nothing here is a model-flagged "fact" — this is a *research/scoping* task, not a verification one, so there is no unverified-value-reaching-a-surface risk. The one thing to carry forward accurately: the shipped GTI pipeline's discipline (propose→human-fold) is the pattern to inherit, and it is Paul-validated.
