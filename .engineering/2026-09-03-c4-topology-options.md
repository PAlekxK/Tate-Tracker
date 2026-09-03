# C4 · TOPOLOGY OPTIONS — environments, repo structure, the rename

**Mode:** path evaluation · **Seat:** `engineering-partner` · **Date:** 2026-09-03
**Half owned:** topology. `practice-steward` owns process concurrently. Designed to its stated
requirement: *a QA environment in which an agent may exercise write paths without touching her
answer record.*
**Nothing here is decided.** No canon changed, nothing renamed, nothing deployed.

---

## 0 · FIVE MEASUREMENTS THAT CHANGE THE ITEM — verified today, not restated from the row

| # | The row / a plan says | I measured | Why it matters |
|---|---|---|---|
| **0a** | ⛔ *"the push is HELD until the topology ruling says where third-party scoping material lives"*; *"Bob: all in the 43 unpushed commits"* | **Bob's full name — his full name — is ALREADY LIVE on `origin/main`**, 3 occurrences in `PRODUCT-ENGINE.md` (lines 84, 104, 379 at `origin/main`), landed in commit **`9d32aaa`**. `git grep -il "\bbob\b" origin/main` returns 4 files; the other 3 are "Bob Moesta" (a research method) and are irrelevant | The boundary the hold protects **has already been crossed once**. The hold is still right (more is worse, and §2b's consent gate is unpaid) but the decision is no longer *prevent* — it is *prevent AND decide about what is already public*. This is Paul's own recorded shape: *a verification is true at an instant, not for a day* |
| **0b** | browser storage: *"12 `tateTracker.*` keys"* | **18 distinct keys**, every one reachable — 15 declared as `const`s (`viewer.html:10456, 11226-11229, 11244, 11436, 12967, 12971, 13968, 18173-18175, 18702-18703, 21107`) + `deviceId`, `maintainer`, `ackSeen.v1` as bare literals. 13 direct `localStorage.*("tateTracker…")` call sites | A migration list built off 12 silently orphans 6 — *and one of the six is `ackSeen.v1`, her acknowledgement receipt.* Principle: **a grep is a good falsifier and a bad source** |
| **0c** | C1: *"a QA environment on that namespace can write test data into her answer record"* | **Worse than that: two write paths are UNGATED.** `worker.js:2286` lets `POST /api/feedback` through **without a token**, and `:2297` does the same for `POST /api/zone-audio` — deliberately, for the 2026-07-15 loss. `authOk` (`:90`) is the only credential in the system | ⭐ **This is the decisive fact for §1.** There is no credential that can distinguish a QA writer from Mom. So key-prefix isolation is enforced *only by the code you are testing* — circular. It also means the `tools/people.json` fence is documentation, not enforcement |
| **0d** | *"the Pages URL … redirect behaviour UNVERIFIED"* | **VERIFIED — it does not redirect.** GitHub docs, *Renaming a repository*: *"all existing information, **with the exception of project site URLs**, is automatically redirected to the new name"* — and the same page's recommendation: *"If you plan to rename a repository that has a GitHub Pages site, we recommend **using a custom domain**"* | Her link 404s. Already accepted. But the docs name the permanent fix, and it is the one that stops this from recurring — see §3 |
| **0e** | data-model §6: `.private/` is *"436 MB"* | **`du -sh .private` → 743 MB** (matches the C4 row) | §6's R7 arithmetic was written against a number that has grown **70% in one day of measurement drift**. Whatever store R7 picks, size it on 743 MB and rising, not 436 |

---

## §1 · ENVIRONMENTS

### 1.1 The served file

| | Option | Effort | Reversible | Costs Mom | Buys |
|---|---|---|---|---|---|
| **S1** | `staging` branch + second Pages site | — | — | — | ⛔ **NOT AVAILABLE AS SKETCHED.** A GitHub repo has **one** Pages site; the source is one branch *or* Actions, never two. A second URL needs a second **repo**. C1-a as written does not exist |
| **S2** | A `staging/` **path** in the same repo (`…/Fernwood-Tracker/staging/viewer.html`) | ~1 h | yes | **nothing** — same origin, so her 18 keys are untouched, and her URL is unaffected | A place to open a build in a browser at 414×A+ before swapping it in. ⚠️ But it is **still a production push** — it is prod with a second path, not a gate. Zero Worker isolation |
| **S3** ⭐ | **Cloudflare Pages project** on the same repo, production branch = `staging`; GitHub Pages stays prod | ~2-3 h | yes (delete the project) | **nothing** — her origin is unchanged | A real second environment at a **distinct origin** (`*.pages.dev`), free tier, per-branch preview URLs, and an **Access policy** that restricts viewing to Paul's Cloudflare account. Verified from Cloudflare docs |
| **S4** | Worker-serves `viewer.html` | high | no | ⛔ resets all 18 keys; risks her access | ⛔ **RULED DOWN 2026-07-17 (A5) and the ruling still binds.** Nothing in C4 reopens it |

**Recommendation: S3, with S2 as a same-day interim if Paul wants a look-at-it surface before the
Cloudflare project exists.** S3 is the only option that gives a *different origin*, which is what
lets an agent drive the app hard without any chance of a same-origin artifact reaching her.

⚠️ **One S3 detail that will bite:** GitHub Pages serves this app under the path `/Tate-Tracker/`;
Cloudflare Pages serves at the **root**. `tools/measure-nesting-width.js:404,432` already carries a
comment about that prefix. Serving at root is simpler, but any code that assumes the prefix must be
found before the first QA run, not during it.

### 1.2 The Worker

| | Option | Effort | Reversible | Can it reach `feedback:<date>`? | Verdict |
|---|---|---|---|---|---|
| **W1** ⭐ | `[env.qa]` in `worker/wrangler.toml` with its **own `kv_namespaces` id** | ~2 h | yes | **NO — by construction** | ✅ **Recommended.** Verified from Cloudflare docs: an env deploys as `<name>-qa`, and *"bindings and environment variables are non-inheritable, and must be specified per environment."* ⭐ **So a forgotten binding fails LOUD** — `env.OBSERVATIONS` is undefined, the handler throws 500. It cannot silently fall through to prod KV. That is the property to buy |
| **W2** | Key-prefix isolation inside the one namespace | ~1 h | yes | **YES** | ⛔ **Reject for QA.** Per **0c** there is no credential to enforce a prefix against, so the fence is the code under test. And the principle already on the shelf: *"Isolation is a guarantee; awareness is a heads-up — never let a safety claim rest on the second"* (2026-08-31). ⚠️ **Prefixing is still the right answer to data-model §5** — same mechanism, different job. Do not let one satisfy the other |
| **W3** | A second standalone Worker project | ~3 h | yes | NO | Same isolation as W1, two configs that can drift. W1 is strictly better: **one file declares both** |

### 1.3 ⭐ THE COMBINATION, and the one thing that makes it real

**S3 + W1 + a derived Worker base.** The gap that would defeat it: `viewer.html` **hardcodes the
production Worker at three sites** — `:7767` (`AMBIENT_ENDPOINT`), `:10292` (`ZONE_AUDIO_ENDPOINT`),
`:11243` (`FEEDBACK_ENDPOINT`). A QA build served from `*.pages.dev` with those constants intact
**writes into Mom's KV**, and every check would read green.

**The right shape** — one `const WORKER_BASE` derived from `location.hostname` (a `.pages.dev` host
resolves the `-qa` Worker), so the QA build is not a second artifact that can drift out of sync.
Principle: *generate the derivable; drift-lint the rest.*

**And the harness must assert it, not assume it.** Extend `/health` (`worker.js:2266`) to return
`env: "qa" | "production"` plus the KV id's last four. Then a write test **refuses to run** until it
has read `env == "qa"` off the wire. Without that, a green QA run is indistinguishable from a run
that went to prod — Paul's own recorded scar: *a release gate was scoring GitHub's 404 page.*

### 1.4 The origin/localStorage bill, priced explicitly

**The repo rename alone costs nothing here, and the row is right about why:** an origin is
scheme+host+port. The path `/Tate-Tracker/` is **not** part of it, so `palekxk.github.io/Tate-Tracker/`
and `palekxk.github.io/Fernwood-Tracker/` **share the same localStorage**. No migration is needed for
the repo rename. ✅

**What does reset all 18 keys:** a custom domain, `*.pages.dev` as prod, or Worker-serving. What is
lost, itemised:

| key | Loss if the origin moves | Recoverable? |
|---|---|---|
| `textSize` | Her **A+** setting reverts. This is M3's exact failure mode | ❌ only by hand, in person, 30 seconds |
| `deviceId` | A new browser bucket → **a seam in the engagement record**, which `tools/people.json` is emphatic must never be crossed by inference | ⚠️ only by Paul recording old→new **from his own observation while standing there** — content-grounded, not inferred |
| `momQueue.answered/snoozed/offered` | She is **re-asked questions she already answered** | ✅ mostly — a durable cross-device dismissal already exists (`viewer.html:12492`), 90-day window |
| `feedbackOutbox.v1` | **Unsent notes are lost silently** | ❌ — must be drained to a 2xx *before* the move |
| `zones.v1` | Unsynced zone edits lost | ✅ if `lastSyncedAt` ≥ `savedAt` — check first |
| `ackSeen.v1` | Her acknowledgement receipt re-fires | ✅ cosmetic |
| remaining 5 (`metrics.v1`, `metricsExclude`, `sync.v1`, `lastSync.v1`, `sync.audience.v1`, `maintainer`, `observations.v1`, `zoneJourney…`) | telemetry + config; `sync.v1` holds **the pasted token** | ⚠️ token must be re-pasted or the write paths that *are* gated go dark |

**Can a migration cover it? Partially, and only as a Paul-in-person act.** No script reads
localStorage cross-origin. The only mechanisms are (a) a one-time bridge page on the **old** origin
that hands the keys to the new one via a fragment — which requires her to open the old link once, and
she will, because Paul is re-linking her by hand anyway; or (b) re-derive from the server copies that
already exist. `textSize` is coverable by neither.

⭐ **The conclusion that should drive §4: an origin move is payable exactly once, and the invoice is
already scheduled — the in-person re-link.** If an origin move is ever going to happen, it belongs in
*that same visit*. Principle: *prove the environment can accept the work while a human is still
standing there.*

---

## §1b · STACK REVIEW — layer by layer

Constraints applied: `.engineering/2026-05-11-path-custom-domain.md`'s own rule — **don't migrate
working infrastructure without a functional reason** — and the site premise: no cell at the property,
Wi-Fi from the house, so nothing may depend on "improve the signal."

| Layer | Measurably straining | What the new approach requires of it | Verdict · price |
|---|---|---|---|
| **GitHub Pages (host)** | No second environment (one site per repo, §1.1-S1); **project-site URLs don't redirect** on rename (0d); 10 builds/hr soft cap vs. a weather bot pushing ~4×/day (fine) | A QA origin; a link that survives a rename; a plantless second instance later | ⭐ **STAYS, plus a bounded change: settle the custom domain.** The domain is the functional reason — it decouples her link from the repo name **permanently**, and the docs name it as the fix. ~$10/yr + one origin reset, paid in the same visit as the re-link. **Do not move prod hosting** |
| **One ~2 MB no-build HTML file with inlined JSON** | The **1 MB cliff hit twice** (silent 2-week write-path outage; Blob-API workaround at 100 MB); 53.2% of it is instance data (`.plans/…§3`); `check-data-inline.py` is a *correctness* gate because for 17 of 21 files the inlined const **is** the app | Per-estate data (§2c); a plantless instance | ⚠️ **STAYS FOR NOW; it is the layer the inversion converts.** The moment `viewer.html` becomes engine-template + instance-data, the re-inline step and the GitHub-Contents write path **both disappear** — the 1 MB cliff goes with them. That is the inversion's largest hidden dividend, and the reason to price the build step against it rather than in isolation |
| **Cloudflare Worker + ONE KV namespace** | **11 key prefixes, zero carry a property coordinate** (§3); **no identity anywhere** — one `SHARED_TOKEN`, and **two write paths ungated** (0c); `feedback:<date>` is the one irreversible thing (§5) | Isolation by construction per estate; tenant derived from the credential, never the path; a QA env | ⭐ **STAYS — and it is the layer that carries the new approach best**, because `[env.*]` gives you real isolation for free (W1). **Bounded change: `[env.qa]` + its own namespace now; the property prefix before instance 2 writes.** ⛔ **Migrating to D1/Durable Objects is not warranted** — no functional reason exists that a prefix and a second namespace don't answer, and KV's read latency is what serves her on house Wi-Fi |
| **System-prompt digest, ~127K tokens** | +73% in 61 days; 62-70% of Haiku's window; **retrieval degradation is the real constraint, not cost or window** — the 2,873/2,800 ft error happened with the correct value in context; every ceiling event so far was paid by *removing capability from her assistant* | R7 (743 MB of receipts) is **not satisfiable by digest at all**; a gardenless instance makes 41% of the digest dead weight | ⛔ **MIGRATE — but not here, and not in C4.** This is `ai-advisor`'s call (tool-use vs. retrieval split), it is already a worked backlog item, and its stated prerequisite is **a test harness that does not forge a Mom-input signal**. ⭐ **That prerequisite IS the QA environment this item is building** — so C4 unblocks it and should not attempt it |
| **Python tools + launchd + GitHub Actions** | 63 tools, **27 derive ROOT as "the directory above me"**, 24 name a domain file directly; 2 launchd plists hardcode the absolute path; the `FERNWOOD_AUG_2026` secret's failure is **silent-green** (documented in `deploy-worker.yml`) | An instance root that is no longer implicit; a QA deploy target | ✅ **STAYS. Do not migrate the automation substrate.** It works, Paul reads it, and 11 tools already carry `--selftest`. **Bounded change: `check-live.py` needs a `--base` flag** (`LIVE_BASE` is hardcoded at `:91`, so today it *cannot* verify a QA origin — the ship check is unusable against anything but prod) |

**Where a migration would change the origin Mom loads from:** only the custom domain, Cloudflare Pages
as *prod*, or Worker-serving. **That cost dominates every other line in this table**, and §1.4 prices
it. Everything else above is invisible to her.

---

## §2 · REPO STRUCTURE

| | Option | Effort | Reversible | What moves | The 44 unpushed commits' Bob material | Can `.private/` (743 MB) leave the laptop? |
|---|---|---|---|---|---|---|
| **(a)** | One public repo; third-party scoping docs → a private sibling (`fernwood-private` or the existing no-remote `tate-commons`) | **~2 h** | yes | 14 of the 19 Bob-naming files are `.plans/`, `.user-research/`, `.ai-advisor/`, `.ux-reviews/`, `.content-reviews/` — **already agent artifacts, not app code.** `BACKLOG.md`, `CLAUDE.md`, `PRODUCT-ENGINE.md`, `VOCABULARY.md` need a scrub, not a move | ⚠️ **See the finding below — this is the one place I push back** | ⛔ no — needs its own store either way |
| **(b)** | Make the repo private, serve Pages from it | ~1 h + **$4/mo** | yes | nothing | unchanged | no |
| | | | | ⛔ **VERIFIED AND IT BUYS NOTHING.** GitHub docs: *"If the account that owns the repository uses GitHub Free … the repository must be public"* → needs **Pro**. And: *"GitHub Pages sites are **publicly available on the internet, even if the repository for the site is private**."* So (b) costs money, hides *history* only, and leaves the served bytes exactly as public as today. A5's light-privacy posture already rules this class down | | |
| **(c)** ⭐ | **The inversion** — engine repo + per-estate instance repos | see §2c | staged: yes | see §2c | | ✅ yes — each instance repo can register its own private store |

### ⛔ 2a-i · THE ONE FINDING I'd push back on, and it has a closing window

**Moving the Bob files out in a new commit does not remove them from the 44 commits' history.**
Pushing then publishes them anyway. Two paths:

- **Accept it,** by analogy to the 2026-09-02 *"we don't need to do a huge scrub if it showed up at
  one point"* ruling. ⛔ **That ruling does not transfer.** It was about **her** name, which was
  *ruled publishable*. Bob is a third party, and §2b of the data-model doc makes his informed consent
  a **hard gate** — *"a gate, not a conversation."* Different subject, different rule.
- ⭐ **Rewrite the 44 commits before the first push.** They are **unpushed**, so there is no shared
  history and no collaborator to break. Effort: low. Reversibility: **high — bundle first**
  (`git bundle create ../fernwood-pre-scrub.bundle --all`, which is the sanctioned local backup path).
  ⚠️ **The window closes the instant Paul pushes.** After that, a rewrite is a force-push over
  published history, which is a different and much worse decision.

⚠️ **And `hooks/guard-secret-push.py` will not catch this.** It matches known provider patterns; a
person's name is not one. Verified: `Tate-Tracker` appears in that hook **only in a comment** (line 20),
not in `NEVER_PUBLIC` — so the rename doesn't break the guard's roster, but the guard was never
covering this class. ⭐ **Any private instance repo created under §2c must be added to `NEVER_PUBLIC`
at creation, not after** — the register is the roster, and an unregistered repo is unprotected.

### 2c · THE INVERSION — Tate-Tracker nested in the engine, not the reverse

**Paul's framing is right, and the measurements support it more than they support the status quo:**
53.2% of `viewer.html` is instance data; the bisection falsifier did **not** fire (the engine half is
soaked in Fernwood's *identity*, not its data); and ⭐ **the tenancy unit today already IS a git
repo** — 27 tools derive ROOT as "the directory above me."

⚠️ **But that last fact cuts against the naive split.** Those 27 tools assume *the data is one
directory below the tool*. Move `tools/` into an engine repo and all 27 resolve ROOT to a directory
with no `plants.json`, plus the 24 that name a domain file directly. That is a 51-site rewrite and a
new "which instance?" parameter on every tool.

⭐ **The cheap shape: invert OWNERSHIP, not the DIRECTORY.** The engine repo is the source of truth;
each **instance repo contains the engine at a known path** (`engine/`), and tools still run from
inside the instance. `ROOT = parent of tools/` stays true. **Zero of the 51 sites change.**

**How to keep the copies honest — reuse a pattern this repo already has.** ⛔ Not submodules
(detached HEAD, forgotten `--recurse-submodules`; wrong bet for a hobbyist-careful stack). Instead
`sync-engine.sh` + `check-engine-sync.py` asserting **byte-identity against the engine repo**, which
is exactly the shape of `tools/generated_views.py`. A divergence in an `engine`-class file is a
**defect** (data-model §4 already says so) — so byte-identity is the correct predicate, and the
checker's absence is what would let two definitions of a lap be born.

**What the inversion costs — now vs. later:**

| Coupling | Cost now | Cost later (after instance 2 exists) |
|---|---|---|
| **The re-inline step** | ⭐ **This is the big one.** `viewer.html` becomes a **build artifact** (engine template + instance JSON). **The inversion introduces the build step this project has deliberately never had.** ~1-2 days | Same work, plus doing it while two instances are live |
| **…and its dividend** | The Worker's GitHub-Contents write path and the **1 MB cliff** both **disappear**. Guru's write-to-canon becomes "commit the JSON, CI rebuilds" | — |
| **The digest build** | `build-digest.py` becomes per-instance; `check-digest-fresh.py` per-instance. Small — it already reads from ROOT | Multiplies by N |
| **Pages source** | Each instance repo gets its own Pages site — which is also exactly how you get a second URL that S1 can't provide | Same |
| **The Worker's single KV** | ⛔ **One Worker cannot honestly serve two instances yet.** §2 rule 3 says tenant derives from the credential — and per **0c** there is no credential on two write paths. ⭐ **So instance 2 gets its OWN Worker + its OWN KV namespace.** Isolation by construction, same argument as one-database-per-estate, and it needs **no auth work at all**. Price: N Workers to deploy — fine at N=2-3, wrong at N=10 | Growing |
| **photo-organizer's in-place read** | 2 hardcoded paths (`album_timeline_sheet.py:43`, `vehicle_service_candidates.py:57`) + ~8 more tools naming the repo. Replace with a one-line instance registry. ✅ **And verified good news: the `service:{vehicle}:{sr_id}` tags are PATH-FREE** (`ingest_service_review.py:240`, `propose_service_entries.py:160`) — the DB survives a path change untouched | Same |

**What it does to the rename:** `Fernwood-Tracker` becomes the **instance** name — and *"Tracker"* is
wrong for an instance (a place is not a tracker; `VOCABULARY.md` §4 rejects portable nouns, and the
interface names places). The instance likely wants to be **`Fernwood`**. ⛔ **The engine's name is
open and I am not naming it** — `VOCABULARY.md` rejects "estate manager," "Almanac"-as-portable, and
hub/portal/dashboard/OS in one stroke. Flagged for `content-steward`.

⚠️ **And this is the sharpest interaction in the whole item:** if the inversion is likely, renaming to
`Fernwood-Tracker` **now** means renaming to `Fernwood` **later** — and per **0d** each repo rename
breaks her Pages URL again. ⭐ **That is the strongest single argument for settling the custom domain
before the rename, not after.** With a domain, the repo can be renamed any number of times and her
link never moves.

**Can it be staged? Yes, and it should be. Recommendation:**

1. **Directory split inside the one repo first** — `engine/` and `instance/`, plus `ENGINE-MANIFEST.md`
   and its checker (data-model §8 step 3 already wants this). Nothing leaves the repo. Fully reversible.
2. ⭐ **Test the "no garden" falsifier at directory granularity** — stand up `instance-condo/` inside
   the same repo with **zero plant data** and render it. If the engine produces a coherent plantless
   app from data alone, the split is proven. If it doesn't, you have learned that **without moving a
   repo, without touching her, and without a build step.** `PRODUCT-ENGINE.md` calls this the
   migration's real falsifier; this makes it cheap enough to actually run.
3. **Repo split second**, only if step 2 passes.

**Recommendation across §2: (a) now — it unblocks the push in ~2 h — plus §2c step 1 immediately
after, because §8 steps 1-5 are all reversible and cheap precisely while nothing branches on them.
Reject (b). Defer (c)'s repo split behind the falsifier.**

**Falsifier for §2c:** if the directory split cannot render `instance-condo/` without editing anything
under `engine/`, the engine/instance line is drawn in the wrong place and the manifest is fiction —
stop and re-classify before any repo moves.

**`.private/` (743 MB) leaving the laptop — the three doors, priced:**

| | Effort | Reversible | Verdict |
|---|---|---|---|
| **Encrypted bundle** to iCloud / the existing encrypted-backup path | low | yes | ✅ **Solves *backup*. Does NOT solve R7** — a bundle is not retrievable in the field when the furnace quits, which is R7's whole point |
| **Private repo** (`fernwood-private`) | medium | yes | ⚠️ Works up to ~1 GB but 743 MB of scans in git is an abuse of git; every clone pays it. **Register in `NEVER_PUBLIC` at creation** |
| ⭐ **Object store** (R2 / B2) + the deterministic lookup tools of §8 step 7 | high | — | ✅ **The only door that satisfies R7**, and it is gated behind §8 step 6 (auth), which the data-model doc correctly says is **its own document**. ⛔ Do not fold it into C4 |

---

## §3 · THE RENAME — mechanics per layer

| Layer | Verified mechanics | Ships independently? | Reversible |
|---|---|---|---|
| **Prose + docs** (268 hits, ~120 files) | Mechanical. `git grep -l` gives the roster (83 files carry `Tate-Tracker`, 53 carry `tate-tracker`, 39 carry `tateTracker`) | ✅ **yes, any time, zero risk** | yes |
| **Local path** + symlink | ⭐ **The breakable surface is far smaller than 165.** With the predicate *executable/config files under `~/.claude` referencing `Developer/Tate-Tracker`, excluding logs*: **8 files** — `tools/{eval-c4-duplicate,health-probe,prove-probe,guard-injection-suite}.py`, `tools/icloud-backup.sh`, `handoff/{health-probe-ack,session-state}.json`, one feedback draft. Plus **2 launchd plists** (`com.fernwood.momqueue-watch`, `com.fernwood.momfunnel-watch` — both point at `tools/*.py` **and** `.private/*.log`), ~10 photo-organizer tools, ~6 operating-layer files (`backend/lib/field_log.py`, `config/projects.json`, `render.py`, `data/board.json` + tests). The remaining ~150 are prose/log mentions — **the row is right that their risk is none** | ✅ **yes** — symlink at the old path makes this a migration, not a cutover. Fix the 8 + 2 + ~16 in stages behind the symlink | yes |
| **GitHub repo name** | git remotes redirect automatically ✅. **Pages project-site URL does NOT** (0d) — her link 404s, accepted. ✅ **Also verified: `git log` provenance is untouched** — a rename is server-side metadata; SHAs, authors, messages unchanged, and blob/commit *permalinks* redirect (only project-site URLs are excepted). ⚠️ The one thing GitHub docs say breaks — *"GitHub will not redirect calls to an action hosted by a renamed repository"* — **does not apply**: `.github/workflows/` consumes only official `actions/*` | ⛔ **NO — must land in ONE push** with the four items below | ⚠️ renameable back, but the URL breaks each way |
| **…the four things that must be in that same push** | `tools/check-live.py:91` `LIVE_BASE` · `tools/build-control.py:84` `LIVE_VIEWER` · the forwarding repo at the old name · and 🔴 **the Worker's `GITHUB_REPO` secret** | | |
| 🔴 **`GITHUB_REPO` — the highest-risk single item in the rename** | It is a Worker secret in `"owner/name"` form (`worker.js:1386`, used at `:1409`, `:1454`). The rename makes it stale. `ghPutFile` issues a bare `fetch(url, {method:"PUT"})` with **no redirect handling** — and a 301 on a PUT is not replayed with its body. ⭐ **This is the exact class that already cost two silent weeks** (the 1 MB cliff: HTTP 200, empty body, every re-inline "succeeded" against nothing). Guru's whole write-to-canon path fails **quietly** if this is missed | ⛔ same push | yes (re-set the secret) |
| **Worker name** | New name = new script = **all secrets re-set** (`SHARED_TOKEN`, `GITHUB_TOKEN`, `GITHUB_REPO`, the Anthropic key, the Ambient pair). ✅ **KV survives**: `wrangler.toml` pins `id = "100f2b95e4be4c088a0000f917cf987b"`, so a new name on the same id keeps her data. Keep the old name live until the viewer ships. ⚠️ 3 hardcoded endpoint constants in `viewer.html` (`:7767`, `:10292`, `:11243`) + 5 tool defaults (`momlib.py:42`, `analyze-fernwood.py:36`, `read-mom-zone-audio.py:47`, `review-pending-species.py:49`, `record-daily-rollup.mjs:40`) + `deploy-worker.sh:28` + `deploy-worker.yml:64` | ✅ **yes** — old name alive means no cutover moment | yes |
| **The 12 → 18 localStorage keys** | ✅ **No migration is needed for the repo rename** — path is not part of origin (§1.4). ⚠️ But **0b**: the roster is **18, not 12**, and a hand-list will rot. **The right shape: one declared roster in code + a drift guard that scans for `"tateTracker.` and fails on an unlisted key** — the same mechanism `check-live.py`'s `FETCH_RE` guard already uses for assets. Build the roster now; it costs an hour and it is the prerequisite for any future origin move | ✅ yes, independently | yes |
| **Variable names** (`tateTracker.*` identifiers, `X-Tate-Token`) | **Last, or never.** ⚠️ `X-Tate-Token` is a *wire contract* between the viewer and the Worker — renaming it is a synchronized two-sided deploy for zero user-visible benefit | ✅ never | — |

---

## §4 · SEQUENCE — one ordered list, the rename lands on her at most once

| # | Step | Rev? | The deterministic check that proves it (existing tool first) |
|---|---|---|---|
| **1** | `git bundle create ../fernwood-pre-scrub.bundle --all` | — | `git bundle verify` on the bundle |
| **2** | Decide the Bob question (§2a-i). If rewriting: scrub the 44 unpushed commits **before any push** | yes (step 1) | `git grep -il "\bbob\b" $(git rev-list --all)` returns only the 3 Bob-Moesta files |
| **3** | Move third-party scoping docs to a private sibling; **register it in `guard-secret-push.py`'s `NEVER_PUBLIC`** | yes | the guard's own `--selftest`; then `git grep -il "\bbob\b"` in the public tree |
| **4** | **Push.** The 44 commits land, the hold releases | ⛔ **no** | `python3 tools/check-live.py --wait 180` |
| **5** | Add `--base` to `check-live.py`; declare the 18-key localStorage roster + its drift guard | yes | the new guard fails on a planted 19th key (positive control) |
| **6** | `[env.qa]` + its own KV namespace; `/health` returns `env` + KV-id tail; `WORKER_BASE` derived from hostname | yes | `curl …-qa.workers.dev/health` shows `env:"qa"` and a **different** KV tail |
| **7** | Cloudflare Pages QA project (branch `staging`), Access policy on | yes | `check-live.py --base <pages.dev>` green; then a **write** test that refuses to run unless `/health` says `qa` |
| **8** | Prose + docs rename; local path rename **with a symlink at the old path**; fix the 8 + 2 + ~16 executable references in stages | yes | `tools/check-loop-docs.py`; launchd: `launchctl list \| grep com.fernwood`; `python3 tools/*.py --selftest` across the 11 |
| **9** | Worker deployed under the new name, **old name still live** | yes | both `/health` endpoints answer; KV-id tails **match** (proves the data followed) |
| **10** | ⏸ **PAUL'S GATE — the custom domain.** Decide *before* step 11, because it decides whether step 11 is her last URL change ever | — | — |
| **11** | **ONE PUSH:** repo rename + `LIVE_BASE` + `LIVE_VIEWER` + forwarding repo + `GITHUB_REPO` secret re-set | ⛔ **no** (her link breaks) | `check-live.py --wait 180`; then 🔴 **exercise `POST /api/promote-species` end-to-end** — the only thing that proves `GITHUB_REPO` is right, because its failure is silent |
| **12** | **In person with Mom:** re-link her home screen. If step 10 said yes, do the origin move **in this same visit** — drain `feedbackOutbox`, confirm `zones.lastSyncedAt ≥ savedAt`, re-set A+, record old→new `deviceId` in `people.json` from his own observation | ⛔ **no** | on her phone: A+ renders; a test note returns 2xx; `/api/feedback` GET shows it |
| **13** | Directory split (`engine/` + `instance/`) + `ENGINE-MANIFEST.md` + checker | yes | the checker classifies 100% of tracked files; **no file is unclassified** |
| **14** | ⭐ Build `instance-condo/` with zero plant data — **run the "no garden" falsifier** | yes | it renders without editing anything under `engine/` |
| **15** | Repo split — **only if 14 passed** | staged | `check-engine-sync.py` byte-identity across both repos |
| — | Variable names | — | never |

**Steps 4, 11 and 12 are the only irreversible ones, and only 11-12 touch her — once.**

---

## §5 · WHAT I DID NOT DECIDE — Paul's calls

1. **The Bob question**: accept the 44 commits' history, or rewrite before pushing. I recommend
   rewriting and I flag that the window closes at the push — but the third-party-consent judgment is his.
2. **What to do about Bob's full name already being public in `9d32aaa`** (finding 0a). It is live now.
3. **The custom domain** — the single decision that determines whether step 11 is her last URL change.
4. **Whether the inversion happens at all**, and whether the build step is an acceptable price.
5. **The engine's name.** `VOCABULARY.md` rules out the obvious candidates; naming is `content-steward`'s.
6. **Whether the instance is `Fernwood-Tracker` or `Fernwood`** — a §2c consequence, not a rename detail.
7. **Which `.private/` door** (bundle / private repo / object store) — and R7's auth is its own document.
8. **Whether `user-researcher`'s "model the condo, don't ship it" caution overrides the expansion sequence.**

## §6 · OPEN QUESTIONS

1. Does the GitHub account already have Pro, or would §2(b) be a new $4/mo line? (I verified the plan
   *requirement*, not Paul's plan.)
2. Is there an intent for the Cloudflare Pages QA project to ever become prod, or is it QA-only forever?
   That answer changes whether §1.1-S3 is a permanent second host or a temporary one.
3. Should the QA Worker share the **Anthropic key** with prod? A QA agent driving `/api/chat` is real spend.
4. Does `tateTracker.sync.v1`'s pasted token exist on Mom's phone today, or has she never been paired?
   It decides whether the origin move costs her a token re-paste.
5. Is `instance-condo/` acceptable as a throwaway directory in the public repo for the falsifier run,
   given nothing about the condo is public-safe yet?
6. Who owns the **forwarding repo** at the old name long-term — does it stay forever, or get deleted
   once she's re-linked?
7. Is the 743 MB `.private/` figure stable, or still growing at the rate that turned 436 into 743?
