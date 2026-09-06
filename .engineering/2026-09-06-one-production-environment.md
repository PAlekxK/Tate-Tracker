# PATH-EVAL — one production environment, many households, shared households

- seat: engineering-partner
- date: 2026-09-06 (evening; supersedes decision 2 of `.engineering/2026-09-06-path-estate-read-and-tenancy.md`)
- inputs re-derived from source, not from the earlier note: `worker/worker.js` @ working tree (3,892 lines),
  `worker/wrangler.toml`, `estate/index.html`, `homes/index.html`, `onboarding/index.html`,
  `tools/{grant-mint,household-export,pages-deploy}.py`
- code_context_confidence: **high** — every load-bearing claim below was re-read from source this session
- user_context_confidence: **medium** — Bob's succession requirement and the new "shared households"
  requirement are both stated second-hand; no `.user-research/` artifact exists for either

---

## 0 · MY RECOMMENDATION MOVED. HERE IS EXACTLY WHY, SO IT CAN BE AUDITED.

This morning I recommended **A now, B next** — deployment-per-household first, per-request scope later.
Paul built A. He is now asking for one production environment.

**My recommendation has changed to: build the one production environment. But not for the reason in
his sentence.**

"Would it not be just one production deployment that we all exist in" is, on its own, **not a
sufficient argument**, and I want that on the record before agreeing with the conclusion. At n=3
households with n≤10 in view, N Cloudflare projects is a perfectly respectable architecture, and it
buys the strongest isolation guarantee available — one that needs no test to be true. If the
requirement were still *"N households, each with one owner, none of whom ever share anything,"* I
would hold this morning's recommendation and tell Paul his instinct was aesthetic rather than
structural.

**The thing that changed my answer is the clause he added second:** *"especially if we're gonna have
shared households between users."*

That is a different product. And it is the one requirement deployment-per-household cannot express at
any n, including n=2. **A did not become wrong. The requirement moved outside A's reach.**

⭐ **The distinction matters for how Paul reads the rest of this document.** Everything below is
downstream of a requirement change, not of a re-analysis. If shared households were withdrawn
tomorrow, my answer would revert to A. That is the honest shape of the advice.

---

# 1 · IS ONE PRODUCTION ENVIRONMENT RIGHT — AND WHAT COSTS CAN HE NOT SEE?

## 1a · The steelman for deployment-per-household, honestly

It deserves better than a dismissal, because four of these are genuinely strong:

1. **Isolation is by construction, not by correctness.** `est-9a74df` and `est-e6696a` live in KV
   namespaces `22250ace…` and `79464451…`. A Worker reads exactly one binding. There is no bug in
   `worker.js` — none, of any kind — that can make Bob's Worker read Mom's key. That is a guarantee no
   amount of testing buys you in a shared namespace.
2. **The escape hatch survives.** "Delete the namespace" is still true, per household, forever.
   `household-export.py`'s own docstring names the moment it dies: *"the first write by a SECOND
   household."*
3. **Blast radius of a bad deploy is one household.** Under one environment, one bad push is everyone.
4. **N is small and the ops is already scripted.** `pages-deploy.py` and `grant-mint.py` both read
   `wrangler.toml` and take `--env`. Adding a household is a config block and two commands.
5. **The measured cost of A is STALENESS, which is visible and recoverable.** `home` sat 26 commits
   behind. That is a bad day, not a bad outcome. B's failure mode is a cross-household read, which is
   silent and unrecoverable once written.

**If the answer is "it depends," here is the exactly one thing it depends on:**

> **Does a PERSON exist independently of a household?**
>
> If no — every person belongs to exactly one place, forever — deployment-per-household wins, and it
> is not close.
> If yes — a person can hold two places, or two people can hold one place — then a person is an entity
> that spans deployments, and N silos cannot represent an entity that spans them. One environment
> wins, and that is also not close.

Paul just answered yes. So the question is settled, and it was settled by a product decision, not an
engineering one.

## 1b · Why A is fatal — not awkward — under shared households

The coordinator asked me to say plainly which. **Fatal.** Three mechanisms, all verified in source:

1. **There is no person under A.** `personId` is minted inside `handleAccountCreate` and written to
   `keyFor(scope,"grant",…)` and `accountKey(scope,username)` — both inside one namespace. Bob-at-
   house-1 and Bob-at-house-2 would be two unrelated `p-…` ids with two password hashes that can
   drift apart. "Bob" would not be a thing the system has a name for.
2. **You cannot invite someone into your house.** An invite is a grant minted in *your* namespace for
   a person who does not exist there. Under A there is nothing to invite — only a fresh stranger who
   happens to share a name.
3. **The shelf cannot be durable.** `homes/index.html:207` already says it in its own comment —
   *"resolves to exactly one estate today; there is no person→estates index."* The only way to build
   a shelf under A is a client-side list of `(origin, token)` pairs in `localStorage`. ⛔ **That
   re-commits, at the level of the person, the exact bug Paul fixed this week at the level of the
   place** — the `/api/profile` grant-row write exists because *"copy that a clear-your-browser
   falsifies is a broken promise."* A device-local shelf is that promise broken one layer up.

And `.plans/2026-09-04-roles-and-access-REQUIREMENT.md` already closed the obvious workaround: Paul
ruled out a cross-silo person index as *"a second derivation that could disagree with"* the grant
rows. He was right, and that ruling is what leaves A with no move.

## 1c · The five costs of one production environment that are NOT obvious

These are the ones I would want on the board before he commits, because none of them is in his
sentence and each one is real.

**① The front end has a tenancy problem the Worker does not, and it is bigger.**
`pages-deploy.py:49` — `HOUSEHOLD = {"bob","paul"}` ships an 8-file allow-list. `home` (Mom's) does
**not**: it ships every tracked file, including `viewer.html` — 2 MB carrying "282 Church Mountain
Road," every plant, and the 1989 Bronco. One production environment means **one origin serving every
household**, so either every household can fetch `/viewer.html` and read Fernwood, or Mom's new home
is the neutral 8-file shell and the legacy Fernwood viewer stays at its own address.

⭐ **The good news, and it is genuinely good: the neutral shell already exists and is already
estate-neutral by construction** — onboarding · estate · homes · settings/place · settings/account,
verified by `check-estate-neutral.py`, 311 needles. **So one production environment is achievable for
the NEW product without touching `viewer.html` at all.** That is the single most important scoping
fact in this document.

⛔ **But it is a product decision, not an engineering one, and it has to be made out loud:** *Mom's
production home is the neutral shell; the legacy Fernwood viewer is not part of the merge.* That is
consistent with the 9/05 ruling that the frozen GitHub-Pages Fernwood is "the legacy version" — but
nobody has said the sentence about `fernwood-home` yet.

**② The chat budget and the weather station stop being deployment facts.**
`dateKey(scopeOf(env),"chat-budget",…)` at `worker.js:2125` and `:3149` is **per-deployment**. Under
one environment, `CHAT_DAILY_BUDGET_USD` becomes a single pot every household draws from — so one
household's Guru use, or one runaway loop, takes Guru down for everyone. It must become per-estate,
and its ceiling probably becomes per-estate data too.
Same shape, different risk class: `AMBIENT_MAC` is a **Worker secret** — one station per deployment.
Under one environment the station is per-*estate* data, and a per-estate third-party credential would
have to live in KV. ⚠️ That is a real change in the shape of the secret store and it should not happen
by accident. Today no other household has a station; keep it out of scope, but **do not let a
per-estate credential land in KV without a decision.**

**③ Usernames become globally unique.** `accountKey` must go global (§3b). "bob" is claimed by
whoever gets there first. At n≤10 that is fine and the 409 already exists — but it is a user-visible
consequence of an invisible change, and Paul should know it before Bob hits it.

**④ The "delete the namespace" hatch dies on the first merge write, by design.** Under A that hatch
was still live. Under one environment it is gone from day one. ⛔ **This promotes
`household-export.py`'s missing restore round-trip from "an afternoon, Paul's call" to a
prerequisite.** An export you have never put back is a forensic artifact, not a backup, and it is now
the only recovery path there is.

**⑤ G3 is already broken and one environment makes it more dangerous.** `wrangler.toml`'s own comment
records it: dev, qa and production all bind `est-3c9f1a`, so `grant-mint.estate_agrees()` can never
fire, and a credential minted with the wrong `--env` lands in production as a working credential. That
is a nuisance today. Under one production environment, "production" holds everybody. **The guard has
to be rebuilt around which NAMESPACE is written, not which estate was named** — and that is
pre-merge work, not post.

## 1d · Path D, named so it is not rediscovered later: Durable Objects

The platform has a primitive that gives per-household isolation by construction *inside* one
deployment: one Durable Object per estate, addressed by `idFromName(estateId)`, each with its own
storage. It is the architecturally cleanest answer to "how do I make cross-household reads
structurally impossible in a shared deployment."

**Recommend against it now**, and the reasons are practical rather than architectural: it rewrites
every KV call site with different consistency and pricing semantics, it is a new primitive to learn
under a live-user deadline, and the identity keyspace has to sit outside it anyway (a login has no DO
to route to yet). ⭐ **But it is the right answer if this ever becomes a product with real tenants**,
and the migration from "one prefixed keyspace per estate" to "one DO per estate" is much easier than
from an unprefixed one — which C5's estate-prefixing has already bought.

---

# 2 · THE IDENTITY MODEL — and the chicken-and-egg is not a lookup problem

## 2a · ⛔ CRITIQUE OF THE GLOBAL POINTER: don't build it

Paul's sketch: `grant:<hash> → estateId`, written at mint, read first, then the estate-scoped row.
He named its three defects himself and was right about all three. But the deeper objection is that
**it solves the wrong problem.**

> The chicken-and-egg is not a missing index. It is a **modelling error that C5 baked in**: the grant
> row was put in the estate's keyspace because, at the time, a grant *was* estate data. Under shared
> households it is not. **A grant is an edge between a person and an estate.** An edge keyed by the
> credential does not belong inside one of its endpoints' silos.

Move the row; do not index it. That removes the second writer, the disagreement failure mode and the
dual-write, because there is only ever one row for one fact.

⭐ **And Paul's "enumerable global keyspace" worry is smaller than he thinks — worth understanding
rather than working around.** `list()` requires the KV binding (the Worker, or wrangler with account
credentials); it returns key *names*; and the name is `sha256` of a 43-char, 256-bit random token.
Enumerating it yields hashes, and a hash is not a credential. **The real cost of leaving the estate
prefix is not enumeration — it is that you lose "one household = one key prefix,"** which is what
makes `household-export.py` and any future per-household delete tractable. So: **estate DATA keeps
the prefix; only IDENTITY leaves it.** Identity is deliberately the thing that spans households — that
is the entire requirement.

## 2b · The minimum honest data model

Three entities, three keyspaces. This is the smallest thing that can express "shared households"
truthfully; anything smaller re-merges two facts that have come apart.

| entity | key | holds | scope |
|---|---|---|---|
| **PERSON** | `account:<username>` → `{personId, salt, hash, iterations, email, phone, contactPref, profileAccent}` | who you are, how you sign in | **global** |
| **MEMBERSHIP** | `membership:<personId>:<estateId>` → `{relationship[], capability, entry, vault, issuedAt, issuedBy, consent[], revokedAt}` | what you may do **here** | **global, prefix-listable per person** |
| **SESSION** | `session:<sha256(token)>` → `{personId, estateId, issuedAt, expiresAt}` | which place this request is in | **global** |
| **ESTATE DATA** | `est-XXXX:<kind>:<suffix>` | everything else — unchanged | **prefixed, exactly as today** |

**Why each boundary is where it is:**

- **`account:` must be global or login cannot route.** This is the harder half of the chicken-and-egg
  and it is not in Paul's brief. `handleSession` (`worker.js:558`) reads
  `accountKey(scope, username)` — so a person typing a username and a word supplies **no estate hint
  at all**, and unlike a token you cannot prefix a thing a human types. ⭐ **The grant lookup has
  three possible fixes; the login lookup has one.** Global accounts is not a preference, it is forced.
- **`membership:<personId>:<estateId>`** puts the person first so `list(prefix="membership:p-abc:")`
  **is the shelf, by construction** — no second index, no derived roster, nothing that can disagree.
  This is the thing Paul ruled out under A, and it is fine here because it is the *same* row the
  authorization check reads, not a copy of it.
- **The session is a pointer, not an authority.** Today the grant token is identity, session and
  authorization fused into one object. Under sharing those three come apart, and fusing them is what
  makes revocation impossible (§2d).

**What this does NOT need, and should not have:**
- ⛔ No `person:<personId>` row. `account:<username>` already is it. A second row means a rename has
  two writers.
- ⛔ No `est-XXXX:members` roster. "Who is in this house" is a `list(prefix="membership:")` + filter
  at n≤50 people. **Do not build the reverse index until a screen actually needs it** — and when one
  does, derive it at read time, never store it.
- ⛔ No capability on the scope object. **A scope answers WHERE a key lives. A membership answers WHAT
  you may do.** Merging them is how a scope check silently becomes an authorization check.

## 2c · The one bug this model makes possible, which nothing in the brief catches

⛔ **Authorized-for-SOME-estate leaking into authorized-for-THIS-estate.**

Under sharing, the natural-feeling check is *"is this person a member anywhere?"* — a
`list(prefix="membership:<personId>:")` and a non-empty result. That is wrong and it will pass every
test in the brief, because in a two-person / two-estate fixture every person is a member of exactly
one place, so "somewhere" and "here" are the same answer.

**The rule:** the request's estate comes from **the session**, and the authorization check is a
**direct GET of `membership:<session.personId>:<session.estateId>`**. Never a listing, never a
membership found by search.

⭐ **Which generalises into a principle worth keeping:**

> **Listings drive views; direct GETs drive decisions.**

This is not abstract here. `household-export.py` measured it on 2026-09-05: `kv key list` is
eventually consistent and omitted a key a direct GET found. **A listing cannot prove presence and
cannot prove absence** — which is tolerable for rendering a shelf and disqualifying for deciding
whether someone may read a house.

## 2d · Revocation — and why it argues for a short derived scope

The coordinator asked when the next request stops working. **The answer must be: the very next one.**
Not at session expiry, not after a redeploy. Paul removing someone from a household is a *social* act
— a falling-out, a sale, an heir — and *"it takes up to 24 hours"* is a sentence he should never have
to say to a neighbour.

**That is achievable and cheap, and it falls straight out of the model:**
- Revoke = one write: set `revokedAt` on `membership:<p>:<e>`.
- Every authenticated request already does 2–4 KV reads. Adding one direct GET of the membership row
  is a few milliseconds and is the read the request needed anyway to know the capability.
- Sessions are not swept on revoke and do not need to be — a session with no live membership resolves
  to nothing.

**So: long session, no cached authority.** Today `grant-mint.py`'s own docstring says *"No exp, no
TTL"* — under sharing, add a sliding TTL via KV's native `expirationTtl` (deterministic, free, no
sweeper to forget). ⚠️ **But keep it long.** Mom's constraint is low-friction auth in a field journal;
a 30-day forced logout would be a self-inflicted adoption wound. The security comes from revocation
being instant, not from the session being short.

## 2e · ⭐ THE ORDERING ANSWER: scope conversion FIRST, and it is not wasted work

The coordinator's fear — converting 30 sites twice — is real in general and **does not apply here**,
for one specific structural reason:

> `scopeFor(request, env, grant)` is a **seam with exactly one producer and N consumers.** The 30
> consumers take `requestScope` regardless of what resolves it. Replacing the identity model changes
> the *producer* and touches no consumer.

So the sites are converted once, whichever order you build in. But the *order still matters*, because
of a safety asymmetry:

- Converting consumers while the producer still yields the deployment binding is **inert** — provably,
  from source: `grantFor` rejects `row.estateId !== env.ESTATE_ID`, so `scopeFor` returns
  `scopeOf(env)` for every real request today. Safe this week, beside a live onboarding.
- Flipping the producer while **one** consumer is unconverted is a silent cross-household write, and
  `assertScope` will not fire (§3).

**Therefore: consumers first, producer last, always.** The identity *design* must be settled on paper
first (it decides whether `requestScope` carries capability — it must not), but the identity *build*
comes after the conversion.

---

# 3 · ⛔ HARDENING — the part Paul most wanted challenged, and the part I most want him to read

The premise is correct and worth restating in its sharpest form: **under one deployment, a scope bug
is a cross-household disclosure rather than a 404.** Testing does not get you there. Structure does.
Five layers, ordered by how much they buy per line of code.

## Layer 1 ⭐ — THE ATTENUATED KV HANDLE. Make the wrong key unaddressable.

**This is the single highest-value change in this document and it is roughly 40 lines.**

Today every handler holds `env.OBSERVATIONS` — the whole namespace, every household — and correctness
depends on each of ~30 call sites having been converted right. Instead, hand the handler a
**prefix-bound store**:

```
const store = estateStore(requestScope, env.OBSERVATIONS);
// store.get/put/delete/list build and VERIFY the `<estateId>:` prefix at the boundary.
// A key that does not start with requestScope.id + ":" throws before it reaches KV.
```

Handlers receive `store`, never the raw namespace. Then **a handler cannot address another household
because the only handle it holds cannot name one.** Correctness moves from "all 30 conversions were
right" to "one wrapper is right," and the second is a thing you can actually read in one sitting.

Pair it with a deterministic grep check — `env.OBSERVATIONS` may appear only inside the wrapper and at
the named deployment-scoped sites — and **wire it into `pages-deploy.py` / `deploy-worker.sh` the way
`check-estate-neutral.py` is already wired**, per this repo's own rule: *a check wired into the thing
it guards cannot be forgotten; a check listed in a document can.*

*Why this shape is right, briefly:* it is the object-capability idea — hand out the least authority
that does the job, as a reference rather than as a rule. It is also, not coincidentally, what a
Durable Object gives you for free (§1d), which is a good sign you are on the grain of the platform.

## Layer 2 ⭐ — TYPE-SPLIT THE SCOPE. This is the direct answer to "assertScope catches FORGOTTEN, not WRONG."

Paul's finding stands and is the reason the identity doors go last. But it is **fixable**, and the fix
is small:

- `scopeOf(env)` returns `{type:"estate", source:"deploy"}` — indistinguishable from a request scope.
  That is precisely why a forgotten site passes `assertScope`.
- **Delete `scopeOf(env)` entirely** at the end of the conversion. Replace it with
  `deploymentScope(env)` returning `{type:"deployment", …}`, used by the ~13 legitimately
  deployment-scoped sites (rate limits, weather/AirNow/drought/today-line caches, `searchLibrary`,
  `listBothEras`).
- `keyFor` / `dateKey` / `blobKey` — the household-data builders — **assert `scope.type === "estate"`
  and throw on a deployment scope.** Deployment keys go through a separate `deploymentKey()`.

**Result: a site that keeps taking the household from config no longer produces a valid key. It
throws.** `assertScope` starts catching WRONG, not just FORGOTTEN — because the two scopes are no
longer the same shape, and the difference is enforced where the key is built.

⚠️ **One migration snag, worth knowing before you start:** three of those sites are `library` keys
(`worker.js:153/157/162`), and the prose library index is *loaded into KV by a tool*
(`build-library-index.py`). Changing that prefix means changing the loader too, or the index goes dark
on the next deploy. Rate-limit and cache prefixes are ephemeral and can change freely.

⭐ **And there is a bonus nobody has priced:** after the split, the grep inventory of `scopeOf(env)`
goes to **zero**, and any future `scopeOf(env)` is a compile-time-ish failure rather than an item on a
roster somebody has to keep re-counting. **The roster stops being a document and becomes a property of
the code.** Measured today: 50 real call sites, ~40 of them keyed by `keyFor`/`dateKey`/`blobKey`.
That inventory is exactly the kind of hand-maintained count this repo has repeatedly watched drift.

## Layer 3 — THE PAYLOAD CARRIES THE ESTATE TOO, and reads check it.

`attributeTo` already stamps `estateId` on feedback rows. Generalise it in the Layer-1 wrapper: on
`put`, stamp `estateId` into the JSON value; on `get`, if `value.estateId` exists and disagrees with
the scope, **throw and log** rather than return.

Cost: one field. What it buys: a key-shape bug and a data-migration bug both surface as an error
instead of a disclosure. This is literally `[[Match the PAYLOAD, not the container]]` from Paul's own
memory index — the container says whose it is, and now so does the payload, and disagreement is
detectable.

## Layer 4 — THE IDENTITY KEYSPACE'S OWN FAILURE MODES

Named so they are designed rather than discovered:

- **A session pointing at an estate the person is no longer in** → resolves to nothing, because the
  membership GET is what authorizes (§2d). This is a *feature* of the split, not a hazard.
- **A membership row that exists with no account row** (account deleted, membership orphaned) →
  must fail closed. `handleSession`'s existing fallback is instructive: it used to hardcode
  `"administrator"`, which turned a lost row into a privilege escalation. That was caught. **The same
  class of default must not be reintroduced anywhere in the new model.** Every missing-row branch
  fails to *less*, never to more.
- **Username rename** — `handleUsernameChange` already does new-key-first / old-key-second for
  exactly the right reason. Under global accounts the race window widens (more contenders) but the
  ordering rule is unchanged and still correct.
- ⚠️ **`hostAgrees` quietly stops being a tenancy control.** Today `FAMILY_HOSTS` is one host per
  deployment, so a household's origin and its data happened to coincide. Under one environment every
  household shares one origin, so the host check discriminates origins and **not households at all**.
  It was never *designed* to be a tenancy control — but it currently reads as a second line of
  defence, and after the merge it is not one. **Do not count it in the layer stack.** (It also
  returns `true` when `Origin` is absent, which any non-browser client can arrange.)

## Layer 5 — THE CHECKS ARE WIRED, NOT LISTED

Everything above is worth less than half if it lives in `CLAUDE.md`. Per this repo's own
fourth-instance finding: the scope-site grep, the isolation suite and the sharing suite each get a
caller — the deploy script for the greps, the session-start block **and** a pre-merge gate for the
tests.

---

# 4 · THE FALSIFIER — Paul's test is necessary and is roughly a third of the job

His test: **two grants · two estates · one namespace · one deployment; write under each; prove neither
read sees the other; assert on RAW KV KEYS.** That is right, and the raw-key assertion is the part
most people get wrong — an API-response test passes just as happily when both households' rows sit in
one key and the handler filters at read time, which is a completely different and far weaker
guarantee.

**What it misses — and the second one is the interesting finding:**

### ⭐ T2 · The SHARING test, which is the isolation test's negative control

One estate `E`, two members `P1` and `P2`, one outsider `P3`. Assert: both members' writes land in
**one** key (`E:feedback:<date>`), both members read **both** rows, and `P3` gets a 404.

> **T1 and T2 are each other's negative control, and neither alone is meaningful.** T1 alone passes
> if the implementation accidentally keys by *person* instead of *estate* — which is a plausible bug
> and the exact opposite failure. T2 alone passes if there is no isolation at all. Isolation and
> sharing are two claims and they need two tests.

### T3 · The multi-estate person — the sneakiest bug in the design

`P1` is a member of `E1` and `E2`. Sign in, choose `E1`, then attempt to read `E2:feedback:<date>`.
Must 404 — the scope comes from the **session's** estate, not from "any estate this person can reach."
This is the §2c bug and **no fixture with one-person-one-estate can catch it.**

### T4 · Revocation

Revoke `membership:P2:E`. Assert the **same token** that worked one second earlier now 404s, with no
redeploy, no logout, no cache flush.

### The assertion shape, tightened

- Assert on raw KV keys, as Paul says. **Also assert on the VALUE's `estateId`** (Layer 3).
- ⭐ **Assert the full set of keys created, not just that the expected ones exist.** A run should
  produce exactly the whitelist; a stray write under a third prefix must fail the test. "The two I
  expected are there" passes over a third one nobody looked for.
- ⚠️ Use direct GETs for assertions. `kv key list` is eventually consistent — measured in this repo on
  2026-09-05 — so a listing-based test can go green over a real miss, or red over nothing.

### ⭐ THE MUTATIONS — one per claim, because a suite with one mutation control proves one thing

| # | mutation | must turn RED |
|---|---|---|
| M1 | revert one converted handler to the deployment scope | T1 (isolation) |
| M2 | key a household record by `personId` instead of `estateId` | T2 (sharing) |
| M3 | authorize by `list(prefix="membership:<p>:")` non-empty | T3 (multi-estate) |
| M4 | cache `capability` on the session and skip the membership GET | T4 (revocation) |

**Write all four RED before the change that makes them green** — a test written afterwards can only
confirm what you built. And run them in `lab` (its own namespace, `est-lab0001`, no real person),
which needs **a second lab estate minted** for T1 and T3.

---

# 5 · SEQUENCING AGAINST LIVE PEOPLE — the honest answer, which is not "both wait"

**First, the thing that should lower the temperature: nothing here is a leak today.** `myhome-bob` and
`myhome-paul` are isolated by construction. There is no emergency. There is a design decision and an
ordering, and the ordering has real slack in it.

## 5a · Bob goes this week, on `myhome-bob`, as built. ⭐ Recommendation.

The reasoning is a cost comparison, not a preference:

- **A is safe today; the merged model is not built.** Rushing the identity split beside a live
  onboarding is the one thing I would refuse outright.
- **The migration cost is small and bounded, and C5 already paid the hard part.** Bob's data keys are
  already `est-9a74df:<kind>:<suffix>` — **globally unique, and unchanged by the merge.** Migrating
  him is: copy his `est-9a74df:*` keys into production's namespace *byte-for-byte*, promote his
  account row to `account:<username>`, write one `membership:<p>:est-9a74df`, mint a session, send a
  new link. His password survives. His data does not change shape at all.
- **The user-visible cost is one changed link**, on a dataset days old, to a neighbour who will shrug
  at *"we moved you to the real address."*

⚠️ **Two conditions on that, and they are conditions, not suggestions:**
1. **Prove the export/restore round-trip on `lab` before Bob's link goes out** — export → delete one
   key → restore → byte-identical. Not because Bob is at risk today, but because his migration is now
   scheduled work and the tool that performs it has never been run backwards.
2. **The `estate/index.html` feedback handler bug from this morning's note (§1d there) still ships on
   the screen Bob meets** — on a non-2xx the textarea is cleared and he is told the note was saved on
   the device, and nothing is saved. Fix (i), two lines, before the link.

## 5b · Mom waits for the merged model. ⭐ And the reason is not safety.

**The rule I would hold to:**

> **Onboard the person you can afford to move. Hold the person you cannot.**

Bob is a neighbour; a second link is a shrug. Mom is the make-or-break adoption case whose documented
fear is *getting things wrong*, and whose behaviour this week shows she takes every affordance that
moves her and zero that ask her for something. **Onboarding her twice would spend exactly the trust
the whole loop is built on**, and it would do it to save a couple of weeks.

She is also gate 3 of the release cascade and has not been invited, so nothing is slipping. This costs
schedule and nothing else.

## 5c · What can land *this week*, safely, beside Bob's link

All of it is inert by construction and none of it touches a live path:

1. **The consumer conversion** — ~30 sites onto `requestScope`, readers first, capture paths ascending
   by what they hold, `handleFeedback` last, identity doors not at all. Provably inert while
   `grantFor` still rejects a foreign estate.
2. **The Layer-1 wrapper and the Layer-2 type split** — pure refactors, no behaviour change, and they
   are what makes step 6 safe rather than merely tested.
3. **T1–T4 written RED**, with M1–M4.
4. **The `household-export.py` restore round-trip.**
5. **The G3 rebuild** (namespace-based, not estate-based) — a live defect today, independent of all of
   the above.

Then, and only then, the producer flip and the identity split — in `lab`, then `qa` with two estates,
then production.

---

# 6 · WHERE I AM RULING vs. WHERE IT IS PAUL'S

**Ruling (engineering — take these unless the reasoning is wrong):**
- **One production environment, because of shared households.** Deployment-per-household is fatal to
  that requirement, not awkward. ⚠️ If shared households is withdrawn, this ruling reverts.
- ⛔ **Do not build the global grant pointer.** Move the row, do not index it. The chicken-and-egg is a
  modelling error, not a missing lookup — and the *login* lookup, which the brief does not mention,
  forces global accounts anyway.
- **Person / membership / session are three things.** Estate data keeps its prefix; identity leaves it.
- **Authorize by a direct GET of `membership:<personId>:<estateId>` from the SESSION's estate.** Never
  by a listing, never by "member somewhere." Revocation takes effect on the next request.
- **A scope answers WHERE; a membership answers WHAT.** Do not put capability on the scope object.
- **Consumers before producer, always.** The 30 sites are converted once regardless of order, so there
  is no double-work argument for waiting — and flipping the producer early is the silent-leak case.
- **Layer 1 (attenuated KV handle) + Layer 2 (type-split scope) are the hardening.** They convert
  "every call site was right" into "one wrapper is right, and the wrong scope will not build a key."
  This is the answer to *assertScope catches FORGOTTEN, not WRONG*.
- **Four tests, four mutations, written RED, asserting on raw keys AND payload AND the full key set.**
  T1 and T2 are each other's negative control.
- **Bob this week on `myhome-bob`; Mom waits for the merge.**
- **The restore round-trip is now a prerequisite, not an afternoon** — the namespace hatch dies by
  design in this architecture.

**Paul's call:**
1. ⭐ **Is Mom's production home the neutral 8-file shell, with the legacy Fernwood viewer staying
   where it is?** One origin cannot serve both without re-shipping the tenancy leak. This is the
   biggest unmade decision in the merge and it is a product one.
2. **Global usernames** — first-come-first-served across all households. Fine at n≤10; user-visible.
3. **Whether the chat budget becomes per-estate data** (it must become per-estate *something*; whether
   the ceiling is configuration or a per-household setting is his).
4. **Whether Bob's second house lands before or after the merge.** I would say after, and now it is
   cheap either way — under this model it is one more membership row.
5. **Whether a founding owner's `administrator` capability, which lets Bob read his daughters' notes,
   is intended.** Still live, still undocumented, and under shared households it stops being a
   Fernwood-family question and becomes a product one.

---

## Principles to propose (NOT added — awaiting Paul's confirmation)

1. **Listings drive views; direct GETs drive decisions.** — cross-project. An eventually-consistent
   listing cannot prove presence or absence, so it may render a screen and may never authorize a read.
2. **Hand out the narrowest handle, not the broadest handle plus a rule.** — cross-project. If a caller
   holds a store it cannot misaddress, correctness stops depending on every call site being right.
3. **A scope says WHERE; a permission says WHAT. Never one object.** — cross-project.
4. **Isolation and sharing are two claims and need two tests; each is the other's negative control.**
   — cross-project.
5. **Onboard the person you can afford to move; hold the person you cannot.** — fernwood.
6. **When a recommendation reverses, say which REQUIREMENT moved.** — cross-project. A reversal that
   reads as a re-analysis teaches the reader to discount the next recommendation.

*(Carried forward, still unconfirmed, from this morning's note: "a receipt reads state, never
re-derives from a log"; "an assertion that validates SHAPE cannot validate CORRECTNESS"; "convert
readers before writers, identity doors last"; "write the isolation test RED before the change".
⭐ Note that Layer 2 above **retires the second one for this specific case** — the type-split is how a
shape assertion is made to carry correctness. The general principle stands; this is the worked example
of escaping it.)*
