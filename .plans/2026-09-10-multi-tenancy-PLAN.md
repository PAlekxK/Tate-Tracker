# Multi-tenancy — an estate is a ROW, not a deployment

`[paul-ruled 2026-09-10]` — *"production as a clean slate other than what people
established… all we really do is give them a grant owner token, owner member, and then that
gives them the right to establish their own estates. I think the only estate truly in
production should be Grant Park Condo, which I established with my user production account."*

And, the same day, where it is going:

> *"we're gonna get that all cleaned up to the point that we can confidently send out Nigel
> and Aida's invites and they will have and set up their own production estates… down the
> road, people can invite each other to view and edit each other's households."*

The constraint every step must keep true:

> *"no one should be able to see each other's estates without the owner inviting someone to
> see that estate and interact with it."*

## Why this is not the model today

An estate is currently a **deployment**: one Worker, one KV namespace, one Pages origin, one
`ESTATE_ID` binding. Isolation is real, but it is achieved by separation of *hardware* rather
than by the code. Measured 2026-09-10:

| | count |
|---|---|
| `scopeOf(env)` — estate read from the DEPLOYMENT | **60** |
| `scopeFor(request, env, grant)` — estate read from the CALLER'S GRANT | **1**, and the result is discarded (`eslint-disable-line no-unused-vars`, worker.js:3788) |
| `keyFor(scope, …)` call sites | 35 |
| `env.OBSERVATIONS` references | 91 |

⭐ **The primitive already exists and is already correct.** `scopeFor()` returns the grant's
estate when there is one and falls back to the deployment when there is not. It was written
and never adopted. This build is adoption, not invention.

⭐⭐ **Storage needs nothing.** C5 6a already made every key `<estateId>:<kind>:<suffix>`, so
one namespace can hold many estates safely — the prefix IS the isolation. That single earlier
decision is what makes this a focused build instead of a rewrite.

## What it dissolves

- **The Nigel/Aida blocker.** Cloudflare merged Pages into Workers and now refuses
  `pages project create myhome-nigel` because a Worker owns that name. Under this model no
  household needs a Pages project, a Worker, a KV namespace or an env block at all.
- **The condo migration.** Grant Park Condo was moved to `est-d93508` on 2026-09-10 because it
  shared `est-e6696a` with Mom and member reads had just been widened. Under this model it
  comes back to production as a row and the separate deployment retires.
- **The hostname derivation** in `onboarding/index.html`, which exists only because each
  household has its own origin.

## The four changes

### 1. A credential must find its estate — the chicken-and-egg
`grantFor()` reads `keyFor(scopeOf(env), "grant", sha256(token))`. To find a grant you must
already know its estate; with many estates per deployment, you do not.

⛔ **Do NOT solve this by dropping the estate prefix from grant keys** — that undoes C5 6a and
puts credentials in a flat space shared across estates.

✅ **Add a router row**, deployment-scoped because it is not estate data:

    credential:<sha256(token)>  →  { estateId }

`grantFor()` becomes: read the router → read `<estateId>:grant:<hash>` → verify the row's own
`estateId` agrees with the router → return `{row, scope}`. Two reads, both O(1). A router row
with no grant behind it is a **404, never a fallback to the deployment's estate**.

⚠️ **Backfill first.** Every existing grant needs its router row written BEFORE this ships or
every live credential dies at once — including Mom's and Bob's. `tools/grant-mint.py` writes
both from then on.

### 2. `POST /api/estate` — the thing the token actually buys
An authenticated caller creates an estate: mint `est-<6hex>`, write their grant row
(`relationship: ["owner"]`, `capability: "member"` — anyone may sign up as a member, owners and
administrators are minted) plus its router row, and return the estateId. ⛔ It must refuse to
name an estate after a person: an estate name never reaches a user-facing surface.

### 3. The 60 call sites
`scopeOf(env)` → `scopeFor(request, env, grant)`. ⚠️ **Not mechanical.** Some sites legitimately
mean the DEPLOYMENT — `/health`, `env-canary`, the digest guard, the chat budget ceiling. Each
one is a decision, deployment-scoped or caller-scoped, and the wrong answer either leaks across
estates or breaks a per-deployment control. Reviewable batches, not one sweep.

### 4. `hostAgrees()` and `FAMILY_HOSTS`
Both assume one household per origin. With one origin for everyone the host check stops
carrying tenancy and becomes an ordinary CSRF-shaped control.

## Down the road, and NOT in this build
People invite each other to view and edit a household. The grant row already has the shape for
it — `relationship` is a SET and `capability` is separate — so this becomes "mint a second
grant at my estate for someone else", not a new model. It is out of scope here and named so
that step 3 does not accidentally foreclose it.

## The falsifier

> Two accounts on one deployment, each having created their own estate, where every read one
> makes for the other's estateId returns 404 — and a grant presented for estate A cannot name
> estate B by any route.

Until that test exists and passes, deployment separation is the only thing holding the
2026-09-10 rule up, and it must not be dismantled.

## Sequence

1. Router row + `grantFor()` + **backfill** + `grant-mint.py` writes both. Nothing else changes;
   every estate still has its own deployment, so this is provable in isolation.
2. The falsifier test, written against two estates in ONE deployment (lab).
3. The 60 call sites, classified deployment vs. caller, in reviewable batches.
4. `POST /api/estate` and the `/homes/` picker.
5. Migrate: Grant Park Condo back to production; Bob off `myhome-bob`; retire the per-household
   envs. Nigel and Aida never get one.

⛔ **Step 5 is the only irreversible step and it is Paul's call, not a consequence of 1–4.**

## ⚠️ Timing, recorded 2026-09-10

Paul sent Mom's and Bob's invites the same afternoon this plan was written. **Step 1 touches
the credential path — the single thing that must not fail while two first-time users are
walking through the door.** A bug there does not degrade the app; it locks both of them out,
and Mom has already met one dead end this week. Do step 1 behind them, not across them.
