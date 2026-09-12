# Sign-in door · what it may claim about what it reveals — security-steward

- question: `.plans/2026-09-11-lap8-build-PLAN.md` §9 **Q3**, which blocks step **A13**
- seat: security-steward, mode ③ legibility with a mode-① disclosure ruling underneath
- commissioned: 2026-09-12, lap 9, after A2's conversion landed so it read converted code
- ⛔ **FLAG, NOT SETTLED. Paul clears.** `settled_by: source` · `authority_checked: false`

## 0 · Denominator — what was examined, and what was NOT

**Examined by symbol:** every `worker.js` route reachable without a grant (`handleAccountCreate` ·
`handleSession` · `handleUsernameChange` · `/api/account/available` · `/api/recover` ·
`/api/onboarding-metrics` · `/api/door` · `/api/estate` · `/api/profile` · `/api/grant/whoami`) ·
**all 20 occurrences of `email`, read individually rather than counted** · `onboarding/index.html`'s
door, recovery block and availability client · `VOCABULARY.md` §3e·R ·
`.content/2026-09-11-recovery-copy-DRAFT.md` · `.engineering/2026-09-10-recovery-route-SECURITY.md`.

⛔ **NOT examined, and each is a real hole in this ruling:**
1. **Nothing was run.** The seat has no Bash by design. Every claim is from SOURCE at the working
   tree, never from live traffic. **A source claim cannot say what an origin actually answers.**
2. `check-error-oracle.py` was not run; its three routes were re-verified by source instead.
3. ⛔ **The lap-9 one-origin code DOES NOT EXIST**, so this reads a DESIGN, not a build.
   `grantFor`'s `row.estateId !== env.ESTATE_ID` rejection still stands; nothing one-origin is
   testable today.
4. ⚠️ **Timing was NOT measured.** The constant-404 path is argued from source (the dummy `derive()`
   on the no-account branch, `waitUntil` on every deny). **A source argument for timing equality is
   weaker than a measurement and is not treated as settled.**
5. `settings/account/`'s use of the availability route — that is Q4's object, not Q3's.
6. ⛔ `/api/door`, metrics and feedback write paths **as disclosure channels** are out of scope and
   therefore **uncleared by this**.

## 1 · Username existence IS published — three symbols, one more than the plan names

| symbol | discloses | to whom |
|---|---|---|
| `/api/account/available` → `accountFor(...)` → `{available, username}` | username existence, **by design** — its own comment reads *"A USERNAME ORACLE, KNOWINGLY"* | anyone |
| `handleAccountCreate` → `409 username-taken` | the same fact | anyone |
| ⚠️ `handleUsernameChange` → `409 username-taken` | **the same fact a THIRD time — not named in the plan.** Behind `grantFor`, so **member-tier**, not public | any credential-holder |

✅ **`handleSession` is CLEAN and is not in this list.** `deny()` returns one byte-identical
`{"error":"not-found"}` for *no such account* and *wrong password*; the no-account branch burns a
dummy `derive()`; the refusal record carries `reason: "signin-refused"` and **never the attempted
username**. Sign-in itself is not an oracle.

⚠️ **Plan citation decay, measured:** §6 A13 cites `:4374–4384` and names `feedbackRateLimitOk`; at
HEAD the route is ~160 lines lower and calls **`probeRateLimitOk`**. **A13 clause (ii) — "its own rate
bucket" — is ALREADY DONE** (lap 7 · B0). A13's remaining scope is clause (i): this ruling.

## 2 · Email existence is NOT disclosed — the plan is right, verified by symbol

**No email index of any kind exists.** `email` is a field on the account row, echoed back **only to a
caller holding a credential**. **No route resolves an account FROM an address.** `/api/recover`
performs **no lookup**: the address is shape-checked and dropped — never stored, compared or echoed.

⚠️ Two response shapes vary (`503 not-recorded`, `429 rate-limited`) and **both vary with the SERVER,
never with the truth about the address.** Ruled non-disclosing.

⭐ **Adjacent, out of this ruling, stated so it lands in someone's denominator:** a credential-holder
on a shared or handed-down device is shown the account's recovery address by `/api/session` and
`whoami`. Correct tier under §3e·R — but **the recovery address is visible to whoever holds the
phone**, and §3e·R's security rests on that address. File where row C lives.

## 3 · ⭐ One origin changes the STAKES and the CLASS OF HARM, not the truth value

- **Both rulings are invariant.** *"We never reveal whether an account exists"* is false at one
  deployment and false at one origin, for the same symbols. *"We do not confirm whether an email
  address is on file"* is true in both, for the same reason.
- **What moves is what the disclosed fact MEANS.** Today: *"someone at this house uses this name"* —
  near-zero harm, the household already knows each other. At one origin usernames must be **globally
  unique**, so the same probe reads ***"this named person is a customer of this product."***
- ⭐⭐ **That is a MEMBERSHIP disclosure about a named individual, not a credential disclosure** — and
  the mechanism is that the username is self-chosen and unconstrained (`/^[a-zA-Z0-9._-]{3,40}$/`,
  labelled *"Your username"*, nothing steering anyone away from their own name). At one origin
  *is this name taken* converges on *does this person have an account here*.
- ⭐ **Under Paul's own frame this costs INPUT, not data** — the asset is a named person with a stated
  duty, at small scale, in a community where people know each other. **A neighbour checking whether
  another neighbour signed up is the fact that frame cannot afford to discover late.**
  ⛔ **Mode-① roster question for lap 9 — `tier: username × global origin` — UNRULED.**

⛔ **The obvious hardening does net harm.** Deleting `/api/account/available` costs a real person a
bounced signup form and protects nothing, **because the 409 publishes the same fact**. Tightening the
rate limit is worse than neutral: `probeRateLimitOk` keys on `CF-Connecting-IP` and **the property's
founding premise is ONE EGRESS IP** — a tighter budget lands on a household of three signing up
together before it lands on anyone with more than one address.

⚠️ **NEW, and unruled:** `probeRateLimitOk` ends `catch (e) { return true; }` — **it fails OPEN**,
while its sibling `recoverRateLimitOk` fails **CLOSED** with its reasoning written down. Fail-open is
correct for **capture** (a limiter outage must never eat her words) — **but this route is a READ
ORACLE, not capture**, and its only rate control disappears during a KV outage. The rule was inherited
from capture and never re-argued for a read. **Question, not verdict.**

## 4 · The claims — ⛔ the seat rules the CLAIM and does not write the copy

✅ **MAY be claimed (true at HEAD, by symbol):**
1. *This page does not say whether an email address is on file.* — TRUE. No index, no lookup.
2. *A recovered credential goes to the address the account already holds, not the one typed here.* —
   TRUE (§3e·R), and it is what makes #1 useful rather than obstructive.
3. *A refused sign-in does not say which of the two things was wrong.* — TRUE (`deny()`), ⚠️
   **truth-conditioned on timing, which was argued from source and NOT measured.**

⛔ **MAY NOT be claimed:**
4. *We never reveal whether an account exists.* — **FALSE**, three symbols, falsifiable in one
   request. Concurs with `.engineering/2026-09-10-recovery-route-SECURITY.md` §R-E.
5. **Any generalisation of #1 to usernames** — *"we don't confirm whether you have an account"*. Same
   falsehood in softer clothes, **and this is the failure a build window will actually produce**: the
   email sentence reads like a general privacy stance and gets copied across one field.

⭐⭐ **THE FINDING A13 SHOULD ACT ON, which is not what Q3 asked.** Claims #1 and #2 **ALREADY SHIP**,
in content-steward's words, Paul-confirmed 2026-09-11, at `onboarding/index.html` `#recover`, rationale
at `.content/2026-09-11-recovery-copy-DRAFT.md`. **So Q3's recommendation is largely a request to
re-mint live copy. A13 must CITE that string, not author a second one** — a second sentence saying the
same thing in different words is how a claim drifts out of true while both copies look confirmed.

⭐ **The real gap is the USERNAME half, and it is a PLACEMENT question, handed off rather than
answered.** The unsaid fact is created when a person **CHOOSES** a username (signup, where the
availability check runs and the 409 fires), not when they **USE** one. ⛔ **On the sign-in door the
fact is not actionable** — you cannot un-choose a name you are typing to get back into your own house,
and a warning there spends a locked-out person's attention on something they cannot act on.
**ux-expert owns placement; content-steward owns the words. A sentence appearing on the sign-in door
would be flagged NET-HARMFUL.**

## 5 · The adjacent channel the door's sentence does not cover — confirmed by source

Three unauthenticated routes return an exception message in a 500: `/api/account` (carries its own
*"DEV-ONLY… must not survive into production"* comment, and survived) · `/api/account/username`
(**no such comment**) · ⭐ **`/api/session` — the sign-in path, no such comment.**

⭐ **Why it belongs to Q3 and not only to row 92:** `handleSession`'s entire design is ONE CONSTANT
REFUSAL. A 500 there is a **second, unconstrained response shape on the same door**, whose body was
never designed and which no sentence describes. The lookup keys on `accountKey(scope, username)`, so a
KV-layer throw can put **the estate id and the attempted username** into a message — **the exact value
`deny()` refuses to write into the record, arriving at the caller instead.**

⚠️ **NOT claimed:** that this is exploitable or a username oracle. **It is not** — it fires on
unexpected throws, which do not vary with whether the account exists, so it cannot be summoned by
choosing a body. It is a **disclosure channel of unknown content**, not a controlled oracle.

⭐ **Actionable part is SCOPE, not severity: BACKLOG row 92 names ONE route; the class is THREE**, and
the two omitted are the rename path and the sign-in path. **Widen the row.**

## 6 · Carried forward

| | |
|---|---|
| verdict | the plan's Q3 posture **CONCURRED**, with three amendments |
| amendment 1 | the ✅ sentence **already ships** — **cite it, do not re-mint** |
| amendment 2 | the real gap is the **username** half; a **placement** question → ux-expert + content-steward |
| amendment 3 | a **third** 409 site (`handleUsernameChange`) the plan does not name; member-tier |
| carried | ⭐ lap-9 roster row: **username × global origin = membership disclosure about a named person** |
| carried | `probeRateLimitOk` **fails OPEN on a read oracle** while its sibling fails closed — unruled |
| carried | **row 92 names 1 of 3 routes**; `/api/session` is one of the two omitted |

## 7 · Falsifiers a person can actually run

1. `GET <origin>/api/account/available?u=<a name you believe exists>` → `{"available":false}` kills
   claim #4 in one request.
2. `POST <origin>/api/account` with an existing username → `409 username-taken`. **Run this one too —
   it is why deleting route 1 fixes nothing.**
3. `POST /api/recover` with an address that exists and one that cannot; `POST /api/session` with a
   real username + wrong password, and a username that does not exist. Both pairs must be
   **byte-identical**. ⚠️ **Compare elapsed time as well as bytes** — the unmeasured half.
4. Once one origin is live: if `/api/account/available` answers for a name belonging to another
   household, the enumerable space is global and the roster row is owed.
5. ⚠️ **Send a User-Agent** — the edge 403s UA-less clients before the Worker runs, and that 403 is
   not evidence about any of this.

⛔ **Nothing here is cleared.** Three of five falsifiers are unrun, timing is unmeasured, the lap-9
world does not exist, and this covers exactly two facts at one door.
