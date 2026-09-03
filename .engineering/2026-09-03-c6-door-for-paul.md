# C6 · THE DOOR FOR PAUL — path evaluation

**Seat:** `engineering-partner` · **Mode:** path evaluation · **Date:** 2026-09-03
**Item:** `BACKLOG.md` § C6 (declared) · **Objective:** O3 · **Depends on:** C4, C5

> ## ⛔ STATUS: EVALUATION ONLY. No canon touched, nothing deployed, nothing written outside this file.
> Every recommendation ends at Paul's gate. The **privacy/security seat is a blocking prerequisite** on
> the credential and the private tier (`~/.claude/agents/backlog.md` — *"BLOCKING PREREQUISITE on step
> 6"*). I am not that seat: §2 and §3 are **inputs to its review**, not conclusions ahead of it. §1 and
> the instrumentation leg of §2 carry no credential and no private material, so they are **not** blocked
> by it.

**Read (by role and section, not path — the repo name changes under C4):** the item row, § M3, § C4
`RULED`, § C5 in the backlog · the product engine's § ACTIVATION, § minimum-is-ZERO,
§ Mom's-retrofit, § credential-per-grant, § BOTH-PASSWORDS-OPTIONAL · the data-model design plan §2
rule 3, §2c, §5, §6, §7 · the ux login-door review (F1a/F1b) · the activation-journeys research
(§1.3, §5.1–§5.4) · the Worker script (routing block, `authOk`, the write-only exceptions, metrics,
`deviceId`) · the viewer (`wireTextSizeToggle` + the decision block above it, the Sync-settings modal,
`MetricsCollector` flush/`flushSync`, `WorkerAPI`) · `tools/people.json` · the C4 topology note (§2
private-tier table) · the contractor-register proposal.

## §0 · Five measurements I made today, because three of them change the item

| # | measured | how |
|---|---|---|
| 1 | **The Worker contains zero occurrences of `textSize`.** M3's central claim reproduces. | `grep -c textSize worker/worker.js` → `0` |
| 2 | **There is exactly ONE credential in the whole system**, and it is a global secret with no identity, no estate and no scope: `authOk` compares the `X-Tate-Token` header to `env.SHARED_TOKEN` by string equality. It gates read of Mom's verbatim words, `/api/chat` spend, `promote`/`remove-species` (which write **public** canon), the admin clean route, and metrics read+write. | Worker § `authOk` + routing block |
| 3 | **Three routes sit ahead of the gate, not two** — `POST /api/feedback`, `POST /api/zone-audio` (write-only, capped, rate-limited, since the 07-15 loss) **and `/api/ambient`** (read-only, ungated 08-02, subordinate-to-Mom's-access). One KV binding (`OBSERVATIONS`), ~9 key prefixes; `wrangler.toml` has no `[env.*]`. | Worker routing block · `worker/wrangler.toml` |
| 4 | ⭐ **Her phone almost certainly holds that master token today.** `MetricsCollector.flush()` returns early unless `WorkerAPI.isConfigured()`, and `flushSync()` returns unless `cfg.workerUrl && cfg.token` — so **no metric can reach KV from an unpaired device**. `text_size_served` is a metrics-only event, and § M3 records it measured on her device 08-20 and 08-24. Only a paired device can have produced that. **Falsifier, cheap:** read the metrics batches for her `deviceId`; if those events arrived by any path other than `/api/metrics`, the deduction fails. |  viewer § `MetricsCollector` + § M3 |
| 5 | ⛔ **The two rooms the vault exists to serve do not exist as data.** No contractor-contacts file and no breaker/shut-off directory anywhere in the repo or `.private/`; the contractor register is a *proposal* whose own headline is *"do not build this"* and which is vehicle-shop-shaped, not household-shaped. What **does** exist is 254 service-record scans (manifest verified: `records: 254`) — the one room that needs an object store. | `ls .private/` · manifest count · contractor-register proposal |

**Why #4 matters more than it looks.** (a) The credential already on the make-or-break user's phone is
the **most powerful one in the system** — that is what `tenant-from-credential` has to *replace*, not
add to. (b) **Rotating `SHARED_TOKEN` silently blinds her telemetry** until it is re-pasted in person:
her denominator dies with no error surfacing anywhere. No rotation inside C6 without an in-person
re-paste in the same visit.

**Why #5 matters.** The door's own rule is *it ships with the room it guards, never before*
(data-model §7). So **the vault's blocker is not authentication — it is an authoring act of Paul's
that has not happened.** That reorders §6.

## §1 · M3 FIRST — where a per-PERSON setting lives before identity exists

The question is narrower than it looks. `apply(stored || DEFAULT_SIZE)` runs at first paint, from
localStorage, with no fetch. **Anything arriving over the network arrives too late**: the words render
small and then jump. So a *fetched* C-person setting is not a fix for M3 — it is a visible reflow, and
it puts an authorization round-trip in front of first paint, the exact violation the ux review names
as critical (F1a: *"render its glance to completion with ZERO authorization round-trips"*). That one
fact eliminates the obvious answer and leaves three.

| option | effort | reversibility | costs Mom | buys |
|---|---|---|---|---|
| **M3-a · served default is instance CONFIG** — the `DEFAULT_SIZE` constant becomes a declared per-instance value, set to `lg` for Fernwood | **low** (one constant + a config read) | **high** — one value | **nothing today.** Her device has `textSize` **stored**, so the default never reaches it; a *new* device with no stored key renders at her size on first paint, no fetch | **the falsifier, satisfied today** — before C5, before identity, before any door. And it preserves the instrumentation semantics already built: nothing is written on a default, so `{size:"lg", stored:false}` (served) stays distinguishable from `{size:"lg", stored:true}` (chosen) |
| **M3-b · Worker `person:` record keyed by C5's `personId`** | medium | high (additive KV) | ⛔ **harmful if read at load** (reflow + a round-trip before first paint); zero if read only at **binding** time | a real C-person carrier for the *next* device — but only as a **restore-at-binding backup**, which is exactly what the ux review's F3 posture already demands (*the device stays authoritative; the account is only a backup*). **Impossible before C5** — a `personId` does not exist, and inventing one to hold a text size is identity applied backwards (activation research §1.3) |
| **M3-c · extend the existing `sync.v1` pairing** | low | high | ⛔ **couples readable text to holding the master credential** | little. `sync.v1` is `{workerUrl, token}` — it is **not** a person record, it is the global secret (§0 #2/#4), and a new phone has none of it until Paul pastes it. Its real value is that it is **the device-binding act that already exists** |

⛔ **One dead end, named so it does not get built:** mirroring the setting server-side keyed on
`deviceId`. A new phone mints a new `deviceId`, so it restores nothing — and `tools/people.json` is
emphatic that a `deviceId` is a browser bucket, not a person.

### Recommendation — **M3-a now; M3-b later as restore-at-binding only; the new-phone journey written down as a person**

The third leg is not a cop-out — it is the activation research's own remedy (§5.1(b)): *a new-phone
journey is a person, exactly like recovery. Paul sets it up.* At n=1 that is the working mechanism,
and the doc should say so rather than pretend the UI self-heals.

⚠️ **What makes M3-a Paul's call, not an engineering call.** He *ruled on this exact constant* on
2026-08-19, walking back an A+ default with the reason recorded in the code — and **his reason was
"she is habituated to A," which the record now contradicts**: she is served `lg`, `stored:true`. So
this is a *different* act from the one he walked back: that one re-formatted every surface for a
person used to A, this one only decides what an **unconfigured** device shows, and hers is configured.
It still needs his word, because the block ends *"do not re-raise the A+ default without new evidence
about HER."* **That evidence is `{size:"lg", stored:true}` on her device.** Present it that way, not
as a bug fix.

**Falsifier (his, to accept or reject):** a browser profile that has never seen the app loads at
`lg` on first paint, with no fetch and no action by her — and her *existing* device is byte-identical
in behaviour to yesterday.

## §2 · THE ENTRY DOOR — for Paul, on Paul's device

**Scored against the six properties the brief names.** ✅ = satisfied by the mechanism; ⚙️ = satisfiable
but must be designed, not defaulted.

| | (a) HMAC token minted per grant | (b) **bearer token → KV grant map** | (c) Cloudflare Access | (d) magic link |
|---|---|---|---|---|
| tenant **from the credential** | ✅ estate is a signed claim | ✅ **strictly better** — the mapping is server-side, so there is nothing a client can tamper with | ⚠️ **partial** — Access proves an *identity*; you still write the identity→estate map yourself, so it replaces the credential, not the tenancy | ⚠️ same as (c) |
| crossed **once** | ✅ omit `exp` | ✅ KV row, no TTL | ❌ session duration is a **configured maximum**; long-lived is a setting you must remember | ❌ a new link per device |
| **never a silent expiry** | ⚙️ only if there is no `exp` **and** revocation is a deliberate act | ⚙️ **cheapest honest version** — revocation = deleting one row, which has an author who can write the copy | ❌ re-auth arrives as an **email OTP** — the email flow the doctrine rejects, arriving as the *routine* path | ❌ expiry is the mechanism |
| recovery **is a person** | ✅ Paul re-mints | ✅ Paul re-issues | ❌ IdP/OTP | ❌ email by construction |
| **her surface untouched** | ✅ `entry:off` → no gate before paint | ✅ same | ❌❌ **gates at the edge, in front of everything** — F1's named violation implemented at the network layer, where the app cannot opt out per person. It would also gate `/api/ambient` and the two write-only POSTs, killing the 07-16 capture doctrine | ✅ if late-presented |
| **instrumentation** | ⚠️ see below | ⚠️ see below | ❌ **a rejection at the edge never reaches the app**, so `door_failed` cannot be recorded — lockout invisible *by construction* | ⚠️ see below |
| effort · reversibility | medium · high | **low-medium · high** (additive; delete the branch and the ungated POSTs still work) | low code · **low reversibility** (an origin-level dependency) | medium · medium (new sender, new secret, deliverability) |

⛔ **(d) is ruled out on doctrine, not on cost:** email has no job (recovery is a person, notification
is anti-doctrine), and a stored address is the channel that was deliberately closed.
⛔ **(c) should be ruled out explicitly rather than by silence** — it is the option a competent
engineer reaches for first, it is genuinely *less code*, and free to 50 users. Its cost is invisible
until it is live, and then it is her glance behind a login.

### ⭐ The instrumentation finding — it decides whether the door can ship at all

The rule is absolute: *the door ships with instrumentation or it does not ship* — `door_reached`,
`door_opened`, `door_failed`, plus sessions-on-a-bound-device-with-zero-door-events (activation
research §5.3). **But every metric today travels `/api/metrics`, which is behind the gate** (§0
#2/#4). So a person who is *locked out* — the exact case the instrumentation exists to make visible —
cannot report being locked out. The failure the record must distinguish is the one the record cannot
see.

**The fix has a precedent in this repo:** door events ride a **write-only, no-token, size-capped,
rate-limited** path — the doctrine of `POST /api/feedback` and `POST /api/zone-audio` (new key prefix,
`GET` still gated). ~15 lines, modelled on code that already survived a real loss.

### Recommendation — **(b), an opaque bearer token mapped to a grant row in KV, with (a)'s discipline about `exp`; instrumentation on the ungated write-only path, shipped FIRST**

**And it answers the data-model plan's falsifier 2 directly** — *if tenant-from-credential proves
impractical on Workers + KV without a real user store, R3's isolation is aspirational.* The honest
answer: **a credential→grant map in KV *is* the user store**, roughly twenty rows and one `get` per
gated request. Tenant-from-credential is not impractical here; it costs one KV read. **The falsifier
does not fire.**

⚠️ **Two disciplines to write into the plan or they will be lost:**
1. **No `exp` claim anywhere.** Expiry becomes an *act with an author* (delete a row) instead of a
   timer — the only way "never a silent expiry" is enforced rather than hoped for, since silent
   expiry is the default behaviour of every session system.
2. **Name it differently from `SHARED_TOKEN` on day one** — different header, different storage key.
   It looks exactly like `sync.v1` and *will* be conflated with it, and the two have opposite scopes:
   one is per-grant, one is the master key.

## §3 · THE VAULT

**Recommendation: a TEXT room, and the smallest one is not the obvious one.** The 254 receipt scans
are the *worst* first room — they need an object store (C4's topology note prices that high-effort,
R7-only, ⛔ *do not fold it into C4*) plus a lookup index. Contacts and the breaker directory are the
*best* rooms — the data-model plan names them as the documents most needed in the field — **and per §0
#5 they do not exist as data.** So:

- **The vault's critical path runs through Paul's keyboard, not the Worker.** Author the contacts /
  shut-off room as a small text file first; the door follows it. Until it exists, *ships with the room
  it guards* makes the vault unbuildable — a *finding*, not a delay.
- **Retrieval shape — the one thing that must not be foreclosed.** Ship `index` + `get one document
  by id`, from the existing KV (a text room needs no R2). ⛔ **No "return the whole room" endpoint.**
  A bulk read is exactly what the Guru would later inline, and the digest is already ~127K tokens /
  62–70% of the window. Rung 3's deterministic lookup needs a door shaped like a lookup; a dump
  forecloses it while appearing to enable it.

### ⭐ `vault:on` with `entry:off` — who is "you" to a vault nobody entered?

This is the sharpest question in the brief, and the default in the product engine (`entry:off,
vault:on`, agent-proposed) is not implementable until it is answered. Two readings:

1. ✅ **`entry:off` means the credential is not DEMANDED AT THE THRESHOLD — never that no credential
   exists.** The same per-grant credential is requested at the vault boundary; on success the app now
   knows who is asking. `vault:on` + `entry:off` is therefore **deferred entry**, and
   tenant-from-credential holds unchanged because the estate is derived from the credential either
   way. It is what the ux review's *door at the boundary of the room it guards* already implies, and
   what makes a wrong credential cost **only** the thing behind the door.
2. ⛔ **A vault-only shared word with no identity.** Rejected: it grants access without knowing who,
   so per-grant blast radius (data-model §6 — the grant list is what stops Bob's contributor reaching
   Paul's receipts) has nothing to check, and Bob would share a secret with his own contributor.

**Consequence worth stating in the plan:** under reading 1, **attribution begins at the vault, not at
the door.** Records written before a vault has ever been opened stay unattributed — `null`, never
absent — so identity-not-applied-backwards holds by construction rather than by discipline.

## §4 · THE SELECTOR IS OUT — the one constraint that keeps it possible

Single grant → no selector (a picker with one item is friction with no benefit). The constraint:

> ⛔ **No estate identifier may appear in any request the client composes** — not a query param, not a
> body field, not hardcoded, not unused. The Worker derives the estate from the credential and must
> **ignore** any estate id it receives.

**Why this and nothing else.** A property id in a URL is a client's claim about itself. If v1 ships
with `?estate=fernwood` anywhere — even inert, even as a convenience during C5's prefix work — the
selector's later arrival turns it live, and rule 3 breaks *retroactively*, at the moment a second
tenant exists and nobody is looking. It is also the one constraint **testable with `grep` today**,
which is why it is the right one to write down.

## §5 · WHAT C4's QA ENVIRONMENT LETS AN AGENT TEST — and what still needs Paul's device

Given C4's ruling (Cloudflare Pages as the QA origin, `[env.qa]` with **its own KV namespace**,
`WORKER_BASE` derived from the hostname), an agent can test **without touching her data**:

1. ⭐ **F1 as a saved Playwright regression** — load the QA origin with **no credential**, intercept
   the network, assert **zero requests to gated routes before the first-paint marker**, and assert
   masthead + jump strip + weather card render. The highest-value test in the item, because F1 is the
   finding most likely to be violated by a reasonable-sounding implementation.
2. **Tenant isolation = R3's falsifier as a harness** — two QA credentials, two estate ids; each
   reads and writes only its own prefix, and a cross-read returns not-found.
3. **The no-`exp` / revocation design** — an old token still opens; a deleted grant row closes **with
   the designed copy**, not a bare 401.
4. **The 07-16 capture doctrine** — with no credential present, both write-only POSTs still land.
5. **Lockout visibility** — drive a wrong credential, then read QA KV for `door_failed`.
6. **M3's falsifier** — a fresh browser profile serves `lg` with `stored:false`.

⚠️ **The harness must assert it loaded the right document** — a 404 page renders perfectly and scores
green, which is how a release gate in this portfolio ended up scoring GitHub's 404 page. Assert on a
marker only the real viewer emits, and throw when it is absent.

**Still needs Paul's device / Paul in person:** her credential word (a conversation, not a form) · the
binding act on **her** phone · a `SHARED_TOKEN` re-paste if it is ever rotated (§0 #4) ·
`wrangler secret put` in a real TTY — ⚠️ never via `!`, which uploads an **empty** secret and prints
success · and whether her *real* phone restores at `lg` (Safari ITP eviction is device-real).

## §6 · ORDER, AND WHAT SHIPS INDEPENDENTLY

| # | step | gated on | ships alone? |
|---|---|---|---|
| 0 | C4's QA env + C5's KV prefix | dependency, not this item | — |
| 1 | **M3-a — served default as instance config** | **Paul's word on the constant he ruled 08-19** | ✅ **yes, today.** No credential, no door, no seat review |
| 2 | **Door instrumentation on the ungated write-only path** | nothing | ✅ **yes, and BEFORE the door** — it records a truthful baseline (`door_reached = 0` while no door exists), which is the denominator the seat's rule needs |
| 3 | The first vault room, authored as data | **Paul** (§0 #5) | ✅ yes — a contacts file is useful laptop-local with no door at all |
| 4 | Credential→grant map + verify helper, Paul's grant only, `entry:off` elsewhere | **privacy seat** + C5's ids | no |
| 5 | Vault retrieval endpoint over room #3 | step 4 | no |
| 6 | C-person mirror, restore-at-binding | C5's `personId` | no |

⭐ **Steps 1–3 are the whole of C6 that is unblocked**, and none needs the privacy seat, a credential,
or Mom. That is the concrete meaning of *build the door for Paul first*: **the first three things are
not a door at all** — they retire M3, install the instrument that makes the door's own failure
visible, and create the room the door is required to guard.

## §7 · WHAT I DID NOT DECIDE — Paul's calls

1. **Her credential word.** Asked in conversation, never typed; a word she would tell Paul, never
   *"a password"* (which harvests her bank credential).
2. **The entry default.** `entry: off, vault: on` remains **agent-proposed, not ruled**.
3. **The first room in the vault.** My input: a text room, and it has to be authored before the door.
4. **Whether the privacy/security seat is stood up as an agent or run as a checklist.** Either
   satisfies *"reviews before build"*; only the first accrues across the portfolio.
5. ⭐ **Added by this evaluation: whether `DEFAULT_SIZE` may change at all.** He ruled that constant on
   2026-08-19 with a written reason, and the reason no longer matches the record. That is his to
   re-rule, not mine to route around.

## §8 · OPEN QUESTIONS

1. Does her phone hold `sync.v1` — the master token — or did `text_size_served` reach KV some other
   way? (§0 #4 says it must be paired; one read of her `deviceId`'s metrics batches settles it.)
2. Who set `textSize=lg` on her device, and when — a shared-phone episode before 07-28, or Paul on her
   phone? Mechanically irrelevant; decisive for how M3-a is explained to her.
3. May the C-person mirror *write* a stored preference on a new device at binding time, or only inform
   what Paul sets by hand? (ux F3 says device-authoritative; a write makes the account the source.)
4. Does `entry:off` mean the app never asks *and never stores* a credential for her, or that one
   exists unasked until a vault boundary is crossed? (§3 reading 1 assumes the latter.)
5. Should door instrumentation be exempt from `excludeFromEngagement`, so Paul test-driving his own
   door does not read as a person hitting it?
6. Does the vault's first room live in `.private/` (laptop-local, invisible to the Worker) or in KV
   from the start — and if KV, has that made the private-tier store decision C4 held open?
7. Is `SHARED_TOKEN` in scope for C6 at all, or unchanged until a visit where it can be re-pasted on
   her phone in the same sitting?

---

> ## 🚪 PAUL'S GATE
> **Three asks, smallest first.**
> **① §1 — may `DEFAULT_SIZE` become a declared per-instance value set to `lg`?** The evidence that
> changes your 08-19 reason is `text_size_served = {size:"lg", stored:true}` on her device. Yes / no.
> **② §6 — do steps 1–3 proceed as the whole of C6 for now**, with steps 4–6 held for the privacy
> seat and C5? Yes / no.
> **③ §7 — the four calls that are yours and that no agent should make**: her credential word, the
> entry default, the first room, and how the privacy seat is stood up.
> ⛔ Nothing above is built, and step 4 does not open until the seat has reviewed.
