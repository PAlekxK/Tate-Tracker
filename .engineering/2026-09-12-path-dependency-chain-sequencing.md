# PATH EVALUATION · the dependency chain, and the build sequence from a fresh slate

- role: **engineering-partner**, mode path-evaluation. Asked to verify the chain mechanically, propose a
  fresh sequence, name the smallest unblocker, and attack the plan.
- repo state: opened at HEAD `e261d9fa` as briefed; **HEAD moved to `041e4b46` during this session** (the
  standing backlog window is live). Every measurement below was taken between those two and is stamped.
  ⛔ Nothing in either commit touches `worker/` or `tools/` — the code readings are stable across the move.
- ⛔ **NO CODE WRITTEN, NO `BACKLOG.md` EDIT, NO DEPLOY, NO WRITE TO ANY ENVIRONMENT.** Two read-only
  instruments were run (`publish-digest.py --check`, `check-canon-scope.py`) plus greps and `git log`.
- ⛔ **PUBLICATION CONSTRAINT HONOURED.** `.engineering/` is tracked and `origin` is public. Two findings
  below carry estate names / place strings in their raw instrument output; **they are named by SYMBOL
  here and the literal readings are routed to `fernwood-private`.**

---

# ① IS THE CHAIN TECHNICALLY CORRECT?

## The mechanical basis re-measured — it holds, and it is FIVE routes, not four

`grep -n foreignCanon worker/worker.js` at `041e4b46`:

```
132  async function canonFor(env, scope)
148  function foreignCanon(env, scope)
2115 handleTodayLine       → foreignCanon
2188 handleClassify        → foreignCanon
2538 (throws "canon-not-this-estate")   ⬅ a FIFTH site the chain does not name
2967 handleChat            → foreignCanon
3478 handlePromoteSpecies  → foreignCanon
```

✅ **The claim that the journal's ASKING and a module's ADDING fail at the same line is TRUE.** The
falsifier the chain names (*re-run the grep before citing it*) passes today.

⚠️ **One correction: `:2538` is a sixth consumer** — `if (!(await canonFor(env, scope))) throw new Error(...)`.
It is inside the audio-identification path. The chain's own falsifier says the claim lapses if the routes
stop sharing the guard; it should say **five call sites**, and one of them raises rather than returning a
503, so it fails with a different shape. Cheap fix to the row; it strengthens the chain rather than
weakening it.

---

## ⛔⛔ THE ATTACK PAUL ASKED FOR — AND IT LANDS HARDER THAN HE SUSPECTED

**Paul's hypothesis:** *`canonFor` already reads `keyFor(scope,"digest")` per request, so the READ side may
already be correct — which would mean layer 1 is more available than the chain implies.*

✅ **Correct, and there are three more layers to it.**

### A · The canon read path is already on `scopeFor`, not `scopeOf`

`worker.js:4877`:

```js
const canonScope = scopeFor(request, env, grant);   // ⬅ the caller's estate, not the deployment's
if (url.pathname === "/api/today-line") return handleTodayLine(request, env, canonScope);
if (url.pathname === "/api/classify")   return handleClassify(request, env, canonScope);
if (url.pathname === "/api/chat")       return handleChat(request, env, auth, canonScope);
if (url.pathname === "/api/promote-species") return handlePromoteSpecies(request, env, canonScope);
```

⭐ **So the four routes the chain is built on are ALREADY CONVERTED.** The cutover (`scopeOf`→`scopeFor`)
does not gate layer 1 at all — layer 1's read half is *on the far side of it already*.

### B · The publish path exists and has been used

`tools/publish-digest.py` writes `<estateId>:digest`. `canonFor` reads exactly that key. **Both halves of
the per-estate canon substrate are shipped.**

### C · ⭐⭐ AND THREE ESTATES HAVE LIVE PUBLISHED DIGESTS TODAY

`python3 tools/check-canon-scope.py`, run 2026-09-12:

| env | estate | model routes |
|---|---|---|
| `dev` | est-lab0001 | ✅ resolves from its own published record |
| `home` | est-e6696a | ✅ resolves from its own published record |
| `paul` | est-d93508 | ✅ resolves from its own published record |
| `legacy` | est-3c9f1a | ✅ resolves — from the **bundled** digest, not a record of its own |
| `qa` | est-qa0001 | ⛔ **DARK — no record published for this estate** |

⛔⛔ **THEREFORE: TIER 2 · 12 IS NOT A `concept` ROW WITH NOTHING BUILT. Its read half, its publish half
and three of five live instances are SHIPPED.** The chain calls it *"the per-estate canon STORE — somewhere
a household's record can BE"* and marks it unbuilt. A household's record already **is** somewhere, and four
model routes already read it from there.

### D · ⛔ WHAT IS ACTUALLY UNBUILT — and the chain conflates it with the above

`grep OBSERVATIONS.put worker/worker.js` → **nothing writes `<estate>:digest` from inside the product.**
The published digest is a **build artifact**, composed offline from repo files and pushed by a terminal
command. `handlePromoteSpecies` still writes canon by committing `plants.json` + re-inlining `viewer.html`
through `ghPutFile`, behind `if (!env.GITHUB_TOKEN || !env.GITHUB_REPO) → 503`.

⭐ **So layer 1 is TWO things wearing one name:**

| layer 1's halves | state |
|---|---|
| **1-READ** — a household's record has a per-estate home a request can read | ✅ **SHIPPED** (`canonFor` + `publish-digest.py`, live at 3 estates) |
| **1-WRITE** — a confirmed entry made *in the product* can LAND in that record | ⛔ **UNBUILT** — canon mutation is still a git commit to this repo |

## ⭐⭐ THE FINDING THAT CHANGES THE ORDERING: LAYER 2 IS NOT GATED BY LAYER 1

The chain says layer 2 (the journal answers) is gated by layer 1. **Measured, it is gated only by 1-READ,
which is shipped.** The evidence is decisive: `home` and `paul` resolve canon from their own records
**today**. Row 15's actual blocker is the 60 hardcoded place literals in five prompt constants — a content
and parameterisation problem in `worker.js` that has **no dependency on where canon is stored**, because
`FACTS` already derives from whatever digest `canonFor` returns.

⛔ **Layer 3 and layer 4 ARE genuinely gated — by 1-WRITE.** That part of the chain survives intact, and it
is the part the MODULE ONBOARDING ⑤ thread measured correctly ("the seam is exactly and only at promotion").

### The corrected chain

```
0 · canon resolves per estate                      ✅ SHIPPED  a263ed3c
1a· the per-estate canon READ store                ✅ SHIPPED  canonFor + publish-digest  ⬅ was called unbuilt
2 · THE JOURNAL answers (row 15's 60 literals)     ⬜ REACHABLE NOW — gated by 1a only
1b· the per-estate canon WRITE path                ⬜ UNBUILT   ⬅ the real root
3 · THE ENTRY PATH                                 ⬜ gated by 1b
4 · MODULE RELEASE                                 ⬜ gated by 3
```

⭐ **The consequence for Paul's ruling:** the chain's own *"work at layers 2, 3 or 4 that does not first land
layer 1 is work that cannot be finished"* is **true for 3 and 4 and false for 2.** Journal work is
shippable today. That is a real option the adopted ordering currently forbids.

---

# ② THE BUILD SEQUENCE FROM A FRESH SLATE

**Two constraints shape everything and neither is negotiable:**

1. **Nothing migrates until the capture/write handlers take the caller's scope.** But the honest size of
   that is not 69 sites — see S2.
2. **The design WIP band is at 2/2** (`capture-write-path` + `zones`). A third design pass needs an
   exception. This is a real gate on parallelism, not a formality.

## ⛔ FIRST, TWO GATES IN THE BRIEF THAT ARE ALREADY DISCHARGED

**The brief says P2's body half (TIER 1 · 80) gates the capture-write-path build. It does not, as of today.**

- `.plans/2026-09-10-multi-tenancy-PLAN.md` § *The four changes* now reads
  **`### 1. … ✅ BUILT`** and **`### 2. … ✅ BUILT`**. The markers landed at `0a4799c0` (09-10 22:58).
- The plan was then **retired to `retro` at `853f76eb` (09-12 16:21)** — commit message:
  *"THE MULTI-TENANCY PLAN IS SPENT … the `design` band clears honestly 3/2 → 2/2."*
- `check-backlog-ready.py` confirms live: **`🚦 WIP bands: · design 2/2`**.

⭐ **This is Paul's own *"an unchecked box is not open work"* rule firing on his own board.** TIER 1 · 80 is
a closed thread still being relayed as a blocker between two lanes. **One cheap probe beat re-reading the
row.** Flagging, not ruling — the row is the standing window's to strike.

**And the code confirms both changes independently**, which matters more than the marker:

- **Change 1** — `grantFor()` at `worker.js` reads `route:<sha256(token)> → {personId/estateId}` FIRST and
  only then reads `<estateId>:grant:<hash>`, with a documented non-breaking fallback to the old
  deployment-scoped read. ⛔ **The claim carried in TIER 1 · 79 and in the lap-9 readiness — *"grantFor
  looks the grant up at `keyFor(scopeOf(env), …)` … the LOOKUP is the harder half"* — is STALE.** The
  harder half is built.
- **Change 2** — `POST /api/estate` → `handleEstateFound` → `writeEstatePlace()` at `:1420`, one caller at
  `:1510`. Built.

## ⛔ AND ONE GATE THE BRIEF DOESN'T NAME, WHICH IS LIVE

`python3 tools/publish-digest.py --check`, run 2026-09-12:

```
🔔 fernwood  est-3c9f1a — not published yet
⬜ home      cannot build — no estate-level place record (`est-e6696a:place`)
⬜ paul      cannot build — no estate-level place record (`est-d93508:place`)
⬜ qa        cannot build — no estate-level place record (`est-qa0001:place`)
```

⭐⭐ **READ THE TWO INSTRUMENTS TOGETHER AND THE FINDING APPEARS:** `check-canon-scope` says home/paul/dev
**have** published digests. `publish-digest --check` says they **cannot be rebuilt.** Both are right.

⛔ **So every live per-estate digest is an UNREPRODUCIBLE ARTIFACT from the refuted election path.** It was
composed when `household_property()` still *elected* a place by rank from member rows — the bug that put
one household's place into a test estate's prompt. `writeEstatePlace` replaced it with a place written
**once at founding**, by ruling: *"No election, no hand-declaration, no backfill by a different path."*
Every estate that predates `found` therefore has a digest it can never refresh and never reproduce.

⭐ **This is `~/.claude/engineering-principles/fernwood.md` § *"A deploy-bundled context artifact needs a
rebuild-and-diff drift alarm"* firing exactly as written.** The alarm works; nothing has acted on it.

⚠️ **And `check-canon-scope` reports 🔴 findings on `home` and `legacy` naming each other.** ⛔ Detail routed
to `fernwood-private` — it involves place strings. **The engineering point publishable here:** the
instrument cannot distinguish *a leak* from *two estate ids for one household*, and TIER 1 · 88 (which Mom
migrates) is precisely that unruled ambiguity. Until Paul rules 88, this instrument reports red for a
condition that may be correct — **a red that cannot be cleared by work teaches a lane to stop reading it.**

## THE SEQUENCE

⭐ **Read the numbers as a DAG, not a queue.** S1/S2/S3 are three independent lanes; the serial spine is
only S2 → S4 → S5 → S6.

| # | step | why HERE | size | parallel with |
|---|---|---|---|---|
| **S0** | **Strike the discharged gates**: TIER 1 · 80 (multi-tenancy plan is retired), the stale `grantFor` claim in TIER 1 · 79 + lap-9 readiness §0-PRIME, the chain's "four routes"→five | Costs minutes. Until it lands, **two lanes are holding for a gate that opened yesterday** and a build lane will re-derive a solved lookup problem | **XS** | everything |
| **S1** | **`configured.canon` on `/health`** — one boolean: did `canonFor` find a record for this deployment's own estate | ⭐ Today the only way to learn whether a household's journal can answer **is to ask the model and see if it 503s.** That is Paul's *"deterministic things need a non-AI door"* failing by the letter of its own falsifier. It is also the assertion `check-zones-containment.py` (B5) is already designed to read | **XS** | S2, S3 |
| **S2** | **The capture/write slice of the cutover — 14 sites, 6 handlers, NOT 69** | The router **already computes** the correct scope at `:4877`. Converting `handleSuggestSpecies`(3) · `handleZoneSave`(2) · `handleZonesGet`(2) · `handleZoneFeedback`(2) · `handleZoneAudio`(4) · `handlePromoteSpecies`(1) means threading `canonScope` into six calls. ⛔ **Do this BEFORE B1 reshapes `handleZoneSave`, not after** — otherwise the same handler is opened twice and the second open is a merge against fresh code | **S–M** | S1, S3 |
| **S3** | **The journal lane — row 15's 60 literals** (research → design → plan, the three phases Paul asked for) | ⭐ **REACHABLE NOW, on the finding above.** No dependency on 1b. Needs a design-band exception (band is 2/2) or waits for `zones` or `capture-write-path` to advance. It is seat work (content-steward + ai-advisor) far more than build work, so it loads a *different* resource than S2/S4 | **M** design, **L** build | S1, S2, S4 |
| **S4** | **B0 → B1 → B4 → B5 → B6** — the capture-write-path build, exactly as audited in `.engineering/2026-09-12-capture-write-path-build-PLAN.md` | The plan is written, audited and the three corrections are in it. Its gate (TIER 1 · 80) is open. **B0 first** — the replay harness is how falsifier 3 is proved without deploying to the frozen env | **M–L** | S3 |
| **S5** | **1b · the canon WRITE path** — `handlePromoteSpecies` writes the estate's canon to KV instead of committing `plants.json`; `publish-digest` becomes a *reader* of that, not the only writer | ⭐ **This is the actual root, and it lands cheaply after S2+S4** because promote-species is already caller-scoped and zone-save's git decoupling (B1) is the same pattern one handler over. ⛔ It needs one ruling first — see the attack, §④·d | **M** | — |
| **S6** | **Layer 3 (entry path) → layer 4 (module release)** | Genuinely gated by S5. The chain is right here | **L** | — |
| **—** | **The `myhome-prod` migration** | ⛔ **Not in this sequence and should not be.** It needs S2 **plus** the remaining ~55 `scopeOf` sites **plus** TIER 1 · 88's ruling **plus** an `<estate>:place` for every migrating estate. Sequencing it against the chain is a category error: the chain is about *reachability*, the migration is about *correctness at two estates* | **L** | — |

### What runs in PARALLEL, stated plainly

- **S1 + S2 + S3** are three lanes with no shared file of consequence. S1 touches the `/health` block, S2
  touches six handler signatures, S3 touches prompt constants and produces documents.
- **S3 is the one that buys the most calendar time**, because its long pole is seat work (which of the 60
  literals is an estate fact vs. register that travels vs. a habitat model needing a per-place source) and
  that pole can be walked while S2/S4 are in the build window.
- ⛔ **S2 and S4 must NOT be parallel.** Same handler, same lines.
- ⛔ **S5 must not be parallel with S4.** Same decoupling pattern; doing them together means one lane learns
  the pattern and the other guesses it.

---

# ③ THE SMALLEST THING THAT UNBLOCKS THE MOST

⭐⭐ **`configured.canon` on `/health` — one boolean, roughly four lines.**

```js
// in the /health handler, beside configured.github / configured.anthropic
canon: !!(await canonFor(env, scopeOf(env))),
```

**Why this and not something bigger:**

1. ⛔ **It is the only missing piece of the guard the whole chain rests on.** Five call sites refuse when
   `canonFor` returns null, and **nothing anywhere can ask whether it will.** `check-canon-scope.py` reads
   the digest through `wrangler kv`; `guru-probe.py` grades answers but is QA-only with no `--env`. Neither
   can be run from a deployment, by CI, by `post-deploy.py`, or by a person.
2. ⭐ **It is Paul's own falsifier, verbatim.** *"If the only way to learn whether a site is up is to ask
   Claude, this is broken."* Today the only way to learn whether a household's journal can answer is to ask
   Claude. This is the non-AI door.
3. ⭐ **It would have caught the live finding by itself.** `qa`'s routes are dark because **no digest is
   published for est-qa0001**, which is a deterministic, greppable fact — and it has instead sat for a day
   as TIER 1 · 72's *"missing `ANTHROPIC_WORKSPACE_ID`"* hypothesis and TIER 1 · 14's *"a263ed3c fixed it"*
   claim. **Neither is the cause.** A canon boolean on `/health` turns a two-candidate folklore row into a
   one-line read. (⚠️ Stated as a code + KV read, not a live confirmation — see §⑤.)
4. ✅ **It is already wanted downstream.** The audited capture-write-path plan's **B5** asserts via `/health`;
   `post-deploy.py` already compares `/health`; TIER 1 · 71's row already names `/health.configured.github`
   as *"the only reader of the REAL state."* This is the same move, one field over.
5. ⭐ **It unblocks measurement, which is what the board is actually short of.** Six of the rows read for
   this evaluation carry an unverified claim about whether a route can answer.

**Honest caveat, so it is not over-sold:** it does **not** unblock a feature. It unblocks *knowing*. The
smallest thing that unblocks the most **work** is **S0** (striking the discharged gates), which costs
minutes and frees two lanes — but that is bookkeeping, not engineering. I am naming both.

---

# ④ WHAT IS WRONG WITH THIS PLAN

### a · ⛔⛔ The chain's layer 1 names a shipped thing as unbuilt, and it changes what is reachable

Covered in §①. **The single most consequential defect:** *"Everything Paul wants to release sits on one
unbuilt store"* is not true. It sits on one unbuilt **write path**. The store exists, is published at three
estates, and is read per request. **Journal work (layer 2) is reachable today** and the adopted ordering
currently tells a lane it is not.

### b · ⚠️ The chain adopts REACHABILITY as the priority ordering and reachability is not the same as VALUE

Four layers, stacked. Nothing in the shape says *how much any layer is worth to the person using it*. The
weather-card conflict (8·3/9·2 vs. the chain) is the first instance and the backlog records it honestly as
unruled. **It will not be the last** — the chain will mechanically demote every user-visible item beneath
every engine item, forever, because engine items are structurally lower in a dependency graph. ⭐ **A
reachability ordering is a CONSTRAINT (never build the unreachable) and a poor OBJECTIVE FUNCTION.** The
honest shape is: *reachability filters the candidate set; value ranks what is left.* That is one sentence
in the adoption block and it prevents a year of silent demotions.

### c · ⚠️ "70 `scopeOf` call sites" is a scary number attached to the wrong unit

69 at HEAD, and **22 of them are inside `handleFeedback` alone**. The real unit is ~34 functions, and the
slice the chain actually needs is **14 sites across 6 handlers**. ⛔ **A count with no predicate makes the
cutover look like a quarter's work when the part that gates layer 3 is a day's.** Several of the remaining
55 *legitimately* mean the deployment (`/health`, `env-canary`, the chat budget ceiling) and must never
convert — so the denominator is not even a target.

### d · ⛔ 1b IS A DATA-MODEL RULING WEARING A BUILD ROW, AND NOBODY HAS TAKEN IT

TIER 2 · 12 says this of itself (*"a data-model decision, not a build"*, *"fires W6"*), and then the chain
made it the root of the ordering — which reads as *schedule it*. ⭐ **It cannot be scheduled, because the
question under it is unanswered:** when a household confirms a plant, does it get a row in *its own*
species record, or a pointer into a **shared species library** with a per-estate instance record? That is
W6, deferred since July. **Every module in layer 4 inherits the answer.** ⛔ Building 1b without ruling W6
means building the wrong store and discovering it at vehicles.

### e · ⚠️ The falsifier is unfalsifiable in practice

*"If a lane completes a layer-3 or layer-4 item and ships it to a household without TIER 2 · 12 existing,
this chain is wrong."* ⛔ **A falsifier that can only fire by someone violating the ordering the chain
itself imposes will never fire.** ⭐ A falsifier that *can* fire: **"if `configured.canon` reads true at a
household and a layer-2 item still cannot ship, layer 2's gate was never layer 1."** That one is testable
this week — and on today's measurement it **already fires** at `home` and `paul`.

### f · ⚠️ The orthogonal track is described as orthogonal and is not, for the handlers that matter

The chain says the cutover *"crosses the chain rather than sitting in it."* For the model-read routes, true
— they are already converted. ⛔ **For the capture handlers it is not orthogonal, it is the same edit.**
`handleZoneSave` needs (i) the gate moved below the KV write, (ii) git demoted behind the token guard,
(iii) its scope taken from the request. Those are three changes to one function. Treating them as two
independent tracks means opening it twice.

### g · ⚠️ An assumption worth naming: `dev`/`home`/`paul` resolving canon is being read as health

They resolve from digests that **cannot be rebuilt**. A green reading from an unreproducible artifact is a
green reading with no source. ⛔ **The `<estate>:place` backfill has no path by ruling** — so today the only
way to make `home`'s digest reproducible is to found its estate again. **That is an unnamed dependency of
the `myhome-prod` migration**, and it is upstream of TIER 1 · 88 rather than downstream.

---

# ⑤ WHAT I COULD NOT VERIFY

- ⛔ **Nothing was POSTed and no request was made to any deployment.** Every environment reading came from
  `wrangler kv` reads via the two repo instruments. The `qa`-is-dark conclusion is a **code + KV read**,
  deterministic but one step short of *seen*. **The confirming act: one `/api/today-line` POST at `qa`.**
  If it answers, this finding is wrong and the DARK reading has a cause still unfound — which is the more
  valuable outcome.
- ⚠️ **Whether `publish-digest --apply` was ever run at `home`/`paul`/`dev`, or whether their digests
  arrived another way.** `check-canon-scope` proves the key is populated; it cannot prove who populated it.
- ⚠️ **W6's status.** I read it only as cited by TIER 2 · 12; I did not open its original.
- ⚠️ **HEAD moved under this session** (`e261d9fa` → `041e4b46`). Re-run `git log -1` before citing any
  line number here; the row text may have moved even where the code has not.

---

# ⑥ RULINGS THIS EVALUATION NEEDS FROM PAUL — flagged, not taken

| # | the question | why it cannot be inferred |
|---|---|---|
| **R1** | ⭐⭐ **Does layer 2 come off the chain's layer-1 gate, given 1-READ is shipped?** | It reopens journal work as buildable now. A lane must not decide this by reading a row |
| **R2** | **Reachability filters; what ranks?** Value, the release cascade, the objective register? | The chain is currently doing both jobs and was adopted to do one |
| **R3** | **W6 — shared species library vs. per-estate species rows** | 1b cannot be designed without it and every layer-4 module inherits it |
| **R4** | **TIER 1 · 88 — which Mom migrates** | `check-canon-scope` reports an uncleannable red until this is ruled |
| **R5** | **The 8·3/9·2 weather-card conflict** | Already named as live in the backlog; R1 changes the terms, because journal work becomes a third option rather than the chain's only reachable one |

---

# ⑦ PRINCIPLES PROPOSED — not added; Paul's confirmation first

### A gate you did not open yourself must be re-verified before it is relayed
**Statement**: Before relaying "X is blocked by Y," read Y's own artifact at today's HEAD — never the row
that cites it.
**Why**: TIER 1 · 80 was discharged at `853f76eb` (09-12 16:21) and was still being relayed as a live gate
on two lanes hours later. `grantFor`'s "harder half" was built and still cited as unbuilt.
**When it applies**: any cross-lane dependency claim; any row whose blocker lives in another document.
**Avoid**: citing a gate from the row that names it; treating an unmarked plan section as unfinished work
(the *code* is the evidence, the marker is the record).

### A dependency ordering filters; it does not rank
**Statement**: Reachability decides what is *possible*; something else must decide what is *worth doing*.
Never let a dependency graph be the objective function.
**Why**: a DAG structurally places engine work beneath user-visible work, so adopting it as the priority
ordering silently demotes everything a person can see, permanently.
**When it applies**: any time a dependency chain, blocker graph or readiness ladder is proposed as "the
priority."
**Avoid**: a queue derived from a graph with no value axis; resolving a value conflict by pointing at depth.

### Every refusal guard needs a deterministic door that answers "would you refuse?"
**Statement**: If code can refuse a request, something must be able to ask — without invoking the thing
being guarded — whether it *will*.
**Why**: `canonFor`/`foreignCanon` guards five routes and nothing can read its state; the only probe is to
ask the model and watch for a 503. That is Paul's *deterministic things need a non-AI door* failing by its
own falsifier, and it cost a day of hypothesis on `qa`.
**When it applies**: any fail-closed guard, allow-list, or capability gate.
**Avoid**: inferring a guard's state from a downstream symptom; a health endpoint that reports bindings but
not the resolutions those bindings feed.
