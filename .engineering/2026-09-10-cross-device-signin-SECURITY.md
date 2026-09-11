# SECURITY-STEWARD — cross-device sign-in · modes ① ROSTER and ③ LEGIBILITY

<!-- Filed VERBATIM by the cross-device-signin lane (tate-tracker-21) on 2026-09-10 ~10:15 PM ET from the
     seat's returned report. The seat has no write tool. Filed under .engineering/ rather than .security/
     because the seat itself flagged that .security/ is not in finding-authority-check.py's FINDING_DIRS
     and prose there is never re-read; where it ultimately belongs is practice-steward's lane, not the
     lane's. Companion trail: .engineering/2026-09-10-cross-device-signin-ENGINEERING.md · synthesis:
     .plans/2026-09-10-cross-device-signin-FINDINGS.md -->

**Repo** `/Users/paulkirschenbauer/Developer/Tate-Tracker` · **sha** `5ffe811` · **2026-09-10**
**Symbols cited, not line numbers** (HEAD moved four times today; `worker.js` shifted ~270 lines).

## DENOMINATOR FIRST — what this run actually covers

**Read and verified by me at `5ffe811`:** `worker/wrangler.toml` (all six env KV bindings) · `worker.js` symbols `handleSession`, `accountKey`, `accountFor`, `putAccount`, `handleAccountCreate` (partial), `handleUsernameChange`, `scopeOf`, `scopeFor`, `scopeOfRoute`, `keyFor`, `grantFor`, `personFor`, `hostAgrees`, `handleDoor`, `doorRateLimitOk`, the `/api/account/available` route branch, and the grant-gate branch that writes `door_failed` · `estate/index.html` `reconcile()`, the `placed` block, and the row-renderer's state ladder · `onboarding/index.html` sign-in handler · `tools/grant-mint.py` `gated()`, `administrators()`, `find_row()`, `mint()`, `revoke()`, `hydrate()` · `.plans/2026-09-10-multi-tenancy-PLAN.md` §"HOW PAUL GETS IN" · `.plans/2026-09-10-account-estate-model-SCOPE.md` §⑥–⑦.

**NOT checked, and each of these could change a ruling:**
- **I did not enumerate the route table.** `worker.js` carries ~23 telemetry writers and `.engineering/2026-09-06-environment-pipeline.md` says a roster of routes omitted eight. I examined **4 auth-surface routes** of an unenumerated total. Any route I did not read may hold a second oracle.
- **I did not read `feedbackRateLimitOk`.** `/api/account/available` calls it — verified at the call site. The nearby constants read 20 per IP per 300 s, but those are bound to `doorRateLimitOk`, which I *did* read. **Attributing them to the availability route is inference and I am not making it.** The availability route's actual ceiling is unmeasured.
- **I did not read `~/Developer/fernwood-private/grants.json`.** Every claim below about the register's contents is conditional on the brief's fact 5 and on the multi-tenancy plan's own §"HOW PAUL GETS IN" ¶1, which states the same row independently. Two in-repo corroborations, zero direct reads.
- **I did not read the live KV.** The 14 `door_failed` rows, the presence/absence of specific account rows, and the two `pkirsch` personIds are yours, unverified by me.
- **I did not verify the deployed Worker matches `worker.js` at `5ffe811`.** Every ruling below describes the *source*. A deployed binary older than HEAD would invalidate them silently.
- **I deliberately did NOT probe production.** I had `WebFetch` and could have called `/api/account/available` against the live origin with a real username. Doing so would have *performed* the enumeration I am reporting, against a real person's name, to confirm a thing the source already shows. Abstention is the finding's own rule applied to the finder.
- **I did not establish whether account creation requires an invite.** `handleAccountCreate` reads a presented invite into a nullable local; I did not read far enough to see whether a null one refuses. **So I cannot certify "invite-only," and L1's threat model below states that as an assumption, not a fact.**

*(Lane's note, added at filing: the register row was read by the lane — `p-paul @ est-e6696a relationship:[owner] capability:administrator` is present in `fernwood-private/grants.json` — so the headline's first falsifier is already answered: the row exists as described. The live KV facts the seat calls "yours, unverified" are in FINDINGS §1–§2. The deployed Worker at `home`/`paul` carries `build_sha` 0d15bd0 / d7b642e with no `worker.js` diff from 318416a to HEAD.)*

---

## 🔴 HEADLINE — NOT IN YOUR BRIEF: the wrong register row disarms the consent gate built for exactly this case

**Tier:** `est-e6696a` (Mom's household) × `p-paul` (administrator) × *register declaration*.

`grant-mint.py:gated()` is G2's discriminator. Its logic, verbatim in structure: for each administrator, if `find_row(reg, admin, estate)` is `None` **or** the row's `relationship` is empty → the estate is **gated** (consent required). Otherwise → **not gated**.

The register declares `p-paul @ est-e6696a` with `relationship: ["owner"]` and `capability: administrator`. Therefore `find_row` returns a row, `relationship` is non-empty, and **`gated()` returns False at Mom's estate.**

`.plans/2026-09-10-multi-tenancy-PLAN.md` §"HOW PAUL GETS IN" consequence 3 asserts the opposite: *"G2 firing at Mom's estate is CORRECT, not noise. The administrator holds no relationship there — that is exactly G2's case."* **That assertion is false against the current register, and the same plan supplies the cause two paragraphs earlier** — it identifies the `["owner"]` row as wrong, and classifies correcting it as *"register work… part of rights in good enough order."*

⭐ **It is not hygiene. It is a live control failure.** The register is an **input to the mint**: `mint()` calls `load_register()`, builds `kv_row` from `row["relationship"]`, writes KV, then `save_register()`. So a run of `grant-mint.py mint --person p-paul --estate est-e6696a --env home` would mint a real administrator grant at Mom's household **with no consent entry required**, because the only gate that would have demanded one reads the very row that is wrong. The back door the 09-10 ruling closes at the *policy* layer is open at the *tooling* layer, and it is held shut today only by nobody having run the command.

This is the CLAUDE.md pattern again, in its sharpest form: **a control entirely correct about its own question** (*does the administrator hold a declared relationship here?*) **answering a different question from the one it is trusted for** (*has this household consented to administrator reach?*). The two diverge exactly when the declaration is wrong — which is the only case the gate exists for.

- `settled_by`: code read at `5ffe811` (`gated`, `mint`) + plan §HOW PAUL GETS IN. `authority_checked: true` for the *logic*; **`false` for the register's contents** — conditional on fact 5.
- **Falsifier (run this before acting):** `python3 -c "import json;r=json.load(open('$HOME/Developer/fernwood-private/grants.json'));print([g.get('relationship') for g in r['grants'] if g.get('personId')=='p-paul' and g.get('estateId')=='est-e6696a'])"` — an empty list or no row means `gated()` already returns True and this finding is void.
- **Second falsifier, structural:** after the register is corrected, `gated(reg,"est-e6696a")` must return True. If correcting the row does *not* re-arm G2, the discriminator has a second defect I did not find.
- ⛔ **Out of my lane:** whether to correct the register, and how, is not mine — the plan already rules the register is the wrong thing. I am ruling only that **correcting it is re-arming a gate, not tidying a record, and should be sequenced as such.**

---

## ROSTER RULINGS

### R1 · May a credential minted at one deployment be presented at another household's origin?

**Tier:** `{any estate}` × `{person holding no grant there}` × `{grant token, class: bearer credential}`.

**RULING: Presentation is always ALLOWED; REACH is decided by the grant row and by nothing else. A credential may never be refused *because of where it was presented*, and may never be accepted *because of where it was presented*.**

Today the refusal is correct but **over-determined by an accident that is scheduled for deletion**. A foreign grant fails twice, as `worker.js`'s own gate comment states: it is not in this deployment's namespace, *and* it would be rejected if it were. Under one-origin, **half of that disappears by design** — namespace separation is the thing M5 removes. What remains is `grantFor()`'s route→row agreement plus the ruled `grant:<personId>:<estateId>` index.

⚠️ **The half that remains has a hole I verified and that the plan's falsifier cannot see.** `hostAgrees()` returns `true` when there is no `Origin` header. Its own comment calls this vacuous agreement and justifies it as *"a routing check, not access control"* — which is correct **today**, and `.plans/…-account-estate-model-SCOPE.md` ⑦ item 8 confirms the destination: `hostAgrees` *"stops carrying tenancy and becomes an ordinary CSRF control."* The risk is the **interval**: between now and one-origin, `hostAgrees` is the only host-shaped control, and it is absent for every non-browser caller. If any step of the migration leans on it while namespaces are collapsing, the lean is on nothing.

- **Falsifier — the plan's, plus the half it is missing.** The SCOPE doc's falsifier is: *two accounts on one deployment, each having founded their own estate, every cross-read returns 404.* ⭐ **Re-run that identical test with the `Origin` header removed.** The plan's falsifier is browser-shaped; the control it silently relies on is Origin-shaped. A pass with a browser and a fail with `curl` is the exact shape that would ship.
- **Could not check:** the ~51 `scopeOf(env)` call sites the code's own gate comment names. The comment states plainly that a site still calling `scopeOf(env)` *"passes `assertScope` perfectly — valid scope, wrong household."* **So the number of handlers that would silently serve the wrong household under one-origin is knowable by `grep -c 'scopeOf(env)' worker/worker.js` and I did not run it.** That count is the real denominator of R1 and it is missing from this report.

### R2 · May Paul's ACCOUNT row be copied cross-namespace so he can sign in at home?

**Tier:** `est-e6696a` × `p-paul` × *account row (identity class)* — distinct from *grant row (authorization class)*.

**RULING: Identity IS portable. An account row at a household implies NO reach — verified. But the account row as it exists today is NOT purely identity, and copying it as-is WOULD collide with fact 5.**

The reach half is clean and I verified it: `handleSession`'s fallback grant sets `estateId: priorEstate || null`, and the write is guarded `if (grantRow.estateId)`. A copied account row with no accompanying route row yields **no grant written at all**. The code's own comments show this was deliberately repaired — the fallback used to hardcode `administrator` (*"a LOST GRANT into a privilege escalation"*) and used to write `estateId: scope.id` (*"the pre-seeding the signup ruling removed"*). Both are fixed. **An account row alone confers nothing.**

⛔ **The collision is in the fields that ride along.** That same fallback reads `acct.conferredRelationship`, `acct.relationship`, `acct.conferredCapability`, `acct.capability` **off the account row**, and the row also carries `tokenHash` — a pointer into the route/grant graph. So:

> **If the copy carries a capability/relationship field, or carries `tokenHash` alongside a copied `route:` row, then signing in MINTS the grant.** That is fact 5's back door reached by *copy* instead of by *mint* — a different verb, the same outcome, and with no `grant-mint.py` gate in the path at all, because `handleSession` is not that tool.

**ROSTER ROW (proposed):** *A value of authorization class — `relationship`, `conferredRelationship`, `capability`, `conferredCapability`, `tokenHash` — may not cross a namespace boundary on an identity-class row. A cross-namespace account copy carries credential material (`salt`, `hash`, `iterations`, `algo`), contact fields, and `personId`. Nothing else.*

- **Falsifier:** copy a stripped account row into a namespace where the person holds no grant, sign in with the correct password, then call `/api/grant/whoami` with the returned token. It must answer `hasEstate:false`, `estates:[]`, `estateId:null`. **Anything else means a field on the row conferred reach** and names which one.
- **Could not check:** the complete field list an account row can hold. `putAccount` writes whatever `row` it is handed, and the profile path writes to the account row too (per its own comment). **So the strip-list above is derived from the fields `handleSession` READS, not from the fields an account row CAN CARRY. Those are different sets and I only measured the first.** The honest form of this rule is an allow-list on the copy, not a deny-list.

### R3 · Register or store — which is the roster of truth?

**Tier:** `est-e6696a` × `p-paul` × *declared relationship*.

**RULING: The STORE is the roster of truth for REACH. The register is a record of intent and of authorship — and it is NOT merely descriptive, which is the part that matters.**

I had expected to rule the register a harmless annotation. **The code says otherwise:** `grant-mint.py` loads the register, derives `kv_row["relationship"]` from it, and gates on it via `gated()`. The register is **upstream of the store on the mint path**. So the clean formulation *"the register describes, the store decides"* is false as built.

**What a register row nobody can enforce does to trust — three effects, in order of severity:**

1. **It disarms the gate** (the headline finding). This is not a trust *perception* problem; it is a control failure.
2. **It creates a reading that is indistinguishable from a grant.** `access-map.py` and `watch-accounts.py` both read this register. A human answering *"who can reach Mom's household?"* from the register gets the wrong answer with no marker of uncertainty.
3. ⚠️ **`watch-accounts.py` reports the divergence as `⚡ DIVERGENT` and names neither resolution.** A divergence has two opposite repairs — mint the grant, or correct the register — and the ruling permits exactly one of them. The tool is correct about its question (*do these disagree?*) and the disagreement's direction is the whole decision. **A reader who trusts the flag to imply the repair will reach for the forbidden one, because minting is the action the tool sits next to.** Same class as the headline: right question, wrong inference available.

**ROSTER ROW (proposed):** *The register may declare only what the store could enforce. A register row asserting a relationship the store does not hold is a finding **against the register**, never against the store, and never an input to a mint. Any tool that reads the register to decide whether a gate applies must first assert register↔store agreement for the rows it consults, and refuse on divergence rather than proceed.*

- **Falsifier:** `python3 tools/grant-mint.py --selftest`. Its 30-odd clauses cover phantom credentials, dry-run byte-identity, G1/G2/G3. **Add one: a register row declaring a relationship with no corresponding live KV grant must make `gated()` REFUSE rather than return False.** If that clause can be added and passes without other changes, this ruling is cheap. If it breaks existing clauses, the coupling is deeper than I measured.
- **Could not check:** the register's actual contents, and whether `access-map.py` has the same coupling. I read one of its readers.

### R4 · Two personIds for one username across namespaces — what does M5 do with them?

**Tier:** production namespace × `{p-yjnw9lt41nww, p-jhgwhxxz6zce}` × *username index*.

**RULING: The collision is REAL, it is SILENT, and it fails CLOSED on authentication but OPEN on identity. Ruling: M5 must refuse on username collision rather than resolve one.**

`usernameIndexKey()` is **bare** — `username:<lowercased>`, no estate prefix. The code's own comment says *"Bare/deployment-scoped, like `route:`. No collision risk: every estate key begins `est-…:`."* ⭐ **That reasoning covers collisions with estate keys and says nothing about collisions between two namespaces being merged into one** — which is precisely M5. The same username at env.paul and env.qa produces the **byte-identical key**. A copy is last-writer-wins, with no error.

**What breaks, precisely:**
- **Authentication fails closed.** `account:<personId>` is authoritative and carries the hash; the index points at one of the two. The loser's password will not match the winner's row → `deny()`. Locked out, recoverable. Not a breach.
- **Identity fails open.** Two authoritative `account:<personId>` rows survive, one of them unreachable by username. `/api/account/available` reports the name taken. `handleUsernameChange` cannot free it — it deletes only `accountKey(scope, from)`, leaving the index and the orphan `account:<personId>` row. **The residue is a person whose account exists, holds their contact fields, and can never again be reached by name.**
- ⛔ **And a dated trap in the rename path.** `handleUsernameChange`'s uniqueness check is a bare `get(accountKey(scope, to))` — **the legacy shape only**. Signup uses `accountFor()`, which checks index-then-legacy, under a comment that says explicitly *"THE UNIQUENESS CHECK MUST SEE BOTH SHAPES."* The rename path does not obey its own file's rule. **It is safe today only because `putAccount` dual-writes both shapes** — accidental safety, the pattern this repo names by name. **At M6 ("delete the old account, grant and route rows") the legacy key disappears and the rename check goes blind: a rename could then claim a username already held under the index.** Not a live vulnerability. A scheduled one, with a named trigger.

- **Falsifier:** in a scratch namespace, write two `account:<personId>` rows and one `username:<u>` index, then attempt sign-in as each. **Expected: one succeeds, one 404s, and no tool reports the orphan.** If any tool reports it, the blindness is narrower than I claim. Second: with `putAccount`'s legacy write stubbed out (M6 simulated), attempt a rename onto an index-only name. **A 200 is the M6 trap confirmed.**
- **Could not check:** whether M5's copy mechanism (unwritten) would even encounter this, and whether the two `pkirsch` rows carry different contact fields — which would decide whether a merge is a choice or a loss.

---

## LEGIBILITY RULINGS

### L1 · The oracle trade — THE RULING

**Threat model, honestly, at this scale.** A handful of families. Sign-up **assumed** invite-only (⚠️ **I could not verify this** — see denominator). No public directory. No money in the product. The plausible adversary is not a researcher; it is an opportunist with a link, or a person in an adjacent household. **Nobody is attacking Fernwood** — the foundation's own framing — and the live cost tonight was not an attacker but *Paul*, locked out of a product he wrote, unable to tell which of two things was wrong.

**What enumeration would actually buy an attacker here — the denominator you asked for:**

| it buys | it does not buy |
|---|---|
| confirmation that a given username has an account **at this deployment** — and since one deployment ≈ one household today, that is a **person↔household association**, the SUBJECT axis the roster was amended for on 09-10 | any data (every estate route resolves a grant) |
| conversion of "guess a name *and* a word" into "guess a word" against a known-valid name | the word itself — PBKDF2 with per-row salt and iterations, verified in `handleSession` |
| a target list for credential stuffing, if a family member reused a word | reach — an account row confers nothing (R2) |

⛔ **AND THE DECISIVE FACT, WHICH REFRAMES THE WHOLE TRADE: the enumeration is already published.** `GET /api/account/available?u=<name>` is unauthenticated, is not behind the grant gate, does **not** call `hostAgrees`, and answers `{available:false}` for a name that exists at that deployment. It is a legitimate signup affordance (the onboarding page debounces on typing) and I am not calling it a defect. **But it means the byte-identical login 404 is protecting a secret that a sibling route on the same Worker gives away over a GET.** `handleSession`'s comment — *"a distinguishable pair is a username oracle"* — is true in isolation and **its denominator excludes the cheapest route to the same fact.**

**Rulings on your four options:**

- **(a) keep the 404 and the one sentence — ⛔ REFUSED.** Not because the 404 is wrong. The 404 and the dummy-`derive()` timing equalization are both good and should stay. It is refused because **its stated justification is falsified by `/api/account/available`**, and it charges a real usability cost — Paul's tonight — for a secret already published. **Paying a person-facing cost for a secret that leaks elsewhere is the worst trade available**, and it is the one currently in force.
- **(c) have the server distinguish — NOT refused on enumeration grounds, but NOT recommended.** Enumeration is already available, so this buys the attacker little that is new. It is declined because it makes the Worker a *second* publisher of the same fact, is irreversible in the record (see L3), and because the ruled destination changes the question entirely. **Do not spend a one-way door on an interim.**
- **(d) one landing page, one house-independent sign-in — ⭐ RECOMMENDED as the structural answer, and it is already ruled.** Under one origin *"not at this house"* ceases to exist as a failure mode: there is one sign-in and afterwards a person picks from their own shelf. The SCOPE doc's ⑦ item 9 reaches this independently from the disclosure side — *"`myhome-bob.pages.dev` tells a stranger a household exists for someone called Bob. One origin for everyone names nobody."* **This is Paul's own stated direction and it is the correct security answer, not merely the convenient one.** ⛔ It is blocked on A5 (per-request canon guard), so it cannot be the interim.
- **(b) keep the 404, widen the sentence — ✅ RULED PERMITTED, and it is the correct interim.**

> ### ⭐ THE DISTINCTION THIS LANE NEEDS, and it is one line
> **An oracle requires the response to VARY with the secret. Copy that enumerates the POSSIBILITIES is not disclosure; only copy that varies with the TRUTH is.**

A sentence naming both possibilities is shown **identically to every failed sign-in regardless of which failure occurred**. It reveals nothing, because it is a constant. `onboarding/index.html`'s comment — *"The copy must not undo server-side care by being more specific"* — conflates *more specific about the SET* with *more specific about WHICH*, and only the second is an oracle. That conflation is what left Paul with a sentence that could not describe what had happened to him.

⛔ **I am not writing the sentence — that is content-steward's.** The **constraints** the copy must satisfy, which are mine:
1. **One string, byte-identical in every failure case**, selected from a single non-2xx branch.
2. **No server-supplied reason code may reach the client.** The response body stays `{error:"not-found"}`.
3. **No second round-trip to disambiguate** — a follow-up call whose timing or result varies with the secret re-creates the oracle the copy avoided.
4. The remedy it points at must be **reachable by someone holding only a phone and a link**, since that is the failing reader's actual situation.
5. ⚠️ **It must not contradict L2's split** — a person who is at the wrong house and a person whose network is down must not be routed to the same next action.

- **Falsifier:** capture the raw HTTP response for (i) a valid username with a wrong word and (ii) a username that does not exist, at the same origin. **Status, body bytes, and header set must be identical, and response times must be indistinguishable.** If they diverge, the oracle is in the transport and no copy decision matters. *(The dummy `derive()` on the missing-account path exists to make (ii) cost the same as (i) — I verified the call, **I did not measure the timing**, and a real measurement is the only thing that settles it.)*
- **Could not check:** whether `/api/account/available`'s rate limit is tight enough to make bulk enumeration impractical (see denominator). **That number is the difference between "the secret is published" and "the secret is published slowly," and my ruling assumes the first.** If the limit turns out to be strict, option (a)'s justification is partially restored — though its usability cost is not.

### L2 · The laptop shell — a page that looks signed in while every request is refused

**RULING: YES — a legibility failure of exactly the "can they TELL" kind, and it is the sharpest one in this report, because the property itself makes the wrong reading credible.**

Verified in `estate/index.html`: the `reconcile()` handler's `!d` branch (a resolved response that was not `ok` — **including the 404 that refuses a credential**) and its `.catch` branch (**network unreachable**) both set the same `reachUnknown` flag, and the row renderer prints one string for it. **A refused credential prints as a network problem.**

⛔ **Why this is worse here than it would be anywhere else.** CLAUDE.md's founding premise: no cell reception, Wi-Fi falls off with distance, *"never propose a design whose mitigation is improve the signal."* At Fernwood, **"we couldn't reach your place" is frequently TRUE** — which makes it the most believable possible cover for a refusal. A person reading it will walk toward the house and try again. **The two states have opposite remedies:**

| state | duration | remedy |
|---|---|---|
| credential refused | **durable** — waiting never fixes it | a new credential, from a person |
| network unreachable | **transient** — moving toward the house fixes it | location, and patience |

**Printing one sentence for both guarantees that at least one reader takes the wrong action, and at this property the wrong one is the likelier read.**

**What the page must distinguish — three states, not two** (constraints, not copy):
1. **Refused** (a response arrived; it was 404). Durable. Remedy is a person. **Must not suggest retrying.**
2. **Unreachable** (the fetch threw). Transient. Remedy is location. **Must not suggest the credential is bad** — telling a person at the far end of the property that their credential is invalid is a false alarm the property manufactures daily.
3. **Record reachable but broken** (a response arrived; 5xx). Currently falls into `!d` alongside the refusal. Transient, remedy is neither — it is Paul's. ⚠️ Arguably honest under the current sentence; named so the split does not silently re-merge it.

⭐ **The code already separates these branches and merges them one line later.** This is a one-flag split, not a redesign.

⚠️ **The masthead half is already recorded and I am corroborating, not discovering.** The `placed` block paints an authored positive claim from `localStorage` before `reconcile()` runs, under the `mine` guard. The file's own comment names this as open item 3, states that three exits never self-correct, and says the honest fix is to render the card from the reconcile rather than before it. **My addition is only the severity ordering: for a REFUSED reader this is not a stale cache, it is a positive assertion about a household they have no standing at**, which is the SUBJECT axis, not a freshness bug.

- **Falsifier:** at a `fernwood-home` origin, put a syntactically valid but unknown grant in `localStorage` and load `/estate/`. Then load it again with the network disabled. **The two screens must differ.** If they print the same string, this finding is live. *(This is the exact pair of states Paul hit tonight, in the order he hit them.)*
- **Could not check:** `/homes/` — the brief references it and `estate/index.html`'s comment says it told Paul the same lie one screen over. **I did not read that surface. There may be a third and fourth copy of this collapse and I measured one.** Same class as the "three readers of estate-neutrality, two instrumented" lesson.

### L3 · The silent refusal — `deny()` logs nothing

**RULING: YES, an unlogged refusal at the door is a trust gap, and the specific shape of it is worse than "we have no data."**

Verified: `handleSession`'s `deny()` returns a response and writes nothing. `door_failed` is written **only** in the grant-gate branch — i.e. only when an `X-Grant` header is presented. So:

> **The system logs the failures of people who HAVE a credential, and logs nothing for people trying to GET one.** The record is blind at first contact — the moment a new family member is most likely to fail and least likely to have another route in.

⭐ **Tonight is the proof, and the numbers are the argument.** 14 `door_failed` rows exist for the laptop's stale grant — the failure that was *already visible*, because Paul was sitting in front of a rendered page. **Zero rows exist for the phone's repeated sign-in failures** — the failure that was *invisible*, and the one he actually reported first. **The record over-represents the observable state and is silent on the unobservable one.** An administrator watching `watch-door.py` would have seen a grant problem and had no way to learn that a person could not sign in at all.

**What may be logged, under `watch-door`'s rule (outcomes, never who):**

✅ **Permitted:** a `signin_failed` outcome carrying `ts`, `env`, `door:"entry"`, `serverSide:true`, and a **single constant reason** — plus `declarePerson()` as every other door record uses, so `personId` is null by construction.

⛔ **Forbidden, and this is the load-bearing half:**
- **The attempted username must never be written.** It is the person's identifier and it is *the exact value the L1 oracle question is about*. **A log of attempted usernames IS the enumeration oracle, written down, at rest, and readable by every tool that reads `door:`.** A product cannot refuse to publish a fact over HTTP and then archive it.
- **The reason must not discriminate** unknown-username from bad-word. Keeping the response undifferentiated while differentiating the *record* moves the oracle rather than removing it — and the record is the more durable of the two.

⚠️ **One live roster observation, made by reading and not in your brief:** `doorRateLimitOk` builds its key as `keyFor(scopeOf(env), "ratelimit", "door", ip, bucket)`. **A client IP is at rest in KV, inside a key.** It carries `expirationTtl` of twice the window, which is the mitigation and a real one. But it sits in tension with `watch-door`'s *"never who was standing at it"*: an IP is closer to a person than a deviceId is, and a key is listable by prefix. **Flagging, not alarming** — the TTL is short and the purpose is legitimate. It belongs on the roster as a **declared** exception rather than an undeclared one, exactly like the census geocoder.

- **Falsifier:** `python3 tools/watch-door.py` over tonight's window. **If it reports grant failures and cannot report that anyone failed to sign in, the gap is confirmed at the reader, not just at the writer.** Then: after adding `signin_failed`, `grep -ri "username" ` over whatever writes it — **any path from the submitted username into a stored record is the forbidden case.**
- **Could not check:** whether `/api/onboarding-metrics` or another channel already captures sign-in attempts from the client side. **The client could be logging what the server does not, which would make the oracle-at-rest risk live TODAY rather than prospective.** I read `onboarding/index.html`'s sign-in handler and saw no such call in the failure branch, but I did not read the file's instrumentation layer.

---

## PROPOSED ROSTER ROWS (mode ①)

| # | tier | rule | fires on |
|---|---|---|---|
| **RR-1** | any × any × *authorization class* | authorization fields (`relationship`, `conferredRelationship`, `capability`, `conferredCapability`, `tokenHash`) may not cross a namespace boundary on an identity-class row; a cross-namespace account copy is an **allow-list**, never a strip-list | any tool or script performing a cross-namespace account copy (M5) |
| **RR-2** | any × administrator × *register declaration* | a register row may declare only what the store could enforce; it may never be an input to a gate without a register↔store agreement assertion, and divergence **refuses** rather than proceeds | `grant-mint.py`, `access-map.py`, any future register reader |
| **RR-3** | any × any × *username* | an attempted username may never be written to any durable record on a failed authentication, at the server or the client | any new `signin_failed`-class telemetry |
| **RR-4** | any × any × *client IP* | a client IP may exist at rest only inside a TTL'd rate-limit key, as a **declared** exception; any other IP-at-rest is a finding | `doorRateLimitOk`, `feedbackRateLimitOk`, any new bucket |
| **RR-5** | any × any × *refusal legibility* | a refused credential and an unreachable network may never render the same string on any surface | every surface that reconciles against `whoami` — ⚠️ I verified one (`estate/`) and the record names at least one more (`/homes/`) |

---

## FILING — one thing about your own instruction

⚠️ You said you would file this verbatim under `.security/`. **`.security/` is not in `FINDING_DIRS`** (`.engineering`, `.ux-reviews`, `.content`, `.cycle-findings` — per `~/.claude/tools/finding-authority-check.py`). Prose filed there is **invisible to `finding-authority-check.py`**, which is the check that exists for this seat's failure mode. My foundation names this exact trap about `agents/audits/`, and the same applies here.

**I am not ruling on where it goes** — that is practice-steward's lane, not mine. I am stating the fact: **filed under `.security/`, nothing will ever re-read this, and the headline finding is one nobody will rediscover by running the loop's own procedure.** That is the shape CLAUDE.md records four times.

---

## ⛔ THE HONEST SHAPE OF THIS RUN

**I did not report "no vulnerabilities found," and this run is not clean.** One finding above (the disarmed G2 gate) is a control failure I found by reading a tool you did not name, and it **contradicts a plan's own written assertion**. One (the rename check at M6) is a scheduled failure with a dated trigger. One thing I expected to find — username takeover via the rename path — **I retracted after reading `putAccount`, which dual-writes both key shapes.** It was a false positive and checking cost two minutes.

**What is most likely to be wrong here:** I read **4 auth-surface routes of an unenumerated route table**, did not run the `scopeOf(env)` call-site count that is R1's real denominator, did not measure the availability route's rate limit that L1's ruling assumes away, did not read `/homes/` where L2's collapse is recorded to repeat, and read **zero live KV**. **If a real failure is found in these surfaces by someone else, it will most likely be in the routes I did not enumerate** — and per the foundation's falsifier, that means this denominator did not name it.
