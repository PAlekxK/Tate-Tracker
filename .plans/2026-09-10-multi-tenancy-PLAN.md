# Multi-tenancy — an estate is a ROW, not a deployment

- row: `BACKLOG.md` TIER 1 · 46 (the account model) · 41 — the single-origin door, LAP 8 · A on `.plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md`
- objective: O3
- class: engine · must-not-diverge
- stage: retro
- seats: engineering-partner → `.plans/2026-09-11-lap8-build-PLAN.md` (its A2 audits this file and finds it stale in three of four changes — read that before this) · security-steward → owed (the existence oracle at `/api/account/available`; no redirect door) · ux-expert → owed (the shelf after sign-in) · content-steward → owed (every word on a door) · user-researcher → owed (multi-household person, cold device) · ai-advisor → waived: no model on any path
- ready: ⛔ NEVER STAMPED, and it no longer needs to be — SUPERSEDED, retired 2026-09-12 on Paul's word (attribution in `## Retro`, deliberately not a stamp token here: what he approved was the RETIREMENT, not the design, and a stamp on this line would read as the opposite). Changes 1–2 shipped before this header existed; 3–4 moved into `.plans/2026-09-11-lap8-build-PLAN.md` § ROW A. Nothing here is live work, so there is no design left for Paul to gate. See `## Retro`.
- stage-note: 2026-09-11 ~2:20 AM ET — header added by the backlog-refinement window on the coordinator's relay (the lap-8 build plan's P2 asks for exactly this). **Changes 1 and 2 are BUILT** (the router row + `grantFor()` + backfill; `POST /api/estate` — seven households founded through it at lab, `walk-founding.py`). **The `credential: → {estateId}` key in change 1 is SUPERSEDED by `route: → {personId}` plus the grant edge `grant:<personId>:<estateId>`** (M1+M2, ruled; OPEN-ITEMS ④·1 *"conforming to a ruling already made"*). Changes 3 (the call sites — a moving number; the lap-8 plan's A3 re-units it) and 4 are lap 8 · A. § *Down the road* is now lap 11's INVITE & JOIN. Body below untouched and predates this header.

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

### 1. A credential must find its estate — the chicken-and-egg  ✅ **BUILT**

> ⛔ **THE DESIGN BELOW IS SUPERSEDED.** The shipped shape is `route: → {personId}` plus the grant
> edge `grant:<personId>:<estateId>` (M1+M2, ruled), **not** the `credential: → {estateId}` row this
> section proposes. Kept for the reasoning, which still holds; do not build from it.
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

### 2. `POST /api/estate` — the thing the token actually buys  ✅ **BUILT**

> Seven households founded through it at `dev`, verified by `walk-founding.py`.
An authenticated caller creates an estate: mint `est-<6hex>`, write their grant row
(`relationship: ["owner"]`, `capability: "member"` — anyone may sign up as a member, owners and
administrators are minted) plus its router row, and return the estateId. ⛔ It must refuse to
name an estate after a person: an estate name never reaches a user-facing surface.

### 3. The 60 call sites  ⛔ **MOVED — lap 8 · ROW A (A2/A3)**

> ⚠️ **"60" is stale.** `measured 2026-09-12`: `scopeOf(env)` has **71** call sites and `scopeFor()`
> has **ONE live consuming call** (`worker.js:4877`) — the other occurrences are the definition,
> comments, and one `requestScope` computed and *deliberately* unused. A number in a plan ages.
`scopeOf(env)` → `scopeFor(request, env, grant)`. ⚠️ **Not mechanical.** Some sites legitimately
mean the DEPLOYMENT — `/health`, `env-canary`, the digest guard, the chat budget ceiling. Each
one is a decision, deployment-scoped or caller-scoped, and the wrong answer either leaks across
estates or breaks a per-deployment control. Reviewable batches, not one sweep.

### 4. `hostAgrees()` and `FAMILY_HOSTS`  ⛔ **MOVED — lap 8 · ROW A (A8)**
Both assume one household per origin. With one origin for everyone the host check stops
carrying tenancy and becomes an ordinary CSRF-shaped control.

## ⭐ HOW PAUL GETS IN, IN PRODUCTION `[paul-ruled 2026-09-10]`

> *"in production, I would expect Mom to have to go through the process of setting up an account,
> setting up an estate, and then inviting me to the estate to see it. We can decide later whether
> there's an administrative portal, but for now, that should be the way I access in production —
> other than, obviously, the back end, which we're working through together."*

⛔ **This CANCELS the obvious repair to the `p-paul @ est-e6696a` divergence.** `watch-accounts.py`
reports that row live in the register and absent from the store, so `grantFor()` 404s Paul at Mom's
estate today. **Minting it is the wrong fix** — a self-minted administrator grant at someone else's
household is precisely the back door this ruling closes. The register row is the thing that is
wrong, not the store.

⭐ **The grant model already has the shape for this, on the two ratified axes:**

| axis | Paul, in production |
|---|---|
| `capability` | `administrator` — a SYSTEM role: canon, admin, the backend |
| `relationship` | **NONE at an estate that has not invited him** — this is the half that grants access |

**He holds administrator of the application; he does not hold a relationship to Mom's household
until Mom grants him one.** The earlier reading — *"I'm an administrator on everyone's"* — is
consistent with this and is about capability, not about standing access to every household.

⚠️ **Consequences, and one of them moves scope:**

1. **`p-paul @ est-e6696a` is declared `relationship: ["owner"]` in the register. That is wrong** —
   Mom owns Fernwood. Correcting it is register work, not store work, and it is part of *"rights in
   good enough order"* before Nigel and Aida are invited.
2. ⭐ **"Invite someone to your estate" stops being purely down-the-road.** This plan defers it
   (§ *Down the road*) and that still holds for THIS build — but it is now **Paul's own production
   access path**, not just a future nicety. Step 3 must not foreclose it, which the plan already
   requires for a different reason.
3. **G2 firing at Mom's estate is CORRECT, not noise.** The administrator holds no relationship
   there — that is exactly G2's case, and the consent Mom gives is what covers it.
4. **Backend access is acknowledged and unchanged.** It is what the signup checkbox discloses
   (`[paul-ruled 2026-09-10]`: one line and a checkbox before account creation, that the
   administrator for the system can see your input). Product access and backend access are
   different claims and the model should keep them apart.

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

---

## Retro — 2026-09-12 · SPENT, and retired without a stamp `[paul-approved 2026-09-12: "Yes go ahead"]`

**What this plan was for:** making an estate a ROW rather than a deployment. All four of its changes are
now either shipped or relocated, so it tracks nothing.

| change | disposition |
|---|---|
| 1 · credential → estate | ✅ **built** — and its *design* superseded by `route:` + the grant edge |
| 2 · `POST /api/estate` | ✅ **built** — seven households founded at `dev` |
| 3 · the call sites | ⛔ **moved** → lap 8 · ROW A · A2/A3 |
| 4 · `hostAgrees()`/`FAMILY_HOSTS` | ⛔ **moved** → lap 8 · ROW A · A8 |

⭐ **Why it is retired rather than stamped, which was the actual open question.** Its `ready:` line read
*"agent-proposed — Paul rules; in flight without the gate"* while two of its changes had already shipped.
That is a trap in both directions: **stamp it and you retroactively bless shipped work; refuse and it sits
in-flight-without-a-gate forever.** The third door is that **there is no design left to gate** — so the
question dissolves instead of being answered.

⭐ **And the band was telling the truth the whole time.** `design` read **3/2**; the honest reading was
*2 legitimately in design + 1 spent spec*. A `wip-exception:` would have papered over a known-stale
specification to make a number go green — which is how a WIP band stops measuring anything. The design
window declined to re-stage it unilaterally and was right to: re-staging another lane's plan to relieve
pressure you yourself put on the band is the exact move that breaks the instrument.

⚠️ **The pre-registered question, answered:** *would a planner reading this file plan work already done?*
**Yes, and that was live for two days.** The 09-11 header said changes 1–2 were BUILT; the body still
presented all four as open and change 1 still proposed a superseded key shape. `.plans/2026-09-11-lap8-build-PLAN.md`
§A2 named it (*"a lane pointing at a stale specification is how a lane rebuilds a shipped thing"*) and §P2
specified this amendment. The header half landed 09-11; **the body half sat until today** — a correction
that reached the document it was written in and not the document it was about.
