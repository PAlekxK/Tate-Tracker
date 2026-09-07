# PATH-EVAL — the environment pipeline: what it should be, and the cheapest honest way there

- seat: engineering-partner · mode: path-evaluation
- date: 2026-09-06 (late evening) · companion to `.engineering/2026-09-06-one-production-environment.md`
  and `.plans/2026-09-06-one-environment-DECISIONS.md` (all seven sections read, §5–§7 included)
- **external research authorised by Paul for this one.** Sources are cited inline and graded at §1a.
- inputs verified from source or from the live deployments tonight, not re-derived from the notes:
  `worker/wrangler.toml`, `worker/worker.js` (`/health`, `legacyBefore`, `ENV_NAME` write sites),
  `tools/{deploy-worker.sh,pages-deploy.py,synthetic-identity.py,journey-walk.py,check-household-isolation.py,check-estate-neutral.py}`,
  and **live `/health` + live HTTP probes against all six Workers and all five Pages origins**
- code_context_confidence: **high** · user_context_confidence: **medium** (no `.user-research/`
  artifact exists for the outside readers now arriving; Bob and the Oculus reader are second-hand)

---

## 0 · FOUR THINGS I MEASURED TONIGHT. READ THESE FIRST — THEY CHANGE THE ANSWER.

Everything below is downstream of these. All four were read off the running system at ~22:50 UTC,
not inferred from the repo.

### ⛔ 0a · The production household origin is serving another household's data RIGHT NOW, and the control built to prevent it reads GREEN.

```
https://fernwood-home.pages.dev/CLAUDE.md                  200 · 93,070 bytes · "282 Church Mountain Road" ×2
https://fernwood-home.pages.dev/plants.json                200 · 314,203 bytes · 135 Fernwood/Church-Mountain lines
https://fernwood-home.pages.dev/onboarding/invite-message.md  200 · 3,562 bytes · the UNSENT invite draft
```

**Root cause, established deterministically rather than theorised:** the same URLs with a
cache-busting query string return the 252-byte shell. The bare URLs return
`cf-cache-status: HIT · age: 24263 · cache-control: public, s-maxage=604800`. The cache entries were
filled **before** the 18:37 pruning deploy and Cloudflare's edge holds them for **seven days**.

⭐ **So `pages-deploy.py`'s allow-list is correct and it worked.** `myhome-bob` and `myhome-paul`
return 252 bytes for both probes — the prune is right. What is wrong is the belief that removing a
file from a deployment un-serves it. **It does not.** The deployment's file set and the *edge's* file
set are two different things, and every check in this repo reads the first one.

⛔ **And `check-estate-neutral.py --url https://fernwood-home.pages.dev` prints
`✅ the arrival surface names no other household` — over 252 bytes.** It fetches the arrival path.
The 314 KB of Fernwood canon sits on the same origin, one path away, invisible to it. This is the
project's own named failure shape — *an instrument whose scope is typed rather than derived from what
declares reality* — occurring inside the instrument built to enforce estate neutrality.

**Severity, calibrated:** this repo is public, so nothing secret escaped. It is **important, not
critical** — until an invite link goes out, at which point it is the first thing a stranger's browser
can reach on the origin you sent them to, and it becomes critical. It self-heals ~2026-09-13. That is
after the timeline.

### ⛔ 0b · QA and production differ in the SECRET SET, not just in `LEGACY_BEFORE`. Nothing compares them.

Read from each deployment's own `/health`:

| env | estateId | legacyBefore | chat ceiling | airnow | ambient | anthropic | github |
|---|---|---|---|---|---|---|---|
| `fernwood` (frozen) | est-3c9f1a | **2026-09-04** | *(absent)* | ✅ | ✅ | ✅ | ✅ |
| `qa` | est-qa0001 | **2026-09-03** | 3 | ✅ | ✅ | **✅** | ❌ |
| `lab` | est-lab0001 | 1970-01-01 | 3 | ❌ | ❌ | ❌ | ❌ |
| **`home` (production)** | est-e6696a | 1970-01-01 | 10 | ❌ | ❌ | **❌** | ❌ |
| `bob` | est-9a74df | 1970-01-01 | 5 | ❌ | ❌ | ❌ | ❌ |
| `paul` | est-d93508 | 1970-01-01 | 5 | ❌ | ❌ | ❌ | ❌ |

⭐ **The `LEGACY_BEFORE` divergence the brief names is real and it is the SMALLER one.** Production
has **no Anthropic key**, so `/api/chat`, `/api/today-line`, `/api/classify` and the image path all
return 503 there (`worker.js:1177/1246/2010/2518`). QA has one. **Garden Guru cannot run on the new
product's production at all**, and production simultaneously declares a `$10.00` daily ceiling for it
— a budget for a capability that cannot execute. Not user-visible yet, because the eight-file
household shell calls only `/api/{account,session,profile,grant,feedback,onboarding-metrics}`. It
becomes visible the day Guru lands in that shell.

⚠️ `ambient: false` on `home` is probably correct-by-design — a new household has no weather station.
That is exactly why the parity instrument needs a *classification*, not a diff (§3).

### ⛔ 0c · QA is not a mirror on the FRONT END either, and this one is total.

`pages-deploy.py:66` — `HOUSEHOLD = {"bob","paul","home"}`. `qa` and `lab` are not in it, so they
ship `git archive <sha>` in full: **819 tracked files**. Production ships **8**. The synthetics walk
an origin with two orders of magnitude more surface than the origin a real person loads, including
`viewer.html`. A green QA walk carries no information about whether the pruned production origin can
serve the same journey. 0a is the proof that it does not.

### ⚠️ 0d · `/health` — the payload I am about to recommend as the parity oracle — carries a hand-typed roster that has already drifted.

Its `endpoints` array names 21 routes. Derived from `worker.js` itself, the router answers at least
eight more that the roster omits: `/api/account`, `/api/account/available`, `/api/account/username`,
`/api/session`, `/api/profile`, `/api/onboarding-metrics`, `/api/ambient`, `/api/remove-species`.

⭐ **That is the entire identity and onboarding surface — the surface the whole tenancy conversion is
about.** The oracle has to be fixed before it can be trusted (§3d).

---

# 1 · WHAT THE PIPELINE SHOULD BE

## 1a · What the research actually says — and how good the evidence is

**Grade A — primary, vendor-authoritative or canonical.**

- **[12factor.net/dev-prod-parity](https://12factor.net/dev-prod-parity)** — the canonical statement.
  It does *not* say "make staging identical to production." It names **three gaps to keep small**:
  the **time** gap (code deployed hours after writing), the **personnel** gap (whoever writes it
  deploys it), and the **tools** gap (same backing services everywhere). ⭐ **The third is the one
  this project is failing**, and it is failing it on *backing services* — the Anthropic key, the
  Ambient station, the file set — which is precisely what factor 10 is about. Paul is already
  perfect on the first two: he ships the day he writes, and he deploys his own code.
- **[Cloudflare — Wrangler environments](https://developers.cloudflare.com/workers/wrangler/environments/)**
  — an environment produces a distinct Worker named `<name>-<env>`; **bindings, vars, secrets and KV
  namespaces are non-inheritable and must be re-declared per environment**; the top level is the
  no-`--env` default. ⭐ *Non-inheritable is the platform telling you that parity is your job.* There
  is no mechanism that makes two environments agree. `wrangler.toml`'s own comment already knows
  this — "*a forgotten one makes the Worker throw*" — which is the right instinct applied to exactly
  one variable.
- **[Cloudflare — KV across environments](https://developers.cloudflare.com/kv/reference/environments/)**
  — same binding name, different namespace id per environment. This repo already does it correctly,
  six times, and `kv_canary` (read *from* the bound namespace, never re-typed) is a better mis-binding
  control than the docs suggest. That is a genuinely good piece of engineering and it should be said.
- **[Cloudflare — Workers best practices](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/)**
  — use **at least two environments** (staging + production) with separate routes and secrets;
  deploy from CI, not a laptop.
- **[Cloudflare — Preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/)**
  and **[per-branch preview deployments, 2025-07-23](https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/)**
  — versioned and aliased preview URLs; each git branch gets a stable preview URL. ⚠️ **The docs do
  not state that a preview version gets different bindings, and it does not: a preview of the
  production Worker reads production KV.** That is a real hazard and it is why I am not recommending
  them (§1c).
- **[Cloudflare Pages — preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/)**
  — the Pages equivalent. Note for this repo: `pages-deploy.py`'s `BRANCH` map names `lab`, `home`,
  `bob`, `paul` — **none of these are git branches** (only `main` and `staging` exist on the remote).
  They are deploy-time labels on a `git archive <sha>` export. That is fine and arguably better, but
  it means nobody should go looking for those branches.

**Grade C — practitioner consensus, mostly vendor content marketing. The argument carries; the source does not.**

- **Ephemeral preview environments vs. long-lived staging**
  ([Autonoma](https://getautonoma.com/blog/staging-environments-dead),
  [Signadot](https://www.signadot.com/articles/comprehensive-guide-to-preview-environments/)) — the
  modern claim is that shared staging fails because *multiple engineers contend for it*: stale state,
  coordination overhead, someone else's half-finished branch. ⭐ **Every stated reason is a
  multi-engineer reason.** The same sources concede that long-lived staging still earns its keep for
  release sign-off and third-party integration. **Paul has no contention.** The argument's premise is
  absent here, so the conclusion does not transfer — see §1c.
- **Testing in production** ([New Relic on synthetic monitors](https://newrelic.com/blog/how-to-relic/smoke-testing-with-synthetic-monitors),
  [Keploy](https://keploy.io/blog/community/production-testing)) — the standard shape is
  **post-deploy smoke tests + synthetic monitors + a bounded ring** (synthetic test identities,
  internal accounts, one tenant). ⭐ This is the finding that breaks the brief's argument at §4.
- **Test data management** ([Parasoft](https://www.parasoft.com/blog/test-data-management-guide/),
  [GenRocket](https://www.genrocket.com/blog/synthetic-data-redefines-the-test-data-lifecycle/)) —
  prefer **isolation first, then masking, then synthetic generation**; never copy production data
  downward; and a TDM strategy must state **who owns the pipeline, how often environments refresh,
  and the cleanup policy**. That is a direct, specific answer to `DECISIONS.md` §7, which asks for
  exactly those three things and does not have them written down.
- **Configuration drift** ([Octopus](https://octopus.com/devops/configuration-management/configuration-drift/),
  [Spacelift](https://spacelift.io/blog/what-is-configuration-drift)) — drift between environments is
  a *named, expected* failure; the remedy is a **declared baseline plus an automated diff in the
  pipeline**, not vigilance. "Testing and staging environments are often under-provisioned or
  simplified due to cost" is the textbook cause and it is the literal cause of 0b.

## 1b · ⭐ THE RECOMMENDATION — three stages, one rig, one archive. Five deployments.

**And the count is not what fixes this. The classification is.** Today there are six deployments and
*zero* declared classes, so `bob` (somebody else's house), `lab` (a scratchpad) and `home` (real
people) are all the same kind of thing to every tool that reads the toml.

| name | class | what it is FOR — one line |
|---|---|---|
| **dev** | stage | Where unreviewed code runs. Nothing produced here is evidence about anything. |
| **qa** | stage | The release candidate on production's substrate; the synthetic loop runs here until it stops failing. |
| **production** | stage | The only place a real person's data exists; code arrives only by promotion from qa. |
| **rig** | not a stage | An empty, production-shaped deployment for walking what production structurally cannot hold, and for two-store diffs. |
| **archive** | not a stage | The frozen legacy Fernwood. A data control. Deploys are refused. |

**Why three stages and not two, given Cloudflare says "at least two":** because Paul's own definition
requires three. *"QA is essentially a mirror of production where I am testing out the latest and
greatest, and dev is separate."* If dev and qa are one environment, then the environment the
synthetics certify is the same one being edited underneath them — and `DECISIONS.md` F3 already
measured that exact failure (four seats reported at `ebdf172`; the countable runs sat at three
earlier shas). **A release candidate has to stop moving. That is what makes qa a third thing.**

**Why not four (adding a staging/pre-prod):** nothing would be true of it that is not true of qa, and
every added environment is another row the parity check has to hold identical. At n=1 engineer, a
fourth stage is pure parity debt.

## 1c · ⛔ Do NOT add ephemeral / preview environments now. Named so it is not rediscovered.

The platform offers them free (per-branch preview URLs for Workers since 2025-07-23; Pages preview
deployments). Three reasons to decline, in order of weight:

1. **The problem they solve is contention, and Paul has none.** Every argument in the literature is
   about multiple engineers colliding on shared staging. One builder plus an AI pair never collides.
2. ⛔ **A preview URL shares its environment's bindings.** A preview of the production Worker reads
   **production KV**. In a codebase whose entire current risk is a scope bug becoming a cross-household
   disclosure, handing out extra URLs onto the production namespace is the wrong direction this month.
3. **They would make parity harder, not easier** — more surfaces, same number of comparators.

⭐ **Revisit when** either (a) a second person writes code here, or (b) the tenancy conversion has
landed and per-request scope makes a preview URL harmless. Learning value is real but it is the
smaller lesson; the parity work below teaches the thing that is actually broken.

---

# 2 · RECONCILING dev / QA / production AGAINST SIX ENVIRONMENTS + GITHUB PAGES

## 2a · ⛔ THE NAMING COLLISION IS A FIRST-CLASS PROBLEM, AND ONE HALF OF IT IS PERMANENT.

There are **four** vocabularies in play and they overlap on the word that matters most:

| vocabulary | says "production" means |
|---|---|
| wrangler's | *(nothing — the top level takes no `--env`)* |
| `wrangler.toml`'s `[vars] ENV_NAME` | **the frozen legacy instance**, est-3c9f1a |
| the tools | `grant-mint.py` calls the top level `prod`; `deploy-worker.sh` refuses `prod\|top\|fernwood` |
| Paul | **`home`** — where real people arrive |

⭐ **AND ONE OF THESE CAN NEVER BE CHANGED.** `ENV_NAME` is not only a label — it is **stamped into
every row** at four write sites (`worker.js:825, 1750, 3065, 3415`): feedback, zone-audio,
observations, server-side records. Eight months of Mom's data carries `env: "production"`, **and she
is still writing to it** — the frozen instance is frozen for *code*, not for *use*.

> ⛔ **Therefore: renaming the frozen instance's `ENV_NAME` would split her record in half at an
> invisible boundary — the exact shape of the `LEGACY_BEFORE` problem, one field over. Do not do it.
> The token `production` is permanently spoken for in the data, and the new production must keep
> `ENV_NAME = "home"` forever.**

That sounds like bad news and it is the opposite: **it means there is no data migration here at all.**
The collision is entirely in the *labels*, and labels are free to move.

### The fix — one new var, one refusal, one vocabulary entry

1. **Add `STAGE` to every environment** (`dev` · `qa` · `production` · `rig` · `archive`) and publish
   it in `/health`. `ENV_NAME` becomes what it always actually was: **an immutable deployment id that
   appears in data**. `STAGE` becomes the **role, which is allowed to transfer** — which is precisely
   the content-steward ruling already recorded in the toml (*"`production` is a ROLE that transfers"*),
   finally given a field of its own instead of borrowing one that is load-bearing in the store.
   ⭐ *One field was doing two jobs.* Same shape as the earlier note's *a scope says WHERE, a
   membership says WHAT* — and the same remedy.
2. **`grant-mint.py` stops calling the top level `prod`.** It calls it `archive`, and refuses it
   without a long flag, the way `deploy-worker.sh` already does. That script's refusal is the model;
   copy it rather than re-inventing it.
3. **One entry in `VOCABULARY.md` §4** recording `production` as a **rejected** name for the
   top-level environment, *with the reason* (it is the value in Mom's rows). §4 exists because
   "an alternative considered and rejected never gets written down, so the next reader re-proposes
   it." Two people lost an hour to this today. That is what §4 is for.

## 2b · The mapping — what is what, and what is vestigial

| today | Worker | KV | serves | → target | migration |
|---|---|---|---|---|---|
| top level `fernwood` | `fernwood` | est-3c9f1a / `100f2b95` | **Mom, live, via GitHub Pages** | **archive** | `STAGE=archive`. `ENV_NAME` **unchanged, forever**. Deploys already refused. |
| `lab` | `fernwood-lab` | est-3c9f1a / `1e0bd883` | Paul + Claude | **dev** | `STAGE=dev`. Renaming the *deployment* lab→dev is cosmetic churn — do it late or never; the toml already says the estate is what made it dev. |
| `qa` | `fernwood-qa` | est-qa0001 | gate 1 | **qa** | `STAGE=qa`, **plus the two parity fixes in §5 step 4** — this is the real work. |
| `home` | `fernwood-home` | est-e6696a | the new product's production | **production** | `STAGE=production`. `ENV_NAME` stays `home`. |
| `bob` | `myhome-bob` | est-9a74df | *empty* (R1 hold) | **retire at the merge** | After one production environment lands, Bob's household is a **row**, not a deployment. Keep until R1 releases, then `wrangler delete`. |
| `paul` | `myhome-paul` | est-d93508 | *empty* | **rig** | `STAGE=rig`. Give it the job in §4c, or delete it — an empty deployment with no job is pure staleness surface (R2's own accepted cost). |
| GitHub Pages `palekxk.github.io/Tate-Tracker/viewer.html` (branch `main`) | — | — | **Mom's actual front end** | **the archive's front end** | Not a pipeline origin. Record the pairing explicitly: `main` → GitHub Pages → top-level Worker → est-3c9f1a. Nothing else in the pipeline touches it. |

**Vestigial, found tonight:**
- Local git branch **`prod`** exists and is unused. Delete it or it will get deployed by somebody.
- Local `main` is **259 ahead / 1 behind** `origin/main`. The 259 is the deliberate freeze. The
  **1 behind** is not deliberate and nobody has looked at it.
- `origin/staging` (QA's branch) is **12 commits behind HEAD**.

## 2c · What "QA mirrors production" costs, concretely

Paul asked what it means and what it costs. Here it is priced, for this project:

| dimension | make it mirror | the cost |
|---|---|---|
| Worker code | already true — same `worker.js`, `--env` only swaps bindings | free |
| KV namespace | separate ids, same binding — already correct | free |
| `LEGACY_BEFORE` | re-key QA's pre-cutover rows, set `1970-01-01` | **~an hour.** The toml says QA "holds only probe rows"; this is the cheapest possible instance of the whole ask |
| secret set | `configured.*` must match | a decision per key, not labour (§6) |
| **front-end file set** | put `qa` in `HOUSEHOLD` — 8 files, not 819 | ⚠️ **the real cost: QA stops serving `viewer.html`.** Check `qa-divergence.py` and the mom-cycle checks first |
| real data | ⛔ **never mirror this** | — every source above says do not copy production data downward |

⭐ **"Mirror" means *structurally identical, differently populated*.** Same code, same shape, same
capabilities, same file set, same era semantics — different namespace, different estate, different
people. It never means the same rows.

---

# 3 · HOW PARITY IS ENFORCED RATHER THAN ASSERTED

## 3a · The mechanism: `tools/check-env-parity.py`, four layers, all derived

Nothing here is novel — it is the drift-detection shape from the literature (declared baseline +
automated diff in the pipeline) built to this repo's own derivation rule.

- **Layer A — config → config, no network.** Parse `worker/wrangler.toml`. Roster of environments
  derived exactly the way `deploy-worker.sh` already derives it (grep `^\[env\.X\]` + the top level),
  so **an environment declared tomorrow is covered tomorrow**. Compare the *key sets*: any var present
  in one environment and absent from another is a finding before anything is deployed. Zero
  environments parsed → **exit 3, UNCHECKABLE**, never green.
- **Layer B — config → reality.** `GET /health` per environment (send a User-Agent; the edge 403s
  UA-less requests). **Declared ≠ served** means either an undeployed config change or a mis-bound
  namespace. `kv_canary` already covers the second and covers it well.
- **Layer C — reality → reality.** `qa` vs `production`, key by key, **over the UNION of keys present
  in either payload** — so a binding nobody thought about is compared automatically rather than
  waiting for someone to add it to a list. Every key falls in exactly one class:

| class | rule | keys today |
|---|---|---|
| `IDENTITY` | **must differ** in every environment | `env`, `kv_canary`, `estateId`, origin/`FAMILY_HOSTS` |
| `STRUCTURAL` | **must be identical** qa↔production | `legacyBefore`, `configured.*`, `endpoints`, cpu limit, **served code sha** |
| `TUNED` | may differ, **but only with a reason recorded in the toml keyed to that env** | `chat_budget.ceiling_usd` |
| `UNCLASSIFIED` | anything not in the table → **exit 3, UNCHECKABLE** | — |

  ⭐ Two agreeing `IDENTITY` values is the *loudest* alarm in the whole instrument — it means two
  environments are pointed at one store.

- **Layer D — the front end.** Compare the served `qa-build.json.sha` per origin (it already exists
  and `pages-deploy.py` already writes and verifies it — good work, reuse it), **and** probe the
  **derived removed-set**: `pages-deploy` computes exactly which files it pruned, so that list needs
  no typing. Each must return the fallback shell **from the edge**, not from the export.

## 3b · What it catches on the day it is written

1. `legacyBefore` qa=`2026-09-03` vs production=`1970-01-01` → STRUCTURAL. **RED.**
2. `configured.anthropic` qa=true vs production=**false** → STRUCTURAL. **RED.** *(the one nobody had named)*
3. `chat_budget` absent on the archive, 3 on qa, 10 on production → TUNED; qa/production need reasons,
   and the archive's **absence** is a shape difference, not a value difference.
4. The front-end file set: 819 vs 8 → STRUCTURAL. **RED.**
5. §0a's cached files → Layer D. **RED**, and it would have been red at 18:37.

## 3c · Where it is wired — not listed

Per this repo's own fourth-instance finding (*a check wired into the thing it guards cannot be
forgotten; a check listed in a document can*), and following `pages-deploy.py`, which is the model:

- **`deploy-worker.sh`, post-deploy** — it already asserts `/health` reports the env it targeted.
  That reads **one field of a payload that carries the whole parity vector.** Widen the same
  assertion; it is the cheapest possible place.
- **A promotion gate** — refuse `--env home` while qa↔production is structurally RED. This is the
  mechanical enforcement of Paul's release loop: *you may not promote what qa did not certify.*
- **`pages-deploy.py`, post-deploy** — purge the removed set, then re-probe it (§5 step 0).
- **The session-start block** — as the reader's index, not the enforcement.

## 3d · ⚠️ TWO ORACLES MUST BE FIXED BEFORE THEY CAN BE TRUSTED

Both are the same defect as the thing being fixed, which is why they are easy to miss:

1. **`/health`'s `endpoints` array is hand-typed and has already drifted** (§0d) — it omits the
   entire identity surface. **Derive it from the router**, or the parity check will compare two
   equally-wrong rosters and print green. *(A shared roster that is wrong in both environments is
   worse than no roster: it is a passing test.)*
2. **`check-estate-neutral.py --url` walks one path** (§0a) — it must walk a **derived path set**: the
   allow-list, plus the pruned set, plus whatever the arrival surface links to. Finding nothing must
   print **UNCHECKABLE**, which the tool already knows how to do in its file mode (exit 3) and does
   not do in its URL mode.

---

# 4 · WHERE SYNTHETIC PERSONAS LIVE

## 4a · The placement

| environment | durable persona data? | why |
|---|---|---|
| **dev** (`lab`) | ✅ scratch personas, freely reset | nothing here is evidence |
| **qa** | ⭐ **the personas' home.** One durable account per role per env — the existing `role@env` key is already right | this is the environment the release loop runs in, so this is where run 2 must be comparable to run 1 |
| **rig** (`paul`) | ✅ one founding persona | see §4c |
| **production** (`home`) | ⛔ **none standing** | real people only |
| **archive** | ⛔ never | Mom is in there |

**Industry practice, and it answers `DECISIONS.md` §7 directly.** A test-data strategy must state
three things — *who owns the pipeline, how often environments refresh, what the cleanup policy is*
(Parasoft, GenRocket). Here is the smallest version that answers §7's actual axes:

| outcome ↓ / env → | dev | qa | rig | production |
|---|---|---|---|---|
| a cycle that **failed** | rows deleted at the next green run; **report kept** | rows deleted at the next green run at a later sha; **report kept forever** | same | n/a |
| a run **superseded** by a later sha | rows deleted, report kept | rows deleted, report kept | deleted | n/a |
| a **durable persona's own profile** | permanent (one per role) | **permanent (one per role)** | permanent | ⛔ none |
| a **real person's** data | n/a | n/a | n/a | permanent; **no tool that resets test data may reach it** |

⛔ **And the rule that falls straight out of §6's incident** — production seats' grants were deleted
by a reset while the register still read live: **`reset-production-estate.py` must refuse any
environment whose `STAGE` is `production`**, and the seat register must derive liveness from the
store rather than from its own file. *A register that can disagree with the store will.*

## 4b · ⭐ TESTING THE "PRODUCTION SYNTH IS THEATRE" ARGUMENT — it is half right, and wrong about the remedy

The argument: production has one household, so a synth there joins Mom's estate rather than founding
its own; therefore a production synth walk is theatre until tenancy lands.

**Where it is right, and it is genuinely right:**

- The estate is a **deploy-time binding** (`ESTATE_ID`), so *founding a household* is structurally
  unavailable to any second walker on production. What gets exercised is "join an existing estate,"
  which is not the journey Mom takes.
- Worse, each synth **contaminates the estate the next one meets** — so on production the durable-
  persona property Paul just ruled for works *against* comparability, because all personas share one
  estate rather than each holding their own.
- And it requires a reset before the real invite, which has already cost real state once.

**Where it breaks — three ways, and the first is decisive:**

1. ⭐ **A walk makes two claims, and only one of them is portable.** It asserts (a) *the journey
   works* — copy, ordering, comprehension — and (b) *this deployment serves it*. Claim (a) travels
   across environments and should be established once, in the lowest environment that can hold it.
   **Claim (b) does not travel and can only be established where it runs.** The theatre verdict is
   correct about (a) and *false about (b)* — and it throws away the half only production can answer.
   **Tonight is the proof:** if there were genuinely nothing worth checking on production, §0a's
   314 KB of Fernwood canon and §0b's missing Anthropic key would not have been sitting there unseen.
2. ⛔ **The premise is factually off.** `--env home` is **Mom's** estate (est-e6696a), not Paul's; and
   `--env paul` is a **separate, empty, production-shaped deployment** (est-d93508) that R2 keeps as a
   declared rig. **So an environment where a synth can found a household from nothing already
   exists** — the argument's constraint is a property of `home`, not of production-shaped
   deployments in general.
3. **Claim (b) does not need a persona at all.** The literature's answer to "verify production
   without a real user" is **post-deploy smoke tests + synthetic monitors + a bounded ring** — not a
   full journey walk. The mistake is using the *journey persona* as the *substrate probe*. Different
   instruments, different data lifecycles: one accretes a profile on purpose, the other must leave
   nothing behind.

⭐ **So the honest rule is not "no synth on production." It is:**

> **A durable persona's home is the lowest environment that can hold the WHOLE journey. Production
> gets a probe, not a persona — and most of what a production walk was reaching for is answerable
> deterministically, with no walk at all.**

Most of §0a and all of §0b were found tonight by `curl` and `/health`, in under a minute, with no
browser and no account. **That is the strongest possible argument that the production check should be
deterministic rather than a walk** — and it is squarely on the standing rule that *deterministic
things need a non-AI door.*

## 4c · So what runs where

| instrument | environment | what it certifies |
|---|---|---|
| the **synthetic loop** (`journey-walk`, `walk-integrity`, `read-onboarding`) | **qa** | the journey works — runs until it stops failing (`DECISIONS.md` §5) |
| the **founding walk** (one persona, sign-up from nothing) | **rig** (`myhome-paul`) | that a first person can found a place on a production-shaped deployment. ⭐ *This gives the rig the job R2 left it without, and turns an accepted staleness cost into a control.* |
| **`check-env-parity`** + the Layer-D origin probe | **production**, every deploy | that production is what qa certified |
| **Paul's own walk** | **production** | gate 3 — the release event. Nothing else. |

⭐ **`--watch` is the unused affordance that makes gate 1 match Paul's stated definition.**
`journey-walk.py` already has it (`paul-stated 2026-09-06`, *"I like being able to watch the walk
through in Chrome"*) and it is not in any procedure. *"All the synthetics have gone through it in
Chrome"* is his stated production-ready bar; the flag that satisfies it exists and is unreachable
from the loop. Fourth instance of that shape — wire it, don't build anything.

---

# 5 · WHAT "RESET THE PIPELINE" MEANS — the cheapest honest sequence

Constraints held fixed throughout: **the frozen instance is never touched** (Mom keeps using it, its
`ENV_NAME` never changes, its GitHub Pages front end never moves); **the two rigs stay empty**; and
**nothing here blocks or is blocked by the tenancy conversion** — this is the pipeline the conversion
will land *on*.

| # | step | why now | cost |
|---|---|---|---|
| **0** | ⛔ **Purge the edge cache for `fernwood-home`'s pruned paths, re-probe, confirm the shell.** | §0a. This is the only step with a live outside-facing consequence, and it blocks any invite. | minutes |
| **0b** | Wire purge + re-probe into `pages-deploy.py` from the derived removed-set. | so the fix is a property of the deploy, not of tonight | ~an hour |
| **1** | Add `STAGE` per env; publish in `/health`; `grant-mint.py` stops saying `prod`; one `VOCABULARY.md` §4 entry. | names the seam. **No data changes.** | one short session |
| **2** | Derive `/health`'s `endpoints` roster from the router; give `check-estate-neutral --url` a derived path set + honest UNCHECKABLE. | **the oracles must be true before the comparator reads them** | one session |
| **3** | Build `check-env-parity.py` (Layers A–D). Wire into `deploy-worker.sh` post-deploy **and** as the qa→production promotion gate. | the instrument. Red on day one, on five real findings | one session |
| **4a** | **Re-key QA's pre-cutover rows under `est-qa0001`; set `LEGACY_BEFORE=1970-01-01`.** | removes the one dimension the tenancy conversion is *about*. QA holds only probe rows, so it is nearly free | ~an hour |
| **4b** | Decide + apply the secret set on production (§6·3). | Guru cannot run on production today | a decision, then minutes |
| **4c** | Add `qa` to `HOUSEHOLD` so it ships the same 8 files production does. ⚠️ Check `qa-divergence.py` and the mom-cycle checks first. | the largest remaining structural divergence | ~a session, **Paul's call** |
| **5** | Give `myhome-paul` the founding-walk job + the staleness control R2 already conceded was overdue. Mark `myhome-bob` for deletion at the merge. | the rigs stop being liabilities | ~an hour |
| **6** | *Then* the tenancy conversion, on a pipeline that works. | R3's store-diff now has a parity baseline under it | (separate) |

**Steps 0–3 are the reset.** Steps 4–5 are what makes QA a mirror. Nothing before step 6 touches
`worker.js`'s scope handling, so none of it collides with the conversion — and step 3's promotion
gate is exactly the instrument R3 wants standing before the blind stretch.

---

# 6 · WHERE I AM RULING vs. WHERE IT IS PAUL'S

**Ruling (engineering — take these unless the reasoning is wrong):**
- Three stages (`dev` · `qa` · `production`), plus a `rig` class and an `archive` class. Five
  deployments. **The classification is the fix, not the count.**
- ⛔ **No ephemeral / preview environments now.** The problem they solve is contention; there is none.
  A preview URL reads its environment's real bindings.
- ⛔ **Never rename the frozen instance's `ENV_NAME`.** It is the value in eight months of Mom's rows
  and she is still writing. Add `STAGE`; keep `ENV_NAME` immutable everywhere.
- **Parity is a derived comparator with four classes and an UNCLASSIFIED→UNCHECKABLE exit**, wired
  into the deploy and the promotion gate. Not a document, not vigilance.
- **Fix `/health`'s roster and `check-estate-neutral --url` before trusting either as an oracle.**
- **Personas live in qa. Production gets a deterministic probe, not a persona** — and the founding
  walk gets the empty rig, which is the job R2 left it without.
- **Purge the edge after pruning a household origin.** Removing a file from a deployment does not
  un-serve it.
- **`reset-production-estate.py` must refuse `STAGE=production`.**

**Paul's call — ordered by what blocks the most:**
1. ⭐ **Purge `fernwood-home`'s edge cache tonight?** Nothing outward can go out over it until then.
2. ⭐ **Does QA prune to the 8-file household shell?** It is the largest remaining divergence and the
   cost is real: QA stops serving `viewer.html`. If the legacy viewer must stay walkable, walk it on
   the archive, where it actually lives.
3. **Does production get an `ANTHROPIC_API_KEY`** — i.e. is Garden Guru part of the new product's
   production, or deferred? Today production declares a $10 ceiling for something that 503s.
4. **Re-key QA's legacy era, or record the divergence as intentional with a reason?** (I recommend
   re-key; it is ~an hour and it is the dimension the conversion is about.)
5. **`myhome-bob` — delete at the merge, or keep as a second rig?** (I recommend delete; after the
   merge Bob's household is a row.)
6. **Is `myhome-paul` the founding-walk rig, or is it deleted?** An empty deployment with no job is
   staleness surface.

---

⭐ **And note the ancestor already in the library:** `fernwood.md` carries *"a deploy-bundled context
artifact needs a rebuild-and-diff drift alarm"* (agent-proposed 2026-07-07, from the stale-digest
incident). `check-env-parity.py` is that same principle applied one level up — **the environment is a
deploy-bundled artifact too, and it has never had the alarm.** If Paul confirms, the cleanest move may
be to *generalise the existing principle* rather than add a new one.

## Principles to propose (NOT added — awaiting Paul's confirmation)

1. **Removing a file from a deployment does not un-serve it.** — cross-project. The deployment's file
   set and the CDN's file set are two different things; a prune is not complete until the removed set
   is purged and re-probed at the edge.
2. **An identifier written into DATA must be immutable; a label that names a ROLE must be free to
   move. Never one field.** — cross-project. When they are the same field, renaming the role
   silently splits the record.
3. **A shared roster that is wrong in both environments is worse than no roster — it is a passing
   test.** — cross-project. Derive the roster on both sides before comparing them.
4. **"Mirror" means structurally identical, differently populated.** — cross-project. Same code,
   capabilities, file set and era semantics; never the same rows.
5. **A walk asserts two claims — *the journey works* and *this deployment serves it*. Only the first
   travels between environments.** — cross-project.
6. **A durable persona's home is the lowest environment that can hold the whole journey. Production
   gets a probe, not a persona.** — cross-project.
7. **Prefer the deterministic probe to the walk wherever the question is about the substrate.** —
   fernwood. Tonight's two worst findings took a `curl` and under a minute.

*(Carried forward, still unconfirmed, from earlier today: listings drive views / direct GETs drive
decisions · hand out the narrowest handle · a scope says WHERE and a permission says WHAT ·
isolation and sharing are two claims needing two tests · onboard the person you can afford to move ·
when a recommendation reverses, say which requirement moved.)*

---
---

# ADDENDUM — direction inverted, blocker tested, framework named
*(2026-09-06, later the same night. Everything above §6 stands except where retracted in A2.)*

## A · CORRECTIONS

### A1 · The edge leak is fixed. I re-verified it myself rather than taking it on report.

| path | before (22:50) | now |
|---|---|---|
| `/CLAUDE.md` | 200 · 93,070 b · address ×2 | 200 · **169 b stub**, no cached object |
| `/plants.json` | 200 · 314,203 b | 200 · **169 b** |
| `/onboarding/invite-message.md` | 200 · 3,562 b | 200 · **169 b** |
| `/estate.json` | *(untested then)* | 200 · **169 b** |
| `/viewer.html` | 200 · shell | **308** |

`grep -c "Church Mountain"` over `/CLAUDE.md`, `/plants.json`, `/estate/`, `/` → **0, 0, 0, 0**. Good
fix, and tombstoning rather than waiting out `s-maxage` was the right call.

⚠️ **One residue, `nit`-level:** `/onboarding/` still contains the string once — at
`onboarding/index.html:1547`, inside a **JS comment** about QA store fixtures. Not rendered; visible
in view-source. Delete the two words from the comment.

⭐ **But note *why* nothing caught it:** `check-estate-neutral.py:31` — `PAGE = estate/index.html`.
**The checker's scope is one hard-coded file.** It does not cover `onboarding/`, `homes/`, or either
settings page. That is §3d's finding again, second instance, on the arrival surface a stranger meets.

### A2 · ⛔ RETRACTED: §2c's "front-end file set" row and §5 step 4c (prune QA to 8 files).

Both were pointed the wrong way. Paul's direction is **production up to QA**, and he is right — see
C3 for *why* he is right in the standard's own vocabulary, which is a stronger reason than the one in
his sentence. §4c's persona split (personas in QA · deterministic probe in production · founding walk
on the rig) stands unchanged and is now the live plan; Paul's "no synths in production" ruling
tightens it rather than moving it.

---

## B · ⭐⭐ THE COORDINATOR'S BLOCKER — I TESTED IT. IT IS MOSTLY ALREADY BUILT.

**The claim:** *production ships 8 files as a leak mitigation; there is no estate-neutral build of the
full application anywhere; so "bring production up to parity" is not a config change but the same seam
as the tenancy conversion.*

**Verdict: right about the requirement, wrong about the state, and the gap is ~10 strings.**

### B1 · The experiment (run tonight, reproducible)

`tools/build-viewer.py` already builds `viewer.html` from `engine/viewer.template.html` (1,091,577 b,
placeholdered) + an instance config. It already takes `--instance <config> --out <path>` — *"another
estate (C4 5c)"* — and already has a **declared-absence** mechanism. So I built one:

```
instance: estate=neutral-probe · estateId=est-probe01 · identity name "My Home"
          canon dir containing ONLY a stub property.json + estate.json
          absent: all 16 domains
→ BUILT: 1,092,020 bytes. A complete, working, non-Fernwood app.

python3 tools/check-estate-neutral.py --page <that build>
→ 🔴 10 household-specific tokens · out of 311 needles
```

**For contrast, the same check on Fernwood's real `viewer.html`** flags the address, every vehicle,
`Acer palmatum`, the whole canon. **On the neutral build, none of that appears.** The data layer is
already fully separated.

### B2 · The entire residual, with line numbers

| # | token(s) | site | class |
|---|---|---|---|
| 1 | `Fernwood` · `Blue Ridge` · `Chestnut` · `Pitcher Plant` | `SOURCES_DATA`, line 5912 | ⭐ **4 of 10 are ONE const** — and it is one of the two P5 consts with **no producer**, already on the C5 Q5 list to get one or retire |
| 2 | `Sequoyah` | line 8542, a literal in a render function | config re-typed into engine (P4) |
| 3 | `Hydrangea` | line 6877 — `const susceptible = ["boxwood","hydrangea","mountain-laurel"]` | P4 |
| 4 | `Japanese Maple` | line 7907, frost-advisory prose | P4 |
| 5 | `Mountain Laurel` | line 7841, rain-advisory prose | P4 |
| 6 | `Snowy Tree Cricket` | line 16692, authored prose | P4 |
| 7 | `White Pine` | line 13548, a display-name map | P4 |

**Five sites. All of them are the P4 class `check-engine-manifest.py` already counts** (P4 = 6,
ARMED). This is not a conversion. It is an afternoon, and the instrument that finds them already
exists and already prints line numbers.

### B3 · So the honest answer to Paul's question — *config change, or a build?*

> ⭐ **Neither. It is a bounded string cleanup that is already instrumented, plus one product decision
> nobody has made: what a brand-new household's app SHOWS when it has nothing in it.**

**That empty state is the real blocker, and it is a product question, not an engineering one.** A
neutral build renders the whole application with every domain empty: no plants, no wildlife, no
vehicles, no zones, no station. Whether that reads as *"a journal waiting for you"* or as *"broken"*
is not answerable by analysis — **it is answerable by one synth walk**, which is exactly why it
belongs on list 2 in §D.

### B4 · ⚠️ Two real defects the experiment surfaced, both small, both worth fixing before this is load-bearing

1. **`absent` is a no-op whenever the canon file exists.** `build-viewer.py:205` —
   `if os.path.exists(path): load()` runs *before* the `absent` branch. With Fernwood's default
   `"canon": ".."`, an instance can declare every domain absent and still be built with Fernwood's
   entire canon, **silently**. *A declaration the build can ignore is not a declaration.* Make an
   explicit `absent` win over a present file, or refuse the combination.
2. **`property.json` is loaded unconditionally** (line 198) even when `property` is declared absent,
   so a foreign instance cannot build without one. Arguably correct — a place has an address — but it
   should say so rather than raising `FileNotFoundError`.

### B5 · ⛔ AND THE COUPLING THE BLOCKER *DID* GET RIGHT, THOUGH NOT WHERE IT LOOKED

The engine/instance split is a **BUILD-time** split: one deployment, one instance, injected at build.
That works because one deployment = one estate. **One production environment with many households
makes it a RUN-time requirement** — the same origin must serve a viewer that resolves *which*
household it is per request.

⭐ **That is a real dependency on the tenancy conversion, and it is not on tonight's critical path**,
because production has one household today. Two things make the eventual conversion cheap and are
worth knowing now: the viewer already fetches 4 of its 21 JSONs at runtime, and `ESTATE_ID` /
`ESTATE_MODULES` are already single consts with single producers — i.e. **the seam is already one
line wide.** Build-time injection is correct until the merge; do not pre-build for it.

---

## C · THE STANDARD FRAMEWORK — named, and Paul's model restated in it

### C1 · It is the **deployment pipeline** from Continuous Delivery (Humble & Farley), not "environments"

The canonical vocabulary, and it is worth adopting wholesale because every question in this thread has
an existing name in it:

- **[Deployment pipeline / Build once, deploy many](https://continuousdelivery.com/implementing/patterns/)**
  — *"build your binaries only once"*, *"binaries should not be environment-specific"*, *"deploy the
  same way to every environment"*, *"each change should propagate through the pipeline instantly"*.
  ⭐ **This is the framework.** The unit that moves is an **artifact**; environments are places you
  **promote** it to; and what makes a green QA run mean anything is that *the same artifact* reaches
  production.
- **[Trunk-based development](https://trunkbaseddevelopment.com/feature-flags/)** + **[feature
  toggles](https://featureflags.io/feature-toggles/)** (Fowler's pattern; Pete Hodgson's
  release / ops / experiment / permission taxonomy) — *"release toggles are short-lived and used to
  **decouple deployment from release**."* The unfinished feature ships everywhere, dark.
- **[12-factor III (config) and X (dev/prod parity)](https://12factor.net/dev-prod-parity)** — config
  in the environment; keep the time, personnel and **tools** gaps small.
- **[Expand / contract, a.k.a. parallel change](https://www.tim-wellhausen.de/papers/ExpandAndContract/ExpandAndContract.html)**
  ([Prisma's writeup](https://www.prisma.io/dataguide/types/relational/expand-and-contract-pattern))
  — the standard four-step for evolving a schema under live data: **expand** (add the new shape,
  backward-compatible) → **migrate** (dual-write / backfill) → **switch reads** → **contract** (remove
  the old). ⭐ This repo is *already doing it* and does not have the name: `LEGACY_BEFORE` is a
  hand-rolled expand-phase read router. Naming it tells you the missing steps — nothing has migrated
  and nothing has contracted, which is why `LEGACY_BEFORE` is still divergent.

### C2 · Where Paul's instinct MATCHES standard practice — and it matches more than it diverges

- **Three stages with promotion between them** is the deployment pipeline, exactly.
- **"Production is the proven part; QA is proven + the candidate"** is *precisely* the pipeline's
  claim that a later stage contains everything earlier stages proved. That is the right mental model
  and most people never articulate it that clearly.
- **"Dev is a loose playground"** matches — the pipeline's first stage is where you are allowed to
  break things, and nothing produced there is evidence.
- **"Bring production up to QA, don't reduce QA"** is right, and the standard's reason is stronger
  than his: reducing QA would violate *"binaries should not be environment-specific."* **You would be
  certifying an artifact nobody ships.**

### C3 · ⛔ Where it diverges — two corrections, since he asked to be corrected

**① "QA = production + the candidate feature" makes the ENVIRONMENT the feature flag.**
In the standard model the feature delta is **configuration inside one artifact**, not a difference
between two artifacts. Environment-as-flag has three costs, and this repo is paying all three:
- What QA proved is not what production runs (today, literally: 819 files vs 8).
- The feature can only be turned on for *everyone in an environment* — never for one household, never
  rolled back without a redeploy.
- Every added feature widens the artifact gap, so parity gets *harder* the more you build.

**The fix is a `FEATURES` var, not another environment.** Same artifact everywhere; QA turns the
candidate on; production turns it on when Paul clears it. That is Fowler's **release toggle**,
short-lived, deleted after the release. ⭐ **And you already have an accidental one:** production has
no `ANTHROPIC_API_KEY`, which is a feature flag implemented by the absence of a secret — the worst
kind, because it cannot be scoped, cannot be rolled back, and reports as a 503 rather than as *off*.

**② "Parity" and "promotion" are two different mechanisms and the thread has been conflating them.**

> **Parity is a property of the ENVIRONMENT — same runtime, same bindings, same capabilities, same
> shape. Promotion is a property of the ARTIFACT — the same built thing moving forward.**

My §5·4c recommendation (prune QA) was a *parity* move applied to an *artifact* problem, which is how
it came out backwards. With the two separated, Paul's instinct and the standard agree completely:

> ⭐ **QA and production must be IDENTICAL in substrate and differ ONLY by a flag.**

That single sentence replaces §2c's table and §5 step 4c.

---

## D · ⭐⭐ THE TWO LISTS — what must be answered now vs. what testing settles

**The sorting rule, so this is reusable rather than a one-off verdict:**

> **If a wrong answer changes the SHAPE of an artifact or a schema, answer it before building —
> unwinding it costs a migration. If a wrong answer changes only pixels, copy, or ordering, ship it
> and let a walk settle it — analysis is slower than the walk and less reliable.**

### LIST 1 — must be answered before building. **Three questions. That is all.**

| # | question | why it cannot wait |
|---|---|---|
| **N1** | **Is production's artifact the FULL app (engine template + its own instance), or the 8-file shell?** | It is the artifact decision. Everything below inherits it, and B2's cleanup is only on the critical path if the answer is "full app." *(My read of Paul's direction: full app. I recommend it.)* |
| **N2** | **Is the feature delta a FLAG in one artifact, or a different artifact per environment?** | Build-once is cheap to adopt now and expensive to retrofit after artifacts have branched further. This is C3·① and it is the highest-leverage decision on the page. |
| **N3** | **For a brand-new household, is a domain ABSENT (module not present) or EMPTY (module present, no records)?** | Schema-shaped, and `build-viewer.py` already fails loud on an undeclared absence — so the build has an opinion and nobody has ratified it. Expand/contract applies: get it right once. |

Everything else that felt like a blocker tonight is either already ruled, already built, or belongs
below.

### LIST 2 — testing settles these, faster and better than analysis. **Do not pre-decide them.**

1. **What the empty app should look like** — which cards render for a household with nothing, in what
   order, what an empty card says. *One synth walk.* ⭐ **This is B3's "real blocker" and it is on
   this list on purpose.**
2. **Whether a first-time reader reads the empty state as "waiting for me" or as "broken."** The only
   instrument for this is a wide-eyed walker.
3. **Which of B2's 10 tokens a foreign reader can actually reach.** Several sit in advisory prose for
   plants a new estate does not have — they may never render. *Build neutral, load it, look.* Fix the
   reachable ones first.
4. **Whether the onboarding journey survives on the full app.** The shell's journey is proven; the
   shell inside a 1 MB app is not. A walk answers it; reasoning cannot.
5. **Whether Guru belongs in a household with no canon.** A Guru with an empty digest is a different
   product. Walk it in QA before spending a decision on it.
6. **Module ordering, theme, text-size default, masthead phrasing for a non-Fernwood name.**
7. **Whether the founding walk on the rig is representative of production.** Run both; diff.
8. **Whether rate limits and the chat ceiling hold under a full synth battery.** Only load answers this.
9. **Whether the neutral build's file size (1.09 MB) is acceptable on Mom's conditions (414 × A+).**
   Measured, not argued.

⭐ **Nine questions moved off the critical path.** Paul's frustration is well-founded: eight of these
had certainty being sought for them, and every one is cheaper to walk than to decide.

---

## E · THE DETERMINISTIC / GENERATIVE SPLIT IN THE ENVIRONMENT STRATEGY

Paul raised this unprompted and it is the sharpest thing in his message. The standard has a name for
it and the name resolves the parity question cleanly.

### E1 · The standard split

The practice literature on testing non-deterministic systems converges on one shape
([property-based testing for LLM systems](https://tianpan.co/blog/2026-04-12-property-based-testing-for-llm-systems),
[golden-dataset evaluation](https://qaskills.sh/blog/golden-dataset-llm-evaluation-guide)):

> **The deterministic SHELL — routing, retrieval, tool calls, guardrails, authorization, fallbacks —
> gets ordinary tests with hard assertions. The probabilistic CORE gets invariant tests (does it
> parse, is every claim grounded, are forbidden fields absent) plus an eval suite scored against a
> versioned golden set with a threshold.**

The named failure is `assertEqual(output, expected)` — *"the most common way LLM features ship
untested is that the team tried it, watched it fail on a re-run, and concluded the thing is
untestable."* This repo has the finding already (**AI output breaks environment parity**) and drew the
right conclusion about capture; it has not yet drawn it about *gates*.

### E2 · What parity MEANS for a generative surface

> ⭐ **Parity on a generative surface is parity of CONFIGURATION and CONTRACT — never of OUTPUT.**

So the §3a comparator gets a **fifth class**:

| class | rule |
|---|---|
| `GENERATIVE` | compare **the key's presence, the model id, the declared ceiling, the guardrail set, the route's status code and response SHAPE**. ⛔ **Never compare the text.** A text difference between qa and production is not drift; it is the product working. |

That class is what makes §0b's finding statable precisely: `configured.anthropic` true-vs-false is a
**GENERATIVE-class parity failure** (the capability is absent), while two different Guru answers to
the same question in qa and production would be **no finding at all**.

### E3 · Can a non-deterministic capability be part of a promotion gate?

**Yes — but only as an invariant/threshold gate, never an equality gate, and it must be able to
report UNCHECKABLE.** Concretely, for Guru: the gate asserts the route answers, the response parses,
the cost lands in the ledger, the budget decrements, no forbidden field appears, and — if a golden set
exists — a grounding score over N runs clears a threshold with margin. It never asserts *what Guru
said*. And if the key is absent, the gate is **UNCHECKABLE (exit 3), never green** — which is exactly
the shape this repo already uses everywhere else, applied to the one surface that most needs it.

### E4 · Flag, or environment?

⭐ **Flag. This is the single cleanest application of feature toggles in the whole project.** Grounded
in the ratified stance — *AI lives on the explicit ask path; capture stays deterministic and AI-free*:

- **The capture path is fully parity-checkable** and belongs in the `STRUCTURAL` class. It must be
  byte-for-byte the same behaviour in qa and production. No exceptions, no toggles.
- **The ask path is structurally unable to satisfy an equality check**, so it gets `GENERATIVE`
  treatment and a **release toggle** — one artifact, Guru on in QA, on in production when Paul clears
  it, and revocable per household later without a redeploy.

> ⭐ **The recorded finding "AI output breaks environment parity" is therefore not a problem to solve.
> It is a BOUNDARY to declare: it tells you exactly where the equality comparator stops and the
> invariant comparator starts.** Naming that boundary is what lets the deterministic 90% of this
> system be gated hard — which is the whole point of keeping capture AI-free.

---

## F · THE SHORTEST PATH, WITH A STOPPING POINT

**Goal, in Paul's words:** *synths have pre-tested in QA, and we can test everything in production.*

| # | step | required? | cost |
|---|---|---|---|
| 0 | ✅ edge purge — **done, independently verified** (A1) | — | done |
| 1 | Answer **N1 · N2 · N3** (§D list 1). Delete "Church Mountain" from `onboarding/index.html:1547`. | **required** | one sitting |
| 2 | Fix B4's two build defects (`absent` must win; `property.json` absence must speak). | **required** — the separation is not trustworthy without them | ~an hour |
| 3 | Fix B2's five sites. Give `SOURCES_DATA` a producer or retire it (4 of 10 tokens). | **required** | an afternoon |
| 4 | ⭐ **Wire `check-estate-neutral.py` to run against a NEUTRAL BUILD in CI**, not against Fernwood's viewer — and widen its `PAGE` from one file to the derived set (A1, §3d). | **required — this is the whole separation gate** | ~an hour, and the check already exists |
| 5 | **One artifact.** Production and QA both ship the full app built from their own instance. The household allow-list stops being the product definition and becomes an **export manifest** (keep repo files off a public origin); step 4's neutrality check on the origin is what proves tenancy safety. | **required** — this is C3·② | a session |
| 6 | Introduce `FEATURES` and move Guru's on/off out of secret-presence into an explicit release toggle. Give production its `ANTHROPIC_API_KEY` or declare Guru off. | **required** if N2 = flag | ~an hour |
| 7 | `check-env-parity.py` (§3a) **with the fifth `GENERATIVE` class** (E2). Wire into `deploy-worker.sh` and as the promotion gate. | **required** — it is what makes "pre-tested in QA" mean anything | a session |
| 8 | Re-key QA's legacy era → `LEGACY_BEFORE = 1970-01-01`. **Name it what it is: the migrate+contract steps of an expand/contract already in flight.** | **required** for qa↔production STRUCTURAL green | ~an hour |
| 9 | Run the synth battery in QA on the full app **until it stops failing** (`DECISIONS.md` §5), with `--watch` so it is Chrome-visible as Paul specified. | **required** | a lap |
| 10 | Promote the artifact to production. Parity gate green. Paul walks it. | **required** | — |
| — | **STOP.** That is the stopping point. | | |
| ✦ | rename `lab`→`dev`; retire `myhome-bob`; the `STAGE` var; runtime instance resolution (B5) | **nice / later** | — |

**Total: ten steps, roughly four working sessions, and steps 2–4 are the only ones that touch the
separation seam at all.** Nothing before step 10 requires the tenancy conversion.

---

## G · PAUL'S CALLS — three

1. ⭐ **N1 + N2 together, as one sentence:** *"Production ships the full app, built from its own
   instance, as the same artifact QA certified — and the feature delta is a flag, not an
   environment."* Yes or no. Everything in §F hangs on it.
2. **N3:** for a new household, is a domain **absent** (module not present) or **empty** (module
   present, no records)? Schema-shaped, so it wants answering once.
3. **Guru in production** — key it and flag it on, or declare it off. It is currently neither, which
   is why it 503s while declaring a $10 ceiling.

⭐ **Nothing else needs his decision.** The other nine questions from tonight are on §D list 2 and a
walk will answer them faster than he can.

## Principles to propose from the addendum (NOT added)

8. **Parity is a property of the ENVIRONMENT; promotion is a property of the ARTIFACT. Never one
   mechanism.** — cross-project. Conflating them is how "make QA match production" comes out
   backwards.
9. **If the environment is the feature flag, what QA proved is not what production runs.** —
   cross-project. One artifact everywhere; the delta is config.
10. **A capability turned off by a MISSING SECRET is an accidental feature flag** — unscopable,
    unrollbackable, and it reports as an outage instead of as *off*. — cross-project.
11. **Parity on a generative surface is parity of configuration and contract, never of output.** —
    cross-project. The deterministic shell gets equality gates; the probabilistic core gets invariants
    and thresholds, and must be able to report UNCHECKABLE.
12. **A declaration the build can silently ignore is not a declaration.** — fernwood, from B4·①.
13. **Answer before building only what changes an artifact's SHAPE or a schema. Everything that
    changes pixels, copy or ordering is cheaper to walk than to decide.** — cross-project. ⭐ Paul's
    own sorting rule, made explicit.
