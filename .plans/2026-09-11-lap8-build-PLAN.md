# Lap 8 — THE BUILD PLAN (DRAFT). The door and what it makes possible, by symbol

- **stage:** `draft`
- **ready:** `agent-proposed — draft against lap 7's outcomes; re-audited at lap 8's open before the build window reads it`
- **row:** `cycle/release/CYCLE-LOG.md` § *Laps 8 and 9 — SCOPE COMMITTED BY RULING* (`767242c`) · `.plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md` §1
- **objective:** O3 · **class:** engine
- **Author:** engineering-partner, mode **path-evaluation**, second enactment of the COMMIT-PHASE RULE
  `[paul-stated 2026-09-10]`, commissioned early `[paul-stated 2026-09-11: "have the build expert audit those two
  commitments as well and produce the build plan like we did in the most recent lap… once we get to a point where
  it's defined enough for a detailed work plan to be built out of it."]`
- **Source of the commitment:** `cycle/release/CYCLE-LOG.md:2698–2736` — the twelve rulings 8·1…8·6, 9·1…9·4,
  D = 10 sessions, G accepted by inclusion. Quoted, never restated.
- **This file changes no code and is not a ruling.** It audits the commitment, orders the work, names a check per
  step. Where it recommends changing the commitment it says so in §2 and **Paul decides**.

### ⭐ TWO RULINGS LANDED WHILE THIS WAS BEING WRITTEN, AND BOTH CHANGE STEPS BELOW

1. **The production origin's ADDRESS is the apex domain `myhome.place`** `[paul-ruled 2026-09-11]` — registered
   2026-09-03 at Cloudflare Registrar, zone active, **0 DNS records today** (C4 2a) **[relayed by the coordination
   window; I did not read the zone]**. ⛔ **Row B grows four steps** (B6a–B6d): bind the Pages project to the apex,
   the DNS records, `tools/pages-deploy.py`'s `ORIGIN` map, and — the one that matters — **the link Mom receives is
   the apex, never `myhome-paul.pages.dev`.** ⚠️ **The product NAME is still unruled and still precedes B** (8·4).
   *An address is not a name;* C4 Q1 ruled the first and explicitly not the second.
2. **Lap 7's row B gained B0 and re-ruled B6** `[paul-ruled 2026-09-11]` **[relayed]** — `/api/account/available`
   gets **its own rate bucket**, split from the household's capture bucket (so §3 A13's "regardless" clause is
   **lap 7's now, not lap 8's**); and the `account-recovery` record lands in **its own admin-only key with its own
   reader**, **no email lookup this lap**, **one constant honest sentence**, with the reset rule written to
   **`VOCABULARY.md` §3e·R** `[paul-ruled 2026-09-11 ~12:45 AM ET]`. ⭐ **That closes §2 A9's open half:**
   V8's rule is no longer in a human's head, and **lap 8 · C inherits it as a citation rather than re-deriving it.**

### ⚠️⚠️ THE SHA THIS WAS WRITTEN AGAINST, AND IT MOVED WHILE I READ

| | |
|---|---|
| **HEAD at the first read** | `1302358` (*"lap 7 P4: instance/paul.json declares ack + questions absent"*) |
| **HEAD at the last read** | `06c2a16` (*"lap 7 row B: security-steward read of the recovery route"*) — **five commits in one reading window** |
| **What that means for this plan** | ⛔ **Every MEASURED line below is stamped `06c2a16` unless it says otherwise, and the lap-7 build window is still committing.** Three of lap 8's own preconditions (B1 · B2 · B3) were **not landed** at `06c2a16` — §2 A1. **Re-run §2's measurements at lap 8's open**; do not carry a count from this file into a build. |
| **The rule this obeys** | CLAUDE.md's concurrent-session guard. I wrote no tracked file but these two, staged nothing, and ran no network probe. |

### What I read (each one opened, not cited from a summary)

`cycle/release/CYCLE-LOG.md` §Lap 7 (`:2463–2697`: beats 1–6, AMENDED Q1–Q8, THE ENVIRONMENT MODEL, the *"synced"*
ruling, the teardown, the readback) and § Laps 8/9 (`:2698–2736`) · `.plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md`
(whole) · `.plans/2026-09-10-lap7-build-PLAN.md` §1, §2 (A1–A10), row P, D, C, **B1 · B2 · B3 · B10**, row H (**H3**),
§4 SEAMS, §5, §6, §7, §8, §9 · `.plans/2026-09-10-multi-tenancy-PLAN.md` (whole) ·
`.plans/2026-09-10-cross-device-signin-FINDINGS.md` §5 · `.plans/2026-09-10-OPEN-ITEMS.md` ⓪ ① ② ③ ④ ⑤ ·
`.plans/2026-09-10-teardown-REPORT.md` §2, §5 · `.plans/2026-09-03-product-name-PLAN.md` (header + the three-level
table) · `.engineering/2026-09-10-recovery-route-SECURITY.md` (DENOMINATOR, ① ROSTER V1–V8, R-A, THE CLOSE) ·
`VOCABULARY.md` §3i · `BACKLOG.md` TIER 1 · **19 · 25 · 30 · 36 · 37 · 41 · 43 · 46 · 48 · 49 · 50** and TIER 2 ·
**7 · 8 · 10 · 11 · 12 · 13 · 18 · 19 · 20 · 25**, § 🤝 INVITE & JOIN, § 📮 ADDRESS VALIDATION ·
`worker/worker.js` (`scopeOf` · `scopeFor` · `scopeOfRoute` · `keyFor` · `assertScope` · `grantFor` · `personFor` ·
`handleSession` · `handleAccountCreate` · `handleEstateFound` · `canonFor` · `hostAgrees` · the `/api/account/available`
branch · the route table) · `worker/wrangler.toml` · `tools/pages-deploy.py` · `tools/journey-walk.py`
(`JOURNEY_IDS` · `JOURNEYS` · `NAMED_UNBUILT` · the `--fresh`/refresh path) · `tools/falsifier-tenancy.py` (clauses) ·
`tools/household-export.py` (existence) · `cycle/release/CYCLE-MAP.md` § The beats.

**Run read-only:** `git log`, `git status`, and greps over `worker/worker.js` and `tools/`. **No network probe, no
live KV read, no deploy.**

**Not read, and named so nothing here pretends otherwise:** `tools/check-household-isolation.py` beyond its name ·
`tools/household-export.py`'s code (I verified it exists; I did not read what it exports) · `tools/grant-mint.py` ·
`tools/watch-door.py`'s roster · `.plans/2026-09-07-weather-card-PLAN.md` beyond its header block · any live origin.

---

# 1 · THE HEADLINE, before anything else

**Lap 8 removes the mechanism that has been doing the isolating, and replaces it with code.** Today an estate is a
deployment: `myhome-paul` cannot read `fernwood-home`'s KV because it is a different namespace. After row A,
production is one origin and the only thing standing between Mom's record and Paul's is that **every key-building
site resolved the caller's estate instead of the deployment's**. `measured` at `06c2a16`: **55 non-comment
`scopeOf(env)` call sites** against **3** `scopeFor(...)` sites, one of which discards its result
(`worker.js:4443`, `eslint-disable-line no-unused-vars`).

⛔ **An unconverted site does not error. It writes into the deployment's estate, silently.** And the deployment's
estate at the production origin will be **`est-d93508` — Paul's condo** (`wrangler.toml:206`), because
`myhome-paul` becomes THE production origin (Q7). So the failure mode of a missed site is *Mom's feedback lands
under Paul's estate prefix*, which is the exact class this repo has measured twice (the 09-07 gauge leak, the
09-08 digest-in-every-prompt leak) — and **no check in the pickup block can see it**: `check-estate-neutral.py`
tests shipped pages for names, `check-canon-scope.py` tests the digest, and neither reads a KV write path.

**So the build order is forced, and it is not the order the commitment lists:**

> **the classifier → the conversion → the falsifier at lab → the door surface → (Paul's word) → the migration.**

The classifier comes first because **the falsifier cannot cover the conversion**. `falsifier-tenancy.py`'s clauses
are C1 (a dangling route must 404), C2 (A cannot NAME B across the surfaces a caller controls — it probes a handful),
C3 (B answers as B), C4/C5 (a foreign administrator invite confers nothing). Every one of them is *estate-A-vs-
estate-B at the routes it probes*. **None of them asks whether site 41 of 55 was converted.** A green falsifier over
an incomplete conversion is precisely CLAUDE.md's own standing rule — *a control can be entirely correct and still
not cover the thing you rely on it for* — and lap 8 is the lap most likely to earn a fourth entry in that table.

**The good news, and it is large.** The primitives are built and correct: `assertScope()` refuses an `env` or a
string at a key builder, so a *forgotten* site throws rather than mis-keys; `scopeOfRoute()` exists; `grantFor()`
already routes through `route:<hash>` with the 404-never-fallback guard the plan demanded; `personFor()` exists and
separates identity from authority; `canonFor(env, scope)` is **already per-request** (`worker.js:132–147`), so the
model routes are not this lap's problem. **This lap is adoption plus one classifier, not a rewrite.**

---

# 2 · AUDIT — where the sources disagree, what is underspecified, what I recommend changing

- stage-note: 2026-09-11 ~3:00 AM ET — the product's STARTING name is RULED (My **Home** Place; product-name plan Q3), so row B's name gate (8·4) is MET; the build-side strings ride beside the apex binding: onboarding/index.html:7,:304 · estate/index.html:7,:172 · homes/index.html:270 fallback · the apex page · VOCABULARY §3b (amended). Re-audit at open confirms the sites. (coordination)
## A1 🔴 BLOCKING · Lap 8's three named lap-7 dependencies were **NOT LANDED** at `06c2a16`

The commitment names **B1 · B2 · B3** as preconditions "all three are lap 7 Worker steps." `measured` at HEAD
`06c2a16`, by symbol:

| step | what it must become | what is there today |
|---|---|---|
| **B1** | `estates` from the person's grant | `worker.js:1008` — `estates: [{ estateId: scope.id, … }]` (**the deployment's**) |
| **B2** | revoke at the grant's scope | `worker.js:977` — `env.OBSERVATIONS.delete(keyFor(scope, "grant", acct.tokenHash))` (**the deployment's**) |
| **B3** | route the account write through `putAccount` | `worker.js:979` — `env.OBSERVATIONS.put(accountKey(scope, username), …)` (**direct**) |

These are the exact two line numbers FINDINGS §5 named (*"fix `handleSession:979` and `:977` before the M2
backfill"*). Lap 7's build window has landed P1–P4, D1–D4 and the B6 security read (`bd74e76`, `8a2021b`,
`06c2a16`); **row B's Worker steps are still ahead of it.**

⭐ **Recommendation: this is not a slip — it is a sequencing fact, and the lap-7 slip table already prices it.**
`.plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md` §3 says *B1 slips → lap 8 · A slips a lap*; **that is too blunt.**
The honest reading is narrower and better: **B1 is superseded, not depended on.** Lap 8 · A9 replaces the single-
element `estates` literal with the array from `grantsFor(personId)` — so if lap 7 ships B1, lap 8 rewrites that line
anyway; if lap 7 drops B1, lap 8 writes the correct version once. **B2 and B3 are real dependencies and are small.**
**Put to Paul:** if lap 7's window is tight, **B1 may be dropped into lap 8** (it is one literal, and A9 owns it);
**B2 and B3 may not** — B2 is a live credential that survives a sign-out, and B3 is the trap M2's backfill arms.

## A2 ⬆️ CHANGE · **The multi-tenancy plan is stale in three of its four changes, and a planner reading it would plan work already done**

`.plans/2026-09-10-multi-tenancy-PLAN.md` is the door's specification and the commitment cites it by name. `measured`
at `06c2a16`:

| the plan's "four changes" | state today |
|---|---|
| **1 · the router row + `grantFor()` + backfill** | ✅ **BUILT.** `ROUTE_PREFIX = "route:"` (`:1519`); `grantFor` reads the router, verifies `row.estateId === routed`, **404s on a dangling route** (`:1565–1582`), and keeps a non-breaking legacy fallback (`:1590`). `tools/grant-route-backfill.py` exists. |
| **2 · `POST /api/estate`** | ✅ **BUILT.** `handleEstateFound` (`:1387`), routed at `:4370`, authenticated by `personFor` not `grantFor` (so an estate-less person can reach it — the empty shelf). Place first, **grant last**, router after the grant. |
| **3 · the 60 call sites** | ⛔ **NOT STARTED**, and the number is wrong three ways — see A3. |
| **4 · `hostAgrees()` / `FAMILY_HOSTS`** | ⛔ **NOT STARTED.** `hostAgrees` (`:1596`) still reads `FAMILY_HOSTS`. |

⚠️ **And its key shape is superseded by a later ruling the plan never learned.** It specifies
`credential:<sha256(token)> → { estateId }`. The code writes **`route:<hash> → { estateId, personId }`**
(`:1494`, `:975`), and `.plans/2026-09-10-OPEN-ITEMS.md` ④·1 rules the destination is **`route: → {personId}` alone**,
plus a `grant:<personId>:<estateId>` edge — *"conforming to a ruling already made — the design specified
`route: → {personId}` and nobody had noticed."* **Three documents, three key shapes, one repo.**

⭐ **Recommendation: amend the multi-tenancy plan's header and its §"The four changes" BEFORE the build window
reads it** — mark 1 and 2 ✅ BUILT with their symbols, and replace the `credential:` key with the ruled
`route: → {personId}` + the grant edge. This is the scope proposal's own READY condition (*"the plan has no header…
it needs `row:` · `stage:` · `seats:`"*) and it is cheap. ⛔ **Do not let the build window discover this by reading
code that disagrees with its brief** — that is how a lane rebuilds something and calls it a finding.

## A3 ⬆️ CHANGE · **"The 60 call sites" is a moving number, and batching by line is the wrong unit**

Three numbers for one thing, all in the tree today: the plan says **60** (`scopeOf(env)`, measured 09-10);
`worker.js:4424`'s own comment says *"`scopeOf(env)` sits at ~51 sites"*; `BACKLOG.md` TIER 1 · 19 says **51 call
sites (~30 carrying real per-household data)**. **`measured` at `06c2a16`: 55 non-comment sites, 41 `keyFor(` sites,
104 `env.OBSERVATIONS` references.** The surface grew while the plan sat.

⭐ **Recommendation: batch by KEY KIND, not by count, and make the count a tool's output rather than a plan's claim.**
The kinds are already the decision boundary. `measured` histogram at `06c2a16`:

| batch | kinds | sites | the call |
|---|---|---|---|
| **B-CALLER** — must convert | `feedback` 2 · `metrics` 2 · `conversation` 1 · `onboarding-metrics` 1 · `observations`(OBS_KEY) 2 · `audio-blob` 3 · `zone-audio` 2 · `zone-audio-blob` 2 · `zone-feedback` 2 · `zones` 3 · `zones-last-seen` 2 · `pending-species` 3 · `cost-log` 2 · `library` 3 | **30** | a household's own record; a missed one writes Mom's words under Paul's prefix |
| **B-CACHE** — convert, and it is not obvious | `cache` 4 (`ambient` · `airnow` · `drought` · `today-line`) | **4** | ⚠️ **the keys carry the payload**: `keyFor(scopeOf(env),"cache","ambient",mac,…)` (`:1850`) and `…"airnow",lat,lon` (`:1899`). Collapsed to one prefix, **a key listing enumerates every household's station MAC and coordinates.** Contents would be *correct* and the key space would be a directory of where everyone lives |
| **B-DEPLOY** — DECLARE, do not convert | `ratelimit` 3 (door · feedback · obmetrics) · `door` 2 · `grant` 2 (grantFor's legacy fallback) · `chat-budget` 2 · `/api/account/available`'s `accountFor` 1 · `/health` · `env-canary` | **~13** | each is a deployment-wide control and is **correct** as `scopeOf(env)`; ⛔ a door record precedes any household by construction (`watch-door.py`'s own rule) |
| **B-SENTINEL** | whatever `ESTATE_ID` becomes at the production origin | — | A4 |

⭐⭐ **Recommendation, and it is the single highest-value step in the lap: build `tools/check-scope-sites.py`
BEFORE converting anything.** Every `scopeOf(env)` site is either **converted** or **DECLARED deployment-scoped with
a written reason**, and an **unclassified site is RED**. This is `check-engine-manifest.py`'s exact shape (*is every
tracked file classified engine/config/instance?*) applied to the one inventory that decides whether two households
share a namespace safely. **Why it earns its keep, stated as the falsifier:** if the conversion lands, the falsifier
passes at lab, and the checker never once goes red across lap 8 and lap 9, **delete it** — it measured nothing.

## A4 🔴 UNDERSPECIFIED · **Nothing says what `ESTATE_ID` is at the single production origin**

`estateId(env)` **throws** when the binding is missing (`worker.js:1044`, *"a Worker that cannot say whose estate it
serves must not read or write a record"*). That was written for one household per deployment. Under one origin for
everyone, **the binding either names a household (and every B-DEPLOY key lands in that household's prefix) or it
names something that is not a household.** No document I read answers this.

**Two shapes, and they trade differently:**

| | **(a) a SENTINEL** — `ESTATE_ID = "est-prod00"`, owned by no person | **(b) keep `est-d93508`** (the condo) |
|---|---|---|
| B-DEPLOY keys | land under a prefix that belongs to nobody — honest | land under **Paul's** prefix — a ratelimit row filed inside a household |
| a missed B-CALLER site | writes into a namespace no person reads → discoverable as junk | writes into **Paul's estate** → looks like his data, reads as his data |
| the bundled digest fallback (`canonFor`, `:145`) | never fires; every estate reads its published digest. ⚠️ **`legacy` keeps its own deployment, so nothing regresses for Mom-today** | fires for the condo only — already true |
| `check-canon-scope.py` | reads a sentinel cleanly | reads Paul's estate as production's identity |
| cost | one `wrangler.toml` var and one retired id | zero |

⭐ **Recommendation: (a), the sentinel, and mint the id the same way an estate id is minted so nothing special-cases
it.** The *why*: the whole point of A2's classifier is that a missed site should be **findable**, and a wrong write
into a namespace nobody owns is findable while a wrong write into a real person's namespace is camouflage. It also
keeps `assertScope`'s promise intact — the deployment still has a scope, it is simply not a household. ⛔ **This is a
ruling-shaped question, not a build decision.** §9.

## A5 🔴 THE COMMITMENT'S OWN "done means" CONTAINS A CLAUSE LAP 8 CANNOT WALK — **s3**

Row A's done-means is Paul's four *"synced"* clauses `[paul-ruled 2026-09-10 ~10:05 PM ET]`:

> **(s1)** written on one device, readable on another by the same person · **(s2)** scoped to the household and the
> account, never the browser · **(s3)** **the owner sees a member's contribution** · **(s4)** the administrator sees
> it from any of his devices.

`measured`: **s3 requires two people in one household, and after lap 8 there are none.** INVITE & JOIN is ruled
*"not this round"* and its build is off lap 9's path (9·1/9·4); `handleEstateFound` grants `relationship:["owner"],
capability:"member"` to the founder and to nobody else (`:1466`); the `grant:<personId>:<estateId>` edge that would
carry a second member is unbuilt (④·1); and `.plans/2026-09-10-OPEN-ITEMS.md` ⑤·1 states that **no instrument in
this project can see within-estate, cross-person** — `falsifier-tenancy.py`'s C1/C2/C3/C5 are all estate-A-vs-B.

**Three honest options:**
1. **Declare s3 OUT OF LAP 8 by name**, as a clause the lap does not claim — the same move `journey_lifecycle`'s
   **L13** makes for the administrator's reset (*"a genuine coverage boundary, not a gap to close with a mock"*).
2. **Hand-mint a second grant** at a qa estate and walk it. ⚠️ This proves the *read path* and proves nothing about
   how a second person legitimately arrives — and minting a relationship to be convenient is the move the multi-
   tenancy plan explicitly forbids (*"a lifecycle tool that minted relationships to be convenient would make the
   consent gate decorative"*).
3. **Pull INVITE & JOIN's build into lap 8** — contradicts 9·4 and is a lap's worth of work on its own.

⭐ **Recommendation: (1), and say it on the release note.** s1 · s2 · s4 are all walkable in lap 8 (§5) and they are
the clauses the door actually buys. ⛔ **Do not score s3 passed on a hand-minted grant** — that asserts a person did
something, which is `check-arrival-dispositions`' rule applied to a walk.

## A6 ⬆️ CHANGE · The harness has **no way to walk s1/s2/s4** — one person, two devices

`tools/journey-walk.py` runs **one browser context per walk**. `refresh(role, env)` (`:67`) re-mints a token before
each run; every journey's `arrival` is a single credential in a single context. There is no `--second-context`, no
storage-state handoff, nothing that can express *"write here, read there."* **So the lap's own falsifier — Paul's
words, *"what I wrote is here when I come back on another device"* — has no stop that can fail.**

⭐ **Recommendation: a harness step, in this lap, before the battery** — a second context in one run, same account,
signed in twice (which is also the only honest way to assert B2's revoke: sign in on context 2, assert context 1's
token now 404s). §3 row H. ⛔ **Without it row A's done-means is unreadable**, and this is the same shape as lap 7's
H2/H3 (*"needs a sign-out/return journey stop `journey-walk.py` does not have — a harness item in the build plan"*).

## A7 · SEAM · **The second-estate refusal is a ruled invariant that lap 9 reverses — and lap 8 must not quietly break it**

`handleEstateFound:1403–1407` returns **409 `already-has-an-estate`**, with its own comment: *"ONE ESTATE PER PERSON,
FOR NOW, AND THE REFUSAL IS THE POINT… a second one cannot be reached until a request can say WHICH — and that is the
unruled question."* `walk-founding.py`'s acceptance clause **B** pins that refusal as correct behaviour.

⚠️ **Lap 8 · A9/A10 (the `estates[]` array and `X-Estate`) are exactly "a request can say WHICH."** The moment they
land, the 409's stated reason is false — and OPEN-ITEMS ①·2 says `X-Estate` **must now be built** and *"the 'refuse
a second estate' workaround is dead."* But **the ruling for lap 8 is one door, not a second house** (9·1 puts
J0 × 2 in lap 9).

⭐ **Recommendation: build the array and the header in lap 8; leave the 409 STANDING, and rewrite its comment to say
why it still stands** (*the mechanism now exists; the founding surface for a second place does not — lap 9 · C*).
⛔ **Do not delete a refusal because its stated cause dissolved.** The lap-7 plan's B4 makes the same move in
reverse (*"the build window must rewrite that comment, not work around it"*). And `walk-founding.py` clause B must
be updated in the **same commit** or the harness goes red on correct behaviour.

## A8 · SEAM · The existence oracle is **two routes, not one**, and the door only closes half of it

The commitment names security-steward on row A for `GET /api/account/available` — correctly. But
`.engineering/2026-09-10-recovery-route-SECURITY.md` is sharper and its finding must ride into the lap 8 brief:
*"do not 'fix' it by deleting the availability route. Deleting it costs a person a bounced signup form to protect a
fact the **409 still publishes**."* `handleAccountCreate` answers 409 on a taken username; the availability route is
a courtesy over the same truth. **The single door changes the question from *does this username exist at this
deployment* to *does this username exist at all*** — a strictly larger disclosure, because there is now one
namespace to enumerate instead of five.

⭐ **Recommendation: the seat rules the disclosure BEFORE the conversion, not after** — and the one constraint
already ruled is carried verbatim into the brief: **no redirect door that names which house a username lives at**
(FINDINGS §5). ✅ The rate-bucket half is **ruled into lap 7 as B0** (the header block) — *"a capture bucket and a
probe bucket are different tiers"*, `worker.js:4377` `feedbackRateLimitOk` **[read]**.

⭐⭐ **AND THE ORACLE POSTURE IS A SENTENCE, NOT A POLICY — this is the half a build window will get wrong.**
There are two candidate honest lines and only one of them is true:

| the line | verdict |
|---|---|
| *"we do not confirm whether an email address is on file"* | ✅ **TRUE and sayable.** No route publishes email existence; with B6 re-ruled to **no email lookup this lap**, the response cannot vary with the truth even by timing |
| *"we never reveal whether an account exists"* | ⛔ **FALSE, and forbidden.** `GET /api/account/available` answers it unauthenticated (`:4374–4384` **[read]**) and `handleAccountCreate`'s **409** publishes the same fact to anyone who tries the name. A door that claims a secret a sibling route gives away is worse than one that says nothing — it teaches a reader the wrong threat model and it is falsifiable in one curl |

⛔ **The two facts are different and the copy must keep them apart: USERNAME existence is published (by design,
because signup needs it); EMAIL existence is not.** The single door does not change either fact — it changes the
*size* of the enumerable space from one deployment's accounts to all of them. ⚠️ **Deleting the availability route
does not fix it** (SECURITY, verbatim: *"deleting it costs a person a bounced signup form to protect a fact the 409
still publishes"*). **The structural answer is the ruled one — the single door — and the copy must be honest about
what it does and does not protect.** §9 Q3, §10.

## A9 · SEAM · **The email editor's write path and the recovery route are the same security object** — ✅ half now ruled

Row C's constraint is stated in the commitment (*"editing the recovery address is a takeover vector, so the editor's
write path must not be weaker than sign-in"*), and **the rule that makes it real is now written down**:

> **`VOCABULARY.md` §3e·R — THE RESET RULE** `[paul-ruled 2026-09-11 ~12:45 AM ET]`: *"A recovered credential is
> delivered to the contact value ON THE ACCOUNT ROW, never to the value in the request, and never to a reply-to…
> a request naming an address is not an identity claim — it is a doorbell."* **[read]**

⭐ **Lap 8 · C therefore CITES this rather than re-deriving it** — which is exactly what the ruling was written for
(*"until tonight it lived only in a human's head"*, the SECURITY V8/R-E finding). **What lap 8 · C still owes is the
other half: the write path.** §3e·R secures where a credential goes; **nothing yet secures who may change the
destination**, and an editor is precisely the surface that changes it.

Plus SECURITY CLOSE item 6, unchanged: **B10 cannot be built from `whoami` today** — read the email from the account
row **inside** the whoami branch; ⛔ do not widen `PLACE_FACTS`, which would put a contact value into the register.

⚠️ And the honest boundary the ruling itself states: email is *"self-asserted, unverified, non-unique, and freely
settable by any signed-in person (`/api/profile`)"*. ⭐ **Recommendation: lap 8 · C ships the editor with (i) a
re-authentication step, (ii) the account-row read, and (iii) one honest line — and §3e·R supplies the reasoning for
all three, so the copy has an authority to cite.** ⛔ **No email lookup this lap** (the re-ruled B6), so the editor
must not introduce one by the back door: a *"we'll check that's not already in use"* affordance would mint the email
oracle the ruling just refused. §9 Q4.

## A10 · SEAM · **`check-data-inline.py --fix` and `build-viewer.py --extract` are live traps on row G's path**

Row G moves `MOM_ACK_DATA` out of `engine/viewer.template.html:12022` and into the instance. CLAUDE.md's session-start
block carries two ⛔⛔ warnings measured on 09-07 and 09-08: `--extract` writes rendered emptiness back over the
template's placeholders, and `--fix` re-inlines **into both** `viewer.html` **and** the template, burning Fernwood's
concrete values over the engine's placeholders — *"instance content burned into the engine, which is the exact class
the estate-neutrality work exists to prevent."* **Row G's step is the same substitution contract C4 5b ratified for
identity**, so the shape is known — but the two tools that touch it are the two tools with tripwires.

⭐ **Recommendation: after every `--fix` or rebuild on row G, `git diff engine/viewer.template.html` and revert the
template if it moved.** Put it in the step, not in a note. Only `viewer.html` should change.

## A11 · SEAM · `household-import.py` **is unwritten, and row B cannot start without it**

`measured`: `tools/household-export.py` exists (15,922 bytes, 2026-09-10); **`tools/household-import.py` does not
exist.** OPEN-ITEMS ④·4: *"Export is fixed. ⛔ Nothing in Phase C runs until both exist."* Row B's gate is therefore
**a build plus an act**, not an act. §3 row B.

## Also audited, and found to need no change

- **`canonFor` is already per-request** (`:132–147`) and the `CANON_FOREIGN_OK` escape is deleted, not defaulted. The
  09-08 *"every deployment carried Fernwood's whole record into five model routes"* class is **closed in code**. Row
  A does not reopen it, and `check-canon-scope.py` remains the second reader.
- **`grantFor`'s legacy fallback is safe under one origin by key construction** — its own comment proves it
  (`:1584–1589`): the key it reads is `<this deployment's estate>:grant:<hash>`, so it can fail to find a foreign
  grant but cannot return the wrong estate's row. ⚠️ Under the **sentinel** (A4) it finds nothing at all, which is
  correct; the backfill is what keeps live credentials alive.
- **`pages-deploy.py`'s `HOUSEHOLD = {"paul","home","qa"}` allow-list** (`:87`) is not row A's to change. When
  production collapses to one origin the labels retire (VOCABULARY §3i: *"the labels retire when the deployments
  collapse, not before"*) — but `home` is still a deploy target until row B tombstones it. **Leave it alone in row
  A; row B edits it.**

---

# 3 · ORDERED STEPS, BY SYMBOL

**Legend.** `[read]` = I opened the file and verified the symbol at `06c2a16`. `[inferred]` = derived from what I
read; the window must confirm. `[not verified]` = I did not check; the window must measure before acting.
**MOVES CANDIDATE** = the step changes what a seat walks, so a fix after the battery is a new sha.

**Build order:** **P → A → C → E → F → G → riders → H** … then **the lab falsifier gate** … then **B (Paul's word)**.

## ROW **P** — preconditions (nothing here is optional)

### P1 · Re-measure A1's three symbols; declare B1's disposition
- **check** — `grep -n "estates: \[{ estateId: scope.id" worker/worker.js` (B1) · `:977` (B2) · `:979` (B3).
- If B2/B3 are still unlanded at lap 8's open, **they move into row A as A0a/A0b** (they are two lines) and the
  release note says lap 7 shipped without them. B1 is superseded by A9 either way (§2 A1).
- **MOVES CANDIDATE:** yes (Worker). **serves:** A.

### P2 · Give `.plans/2026-09-10-multi-tenancy-PLAN.md` a header and mark changes 1 and 2 BUILT
- **change** — `row:` (TIER 1 · 46) · `stage:` · `seats:` per the scope proposal · and §2 A2's corrections: 1 ✅, 2 ✅,
  the key shape replaced by `route: → {personId}` + the grant edge.
- **why** — `check-backlog-ready.py --ladder` reads it `absent`, and the build window's brief points at it. A brief
  pointing at a stale specification is how a lane rebuilds a shipped thing.
- **MOVES CANDIDATE:** no. **serves:** A, and the row's READY rung.

### P3 · A still HEAD, declared
- **why** — OPEN-ITEMS ③: *"Gate ① is 0 of 5 and this is STRUCTURAL… `handover` passed all six clauses today, the
  first time ever, and expired when the tree moved. Main took 107 commits."* **The next lap needs a still HEAD as a
  precondition, not a favour.** This plan was written across five commits (the header block).
- **MOVES CANDIDATE:** no. **serves:** the battery.

### P4 · The pickup block, green or explained — `check-engine-manifest.py` · `check-storage-keys.py` ·
`build-viewer.py --check` **plus the headless load** · `check-estate-neutral.py --page /tmp/<neutral build>`
- ⛔ **A green `--check` is not a working page** (CLAUDE.md; lap 7 §7 risk 1). Declare the candidate on a `lab`
  deploy that passed `pages-deploy.py`'s `page_errors_on_load()`, never on `--check`.

## ROW **A** — the door (16 steps)

### A0 · ⭐ **`tools/check-scope-sites.py` — the classifier, BEFORE any conversion**
- **new file** — reads `worker/worker.js`, finds every non-comment `scopeOf(env)` site, and requires each to be
  either (i) gone (converted) or (ii) present **with a declared reason** in a small register the tool reads.
- **what it prints** — converted N · declared-deployment N (with reasons) · ⛔ **UNCLASSIFIED N (red)**; and the
  inverse clause: a `keyFor(` whose scope came from neither `scopeFor` nor a declared site.
- **boundaries on its own face** (CLAUDE.md's rule that a control states what it does not cover): it reads **source,
  not behaviour** — it cannot tell you a converted site resolved the *right* grant, only that it stopped reading the
  deployment. **That question is the lab falsifier's (A15), and neither covers the other.**
- **check** — `--selftest` proves each clause can fail: an undeclared site is red · a declared one with an empty
  reason is red · a `keyFor` with a bare `env` is red.
- **falsifier for the tool itself** — if it never goes red across laps 8 and 9, delete it.
- **MOVES CANDIDATE:** no. **serves:** A, and it is the precondition for A2–A4.

### A1 · Declare the production origin's `ESTATE_ID` (§2 A4) — **Paul's ruling, then one var**
- **file:symbol** — `worker/wrangler.toml` `[env.paul.vars] ESTATE_ID = "est-d93508"` (`:206`) **[read]** ·
  `worker.js` `estateId(env)` (`:1044`) **[read]**.
- **change** — on the sentinel ruling: mint `est-<6hex>` the same way founding does, set it as the production
  origin's binding, and **retire `est-d93508` as a deployment binding while keeping it as Paul's estate row**.
- ⛔ **Blocked on §9 Q1.** Everything downstream builds keys under whatever this says.
- **check** — `/health` reports the new id; `falsifier-tenancy.py --setup` runs at lab under the same shape.
- **MOVES CANDIDATE:** yes. **serves:** A.

### A2 · Convert **B-CALLER** (30 sites, by key kind, in reviewable batches)
- **file:symbol** — every `keyFor(scopeOf(env), <kind>, …)` / `dateKey(scopeOf(env), …)` / `blobKey(…)` in the
  B-CALLER table of §2 A3 **[read — line numbers listed there are at `06c2a16` and will move]**.
- **change** — `scopeOf(env)` → `scopeFor(request, env, grant)` at each, resolving the grant the handler already has.
  ⚠️ **Not mechanical** (the plan's own word). Each site is a decision; batch by kind so a reviewer sees one question
  at a time.
- ⛔ **The handler must already hold a resolved grant.** Where it does not, the site is either genuinely deployment-
  scoped (move it to B-DEPLOY with a reason) or the route is unauthenticated and must not write household data at
  all. **A third answer — "pass `scopeOf(env)` for now" — is the silent-wrong-key case `assertScope` cannot catch.**
- **check** — `check-scope-sites.py` after each batch; `node --check worker/worker.js`.
- **MOVES CANDIDATE:** yes. **serves:** A · s1 · s2.

### A3 · Convert **B-CACHE** (4 sites) — and say in the code why the key shape matters
- **file:symbol** — `:1850` ambient (`mac`) · `:1899` airnow (`lat, lon`) · `:1940` drought (`fips`) · `:1986`
  today-line (`date`) **[all read]**.
- **why it is its own step** — these four are the only keys whose **suffix is household-identifying data**. Left on
  `scopeOf(env)` under one origin, a key listing is a directory of every household's coordinates and station MAC.
  ⭐ This is the 09-07 gauge-leak lesson at the key layer: *the leak was numbers, not names*, and no needle list can
  see it.
- ⚠️ **Cost, stated honestly:** per-estate cache keys reduce the hit rate (two households in one county no longer
  share an airnow row). **That is the correct trade and it should be a comment, not a surprise.**
- **check** — a KV key listing at lab after two households fetch weather contains **no coordinate outside its own
  estate prefix**.
- **MOVES CANDIDATE:** yes. **serves:** A.

### A4 · **Declare** B-DEPLOY (~13 sites) — annotate, do not convert
- **file:symbol** — `ratelimit` `:1141` `:1651` `:4324` · `door` `:1159` `:1640` · `grantFor`'s fallback `:1590` ·
  `chat-budget` `:2948` `:4084` · `/api/account/available`'s `accountFor` `:4381` · `/health` · `env-canary` **[read]**.
- **change** — one line per site naming *why the deployment is the right scope*, in the form `check-scope-sites.py`
  reads. ⛔ A door record precedes any household by construction; a ratelimit is an IP control; the chat budget is a
  per-deployment ceiling. **These are correct and must stay correct.**
- **check** — `check-scope-sites.py` reports 0 unclassified.
- **MOVES CANDIDATE:** no (comments + a register). **serves:** A.

### A5 · **M1** — `route:` stops naming the estate
- **file:symbol** — `handleSession`'s route write (`:974–976`) · `handleEstateFound`'s (`:1493–1495`) ·
  `personFor` (`:1540`) · `grantFor`'s router read (`:1565–1571`) **[all read]**.
- **change** — the route value becomes `{ personId }` alone (OPEN-ITEMS ④·1, *conforming to a ruling already made*).
  `grantFor` then resolves **person → grants → the estate the request names**, not person → one estate.
- ⛔ **A5 and A6 are ONE commit.** Dropping `estateId` from the route before `grantsFor` exists leaves `grantFor`
  with nothing to resolve — every credential dies at once. **This is the plan's own *"backfill first"* warning
  moved to a different key.**
- **check** — `falsifier-tenancy.py` C1 (a dangling route 404s, never the deployment's estate) stays green;
  every existing credential still resolves at lab after the backfill.
- **MOVES CANDIDATE:** yes. **serves:** A.

### A6 · **M2** — the `grant:<personId>:<estateId>` edge, and `grantsFor(personId)`
- **file:symbol** — new writer beside `handleEstateFound`'s grant write (`:1483`) and `handleSession`'s (`:963`);
  new reader `grantsFor(env, personId)` **[new]**.
- **change** — every grant write also writes the edge; `grantsFor` lists a person's estates by KV prefix.
- ⚠️ **Backfill before the reader ships.** Same rule as the router row: an edge nobody wrote is a person with no
  houses.
- ⛔ **B3 (lap 7) is the trap this arms** — `handleSession`'s direct `accountKey` put bypasses `putAccount`, so once
  an index exists the authoritative row goes stale on `tokenHash` at the first sign-in (FINDINGS §4.1(4)). **If lap 7
  did not ship B3, ship it here, before A6.**
- **check** — a founded seat's `grantsFor` returns exactly its own estates; a person with none returns `[]`.
- **MOVES CANDIDATE:** yes. **serves:** A · the shelf.

### A7 · **M4** — `X-Estate`: a request names WHICH house
- **file:symbol** — the route table's gated branches; `scopeFor(request, env, grant)` (`:1052`) **[read]** — it
  already takes `request` and ignores it. *"The host step lands with multi-household"* is its own comment.
- **change** — `scopeFor` reads `X-Estate` when present, **verifies the caller holds a grant at that estate via the
  A6 edge**, and 404s otherwise. Absent header + exactly one grant → that estate. Absent header + several → ⛔ **a
  named refusal, never a guess.**
- ⛔ **OPEN-ITEMS ①·2 is an open ruling** (*"the 400 collision"*). §9 Q2.
- **check** — `falsifier-tenancy.py` C2: *A cannot NAME B* — now with the header as one of the surfaces a caller
  controls. **This clause must be extended to probe `X-Estate` explicitly or C2's denominator silently shrinks.**
- **MOVES CANDIDATE:** yes. **serves:** A.

### A8 · `hostAgrees()` / `FAMILY_HOSTS` becomes an ordinary CSRF control
- **file:symbol** — `hostAgrees` (`:1596`) **[read]** · `wrangler.toml` `FAMILY_HOSTS` per env **[read]**.
- **change** — one origin, so the host check no longer carries tenancy. Keep it; rewrite the comment to say what it
  now is. ⛔ **Do not delete it** — it is still the only thing refusing a cross-site POST.
- **check** — a request with a foreign `Origin` is still refused at lab.
- **MOVES CANDIDATE:** yes. **serves:** A.

### A9 · `/api/session` returns the **array** of estates (supersedes lap 7 · B1)
- **file:symbol** — `handleSession`'s response literal `:1008` **[read]**.
- **change** — `estates: await grantsFor(env, acct.personId)`, each row `{estateId, relationship, capability,
  placeName}`. A person who has founded nothing gets `[]` — **the empty shelf, normal, not an error state**
  (`.plans/2026-09-10-account-estate-model-SCOPE.md` §5.1, cited via `walk-founding.py`).
- **check** — journey stop: sign in as a founding-less account → `[]`; as a one-house account → length 1.
- **MOVES CANDIDATE:** yes. **serves:** A · the landing branch.

### A10 · The 409 stays; its comment is rewritten (§2 A7)
- **file:symbol** — `handleEstateFound:1403–1407` **[read]** · `tools/walk-founding.py` acceptance clause **B**
  (`:246–271`) **[read]**.
- **change** — the comment says *the mechanism now exists (A7); the founding surface for a second place is lap 9 · C;
  until then the refusal is a product decision, not a technical limit.* **Same commit** updates clause B's wording so
  the harness is not red on correct behaviour.
- **MOVES CANDIDATE:** no (comment + tool text). **serves:** A, lap 9 · C.

### A11 · **The single sign-in page** — one door for the account
- **file:symbol** — `onboarding/index.html` `#s-door` / `#s0` / `#si-*` (the lap-7 A2 door work) **[not verified at
  `06c2a16` — lap 7's row A had not landed when I read]**.
- **change** — one form at the production origin. ⛔ **No per-house doors. No redirect door that names which house a
  username lives at** (FINDINGS §5, verbatim). The refusal string stays the **one constant string** lap 7's B11
  ships — wrong password, unknown username and another house's credential must remain byte-identical.
- ⚠️ **All copy is a slot** — content-steward's, DRAFT, human-confirmed before it reaches a person.
- **check** — journey: wrong password vs unknown username produce byte-identical `#si-trouble` text; a `door_failed`
  record carries **no username** (`grep -rn "username"` over the write path — lap 7 §7 risk 6's check, re-run).
- **MOVES CANDIDATE:** yes. **serves:** A.

### A12 · **The shelf after sign-in** — the landing branch on the real count
- **file:symbol** — `onboarding/index.html:1217` (`location.href="/viewer.html"`) **[read via lap-7 plan A3]** ·
  `homes/index.html` **[not verified]**.
- **change** — branch on `estates.length`: **0 → `/homes/` (the empty shelf) · 1 → `/viewer` · 2+ → `/homes/`**.
  Now honest because A9 supplies a real count.
- ⚠️ **Row content stays name + town only** (lap 7 A22). The shelf lists houses; it does not preview them.
- **check** — three journey walks, one per branch. ⛔ The 2+ case has **no fixture until lap 9 · C** — walk it at lab
  with two hand-founded estates for one person **as a mechanism test, declared as such**, not as a J-journey.
- **MOVES CANDIDATE:** yes. **serves:** A · s2.

### A13 · `/api/account/available` — the disclosure, ruled then built (§2 A8)
- **file:symbol** — `:4374–4384` **[read]**, incl. the shared `feedbackRateLimitOk` bucket (`:4377`).
- **change** — (i) whatever security-steward rules; (ii) **regardless: its own rate bucket**, not the household's
  capture bucket.
- ⛔ **Blocked on the seat.** §9 Q3.
- **MOVES CANDIDATE:** yes. **serves:** A.

### A14 · The migration rehearsal at lab — **before any real row moves**
- **change** — found two estates for one person at lab (or two people, one estate each), run the whole surface.
- **check** — `falsifier-tenancy.py` **C1 · C2 · C3 · C5 all green**, plus `check-scope-sites.py` **0 unclassified**
  — ⛔ **both, and neither substitutes for the other** (§1).
- **MOVES CANDIDATE:** no. **serves:** the gate before B.

### A15 · ⭐ **THE GATE BEFORE B** — the multi-tenancy falsifier, verbatim, at lab
> *"Two accounts on one deployment, each having created their own estate, where every read one makes for the other's
> estateId returns 404 — and a grant presented for estate A cannot name estate B by any route."*
- **ruled** 8·2: **B comes after this passes at lab.** ⛔ Not after it is *written* — after it **passes**.
- **check** — `python3 tools/falsifier-tenancy.py --env lab` (with `--setup` for the C4/C5 fixture) exits 0 with no
  clause UNPROVEN, at the candidate sha.
- **MOVES CANDIDATE:** no. **serves:** B.

## ROW **C** — the email editor (5 steps)

### C1 · Read the email from the **account row**, inside the whoami branch
- **file:symbol** — `settings/account/index.html` whoami read **[not verified]** · `worker.js` `/api/grant/whoami`
  response literal **[not verified — cited from the security read]** · `handleSession`'s `email: acct.email || null`
  (`:1000`) **[read]**.
- ⛔ **Do not widen `PLACE_FACTS`** — it puts a contact value into the register (SECURITY CLOSE item 6).
- **check** — the three states of lap 7 B10 render from a page load with no fresh sign-in; ⛔ **never simply absent**.
- **MOVES CANDIDATE:** yes. **serves:** C.

### C2 · The write path — **re-authenticate before a recovery address changes**
- **file:symbol** — `/api/profile`'s account branch (`:4226` area) **[not verified — cited from the security read]**.
- **change** — a change to `email` requires the current password (or a fresh session, per Paul's ruling). Other
  profile fields do not.
- **why** — the commitment's own words: *"editing the recovery address is a takeover vector, so the editor's write
  path must not be weaker than sign-in."* Today `email` is *"unverified, non-unique and freely settable"*; behind an
  account whose password recovery reads that field, **whoever can set it can take the account.**
- **check** — a journey stop: change the address without the password → refused; with it → accepted and shown back.
- **MOVES CANDIDATE:** yes. **serves:** C.

### C3 · Cite §3e·R at the site, and give it a test
- **change** — a comment at the editor's write path citing **`VOCABULARY.md` §3e·R**, and the rule's own falsifier
  turned into a check: *a credential sent to an address that appears in a recovery request and not on the account
  row* **[read, §3e·R verbatim]**.
- ⭐ **This is a citation step, not a derivation step** — the rule is ruled. ⛔ Do not restate it in prose here or in
  the code; a second copy of a security rule is a second rule.
- ⚠️ **Lap 7 ships the recovery *request*; nothing delivers a credential.** *"The route's purpose is out of scope of
  the route"* (SECURITY V8). **Lap 8 · C does not close that** — it closes the editor. **Say so on the release note.**
- **MOVES CANDIDATE:** yes. **serves:** C.

### C4 · The honest line about what the address is for — and ⛔ **no lookup behind it**
- **change** — one sentence, grounded in §3e·R: this address is where a recovered credential goes; it is not
  verified and it is not how we know who you are. ⛔ **Copy is a slot** — content-steward's.
- ⛔ **The editor must introduce NO email lookup** — no *"already in use"*, no availability check, no differing
  response. The re-ruled B6 removes the lookup from recovery; an editor that adds one back **mints the email oracle
  at the other end of the same flow.** ⭐ *A fact protected on one route and published on another is not protected*
  — the username lesson (§2 A8), one field over.
- **check** — after C1–C4: `grep -rn "email" worker/worker.js` over the new write path shows **no read keyed on an
  address** and **no key whose suffix is an address** (RR-7: a plaintext `email:` key is refused).
- **MOVES CANDIDATE:** yes (copy + code). **serves:** C.

### C5 · The lifecycle journey gains an editor stop
- **file:symbol** — `tools/journey-walk.py` `journey_lifecycle` (lap 7 H3, stops `L01…L15`) **[read as specified;
  not yet present at `06c2a16`]**.
- **change** — a stop between **L03** (the email renders) and **L04**: tap Edit → re-auth → change → shown back.
- **check** — `journey-walk.py --journey J8 --role owner --env qa`, zero failed actions.
- **MOVES CANDIDATE:** no. **serves:** C's falsifier.

## ROW **E** — the Midtown repoint (3 steps)

### E1 · `tools/check-condo-falsifier.py` → `instance/paul.json`
- **file:symbol** — its `SCRATCH` default (`.private/condo-falsifier/`) **[cited from teardown §2; not verified in
  the file]**. Paul: *"use the Grant Park condo to inform them."*
- **check** — green against `instance/paul.json`; ⛔ exit 3 = UNCHECKABLE, never green by absence.

### E2 · `tools/place-claims.py` → `instance/paul.json`, ledger regenerated
- **file:symbol** — `LEDGER = .private/condo-falsifier/uniqueness-ledger.json` **[cited from teardown §2]**.
- ⚠️ **`place-claims.py --check` is in CLAUDE.md's pickup block** — deleting the directory before the repoint breaks
  a pickup check. **Repoint, prove, then remove.**
- **check** — `python3 tools/place-claims.py --check` green; no row unclassified.

### E3 · `trash` the scratch directory (⛔ never `rm` — `~/Developer` is a protected root)
- **check** — `grep -rn "condo-falsifier" tools/` returns nothing; both tools still green; no file under `instance/`
  names Midtown; `check-estate-neutral.py` reads the removal as a fix.
- **MOVES CANDIDATE:** no (all three). **serves:** E.

## ROW **F** — the fixture stamp, **qa/lab only** (4 steps)

### F1 · `OPEN_SIGNUPS_ARE_FIXTURES` on `[env.qa]` and `[env.lab]` **only**
- **file:symbol** — `worker/wrangler.toml` `[env.qa.vars]` (`:43`) · `[env.lab.vars]` (`:104`) **[read]**.
- ⛔ **The production origin and `legacy` never set it.** The deployment decides; **never the applicant** — a
  client-claimed fixture flag would let a real signup mark itself disposable.
- **check** — `grep -n OPEN_SIGNUPS worker/wrangler.toml` shows exactly two blocks.

### F2 · `handleAccountCreate` reads it
- **file:symbol** — `handleAccountCreate` (`:643`); the invite-inherited stamp at `worker.js:803` **[cited from
  teardown §5; the line is at `:803` per that report]**.
- **change** — an open-door signup at a stamped deployment sets `fixture: true`. An invited signup keeps inheriting
  from the invite, unchanged.
- **check** — a J0 seat walk at qa produces an account reading `signupVia:"open", fixture:true` (today: `false` on
  all seven, teardown §5 Gap 1).

### F3 · `handleEstateFound` carries it forward
- **file:symbol** — `handleEstateFound`'s `grantRow` (`:1466`) and `writeEstatePlace` call (`:1481`) **[read]** —
  neither contains `fixture` today (Gap 2).
- **change** — copy `person.fixture` onto the founding grant row **and** the place row.
- **check** — a house founded by a stamped seat has a stamped founding grant.

### F4 · `household-fixtures.py --teardown` proves it
- **check** — at qa, a house founded by a seat **after** F2/F3 tears down with **zero REFUSED rows**; the same run
  at the production origin finds **zero stamped rows by construction**.
- ⛔ **An unmarked row is still a STOP, not a skip** — the tool's rule is unchanged and must stay unchanged. The
  fourteen existing houses stay hand-work against teardown §5's evidence table.
- **MOVES CANDIDATE:** yes (F2/F3 are Worker). **serves:** F.

## ROW **G** — the ribbon seam (4 steps)

### G1 · `MOM_ACK_DATA` becomes an instance-supplied domain, on the ratified substitution contract
- **file:symbol** — `engine/viewer.template.html:12022` (the concrete literal) **[cited from TIER 1 · 50 and the L4
  finding; not opened by me]** · `tools/build-viewer.py`'s IDENTITY/domain substitution (C4 5b) **[not verified]** ·
  the gates at `viewer.template.html:12555` and `:13583` **[cited from commit `1302358`]**.
- **change** — the literal becomes a placeholder fed from `instance/<env>.json`; Fernwood's lines move **into
  `instance/fernwood.json`**, where they have always belonged.
- ⛔ **Never write Paul's line into the literal** — that inverts the leak (TIER 1 · 50, verbatim).

### G2 · **"none" is the honest empty**, and it is a content question one card down
- **change** — a household with no acknowledged input renders **no ribbon**, not an empty one. ⚠️ This is the same
  question as TIER 1 · 43 (*"the 'Your Perspective' card was there but empty"* — an affordance-without-signal on the
  founding path). **Answer both in one brief or mint a second empty state.**
- ⛔ **content-steward's**, not the build window's. §10.

### G3 · The template-diff tripwire (§2 A10)
- **check, every time** — after any `check-data-inline.py --fix` or rebuild: `git diff engine/viewer.template.html`.
  **Only `viewer.html` should change.** Recovery if it moved: `git checkout -- engine/viewer.template.html`.

### G4 · The reader TIER 1 · 50 asks for
- **check** — a build at any non-Fernwood instance renders **no** Fernwood ribbon text (grep the built page for the
  literal's phrases → nothing), **and Fernwood's own build is byte-identical to before** (`build-viewer.py --check`).
- **MOVES CANDIDATE:** yes. **serves:** G.

## RIDERS (3 steps) — *an event with no reader is not instrumentation*, and now: *an ask with no ledger is not a loop*

### R1 · TIER 1 · 37 — `GET /api/onboarding-metrics` and its reader
- **file:symbol** — the POST-only branch and the read at `:3907` **[read]**.
- **change** — a GET route plus a named reader (extend `watch-door.py`, per the row's own pointer).
- **check** — the reader prints the position-vs-preference series for a walked seat at qa.

### R0 · ⭐ **`tools/ask-ledger.py` — the ASK LEDGER reader** `[paul-ruled 2026-09-11]` **[relayed; spec pending]**
- **new file** — **derived, never typed.** Per ask: **served · answered (COUNTS, never people) · folded into which
  household-record field · which feature row it links to.**
- ⚠️ **Its full spec is being written by the ask-design window** — `.plans/2026-09-11-ask-design-PLAN.md` §4.
  ⛔ **This step is a placeholder with its inputs named, not a specification. Re-audit at lap 8's open** and take
  the spec from that plan; where the two disagree, **that plan wins** and this step is stale.
- **inputs, by file** — `BACKLOG.md`'s committed rows' **`ask`** field (the four-field contract,
  `[paul-ruled 2026-09-07]`) · `questions.json` (the card queue, incl. `_ordering` and `_kind`) · the card-intro
  asks · `.private/feedback-log.json` (where each note went — ⛔ never her words; this repo is public) · **the
  feedback and onboarding stores per env** (`GET /api/feedback`, `GET /api/onboarding-metrics` — ⚠️ **the GET is
  R1**, so **R1 is a precondition of R0's onboarding half**).
- **why it is a rider and not a feature** — it is the reader half of a rule already in force: *an event with no
  reader is not instrumentation*, applied to **asks** rather than events. `measured` context: the product has asked
  a great deal and **no single surface says what it asked, what came back, and where the answer went** — which is
  why TIER 1 · 36's wording stamp and TIER 1 · 37's missing GET both read as isolated gaps rather than as two rows
  of one ledger.
- **boundaries on its own face** (CLAUDE.md's rule that a control states what it does not cover): ⛔ **COUNTS, never
  people** — a `deviceId` is a browser bucket and an answer carries no personId by construction · it reports **where
  an answer was folded**, which for a reflective card is *unprobeable by design* and must print as such, never as
  *unanswered* (`momlib.question_state()` is the one definition of settled — ⛔ **import it, do not re-derive it**;
  three tools disagreeing about "pending" already produced a real wrong claim on 2026-07-26) · **exit 3 =
  UNREADABLE, never green by absence.**
- **check** — `python3 tools/ask-ledger.py --env qa` prints every ask a lap-8 seat walk was served, with its answer
  count and its fold target; a `--selftest` proves each clause can fail (an ask with no row · a row with no ask ·
  an answer whose fold target cannot be probed).
- **falsifier for the tool itself** — if every ask it lists already had a reader, it measured nothing; delete it.
- **MOVES CANDIDATE:** no (a reader, no app surface). **serves:** the four-field contract · R1 · TIER 1 · 36/37.

### R2 · TIER 1 · 36 — stamp every ranking with its wording
- **file:symbol** — `onboarding/index.html` s5 · the feedback record's `context` **[not verified]**.
- **why** — *"rewording s5 changes what a ranking means; hers becomes incomparable to every later one unless the
  wording rides with the record."* Lap 7 ships without it, so every lap-7 ranking is under today's labels **by
  omission** — a fact that should be written down, not inferred later.
- **check** — a walk's ranking record carries the label set it was shown.
- **MOVES CANDIDATE:** yes (R1 Worker, R2 page). **serves:** the four-field contract.

## ROW **H** — the harness (3 steps). ⛔ Without H1 the lap's own done-means cannot be read.

### H1 · **Two browser contexts in one run** — the capability s1/s2/s4 need (§2 A6)
- **file:symbol** — `tools/journey-walk.py`, the single-context runner and `refresh(role, env)` (`:67`) **[read]**.
- **change** — a second context for the **same account**: sign in on context 2, act on context 1, read on context 2.
- ⚠️ **It also gives B2 its only honest assertion**: after context 2 signs in, context 1's token must 404 at
  `/api/grant/whoami`.
- **check** — `journey-walk.py --selftest`; the new clauses fail when mutated.

### H2 · **`J9 · cross-device`** declared and written
- **file:symbol** — `JOURNEY_IDS` (`:308`) and `JOURNEYS` (`:781`) **[read]**. ⚠️ The selftest clause binds:
  `set(JOURNEY_IDS) == set(JOURNEYS) | set(NAMED_UNBUILT)` — adding to one dict only fails, **which is the design
  working**. ⛔ Confirm no id collision: J7 is spoken for in prose as *second-member* (`journey-walk.py:869`), J8 is
  lap 7's lifecycle.
- **stops** — `X01` sign in (context 1) · `X02` write a journal entry / field note · `X03` sign in on context 2,
  same account · `X04` **the entry is there** (s1) · `X05` it is scoped to the household and the account, not the
  browser — clear context 1's storage and re-read on context 2 (s2) · `X06` context 1's original token 404s (B2) ·
  `X07` the administrator reads it from a third context (s4) · ⛔ **`X08` *(declared out)* — the owner sees a
  member's contribution (s3): there is no second person in any household; see §2 A5.**
- **check** — `journey-walk.py --journey J9 --role owner --env qa` → zero failed actions; `walk-integrity.py` counts
  it; **`walk-fixtures.py` shows J9 with a fixture per env.**

### H3 · Extend `falsifier-tenancy.py` C2 to probe `X-Estate`
- **why** — A7 adds a surface a caller controls. **A clause whose surface list does not grow with the attack surface
  silently shrinks its own denominator** — the classifier's sibling failure.
- **check** — `--selftest`; a mutation that lets `X-Estate` name a foreign estate turns C2 red.
- **MOVES CANDIDATE:** no (all three). **serves:** A's done-means.

## ROW **B** — the migration. ⛔ **ITS OWN GATE, on Paul's word at the act** (7 steps)

> *"Step 5 is the only irreversible step and it is Paul's call, not a consequence of 1–4."* — the multi-tenancy plan.
> **RULED 8·2:** after A15 passes at lab. **RULED 8·4:** the product name is ruled first.
> **RULED 8·1:** nobody real walks the door while A's steps land; **Mom founds once, at the production origin.**

### B1 · Write `tools/household-import.py` (§2 A11)
- **new file** — the inverse of `tools/household-export.py` **[exists; its code not read]**.
- **shape** — reads an export, writes every key under the target namespace **without transforming ids**, and
  **verifies key-by-key after writing**. ⛔ Refuses a target key that already exists (never silently overwrites).
- **check** — a round trip at lab: export a founded estate, import it into a second namespace, diff key-for-key.

### B2 · Export `fernwood-home`'s account row **and everything under `est-e6696a:`**
- ⚠️ **Not just the account.** `marguerite`'s row is one key; her 17 feedback records, her grant, her place row and
  her metrics are others. **An export that moves identity and leaves her words is a migration that loses data while
  reporting success.**
- **check** — the export's key count matches a `list` of the namespace; both recorded in the report.

### B3 · **Verify the copy before the source is touched**
- **check** — a byte-for-byte comparison, written to `.private/`, **read by a human**. ⛔ *"A `du`/UI read is
  inference, not verification"* (CLAUDE.md).

### B4 · Import into the production origin's namespace
- ⚠️ **Under the sentinel (A1), her records keep `est-e6696a:` as their prefix** — that is her estate id and it does
  not change. **Only the namespace changes.** ⛔ If A1 lands option (b) instead, her prefix collides with nothing but
  the deployment's own binding — re-read this step before running it.
- **check** — `watch-accounts.py` reads `marguerite` **at the production origin and nowhere else**.

### B5 · **Prove it** — she can sign in and her record is hers
- **check** — one sign-in at the production origin reaches every house `whoami` lists; the J9 walk (H2) passes for
  her account shape; `falsifier-tenancy.py` still green with a real row present.
- ⛔ **The falsifier is not "can sign in."** It is *"what I wrote is here when I come back on another device"*
  (Paul's words, the lap's done-means).

### B6a · ⭐ **Bind the production origin to the apex `myhome.place`** `[paul-ruled 2026-09-11]`
- **change** — a custom domain on the production Pages project. `measured` **[relayed, not verified by me]**: the
  zone is active at Cloudflare Registrar with **0 DNS records**, so this is the first record in it.
- ⚠️ **Registrar ≠ DNS ≠ Pages binding — three acts, and only the first is done.** A zone with no records resolves
  nowhere; a bound Pages project with no DNS record serves nothing.
- **check** — `curl -sI https://myhome.place/` returns the app's headers **and** `/qa-build.json` reports the
  candidate sha (`pages-deploy.py`'s own post-deploy read, `:390`) **[read]**.

### B6b · `tools/pages-deploy.py`'s `ORIGIN` map gains the apex
- **file:symbol** — `ORIGIN` (`:32`) **[read]** · `post-deploy.py`'s host map **[not verified]**.
- ⛔ **`post-deploy.py` verifies the ORIGIN it is given** — *"an origin serving what the export never contained… a
  Worker on a different host serving another estate"* (CLAUDE.md). If the map still names `myhome-paul.pages.dev`
  while people load the apex, **the post-deploy check certifies a host nobody visits.**
- **check** — `python3 tools/post-deploy.py --env <production>` runs against the apex and passes.

### B6c · **The link Mom receives is the apex** — and nothing else
- ⛔ **This is the step 8·4 exists for.** *"A link she receives is the one thing that should not be renamed under
  her."* A `*.pages.dev` link handed out now is a link that must be re-handed later.
- **check** — a grep of whatever carries the link to her (the invite/recovery text, the handover note) finds **no
  `pages.dev` host**. ⚠️ `*.pages.dev` must keep working — it is how a deploy is verified — but it is **not what a
  person is given**.

### B6d · ⚠️ The NAME is still unruled, and it is not this step's to invent
- The apex is the **address**; the **product apex name** and the **family door** are open
  (`.plans/2026-09-03-product-name-PLAN.md`, `stage: ready`, AWAITING PAUL). ⛔ **A build window must not fill a
  name slot because a domain now resolves.** §9 Q0.

### B6 · Tombstone `fernwood-home`
- **file:symbol** — `worker/wrangler.toml` `[env.home]` (`:155`) **[read]** · `tools/pages-deploy.py`
  `PROJECT`/`BRANCH`/`ORIGIN`/`HOUSEHOLD` (`:29–32`, `:87`) **[read]** · `tools/deploy-worker.sh` ·
  `tools/post-deploy.py` maps **[not verified]** — the same four-file shape the teardown lane used for `bob`.
- ⛔ **`est-e6696a` is KEPT** — it is her estate id, not a fixture's (the commitment says so).
- ⛔ **The release note promises nothing about `home`** (Q7).
- **check** — `python3 tools/check-domains.py`, `check-engine-manifest.py`, and a `--env home` deploy attempt
  **refuses by name**.

### B7 · What Paul's word at the act looks like
- **the ask, in one screen:** the lab falsifier's output at the candidate sha · `check-scope-sites.py` 0 unclassified
  · the export's key count and the verified-copy diff · the exact commands B4/B6 will run · **and the one thing that
  is irreversible** (the tombstone, after which `home` answers nothing).
- ⛔ **A one-word go is enough only if the screen above is on the screen.** Gate only where the ACT is the decision
  (CLAUDE.md) — this is one of the few places where it is.
- **MOVES CANDIDATE:** B1 no; B2–B6 do not move the *app* candidate at all — **row B is a migration, not a build**,
  and its evidence is a report, not a battery.

---

**Step count: P 4 · A 16 · C 5 · E 3 · F 4 · G 4 · riders 3 · H 3 = 42 in the candidate · B 11 as its own gate
(7 + the four apex steps B6a–B6d) = 53.**

⚠️ **Two of the 42 are placeholders whose specification lives elsewhere and is still being written** — R0 (the ask
ledger, `.plans/2026-09-11-ask-design-PLAN.md` §4) and G2 (the empty-ribbon content question). **Both are marked
re-audit-at-open.** A build window must not treat a placeholder's prose here as a spec.

---

# 4 · SEAMS

**SEAM-1 · The Worker and the pages must land together, and they deploy through different tools.** A11/A12 (pages)
read the array A9 (Worker) returns. `pages-deploy.py` and `deploy-worker.sh` are separate acts — **Worker first at
every env**, the lap-7 rule, unchanged.

**SEAM-2 · Every household's record moves house at the same moment the code stops separating them.** Today
`myhome-paul` physically cannot read `est-e6696a`. After row B it can, and the only thing stopping it is A2–A4. ⛔
**This is why A15 gates B and why `check-scope-sites.py` is a precondition of A15's meaningfulness, not a nicety.**

**SEAM-3 · A5 and A6 are one commit** (§3). Splitting them kills every live credential.

**SEAM-4 · What a real user could hit, named.** After the door: **Paul is the only account at the production
origin**, and **Mom's row moves into it**. So the only two people who can hit a defect in lap 8 are the two people
whose trust the project runs on. ⚠️ And `legacy` — Mom's live Fernwood at `palekxk.github.io` — **is untouched by
every step above** and must stay untouched; it is her app today.

**SEAM-4a · The apex makes the link PERMANENT, which cuts both ways.** `myhome.place` is the right destination and
it removes the *"the updated link"* class of failure (TIER 1 · 41, where a person could not reach his own house from
the wrong origin). ⛔ **But a permanent link is one that cannot be quietly re-issued** — so B6c's grep is not
hygiene, and the unruled product NAME (§9 Q0) becomes more expensive the later it lands, not less.

**SEAM-5 · The 09-04 fail-closed rule survives the conversion, and here is the argument.** A label that cannot be
resolved produces a host that does not exist → the fetch throws → `res.ok` is false → **the outbox keeps the words**
(lap-7 plan §2 A7). A7's `X-Estate` must fail the same way: an unheld estate is a **404**, never a fallback to the
caller's only estate. ⛔ `grantFor`'s own comment names the forbidden answer — *"a router row with NO GRANT BEHIND IT
falling back to the deployment's estate… hands a stranger this household."*

**SEAM-6 · The existence oracle is larger after the door than before it** (§2 A8) — one namespace to enumerate
instead of five. The security seat rules **before** A13 is built.

**SEAM-7 · Row G and row A touch the same build path.** G1 edits `engine/viewer.template.html`; A11/A12 edit
`onboarding/` and `homes/`. Both rebuild `viewer.html`. ⛔ **`--extract` and `--fix` are traps on this path** (§2 A10)
and the diff check is per-run, not per-lap.

**SEAM-8 · `pages-deploy.py`'s `HOUSEHOLD` set is edited by row B and by nothing else.** If A-row work touches it,
two steps are editing one literal for different reasons.

**SEAM-9 · The lap-7 window may still be committing when lap 8 opens.** It was at `06c2a16`. **`git commit --only
<paths>`** — the rule adopted 09-10 after the `dcbc660` slip — binds every window in this lap.

---

# 5 · THE BATTERY — what proves the door, and what proves *"synced"*

**One candidate sha. One full battery at that sha. Then Paul.**

| | |
|---|---|
| **Where** | **`qa`** — `release-gate`'s `walked-in-qa` clause is mandatory; a walk at `lab` does not count |
| **Journeys** | **J0** (founding-owner, bare door) · **J2** (returning-unfinished, fixture per run) · **J3** (returning-finished) · **J8** (lifecycle, incl. C5's editor stop) · ⭐ **J9 cross-device, new (H2)** |
| **Seats** | **five** — `mom` · `owner` · `strict` · `wide-eyed` · `handover`, each read **unprimed** |
| **Conditions** | **414 × 848 × A+**, visible Chrome (`--watch`) |
| **Gate ①** | every clause true for every seat: `at-sha` · `watched` · `countable` · `no-failed-actions` · `not-rate-limited` · `walked-in-qa` · the content clause (lap 7 H4) |
| **The door's own falsifier** | `falsifier-tenancy.py` C1 · C2 (**with `X-Estate`**, H3) · C3 · C5 green at **lab**, at the candidate — ⛔ **BEFORE row B**, ruled 8·2 |
| **The conversion's falsifier** | `check-scope-sites.py` — **0 unclassified**. ⛔ Not covered by the clause above (§1) |
| **"synced" s1 · s2 · s4** | **journey J9**, stops **X04** (s1) · **X05** (s2) · **X07** (s4) — named here so a reader can find the stop that proves each clause |
| **"synced" s3** | ⛔ **DECLARED OUT OF LAP 8** (§2 A5) — no household has two people; stop **X08** prints as out-of-scope, **never as passed** |
| **Explicitly not covered, declared** | one viewport (414×848) · **L13** the administrator's reset (human, out of harness) · **X08** s3 · a deployed Worker older than the tree (nobody has ever compared them — SECURITY's own denominator) |

**Order:** deploy `qa` → J0 × 5 → J2 × 5 → J3 × 5 → J8 × 5 → **J9 × 5** → each seat reads its own walk →
content-steward reads all → `release-gate.py --sha <candidate>` → Paul. **Then, separately: A15 at lab → Paul's word
→ row B.**

---

# 6 · OUT OF LAP 8 — each with its ruling

| out | the ruling |
|---|---|
| **The weather card from an address** | **RULED lap 9, first row** (8·3 / 9·2) |
| **§ INVITE & JOIN — the build** | **RULED** *"not this round… just owners setting up houses"*; its **five-seat scoping runs IN lap 8** (9·4) — a scoping is not a build and does not touch the candidate |
| **Bob's second house / the *add another place* surface** | **RULED lap 9 · C** (9·1, J0 × 2). Lap 8 builds the mechanism (A7/A9) and **leaves the 409 standing** (§2 A7) |
| **Zones preload (Z-13)** | **RULED** gated on Mom founding her own Fernwood — *a person's act, not a lap's* (9·3) |
| **The capture write path** (TIER 2 · 8) | stamped `concept`; a design pass is owed first — lap-9 candidate |
| **D9 · the glance consolidation (the design pass)** | **CONDITIONAL, ruled**: `read-glance-order.py` must read **≥ 10 real sessions** across the real households at lap 8's beat 6, **else it moves to lap 9 by rule.** ⚠️ `measured` at `06c2a16`: **the tool does not exist yet** — it is lap 7 · C7. A reading window cannot open before it ships and G6 deploys |
| **The glance BUILD** | lap 9 · E at the earliest, after the design pass |
| **§ ADDRESS VALIDATION** | **RULED** *not this lap*; security-steward roster mode rules first whether an address may leave the estate at all |
| **The reset act itself (V8)** | lap 8 · C ships the **editor**, not the delivery. ✅ The *rule* for the delivery is ruled (`VOCABULARY.md` §3e·R) and cited at C3; the **act** is not built. **Named on the release note** rather than left unsaid |
| **Email verification** | not ruled in; the address stays a courtesy channel and C4 says so honestly (§9 Q4) |
| **Houseplants** | **RULED a research item, not a build** |
| **`Almanac → Journal`** | unruled as copy; content-steward's and Paul's (TIER 2 · 20) |

---

# 7 · RISKS, ranked and calibrated

**The stakes, stated once.** After row B there are **two real accounts on one origin** — Paul's and Mom's — and one
real user on `legacy` whose app nothing in this lap touches. Everything else is ours.

### 🔴 1 · An unconverted call site writes one household's record into another's prefix
The lap's defining risk, and **it is silent**: no error, no log, a key under the wrong estate. It is the class this
repo has measured twice, and after row B the two households are Paul's and Mom's. **Mitigations, both required:**
`check-scope-sites.py` (A0) refuses an unclassified site, and `falsifier-tenancy.py` (A15) refuses a leak at lab.
⛔ **Neither covers the other**, and a green on one has already been mistaken for coverage of the other three times
this month (CLAUDE.md's control-scope table).

### 🔴 2 · A real credential row moves, and a migration that half-succeeds reports success
Row B moves `marguerite` — a real person's account — between namespaces. **Two failure shapes:** an export that
carries identity but not her 17 feedback records (B2's warning), and an import verified by inference rather than by
a key-for-key diff (B3). **Mitigation:** verify before the source is touched; the tombstone is the **last** act and
is Paul's word at the act, not a consequence of B1–B5.

### 🔴 3 · A door that publishes which house a username lives at
Ruled out in words (FINDINGS §5) and easy to reintroduce **by accident** — a redirect, a differing error, a
different response time. And the disclosure grows under one origin (§2 A8). **Checks:** the byte-identical refusal
string; `grep -rn "username"` over every door write path; ⚠️ **timing is unmeasured by anyone, for the third
consecutive artifact that asserts it** (SECURITY CHANGE-7) — **mark it UNCHECKED rather than asserting it.**

### 🟠 4 · Lap 7 slips, and lap 8 inherits the gap
The slip table's rows, **re-priced against what is actually landed** (§2 A1): **B1 → absorbed by A9, no slip.**
**B2/B3 → build them in lap 8 as A0a/A0b, small.** **B10 → row C has nothing to put an editor behind; C slips.**
**C (G6 + the reader) → row D cannot design from evidence; it moves to lap 9 by the ruled slip rule, which is a
rule and not a failure.** **D (the Worker map) → row B would migrate a person into a house with no Worker; ⛔ MUST
NOT HAPPEN.** **H3 (`journey_lifecycle`) → row C has no falsifier and C5 has nothing to extend.**

### 🟠 5 · The email editor becomes the takeover vector it exists beside
`email` is unverified, non-unique and freely settable; the reset path delivers **to the account row's value**
(§3e·R). So the *delivery* is now ruled safe and **the editor is the remaining attack surface**: whoever holds a
session can change where a recovered credential goes. **Mitigation:** C2 (re-auth with the password), and C3's
citation + falsifier in code. ⛔ **Second failure shape, easy to ship by accident:** an availability/"already in
use" affordance on the editor re-mints the **email** oracle that the re-ruled B6 just removed — C4's grep is the
check. **Falsifiers:** change the address without the password → refused; a credential delivered to an address that
appeared only in a request → the §3e·R violation.

### 🟠 6 · `ESTATE_ID` at the production origin is decided by default rather than by ruling
If nobody rules A4, the binding stays `est-d93508` and every deployment-scoped key — and every missed conversion —
lands inside **Paul's** estate. That is not a bug that announces itself; it is a namespace that looks tidy.

### 🟡 7 · Row G's rebuild burns instance content into the engine
The `--fix` / `--extract` trap, measured twice in four days (§2 A10). **Mitigation:** the per-run diff check, in the
step. **Recovery:** `git checkout -- engine/viewer.template.html`.

### 🟡 8 · The candidate is large and the battery certifies a bundle
41 steps in the candidate across a Worker, five pages, the harness and two new tools. **Freeze the candidate before
the battery; any fix after it starts is a new sha and a new battery** — `release-gate` is per-sha because evidence
expires when the build moves. Say it in the brief.

---

# 8 · WHAT THE BUILD WINDOW'S BRIEF MUST SAY

1. **Its pull — the rows it freezes.** TIER 1 · **41 · 46** (row A) · TIER 2 · **18** (row C) · TIER 1 · **49**
   (row E) · TIER 1 · **48** (row F) · TIER 1 · **50** (row G) · TIER 1 · **36 · 37** (riders) · **the ask ledger's
   row when the ask-design plan mints one** (R0). ⛔ **Row B is NOT this window's** — it runs on Paul's word at the
   act, after A15.
2. **Its authorities, in precedence order.** The **beat-6 table at lap 8's open** → **the twelve rulings**
   (`CYCLE-LOG:2698–2736`) → **the multi-tenancy plan as amended by P2** → this plan → the seat reviews. ⛔ Where a
   review conflicts with a ruling, **the ruling wins.**
3. **What it may not decide.** All **copy** — every sentence here is a slot, content-steward's, DRAFT, human-confirmed
   before it reaches a person. The **AI boundary** binds. ⛔ **And it may not decide A1 (the sentinel), A7's header
   collision, A13's disclosure, or C4's honesty line** — those are §9.
4. **The freeze.** One sha, frozen **before** the battery. Any fix after it is a new sha and a new battery.
5. **The order it may not reorder.** **A0 before A2** · **A5 and A6 in one commit** · **B3 before A6** ·
   **A2–A4 before A15** · **A15 before B** · **E1/E2 before E3** · **R1 before R0's onboarding half** ·
   **Worker before pages at every env** · **P2 before the window reads the multi-tenancy plan.**
6. **The checks before declaring a candidate** — `build-viewer.py --check` **and** `git diff --stat
   engine/viewer.template.html` empty **and** a `lab` deploy that passed the headless load **and**
   `journey-walk.py --selftest` · `release-gate.py --selftest` · `falsifier-tenancy.py --selftest` ·
   `check-scope-sites.py --selftest` · `check-storage-keys.py` · `check-telemetry.py`.
   ⛔ **A green `--check` is not a working page.**
7. **What it hands back.** The candidate **sha** and the deploy that proved it loads · `RELEASE_NOTES.md` +
   re-inline, **naming what is NOT in this build** (s3 · the reset act · the second house · the glance) · **the ask,
   the telemetry event AND its reader, the ribbon line where it traces to feedback** (the four-field contract) · the
   battery's evidence, five seats × five journeys · `check-scope-sites.py`'s final output · **a short note on every
   place this plan said "not verified" and what the window found there** · ⛔ **it does NOT run row B.**

---

# 9 · WHAT PAUL MUST RULE BEFORE LAP 8 OPENS

| # | question | recommendation |
|---|---|---|
| **Q0** | **The product NAME** — ruled a lap-8 prerequisite (8·4) and **still open**. ✅ The **address** is now ruled: the production origin is the apex **`myhome.place`** `[paul-ruled 2026-09-11]`, so B6a–B6d exist. ⛔ **That settles where, not what it is called.** Two slots stay empty: the **product apex name** and the **family door** (`<family>.myhome.place` — `<family>` is a placeholder in every tracked file) | Rule both before **B6c**, not before **A** — A ships nothing Mom receives. ⛔ A link she receives is not renamed under her, and the apex ruling makes the link *permanent*, which raises the cost of a late name rather than lowering it |
| **Q1** | **What is `ESTATE_ID` at the single production origin?** (§2 A4) A sentinel owned by nobody, or the condo's `est-d93508`? | **The sentinel.** A missed conversion should land somewhere findable, not inside a real person's namespace |
| **Q2** | **`X-Estate` — build it in lap 8?** OPEN-ITEMS ①·2 says it *"must now be built"* and that the refuse-a-second-estate workaround is dead; the ruling for lap 8 is one door, not a second house | **Build the header, keep the 409** (§2 A7). The mechanism is lap 8; the surface is lap 9 · C |
| **Q3** | **What may the door SAY about what it reveals?** (§2 A8) Username existence **is** published — by `/api/account/available` and by signup's 409 — and email existence is not. Under one origin the enumerable space grows from one deployment's accounts to all of them | **Ship the true sentence, not the reassuring one:** *"we do not confirm whether an email address is on file"* ✅ · *"we never reveal whether an account exists"* ⛔ **false today and falsifiable in one curl.** security-steward rules the posture before A13 is built. ✅ The rate-bucket split is already lap 7 · B0 |
| **Q4** | **Does the email editor need anything beyond re-auth?** ✅ **§3e·R now rules where a recovered credential goes**; B6 is re-ruled to **no email lookup this lap**. What is still open is (i) whether the editor re-authenticates with the password or a fresh session, and (ii) whether the address is ever verified | **(i) the password** — a fresh session is what an attacker already has. **(ii) not this lap; state it honestly** (C4). ⛔ Do not add an availability check to the editor — it re-mints the oracle §3e·R's re-ruling just removed |
| **Q5** | **s3 — declare it out of lap 8?** (§2 A5) The owner-sees-a-member clause has no second person to see | **Yes, declare it out by name**, as L13 is declared out. ⛔ Not a hand-minted grant |
| **Q6** | **If lap 7's row B slips, do B2/B3 move into lap 8?** | **Yes, as A0a/A0b — two lines.** B1 is absorbed by A9 either way |
| **Q7** | **Row D's threshold is ruled at 10 sessions — but `read-glance-order.py` does not exist yet** (`measured`, `06c2a16`; it is lap 7 · C7). If lap 7 ships the tool and G6 deploys late, the reading window may be hours old at beat 6 | **State the window's start, not just the count** — 10 sessions *since G6 deployed*. A count with no window is the reading this loop has been burned by twice |
| **Q8** | **Row B's export scope** — her account row only, or everything under `est-e6696a:`? | **Everything.** A migration that moves identity and leaves her words is a data loss that reports success |

---

# 10 · WHERE DESIGN CLOSURE IS OWED — commission ux-expert at lap 8's open

The commit-phase rule runs **ux-expert closure → engineering-partner plan → build window**. This plan is written
*before* that closure, so the surfaces below are named with **their open questions, not their answers**. ⛔ **I have
not designed any of them and must not.**

| surface | what is not closed | why it cannot wait for the build window |
|---|---|---|
| **The single sign-in page** (A11) | one form for every household: what it says it is · what it says when it refuses (the one constant string is ruled — its *placement and prominence* are not) · what the *"Can't get in?"* entry looks like when it now covers every house · ⛔ what it must **never** show: any hint of which house a username lives at · ⭐ **and the one sentence about what is and is not confidential** — *"we do not confirm whether an email address is on file"* is true and sayable; *"we never reveal whether an account exists"* is **false** while the 409 and `/api/account/available` publish username existence (§2 A8) | It is the one surface every person meets, and the refusal copy is where a security ruling becomes a sentence. A build window choosing this is a build window making a security decision in prose — **and the tempting sentence is the false one** |
| **The shelf after sign-in** (A12) | the **empty** shelf (0 houses — *"the empty shelf… ⛔ NORMAL, not an error state"*), the **one-house** case (does it render at all, or is it a redirect?), and the **2+** case that nobody has designed because nobody could have two. Row content is ruled at name + town only (lap 7 A22) | A12's branch is three screens and only one of them exists today. And TIER 1 · 30 is Paul's own live complaint about this surface's formatting — **an unclosed design here ships a known defect forward** |
| **The email editor** (C1–C4) | what an Edit looks like on a value that was display-only last lap (lap 7 closure row 19 designed the *display*, not the edit) · what re-authentication looks like mid-edit (C2) · what the honest line about verification says (C4) · ⛔ and whether the editor sits on `/settings/account/` or is reached from the receipt's `Edit` (lap 7 A14 routes *How to reach you* → `/settings/account/` — **so A14 already points at a page whose editor does not exist**) | The re-auth step is a screen nobody has drawn, and it interrupts an edit. Drawn badly it reads as a failure |
| **The ribbon's empty state** (G2) | whether a household with nothing acknowledged renders **no ribbon** or a quiet line — and the same question one card down for the empty *Your Perspective* card (TIER 1 · 43, Paul's own report) | ⛔ These are **one** question. Answered separately, the app grows two different empty states for two cards that sit inches apart — and the standing rule is *never a standing "add data" button* |

⭐ **Commission all four in one closure**, and give it TIER 1 · 30 and TIER 1 · 43 as inputs — they are Paul's own
words about two of the four surfaces. ⚠️ **content-steward owns every sentence** on all four; the ux-expert closure
decides shape, not copy.

---

# 11 · FALSIFIER FOR THIS PLAN

If lap 8's beat-6 table at its open contains an item that appears in neither §3 nor §6, this plan's derivation was
wrong — the fix is in the commitment's source, not in a wider table here. And **if any step above cites a symbol
that has moved by lap 8's open, the step is stale, not the code**: every line number here is stamped `06c2a16`,
written while the lap-7 build window was committing, and §2's measurements must be re-run before the window reads
this file.

# 12 · QA

```
git rev-parse --short HEAD                      # this plan's measurements are at 06c2a16
grep -c "scopeOf(env)" worker/worker.js         # 66 raw · 55 non-comment at 06c2a16
grep -n "estates: \[{ estateId: scope.id" worker/worker.js   # B1 · unlanded at 06c2a16
python3 tools/falsifier-tenancy.py --selftest
python3 tools/journey-walk.py --selftest
python3 tools/check-backlog-ready.py --ladder   # the multi-tenancy plan's header (P2)
```
