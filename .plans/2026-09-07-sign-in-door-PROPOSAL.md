# sign-in-door · The door a person who ALREADY has an account comes back through — sign in · create · recover
- row: proposed — BACKLOG.md § C6 · THE DOOR (ROW TO ADD — this scopes the *returning* half of C6; the orphan flag is expected until the row lands)
- objective: O3
- class: engine · declared
- seats: engineering-partner → .engineering/2026-09-05-account-credential.md
         ux-expert → ../fernwood-private/.ux-reviews/2026-09-02-login-door-and-selector.md
         user-researcher → ../fernwood-private/.user-research/2026-09-02-activation-journeys.md
         privacy-security → .engineering/2026-09-03-c6-privacy-seat-review.md
         content-steward → owed, not waived: every word on this door is read by a person who is already worried she has been locked out. This file specifies slots and constraints; it words nothing.
         ai-advisor → waived: no model is on this path. A credential is verified deterministically, and ⛔ a model may never generate the credential (activation-journeys §4).
- depends-on: .plans/2026-09-03-c6-door-for-paul-PLAN.md
- depends-on: .plans/2026-09-05-onboarding-PLAN.md
- ready: agent-proposed 2026-09-07 — **Paul rules**. ⛔ NOTHING IN § Sequence STARTS. This document was produced under a scoping instruction: *"we should definitely start a lane scoping it now because we're gonna need it in the future."*
- stage: concept
- wip-exception: opens no WIP. It executes nothing, ships nothing, and cannot move past `concept` without a `ready:` stamp. Declared so the in-flight count stays honest.
- stage-note: 2026-09-07 — drafted in the `door-scope` worktree at `bb00997`. Read-only apart from this file: no tracked file outside `.plans/` edited, nothing deployed, no network call to production. Every 🔬 claim below was executed today; every other claim is graded on its own line.

> ### ⚠️ TWO NOTES ON THE HEADER, because the one-line keys above cannot carry them
>
> **`class: engine · declared` — and the qualifier is load-bearing.** The SURFACE is engine (one door,
> every household, no fork). Whether a door is *demanded* is `config`, per § 🔓 BOTH PASSWORDS ARE
> OPTIONAL `[paul-stated 2026-09-02]`. **A build that hard-codes *"you must sign in"* has silently
> promoted config to engine**, and that is the failure this line exists to prevent.
>
> **The seat lines name ONE trail each; the seats each have TWO.** Also read:
> `.engineering/2026-09-03-c6-door-for-paul.md` (§2 the entry door, §4 the estate-id constraint) ·
> `../fernwood-private/.ux-reviews/2026-09-05-account-creation.md` ·
> `../fernwood-private/.user-research/2026-09-04-onboarding-journey.md`. Sections that carry this
> lane: ux **F1** (the never-behind-the-door list) · **F2** (the door's shape) · **F3** (text size) ·
> **F7** (one resolver); research **§4** (who sets the password) · **§5.1–5.4** (the failure journeys);
> engineering **Option D** (the mechanism this door drives).
>
> ⛔ **`privacy-security` IS CITED, NOT RE-RUN, AND ITS PREMISE HAS MOVED.** It reviewed a world with no
> credential-returning route. `/api/session` now returns a bearer token (§1.2), and §4.3 names two
> consequences it could not have weighed. **A fresh pass is owed BEFORE any of § Sequence starts.**

**Read before drafting** (by role, not line number — C4 renames the root): the three C6 seat trails and the
privacy seat · `.engineering/2026-09-05-account-credential.md` §0–§4 · `PRODUCT-ENGINE.md` § 🚪 ACTIVATION
(including the retired model, preserved), § The minimum a person supplies is ZERO, § Credential ownership is
PER GRANT, § 🔓 BOTH PASSWORDS ARE OPTIONAL, § 🧭 THE SETUP JOURNEY · `VOCABULARY.md` §3b (surfaces and
doors) and §4 (what was rejected) · `onboarding/index.html` in full · `worker/worker.js` accounts block and
router · `estate/index.html` and `homes/index.html` empty states · `tools/check-backlog-ready.py` for this
header's shape.

---

## 1 · WHAT EXISTS TODAY — 🔬 measured 2026-09-07, and the headline is not what the ask assumed

### 1.1 There is no sign-in SURFACE. That much is true.

🔬 `grep -l 'type="password"'` over the tracked tree returns **three** files: `onboarding/index.html`,
`viewer.html`, `engine/viewer.template.html`. The viewer's two are the maintainer **Sync settings** modal
(`Worker URL` + `Shared token`, a paste field for the master secret on Paul's own device) — not a door.
**So the only password field a person meets in this product is account CREATION**, exactly as the brief says.

### 1.2 ⭐ BUT THE MECHANISM IS BUILT, AND IT IS BETTER THAN THE BRIEF ASSUMES.

🔬 `POST /api/session` exists in `worker/worker.js` (`handleSession`), is wired in the router ahead of the
master-token gate, and does the whole job: it verifies `{username, word}` by PBKDF2 against the
username-keyed **account row**, **mints a fresh opaque token**, writes the new grant row, **deletes the
prior one** (so a stale credential stops working at the next sign-in), copies the place's facts
(`placeName`, `accent`, `address`, `addressParts`, `ranked`, `contactPref`, `profileAccent`, `coordinates`)
from the account row onto the grant, and returns the token plus those facts.

🔬 **Nothing a person can reach calls it.** `grep -rn 'api/session'` over the tree returns exactly two
callers, both agent tooling: `tools/synthetic-identity.py` and `tools/journey-walk.py`.

🔬 **It is not in production.** `git show origin/main:worker/worker.js | grep -c api/session` → **0**;
`origin/staging` → **1**. The credential code is QA-only, and the comment above it says so:
*"⛔ DEV ONLY UNTIL REVIEWED."*

> ⭐ **THE FINDING THAT REFRAMES THE LANE.** *The sign-in door is not a mechanism problem. It is a surface
> problem plus a policy problem.* The hard cryptographic half is built and exercised by four synthetic
> seats every walk. What does not exist is (a) a page a human being can open, (b) a decision about who
> resets a password, and (c) a review of two things that changed under the privacy seat's feet (§4.3).
> **Scoping this as "build a login page" would get the easy half right and the expensive half wrong.**

### 1.3 The three states, confirmed against the code

| the person | what they meet today | 🔬 where |
|---|---|---|
| has a grant in this browser | `estate/` renders their place | `estate/index.html` render path |
| ⛔ **has an account, this browser has no grant** | ⛔ **routed to CREATE AN ACCOUNT** | `onboarding/index.html` — the returning-reader test is `read(K_USER)`, a **localStorage** key. A new browser has no `K_USER`, so a person who already has an account is sent to make a second one — and their username is taken. |
| no account | *"Open your invitation link and your place will be here."* / *"…your homes will be here."* | `estate/index.html`, `homes/index.html` |

⚠️ **The middle row is worse than "nothing".** The brief describes it as *nothing*; the code routes it to
the **wrong** thing. The file's own comment already names the shape — *"⛔ THE TEST IS 'DOES SHE ALREADY
HAVE ONE', NOT 'DID SHE ARRIVE WITH A LINK'"* — but the only test available on a fresh device is a
device-local key, so the condition it wants cannot be evaluated. **A sign-in door is the missing evaluator.**

### 1.4 The promise already made, and currently unbacked

The setup flow tells a person their place is theirs *on any phone, not just this one*. §1.3's middle row is
that promise failing, on the exact device where it was supposed to pay off. **This is the strongest argument
for the door and it should lead the case to Paul** — not "we need a login page", but *we made a portability
promise and there is no route that keeps it.*

---

## 2 · WHAT IS MISSING — and the one thing that is missing is not a form

Three surfaces, in the order a person meets them:

1. **Sign in** — a username and a password, exchanged for a credential this browser keeps. `/api/session`
   already does the exchange; nothing calls it.
2. **Create an account from the same door** — the person who arrives without one. ⛔ *Not* a second copy of
   the setup flow: the same `onboarding/` journey, reached from the door.
3. **Recover access** — ⛔ **the only one of the three that is not an engineering task.** See §5.

⭐ **And one that is missing and is easy to miss: the door has no PLACE to be.** The ux seat's F2 ruling —
*the door is never on the path into the app; it exists only at the boundary of the thing it guards* — was
written for the **vault**, under the closed-enrolment model where nobody signed in. Under the 09-05
registration ruling (§3) there is now a returning stranger with no grant and no invitation link, and F2 gives
them nowhere to stand. **That is a genuine gap between two ratified positions, not a contradiction to route
around**, and §3.3 states it for Paul rather than resolving it.

---

## 3 · ⛔ THE MODEL COLLISION, AND IT HAS TO BE RESOLVED BEFORE THE FIRST FIELD IS DRAWN

### 3.1 What changed

`PRODUCT-ENGINE.md` § 🚪 ACTIVATION: **"NOBODY SIGNS UP" IS RETIRED** `[paul-ruled 2026-09-05]` — *full
registration: people set up their own account and add their own properties.* The section beneath it, which
argued *recognized, never registered*, is preserved as history and **is no longer the design**.

### 3.2 Which prior findings survive that ruling, and which do not

⚠️ **The three seat trails this lane was told to start from were all written 2026-09-02/03, under the
retired model.** Reading them as current would import a dead premise. Graded:

| finding | source | survives the 09-05 ruling? |
|---|---|---|
| The app renders its glance with **zero authorization round-trips** | ux F1a | ✅ **STANDS, and gets stronger.** A registration product has *more* reason to keep the journal public: a stranger who cannot get in must still see something real. |
| The capture path stays ungated | ux F1b #5 | ✅ **STANDS.** Unchanged by who authored the account. |
| Text size must survive being signed out | ux F3 | ✅ **STANDS** — and is now *load-bearing on a route that exists*, because §1.3's middle row is exactly the signed-out render. |
| **One resolver returns the trust state; the client never re-derives it** | ux F7 | ✅ **STANDS**, and a sign-in door is precisely where a second resolver gets written by accident. |
| No `exp`, no TTL; trust is revoked by an act | eng §2 discipline 1 · ux P2 | ✅ **STANDS.** ⚠️ Note `/api/session` already *rotates* on every sign-in — a deliberate act at a person's own request, not a clock. The rule is intact; say so, or the next reader reads rotation as expiry. |
| No estate id in any client-composed request | eng §4 | ✅ **STANDS**, and is the one constraint testable by `grep` today. |
| *"The minimum a person supplies is ZERO"* | research §1 | ⛔ **RETIRED as the model.** It is now the *floor argument* for keeping the returning door to two fields, not a description of the product. |
| *"Mom's retrofit: no visible change"* | research J2 | ⛔ **RETIRED** `[paul-stated 2026-09-05: "I'll even make Mom set up her own account and all that."]` |
| **Recovery is a person** | research §5.3 · eng §3.4 | ⚠️ **UNRESOLVED, NOT SURVIVING.** It was a *consequence* of closed enrolment — of course recovery is the person who enrolled you. Under self-registration the enroller is the person themself. §5 is that hole. |
| *"Email has no job" · "Phone has no job"* | research §1.1 · PRODUCT-ENGINE | ⛔ **REVERSED IN THE SHIPPED CODE.** `onboarding/index.html` asks for both `[paul-stated 2026-09-05]`, and the file names the reversal in its own comment. **The engine document still carries the old rule.** ⚠️ A ruling that is not in the register is not in force — and here the register carries the *retired* rule while the code carries the new one. Flagged to Paul in §7. |

### 3.3 ⭐ The gap the collision opens, stated and not closed

> **F2 says the door is met only by reaching for the thing it guards. Registration says a stranger arrives
> with no grant and no link. Those two cannot both be satisfied by the same surface.**

Three honest readings, all consistent with something Paul has already ruled. **Not resolved here:**

- **(i) Two doors, and only one of them is F2's.** The *vault* door stays where F2 put it, in place, at the
  boundary. A separate **entry** door lives at the front and is met only by someone with no grant — which is
  never Mom on her own phone, and always a person on a new device. F2 is preserved by scope, not overridden.
- **(ii) The door is an empty state, not a page.** `estate/` and `homes/` already have the exact empty state
  where it belongs (§1.3 row 3), and it currently says *"open your invitation link."* Adding *"or sign in"*
  there is the smallest possible change and adds **no new surface at all**.
- **(iii) A front door for everyone.** Simplest to explain, and it is the one option that ⛔ **contradicts
  F1a outright** if it is ever reached before first paint. Named because it is what an implementer will
  build by default (F1's own warning), so it needs to be rejected in writing rather than by silence.

⭐ **(ii) is the cheapest and it costs no new pixels** — the same shape of argument the ux seat used to win
the selector into the masthead. It is not recommended here, because which reading is right depends on §5's
answer and on whether a landing page exists, and both are Paul's.

---

## 4 · THE STANDARDS — checked, cited, and three places this product already diverges

⭐ **CHECK THE STANDARD BEFORE BUILDING THE FIELD** `[paul-stated 2026-09-05]`. Everything in this section was
looked up today rather than recalled.

### 4.1 What the specs actually say

| # | the standard | what it requires | source |
|---|---|---|---|
| S1 | **NIST SP 800-63B-4** (final, July 2025) | Passwords used as a **single factor SHALL be ≥ 15 characters**; ≥ 8 only when part of multi-factor. **Composition rules SHALL NOT be imposed.** Verifiers **SHALL** check the candidate against a blocklist of known-compromised passwords. **SHOULD** permit ≥ 64 characters. | [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) |
| S2 | **WCAG 2.2 SC 3.3.8 · Accessible Authentication (Minimum), AA** | A **cognitive function test** (remembering a password) must not be required unless an alternative or an assist mechanism exists. **Unrestricted copy-paste into password fields** is a named, sufficient assist; blocking paste is a documented failure. | [W3C WAI](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) |
| S3 | **OWASP Authentication Cheat Sheet** / **Top 10:2025 A07** | **One generic failure message** for unknown-user, wrong-password, locked and disabled alike. **Rate-limit by IP and by account.** Prefer progressive delay and short temporary lockouts over permanent ones — an aggressive lockout is itself a denial-of-service against the real person. | [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) · [A07:2025](https://owasp.org/Top10/2025/A07_2025-Authentication_Failures/) |
| S4 | **HTML Standard · autofill field names** | `autocomplete="username"` + **`current-password`** on a *sign-in* form; **`new-password`** on create/change. The tokens are what let a password manager tell the two forms apart. `autocomplete="current-password webauthn"` resolves a pending conditional-mediation WebAuthn request instead of autofilling. | [WHATWG HTML](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) |
| S5 | **web.dev / Chromium sign-in form guidance** | Where username and password are split across steps, **include the username field in the form that collects the password** (hidden by CSS if needed) or managers cannot pair them. Doing nothing exotic is the design: forms that follow the conventions work across every manager. | [web.dev](https://web.dev/articles/sign-in-form-best-practices) · [Chromium](https://www.chromium.org/developers/design-documents/form-styles-that-chromium-understands/) |
| S6 | **Apple · Account Recovery Contact** | A real, shipped precedent for *recovery is a person*: up to five trusted contacts generate an out-of-band recovery code. ⭐ **Note the asymmetry that matters here** — Apple's recovery contact **cannot read your data**; the code only unlocks recovery. §5 has no such split unless one is designed. | [Apple Support](https://support.apple.com/guide/security/account-recovery-contact-security-secafa525057/web) |

### 4.2 Where the shipped account-creation surface already conflicts

| # | 🔬 measured today | against | reading |
|---|---|---|---|
| D1 | `ACCOUNT_MIN_WORD = 8`, and the copy says *"Eight characters or more."* | **S1** (≥ 15 for a single factor) | ⛔ **Roughly half the current floor.** ⚠️ And the honest counterweight is real: a 15-character minimum lands on a reader whose documented fear is getting things wrong, and S2 is the reason it is not a simple "raise it". **A genuine trade, and Paul's** (§7 R3). |
| D2 | `PBKDF2_ITERATIONS = 100000`, with the code's own note that this is the **Workers platform ceiling**, below OWASP's 210,000 floor for PBKDF2-SHA256 | OWASP KDF guidance | ⚠️ **Already recorded as a known shortfall** in the code, not hidden. It is an argument about the *host*, not about this door — noted so it is not re-discovered as new. |
| D3 | No blocklist check anywhere on `handleAccountCreate` | **S1** | ⚠️ Missing. Cheapest honest version is a small local list of the top few thousand, not a network call to a breach API — this product has a no-outbound posture and a k-anonymity range query is still an outbound call about a person's secret. **Scoped, not built.** |
| D4 | `autocomplete="username"` and `new-password` are correct on the creation form | **S4** | ✅ **Already right.** The sign-in form needs **`current-password`**, not `new-password` — the one token that distinguishes them. |
| D5 | Nothing blocks paste; the field has a **Show** toggle | **S2** | ✅ **Already right**, and the Show toggle is a real assist mechanism for the no-glasses reader. |
| D6 | `handleSession` returns **one** failure shape (`404 not-found`) for unknown-username and wrong-password alike, with a dummy `derive()` on the miss so the timing does not leak | **S3** | ✅ **Already right, and better than most.** The dummy derive is a genuine constant-time posture, not a comment claiming one. |

### 4.3 ⛔ Two findings the privacy seat could not have weighed, because the route did not exist when it ran

🔬 Both measured 2026-09-07 on the working tree; both are on **staging only**, never production (§1.2), which
is the right time to raise them.

- **P1 · `Access-Control-Allow-Origin: "*"` now sits on a route that returns a credential.**
  `CORS_HEADERS` sets `"*"` globally. The privacy seat ruled *do not tighten it* — correctly, because CORS
  restrains browsers not clients, and `*` is what keeps the ungated capture path alive from any device.
  **That ruling was made when no route returned a credential.** `/api/session` does. Any site a person
  visits can POST guesses from their browser and read the response. ⚠️ **This is not a reversal of the
  seat — it is the one route its premise does not cover**, and `.engineering/2026-09-05-account-credential.md`
  §3.5 already named it. It is **still open** today.
- **P2 · `/api/session` and `/api/account` have NO rate limit.** 🔬 `keyFor(..., "ratelimit", ...)` appears
  three times in the Worker: `door`, `feedback`, `obmetrics`. Neither credential route has a bucket. Against
  **S3** that is the single largest gap in the mechanism, and it is one call site each — the machinery is
  already written and proven on three other routes.

⛔ **Neither is fixed here, and neither should be fixed as a side effect of building a surface.** They are
the privacy seat's to review as a pair, because the fix for P1 (echo the Origin when it is a known host)
touches a header the seat deliberately left wide.

---

## 5 · ⛔ THE RECOVERY QUESTION — options, costs, and NO answer

**Why this is the hardest problem in the lane and not a form.** `onboarding/index.html` asks *"How should
Paul reach you?"* with three answers, and the third is **"Please don't."** The file's own comment states the
consequence: that branch *"closes the only route to a forgotten password."* Two seats plus `ux-expert`
flagged it independently. **So recovery is a policy question about a person who declined to give you a
channel — and the product currently lets them decline without the system having any second route.**

🔬 **And nobody has ever walked it.** `read-onboarding.py` returns **zero** `onboard-contact` answers across
`qa`, `lab` and `home`; the four synthetic seats (`mom`, `owner`, `wide-eyed`, `strict`) set no contact
preference at all, so the pre-selected `email` default rides in every run — including `strict`, the seat that
exists to exercise exactly this posture. **The refusal path is unexercised by anyone, synthetic or real.**

⛔ **Off the table before the options start:** making contact mandatory. It reverses a shipped promise Paul
calls the product's *"newest and boldest"*, and *"Please don't"* being a real answer is the whole point of
asking the permission before the detail.

### The options, each with what it costs the person

| | **A · The administrator is the reset path** | **B · A recovery code the person keeps** | **C · Email, where they gave one** | **D · A second device already signed in** |
|---|---|---|---|---|
| **what happens** | They tell the administrator; a terminal command rewrites the account row's salt+hash | At creation the system shows a one-time code; entering it later sets a new password | A reset link to the address on the account row | An already-trusted device authorises a new one, Apple-style (S6) |
| **works for "Please don't"?** | ✅ **yes** — the only option here that does | ✅ yes | ⛔ **no** — it is the branch they closed | ⚠️ only if a second device exists |
| **what it costs the person** | ⛔ **They must be able to reach a specific human, and that human can read everything behind their door.** At Fernwood that is family. At another estate it is a person they may have met once | ⚠️ **A thing to keep.** The failure mode is losing the code and the password, which is the same person on a worse day. WCAG S2's cognitive-function concern applies to the code too | Nothing — but only for people who gave an address | ⚠️ Nothing, when it works; **useless in the case that actually happens** (one phone, replaced) |
| **what it costs the product** | ⭐ **It is a statement about the operating model, not the UI** — see below | Moderate: one more secret to store, show once, and never show again | ⛔ **The Worker has no send capability today, by design.** Adding one adds a channel the tone charter closed, plus deliverability, plus a new failure surface | High: pairing protocol, and it is the largest new code surface on the table |
| **precedent** | S6's shape without S6's split | Standard practice; every 2FA product ships one | Universal, and the one the product declined | Apple Account Recovery Contact (S6) |
| **already exists?** | ✅ `grant-mint.py --rotate` deletes the hash row today; the account-row half is a small extension | ❌ | ❌ | ❌ |

### ⭐ The thing to say plainly, which is the reason this is Paul's and not an agent's

> **A is probably right, and A means Paul is the reset path — for every household, including ones he has
> never met.** That is a claim about how the business runs, not about a button. It says the product cannot
> onboard a household faster than one person can answer a phone, and it says the administrator can read
> anything behind anyone's door. **The second half is already true and already stated** — the account-credential
> seat wrote *"because Paul can reset her password, Paul can read everything behind it… the threat model is a
> stranger with the URL, not Paul."* ⭐ **Choosing A makes that a product property rather than an
> implementation detail, and copy that implies privacy-from-the-administrator would be false.**

⚠️ **And the honest note on A's ceiling:** the 2026-09-02 amendment already made the gate a **ROLE**, not a
person, precisely so this generalizes — but it also attached a duty, *"an administrator who is not a member
of the household reads that household's notes, voice and Guru turns… requires explicit up-front agreement
before the first contributor input."* **A recovery path routed through that role inherits that duty.**

⛔ **This document does not choose.** The options are the deliverable; the ruling is R1 in §7.

### One constraint that binds whichever option wins

⭐ **A failed sign-in must write a `door_failed` record.** The machinery is built (`storeDoorRecord`, its own
rate bucket, `ctx.waitUntil`) and 🔬 `door_reached = 0` is a truthful baseline today because no door exists.
The moment one does, **nothing in the record distinguishes *"locked out"* from *"didn't want the private
tier"*** — the same invisible-failure shape this project has now recorded three times (the empty answer
record, the undiscovered selector, the un-activated grant). **Instrument it in the same commit as the route,
or the lockout is invisible and it will be found weeks later.**

---

## 6 · THE THREE SURFACES, SCOPED

**Naming, checked against `VOCABULARY.md` §3b/§4 before proposing anything.** The words are already ruled:
**username** and **password** `[paul-stated 2026-09-05]` — ⛔ not *"a word only you know"*; **entry door** for
the schema-side thing; **the safe** for the reader-facing vault door; **activation** for a first credential
and **login** for the returning act — *they are different words for different journeys and this door is the
second one*; **"your homes"** as the product-level greeting; and **the top bar always answers "where am I"**.
⛔ **No new noun is proposed by this file.**

### 6a · Sign in
- **Two fields, in one form**, `autocomplete="username"` and **`current-password`** (S4/S5/D4). Nothing exotic.
- **One generic failure** — `/api/session` already returns exactly one shape (D6). The *copy* must match the
  mechanism: it may not say "no such account", ever. ⚠️ Copy is content-steward's.
- **Takes the blame, in the register, in the palette** (ux F2 / research §5.2): not *"Session expired"*, not
  *"Please sign in again"*, no red, no ⚠️, no alert chrome.
- **On success the client stores the returned token and nothing else it can derive.** ⛔ ux F7: one resolver.
  The client renders *from* the trust state and never re-derives it.
- ⛔ **It must not be reachable before first paint** (ux F1a). Whatever §3.3 reading wins, the falsifier is
  unchanged, and the tool for it is **declared in C6 § Files touched and 🔬 does not exist yet** (`ls tools/ | grep glance` → nothing): `check-glance-ungated.py`. Building it is step 4's first act, not an assumption.

### 6b · Create an account from the same door
- **A link to the existing `onboarding/` journey, not a second form.** Two account-creation surfaces is the
  divergence this repo pays for repeatedly; `onboarding/index.html` is already seat-reviewed, walked and
  instrumented.
- ⚠️ **The `!read(K_USER)` routing test (§1.3) is the actual defect and it is upstream of this door.** Fixing
  it *is* adding a sign-in route: "do you already have one?" is answerable only by asking.
- ⭐ **Consider the order the standards imply:** on a device with no state, *sign in* is the returning act and
  *create* is the exception — but a registration product's front page conventionally leads with create.
  **Which leads is an evidence question, not an argument**, and there is no evidence yet (🔬 `read-onboarding`
  reports **0 real** answers in every environment; every walk to date is synthetic).

### 6c · Recover access
- **Whatever §5 rules, the affordance is a slot with one rule: it must name the real route.** The creation
  screen already models this — it was changed `[paul-confirmed 2026-09-05]` from *"there's no email reset"* to
  naming the thing that actually works, on the reasoning that *a true sentence pointing the reader away from
  the one working door is worse than a vague one.*
- ⛔ **No "Forgot password?" link with nothing behind it.** ux F2 ruled the footer is a person; the
  account-credential seat noted that this became load-bearing rather than stylistic.
- ⭐ **P6 is pending, not claimed:** *"signify a person-to-person channel with the person's FACE"* reaches its
  second occurrence here if this ships as drawn. It has not shipped, so it is not promoted.

---

## Files touched

⛔ **NOTHING IS TOUCHED BY THIS DOCUMENT.** This section declares what a *build* would touch, so the blast
radius is visible before it is authorised — every row is gated on §7.

- **`onboarding/index.html`** — the routing test at the bottom of the file (`!read(K_USER)` → `s0`), which is
  where the middle state of §1.3 is decided; a sign-in view beside `s0`; the recovery slot's copy.
- **`estate/index.html` · `homes/index.html`** — the no-grant empty states, if §3.3 reading (ii) wins.
- **`worker/worker.js`** — ⛔ **no new route is needed for sign-in**; `/api/session` exists. What a build
  would add: a rate-limit bucket on `/api/session` and `/api/account` (P2), an Origin-scoped ACAO on those two
  routes only (P1), a `door_failed` write on a failed sign-in, and — if §5 rules D3 in — a blocklist check on
  create.
- **`tools/grant-mint.py`** — a `--rotate-password` if §5 rules **A**.
- **`tools/journey-walk.py` · `tools/synthetic-identity.py`** — a seat that actually chooses *"Please don't"*,
  so the refusal path stops being unexercised.
- **`tools/check-storage-keys.py`** — any browser key the door writes must be rostered or the origin move loses it.
- **`RELEASE_NOTES.md`** — a sign-in door is user-facing.
- ⛔ **NOT touched, by rule:** `viewer.html` (the door is not on her glance), `PRODUCT-ENGINE.md` and
  `VOCABULARY.md` (a ruling goes in the register *by Paul*, and §7 R4 is exactly that), `BACKLOG.md`.

## Sequence

⛔ **Nothing here starts.** Each step names **who** · **reversible?** · **the deterministic check**. Ordered so
that the two things that make the door *safe* land before the thing that makes it *reachable*.

**0 · Paul rules §7.** — **Paul** · — · no step below opens without R1 and R2. R1 in particular changes what
6c even is.

**1 · The privacy seat re-runs on its moved premise.** — agent or checklist, Paul's call · — · scope is
narrow and named: P1 (ACAO on a credential-returning route) and P2 (no rate limit on either credential
route), plus whatever §5's ruling adds. ⛔ **Step 3 does not open until it has run** — the same gate C6 set,
for the same reason.

**2 · Rate-limit and Origin-scope the two credential routes.** — agent · reversible · the `feedback`/`door`
bucket idiom, a second bucket keyed by **account** as well as IP (S3 asks for both). Check on the QA Worker:
N failed sign-ins from one IP → 429 **while a feedback POST from the same IP still lands** (the separate-bucket
positive control that `qa-write-probe.py` already runs for the door); a cross-origin POST to `/api/session`
carries no ACAO; the capture POSTs are untouched from any origin.

**3 · `door_failed` on a failed sign-in.** — agent · reversible · one call site into machinery that exists.
Check: a wrong password on QA leaves a `door:<date>` record with a reason; a right one does not; ⛔ and no
`personId` is stamped on a failure (identity is not applied backwards — a failed credential attributes nothing).

**4 · The sign-in surface.** — agent builds, **Paul walks** · reversible · two fields, S4's tokens, one
generic failure, the trust state read from one resolver. Check: `check-glance-ungated.py` (**to be built here — it does not exist today**) — fresh context,
414 × A+, all `/api/*` blocked: masthead, jump strip, six destinations, weather card and composer render and
accept input, **and the viewer's own marker is present or the tool throws**; zero requests to gated routes
before the first-paint marker, signed in or out.

**5 · The routing fix.** — agent · reversible · `onboarding/`'s returning-reader test stops being
device-local. Check: a walk that creates an account, clears storage, and gets back in **without a link** — the
promise in §1.4, tested rather than asserted.

**6 · Recovery.** — **Paul rules, then agent builds** · reversibility depends on the option · gated on R1.

**7 · A walk seat that refuses contact.** — agent · reversible · a fifth synthetic seat, or an existing one
re-pointed, that chooses *"Please don't"* and then loses its password. Check: `read-onboarding.py` reports a
non-zero `onboard-contact` count with a `none` value — 🔬 it is **0** in every environment today.

## Falsifier

For the design as a whole. Each is an observation and how it is measured.

- **The door reached her glance.** Measured: `check-glance-ungated.py` (once built) logs any request to the Worker before
  the first-paint marker, signed in or out; or first paint differs between the two states. If true, ux F1a is
  violated whatever the code intends, and the build stops.
- **A locked-out person is invisible to the record.** Measured: a wrong credential on QA produces no
  `door_failed`; or the reader prints `0` where the route did not exist. If true, *"doesn't want it"* and
  *"can't get in"* are still one observation and the door must not ship.
- **The door invented a second resolver.** Measured: the client decides what to render from anything other
  than the one trust state — `grep` for a client-side re-derivation beside a Worker verdict. If true, ux F7's
  fourth occurrence has arrived and the answer is not another reconciliation layer.
- **Trust is revoked by a clock.** Measured: a `Date` comparison inside the sign-in path, or a TTL on a
  `grant:` key. ⚠️ Sign-in *rotation* is not expiry — a person asked; note the distinction or the next reader
  reads a green check as a violation.
- **Two account-creation surfaces exist.** Measured: `grep -c 'new-password'` over the tracked tree returns a
  form outside `onboarding/`. If true, 6b was built as a copy and the divergence has already started.
- **A person who declined contact cannot get back in.** Measured: the §Sequence-7 seat completes a walk that
  refuses contact, loses the password, and reaches its place again. If it cannot, §5's ruling did not actually
  cover the branch the product ships.
- **The standards claim is stale.** Measured: S1's ≥ 15 and D1's `ACCOUNT_MIN_WORD` still disagree at the time
  a build starts, with no `[paul-ruled]` line reconciling them. A divergence Paul chose is fine; an
  undocumented one is the defect.
- **This document is ceremony** (readiness §5, discharged in a `## Retro` if this is ever stamped): the parts
  that exist only because something was executed rather than recalled — today §1.2 (the route is built), §4.3
  P1/P2, §5's zero contact answers, §1.3's `K_USER` test. Zero at retro is a valid, informative answer.

## QA

**An agent may exercise, and where.** Nothing in this document was exercised beyond read-only measurement:
🔬 marks in §1, §4.2 and §5 are `grep`, `git show`, and `read-onboarding.py --env {qa,lab,home}` — no write,
no deploy, no production call. When § Sequence opens: steps 2–3 and 5 on the **QA Worker only**, plant and
read back and delete, with fixture accounts; step 4 on the QA origin via Playwright at **414 × 848 × A+**
(`herConditions()`), never `main`. On production, permanent: **read-only**.

**Agent may NOT:** mint or hold a credential value outside `/secrets`; rotate production `SHARED_TOKEN`; write
a ruling into `PRODUCT-ENGINE.md` or `VOCABULARY.md`; word any screen a person reads; choose the recovery
option; touch her device or her origin's storage; write `- ready:`.

**Paul verifies:** R1–R5 before the steps they gate; the first real sign-in on his own device; the walk in §5
that refuses contact; `check-live.py --wait 180` after any shipped surface.

**Presence of a person: none.** ⛔ Every walk in this scope is synthetic, and 🔬 `read-onboarding` reports
**0 real** answers in every environment — which is a statement about the evidence base for §6b's ordering
question, not a gap to fill by asking someone.

---

## 7 · ⛔ WHAT ONLY PAUL CAN RULE — five, smallest last

These stay open. ⚠️ **A ruling that is not in the register is not in force** — whichever way each goes, it is
written into the citing file *before* anything is built on it.

1. **R1 · RECOVERY — which option in §5, and does the administrator become the reset path for households he
   has never met?** ⭐ The largest one. It is an operating-model decision wearing a UI question's clothes, and
   every other row waits on it. ⚠️ Whichever wins, the *"Please don't"* branch has to be covered or removed,
   and removing it reverses a shipped promise.
2. **R2 · WHERE THE DOOR STANDS — §3.3's (i), (ii) or (iii).** ux F2's *"a door belongs to the room"* was
   ruled under closed enrolment; registration puts a stranger outside every room. (ii) costs no new surface;
   (iii) is what an implementer builds by default and needs rejecting in writing.
3. **R3 · THE PASSWORD FLOOR — 8 (shipped) or 15 (NIST SP 800-63B-4 for a single factor)?** A real trade, not
   a compliance box: 15 characters lands on a reader whose documented fear is getting things wrong, and
   WCAG 3.3.8 is why *"just raise it"* is not the obvious answer. **Related and cheap: does a blocklist go in
   (D3)?**
4. **R4 · THE REGISTER DISAGREES WITH THE CODE ON EMAIL AND PHONE.** `PRODUCT-ENGINE.md` still says both
   *"have no job"*; `onboarding/index.html` collects both `[paul-stated 2026-09-05]` and names the reversal in
   its own comment. **One of the two is wrong and the engine document is the one that governs.** A sentence
   in the register closes it.
5. **R5 · HOW THE PRIVACY SEAT RE-RUNS — agent or checklist.** Same fork C6 answered once (it chose an agent,
   and four of fifteen findings existed only because something was executed). Its premise has moved: it
   reviewed a world with no credential-returning route.

> ### 🚪 THE ASK, IN ONE PARAGRAPH
> The mechanism for signing in is **built and proven** — it just has no door and nobody has decided what
> happens when someone forgets. **The expensive question is R1**, and it is not a UI question: choosing
> *the administrator resets it* means the product's recovery path is a person answering a phone, and that
> the administrator can read anything behind anyone's door. That is worth ruling deliberately rather than
> discovering it the first time a stranger is locked out. **Everything else in this file waits behind it,
> and nothing in it has been built.**
