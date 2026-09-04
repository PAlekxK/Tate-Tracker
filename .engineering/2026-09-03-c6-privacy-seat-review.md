# C6 · THE PRIVACY / SECURITY SEAT — review of steps 3a–3c and 4a–4b

- item: `.plans/2026-09-03-c6-door-for-paul-PLAN.md` · **Q4** (this document is the seat)
- mode: review · seat: privacy/security (satisfying C6 Q4's *"an AGENT or a CHECKLIST — either satisfies"*)
- date: 2026-09-03 (ET)
- scope: the **design** of 3a · 3b · 3c and 4a · 4b, plus Q5, plus the 3c vacuous-Origin rule.
  ⛔ Not in scope: step 1 (re-drafted after Q1), step 2 (shipped tonight — reviewed only where 3/4 inherit from it),
  steps 5–7 (reviewed only where a decision made in 3/4 forecloses them).
- read first: the C6 plan (whole) · `.engineering/2026-09-03-c6-door-for-paul.md` §2 §3 §4 §5 §8 ·
  `../fernwood-private/.ux-reviews/2026-09-02-login-door-and-selector.md` F1 F2 F3 ·
  `../fernwood-private/.plans/2026-09-02-data-model-design.md` §2b §2c §5 §6 §7 ·
  `.engineering/2026-09-03-c4-topology-delta.md` D3 D6 · `CLAUDE.md` § The AI boundary ·
  `worker/worker.js` (router, `authOk`, `keyFor`/`dateKey`/`estateId`, `handleDoor`, the three write-only blocks) ·
  `worker/wrangler.toml` · `../fernwood-private/grants.json` · `viewer.html` (header construction).

**Calibration, stated up front so no severity below is read at the wrong altitude.** This is a family
app with **one vulnerable user**, ~2 people, no adversary with a motive, and a threat model whose worst
realistic actor is a bored scanner that found a `*.workers.dev` hostname. Nothing here is scored as if it
were a production multi-tenant SaaS. The two things that *do* raise the floor above hobby stakes, and
that every severity below is measured against:

1. **The private tier is now real.** Paul ruled tonight that receipts, contractor phone numbers and the
   breaker directory are in scope behind this door. A leak there is somebody's contractor's phone number
   and somebody's house's shut-off locations — not a garden journal.
2. **A third household is one item away.** `data-model §2b`'s hard prerequisite means the next estate
   holds someone else's words. A boundary that is decorative at n=1 becomes load-bearing at n=2, and the
   design decisions that make it real are being made **now**, in step 3.

**How to read the findings.** Every claim is marked `[verified]` (I read it in the code or measured it
against the running system tonight) or `[unverified]` (inference, or a claim I am taking from a document).
The seat's own recorded failure shape applies to itself: *a tool that reads OUR files reports on the
RECORD, not the world* — so where a plan and the world disagreed, I went and looked.

---

## THE THREE ANSWERS, up front

### Q4 — agent or checklist?

**This review satisfies the gate for step 3.** An agent ran; step 3's *"reviews before build"* condition is
discharged by this document.

**And the answer to the standing question is: an agent, not a checklist** — on evidence from tonight, not
on preference. Findings **1**, **2**, **13** and **14** are all of the same class: *a document asserted
something the world does not do.* A checklist cannot produce them, because a checklist is a reading of the
record, and the record was the thing that was wrong. Specifically: the plan says `keyFor`'s *"signature is
already shaped for it"* (it is not — F1); `wrangler.toml` gives QA prod's real estate id, which makes 3b's
own two-estate check unrunnable (F2); the C4 delta calls the QA origin *"Access-gated"* and it answered an
anonymous request with 200 tonight (F13); the plan scopes the client change to `WorkerAPI.call` and the
header is set in seven places (F14). Four of the fifteen findings below exist only because something was
executed or fetched.

⚠️ **What a checklist would still be good for, and this is not a consolation prize:** the *recurring*
half. This seat should not re-derive the same twelve questions each time. The durable artifact is a short
standing list — *where does the estate come from · what does a leaked credential unlock · what does the
error tell an attacker that it doesn't tell the user · what is written to a public tracked file · who may
hold a secret* — carried **into** an agent run, not instead of one.

### Q5 — may Mom's grant credential be a word she can remember?

> ### ⛔ **Not as the value that crosses the network. The presented credential is opaque and minted, for
> every grant including hers.** The word, if Paul still wants it, is a **later, device-local** mechanism
> and is not C6's.

Four reasons, in the order they bind:

1. **The store's own shape forecloses the defence a word needs.** `grant:<sha256(presented)>` uses the hash
   as the KV **key**, which means you must hash *before* you know which row you are looking at. That is
   what makes the single-`get` lookup cheap — and it is also why **no per-row salt is possible**. A salt
   you must look up first is not a salt. So the only strength available is entropy in the presented value.
   A memorable word has none. `[verified — the design is stated in 3a; the constraint follows from it]`
2. **SHA-256 is a fast hash, and that is correct for a token and wrong for a word.** For
   `secrets.token_urlsafe(32)` (~256 bits) an unsalted SHA-256 is exactly right: nothing to precompute,
   nothing to invert, and no KDF work factor to pay on every gated request. For a word it is the worst
   case — a leaked KV row is reversed against a wordlist in well under a second, and there is no dial to
   turn, because turning it would slow every request Paul makes. The prompt's own framing —
   *"the KV row is the only secret material"* — is precisely the condition under which a word fails and a
   token does not.
3. **Online guessing is currently unmetered.** `[verified]` `authOk` returning false produces a bare 401
   with no rate limiting anywhere on the gated path; the only two buckets in the Worker are on
   `POST /api/feedback` and `POST /api/door`. A dictionary run against `GET /api/vault/index` would be
   limited by nothing but Cloudflare's own platform limits. Against 256 bits that does not matter. Against
   a word it is the whole game. See F11.
4. **The word buys nothing C6 needs.** ux F2 rules that *recovery is a person* — the door's footer is
   "Ask Paul," not "Forgot password?" — and F1c rules that **she never meets the door**, because the box
   answers from the public tier and only offers the door at the moment a private answer is needed. A
   memorable credential exists to let someone let *themselves* back in. This design has already decided
   that job belongs to Paul. So the word is solving a problem the product does not have.

**The shape that keeps the word alive without breaking any of this, for Mom's retrofit:** the word is a
**local unlock over the stored token** — the device holds the minted token encrypted, WebCrypto derives a
key from the word in the browser, and the Worker never sees the word. 3a's *"hash of what is presented"* is
then **still literally true** (what is presented is always the token), the store needs no change, and Q5
can be re-opened later without re-opening step 3. ⚠️ Be honest with Paul about what that shape costs: if
the device is *cleared*, the ciphertext is gone too, so the word does not restore anything — recovery is
still Paul. Which is the tell that the word's real job is comfort, not access. That is a legitimate job.
It is not a C6 job.

**Ruling for the plan:** answer Q5 as **opaque-only in C6**, record the local-unlock shape as the named
successor, and make F11's rate limit the **stated precondition** on ever revisiting it — so the next
reader cannot reach for a word without first meeting the check that would make it survivable.

### The 3c rule — *"no `Origin` header = no claim = agrees vacuously"*

> ✅ **CONFIRMED as behaviour. ⚠️ TIGHTENED as framing** — the sentence is right and the *falsifier built on
> top of it* claims more than the mechanism delivers.

**Confirm the behaviour, and it is not close.** Vacuous agreement must stay. `[verified]` Every deterministic
tool in this repo speaks to the Worker without an `Origin` header — `check-live.py`, `qa-write-probe.py`,
`guru-probe.py`, `read-mom-engagement.py`, `deploy-worker.sh`'s `/health` call, the weather recorder. Making
a missing `Origin` a failure would 404 the entire non-AI door in one line, which is a violation of
`CLAUDE.md`'s standing *deterministic things need a non-AI door* rule, arriving through a security check.

**Tighten this, because the plan's falsifier reads as if the 404 were the boundary.** It is not:

> **`hostAgrees` is a routing-consistency and misconfiguration check. It is not access control, and it
> cannot be, because `Origin` is a client's claim about itself and any non-browser client omits or forges
> it at will.** An attacker holding a credential simply sends no `Origin` and the check agrees with them.

That is not a defect — D3 already says *"a subdomain is ROUTING"* and the plan already says *"the credential
decides."* The defect is only that the falsifier *"a token is accepted at the wrong family's door"* will,
read cold in three months, be taken as the isolation guarantee. **The thing that actually isolates estates
is the grant row's estate, and nothing else.** Two concrete tightenings, both in F4.

---

## FINDINGS

Severity is `critical` / `important` / `nice-to-have`, calibrated to *this* app. `critical` here means
*this breaks the isolation rule the whole item exists to establish, or it will be broken on day one.*

---

### 1 · ⛔ `critical` — **two sources of estate in one request.** `grantFor` cannot pass an estate into `keyFor`, and if it is made to, one request will carry two estates

**Observation `[verified]`.** Plan 3b: *"the estate comes from the row and is passed into C5 6a's
`keyFor(estateId, …)` — the signature is already shaped for it."* Measured in `worker/worker.js`:

```js
function estateId(env) { if (!env.ESTATE_ID) throw new Error(...); return env.ESTATE_ID; }
function keyFor(env, ...parts) { return estateId(env) + ":" + parts.join(":"); }
```

The signature is `keyFor(env, ...parts)` and the estate is read from the **deploy-time binding**, not from
a parameter. There is no `estateId` argument, and ~25 call sites pass `env` first.

**Why it matters, and it is the sharpest thing in this review.** Threading a row-derived estate into the
vault routes while every *other* route keeps deriving from `env.ESTATE_ID` produces a request that has
**two estates at once**: a grant for estate B, presented to a Worker deployed with `ESTATE_ID = A`, reads
B's vault and A's feedback. That is not a bug that shows up as an error — it shows up as one person's
receipts beside another person's words, in a report Paul reads, with nothing red anywhere.
`data-model §5` names exactly this class as the one thing that does **not** retrofit cheaply.

**The concrete change, and it is three lines, not a refactor.**

```
grantFor(): after the KV get, ASSERT grant.estateId === env.ESTATE_ID.
            Mismatch → treat as no grant at all (404 via the same path as 3c). Never thread a second estate.
```

Leave `keyFor(env, …)` exactly as C5 shipped it. **One estate per deploy, one estate per request** is the
truth today and it is the truth under P1; the row's `estateId` becomes a *check* rather than a *source*,
which is strictly safer and strictly less code. When a single Worker genuinely serves two estates (P2, and
not before), that is the moment to re-signature `keyFor` — as one deliberate act, with every call site
moved together, not as a side effect of adding a vault.

**Also correct the plan's sentence**, because it is the sentence a future implementer will trust.

---

### 2 · ⚠️ `important` — **QA's `ESTATE_ID` is prod's real estate id, so 3b's own check proves nothing**

**Observation `[verified]`.** `worker/wrangler.toml` sets `ESTATE_ID = "est-3c9f1a"` under **both** `[vars]`
and `[env.qa.vars]`. Confirmed live tonight: `GET https://fernwood-qa.paul-kirschenbauer.workers.dev/health`
→ `{"env":"qa","kv_canary":"qa","estateId":"est-3c9f1a",…}`. Meanwhile plan 3b's check reads: *"on QA, two
grants → two estate ids (`fernwood-qa`, `estate-b-qa`)."* Those ids do not exist anywhere.

**Why it matters.** Two things, and the second is the real one:

- The check as written **cannot run**. With F1's assertion in place, a fixture grant naming `fernwood-qa`
  is rejected by the Worker; without it, the cross-read test is testing a code path nothing will ship.
- A QA grant row is **shaped identically to a prod grant row**. The only thing separating a QA credential
  from a prod one is which KV namespace happens to be bound. That is one `wrangler.toml` edit away from
  being nothing, on the exact step where credentials start existing.

**Concrete change, and it is a precondition for step 3, not a follow-up.** Give QA its own estate before
the first grant row is minted:

```toml
[env.qa.vars]
ESTATE_ID = "est-qa0001"   # QA is not Fernwood; a QA credential must not be shaped like a prod one
```

Then mint the two fixture grants against `est-qa0001` and a second fixture id, and rewrite 3b's check to
name them. ⚠️ **Say the cost out loud rather than discovering it:** this re-keys QA's existing records
(they were written under `est-3c9f1a:`) — QA data is fixtures and disposable, but **re-run C4 3f's probe
after the change**, because its read-back leg will otherwise report a miss that is the re-key, not a
defect. `[unverified — I did not enumerate what is currently in the QA namespace]`

---

### 3 · ⚠️ `important` — **a device id Paul ruled private is in a public tracked file**, in the same file 3a is about to add its placeholder discipline to

**Observation `[verified]`.** `worker/wrangler.toml` — tracked, committed (`9d65723`), remote
`github.com/PAlekxK/Tate-Tracker` — carries `AMBIENT_MAC = "D8:F1:••:••:••:B8"` in **both** environments.
`tools/check-config-derivation.py:68` declares it *"the ONE place the station lives."* The repo is public
`[stated in CLAUDE.md's AI-boundary amendment — "committed into a public repo"; not re-verified via the
GitHub API, gh is not installed on this machine (measured)]`. `.private/ambient-station.json` still exists
on disk and is gitignored — this value used to live there. C5 7c moved it out.

**Why it matters here, in this review.** Paul ruled tonight: **device ids are private; VIN prefixes public.**
A weather-station MAC is a device id. And step 3a is about to put `FAMILY_HOSTS` **placeholders** into this
same file, on the reasoning that *"a family's name never enters a tracked file."* That discipline is worth
having — and it reads as ceremony if the file it lands in already publishes a device identifier and the
real estate id.

**Honest calibration, because I would rather you act on this for the right reason.** The *marginal*
exposure is small: the property's street address is already published in `CLAUDE.md`, and the MAC alone
grants nothing (Ambient's API needs an application key and an API key, both of which are Worker secrets and
`[verified]` are not in any tracked file). This is a **policy** finding, not a breach. It is `important`
rather than `nice-to-have` because the policy was ruled *tonight*, the file is being edited *tomorrow*, and
the cost of fixing it now is one line.

**Concrete change.** `wrangler secret put AMBIENT_MAC` per environment (or a `.private/` deploy overlay that
`deploy-worker.sh` reads), and update `check-config-derivation.py`'s roster row to expect it **absent** from
tracked files — so the check that currently blesses the leak becomes the check that catches it.
⚠️ **And state the limit:** the value is already in git history and a MAC cannot be rotated. This stops the
publishing; it does not unpublish. Do not let anyone record it as "fixed."

---

### 4 · ⚠️ `important` — **`hostAgrees` is framed as a boundary and is a signal**; tighten the falsifier, not the code

**Observation.** See the ruling above. The behaviour is right; the falsifier *"a token is accepted at the
wrong family's door"* over-claims, and the plan's own D3 text (*"a subdomain is ROUTING"*) already knows
better. `[verified — the mechanism; the framing risk is my read]`

**Two concrete changes:**

1. **Rewrite the falsifier to the thing that is actually checkable.**
   > **A handler is reachable whose estate did not come from the grant row's check.** Measured:
   > `grep -n 'ESTATE_ID\|estateId(' worker/worker.js` lists a source other than the binding, or a route is
   > added below the assertion. The cross-family curl stays as a **regression test on routing**, and is
   > labelled as one.
2. **Record the vacuous case rather than silently collapsing it into agreement.** The server-side
   host-mismatch record should carry `originPresent: true|false`. It costs one field, and it is the
   difference between *"a browser at the wrong door"* (a misconfiguration, probably Paul's own) and
   *"a client that declined to say"* (a tool, or someone who read this file). Without it, a future reader
   examining `door:` cannot tell those apart and will guess.

⚠️ **Do not "fix" the vacuous rule by requiring `Origin`.** It would 404 every deterministic tool, which
is the non-AI door. Named here so the next reader does not helpfully close it.

---

### 5 · ⚠️ `important` — **the 404 must be byte-identical to the router's real 404**, or the whole 403-avoidance is undone by comparing two response bodies

**Observation `[verified]`.** The router's terminal 404 is `json({ error: "not-found", path: url.pathname }, 404)`
— it **echoes the path**. If 3c's mismatch returns anything else (a bare `{error:"not-found"}`, a different
key order, a different status text), then an attacker holding a credential distinguishes *"this route does
not exist"* from *"this route exists and my token is wrong for this host"* by a single string comparison —
which is exactly the fact the plan chose 404-over-403 to hide.

**Concrete change.** The mismatch path returns the **same expression**, not a lookalike:
`return json({ error: "not-found", path: url.pathname }, 404);` — and the QA check asserts the two bodies
are byte-identical, not merely both 404. This is ten minutes and it is the difference between the choice
meaning something and the choice being a comment.

**What the *client* learns, since the plan asks:** nothing — which is right, and creates one obligation.
`[verified in the plan]` 5a returns 401 with `{error, door:"vault"}` for a wrong/revoked credential, and 3c
returns a bare 404 for a host mismatch. **The viewer must render the identical human state for both.**
ux F2 governs this: *the app forgot; she did not do anything* — not "Session expired," not red, no alert
chrome. Plan 4b already fires `door_failed` on 401 **and** 404, which is the right instinct; make the copy
rule explicit too, or the first person to see the 404 will write a second, more "helpful" message for it.

---

### 6 · `nice-to-have` — **the host-mismatch path is measurably slower than the unknown-credential path**, which is the oracle the 404 was chosen to close

**Observation `[verified by reading the intended control flow; not measured against a deployed
implementation, which does not exist yet]`.**

| presented | work before the response |
|---|---|
| unknown credential | one KV `get` (miss) → return |
| **valid credential, wrong host** | one KV `get` (**hit**) → read `door:<date>` → parse → push → **write it back** → return |

The second is a KV read-modify-write slower than the first, reliably, over many samples. So an attacker
probing tokens can separate *"valid token, wrong host"* from *"invalid token"* on latency alone — the exact
discrimination 404-not-403 exists to prevent.

**Concrete change.** Do the record write **outside the response path**:
`ctx.waitUntil(recordDoorFailed(...))`. ⚠️ This requires adding `ctx` to the handler signature — currently
`async fetch(request, env)` `[verified]` — a one-word change to `async fetch(request, env, ctx)`.

**Why this is `nice-to-have` and not higher, stated so it is not over-invested in.** It only matters to an
attacker who *already holds a valid credential for another estate* and is trying to learn which host it
belongs to. At n=1 estate there is no other estate. Do it when 3c is written, because it costs one word
then and a re-read later; do not hold step 3 for it.

---

### 7 · ⚠️ `important` — **the header name, and the CORS line that will break it on day one**

**Observation `[verified]`.** `CORS_HEADERS` declares
`"Access-Control-Allow-Headers": "Content-Type, X-Tate-Token"`. A new custom request header triggers a
**preflight**, and a preflight that does not list the header fails — so every browser call carrying the
grant header is blocked by the browser before it reaches the Worker. The failure looks like a network
error, not an auth error, which is the worst diagnostic shape available.

**Concrete change, both halves:**
- **Name: `X-Grant`.** It differs from `X-Tate-Token` in every character (seat discipline 2); it uses the
  ratified vocabulary word (`grant`, `VOCABULARY.md §2`); it carries **no product name and no family name**,
  so it survives the rename and leaks nothing in a request log; and it pairs cleanly with 4b's storage key
  `tateTracker.grant.v1`. ⛔ Avoid `X-Fernwood-*` — that is an instance name on an engine-class surface.
- `"Access-Control-Allow-Headers": "Content-Type, X-Tate-Token, X-Grant"`, shipped **in the same commit as
  the first client send**, never after.

**And one thing to explicitly NOT do, so nobody spends effort there.** Do **not** tighten
`Access-Control-Allow-Origin: "*"` to the family hosts. CORS restrains browsers, not clients; it buys
nothing against anyone holding a credential, and `*` is what keeps the ungated capture path working from
any device — which is the 2026-07-15 doctrine. `[verified — ACAO is "*" today]` Leave it.

---

### 8 · ⚠️ `important` — **what a leaked grant unlocks, and the capability/relationship confusion in 6a that decides it**

**Part A — the blast radius, named plainly.** Under 6a as drafted, an `administrator` grant unlocks
*"what the master unlocks today"*, which `[verified]` is: `GET /api/feedback` (**her verbatim notes**),
`GET /api/zone-audio` (**her voice recordings**), `/api/conversations` (Guru turns), `/api/metrics`,
`/api/chat` (**real Anthropic spend**), `/api/promote-species` and `/api/remove-species` (**writes and
DELETEs to public canon via a GitHub token**), `/api/admin/clean-observations`, `/api/zone-save` — plus, from
5a, the **private tier**. That is one opaque string, in localStorage on a phone, sent on every request, with
**no expiry ever** by deliberate design, revocable only when Paul notices.

⛔ **The no-expiry ruling is right and I am not reopening it.** ux F2 is correct that a TTL is a silent
expiry with a longer fuse, and the seat's discipline 1 is correct that revocation must be an act with an
author. The consequence, which should be written down beside it rather than left implied: **the only
control on blast radius is scope, because there is no clock.** So scope has to do all the work.

**Concrete change.** 6a's own title says *"dual-accept on the read paths"* and its body then grants
promote/remove-species. Resolve it in favour of the title: **in C6, a grant unlocks reads + `POST
/api/metrics` + the vault, and nothing else.** `/api/chat`, `/api/promote-species`, `/api/remove-species`,
`/api/admin/*` and `/api/zone-save` stay master-only until there is a reason. Money and commits to a public
repo are not "reads," and nothing in C6 needs them.

**Part B — and this is the part that will silently do the wrong thing.** 6a reads: *"`contributor` unlocks
`/api/metrics` POST and the vault only."* `[verified]` **`contributor` is a *relationship*, not a
*capability*.** `VOCABULARY.md` and `data-model §2b` ratified **two axes, not one ladder**, and
`grants.json` already reflects it:

```json
{ "relationship": ["owner","contributor"], "capability": "member",        "_handles": "mom @ fernwood"  }
{ "relationship": ["contributor"],          "capability": "administrator", "_handles": "paul @ fernwood" }
```

A Worker that branches on `relationship.includes("contributor")` would grant **Mom** (relationship
contributor) the contributor policy and deny a **resident** who was meant to have it — a different policy
from the one Paul ratified, arriving as a naming slip, with no test that would catch it.

**Concrete change.** Authorization branches on **`capability` only** (`administrator` | `member`);
`relationship` is **never** consulted for an access decision. Write that as a one-line rule in the plan, and
give it a grep falsifier: `grep -n 'relationship' worker/worker.js` → **0 hits**. Fix 6a's sentence to say
`member`.

---

### 9 · ⚠️ `important` — **`declarePerson` is a default, not a guard**, and 3b is exactly the edit that turns that into a bug

**Observation `[verified]`.**

```js
const PERSON_UNKNOWN = Object.freeze({ personId: null });
function declarePerson(record) { return Object.assign({}, PERSON_UNKNOWN, record); }
```

The `record` argument **wins**. Today no call site passes `personId`, so it is safe — I checked all six
`[verified: lines 259, 1177, 1415, 2391, 2828 and the definition]`. But the name says *declare* while the
behaviour is *default*, and 3b is precisely the change that will start passing a `personId` in. The moment
one handler does, any handler that spreads a client-supplied body through `declarePerson` attributes from
the client. `handleFeedback` is already one spread away — it copies `body.context` through verbatim.

**Why this is `important` at these stakes and not paranoia.** The plan's own falsifier is *"identity is
applied backwards… the 2026-08-01 retraction is recurring with a stronger-looking warrant."* This is the
mechanical route by which that recurs, and it costs three lines to close **before** the first non-null
person is ever written.

**Concrete change.**

```
declarePerson(record):  if ("personId" in record) throw — this function declares ABSENCE, not identity.
attributeTo(record, grant):  the ONE function that may set a non-null personId, and it takes a resolved
                             grant row, never a request, never a body.
```

Then C5's grep falsifier has exactly **two** names to find — the resolver and `attributeTo` — instead of a
convention nobody can check.

---

### 10 · ⚠️ `important` — **there IS a path that attributes on an unauthenticated field**, and C6's rule does not cover it because it lives on the read side

**Observation `[verified in design; the resolver itself is C5's and I did not read `momlib.person_for`]`.**
The plan's rule — *"a person ONLY from a valid grant header on `door_opened`"* — governs **the Worker**.
But C5 1b's resolver *"the only writer of a non-null person"* runs on the **read side** and derives a person
from a **`deviceId`** — a value that arrives on the three **ungated** POST routes, entirely client-supplied,
unauthenticated, and never verified. `handleFeedback` stores `deviceId: body.deviceId || null` verbatim
`[verified]`.

So: forge a `deviceId` (or merely copy a browser profile, or run the test harness under the wrong id) and
the record is attributed to Mom **in a report Paul reads**, with no forged credential involved and every
grant-side falsifier green.

**This is not a new hole and I am not asking C6 to close it** — the project has said from the start that
*a deviceId is a browser bucket, not a person*, and every surface that renders one says so. The finding is
that **C6 is the moment the two writers become confusable**, because for the first time one of them is
genuinely authoritative and the other is not, and they write into the same field.

**Concrete change, one field.** Wherever a person is written or derived, carry the source beside it:

```
personId:     "p-b91e4d" | null
personSource: "grant" | "device-inference" | null
```

`grant` is a claim; `device-inference` is a guess with a long-standing disclaimer; `null` is honest silence.
This is the **same shape as 6a's `via: "master"|"grant"`** — adopt it in both places and it is one idea, not
two. It also means the falsifier *"a person stamped on a `door_failed`"* becomes checkable on the record
itself rather than on the code that wrote it.

---

### 11 · `nice-to-have` today, **`important` the moment a word is entertained** — nothing rate-limits a credential attempt

**Observation `[verified]`.** The Worker has exactly two rate buckets — `feedbackRateLimitOk` and
`doorRateLimitOk` — and both sit on **ungated POSTs**. A failed `authOk` returns a bare 401 with no bucket,
no backoff, no counter. 5a's vault routes inherit that: an unlimited number of credential guesses per second
against the route that returns the private tier.

**Why `nice-to-have` and not higher, honestly.** Against `secrets.token_urlsafe(32)` this is irrelevant —
2^256 does not care about your request rate, and adding a KV read to every gated request to defend against
an impossible attack is exactly the over-engineering Paul's foundation tells me not to recommend.

**Why it is nonetheless written down.** It is the **precondition on Q5**. Reuse `doorRateLimitOk`'s shape —
20 failed presentations per IP per 5 minutes, its own bucket — and it becomes cheap; skip it, and a future
"let's just use a word, it's only Mom" has nothing standing in its way. **Recommendation: don't build it
now; write it into the plan as the named gate that must exist before any low-entropy credential is
considered.**

---

### 12 · ⚠️ `important` — **the ungated writes stay ungated. Confirmed. And the abuse ceiling is not graffiti — it is denial of capture**

**Confirmed, without reservation.** `/api/feedback`, `/api/zone-audio` and now `/api/door` stay write-only
and token-free. The reasoning is already in the file at the site of the code, it was bought with a real loss
(2026-07-15, her MacBook, her words gone, invisible to Paul), and three independent rules converge on it:
ux F1b#5 (*a capture that can fail because a session lapsed is a capture that lies*), the site premise
(*the places worth walking to are the places with no network*), and the seat's own instrumentation finding
(*the locked-out person is exactly who must be able to report being locked out*). ⛔ **The day identity
exists, someone will propose authenticating capture. The answer is no, and the reason is written down in
three places.**

**But the plan's stated ceiling — *"graffiti in a notebook — recoverable"* — is optimistic, and here is what
I measured `[verified]`:**

1. **The size cap is advisory.** All three blocks test `parseInt(request.headers.get("Content-Length") || "0")`.
   A client that sends no `Content-Length` (chunked) yields `0`, which passes every cap. The body is then
   read in full by `request.json()`.
2. **`handleFeedback` stores unbounded client strings.** `id`, `ts` and `deviceId` are copied with no
   `.slice()`, and `context` is stored as **an arbitrary client object with no size bound**. Only `note` is
   capped (2000 chars).
3. **Every POST read-modify-writes the whole day.** `get(feedback:<date>)` → parse → push → `put`. KV's
   value ceiling is ~25 MB. As the day's array grows, every write costs the full array both ways, and past
   the ceiling **the `put` throws** — with no `try/catch` around it.
4. **The window is fixed, not sliding.** `Math.floor(Date.now() / 300000)` → **40 requests in a burst**
   across a boundary, not 20.

**So the honest ceiling:** a single actor with a script can inflate one day's key until writes fail, and
from that moment **Mom's note does not land**. The client outbox retains and replays it `[unverified — I did
not read the outbox's retry policy]`, so *capture does not lie* — but the note never arrives, and every tool
in the mom-cycle reads that as **her going quiet**. This project has an entire doctrine block
(*an empty answer record is not a quiet user*) about how expensive that misreading is.

⚠️ **Likelihood is low and I want that said plainly** — the Worker URL is discoverable from the public
repo, but nobody has a motive, and this has been live for months without incident. It is `important`
because the *failure mode* is the one failure this product has ruled unacceptable, and the fixes are small.

**Concrete changes, in order of value:**
1. **Cap the day's array** (e.g. 500 records — ~25× the busiest real day `[unverified — not measured]`) and
   return a non-2xx when full, so the outbox retains rather than the app pretending.
2. **Slice the strings, bound the object** in `handleFeedback` — `id`/`ts`/`deviceId` to 40 chars,
   `JSON.stringify(context).length` capped. ⭐ **`handleDoor` already does exactly this, field by field,
   and it is the model** — copy its shape upward rather than inventing one.
3. **Note the read-modify-write race:** two concurrent POSTs both read, both push, last write wins, one
   record is lost silently. At n=2 people this is theoretical — but the falsifier *"a locked-out person is
   invisible to the record"* rests on this exact write, so it belongs in the plan as a known limit rather
   than as a surprise.

**And one inconsistency 2a created without noticing `[verified]`:** the door got its own bucket on the
reasoning that *"a door storm never 429s a note"* — while `/api/zone-audio` still calls
`feedbackRateLimitOk`, sharing the note's bucket with payloads three orders of magnitude larger, on a link
the site premise says is flaky. The same sentence applies verbatim. `nice-to-have`; give zone-audio its own
bucket when something else touches that block.

---

### 13 · ⚠️ `important` — **the QA origin is public. Measured tonight, and the record says otherwise**

**Observation `[verified — measured 2026-09-03 ~20:57 ET]`.**

```
GET https://fernwood-qa.pages.dev/            → 200   (anonymous)
GET https://fernwood-qa.pages.dev/viewer.html → 308 → /viewer
GET https://fernwood-qa.pages.dev/questions.json → 200
GET https://fernwood-qa.paul-kirschenbauer.workers.dev/health → 200
     {"env":"qa","kv_canary":"qa","estateId":"est-3c9f1a","legacyBefore":"2026-09-03",
      "configured":{…,"anthropic":true,"github":false,…}}
```

`.engineering/2026-09-03-c4-topology-delta.md` D3 states the QA origin is an *"Access-gated `*.pages.dev`
host"* — **twice**. It is not gated. That is a record-vs-world gap of exactly the shape this project has
recorded four times in one lap.

**What it exposes for the door tests, concretely:**
- **The public canon on QA is already public on prod** — no new exposure there.
- ⚠️ **Step 5b will publish the vault fixture's *declaration*.** The built QA `viewer` carries the instance
  config, so `vault.rooms`' declared **names** are readable by anyone. The room's *contents* need a grant;
  its *existence and title* do not. **Rule: the QA fixture room's title, ids and body must be
  non-identifying by construction** — not "no real contact" (which the plan already says) but *no real room
  name, no real address, no real person's name, no plausible-looking phone number*.
- **`/health` publishes the estate id and the legacy cutover.** Both are opaque and neither is a credential
  — ⛔ **do not over-react and hide them**; they are the deterministic non-AI door onto "which deploy am I
  talking to," and that is worth more than the nothing they leak.
- ⚠️ **QA holds a live Anthropic key** (`configured.anthropic: true`). The QA `SHARED_TOKEN` is therefore a
  **spend credential**, not a throwaway. Treat it with the same care as prod's — it is currently in
  `.private/fernwood-qa-token` `[verified via tools/guru-probe.py:21]`, which is right.

**Concrete change — pick one, before 5b declares a room, not before step 3:**
- **(a)** put Cloudflare Access in front of `fernwood-qa.pages.dev` (which is what D3 already claims), or
- **(b)** ⭐ **recommended** — accept a public QA origin, and make the fixture non-identifying by
  construction as above. It is less machinery, it keeps agent testing frictionless, and *"the QA fixture
  contains nothing real"* is a rule that can be checked by reading it, whereas an Access policy is a
  setting that can be silently changed.

Either way, **correct D3's two sentences.** A claim that the origin is gated is worse than no claim,
because the next reader will design against it.

---

### 14 · ⚠️ `important` — **4b's client change is scoped to one call site and the header is set in seven**

**Observation `[verified]`.** Plan 4b: *"`WorkerAPI.call` sends the grant header when present, the master
otherwise."* Measured: `grep -c '"X-Tate-Token"' viewer.html` → **7**, at lines 12294, 13297, 13335, 18299,
18451, 19015, 19147 — six of which read `tateTracker.sync.v1` directly rather than going through
`WorkerAPI`. There are 6 direct reads of the `sync.v1` key.

**Two consequences:**
1. **In C6:** Paul binds a grant, and six of seven paths on his device keep presenting only the master. The
   door "works" (the vault probe goes through `WorkerAPI`) while most of the app is still on the old
   credential — so `handleMetrics`' `via: "master"|"grant"` stamp, which 6c's **measured-zero gate** depends
   on, reports a mixture that reflects *which code path fired*, not *which credential he holds*. The gate
   would never go green, and the reason would be invisible.
2. **At 6c:** the rotation replaces `SHARED_TOKEN`. Every device still holding the old value in `sync.v1`
   loses those six paths **silently** — including hers. 6c's stated protection is *"the master survives for
   tools"*, which is about `.private/fernwood-token` readers, not about the six in-page call sites.

**Concrete change.** One function, seven call sites:

```
authHeaders():  { "X-Grant": grant }  if tateTracker.grant.v1 is present
                { "X-Tate-Token": token } otherwise
                (never both — one credential per request, so the Worker never has to choose)
```

**Falsifier, and it is a one-liner Paul can run:** `grep -c '"X-Tate-Token"' viewer.html` must equal **1**
after 4b. That single number is what makes 6c survivable later.

---

### 15 · ⚠️ `important` — **the router's security-relevant order is not written down**, and 3c's stated placement contradicts two other rules in the same plan

**Observation `[verified]`.** 3c says `hostAgrees` runs *"at the top of the router before any dispatch."*
Taken literally that is above the `OPTIONS` branch (line 2459) and above the three ungated write blocks —
which would 404 CORS preflights and would host-check credential-free capture POSTs, contradicting 3c's own
*"ungated POSTs with no credential are untouched"* and F1b#5.

**Concrete change — write the order once, as a numbered list, in the plan.** It is the whole
security-relevant control flow and it is currently distributed across four paragraphs:

```
1. OPTIONS                 → 204 + CORS. No credential, no host check. (A preflight carries no grant header.)
2. /health                 → open. The non-AI door; nothing behind it.
3. Resolve the grant       → ONLY if the grant header is present. One KV get, once, in the router.
                             Assert grant.estateId === env.ESTATE_ID (F1). No clock comparison (ux F2).
4. Host agreement          → ONLY if a grant resolved. mismatch → 404 identical to step 8's (F5).
                             absent Origin → vacuous agree, recorded (F4).
5. Ungated write exceptions→ ONLY when NEITHER credential is present. Size cap, own rate bucket, write-only.
6. /api/ambient            → open (2026-08-02 ruling, unchanged).
7. Gate                    → authOk(master) || (grant && capability permits this route)   [F8]
8. Dispatch / 404
```

⭐ **And one structural point that follows: resolve the grant exactly once, in the router, and pass the
resolved row into handlers.** No handler re-reads the header. Otherwise `handleDoor` — which is reachable
by **two** routes, the ungated branch at step 5 and the gated dispatch at step 8 `[verified]` — has to
resolve it a second time to honour the 3b attribution rule, and "only one place writes a person" becomes a
convention spread across handlers instead of a fact.

---

### 16 · ✅ `praise` — four things this code already gets right, named so they are not refactored away

`[all verified]`

1. **`handleDoor` validates and bounds every field individually** — enum-checked `event` and `door`,
   `.slice(0,40)` on `ts` and `deviceId`, nothing copied from the body wholesale. It is the only handler in
   the file that is safe against finding 12 by construction. **Make it the template, not the exception.**
2. **`personId: null` as a *declared* value, distinguished from absent.** *"Written after the field existed
   and nobody could say"* vs *"written before the field existed"* are genuinely different observations, and
   almost nobody bothers to keep them different. It is what will make finding 10's `personSource` field
   land cleanly.
3. **`estateId(env)` throws on a missing binding** rather than defaulting. *A Worker that cannot say whose
   estate it serves must not read or write a record* is the correct posture, and it is the reason finding
   1's assertion is cheap to add.
4. **The legacy window reads by the record's own date and never `get(new) || get(old)`** — with the reason
   written at the site. That fallback is the single most common way a migration hides a missing key forever,
   and someone saw it coming.

---

## What Paul must set by hand, and what an agent may do

Asked directly, so answered as a roster rather than prose.

**⛔ Paul only — and each for a stated reason, not by default:**

| act | why it is his |
|---|---|
| `wrangler secret put` for **any** secret — `SHARED_TOKEN`, `AMBIENT_MAC` (F3), a future `GRANT_PEPPER` | a secret an agent has typed is a secret in a transcript. ⚠️ **In a real TTY** — the plan already records that `!` uploads an empty secret and prints success |
| **running `grant-mint.py` against any environment, and holding the printed token** | the mint's output *is* the credential. It exists for exactly one moment, through `/secrets`, and never in a file, a commit, or a scrollback an agent can read |
| **pasting the grant into a device** (4b on his phone, 6b on hers) | it is the credential, and 6b is on her device — which the plan already fences |
| **the values in `grants.json`** (rows are the agent's, values are his) | already ruled; unchanged by this review |
| **the real `FAMILY_HOSTS` values** | see below |
| **the prod `SHARED_TOKEN` rotation (6c)** | already ruled, irreversible |

**✅ An agent may:** write the Worker code and the checks; write `grant-mint.py`; deploy the **QA** Worker;
run every QA probe; add grant **rows** (no values) and the `FAMILY_HOSTS` **placeholder keys**; run the
cross-family curls; and deploy the **prod** Worker for additive branches (already ruled, `/health` proves it).

**Three additions this review would put on the "agent may not" list:**

1. ⛔ **An agent may not persist a credential value anywhere — including a test fixture, a selftest, or a
   `.private/` file.** `grant-mint.py --selftest` must **mint an ephemeral value at runtime, use it, and
   delete the KV row**, never read one from disk. A QA token in a fixture is a real credential with a
   "just testing" label on it, and QA holds a live Anthropic key (F13).
2. ⚠️ **An agent may not add a route below the grant resolution without re-running 3c's check.** F15's
   ordering is the kind of thing that is correct on the day it is written and wrong four routes later;
   the falsifier in F4 is what catches it.
3. **`FAMILY_HOSTS` should be a `wrangler secret`, not a `--var`** — vars set at deploy are visible in the
   Cloudflare dashboard and echoed in `wrangler deploy` output; secrets are not. ⚠️ **And say the honest
   limit out loud, because it changes what the placeholder discipline is *for*:** a hostname is public DNS,
   and **D6 already establishes that certificate transparency publishes every first-level subdomain to a
   permanent, undeletable log.** So keeping a family's name out of a tracked file protects **the repo**, not
   **the world**. The control that protects the world is D6's — a wildcard SAN, or **non-identifying
   subdomain labels chosen before the host is created.** These are the same decision and should be made
   together, once, before `<family-b>` exists.

---

## VERDICT

**Step 3 opens.** The design is sound where it matters most: tenant-from-credential with the mapping held
server-side is the right mechanism, no `exp` and revocation-as-an-authored-act is the right discipline, a
distinct header and storage key is the right hygiene, 404-not-403 is the right instinct, and the decision to
put the door's instrumentation on the *ungated* path — so the locked-out person can report being locked out
— is the finding that makes this item shippable at all. **Four conditions, all small, none a redesign:**
**(1) F1** — `grantFor` *asserts* `grant.estateId === env.ESTATE_ID` and 404s otherwise; `keyFor` is **not**
re-signatured in C6, so one request never carries two estates; **(2) F2** — QA gets its own `ESTATE_ID`
before the first grant row is minted, or 3b's own check proves nothing and a QA credential is shaped exactly
like a prod one; **(3) F5 + F7** — the mismatch 404 is byte-identical to the router's real 404, and `X-Grant`
is added to `Access-Control-Allow-Headers` in the same commit as the first client send, or the door is
broken in the browser on day one; **(4) F9** — `declarePerson` becomes a guard that *throws* on a
client-supplied `personId` **before** 3b writes the first non-null person, because 3b is the exact edit that
makes today's safe default unsafe. **Q5 is answered opaque-only** — the presented credential is minted for
every grant including hers, the memorable word is deferred with a named successor shape (a device-local
unlock the Worker never sees) and F11's rate limit written into the plan as the gate that must exist before
it is reconsidered. **Q4 is discharged by this document.** Two things outside step 3 that should not wait for
the item that formally owns them: **F3** (a device id Paul ruled private is in a public tracked file, and 3a
is about to add its placeholder discipline to that same file) and **F13** (the QA origin is public, measured
tonight, and the record says it is gated — correct the record before 5b declares a vault room there). And
one sentence to carry forward into every later step: **there is no clock in this design, deliberately and
rightly — so scope is the only thing limiting what a lost credential costs, which makes F8's "reads +
metrics + vault, and nothing else" the load-bearing decision of step 6, not a detail of it.**
