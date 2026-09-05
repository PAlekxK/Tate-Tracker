---
type: path-evaluation
project: fernwood / Tate-Tracker
subject: the account credential — what she presents on every later visit, and what changes server-side
date: 2026-09-05
seat: engineering-partner
mode: path-evaluation
scope: MECHANISM ONLY. Not the fields she sees (ux-expert), not whether "an account" fits her (user-researcher).
settled_and_not_relitigated:
  - "[paul-ruled 2026-09-04] she has to log in, create an account, and then is presented with the options"
  - "[paul-ruled 2026-09-05] go through the motions on everything; Mom sets up her own account"
code_context_confidence: high (worker.js, grant-mint.py, grants.json, wrangler.toml all read 2026-09-05)
user_context_confidence: medium (journey + activation artifacts read; nobody has been asked anything about an onboarding flow — the artifacts say so themselves)
---

# The account credential — the mechanism, the migration, the failure modes

---

## 0 · WHAT I VERIFIED, AND THREE THINGS THAT CONTRADICT THE BRIEF

The brief asked me to verify rather than trust. Here is what the code actually says.

**✅ CONFIRMED — the hash IS the key.** `worker.js:501`:

```js
const raw = await env.OBSERVATIONS.get(keyFor(env, "grant", await sha256Hex(presented)));
```

`keyFor(env, "grant", h)` → `est-3c9f1a:grant:<h>`. You must hash before you know which row you are
looking at, so no per-row salt is reachable. The brief's reading is exactly right, and the privacy
seat's finding 1 (`.engineering/2026-09-03-c6-privacy-seat-review.md:69`) states it correctly.

**✅ CONFIRMED — SHA-256 is the only hashing in the credential path** (`sha256Hex`, `worker.js:1950`,
one `crypto.subtle.digest` call). No KDF anywhere. No rate limit on any gated route — the Worker has
exactly two buckets (`feedbackRateLimitOk`, `doorRateLimitOk`) and both sit on ungated POSTs.

**✅ CONFIRMED — no send capability.** No fetch to any mail provider anywhere in `worker.js`. "Forgot
password" cannot email anyone. Recovery is Paul, full stop.

### ⚠️ Contradiction 1 — **there is no migration, because no real credential exists.**

The brief asks "what migration the existing grant rows need." I read the private register
(`../fernwood-private/grants.json`). Five rows:

| personId | estate | credential | entry / vault |
|---|---|---|---|
| `p-b91e4d` | `est-3c9f1a` (Fernwood) | **`null`** | false / false |
| `p-7f3a2c` | `est-3c9f1a` (Fernwood) | **`null`** | false / false |
| `p-qa-synth-1` | `est-qa0001` | hash | true / false |
| `p-lab-synth-1` | `est-lab0001` | hash | true / false |
| `p-7f3a2c` | `est-lab0001` | hash | true / false |

**Every row that carries a credential hash is a QA or lab fixture, or Paul's own lab row.** Both real
Fernwood rows have `credential: null`, `entry: false`, `vault: false`. And `est-e6696a` — the `home`
environment, the one where "a person logs in and keeps their places" — has **zero rows**.

> ⭐ **This is the single most useful fact in this evaluation.** There is nothing to migrate. The
> credential design is a **greenfield decision on the `home` deployment**, not a retrofit under a
> live credential. That removes the usual reason to accept a bad shape, and it means the cost
> difference between the cheap option and the right one is *hours*, not a migration.

⚠️ **One cheap verification before you build on this** (the register is the writer's record, not the
store): `npx wrangler kv key list --namespace-id 100f2b95e4be4c088a0000f917cf987b --prefix "est-3c9f1a:grant:"`
should return `[]`. Same for `est-e6696a` in the home namespace (`79464451e3a7497594b17d8c60c7254d`).
A register-vs-store disagreement is exactly the drift class this repo already guards elsewhere.

### ⚠️ Contradiction 2 — **`tateTracker.grant.v1` is not built.**

The onboarding journey (§2 row 4) calls it "rostered." It is rostered **in the C6 plan** (steps 4b/6b).
`grep -rn "grant\.v1" viewer.html` → **zero hits**. The client has never sent `X-Grant`. So the client
side of this is not "add a login screen to a working credential path" — it is *the first time the app
presents a grant at all*, plus the `authHeaders()` consolidation the seat's finding 8 asks for
(`grep -c '"X-Tate-Token"' viewer.html` must fall to **1**), plus a new row in
`tools/check-storage-keys.py`.

### ⚠️ Contradiction 3 — **the hardest problem here is not hashing. It is that one credential must
resolve to N grants, and `grantFor()` is built to resolve exactly one.**

`.plans/2026-09-04-roles-and-access-REQUIREMENT.md` (Paul-stated 2026-09-04) rules that after login
**a chooser is rendered from her grant rows** — Angel sees *view Fernwood* + *add a place*; Mom sees
*add a place*. But `grantFor()` returns a single row and asserts `row.estateId === env.ESTATE_ID`
(`worker.js:504`), and `ESTATE_ID` is one string per deployment.

> **Today: credential → one grant → one estate. Ruled: credential → one person → many grants.**
> That is a shape change in the KV layout **regardless of which hash you pick.** Any option that
> leaves the credential welded to a single grant row has to be redone when the chooser lands.

This is what actually decides the recommendation, and I don't think it has been named anywhere yet.

---

## 1 · THE OPTIONS, PRICED

### Platform facts I checked rather than assumed

| fact | value | source |
|---|---|---|
| Workers SubtleCrypto KDFs | **PBKDF2 only** (`deriveBits`/`deriveKey`). No scrypt, bcrypt, or Argon2 | [Workers Web Crypto docs](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/) |
| CPU budget per request | Paid plan: **30 s default**, up to 5 min via `limits.cpu_ms`. (Free is 10 ms — you moved to Workers Paid 2026-09-04, which is what makes a KDF possible at all) | [Workers limits](https://developers.cloudflare.com/workers/platform/limits/) |
| PBKDF2-SHA256 cost, **measured** | 100k → 12.9 ms · 210k → 25.0 ms · **600k → 71.2 ms** · 1M → 117.9 ms (Node 24 WebCrypto, arm64, mean of 3). workerd uses the same BoringSSL primitive; budget **2–4× slower** on a shared Workers core, so 600k ≈ **150–300 ms** | measured locally 2026-09-05 |
| Defensible iteration count | **600,000** for PBKDF2-HMAC-SHA256 | [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) |
| KV consistency | writes take **up to 60 s** to propagate; **negative lookups are cached too**; read-your-own-write "is not guaranteed" even at the write location | [How KV works](https://developers.cloudflare.com/kv/concepts/how-kv-works/) |
| Native rate limiting | `[[ratelimits]]` binding exists; **period must be 10 or 60 seconds**, and limits are **per Cloudflare location**, not global | [Rate limiting binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/) |

So: **PBKDF2 at 600k iterations is comfortably affordable** (0.3 s of a 30 s budget), and it is the
*only* KDF available without a WASM build. bcrypt/scrypt/Argon2 would each mean shipping a WASM blob
into a Worker that currently has **no `package.json` and no dependency tree at all** — I checked; there
is none, at the repo root or in `worker/`. That is a bigger architectural change than the credential.

---

### Option A — password hashed with per-person salt, filed **by username**, on the grant row

Replace "the hash is the key" with "the username is the key." Row at `<estate>:cred:<sha256(lower(username))>`
holds `{personId, salt, hash, iterations, algo}`. Login reads the row by username, derives, compares
in constant time.

- **worker.js:** new `POST /api/session`; a `verifyPassword()` helper (~40 lines); router-order change
  so the login route sits *before* the gate; rate limit before the KDF.
- **migration:** none (§0). `grant-mint.py` gains `--username` / `set-password`.
- **breaks:** nothing today. **But** it still ties one credential to one grant row, so it gets redone
  when the chooser lands (§0, contradiction 3).
- **effort:** ~1 focused session on the Worker + tool.

### Option B — password reusing today's hash-as-key, unsalted

`grantFor()` is literally unchanged; the "presented" string is just a password instead of a token.
3a's "hash of what is presented" stays true.

- **worker.js:** **zero lines.** It already works — mint a grant whose token *is* her password.
- **migration:** none.
- **breaks:** the security posture, comprehensively. See §3. Also the chooser, same as A.
- **effort:** ~0. This is the option that is already sitting there, which is exactly why it needs to be
  named and refused rather than left available.

### Option C — device-local unlock (a word) over the already-stored strong token

The seat's named successor. The device holds the 256-bit minted token **encrypted**; WebCrypto derives
an AES-GCM key from her word in the browser; the Worker never sees the word. `grantFor()` untouched.

- **worker.js:** **zero lines.**
- **client:** ~100 lines (PBKDF2 → AES-GCM wrap/unwrap around `tateTracker.grant.v1`).
- **breaks:** **the new phone.** A cleared or replaced device has no ciphertext, so the word restores
  nothing. The seat said this plainly and it is the honest tell: the word's job here is *comfort*, not
  access.
- **effort:** ~half a session.

### ⭐ Option D — **separate the account row from the grant rows; login trades the password for the
existing opaque token**

This is Option A done in the shape the chooser ruling already requires. Two stores, not one:

```
account:<sha256(lower(username))>   →  { personId, salt, hash, iterations, algo,
                                         createdAt, failedSince, failedCount }
<estate>:grant:<sha256(token)>      →  UNCHANGED. Exactly what grant-mint writes today.
```

The flow:

1. `POST /api/account` — she picks a username + a word. Worker mints `secrets.token_urlsafe(32)`-equivalent
   (`crypto.getRandomValues`), writes the grant row **and** the account row, and **returns the token in
   the response body** (it never reads it back — see §3, the KV negative-cache trap).
2. `POST /api/session` — username + word in, PBKDF2 verify, **the opaque token out**.
3. Every later request: `X-Grant: <token>`. **`grantFor()` is not touched. Not one line.**

**Why this is the shape, not just a variant:**

- **The password never becomes a KV key.** The seat's Q5 objection (`no per-row salt is possible`) is
  answered structurally rather than argued around — the salt lives in the account row's *value*, which
  is reachable because the *username* is the lookup.
- **3a's invariant survives verbatim.** "The hash of what is presented" — what is presented on every
  gated request is still the opaque token. The vault, the dual-accept block, `hostAgrees`, the
  byte-identical 404, the `door_failed` timing-oracle handling: all unchanged and already QA-proven.
- **It absorbs the chooser.** `POST /api/session` returns a *list* — `[{estateId, token, relationship,
  capability}]` — length 1 today, length 2 the day Angel or the condo lands. The client's chooser is
  written once. When the instance↔deployment weld comes out, the account store is already person-scoped
  and doesn't move.
- **`grant-mint.py` stays the only writer of grant rows** — the Worker writes account rows and calls
  the same mint shape for grants, and the G1/G2 consent gates keep living at the mint.

- **worker.js:** ~250–300 lines — two routes, `derivePbkdf2()`, `timingSafeEqual()`, a rate-limit call,
  a failure record into `door:`, and one new numbered step in the router order.
- **migration:** none (§0). `grant-mint.py` gains an `account` writer + `--rotate-password`.
- **breaks:** nothing shipped. The CORS change in §3 item 5 is the one real edit to existing behaviour.
- **effort:** Worker + tool ≈ 1 focused session · client login surface ≈ 1 more (that surface is
  ux-expert's to shape) · QA/lab verification ≈ half.

### Option E — passkeys / WebAuthn — see §4. **Viable on the current host, and I still don't recommend it as the credential.**

---

## 2 · RECOMMENDATION

> ## ⭐ **Option D.** The password is verified at a login route against a **username-keyed account row
> with a per-person salt and PBKDF2-SHA256 at 600,000 iterations**, and what it buys is the opaque
> token the app already knows how to present.

**The trade-off, named.** D costs you **one new concept** — an account row that is not a grant row —
and about a session of work over Option B's zero. What that concept buys is three things B cannot have
at any price: a **salt** (because the lookup key is the username, not the secret), a **work factor**
(because the KDF runs once at login, not on every gated request), and a **credential that is one
person's rather than one estate's** (because the chooser ruling needs that and the current shape
cannot give it). You are paying a concept to avoid a rewrite you have already been told is coming.

**Against Option A** — A is D with the two stores fused. It costs the same to build and has to be
unfused later. There is no reason to pick it.

**Against Option C** — C is a good mechanism solving the wrong job. §5.1 of the activation research is
emphatic that the new phone is *already broken today*, and it is the strongest practical argument for
an account existing at all. C does not help there. Keep it in the drawer as an optional second layer
if Paul ever wants the vault to need a second touch; do not make it the account.

**Against Option B** — B is genuinely tempting: zero code, and it satisfies the letter of the ruling
tonight. Refuse it for the reason in §3 that has nothing to do with the journal: an unsalted fast hash
of a memorable word means a KV leak hands an attacker **a password she may use somewhere that matters
more than a garden journal.** The activation research already forbids harvesting a credential she uses
elsewhere; storing one badly is the same harm arriving through the back door.

**And the honest calibration.** At two real people, none of this is protecting a high-value target. The
work factor is not there to defeat a determined adversary — it is there so that (a) a leak of the KV
namespace does not become a leak of *her*, and (b) the design does not have to be re-argued when this
engine holds a second household's data, which the record says it will. That is proportionate. What
would be over-engineering: session expiry, refresh tokens, MFA, a Durable Object, an audit log beyond
the `door:` records that already exist. None of those are in the recommendation.

### The build order I would take

1. `derivePbkdf2()` + `timingSafeEqual()` + the account-row schema, with a `--selftest` in the tool
   the way `grant-mint.py` already does 18/18. **Nothing deployed.**
2. `POST /api/account` + `POST /api/session` on **lab** (`est-lab0001`) — the environment that exists
   precisely so no real person is served from it. Prove: create → login → `X-Grant` → `whoami`.
3. Rate limiting + the `door_failed` record for a wrong password, proven by driving it wrong.
4. The CORS narrowing (§3 item 5), proven by a cross-origin `fetch` from a scratch page.
5. Only then the client surface, on QA, at ux-expert's shape.
6. A Playwright flow saved for: create → reload → login → wrong password → right password. That is the
   one flow load-bearing enough to merit saved coverage; it is also the only place a regression would
   be invisible to Paul.

---

## 3 · THE FAILURE MODES

### 1. Online guessing, and how it is rate-limited

**Today: nothing.** A failed `authOk` is a bare 401; the two existing buckets are on ungated POSTs
(seat finding 11, verified). Against 256 bits that is fine. Against a word it is the whole game.

**Under D, two brakes, and the ordering matters:**

- **Burst** — the native `[[ratelimits]]` binding, keyed by **username** (not IP; an IP rotates and a
  password attack is per-account), `limit = 5, period = 60`. ⚠️ Per-Cloudflare-location, so a
  distributed attacker gets 5 × N colos. Say that out loud rather than believing the number.
- **Drip** — `failedCount` / `failedSince` on the account row itself. After ~10 failures in an hour the
  route refuses regardless of colo. KV is eventually consistent so this leaks a little; at n=2 that is
  the right amount of engineering.

> ⭐ **Both brakes must run BEFORE the PBKDF2 derivation, not after.** Otherwise every guess costs you
> 150–300 ms of billed CPU, and a guessing attack becomes a *billing* attack against a Worker that just
> started paying for CPU-ms. This is the non-obvious one and it is a one-line ordering decision.

**And the response must be identical for unknown-username and wrong-password** — same status, same
body, and **the KDF must run either way** (derive against a fixed dummy salt when the row is missing).
Skip that and the response *time* tells an attacker which usernames exist. This is the same discipline
the router already applies with its byte-identical 404 for an unknown grant; it just has to reach one
more route.

### 2. What a stolen KV dump yields

| option | what the dump contains | what it costs to break |
|---|---|---|
| **B** (unsalted, hash-as-key) | ⛔ `sha256(password)` **as the key name** | Reversed against a wordlist in **well under a second**, and unlike a value, a key name is exposed by `wrangler kv key list` — a listing permission is enough. Then it is presented directly. |
| **A / D** | `{salt, sha256-pbkdf2(password, salt, 600k)}` in the **value**; key name leaks only the **username** | Offline, per-account, no precomputation. A 4-word passphrase: not happening. A single memorable word: still falls to a GPU eventually — the KDF buys **time and per-target cost, not immunity**. |
| **C** | `sha256(256-bit token)` | Nothing. Best of the four. |
| **E** (passkey) | a **public** key | Nothing. Also best. |

> The honest framing for Paul: at n=2 the thing worth protecting in a KV dump is not the journal — it is
> **her**. A/D means a leak does not hand anyone a password she might reuse. B means it does.

### 3. ⚠️ The new-phone path — and the KV negative-cache trap that will bite on day one

**Under D she types her username and her word on the new phone and she is in.** That is the whole reason
an account is worth the concept, and it is the only option here (with E) that fixes the journey
`activation-journeys §5.1` calls *already broken today*.

> ⛔ **But note what it does NOT fix, and the research is emphatic about it:** the loudest failure on
> her new phone is *"the words got smaller,"* not a login prompt. `tateTracker.textSize` is device-local
> and an account does not restore it. If C6 Q1 has shipped (A+ is the one base size, no toggle), that is
> already solved by construction — but that ruling is measured as **not yet shipped** (C4 in the
> onboarding journey: three positions live in one repo). **Ship the A+ base before the account layer, or
> the new phone still fails at the thing that hurts most and the login will get blamed for it.**

**And the trap.** KV caches **negative lookups**, and read-your-own-write is explicitly not guaranteed.
So this sequence is a real bug:

```
POST /api/account  → Worker PUTs the grant row → 200
client immediately GETs /api/grant/whoami with the new token
→ KV read may miss for up to 60 s → the router's 404 → "not-found"
→ she just made an account and the app says it doesn't exist
```

**The fix is free and it is a design rule, not a retry loop:** the creation response **carries** the
token and the resolved grant, because the Worker already holds both — it just wrote them. **Never read
back a key you just wrote to confirm it.** Same rule applies to any "is this username taken?" check: the
miss you cache is the miss you will still be serving a minute later.

### 4. She forgets it, and there is no email

**Recovery is Paul. There is no second answer and the design should stop implying there might be.**

- **The mechanism already exists**: `grant-mint.py --rotate` (`tools/grant-mint.py:230` deletes the old
  hash row) — extend it with `--rotate-password` to rewrite the account row's salt+hash. Recovery is a
  terminal command Paul runs, in person or over the phone, in about ten seconds.
- **The door's footer is "Ask Paul," never "Forgot password?"** — already ruled (ux F2), and it is now
  load-bearing rather than stylistic: a "Forgot password?" link with nothing behind it is a promise the
  system cannot keep.
- ⛔ **The failure that actually costs you is §5.3 path 3b: she does nothing, and nothing in the record
  distinguishes "locked out" from "didn't want it."** So a failed login **must** write a `door_failed`
  record with a reason — the machinery is already there (`storeDoorRecord`, `ctx.waitUntil`, the
  timing-oracle handling) and this is one call site. **Instrument it in the same commit as the route, or
  the lockout is invisible and you will find out weeks later.**
- **Say the consequence plainly:** because Paul can reset her password, Paul can read everything behind
  it. The threat model here is *a stranger with the URL*, not *Paul*. Nothing in this design pretends
  otherwise, and any copy that implies privacy-from-Paul would be false.

### 5. ⚠️ `Access-Control-Allow-Origin: "*"` on a route that returns a credential

`CORS_HEADERS` sets `"Access-Control-Allow-Origin": "*"` (`worker.js:319` region). The privacy seat
explicitly ruled **do not tighten it** — correctly, because CORS restrains browsers not clients, and `*`
is what keeps the ungated capture path working from any device. That ruling was made when **no route
returned a credential.**

`POST /api/session` returns one. With `ACAO: *`, **any website Mom visits can POST guesses to the login
route from her browser and read the response** — using her IP, from many origins, as a guessing oracle.

**Concrete change, scoped to the two new routes only:** echo the request's `Origin` when it is in
`FAMILY_HOSTS`, omit the ACAO header otherwise, and send `Vary: Origin`. Leave `*` exactly as it is on
every other route — the seat's reasoning there still holds. This is not a reversal of the seat; it is
the one route its premise does not cover.

### 6. The multi-estate collision (from §0)

`grantFor()` asserts `row.estateId === env.ESTATE_ID`. **Keep that assertion** — it is privacy-seat
condition ① and it is the check that stops two estates appearing in one request. Under D you do not
need to weaken it: the account row is deployment-scoped, and the login route returns the grants *it can
resolve in this deployment's binding*. **Shape the response as a list from day one** so the chooser
lands without a protocol change, and leave the instance↔deployment weld to its own evaluation.

### 7. Where the account row lives, and one thing to decide

`keyFor()` prefixes **every** key with the estate. An account is above estates by construction (that is
the whole point of the chooser). So `account:<h>` is a **new top-level key kind**, sibling to the estate
prefix rather than under it — deliberately, with the reasoning written at the site of the code the way
this codebase writes everything else. ⚠️ It is the first key that does not carry an estate; the C5
prefix doctrine should gain an explicit sentence saying accounts are person-scoped and why, or the next
reader will read it as a bug and "fix" it.

---

## 4 · ⚠️ PASSKEYS / WEBAUTHN — CHECKED PROPERLY, AND THE ANSWER IS "TECHNICALLY YES, STILL NO"

The brief was right that this deserved a real check rather than a dismissal, because typed fields are
the named risk and a passkey removes them all.

**What I verified:**

- ✅ **The RP ID works on your current host.** I expected this to be the blocker and it is not.
  `pages.dev` and `github.io` are on the Public Suffix List, so you cannot scope an RP ID to the shared
  parent — but you *can* use the full hostname. [web.dev's RP ID article](https://web.dev/articles/webauthn-rp-id)
  gives exactly your case: for `https://myapp.pages.dev` the valid RP ID is `myapp.pages.dev`. So
  `fernwood-home.pages.dev` is legal.
- ✅ **iOS Safari supports passkeys** and syncs them through iCloud Keychain, with recovery via
  iCloud Security Code / recovery contact / Recovery Key — genuinely no email required
  ([Apple](https://support.apple.com/guide/security/secure-icloud-keychain-recovery-secdeb202947/web)).
- ✅ **The new-phone story is excellent** where it applies: same Apple ID → the passkey is simply there,
  no typing, no Paul. It would also have covered the 2026-07-15 MacBook incident.
- ✅ **Server-side verification is possible** on Workers — SubtleCrypto verifies ECDSA P-256.

**Why I still would not make it the credential:**

1. ⛔ **It contradicts the ruling, twice made.** Paul's model is a remembered username and a typed
   password; last night's *"go through the motions on everything"* reinforced it. A passkey is a system
   sheet and a Face ID scan — a different act. Not mine to relitigate.
2. ⛔ **The RP ID is cryptographically bound to the hostname, and this project moves hostnames.** The
   record has `production` as *"a ROLE that transfers"*, a `home` env that becomes production later,
   Tate Commons wanting a Tate subdomain, and an engine designed to be re-instanced per household. **The
   day you move off `fernwood-home.pages.dev`, every passkey is dead and every person must re-enrol** —
   with no email to tell them so. That is a bad interaction with this specific project's trajectory.
3. ⛔ **Verification is the largest new code surface on the table.** Doing it by hand means CBOR
   decoding, COSE key parsing, clientDataJSON validation, challenge storage, and signature-counter
   handling — several hundred lines of fiddly crypto you cannot eyeball for correctness. Doing it with
   `@simplewebauthn/server` means introducing the **first `package.json` and dependency tree this Worker
   has ever had** (verified: none exists at the repo root or in `worker/`). Both are bigger changes than
   the credential itself.
4. ⚠️ **Recovery is worse, not better, in the case that actually happens.** iCloud Keychain covers
   *her Apple devices*. It does not cover a borrowed device, an Android, a different Apple ID, or a
   Keychain she has turned off — and in every one of those, the fallback is Paul, whom you need anyway.
   A password works on any device on earth with no platform dependency.

**⭐ Where it does belong.** Once D exists, a passkey is a clean **optional add** later — enrolled from
a settings screen *after* the password exists, as a faster way in on her own phone, with the password as
the fallback that keeps the RP-ID-move survivable. That ordering costs nothing now and keeps the door
open. **Note that ordering; do not build it.**

---

## 5 · WHAT I DID NOT EVALUATE, AND WHY

| not evaluated | why |
|---|---|
| **The fields, the labels, the error states, the moment she gets it wrong** | `ux-expert` is on this in parallel. Where my mechanism forces a surface (identical response for unknown-username vs wrong-password; "Ask Paul" instead of "Forgot password?"), I named the constraint and stopped. |
| **Whether "create an account" fits this person; what recovery means socially** | `user-researcher`'s lane, running in parallel. |
| **What the username should BE** | ⚠️ It becomes a KV key name, and key names are exposed by a listing. Given ⛔ *"her name does not appear in tracked files,"* the choice has a privacy dimension I am flagging to the researcher/privacy seats rather than deciding. |
| **The instance↔deployment weld** (many estates per namespace, widened blast radius, per-prefix backup) | Named as a Paul decision in the roles requirement and it is a larger path-eval of its own. D is *shaped* to survive it (list response, person-scoped account rows); it does not depend on it. |
| **Cloudflare Access in front of the `home` origin** | A different layer entirely (network gate vs. application credential). QA already sits behind it; whether `home` should is a separate call. |
| **Session expiry, refresh, rotation, MFA, audit logging** | ux F2 ruled no clock is compared and no TTL exists; adding any of it re-opens a settled decision and is over-engineering at n=2. |
| **Formal threat modelling / pentest** | Out of scope for this seat until the parked privacy/security reviewer is stood up. The 2026-09-03 privacy seat is the standing input and I built on it rather than re-running it. |
| **A workerd-native PBKDF2 benchmark** | Measured on Node's WebCrypto (same underlying primitive) and applied a 2–4× margin. If Paul wants the real number: a five-line `wrangler dev` handler that times one `deriveBits`. Not load-bearing — the budget is 30 s and the cost is sub-second. |

---

## 6 · PRINCIPLES TO PROPOSE (not written — Paul confirms first)

**① Never read back a key you just wrote (scope: cross-project).** KV caches negative lookups and does
not guarantee read-your-own-write. A create-then-confirm round trip is a silent up-to-60-second lie. The
writer already holds the value: return it. This generalises past KV to any eventually-consistent store.

**② The lookup key decides what defences are available (scope: cross-project).** Filing a row *by* its
secret forecloses salting, because a salt you must look up first is not a salt. Choose the key by what
you will need to defend, not by what makes the read cheapest. Fernwood's grant store is the worked
example, in both directions: exactly right for a 256-bit token, unfixable for a word.

**③ Rate limits run before expensive work, not after (scope: cross-project).** A KDF, a model call, or
any billed compute placed ahead of the brake turns a guessing attack into a billing attack. Cheap checks
first, in cost order.

**④ A blanket CORS ruling is scoped to the routes that existed when it was made (scope: fernwood).**
`ACAO: *` was ruled correct for capture and read routes and it still is. The first route that *returns*
a credential is outside that premise. Re-check a standing security ruling against each new route class
rather than inheriting it.
