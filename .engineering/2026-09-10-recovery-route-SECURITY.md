# Recovery route — security-steward read (roster + legibility) · lap 7 row B · B5/B6/B7/B9/B10

<!-- filed VERBATIM by the coordination window (tate-tracker-ea) 2026-09-11 ~12:40 AM ET from the seat's return;
     commissioned at 7b36392 after the build window's readback found no security read of the recovery route
     (handoff/handoff-lap7-build.readback.md §5 item 4). The seat has no write tool; nothing below is edited.
     ⚠️ The seat did not read the build plan's §6–§9 and ran no probe; its own DENOMINATOR section states this. -->

**SECURITY-STEWARD — lap 7 row B · the RECOVERY route · modes ① ROSTER and ③ LEGIBILITY**

Repo `/Users/paulkirschenbauer/Developer/Tate-Tracker`. **Symbols cited; line numbers are as read in the working tree this session.** The caller reports HEAD `7b36392`; I have no `Bash` and **could not verify the sha** — if `worker.js` has moved, trust the symbol, not the number.

---

## DENOMINATOR FIRST — what this run covers, and what it does not

**Read and verified by me:** `.plans/2026-09-10-lap7-build-PLAN.md` §1, §2 (A1–A10), row P, row D, row C, row B **B1–B15**, row H, §4 SEAMS, §5 (I did **not** read §6–§9; see below) · `.ux-reviews/2026-09-10-lap7-design-closure.md` rows 19, 25–33, 41–44, the 15-tap lifecycle journey, *What I did NOT decide* · `cycle/release/CYCLE-LOG.md` beat-6 table + the AMENDED Q1–Q8 block · `.engineering/2026-09-10-cross-device-signin-SECURITY.md` (my own prior run, whole) · `.plans/2026-09-10-founding-flow-design-PLAN.md` R1–R3, D1, **D4 items 1–4**, D4's falsifier · `VOCABULARY.md` §3e, §3f · `worker/worker.js` symbols `handleSession` (incl. `deny`, the dummy `derive()`, the rotation block, the response literal), `handleFeedback`, `feedbackDestination`, `accountFeedbackKey`, `ACCOUNT_SURFACES`, `declarePerson`, `stampVia`, `feedbackRateLimitOk`, `doorRateLimitOk`, `DOOR_EVENTS`, `handleDoor`'s event guard, the `/api/account/available` route branch, the `/api/profile` account branch, the server-side `door_failed` writer, the `/api/grant/whoami` response literal, `ADMIN_ONLY`/`MEMBER_OK` · `settings/account/index.html` the whoami read and `#save` handler · `tools/watch-feedback.py` (its label extraction and its no-note-text clauses) · `tools/grant-mint.py` `PLACE_FACTS` + its selftest clause.

**NOT checked, each of which could change a ruling:**
- **I did not read `.plans/2026-09-10-lap7-build-PLAN.md` §6–§9.** §9 is where the plan says its NEEDS-PAUL rulings live, and **B6's own text points at §9 for the channel question.** I am ruling on B6 from B6 and from Q4. If §9 already answers something below, mine is the second voice, not the first.
- **I ran no network probe and read no live KV.** Nothing here is a measurement of a deployed Worker. A deployed binary older than the tree invalidates every code ruling silently.
- **I did not enumerate the route table.** Same gap as my 09-10 run: I examined the auth/feedback/door surfaces. A route I did not read may hold another oracle. This remains R1's missing denominator.
- **I did not read `tools/watch-door.py`** (B7's subject) beyond confirming `DOOR_EVENTS` in the Worker. Whether its roster is keyed on that constant is **inference** below, flagged as such.
- **I did not measure timing anywhere.** L1's transport falsifier and L12's "equally timed" are both still unmeasured, today, by anyone. See CHANGE-7.
- **I did not read `onboarding/index.html`'s sign-in failure branch instrumentation**, so I still cannot certify the client does not log an attempted username. My prior run said the same. **Two runs, same hole.**

---

# ① ROSTER

A tier is `estate × person × credential class`. The recovery caller's credential class is **none** — that is the defining fact and it drives half of what follows.

### The values the route creates, moves or reveals

| # | value | class | tier it lands in *as specified* | ruling |
|---|---|---|---|---|
| V1 | the **submitted email address** | contact / identity, **self-asserted and unverified** | the deployment's estate feedback stream, **member-readable** | ⛔ **MAY NOT EXIST AT REST.** See R-A. |
| V2 | **the fact an account exists** for that address | existence | the response (closed) + the record (open) | ⚠️ closed in the response, **re-opened in the record** if the record varies with the truth. See R-B. |
| V3 | **the fact a recovery was requested** | event | same stream | ⚠️ permitted **only** where it does not carry V1 or V2 and does not join to behaviour. See R-C. |
| V4 | the **username** (B9, signed-in twin) | identity | `account:<personId>:feedback:<date>` **only if** the build sets `context.surface` | ✅ permitted account-scoped; ⛔ forbidden estate-scoped. See R-D. |
| V5 | the **requester's IP** | network identifier | a TTL'd rate-limit key | ✅ permitted as a **declared** exception — RR-4 extended. |
| V6 | **timing** | side channel | the response | ✅ trivially constant *today* (there is no lookup); ⛔ **stops being constant the moment a lookup exists.** See R-E. |
| V7 | the **administrator's channel** — who learns, and how | reach | `watch-feedback.py`, i.e. a human running a tool | ⚠️ **not a channel; it is a sweep.** See ③-L2. |
| V8 | the **new credential**, delivered out of band | bearer credential | nowhere in this build | ⛔ **lap-8 question, and it is the whole point of the route.** See the close. |

---

### R-A · The `account-recovery` record as specified **cannot avoid** a member-readable tier

**This is the load-bearing finding and it is structural, not a wording problem.**

1. A locked-out person presents **no grant** — that is what locked out means.
2. `feedbackDestination(grant, context)` (`worker.js`, `:3938–3945`): **rule 1** is `if (!personId) return { kind: "estate" }`. No credential → the **place**. The `ACCOUNT_SURFACES` branch (`:3932`, `:3942–3943`) is unreachable without a `personId`.
3. So the key is `dateKey(scopeOf(env), "feedback", today)` (`handleFeedback`, `:3994–3995`) — the **deployment's** estate.
4. `GET /api/feedback` is in **`MEMBER_OK`**, not `ADMIN_ONLY` (`:4633–4642`), **`[paul-ruled 2026-09-10]`** with the consequence stated to him: *"on that estate a member can read the other's notes."*

> **Therefore: every recovery request lands in a stream any member grant at that deployment can read.** Not the administrator's inbox. The household's.

⛔ **And it lands in the stream the mom cycle sweeps.** `watch-feedback.py` and `read-mom-feedback.py --pickup` read that key. At `home` (Mom's household) a stranger's failed recovery attempt becomes an **arrival** — it needs a disposition under `check-arrival-dispositions.py`, it can hold the watermark, and per `mom-cycle-status.py`'s trigger doctrine **an unresolved arrival can FIRE a lap**. A lifecycle event would be entering the loop whose whole doctrine is *her words fire it*.

- `settled_by`: code read (`feedbackDestination`, `handleFeedback`'s key selection, the `MEMBER_OK` literal). `authority_checked: **true**` for the routing; **`false`** for the mom-cycle consequence — I reasoned that from CLAUDE.md's own description of the trigger, I did not read `mom-cycle-status.py`.
- **Falsifier (run before acting):** `python3 -c "import re;s=open('worker/worker.js').read();print('estate-only' if re.search(r'function feedbackDestination[\s\S]{0,200}?!personId\) return \{ kind: \"estate\"', s) else 'CHECK')"` then `grep -n '"/api/feedback"' worker/worker.js` and confirm it appears in `MEMBER_OK` and not `ADMIN_ONLY`. If `/api/feedback` GET is administrator-only, half this finding is void.
- ⛔ **Out of my lane:** Q4 is a ruling. I am not overruling it. I am stating the tier it lands in, which is not in Q4's text, and **the permitted field list below is the form of Q4 that survives this tier.**

### The permitted field list — what an `account-recovery` record may carry

`declarePerson()` (`:490–495`) **throws** if a literal carries `personId` or `estateId`, and `attributeTo()` is the only legal writer of a non-null person — from a **resolved grant**. A recovery caller has none. **So the record is structurally incapable of naming its subject.** That is not a limitation to work around; it is the guard working.

| field | ruling |
|---|---|
| `id`, `ts`, `env` | ✅ |
| `context: { type: "account-recovery" }` | ✅ — the label `watch-feedback.py` reads (`:156–157`, `:169–170` read `questionId`/`field`/`type`) |
| `personId`, `estateId` | ✅ **null by construction** — do not attempt to set them |
| `sessionId` | ⛔ **FORBIDDEN.** It is a join key into `/api/metrics` batches. A session id turns an outcome-only record into a pointer at a whole behaviour trace. This is not in the plan. |
| `deviceId` | ⛔ **FORBIDDEN.** The existing server-side `door_failed` sets `deviceId: null` explicitly (`:4467`) — copy that, do not omit it. |
| `note` | ⛔ **FORBIDDEN** — and note that `handleFeedback` **rejects** a record with neither sentiment nor note (`need-sentiment-or-note`, `:3962–3966`). **A genuinely outcome-only record fails that validation.** The handler must write the KV row itself rather than pass through `handleFeedback`, or carry a fixed non-personal sentiment token. **This is a build-blocking detail the plan does not name.** |
| the submitted address | ⛔ **FORBIDDEN** (R-A + R-B) |
| a matched / not-matched outcome | ⛔ **FORBIDDEN while the stream is member-readable** (R-B) |

### R-B · The constant response is defeated at rest, for exactly the adversary in the threat model

My own L3 rule: *keeping the response undifferentiated while differentiating the record moves the oracle rather than removing it — and the record is the more durable of the two.*

Concretely: a person holding **any member grant** at that deployment can submit addresses at the door and then `GET /api/feedback` and read the outcome. **The constant response protects them from nobody they are not already inside of.** The plausible adversary named in my L1 threat model is *"a person in an adjacent household"* — this is that person, exactly.

**Two exits, and they are not equivalent:**
- **(i) drop the outcome from the record.** Then the record is a doorbell with no name and the administrator cannot act — which is ③-L2's problem, not a solution.
- **(ii) ⭐ move the record out of the member-readable stream** — its own key, served by a route that is `ADMIN_ONLY` or by the master token only, with its own reader. This is the only exit that is both honest and actionable. **It is a change to Q4's "no new channel" and therefore Paul's.**

### R-C · What may be written unconditionally

A record that carries **only** `{id, ts, env, context:{type:"account-recovery"}}` with personId/estateId null, **written on every submission regardless of outcome**, is ✅ permitted in the estate stream. It tells the administrator *someone at this door is locked out and has asked* — which is a real signal and is the one that closes the *"nobody reads the failures of people trying to GET in"* gap from L3. It does not tell them **who**, and it must not.

### R-D · B9 (the signed-in twin) is permitted, with one line the plan does not name

Row 30 / B9 sends a request **naming the username**. The caller here **has** a grant, so `feedbackDestination` can reach the account branch — **but only if the build sets `context.surface` to one of `ACCOUNT_SURFACES` (`"onboarding"`, `"homes"`, `"account"`, `:3932`).** Omit it and rule 3 returns `{kind:"estate"}` and the username lands in the household stream, member-readable.

> **ROSTER ROW (proposed) RR-6:** *A record naming a person — their username, their contact value, or a fact about their access — may land only at `account:<personId>:…`. If the writer cannot supply an authenticated personId, the record may not name the person at all.*

- **Falsifier:** `grep -n 'surface' settings/account/index.html` at the new card's POST and assert the value is in `ACCOUNT_SURFACES`; then `python3 tools/watch-feedback.py --env qa` must **not** show the request on the estate's channel.

### R-E · There is no lookup path, so "if that address is on file" is not backed by anything

**Measured:** email lives on the account row (`handleAccountCreate`, `:655`, `:775`; `/api/profile`, `:4226`). **There is no `email:` index anywhere** — `grep -n "email" worker/worker.js` returns 12 sites and none is a key. `accountFor()` resolves by **username**, never by address.

So `POST /api/recover` as specified has **three** possible shapes and the plan does not say which:

1. **No lookup at all.** The response is constant because nothing was checked. ⭐ This is the most secure shape and the least honest one — see ③-L1.
2. **A `list()` scan** over account keys per request. An unauthenticated, rate-limited route that scans a namespace is a cost and latency lever; and **the scan's duration varies with the store**, not with the secret, so it does not leak — but it will be tempting to cache, and a cache does.
3. **A new `email:<lowercased>` index.** ⛔ **ROSTER RULING: a listable email index is a directory of the product's users' email addresses, at rest, keyed by the value itself.** KV keys are enumerable by prefix. That is a strictly worse artifact than the thing the constant response protects. If an index is built it must be keyed by a **salted hash** of the normalised address, never the address.

> **ROSTER ROW (proposed) RR-7:** *A contact value may be a KV **value**; it may never be a KV **key** or part of one. Keys are listable; values are not.*

⚠️ **And the deeper one: email is not an identity claim here.** It is never verified, it is not unique, and `/api/profile` lets any authenticated person set it to any string (`:4226`, no uniqueness check). **Anyone may set their own account's email to someone else's address.** A recovery flow that resolves address → account and hands the result to a human who then resets a credential is a support-channel takeover path. **Mitigated entirely by one rule, which must be written down and is nowhere today:** the administrator sends the new credential to **the address on the account row**, never to the address in the request, and never to a reply-to. That rule is the whole security of the route, and it lives in a human's head.

### The oracle surfaces — the direct answer to the brief

**Does B6's constant response + equal timing close existence enumeration while `/api/account/available` still answers it unauthenticated?**

**No — and the honest statement is narrower and more useful than a yes/no.**

| oracle | status |
|---|---|
| `GET /api/account/available?u=` (`:4374–4385`) | **publishes USERNAME existence per deployment, unauthenticated, pre-gate, by design.** Its own comment (`:4303–4308`) says so and names itself *"a username oracle, knowingly."* |
| account creation's 409 | a second publisher of the same fact, named in that comment |
| `POST /api/recover` (B6) | would publish **EMAIL** existence — a value class **nothing else publishes** |
| the record at rest | R-B — publishes it to members |
| **the administrator's behaviour** | ⚠️ unavoidable and out of band: a person who gets a reply learns they were on file. **No code decision closes this.** |

⭐ **So B6's constant response is not theatre — it closes a real and otherwise-open oracle on a value class that is not already published.** That is worth building. What it does **not** do is make the product non-enumerable, and **the danger is a claim, not a gap.**

> ### ⛔ THE HONEST POSTURE IF `/api/account/available` STAYS — and it is one sentence with one forbidden inverse
> **True and sayable:** *we do not confirm whether an email address is on file.*
> **False and MUST NOT be said, by the product, a release note, or Paul to a neighbour:** *we never reveal whether an account exists.* That is false while signup must tell someone their chosen name is taken — and it is false in the direction that costs the most (foundation: *overclaiming is catastrophic and permanent; a false claim from Paul, to a neighbour, costs him personally with someone he will see again*).

⛔ **And do not "fix" it by deleting the availability route.** Deleting it costs a person a bounced signup form to protect a fact the 409 still publishes. **Widening a claim by narrowing a feature is the trade my L1 already refused.** The structural answer is the ruled one — the single door at lap 8 — and it is Paul's own direction.

### Two rate-limit findings, one of them not in anyone's plan

1. ✅ **B6's own bucket is correct** and closure row 29 is right about why: a locked-out person must not spend their capture quota. ⚠️ **But do not copy `feedbackRateLimitOk` wholesale — it FAILS OPEN on a KV error (`:1660–1664`), deliberately, because *"a rate-limiter outage must never be the thing that eats her words."* That ruling was made for capture.** For a reset-request route, fail-open during a KV wobble means an unbounded flood of requests into the administrator's queue. **B6 must state its failure direction explicitly; a copied limiter inherits a decision made about a different value.**
2. ⛔ **NEW — `/api/account/available` shares the feedback bucket, and the property's own physics amplify it.** `:4377` calls `feedbackRateLimitOk`, which is also spent by `POST /api/feedback` (`:4106`) and `POST /api/zone-audio` (`:4412`). `FEEDBACK_RATE_MAX = 20` per IP per `FEEDBACK_RATE_WINDOW_SEC = 300` (`:1131–1132`). **CLAUDE.md's founding premise: the only network at the property is the house Wi-Fi** — so every device on the place shares one egress IP. **Twenty username-availability probes in five minutes silently consume the household's entire note-and-voice quota.** That is a denial-of-**capture** lever against the channel the product's whole premise depends on, reachable by anyone, unauthenticated, and it exists today. *(This closes my prior run's "could not check" on the availability route's ceiling — the number is 20/300s, shared, fail-open.)*
   - `settled_by`: code read at `feedbackRateLimitOk`, the three call sites, and the two constants. `authority_checked: **true**` for the sharing; **`false`** for "this has ever happened" — I read no live KV.
   - **Falsifier:** `grep -n "feedbackRateLimitOk(request, env)" worker/worker.js` — three call sites is the finding; one is not.
   - ⛔ **Fix is engineering-partner's**, not mine. My ruling is only that a **capture** bucket and a **probe** bucket are different tiers and must not share.

### RR-4, extended

*A client IP may exist at rest only inside a TTL'd rate-limit key, as a **declared** exception.* B6 adds a **third** such site after `doorRateLimitOk` and `feedbackRateLimitOk`. ✅ Permitted; it must carry `expirationTtl` like its siblings (`:1146`, `:1656–1658`), and the roster row now names three sites, not two.

### B5 (`signin_failed`) — permitted as written, with two additions the plan does not carry

✅ The shape is right and it has a precedent to copy exactly: the server-side `door_failed` writer (`:4465–4467`) carries `ts`, `event`, `door`, `deviceId: null`, `env`, `receivedAt`, a **constant** `reason`, `serverSide: true`, through `declarePerson`, via `waitUntil` (`:4468–4469`). **Copy that record's shape field-for-field.** RR-3 (the attempted username never written) stands and the plan states it.

⛔ **Addition 1 — do NOT add `signin_failed` to `DOOR_EVENTS`.** `DOOR_EVENTS` (`:1136`) is the allow-list `handleDoor` validates client POSTs against (`:1615`, `bad-event`). A builder who sees B7's reader miss the event will be tempted to add it there. **Adding it makes `signin_failed` client-forgeable, unauthenticated** — anyone could manufacture sign-in-failure records at any household. Keep it server-side-only, and **B7's reader must read the `door:` stream by event name, not by importing the allow-list.** *(That the reader keys on `DOOR_EVENTS` is **inference** — I did not open `watch-door.py`. If it does not, this addition is free anyway.)*

⛔ **Addition 2 — `waitUntil` on both branches or timing diverges.** The missing-account branch runs a dummy `derive()` (`:883`) precisely to make it cost what the wrong-word branch costs. A KV write off the response path is fine; **a KV write awaited inline on one branch and deferred on the other re-opens the timing oracle the dummy exists to close.** The plan says "both branches or neither" about *instrumenting*; this is the same rule about *awaiting*.

### B10 (email shown back) — ⛔ **IT CANNOT BE BUILT FROM THE ROUTE THE PAGE ALREADY CALLS**

The plan flags this as unverified. **Here is the measurement.**

- `settings/account/index.html:212–226` reads `/api/grant/whoami` and renders `d.email` / `d.phone`.
- **`/api/grant/whoami`'s response literal does not contain `email` or `phone`** (`worker.js`, the whoami branch, response object at ~`:4536–4567`).
- whoami reads the **grant** row, and the grant's field-copy list in `handleSession` (`:942–944`) is `placeName, accent, address, addressParts, ranked, contactPref, profileAccent, coordinates` — **`contactPref` but never the value.**

> **So today the page asks for the value, is told the channel, and renders nothing.** `parts` is empty, `cv.hidden = true`, the field is **absent**. That is not a display decision — it is the exact defect three seats reported across two builds, and its cause is in the Worker, not the page.

⛔ **And the obvious fix is a roster violation.** Adding `email` to the `:942` copy list puts a contact value onto **every grant row, at every rotation** — and `tools/grant-mint.py`'s `PLACE_FACTS` (`:226`) mirrors that list with a **selftest clause binding them** (`:622–623`), so widening it puts the address into `fernwood-private/grants.json`, the register. **Contact values are identity class; grant rows are authorization class. RR-1 forbids the traffic in the other direction and this is the same boundary.**

✅ **The permitted shape:** the whoami branch **already reads the account row** in the same request, for the geocode repair (`:4517–4525`). Read the address from there and return it **in the response**, creating no second copy at rest. And ⛔ **no `fw-email` localStorage key** — there is none today (`grep -n "fw-" onboarding/index.html` lists every key and email is not among them) and B10 must not mint one. An email cached on the device is a contact value surviving a sign-out unless it is rostered, which is `check-storage-keys.py`'s whole job.

- **Falsifier:** `grep -n "email" worker/worker.js | grep -n whoami` returns nothing today; after the fix, `curl -H "X-Grant: <a test grant>" <origin>/api/grant/whoami` returns an `email` field. And `python3 tools/grant-mint.py --selftest` must still pass **without** `PLACE_FACTS` being widened.

---

# ③ LEGIBILITY

### L1 · *"if that address is on file, it has been sent"* — the copy is **false in three independent ways**

⛔ I do not write the sentence. I am reporting that the world it describes does not exist.

1. **Nothing sends anything.** `grep -ril "sendgrid|resend|mailgun|smtp|sendMail|postmark|MailChannels"` over the repo returns `worker.js` **only on the word "resend" inside an unrelated zones error hint** (`:4859`), plus plan/exhibit prose and `tools/mom-queue-watch.py`'s deliberately-unconfigured `notify_email`, which CLAUDE.md says by name is **not to be "fixed."** **The Worker has no outbound email capability of any kind.** *(Searched-negative, not a silence.)*
2. **"Has been sent" asserts a completed act in the past tense.** D1 rules **the administrator is the reset path** — a human, on human time, who learns about this by someone running `watch-feedback.py`. Nothing has been sent at the moment the sentence renders. Nothing may have been sent an hour later.
3. **"If that address is on file" asserts a check that did not happen** (R-E: there is no lookup path). The clause reads as *we looked and will not tell you*; the truth is *we did not look.*

> ⭐ **This is `capture must not lie` on the one surface where the person has no other channel.** A note that says "Saved ✓" against a dead endpoint is the failure this repo has already paid for twice. This is that shape, on a screen reached by someone who cannot get in.

**The three exits, in the foundation's order — and I am not choosing:** change the **world** (build a send path, or make the administrator's act produce a state the page can reflect) · change the **sentence** (content-steward) · **Paul decides**. ⛔ **Do not reach for the sentence by default.** A sentence that is merely *technically* non-false — *"your request has been recorded"* — is still a dead end for the reader if nothing tells them what happens next.

### L2 · Who will see the request — the person cannot tell, and neither can the administrator

**Three separate legibility failures stacked on one route:**

- **The person is told nothing about who reads it.** A recovery request hands a contact value to a **named human who may not be a member of their household**. CLAUDE.md's AI-boundary amendment already carries the duty: *"an administrator who is not a member of the household reads that household's notes, voice and Guru turns… that requires explicit up-front agreement before the first contributor input"* (`.plans/2026-09-02-data-model-design.md` §7). **This route is the first surface where a person hands over a contact value while locked out and unable to read any policy page.** The person must be told, at the point of the ask: **a person reads this, not a system; a named one; and they reply on human time.** ⭐ That is also the **only trust credit available** here — the foundation's own finding is that the category's vocabulary (staff-blindness) is unavailable to Fernwood, and what is left is *accountability: a named person with a stated duty.* **The route that most looks like stonewalling is the one where naming the human is both honest and the strongest thing the product can say.** ⛔ The words are content-steward's.
- **As specified, a member of the household sees it too** (R-A). If any sentence tells the person who reads this, and the record lands in a member-readable stream, **that sentence is false.** The copy and the tier must be decided together or one of them will be a lie.
- ⚠️ **The administrator is not notified; a sweep might find it.** Q4's *"`watch-feedback.py` is its reader; no new channel"* satisfies *an event with no reader is not instrumentation* — **and a reader is not a channel.** `watch-feedback.py` runs when a human runs it. A locked-out person's request sits in a dated KV key until someone opens a terminal. **The product is about to promise a reply on a path whose latency is "whenever Paul next runs the pickup block."** That is a real design constraint on whatever the copy is allowed to promise about *when*, and it is not named anywhere I read.

### L3 · The true posture is strong here and completely invisible — and the constant response reads as stonewalling

The 404 discipline, the dummy `derive()`, the personId-null guard, the member/admin route split, no third-party requests — **real, paid for, and unreadable from the person's seat.** Under a breach frame that is a win; under Paul's frame it is protection paid for with no trust credit earned.

⛔ **The remedy is NOT to weaken the constant.** It is that the mechanism must be legible as a *deliberate protection of them*, not as an unhelpful machine. My L1 distinction still governs and is the thing that makes this possible: **copy that enumerates the POSSIBILITIES is not disclosure; only copy that varies with the TRUTH is.** A sentence may say *we deliberately do not confirm whether an address is on file — including to you — because confirming it to you would confirm it to anyone*, shown identically to every caller, and reveal nothing.

**Constraints on whatever is written (mine); the sentence is content-steward's:**
1. One string, byte-identical for every outcome, from a single branch. No second round trip.
2. It may not assert an act the system does not perform (L1).
3. It must name that **a person** reads it, and set an honest expectation of **when** (L2).
4. It must be readable by someone holding only a phone and a link — no policy page, no sign-in.
5. It must not contradict the refused/unreachable split (RR-5) — a locked-out person and an out-of-range person must not be routed to the same next action.
6. ⭐ It must leave the person a **second door** that does not depend on this route working, because on this route *nothing is verifiable by them.*

### L4 · L12 is not the machine check it is presented as

The journey's *"byte-identical and equally timed"* (closure L12, plan B6) is ⛔ **the journey's last machine-checkable stop** in the closure's own words. **The timing half is not checkable from a Chrome walk** — browser-measured round trips over a real network are dominated by noise that swamps a KV lookup. It will be either flaky or vacuous, and a vacuous green on a timing assertion is precisely a false negative wearing a check.

**The timing claim needs a transport-level measurement** (N samples of each case via `curl -w %{time_total}`, compared as distributions) — which is my prior run's L1 falsifier, **still unrun by anyone, twice named.** Byte-identity **is** checkable in the walk; keep that half, and mark the timing half **UNCHECKED** in the walk report rather than scoring it walked. *(`walk-integrity.py` refuses a stop scored "walked" over its own "could not do" — this is that rule, applied before the walk is written.)*

---

# THE CLOSE

### ✅ May be BUILT to the plan's spec as written

- **B5** `signin_failed` — plus *addition 1* (not in `DOOR_EVENTS`) and *addition 2* (`waitUntil` on both branches).
- **B7** the reader — provided it reads by event name, not by the allow-list.
- **B11** the one constant refusal string — unchanged from L1(b); exhibit 3b stays rejected.
- **B12** one entry point covering both username and password — shape is right.
- **B13** the signed-out lede.
- **B15 / D3 / D4** the refused · unreachable · broken split — this is RR-5 and it is the sharpest legibility fix in the lap.
- **B9**, with R-D's one line (`context.surface` must be in `ACCOUNT_SURFACES`).
- **B1, B2, B3, B4** — auth *code*; **engineering-partner's**, not mine. I read them and raise nothing new.

### ⚠️ Must CHANGE in spec before build

1. **B6's destination.** As specified the record lands in a **member-readable** stream and in the **mom cycle's arrival record**. Either the outcome leaves the record (R-B(i)) or the record leaves that stream (R-B(ii)). ⛔ **Q4 is a ruling; this tier is not in Q4's text. Put it in front of Paul, do not resolve it in the build window.**
2. **B6's field list.** No `sessionId`, no `deviceId`, no `note`, no submitted address, no truth-varying outcome. And `handleFeedback` **rejects** a record with neither sentiment nor note — the handler must write its own row or the route 400s on its own first request.
3. **B6's lookup.** Decide between *no lookup*, *a scan*, and *a hashed index*. ⛔ **A plaintext `email:` key is refused** (RR-7).
4. **The recovery copy.** It asserts an act nothing performs, a check that does not happen, and a reader the person is not told about. Three exits; **Paul's, not the build window's.**
5. **B6's limiter failure direction** — do not inherit `feedbackRateLimitOk`'s fail-open without deciding it.
6. **B10.** Cannot be built from `whoami` today; the tempting fix widens `PLACE_FACTS` and puts a contact value into the register. Read it from the account row inside the whoami branch; mint no storage key.
7. **L12's timing assertion** — mark UNCHECKED in the walk; run the transport measurement separately, once, ever.
8. **`/api/account/available`'s shared bucket** — a capture bucket and a probe bucket are different tiers. *(engineering-partner's fix.)*

### 🗓 Lap-8 questions

- **The single door** (L1(d)) is the structural answer to the whole oracle trade and is already Paul's direction. Nothing in row B substitutes for it.
- **V8 — the reset act itself.** This build ships the *request* and nothing that delivers a credential. **The route's purpose is out of scope of the route.** Roster row owed: what class the new credential is, what channel carries it, and the rule that **it goes to the address on the account row, never the address in the request.** That rule currently exists only in a human's head and is the entire security of the flow.
- **Email is unverified, non-unique, and freely settable** (`/api/profile:4226`). A recovery flow resting on it is resting on an unverified value. Verification, or an explicit ruling that it is a courtesy and not an identity claim.
- **R23 bullet 2 / the up-front agreement** before a person hands a contact value to an administrator who is not in their household — still unruled, still carried from 09-10, and this route is where it stops being abstract.

---

### ⛔ THE HONEST SHAPE OF THIS RUN

**Not clean, and not complete.** I read **§1–§5 of a §9 plan and B6 points at §9** — if Paul has already ruled the channel there, finding R-A is a second voice on a settled question and I did not read the first. I ran **no probe, read no live KV, measured no timing** — so *"equally timed"* is unmeasured for the **third** consecutive artifact that asserts it. I did not open `watch-door.py`, so *addition 1* rests on inference about what B7's reader keys on. I did not enumerate the route table — **the same denominator gap as my 09-10 run, now twice stated and twice unclosed.**

**Where a real failure in these surfaces is most likely to be found by someone else:** in the routes I have never read, and in the **deployed** Worker, which I have never compared to the tree. Per the falsifier: if that happens, **this denominator did not name it.**
