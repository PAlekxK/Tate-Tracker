# THE GROOMING QUEUE — 2026-09-03 `[paul-approved]`

**What this is.** The batch of items being taken to READY while C4 is the one item in the pipeline.
Grooming (seats → plan → stamp) is not the pipeline (concept → build → qa → shipped); several items
may sit at READY, **one** may be between concept and QA. Mechanism: `.plans/2026-09-03-backlog-readiness-PROPOSAL.md`.
Check: `tools/check-backlog-ready.py`. **State below is DERIVED** — the plan file's existence and
header are the truth; this table is the map. If they disagree, the file wins and this row is stale.

⚠️ **Every plan drafted before C4's rename lands cites files by section and role, never by path**, and
carries `depends-on: .plans/2026-09-03-c4-environments-PLAN.md` where it does — the check flags a
plan whose dependency is newer than it.

**Seat rule per the defaults** (readiness proposal §2): a seat that already produced a trail for the
item cites that trail — a review is not re-run because a plan is new. Waivers carry a reason.

| # | item | row | objective | class | seats to run · (existing trails to cite) | waived (reason) | depends on | state |
|---|---|---|---|---|---|---|---|---|
| 0 | Environments + repo structure + rename | C4 | O3 | engine · must-not-diverge | ran: practice-steward · engineering-partner | ai-advisor · ux-expert · content-steward (no model, nothing she sees, no copy) | — | **plan DRAFTED** · 6 of 8 questions ruled · Q1 refined to THREE LEVELS (product apex · family door · instance) — **topology DELTA running** (prod moves to Cloudflare) · **STAMPED `[paul-approved 2026-09-03]` · stage: build** — 1a bundle ✅ · 1b sibling ✅ · 1c rewrite ✅ (three filter-repo passes, verified) · 1d PUSH ✅ (live-verified) · **next: 3a `[env.qa]` — the QA Worker; the sibling's `/encrypted-backup` still owed** |
| 1 | Record prep, data-model steps 1–5 | C5 | O3 | engine · must-not-diverge | engineering-partner (schema, KV prefix, manifest, config derivation) · practice-steward (the engine-manifest CHECK is a check) · content-steward, narrow (the product name in her prose) · (cite: data-model design §3–§5, §8) | ai-advisor (no model on the path) · ux-expert (nothing she sees changes) · user-researcher (no user question) | C4 (prefix + manifest only — steps 2, 3, 5a ship independently) | **plan DRAFTED** `.plans/2026-09-03-c5-record-prep-PLAN.md` · check silent · **7 questions open before the stamp** (the module unit first) |
| 2 | The door for Paul + M3 first | C6 | O3 | engine · declared | engineering-partner (auth mechanism on Workers+KV, tenant-from-credential, the textSize sync) · privacy/security seat when unparked · (cite: `.ux-reviews/2026-09-02-login-door-and-selector.md` · `.user-research/2026-09-02-activation-journeys.md`) | ai-advisor (no model on the path in this item) · content-steward (no Mom-facing copy: her surface is untouched) | C5 | **engineering seat DONE** `.engineering/2026-09-03-c6-door-for-paul.md` · privacy seat pending (agent or checklist — Paul's call) · **plan DRAFTED** `.plans/2026-09-03-c6-door-for-paul-PLAN.md` · check silent · **6 questions open before the stamp** |
| 3 | The condo as a paper model + the no-garden falsifier | C7 | O3 | config | engineering-partner (the falsifier harness, the plantless render) · (cite: `.user-research/2026-09-02-condo-feature-research.md` · `.content-reviews/2026-09-02-estate-naming-layer.md`) | ux-expert (nothing ships to her) · ai-advisor (the outward-facing domain is captured, not built) | C4 directory split · C5 | **engineering seat DONE** `.engineering/2026-09-03-c7-condo-paper-model.md` (the falsifier was vacuously true; the blocker is the place group) · **plan DRAFTED** `.plans/2026-09-03-c7-condo-paper-model-PLAN.md` · check silent · **9 questions open before the stamp** |
| 4 | Guru: from digest-stuffing to retrieval | A6 · *"How to evolve Guru's capability — the worked question"* | O2 | engine · must-not-diverge | ai-advisor (must) · engineering-partner (the test harness is the first build) · ux-expert (latency/streaming on her surface) · (cite: `research/2026-07-28-garden-guru-scope.md`) | content-steward (no copy until a surface exists) · user-researcher (her Guru use is measured, not asked) | C5 (the estate-scoped digest) | **ai-advisor DONE** `.ai-advisor/2026-09-03-guru-retrieval.md` (the live defect it found → Tier 1 #16, FIXED + deployed) · **engineering DONE** `.engineering/2026-09-03-guru-harness.md` · ux-expert waived (no surface changes until streaming is chosen — it runs at that step) · **plan DRAFTED** `.plans/2026-09-03-guru-retrieval-PLAN.md` · check silent · **10 questions open before the stamp** |

**Order of running, two seats at a time** (the API dropped four of seven subagent launches on
2026-09-03): item 1 and item 2's engineering seats first → item 1's practice-steward and item 4's
ai-advisor → item 3's engineering seat and item 4's engineering seat → plans drafted per item as its
seats land → Paul stamps in whatever order he chooses.

**What the batch is expected to surface** (pre-registered, discharged in each plan's `## Retro` and
summarised at the end of this file when the batch closes): cross-item collisions the seats find while
looking at something else · the objective trace's coverage (if everything cites O3 and nothing cites
O1, that is a finding about the backlog) · whether the default-seats table produces all-waivers or
all-reviews across n=5 (the readiness proposal's §5 question, now answerable).

## Next batch — queued, not groomed

| # | item | row | objective | class | seats | depends on | state |
|---|---|---|---|---|---|---|---|
| 5 | The setup journey — invite → account → profile → devices joined `[paul-stated 2026-09-03]` | `PRODUCT-ENGINE.md` § THE SETUP JOURNEY | O3 | engine · declared | user-researcher (the four journeys, re-read against a setup phase) · engineering-partner (account record, device binding, the sync path) · practice-steward if the invite becomes a governed act | C5 (1b) · C6 | **captured** — collides with § ACTIVATION; Paul resolves the collision before seats run |

## Closing note — the batch CLOSED 2026-09-03: five plans drafted, zero stamped, check silent across all five

**The three pre-registered questions, answered from the files (not from memory):**

1. **Cross-item collisions the seats found while looking at something else — seven, all recorded:** Bob's full name
   already on `origin/main` (topology seat) · two Worker write paths ungated by design (topology) · the Guru hard-facts
   block injecting the stale 2,959 ft — FIXED + deployed the same day, Tier 1 #16 (ai-advisor) · the deploy workflow's
   `paths:` missing four digest sources, Tier 1 #17 (harness seat) · the C4 5c falsifier vacuously true on an empty
   `engine/` (C7 seat → C4 plan amended) · `momQueue.*` keys holding per-estate state on a per-family origin (topology
   delta) · `momlib.resolve_token()` falling back to the prod token (harness seat). **Every one was caught mechanically or
   by a second reader; none by anything looking wrong.**
2. **Objective coverage:** four plans cite **O3**, one cites **O2**; **nothing cites O1, O4 or O5.** A finding about the
   batch, not the items: the batch is the engine's, and Mom's adoption (O1) and the fleet record (O4) have no groomed item.
   The mom-cycle and fleet loops own O1/O4 work by design, so the absence is expected — but a second batch should start there.
3. **Reviews vs waivers across n=5:** seats run or cited **12**, waived **14** (every waiver with a reason). Neither
   extreme: the defaults produced judgment, not paperwork. ⚠️ The waivers cluster on `ux-expert` (5 of 5 items) and
   `content-steward` (4 of 5) — correct for an engine batch, and the exact thing to re-read when a Mom-facing item is groomed.

**Dependencies, derived:** C4 ← nothing · C5 ← C4 · C6 ← C5, C4 · C7 ← C4, C5 · Guru ← C5, C4. `check-backlog-ready.py`
flags any plan whose dependency is re-added newer than it. **Steps that ship independently of every dependency**, named
in the plans: C5 steps 1–4 (personId, ids as data, the module declaration, the config accessor + lint) · C7 step 0 (the
null-guard pass) · Guru step 1 (the origin enum, the latency clocks, the debug field, the `paths:` fix).

**Questions open before any stamp:** C4 **1** (the apex name) · C5 **7** · C6 **6** · C7 **9** · Guru **10** — each plan's
last section, one sentence each. The module UNIT (C5 Q1) is upstream of C5, C7 and Guru.
