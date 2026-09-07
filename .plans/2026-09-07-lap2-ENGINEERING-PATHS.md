# Lap 2 → lap 3 — the identity seam, six paths

- row: F4 · F5 · F6 (`.plans/2026-09-07-lap3-paul-feedback-CAPTURE.md`) · BACKLOG rows 14 · 20
- objective: O5 (the loops are the artifact) · C6/C7 (the door)
- kind: path-eval
- seats: engineering-partner, one seat, reading production code at `1e2748d`
- ready: agent-proposed 2026-09-07 — Paul rules
- gate: ⛔ NOTHING HERE EXECUTES. No code was written. Every option below is a shape, not a patch.
- provenance: Paul's production walk 2026-09-07 as owner of `est-e6696a` (account `pkirsch`,
  person `p-yjnw9lt41nww`), three repairs to reach his own account. His framing, verbatim:
  *"An account's facts and its credential are two separate records, and exactly one code path
  reconciles them — the one with no door."*
- revision: **v2, same night.** The coordinator challenged §D's premise (*"ObservationStore never
  sends `X-Grant`"*) as too absolute. Re-measured. **The premise survives for the store that backs
  the notes and was wrong as a statement about the file** — §D now carries the inventory instead of
  the word "never". ⭐ **And re-measuring found the actual size of F4**, which is not a door-card
  bug: the same owner guard is copy-pasted at **nine** sites and governs the whole household app.
  §B is rewritten around that. The challenge was worth more than the answer.
- code read: `worker/worker.js` (handleAccount :455-517 · handleSession :559-628 · whoami
  :3605-3645 · the entry gate :3660-3678 · applyGeocode :869-905 · handleObservations :1098-1127 ·
  loadObservations :1030-1043) · `estate/index.html:220-590` · `viewer.html` (the nine guard sites,
  inventoried in §B) · `tools/grant-mint.py`
- calibration: two households, one of them Paul's own, one invite unspent in Mom's hands. Severity is
  read against that, not against a system with users.

---

## 0 · The finding that reorganises A–F, and it is not the one that was walked

Paul's framing is right and it is one layer short of the actual cardinality problem.

**`acct.tokenHash` is singular.** `handleSession` mints a new token, writes the new grant row, and
then does this (`worker.js:614-616`):

    if (acct.tokenHash && acct.tokenHash !== tokenHash) {
      await env.OBSERVATIONS.delete(keyFor(scope, "grant", acct.tokenHash));
    }

**So signing in on a second device deletes the first device's credential.** Phone A then answers 404
at `/api/grant/whoami` — which is repair #1, exactly as walked tonight, and it is not a KV divergence
or a lost row. It is the shipped design working as written.

The account row models **one live credential**. The product promises *"a way back in — so this is
yours on any phone, not just this one"* (s0, quoted in `estate/index.html:243`). Those two statements
cannot both be true, and nothing in the repo says so.

⚠️ **This is the premise under A, and it changes what "fix the copy" means.** Widening the writer set
for the eight place facts does not help a device whose grant has been deleted out from under it. The
copy is a symptom; the cardinality is the disease; the missing door is why neither was ever felt.

Three claims, and their evidence class:
| claim | evidence |
|---|---|
| sign-in deletes the prior grant | 🟢 read directly, `worker.js:614`; ✅ independently confirmed by the coordinator |
| that is what produced repair #1 tonight | 🟡 `inferred` — consistent with a 404 on a grant that once worked; not proven against the KV history |
| the register/KV divergence `watch-accounts.py` reports is the same event | 🟡 `inferred` — the register is written by `grant-mint.py`, the delete is server-side and the register never hears about it, which would produce exactly that divergence class |

**Cheap falsifier for all three:** mint a grant, read whoami (200), sign in as the same account in a
second browser, re-read the first grant's whoami. A 404 confirms it in under a minute.

---

## A · The identity seam — two records with a copy, or something else

**Read `worker.js:595-612` before anything here.** The copy has a stated, correct reason: `/api/profile`
writes the **account** row; `/api/grant/whoami` reads the **grant** row; without the copy, whoami cannot
see facts the account holds, which is precisely the 2026-09-06 defect that comment records. It also
states its own discipline — *copied, not moved* — and refuses to overwrite a present value with a null.
**None of that is wrong. It is a cache that acquired exactly one writer, and the writer sits behind a
door that was never built (BACKLOG row 20).**

One structural fact decides the option set: **a grant row has no pointer to its account.** It carries
`personId`; accounts are keyed by *username* (`accountKey(scope, username)`). So today there is no
read-time path from a credential to its record without a scan. That is why the copy exists and it is
also the cheapest thing to change.

### The options

| | shape | what it costs | what it buys | second device |
|---|---|---|---|---|
| **A1** | keep the copy, **widen the writers** — every account-fact write also refreshes the live grant | N writers must remember; a helper + a drift check makes it survivable | smallest diff; no read-path change | ⛔ still stale until that device signs in; ⛔ still only one live grant |
| **A2** | **grant references the account; whoami joins at read time.** Grant carries `personId`; add `<estate>:person:<personId> → {username}`; whoami reads grant → pointer → account and returns the account's facts. Delete the eight-field copy. | +2 KV reads per whoami (edge-cached, effectively free at this volume); a pointer row written at signup and at rename; a one-time backfill for 2–3 existing accounts | **one record is authoritative and has zero fan-out.** Every fact a person edits is visible on every device on the next load, with no sign-in | ✅ any live grant reads current facts |
| **A3** | keep the copy + a **`factsVersion` stamp**; whoami compares and refreshes lazily | you must read the account to compare the version — so you have already paid A2's cost — **and** you keep A1's writer discipline | nothing A2 does not | ✅ but at strictly higher cost |
| **A4** | key accounts by `personId`, make `<estate>:account:<username>` a pure index | a real migration of the auth path | the cleanest end state | ✅ |

**A3 is dominated and is written down so it stops being re-proposed** — this corpus's measured leak is
that a rejected alternative nobody recorded gets proposed again next lap (`VOCABULARY.md` §4's whole
rationale).

**A4 is right and premature.** At two accounts it buys the same thing A2 buys, for a migration of the
one path where a mistake locks somebody out of their own house. `handleRename`'s comment already shows
how carefully that path has to be ordered. Not this lap.

### Recommendation — **A2**, plus a per-account grant **set**

Two changes, and the second is separable:

1. **whoami joins.** The account row becomes the single source of truth for place facts, exactly as
   `[[Single source of truth per record, declared explicitly]]` asks. The `worker.js:595` copy loop
   is deleted and its comment is rewritten to say what replaced it and why — *the reason it existed is
   still true; the read path just stopped needing it.*
2. **stop deleting the prior grant on sign-in.** Keep `acct.grants: [tokenHash, …]`, cap it (5 is
   generous for a household), evict oldest. The security intent behind the rotation — *"a stolen or
   stale credential stops working the next time she signs in"* — is preserved by making **sign out
   everywhere** an explicit act a person takes, rather than a side effect of using a second phone.
   ⚠️ This is the half that carries a real trade: today a stolen link dies at the next sign-in without
   anyone doing anything. After the change it dies when someone asks it to. At two households with a
   product whose stated posture is *light privacy, never at the cost of her access*, that is the right
   side to err on — **but it is Paul's call, not mine.**

**Why A2 is the "cohesive" answer Paul asked for:** it closes A, closes C, and closes half of F, in one
change. See §F — the coordinates backfill is already written and both of its ends read and write the
cache instead of the record.

**What breaks on a second device today, enumerated** (so the fix can be checked against a list):
| # | symptom | cause | closed by |
|---|---|---|---|
| i | grant 404 on the older device | sign-in deletes the prior grant | A2 part 2 |
| ii | a minted grant is born blank | `mint()` carries identity only; the copy has one writer | A2 part 1 |
| iii | a profile edit on A never reaches B | same | A2 part 1 |
| iv | B fetches the right record and hides it — **and hides the rest of the app with it** | the owner stamp names A's grant | **B**, below |

**Falsifier for A2:** change `placeName` via `/api/profile` on device A. Device B, holding a live grant
and having never signed in since, must show the new name on its next load. If it does not, the join did
not replace the copy.

**Falsifier that would prove me wrong:** if a whoami join measurably slows the door — it is the one
request that stands between a person and their place — the copy earns its keep and A1 is right. I do
not expect this (two extra KV reads at the edge, on a request that already does one), but it is
measurable and it should be measured rather than assumed.

---

## B · The owner guard — 🔴 nine sites, not one, and it decides what app you get

### ⭐ REVISED. F4 is not a door-card defect.

`(!o || o === g)` — or its inverted twin — is **copy-pasted at nine sites**, one in `estate/index.html`
and eight in `viewer.html`. It is not a component, it is a phrase. Every site was added correctly, for
a stated reason, usually to close a real leak. **Nobody has ever read them together.** Here they are:

| # | site | what it gates | what a stale stamp does |
|---|---|---|---|
| 1 | `estate/index.html:269` | all seven door-card rows | 🔴 the walked defect — correct record fetched, every row suppressed |
| 2 | `viewer.html:6420` | **`window.__HOUSEHOLD_NAME`** | 🔴🔴 **see below — this one governs the whole app** |
| 3 | `viewer.html:7312` | `adoptHouseholdCoordinates()` | 🔴 the household paints **unplaced (S0)** — no weather, no sky — *even with correct coordinates in localStorage* |
| 4 | `viewer.html:18062` | `addressIsBox()` | 🟠 a PO-box household stops being told the app cannot place it — the honesty line Paul ruled on 09-06 goes silent |
| 5 | `viewer.html:18078` | `READER_RANKING` | 🟠 every card falls to variant B; *"You put Gardening first"* never renders |
| 6 | `viewer.html:18208` | the ask-next `/api/feedback` POST | 🟠 **fails CLOSED** — no request at all, the ranking-add is lost silently |
| 7 | `viewer.html:18400` | `renderHouseholdFirstScreen()` | 🟠 the place card is not promoted to the front |
| 8 | `viewer.html:12940` (`sendRecord`) | whether `X-Grant` rides on a feedback POST | 🔴 **fails OPEN — see the coordinator's finding below** |
| 9 | `viewer.html:19803` (`grantHeader()`) | MetricsCollector's flush | 🔴 **telemetry stops entirely for that device** |

### 🔴🔴 Site 2 is the one that changes the size of this

`__HOUSEHOLD_NAME` does **two jobs**, and its own comment at `:6423` says so — it is the name to print
**and, in eleven places, the test for "is this a household at all."** A stale owner stamp makes it
empty. So a household on a device that once held another grant does not get a broken card. **It gets
the pre-ruling Fernwood reference app**: every empty module renders, the journal tile returns, the place
card does not appear — the exact surface Paul ruled against on 2026-09-07, restored silently by a
localStorage key.

⭐ **And it flips `ObservationStore.getStatus()` from `household-local` to `local-only`** (`:20470-20474`
tests `window.__HOUSEHOLD_NAME`). So the person is told *"Local only — set up Sync to follow you between
devices"* — the paired-device instruction three seats rejected as *"the app not knowing I signed in"*,
and the sentence that was deliberately replaced. **The fix for that copy is undone by a stale stamp**,
which ties §B directly to §D.

### 🔴 Site 8 — the coordinator's finding, and it is the sharpest one on this page

    if (base.token) headers["X-Tate-Token"] = base.token;
    else { const g = …, o = …;
           if (g && (!o || o === g)) headers["X-Grant"] = g; }

The guard's own comment states the rule it is enforcing: *"FEEDBACK MUST HAVE AN ACCOUNT ASSOCIATED
WITH IT `[paul-ruled 2026-09-06]` … an unpaired device sent none, so every new household's note landed
personId:null."*

**On a device whose owner stamp names a prior grant — Paul's state for most of tonight — the guard
withholds the header, the POST still fires, the Worker still accepts it, `res.ok` is true, and the
record lands `personId: null`.** The client logs nothing; the person sees a normal confirmation. **A bug
ruled fixed on 09-06 silently re-opens on 09-07, through a guard added to fix a different bug.**

⚠️ **And it is worse than a lost attribution, because of what is being built next.** Paul has a
per-account feedback sweep queued for lap 3. A sweep that reads `personId` finds orphaned records **and
has no way to learn why** — the record carries no marker saying *a credential was available and was
withheld*. It will read exactly like an unpaired device, which is the state this rule was written to
eliminate. **The sweep will be measuring a population it cannot explain.**

### The two invariants, and they are different

**① A guard that strips a credential must not leave the request sendable.**

Sites 6 and 8 are the *same guard* on the *same endpoint* with **opposite failure postures** — 6 fails
closed (nothing sent), 8 fails open (sent, unattributed). That divergence is not a decision anyone made;
it is what happens when a rule is a phrase instead of a function. The rule:

> *Withholding a credential and sending the request are two acts. Do one or the other — never both.*
> A request that cannot be attributed must either not be sent, or must carry an explicit marker that
> attribution was unavailable, so the absence is **readable downstream instead of indistinguishable
> from a device that never had one.**

That marker is the part that matters for the lap-3 sweep. `personId: null` today conflates *never had a
credential* with *had one and the client refused to attach it*. The Worker already models exactly this
distinction elsewhere and states the principle in its own words (`:340`): *"an absent field means
'written before the field existed'; a null means 'written after it existed and nobody could say' — two
different observations, kept different."* **Site 8 produces a third observation and files it under the
second.**

**② The guard is being applied to the one thing it must never gate.**

`(!o || o === g)` answers *"are these stored ANSWERS mine?"* — a question about **localStorage**, and a
correct and necessary question at sites 1–5 and 7. Sites 8 and 9 use it to answer *"may I attach my
CREDENTIAL?"* — a question about **the grant**, and one it has no business answering. **If this browser
holds a grant, that grant is this browser's credential, and only the server can say whose it is.** A
stale note beside it changes nothing about the token's validity — the Worker hashes it and looks it up.

So: **two questions, two guards.** *May I display these answers?* keeps the owner stamp. *May I attach
this credential?* is simply `!!grant`. Conflating them is what let a display-safety rule silently
disable attribution and telemetry.

### The smallest correct fix, in three parts

1. **The reconcile stamps the owner.** A 200 from `/api/grant/whoami` carrying this grant *is* the
   server saying this credential owns this record — so the reconcile is the authority for the stamp.
   Inside the `.then` at `estate/index.html:483`, after `if (!d) return;`, write `K_OWNER = grant`
   **through the existing `put()`**. `put()` flips `changed` when it differs, and `changed` already
   drives `location.reload()` — so the existing mechanism re-renders with `mine` now true. One line, no
   new code path. ⭐ **And it heals all nine sites at once**, because they all read the same key.
2. **Split the two questions** (invariant ②). Sites 8 and 9 stop consulting the owner stamp.
3. **One `grantHeader()`, nine callers.** The function already exists at `:19803` and **one of nine
   sites uses it.** Promote it, give it the split from (2), and make its `null` mean *cannot attribute*
   at every caller — with each caller's choice of fail-closed or explicit-marker written down rather
   than inherited from whoever pasted last.

⚠️ Also ship with it: **the spinner has no terminal state.** `fetching` is set at `:479` and cleared
only by a reload; the three exits that never self-correct are already in the lap-2 handover §3.
*A settled outcome must always re-render, whatever it settled to. A spinner is a state, never an
outcome.*

### The invariant that would have caught the original

> **A guard value must be written by whatever proves the guarded fact, and by nothing else.**

`fw-onboard-owner` has exactly one writer — onboarding — on a path a *returning* device never takes.
The guarded data has a different writer — the reconcile. **When a guard and its data have different
writers, the guard goes stale in the direction that hides correct data**, which is the silent
direction. Same family as `[[Three ways a gate stops being a gate: unwired, unconsumed, un-rederived]]`;
this one is *un-rederived*.

**Executable forms, cheapest first:**
1. **The returning-device walk** (below) — catches the class by behaviour, no new tool.
2. **A grep control for the phrase.** Nine copies of one predicate is exactly the shape
   `entity_map_divergence()` and `check-box-test-agreement.py` already exist to police in this repo —
   *an irreducible copy is AGREED BY A CHECK rather than by hand.* Here the copy is **not** irreducible
   (same file, same scope, a function two hundred lines away), so the answer is the function, and then
   a grep that fails on a tenth hand-rolled copy.
3. **Extend `tools/check-storage-keys.py` with a `writers` column** and fail when a key used in a guard
   expression has no writer in that file's server-reconcile block. The roster records membership, not
   authority. Also catches §C.

### Why four synthetic seats passed this build

**Every seat is a fresh browser walking one journey.** Onboarding writes `fw-grant` and
`fw-onboard-owner` in the same act, so `owner === grant` **by construction, on every seat, every run**.
The defect requires a device with a *history*.

The harness's identity model is *a person is a fresh browser*. The product's is *a credential arriving
on a device that may have carried another*. **The harness cannot see any defect that lives in the gap
between those two models** — and that gap is where the owner guard lives, since the guard exists only
for shared devices.

⭐⭐ **And site 9 is why it will stay invisible even in production.** A stale stamp kills
`grantHeader()`, `flush()` returns early, and **the device stops reporting telemetry entirely.** The
defect suppresses its own instrument. Every affected device looks, in the record, exactly like a device
nobody used. *This is the strongest argument on the page for fixing it by construction rather than
waiting to observe it.*

**What makes the class visible, and it is cheap:** not a fifth persona — a **device-state dimension** on
the seats you have. Give a walk a `--carry <priorGrant>` option: the seat completes onboarding as A,
then the same browser context is handed grant B via `?g=` and must arrive at B's place. One harness
change, one extra stop per round, and it is the **substitution** method lap 2 already credits as its
best-working practice — hold the browser constant, change the credential, and the difference is
attributable.

**Falsifiers for B:**
- on a device holding grant A's owner stamp, present grant B via `?g=`. The card must render B's rows,
  or say it cannot confirm who this is. It must never render zero rows under A's username.
- **on that same device, the viewer must render the household app** — named card, placed coordinates,
  ranking honoured, sync pill reading `household-local` — not the Fernwood reference surface.
- **submit feedback from that device and read the stored record.** It must carry a `personId`, or it
  must not exist. It must never exist without one.

---

## C · Stale identity — `fw-username`, and what else is in its class

### Is this the same bug class as BACKLOG row 14? — **Same rule, opposite side.**

Row 14: `/api/zone-audio`'s `reviewed` has **no writer**, so it reads `false` forever — *a value that
can never become true.*
`fw-username`: it has a writer (this device, at onboarding or sign-in) but **no corrective writer** —
whoami returns no `username` field at all, so nothing can ever contradict the local copy — *a value that
can never stop being true.*

> **A value shown to a person must have a path by which the authority can change it.**
> Row 14 is that rule broken on the write side. `fw-username` is it broken on the read side.

Row 14's own phrasing — *"a container that cannot match its payload"* — covers both, and
`[[reference_match_payload_not_container]]` already carries it. So: **yes, same class**, and I would
record `fw-username` under row 14's rule rather than mint a new one.

### Should whoami return the username?

| | option | cost | verdict |
|---|---|---|---|
| **C1** | **whoami returns `username`** | free *under A2* (the join already reads the account row, which is keyed by it). Without A2 it needs a ninth field copied onto the grant — i.e. one more instance of the seam we are closing | ✅ **recommend, as part of A2** |
| **C2** | drop the username line; identify by place name | cheap; loses the one thing that tells a person *which* account this device holds, which is what she needs at a sign-in door | ✗ |
| **C3** | owner-guard it (`4a3a61b`, on main, unwalked) | necessary, and it stops the *leak* | ✅ **necessary, not sufficient** — a guarded stale value is still stale on your own device |

**Privacy check, stated so it is not assumed:** whoami already returns the caller's address, ranked
priorities, contact preference and personId. A username is strictly less identifying than the address
beside it, and it is the caller's own. **No new disclosure**, and the *"it returns the estate's own facts
and never another person's authored words"* boundary at `:3630` is untouched.

### The hygiene rule this needs, and its one dangerous edge

> **Identity fields are authoritative-or-absent. Place facts are last-known-good.**

On a whoami 200, an identity field the server does not name should be **cleared**. A place fact it does
not name should be **kept**. That is not pedantry — it is the honest reason `put()` skips nulls for
`coordinates` (a provider outage must not un-place a household, `worker.js:884`) while it must *not*
skip for `username`. Applying one rule to both is how you either strand a stale name or un-place a
household, and this lap has produced one of each.

### What else is in the class — client state with no server writer

| key | server authority | rendered to a person | verdict |
|---|---|---|---|
| `fw-username` | ❌ none | ✅ "Signed in as …" | 🔴 **the walked defect** |
| `fw-onboard-owner` | ❌ none | gates **nine** sites across two files | 🔴 **§B** |
| `fw-onboard-contact-chosen` | ❌ none | drives *"The default — change it whenever you like"* | 🟠 a device that never onboarded tells someone their deliberate choice was a default — **wrong in the direction that says her answer did not take**, the one direction this product's copy rules forbid |
| `profileAccent` | ✅ whoami returns it (`:3634`) | ❌ nothing reads it | 🟡 the inverse: an authority with no reader |

**Four instances of one class.** That is the argument for the `check-storage-keys.py` extension rather
than four separate fixes: add an `authority: server | device | none` column, and **any key rendered to a
person with `authority: none` is a finding.**

**Falsifier for C:** rename the account (`worker.js:540`). The door card must show the new username on
its next load, on a device that has not signed in since. And a device with no onboarding history must
not print a username at all.

---

## D · 🔴 Household sync — re-derived against the inventory

### ⚠️ v1 said *"`ObservationStore` sends `X-Tate-Token` and never `X-Grant`."* Half right, and the wrong half was the word choice.

The **file** is mixed. The **store that backs the almanac notes** is not. Full inventory:

| store / caller | credential | grant fallback |
|---|---|---|
| **`ObservationStore.callWorker` `:20482`** — **the almanac notes** | `X-Tate-Token` only | ❌ **none** |
| **`WorkerAPI.call` `:19703`** — Garden Guru, classify, today-line | `X-Tate-Token` only | ❌ **none** |
| `MetricsCollector.flush` / `flushSync` `:19856` `:19882` | either | ✅ via `grantHeader()` |
| mom-queue `sendRecord` `:12934` | either | ✅ inline copy (§B site 8) |
| ask-next feedback `:18211` | grant only | ✅ inline copy (§B site 6) |
| zone-save `:13958` `:13996` | token only | n/a — Paul-only surface |
| `testConnection` `:20617` | token | n/a — the pairing check itself |

**So the §D conclusion stands and the reasoning improves.** The two stores a household actually
touches — **its notes and its Guru** — are the two with no grant path at all. And the pattern they need
is already written, two hundred lines away, in `grantHeader()`. **D1's cost is lower than v1 estimated,
and its shape is "use the function that exists" rather than "invent a fallback."**

### What else is true today, measured

1. **The Worker would already permit the household owner.** The entry gate (`:3670-3676`) dual-accepts
   master **or** a resolved grant; `/api/observations` needs `capability: "administrator"`; a **founding
   owner is an administrator** (`grant-mint.py:374` refuses a founding mint below administrator;
   signup inherits from the invite, `:488`). **The door is open on the server and the client never
   knocks.**
   ⚠️ The comment at `:20469` says *"a member cannot write observations."* True of an invited **member**;
   **not** true of the household **owner**, which is who Paul and Mom each are at their own place.
2. **Storage shape:** one KV blob per estate, `<estate>:observations:all`, whole-array
   read-modify-write. And `loadObservations(env)` takes **`scopeOf(env)`** — the deployment binding, not
   the request scope.
3. **Site premise is binding:** no cell reception, Wi-Fi near the house. **Capture is local-first by
   construction and always will be.** Sync is deferred, never synchronous with the act.

### ⭐ The cost of D0 that is not about multi-device at all

**A new household's field notes have no copy anywhere.** Fernwood's are in KV because Paul's device
holds the master token. For every household that arrives by invite, the notes live in one browser's
`localStorage` — and `fnSaveAll` already carries a quota-failure path because iOS Safari evicts. A
cleared browser, a lost phone, or an eviction loses the record with nothing to restore from.

That is a **durability** finding, not a convenience one, and it is the strongest argument in this
section. *"Notes don't travel between devices yet"* is true and it undersells the risk: they also do not
survive the device.

### The options

| | shape | cost | buys | risk |
|---|---|---|---|---|
| **D0** | keep `household-local` | none | honesty about a limitation, which is real value | ⛔ no backup of any invited household's notes; the s0 promise stays false for notes |
| **D1** | **`ObservationStore.callWorker` falls back to `grantHeader()` + `WORKER_BASE`** when no sync config exists | small — the helper exists; no new endpoint, store or credential | notes durable in KV, present on any device with a live grant; removes the *"set up Sync"* instruction a household cannot follow | last-write-wins on a whole-array put; **and the sequencing dependency below** |
| **D1b** | the same for `WorkerAPI` → **Guru works for a household** | same one-line shape | the Almanac stops being Fernwood-only | ⚠️ **a budget consequence** — Guru is a paid model call and this opens it to every household. Flag to Paul, do not bundle |
| **D2** | per-note keys `<estate>:obs:<id>` + an index | a migration of the array, new merge on both sides | real concurrency safety, small writes, no value-size ceiling | medium; **not what tonight's evidence demands** at ≤2 devices per household |
| **D3** | per-person visibility *within* a household | a policy ruling first, then read filtering | answers "does Bob's wife read Bob's notes" | ⛔ **a ruling, not an engineering choice** |

### 🔴 The sequencing dependency, and it is the load-bearing constraint on D1

`loadObservations` builds its key from **`scopeOf(env)`** — the deployment binding. Correct while one
deployment serves one estate; **silently wrong** the moment it serves two — notes read and written under
the wrong household with no error. `scopeFor(request, env, grant)` exists, and the file's own comment
sequences the conversion: *read-only handlers move first, writers last, because `assertScope` catches a
forgotten conversion and never a wrong one.*

**So D1's honest form is two steps, in this order:** move `handleObservations` onto the request scope
**first**, then let the client present a grant. The other order builds a household's notes into a key
the multi-household flip must migrate — the exact class the C5 6a/6b comments exist to prevent.

### Recommendation — **D1, after the scope move, with four conditions**

1. **Use `grantHeader()`, after §B's split** (invariant ②). Shipping D1 on top of today's guard would
   mean a stale owner stamp silently disables a household's only backup path — the §B blast radius,
   applied to durability.
2. **Local-first is unchanged.** The local write is the save; the push is an attempt. Silence on
   transport failure — the property has no signal away from the house, and *capture must not lie* means
   it must not report failure either.
3. **The copy gets more precise, not less.** After D1 an **owner**'s notes travel and a **member**'s
   still do not — two states, where *"Notes don't travel between devices yet"* covers one. Either the s0
   promise gets scoped in copy, or member write access gets ruled. Content-steward's, then Paul's.
4. **D1b is a separate decision** because it spends money.

**D3 must be ruled before any multi-person household is onboarded.** `CLAUDE.md` §7 already says an
administrator who is not a household member reads that household's notes and that this needs explicit
up-front agreement. Moot at Paul's condo and Mom's condo; not moot at Bob's.

**Falsifier for D1:** save a note as a grant-holding owner on device A; open the app on device B holding
a live grant for the same estate; the note appears with no token pasted anywhere. And: kill the network
at save time — the note must still be readable on device A, with a status line that says local, not
error.

**Falsifier that would prove me wrong:** if two devices in one household routinely write within KV's
propagation window, last-write-wins loses a note and **D1 is worse than D0** — a note that silently
disappears is worse than one that never left the phone. Unlikely at 1–2 people writing minutes apart,
and worth one measured probe (two saves, three seconds apart, two contexts) before shipping.

---

## E · The ask path and the save path share one error surface

**The systems are already correctly separate; the *reader* is not.** `sendTurn`'s catch
(`viewer.html:21356`) is the **ask** path — a model call, where doctrine says AI lives.
`ObservationStore.getStatus()` is the **capture** path, with its own vocabulary (`synced` ·
`local-only` · `household-local` · `local-full` · `error`) and its own surface.

The defect is that the ask-path failure states a **global** condition — *"The Almanac can't reach the
network just now"* — on a screen where a note has just saved successfully and durably. It makes a
**successful capture look failed**, which is *"capture must not lie"* broken from the side nobody guards.

| | option | verdict |
|---|---|---|
| **E1** | **scope each message to the act that failed.** The ask error stays in the conversation turn (it already is — an assistant turn with `isError`) but stops narrating the machine: *"I couldn't get an answer just now"*, not *"can't reach the network"* | ✅ **recommend** — content-steward writes the words |
| **E2** | one unified online/offline model shared by both | ✗ **reject.** It lets an ask-path outage discolour the capture surface — the exact coupling the site premise forbids, since capture must work, and must *report* that it worked, with no network at all |
| **E3** | split the ask-path catch three ways: *not connected* · *couldn't reach* · *reached and couldn't answer* | ✅ **recommend the lite form.** One catch covers no-network, a 429/budget stop, a 5xx and a model timeout. The third matters because *retry immediately* is the wrong advice for it |

> **An error names the act that failed, never the machine. And no ask-path failure may change any
> capture-path status or wording.**

The client-side statement of the doctrine already in `CLAUDE.md` — *AI on the ask path; capture stays
deterministic and AI-free* — extended from where AI may **write** to what a failure may **claim**.

⚠️ **Sequencing note:** under D1b, Guru's `notConfigured` branch stops being reachable for a household,
which changes which of these strings can fire. Do E after D, or do it twice.

**Falsifier / the Playwright flow worth saving:** intercept `**/api/chat` and abort it while leaving
`/api/observations` reachable. Save a note, then ask a question. **The sync pill's text must be
byte-identical to the fully-online run**, and the ask's error must not mention the network as a whole.
Substitution again — one input changed, everything else held.

---

## F · `coordinates` absent on an account that predates geocoding

### ⚠️ Paul's screen had TWO independent causes, and fixing the geocode fixes one

**Cause 1 — the record.** `whoami` carries a retry (`worker.js:3606-3623`): a household with an address
and no coordinates is geocoded on its next load. Two things are wrong with it, and both are §A again:

1. **The trigger reads the grant.** `if (grant.address && !(grant.coordinates && …))`. Paul's grant was
   **born blank** — no address — so the condition was false and **the backfill was silently disabled by
   the missing copy.** The account held the address the whole time. 🟡 `inferred`, and it predicts the
   hydrate has now *armed* it: **one more load of the door should place his household with no profile
   write.** Untested — the cheapest test on this page.
2. **The write goes to the grant.** On `placed`, the branch puts the **grant** row and never the
   account. A *successful* backfill leaves the SSOT unplaced and the next device inherits the emptiness.
   The record gets a fresh cache; the record does not learn.

**Cause 2 — the display, and it is §B site 3.** `adoptHouseholdCoordinates()` (`viewer.html:7312`) is
owner-guarded. **On a stale stamp it returns early and the app paints unplaced even when the coordinates
are correct in localStorage.** So *"the household is still unplaced"* is produced by two independent
mechanisms, and **F alone would not have fixed his screen.** Any test of F must be run on a device whose
owner stamp is current, or it will report a false negative.

**⭐ F is the strongest single argument for A2 that tonight produced** — under a read-time join, whoami
reads the account, sees address-without-coordinates, geocodes, and writes the account. Both ends land on
the record and the bug cannot return by forgetting a copy, because there is no copy.

### The general rule for a field added after accounts exist

| | option | when it is right |
|---|---|---|
| **F1** | **lazy backfill on read** | ✅ **the default.** Costs nothing for records that do not need it, self-heals on use, never touches a record nobody is using |
| **F2** | eager migration tool | when something *other than the person's own next load* needs the field — a batch job, a check, a report — or when you want a countable "all done" |
| **F3** | declare absence, never backfill | when filling it would assert something not evidenced |

**Recommendation: F1 as the standing rule, with a four-part contract declared the day the field ships**,
and F2 only as a **read-only audit**:

> **A field added after records exist declares, on the day it ships:**
> **(1)** which record is authoritative for it;
> **(2)** what triggers its backfill on an existing record — reading the *authoritative* row;
> **(3)** where the backfill writes — the *authoritative* row;
> **(4)** how a reader tells *never had it* from *tried and could not*.

Fernwood has (4) and has it well — three outcomes, `refused:box` never printing as `failed`, null
declared rather than absent. W0 shipped without (2) and (3) being checked against a blank grant, which
is the case that existed in production six hours later.

⭐ **And (4) is the same clause §B invariant ① needs for feedback attribution.** *Never had it* /
*tried and could not* is one rule appearing twice tonight, on coordinates and on `personId`. That is a
promotion candidate, not two findings.

**Do not mint a backfill tool.** `watch-accounts.py` already shouts on *"an arrival carrying an address
with no coordinates"* and `read-geocodes.py` reports placed · refused · failed per estate per env. Wire
the count into those. **One source, N readers.**

**Falsifier for F:** on a device with a **current** owner stamp — (a) load the door once on Paul's
hydrated grant; coordinates must appear with no profile write; (b) then read the **account** row. If the
grant is placed and the account is not, the write end is confirmed wrong and A2 is load-bearing rather
than merely tidier.

---

## Sequencing — what I would do, and why in this order

| # | move | why here | effort |
|---|---|---|---|
| 1 | **B part 1** — the reconcile stamps the owner | 🔴 live in production, silent, self-concealing, and **Mom's invite is unspent**. One line, and it heals all nine sites | low |
| 2 | **B parts 2–3** — split the two questions; one `grantHeader()`, nine callers | 🔴 closes the re-opened attribution bug **before** the lap-3 feedback sweep is built against a population it cannot explain | low–medium |
| 3 | certify `4a3a61b` (the last three unguarded reads + the `isFinite(Number(null))` predicate) | written, on main, unwalked — lap 3's stated easy win | low |
| 4 | **A2 + C1 + F** as **one** change | whoami joining the account closes the seam, gives the username an authority, and points the backfill at the record. **The cohesive answer** — four of six findings, one change | medium |
| 5 | **A2 part 2** — grant set instead of grant rotation | separable, and it carries a security trade Paul should rule rather than inherit | medium |
| 6 | `handleObservations` → request scope, **then** **D1** | durability for invited households; the order is not optional, and it must sit on top of a fixed §B | medium |
| 7 | **E1 + E3-lite**, and **D1b** as its own decision | copy work with a Playwright falsifier; D1b spends money | low |

⚠️ **What I did not do, deliberately:** rank these against zones (F1), the jump-strip ruling (F2), or
anything else competing for lap 3. That is value rank, and the F3 charter finding says plainly it is
Paul's alone. **This is dependency sequence only.**

⭐ On F3's own terms this seam is a clean pipeline test case: item 1 is **production-ready tonight**,
item 4 is **design**, item 6 is **design blocked on a sequencing move**, item 5 is **blocked on a
ruling**. Four items, four stages, one subject — the shape Paul said he wanted a lap to carry.

## Principles this session would propose (⛔ not added — Paul rules)

1. **A guard value must be written by whatever proves the guarded fact.** *(cross-project candidate —
   second sighting of the un-rederived-gate family.)*
2. **Withholding a credential and sending the request are two acts — do one or the other.** An
   unattributable request either is not sent, or carries an explicit marker that attribution was
   unavailable. *(cross-project candidate. Measured tonight: the same guard fails closed at one site
   and open at another, on the same endpoint.)*
3. **Never had it ≠ tried and could not.** Any nullable field a reader will act on must distinguish
   them. *(cross-project — the Worker already states this for `personId` at `:340`; it appeared twice
   more tonight, on `coordinates` and on feedback attribution. Ready for promotion, not invention.)*
4. **Identity fields are authoritative-or-absent; state fields are last-known-good.** *(Fernwood.)*
5. **A field added after records exist declares its authority, its trigger, its write target, and its
   never-had-it/tried-and-failed distinction.** *(cross-project candidate.)*
6. **A test harness that only ever sees fresh state cannot see any defect that lives in prior state.**
   *(Fernwood — generalises to every synthetic-walk harness Paul builds.)*
7. **A predicate copy-pasted past three sites is a function you have not written yet.** Nine copies, two
   divergent failure postures, and the function already existed. *(Fernwood; watch for a cross-project
   second sighting.)*
