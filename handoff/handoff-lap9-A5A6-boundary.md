# HANDOFF — LAP 9 · THE DOOR · stopped AT the A5+A6 migration boundary

<!-- generated 2026-09-12 · source: Tate-Tracker@2f85f3a3 · main · CLEAN TREE
     RECEIVER: verify the sha against HEAD before trusting any status below.
     ⛔ Cite the SYMBOL, stamp the sha, re-read immediately before the commit. -->

## 1 · Where this stopped and why

**`[paul-ruled 2026-09-12]` — STOP AT A5+A6, RESUME FRESH.** Offered stop / do-it-tonight /
land-code-only; he chose stopping. **Nothing is broken, nothing is half-applied, the tree is clean.**

**A5+A6 is the first step in this lap that touches LIVE DATA**, and the plan makes them ONE commit
for a hard reason: A5 drops `estateId` from the `route:` value, and if `grantsFor` does not exist
yet **`grantFor` has nothing left to resolve and EVERY CREDENTIAL DIES AT ONCE.**

## 2 · Done — A0 · A1 · A2 · A4 (+ the security seat)

```
check-scope-sites.py:  58 baseline -> 32 live · 26 converted · 8 declared · 24 unclassified
```

| step | state |
|---|---|
| **A0** | ✅ `tools/check-scope-sites.py` + `worker/scope-sites.json`. Selftest 7/7 by mutation |
| **A1** | ✅ sentinel **`est-hmqec0`** minted + recorded in `VOCABULARY.md` §3i. ⛔ **BINDS NOTHING** |
| **A2** | ✅ six batches, every convertible B-CALLER site |
| **A3** | ⏸ written, **deliberately NOT run** — see §5 |
| **A4** | ✅ 8 declared with individual reasons; 24 unclassified **on purpose** |
| **Q3** | ✅ security-steward filed → `.engineering/2026-09-12-signin-door-disclosure-RULING.md` |

## 3 · ⛔ THE MIGRATION, measured — do not re-derive this

```
est-lab0001:grant:   43 keys      <- the backfill's denominator
route:               54 keys
grant:                0 keys      <- the NEW A6 edge prefix, empty
est-lab0001:account: 53 rows      <- 52 carry a personId · 1 UNREADABLE
```

**The 11-row gap between routes and grants is DANGLING ROUTES — the expected C1 case** (a dangling
route must 404, never fall back to the deployment's estate).

⭐ **THE EDGE IS DELIBERATELY UNPREFIXED and this LOOKS like a C5 6a/6b violation.** It is not. The
whole point is finding a person's estates **without already knowing the estate** — the *"lookup is the
harder half"* problem `grantFor`'s own comment names. **`route:` is already unprefixed for exactly
this reason**, so this follows the existing precedent rather than minting an exception. Someone will
challenge this; the answer is `route:`.

## 4 · ⭐ THE THREE-STEP SPLIT — the reasoning, not just the steps

The plan calls A5+A6 one commit. **That is right for the CODE and wrong for the BACKFILL.**

1. **Land the CODE** — edge writer on every grant write · `grantsFor(env, personId)` · `route:`
   stops naming the estate · `grantFor` resolves person → grants. **One commit, as the plan requires.**
2. **Run the BACKFILL as its own verified act** — dry-run printing what it would write, then write,
   then verify 43 edges exist and **every one points at an estate that exists**.
3. **Deploy dev, confirm every existing credential still resolves.**

⛔ **Why split:** a backfill is a MIGRATION, and this repo's doctrine is that a migration is verified
separately rather than riding inside a code commit. Collapsing 2 and 3 into 1 is the thing to refuse.

✅ **A6's named precondition is MET: B3 SHIPPED.** `worker.js:1039–1040` — `handleSession` goes
through `putAccount` when `acct.personId` exists; the residual bare put at `:1040` is confined to
legacy rows with no personId and `putAccount` throws without one, so it is deliberate, not a bypass.
⚠️ **OPEN QUESTION, not a finding:** 52 of 53 dev account rows carry a personId and **1 is
UNREADABLE** — unreadable is not "none". If a no-personId row exists, `grantsFor` returns `[]` for
it under A6.

## 5 · ⛔ A3 is ordered AFTER the conversion — it is NOT fixture-blocked

Its check wants *"two households fetch weather at dev"*. `worker.js:1683` still rejects
`row.estateId !== env.ESTATE_ID`, so **a second estate cannot AUTHENTICATE**. That state is what
this lap CREATES. Running it early returns the verdict `falsifier-tenancy.py`'s docstring exists to
refuse: *estate B holds no foreign coordinate because estate B holds nothing.* **Green by absence.**
⚠️ `falsifier-tenancy.py --setup` does NOT serve A3 — it mints **grant rows only**. A3 needs a
**place**, which is `synthetic-identity.py --complete-setup`. Different fixtures.

## 6 · Still owed before ANYTHING certifies

1. ⛔ **ROW 89 SHIPS WITH THE DOOR** — zone keys under a bare browser key + a 1500 ms boot timer that
   POSTs one household's overrides into another's. Symbols confirmed at HEAD.
   ⚠️ `check-storage-keys.py` now names **6** unclassified keys, not row 89's 2.
2. ⛔ **THE QA DEPLOY** — qa serves `87c7aae`, **220 behind**. Deliberately held so the candidate is
   not a half-converted worker. **Schedule it as an early beat, never at gate ①.**
3. **BACKLOG row 92 names 1 of 3 routes** — `/api/account/username` and `/api/session` are omitted.
   **Widen it.** (⛔ route it to the backlog window; this lane must not write `BACKLOG.md`.)
4. **The lab→dev relabel is HALF-LANDED and UNAUTHORISED** `[paul-ruled 2026-09-12: not this lap]`.
   Captured at `~/.claude/handoff/captures-inbox.md`. ⚠️ It contains a ruled KILL that happened
   anyway — **unresolved, and Paul's to rule.**

## 7 · ⚠️ Two instruments of MINE were wrong, and both are fixed — do not re-trust blindly

1. **"0 routes above the resolution"** — matched only single-line dispatches. **There are SEVEN**, all
   pre-auth, and two of them write household data.
2. **`enclosing()` credited 13 dispatcher sites to `handleFeedback`**, which holds 2. The dispatcher
   is `export default { async fetch(...) }` — not a `function` declaration. **Fixed at `32f7fb71`.**
   ⚠️ **Function counts in commit messages before that sha are inflated. Site counts were always right.**

**The lesson both times is this lap's own:** a control correct about its narrow question, trusted for
a broader one. **Re-measure before quoting any count from a commit message.**
