# MOVING PAUL'S REVIEW GATE FROM PRODUCTION TO QA — the mirror, what it takes to make QA one, and the class that survives a perfect mirror · DESIGN

- row: process (no BACKLOG row — same posture as the 09-04 wiring audit and the 09-06/09-07 audits)
- objective: O5
- class: engine · declared (process machinery; nothing here ranks a feature, a module or an item)
- seats: practice-steward (this file)
        engineering-partner → owed at any build: M2 (symmetric build path), M3 (a QA seed), M4 (a var roster), M5 (a Worker build stamp), D1 (`instance/dev.json`), D2 (the lab refusal), D3 (the `walked-in-qa` clause), D5 (`cleared_sha` as a deploy precondition), D6 (the post-deploy read). **Nothing here designs a mechanism**
        ux-expert · content-steward · user-researcher · ai-advisor → waived: no surface, no copy, no person and no model sits on any path in this file
- depends-on: .plans/2026-09-07-pipeline-flex-point-AUDIT.md
- depends-on: .plans/2026-09-06-cascade-and-release-state-AUDIT.md
- depends-on: .plans/2026-09-06-conversion-method-DESIGN.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- kind: design

> **Method only.** Nothing here executes, nothing here is applied. Where a call turns on real-world
> context only Paul holds — his household, who may reach an origin, what a defect is worth — it is
> named and declined (§8). Every claim graded `measured` · `inferred` · `proposed`, at HEAD `cfd41fb`.

---

## 0 · FOR PAUL — the answer, in seven lines

1. **The shape is right, and the principle you named is the ordinary one.** *You don't test in
   production; you test in a mirror of it.* Where this repo deviates, **the deviation is the finding.**
   Your loop currently runs the human gate *after* the irreversible act, which is the deviation, and it
   breaks your own ratified rule that gates sit on irreversible acts. §1.
2. ⛔ **QA is not a mirror today, and the largest break is not the one anyone named.** `measured`:
   **QA and production are built by different branches of one script.** `pages-deploy.py:66` —
   `HOUSEHOLD = {"bob","paul","home"}` — and everything at `:151-238` (the allow-list prune, the
   tombstoning, the index rewrite, the neutrality falsifier) runs **only for that set**. QA takes none
   of it. Adding `"qa"` to that set is close to a one-line change and it closes the deepest defect. §3·M2.
3. **Your three caveats, re-read as mirror defects: two are closable, one is irreducible.** Access is
   closable in *either direction* and the direction is yours. The estate difference is closable — the
   reset tool already exists and is misnamed. Generative parity is irreducible and always was. §3.
4. ⭐ **And Access on QA is a HOLD with no release condition.** `measured`: the privacy seat reviewed
   this on 09-03 and **recommended the opposite** — *"accept a public QA origin… it keeps agent testing
   frictionless"* — Access went on the next day for a stated, **time-bounded** reason (keep the parallel
   instance away from Mom). That reason has an expiry and nobody wrote one. §3·M1.
5. **Environment names: four renames, no new environment.** `dev · qa · prod`, plus `legacy` for the
   frozen Fernwood that is currently *named* `prod`. Every one of those renames is already argued in
   this repo's own text and none of them is a new decision. A fourth rung would be a rung nobody walks. §4.
6. ⭐ **The class that survives a perfect mirror: defects created by the DEPLOYMENT, not by the build.**
   A mirror proves the artifact is right; it cannot prove *this deployment of it* landed right, because
   deployment happens once, on one origin, with a cache and a Worker that outlive it. Three named, all
   with measured precedent in this repo. §5.
7. ⛔ **The one change that makes the ruling enforceable at all**: `cleared_sha` sits in
   `cycle/release/cycle-state.json` and **no tool reads it** (`grep cleared_sha tools/release-gate.py
   tools/pages-deploy.py` → zero). Your clear now precedes the deploy, so the deploy must refuse
   without it. Today it checks the seats and never asks about you. §6·D5.

---

## 1 · IS THE SHAPE RIGHT — yes, and the principle is standard

### 1.1 · The deviation is the current arrangement, not the proposed one

`measured` — `cycle/release/CYCLE-MAP.md:43-51`:

| beat | who | today |
|---|---|---|
| 1 | main session | a sha is deployed to **QA** |
| 2 | seats | the synthetic loop, gate ① |
| **3** | **Paul** | **PAUL WALKS IT** |
| 4 | main session → seats | a failure re-enters beat 2 |
| **5** | **Paul** | **PAUL CLEARS IT** — *"this is the release event. Nothing is released before it"* |

and `:182`: *"Synthetics run in QA. **Paul runs production.**"*

⛔ **Beat 3 fires against an origin that is already deployed.** The production deploy is not gated by
beat 3; it precedes it. Beat 5 then declares "released" a build that has been live throughout, so
`:49`'s sentence is **false as written today** and becomes **true** under the change.

Two of your own ratified rules are violated by the current arrangement and repaired by the new one:

- *The gate sits on irreversible acts, never on work.* The release loop is the loop breaking it.
- `CYCLE-MAP.md:51`: *"Beats 2→3→4→2 repeat. **There is no bound on the number of turns.**"* Today
  every turn passes through production. `measured`: `home` serves `1e2748d` (built `2026-09-07T17:39`)
  while QA serves `fbd5072` — production has already been redeployed inside this lap. **A loop that
  iterates through the irreversible surface spends it.**

### 1.2 · It completes a ruling you already made

`measured` — `instance/qa.json:_meta.ruling` `[paul-ruled 2026-09-06, R4]`: *"production ships the full
app, built from its own instance, **as the same artifact QA certified**."* And `instance/qa.json` and
`instance/home.json` are identical apart from `estate`/`estateId`.

⭐ **Your walking QA is that ruling's missing human half.** R4 makes the *machine* certify the shipped
artifact; today you inspect a rebuilt copy of it. Under the change you inspect the certified object.

### 1.3 · Where the corpus itself already agrees with the standard

Putting synthetics in QA and keeping them out of production (`CYCLE-MAP.md:180-189`) is the same
principle applied one rung down, ruled 2026-09-06. **The new ruling is not a new principle; it is the
existing one, finished.** That is the strongest argument for it and it is not mine.

---

## 2 · WHAT BREAKS — file and line

### 2.1 · ⛔ A vocabulary FORK already exists; this ruling would be its third value

`measured` — three live statements of where Paul's gate sits, in one repo:

| file:line | says Paul's gate is |
|---|---|
| `tools/journey-walk.py:336` — *"default qa — gate 1. **lab is gate 2.**"* | **lab** |
| `tools/synthetic-identity.py:61` — *"**Gate 1 is QA and gate 2 is lab**"* | **lab** |
| `.plans/2026-09-05-process-registry-PROPOSAL.md:68` — *"**Paul walks the build in lab**, his own profile"* | **lab** |
| `handoff/handoff-onboarding-journey-testing.md:30` — *"**Paul's gate-2 grant is LIVE**"* (lab row) | **lab** |
| `cycle/release/CYCLE-MAP.md:182` — *"**Paul runs production**"* | **production** |
| this ruling | **QA** |

⭐ **The work is closing a fork, not applying a rename** — and this repo's most-recorded failure is a
claim living in two places with the change reaching one (`CYCLE-MAP.md:216`, *"the same failure the
audit found eight times over"*).

### 2.2 · The map's sentences

| file:line | state under the new shape |
|---|---|
| `CYCLE-MAP.md:45` — beat 1 exit *"deployed to **QA**"* | ⚠️ becomes the **second** rung; beat 1 becomes dev and a new beat carries the promotion |
| `CYCLE-MAP.md:47` — *"PAUL WALKS IT"* | 🟡 same words, **new referent**, and the referent is nowhere in the row |
| `CYCLE-MAP.md:49` — *"Nothing is released before it"* | ⭐ **becomes true for the first time** |
| `CYCLE-MAP.md:182` — *"Paul runs production"* | ⛔ **false on the ruling.** The two reasons below it (`:184-189`) argue only against *synthetics in production* and survive intact |
| `CYCLE-MAP.md:167` — *"**Every walk on record uses `--fresh`**, so the RETURNING journey has never been walked by anyone"* | ⛔ **already false, independent of this change.** `measured`: **8 of 157** transcripts carry `fresh: false` — mom `2026-09-05T190326`, `2026-09-07T094426`; owner `2026-09-05T180909`, `2026-09-06T135556`, `2026-09-07T094657`; strict `2026-09-07T094936`; wide-eyed `2026-09-07T095158`; plus one run predating the field. ⚠️ **Reported, not resolved**: all seven qa ones carry `signedInAs: null` while every fresh walk carries an id — whether a returning walk *establishes* a session is engineering-partner's question, not a sentence for me to rewrite |

### 2.3 · Tools that hardcode the old ladder

| file:line | breaks how |
|---|---|
| ⛔ `tools/journey-logic.py:88` — `if "lab" in QA_ORIGIN: raise SystemExit(…)` | **the harness refuses the dev rung by name.** Its stated reason #2 (`:78-82`, *"lab's stamp is whatever some earlier CI run left behind"*) is `measured` **stale**: lab's live stamp reads `"builtBy": "tools/pages-deploy.py"`, `"builtAt": "2026-09-05T22:39:17"`. `pages-deploy.py:14-20` was written to fix exactly that and the refusal never re-read it |
| `tools/journey-logic.py:45` — `QA_ORIGIN = "https://fernwood-qa.pages.dev"` | a constant, no flag. Dev cannot be targeted at all |
| ⛔ `tools/release-gate.py` `judge()` `:88-190` | **never reads `origin`**, though `journey-walk.py:405` writes it into every transcript. Harmless today (140 of 157 walks are qa); **fatal once dev walks are the norm** — a dev walk and a QA walk become indistinguishable to the gate `pages-deploy.py:280` consults before shipping to production |
| `tools/release-state.py:170` — `served = jw.served_sha("qa")` | ✅ **stays correct and gets more correct**: "what QA serves" becomes precisely what awaits your gate |
| `tools/qa-behind.py:19` + `.git/hooks/post-commit` | ✅ **right as-is; do not touch.** §6·caveat 5 |
| `tools/check-cycle-map.py:35` (`MOM-CYCLE-MAP.md`) · `tools/check-loop-docs.py:56-60` | ⚠️ **the release map has no drift control at all.** Both instruments are mom-cycle-scoped |

---

## 3 · ⭐ THE MIRROR — every way QA is not production, and what closing it costs

Your principle read as a specification: **list the ways the mirror is not a mirror, close what can be
closed, and let the irreducible remainder define the post-deploy check.** Nine defects. Five closable,
four irreducible.

| # | mirror defect | evidence | closable? |
|---|---|---|---|
| **M1** | QA sits behind Cloudflare Access; production does not | `measured`: `GET fernwood-qa.pages.dev/qa-build.json` → **302** → `fernwood-qa-pages.cloudflareaccess.com`; same path at `home` → **200** | ✅ **either direction — Paul's call** |
| **M2** | ⭐ QA and production are **built by different branches of one script** | `pages-deploy.py:66` `HOUSEHOLD={"bob","paul","home"}`; `:151-238` prune + tombstone + index rewrite + neutrality falsifier run for that set only | ✅ **≈ one line** |
| **M3** | QA's estate is an accumulation; production's is a household | `measured`: 140 walk signups into `est-qa0001`; 1 account at `est-e6696a`; 431 vs 10 feedback records | ✅ **the mechanism exists and is misnamed** |
| **M4** | env vars differ where the var **is** the behaviour | `wrangler.toml`: `CHAT_DAILY_BUDGET_USD` 3.00 (qa) / 10.00 (home); `LEGACY_BEFORE` `2026-09-03` / `1970-01-01`; `FAMILY_HOSTS` per origin | ✅ **partly — some must differ** |
| **M5** | the Worker is deployed by a different act and has **no build identity** | `measured`: `/health` at all three envs returns `env`/`estateId`/`legacyBefore` and **no sha, no version, no timestamp**. qa via `deploy-worker-qa.yml` on push to `staging`; home by hand | ✅ **one line + a rule** |
| **M6** | generative output differs by construction | ruled — `[[feedback_ai_output_breaks_environment_parity]]` | ⛔ **irreducible** |
| **M7** | production accumulates real, aged data | Mom and Paul, months of it | ⛔ **irreducible, and must stay so** |
| **M8** | third-party quota is genuinely shared | `measured` precedent, `BACKLOG.md:130`: the account-wide KV write cap — a QA library load (8,114 keys) took prod's `/api/ambient` dark until the daily reset | ⛔ **irreducible** |
| **M9** | edge cache state is per-origin and outlives a deploy | `measured` precedent, `pages-deploy.py:~180`: Pages served removed paths for **7 days** (`s-maxage=604800`) after two correct deploys — the tombstone mechanism exists *because* of this | ⛔ **irreducible** |

### M1 · Access — closable in either direction, and the direction is yours

⭐ **Two things you should know before ruling it, both `measured`.**

**(a) The privacy seat reviewed this and recommended the opposite.**
`.engineering/2026-09-03-c6-privacy-seat-review.md:539-547` offered exactly this fork and marked
option (b) **recommended**: *"accept a public QA origin, and make the fixture non-identifying by
construction… It is less machinery, **it keeps agent testing frictionless**, and 'the QA fixture
contains nothing real' is a rule that can be checked by reading it, whereas an Access policy is a
setting that can be silently changed."* Access went on the following day — option (a).

**(b) The reason it went on is real and TIME-BOUNDED, and nobody wrote the expiry.**
`BACKLOG.md:130` `[paul-stated 2026-09-04]`: QA is *"something that we're not sharing with Mom"* while
the parallel instance is built out. That is a hold on a specific risk. Under the 09-06 rulings Mom goes
to a **new household**, not to QA — so the condition has moved. `[[feedback_a_hold_names_the_work_not_the_mechanism]]`:
*a hold needs a release condition, and "indefinite" is abandonment with manners.*

**The method requirement, which is all I will assert:** whichever way you rule, **the two origins must
match, and something must report it when they stop matching.** Today they differ and nothing says so.
Both directions are live in the record — `.engineering/2026-09-05-account-credential.md:417` names
*"Cloudflare Access in front of the `home` origin"* as an open call.

⚠️ **And the reframe matters here.** I first read Access as an argument against moving your gate. It is
not. It is a defect in the mirror with a documented prior review and a lapsed hold. ⛔ **But it is not
free either:** if you drop Access, the QA origin becomes publicly reachable, and the seat's own
condition rides with it — *the fixture must be non-identifying by construction*, checkable by reading.
That check does not exist today.

### M2 · ⭐ The build path — the largest break, and nobody had named it

`measured` — `pages-deploy.py:66`. Production is pruned to eight allow-listed files and every other
path is re-created as a **tombstone**; QA is not pruned at all. Consequences, live right now:

```
GET https://fernwood-home.pages.dev/questions.json        → 200  {"tombstone":true,…}
GET https://fernwood-home.pages.dev/zones.json            → 200  {"tombstone":true,…}
GET https://fernwood-home.pages.dev/weather-history.json  → 200  {"tombstone":true,…}
GET https://fernwood-home.pages.dev/plants.json           → 200  {"tombstone":true,…}
```

and the production build's own JavaScript fetches four of those at runtime — `measured` in the bytes
`fernwood-home.pages.dev` is serving: `questions.json` **:13302**, `zones.json` **:14063**,
`./weather-history.json` **:20223**, `./weather-bias.json` **:20241**. QA serves the real files at all
four paths.

**Why nothing has broken, and why that is not reassurance.** All four guard on *shape* —
`Array.isArray(data && data.questions)` (:13305), `Array.isArray(cloud.zones)` (:14066),
`Array.isArray(data.days)` (:20226), `data.headline` (:20245). But each also carries
`if (!res.ok) return;` **and that line can never fire in production, because a tombstone is a 200.**
The safety is four guards written by four hands, not an environment invariant. This is
`[[reference_match_payload_not_container]]` at the scale of an origin.

⭐ **Closure — add `"qa"` to that set.** Then QA is built by the branch production is built by, and the
whole class becomes visible one rung earlier. ⚠️ **Verify one behavioural delta before doing it**: the
branch also rewrites `index.html` (`:236`) to redirect to `estate/`, where the tracked `index.html`
redirects to `viewer.html` — so `/` changes meaning at QA. Everything the harness fetches
(`/onboarding/`, `/viewer.html`, `/qa-build.json`) is already on the allow-list, so `inferred`: the
walkers are unaffected. **Engineering owns that verification; I own naming it.**

### M3 · The estate — the mechanism exists and is misnamed

`measured`: `tools/reset-production-estate.py` is **not production-specific**. `:121-125` — it takes
`--estate`, with `choices` derived from `wrangler.toml`, so `--estate qa` is already legal. The
filename says production; the payload takes any declared estate. (Third instance of
`[[reference_match_payload_not_container]]` in this document.)

**So what is missing is not a reset — it is a SEED and a trigger.** Closure spec, `proposed`:
a fixture household that matches production's shape (one owner, one place, no accumulated feedback),
applied at lap open, so QA is a mirror **of a known state** rather than a midden of 140 signups.
⛔ Note the direction of the current error, because it is the opposite of the usual worry: **QA is the
crowded estate and production is the sparse one**, so walking QA today under-exposes you to the
empty-household case — which is the state every future household starts in.

### M4 · The vars — declare which must match

Three kinds are tangled in one file today: vars that **must match** (a behaviour ceiling like
`CHAT_DAILY_BUDGET_USD` — 3 vs 10 makes a cost-refusal untestable in QA), vars that **must differ**
(`ESTATE_ID`, `FAMILY_HOSTS`, the KV binding — differing is the isolation), and vars that are
**historical** (`LEGACY_BEFORE`). **No roster says which is which**, so no check can. Closure is the
roster, then a check over it. `[[reference_lap_clamp_is_time_scoped]]`'s discipline: a rule with no
register is a rule nobody can apply.

### M5 · The Worker — the one with zero instruments today

`measured`, live:

```
fernwood      → {"ok":true,"env":"production","estateId":"est-3c9f1a","legacyBefore":"2026-09-04",…}
fernwood-qa   → {"ok":true,"env":"qa","estateId":"est-qa0001","chat_budget":{"ceiling_usd":3,…}}
fernwood-home → {"ok":true,"env":"home","estateId":"est-e6696a","chat_budget":{"ceiling_usd":10,…}}
```

⛔ **No build identifier of any kind, in any environment.** So no instrument can say whether the
production Worker runs the code QA certified — and gate ① is per-sha for the **page** and blind to the
**Worker** entirely (`release-gate.py`'s five clauses all read a walk transcript). Under the current
shape your production walk exercised it *by use*; that was its only coverage.
`[[reference_anthropic_identity_linked_keys]]` is the precedent: prod Guru died with **no code change**,
and the ruling from it was *verify by USE*. **Stamping the sha into `/health` is one line and it is the
highest value-per-line item in this document.**

### M6–M9 · The irreducible remainder — and this is the specification for §5

**A mirror is never perfectly a mirror, and these four say exactly where the limit is:**

- **M6 generative output** — do not diff it. Gate it on invariants (cost ceiling, refusal behaviour,
  no-leak). M4 is what makes the ceiling comparable at all.
- **M7 real aged data** — ⛔ **this one must NOT be closed.** The AI boundary forbids her words
  reaching a test estate, and copying production data into QA is the standard practice this project
  correctly does not follow. **It is a constraint to honour, not a gap.**
- **M8 shared quota** — a shared external limit is genuinely shared; only production can show you
  production's share of it.
- **M9 edge cache** — cache state cannot be mirrored, and this repo already has the scar.

---

## 4 · ENVIRONMENT NAMES — four renames, no new environment

You authorised a reshuffle. `proposed`: **do not add a rung. Rename four things.** Every rename below
is already argued in this repo's own text, so none of them is a new decision — they are unapplied ones.

| today | proposed | already argued at |
|---|---|---|
| `lab` | **`dev`** | `wrangler.toml:76` — *"The DEPLOYMENT is still named lab… Renaming it to dev is separate churn and is not what makes this Fernwood dev."* The churn is now authorised |
| `qa` | **`qa`** | unchanged — it is the standard name for the rung and it already is one |
| `home` | **`prod`** | `wrangler.toml:112-115` — *"the word is free and this environment is Fernwood production — the rename is bookkeeping, not a decision"* |
| top-level `prod` | **`legacy`** | ⛔ **the worst name in the system.** `wrangler.toml:112` already calls it *"the legacy version"* `[paul-stated 2026-09-05]`, while the flag named `prod` points at **the frozen archive**. `CYCLE-LOG.md` lap 3 records you being misled by exactly this: *"`prod` reads as the live product and points at the archive"* |
| `bob`, `paul` | **household deployments, not environments** | `pages-deploy.py:~140` already says so in prose; `VOCABULARY.md` has **no environment section at all** (the flex-point audit measured `grep -c '\bdev\b' VOCABULARY.md` → **0**) |

**Why no new environment.** Three rungs is the standard shape and you have three. A fourth is a rung
nobody walks, which is the one thing your own doctrine is most consistent about. What is missing is not
an environment — it is **an instance declaration for dev** (§7·D1) and **a symmetric build path for QA**
(§3·M2). Adding a rung would hide both.

⚠️ **A rename is not free and this repo knows why.** `wrangler.toml:76` calls it churn for a reason:
the name appears in origins, worker names, KV bindings, CI workflows, tool constants and prose. **Do it
as one commit, with `VOCABULARY.md` gaining an environment section in the same commit** — that section
is the register the flex-point audit already asked for (R2·c), and without it the fork in §2.1 simply
re-grows under new names.

---

## 5 · ⭐ THE CLASS THAT SURVIVES A PERFECT MIRROR

Your principle does not dissolve the question; it sharpens it. **Assume M1–M5 are closed and QA is as
good a mirror as this project can build.** What is still structurally invisible if you never walk
production?

> ### Defects created by the DEPLOYMENT, not by the build.

A mirror proves the **artifact** is right. It cannot prove **this deployment of that artifact landed
right**, because a deployment is an act performed once, on one origin, whose cache and whose Worker
outlive it. That is not a coverage gap you can look harder at — it is a category the mirror is not in.

Three members, each with measured precedent in this repo:

| | the defect | precedent |
|---|---|---|
| **(a)** | the **shipped sha ≠ the certified sha** | nothing checks it. `pages-deploy.py:280` re-runs gate ① at the sha, and no instrument afterwards asks the production origin what it is actually serving |
| **(b)** | the **production Worker ≠ the certified Worker** | M5 — no build identity exists in any environment, and the two Workers are deployed by two different acts |
| **(c)** | **stale objects at the production edge** | M9 — measured: Pages served removed paths for 7 days after two correct deploys. The tombstone mechanism exists because this happened |

⛔ **None of the three is reachable from QA, however good the mirror is** — they are properties of the
production origin at a moment in time, not of the artifact.

### 5.1 · The cheapest thing that keeps it visible

`proposed`: **`tools/post-deploy.py`, ~30 lines, no browser**, called by `pages-deploy.py` after the
production deploy the way `check-estate-neutral` is called before one (`:240-262` is the model — *a
check wired into the act it guards cannot be forgotten; one listed in a document can*).

1. `prod/qa-build.json.sha == qa/qa-build.json.sha == cleared_sha` → **the artifact you certified is
   the artifact that shipped, and it is the one you cleared.** Covers (a), and it is the whole R4
   ruling made checkable in one line.
2. **Every path the built viewer fetches at runtime** — derived by regex from the built bytes, **never
   a typed list** (`release-gate.py:80` names the four times a typed roster bit this repo) — fetched
   **on the production origin**, refusing on `{"tombstone":true}` or a body that is not the expected
   shape. Covers (c). ⭐ **This stays useful even after M2 closes**, because it is the only check that
   reads the *origin* rather than the *export* — and M9 says the origin can disagree with the export
   for seven days.
3. `GET <prod worker>/health` → assert `env`, `estateId`, and once M5 lands, the sha. Covers (b).
4. A **coverage line, counted and never graded** (`release-gate.py:250-258` is the model), naming what
   it did not reach: everything behind the sign-in door, and M6–M8.

**FALSIFIER, stated because a recommendation without one is an opinion:** *if this fires zero times
across three production deploys **and** M2 has closed, delete it — at that point it is reading the
export twice.* The inverse tell is equally clear: if step 2 ever fires, M2 was live rather than latent.

**Cost, honestly.** One HTTP read of four to eight URLs, added to an act that already polls the origin
until it reports the new sha (`pages-deploy.py` fix #3). **It costs seconds and it is not a walk.**

### 5.2 · Does a human still need to smoke-walk production?

**My read: no, as a gate — and yes, as a cheap habit for the one thing §5.1 cannot see.** §5.1 reads
the origin from outside; it cannot see the app behind sign-in. Two honest options, and only the first
is mine to recommend:

- ✅ **A fresh synthetic walker at production, post-deploy, disposable.** Your own two-classes ruling
  (`CYCLE-MAP.md:154-165`) already defines exactly this object — *"brand-new, spawned to walk signup
  once,"* which *"does not endure, and that is fine,"* whose account may vanish while its evidence is
  retained. The two reasons `CYCLE-MAP.md:184-189` bans synthetics in production are both about a
  **durable** persona joining your household permanently. `measured`: **14 such walks already ran at
  `home`** (owner/mom/wide-eyed/strict, `2026-09-05T214301` → `2026-09-06T181454`, all `fresh: true`),
  none since the 09-06 ruling — so the act is demonstrated and the ban postdates it.
  ⛔ **Whether a disposable walker may touch your mother's future household is a judgment about your
  family and your data. I decline it and it is §8·1.**
- **Your own two-minute look**, unscheduled, no gate, no artifact. Ordinary practice calls this a smoke
  check and it is not "testing in production" — it is confirming a deployment landed. **It is not a
  beat and must never become one**, because a beat that reads red whenever you are busy is the
  permanently-red control you have ruled against.

---

## 6 · WHAT MUST CHANGE BEFORE THIS RUNS — ordered by dependency

⛔ **What the reframe changed:** M1–M5 moved from *reasons not to* into *the work*. D-rows are the
ladder; M-rows are the mirror. **Nothing here is applied.**

| # | change | file | why here in the order |
|---|---|---|---|
| **D0** | ⭐ **rule the fork** — one value for *where Paul's gate sits* | `cycle/release/CYCLE-MAP.md:182` is the register; §2.1 lists the four other sentences | Nothing below can be applied consistently while the variable holds three values. **Yours, and it is one word** |
| **M1** | rule Access — **drop it from QA, or add it to production** | Cloudflare policy; `tools/qa_access.py` becomes a no-op or grows a prod arm | ⭐ **Second because it is the only mirror defect that is yours and not engineering's**, and everything about what you meet at the door depends on it. §3·M1 |
| **M2** | give QA production's build path | `tools/pages-deploy.py:66` (+ verify the `:236` index rewrite) | ≈ one line, closes the deepest break, and makes §5.1 step 2 a *regression* check instead of a *discovery* one |
| **D1** | `instance/dev.json` (today: `instance/lab.json`) | new file; consumed at `pages-deploy.py:223` | Without it dev keeps the **tracked Fernwood** viewer (`:232` refuses only for households). `measured`: lab 2,072,954 B / "Church Mountain" ×11; home 1,181,836 B / ×0. **Dev cannot certify what production ships** |
| **D2** | lift or parameterise the lab refusal | `tools/journey-logic.py:88`, constant `:45` | Reason #2 (`:78-82`) is `measured` stale. ⚠️ Reason #1 (lab is not the gate-1 estate) is **not** stale and is a real question upstream of this |
| **D3** | a `walked-in-qa` clause on gate ① | `tools/release-gate.py judge()` `:88-190`; field already written at `journey-walk.py:405` | Once dev walks are normal the gate cannot tell them apart — and `pages-deploy.py:280` consults it before shipping |
| **D5** | ⛔ **`cleared_sha` gates the production deploy** | `pages-deploy.py:280`, beside the gate ① call; value at `cycle/release/cycle-state.json:last_lap.cleared_sha` | **The change that makes the ruling real.** The human gate now precedes the irreversible act, so the act must refuse without it. `grep` → zero readers |
| **M5** | a build sha in the Worker's `/health` | `worker/worker.js` health handler | One line; converts the only *uninstrumented* mirror defect into a checkable one; a precondition of §5.1 step 3 |
| **D6** | the post-deploy read | new `tools/post-deploy.py`, called from `pages-deploy.py` | §5.1. Depends on D5 (there must be a cleared sha to compare) and is better after M2/M5 |
| **M3** | a QA seed at lap open | `reset-production-estate.py --estate qa` already exists; the **seed** does not | Makes QA a mirror of a known state. Not blocking, but until then your QA walk meets a crowd |
| **M4** | a roster of which vars must match | `worker/wrangler.toml` + a check | Not blocking; without it M6's ceiling stays untestable |
| **D4** | apply the rename to all five surfaces + §4's four env renames | §2.1's five files · `wrangler.toml` · `pages-deploy.py:29-34` · CI workflows · **`VOCABULARY.md` gains an environment section in the same commit** | After D0. One commit, or this repo's eight-times failure happens a ninth |
| **D8** | a map-drift control for the release map | `check-cycle-map.py:35` is hardcoded to `MOM-CYCLE-MAP.md`; `check-loop-docs.py:56-60` covers three mom-cycle surfaces | ⚠️ **The release map has none — and its own conformance table read false for four rows across two laps while a commit edited that very file** (`CYCLE-MAP.md:213-216`). A hand-applied nine-file rename with no control is the same bet, taken again |

### Your six caveats, re-answered under the principle

1. **Access.** ⛔ **Not an argument against the move — mirror defect M1**, closable in either
   direction, with a prior seat recommendation against it and a hold whose release condition was never
   written. **Your ruling.** ⚠️ Note what it is *not*: it is not the reason the synthetics are blind to
   the door — they are blind because `journey-view.py:20-30` mints an Access cookie before every walk,
   so **all 140 QA walks arrived pre-authorised.** Closing M1 fixes both at once.
2. **Different estate, different data.** ⛔ **Mirror defect M3**, closable, mechanism already exists
   and is misnamed. Direction inverted from the usual worry: QA is the crowded one.
3. **Generative parity.** ⛔ **M6 — genuinely irreducible**, and it is not the binding constraint here:
   every divergence I measured is in the deterministic substrate, which is exactly what that ruling
   says to diff.
4. **The cascade and Mom as gate 3.** `inferred`: gate 3's meaning is unchanged, but the cascade now
   **crosses an environment boundary between gate 2 and gate 3** where today both meet the same origin.
   §5.1 is precisely the instrument that spans it. Whether the residual is acceptable is yours.
5. **The `qa-behind` nag.** ✅ **Right under the new shape; do not touch it.** `measured`:
   `qa-behind.py:19` takes an env and defaults to `qa`; the post-commit hook passes `qa` explicitly, so
   **nothing nags `home` today and nothing will.** ⚠️ The new risk is the mirror of the one you asked
   about: nothing says when production is behind a sha you have **cleared** — D5.
6. **Does the clear travel with the sha?** Three parts; only the first is sound.
   - ✅ **The seat evidence travels correctly** — `release-gate.py` is per-sha (`at-sha`, `:107-113`)
     and `pages-deploy.py:280` **re-runs it** at the production deploy rather than trusting a stored
     verdict.
   - ✅ **One thing genuinely is re-verified at production**: `:291` loads the *production-built,
     pruned* export headless and refuses on any page error — so the artifact that differs is the
     artifact that is loaded. Partial cover for M2, thrown-errors-only.
   - ⛔ **Your clear does not travel, because nothing carries it.** D5.

---

## 7 · THE DEV RUNG — `lab` is the right place and is not yet the rung

| | state | evidence |
|---|---|---|
| an isolated estate | ✅ **yes** | `wrangler.toml [env.lab]` → `ESTATE_ID = "est-lab0001"`, own KV namespace `1e0bd883…` (corrected off prod's id 09-05) |
| a build stamp | ✅ **yes — and this repairs the stated reason it was refused** | `GET fernwood-lab.pages.dev/qa-build.json` → 200, `"builtBy": "tools/pages-deploy.py"` |
| ⛔ the same app production ships | **NO** | serves the tracked Fernwood viewer — 2,072,954 B, "Church Mountain" ×11 — because no `instance/lab.json` exists and `pages-deploy.py:223-232` keeps the tracked file for a non-household without one. **D1** |
| ⛔ reachable by the harness | **NO** | `journey-logic.py:88` refuses it by name. **D2** |
| a staleness signal | **NO** | lab's stamp reads `2026-09-05T22:39:17` / `9ef14d1` — **two days old**, and `qa-behind.py` is only ever invoked with `qa`. *"Run in dev until it clears"* would run against a two-day-old build with nothing saying so. **One argument, one hook line** |

⭐ **One asset, and it is now an INTERIM answer rather than a design.** `measured`:
`GET fernwood-lab.pages.dev/qa-build.json` → **200, no redirect** — dev has no Access, corroborated at
`handoff/handoff-onboarding-journey-testing.md:30` (*"onboarding deployed; **no Access**"*). So while
M1 is open, **the unauthenticated door is walkable one rung down.**

⛔ **Labelled interim on purpose, with its own release condition** — *this line retires the moment M1 is
ruled*. Under your principle, "walk the door at dev because QA can't show it" is a workaround for a
mirror defect, not a ladder design. It is worth having while M1 is open and worth deleting the day it
closes.

---

## 8 · WHAT I DECLINED TO DECIDE

1. **Whether a fresh synthetic walker may walk production.** §5.2. A judgment about your household and
   your data. I have stated the four structural facts and stopped.
2. **Which direction M1 closes** — dropping Access from QA or adding it to production is a call about
   who may reach an origin, which is real-world context I do not hold. I assert only that they must
   match and that the mismatch must be reported.
3. **Which estate should certify a release** — `journey-logic.py`'s reason #1 is a real question, not a
   stale one, and it sits upstream of D2.
4. **Whether the returning-walk defect (`signedInAs: null` on all seven) is a harness gap or a product
   defect.** §2.2 → engineering-partner.
5. **Whether the release loop gets its own row on the portfolio board or folds into Fernwood's** —
   already on the record as yours (`CYCLE-LOG.md` lap 3, beat 0 step 4). It is why this loop's gate
   sweep read UNCHECKABLE, and D8 does not fix it.
