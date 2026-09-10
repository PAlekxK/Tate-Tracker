# Readback: fernwood-multi-tenancy

<!-- written 2026-09-10 · receiver session · brief stamped Tate-Tracker@8edcc20, fernwood-private@ac1d414, origin/main@e9c9dac -->
<!-- REVISED 2026-09-10 after the outgoing session graded this readback and amended the brief at 8d17e4e. Two of my statements were corrected; both are marked ⛔ CORRECTED / ✅ ANSWERED in place rather than deleted. -->

> ### ⛔ Correction accepted — and the way I was wrong is the point
> I reported the condo backup *"not on disk"* after *"checking every session scratchpad"* and drew
> the stronger conclusion *"there is now no second copy of those four rows."* **False.** All four
> rows, plus `_rewritten.json` and `_put.json`, are at
> `/private/tmp/claude-501/-Users-paulkirschenbauer/aee5db3e-…/scratchpad/condo-backup/` — I have
> now `ls`'d them myself.
>
> **My glob covered one project's scratchpads** (`…-Developer-Tate-Tracker/*/`) **and I reported the
> result as if it covered the world.** The outgoing session ran from a different cwd, so its scratch
> lives under a different prefix entirely. That is this repo's own standing lesson, self-inflicted:
> **absence under a prefix is a fact about the prefix, not about the world** — the same shape as
> `watch-activity.py` printing *"no metrics batches"* for the busiest estate in the project.
> A search that comes back empty is a fact about the search until the search itself is checked.

## 0. Stamp verification — the brief is TRUSTWORTHY, with one caveat

| stamp | claimed | actual | verdict |
|---|---|---|---|
| Tate-Tracker | `8edcc20` | HEAD `e318358` | ✅ **one commit ahead, and that commit IS the brief** (`handoff/handoff-fernwood-multi-tenancy.md`, 92 insertions, 1 file). No code moved between the stamp and now. |
| fernwood-private | `ac1d414` | `ac1d414` | ✅ exact, tree clean |
| origin/main (legacy Pages) | `e9c9dac` | `e9c9dac` | ✅ exact |
| working tree | "clean, no uncommitted work" | clean | ✅ |

⚠️ **Caveat: line numbers in the brief have already drifted.** §3 step 3 cites `grantFor()` at
`worker/worker.js:1029`; it is at **:1058**. §2's `774-788` for `scopeOf`/`scopeFor`/`keyFor` is
correct. I am treating every line reference as approximate and re-grepping before touching anything.

**Counts in the plan re-verified against the code at HEAD, all three hold:**
`scopeOf(env)` = **60** · `scopeFor(...)` live call sites = **1** (`:3788`, result discarded;
`:3925` is a comment) · `keyFor(` = **35**.

---

## 1. What I understand the thread to be

Fernwood's Worker currently makes **an estate a deployment**: one Worker + one KV namespace + one
Pages origin + one `ESTATE_ID` binding per household. Isolation is real but it is achieved by
separating *hardware*, not by the code. Paul ruled on 2026-09-10 that an estate must instead be **a
row an owner creates** — a grant token buys you the right to establish your own estate, and the
constraint that must survive every step is *"no one should be able to see each other's estates
without the owner inviting them."*

The build is **adoption, not invention**, and two earlier decisions are why:
- `scopeFor(request, env, grant)` already exists and is already correct — written, never adopted.
- C5 6a already made every KV key `<estateId>:<kind>:<suffix>`, so one namespace can hold many
  estates safely. **The prefix IS the isolation.** Storage needs nothing.

Four changes: (1) a `credential:<sha256(token)> → {estateId}` **router row** so a credential can find
its estate without already knowing it; (2) `POST /api/estate`; (3) classify and convert the 60
`scopeOf(env)` sites; (4) demote `hostAgrees()`/`FAMILY_HOSTS` from tenancy to a CSRF-shaped control.

It dissolves three things rather than solving them: the Nigel/Aida Pages-project blocker (Cloudflare
merged Pages into Workers and refuses a project name a Worker owns — under this model no household
needs a Pages project at all), the Grant Park Condo migration, and the hostname derivation in
`onboarding/index.html`.

---

## 2. Current state, as I read it

- **Repo:** `main` @ `e318358`, clean. Register `fernwood-private` @ `ac1d414`, clean.
- **Eight environments, and this is the fact I think matters most for step 2 — eight SEPARATE KV
  namespaces.** `prod/legacy` `est-3c9f1a` (frozen) · `qa` `est-qa0001` · `lab` `est-lab0001` ·
  `home` `est-e6696a` (Mom) · `bob` `est-9a74df` · `paul` `est-d93508` (Grant Park Condo, moved
  today) · `nigel` `est-76012d` · `aida` `est-92e588`. Nigel and Aida are Workers + KV only, no
  Pages origin.
- **Nothing of this build exists yet.** `grep credential: worker/worker.js` finds only a prose
  comment; there is no router row, no `POST /api/estate`, no falsifier test. `grantFor()` is
  untouched and still does `keyFor(scopeOf(env), "grant", sha256(token))` then nulls any row whose
  `estateId !== env.ESTATE_ID`.
- **Release loop is open and stranded.** `release-state.py` reads *FIRED · beat 8/12 (the synthetic
  loop) · owner: session · candidate `ec88009` · seats pass: False*, and says plainly **HEAD
  `e318358` is not deployed** — the QA candidate is now **8 commits behind**. Gate ① is red.
- **Why gate ① is red is a ruling, not a bug** (`0cf2418`, 2026-09-08): every fresh walk in this
  project's history was an existing person shown a signup form by a device-local cache. Paul ruled
  the remedy (an unspent invite per fresh run) is **carried to `BACKLOG § SPLIT THE JOURNEY FROM THE
  READER`**, not patched into `journey-walk.py`, and recorded the consequence rather than softening
  it: *"gate ① does not go green this lap."*
- **Mom's and Bob's invites went out this afternoon.** As of the stamp, neither grant was spent —
  **nobody has ever completed a signup on any household estate.** Both are gate 1 on an unwalked
  path, and Paul chose to send anyway, knowingly.
- ⛔ **CORRECTED — the condo backup EXISTS.** (I had reported it gone; see the correction note at
  the top.) Four rows + `_rewritten.json` + `_put.json` at
  `…/-Users-paulkirschenbauer/aee5db3e-…/scratchpad/condo-backup/`. It is **session scratch and will
  vanish** — so the actionable item stands, just not the alarming version of it: **if a durable
  second copy is wanted, copy it somewhere real.** Byte-parity was verified before the delete, so
  nothing is currently lost either way.

---

## 3. The open decision

**As the brief states it, one:** plan **step 5 — the migration** (Grant Park Condo back to
production, Bob off `myhome-bob`, retire the per-household envs, Nigel and Aida never get one). It is
the only irreversible step and it is explicitly *"Paul's call, not a consequence of 1–4."*

**I think there are three more that are live and the brief does not frame as decisions:**

1. **Does the release loop close before or after this build?** Paul chose to start multi-tenancy with
   lap 5 open at beat 8. §7 says the open door *probably* turns gate ① green cheaply. If that is
   true, closing lap 5 first costs little and un-strands a candidate that is drifting further behind
   HEAD with each commit. If it is false, multi-tenancy work makes `ec88009` harder to certify, not
   easier. **I would want this ruled before I start, because it changes what I do first.**
2. **Does Paul keep an administrator row on Mom's estate?** §8 flags `p-paul @ est-e6696a` present in
   the register with **no matching grant in the store**. See §5.1 — under this build that divergence
   stops being cosmetic.
3. **Who mints?** See §5.3. `POST /api/estate` makes the Worker a second writer of a store that
   `grant-mint.py` currently declares itself the sole writer of. That is a model decision, not an
   implementation detail.

---

## 4. What has NOT been tested or verified

**By the outgoing session's own accounting (§8), flagged and NOT cleared:**
- The `door_failed` on Bob's estate at `2026-09-10T15:41:16Z` (`unknown-or-other-estate`,
  `serverSide: true`, `deviceId: null`) being self-inflicted — **timing evidence only.** If it
  recurs after Bob clicks, that is the *"you have no homes"* failure and it is urgent.
- That the open door turns gate ① green — **never run.**
- The `p-paul @ est-e6696a` register row.
- Nigel/Aida Pages origins being impossible (confirmed twice via wrangler, both orderings).

**Additionally, and these are mine:**
- **The falsifier does not exist.** Until it does, *deployment separation is the only thing holding
  the 2026-09-10 rule up.* Everything in §8's "verified by use" row for cross-estate isolation is
  verified for **the current model**, not the target one.
- ✅ **ANSWERED by the amended brief (field 4) — this is no longer open.** `/health` returns
  `build_sha: null` on every environment, so **no origin can answer this**; it existed only in the
  outgoing session's context and is now on disk. **Seven Workers carry `worker.js` @ `36c82bf`**
  (open door + widened capability gate): `home` · `bob` · `paul` · `qa` · `lab` · `nigel` · `aida`.
  ⛔ **`legacy`/production (`est-3c9f1a`) was deliberately NOT redeployed — it is the frozen data
  control**, verified by use at handoff (`POST /api/account` → `401`, older than the account
  carve-out). **Leave it frozen.**
  ⚠️ Note the residual: `build_sha: null` means **this fact is un-re-derivable from any origin.** If
  it drifts, nothing will say so. That is a small instrument gap worth naming, not fixing today.
- **I ran no live probe.** Not `watch-accounts.py`, not `watch-door.py`, not `release-gate.py` —
  because "confirm Mom and Bob are through the door" **is step 1 of the work**, and you said not to
  start. Consequence to state plainly: **the single fact that gates step 3 is unknown to me right
  now, and could have changed since the stamp.** It is the first thing I will run.
- I did **not** run the CLAUDE.md session-start block. This is a resumed thread, not a Fernwood
  pickup, and the block is ~40 tools deep. Say the word if you want it.

---

## 5. What looks thin, or that I am unsure of

### 5.1 The backfill is per-namespace × 8, and the brief reads as one sweep
Brief step 2 says *"iterate `<estate>:grant:<hash>` and write `credential:<hash>`. No token needed."*
The mechanism is right — the key suffix **is** the hash, so no token is recoverable or needed. But
the router row is **deployment-scoped**, and today "deployment" means **one of eight distinct KV
namespaces**. So:
- The backfill must run **once per namespace**, and a router row written in namespace A **cannot
  find a grant living in namespace B**.
- Which means **migration is not just retiring envs** — it is **copying grant rows across
  namespaces** into production's store before the router can route them. The plan's step 5 implies
  this; neither document says it out loud, and it is the part that touches live credentials.
- And **the backfill iterates the STORE**, so a **register-only row — exactly `p-paul @ est-e6696a`
  — gets no router row and is silently not covered.** That is the same shape as the `⚡ DIVERGENT`
  reading CLAUDE.md already records (345 rows at qa; `p-paul` live in the register and absent from
  production's store, which answers `unknown-or-other-estate` at the door and renders as *"you have
  no homes"*). **It is also the same reason code as Bob's unexplained `door_failed`.** I am not
  claiming they are the same incident — but I would not treat that flag as cosmetic while building
  the thing that reads that store.

### 5.2 `credential` is now two things
`grant-mint.py:15` documents a **field inside the grant row**: `credential: {hash, issuedAt,
issuedBy, revokedAt}`. The plan proposes a **KV key** `credential:<sha256(token)>`. Same word, two
referents, one repo — which is the double-booking VOCABULARY.md exists to catch (`group` is the
standing example). Worth a different key noun before it is written 60 times.

### 5.3 `POST /api/estate` makes the Worker a second minter — and the gates are in Python
`grant-mint.py` calls itself *"the ONE writer of the grant register and the KV grant store,"* and it
enforces two gates **at the mint**, per `[paul-ruled 2026-09-03]` *"no watcher; enforce at the mint"*:
- **G1** — a founding owner grant needs a `founding-request` consent entry whose `agreedBy` **is** the
  person.
- **G2** — where the administrator holds no relationship, a non-administrator grant needs an
  `administrator-reads` consent entry. Its own docstring says **the discriminator is a field Paul
  writes, and there is no check that can be.**

A server-side `POST /api/estate` either re-implements both gates in JS, or bypasses them. And either
way it **writes a grant the local register does not know about** — structurally guaranteeing the
`⚡ DIVERGENT` condition. The plan does not mention consent, `grants.json`, or G1/G2 at all. **This is
the thinnest part of the plan and it is change #2, not a corner.**

### 5.4 The 60 call sites are counted but not classified
The plan names four that legitimately mean the deployment (`/health`, `env-canary`, the digest guard,
the chat budget) and says the rest are *"each one a decision."* That classification is the real work
of change #3 and **none of it is done**. I would produce the classified inventory as a reviewable
artifact *before* converting anything, so the batches are auditable rather than trust-me.

### 5.5 Change #4 is stated as a demotion but not specified
*"`hostAgrees()` becomes an ordinary CSRF-shaped control"* — but with one origin serving everyone,
what `FAMILY_HOSTS` should contain, and whether a no-Origin request still agrees vacuously, is
unspecified. Small, but it is a security control and it should not be decided incidentally mid-batch.

### 5.6 One thing I could not reconcile
Brief §7 says the open door means fresh walks *"no longer need"* an unspent invite — which would
partly dissolve the 09-08 carried ruling. But that ruling explicitly routed the fix to the backlog
because *"the three-axis redesign dissolves the defect and patching first hardens the unit it
replaces."* **Is the open door that dissolution arriving early, or a second path to the same
symptom that leaves the axis question open?** The brief treats it as the former and marks it
unproven. I do not have enough to tell, and it bears directly on §3 decision 1.

---

## 6. What I would do next (ordered, nothing started)

0. **Ask you decision 1** (close lap 5 first, or push through). Cheap, and it reorders everything below.
1. `python3 tools/watch-accounts.py` — are Mom and Bob through the door. **Read the `⚡ DIVERGENT`
   rows**, not just the arrival counts. `python3 tools/watch-door.py` for the Bob `door_failed`.
   ⚠️ `--remote` on every `wrangler kv` call; a bare `key list` returns `[]` and reads as an empty estate.
2. Establish **what sha each of the eight Workers is serving**, since I cannot tell from disk.
3. If §7's cheap close is real: run the walk battery, see whether gate ① goes green, close lap 5.
4. Write the **backfill** — per-namespace, dry-run first, reporting store-vs-register divergence per
   estate rather than a bare count. Backfill is safe to run **before** `grantFor()` changes, and I
   would land and verify it as its own commit while Mom and Bob are still walking in.
5. Only once §3 decision 3 is ruled: `grantFor()` router read, then the falsifier on `lab`, then the
   classified 60-site inventory.

**Guardrails I have taken on board:** don't set `CANON_FOREIGN_OK=true` to "fix" Garden Guru (it
would feed Fernwood's canon into Bob's estate; the real fix is a per-estate digest and per-env
bundling). Don't flatten grant keys. `pages-deploy.py --env home` is behind red gate ①. Commit
messages via `-F -` with a quoted heredoc; stage explicit paths, never `git add -A`.

---

## 7. Bottom line

The brief is accurate, well-stamped, and its judgment calls are labelled as judgment. My four
substantive additions are: **the backfill is eight namespaces, not one, and skips register-only rows
like `p-paul`** (§5.1); **`POST /api/estate` collides with grant-mint's sole-writer claim and its two
consent gates, and the plan is silent on it** (§5.3); **`credential` is about to be double-booked**
(§5.2); and **the release-loop question is a live decision, not just context** (§3.1).

**Post-grade status:** the brief is amended at `8d17e4e` and I have read it. All four findings
above are folded into its field 7 and will survive this window. My one factual error (the condo
backup) is corrected in place. `release-state` still reads beat 8/12 · candidate `ec88009` · gate ①
red, so §3 decision 1 is unchanged and still the one I would put to you first.

Not starting. Waiting on you.
