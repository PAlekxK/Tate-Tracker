# ENVIRONMENTS, ESTATES AND ROLES — the operating model · DESIGN

- row: process (no `BACKLOG.md` row — same posture as the 09-04 wiring audit and the 09-06/09-07 audits)
- objective: **O3** (the engine transfers to a second estate without a fork) · **O5** (the loops are the artifact)
- class: **engine · declared** — process machinery. ⛔ Nothing here ranks a feature, a module or an item.
- seats: practice-steward (this file)
  - engineering-partner → owed at any build: every mechanism named in §7 is described, none is designed here
  - content-steward → owed for the *reader-facing* half of §5 only if a Pages hostname changes; the `--env`
    flag is not a user-facing surface and `VOCABULARY.md` §2 keeps `estate` off one
  - ux-expert · user-researcher · ai-advisor → waived: no surface, no person and no model sits on any path in this file
- depends-on: `.plans/2026-09-07-review-gate-to-qa-DESIGN.md` (§4 proposed four of these renames; this
  supersedes its §4 **only** by costing them and by adding the axis split it did not see)
- depends-on: `.plans/2026-09-07-qa-access-DECISION.md` · `.plans/2026-09-08-setup-journey-PLAN.md` ·
  `cycle/release/CYCLE-MAP.md` · `VOCABULARY.md`
- ready: **agent-proposed 2026-09-08 — Paul rules.** ⛔ Nothing in § Sequence starts.
- stage: concept
- stage-note: 2026-09-08 — written read-only at HEAD `13b98a4`. No tracked file outside `.plans/` and
  `.practice/` was edited; nothing deployed; nothing minted; no `--confirm` anywhere.

> **Method only.** Every claim is tagged `measured` · `inferred` · `proposed`. Where a call turns on
> real-world context only Paul holds — whose home is whose, what a record is worth, who may read whom —
> it is named and declined (§8). ⛔ **This file contains no address and no person's data**; the repo is
> public and two of the measured records below are Paul's own.

---

## 0 · FOR PAUL — the answer in eight lines

1. ⭐ **Your model is right, and it is not expressible in the flag you have.** `--env` is one word doing
   **two jobs**: a **RUNG** (dev → qa → production — a property of the *artifact*, and the thing that can
   be promoted) and a **HOME** (one estate's store, credentials and origin — a property of a *place*).
   All six deployments pin both at once. *"My production home **and** my QA home"* is **one PLACE at two
   rungs**, and the flag has no way to say that. §1. ⭐ **Amended by §10:** under the Q1 ruling that is
   **two homes**, deliberately — *"I understand they won't be quite the same."*
2. **So the renames are necessary and not sufficient.** Calling `home` `production` makes the word true
   and leaves the axis collapsed. Do them — but do not expect them to deliver the model. §5.
3. ⛔ **"Nothing reaches production without QA" is not enforced today, in three separate ways**, and one
   of them is that **two of the three production origins have no gate at all**. §3.
4. ⛔ **You already hold both roles — six times over — and nothing records which row is which.**
   `measured`: the access map shows **six person rows that are you**, across four estates, with ad-hoc
   ids (`p-7f3a2c` · `p-paul` · `p-paul-home` · `p-paul-qa` · `p-paul-qa2` · `p-paul-qa3`). §4.1.
5. ⭐ **The QA home you are asking for half-exists, and it is co-owned.** `measured`: every account in
   QA is an **owner of the same single estate** `est-qa0001` — you and twelve synthetic walkers. A
   "home" in QA is not a home; it is a shared room. §4.2.
6. ⛔ **Your real records have already disarmed QA's reset.** `reset-production-estate.py` aborts the
   whole run on one `real` record, and QA now holds four. The environment whose job is to be
   reconstructible is currently not resettable. §4.3.
7. ⭐ **D5 forces the axis split whether or not you take this design.** `measured`: `grantFor()` binds
   every credential to `env.ESTATE_ID`; `scopeOf(env)` has **59 call sites** and `scopeFor(request,…)`
   has **one, whose result is discarded**. Multiple homes per account cannot exist while the estate
   comes from the deployment. §1.3.
8. ⭐ **One decision unlocks the rest and it is yours:** *when one place exists at two rungs, is it the
   **same estate id** or a different one?* Your corpus contains both answers, ruled eleven hours apart,
   in the same file. §8 · Q1.
9. ⭐ **Your four tier definitions land cleanly, and one of them retires a contradiction for free.**
   Naming `dev` *a playground* — rather than *"Fernwood dev"* `[paul-ruled 2026-09-05]` — removes the
   only reason dev ever wanted Fernwood's estate id, which is what broke G3. §2.2.
10. ⛔ **`legacy` is the tier with the real work in it, and *"unpublished"* and *"a data reference point"*
    are two separate builds, neither of which exists.** Unpublishing has a **prerequisite that expires**
    (her outbox), and the reference point is **6.03 MB in a gitignored directory with no reader**. §2.3.

---

## 1 · THE MODEL

### 1.1 · What exists today — measured, from `worker/wrangler.toml` at HEAD `13b98a4`

| `--env` | `ENV_NAME` | estate id | KV namespace | worker name | Pages project | origin |
|---|---|---|---|---|---|---|
| *(top level)* | `production` | `est-3c9f1a` | `100f2b95…` | `fernwood` | — (GitHub Pages, `origin/main`) | `palekxk.github.io/Tate-Tracker/viewer.html` |
| `qa` | `qa` | `est-qa0001` | `a0cf82b6…` | `fernwood-qa` (derived) | `fernwood-qa` | `fernwood-qa.pages.dev` |
| `lab` | `lab` | `est-lab0001` | `1e0bd883…` | `fernwood-lab` (derived) | `fernwood-lab` | `fernwood-lab.pages.dev` |
| `home` | `home` | `est-e6696a` | `79464451…` | `fernwood-home` (derived) | `fernwood-home` | `fernwood-home.pages.dev` |
| `bob` | `bob` | `est-9a74df` | `22250ace…` | `myhome-bob` (**pinned**) | `myhome-bob` | `myhome-bob.pages.dev` |
| `paul` | `paul` | `est-d93508` | `e752e1c3…` | `myhome-paul` (**pinned**) | `myhome-paul` | `myhome-paul.pages.dev` |

`measured`: `bob` and `paul` **pin `name =`** inside their env block; `qa`, `lab` and `home` let wrangler
derive it from `<top-level name>-<env>`. **That asymmetry is the single most useful fact in §5** — it is
what decides whether a rename is bookkeeping or a migration.

### 1.2 · The two axes the flag is holding at once

> **RUNG** — *how far along the way to a person is this artifact?* `dev` → `qa` → `production`.
> A property of the **build**. It is the thing that gets **promoted**, and it is what you mean by
> *"production is just production."*
>
> **HOME** — *whose place is this, and where does its record live?* One estate id, one KV namespace,
> one credential space, one origin. A property of the **place**. It is never promoted; it **persists**.

`measured`, and this is the whole finding: **every row in §1.1 fixes both coordinates simultaneously.**
Consequences that follow mechanically, not by opinion:

| because the axes are one flag | consequence, measured |
|---|---|
| a rung holds exactly one estate | QA is **one** estate. 12 synthetic owners + you are all `est-qa0001` |
| a home exists at exactly one rung | *"my production home and my QA home"* **cannot be named** — they are two estates that happen to be the same person's place, and nothing in the system says so |
| the word `production` is a deployment | it can be **held** by one deployment and is therefore contested. `wrangler.toml:112` — *"`production` is a ROLE that transfers… and the frozen Fernwood held it"* |
| an env name is both a tier and a tenant | `HOUSEHOLD = {"bob","paul","home","qa"}` in `pages-deploy.py:66` must **hand-list** which envs are tenants, and its own comment says getting it wrong *"moves the leak rather than fixing it"* |

⭐ **Your sentence *"production is just production"* is precisely the request to split them.** A tier is a
word about artifacts. Today it is a word about a deployment, which is why it reads as *"a clean slate for
someone."*

### 1.3 · D5 forces the split anyway — so this is not an optional refactor

`[paul-ruled 2026-09-08, D5]` — *multiple homes per account, this lap.*

`measured`, `worker/worker.js`:

- `grantFor()` **:1004** — `if (!row || row.estateId !== env.ESTATE_ID || row.revokedAt) return null;`
  Every credential is nulled unless its estate equals the **deployment binding**.
- `scopeOf(env)` **:713** — *"The DEPLOYMENT's scope. ⛔ The only function in this file that reads
  `ESTATE_ID`."* **59 call sites.**
- `scopeFor(request, env, grant)` **:719** — the per-request resolver that would replace it.
  **One call site (`:3716`), and its result is assigned to a variable marked
  `eslint-disable-line no-unused-vars`.** The multi-home path is scaffolded and dead.

⚠️ `wrangler.toml`'s own estimate — *"`scopeFor()` wired through its **~30** call sites"* — is
`measured` **wrong by 2×** at HEAD. It is 59. That number is load-bearing because it is what anyone
sizing D5 will read.

⭐ **So D5 and this design are the same work.** The moment a person can hold two homes, the estate must
come from the **request**, not the **binding** — and once the estate no longer comes from the binding,
`--env` stops being a tenant noun and becomes a rung. **The ask you made minutes ago and the ruling you
made this morning converge on one change.**

### 1.4 · The target model, stated as a rule

> **A deployment is a (RUNG × HOME) pair. The rung is declared by the deployment; the home is resolved
> per request from the grant. Renaming a rung never moves a record; adding a home never adds a rung.**

`proposed`. Under it, your ask reads cleanly:

- `production` is a rung. Nothing reaches it that has not exited the QA rung's loop.
- **End users exist only at the production rung.** Mom, Bob and their people have grants there and nowhere else.
- **You exist at two rungs**, as **two person rows that both know they are you** (§4.4) — an owner in
  your production home, and an owner in a QA home that is *yours* and not the harness's.
  ⭐ **Under §10 those are TWO ESTATES, not one estate seen twice**, and they are expected to diverge.
- **Synthetics exist only at the QA and dev rungs**, which restates `CYCLE-MAP.md:182` without changing it.
- ⭐ **`legacy` is a fourth rung and it is not on the promotion path at all** — nothing is ever promoted
  *to* it, and nothing is promoted *from* it. It is a terminus. §2.3.

---

## 2 · THE MAP

```
        ┌───────────────────────── HOMES (estates — persist, never promoted) ────────────────────────┐
        │                                                                                            │
        │   Fernwood        Mom's new home     Bob's home       Paul's home     the harness's home    │
        │   (legacy)                                                                                 │
────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
 dev    │      ●  est-lab0001                                        ○ owed        ●  synthetics      │   Paul + Claude
        │      `lab`                                                                                  │   no real person, ever
────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
 qa     │      ○ owed                                            ⭐ ASKED FOR      ●  est-qa0001      │   synthetics walk
        │   (canon-bearing)                                       (Paul as an      12 synth owners    │   Paul walks as an END USER
        │                                                          end user)       + Paul's 4 real    │
────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
 prod   │      ⛔ NOT HERE     ●  est-e6696a    ●  est-9a74df    ●  est-d93508          ⛔ never      │   real people only
        │      (see below)     `home`           `bob`            `paul`                                │   ⛔ no synthetic
        │                      4 owner grants,  0 grants —        contested:                           │
        │                      3 are not Mom    unreachable       "his own home" vs "an ARTIFICIAL rig"│
────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
 legacy │      ●  est-3c9f1a                                                                           │   ⛔ a TERMINUS —
        │      TOP LEVEL, ENV_NAME = "production"  ← the word is here, on the thing being unpublished   │   nothing in, nothing out
        │      175 KV keys · Mom is using it TODAY · GitHub Pages from `origin/main`                    │
────────┴────────────────────────────────────────────────────────────────────────────────────────────┘
             ▲                                        ▲
             │  the word `production` is held here    │  and claimed here (`home`)
             └────────── the collision, in one picture ─────────────┘

⭐ **The picture is the argument for N1.** The only cell carrying the string `production` is the one on
the legacy rung, and it is the one deployment that will never be on the promotion path again.

PROMOTION runs DOWN a column only in the sense that an ARTIFACT moves dev → qa → prod.
A RECORD never moves. A HOME never changes rung. Today the diagram has no cells, only points,
because a point is all one flag can name.
```

`measured` for every filled cell (`wrangler.toml`, `tools/access-map.py` output at HEAD). `○ owed` = a
cell the model implies and nothing declares.

### 2.1 · What may be written where

| rung | who writes | what is written | may it be deleted? |
|---|---|---|---|
| **dev** | Paul + agents | anything | yes, freely |
| **qa** | synthetic walkers **and Paul as an end user** | real form input from Paul, synthetic input from seats | ⛔ **not today** — §4.3 |
| **production** | real people | their record | ⛔ `reset-production-estate.py` aborts on one real record, by design |
| **legacy** | ⛔ **nobody** — after the sunset, nothing writes | 175 KV keys, eight months of Mom | ⛔ never. It is the reference point (§2.3) |

---

### 2.2 · ⭐ THE FOUR TIERS — Paul's own definitions `[paul-stated 2026-09-08]`

> *"dev is just a playground for us to try things, prove things, test errors… And then legacy is the old
> Fernwood that is going to be unpublished. So it's not publicly available, but we will keep it as a data
> reference point."*

| rung | what it is, in his words | who is in it | gate on entry | may it be reset? |
|---|---|---|---|---|
| **dev** | *a playground — try things, prove things, test errors* | Paul + agents. ⛔ no real person, ever | none | ✅ freely |
| **qa** | Paul tests **as an end user**; synthetics walk | Paul (end-user seat) + the harness | none | ⛔ **not today** — §4.3 |
| **production** | real people only | Mom · Bob · Paul's own home | ⭐ **gate ① + `cleared_sha`** — and only at one of three origins (§3.2) | ⛔ never, by design |
| **legacy** | *the old Fernwood — unpublished, kept as a data reference point* | Mom, today, live | ⛔ **nothing enters** | ⛔ never — it **is** the record |

⭐ **`dev` as a PLAYGROUND retires a live contradiction, and this is the one free win in the file.**
`wrangler.toml:64-72` carries *"⭐ FERNWOOD DEV `[paul-ruled 2026-09-05]`: we should have a Fernwood dev,
qa, and production"* — and it is that framing, *dev is Fernwood at the dev rung*, that made dev want
`est-3c9f1a` and **broke G3** (`:66-72`: *"THE CHECK CAN NEVER FIRE"*). It was reverted to `est-lab0001`
hours later as a safety call (`:80-87`, `paul-approved`), which left **two rulings in one file with the
weaker one winning on merit rather than on record.**

> ⚠️ **AMENDED BY §10.7·W1 — this paragraph credits the tier definition for what the Q1 ruling now does
> generally. Read it as history.** Tonight's words settle it for dev: **a playground has no reason to be
> Fernwood.** `est-lab0001` stops being a
> safety override and becomes the ruled answer. ⛔ ~~`estate_agrees()` is not repaired by this~~ — ⭐ **it IS repaired, by the
> Q1 ruling: §10.3.** The hypothetical this sentence warned about is now closed by rule.

⚠️ **What it does NOT change: `CANON_FOREIGN_OK`.** `dev` and `qa` both declare `CANON_FOREIGN_OK = "true"`
on the stated grounds that they *"ARE Fernwood"* (`wrangler.toml`, qa and lab blocks). ⭐ **That premise
has now moved for both of them** — dev is a playground, and qa is where you sit as a condo owner with your
real address. See B10.

---

### 2.3 · ⛔ THE LEGACY TIER — two builds, neither of which exists

*"Unpublished"* and *"a data reference point"* are **two separate capabilities**, and the record says
neither is in hand.

#### 2.3.1 · Does the sunset ORDER still hold under four tiers? — **yes, unchanged, and it is the strongest thing here**

`measured`, `BACKLOG.md:259-265` `[paul-stated 2026-09-06]`:

> drain her device *during the visit* → re-archive + `--verify` → rotate `SHARED_TOKEN` (**that is the
> actual lockout**) → tag the sha → disable Pages (**never edit `main`**) → stop the bots

Nothing in the four-tier model touches it, because the order is not about environments — it is about
**one prerequisite that expires**. `measured`, `BACKLOG.md:261-263`: `tateTracker.feedbackOutbox.v1`,
`tateTracker.door.outbox.v1` and four `momQueue.*` keys **exist nowhere but her phone** until they flush
(`viewer.html:11552` holds them until a 2xx), **and no new surface reads any `tateTracker.*` key.**

> ⭐ **So the first step of the sunset is not a lockout, it is a drain — and rotating `SHARED_TOKEN`
> before it strands those records permanently, with no error anywhere.** *"One phone tap while online,
> before lockout, is the difference between a sunset and a silent deletion."*

⛔ **This is CRITICAL in my lane and I am stating it unprompted, with the measurement attached:** the
sunset's steps are **ordered by an irreversible dependency**, and the step that *feels* like the sunset
(rotate the token) is the one that must come **third**. It stays true with the business value of every
record set to zero — it is a statement about a write path that has no retry after the credential moves.
⛔ It is **not** a claim that the sunset outranks anything else on your board.

⚠️ **One dependency the order does not state and the four-tier model makes visible:** the drain happens
*during the visit*, and the visit is when she founds her production home. **So legacy's sunset is gated on
production having a real owner** — which `BACKLOG.md:342` already says (*"everything gated on her getting
her link to set up in prod"*) and which `reset-production-estate.py`'s `real` abort is the named signal for.

#### 2.3.2 · What "unpublished" means mechanically — three different acts, and only one of them is in the order

`measured` where marked; `inferred` where marked.

| act | what it stops | what it does **not** stop | in the sunset order? |
|---|---|---|---|
| **rotate `SHARED_TOKEN`** | every write and every authenticated read to the frozen Worker | the page loading | ✅ step 3 — *"the actual lockout"* |
| **disable GitHub Pages** | `palekxk.github.io/Tate-Tracker/viewer.html` serving | ⚠️ **a copy already cached on her phone** — `CLAUDE.md` § "A COMMIT IS NOT A SHIP" measures exactly this: *"a phone can still serve a cached copy long after Pages is correct"* | ✅ step 5 |
| **make the repo private** | `github.com/…/blob/main/viewer.html` being publicly readable | — | ⛔ **not in the order, and it is a different act with different blast radius** |

⭐ **The honest reading, and it is worth one sentence to you: with Pages disabled and the repo public,
the app is unpublished and the FILE is not.** `viewer.html` on `origin/main` stays readable to anyone with
the URL. Whether that satisfies *"not publicly available"* is your call (§8·Q6) — ⛔ and taking the repo
private is **not** a bookkeeping move: `inferred`, GitHub Pages on a private repo requires a paid plan,
and this repo is the engine's home, referenced by tools and by `raw.githubusercontent` paths. **I decline
the choice and cost both.**

⚠️ **And a cached app against a rotated token is the failure mode her surfaces exist to prevent.** The app
would load, look normal, and fail every write. `CLAUDE.md`'s standing rule is *capture must not lie*.
⭐ **The cheapest honest answer already exists and shipped**: the sunset banner (`e0746c5`, `517e597`,
`edfff1c` on `origin/main`, 09-07). **`measured`: the banner is on the branch it needs to be on.**

#### 2.3.3 · ⛔ "A data reference point" is not a capability today — three measured gaps

| # | gap | `measured` |
|---|---|---|
| **L1** | ⭐ **no restore tool exists, and the archive tool says it never will** | `archive-frozen-estate.py:19-21`: *"READ-ONLY BY CONSTRUCTION. This tool has no delete path and never will. If you want one, that is a different tool."* Verified by two methods: `ls tools/ \| grep -i restore` → **nothing**; `grep -rln restore tools/*.py` → six files, **none an estate restore** (build-control, check-digest-fresh, harvest-questions, journey-walk, test-feedback-cycle, watch-feedback, all other senses) |
| **L2** | ⭐ **the archive has no READER either — not a restore, a *read***. A 6.03 MB JSON blob of raw KV values is a *stored file*, not a reference point. Nothing renders it, queries it, or diffs it against the new instance | `.private/frozen-fernwood-archive/frozen-2026-09-06T000836.json`, **6,033,721 bytes**, `keyCount: 175`, `unreadable: []`. `grep -rn frozen-fernwood-archive tools/` → written by one tool, read by that same tool's `--verify` and by nothing else |
| **L3** | ⛔ **the only copy is in a gitignored directory** — `.gitignore:5` is `.private/`, correctly, under the AI boundary's QUARANTINE clause (her words, public repo). **So no git-based backup carries it.** Whether any other backup does is `unknown`, and ⛔ **unknown is never counted as healthy** | two archive files, both `2026-09-06`, both local |

⭐ **And the reference point is already stale, by the record's own count.** `BACKLOG.md:348`, `measured`
2026-09-07: **177 live keys vs 175 archived · 0 changed · 2 gone (TTL) · 4 added** — *"the archive is one
feedback arrival behind and nothing re-takes it."* The re-take is step 2 of the sunset order, so this is
handled **only if the order is executed**; there is no standing control.

> #### ⭐ What would have to be true for *"a data reference point"* to be a real capability
> `proposed`, three things, smallest first:
> 1. **A READER** — one tool that answers questions of the archive (*what did she say about X · what did
>    the map look like · what changed between the archive and the new instance*). Without it, L2 stands
>    however good the archive is.
> 2. **A second copy, off this laptop**, satisfying the quarantine clause. ⛔ The destination is a
>    judgement about her words and it is yours (§8·Q7); `CLAUDE.md` already names local `.bundle` and the
>    iCloud bare repo as the sanctioned local backup path, and ⛔ **a bare git repo does not carry a
>    gitignored file**, so that path does **not** cover this today.
> 3. **A freshness control** — the archive's own `takenAt` against the live key count, read somewhere a
>    human looks. ⚠️ **It must be counted, never graded**: an archive of a frozen estate that gains a
>    metrics key a day would be permanently red, which is the one control this project refuses to build.
>
> **Falsifier:** *if nobody asks the archive a question in the ninety days after the sunset, L1 and L2
> were not gaps and the file alone was the right answer.* ⛔ **It is a BUILD, not bookkeeping** — and
> whether it is worth building is a value call I decline (§8·Q7).

#### 2.3.4 · ⚠️ A correction to how this was described to me — and it matters for scoping

The brief that reached me said *"171 of 175 **localStorage** keys are legacy unprefixed."* **The record
says KV, not localStorage**, and the two differ by an order of magnitude:

| | count | source |
|---|---|---|
| **KV keys in `est-3c9f1a`** | **175 — 4 prefixed `est-3c9f1a:`, 171 unprefixed** | `measured` two ways: the archive dump (91 `metrics:`, 35 `conversation:`, 22 `cost-log:`, 10 `feedback:`, 9 `zone-audio*`, …) and `BACKLOG.md:257,265` |
| **browser-storage keys** | **19 rostered · 18 distinct literals in use** | `measured`: `python3 tools/check-storage-keys.py` |

⭐ **Both facts are real and they are different facts.** The 171/175 unprefixed split is why *only*
`archive-frozen-estate.py` can see the frozen estate (prefix-scoped enumeration finds 4). The
localStorage story is the **six unflushed keys on her phone** in §2.3.1. ⛔ **Conflating them would size
the drain against the wrong number** — this repo's named failure of measuring a proxy and reporting the
target.

---

## 3 · PROMOTION — what "nothing reaches production without QA" means, and what enforces it

### 3.1 · What is enforced today, mechanically

`measured`, `tools/pages-deploy.py:271-311` — **inside `if a.env == "home":` and nowhere else**:

1. `release-gate.py --sha <sha> --seats-only` must pass — every seat walked **this** sha, `watched: true`,
   read its own report, zero failed actions;
2. `cycle-state.json → last_lap.cleared_sha` must **equal this sha**, and an unreadable or empty value
   **refuses** (fail-closed).

That is a real gate and it is the strongest thing in the loop. Three holes, each `measured`:

### 3.2 · ⛔ HOLE 1 — two of the three production origins have no gate at all

The gate block is guarded by `a.env == "home"`. `pages-deploy.py --env bob` and `--env paul` run the
household prune, the neutrality falsifier and the headless load — and **never call `release-gate` and
never read `cleared_sha`.** Under your model those two *are* production. So *"nothing reaches production
without being tested by QA"* is enforced for one of three production origins.

⭐ **This is the cheapest fix in the file and it is one condition**, not a design: the gate is keyed on a
deployment name where it means to be keyed on a **rung**. It is the same defect as §1.2 in miniature.

### 3.3 · ⛔ HOLE 2 — nothing says the walk happened in QA

`measured`, verified by two methods (clause table read at `tools/release-gate.py:190-205`, plus
`grep -n "env\|origin\|qa" tools/release-gate.py` returning no environment clause): gate ①'s clauses are
**at-sha · watched · countable · no-failed-actions · not-rate-limited**. **None of them asks where.** A
battery walked at `lab`, or at `home` itself, satisfies gate ① byte-identically to one walked at QA.

`.plans/2026-09-07-review-gate-to-qa-DESIGN.md` §7 already named this as owed (`D3`, *a `walked-in-qa`
clause*). It is still owed. `measured`: `grep -c walked-in-qa tools/release-gate.py` → **0**.

### 3.4 · ⛔ HOLE 3 — QA has two build paths and they produce different origins

This is the one I would put in front of you first, and it is `measured` to the byte.

| path | what it ships to `fernwood-qa` |
|---|---|
| `tools/pages-deploy.py --env qa` | prunes to `HOUSEHOLD_ALLOW`, tombstones every removed path, replaces `index.html`, **rebuilds `viewer.html` from `instance/qa.json`**, runs the neutrality falsifier, loads it headless, refuses on any page error |
| `.github/workflows/deploy-worker-qa.yml:105-136` — **on every push to `staging`** | `git archive HEAD` → `wrangler pages deploy … --branch staging`. **No prune. No tombstone. No `index.html` replacement. No `build-viewer`. No neutrality check. No headless load.** |

**Both write the same Pages project on the same branch. Last deploy wins.**

`measured` today, and the numbers are exact:

- tracked `viewer.html` = **2,216,135 bytes**, **12** occurrences of the property's road name;
- `build-viewer.py --instance instance/qa.json` = **1,203,913 bytes**;
- `https://fernwood-qa.pages.dev/viewer.html` right now = **1,203,913 bytes**, `qa-build.json` says
  `builtBy: tools/pages-deploy.py`, sha `13b98a4`, **10:57 ET**;
- `origin/staging` last moved **09:35 ET today**. The hand deploy won by 82 minutes.

⭐ **CRITICAL, IN MY OWN LANE, WITH THE MEASUREMENT ATTACHED:** *the next push to `origin/staging`
replaces the QA origin's 1,203,913-byte neutral build with the 2,216,135-byte Fernwood build and
un-tombstones every pruned path — including `onboarding/invite-message.md`, whose own first line reads
"Nothing here has been sent."* This is a statement about two code paths writing one origin; it stays true
with the business value of every affected item set to zero, which is the test that keeps it out of
ranking. ⛔ **I am not saying it matters more than anything else on your board.**

⚠️ **And the CI's own verification step depends on the un-pruned build.** `deploy-worker-qa.yml:145-150`
runs `check-live.py --base $QA_PAGES_URL`, which asserts the origin's `viewer.html` is **byte-identical
to `HEAD:viewer.html`**. Under `pages-deploy.py` it never can be — QA's is rebuilt. **So the two paths do
not merely differ; each one falsifies the other's check.** `measured`.

### 3.5 · What "nothing reaches production without QA" would take, mechanically

`proposed`. Four clauses, none of them new machinery:

| # | clause | where it goes | cost |
|---|---|---|---|
| **P1** | the gate block keys on **rung == production**, not on `env == "home"` | `pages-deploy.py` | one condition + a rung declaration |
| **P2** | gate ① gains a **`walked-at`** clause — the walk record already carries an origin; the gate does not read it | `release-gate.py` (`D3`, already owed) | one clause + one selftest mutation |
| **P3** | **one QA build path.** Either CI calls `pages-deploy.py --env qa`, or CI stops deploying Pages and only deploys the Worker | `deploy-worker-qa.yml` | ⚠️ ⛔ **which one is right is a judgement and it has consequences for how you push.** §8 · Q3 |
| **P4** | the production deploy asserts the **QA origin served the same sha** before shipping it | `post-deploy.py` already reads origins; it has no cross-origin clause | ~15 lines |

**Falsifier for the set:** if, over three laps, no production deploy is ever refused by P1–P4 **and** a
build never reaches an origin by a path other than `pages-deploy.py`, they are reading the same fact
four times — collapse them. `[stated because a recommendation without a falsifier is an opinion]`

---

## 4 · THE ROLE QUESTION — you as end user and as administrator/builder, at once

### 4.1 · You are already both, six times, and nothing records which is which

`measured`, `python3 tools/access-map.py` at HEAD:

| person row | estate | deployment | relationship | capability |
|---|---|---|---|---|
| `p-7f3a2c (paul)` | `est-3c9f1a` | production (top level) | owner | **administrator** |
| `p-7f3a2c (paul)` | `est-lab0001` | lab | owner | member |
| `p-paul` | `est-e6696a` | home | owner | **administrator** |
| `p-paul-home` | `est-d93508` | paul | owner | **administrator** |
| `p-paul-qa` · `p-paul-qa2` · `p-paul-qa3` | `est-qa0001` | qa | owner | **administrator** |

**Six rows, five ids, four estates, and the id scheme is ad-hoc** — `p-paul` is in `home`, `p-paul-home`
is in `paul`. ⛔ **Nothing in any row says whether it is the seat you *use* or the seat you *test with*.**
A person row carries `relationship` and `capability`; it carries no field for *which of your two hats
this is*. So the distinction you are asking for **cannot be recorded today**, let alone enforced.

⚠️ **Three QA rows for one person is itself the tell.** `p-paul-qa`, `-qa2`, `-qa3` are what re-minting
looks like when nothing owns the identity.

### 4.2 · ⛔ A "QA home" is not a home today — QA is one estate with thirteen owners

`measured`: `grantFor()` (`worker.js:1004`) admits a credential only when `row.estateId === env.ESTATE_ID`.
QA binds `est-qa0001`. Therefore **every** account created in QA — the 12 synthetic walkers and every one
of your three rows — is a grant on **the same estate**, and the access map shows them all as
`relationship: owner`.

So *"a QA home that I am a part of testing in"* resolves today to **a single shared estate co-owned by the
harness.** That is not the same object as your production home, and no rename makes it one.

### 4.3 · ⛔ Your real records have disarmed QA's reset — measured

`measured`, `tools/read-onboarding.py --env qa` at HEAD:

```
provenance: 4 real · 463 synthetic · 44 unknown
standing:   12 current · 451 superseded · 4 unlinked · 44 pre-date run identity
```

The four `real` rows are your own setup today, and they read **`real unlinked`** — real by marker,
unlinked because they carry no synthetic run identity. ⭐ **The marker works: your answers are
distinguishable from the harness's.** That is the good news and it is the direct answer to the question.

The cost is elsewhere. `tools/reset-production-estate.py:24-26,179-181` (`measured` by source read;
execution of the dry run was blocked in this session, so this is graded by code and not by observation):

> *"ONE `real` RECORD ABORTS THE WHOLE RUN, including the synthetic ones."*
> `if buckets["real"]: print("⛔ REFUSING: %d record(s) look like a real person's.")`

⭐ **So the environment whose entire job is to be reconstructible is, right now, not resettable — and it
became so the moment you used it as an end user.** This is the exact structural cost of the role
you are asking to hold, arriving before the design does. It is not an argument against holding it. It
is the thing the design has to answer.

⚠️ **The tool is correct and should not be loosened.** *"The moment a real person has onboarded, this
tool is wrong to run at all"* is the right rule. The defect is that **your test-seat records and your
end-user records are the same class to it**, because §4.1 gives it no way to tell them apart.

### 4.4 · Where holding both roles is safe, and where it is a hazard

| | safe | hazard |
|---|---|---|
| **your production home** | ✅ `[paul-ruled 2026-09-06]` *"I don't want my profile in production to have any more rights than Mom's."* An estate owner among estate owners. `VOCABULARY.md` §3f already separates **application administrator** (the master token, across estates) from **estate owner** (a grant, one estate) | ⚠️ ⛔ **`[paul-ruled 2026-09-08, D1]` made administrator reach a stated PRODUCT PROPERTY.** You now hold, in one seat, the master token that can read behind Bob's daughters' door **and** an ordinary end-user account. Those are two credentials; they are not two *people*, and nothing in the record distinguishes an act done under one from an act done under the other |
| **your QA home** | ✅ your real address in QA is right — `.plans/2026-09-07-qa-access-DECISION.md` measured that no address is in either origin's public bytes | ⛔ §4.3 — a real record in a resettable environment. ⛔ §4.2 — co-owned with the harness |
| **the record** | — | ⛔⛔ **this repo has already paid for exactly this confusion once.** `tools/people.json:_meta` — Paul's own device was attributed to Mom until 2026-07-28, and *"every engagement number computed before 2026-07-28 attributed Paul's own app-opens to Mom and Mom's to nobody… do not cite any pre-2026-07-28 funnel verdict"*. **One commit changed Mom's surface on the strength of a figure that was a count of the wrong person.** `measured` |

⭐ **The precedent is the argument.** The failure mode of holding two roles is not that you do the wrong
thing; it is that **the record cannot say which role did it**, and a later reading treats a test as a
signal. It happened here, it invalidated a month of numbers, and it was caught only because someone read
content instead of activity shape.

### 4.5 · What must be true so a test action is never mistaken for a real one

`proposed`. Three properties, in order of how much they buy per unit of work:

| # | property | how it is checkable |
|---|---|---|
| **R1** | ⭐ **every person row declares its SEAT** — `seat: person` \| `seat: test` \| `seat: harness` — as a **first-class field, absent ≠ false** (`grant-mint.declare()`'s own rule at `:98-104`) | `access-map.py` prints it; a row without one reads **UNDECLARED**, never "person" |
| **R2** | ⭐ **`reset-production-estate.py` classifies on the SEAT, not on the marker alone** — so a `real` record held by a `seat: test` row does not abort a QA reset, and a `real` record held by a `seat: person` row still aborts everything | its existing three-bucket classifier + one mutation in its selftest. ⛔ **Never a `--force`**; the same reasoning that refused `--dispose-class` in `watch-feedback.py` |
| **R3** | **your two seats carry the same `personId` prefix and differ by rung**, so the map can say *"this is one human at two rungs"* rather than showing six unrelated strings | `access-map.py` groups them; nothing else changes |

⛔ **R1 is the load-bearing one and R2/R3 are worthless without it.** ⚠️ And R1 is a claim about a human's
intent, which no derivation can supply — **it is declared at mint time, by you, or it is UNDECLARED.**

**Falsifier for R1:** if, after one lap, every row's seat has to be inferred from its id string because
nobody set the field, the field is decoration and the honest fix is to make `grant-mint` refuse a mint
without it.

---

## 5 · THE RENAMES, COSTED

⭐ **The pin is the whole trick.** `measured`: `[env.bob]` and `[env.paul]` set `name =` inside the env
block; `qa`, `lab`, `home` do not, so wrangler derives `fernwood-<env>` and **the workers.dev hostname
follows the flag.** Pinning `name` to today's value **before** renaming the flag turns a hostname
migration into a flag rename. `inferred` from wrangler's documented `name` override plus the two pinned
envs that already work this way; ⛔ **verify with one `--dry-run` deploy before relying on it.**

| # | today → proposed | class | true cost |
|---|---|---|---|
| **N1** | top-level `ENV_NAME = "production"` → **`legacy`** | ⚠️ **half-migration, and the fork already exists** | `measured`: **8 tools already say `legacy`** (`grant-mint` · `walk-integrity` · `post-deploy` · `watch-accounts` · `watch-feedback` · `read-onboarding` · `check-release-docs` · `build-library-index`), and **two of them hardcode the translation** — `grant-mint.py:320` and `watch-accounts.py:211` both read `("production" if env == "legacy" else env)`. The tool layer renamed it; the deployment did not. ⛔ Changing `ENV_NAME` changes what `/health` reports **and the `env` stamp on every new record**, so the two hardcodes must move in the same commit or `env_agrees()` refuses every mint. **The old records keep the old stamp — that is history, not drift, and nothing should rewrite it.** ⛔ It also renames a value `watch-feedback.GATING_ENVS` reads (`{"home","legacy"}`) — already `legacy` there, so this rename *closes* a fork rather than opening one. ⭐ **Under the four-tier model this rename is no longer cosmetic: it is the tier label of the thing being unpublished** (§2.3), and ⛔ **it must not be confused with the unpublish itself** — `ENV_NAME` is a var; disabling Pages and rotating `SHARED_TOKEN` are separate acts in a separate order |
| **N2** | `home` → **`production`** | ⚠️ **migration unless pinned** | `measured`: **89 `"home"` literals across 13 tools · 55 `--env home` invocations in tracked text · 4 toml blocks · Pages project `fernwood-home` · `FAMILY_HOSTS = fernwood-home.pages.dev` · `BRANCH["home"] = "home"`.** ⭐ Pin `name = "fernwood-home"` and **the Worker hostname does not move**. ⛔ The **Pages project name cannot be renamed in place** (`inferred` — Cloudflare has no rename; you create a new project), so `fernwood-home.pages.dev` either **stays** (the flag and the host disagree — honest, cheap, and already true of `bob`) or you **migrate the origin**, which changes `FAMILY_HOSTS`, invalidates `hostAgrees()` for every existing credential-bearing device, and leaves the old origin live. **Recommend: rename the flag, keep the host.** ⚠️ `check-release-docs.py` will catch the `CYCLE-MAP` ↔ `GATING_ENVS` half automatically and **it will go red until both move** — that is the control working |
| **N3** | `lab` → **`dev`** | ⚠️ **migration unless pinned** | `measured`: **31 `"lab"` literals · 12 `--env lab` · 4 toml blocks · Pages project `fernwood-lab` · `journey-logic.py:88` branches on the string `"lab"` being *inside a URL*.** Same pin trick. ⛔ `wrangler.toml:76` already calls this *"separate churn"*; nothing has changed to make it cheaper. **Lowest value of the four** — the flag is honest enough and no reader is misled by it |
| **N4** | `bob`, `paul` → **not environments; homes at the production rung** | ✅ **bookkeeping — if it is a declaration, not a rename** | `measured`: `pages-deploy.py:~140` already says so in prose and `HOUSEHOLD` already lists them. The cheap move is **a `rung =` var in each env block** and a derived reader, so `HOUSEHOLD` stops being a typed roster — the control this repo has been bitten by four times (`release-gate.py:80` names them). ⛔ Do **not** rename the flags: `name` is pinned, the hosts are right, and `VOCABULARY.md` §2 already keeps an estate's name off a user-facing surface |
| **N5** | local branch `main` → *(leave it)* | ✅ **no change; record the fact** | `measured`: local `main` tracks **`origin/staging`**, `push.default = upstream`, and `origin/main` ↔ `origin/staging` diverged at 2026-09-06 15:00 with **10 / 542** unique commits. So `main` here means *the new product's trunk* and `origin/main` means *the frozen legacy branch GitHub Pages serves Mom from*. ⚠️ **A rename is not worth it; a line in `CLAUDE.md` is.** An explicit `git push origin main` from this tree would put 542 product commits on Mom's live branch |

⭐ **What is genuinely free, and it is the highest-value item in this section:** `VOCABULARY.md` has
**no environment section at all** (`measured`: `grep -c '\bdev\b' VOCABULARY.md` → 0). Every rename above
re-forks the moment it lands unless the register lands in the same commit. **`rung` and `home` are two
words this corpus does not yet have, and §4's rejected-words table is where the next reader will look.**

---

## 6 · WHAT BREAKS

| # | what | grade | detail |
|---|---|---|---|
| **B1** | ⛔ **G3's guard is already unfireable in one direction, and Paul's ask points straight at the other** | `measured` | `grant-mint.estate_agrees()` (`:339`) compares the estate you asked for against the estate the env binds. `env_agrees()` (`:320`) adds a **KV canary read** — so today the destination *is* confirmed by namespace. ⭐ **The canary IS the repair `wrangler.toml:66-72` says is needed, and it landed in the same commit as
that comment** (`cb29e08`, 09-05 16:05 — *"that killed G3, so G3b asks the destination who it is"*). ⚠️ **So
the comment has read as an open defect for three days while its own fix sat beside it.** ⛔ **But if one home exists at two rungs sharing one estate id (§8·Q1 answer "same"), `estate_agrees` is vacuous again and only the canary stands.** ⚠️ ~~And `reset-production-estate.environments()` (`:66`) builds a dict **keyed by estate id** — two envs on one estate silently collapse, last-one-wins.~~ ⭐ **RETIRED by the Q1 ruling (§10.7·W3): the collision cannot legally occur. Retired by RULE, not by code — the dict is still unguarded, which is §10.6** |
| **B2** | ⛔ **the household/environment distinction is a typed roster in three places** | `measured` | `pages-deploy.HOUSEHOLD` · `HOUSEHOLD_ALLOW` · `PROJECT`/`BRANCH`/`ORIGIN` maps. A new home is **four hand edits** and the failure mode is the one its own comment names: *"moves the leak rather than fixing it."* A `rung`/`class` var in the toml with derived readers removes all four |
| **B3** | ⛔ **the frozen legacy instance is named `production` in the one place a record can read it** | `measured` | `ENV_NAME` is *"stamped on every new feedback / zone-audio record"* (`wrangler.toml:20-22`). So Mom's live records carry `env: "production"` and the new product's carry `env: "home"`. **Renaming N1/N2 makes the *future* right and leaves a two-era stamp in the store.** ⛔ **Do not backfill.** Two eras honestly stamped beats one era retroactively edited — and `LEGACY_BEFORE` is the precedent for how this repo handles exactly this |
| **B4** | ⛔ **walk evidence does not name its origin** | `measured` | §3.3. Any rename that moves an origin also silently invalidates nothing, because nothing was reading it. That is the defect, not the relief |
| **B5** | ⛔ **`est-e6696a` — "the production home is her blank slate" — holds four owner grants and three are not Mom** | `measured` | `access-map.py`: `p-paul`, `p-vfy`, `p-yjnw9lt41nww` all `owner + administrator` at `est-e6696a`, plus `p-b91e4d (mom)` as `owner + member`. ⛔ **The record and the ruling disagree.** Which should win is a call about your family's data and is §8·Q4 |
| **B6** | ⛔ **`est-9a74df` (Bob) has a deployment and zero grants** | `measured` | `access-map.py`: *"ESTATES WITH A DEPLOYMENT BUT NO GRANT (nobody can reach them): est-9a74df."* A production origin nobody can open |
| **B7** | ⚠️ **eight grant rows carry NO CONSENT RECORD, including every one of yours** | `measured` | `access-map.py --gaps`. §3e requires one. *"An absent record cannot be distinguished from a refused one"* — and under D1 the administrator-reads consent is now the thing that makes your reach legitimate |
| **B8** | ⚠️ **`instance/paul.json` and `instance/bob.json` both call their deployment "an ARTIFICIAL rig `[paul-ruled 2026-09-06]`"** | `measured` | The stamp appears **nowhere else in the corpus** (`grep -rn ARTIFICIAL` → those two lines only), and it was committed at **19:44** on 09-06, **after** `wrangler.toml`'s *"PAUL'S OWN HOME — A HOUSEHOLD LIKE ANY OTHER"* (14:47) and *"a household of his own"* for bob (12:12). ⛔ **Two tracked files claim a ruling that a third contradicts, and the newer one is the weaker-provenanced.** Your ask resolves it in one sentence; **I do not resolve it.** §8·Q4 |
| **B9** | ⛔ **the `qa` rung name is triple-booked** | `measured` | `--env qa` (rung) · branch `staging` (CI) · `stage: qa` (pipeline, `VOCABULARY.md` §3d, **a knowingly declared collision**). A fourth reading — *"my QA home"* — is what your ask adds. ⚠️ §3d's falsifier is *"if a reader cannot tell which act 'QA passed' means, the stage renames"*. **Adding a QA home is the strongest test that falsifier will get** |
| **B10** | ⛔⛔ **`CANON_FOREIGN_OK` breaks the mirror in BOTH directions, and your two new tier definitions are what expose it** | `measured` | `worker.js:116-129` — `canonIsThisEstate()` refuses every model route (503 `canon-not-this-estate`) unless the bundled digest's estate equals the deployment's, **or** the env declares `CANON_FOREIGN_OK = "true"`. **`qa` and `lab` declare it; `home`, `bob` and `paul` do not.** ⭐ **So the behaviour QA most needs to mirror — what Guru and the today-line do at a household with no canon of its own — is the one behaviour QA structurally cannot show you: production refuses, QA answers.** ⛔ And in the other direction, at your QA end-user seat with your real address, a model route answers from **Fernwood's** bundled record — `worker.js:1386`'s own comment: *"TODAY_LINE_SYSTEM names the estate, its address and its elevation."* ⚠️ `check-estate-neutral` **cannot see this**: `CLAUDE.md`'s own ⛔⛔ note says it tests for NAMES, and the 09-07 leak that reached Roswell and Bangor was *"NUMBERS AND POSSESSIVE PRONOUNS"*. ⭐ The var's stated warrant — *"qa and lab may carry Fernwood's canon, because they ARE Fernwood"* — is the premise **tonight's definitions moved**: a playground is not Fernwood, and neither is your condo |
| **B11** | ⛔ **the "data reference point" has no reader, no restore and one copy** | `measured` | §2.3.3 · L1–L3. ⚠️ **Not a defect in `archive-frozen-estate.py`** — that tool does exactly what it says and its read-only construction is right. The gap is that *"keep it as a reference"* was ruled and **nothing was built to honour the second half of the sentence** |
| **B12** | ⚠️ **175 is a KV count and was relayed as a localStorage count** | `measured` | §2.3.4. Browser storage is **19 rostered / 18 in use** (`check-storage-keys.py`). Recorded because scoping the drain against 175 would size the wrong work — and because a number that travels wrong once travels wrong again |

---

## 7 · THE SEQUENCE

⛔ **Nothing here starts.** Ordered so the step that makes every later failure legible lands first. Each
row: reversible or not, and its falsifier.

| # | step | who | reversible | falsifier — *how you would know it did not land* |
|---|---|---|---|---|
| **S0** | ⭐ **RULE Q1–Q5 (§8).** Nothing below is safe to build without Q1 | **Paul** | n/a — a ruling | the ruling is not written into a citing file; *"a ruling that is not in the register is not in force"* |
| **S1** | ⭐ **Declare `rung` and `home` in `VOCABULARY.md`**, with §4 rows for what they are **not** (`environment` as a tenant noun; `production` as a deployment) | agent → Paul ratifies | ✅ fully | a later document uses `environment` to mean a tenant and nothing catches it |
| **S2** | ⭐ **Add `rung = "dev"\|"qa"\|"production"` as a var in every `wrangler.toml` env block**, and make `pages-deploy.HOUSEHOLD` **derived** from it | engineering-partner | ✅ fully — additive; nothing reads it until S3 | a new env added without `rung` is silently treated as a household. ⛔ **Vars do not inherit — so a missing `rung` must REFUSE**, the same allow-list-never-exclude-list rule `CANON_FOREIGN_OK` already states in that file |
| **S2b** | ⭐ **Assert estate-id uniqueness across the toml** (§10.6) — the invariant the Q1 ruling creates and nothing checks | engineering-partner | ✅ fully — one assertion in an existing parser | add a duplicate id to a scratch toml and the parser still returns a dict. ⛔ **It must THROW, never count** |
| **S3** | ⛔ **Close HOLE 3 (§3.4) — one QA build path** | engineering-partner, on Q3 | ✅ fully — one workflow job | push to `staging`; `fernwood-qa.pages.dev/viewer.html` is still **1,203,913** bytes and `CLAUDE.md` still answers `{"tombstone":true}` |
| **S4** | **Key the production gate on `rung`, not on `env == "home"`** (P1) | engineering-partner | ✅ fully | `pages-deploy.py --env bob --sha <an uncleared sha>` still deploys |
| **S5** | **Gate ① gains the `walked-at` clause** (P2, already owed as D3) | engineering-partner | ✅ fully | a walk recorded at `lab` still passes gate ① — and the selftest has no mutation proving it can fail |
| **S6** | ⭐ **`seat:` on every grant row** (R1), then **R2**, then **R3** | agent mints, **Paul declares each seat** | ✅ fully — additive field | `access-map.py` prints a seat for a row nobody declared |
| **S7** | ⚠️ **N1 — `ENV_NAME` top level → `legacy`**, with the two hardcoded translations moved in the **same commit** | engineering-partner | ⚠️ **partially.** The var is reversible; **records stamped in between are not** (B3) | `/health` on the top-level Worker still reports `env: "production"`, or a mint refuses with a G3b canary mismatch |
| **S8** | ⚠️ **N2 — `home` → `production`, `name` pinned, Pages host unchanged** | engineering-partner | ⚠️ **partially** — same record-stamp asymmetry | the Worker hostname moved (the pin failed), or `check-release-docs.py` is still red after both halves moved |
| **S9** | ⛔ **THE AXIS SPLIT — `scopeFor()` through its 59 sites** (this is D5). ⭐ **§10.4: same size, materially safer under the Q1 ruling** — and ⚠️ **Q2·(b) now depends on it**, so Paul's QA condo is downstream of this step unless he takes route (a) | engineering-partner | ⛔ **STILL NOT REVERSIBLE, now DIAGNOSABLE (§10.4).** Keys are `<estateId>:<kind>:<suffix>`; a wrong scope writes a key under the wrong home with **no error** (`worker.js:704-712` says exactly this) | `grep -c "scopeOf(env)" worker/worker.js` has not fallen; or `assertScope` never throws in any test, which means no site was proven to fail |
| **S10** | **N3 — `lab` → `dev`** | engineering-partner | ✅ | — |
| **L-a** | ⭐ **DRAIN HER DEVICE — during the visit, before anything else** | **Paul**, on her phone | ⛔ **NOT REVERSIBLE IF SKIPPED.** Six `tateTracker.*` / `momQueue.*` keys exist nowhere else | after the drain, `read-mom-feedback.py --pickup` and `watch-feedback.py` show her last arrivals landed. ⛔ **A device that never came online cannot be drained later once the token has rotated** |
| **L-b** | **RE-ARCHIVE + `--verify`** — the archive is 4 keys behind (`BACKLOG.md:348`) | agent | ✅ additive; the tool has no delete path | `--verify` reports any key it could not read; ⛔ a non-empty `unreadable` is a refusal, not a note |
| **L-c** | **ROTATE `SHARED_TOKEN`** — *"that is the actual lockout"* | Paul | ⛔ **irreversible for anything undrained** | her app still writes |
| **L-d** | **TAG THE SHA · DISABLE PAGES** — ⛔ **never edit `main`** | Paul | ⚠️ Pages can be re-enabled; the tag is permanent and cheap | `viewer.html` still serves at the GitHub Pages URL. ⚠️ **Her cached copy will still load** — that is expected, and the sunset banner already shipped to `origin/main` (`e0746c5`·`517e597`·`edfff1c`) |
| **L-e** | **STOP THE BOTS** — `record-weather.yml` and any scheduled writer against the frozen Worker | agent | ✅ | a rollup commit appears on `origin/main` after L-d |
| **L-f** | ⭐ **BUILD THE READER** (§2.3.3) — or rule that the file alone is the reference | **Paul rules first** | ✅ | ninety days after the sunset, nobody has asked the archive a question — in which case L-f was correctly declined |

⛔ **L-a → L-e is a strict order and the dependency is one-way.** ⚠️ **The whole legacy sequence is gated
on `production` having a real owner** (`BACKLOG.md:342`), because L-a happens during the visit that founds
it. So **S-anything on the production rung comes before L-anything**, which is a second reason S3 (one QA
build path) is first: the build she founds her home on is the one QA certified.

⭐ **S1–S6 are all reversible and all independent of Q1.** ⛔ **S7–S9 are not**, and S9 is the only one
that can silently corrupt a record. **If you take nothing else from the sequence: S3 first, S9 last.**

---

## 8 · WHAT I DECLINE — Paul's calls, not mine

| # | the question | why it is his |
|---|---|---|
| ~~**Q1**~~ | ✅ **RULED 2026-09-08 — see §10.** *"It's gotta be two different estate IDs… I'll have a QA version of my condo and then a production version, and I understand they won't be quite the same."* **`(place, rung)` → one estate id.** | — |
| **Q2** | **Is `est-qa0001` your QA home, or do you want a QA home of your own beside the harness's?** Today they are the same estate with thirteen owners (§4.2) | Scope, and a call about whether your real answers should sit in the harness's store at all |
| **Q3** | ⛔ **Which QA build path survives (§3.4)?** CI calling `pages-deploy.py` keeps push-to-deploy and makes every QA deploy pass the falsifiers. CI deploying only the Worker means **QA Pages moves only when a human runs the deploy** — which changes how you ship | A tradeoff between automation and control, on your own working rhythm |
| **Q4** | ⛔ **Whose home is `est-e6696a`, and what is `est-d93508`?** The record says the first has four owners and three are not Mom (B5); two tracked files say the second is an *"ARTIFICIAL rig"* while a third says it is **your home, set up from scratch** (B8) | It is about your family's data and your own intent. **I report the contradiction; I do not pick** |
| **Q5** | ⚠️ **D2's reconciliation with ux F1a.** You took the front door knowing it was flagged. The likely shape — *a credentialed device passes straight through; only an un-credentialed visitor meets the door* — honours both, but **F1a's owner has not agreed it** and it is a surface decision | Not method. → `ux-expert`, then you |
| **Q6** | ⭐ **What does *"not publicly available"* mean for legacy — Pages disabled, or the repo private, or both?** Disabling Pages unpublishes the **app** and leaves `viewer.html` readable on a public repo (§2.3.2). Taking the repo private is a different act with a different blast radius (`inferred`: Pages on a private repo needs a paid plan; this repo is the engine's home) | It is a claim about how private her eight months need to be, and about a repo that is the whole project's home. **I cost both and pick neither** |
| **Q7** | ⭐ **Is *"a data reference point"* a BUILD this lap, or is the file enough?** §2.3.3 names the three things that would make it real (a reader · a second copy off this laptop · a freshness control, counted never graded). ⛔ **Where the second copy of her words may live is a privacy call under the QUARANTINE clause, not a storage call** | Value and privacy both. ⛔ I state what would have to be true; **whether it is worth doing is yours** |

⚠️ **And one thing I decline on principle:** whether any of the above outranks the zones work, the ask
surface, or anything else on the board. §3.4 is critical **in this lane** and I have shown the bytes;
**the ordering across lanes is yours** (`CYCLE-MAP.md` § WHO LAYS OUT THE BOARD, `[paul-ruled 2026-09-07,
A-6]`).

---

## 9 · THE FALSIFIER FOR THIS FILE

**If, in three months, `--env` still names both a rung and a tenant and nothing has gone wrong, the axis
split was over-engineering and §1 was a category error dressed as a finding.** The tell that it was not:
**a record written under the wrong home with no error** (`worker.js:704-712`'s named fear), or a fourth
identity minted for you in QA.

**And the cheap early tell, checkable in one line at any pickup:**
`curl -s https://fernwood-qa.pages.dev/CLAUDE.md | head -c 40` — if it is not `{"tombstone":true`, HOLE 3
fired and this file was right about the mechanism.

**And the legacy half has its own tell, which is the one that would hurt:** if the sunset runs and a later
session has to ask *"what did she say about the pond in June"* and the answer is *"there is a 6 MB JSON in
`.private/`"*, then §2.3.3 was right and the reader should have been built. If nobody ever asks, it was
not.

---

## 10 · ⭐ AMENDMENT — Q1 IS RULED `[paul-ruled 2026-09-08]`

> *"If one place exists at two rungs — if you're saying Fernwood exists in QA and production — it's
> gotta be two different estate IDs, I think. Otherwise we get too much divergence with all the
> generative AI, nondeterministic input. So, like, I'll have a QA version of my condo and then a
> production version, and I understand they won't be quite the same."*

> ### THE RULE
> **`(place, rung)` → one estate id. An estate id is globally unique across every deployment.**
> A place at two rungs is **two estates**, and they are **expected to diverge**.

⭐ **The reason is the load-bearing half, and it is not a preference.** Sharing an id would not prevent
divergence — generative and nondeterministic input produce it regardless. It would only decide **where
the divergence lands**: inside one record instead of across two. **Today's measurement is that case
already happening** — his four `real` onboarding rows sit among **463 synthetic** in `est-qa0001`.
`measured`. He is ruling against a pollution he has already seen.

### 10.1 · ✅ The current `wrangler.toml` already satisfies the ruling

`measured`, parsed at HEAD: **six deployments, six distinct estate ids, six distinct KV namespaces.**
So this ruling **ratifies the reverted state** rather than asking for a migration. ⛔ **Nothing has to
move.**

### 10.2 · ⛔ Which line is superseded — and it is narrower than it looked

| line | status |
|---|---|
| `worker/wrangler.toml:64-70` — *"an estateId names an ESTATE, not an estate-in-an-environment… The environment is the NAMESPACE"* `[paul-ruled 2026-09-05]` | ⛔ **SUPERSEDED by this ruling.** The environment is no longer *only* the namespace; the **rung is part of the estate's identity** |
| `worker/wrangler.toml:80-87` — *"LAB MUST NOT SHARE PRODUCTION'S ESTATE ID"* `[paul-approved 2026-09-05]` | ✅ **UPHELD, and promoted from a safety override to the general rule.** It won on merit on 09-05; it now wins on record |
| `estate.json:4` — *"An id is a COORDINATE, not a label — renaming the place does not rename the estateId"* | ✅ ⭐ **NOT SUPERSEDED, and this is the correction that matters.** It says an id is stable under **renaming**. It says nothing about one place at two rungs. `wrangler.toml:64-70` **cited it to justify sharing an id across environments — an inference the cited rule does not support.** ⚠️ That is this corpus's seven-forks shape in miniature: *a rule cited beyond what it says*, and the citation is what became doctrine |

⭐ **So the contradiction I reported in §8·Q1 resolves without either 09-05 ruling being wrong.** One was
a rule about renaming; the other was a rule about environments; the second was derived from the first and
should not have been.

### 10.3 · G3 — **RESTORED, confirmed**

`estate_agrees()` (`grant-mint.py:339`) compares the estate you asked for against
`ENVIRONMENTS[env].estate`, read from the toml. With **globally unique ids the comparison is decisive
again**: `--estate est-e6696a --env qa` now refuses. `measured` precondition: six ids, zero collisions.

| | |
|---|---|
| **what G3 now guards** | the **flag pair** — you named an estate the target rung does not bind. It fires on the exact mistake it was written for: a credential minted with the wrong `--env`, which used to land as a valid-looking row that opens nothing |
| **what G3 still cannot** | it reads the **toml**, so it checks two flags against a *declaration*, not against *reality*. If the toml itself gave two envs one id, G3 is vacuous again — ⭐ **and nothing checks that.** §10.6 |
| **what G3b (the canary) still covers, and still must** | the destination **namespace** answering who it is. ⛔ **Do not retire it.** G3 checks what was declared; G3b checks what was reached, and those are different claims |
| **what neither covers** | the right estate, right rung, **wrong person**; and a caller who misunderstood which rung a place is on |

### 10.4 · ⛔ What this does to the `scopeFor` conversion (S9) — **same size, materially safer**

**Unchanged in size: still 59 `scopeOf(env)` call sites.** Nothing about the ruling removes one.

⭐ **What changes is verifiability, and it changes the reversibility grade.** `worker.js:704-712`'s named
fear is *"a site that keeps reading the binding builds a key under the WRONG household **with no
error**."* Under multi-home, one namespace holds several estates, and the key's prefix is the only
tenant separator.

- **With shared ids** a wrongly-scoped key would be **byte-identical to a correct one** — the corpus's
  signature shape, *X and not-X produce the same observation*, and unrecoverable after the fact.
- **With globally unique ids** a wrongly-scoped key **names exactly one `(place, rung)`**, so the damage
  is silent at write time but **forensically resolvable** by reading the prefix.

⭐ **So S9 moves from `⛔ NOT REVERSIBLE` to `⛔ still not reversible, but diagnosable`** — and its
falsifier gets stronger: `assertScope` throwing in a test is now provable against a known-unique id set.
⚠️ It does **not** become safe. It is still the only step that can corrupt a record silently.

### 10.5 · Q2 and Q4 — how far the ruling carries them

| | |
|---|---|
| **Q2 — is `est-qa0001` Paul's QA home?** | ⭐ **ANSWERED IN PRINCIPLE, BLOCKED IN PRACTICE.** `est-qa0001` is *(the harness's place, qa)* — 463 synthetic records say so. Under the rule, **Paul's QA condo is a different place and therefore needs its own estate id.** ⛔ **But a second estate at the qa rung is not buildable today**, because the estate comes from the deployment binding (§1.3). Two routes, both real, and **the choice is his**: **(a)** a **seventh deployment** at the qa rung — new KV namespace, Pages project, Worker, `FAMILY_HOSTS`, `instance/*.json`, plus four roster edits in `pages-deploy.py`; works today, and ⚠️ re-instantiates the deployment-per-estate coupling he is trying to leave. **(b)** wait for **S9**, after which one qa deployment hosts several estates and his condo is one of them; right shape, and it is the irreversible step. ⛔ **I decline the pick** |
| **Q4a — `est-e6696a`** | ⛔ **NOT answered — but now FORCED, which it was not before.** Under the rule an id belongs to **one** `(place, rung)`. `measured`: it holds four owner grants — `p-paul`, `p-vfy`, `p-yjnw9lt41nww` and Mom. So the id cannot be both *"Mom's production home"* and *"the place where we verified things."* **Something must give**, and ⚠️ the cheap exit is blocked: `reset-production-estate.py` aborts on one `real` record, so if any of those three classifies `real`, the tool cannot clean it. ⭐ The §4.5 `seat:` field is what makes the three rows *nameable*; **which of them belongs there is his** |
| **Q4b — `est-d93508`** | ⭐ **The ruling settles the STRUCTURE and leaves the fact to him.** *An artificial rig is not a place*, so under `(place, rung) → one id` a rig cannot hold an estate id of its own. **The two claims can no longer both be true**: `wrangler.toml`'s *"PAUL'S OWN HOME… set this up in production from scratch"* is consistent with the ruling; `instance/paul.json` and `instance/bob.json`'s *"an ARTIFICIAL rig `[paul-ruled 2026-09-06]`"* is not. ⛔ **I am naming which line the rule contradicts, not deciding whose home it is.** Same reading applies to `instance/bob.json` against `est-9a74df` |

### 10.6 · ⭐ THE INVARIANT THE RULING CREATES, AND NOTHING CHECKS IT

**Globally-unique estate ids are now a rule, and no tool asserts it.** `measured`: six ids, zero
collisions **today** — which is exactly when a control is cheapest and least alarming.

`proposed`: a single assertion where `environments()` is already parsed (`grant-mint.py:47`,
`access-map.py:35`, `watch-accounts.py:121`, `reset-production-estate.py:51` — **four existing parsers,
one rule**). ⛔ **A fail-closed assert, not a metric** — it is binary and permanently green by
construction, so it must **throw**, never report a number. **Falsifier:** *if it ever fires, the toml
gained a duplicate and G3 was vacuous from that commit onward.*

### 10.7 · ⛔ WHAT BECOMES NEWLY WRONG — including in this document

**The half most worth reading. Three of the five are mine.**

| # | what is now wrong | grade |
|---|---|---|
| **W1** | ⭐ **§2.2 overstates the `dev = playground` definition.** I wrote that naming dev a playground *"retires a live contradiction"* and that G3 *"reopens the instant any two deployments bind one estate id."* **The ruling retires it directly and generally**, and closes the hypothetical by rule. My finding was right about the state and **wrong about what fixed it** — I credited a tier definition for what a rule now does | ⛔ mine |
| **W2** | ⭐ **§0·1 and §1.2's phrase *"one home at two rungs"* is wrong in his own vocabulary.** It is **one PLACE at two rungs**, which is **two homes**. A `home` is an estate; an estate now carries its rung in its identity. **Amended in place** — and worth noticing that my framing had already imported the confusion the ruling removes | ⛔ mine |
| **W3** | ⛔ **§6·B1's second half is retired.** I flagged that `reset-production-estate.environments()` (`:66`) builds a dict **keyed by estate id** and would silently collapse two envs onto one row. **Under the ruling that collision cannot legally occur, so the finding is closed** — ⚠️ *by rule, not by code.* The dict is still unguarded, which is §10.6 | ⛔ mine |
| **W4** | ⛔ **`worker/wrangler.toml:64-70` is now factually superseded and still reads as current doctrine.** It is the passage a future session will quote when it next wants to share an id. §10.2 | not mine |
| **W5** | ⚠️ **Any artifact that used *"the estate is the coordinate; the environment is the namespace"* as a reason.** `measured`: that phrasing originates at `wrangler.toml:64-70` and cites `estate.json:4`; the cited rule does not support it. ⛔ **`estate.json:4` itself stays true and must not be "corrected"** — the defect is in the citation, not the source | not mine |

⚠️ **And one thing that is NOT newly wrong, stated because it looks like it should be:** §2.3's legacy
model. `est-3c9f1a` = *(Fernwood, legacy)* and `est-e6696a` = *(a place, production)* are already two ids
for what a reader might call one project. ⭐ **The ruling retroactively explains that split rather than
disturbing it** — it was the first instance of the rule, made before the rule existed.
