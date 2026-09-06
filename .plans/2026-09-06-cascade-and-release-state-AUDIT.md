# CASCADE AND RELEASE STATE — where the four gates actually stand at `b784dc9`, what today's instruments can and cannot reach, and the one thing that must exist before a synthetic household lands in production · AUDIT

- row: process (no BACKLOG row yet — same posture as the 09-04 wiring audit, the 09-05 state-of-the-work proposal and this morning's audit)
- objective: O5
- class: engine · declared (process machinery; nothing here is Fernwood-specific content)
- seats: practice-steward (this file)
        engineering-partner → deferred: §2.3's tenancy options and §7's supersede mechanism have code consequences; nothing is designed here
        ux-expert → cited, not commissioned: `.ux-reviews/2026-09-06-onboarding-handoff-seam.json` is untracked and unread by this pass
        content-steward → deferred: every copy row the seats raised is its call
        ai-advisor · user-researcher → waived: no model is on the onboarding capture path, and no real person is studied here
- depends-on: .plans/2026-09-06-state-and-next-steps-AUDIT.md
- depends-on: .plans/2026-09-05-release-cascade-tracking-PROPOSAL.md
- depends-on: .plans/2026-09-06-user-feedback-cycle-PROPOSAL.md
- ready: agent-proposed 2026-09-06 — **Paul rules**
- stage: audit — ⚠️ **fourth file to need a word that does not exist.** `tools/check-backlog-ready.py:46`
  reads `STAGES = ["ready", "concept", "build", "qa", "shipped", "retro"]`. Two of the files that
  would turn today's work into a process (`2026-09-05-release-cascade-tracking-PROPOSAL.md`,
  `2026-09-05-journey-test-cycle-PROPOSAL.md`) are parked at `stage: draft`, also illegal, unruled
  since 09-05. See §3.4.

> **Method only.** This file ranks no feature and decides no schedule. Where a call turns on
> real-world context only Paul has, it is named and declined — §9.

---

## 0 · THE STAMP — ⚠️ HEAD MOVED UNDER THIS PASS

**Opened at `b784dc9` 12:30 EDT. Closed at `fae767e` 12:41 EDT. Three commits landed while this file
was being written.**

```
fae767e  back-merge the legacy weather line (second time today)
bb21863  run identity: the thing superseding had nothing to group by
afee65c  weather-history: rollup update 2026-09-06T15:00Z   (weather-recorder[bot])
```

⭐ **`bb21863` is a build of §7 of this file, from the same findings, while the file was open.** That
is not a problem to route around — it is §5.2's rule landing on its own author. **Every measurement
in §7.1 was taken at `b784dc9` and is now historical; §7.4 records what superseded it and what did
not.** Sections 1–6 and 8–11 were re-checked against `fae767e` and stand, with one amendment at §3.2.

Working tree at close: **one modified tracked file** (`tools/synthetic-identity.py` — adds the
`handover` role, still uncommitted) and **two untracked files**
(`.ux-reviews/2026-09-06-onboarding-handoff-seam.json`, and this file).

⚠️ **One probe in this pass was blocked and is reported as unrun, not as clean.**
`python3 tools/reset-production-estate.py` with no flag — the read-only dry run that answers *what
does production actually hold* — was refused by the sandbox classifier. **It was row 1 of this
morning's punch list and it is still row 1.** Everything this file says about production's contents
is therefore `unverified`, and §2 flags where that matters.

---

## 1 · WHAT MOVED SINCE 09:19 THIS MORNING, AND WHAT DID NOT

Measured against `.plans/2026-09-06-state-and-next-steps-AUDIT.md` (written at `de56e76`).

### Closed since this morning

| this morning | now | evidence |
|---|---|---|
| **I3** — *"no walker wrote a report. Not one."* `WALK-REPORT-UNWRITTEN` had never once been cleared | ✅ **four seats wrote one**, and the marker is honoured rather than read around | `walk-integrity.py` → `runs: 26 · countable: 4 · refused: 22` |
| **I4** — *"two seats on one instrument count as one"*; effective interpretive n = 0, behavioural n = 1 | ✅ **4 distinct inputs across 4 seats** | same run; `.private/walk-answers/{mom,owner,strict,wide-eyed}.json` |
| **I1** — structured `status:"walked"` disagreeing with the prose `could not do` | ✅ **detected and refused**, 6 runs caught on that predicate alone | `walk-integrity.py` refusal class `prose-contradicts-status` |
| **step 1** — back-merge `origin/main` → staging | ✅ done at 09:45 — `d0fd828` | and **already undone**, §3.1 |
| **§4 step 3(b)** — no reader existed for the new estate | ✅ **partially** — `tools/read-onboarding.py` is the first reader the setup answers ever had. ⛔ It reaches **qa only** in practice; §4.3 |

**That is a real day's closure and it should be said plainly: `WALK-REPORT-UNWRITTEN` had never been
cleared in this corpus's history and it was cleared four times in ninety minutes.** The instrument
that refuses uncountable runs was built *and immediately refused 20 of the 20 runs that predated it*
— a negative control that fired on the first pull.

### Still open, unchanged

- **A2** — intermittent *"That didn't go through"*, cause undiagnosed. Still the top open
  engineering row, now 36h.
- **§3.D — Paul's 23 rows from GATE2 lap 2.** Still unactioned by his own instruction, and now
  correctly so under his refinement: they are step ④ material.
- **§5.1 — no instrument reports which Worker code is live in any environment.** Unchanged.
  `/health` on all four deployments reports `env · kv_canary · estateId · legacyBefore · budget` and
  **no version**. Verified live on `home`, `bob`, `qa`, `lab` at 16:31Z.
- **§5.2 — the `legacy` / `production` rename bookkeeping.** Unpaid. `wrangler.toml:25` still reads
  `ENV_NAME = "production"` for the legacy estate.
- **§5.4 — `check-backlog-ready.py` flags and exits 0.** Still exits 0; now also reports
  `WIP: 9 items between concept and qa`.
- **`.private/synthetic-production-manifest.json`** — self-declared cleanup obligation, trigger
  *"before Mom's invite"*, still no watcher. §2.4 makes it materially more important than it was.

### New since this morning, and it changes the shape of the question

Four instruments, one surface, one live household, one provenance marker — and **every one of them
is unreachable by any procedure this repo writes down.** That is §3.

---

## 2 · A · WHERE WE ARE IN THE CASCADE, HONESTLY

### 2.1 · The cascade as Paul restated it today

> ① synthetics walk the latest build → ② synthetics stand up **durable households in production** →
> ③ Paul stands up **his own property in production** → ④ **action all feedback** → ⑤ send to Mom.
> *(Bob was added as a fourth gate earlier in the day: "all the synthetics run profile creation in
> chrome that we can watch, then I will do it, then Mom will do it, then Bob will do it.")*

**Measured position: ① is DONE and it is the only gate with evidence behind it.**

| gate | state | evidence |
|---|---|---|
| **① synthetics walk the build** | ✅ **ran, reported, countable** — for the first time | 4 countable runs, 4 distinct inputs, 4 written REPORTs |
| **② durable synthetic households in production** | ⛔ **structurally blocked** — §2.3 | `scopeOf(env)` at **51 call sites**; `scopeFor()` has **zero callers** |
| **③ Paul's own property in production** | ⛔ blocked by the same constraint, and by ② preceding it | same |
| **④ action all feedback** | ⚠️ **cannot be run to completion today** — production and bob are unreadable by construction | §4.3 |
| **⑤ Mom** | not started | — |
| **⑥ Bob** (added today) | instance **live and neutral**, nothing sent | `myhome-bob.pages.dev` @ `b784dc9`, `est-9a74df`, own KV; `check-estate-neutral` ✅ 311 needles, zero hits |

⭐ **The single most important correction to make out loud: gate ① walked a build that no longer
exists.** See §5. It does not invalidate the day; it changes what step ② would be walking.

### 2.2 · THE COMMITMENT TENSION — stated precisely, not adjudicated

Paul ruled Bob gets the link **2026-09-07 .. 09-10**. That window opens tomorrow. Bob is gate ⑥ in a
cascade whose ② and ③ are blocked and whose ⑤ has not begun.

**What each option costs, structurally. Which to take is his.**

| option | what it costs, structurally |
|---|---|
| **Compress the cascade into this week** | The gates stop being sequential and become concurrent. A concurrent cascade is not a cascade — its whole information value is that gate *n*'s findings are actioned before gate *n+1* meets the product, and Paul stated that ordering himself (*"then we would actually look at ALL feedback, action it, then send to Mom"*). Compressing does not make the gates faster; it makes them **unattributable**: when Bob and Mom hit the same defect you cannot tell whether gate ③ missed it or never had the chance to see it. |
| **Move the commitment** | Costs a date Paul gave a person. That is real-world cost this seat cannot weigh. |
| **Re-order Bob ahead of Mom** | ⛔ **Not neutral, and it is worth naming: Bob's instance is already the most current deployment in the estate** — `myhome-bob` serves `b784dc9`, the same sha as qa, while Mom's `home` serves `c111417`. On the pure evidence, Bob's household is running *newer, less-walked* code than Mom's. Sending it first is not "the safe end of the cascade"; it is the **least-walked** end. |

⭐ **The method claim, and it is the only one I will make here: a gate is PASSED when its walker met
the build that the next gate will meet and their findings were dispositioned. A gate is SKIPPED when
either half is missing.** By that definition, at `b784dc9`:

- gate ① is **passed for `3b7d7be`/`4ea8e23`** and **not passed for `b784dc9`**;
- gate ② and ③ have not started;
- gate ⑥ (Bob) would be **skipped**, not passed, if the link goes tomorrow — because nothing has
  walked `myhome-bob` at all (§4.2), and because gate ④ has not run.

**Falsifier:** if Paul rules that "passed" means *the walker met a build that shares the same journey
semantics*, then a diff-scoped rule replaces the sha rule and my §5 re-walk claim weakens
substantially. That is a legitimate ruling and I would take it.

### 2.3 · ⛔ THE CRUX — step ② as stated cannot be built on today's isolation model

**Verified, three ways:**

1. `worker/wrangler.toml` — `ESTATE_ID` is a **per-environment `[vars]` binding**. `home` →
   `est-e6696a`, `qa` → `est-qa0001`, `lab` → `est-lab0001`, `bob` → `est-9a74df`, top-level →
   `est-3c9f1a`. **One deployment, one estate, by construction.**
2. `worker/worker.js:651` — `scopeOf(env)` is *"the only function in this file that reads
   ESTATE_ID"*, and it is called at **51 sites** (`grep -c "scopeOf(env)"` → 51). The file's own
   comment says these are *"an exact, greppable inventory of the sites that still take the household
   from config — which is what the multi-household flip has to work through."*
3. `worker/worker.js:657` — `scopeFor(request, env, grant)` **exists**, resolves a grant's
   `estateId` ahead of the deployment, and has **zero call sites** (`grep -n "scopeFor("` returns
   the definition only). Including `handleAccountCreate`, which is invoked at `:3174` as
   `handleAccountCreate(request, env, scopeOf(env))` — **an account is always created under the
   deployment's estate, never under the inviter's.**

> **So four synthetic households plus Paul's own property in `home` would all be ONE estate,
> `est-e6696a`, reading and writing each other's rows.** That is exactly the leak `estate/index.html`
> and `check-estate-neutral.py` were built today to stop — arriving from the other side. Not through
> a shared *viewer*, through a shared *store*.

⭐ **This is not a discovery, and that is the finding worth having.** The seam is already built,
already named, already self-documenting, and **has no caller**. This repo's own recorded pattern:
*the check usually already EXISTS and has no CALLER.* The multi-household flip is 51 greppable sites
against a function that already does the right thing.

**The three shapes step ② can take. I state what each costs; I do not choose.**

| | what it is | what it costs |
|---|---|---|
| **(a) a deployment per synthetic household** | The `bob` path, repeated. Proven end-to-end today: own Pages project, own KV namespace, own Worker, `check-estate-neutral` green. | **N permanent Cloudflare objects for N synthetic seats**, each with its own KV namespace id in `wrangler.toml`, each needing a read token that does not exist (§4.3), each needing a deploy on every release or it silently rots to an old sha — **which is exactly how `home` got 26 commits behind.** The instrument that would catch that rot (a version stamp on the Worker) does not exist. |
| **(b) the tenancy conversion** | Wire `scopeFor()` through the 51 sites. | The real fix. It is a Worker-wide refactor of every read and write path, beside a live onboarding and a dated commitment. `assertScope` means a **forgotten site throws at the call**, not silently — which is the good news and also means partial conversion is not a stable resting state. |
| **(c) synthetic households somewhere that is not production** | qa or lab or a fifth environment. | Contradicts what Paul asked for and loses the thing he wants — durability **in the environment that matters**. It also loses the thing step ② is actually for, which is proving that a household stands up *in the place Mom's will stand up*. |

⛔ **I decline the choice.** It trades a schedule Paul owns against a refactor risk beside a live
onboarding, and both sides of that trade are real-world context only he has.

⚠️ **One thing that is method, not preference, and it applies to (a) and (b) alike:**
`tools/synthetic-identity.py`'s docstring says **"⛔ REFUSES TO TOUCH PRODUCTION"** while its
`WORKERS` map contains `home` and `.private/synthetic-identities.json` already holds **four
identities on `home`** (`syn-owner-0151`, `syn-mom-d940`, `syn-wide-eyed-ddcd`, `syn-strict-b1c8`).
**The file contradicts itself in its own text.** It also has no entry for `bob`, so the tool cannot
reach the one household that is live. Report, do not resolve — the docstring may be the ruling and
the map may be the exception, and only Paul knows which.

### 2.4 · WHAT "PRODUCTION IS EMPTY" MEANS AFTER STEP ②

`.plans/2026-09-05-production-promotion-PLAN.md` §S6: the reset tool *"After Mom onboards it must
never be run again."* And `tools/reset-production-estate.py`'s own docstring: *"THE ONE THING IT
CANNOT DO IS TELL SYNTHETIC FROM REAL."*

**Populating production with durable synthetic households changes what the emptiness is for.** Under
today's model those households ARE Mom's estate. So the promise *"start from nothing other than a
text to Mom"* and the plan *"durable synthetic households in production"* cannot both hold in
`est-e6696a`. **One of them has to be restated or retired, and that is Paul's sentence to write, not
mine.** What is method: the two statements currently sit in two files that do not cite each other,
and a reader of either one would not know the other exists.

⭐ **And the marker he asked for does not yet cover the case he asked it to cover.** Paul: *"we can
even get rid of them once Mom populates an estate with that address."* Verified:

- `onboarding/index.html:1512` — `var SYNTHETIC = /[?&]syn=1(&|$)/` and `:1514` stamps
  `ctx.synthetic = true` **on answers only**, inside `postAnswer`.
- `worker.js` `handleAccountCreate` writes the account row (`personId, salt, hash, tokenHash, email,
  phone, contactPref, relationship, capability, accent, placeName`) and the grant row — **neither
  carries any provenance field.** `grep -n "synthetic" worker/worker.js` returns two hits, both about
  an unrelated Anthropic text block.
- There is no estate record at all to mark; the estate is a config binding.

> **So today: a synthetic ANSWER is findable. A synthetic ACCOUNT and its GRANT are not, and they are
> what a durable household actually is.** "Get rid of them" would remove the words and leave the
> credentials — and a leftover grant row is a live credential, which `c111417`'s own commit message
> is about. **The gap matters, and it matters more under step ② than it did this morning.**

---

## 3 · B · IS THE RELEASE PROCESS A PROCESS, OR A SEQUENCE OF GOOD SESSIONS?

**Measured answer: a sequence of good sessions. Four new instruments, zero of them reachable by
running the loop's own procedure.**

### 3.1 · The reachability census — verified two ways

`git grep -ln <tool> -- .` across **every tracked file**, then a second pass over `~/.claude/skills`,
`~/.claude/commands`, `~/.claude/rituals`:

| instrument | named in `CLAUDE.md` session-start block | named in `MOM-CYCLE-MAP.md` | named in any `.md` at all | named in any skill / command |
|---|---|---|---|---|
| `walk-integrity.py` | ❌ | ❌ | ❌ | ❌ |
| `walk-brief.py` | ❌ | ❌ | ❌ | ❌ |
| `check-estate-neutral.py` | ❌ | ❌ | ❌ | ❌ |
| `read-onboarding.py` | ❌ | ❌ | ❌ | ❌ |
| `journey-walk.py` | ❌ | ❌ | ✅ 4 plans + 1 handoff | ❌ |
| `synthetic-identity.py` | ❌ | ❌ | ✅ 1 (my own audit) | ❌ |
| `pages-deploy.py` household mode | ❌ | ❌ | ✅ 3 plans | ❌ |

`walk-integrity` is referenced by `journey-walk.py` and `journey-view.py` — **tool-to-tool, not
procedure-to-tool.** `check-estate-neutral` is referenced by `pages-deploy.py` (which *calls* it —
that one is genuinely wired) and by the two HTML surfaces in comments. **`walk-brief.py` and
`read-onboarding.py` are referenced by nothing but themselves.**

> ⛔ **This is the fourth instance of the shape `CLAUDE.md` already records three times** — `/ux-sweep`
> unnamed for 21 days, `telemetry-walk.js` unnamed for 16, weather-history completeness living
> outside the loop. Its own words: *"A capability the loop cannot reach by running its own procedure
> is not a capability the loop has."*
>
> **The difference this time is scale.** Those three were one capability each. This is an entire
> release gate — the instrument that decides whether a walk may be counted, the instrument that
> refuses a household leak, and the only reader the setup answers have ever had — landing on the same
> day with no procedure naming any of it.

**And the loop it would belong to does not exist yet.** `MOM-CYCLE-MAP.md` governs Fernwood's
feedback loop and correctly does not cover onboarding. The two documents that would make this a
process are `.plans/2026-09-05-release-cascade-tracking-PROPOSAL.md` and
`.plans/2026-09-05-journey-test-cycle-PROPOSAL.md` — **both `stage: draft`, both unruled since
09-05, and `draft` is not a legal stage word so no instrument reads either of them.**

**Falsifier:** if a fresh session, given only `CLAUDE.md`, can reach `walk-integrity.py` before
counting a walk, this finding is wrong. I tested it by grep and by a second sweep of the skill
surface; I did not test it by spawning a session.

### 3.2 · ⚠️ A CONTROL THAT IS NOW RED ON A TIMER

`qa-divergence.py --check` was cleared this morning by the back-merge `d0fd828` at **09:45**. It went
🔴 again at **15:00Z** on **one** commit: `afee65c weather-history: rollup update`. It was cleared a
**second time** at 12:41 EDT by `fae767e`, whose own subject says *"back-merge the legacy weather line
(second time today)"*.

> ⭐ **Two back-merges in one working day, both to clear one bot's data commits, is the measurement.**
> The remedy has become a chore on the bot's schedule.

⚠️ **Amended at `fae767e`: the check is STILL 🔴 (`exit 1`), on a different predicate** — *"11 SURFACE
commit(s) on QA are not named in any plan stage-note."* The fast-forward half now reads ✅. **So the
control has been red continuously through this audit for two independent reasons, and clearing one
reveals the other.** The 11 unrecorded SURFACE commits are today's onboarding work, and the plan that
would name them (`2026-09-05-onboarding-PLAN.md`) has a `stage-note` pinned at `408ff94`.

**Time to red: 5h15m.** Measured cadence on `origin/main`: 4 bot commits/day (09-04, 09-05, 09-06),
and **the last human commit on that branch was `315419c` on 09-04**. The legacy Pages branch now
receives nothing but `weather-recorder[bot]`.

`qa-divergence.py:74` gates on `behind != "0"` with **no author or class distinction** — a bot data
rollup on the retired line is a hard 🔴 and `exit 1`, identical to a real surface divergence.

> **This is a control whose alarm will now be on more often than off, for reasons no human act can
> clear for longer than a few hours.** That is the one thing Paul's own practice forbids installing
> — and it is worse than a permanently-red control, because it goes green just often enough to look
> like it is working.

⛔ **The remedy is a content call and I decline it** — it turns on whether the legacy weather line is
still wanted, which is a real-world question about Mom's live app. What is method: **the check's
predicate and the branch's actual traffic have diverged, and the check does not know it.** The
options are structurally distinct (class bot-authored data commits the way `NOT_SURFACE` already
classes `engine/place-claims.json`; retire the legacy branch's bot; or accept a scheduled red and say
so in the file), and this repo already owns the first pattern one function above.

### 3.3 · What IS wired, and it deserves saying

`tools/pages-deploy.py` is the one place today's work became procedure rather than capability:
`HOUSEHOLD_ALLOW` (`:49`) prunes the export to four paths, then **the deploy calls
`check-estate-neutral` and refuses on any hit** (`:127`–`:152`) — *"THE ALLOW-LIST IS CHECKED, NOT
TRUSTED. A list of paths is a claim about what we thought of."* **A gate that runs as part of the act
it gates cannot be forgotten.** That is the shape the other four want.

### 3.4 · The stage enum, fourth instance

Four files have now needed a stage word for *a finished analysis awaiting a ruling*: two chose
`audit`, two chose `draft`, all four flagged themselves, `STAGES` has not moved.
`check-backlog-ready.py` prints the violation and **exits 0**. ⛔ Stated once, not re-raised.

---

## 4 · C · WHAT "TESTED" MEANS NOW, AND WHAT IS NOT TESTED

### 4.1 · Every environment, with its evidence — read live at 16:31Z

| env | page sha | Worker | walked by | evidence class |
|---|---|---|---|---|
| **qa** | `b784dc9` (via Access service token) | `env:qa · est-qa0001 · legacyBefore 2026-09-03` | **4 countable walks — but at `3b7d7be`/`4ea8e23`, not at `b784dc9`** | ⚠️ **evidence, one build stale** |
| **bob** | `b784dc9` | `env:bob · est-9a74df` | **nobody, ever** | 🔴 **deploy line only** |
| **home** (production, Mom's) | `c111417` | `env:home · est-e6696a` | Paul, 2026-09-05 23:35 (GATE2 lap 2, 23 findings) — **at `c111417`, which is what it still serves** | ⚠️ **evidence, 26 commits stale** |
| **lab** | `9ef14d1` | `env:lab · est-lab0001` | 2 walks 09-05, **both refused** by walk-integrity | 🔴 **deploy line only** |
| **legacy Fernwood** | GitHub Pages `origin/main` | `env:production · est-3c9f1a` | Mom, daily, for months | ✅ the only environment with a real human's continuous use |

⭐ **`home` is the one environment where the walk and the build agree**, because it has not moved
since Paul walked it. That is an accident of neglect, not a process.

### 4.2 · Bob has a deploy line and nothing else

`myhome-bob.pages.dev/qa-build.json` → `b784dc9`, built 12:12:55 EDT by `pages-deploy.py`.
`/health` → `env:bob`, `kv_canary:bob`, `est-9a74df`, budget $5. `check-estate-neutral` ✅.
`https://myhome-bob.pages.dev/estate/` → **200**.

**What that proves: it is deployed, it is isolated, and it serves no other household's name.**
**What it does not prove: that anybody can complete a journey on it.** No walk has run against `bob`.
`synthetic-identity.py`'s `WORKERS`/`PAGES` maps do not contain `bob`, so the standing walkers cannot
reach it. `read-onboarding.py`'s `WORKERS` map does not contain `bob`, so nothing can read what a
walker would write there.

### 4.3 · ⛔ THE READ DOOR EXISTS FOR EXACTLY ONE ENVIRONMENT

`tools/read-onboarding.py:40` — `TOKENS = {"qa": "fernwood-token-qa", "legacy": "fernwood-token",
"lab": "fernwood-token-lab", "home": "fernwood-token-home"}`. On disk in `.private/`: **two token
files, `fernwood-token` and `fernwood-token-qa`.** No `-home`, no `-lab`, no `-bob`, and `bob` is not
in the map at all.

The tool is honest about it — its own docstring: *"production is currently unreadable BY
CONSTRUCTION"*, exit 3 = UNREADABLE, never *"nothing came in"*. **That is correct instrument
behaviour and it is the finding, not a defect in the tool.**

> **Step ④ — "action ALL feedback" — cannot be run to completion today, because the feedback written
> in steps ② and ③ would land in a store no reader can open.** Steps ② and ③ are the steps that put
> feedback in production. This is the *channel nobody sweeps* shape, pre-registered rather than
> discovered.

### 4.4 · What the four countable walks actually establish

Read the four REPORTs. **The gate produced exactly what a gate is for and it produced it four
different ways**, which is the thing that has never happened before:

- `strict` gave a **PO box** and watched it pass unchallenged into a promise to build weather from it
  — *"recognized as a string but not evaluated as content."*
- `mom` ranked **household systems first** and found no trace of the ranking on the landing screen —
  and then said she would **not** file that in the feedback box, because *"using that box means
  deciding, on my own, that the app is at fault rather than me."* **That last sentence is the single
  most valuable line the battery has ever produced and no deterministic check could have produced
  it.**
- `wide-eyed` was asked *"Does the map find you?"* with **no map on screen** and tapped yes anyway.
- `owner` found the place was **already named** before she was asked to name it.

⚠️ **And the seats' own "what I cannot tell you" sections are load-bearing.** Every one of them says
some version of *I could not decline, and I could not stop.* `mom`: *"the walk never had the option
of stopping."* `strict`: *"I always had to keep going."* **The instrument cannot produce abandonment
evidence, and abandonment was the original defect this whole flow was built to fix.** That is a
structural limit of the harness, not a gap in the seats — and it means gate ① can never be the gate
that clears the abandonment question. Only gates ③/⑤/⑥ can.

---

## 5 · D · THE SEATS REPORTED ON A BUILD THAT NO LONGER EXISTS

### 5.1 · Measured

| seat | build walked | delta to `b784dc9` on the two onboarding surfaces |
|---|---|---|
| `mom` 10:59:30 | `4ea8e23` | **+185 / −29 lines** |
| `owner` 11:03:01 | `3b7d7be` | **+161 / −28 lines** |
| `strict` 11:12:07 | `3b7d7be` | same |
| `wide-eyed` 11:12:47 | `3b7d7be` | same |

Commits landing after `3b7d7be` that touched `onboarding/` or `estate/`: `d4f0fc1`, `c4d3c66`,
`209cd12`, `70c6d4b` — the land-default fix, the ranker fix, the allow-list, the Fern rename. **Every
fix the seats motivated landed after the last seat finished.** Zero of four walked the current build.

**And production is further out than that:** `c111417 .. b784dc9` on those two files is **+542 / −29
lines**, and `estate/index.html` — 386 lines, the entire arrival surface — **did not exist at
`c111417` and is not on production.** (`git cat-file -e c111417:estate/index.html` → *exists on disk,
but not in `c111417`*; added by `4ea8e23`.)

### 5.2 · Is a re-walk owed, and what is the rule?

**Under Paul's refinement the question moves but does not go away.** He wants ④ *after* ③. So the
question is no longer "re-walk before gate 2" — it is:

> **What is step ② walking, and does the gate-① evidence still describe it?**

**It does not.** The seats' four headline findings — PO box unscrutinised, land-default in the
ranking, name/address ambiguity, two presses for one decision — are all *fixed*. A reader of the
walk corpus tomorrow, with no conversation history, would find four REPORTs describing defects that
no longer exist, with **nothing in the corpus saying so**: `REPORT.md` carries the seat's prose;
`walk-integrity` records the build sha; **nothing records that a later commit answered a finding.**

⭐ **The rule I propose, grounded in a mechanism this repo already runs rather than imported:**

> **A walk's findings stay live until a commit names them; a walk's EVIDENCE expires when the build
> it walked stops being the build the next gate meets.** Those are two different clocks and today
> only the first is even informally tracked.

The repo already owns the machinery for the second clock. `qa-divergence.py --check` asks that every
SURFACE commit's sha **or the first 40 chars of its subject** appear in some plan's `stage-note` —
*"subjects survive rebase; shas do not."* **The same predicate, pointed at a walk instead of a plan,
answers "has the build moved under this evidence" deterministically.** `walk-integrity.py` already
parses and stores the build sha per run; it is one comparison away from also reporting *stale-vs-HEAD*.

**Cost of not having it, stated as a mechanism rather than a risk:** a re-walk that finds a defect
gone cannot be distinguished from a re-walk that never met it, and a finding fixed cannot be
distinguished from a finding forgotten. That is the corpus's own dominant failure shape — *X and
not-X produce the same observation*.

⛔ **What I decline: whether a re-walk should run before step ② or whether the fixes are small enough
to carry forward.** That is a judgement about the size and risk of four diffs against a schedule, and
Paul holds both halves. What is method: **whichever he rules, the walk corpus must record the ruling,
because right now the corpus records a build sha and no verdict on it.**

**Falsifier:** if a `walk-integrity` run flags a walk as stale against HEAD and Paul overrides it as
noise twice, the rule is wrong and I should stop proposing it.

---

## 6 · E · WHERE TODAY'S RULINGS SHOULD BE RECORDED

### 6.1 · Measured: today's rulings live where a reader will not find them

`git grep -n "paul-\(ruled\|stated\|approved\|ratified\|decided\|confirmed\) 2026-09-06"` across
every tracked file → **20 stamps in 9 files.**

| where | count |
|---|---|
| `.py` / `.html` / `.toml` / `.json` (code and config) | **19** |
| `.md` (a document someone opens) | **1** — my own morning audit, citing the bubble ruling |

**Against the corpus norm, which is the opposite.** All-time stamp distribution: **457 in `.md`**,
124 html, 92 json, 66 py, 13 js, 7 toml, 5 jsonl. Top files: `BACKLOG.md` (69), `viewer.html` (55),
`MOM-CYCLE-LOG.md` (38), `MOM-CYCLE-MAP.md` (25), `VOCABULARY.md` (23), `CLAUDE.md` (19).

> **Today inverted the ratio.** Nineteen rulings are recorded exactly where the code that enacts them
> lives — which is genuinely good practice and is why they are self-documenting — and **none of them
> reaches a surface a fresh session reads before touching the work.** A ruling in a `.html` comment
> is discoverable by whoever edits that file and by nobody else.

Second-method check, because a clean absence from one grep is not a finding: I searched for the
ruling *phrases* independently — `"Early days"`, `"derive-from-ranking"`, `"mechanism banner"`,
`"cold start"`, `"PO box"`, `"myhome-"` — across tracked `.md`. **`Early days`, `derive-from-ranking`
and `mechanism banner` return zero.** `cold start` and `PO box` return only unrelated historical
hits. `myhome-` returns only the product-name plan, which is about naming and not about hostnames.

### 6.2 · Where each belongs, by the repo's own existing convention

I am proposing **destinations, not wordings**, and every destination is a file that already holds
rulings of that kind.

| ruling | destination, by existing convention | why that file |
|---|---|---|
| **Mom is a COLD START, not a migration** | ⭐ `CLAUDE.md` — it changes what a Fernwood pickup is *for*, and it contradicts the migration framing already in `handoff/handoff-fernwood-migration-era.md` | this is the one that will be re-litigated first, because the migration story is written down and the cold-start story is not |
| **`[env.bob]` now · `myhome-` hostnames · household allow-list** | `PRODUCT-ENGINE.md` (already holds `allow-list`, and it is the engine's file, not Fernwood's) | Bob is the engine's second instance; `BACKLOG.md` is Fernwood's |
| **Fern rename (swatch)** | ✅ **already correctly recorded** in `engine/palette.json`, with the superseded ruling kept above it | this is the model the others should follow |
| **PO box honesty · derive-from-ranking · "Early days" · mechanism banner** | `VOCABULARY.md` §4 for the words; the surface comment stays where it is | §4 exists *because* "an alternative considered and rejected never gets written down, so the next reader re-proposes it" — and "validate the address" is exactly the alternative that was considered and rejected today |
| **the whole cascade as restated (① … ⑤ plus Bob)** | ⛔ **has no home at all** — `feedback_release_cascade_persona_paul_mom` in auto-memory says *persona → Paul → Mom*, three gates, and is now wrong | this is the highest re-litigation risk on the list: an agent reading memory tomorrow gets a three-gate cascade |

⚠️ **`.plans/2026-09-05-release-cascade-tracking-PROPOSAL.md` is the file that was commissioned to
hold exactly this and it is `stage: draft`, unruled.** The rulings have a home; the home has no
ruling authorising it.

---

## 7 · ⭐ TEST-DATA VERSION CONTROL — the risk Paul named, measured as already present

### 7.1 · Independently verified, `est-qa0001`, last 7 days

Re-derived from `tools/read-onboarding.py --env qa`, not taken on report:

```
onboard-name        18 rows ·  7 distinct
onboard-address     18 rows ·  8 distinct
onboard-interests    5 rows ·  4 distinct   (one of which is "(none chosen)", ×2)
```

That one estate simultaneously claims to be called `QA` (×9), `Fernwood QA` (×2), `The Old Miller's
Place on the Bend` (×2), `A place` (×2), `the condo`, `Hollow Creek Road`, and `Home`; and to be at
eight different addresses in three states. **Nothing in the store says which is current.**

`read-onboarding` reports `0 real · 0 synthetic · 44 unknown` — because the marker landed in
`c4d3c66`, **after** every countable walk ran. `journey-walk.py:286` does append `&syn=1`, so the
mechanism is correct and simply post-dates its own evidence. **Every row in the store today is
`unknown`, and `unknown` is correctly never promoted to `real`** (`read-onboarding.py:108`).

### 7.2 · Accept the distinction, and sharpen it

**I accept the coordinator's RECORD/STATE split. It is right, and it is under-stated.**

Verified at `worker.js:3059–3074`: `/api/feedback` reads the day's array, **appends**, and writes it
back. It is **idempotent on a client-supplied `id` only** — a genuine re-send is deduped; a *new
answer to the same question* is a new row by construction, because `postAnswer` fingerprints on
credential **and** answer text. **There is no upsert, no supersede, and no current pointer anywhere in
the feedback path.**

⭐ **But the sharper finding is that "state" already exists for two fields and not the others, and
nobody has said so:**

| what a household is made of | where it lives | semantics |
|---|---|---|
| **place name** | account row + grant row `placeName`, written by `/api/profile` (`worker.js:3199`, `:3212`) | ✅ **single-valued, upsert, last-write-wins — this IS state** |
| **accent colour** | same | ✅ state |
| **address** | ⛔ **the append-only feedback log only** | no current, ever |
| **ranking** | ⛔ **the append-only feedback log only** | no current, ever |
| **what the estate screen SHOWS** | ⛔ **`localStorage` on the walker's own browser** — `estate/index.html:180–212`: `K_ADDR`, `K_NAME`, `K_PARTS`, `fw-onboard-interests` | 🔴 **device state, not household state** |

> **So the receipt screen looks personalised because the browser remembers, not because the household
> does.** `estate/index.html` makes **no GET to any endpoint** — its only network calls are a POST to
> `/api/feedback` and a beacon to `/api/onboarding-metrics` (`:324`, `:328`, `:368`).
>
> ⛔ **This is a second, independent problem with "durable households" and it is upstream of the
> version-control question:** a durable identity returning in a fresh browser has a name and a colour
> and **no address and no ranking**, because those were never state anywhere. The version-control
> problem is about picking between competing values; this is about there being no place to put the
> winner. **Fixing supersede without fixing this gives you an authoritative answer nothing renders.**

**And Paul's generative-AI point does defeat the obvious fix, exactly as stated.** This repo already
ruled it: `feedback_ai_output_breaks_environment_parity` — dev ≠ qa **by construction**; diff the
deterministic substrate, never the generative output. So *"run it twice and take the values that
agree"* is unavailable, and would be unavailable even if the storage were fixed.

### 7.3 · Answers to the four questions

**1 · Where does the declaration live, and who may write it?**

⭐ **Not on the rows.** A per-row `superseded: true` puts the declaration in the same append-only
store it is meant to govern, keyed by nothing, writable by the same POST that created the row —
which is how it drifts. **It belongs on the RUN, in the repo, beside the walk corpus**, because the
run is the unit Paul is actually judging (*"the FINAL SUCCESSFUL run of a synthetic"* — his noun is
*run*).

**The pattern to reuse is `approvedForServe`, and the fit is exact.** `rationalize-bench.py`'s rule,
in this repo's own words: *"`--apply` promotes ONLY cards carrying an `approvedForServe` stamp, and
nothing writes that stamp except `--approve <id>`, run by a human. An agent may run the report
freely; an agent may not approve a card."* Map it directly:

- an agent may run a walk freely, and every run is kept entire;
- **only a human command marks a run CURRENT** for a given synthetic household;
- every reader defaults to CURRENT and **refuses rather than guesses** when none is marked —
  `walk-integrity`'s existing posture, where an unmarked run is `refused`, never `assumed good`.

⛔ **What must NOT be reused: last-write-wins.** It is an inference, and Paul named precisely the case
where it inverts — *the aborted run is often the last one*.

**2 · Must it exist before step ②? — Yes, and the reasoning is ordering, not importance.**

Three facts compose:
(i) the pile-up in §7.1 is what a re-run produces, measured, in the environment where it has already
happened; (ii) under today's isolation model every synthetic household in production writes into
**Mom's estate** (§2.3); (iii) `reset-production-estate.py` is ruled **never to run again** after Mom
onboards, and cannot tell synthetic from real regardless.

> **After Mom onboards there is no eraser and no sorter.** So the marker that lets anyone tell the
> rows apart has to be on the rows **before** they are written, not after. This is not a claim that
> version control matters more than the cascade; it is a claim that it is **upstream** of it, in the
> same way `walk-integrity` was upstream of counting a walk.

**Falsifier:** if step ② runs each synthetic household in its own deployment (option 2.3(a)), each
with its own estate, then re-run pile-up is confined to that household's own store and never touches
`est-e6696a`. **In that case the ordering claim weakens to "before step ③"** — because Paul's own
property in production is the first household where a bad run is genuinely unrecoverable. It does not
disappear.

**3 · Is run identity the same mechanism as `context.synthetic`? — No. Keep them apart.**

They answer different questions and have different lifetimes:

- `context.synthetic` = **is this ours?** Boolean, permanent, stamped by the producer at capture,
  never revised. Its job, in its own text, is *"to let us find and remove OUR OWN test data."*
- run identity + CURRENT = **which of ours counts?** Multi-valued, **revisable by a human**, and
  meaningful only within one household's history.

**Merging them would make a provenance fact revisable**, which is the one property that makes it
trustworthy. ⚠️ **They do need to travel together**: a row today carries `context.synthetic` and
nothing that says which run wrote it, so even with a CURRENT declaration there is no join key. **The
extension needed is a `context.run` id on the same stamp site** (`onboarding/index.html:1514`), which
is additive and does not touch the boolean's semantics.

**4 · Existing patterns, ranked by fit — reuse, do not invent.**

| pattern | fit |
|---|---|
| ⭐ **the bench's `approvedForServe`** | **best.** Human-only stamp, agent may report but not approve, `--apply` acts only on stamped items. Exactly the authority model Paul described. |
| ⭐ **`walk-integrity`'s refusal model** | **best for the reader half.** Unmarked = refused, never assumed. `runs / countable / refused` is already the vocabulary; `current / superseded / undeclared` is the same three-state shape and adds no new state word. |
| **`question_state()` in `momlib.py`** | **strong.** *"the answer to 'what counts as settled?' — one function to read instead of four tools disagreeing."* A `current_run()` belongs in the same module for the same reason. |
| **`fold-answer.py`'s clamped watermark** | **relevant, as a warning.** Its recorded bug is exactly this class: a watermark stepped over an answer that still needed a human. Any supersede must not bury an un-dispositioned run. |
| **`verified_at_sha` provenance** | **adjacent, not it.** It says *when a claim was checked*, not *which of several competing claims wins*. |

⛔ **What I decline: the storage design, the command surface, and whether the walk corpus's
append-only property should ever be relaxed.** The first two are engineering-partner's; the third is
Paul's and I would argue against it, but arguing is not ruling.

### 7.4 · ⭐ AMENDMENT — this was built at `bb21863` while §7.1–7.3 were being written

**What landed, verified by execution at `fae767e`:**

- `onboarding/index.html` — `SYN_RUN` parses `?syn=<runId>` and **`SID` becomes the run id**, so the
  Worker's already-existing-and-always-null `sessionId` finally carries a value.
  `SYNTHETIC` widened from `/[?&]syn=1/` to `/[?&]syn=/`. **The join is exact:** a stored
  `sessionId` equals `.private/synthetic-walks/<role>/<runId>/`, so a KV row and a transcript meet
  without inference.
- `read-onboarding.py` — reports **four standings**: `current · superseded · unlinked · pre-date run
  identity`, plus `--current`. Authority is derived as *the newest run **walk-integrity will
  count***, with `.private/current-runs.json` (role → runId) as **Paul's override**.

**Against §7.3, point by point:**

| my proposal | what was built | verdict |
|---|---|---|
| declaration on the RUN, not the row | ✅ run id on the row, authority derived per run | **held** |
| reuse `walk-integrity`'s refusal posture | ✅ *"a run that fell over cannot become the authority by being late"* — current ≠ newest | **held, and better sited than I had it** |
| human-only stamp on the `approvedForServe` model | ⚠️ **inverted** — authority is **derived by default**, and the human file is the **override**, not the gate. `.private/current-runs.json` **does not exist yet**, so today nothing human has been stamped | **not what I proposed, and it may be the better call** — a derived default that a human overrides is reachable without a ritual, where `approvedForServe` needs one per item. ⛔ **Paul's ruling either way; I withdraw my preference and note only that the two differ.** |
| keep `context.synthetic` and run identity apart | ✅ separate fields, both on `context` | **held** |
| the join key I said was missing | ✅ **supplied, and it was already in the Worker's schema** — *"the field existed, the value existed, the storage existed, and one line never connected them"* | **closed** |

⭐ **Live reading at `fae767e`, and it is worth stating plainly:**

```
48 answer(s) · provenance: 0 real · 4 synthetic · 44 unknown
standing:     0 current · 4 superseded · 0 unlinked · 44 pre-date run identity
authoritative run per seat: mom=…T105930 · owner=…T110301 · strict=…T111207 · wide-eyed=…T111247
```

> **`0 current` is the correct and honest reading: the qa estate presently claims nothing.** The four
> countable walks pre-date run identity, so their rows can never be linked; the four stamped rows come
> from a later, uncounted run and are correctly superseded. **The pile-up in §7.1 is now legible
> rather than resolved** — which is the right first move, and it means §7.2's deeper finding still
> stands untouched.

⛔ **WHAT §7.4 DOES NOT CLOSE, and it is the half that matters most for step ②:**

1. **§7.2's storage split is unchanged.** Address and ranking still live **only** in the append-only
   feedback log; `placeName` and `accent` are still the only server-side state; and
   `estate/index.html` still renders its receipts from **`localStorage`** — it makes no GET to any
   endpoint. **A durable identity returning in a fresh browser still has a name and a colour and no
   address and no ranking.** Supersede now names a winner that nothing renders.
2. **Nothing is retro-linkable.** The 44 pre-existing rows are permanently unattributable. That is
   correct behaviour and it means the qa store can never be sorted, only aged out.
3. **`.private/current-runs.json` does not exist**, so Paul's override path is untested. A file that
   has never been written is not yet a mechanism.
4. **This is on `onboarding/index.html` only.** `estate/index.html`'s own POST to `/api/feedback`
   (`:368`) was not in the diff — ⚠️ **unverified whether the arrival surface's notes carry the run
   id.** If they do not, the one screen where a person says *"my ranking isn't here"* writes an
   unlinkable row.

**Falsifier for the whole of §7:** if `--current` on a re-run household returns the aborted run's
values, the derivation is wrong and the human stamp should become the gate rather than the override.

## 8 · F · WHAT IS UNOWNED

**Carried forward from the morning audit, still open:** A2 (undiagnosed POST failure) · B5 / RULE-2
(two — now three — terminal commits on one screen) · B3 (ranking renders no composed answer;
**partially answered by `3b7d7be`'s derived row on the estate screen, not on the ranking screen
itself**) · B2 (the "say what" invitation with no text field) · §E4 (disclosure sentences at
`class="quiet"`, fold unmeasured) · ARCH F2 (concurrent day-key writes lose an answer — **now more
live: two synthetic households in one estate is exactly two writers**) · ARCH F4–F9 (`unverified`,
not `open`) · the `legacy`/`production` rename · `fernwood-token` at mode `644`.

**New, and unowned:**

| # | thing | evidence | who could own it |
|---|---|---|---|
| U1 | **The offsite verifier is DOWN.** `launchctl list` → `com.paul.verify-offsite` last exit **1**. Log: `PermissionError: Operation not permitted: .../CloudDocs/Backups/git` — a TCC grant, not a code fault | `~/.claude/tools/verify-offsite.launchd.log` | `/team-audit` — it is stack, not work |
| U2 | **It does not watch encrypted bundles at all, by design.** `verify-offsite.py:64` — *"`_bundles` holds encrypted bundles, not bare repos, and is deliberately not a repo home"*, and `PARENT_TO_LOCAL` has no entry for it | same file | `/team-audit` |
| U3 | `synthetic-identity.py --create` blocked by `invite-required` — `worker.js` `handleAccountCreate` returns 403 without a grant (`c111417`, correct). The tool has no invite-minting step; `grant-mint.py` is the writer and the two are not wired | `worker.js` `handleAccountCreate`; `tools/synthetic-identity.py` | engineering-partner — **and it blocks step ②** |
| U4 | **The `handover` seat is registered and has no account anywhere.** `.private/synthetic-identities.json` holds 12 identities across lab/qa/home; none is `handover`. The role is added in an **uncommitted** working-tree edit | `git diff tools/synthetic-identity.py` | — |
| U5 | `.ux-reviews/2026-09-06-onboarding-handoff-seam.json` is **untracked**. A ux-expert return from today, outside version control | `git status --porcelain -uall` | — |
| U6 | **No read token exists for `home`, `lab` or `bob`; `bob` is in no reader's map.** §4.3 | `.private/` listing; `read-onboarding.py:33,40` | engineering-partner — **blocks step ④** |
| U7 | `.plans/` stage words — fourth instance. §3.4 | `check-backlog-ready.py:46` | Paul, one word |

---

## 9 · WHAT I DECLINE

- **Whether the cascade compresses or the Bob commitment moves.** §2.2 states both costs. The trade is
  a date given to a person against evidence quality; only Paul holds the first half.
- **Which of the three tenancy shapes step ② takes.** §2.3.
- **Whether a re-walk runs before step ②.** §5.2. I state the rule that would make either answer
  legible; I do not pick.
- **Whether the "production starts empty" promise or the "durable households in production" plan is
  the one that moves.** §2.4. Both are Paul's sentences.
- **How `qa-divergence` should treat bot commits on the legacy line.** §3.2 — it turns on whether the
  legacy weather line is still wanted, which is a question about Mom's live app.
- **Ranking any open defect against any other.** Not mine, ever.

## 10 · FALSIFIERS

1. **§3.1** is wrong if a fresh session reaches `walk-integrity.py` from `CLAUDE.md` alone. I tested
   by grep across all tracked files plus the skill/command/ritual surface; I did not spawn a session.
2. **§5.2's re-walk rule** is wrong if a staleness flag is overridden as noise twice. Then it is a
   nag and should be deleted.
3. **§7.3's ordering claim** weakens to *before step ③* if each synthetic household gets its own
   deployment and estate (option 2.3(a)).
4. **§3.2** is closed the moment `origin/main` stops receiving bot commits — no code change needed.
   If it is still red in a week having been cleared twice, the predicate is the problem.
5. **§6.1's "rulings are unreachable"** is wrong if `paul-ruled` stamps in code comments are
   discoverable by whatever a session actually reads first. I measured file extensions, not session
   behaviour.
6. **§2.3's "zero callers"** is wrong if `scopeFor` is invoked dynamically. I grepped for the literal
   `scopeFor(`; a dynamic dispatch would evade it.

## 11 · WHAT THIS AUDIT DID NOT DO

- **Did not read production's contents.** The read-only dry run was blocked (§0). Every production
  claim is `unverified`.
- **Did not read `bob`'s store.** No token exists.
- **Did not open the untracked `.ux-reviews/2026-09-06-onboarding-handoff-seam.json`.**
- **Did not verify any Worker's deployed code version.** No instrument can (§1, carried).
- **Did not read screenshots as images.** Every status is a string, a structure, or a live HTTP read.
- **Did not edit `BACKLOG.md`, `CLAUDE.md`, `VOCABULARY.md`, or any plan's `stage-note`.** Flags,
  never edits.

---

## ⛔ PAUL MUST RULE — five, ordered, and the first two block everything after them

| # | ruling | blocks |
|---|---|---|
| **1** | **Step ② — which tenancy shape.** A deployment per synthetic household (proven today with Bob, N permanent objects) · the `scopeFor` conversion across 51 sites · or synthetic households somewhere that is not production. **All three are available; none is free.** §2.3 | ②, ③, and every gate after |
| **2** | **The Bob window (09-07..09-10) against a cascade whose ② and ③ have not run.** Compress · move the date · or send Bob the least-walked build in the estate. §2.2 | ⑥, and how ④ is scoped |
| **3** | ⚠️ **Half-discharged at `bb21863`.** Run identity is built and authority is now DERIVED (newest countable run) with `.private/current-runs.json` as your override — **not** the human-gated stamp I proposed, and that file has never been written. **Rule: is derived-with-override the model, or does a run need your hand on it before it counts in production?** §7.4 | ② (or ③ — see falsifier 3) |
| **4** | **Does the re-walk rule bind — evidence expires when the build moves?** Yes/no, and if yes, does step ② re-walk `b784dc9` first. §5.2 | ② |
| **5** | **Where the cascade itself is recorded.** Auto-memory currently says three gates; there are now six. And `2026-09-05-release-cascade-tracking-PROPOSAL.md` — the file commissioned to hold this — is `stage: draft`, unruled since 09-05. §6.2 | nothing — which is why it will be re-litigated |

**Three cheap ones, not blocking, one word each:** the `.plans/` stage enum (fourth instance) · whether
`qa-divergence`'s legacy-line red is accepted-and-documented or re-predicated · whether U1/U2 (the
offsite verifier) hand to `/team-audit`.

**Not rulings — an agent can drive these unattended:** run `reset-production-estate.py` with no flag
(still punch-list row 1, now a day old) · mint `fernwood-token-home` and add `bob` to
`read-onboarding`/`synthetic-identity`'s maps · commit `tools/synthetic-identity.py` and track
`.ux-reviews/2026-09-06-onboarding-handoff-seam.json` · name the four new instruments in `CLAUDE.md`'s
session-start block, which is the whole of §3's remedy.
