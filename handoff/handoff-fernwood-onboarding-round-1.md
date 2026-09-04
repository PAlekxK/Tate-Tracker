<!-- clearing-state: LIVE — the forward baton after the 2026-09-04 rulings; close-out clears it when Paul's round-1 picks are on fernwood-13 -->
# PICK UP HERE — Fernwood, onboarding round 1 (written 2026-09-04 ~2:40 PM ET at the seam; staging = 95e518f)

**Where things stand.** Prod (main → GitHub Pages) is FROZEN; Mom's feedback is HELD. QA (staging → `fernwood-qa.pages.dev` behind Access + the `fernwood-qa` Worker) is a PARALLEL instance nobody shares with her; the features hold is LIFTED on QA only; Workers Paid is active; Deploy QA is fully green. THE GOAL: transition Mom by a message with a link → an account → full onboarding, the condo as the first run, naming as a step she answers. All in `BACKLOG.md`'s FREEZE block, in his words. The live queue: `.plans/2026-09-04-independent-queue.md`.

## What Paul is doing on his phone
**The exhibit:** https://claude.ai/code/artifact/805bf1a2-3213-4c2f-b1c6-c97e92f63df9 (private Artifact) — also `~/Desktop/design-options/4-onboarding-round-1.html`. Nine steps × three versions at 414 × A+, the 9/02 door + selector sets as baselines. **His picks land on `.decisions/fernwood-13.md`** (options: = the exhibit set) — verbatim, one letter or "none — <what's missing>" per step. Then: synthesize into the onboarding plan's first stage-notes (§D.3 of the process audit); killed options → `exhibit.py drop <id> "<his reason>"`.

## Run these first (session-start block in CLAUDE.md; the migration-era gates still apply)
```
python3 tools/qa-divergence.py --check · check-qa-fixtures.py --check · place-claims.py --check · check-public-build.py · build-library-index.py --check · check-storage-keys.py · build-viewer.py --check
```
Access token: `.private/cf-access-service-token.json`; CI has the same pair as repo secrets. Local `main` tracks `origin/staging` — a bare `git push` reaches QA, never her page; a push to `main` is Paul's own terminal.

## Open, in order (each ends at a gate)
1. **Round-1 picks → synthesis** (above). Before his synthesis, §D.4: a fresh-eyes pass on the mock screens scoped to *can a first-time reader complete this step* — never ranking.
2. **Stamp the vocabulary plan** `.plans/2026-09-04-vocabulary-nicknames-PLAN.md` (§4 amendment; condo word = "the record" until she names it) → queue #2 (words scheme; WORKER_BASE → instance config first).
3. **The onboarding plan** (queue #7) — drafted AFTER the picks; seats' trails already exist (journey map + step proposals in fernwood-private/.user-research/, both 2026-09-04). Carries 7a inventory, 7b the E2E two-agent walk, the naming step from the vocabulary plan.
4. Queue #4 C7 rows (R3 needs a WRITERS roster + guard), #5 vault 5a/5b, #6 UX sweep (owed, 56 viewer commits).
5. Process wiring (`.plans/2026-09-04-process-wiring-AUDIT.md` §B + §D): the `draft` stage word, the freeze pointer above the session-start fence, E2E's home, THE SWITCHOVER RULE (§D.5) — Paul stamps.

## Done this session (all on staging, all green)
Library index reads tracked sources only (Deploy QA green) · withCache best-effort (QA + prod by cherry-pick 315419c) · Workers Paid + QA library reloaded · Access secrets in CI · per-estate storage keys (C4 2b) · Guru cost analysis (`.engineering/2026-09-04-guru-cost-analysis.md`) · vocabulary plan + two seats folded · process audit + §D · journey map + step proposals + 27 mock screens (private sibling, committed 48b2798, no remote) · decision card fernwood-13 · design-options run log appended.

## Held / never re-open silently
Mom's feedback HELD · the condo research + the residency contradiction the researcher named (A6) live ONLY in fernwood-private · README title is the product-name plan's open question (other session) · the two orphan plans are the grooming session's · the recorder's 18:00Z run is the first since the KV cap lifted — read it, don't re-run it.
