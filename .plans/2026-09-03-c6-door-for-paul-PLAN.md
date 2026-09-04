# c6-door-for-paul · The door for Paul — entry + vault on his device, her surface untouched; M3 first
- row: BACKLOG.md § C6 · THE DOOR FOR PAUL — entry + vault on his device, her surface untouched; M3 fixed first
- objective: O3
- class: engine · declared
- seats: engineering-partner → .engineering/2026-09-03-c6-door-for-paul.md
         ux-expert → ../fernwood-private/.ux-reviews/2026-09-02-login-door-and-selector.md
         user-researcher → ../fernwood-private/.user-research/2026-09-02-activation-journeys.md
         ai-advisor → waived: no model on the path in this item; the vault's retrieval is the Guru item's
         content-steward → waived: no Mom-facing copy — her surface is untouched; door copy for Paul is not hers
- depends-on: .plans/2026-09-03-c5-record-prep-PLAN.md
- depends-on: .plans/2026-09-03-c4-environments-PLAN.md
- ready: [paul-approved 2026-09-03]
- stage: build
- wip-exception: C4 stays `build` only because its remaining steps (2c/2d the visit · 4b the session seam · 4d the rename · 5d the split) are all HELD on Paul; nothing in C4 can move tonight. C6 opened under Paul's 2026-09-03 instruction to run the queue autonomously; its shipped steps (2a–2c · 3b/3c) touch no C4 file.
- stage-note: opened 2026-09-03 9:00 PM ET — steps 2a–2c shipped; 1b/1c wait on Paul's A+ default gate; 3 waits on the privacy seat, spawned

Drafted by the planning agent 2026-09-03 from the row, § M3, C4's RULED table and its three-levels ruling (decided, not
re-argued: product apex · family door per family · instance by grant; two example families, `<family-a>` and `<family-b>`;
the app served from Cloudflare; **a subdomain is ROUTING — the Worker derives the grant from the credential and checks
the hostname's family agrees**), § C5, the three seat trails, the C4 topology delta, `PRODUCT-ENGINE.md` § BOTH PASSWORDS
ARE OPTIONAL / § Credential ownership is PER GRANT / § Mom's retrofit, the data-model design §2 rule 3, §6, §7, the Worker
script, the viewer and the people register. Files are cited by **name relative to the repo root + role, never by line
number** — C4 renames the root. ⛔ No third party and no real name of Mom appears in this file. **Measured while drafting:**
the viewer emits **no** `door_*` event today (a truthful zero baseline); the Worker's auth path **compares nothing
against the clock** (every TTL is a cache, the rate-limit bucket or the audio blob); `wrangler.toml` still has zero
`[env.*]`; `qa-write-probe.py`, `check-live.py --base`, `instance/`, `engine/` and `momlib.config` **do not exist yet**
(C4 3d/3f, C4 5b, C5 4a/7a) — so every dependency below is real, not ceremonial; `people.json` keys people by `name`
(C5 2b promotes `id`). **Reconciled:** the seat's §6 puts room-authoring at step 3; here it is the vault's gate (5c),
because it is Paul's keyboard and not a build step. C5 1b's rule *"the resolver is the only writer of a non-null
person"* gains a **second declared writer** here — the Worker, from a presented credential — and C5's grep falsifier
must list both at the stamp. The seat's `authOk` finding holds: one credential, string-compared, on her paired phone;
**no step here rotates it**. `entry:off` means *not demanded at the threshold*, never *no credential exists* (seat §3
reading 1) — so the vault is **deferred entry** and tenant-from-credential holds at both doors. **Order:** 1 M3 → 2 the
instrument → 3 the grant map + host check → 4 Paul's binding → 5 the vault as a lookup → 6 the master token, sequenced
so her phone never goes quiet → 7 the ungated writes, declared as `<family-b>`'s gate. Steps 1–2 need no credential,
no privacy seat and no Mom; **step 3 does not open until the privacy seat has reviewed** (Q4).

## Files touched

**Step 1 — M3.** `viewer.html` `wireTextSizeToggle` (`DEFAULT_SIZE` + the dated decision block above it; nothing written
to storage on a default — unchanged); `RELEASE_NOTES.md` (a new-device behaviour is user-facing); **with C5 7:**
`instance/<estate>.json` (`display.defaultTextSize`), `engine/viewer.template.html` (the placeholder), `tools/build-viewer.py`,
`tools/check-config-derivation.py` roster (+1 row); `tools/people.json` `_meta` (the new-phone journey, as a person).
**Step 2 — the instrument.** `worker/worker.js` (a `POST /api/door` branch ahead of the gate, its own rate bucket, key
`door:<date>` through C5 6a's builder); `viewer.html` (a `DoorEvents` sender, not `MetricsCollector`; one rostered
buffer key); `tools/qa-write-probe.py` (C4 3f — DOOR leg); `tools/read-mom-engagement.py` (one door line, `?` before
the route exists); `tools/check-telemetry.py` (WIRED vs USED covers door events); `tools/check-storage-keys.py` (C4 2b).
**Step 3 — the grant map.** `grants.json` in the private sibling (C5 2c — `entry`, `vault`, `credential.hash`, never a
token); new `tools/grant-mint.py` (runs where the sibling is); `worker/worker.js` (`grantFor` + `hostAgrees` beside
`authOk`, called at the top of the router); `worker/wrangler.toml` (`[env.*.vars] FAMILY_HOSTS`, placeholder values only).
**Step 4 — Paul's binding.** `viewer.html` (the Sync settings modal gains a grant field; `WorkerAPI.call` sends the
grant header when present, the master otherwise; `STORAGE_KEYS` += `tateTracker.grant.v1`); new
`tools/check-glance-ungated.py` (the F1 regression, Playwright, asserts the viewer's own marker).
**Step 5 — the vault.** `worker/worker.js` (`GET /api/vault/index`, `GET /api/vault/doc?id=`); `viewer.html` (a vault
card, rendered only when the instance file declares `vault.rooms` non-empty); `instance/<estate>.json` (`vault.rooms: []`
at Fernwood until Q3); the QA fixture instance (one room, two documents, no real contact).
**Step 6 — the master token.** `worker/worker.js` (dual-accept on the read paths; `handleMetrics` stamps `via`);
`.private/fernwood-token` readers (last consumers, listed not moved). **Never here:** `X-Tate-Token`'s name, `sync.v1`,
prod `SHARED_TOKEN`'s value. **Step 7:** nothing built — a reserved header name in this file and the delta's D8 step 16.
**At the stamp:** `BACKLOG.md` § C6 gains `→ READY · .plans/2026-09-03-c6-door-for-paul-PLAN.md`; this file gains `- ready:`.

## Sequence

Each step: **who** · **reversible?** · **the deterministic check**. Existing tools first; new checks prove themselves by mutation.

**1a · The re-ruling, presented as evidence** — **Paul** (Q1) · — · the 08-19 block ends *"do not re-raise the A+
default without new evidence about HER."* The evidence: `text_size_served = {size:"lg", stored:true}` on her device
(08-20, 08-24) and 0 of 37 toggle firings from it. This is a different act from the one walked back: that one
re-formatted every surface for a person on A; this one decides what an **unconfigured** device shows, and hers is
configured — her device is untouched by construction. Check: none; it is a ruling, and 1b does not start without it.
**1b · Interim — the one-line constant** — agent · reversible · `DEFAULT_SIZE = "lg"` in `wireTextSizeToggle`; the
decision block amended in place (dated, the reason, the evidence); **nothing is written to storage on a default** so
`{lg, stored:false}` (served) stays distinguishable from `{lg, stored:true}` (chosen). Ships through C4's QA origin,
then `main` at Paul's gate. Check: `check-live.py --base <QA> --ref origin/staging` exit 0; Playwright, fresh context at
414: `body.text-lg` present at first paint with `/api/*` blocked, and the metrics buffer holds `text_size_served
{size:"lg", stored:false}`; a second context with `tateTracker.textSize=normal` set renders A (the stored key wins — the
proof her `stored:true` device behaves as yesterday); `herConditions()` `clean:true`; after `main`, `check-live.py --wait 180`.
**1c · The served default as instance config** — agent · reversible · **with C5 7** · `instance/<estate>.json`
`display.defaultTextSize: "lg"` (the value; the reason stays in the decision block), a placeholder in
`engine/viewer.template.html`, filled by `build-viewer.py`; the lint roster gains the row (detector: the literal beside
`DEFAULT_SIZE` outside the instance file); the condo fixture declares its own value so *per instance, no fork* is
exercised. Check: `build-viewer.py --check` exit 0; `grep -c '{{' viewer.html` = 0; 1b's Playwright assertions re-run on
the built file; `check-config-derivation.py --selftest` fires on a planted `DEFAULT_SIZE = "lg"` literal under `engine/`.
**1d · The new-phone journey, written as a person** — agent drafts, Paul stamps · reversible · one `_meta` line in
`people.json`: a new device for her is set up by Paul in person — A+ (30 s) and, after 6b, her grant credential. The
working mechanism at n=1, said rather than pretended (seat §1). **Restore-at-binding (seat M3-b) is deferred out of
C6**: it needs C5's `personId` and ux F3 says the device stays authoritative; a mirror is a later item.
**2a · `POST /api/door`, ahead of the gate** — ✅ **SHIPPED 2026-09-03 `c96b085` `[paul: run the queue]`** — write-only no token on its OWN bucket (`ratelimit:door:`), `event ∈ door_reached|door_opened|door_failed`, `door ∈ entry|vault`, no estate field read, stamps `env · receivedAt · personId:null`, key `door:<date>` via `dateKey`, GET behind the token. QA (`qa-write-probe` DOOR leg, 7/7): no-token POST 2xx · GET 401 · 1.1 KB 413 · unknown event 400 · the door bucket 429s at the 21st **while a feedback POST from the same IP still lands** · read-back `env:qa · personId:null · no estate echoed`. Prod: `/health` lists `/api/door`. ⚠️ Two probe defects found on the way and fixed: it read back in a LOCAL-date window (a day behind after 8 PM ET — the Worker keys by UTC) and it did not wait for KV consistency. — agent · reversible (additive; delete the branch) · the `/api/feedback`
shape: write-only, no token, `Content-Length` ≤ 1 KB, rate-limited on **its own bucket** (`ratelimit:door:`) so a door
storm never 429s a note; body `{event ∈ door_reached|door_opened|door_failed, door ∈ entry|vault, deviceId, ts}`; ⛔
**no estate field is read** — one is ignored if sent (seat §4); the Worker stamps `env`, `receivedAt`, `personId: null`
(C5 1a), and a person **only** from a valid grant header on `door_opened` — a failed credential attributes nothing.
Key `door:<date>` via C5 6a's builder; GET falls through to the gate. Check, **QA Worker only**: `qa-write-probe.py`
DOOR leg — no-token POST → 2xx; GET no token → 401; 1.1 KB → 413; the 21st in 5 min → 429 **while a feedback POST from
the same IP still lands** (the separate bucket, positive control); read-back carries `env:"qa"`, `personId:null`, and no
estate echoed from the body. Prod after `deploy-worker.sh`: `/health` lists `/api/door`; nothing else changes.
**2b · The client sender** — ✅ **SHIPPED 2026-09-03** — `DoorEvents.send(event, door)` posts direct with `keepalive`, never through `MetricsCollector`; buffers under the rostered key `tateTracker.door.outbox.v1` when offline and flushes on load; **nothing calls it yet — `door_reached = 0` is the truthful baseline**. `check-storage-keys.py` passes with the key rostered; the viewer walks clean on QA and prod. — agent · reversible · `DoorEvents.send()` posts direct with `keepalive`, never through
`MetricsCollector` (its flush is gated — the locked-out person is exactly who it cannot carry); buffered under a
rostered key when offline (the site premise) and flushed on the next in-range load. No door exists yet, so nothing
fires: **`door_reached = 0` is a truthful baseline**, the denominator the seat's rule needs. Check: `check-storage-keys.py`
passes with the key rostered and fails on a planted unrostered one; on the QA origin under `d-telemetrytest-harness-v1`
a synthetic send lands in QA KV; `check-telemetry.py` reports it WIRED, not USED.
**2c · The reader** — ✅ **SHIPPED 2026-09-03** — `read-mom-engagement.py` gains the door line (`?` before the route is readable · `unbound` · `UNREACHED · N sessions · 0 door events — go look` · counts since binding), `--selftest` 4/4, binding date read from the private `grants.json` (`boundAt`, lands with 4a). ⚠️ **Found on the way:** this reader and `read-mom-funnel.py` still opened `tools/people.json` directly for device ids — after C5 8a's move that mapped NOBODY and would have counted zero for Mom silently; both now read momlib's merged register and print UNMAPPED when the private register is absent. — agent · reversible · `read-mom-engagement.py` gains one line: door events on her device since the
last lap, **and sessions on a bound device with zero door events** (metrics sessions × `door:` records × the binding
date from `grants.json`; runs where the sibling is). Before 2a exists on prod it prints `?`, never `0`. Check:
`--selftest` — bound device, 3 sessions, 0 door events → `UNREACHED · 3 sessions · 0 door events — go look`; unbound
device → `unbound`; a window before the route → `?`.
**3a · The grant row and the mint** — agent (rows) · Paul (values) · reversible (delete the row) · ⛔ **after the
privacy seat reviews (Q4).** `grants.json` (C5 2c) rows gain `entry`, `vault`, `credential: {hash, issuedAt, issuedBy,
revokedAt: null}` — **never a plaintext token**. The KV user store: `grant:<sha256(presented)>` → `{personId, estateId,
relationship: [...], capability, entry, vault, issuedAt}` — **no `exp`, no TTL** (seat §2 discipline 1). Hashing *what
is presented* is what lets Paul's row hold an opaque minted token and her row hold a word, if the seat allows a word
(Q5) — the door does not decide that. `grant-mint.py`: mints (`secrets.token_urlsafe`), writes the hash row, emits the
`wrangler kv key put` for the target env, prints the token **once**, through `/secrets` — never a file, a transcript or
a commit. `--revoke` = one KV delete + `revokedAt` — an act with an author. Check: `--selftest` — mint → the row has a
hash and no token; `git -C <sibling> grep -c <token>` = 0; revoke → `wrangler kv key get` not-found; in the public repo
`git grep -c grants.json` = 0.
**3b · `grantFor(request)` beside `authOk`** — ✅ **BUILT + QA-PROVEN 2026-09-03 `e911007`** — `X-Grant` → `sha256Hex` → one KV `get` of `<estate>:grant:<hash>` → row or null; **the row's `estateId` must equal `env.ESTATE_ID`** (the seat's condition ①; a foreign row is *no grant*), `revokedAt` honoured, no clock compared (`grep Date` inside = 0), the estate never read from path/query/body (grep = 0). `/api/grant/whoami` is the one read a grant unlocks today (personId · estateId · capability · relationship · entry · vault). QA, with two fixture rows planted in the QA namespace only (tokens in the scratchpad, never the repo): valid grant → 200 the row; another estate's grant → 404; garbage → 404; no grant → 404; a grant alone still cannot read `/api/feedback` (401 — 6a widens). — agent · reversible · reads the grant header (name ≠ `X-Tate-Token`,
seat discipline 2), hashes, one KV `get`, returns the row or `null`; **the estate comes from the row** and is passed into
C5 6a's `keyFor(estateId, …)` — the signature is already shaped for it. Any estate on the path, query or body is
**ignored**. It compares nothing against the clock (ux F2's checkable rule). Check: C5 6a's grep stays 0; `grep -n
'Date.now\|new Date' worker/worker.js` has no hit inside `grantFor`/`hostAgrees`; on QA, two grants → two estate ids
(`fernwood-qa`, `estate-b-qa`; fixtures, no family name) — each reads only its own prefix; a cross-read is not-found.
**3c · `hostAgrees(request, grant)` — the check and its fail mode** — ✅ **BUILT + QA-PROVEN 2026-09-03** — sits AFTER preflight and the credential-free capture POSTs (seat 15), before anything a grant unlocks; `FAMILY_HOSTS` per env (only already-public hostnames in the toml: prod `palekxk.github.io`, QA `fernwood-qa.pages.dev`); no Origin agrees vacuously (seat-confirmed); mismatch → **the router's own `{error:"not-found", path}` 404** and a server-side `door_failed {reason: host-mismatch | unknown-or-other-estate, serverSide: true}` written through `ctx.waitUntil` (the seat's timing oracle). QA: valid grant + QA Origin → 200; valid grant + `Origin: https://family-b.example` → 404; the QA `door:` key gained both reasons. ⚠️ Note for 6a: an unauthenticated unknown path answers 401 (the master gate comes first), so the byte-identical 404 is identical to the *authenticated* 404 — the seat's intent (no 403, no existence leak) holds. — agent · reversible · at the **top of the router
before any dispatch** (delta D3 — handlers here are reached by paths that bypass the gate above them). *The credential
decides; the hostname must agree*: the hostname is the request's `Origin` under P1 (Pages serves the page) or the
Worker's own host under P2 — one function, one line differs. `FAMILY_HOSTS` per env in `wrangler.toml` holds
**placeholders** (`family-a`, `family-b`); real hostnames are set as vars from the sibling at deploy — a family's name
never enters a tracked file. Mismatch → **404, never 403** (a 403 confirms the door exists and the token is valid for
something); a server-side `door_failed {reason: host-mismatch}` lands in `door:` — the client never learns why.
No `Origin` (curl, tools) = no claim → agrees vacuously — **the seat confirms or tightens this**. Ungated POSTs with no
credential are untouched (step 7). Check on QA: `-H 'Origin: https://family-b.<qa-host>'` + family-A's grant → 404;
family-A's origin → 200; no `Origin` + a valid grant → 200; the QA `door:` key gains the server-side record.
**4a · The declaration** — **Paul** (Q2) · reversible · `grants.json`: her grant `entry:off, vault:on`; Paul's
`entry:on, vault:on`. The Worker reads the flags from the row; the client never guesses them. In this item `entry` has
**no paint consumer** — its first is the family door's chooser (C4's item). Declaring it now is what keeps her
`entry:off` a **declaration** rather than an absence when that door lands.
**4b · The binding act, on Paul's device** — agent builds, **Paul binds** · reversible (clear the key) · the Sync
settings modal (opened on her phone only by Paul, at pairing) gains one field, *grant* — the one text input in the
product, on the administrator's device (activation §3's corollary); stored under `tateTracker.grant.v1`, **named unlike
`sync.v1`**; `WorkerAPI.call` sends the grant header when present, the master otherwise (additive). First paint reads
localStorage and nothing else. Events: `door_reached` on opening the field, `door_opened` on a 2xx probe
(`GET /api/vault/index`), `door_failed` on 401/404. Check: `check-glance-ungated.py` — fresh context, 414 × A+, QA
origin, all `/api/*` blocked: masthead, jump strip, six destinations, weather card and composer render and accept input;
**the viewer's own marker is present or the tool throws** (a 404 page scores green otherwise); the request log before
the first-paint marker holds **zero** requests to gated routes; re-run with `grant.v1` set → the same first paint;
`herConditions()` `clean:true`. Her device: nothing.
**5a · The vault routes, shaped as a lookup** — agent · reversible · `GET /api/vault/index` (ids, titles, kinds,
capped) and `GET /api/vault/doc?id=` (one document), behind `grantFor` + `hostAgrees` + `vault:on` on the row; estate
from the grant; content at `<estateId>:vault:<docId>` in KV (a text room needs no object store — the 254 scans are the
**worst** first room, seat §3). ⛔ **No route returns the whole room** — a dump is what the Guru would inline, and the
digest is already ~127K tokens. Wrong or revoked credential → 401 with a shaped body `{error, door:"vault"}` (copy is
the steward's, later), never a timeout. Attribution begins here: a person on any write behind the vault comes from the
grant (seat §3 consequence). Check on QA with the fixture room: index → 2; doc → 1; the other estate's id → not-found;
no token → 401; `grep -c 'vault/all\|vault/dump' worker/worker.js` = 0; `check-digest-fresh.py` exit 0 and
`worker/digest.json` byte-identical — the Guru item's rung-3 lookup is what will call `doc?id=`, and nothing here forecloses it.
**5b · The vault card, in place, declared per instance** — agent · reversible · a Fernwood card in the stream (ux F2:
identity square, Crimson title, the ratified affirmative components — literally those; not a modal, not a redirect),
rendered **only** when the instance file declares `vault.rooms` non-empty. Fernwood declares `rooms: []` — declared
empty, never absent — **until Paul rules Q3 and authors the room**; QA's fixture declares one. So prod renders no card
and her surface is untouched **by construction**; the day a room is declared at Fernwood, this header's ux and content
waivers expire and that ship is its own gate. Check: built with Fernwood's instance → Playwright at 414 × A+ finds no
`.vault-card`; built with QA's → present; tapping it unbound records `door_reached` and renders the door in place
(`location.pathname` unchanged, no modal open); bound → the index renders.
**5c · The first room — Paul's keyboard** — **Paul** (Q3) · — · a text file (contacts / shut-offs) authored in the
sibling, loaded to KV by a tool. Not a build step and not this plan's to schedule; listed so the vault is read as
blocked on an authoring act, not on auth (seat §0 #5).
**6a · Dual-accept on the read paths** — agent · reversible · the gate becomes `authOk(master) || (grant && host
agrees)`; `capability: administrator` unlocks what the master unlocks today (reads of her words, chat spend,
promote/remove, admin clean); `contributor` unlocks `/api/metrics` POST and the vault only (the wrong-capability code
is the seat's). `handleMetrics` stamps `via: "master"|"grant"` per batch. **Nothing is removed**; her paired phone keeps
reporting through the master. Check: on QA both credentials read `/api/feedback`; a contributor grant on
`/api/promote-species` is refused; on prod after deploy, `check-live.py`, `test-feedback-cycle.py` unchanged;
`read-mom-engagement.py --pickup` shows her sessions still arriving, `via:master`.
**6b · Her credential onto her phone — in the C4 2d visit only** — **Paul with her** · reversible (clear the key) ·
pasted into 4b's field, his thumb, ~30 s, in the same sitting as A+ and the master re-paste C4 already carries.
Nothing she sees changes (Tuesday looks like Monday). After: her batches read `via:grant`. ⛔ **No step in C6 rotates
prod `SHARED_TOKEN`.**
**6c · Retiring the master from metrics, then rotating** — agent proposes, **Paul gates** · ⛔ not reversible past the
rotation · only after **7 days of her device's batches with zero `via:master`** (a measured zero, the C4 4c idiom — not
a calendar); then master acceptance drops from the metrics POST; then the rotation via `/secrets` in a real TTY —
never `!`, which uploads an empty secret and prints success. The master survives for tools until each
`.private/fernwood-token` reader is on an administrator grant. Check: `read-mom-engagement.py` after the rotation shows
sessions from her device, `via:grant`; `test-feedback-cycle.py --live` (Paul's) green.
**7 · Closing the two ungated writes — `<family-b>`'s gate, not Paul's** — **declared, not built** · the fix is a
per-family write key **she never types**: baked into the family door's built bundle by C5 7b from instance config, sent
on the two POSTs, mapped by the Worker to a family, 404 without it — never a return to per-device pairing (the 07-15
loss). It **blocks `<family-b>`'s host** (delta D8 step 16) and **blocks nothing for `<family-a>`**: the same two people,
the same access. The header name is reserved so 3c has a claim to check on ungated POSTs later; the design is the
privacy seat's to review before it is built. Check when built: no-key POST at a family-B origin → 404; family-A's
key at family-A's origin → 2xx; **her phone's POSTs still land with no paste** (the key rides the bundle).

## Falsifier

For the design as a whole — each observation, and how it is measured:
- **A locked-out person is invisible to the record.** Measured: on QA, a wrong credential at the vault produces no
  `door_failed` in `door:`; or 2c prints `0` where the route did not exist. If true, `does not want the private tier`
  and `locked out` are still one observation and the door must not ship (the seat's absolute rule).
- **Her glance gains an auth round-trip.** Measured: `check-glance-ungated.py` logs any request to the Worker before
  the first-paint marker on her origin, bound or unbound; or her first paint differs between the two runs. If true,
  F1a is violated whatever the code intends.
- **A token is accepted at the wrong family's door.** Measured: 3c's cross-family curl returns anything but 404; or a
  handler is reachable without passing `hostAgrees` (a route added below the check). If true, the subdomain is access,
  not routing, and rule 3 is decorative.
- **Her telemetry goes quiet after a rotation.** Measured: `read-mom-engagement.py` reads zero sessions from her device
  over a window with no visit recorded in `people.json`. If true, 6's sequencing was skipped and her denominator died silently.
- **Identity is applied backwards.** Measured: a non-null `personId` on any record dated before its grant's `issuedAt`;
  a person stamped on a `door_failed`; or `git grep -l personId -- tools worker` lists a writer beyond C5's resolver and
  3b. If true, the 2026-08-01 retraction is recurring with a stronger-looking warrant.
- **An estate id rides a client request.** Measured: C5 6a's grep > 0, or `grep -c 'estate=' viewer.html` > 0. If true,
  the selector's arrival will turn it live retroactively (seat §4).
- **Trust is revoked by a clock.** Measured: a `Date` comparison inside `grantFor`/`hostAgrees`, or a TTL on a `grant:` key.
- **The vault forecloses the lookup.** Measured: a route returning more than one document, or a vault key in the digest.
- **The readiness mechanism is ceremony** (readiness §5, discharged in `## Retro`): steps that exist only because a seat
  measured something — today 2a (the gated-metrics finding), 2b's own bucket, 3c's 404, 5a's no-dump, 5b's `rooms: []`,
  6c's measured zero. Zero at retro is a valid, informative answer.

## QA

**Agent may exercise, and where.** Steps 1b–1c: the QA origin via Playwright at 414 × A+ and locally
(`python3 -m http.server 8765` + `herConditions()`); `main` only at Paul's gate. Steps 2–3, 5a, 6a: **the QA Worker only**,
after C4 3f is green (`/health` → `env:"qa"`, `kv_canary:"qa"`) — plant, read back, revoke, delete; two fixture grants,
one fixture room, no real contact, no family name. Steps 4b, 5b: the QA origin, then **Paul's device** for the binding.
On prod, permanent: **read-only** — `/health`, `check-live.py`, `GET /api/feedback`, `read-mom-engagement.py`; the Worker
deploy for 2a and 6a is the agent's (`deploy-worker.sh`, sandbox off; `/health` proves it), both additive.
**Agent may NOT:** mint or hold a credential value outside `/secrets`; rotate or re-set prod `SHARED_TOKEN`; write
`grants.json` values (rows yes, values Paul's); touch her device or her origin's storage; author the first room or the
door's copy; write a non-null `personId` anywhere but C5 1b and 3b; run `test-feedback-cycle.py --live`; write `- ready:`.
**Paul verifies:** Q1–Q4 before the steps they gate; the binding on his own device (4b) and the first `door_opened` in
QA KV; `check-live.py --wait 180` after any viewer ship; the 7-day `via:master` zero before 6c; the rotation itself.
**Mom's presence: nothing — and if a step needs her phone outside the C4 2d visit, the plan is wrong and the step stops.**
6b is the one act on her device, and it lands inside that visit, alongside what C4 already carries.
**Expected outputs, named:** `check-glance-ungated.py` → `marker present · 0 gated requests before first paint · glance
complete`; `qa-write-probe.py` DOOR leg → `2xx · GET 401 · 413 · 429 with feedback still 2xx · env qa · personId null`;
3c's curl → `404 · 200 · 200`; `read-mom-engagement.py` → `door: ? (route absent on prod)` today; `check-backlog-ready.py` → silent.

## Open before stamping

> 🔒 **PRIVACY SEAT RAN 2026-09-03 (an agent — Q4 answered: an agent, because four of its fifteen findings existed only
> because something was executed or fetched). Trail: `.engineering/2026-09-03-c6-privacy-seat-review.md`.** **Verdict:
> step 3 OPENS on four conditions** — ① `grantFor` ASSERTS `grant.estateId === env.ESTATE_ID` and 404s otherwise (never
> thread a row-derived estate into `keyFor` beside the binding — two estates in one request); ② QA gets its own estate id
> — **done tonight: `est-qa0001`**; ③ the mismatch 404 is byte-identical to the router's real 404; ④ `X-Grant` is the
> header and it is in `Access-Control-Allow-Headers` — **done tonight**. **Q5 answered: NO word — the presented credential
> is an opaque minted token for every grant, hers included** (`grant:<sha256(presented)>` uses the hash as the KEY, so no
> per-row salt is possible; a word's only defence would be entropy it does not have). A device-local unlock over the stored
> token is the named successor if Paul still wants a word. **Also fixed tonight from the review:** feedback fields bounded
> and the body measured (finding 12 — Content-Length is advisory; every POST rewrites a day's key); `personSource` on the
> resolver's attributions (finding 10). **For Paul:** the station MAC sits in the public `wrangler.toml` (a device id,
> ruled private) — moving it to a Worker secret means a short ambient outage between the var's removal and the secret's
> landing, so it is his call and his `/secrets` (finding 3); `fernwood-qa.pages.dev` answers anonymously — the C4 delta's
> "Access-gated" claim is wrong; Cloudflare Access on QA is a decision (finding 13). **Design notes carried into 3c/4b/6a:**
> the host check is routing not access control (4); `X-Tate-Token` is set in 7 client places, not one (14); the host check
> sits AFTER preflight and the credential-free capture POSTs (15); 6a's grant unlocks reads + metrics + vault only, branching
> on `capability` never `relationship` (8); the host-mismatch record write goes through `ctx.waitUntil` (timing oracle).

> **✅ STAMPED 2026-09-03 `[paul-approved]` — Q1 ruled DIFFERENTLY from the recommendation; Q2 · Q6 on the
> recommendations as written** (Paul opened with *"Yeah"* and then re-ruled only Q1 — read as acceptance of the other
> two; a one-word reversal re-opens either).
> - **Q1 → THE TOGGLE GOES. A+ (`lg`) becomes the ONE standard size; there is no served default because there is no
>   choice.** Paul: *"for now, let's just remove the text zoom and make A+ just the standard text. We can always come
>   back to that. If we do anything, I would think we would add an option to make the text even bigger for older people,
>   frankly. But let's save that for later — that can go to the frozen questions."* **Consequences, and step 1 must be
>   RE-DRAFTED before build:** 1a is discharged by this ruling · 1b/1c are **void** (no `DEFAULT_SIZE`, no per-instance
>   `display.defaultTextSize`, no placeholder, no lint row) and are replaced by **1b′ remove the control and make `lg`
>   the base styling** — the stored `tateTracker.textSize` key is left in place and no longer read (never deleted from
>   her phone), `text_size_served` / `text_size_changed` retire from the instrument roster with a dated note, the
>   08-19 decision block in `wireTextSizeToggle` is superseded in place with this ruling, and `RELEASE_NOTES.md` carries
>   it (a control she can see disappears — **Mom-facing, so it ships through C4's QA origin and `main` at Paul's
>   gate**) · **M3 retires by construction** — nothing is left to sync, so *"M3 fixed first"* is satisfied by removal ·
>   1d stands, shorter (a new phone needs no A+ step). ⚠️ Measured footprint: `viewer.html` carries **158** lines
>   mentioning `textSize` / `text-lg` / `wireTextSizeToggle` — the removal is a real edit, not a constant flip; the
>   `.text-lg` class either becomes the base or every rule under it is folded into the base rule set. **The "even
>   bigger" option is parked in the FOCUS FREEZE** (`BACKLOG.md` § FOCUS FREEZE → frozen questions), not here.
> - **Q2 → `entry:off, vault:on` for her grant; Paul's own `entry:on`.**
> - **Q6 → `/api/ambient` stays ungated in C6.**
> - **Still open at their named steps:** Q3 (the first vault room — 5c) · Q4 (privacy seat, agent or checklist — before
>   step 3; recommendation stands: agent) · Q5 (her credential word — Mom's retrofit, not this item). The flagged
>   `isTestHarness` split stands as the recommendation.


1. **Q1 `DEFAULT_SIZE` re-ruling** — may the served default become a declared per-instance value set to `lg`? Ruled
   `normal` on 08-19 on *"she is habituated to A"*; the record now reads `{lg, stored:true}` on her device. Yes / no.
   1b cannot start without it; 1c follows C5 7 either way.
2. **Q2 The entry default** — `entry:off, vault:on` for her grant is **agent-proposed, not ruled**; Paul's own
   `entry:on`. Nothing paints on it in this item, but 4a declares it and the family door will read it.
3. **Q3 The first room in the vault** — the seat's input: a **text** room (contacts / shut-offs), authored before the
   door; not the scans. Until ruled and authored, Fernwood declares `rooms: []` and her surface shows no card.
4. **Q4 The privacy/security seat — an AGENT or a CHECKLIST.** Its unpark condition fired 2026-09-02; either satisfies
   *"reviews before build"*; only an agent accrues across the portfolio. **Step 3 does not open until it has run.**
5. **Q5 Her credential word** — asked in conversation, never typed by her; a word she would tell Paul, never *"a
   password"*. Not needed for Paul's door. And for the seat: is the word itself the presented credential, or does it
   unlock a minted one on the device? 3a's hash-of-what-is-presented fits both.
6. **Q6 Whether `/api/ambient` stays ungated** — the third ungated route, read-only, scoped to one station, ruled
   *subordinate to her access* on 08-02. Recommend unchanged in C6; under two families it becomes a per-instance
   question (whose station), which is 3c's `hostAgrees` on a read path — the seat's to weigh.
7. **Flagged, not decided:** whether door events are exempt from `excludeFromEngagement` so Paul test-driving his door
   does not read as a person hitting it (seat §8 Q5 — recommend the `isTestHarness` split, not an exemption); the
   wrong-capability response code within a family (6a).
