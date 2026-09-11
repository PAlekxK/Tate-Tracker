# Cross-device sign-in — FINDINGS: the four attempts, the defects, and the question for Paul

<!-- lane: cross-device-signin (tate-tracker-21) · written 2026-09-10 ~9:30 PM ET, closed ~10:30 PM ET · measured at Tate-Tracker@5ffe811 · HEAD at close 4b3b06a (register commits only; no diff to worker/, onboarding/, estate/, homes/, viewer.html since 5ffe811)
     brief: handoff/handoff-cross-device-signin.md · readback: handoff/handoff-cross-device-signin.readback.md
     Every claim marked MEASURED was read tonight from KV (read-only, wrangler --remote), the door record, the
     Worker health endpoints, or the code at 5ffe811. Every claim marked SEAT is one seat's reading and is
     linked to its trail. Nothing here was deployed, written to KV, or minted. -->

## 0. In one paragraph

Paul could not sign in at `fernwood-home.pages.dev` because that origin is Mom's household's deployment and
accounts live per deployment: his `pkirsch` row exists at his condo's deployment (`myhome-paul`) and at `qa`,
and nowhere else. The page told him his username and password "don't go together" because the Worker
deliberately answers *no such account* and *wrong password* with one identical 404 (a username-oracle
defence), so it cannot say *not this house*. His laptop was **not** signed in either: it painted a cached
place name from an earlier session, every request behind it was refused (14 server-side refusals in ten
minutes), and the page rendered that refusal as "We couldn't reach your place just now." His phone, with
nothing stored, got the bare door. The same credentials then worked at the condo's own origin. So the
per-deployment namespace explains all four attempts; the defects are that the product cannot tell him any of
this, and that a person with one identity and two houses has no single door. The direction Paul stated the
same evening — one landing page, one sign-in, every place reachable — is the destination the multi-tenancy
plan already ruled toward on 2026-09-10; this lane frames the mechanism and the interim.

## 1. The four attempts, by symbol — MEASURED

| # | device · URL | what he saw | what happened |
|---|---|---|---|
| 1 | phone · `fernwood-home.pages.dev/onboarding` | "That username and password don't go together. Have another look — or ask Paul for a fresh link." | `handleSession` (`worker/worker.js:870`) resolved `keyFor(scopeOf(env),"account","pkirsch")` → `est-e6696a:account:pkirsch`. **That key does not exist at `home`**; the only account row there is `est-e6696a:account:marguerite`. `deny()` (`:877`) → `404 {error:"not-found"}`. `onboarding/index.html` ~`:1177` prints its one sentence for any non-2xx. **No server-side record of this attempt exists** — `deny()` writes nothing. |
| 2 | laptop · same URL | same sentence | same path, same absence from the record. |
| 3 | laptop · `fernwood-home.pages.dev/estate/` | "auto-logged in" (his words) | `estate/index.html` reads `fw-grant` from localStorage (`:232`, `:261`) and paints the masthead from the cached name under the owner guard (`:331`) **before** any network call. It then calls `/api/grant/whoami` with that grant (`:509`). The grant is not in `home`'s store → `grantFor()` returns null → the Worker writes a server-side `door_failed reason=unknown-or-other-estate` (`:4463-4470`) and answers 404 → the page sets `reachUnknown` (`:518`) and renders **"We couldn't reach your place just now — nothing is lost."** (`:475`). **He was not signed in. A refused credential was printed as an outage, over a cached shell.** |
| 4 | phone · same `/estate/` URL, first visit ever | "the generic empty My Home green page with all the empty cards" | No `fw-grant` stored (Paul: *"no this was the first time"*) → no whoami call → the bare door: "Open your invitation link and your place will be here." (`:473`) plus the empty cards. There is no sign-in control on it; `/onboarding` is reachable only by knowing the URL (the founding-flow sweep's **F1 blocker**, `.ux-reviews/2026-09-10-founding-flow.md:66`). |
| — | phone · `myhome-paul.pages.dev`, same credentials | signed in, submitted feedback (his words: *"I can log in successfully on my phone. I submitted some feedback via my phone."*) | `est-d93508:account:pkirsch` exists at `paul`. Door record at `paul`: 3 `door_reached` 9:02–9:06 PM ET, **0 `door_opened`** — no page emits `door_opened` (grep), so success is as invisible to `watch-door` as refusal is. Onboarding metrics show `s0 → s-nolink` with a username typed (backlog session's read). ⛔ **And there is NO feedback record at `paul` — the namespace holds no `feedback` key at all** (18 keys, re-listed 9:40 PM ET: door ×2, onboarding-metrics ×4, account, digest, geocode, grants, routes). Either a successful sign-in AND a successful Send are both invisible to the record, or the Send did not complete as it looked. The backlog session is asking Paul which page and what the screen said after Send. **This is the one finding tonight that touches the capture rule — a capture path that can lose words while appearing to succeed.** See D7. |

### 1.1 The record behind row 3 — MEASURED

`est-e6696a:door:2026-09-10` and `…:2026-09-11`, read directly from KV:

| time (ET) | event | reason |
|---|---|---|
| 7:55:18 PM | door_failed | unknown-or-other-estate (server-side) |
| 7:56:13 → 7:56:53 PM | door_failed ×5 | unknown-or-other-estate |
| 7:57:04 PM | door_reached | (client-side, no reason) |
| 7:57:49 → 8:04:29 PM | door_failed ×8 | unknown-or-other-estate |

Fourteen refusals. A `door_failed` is written only when an `X-Grant` header is presented and fails to
resolve. The phone had nothing to present and the sign-in form sends no grant header, so **every one of
these is the laptop's stored credential being refused at Mom's origin.** Which token the laptop holds is
unread (it is in his browser, not in KV); the only plausible candidate is a grant from the 09-04 → 09-08
era when the condo shared `est-e6696a` with Mom. The local register (`fernwood-private/grants.json`) still
lists `p-paul @ est-e6696a relationship:[owner] capability:administrator`; the store does not hold it.

### 1.2 Timing — MEASURED

The attempts (7:55–8:04 PM ET) post-date the deploy. Health endpoints at 9:18 PM ET: `fernwood-home`
`build_sha 0d15bd0`, `myhome-paul` `d7b642e` — both commits after `318416a` with **no change to
`worker/worker.js`** between `318416a` and HEAD (`git diff --stat` is empty), and both answer `404` to an
uncredentialed `POST /api/estate`, the founding-build signature. So the attempts were against the founding
build, as the brief guessed and could not verify.

## 2. The state of the store — MEASURED

| namespace | account rows | `username:` / `account:` (bare) | routes | grants |
|---|---|---|---|---|
| `home` (est-e6696a) | `est-e6696a:account:marguerite` | **0 / 0** | 1 (Mom's) | 1 (Mom's, `c842311d…`) |
| `paul` (est-d93508) | `est-d93508:account:pkirsch` | **0 / 0** | 5 | 3 (two routes have no grant behind them — a 404 by design, incl. `6608722e` whose grant was deleted today) |
| `qa` (est-qa0001) | `est-qa0001:account:pkirsch` (a **separate** account, its own personId) | — | — | — |

Two things this settles. **The `username:` index the SCOPE plan describes does not exist yet** — accounts
are still the estate-prefixed shape, so sign-in is the deployment's estate prefix plus the username, and
nothing else. And **`pkirsch` is two people to the system**: `p-yjnw9lt41nww` at `paul` and
`p-jhgwhxxz6zce` at `qa` (personIds from `watch-accounts.py` and the coordinator's sweep; I did not pull the
rows, which hold password hashes). Paul's word: *"pkirsch should be production only."* The `qa` copy is a
fixture-hygiene fact and a demonstration of the shape: one human, one username, N namespaces, N identities,
no link between them.

## 3. The defects, named

| # | defect | where | class |
|---|---|---|---|
| D1 | **No single door.** One person with two houses must know two origins. The root `/` redirects to `viewer.html`; `/estate/` has no sign-in control; `/onboarding` is unlisted. | `index.html:6`, `estate/index.html:473`, F1 | structural — the ruled destination (§5) |
| D2 | **The refusal cannot say *not this house*.** One sentence for wrong-password and unknown-username, mirroring a deliberate byte-identical 404. | `worker.js:877`, `onboarding/index.html:~1177` | a **trade**, not a bug — security-steward rules (§4.2) |
| D3 | **A refused stored credential renders as an outage over a cached shell.** The page cannot distinguish *your credential was refused here* from *the network is down* — and on this property the second is common, so the first hides inside it. | `estate/index.html:331, :475, :518` | legibility — cheap to fix once the rule is stated |
| D4 | **Refusals at the sign-in door are unlogged; successes are unlogged too.** `deny()` writes no door record; nothing emits `door_opened`. `watch-door.py` could not have seen attempts 1, 2, or the later success. | `worker.js:877`; grep `door_opened` | instrumentation — outcomes only, never people |
| D5 | **One username, two identities** across `paul` and `qa`; the M5 merge must decide what a username that exists in two namespaces becomes. | KV | hygiene now, migration rule later |
| D6 | **The register asserts a grant the store rejects** (`p-paul @ est-e6696a owner/administrator`). The multi-tenancy plan already rules the *register* wrong and forbids minting it. Left as is, `watch-accounts.py` prints the divergence every run and a reader may "repair" it the wrong way. | `fernwood-private/grants.json` | register correction, Paul's |
| D7 | **A Send he reports as done is not in the store.** No `feedback` key exists at `paul` after his 9 PM ET phone session. Until he says what the screen showed after Send, this is UNRESOLVED between *the record cannot see a success* and *the capture was lost while looking successful*. The second would break the rule every capture surface is built on. Cross-ref **TIER 1 · 42**. | `paul` KV; `/api/feedback` path from `viewer.html` at the `myhome-paul` origin | ⛔ open — Paul's answer decides which |
| D8 | **Instrument trap, reproduced twice tonight (once by this lane):** `wrangler kv key list` **without `--remote`** returns `[]` with exit 0 on a namespace holding 18 keys — it lists the local dev store. A reader who forgets the flag gets a confident empty answer. `watch-accounts.py`/`watch-door.py` pass it; a hand probe may not. Cross-ref TIER 1 · 42. | wrangler CLI | doc + tool guard |
| D9 | **Shared rate-limit bucket** (backlog session's read, not measured by this lane): `ratelimit:feedback` is shared by `/api/feedback`, `/api/account/available` and `/api/zone-audio`, so a counter that reads as "a note arrived" may be a username-availability check. Cross-ref TIER 1 · 42. | `worker.js` rate-limit helpers | instrumentation |

## 3.1 ⛔ D7 RESOLVED TO A LEADING EXPLANATION — the app at the condo has no Worker, and it said "Saved" — MEASURED

Paul's later word: *"I signed in via this link that you sent me — https://myhome-paul.pages.dev/onboarding/ — I
got no error indication on the feedback I submitted."* The chain, every link read tonight:

1. **The onboarding page's own feedback box was not used.** `est-d93508:onboarding-metrics:2026-09-11` holds 14
   events 9:02–9:06 PM ET: screens `s0`/`s-nolink`, `session`, one `field`. **No `feedback_open`, no
   `feedback_sent`** — the events that box fires (`onboarding/index.html:1665,1680`).
2. **A successful sign-in leaves onboarding for the app.** `onboarding/index.html:1217`: `location.href =
   "/viewer.html"`. At `myhome-paul.pages.dev` that 308s to `/viewer`, the 1.18 MB app (fetched live, 200).
3. **The app's Worker map has no row for the condo.** `viewer.html:7316-7320` `PAGES_WORKERS` maps exactly
   `fernwood-qa`, `fernwood-lab`, `fernwood-home`. Any other `.pages.dev` label gets `WORKER_BASE = ""` —
   **deliberately fail-closed** (09-04: *"a new preview host must FAIL CLOSED, never inherit a neighbour's
   Worker"*), written two days before the `myhome-*` origins existed and never extended. The served `/viewer`
   at the condo carries those three rows plus the legacy default and **zero references to
   `myhome-paul.paul-kirschenbauer.workers.dev`**. (The other four pages — onboarding, estate, homes — derive
   the Worker from the host label and reach it; the app alone does not.)
4. **So a Send from the app goes nowhere and says it is saved.** `viewer.html:12243` `FEEDBACK_ENDPOINT =
   WORKER_BASE` → `""`. `sendRecord` fetches `"" + "/api/feedback"` → relative → the Pages origin → **405**
   (measured). `res.ok` false → the note is already in the localStorage outbox
   `tateTracker.feedbackOutbox.v1` (durable first, send second, `:13183-13190`) → result `"queued"` →
   `ackFor()` (`:13136`): **"Saved on your phone — it'll reach the record next time you're back on Wi-Fi. ✓"**.
   That is the "no error indication". `flushOutbox` runs on every load and on `online` (`:13576-13578`) —
   against a dead relative URL, forever.
5. **Not only feedback.** `AMBIENT_ENDPOINT`, `ZONE_AUDIO_ENDPOINT` and every `WorkerAPI` call derive from
   `WORKER_BASE`. **The app at the condo has no backend at all** — no Guru, no station, no metrics, no
   capture. *"Take pictures at my condo to share with the Guru"* cannot work in that build. `myhome-bob`
   `/viewer` serves a 252-byte stub (200), so Bob's origin does not serve the app at all.

**Class:** capture accepted, receipt printed, promise false — the note is durable on the device, so it is not
lost *yet*; it is lost the day the browser's storage is cleared, and it is unreachable by any tool until
then. **Deterministic check, his phone only:** localStorage `tateTracker.feedbackOutbox.v1` at the
`myhome-paul.pages.dev` origin holds it. **Recovery without a deploy, his act:** the app's paired-device
setting (`#fn-sync-url`, "Save & test", stored as `tateTracker.sync.v1`, `viewer.html:7273,:20850`) — `feedbackBase()`
prefers `c.workerUrl` when set (`:13183`); paste `https://myhome-paul.paul-kirschenbauer.workers.dev` and the
outbox flushes on the next load. ⚠️ **Not walked by this lane** — read from the code, not tested. The build
fix (a map row per served origin, or the label derivation the other four pages already use) is Paul's ruling
and moves the candidate.

**One caveat, stated so it does not vanish:** the backlog row `TIER 1 · 42` (409cb7f) reads *"sent from the
condo's onboarding page after signing in"*. The metrics say the onboarding page's box was not opened. Both
can be true if *"the onboarding page"* names the link he opened rather than the screen he typed on — sign-in
hands off to the app in the same tab. The outbox on his phone settles it either way.

## 4. Seat readings — all four landed; each trail is sha-stamped `5ffe811`

### 4.1 engineering-partner — path-evaluation → `.engineering/2026-09-10-cross-device-signin-ENGINEERING.md`

Its ten lines, lifted: **(1)** nothing is broken — per-deployment accounts working as designed; the defect is
that no surface can say so. **(2)** the bug tonight is a sentence, not a schema. **(3)** ⭐ **M2 is already in the
code and has never touched the data** — `accountFor()` reads `username:` → `account:<personId>` index-first
with legacy fallback, `putAccount()` dual-writes; *"M1+M2 parked, not started"* in the credential-path brief
is stale; the zero `username:` rows mean the **backfill** has not run. **(4)** 🔴 **the backfill is armed with a
trap**: `handleSession` is the one account writer that bypasses `putAccount` (`worker.js:979` writes the
legacy key alone), so once an index exists the authoritative row goes stale on `tokenHash` at the first
sign-in — fix before the backfill. **(5)** 🔴 rotation revokes at the wrong scope (`:972` writes at the person's
estate, `:977` deletes at the deployment's) — for any founder, signing in does not kill the previous
credential. **(6)** A5 gates the destination, not the door — sign-in, whoami and the shelf read no digest, so
one landing page can ship ahead of the long pole; what A5 gates is the condo's Guru once the condo is a row,
so **M5 before A5 regresses the capability Paul named.** **(7)** interim: **(i) plus honesty** — keep two
origins, fix three strings and one fetch branch; reject (ii) (publishes a household→origin map), (iii) legal
but buys a house he still cannot enter, (iv) is M5 in disguise. **(8)** the qa duplicate is per-deployment
uniqueness met, and becomes a **blocking M5 precondition** (`username:` last-writer-wins; the loser keeps a
working token and loses password login). **(9)** D's rule: *a refusal changes what the page CLAIMS; only the
person changes what the device KEEPS* — quarantine, never clear. **(10)** E: three emits, one reader —
server `session_refused` on **both** deny branches via `waitUntil` (one branch only re-opens the timing
oracle), client `door_opened` on whoami-200, client `door_failed` on whoami-404.

### 4.2 security-steward — roster + legibility → `.engineering/2026-09-10-cross-device-signin-SECURITY.md` (filed verbatim by the lane; the seat has no write tool and flagged that `.security/` is read by nothing)

🔴 **Headline, not in the brief:** the register row `p-paul @ est-e6696a relationship:[owner]` **disarms G2** —
`grant-mint.py:gated()` returns *not gated* at Mom's estate because the row exists with a non-empty
relationship, so a mint there would require no consent entry. The multi-tenancy plan asserts the opposite
(*"G2 firing at Mom's estate is CORRECT"*) two paragraphs after naming the row wrong. **Correcting the
register is re-arming a gate, not tidying a record.** (The lane read the register: the row is present as
described, so the seat's first falsifier is answered.)
**R1** presentation of a credential anywhere is allowed; reach is the grant row's alone; ⚠️ `hostAgrees()`
is vacuous without an `Origin` header — re-run the plan's two-estate falsifier with the header removed.
**R2** identity is portable and an account row confers no reach (verified) — but the row carries
authorization-class fields (`relationship`, `conferred*`, `tokenHash`) that would mint a grant on sign-in if
copied; a cross-namespace copy must be an **allow-list**. **R3** the store is the roster of truth for reach;
the register is upstream of the mint and must refuse on divergence. **R4** the two `pkirsch` personIds collide
byte-identically on `username:` at M5 — fail closed on auth, open on identity; **M5 must refuse a collision**;
and the rename path's uniqueness check goes blind at M6.
**L1 — THE RULING:** ⛔ **(a) refused** — the byte-identical 404 stays, but its justification is falsified:
`GET /api/account/available` already publishes username existence per deployment, unauthenticated; paying a
person-facing cost for a secret published elsewhere is the worst trade. **(c) declined** (a one-way door for an
interim). ⭐ **(d) recommended and already ruled** (one origin: *not this house* stops being a failure mode).
✅ **(b) permitted as the interim** — *an oracle requires the response to VARY with the secret; copy that
enumerates the possibilities is not disclosure.* Five constraints on the sentence (one string, no reason
code, no second round-trip, remedy reachable with a phone and a link, must not collide with L2's split).
**L2** refused ≠ unreachable, three states not two, and the merge is one line after the branches already
split; at this property the outage reading is the *likelier* wrong read. **L3** an unlogged refusal at the
door is a trust gap — log `signin_failed` as an outcome, **never the attempted username** (a log of usernames
is the oracle at rest). Five roster rows proposed (RR-1…RR-5).

### 4.3 ux-expert — review → `.ux-reviews/2026-09-10-cross-device-signin.md`

*"Three screens told Paul three different stories about one fact, and none of them was the fact."* He was
**coherently misinformed** — each screen confirmed a wrong theory he could already hold. Sharpest line:
`estate/index.html:462` — every honest thing the page knows to say about a refused credential lives inside
`if (!rows.length)`, so honesty is implemented where nobody needs it and absent where it is load-bearing;
`:344-345` paints **"Signed in as pkirsch"** from localStorage while the Worker is refusing that credential.
**S1/S4 copy** is cheap and needs no ruling beyond L1: say nothing about the *account*, something about the
*door* — and delete *"or ask Paul for a fresh link"*, a promise `[paul-ruled 2026-09-10]` already killed forty
lines earlier. **S3 rule:** quarantine — keep the rows, drop the byline, label once, swap **[Open your place ›]**
for **[Sign in ›]**; on unreachable change nothing but add a sentence and **[Try again ›]**. *The difference is
carried by the control, not the adjective.* **The cross-device job is six steps, two of which live only in
Paul's memory** (the origin and `/onboarding/`). **The landing page:** one sentence, two co-equal doors, neutral
accent, branch on count after sign-in (0 → onboarding, 1 → in, 2+ → the shelf, which `homes/index.html`
already implements); never list, count, name or hint at a house to someone not signed in. **Regression found
in passing (F12):** `estate/index.html:437` re-declares `var placed = false` after `:301`, so the 09-08 fix at
`:489` is dead code.

### 4.4 user-researcher — JTBD → `.user-research/2026-09-10-cross-device-signin-jtbd.md`

**Four jobs tangled in one report**, only one about signing in: capture from the device in my hand · share it
onward · get in from a new device · administer without impersonating. **(c) is Paul's alone today** — Mom has
never typed a URL. **(d) is administrator-only and must not generalise** `[paul-ruled 2026-09-10]`. **He did not
go to the wrong door; he went to the door he had open** after a week administering her household. *"Synced
automatically"* is three layers in three states: place facts ✅ shipped 09-08 · credential ⛔ per-deployment ·
capture drafts ⛔ device-local **and should stay so**. Paul's binding constraint is identity; Mom's is
connectivity — same job, opposite fixes. ⭐ **Criticality:** *the only reason this was diagnosable is that the
person it happened to owns the KV store.* Two questions for Paul it refused to guess: by *"devices synced"*,
did he mean the credential works anywhere, or that things started on one device appear on another? And on
his phone at her origin, was he trying to reach her place or his? Uncovered walk shape named: **multi-household
person, cold device** — no synthetic seat has ever presented one credential at two origins.

## 5. The question for Paul — question · recommendation · alternatives

**Question.** *One person, one sign-in, every device, every place they belong to* — what is the mechanism, and
what do we do between now and then?

**Recommendation.** Three parts, in this order, and the first is not a build.

1. **Recover tonight's note and fix the condo's app before anything about accounts** (§3.1). The app served at
   `myhome-paul` has no Worker; every capture there queues forever behind a "Saved" receipt. Recovery is his
   act on the phone (the sync setting); the build fix is one map row per served origin, or the host-label
   derivation the other four pages already use. **This is the critical-fail class by his own definition and
   it is orthogonal to the account model.**
2. **The destination needs no new ruling — it is the one already made.** One origin, estate-as-row, one
   sign-in, the shelf after it (`.plans/2026-09-10-multi-tenancy-PLAN.md`, sequence 1–5). His direction tonight
   restates it. What this bug **adds** to that plan: fix `handleSession:979` and `:977` **before** the M2
   backfill; M5 **refuses** on a username collision (the `qa` `pkirsch` is torn down first — his word,
   *"production only"*); correct the register row `p-paul @ est-e6696a` **as a gate re-arm** (§4.2 headline);
   and note that a landing page can ship **ahead of A5** because sign-in, whoami and the shelf read no digest.
3. **The interim is (i) plus honesty — two origins, four honest surfaces.** Sign-in failure copy under L1(b):
   one constant sentence that names the *door*, not the credential, and drops "ask Paul for a fresh link".
   `estate/` splits refused from unreachable and stops painting "Signed in as" from cache (quarantine, never
   clear). The bare door gets **[Sign in ›]**. `deny()` and whoami success/failure get outcome-only door
   records. **No redirect door** (it publishes which house a username lives at). **No account copy into
   `home`** — legal as identity, but by his own 09-10 ruling he holds no relationship at Mom's household until
   she invites him, so it buys a sign-in to an empty shelf.

**Alternatives, each with why not.**
- **A. Build the one-origin door now, ahead of the plan's sequence.** Faster to his direction, and the seats
  agree the door does not wait on A5. But it moves the credential path while two first-time users are
  walking through it (the plan's own timing warning), and if M5 lands before A5 the condo's Guru regresses.
- **B. Copy his account into `home` so `pkirsch` signs in at Mom's origin.** Identity-only copy is
  permitted (RR-1 allow-list). He would sign in and see `estates: []` — correct, and useless, until Mom
  invites him. Also leaves Bob's and every future origin with the same wall.
- **C. Change only the copy.** Cheapest; leaves the laptop shell lying, the door unlogged, and the condo app
  without a backend. Not enough.

**What only he can answer** (from §4.4, unguessed): what *"synced"* means to him, and which house he was
trying to reach from the phone at Mom's origin. The first forks the cross-device design.

## 6. Rows proposed for the register (sent to `tate-tracker-0d`, the one door; this lane edits nothing there)

| # | row | evidence | class |
|---|---|---|---|
| P1 | 🔴 **The app served at `myhome-paul` (and any `myhome-*` origin) has no Worker: `PAGES_WORKERS` lacks the row, `WORKER_BASE=""`, every capture queues forever behind "Saved on your phone".** Recovery of tonight's note: the sync setting on his phone. Fix: a map row per served origin or the host-label derivation. | §3.1 | critical — capture accepted, promise false |
| P2 | `estate/index.html`: refused ≠ unreachable (one `reachUnknown` for both, `:518/:565`); "Signed in as" painted from cache while refused (`:344`); dead `placed` re-declaration (`:437`, F12). Rule: quarantine, never clear. | §4.2 L2, §4.3 | legibility |
| P3 | Sign-in failure copy under L1(b): one constant sentence naming the door, not the credential; delete "ask Paul for a fresh link" (`onboarding:~1181`). Content-steward writes it under the five constraints. | §4.2 L1 | copy, ruled permitted |
| P4 | `deny()` writes no door record; nothing emits `door_opened`. Add `session_refused` on **both** deny branches via `waitUntil`, never the username; client `door_opened`/`door_failed` on whoami. `watch-door.py` reads them. | §1 D4, §4.1 E, §4.2 L3 | instrumentation, outcomes only |
| P5 | ⛔ **Precondition to the M2 backfill:** `handleSession:979` bypasses `putAccount` (stale `tokenHash` on first sign-in once an index exists); `:977` revokes at the deployment's scope, not the person's estate. | §4.1 (4)(5) | credential path — before any backfill |
| P6 | 🔴 **Register row `p-paul @ est-e6696a owner/administrator` disarms G2** in `grant-mint.py:gated()`. Correct the register (Paul's; the plan already rules it wrong); add a selftest clause that a register relationship with no live grant makes `gated()` refuse. | §4.2 headline, R3 | control failure — gate re-arm |
| P7 | M5 precondition: a read-only `check-username-collisions` across bound namespaces (exit 3 = uncheckable); the `qa` `pkirsch` (`p-jhgwhxxz6zce`) torn down first — *"production only"*. | §2, §4.1 C, §4.2 R4 | migration gate |
| P8 | The landing page: one sentence, two doors, neutral accent, branch on count after sign-in; feeder to `homes/`; never names a house to someone not signed in. Sequenced with one-origin, and it does not wait on A5. | §4.3 (4), §4.1 (6) | design — `tate-tracker-8d` cites |
| P9 | `hostAgrees()` is vacuous without `Origin`; re-run the plan's two-estate falsifier with the header removed before any step leans on it. | §4.2 R1 | test |
| P10 | Instrument traps: `wrangler kv key list` without `--remote` returns `[]` exit 0 (reproduced twice tonight); the shared `ratelimit:feedback` bucket (backlog session's read). Already on TIER 1 · 42 — cross-reference, do not duplicate. | §3 D8/D9 | doc |
| P11 | Uncovered walk shape: **multi-household person, cold device** — no seat has ever presented one credential at two origins. A hypothesis with a falsifier for `seat-portfolio.py`, not a persona. | §4.4 | testing coverage |

**To `tate-tracker-8d` (account-lifecycle screens):** cite §5 for the model and P8 for the door; the stored-credential
rule (P2) and the sign-in copy constraints (P3) are the two things its screens must not contradict.

## 7. What this lane did NOT do

No deploy. No KV write. No invite minted. No edit to any surface. The laptop's stored token was not read
(it lives in his browser). `check-canon-scope.py --deep` for `home` (TIER 1 · 33) was not run — same seam,
different owner. The two `/onboarding` refusals are timed by Paul's word only, because nothing recorded them.
