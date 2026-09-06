# Migration readiness — the DEVELOPMENT STATE, measured

**Reviewer:** engineering-partner · **Written:** 2026-09-06, measurements taken 22:20–22:45 UTC (18:20–18:45 ET)
**Question this feeds:** move Mom onto production of the estate manager, then sunset and lock her out of the
Fernwood she uses today — *what is actually built, what actually blocks it, and what does the sunset require.*
**Mode:** review · read-only · nothing committed, pushed or deployed by this pass.

> ⚠️ **HEAD MOVED TWICE WHILE THIS RAN.** At start HEAD was `6d94a9a`; at 18:30:59 another session committed
> `79a31c8`, at 18:37:31 `6f13139`, at 18:38:50 `2a476f4`. A **production deploy also ran at ~18:38** (that is
> what `2a476f4` records). Every claim below carries its measurement time; anything about a deployed build is
> true as of the stamp and not after. Three sessions share this tree tonight — re-measure before acting.

**Evidence grades used:** `measured` (a named command/file establishes it) · `inferred` (follows from measured
facts, not directly observed) · `assumption` (stated so it can be shot down).

---

## 0 · The one-paragraph answer

The new product is **further along than the paperwork suggests and its deployment story is weaker than its code**.
Five surfaces exist and are live on a genuinely empty production estate; the identity, grant and revocation
machinery is real; the isolation model is proven at the binding level. But **not one countable end-to-end journey
run exists against production** — all 12 countable runs are on QA, and the newest run at every one of the four
seats is REFUSED. The single hardest blocker is not a missing feature; it is that **no Worker in this project can
say which code it is running**, so "is the production Worker current?" is answerable only from a human transcript.
Separately, the red gate everyone is treating as the migration blocker — `qa-divergence.py`'s fast-forward
assertion — is **enforcing a procedure tonight's ruling retired**, and will now be red forever. The sunset is
achievable as designed and the "frozen data control" and "locked out" goals do not actually conflict — but the
control **is not currently frozen** (a cron bot rewrites its branch every six hours) and the real data-loss
surface is on Mom's phone, not in KV.

---

## 1 · What is actually built, and where does it live

### 1.1 The environment table — read live, 18:42 ET `[measured]`

`worker/wrangler.toml` declares six environments; every one answers and every one reports its own identity.
Command: `curl <worker>/health` per env · `curl <origin>/qa-build.json?cb=…` per Pages project.

| env | Pages origin serves | Worker `/health` | estate | Worker code version |
|---|---|---|---|---|
| **`home` = the new PRODUCTION** | `6f13139` @ 18:37:59 | `env:home` `kv_canary:home` | `est-e6696a` | ⛔ **no instrument can say** |
| `qa` | unreadable (Cloudflare Access, by design) | `env:qa` `kv_canary:qa` | `est-qa0001` | ⛔ no instrument |
| `lab` (dev) | `9ef14d1` @ 09-05 22:39 | `env:lab` `kv_canary:lab` | `est-lab0001` | ⛔ no instrument |
| `bob` (test rig) | `b784dc9` @ 12:12 — **32 commits behind HEAD** | `env:bob` `kv_canary:bob` | `est-9a74df` | ⛔ no instrument |
| `paul` (test rig) | `ebdf172` @ 14:52 — **12 behind HEAD** | `env:paul` `kv_canary:paul` | `est-d93508` | ⛔ no instrument |
| **legacy Fernwood (Mom's)** | GitHub Pages @ `origin/main` | `env:production` `kv_canary:production` | `est-3c9f1a` | ⛔ no instrument |

Six distinct KV namespace ids, six distinct estate ids, and each Worker's `kv_canary` is **read from its bound
namespace rather than re-typed** — so the binding-level isolation is not asserted, it is proven per request.
That is the strongest thing in this system and it should be said out loud. `[measured — /health on all six]`

### 1.2 Mom's live instance — verified byte-for-byte `[measured]`

`palekxk.github.io/Tate-Tracker/viewer.html` serves **2,047,188 bytes**, which is exactly
`git show origin/main:viewer.html | wc -c`. The local working-tree `viewer.html` is 2,078,223 bytes — a
different file. So her page is `origin/main`'s build and nothing local has leaked to her. `last-modified`
is 2026-09-06T20:04:20Z, i.e. the bot commit `294c0b4` republished her site 2.5 h ago (bytes unchanged).

### 1.3 The estate manager — the surface inventory

Five tracked surfaces, all served on production, all confirmed 200 with real HTML at 18:20 ET `[measured]`:

| surface | file | on `home` |
|---|---|---|
| arrival / onboarding | `onboarding/index.html` (113,851 B served) | ✅ |
| the estate view | `estate/index.html` (30,824 B served) | ✅ |
| the shelf (many places) | `homes/index.html` | ✅ |
| place settings | `settings/place/index.html` | ✅ |
| account settings | `settings/account/index.html` | ✅ |

The production estate `est-e6696a` holds **exactly 1 key (`env-canary`)** — verified three times today
(`.private/kv-exports/prod-reset-2026-09-06T{095204,165612,180236}.json`, each `values: len=1`). **The blank
slate is real and current.** `[measured]`

### 1.4 Proven vs. committed vs. deployed — the three are not the same here

- **Committed and deployed and proven:** the promotion of production on 2026-09-05 ~23:00 at `bce212a` —
  `.plans/2026-09-05-production-promotion-PLAN.md` records S1–S6 passing, each verified against the world,
  including `handoff` and `complete` events landing in `est-e6696a`, sign-in returning the record, and the
  estate reset back to 1 key. That is a genuine end-to-end production proof. `[measured — the plan's own
  stage-note, corroborated by the reset dumps]`
- **Committed and deployed, NOT proven:** everything on production since. The page moved `bce212a → c111417 →
  9cb468d → 6f13139` today; **zero countable walks ran against `home` at any of those builds** (§2.1).
- **Committed, deployed nowhere:** `79a31c8` (18:30 tonight) — the `sanitizeZone` fix (§4.5). Present at HEAD,
  absent from every build that was live when measured.
- **Fixture, not proof:** `.private/walk-sessions.json` holds four synthetic accounts minted **at 18:25–18:27
  tonight, all against `qa`** (`owner@qa`, `mom@qa`, `strict@qa`, `wide-eyed@qa`), with live tokens in
  plaintext. Useful evidence about QA; says nothing about production. `[measured]`

---

## 2 · What genuinely stands between here and "Mom on the new production instance"

Ordered by what actually blocks. **E** = engineering can close it · **P** = needs Paul.

### HARD BLOCKERS

**B1 · No countable journey evidence exists on production. `[measured]` — E**
`python3 tools/walk-integrity.py` at 18:35 ET: **53 runs · 12 countable · 41 refused.** Breakdown by env:
`qa` 33 runs / **12 countable**; `home` 14 runs / **0 countable**; `lab` 2 / 0; unknown 4 / 0. The three
countable shas are `3b7d7be`, `fae767e`, `9112b4b` — all QA, all ≥ 5 commits behind HEAD. All 14 `home` runs
were on 2026-09-05 at `090a42a` and every one is REFUSED (`report-unwritten`, plus
`prose-contradicts-status` on three screens where `page.fill: Timeout` was recorded as *walked*).
And: **the newest run at all four seats is REFUSED** — the tool says so itself in its closing line.
*Why it blocks:* the release cascade puts Mom at gate 3. Gate 1 is a passing journey on the build she will
load. There is no such run, on the environment she will load, at any build. The 09-05 promotion proof is real
but it expires when the build moves, and the build has moved four times since.
*Shape of the fix:* one clean `journey-walk` per seat against `home` at the sha `home` is serving, with
`walk-integrity` reporting them countable — then `reset-production-estate.py --estate est-e6696a` to return
the slate to 1 key, exactly as S3→S6 did on 09-05. That sequence is already written and already worked once.

**B2 · Nothing can establish which code the production Worker is running. `[measured]` — E**
No Worker exposes a build stamp. `/health` returns `env`, `kv_canary`, `estateId`, `legacyBefore`,
`chat_budget`, `endpoints`, `configured` — **all echoes of the deploy-time bindings, none of the code.**
Pages origins each carry `qa-build.json` (written by `tools/pages-deploy.py`); the Worker half has no
counterpart. Proof that this is not theoretical: `.plans/2026-09-06-state-and-next-steps-AUDIT.md:38–52`
records a **false SECURITY finding that came within fifteen minutes of being filed** about `56c5b0d` (the
login-path privilege-escalation fix), and what caught it was a human-authored transcript plus
`wrangler versions view` — *"no read-only instrument in this repo could have answered the question either
way."* That is still true tonight, and tonight it is load-bearing: a production deploy ran at ~18:38 and I
cannot confirm from outside that it carried `79a31c8`.
*Why it blocks:* handing Mom a link means asserting production runs current code. Right now that assertion
rests on a transcript. The audit trail for a security fix should not be prose.
*Shape of the fix, and it is small:* set `BUILD_SHA` at deploy (`wrangler deploy --env home --var
BUILD_SHA:$(git rev-parse HEAD)`), echo it from `/health`, and make `deploy-worker.sh` step [4/4] assert it
equals the sha it just shipped — the same shape step [4/4] already uses for `env`. This retires the whole
class, and it directly serves *"a deploy-bundled artifact needs a rebuild-and-diff drift alarm"*
(engineering-principles/fernwood.md) which the Pages half already honours and the Worker half does not.

**B3 · The invite is Paul's outbound act, and the copy has never been read by a content seat. `[measured]` — P**
`.plans/2026-09-05-onboarding-PLAN.md:8` — *"content-steward → waived: FOR NOW, and this is a DEBT not a
judgement — every word on `onboarding/index.html` and the invite message is Mom-facing authored content and
no content seat has read either; must not stay waived past gate 2."* Gate 2 is Paul's own walk, which per the
same plan (`:52`) has not happened. `onboarding/invite-message.md` is still stamped
*"⛔ DRAFT. Nothing here has been sent."*
*Not an engineering blocker* — but it is on the critical path to the one act that starts the migration, and
it is a Paul/content decision, not a code one.

**B4 · Production's Worker has none of the three external capabilities Mom's current one has. `[measured]` — P**
`/health.configured` on `fernwood-home`: `airnow:false · ambient:false · anthropic:false · github:false`.
On the legacy `fernwood`: `airnow:true · ambient:true · anthropic:true · github:true`.
So on the new production instance **Garden Guru cannot answer** (no `ANTHROPIC` key, despite
`CHAT_DAILY_BUDGET_USD = "10.00"` being provisioned for it), the on-site weather station is unreachable, and
air quality is unreachable. `[measured]`
*Grading this honestly:* the five household surfaces are onboarding/estate/shelf/settings — **none of them
appears to call Guru or weather** `[inferred — not verified by reading their fetch lists]`. So this may be
correctly *not yet* rather than *broken*. But it needs to be a decision, not a discovery: if Mom's first
week on the new instance is meant to include Guru, three secrets have to be installed and Guru re-proven
there, and that is Paul's act (`wrangler secret`), not an agent's. **No `GITHUB_TOKEN` on `home` is
deliberate and correct** — `wrangler.toml` explains that `GITHUB_BRANCH` defaults to `main`, so a token
there would promote species onto Mom's live legacy branch.

### NOT BLOCKERS — and one of them is being treated as one

**N1 · `qa-divergence.py --check` is red, and it is enforcing a retired procedure. `[measured]` — needs Paul's word**
Measured 18:22 ET: exit 1, message *"the migration cannot fast-forward — back-merge origin/main into the
staging line before anything else"*, blocked by `294c0b4 weather-history: rollup update`. **This is a stale
gate, not a blocker.** Its assertion comes from the 2026-09-04 ruling that *"the migration IS a fast-forward
— `git push origin staging:main` ships the exact sha QA served"* (`BACKLOG.md` §FOCUS FREEZE). Tonight's
ruling retires that mechanism: Mom's Fernwood stays exactly as it is as a frozen data control, `home` stopped
shipping `viewer.html` at `9cb468d`, and the new production is `fernwood-home.pages.dev` serving the neutral
shell. **If `origin/main` is never to move again, then `staging → main` is not the migration and this gate is
asserting an invariant that no longer matters.** It is also now *permanently* unsatisfiable: the weather
recorder pushes to `main` every six hours forever (§4.1), so the fast-forward window is at most six hours
wide and unattended. A gate that is red forever teaches you to read past red, which costs you the next real
red. This is the highest-value cheap fix in the whole review: **re-scope it or retire it, tonight, with
Paul's word on what `origin/main` now means.**

**N2 · Held feedback is one arrival. `[measured]`**
`.private/mom-feedback-state.json` has `lastReviewedTs: 2026-08-20T13:31:14.649Z`. The frozen archive holds
20 feedback entries across 10 dates; **exactly one** post-dates that watermark (`2026-09-03T20:43:03Z`). The
freeze's "backlog of unread arrivals" is a single item. Cheap to honour, cheap to pour into the new instance.

**N3 · `_qaFixture` markers: 0 at HEAD — but see §5.2 before believing it.**

**N4 · The two test rigs are stale but empty. `[measured]`** `bob` 32 commits behind, `paul` 12 behind. R2 of
`.plans/2026-09-06-one-environment-DECISIONS.md` already named this ("*already overdue*"). Both hold no real
data, so migrating them is a no-op — correctly ruled. Staleness matters only because a walk against a stale
rig produces evidence about a build nobody serves.

---

## 3 · What the sunset requires technically — and does the tension resolve?

**The tension resolves, because "the data control" and "the URL" are two different objects.** `[inferred,
and I am confident]` The control that has evidentiary value is (a) the KV records of her use and (b) the exact
bytes she was served. Both are already immutable and independent of whether anyone can reach the site:

- **(a) is archived. `[measured]`** `.private/frozen-fernwood-archive/frozen-2026-09-06T000836.json` —
  **175 keys, `unreadable: []`**, namespace `100f2b95…`, estate `est-3c9f1a`, taken 2026-09-06 00:08 ET.
  Composition: `metrics:<date>` ×91 · `cost-log:<date>` ×22 · **`feedback:<date>` ×10 (20 entries)** ·
  `zone-audio:<date>` ×3 · `conversation:<id>` ×38 · `env-canary` · plus 4 prefixed keys
  (`est-3c9f1a:observations`, `est-3c9f1a:zones:all`, two ambient caches). Earliest 2026-05-20, latest
  2026-09-05. `archive-frozen-estate.py` has **no delete path by construction** and says so — good design.
- **(b) is pinned by git.** `origin/main`'s `viewer.html` is 2,047,188 bytes and is what she is served
  (§1.2). Git preserves it whether or not Pages serves it.

**So the sunset is: preserve the two artifacts, then remove the serving surface and the credential.** Both
"locked out" and "unchanged" can be true. The ordered technical requirements:

1. **Re-run the archive at the moment of cutover, then `--verify`. `[measured gap]`** The existing archive is
   **~22.5 h stale** and her instance has been live and writable the whole time. `archive-frozen-estate.py
   --verify` exists for exactly this. A sunset without a *fresh* verified archive is, in the tool's own words,
   *"a deletion with a plan attached."*
2. ⛔ **Drain her device first — this is the only irreversible data loss in the whole plan. `[measured]`**
   `viewer.html` touches **19 `tateTracker.*` browser-storage keys**. Two of them are outboxes that exist
   *nowhere else until they flush*: `tateTracker.feedbackOutbox.v1` (`viewer.html:11552` — *"held until a
   2xx"*) and `tateTracker.door.outbox.v1` (`:7125` — *"door events buffered offline, flushed on the next
   in-range load"*). Four more are her ask-stack state: `momQueue.answered/offered/general/snoozed.v1` —
   **grepping `viewer.html` finds no network payload that carries `momQueue`**, so that state is device-only.
   Whether its *content* is duplicated server-side via `/api/feedback` is `[inferred — unverified]`; the
   *outboxes* are unambiguously device-only until flushed `[measured]`.
   **None of the five new surfaces reads any `tateTracker.*` key** (grep: 0 hits in all five) — they use 11
   `fw-*` keys. That is correct under the blank-slate ruling, but it means **nothing carries her device state
   across, so anything unflushed at lockout is gone.**
   *The cheap remedy, and it is Paul's:* have her open the legacy app once while online immediately before
   cutover so both outboxes flush, then re-run the archive and confirm the new entries landed. One phone tap
   is the difference between a sunset and a silent deletion. `check-storage-keys.py`'s own header states the
   principle — *"a key the origin-move migration does not know about is a key she loses"* — and it is green
   today (19 rostered, 18 literals, every `fw-*` key declared), so the roster is trustworthy; it is the
   *carrier* that does not exist.
3. **Stop the two bots writing to `main`, or the control keeps moving. `[measured]`** §4.1.
4. **Revoke the credential, which is what actually locks her out.** Her page authenticates to the legacy
   Worker with the master `SHARED_TOKEN`. Rotating that secret on the top-level Worker (`wrangler secret put
   SHARED_TOKEN`) is the act that ends her write and read access — and it touches neither `origin/main` nor
   the archive. Note `/api/metrics` already returns `{"error":"unauthorized"}` to an unauthenticated caller
   `[measured]`, so the read paths are genuinely gated and rotation genuinely closes them.
5. **Remove the URL last, and only if Paul wants it gone.** Disabling GitHub Pages (or repointing Pages at a
   branch other than `main`) removes the surface **without modifying `main`** — which is the version that
   preserves the control most exactly. Editing `viewer.html` on `main` to add a redirect would *mutate the
   control* and should be rejected for that reason. ⚠️ And be plain about the limit: the repo is public, so
   the *bytes* stay readable at github.com regardless. "Locked out" means her app stops working, not that the
   content becomes private.
6. **Tag the frozen sha** (`git tag frozen-fernwood-2026-09-06 <sha>`) so the control is addressable by name
   and not by a line in a document. Cheap; makes the control legible to future-Paul-with-Claude.

⚠️ **One trap in the sunset toolchain. `[measured]`** 171 of the 175 keys in the legacy namespace are
**unprefixed** (`feedback:2026-07-13`, not `est-3c9f1a:feedback:…`). `reset-production-estate.py` enumerates
*under an estate prefix*. Pointed at `est-3c9f1a` it would see **4 of 175 keys** and could report near-empty
about a store holding everything she ever wrote. The tool is not designed to be run there and its refusals
are strong, but the mismatch is worth knowing before anyone reaches for it. `check-household-isolation.py`
reports the same fact from the other side: *"production LEGACY_BEFORE=2026-09-04 → 19 kinds share ONE
unprefixed key across households."*

---

## 4 · Deploy topology — failure modes

### 4.1 ⛔ The bot-writes-to-`main` blocker is a DESIGN FAULT, and the documentation misidentifies it. `[measured]`

`BACKLOG.md:108` attributes the fast-forward blocker to *"the deploy bot commits a digest rebuild to main
after every prod Worker deploy — that one commit was the only fast-forward blocker."* That is the wrong bot.
Measured on `origin/main`'s log:

- `weather-recorder[bot]` — **447 commits**, `record-weather.yml`, **`cron: "0 */6 * * *"`**, plus
  `analyze-weather-bias.yml` weekly. Both end in `git push` to the default branch.
- `fernwood-deployer[bot]` — 38 commits, `deploy-worker.yml`, event-driven, `[skip ci]`.
- Tonight's blocker `294c0b4` is a **weather-recorder** commit. The last eleven commits on `origin/main` are
  *all* bot commits.

So the blocker is not an occasional consequence of deploying; it is a **cron that fires four times a day
forever**. The fast-forward window is ≤ 6 h and unattended, which is why it has blocked twice today. The
design fault is precise: **an unattended writer owns the branch a human procedure must fast-forward from.**
*Why the shape is wrong:* a fast-forward is a claim that one line strictly contains another. Giving a robot
commit rights to the trailing line makes that claim expire on a timer. The remedies, in increasing cost:
(i) retire the fast-forward as the migration mechanism (which tonight's ruling already implies — §N1) and the
problem evaporates; (ii) point the two weather workflows at a data-only branch, or write the rollup to KV
through the Worker instead of to git — the recorder already reads the station *through* the Worker, so it is
one hop from not needing git at all; (iii) keep the back-merge chore and accept that it is a chore forever.
**(i) is almost certainly right and costs a sentence from Paul.**

⚠️ **Second-order consequence nobody has named:** because `record-weather.yml` pushes to `main`, **GitHub
Pages republishes Mom's "frozen" site every six hours** (`last-modified: 2026-09-06T20:04:20Z`, matching
`294c0b4` — `[measured]`). Her `viewer.html` bytes are unchanged, but `weather-history.json` — which her page
fetches at runtime — changes on that cadence. **The frozen data control is not frozen.** For weather that is
arguably harmless (the signal is exogenous), but a control whose inputs move is a control with an asterisk,
and the asterisk should be written down before it is used as evidence.

### 4.2 ✅ The default-targets-the-frozen-instance hole was closed today, and closed well. `[measured]`

`dedf849` rewrote `tools/deploy-worker.sh`: `--env` is now required with no default; `prod`/`top`/`fernwood`
are refused unless `--i-mean-the-frozen-fernwood` is passed; the environment roster is **parsed out of
`worker/wrangler.toml` rather than typed** (and refuses with `UNCHECKABLE` if it parses zero); the health
check derives its URL from the target and **exits 1 if `/health.env` disagrees with what was deployed.** It
even records that `mapfile` was avoided because macOS ships bash 3.2 and *"a guard that cannot run is not a
guard."* This is exactly the shape the principle library asks for and it deserves saying: **praise.** The
prior state — a bare `wrangler deploy` that hit `est-3c9f1a` and then printed OK from that same frozen
URL — was the single most dangerous default in the repo.

### 4.3 ⛔ The Worker deploy path still has NO tenancy gate. `[measured]` — DECISIONS F1 is only half-closed

`deploy-worker.sh` runs `build-digest.py` → `check-digest-fresh.py` → deploy → `/health`. That is a
*freshness* gate and an *environment* gate. It runs **no isolation, tenancy, or estate check at all** —
`check-household-isolation.py` is not called by it, and (§5.1) is not called by anything. Meanwhile
`pages-deploy.py` calls `check-estate-neutral.py` **in-process** before shipping a household export, and
refuses on a hit. So the *page* half is gated and the *Worker* half — where the entire multi-household
conversion lives — is not. F1's headline ("takes no `--env`") is fixed; F1's substance ("*a falsifier you
cannot gate a deploy on is a report*") stands.

### 4.4 🔴 Cloudflare's edge is still serving Fernwood's canon from the production household origin. `[measured]`

This is the finding I would not have gotten from any check in the repo, and it is the cleanest possible
illustration of *template parity ≠ serving parity*.

The `9cb468d` conversion is correct: `home` joined `HOUSEHOLD`, the export is pruned to the eight-file
allow-list, and `check-estate-neutral.py` runs against the export and passes (311 needles, zero hits —
verified by running it, exit 0). Fetching a non-allow-listed path **with a cache-buster** returns the
252-byte redirect stub, as designed.

**Fetching it without a cache-buster does not.** Measured 18:33 ET:

| URL on `fernwood-home.pages.dev` | bytes | `cf-cache-status` | `age` |
|---|---|---|---|
| `/BACKLOG.md` | 531,505 | **HIT** | 23,253 s |
| `/plants.json` | 314,203 | **HIT** | 23,250 s |
| `/CLAUDE.md` | 93,070 | **HIT** | 23,253 s |
| `/tools/momlib.py` | 91,971 | **HIT** | 23,254 s |
| `/property.json` | 33,240 | **HIT** | 23,251 s |
| `/onboarding/invite-message.md` | 3,562 | **HIT** | 23,270 s |
| `/viewer.html`, `/vehicles.json`, `/zones.json`, `/MOM-CYCLE-LOG.md`, `/estate.json`, `/instance/fernwood.json`, `/people.json`, `/worker/digest.json`, `/guides/*` | 252 (stub) | none | — |

`cache-control: public, s-maxage=604800` — **seven days.** The cached objects are from ~12:06 ET and
**survived the 18:10 deploy**, which establishes the mechanism: *a new Pages deployment does not purge the
edge cache for a `pages.dev` host*. The leak set is exactly the URLs someone requested before the conversion.

*Grading it honestly at Paul's stakes:* **important, not critical.** The repo is public, so those same bytes
are already readable at github.com — no secret is disclosed, and the highest-value file (`viewer.html`, with
the street address) is **not** in the cache. What is genuinely wrong is (a) `onboarding/invite-message.md` —
an unapproved outbound draft whose own first line says *"Nothing here has been sent"* — is publicly readable
**on the very origin a reader is sent to**, which is the exact defect `9cb468d` was written to fix and which
it did not actually clear; and (b) the claim *"the household export is neutral"* is true of the **export** and
false of the **origin**, and the check only ever knew about the export.

*Shape of the fix, and it is the general one:* **`pages-deploy.py`'s verify-by-use step should verify a
negative, not just a positive.** It already polls `/qa-build.json` until the origin reports the sha — the
right instinct, half-applied. Add: for a household env, fetch a short roster of known-non-allow-listed paths
**without a cache-buster** and assert each returns the stub. That turns "we pruned the export" into "the
origin does not serve it", which is the thing anyone actually cares about. Derive the roster from the files
`git archive` produced and then removed — so it can never rot as files are added (the F2 control, applied to
the one instrument that was measuring the wrong side of the boundary). For the existing 7-day window: a
`pages.dev` host is in Cloudflare's own zone and Paul cannot purge it, so the practical options are wait it
out (expires ~2026-09-13), or serve Mom's production from a hostname that has never served the canon.

### 4.5 ⛔ A data-destroying defect is live on every deployed build, including Mom's. `[measured]`

`79a31c8` (18:30 tonight) fixes `sanitizeZone`, which rebuilds a zone from a fixed key list and therefore
**dropped `partOf` and `provenance`** — two fields schema v3 added on 2026-09-01. `handleZoneSave` writes
`body.zones.map(sanitizeZone)` **wholesale** to `zones.json` via the GitHub API, to the KV `zones:all` key,
and back into `viewer.html`'s inlined `ZONES_DATA`; the client posts the entire zone set on every save. So one
rename, drag or added place stripped both fields from canon **and committed the deletion**. Already measured
in that commit: *"`the-green` is the only zone of 23 carrying them."* The trigger is reachable by Mom.

Two things make this a topology finding rather than a bug report:
1. **`check-data-inline.py` could not see it** — the Worker writes `zones.json` and the inlined copy from the
   *same* sanitized object, so both sides were stripped consistently and the equivalence check read green.
   A parity check between two artifacts produced by one function cannot detect that function losing data.
   This is the strongest example in the repo of a check that is green while the thing it checks is wrong.
2. **The fix is deployed nowhere as measured.** `home`'s page moved to `6f13139` at 18:37:59 and the
   `2a476f4` commit records a production deploy, so the Worker *may* now carry it — **but B2 means that
   cannot be confirmed**, and the legacy Worker Mom uses tonight certainly does not.

The general rule the commit itself names is worth promoting: **a field whitelist at a storage boundary is a
copy of the schema, and it drifts silently every time the schema moves.** `zones.json`'s own
`_meta.fold_2026_08_31` predicted it in writing and it still happened.

### 4.6 ⚠️ Two more instruments that answer from a hand-typed roster `[measured]`

- **`/health.endpoints` is a hand-written literal of 21 routes.** The Worker's actual route table has **28**
  `url.pathname ===` branches, and the missing ones include the entire account/session/onboarding surface.
  Worse for my purposes tonight: the literal is **byte-identical at `bce212a` and at HEAD**, so it cannot be
  used to date a deployment — I tried. An endpoint roster that neither derives itself nor changes is
  decoration. (`grep -c 'url.pathname === "' worker/worker.js` = 28.)
- **`qa-divergence.py` reads `origin/main..origin/staging` — remotes only.** Local `main` is currently **11
  commits ahead of `origin/staging`** (`git rev-list --count origin/staging..HEAD`), and QA was deployed
  tonight from the *working tree* at `2fc2b71`, which is not on `origin/staging`. So the divergence ledger
  **under-reports by 11 commits**, including the entire one-environment conversion. Its own premise —
  *"`staging` is main-in-waiting and the migration ships the exact sha QA served"* — is false right now: the
  sha QA served is not on `staging` at all. `[measured]`

---

## 5 · The real state of the gates

### 5.1 The census — 5 of 30 checks have a caller `[measured]`

Counted by grepping `.github/` and `.git/hooks/` for every `tools/{check,qa,walk,guard}-*` script:

| gate | CI | git hook | verdict |
|---|---|---|---|
| `check-data-inline.py` | ✅ build-viewer.yml | — | wired (but see §4.5 — it cannot see the bug it was nearest to) |
| `check-digest-fresh.py` | ✅ both deploy workflows | — | wired |
| `check-live.py` | ✅ deploy-worker-qa.yml | — | wired (QA origin, with Access headers) |
| `check-public-build.py` | ✅ build-viewer.yml | ✅ pre-push | wired both sides |
| `check-qa-fixtures.py` | ✅ build-viewer.yml | ✅ pre-push (main/prod refs) | wired both sides — but see 5.2 |
| **`check-household-isolation.py`** | — | — | ⛔ **no caller anywhere** |
| **`check-estate-neutral.py`** | — | — | called in-process by `pages-deploy.py` only |
| `qa-divergence.py`, `walk-integrity.py`, `check-storage-keys.py`, `check-config-derivation.py`, `check-engine-manifest.py`, `check-vocabulary.py`, `check-telemetry.py`, `check-domains.py`, `check-condo-falsifier.py`, `check-text-size-default.py`, `check-backlog-*`, `check-cards.py`, `check-cycle-map.py`, `check-mom-ack.py`, `check-ux-sweep.py`, `check-arrival-dispositions.py`, `check-loop-docs.py`, `check-season-notes.py`, `guard-concurrent.py`, `qa-walk.py`, `qa-write-probe.py`, `walk-brief.py` | — | — | **run only when a session remembers** |

`.git/hooks/pre-push` is the only installed hook (1 file, 1,325 bytes) and it is well-shaped: it runs the
public-build audit on every push and adds the fixture check **only when the target ref is `main` or `prod`**,
parsing the refspec from stdin rather than assuming. Good.

This is the *unwired* leg of the ratified principle **"three ways a gate stops being a gate: unwired,
unconsumed, un-rederived."** 25 of 30 are unwired. That is not automatically wrong — most are cycle
instruments, not deploy gates. But two of them are deploy gates by intent and are unwired anyway:
`check-household-isolation.py` (the R3 falsifier, which `DECISIONS` §R3 says must exist *before* the blind
stretch) and `check-storage-keys.py` (whose subject is *"a key she loses"*).

### 5.2 Gates that can report green while the thing they check is wrong

**G1 · `check-qa-fixtures.py` — green over a roster of one file that nobody has ever marked. `[measured]`**
Its scope is `git ls-tree <ref> instance/` filtered to `.json`. There is **exactly one such file**
(`instance/fernwood.json`). And `grep -rl '_qaFixture'` across the repo finds the marker in **zero** code or
data files — only in the tool itself and in eight prose documents describing it. So the mechanism has never
been used once, and its 0-marker green is *green by absence*, not green by inspection. Meanwhile the actual
QA-only values live where it cannot look: worker vars, the grant register, `.private/synthetic-identities.json`,
the five new surfaces. It is wired into CI *and* a pre-push hook — the two strongest positions in the repo —
guarding a surface with one file in it. *Fix:* either widen the scope to whatever declares reality (the
surfaces `check-storage-keys.py` already discovers recursively — that tool solved this exact problem today,
three times over, and its solution is reusable), or say plainly in its banner that the roster is one file so
its green is never over-read.

**G2 · `check-household-isolation.py` is honest in prose and dishonest in its exit code. `[measured]`**
Its output is exemplary: *"🟡 PARTIAL — 1 of 5 tests genuinely runs (T1); T1b reads the CONFIG, not the store;
3 cannot run until the merged Worker exists"*, and it explicitly says *"⛔ THIS IS NOT A MERGE GATE AND MUST
NOT BE USED AS ONE. T1b can be turned green by editing LEGACY_BEFORE — the same edit that strands the history
it is watching."* That is first-rate engineering and I want it on the record as praise. **But `echo $?` is
0.** So the first person to wire it into CI — which R3 says should happen — gets a green from a 1-of-5 suite,
and every word of the banner is invisible to the machine. *Fix:* exit non-zero (2, "uncheckable") whenever any
declared test is unrun, so the honesty survives automation. This is the same lesson `pages-deploy.py` learned
about QA (*"it says so rather than reporting a green it did not earn"*) — applied to the exit code, not just
the stdout.

**G3 · `/health` cannot fail on the thing that matters.** It asserts bindings, never code (§B2, §4.6).

**G4 · `check-data-inline.py` structurally cannot catch a lossy writer** (§4.5) — both sides of its
comparison come through the same function.

**G5 · The silent-skip hazard is documented and still live.** All three deploy workflows guard on
`if: env.CF_TOKEN != ''`, so a secret under any other name makes the run **green and deploy nothing**. The
workflows say so at length and each emits a named `::warning::`. That is the right mitigation available in
Actions — but a warning in a green run is *awareness, not a guarantee*, and the principle
*"isolation is a guarantee; awareness is a heads-up — never let a safety claim rest on the second"*
applies. The cheap upgrade: fail the job when the token is absent on a branch that is supposed to deploy.
Nothing is lost — a push that cannot deploy is not a success.

### 5.3 Gates that are working, and should be said so

`build-viewer.py --check` exit 0 · `--selftest` in CI · `check-estate-neutral.py` exit 0 with 311 derived
needles and called in-process before every household export · `check-storage-keys.py` exit 0, now
**discovering** household surfaces recursively after being wrong three ways in one day (viewer-only → two
files by hand → one level deep) — that repair sequence is the best worked example of *"generate the
derivable; drift-lint the rest"* in this repo · `pages-deploy.py`'s `git archive` export (an untracked
`.private/` file **cannot** ride along, and it re-checks after the export) · `walk-integrity.py`, which
refuses 41 of 53 runs rather than counting them, and says in its closing line that the newest run at every
seat is refused. A tool that reports its own subject as unproven is worth more than four that pass.

---

## 6 · What I would do tonight, in order

1. **Get Paul's sentence on what `origin/main` now means** (§N1, DECISIONS §4 F5 — still open). Everything
   else in the deploy topology is downstream of it. If it is "frozen forever, never receives `staging`", then
   retire `qa-divergence`'s fast-forward clause and point the weather bots elsewhere in the same pass.
2. **Add `BUILD_SHA` to the Worker and assert it in `deploy-worker.sh` step [4/4]** (§B2). Fifteen minutes,
   retires a class, and stops the next security question being answered from a transcript.
3. **Redeploy the `home` Worker at HEAD and prove it** — `79a31c8` is a live data-destroying defect (§4.5)
   and confirmation that it shipped currently does not exist.
4. **One countable journey per seat against `home`, then reset to 1 key** (§B1). This is gate 1 and it does
   not exist on production.
5. **Add the negative-verification step to `pages-deploy.py`** (§4.4) — verify the origin does not serve what
   the export pruned, not merely that the export pruned it.
6. **Before any lockout: have Mom open the legacy app once, online, then re-run
   `archive-frozen-estate.py` and `--verify`** (§3.2, §3.1). The outboxes are the only irreversible loss.
7. Then the sunset acts in order: rotate `SHARED_TOKEN` → tag the frozen sha → disable Pages (never edit
   `main`) → stop the bots.

Items 1, 6 and the invite copy (§B3) are Paul's. 2, 3, 4, 5 and 7's mechanics are engineering.

---

## 7 · Principles this surfaced — proposed, not added

Per standing practice these are proposals; nothing is written to `~/.claude/engineering-principles/` without
Paul's confirmation.

1. **A deployment must be able to name the code it is running, not just the config it was given.**
   *Why:* `/health` echoed `estateId` and `legacyBefore` correctly for days while nothing could say whether
   the *code* was current, and a false security finding got within fifteen minutes of being filed on the gap.
   *When it applies:* any deploy target — Worker, Pages, container. *Avoid:* treating a config echo as a
   version stamp; verifying a deploy only by its own success line. Scope: cross-project.
2. **Verify the negative at the boundary you are claiming to close.** *Why:* the household export was proven
   neutral and the origin served the canon anyway, from a 7-day edge cache a redeploy does not purge.
   *When:* any allow-list, prune, redaction or exclusion. *Avoid:* proving the artifact and inferring the
   surface. Scope: cross-project. (Sibling to the ratified *"isolation is a guarantee; awareness is a
   heads-up."*)
3. **A field whitelist at a storage boundary is a copy of the schema, and it drifts silently.** *Why:*
   `sanitizeZone` deleted `partOf` and `provenance` from canon on every save for five days, and the parity
   check could not see it because both sides came through the same function. *Avoid:* rebuild-from-key-list
   at a write boundary without a round-trip test that adds an unknown key and asserts it survives. Scope:
   cross-project, and it belongs beside the promoted *"build script that overwrites a hand-edited artifact
   must reconcile membership."*
4. **A robot must not own the branch a human procedure depends on.** *Why:* a 6-hourly cron blocked the
   migration fast-forward twice in one day and will block it forever. *Avoid:* granting an unattended writer
   push rights to a release line. Scope: fernwood, promotable.
5. **An honest banner must be matched by an honest exit code.** *Why:* `check-household-isolation.py` says
   "🟡 PARTIAL, 1 of 5, do not use me as a gate" and exits 0. *Avoid:* leaving the caution in stdout where
   only humans read it. Scope: cross-project. (This is the *un-consumed* leg of the ratified three-ways rule,
   seen from the tool's side rather than the caller's.)

---

## 8 · Open questions for Paul

1. **Does `origin/main` ever move again?** Everything in §4.1 and §N1 turns on this one word.
2. **Is Guru (and the weather station) part of Mom's first week on the new instance?** If yes, three secrets
   and a re-proof; if no, say so and stop reading `configured:false` as a defect (§B4).
3. **Is the legacy URL taken down, or left up and merely de-credentialed?** Both preserve the control; only
   the first stops her app being reachable at all (§3.5).
4. **Does the frozen control's asterisk matter to you?** `weather-history.json` moves every six hours; if the
   control is meant to be evidentiary, that should be stopped or written down (§4.1).
5. **DECISIONS §4 is still open on F5's sentence** — tonight's ruling appears to answer it ("the production
   home is her blank slate", and `9cb468d` acted on it), but it has not been recorded as answered where the
   decision lives.
