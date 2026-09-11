# Cross-device sign-in — the path from "my credentials don't work at Mom's house" to one door

- **mode:** path-evaluation (engineering-partner)
- **date:** 2026-09-10
- **sha measured:** `5ffe811` (the lane's ground facts) · **read at** `10a042c` (HEAD)
- ⭐ **the two shas are byte-identical on every file this note reads.** `git diff --stat 5ffe811..HEAD -- worker/worker.js estate/index.html onboarding/index.html homes/index.html worker/wrangler.toml` returns **empty**; the three commits since are register and plan prose. So every `worker.js:NNN` below is true at both.
- **files touched by this note:** this file only. No wrangler, no deploy, no KV write, no code edit.
- **deployment context:** production, two real households live (Mom @ `home`, Paul @ `paul`), two strangers (Nigel, Aida) invited but not yet arrived. Calibrated to that — not to enterprise.

---

## THE TEN LINES (liftable into a FINDINGS doc)

1. **Nothing is broken.** `pkirsch` failing at `fernwood-home` is the deployment-per-household model working exactly as designed — `handleSession` resolves `est-e6696a:account:pkirsch`, which does not exist, and 404s. The defect is that **no surface can say so.**
2. **The one true bug tonight is a SENTENCE, not a schema.** Two byte-identical 404s (sign-in, and the laptop's whoami) were rendered as *"that username and password don't go together"* and as a **cached masthead that looked signed-in**. Both were false, and both are cheap to fix without touching tenancy.
3. **M2 is already in the code and has never touched the data.** `accountFor()` reads `username:<u>` → `account:<personId>` index-first with a legacy fallback (`worker.js:608-621`); `putAccount()` dual-writes (`:628-641`). The handoff's *"M1+M2 parked, not started"* is **stale**. Zero `username:` rows at `home`/`paul` means the **backfill** has not run — code ahead of data.
4. 🔴 **And the backfill is armed with a trap.** `handleSession` is the **one** account writer that bypasses `putAccount` — `worker.js:979` writes `accountKey(scope, username)` alone. The moment an index exists, the authoritative `account:<personId>` row goes **stale on `tokenHash` at the first sign-in**. Fix `:979` **before** M2's backfill, not after.
5. 🔴 **Rotation revokes at the wrong scope.** `:972` writes the new grant at the **person's** estate; `:977` deletes the old one at the **deployment's** (`keyFor(scope, …)`). For any founder these disagree, so **signing in does not kill the previous credential** — the opposite of what `:895`'s own comment promises.
6. **A5 gates the DESTINATION, not the DOOR.** Sign-in, `whoami` and the shelf touch no digest. One landing page, one sign-in, and an honest list of a person's places can ship **ahead of** the long pole. What A5 does gate is the condo's **Guru** once the condo is a row in production — so **M5 before A5 would regress the exact capability Paul named** ("take pictures in my condo… share with the Guru").
7. **INTERIM: recommend (i) + honesty.** Keep the two origins, fix the two sentences, fix the refusal/outage split. Reject (ii) redirect-door — it publishes a household→origin map, which is finding #9's leak made enumerable. Reject (iii) account copy — it is legal under the invite ruling (identity ≠ relationship) and still buys a house he cannot enter. Defer (iv) the shelf until one namespace holds the accounts.
8. **The qa `pkirsch` duplicate is neither a defect nor mere hygiene** — it is what per-deployment uniqueness *means*. It becomes a **blocking M5 precondition**: a username live in both namespaces makes `username:<u>` last-writer-wins, which detaches sign-in from a still-valid `route:` row and surfaces **later**, as "my credentials stopped working."
9. **D, the honest rule: a refusal changes what the page CLAIMS; only the person changes what the device KEEPS.** `estate/index.html:511` throws the discriminator away (`r.ok ? r.json() : null`) — a 404 and a dropped Wi-Fi become one `reachUnknown`. Split them; never clear cache on silence (no cell signal, Wi-Fi falls off with distance).
10. **E, three emits and one reader.** Server `session_refused` (written on **both** deny branches, via `waitUntil`, or you re-open the timing oracle the dummy PBKDF2 closed) · client `door_opened` on whoami-200 · client `door_failed reason:"grant-not-known-here"` on whoami-**404**. Tonight would then read *2 refusals at a house that does not hold that name · 1 stale credential · 1 opening* — naming nobody.

---

# A · The smallest honest set, mapped to the ruled sequence

## A.0 · The decomposition that makes this tractable

"One person, one door, every estate they hold" is **two independent halves**, and this repo's plans treat them as one:

| half | what it needs | A5-gated? |
|---|---|---|
| **identity** — a person can authenticate at one origin | account rows + `username:` index + `route:` rows in **one** namespace | ❌ no |
| **reach** — that credential resolves data at each estate | `grant:<personId>:<estateId>` · enumeration · `X-Estate` · the 60 call sites · **A5** | ✅ yes |

⭐ **This is the most useful thing in this note.** Paul's direction — *"a landing page, just in the production environment, and everyone can access by logging in"* — is the **identity** half. Sign-in (`handleSession`), `whoami` and `/homes/` read no digest, so the door is not behind the long pole. What *is* behind it is Guru-at-the-condo-once-the-condo-is-a-row.

⛔ **And that produces the note's one counter-intuitive warning: doing M5 early makes Paul's stated problem WORSE.** Today the condo's Guru works at `myhome-paul` because that deployment's digest is its own. Copy the condo into production's namespace before A5 and `canonIsThisEstate()` answers **503 canon-not-this-estate** on all five model routes for whichever estate is not production's. He would gain one door and lose the Guru he named as the reason he cares.

## A.1 · The smallest honest set

Ordered by dependency, not by size. Each row says what it costs and what breaks if skipped.

| # | change | why it is in the *smallest* set | breaks if skipped |
|---|---|---|---|
| **S1** | `worker.js:979` → `putAccount(env, scope, username, acct.personId, …)` | the **only** account writer not converted; it is on the auth path | M2's backfill arms a stale-`tokenHash` authoritative row (#4) |
| **S2** | `worker.js:977` delete at `scopeOfRoute(grantRow.estateId \|\| priorEstate, env)` | rotation must revoke where it wrote | old credentials never die for founders (#5) |
| **S3** | run the M2 backfill (`username:` + `account:<personId>`) at every namespace | login's first hop stops being estate-keyed — this is what makes one door *possible* | one door stays impossible; every read stays on the legacy fallback |
| **S4** | M3 backfill: `route:<hash>` → `{personId, estateId}` over the ~230 rows | `personFor()` is blind to anyone who merely signed in again | `POST /api/estate` 404s for real people; the empty-shelf case is unreachable |
| **S5** | D's refusal/outage split (`estate/index.html:509-518`, `homes/`, `onboarding/`) | it is the reported bug | the next stale credential reads as an outage again |
| **S6** | E's three emits + `watch-door.py` teaching | *"an event with no reader is not instrumentation"* — CLAUDE.md's own rule | the next four attempts are unreadable too |

**S1 · S2 · S5 · S6 are independent of the destination and safe to land tonight-shaped.** S3 · S4 are the migration proper and carry the plan's own timing rule: **behind the two first-time users, not across them.**

⛔ **S1 before S3 is not a preference, it is an ordering constraint.** The backfill is what makes `accountFor()` prefer the new row; `:979` is what makes that row wrong. Running them in the other order produces a divergence on the single path where a mistake locks somebody out.

## A.2 · Mapped onto the two ruled sequences

`.plans/2026-09-10-multi-tenancy-PLAN.md` § Sequence (1–5) · `.plans/2026-09-10-account-estate-model-SCOPE.md` §6.1 (M1–M6) and § Sequence (1–8).

| step | this bug… | detail |
|---|---|---|
| PLAN 1 · router + backfill | **ADDS a precondition** | measured: the router shape shipped, the **backfill has not run** at `home`/`paul`. Add S1 · S2 as blockers *of* the backfill |
| PLAN 2 · the falsifier test | **REORDERS — pull it forward** | every change above touches the credential path while Nigel/Aida are about to arrive. The plan's own timing note argues this; the bug is the evidence |
| PLAN 3 · the 60 call sites (A4) | **untouched** | none of S1–S6 needs `scopeFor()` at a handler |
| PLAN 4 · `POST /api/estate` + `/homes/` picker | **partly done, and the register is stale about it** | `worker.js:4369` routes it **unconditionally** — no env gate. Whether `home`/`paul` *answer* it is a question about **which sha those deployments carry**, not about the code. One read-only probe settles it: `GET /health` at each origin and compare the sha. ⛔ Do not restate "qa/lab only" from the brief without that probe |
| PLAN 5 · migrate + retire envs | **REORDERS a precondition in** | the qa `pkirsch` duplicate (§C) becomes **blocking**, not hygiene |
| M1 (delete nigel/aida) | done | reversed then executed 2026-09-10 |
| **M2** | **ADDS S1, and corrects the record** | the code is **landed**; the data is not. `handoff/handoff-fernwood-credential-path.md` §2 says "not started" — measured false at `worker.js:608` |
| **M3** | **ADDS S4 as a re-run** | value shape already written (`:986-988`) |
| M4 (`grant:<personId>:<estateId>`) | **untouched — and bound** | ⛔ ships with `POST /api/estate` per the 09-10 bound ruling. Not needed for the door |
| **M5** (cross-namespace copy) | **ADDS a hard precondition + a hard warning** | precondition: no username live in two namespaces (§C). Warning: **A5 first, or the condo loses Guru** (§A.0) |
| M6 (delete old rows) | untouched | last, after verification by use |
| SCOPE 2 (§5.3 attribution) | untouched, still owed | independent live defect |
| SCOPE 6 · **A5** | **the long pole, and it is NOT on this bug's path** | gates `library:*`, `cache:today-line`, five model routes. Gates the destination; not the door |

## A.3 · What the set does *not* include, deliberately

- ⛔ **Removing the byte-identical 404.** Out of scope for me and named below (§B.3).
- ⛔ **Minting `p-paul @ est-e6696a`.** `[paul-ruled 2026-09-10]` — the **register row is what is wrong**, not the store. Paul holds administrator **capability**, no **relationship** at Mom's house until she invites him. Nothing in S1–S6 touches that.
- ⛔ **Any schema change to grant keys.** Bound to `POST /api/estate`; not needed for one door.

---

# B · The interim, while two origins exist

## B.1 · The options, read straight

| | option | complexity | what it actually buys | what it costs |
|---|---|---|---|---|
| **i** | **do nothing structural; fix the sentences** | lowest — copy + one `fetch` branch | Paul's condo already works at `myhome-paul`; the phone confirmed it | he must know which link is his — a **fact**, not a UI |
| ii | redirect-shaped door: known username → its origin | medium | one bookmark | ⛔ **publishes a household→origin map.** See B.2 |
| iii | cross-namespace copy of `account:pkirsch` into `home` | low mechanically | **nothing usable** | he could sign in at Mom's origin and hold **no grant** → the same 404 one screen later. Legal under the invite ruling (an account is identity; a relationship still needs Mom's invite) and therefore **pointless**, which is the sharper objection |
| iv | a `/homes/`-style shelf on one origin that asks each Worker | high | the ruled end state, early | a token minted at origin A **cannot resolve at origin B** — `route:` rows are per-namespace. Either the landing Worker binds N namespaces (deployment-per-household with extra steps) or it cannot sign anyone in. **This is M5 wearing a disguise** |

## B.2 · Is (ii) a username oracle? — the precise answer

**Existence is already disclosed, by design.** `/api/account/available` (`worker.js:4374-4385`) is **unauthenticated**, rate-limited, and answers `{available:false}` for a name that exists at that deployment. You cannot run a signup flow that refuses duplicates without it. So (ii) leaks **no new existence fact**.

⭐ **What (ii) leaks is ASSOCIATION** — *which house* a name lives at — and it leaks it **without a probe**, as a published table in a public page. That is `SCOPE §⑦ row 9`'s finding (`myhome-bob.pages.dev` tells a stranger a household exists for someone called Bob) turned from *inferable* into *enumerable*. ⛔ **That is the disqualifier, not the oracle question.** And it is exactly the leak the ruled destination *dissolves*: one origin for everyone names nobody, and a global `available` answers existence with no house attached.

## B.3 · The 404 trade — stated, not ruled

I am not proposing any change to the byte-identical 404, and I am naming its cost so the ruling is informed:

- **What it protects:** the pair *"no such account"* / *"wrong word"*, at the moment of authentication. Timing is equalised by the dummy PBKDF2 (`worker.js:882`).
- **What it costs:** the page cannot tell a person *"you're at the wrong house"* — which is **tonight's entire user-visible defect**. Mom's most likely failure mode and Paul's actual one are both mis-explained by one sentence.
- **The asymmetry worth putting in front of the security-steward:** existence is already public via `/api/account/available`, so the 404's marginal protection is over the *credential-validity* distinction, not over existence. Whether that marginal protection is worth the mis-explanation is **theirs to rule, not mine.**
- **What can be fixed without touching it:** the *client's* copy on a **whoami 404 with a stored grant** — that is a different act from sign-in, carries no password attempt, and can honestly say *"this credential isn't known at this place"* without disclosing anything about a username. See §D.

## B.4 · Recommendation — (i), plus honesty

**Keep two origins. Change three strings and one `fetch` branch.** Reasoning:

1. The condo **works today** at its own origin — measured tonight, twice (phone + laptop). The capability Paul says he needs (photos → Guru at the condo) is **available now** and would be *lost*, not gained, by an early M5 (§A.0).
2. Every structural interim is M5 in miniature, paid twice.
3. The defect that actually cost him an evening is **explanatory**, and that fix is free and is a strict subset of the destination's work.

> ### The falsifier for B.4
> **If Paul (or Mom, or Nigel) lands on an origin that is not theirs and the screen still cannot say so — or if anyone needs to be told by a human which URL is theirs more than once — (i) has failed and the shelf (iv) stops being premature.**

A second, harder falsifier for the *whole* interim: **if Mom ever needs to reach a second place** (the condo, or a place she founds), two origins stop being an inconvenience and become the product's shape. That is the day M5 ceases to be optional.

---

# C · Two personIds, one username — what it is and what M5 owes it

## C.1 · Classification

**Neither a defect nor merely fixture hygiene: it is the definition of per-deployment uniqueness, met.** `worker.js:4380`'s own comment says it — *"this route has enforced per-deployment uniqueness ALL ALONG."* Two namespaces are two uniqueness domains, so `pkirsch@qa` (`p-jhgwhxxz6zce`) and `pkirsch@paul` (`p-yjnw9lt41nww`) are two legitimate rows under one rule. The **person directory dissolves it** only in the sense that one namespace restores one domain; it does not merge two existing ids.

There *is* a hygiene component — `[paul-ruled 2026-09-10]` *"pkirsch should be production only"*, and the qa copy is already on the named teardown list (`a425a5c`). **The finding is that this hygiene item is load-bearing on a migration step**, which no artifact currently says.

## C.2 · What M2/M3 must do about it — nothing. What M5 must do — refuse.

M2 and M3 are **intra-namespace**; neither can see the collision, and neither should try. ⛔ **The whole obligation lands on M5**, and it is the sharpest hazard in the migration:

1. 🔴 **`username:<u>` is deployment-scoped with no estate prefix** (`worker.js:600-602`). A cross-namespace copy that writes it is **last-writer-wins, silently.**
2. 🔴 **The loser is not locked out immediately — which is why this is dangerous.** `grantFor()` and `personFor()` read **`route:` only** (`:1519`, `:1544`). So a copy that orphans `account:<personId>` leaves the losing person's **existing token working** while their **password login is dead**. The failure surfaces days later, on a device that clears storage or a second device — and it presents as ***"my credentials stopped working,"* which is tonight's symptom, arriving with no cause attached.**
3. **The rule M5 needs is one this repo has already written for deletion** (`household-fixtures.py --teardown`): **an unprovable row is a STOP, not a SKIP; one collision refuses the whole run.** Applied to copying: *a username present in both the source and the destination namespace refuses the migration by name, and is resolved by a human **before** the copy — by teardown, or by `handleUsernameChange` at the source — never during it.*
4. **Cheap enforcement, and it does not exist yet:** a read-only `check-username-collisions` that enumerates `username:` + `<estate>:account:` across every bound namespace and prints the intersection. Exit 3 = UNCHECKABLE (a namespace that could not be listed), never green by absence. ⛔ It must **flag, never resolve** — which of two rows is entitled to a name is an identity judgement.

⭐ **And the promotion this argues for:** move *"delete `pkirsch@qa`"* off the hygiene list and onto **M5's precondition list**, in the plan, by name. A hygiene item nobody is blocked by is a hygiene item that does not get done — this repo's most-repeated failure shape.

---

# D · The stale-credential shell — the honest rule

## D.1 · What the code does now

```js
// estate/index.html:509-511
fetch(WORKER + "/api/grant/whoami", { headers: { "X-Grant": grant } })
  .then(function (r) { return r.ok ? r.json() : null; })        // ⛔ the discriminator dies here
  .then(function (d) { if (!d) { fetching = false; reachUnknown = true; render(); return; } … })
  ["catch"](function () { fetching = false; reachUnknown = true; render(); });   // :565
```

**The information is on the wire and is discarded one line before it is needed.** A server-issued **404** ("I answered; this credential is not known here") and a rejected promise ("nobody answered") collapse into the same `reachUnknown`, whose copy is *"We couldn't reach your place just now — nothing is lost."* Tonight that sentence was **false in the first half and true in the second**, and it is what Paul read as *auto-logged in* — because `:331` had already painted the masthead from `localStorage` under the `mine` guard, synchronously, before the fetch.

## D.2 · The proposed rule

> ## A refusal changes what the page CLAIMS. Only the person changes what the device KEEPS.

Three states, not two, and the split is on **whether a server answered**:

| the wire | meaning | what the page does | what it stores |
|---|---|---|---|
| **2xx** | the record answered | reconcile as today | write through (`put`), stamp `K_OWNER` |
| **404 / 401 / 403** on a **stored** grant | ⭐ **an answer**: this credential is not known at this origin | **stop claiming.** Suppress the place identity (name, address, ranking, accent) and say so: *"You're signed in, but not at this place"* + a route to sign in | ⛔ **quarantine, never delete** — set a `fw-grant-refused-at:<origin>` flag; leave every `K_*` value intact |
| **network throw · 5xx · 429 · timeout** | ⭐ **not an answer** | keep the cached view exactly as today; say *"couldn't reach"* | touch nothing |

⭐ **Why quarantine rather than clear, and it is the site's physical premise doing the work.** CLAUDE.md § *THE SITE'S PHYSICAL PREMISE*: no cell reception, Wi-Fi falls off with distance, permanently. A clear-on-failure rule destroys the only local copy of a household's state at exactly the moment the person walks toward the pond. But even on a **404** clearing is wrong: a 404 also means *"your token rotated on another device"* (which `handleSession` does deliberately, `:876`) — recoverable by signing in, and the local record may hold the only copy for that origin. **Clearing is a destructive act with a non-destructive alternative that reads identically to the user.**

⚠️ **And one thing `reachUnknown` gets right that the fix must keep:** *"a rejection and a refusal are the same claim: we did not learn anything"* is correct **about the record's contents** and wrong **about the credential**. The split is on the credential, not on the place. Don't let the new branch start asserting things about a household it never heard from.

⭐ **The deeper fix the comment at `:296` already names and this note endorses:** render this card **from** the reconcile rather than **before** it — the sync paint is what let a cached shell read as a session. That is bigger than tonight and should be scheduled, not smuggled.

⛔ **One thing to verify before shipping the 404 branch:** whether `hostAgrees()` failure also produces a 404 (`worker.js:4463`, `reason: "host-mismatch"`). It does. So *"not known at this place"* must be worded to cover **both** *unknown credential* and *right credential, wrong origin* — it already does, which is a small argument for that exact phrasing.

---

# E · The minimal instrumentation

## E.1 · Why tonight was unreadable

| attempt | what the record holds | why |
|---|---|---|
| phone sign-in @ home | **nothing** | `deny()` (`worker.js:875`) writes no door record |
| laptop sign-in @ home | **nothing** | same |
| laptop whoami @ home | 14 `door_failed reason=unknown-or-other-estate` — **the only server-side trace** | the gate at `:4461-4470` writes only when `X-Grant` is presented |
| sign-in success @ paul | 3 `door_reached`, **0 `door_opened`** | `onboarding/index.html:2215` is the **only** emitter in the repo; no page ever emits `door_opened` |

⭐ **`door_opened` has existed in `DOOR_EVENTS` (`:1136`) since the channel was built and nothing has ever written one.** `reached > opened` is the reading `watch-door.py` exists for, and one side of it has never been instrumented — the same shape as the `/api/door` GET that no tool called.

## E.2 · The three emits

1. **Server · `session_refused`** — in `handleSession`'s `deny()`. `{event:"door_failed", door:"entry", reason:"session-refused", serverSide:true}`. **No username, ever.**
   - ⛔ **Write it on BOTH deny branches and via `waitUntil`.** The unknown-account branch already burns a dummy PBKDF2 (`:882`) precisely to equalise timing; a KV write on one branch only would **re-open the timing oracle that line exists to close**. The gate at `:4467` already models the correct shape.
2. **Client · `door_opened`** — `estate/index.html`, on a whoami **2xx**. It is the only page that can honestly say someone arrived (its own `complete` comment makes this argument already).
3. **Client · `door_failed reason:"grant-not-known-here"`** — same page, on the **404** branch from §D. Distinct from the network branch, which emits **nothing** (a request that never arrived is not an event about a door).

## E.3 · The reader, and the boundary

⛔ **`watch-door.py` must learn the two new reasons in the same change** — CLAUDE.md: *an event with no reader is not instrumentation.*

**Then tonight reads:** `home` — 2 × `session-refused`, 1 × `grant-not-known-here`; `paul` — 1 × `door_opened`. Four attempts, four rows, **no person named.**

⚠️ **The one judgement call, flagged not taken.** A `knownHere: true|false` discriminator on `session-refused` would answer *"did somebody try to sign in at a house that does not hold their name?"* — precisely tonight's question — but it is a fact **about whether a person exists in a store**, and an administrator who knows who was at the keyboard can combine it. `watch-door`'s rule is *reports what happened at a door, never who was standing at it.* **Two honest options:** omit it (the count alone still shows a spike of refusals at one origin), or record it **as a daily aggregate count** rather than per-row, which carries the reading without carrying an event about a person. ⛔ **Paul's or the security-steward's call; I am not taking it.**

📎 **And a scoping note for SCOPE §Q4 (*what scope do DOOR records take?*), measured rather than argued:** `storeDoorRecord` writes `dateKey(scopeOf(env), "door", …)` (`worker.js:1264`) — **deployment-scoped, today, in code.** Whatever Q4 rules, it is a change, not a confirmation.

---

# Findings, by severity

| id | intent | severity | where | finding |
|---|---|---|---|---|
| **E1** | issue | **critical (latent — arms on M2's backfill)** | `worker/worker.js:979` | the only account writer bypassing `putAccount`; makes the authoritative row stale on `tokenHash` at the first sign-in. **Fix before the backfill** |
| **E2** | issue | **critical (latent — arms at M5)** | `username:` key shape + M5 | a username live in two namespaces is last-writer-wins; the loser keeps a working token and loses password login. Must **refuse**, per the teardown doctrine |
| **E3** | issue | **important** | `worker/worker.js:972` vs `:977` | rotation writes the new grant at the person's estate, deletes the old at the deployment's — a founder's previous credential is never revoked |
| **E4** | issue | **important** | `estate/index.html:509-518, :565` | a server refusal and a network failure collapse into one state; the cached masthead then reads as a session |
| **E5** | issue | **important** | `handleSession` `deny()` (`:875`) | two real sign-in failures left **zero** trace; the loop cannot see its own front door |
| **E6** | issue | **important** | `DOOR_EVENTS:1136` + all pages | `door_opened` has never been emitted; `reached > opened` is half-instrumented |
| **E7** | question | **important** | `PLAN` step 5 / `SCOPE` M5 | **does M5 precede A5?** If yes, the condo loses Guru. Nothing in either plan says so |
| **E8** | issue | nice-to-have (doc) | `handoff/handoff-fernwood-credential-path.md` §2 | says M1+M2 "not started"; M2's code is landed at `worker.js:608-641`. Stale, and it is the kind of stale that suppresses work |
| **E9** | question | nice-to-have | `worker.js:4369` | `POST /api/estate` is routed **unconditionally**; "qa/lab only" is a claim about deployed shas. Settle with one `/health` read per origin |
| **E10** | praise | — | `worker.js:890-905`, `:960-975` | the founder-estate corrections on the sign-in path are exactly right and are commented with the measurement that produced them. The two remaining defects (E1, E3) are **residue of that same fix**, one scope argument short — which is why they are worth catching now rather than after a migration |
| **E11** | praise | — | `estate/index.html:284-300` | the owner-guard block is the honest version of this problem: seven person-scoped reads, a named predicate, and defect #3 **left open and labelled** rather than papered over. §D is the continuation of that block's own argument |

---

# Open questions for Paul

1. **E7 — M5 before or after A5?** My read: after, or the condo regresses. This is the one ordering question in the note with a user-visible consequence.
2. **E's `knownHere` discriminator** — omit, per-row, or daily aggregate? (§E.3)
3. **The 404 trade** (§B.3) — security-steward's, informed by the fact that existence is already public via `/api/account/available`.
4. **Does "one landing page" mean one ORIGIN or one PAGE?** Paul said *"a landing page, just in the production environment."* A page is cheap; an origin is M5. The direction is recorded as a direction, not a mechanism ruling — and §A.0 says the page can come first.
5. **`index.html` redirects to `viewer.html`** (the ux sweep's F1 blocker, *"`/` has no front door"*). Is the landing page **that** file, or a new surface? That answer decides whether F1 and this bug are one piece of work.

# Principles this session would propose (NOT written — proposal only)

### A control's scope is a claim about the CONTROL, not about the world
**Statement:** when a check passes, name the question it answered and the question you are relying on it for, and read them side by side — they diverge silently.
**Why:** already ruled in CLAUDE.md 2026-09-10; this session produced a **fourth** instance in a new shape — `reachUnknown` is a *client-side* control that is perfectly correct about *"we did not learn about her place"* and was trusted for *"we do not know if you are signed in."*
**When it applies:** any error branch that merges two upstream causes.
**Avoid:** collapsing an HTTP status into a boolean before the branch that needs it.

### Convert the last writer first
**Statement:** in an additive-then-cut-over migration, the **unconverted writer** is the defect, not the unconverted reader — a reader that misses the new shape falls back; a writer that misses it corrupts.
**Why:** `worker.js:979` — nine of ten account writes went through `putAccount`; the tenth is on the auth path and is the one that runs most often.
**When it applies:** every M2/M3/M4-shaped step in this repo's remaining migration.
**Avoid:** running a backfill before `grep`-ing for every writer of the key you are about to make authoritative.

---

# Principles applied (from `~/.claude/engineering-principles/`)

| principle | where it bit |
|---|---|
| **Loud failure beats silent fallback in personal-stakes pipelines** | E4 — a refusal rendered as an outage, and E2 — a username collision resolved by last-writer-wins instead of refusing |
| **Single source of truth per record, declared explicitly** | E1 — two account rows exist, one is authoritative, and the highest-frequency writer updates the other |
| **Three ways a gate stops being a gate: unwired, unconsumed, un-rederived** | E5 · E6 — `deny()` is unwired to the record; `door_opened` has never been emitted; §E.3 requires the reader in the same change |
| **Isolation is a guarantee; awareness is a heads-up — never let a safety claim rest on the second** | B.2 — the association leak in option (ii) is awareness-shaped; and §A.0's warning that M5 trades a *guarantee* (separate namespaces) for a *check* (`canonIsThisEstate`) |
| **Match failure posture to stakes, not to the artifact's name** | the severity column — "critical (latent)" for two defects that are harmless today and arm on a scheduled step |
| **Fernwood · A deploy-bundled context artifact needs a rebuild-and-diff drift alarm** | A5 is the same principle at request scope: the digest is deploy-bundled, and one deployment serving many estates is what breaks the binding |
