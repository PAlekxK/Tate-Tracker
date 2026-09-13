# HANDOFF — LAP 9 · THE DOOR · A5·A6·A7·A8·A9·A10·H3 landed; stopped AT A3's design question

<!-- generated 2026-09-13 ~02:50 ET · source: Tate-Tracker@3dda851a · main · CLEAN TREE
     RECEIVER: verify the sha against HEAD before trusting any status below.
     ⛔ Cite the SYMBOL, stamp the sha, re-read immediately before the commit. -->

## 1 · What landed, and dev is serving it

```
3dda851a  A8   hostAgrees is CSRF, not tenancy (comment only; checked against the deploy)
3190c87d  A9✚  the shelf went into a branch that CANNOT RUN — live one is inside the credential gate
b414f981  A9   the shelf: every house a person holds, not the one the credential belongs to
41135e77  H3   the positive control, on the second attempt
49fe8c8e  A7   `X-Estate` + A10 (the 409 STAYS, reworded) + H3's fixture
a88e88a2  A6₂  67 edges written at dev · --check clean · --resolvable before/after
6e68f3de  A5+A6 route stops naming the estate; the person→estate edge replaces it
```
`/health` at dev: **build_sha 3dda851a = HEAD** · env=dev · est-lab0001. ⛔ NOTHING IS PUSHED.

**Verified, not asserted:** `falsifier-tenancy.py` 10 clauses ✅ at dev (P1 P2 C1 C2 C2b C2c C2d C3
C4 C5) · `grant-edge-backfill.py --check` 67/67 edges, every one at a PROVEN estate ·
`--resolvable` `route 42 · none 16 · legacy 11 · edge 2`, **zero rows reachable before and not
after** · `--selftest` 24/24 by mutation · A8's three Origin cases probed live.

## 2 · ⛔ THE DENOMINATOR IN THE PREVIOUS HANDOFF WAS WRONG — do not re-inherit it

It said `est-lab0001:grant: 43 keys ← the backfill's denominator`. The A6 edge is **deliberately
unprefixed**, so its reach is the whole namespace: **71 grant rows across 13 estate prefixes** →
**67 edges + 2 refused**. 43 was right about a prefixed count and wrong for an unprefixed index.
**Fourth instance of this lap's signature failure** (dispatcher 20-of-24 · `enclosing()` 13-that-
were-2 · this · and §4 below).

## 3 · ⭐ THE BIG FINDING: 16 of 71 rows at dev resolve by NO path — and it predates this lap

`--resolvable` baseline, taken BEFORE the backfill. **14 are `est-3c9f1a` rows with no `route:` row
at all**, because `grant-route-backfill.py` lists `<ESTATE_ID>:grant:` and never reached the 28 rows
at other estates. The other 2 are mis-keyed rows that are terminal by C1 (correct).
⛔⛔ **DO NOT "FIX" THIS.** Giving those 14 a route RESURRECTS historical credentials. That is a
security act, Paul's, not a migration. Also in `~/.claude/handoff/captures-inbox.md`.

## 4 · ⛔ TWO PLACES I WAS WRONG TONIGHT — both caught by verifying, both worth knowing

1. **I retired the 409 `already-has-an-estate` and had to revert it.** `.plans/2026-09-10-OPEN-ITEMS.md`
   ①·2 says the workaround "is dead" with a same-commit `C2 retired by name`; the **09-11 plan row A10
   says the 409 STAYS**, the 09-11 re-audit confirms it, and `VOCABULARY.md:483` calls it a ruled
   invariant. The newer document wins. ⚠️ That `C2` label is **defined nowhere in the corpus** and is
   NOT `falsifier-tenancy`'s C2 (*"A cannot NAME B"*), which A7 strengthens.
   ⭐ And the code argues for keeping it: `handleEstateFound` keys the new grant by the CURRENT
   credential's hash, so founding a second estate gives ONE hash live grants at TWO estates — exactly
   what `resolveByEdge` now refuses. No client sends `X-Estate` yet, so removing the 409 today turns a
   clean named 409 into a silent 404 on everything.
2. **A9's repair went into unreachable code and I deployed it before noticing.** `/api/grant/whoami`
   has TWO identical empty-shelf branches; the live one is INSIDE `if (request.headers.get(GRANT_HEADER))`
   (every path in that gate returns). The dead one is below it and is now **marked, reverted, and left
   for a human to delete** — deleting a route branch is a behaviour change.

## 5 · ⭐ WHERE I STOPPED, AND IT IS A DESIGN QUESTION NOT A BLOCKER — A3

A3 converts the 4 **B-CACHE** sites (`ambient`/`airnow`/`drought`/`today-line`) to per-estate keys.
✅ **Its stated precondition is now MET** — a second estate CAN authenticate at dev (falsifier P2).
✅ **Its fixture blocker is cleared** — the four `@lab` identities are **re-keyed to `@dev`**, each
verified to hold a grant edge in `[env.dev]`'s own namespace first (never inferred from the rename);
backup at `.private/synthetic-identities.json.pre-dev-rekey.bak`.
⛔⛔ **THE UNANSWERED QUESTION: `/api/ambient` IS DELIBERATELY UNGATED** (2026-08-02, so Mom's
unpaired devices keep working). An ungated request has no grant, so `scopeFor(request, env, null)`
returns the DEPLOYMENT's estate and the conversion is a **no-op on exactly the path the leak
argument is about**. A paired device would key per-estate; an unpaired one would not — one cache,
two key spaces, and the household-identifying suffix still sits under the deployment prefix for
anyone unpaired. **That is a design call, not a mechanical conversion.** A3's own text does not
address it. Do not guess it at 3am; it is worth ten minutes awake.
⚠️ A3's check also needs two **PLACED** households (`synthetic-identity.py --complete-setup <role>`),
which is a different fixture from the falsifier's grant-only pair. Not run.

### ⭐ A3 IS 3 SITES, NOT 4 — MEASURED, so the next lane does not re-derive it
`/api/airnow` · `/api/drought` · `/api/today-line` all dispatch **BELOW** the capability gate and are
named in `MEMBER_OK`, so every caller has a resolved grant and `scopeFor(request, env, grant)`
converts them **meaningfully**. `/api/ambient` dispatches **ABOVE** that gate (deliberately ungated
since 2026-08-02 so Mom's unpaired devices keep working), so it has no grant and the conversion is a
**no-op** there.
⛔⛔ **AND `/api/ambient` MUST BE LEFT *UNCLASSIFIED*, NOT DECLARED.** Declaring it in
`worker/scope-sites.json` would assert *"this one stays on `scopeOf` BY DESIGN"* — which is exactly
what nobody has ruled. Unclassified is the honest state for a site awaiting a ruling, and it has the
right consequence: **A14's 0-unclassified clause holds the gate shut until someone answers.** That is
the gate working, not the gate blocking.
⭐ **The real question, framed so it can be answered in one sitting:** *should `/api/ambient` be gated
at all?* It is a product-and-security call (the 2026-08-02 reasoning is Mom's access, and it is
strong), not a conversion detail. **Paul's.**

## 5b · ⛔ A FOURTH MORNING ITEM — `.plans/2026-09-10-OPEN-ITEMS.md` IS SUPERSEDED AND STILL IN PLACE
Its ①·2 says the 409 workaround "is dead" with a same-commit `C2 retired by name`. The 09-11 plan row
A10 says the opposite in four words. **It cost a near-miss tonight** (a behaviour change written,
committed and reverted) and it will do it again to the next reader. Strike it or date-stamp it.

## 6 · Still owed
- **A11** — copy is on disk (`.ux-reviews/2026-09-12-A11-signin-door-copy.md`, another lane's file,
  untracked). Gate LIFTED as a 2026-09-12 expedite exception with **Paul's review DEFERRED TO
  IN-SITU** — record it as OPEN in the commit and at the top of that file. ⛔ The byte-identical
  refusal string is a SECURITY invariant the exception does NOT cover.
  ⚠️ Same commit must fix `tools/journey-logic.py:185` (`"<title>My Home</title>"`) or gate 1 breaks.
- **A12** (2+ branch, walk as a mechanism test, declared as such) · **A13** (cite the ruling at
  `2f85f3a3`, do not re-spawn; third 409 site is `handleUsernameChange`) · **A14** · **A15** · **H1**
  (two browser contexts, ahead of A11).
- **The QA deploy** — Paul pre-authorized it **in the build window, first-hand**. Ordered: only once
  the conversion has SETTLED. Re-state the real commit count at the act (228 behind at 02:50), tell
  the coordinator immediately, and ⛔ **if the pre-push guard refuses, STOP** — never the escape token.
- **`falsifier-tenancy.py` covers path 2 now** (its fixture carries the person + the edge). Before
  tonight it wrote `{estateId}`-only routes, so **A5/A6/A7 were untested by the one tenancy
  instrument** while it read green.

## 7 · ⚠️ Instruments to trust carefully
- `storeResolveRecord` → `<estate>:resolve:<date>` is **proven end-to-end** (2 real
  `ambiguous-refused` fires, read back by `grant-edge-backfill.py --check`). Its 2 records are LEFT
  in place; they happened.
- `--check` exits **1** at dev by design: the 2 mis-keyed rows are reported with ⭐ COVERAGE NOT
  LOST. **Red with an explanation, not green with a silent skip.** Do not "fix" the exit code.
- ⛔ `synthetic-identity.py --login` **prints the credential in a walk link**. `owner@dev`'s token is
  in the 2026-09-12 build transcript — synthetic, dev-only, re-mintable, no real person.
