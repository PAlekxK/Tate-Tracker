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
| 0 | Environments + repo structure + rename | C4 | O3 | engine · must-not-diverge | ran: practice-steward · engineering-partner | ai-advisor · ux-expert · content-steward (no model, nothing she sees, no copy) | — | **plan DRAFTED** · 6 of 8 questions ruled · Q1 refined to THREE LEVELS (product apex · family door · instance) — **topology DELTA running** (prod moves to Cloudflare) · Q3 waits on the Guru seat's harness (now landed) |
| 1 | Record prep, data-model steps 1–5 | C5 | O3 | engine · must-not-diverge | engineering-partner (schema, KV prefix, manifest, config derivation) · practice-steward (the engine-manifest CHECK is a check) · content-steward, narrow (the product name in her prose) · (cite: data-model design §3–§5, §8) | ai-advisor (no model on the path) · ux-expert (nothing she sees changes) · user-researcher (no user question) | C4 (prefix + manifest only — steps 2, 3, 5a ship independently) | **both seats DONE** `.engineering/2026-09-03-c5-record-prep.md` · `.plans/2026-09-03-c5-manifest-check-PROPOSAL.md` · **plan drafting** (content-steward waived: the product name is upstream in C4 2a) |
| 2 | The door for Paul + M3 first | C6 | O3 | engine · declared | engineering-partner (auth mechanism on Workers+KV, tenant-from-credential, the textSize sync) · privacy/security seat when unparked · (cite: `.ux-reviews/2026-09-02-login-door-and-selector.md` · `.user-research/2026-09-02-activation-journeys.md`) | ai-advisor (no model on the path in this item) · content-steward (no Mom-facing copy: her surface is untouched) | C5 | **engineering seat DONE** `.engineering/2026-09-03-c6-door-for-paul.md` · privacy seat pending · plan waits on C5 |
| 3 | The condo as a paper model + the no-garden falsifier | C7 | O3 | config | engineering-partner (the falsifier harness, the plantless render) · (cite: `.user-research/2026-09-02-condo-feature-research.md` · `.content-reviews/2026-09-02-estate-naming-layer.md`) | ux-expert (nothing ships to her) · ai-advisor (the outward-facing domain is captured, not built) | C4 directory split · C5 | **engineering seat running** |
| 4 | Guru: from digest-stuffing to retrieval | A6 · *"How to evolve Guru's capability — the worked question"* | O2 | engine · must-not-diverge | ai-advisor (must) · engineering-partner (the test harness is the first build) · ux-expert (latency/streaming on her surface) · (cite: `research/2026-07-28-garden-guru-scope.md`) | content-steward (no copy until a surface exists) · user-researcher (her Guru use is measured, not asked) | C5 (the estate-scoped digest) | **ai-advisor DONE** `.ai-advisor/2026-09-03-guru-retrieval.md` (⚠️ found a LIVE defect → Tier 1 #16) · engineering + ux seats next |

**Order of running, two seats at a time** (the API dropped four of seven subagent launches on
2026-09-03): item 1 and item 2's engineering seats first → item 1's practice-steward and item 4's
ai-advisor → item 3's engineering seat and item 4's engineering seat → plans drafted per item as its
seats land → Paul stamps in whatever order he chooses.

**What the batch is expected to surface** (pre-registered, discharged in each plan's `## Retro` and
summarised at the end of this file when the batch closes): cross-item collisions the seats find while
looking at something else · the objective trace's coverage (if everything cites O3 and nothing cites
O1, that is a finding about the backlog) · whether the default-seats table produces all-waivers or
all-reviews across n=5 (the readiness proposal's §5 question, now answerable).

## Closing note — written when the batch closes

*(empty — the batch is open)*
