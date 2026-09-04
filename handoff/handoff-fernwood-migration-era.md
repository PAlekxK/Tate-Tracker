<!-- clearing-state: LIVE — the forward baton for the Product Engine migration era; close-out clears it when the migration lands -->
# PICK UP HERE — Fernwood, migration era (written 2026-09-04 ~9:30 AM ET at close-out)

**Where things stand, in one screen.** Everything buildable without Paul is built and on **QA** (`staging` branch →
`fernwood-qa.pages.dev`, now behind Cloudflare Access, + the `fernwood-qa` Worker). **Mom's page (`main`) is frozen** by
Paul's ruling until he runs the migration himself. The migration is a **fast-forward** of staging onto main.

## Run these first (the deterministic doors — all in CLAUDE.md's session-start block)
```
python3 tools/qa-divergence.py --check      # what QA has that Mom does not; RED if main holds anything staging lacks
python3 tools/check-qa-fixtures.py --check  # no `_qaFixture` marker at origin/main (none exist today)
python3 tools/place-claims.py --check       # shared engine prose that claims a place: ratchet at 0 at the condo
python3 tools/check-public-build.py         # private-tier classes + the supplied-names needle row (exit 3 = sibling absent)
python3 tools/build-library-index.py --check   # the Guru's prose-library index still matches its sources (loaded on QA only)
```
The QA page needs the Access token: `.private/cf-access-service-token.json` (mode 600) — `tools/qa_access.py` adds the
headers for qa-walk · check-text-size-default · uniqueness-ledger · check-live. The Worker is not behind Access.

## What Paul owes (one at a time — his words on 9/04: "prioritize these decisions and give them to me one by one")
1. **The migration itself** — with Mom, at the visit (C4 2d also moves the origin to `kirschenbauer.myhome.place`). Procedure in
   BACKLOG "BUILD IT ALL IN QA" block: remove every `_qaFixture` on staging → rebuild → QA verifies → gates green → `git push origin staging:main` → prove live at 414×A+.
2. **Lift the features hold** (his 9/04 ruling: everything else before new features). Behind it: the vault (C6 5a/5b), the condo rows C7-R1…R5, the sky split, identity.theme's build, the settings selector.
3. **Name the condo's journal** (identity.journalTile/journalShort are agent placeholders) and its tagline → then the content steward.
4. **The three place-claim rows** were applied (chestnut callouts → property.json plantContext; sky verdict derived from bortleEstimate; the capture intro names the journal). Read `.content-reviews/2026-09-04-place-claims-classification.md` if he wants to see the classes.
5. Lower: Cloudflare Access token for CI (only if a workflow fetches the QA page); the two old Anthropic keys are REVOKED (done 9/04).

## What is held and why (never re-open silently)
- **Mom's feedback: HELD** — not ingested, not actioned — until Paul lifts the freeze in his own words (BACKLOG freeze block).
- **The condo research** (residency fact) lives in `~/Developer/fernwood-private/.user-research/` — never the public repo.
- **The Guru's honesty strings** are Paul-approved (Q6 closed, "login"); they live ONLY in `LOOKUP_STRINGS_TEMPLATE` (worker.js).

## The plans, by stage-note (read the plan, never this list, for detail)
- `.plans/2026-09-03-c4-environments-PLAN.md` — QA origin, Access, the fast-forward finding.
- `.plans/2026-09-03-c6-door-for-paul-PLAN.md` — 1b/1c A+ · 3a grant-mint · 6a dual-accept (prod too) · the door design note (username + password is Paul's model).
- `.plans/2026-09-03-guru-retrieval-PLAN.md` — 4a core · 4b flag · 5a lookups · 5b fences · 6a library · Q6 strings · the cost analysis owed (seeded to the meta-cycle).
- `.plans/2026-09-03-c7-condo-paper-model-PLAN.md` — Paul's two reads, the fixes shipped, the rows held.

## Cross-session
The other session (grooming, "fb") owns `.plans/2026-09-03-{c3-trace-query,product-name,grooming-conversation}*`, `.engineering/2026-09-03-*` seat trails, and pushed to `main` once (batch-2 grooming) — main is NOT frozen for docs, only for surface. Token optimization has no home yet: seeded to the meta-cycle (`~/.claude/agents/audits/NEXT-AUDIT-SEEDS.md`, 9/04).
