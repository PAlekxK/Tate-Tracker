# PATH-EVAL — the grant-scoped read for an estate's own facts, and the tenancy shape for durable households in production

- seat: engineering-partner
- date: 2026-09-06
- inputs: `.plans/2026-09-06-cascade-and-release-state-AUDIT.md` (practice-steward), `worker/worker.js` @ working tree,
  `estate/index.html`, `onboarding/index.html`, `worker/wrangler.toml`, `tools/{grant-mint,household-export,pages-deploy,check-storage-keys}.py`,
  `.plans/2026-09-04-roles-and-access-REQUIREMENT.md`
- user context: Fernwood is a family field-journal app. Mom is the make-or-break user (test subject, not the end user —
  `feedback_mom_is_a_test_subject_not_the_end_user`). Bob Rolader is the first real outside household, arriving this week,
  planning succession of two houses to two daughters. Stakes: a family tool with one real outside user, NOT enterprise.
  Severity calibrated to that.
- code_context_confidence: high (every claim below re-derived from source, not taken from the audit)
- user_context_confidence: medium (Bob's requirement is stated second-hand; no `.user-research/` artifact for him)

---

## 0 · CORRECTIONS TO THE BRIEF — three, and one of them changes decision 1b

**(1) `/api/feedback` GET is NOT admin-token-only.** `worker.js:3364–3376` — the dual-accept block. A read is
permitted by the master token **OR** by a resolved grant whose `capability === "administrator"` and whose host agrees.
A `member` capability gets a shaped 403.

**Consequence, and it is live today:** `handleAccountCreate` (`:487`) inherits capability from the invite —
`capability: invite.capability === "administrator" ? "administrator" : "member"`. So **a founding owner invited as
administrator can already `GET /api/feedback?start=&end=` and read every row in the estate, verbatim, including notes
authored by anyone else in that household.** That is probably what Paul intends for a household owner. It is currently
a *side effect of the invite's capability field*, not a decision anyone recorded — and CLAUDE.md's standing consent rule
covers only *"an administrator who is not a member of the household."* An owner-administrator inside the household is
uncovered. **Paul's call, but it should be a sentence somewhere before Bob's daughters write their first note.**

**(2) A person-scoped read is already mechanically possible and nobody has said so.** `attributeTo` (`:377`) stamps
`personId` + `estateId` on a feedback row **from the resolved grant and from nothing else**, and `declarePerson`
*throws* if anything tries to set them in a literal. So `r.personId === grant.personId` is a sound predicate for
"rows this credential wrote." Caveat that must ride with it: rows written without a grant carry `personId: null`, and
**`null` must never resolve to the caller's** — unattributed is not yours. (Same posture as `walk-integrity`: unmarked
is refused, never assumed.)

**(3) `check-storage-keys.py` is green over a surface it does not look at.** `tools/check-storage-keys.py:23` scans
**`viewer.html` only**. `onboarding/index.html` and `estate/index.html` hold at least eight localStorage keys —
`fw-grant`, `fw-onboard-addr`, `fw-onboard-parts`, `fw-onboard-name`, `fw-onboard-interests`, `fw-onboard-contact`,
`fw-onboard-owner`, `fw-accent`, `fw-username` — **none of them rostered, none of them scanned**, and the check prints
`✅ every browser-storage literal is rostered.` CLAUDE.md's own line on this check is *"a key the origin-move migration
does not know about is a key she loses"* — and these are precisely the keys that are about to move origins
(`fernwood-home.pages.dev`, `myhome-bob.pages.dev`). A one-line widening of the scan; a real hole until then.

---

# DECISION 1 · THE GRANT-SCOPED READ

## Recommendation

**Do (d) — promote the onboarding answers into the grant/account row at capture — and pair it with (a), widening
`/api/grant/whoami`. Do not build a new read endpoint and do not add a read verb to `/api/profile`.**

Paul's instinct that (d) is correct long-term is right. His premise that it is *the slowest now* is wrong, and that is
the finding worth having.

## Why (d) is not slow — measured, not asserted

The promote-at-capture path **already exists and is already proven in production shape**:

| piece | where | state |
|---|---|---|
| server-side write of a household fact to the grant row | `worker.js:3193–3202` — the `if (!uname)` branch of `POST /api/profile`, writing `placeName` and `accent` onto the grant row | ✅ built, live |
| client-side partial patch | `onboarding/index.html:934 saveProfile(patch)` | ✅ built, called at 2 sites |
| the field-by-field guard | `if (typeof b.name === "string") …` ×4 in the account branch — *"a caller sending one field never blanks the others"* | ✅ built |

So (d) is: **add four more field names to a block that already handles four**, and **add the same
`saveProfile({...})` line beside the `store(K_ADDR, …)` calls that already exist** at `onboarding/index.html:1663`,
`:1464`, and the contact-pref site. Roughly 30 lines across two files, reusing a path that has already been proven by
Mom's place name surviving a browser wipe.

The genuinely expensive option is **(b) / (c)** — a new read verb or a new endpoint. That costs a new auth decision, a
new privacy surface, new tests, and, worst of all, it **has to re-derive current-value-from-append-only-log at render
time**, which is exactly the unresolved problem §7.4 of the audit says supersede did *not* close. Measured cost of
that shape, from the audit's own reading of `est-qa0001`: 18 address rows, 8 distinct, across three states, with
`0 current`. **A read endpoint over the feedback log inherits all of that; a read of a state row inherits none of it.**

## Why `whoami` and not a new endpoint

1. **It is pre-authorised by the code's own text.** `worker.js:3339` — *"the one read a grant unlocks TODAY: what the
   credential itself is. 6a widens this."* It already returns `name` and `accent` from the grant row for exactly this
   reason: *"her place, so a return on a cleared browser is a RESUME and not a fresh start."* Address and ranking are
   the same class of fact and belong beside them.
2. **It reads exactly one row — the row the caller's own credential *is*.** No date range, no array, no other person's
   bytes anywhere in the code path. The privacy analysis is a sentence long.
3. **It sits ABOVE the dual-accept capability gate** (`:3339` vs `:3364`), so it never inherits the
   administrator/member question at all.
4. **It is already the first call the flow makes** (`onboarding/index.html:1715`). `estate/index.html` making the same
   call is one round trip and one new code path, not a new door.

## The principle this is really about

> **A receipt reads STATE; it never re-derives from a LOG.**

The feedback store is an append-only event log — its job is *who said what, when, in which run*. The arrival screen is
a state view — its job is *what is true now*. Those are two questions with two correct storage shapes, and this repo
already draws the line correctly for `placeName` and `accent` and incorrectly for address and ranking. Keep BOTH writes:
the answer still POSTs to `/api/feedback` (that is the provenance record, and it is what run identity attaches to), AND
the value lands on the grant row (that is the current value). Same split as `momlib.question_state()` — *"one function
to read instead of four tools disagreeing."*

⭐ **This also dissolves the audit's §7.4(1) finding without touching supersede.** *"Supersede now names a winner that
nothing renders"* is true only because there is nowhere to put a winner. Promote-at-capture creates the slot. Supersede
then governs the log (which run counts), and the grant row holds the value (what is on screen) — and neither has to
know about the other.

## 1b · WHAT A GRANT MAY READ — three tiers

| tier | contents | who reads it | where |
|---|---|---|---|
| **1 · your own row** | placeName, accent, address, addressParts, ranking, contactPref, relationship, capability, entry, vault | **any grant, no capability check** | `whoami`, widened |
| **2 · the household's published facts** | zones, the estate's shared canon | any grant in that estate | later; not needed for arrival |
| **3 · other people's authored words** | feedback notes, zone voice, Guru turns, observations | **administrator only**, plus Paul's standing consent rule | unchanged, where it is |

> **The rule: a grant reads what it WROTE, plus what the household PUBLISHED — never what another person AUTHORED.**

Tier 1 is safe by construction, not by promise: it is a single-row read keyed by the hash of the token the caller is
holding. You cannot read a row you do not hold the key to.

⛔ **Do not build a `personId`-filtered read over the feedback log now**, even though §0(2) shows it would be sound.
Two reasons: you do not need it if you do (d), and building it creates a read path over the log that becomes the standing
excuse never to fix the storage. If it is ever needed, the predicate is `r.personId === grant.personId` and rows with
`personId: null` are **refused, never adopted**.

⚠️ **What (d) does NOT fix, and must be said out loud:** the 44 pre-existing qa rows and every answer written before
promote-at-capture ships stay only in the log. They are not retro-promotable — you cannot tell which of eight addresses
was current. **The first estate that renders correctly is the first one onboarded after this ships**, which is an
argument for shipping it before gate ② rather than after.

## 1c · OFFLINE-FIRST — the cache/truth arrangement

The site's physical premise (CLAUDE.md § THE SITE'S PHYSICAL PREMISE) is permanent: Wi-Fi near the house, nothing
beyond it. Note the shape of the actual exposure here, though — **the arrival screen's first visit is almost certainly
online** (it is reached seconds after a flow that POSTs). The offline case for `estate/` is the **return visit**.

**The arrangement:**

1. **Render from localStorage immediately** — what it does today, and it is right. Zero latency, works offline, no
   skeleton, no spinner. **Keep the `K_OWNER === grant` guard** (`estate/index.html:190`); it is load-bearing and was
   correctly carried over from the shared-device incident.
2. **Fire `whoami` in parallel.** On 2xx, if a server value differs, re-render and overwrite the cache. On transport
   failure, leave the cached render exactly as it is and say nothing — **a cached receipt is not an error state.**
3. **Three distinguishable empty states**, where today there is one:
   - grant + `whoami` answered → server values.
   - grant + no cache + offline → *"I can't reach your place right now — this fills back in on wi-fi."*
     **Not** the current copy.
   - no grant → the current *"Once you've set your place up…"*, which is then true.

   ⛔ Today, a returning reader on a fresh device sees *"Once you've set your place up, what you told me shows up here"*
   — which tells someone who **did** set their place up that they did not. That is the same class of defect as the
   `s0` promise it breaks; it is the empty state lying rather than the copy lying.

**When they disagree — server wins, and here is why it is that simple today.**

`estate/index.html` has **no write path for these values**. The edit route is deliberately a feedback note (the F12
comment at `:301`), not an in-place edit. So the local copy has no authority it could assert: **server is truth,
local is a pure cache, last server read wins.**

⛔ **Do not resolve disagreements by timestamp.** The audit already recorded why (§7.3): *the aborted run is often the
last one*. Add device clock skew and a phone that has been off for a month and a cross-seam timestamp comparison is an
inference dressed as a rule.

**When an in-place edit control does ship**, the rule extends to: *local wins only while it holds an UNSENT edit;
the moment the write is acknowledged it is a cache again.* Do not invent a second sync model for it — this repo already
has an outbox (`tateTracker.door.outbox.v1`, rostered in `viewer.html`, and the pattern `handleFeedback`'s idempotency
comment at `:3068` was built for). One outbox, N callers.

## 1d · ⛔ A BUG ON THIS SURFACE, THIS WEEK — `estate/index.html:376–395`

Not a path question, but it is on the screen Bob meets and it violates the one rule these surfaces are built on.

```js
.then(function (r) {
  el("fbbox").hidden = true; el("fbnote").value = "";      // ← cleared BEFORE the branch
  ...
  t.textContent = r && r.ok ? "Got it — I'll put that right."
                            : "Saved on this device. I'll pick it up next time you're online.";
```

**On a non-2xx the textarea is wiped and the reader is told the note is saved on the device. Nothing is saved. Nothing
will pick it up.** There is no localStorage write and no retry anywhere on this page. The `.catch` branch is only
marginally better — it leaves the text in the box but hides the box, and nothing survives a reload.

CLAUDE.md, § the physical premise: *"A capture path that can lose her words while appearing to succeed would break the
one rule her surfaces are built on: capture must not lie."* This is that, on the arrival screen, shipped today.

**Two fixes, both cheap:** (i) 2 lines — do not clear the textarea until `r.ok`, and on failure say what is true
(*"That didn't go through — it's still here, try again in a moment."*); (ii) ~15 lines — write the note to the existing
outbox on failure and replay on next load, and then the current copy becomes true. **Do (i) before Bob's link goes out
regardless of which decision lands.**

⚠️ It may also be the visible half of the undiagnosed **A2** *"That didn't go through"* row, now 36h old — this handler
would render a real server failure as a reassuring message on a different surface. Worth checking whether the onboarding
POST path has the same shape before hunting further.

## Trade-off table — decision 1

| | (a) widen whoami | (b) read verb on /api/profile | (c) new /api/estate GET | (d) promote at capture |
|---|---|---|---|---|
| **complexity** | lowest — one row, one existing handler, above the capability gate | medium — POST-only route becomes a verb-switch; two auth shapes in one block | highest — new route, new auth decision, new tests | **low** — 4 field names in an existing block + 3 client lines |
| **scalability** | scales exactly as far as the grant row does | same | same | **the record becomes readable by anything, forever** |
| **future features** | the chooser (roles-and-access) is a render of grant rows — this is the same read | nothing extra | nothing extra | **unblocks the chooser, an estate summary, any second surface** |
| **future-Paul-with-Claude** | one endpoint, one comment, already annotated | a route that means two things is the harder one to come back to | a fourth door to hold in your head | **the record says what it holds; no re-derivation to re-learn** |
| **learning value** | low | low | medium (auth design) | **high — it is the log-vs-state distinction, which is the reusable idea** |
| **does it fix the broken promise?** | ✅ with (d) | ⚠️ only by re-deriving from the log | ⚠️ same | ✅ it is the fix |

**(a) + (d) together. (b) and (c) are the same work with a worse blast radius.**

---

# DECISION 2 · THE TENANCY SHAPE

## Recommendation

**A now, B next, and A is a stepping stone that does not tax B — with three named exceptions.**

Specifically:
- **synthetics → A**, their own deployments, their own namespaces.
- **Paul's own property → A**, `home` or its own, his call.
- **Bob this week → A, ONE house.**
- **Bob's second house → after B, in Bob's existing namespace.**
- **B starts with a no-op slice that can land any time, including this week.**

## 2d · Does A make B harder? No — and the reason is structural, not optimistic

**A and B touch disjoint code.** A is deployment configuration — `wrangler.toml` env blocks, Pages projects, KV
namespace ids, `pages-deploy.py`'s household mode. B is the Worker's key-building call sites. Nothing in `[env.bob]`
has to be undone to wire `scopeFor`.

**And B is a strict generalisation of A, not a replacement.** `scopeFor(request, env, grant)` returns `scopeOf(env)`
when there is no foreign grant — so **after B lands, an A-provisioned deployment keeps working, unmodified, forever.**
One deployment serving one estate is the n=1 case of many-estates-per-deployment, not a fork of it. That is the single
strongest argument for A and it is worth stating plainly: *A is not a detour, it is the base case.*

**What A genuinely costs, honestly:**
- N Pages projects, N Workers, N KV namespaces, N read tokens, **N deploys per release**. The audit measured what that
  rots into: `home` sat 26 commits behind because nothing deploys it, and no instrument reports a Worker's version.
  **That cost is real and it will bite.** But it bites as *staleness* — visible, diagnosable, fixable. B's failure mode
  is *cross-household reads and writes* — silent, and unrecoverable once written.
- Each household's data accumulates in its own namespace. Consolidating later is a key-by-key move.
  `tools/household-export.py` exists precisely for that and its docstring is explicit that it is a copy, never a move.

**But you probably never consolidate.** B does not require one namespace; it requires that a *request* resolve its
estate from the grant. You would only merge namespaces to give **one person a chooser across estates** — which is
Bob's actual long-horizon requirement, and the one place A does foreclose something (below).

⭐ **An unpriced benefit of A that should be on the board.** Under A, synthetic households never write into
`est-e6696a`. That means §2.4's conflict — *"production starts from nothing other than a text to Mom"* vs *"durable
synthetic households in production"* — **does not have to be adjudicated at all.** Neither sentence has to be retired.
Under B-first, one of them does, and it is Paul's sentence to write.

⭐ **And it discharges the audit's own falsifier 3.** §7.3's ordering claim — *the run-identity marker must exist before
step ②* — weakens to *before step ③* under A, by the audit's own stated falsifier. A buys the schedule back.

## 2e · If B: the order, the smallest first slice, and the falsifier

### ⚠️ First, a correction that changes the order

The audit says *"`assertScope` means a forgotten site throws at the call, not silently — which is the good news."*
That is true and it is only half true.

> **`assertScope` catches a FORGOTTEN conversion. It cannot catch a WRONG one.** A site that keeps calling
> `scopeOf(env)` passes `assertScope` perfectly — it is a valid, well-formed scope. It is just the wrong household.

So the real control is **the greppable `scopeOf(env)` inventory, not the assertion.** Before converting anything,
write down which of the 51 sites are *deliberately* deployment-scoped (rate limits at `:740`/`:839`, the chat budget,
the weather/AirNow/drought caches, `searchLibrary`, `listBothEras`) as a roster with a count, and make a check that
fails when the count moves for an unrostered reason. Without that, "done" is unfalsifiable.

Measured distribution of the 51, by enclosing function:

| cluster | sites | class |
|---|---|---|
| `handleFeedback` | 10 | per-household — Mom's words |
| `handleZoneAudio` | 4 | per-household — her voice |
| `handleZoneSave` · `handleZoneFeedback` · `handleZonesGet` · `handleZonesSyncStatus` | 7 | per-household |
| `handleSuggestSpecies` | 3 | per-household |
| `handleChat` · `persistConversation` · `logChatCost` | 4 | per-household |
| `handleMetrics` | 2 | per-household |
| `handleDoor` · `storeDoorRecord` | 2 | per-household |
| `loadObservations` · `saveObservations` · `handleAudioUpload` · `handlePromoteSpecies` · `handleCostLog` | 5 | per-household |
| `grantFor` | 1 | ⭐ **the identity door — special, see below** |
| rate limiters, `searchLibrary`, `listBothEras`, caches, `handleAmbient`/`AirNow`/`Drought`/`TodayLine` | ~13 | **legitimately deployment-scoped** |

### The order — readers before writers, identity doors absolutely last

1. **SLICE ONE, and it changes nothing: thread the scope through the router.** `grant` is already resolved once at
   `:3327`. Compute `const scope = scopeFor(request, env, grant)` immediately after it and pass it into each handler as
   an extra argument the handler **ignores**. Today `scopeFor` returns `scopeOf(env)` for every real request, because
   `grantFor()` nulls any grant whose estateId differs from the binding. **Zero behaviour change, independently
   verifiable, and it can land this week beside a live onboarding without touching a single key.** It also makes every
   subsequent step a one-line diff per site instead of a signature change.
2. **Canaries — small, read-only, low-value:** `handleZonesGet`, `handleZonesSyncStatus`, `handleCostLog`.
3. **Capture paths, one handler per commit, ascending by what they hold:** `handleZoneFeedback` → `handleZoneSave` →
   `handleDoor` → `handleMetrics` → `handleConversations`/`persistConversation` → `handleObservations` →
   **`handleFeedback` last** (10 sites, and Mom's words).
4. **The identity doors last of all.** `handleAccountCreate` (`:3174`) and `handleSession` (`:3298`) are each passed
   `scopeOf(env)` explicitly at the router — a one-line change each, and therefore *tempting to do first*.
   ⛔ **Do not.** Flipping the identity door first mints grants for a second estate in a namespace whose handlers still
   key by the deployment binding — so **every one of that person's writes lands under the wrong household, silently,
   and `assertScope` will not fire**, because it is given a perfectly valid scope. The identity door is what *creates*
   the second household; it goes last, after everything downstream can already read a foreign scope.
5. `grantFor()`'s `row.estateId !== env.ESTATE_ID` check (`:783`) is the last line to change, and it is the actual
   flip. Until it changes, B is inert and reversible by `git revert`.

### The falsifier — a test, written RED, before the change

> **Two grants · two estates · ONE namespace · ONE deployment. Write under each. Prove neither read sees the other.**

`tools/test-estate-isolation.py`, run against `lab` (own namespace, no real person):

1. Mint two grants in the lab namespace with different `estateId` — `est-lab0001` and a new `est-lab0002`.
   ⭐ **This cannot pass today**, because `grantFor()` rejects a foreign-estate grant. That is correct and it is the
   point: **write the test now, watch it be red, and turning it green is the definition of done for B.** A test written
   after the change can only confirm what you built.
2. POST a feedback note through each grant with a distinguishable marker.
3. GET the feedback range through each grant. Assert each read returns its own marker and **zero** of the other's.
4. ⭐ **The negative control that actually matters: assert raw KV holds TWO keys** —
   `est-lab0001:feedback:<date>` and `est-lab0002:feedback:<date>` — **not one merged array.** A test that only checks
   the API response passes just as happily when both rows sit in one key and the handler filters at read time, which is
   a completely different and far weaker guarantee. This is `[[Match the PAYLOAD, not the container]]`.
5. **The mutation control this repo's practice requires:** revert one converted handler to `scopeOf(env)` and prove the
   test goes red. A test that does not fail when you break the thing is not a test.
6. Wire it into the session-start block. An instrument no procedure reaches is not a capability the loop has — §3.1,
   fourth instance.

## 2f · ⛔ WHAT MUST BE DECIDED BEFORE THE FIRST SYNTHETIC WRITES INTO PRODUCTION

⭐ **The first answer is that choosing A makes this constraint not bind.** The hatch dies at the moment a **second**
household writes into a namespace that already holds one. Under A that never happens — every namespace holds exactly
one household, and *"delete the namespace"* survives intact. **This is the single largest risk-reduction A buys, and it
is worth more than the N-deploys cost.**

If B (or any shared-namespace write) is chosen, four things must land first, in this order:

1. **Which namespace the first synthetic writes into.** Everything else is downstream. Under B it is `home`'s — Mom's —
   and that is the write that removes the hatch.
2. **`household-export.py` must be RUN, not merely exist, against a namespace that holds data, with its coverage
   statement read by a human.** Its own docstring: *"The coverage statement is the product; the bytes are a side
   effect."* Run it against **`qa`** — that namespace holds three estates' keys and 48 answers, which is the closest
   thing that exists to the post-B world. **If it cannot enumerate qa's three estates today, it cannot protect
   production tomorrow.** This repo's own recorded rule: a file that has never been written is not yet a mechanism.
3. **A proven RESTORE, not just an export.** The tool is a copy and there is no `--restore`. An export you have never
   put back is a forensic artifact, not a backup. Prove the round-trip on `lab`: export → delete one key → restore →
   byte-identical. Unproven restore is the most common backup failure there is and closing it is an afternoon.
4. **Provenance on the ACCOUNT and GRANT rows, not just the answers** — and **do this regardless of A or B.**
   §2.4 measured it: `context.synthetic` lands on answers only; `handleAccountCreate` writes neither. So *"get rid of
   them once Mom populates an estate"* removes the words and **leaves live credentials behind**, and after Mom onboards
   `reset-production-estate.py` may never run again and cannot tell synthetic from real anyway. A single
   `provenance: "synthetic" | null` field, inherited from the invite the same way `capability` already is (`:487`), is
   ~4 lines in the Worker plus a `--synthetic` flag on `grant-mint.py`. **It is cheap now and unrecoverable if skipped.**

**And one broken control that blocks any of this.** `tools/synthetic-identity.py`'s docstring says
*"⛔ REFUSES TO TOUCH PRODUCTION"* while its `WORKERS` map contains `home` and
`.private/synthetic-identities.json` already holds four identities on `home`. The audit reports it and declines to
resolve it, correctly — the *ruling* is Paul's. **The engineering half is not a judgment call: a safety claim that
contradicts its own code is worse than no claim** (global CLAUDE.md: *"an OVERstated boundary is worse than an unstated
one: it reads as a promise"*). One of the two must change before that tool is used again, whichever way Paul rules.

## 2g · BOB'S TWO HOUSES — does the recommendation leave room?

Decompose the requirement — *two houses, two daughters, each seeing only her own*:

| requirement | under A | under B |
|---|---|---|
| two estates | ✅ two deployments | ✅ two estates, one deployment |
| each daughter sees only her own | ✅ **by namespace isolation — the strongest form available** | ✅ by `scopeFor` |
| Bob sees both | ⛔ **two links, two logins, no chooser** | ✅ one login, chooser renders his grant rows |

**A delivers the isolation requirement and fails the convenience requirement.** And the failure is not fixable within A:
`.plans/2026-09-04-roles-and-access-REQUIREMENT.md` establishes it — `worker.js` reads exactly ONE KV binding, no
deployment can read another's silo, **and the obvious workaround (a person-level index across silos) is already ruled
out by Paul as "a second derivation that could disagree with" the grant rows.**

⛔ **So here is the one place A genuinely forecloses something, and it is the thing to hold onto:**
**do not provision Bob's two houses as two A-deployments.** Two namespaces means a cross-namespace read to give him a
chooser later, and that read is forbidden. One house now; the second house lands in **Bob's existing namespace** after B.

⭐ **And that is the right home for B's first real requirement.** Bob's deployment — two estates, three people, one
person spanning both — is a far better test of `scopeFor` than Mom's ever will be, and **it carries none of Mom's data.**
B should be built against Bob's household, not against `home`.

**What I would ship this week:** Bob gets ONE house. His succession plan is not this week's requirement — nothing has
walked `myhome-bob` at all (audit §4.2), and building a second estate for a deployment where no one has completed a
single journey is building two gates ahead of the evidence.

## Trade-off table — decision 2

| | A · deployment per household | B · the `scopeFor` conversion | C · not production |
|---|---|---|---|
| **complexity** | low per household, linear forever (N of everything) | one bounded refactor, ~30 sites, then flat | lowest |
| **scalability** | ⛔ breaks at "one person, many estates" and at N-deploys-per-release | ✅ the actual answer | n/a |
| **future features** | ✅ synthetics, Paul, Bob-one-house · ⛔ the chooser, self-serve estates, Angel's read-only | ✅ all of them | ⛔ loses durability, the point of gate ② |
| **future-Paul-with-Claude** | ✅ each household is one obvious config block; `wrangler.toml` is already the readable roster | ⚠️ scope threading is subtle — but `assertScope` + comments make it legible, and the file already documents itself well | — |
| **learning value** | low — it is ops repetition | ⭐ high — multi-tenancy done properly, with a mechanical isolation proof. This is the portfolio artifact | none |
| **blast radius if wrong** | one household's namespace | **all households in a namespace, silently** | none |
| **reversibility** | ✅ delete the namespace, always | ⛔ dies at the first second-household write | ✅ |
| **cost that will actually bite** | **staleness** — `home` is 26 commits behind and nothing reports a Worker version | **a wrong-scope write nothing catches** | — |

---

## Where I am RULING vs. where it is PAUL'S CALL

**Ruling (engineering — take these unless you disagree with the reasoning):**
- The read shape: **promote at capture + widen `whoami`**. No new endpoint. (§1)
- The three read tiers, and *a grant reads what it wrote plus what the household published, never what another person
  authored*. (§1b)
- **Server wins on read; local is a pure cache; never resolve by timestamp.** Three distinguishable empty states. (§1c)
- The `estate/index.html` feedback handler is a **bug**, not a preference — fix (i) before Bob's link goes out. (§1d)
- **A does not foreclose B.** Conversion order: no-op slice → read canaries → capture paths → identity doors last.
  `assertScope` catches forgotten, not wrong. (§2d, §2e)
- The isolation proof is **mechanical, written RED first, asserts on raw KV keys, with a mutation control**. (§2e)
- **Provenance on the grant/account row regardless of which shape wins.** (§2f·4)
- `synthetic-identity.py`'s self-contradiction must be resolved before that tool is used again. (§2f)
- Widen `check-storage-keys.py` to `onboarding/` and `estate/`. (§0·3)
- **Do not provision Bob's two houses as two deployments.** (§2g)

**Paul's call:**
1. Whether *"durable synthetic households in production"* means **their own production deployments** (A). I believe
   yes and I believe A is what he wants once it is stated — but it restates his sentence and that is his to write.
2. **Bob: one house now, or wait for two.** I recommend one. It is a schedule-vs-evidence trade and he holds the date.
3. **Whether a founding owner's `administrator` capability — which lets Bob read his daughters' notes via the API —
   is intended.** Live today, undocumented, and it is a household-relationship question, not an engineering one.
4. **Whether B starts this week at all.** Slice one is a no-op and safe; anything past it is not a job to run beside
   Bob's link going out.
5. Whether to spend the afternoon on the restore round-trip now or after gate ②.

---

## Principles to propose (NOT added — awaiting Paul's confirmation)

1. **A receipt reads state; it never re-derives from a log.** — scope: cross-project.
2. **An assertion that validates SHAPE cannot validate CORRECTNESS — the greppable inventory is the control.** —
   scope: cross-project.
3. **Convert readers before writers; convert the identity door last.** — scope: fernwood.
4. **Write the isolation test RED before the change that makes it green.** — scope: cross-project.
