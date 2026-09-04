# THE SETUP JOURNEY — invite → account → profile → devices joined · path evaluation

- row: `BACKLOG.md` § grooming batch · *The setup journey* (`PRODUCT-ENGINE.md` § THE SETUP JOURNEY, CAPTURE ONLY)
- objective: O3
- class: engine · declared
- seat: engineering-partner
- mode: path-evaluation
- date: 2026-09-03
- depends-on: `.plans/2026-09-03-c5-record-prep-PLAN.md` (1b · 2b · 2c · 6a) · `.plans/2026-09-03-c6-door-for-paul-PLAN.md` (3a · 3b/3c · 4b)
- parallel-seat: `user-researcher` → `.user-research/2026-09-03-setup-journey.md` (the journeys, the human side of the name, Mom's exception)
- code_context_confidence: high (every claim below re-measured tonight against `worker/worker.js`, `viewer.html`, `tools/`, and the private sibling)
- user_context_confidence: medium (persona + activation research read; the *"does Mom go through setup"* collision is unresolved and is Paul's)

> ## ⛔ EVALUATION ONLY. Nothing built, nothing decided, no file touched but this one.
> Credentials are **settled and out of scope** (privacy seat Q5: the presented credential is an opaque
> minted token for **every** grant including Mom's; device-local unlock is the named successor). C6 4b —
> Paul binding his own device — stays inside C6's build and is not evaluated here.
> Under the FOCUS FREEZE, everything here is **QA-target work**; Paul runs the migration.

**Read:** `OBJECTIVES.md` · `BACKLOG.md` § FOCUS FREEZE, § M3, § C6 · `.plans/2026-09-03-backlog-readiness-PROPOSAL.md`
§1.2–§1.4 · `PRODUCT-ENGINE.md` § THE SETUP JOURNEY, § ACTIVATION, § minimum-is-ZERO, § Mom's-retrofit ·
`~/Developer/fernwood-private/.plans/2026-09-02-data-model-design.md` §2 · §2b · §2c ·
`~/Developer/fernwood-private/.user-research/2026-09-02-activation-journeys.md` §1.3 · §5.1 · §6 ·
`VOCABULARY.md` §2 · §3 · §3b · §4 · `.engineering/2026-09-03-c6-door-for-paul.md` §1 · §6 ·
`.engineering/2026-09-03-c6-privacy-seat-review.md` (Q5, F9, F10, F14, F15) · `CLAUDE.md` § THE SITE'S
PHYSICAL PREMISE · `worker/worker.js` · `worker/wrangler.toml` · `viewer.html` · `tools/momlib.py` ·
`tools/people.json` · `tools/check-public-build.py` · `tools/check-storage-keys.py` · `estate.json` ·
`fernwood-private/grants.json` · `fernwood-private/people-devices.json`.

---

## §0 · WHAT I MEASURED — because the brief's own lesson is that a document asserted something the world does not do

Everything the brief handed me as given, I re-drove against the code. Two things it said are right and I
confirm them; **four things nobody handed me change the shape of this item.**

| # | measurement | where | verdict |
|---|---|---|---|
| 1 | `X-Grant` → sha256 → one KV row `<estate>:grant:<hash>`; row's `estateId` must equal `env.ESTATE_ID`; `revokedAt` also nulls the grant; presented value capped at 256 chars | `worker.js:268–278` | ✅ **as briefed, plus `revokedAt`** — per-row revocation already exists and nothing has claimed it yet |
| 2 | `hostAgrees`: no `Origin` → `true` (agrees vacuously); otherwise hostname ∈ `FAMILY_HOSTS` | `worker.js:283–290` | ✅ as briefed |
| 3 | `/api/grant/whoami` is the one read a grant unlocks; no grant presented → the router's own 404 | `worker.js:2624–2629` | ✅ as briefed |
| 4 | ⭐ **The three ungated capture POSTs short-circuit at `2580 · 2589 · 2600`, BEFORE the grant block at `2607` — but only when `!authOk`.** So an `X-Grant` on a capture POST from an **unpaired** device is never consulted; the identical header from a **paired** device is | `worker.js:2580–2620` | ⚠️ **new, and it decides §3** |
| 5 | ⭐⭐ **`authOk` — the hand-pasted shared token — gates `/api/observations`, `/api/chat`, `/api/conversations`, `/api/zone-feedback`, `/api/zones`, and every GET.** `WorkerAPI.call()` throws `worker-not-configured` without it and the feature *"hides silently"* (its own comment) | `worker.js:2645–2664` · `viewer.html:18294, 18307–18310` | ⚠️ **new, and it is the real size of ④** |
| 6 | `viewer.html` sends `X-Grant` **0 times**; `X-Tate-Token` at **7** call sites | `grep viewer.html` | ✅ confirms privacy F14 |
| 7 | `declarePerson()` is still `Object.assign({}, PERSON_UNKNOWN, record)` — **the record argument still wins**; 6 call sites, none passes `personId` | `worker.js:139–141` | ⚠️ privacy **F9 has not been applied** |
| 8 | `momlib.attribute()` already returns `personSource: "device-inference"` | `momlib.py:1263–1307` | ✅ privacy **F10's read half landed**; the Worker half has not |
| 9 | `momlib.split_arrivals()` splits by ORIGIN into `bench` / `unresolved`, **no `hers` bucket**, fails open | `momlib.py:1355–1383` | ✅ as briefed, and load-bearing for §3 |
| 10 | `DEFAULT_SIZE = "normal"`; `tateTracker.textSize` **is still read** at `viewer.html:21321` | `viewer.html:21304–21324` | ⚠️ **M3 is live.** And the `STORAGE_KEYS` roster comment says the key is *"no longer read"* — **that comment is false today** |
| 11 | `check-public-build.py` scans **six** artifacts (`viewer.html`, `worker/digest.json`, `vehicles.json`, `property.json`, `tools/people.json`, `service-records.manifest.json`) | `check-public-build.py:24` | ⚠️ **new** — `BACKLOG.md`, `MOM-CYCLE-LOG.md`, `.plans/`, `.engineering/`, `instance/fernwood.json`, `feedback-log.json` are **not scanned** |
| 12 | KV kinds actually in use: `observations · feedback · door · zone-audio · zone-feedback · conversation · metrics · cost-log · chat-budget · pending-species · zones · zones-last-seen · ratelimit · cache · grant`. **There is no `person:` kind** | `grep keyFor/dateKey` | ⚠️ **new** — the profile has no runtime home |
| 13 | `VOCABULARY.md` §3 ratifies **person**: *"Never 'user,' never **'account'**"*; §4 rejects **`profile`** as a new noun (*"exactly `person` + their `grants`"*) | `VOCABULARY.md:74, 173` | ⛔ **Paul's own two nouns for this item are already-rejected words.** §1 confronts it |
| 14 | `instance/fernwood.json` is **tracked**, and `build-viewer.py` inlines it into `viewer.html` | `git ls-files` | ⚠️ decides §2 — *"held in her instance's data"* reads as permission for a tracked file |

**Two of these (4 and 5) mean the item is bigger than it looks and simpler than it looks at the same time**:
bigger because *"the syncing issue is kind of manual now"* is not an ergonomics complaint — the manual
paste is what stands between an unbound device and having **no Garden Guru, no field-note sync and no zone
feedback at all**; simpler because almost every record this journey needs already exists.

---

## §1 · THE ACCOUNT RECORD — it is not new, and the word is already ruled against

### The answer, first

> **No new account entity. One new runtime row.** What Paul is calling an *account* already exists as
> four records that were built over the last two days. What is genuinely missing is a **runtime-readable
> profile** — a place a person's own name and reading posture can live where the Worker and her browser
> can reach them, which none of the four are.

### What exists today, measured

| record | what it holds | where it lives | tracked? |
|---|---|---|---|
| **person** | opaque `id` (`p-b91e4d`), a public-safe **handle** (`mom`), engagement flags | `tools/people.json` | ✅ public |
| **grant** (the edge) | `personId` × `estateId`, `relationship` as a SET, `capability` as a value | `~/Developer/fernwood-private/grants.json` | never-public sibling |
| **device → person** | `personId` → `[deviceId…]`, plus an `assumedNotVerified` register | `~/Developer/fernwood-private/people-devices.json` | never-public sibling |
| **the credential** | `<estate>:grant:<sha256(presented)>` → `{personId, estateId, relationship, capability, entry, vault, issuedAt, revokedAt?}` | Cloudflare KV | runtime |
| **estate** | `estateId.id` (coordinate) + `handle` + the module set | `estate.json` | ✅ public |

`tools/people.json` `_meta.personId` already writes the missing piece down as a promise:
*"Under C6 the person supplies their own display name at setup and **it lives in the account record**,
never here."* **That account record does not exist.** There is no `person:` KV kind (§0 #12), and the two
files that could hold it are a git repo on Paul's laptop, not something a browser can read.

### The failure mode this section exists to prevent

> ⛔ **A plan that mints an `account` entity would be adding a fifth name for a thing that already has
> four records and two ratified words.** `VOCABULARY.md` §4 already rejected `profile` for exactly this
> reason — *"a third word for a thing that already has two is how a fork starts"* — and §3 ratifies
> `person` with *"never 'user,' never 'account.'"* Paul used both words naturally in the ask. **That is
> his vocabulary to overrule; it is not something a plan may quietly decide by writing code.** (Q1.)

### Three candidate homes for the profile

| | option | new shapes | cost | reversibility |
|---|---|---|---|---|
| **a** | **fields on the grant row** — `displayName` beside `entry`/`vault` | **zero** | ⛔ the grant row is *credential*-shaped. The moment ④ mints one row per bound device, the name is duplicated N times and drifts. Retrofitting it out later is a migration | high now, falling |
| **b** | ⭐ **a new `<estate>:person:<personId>` KV row** — the profile; grant rows point at it by `personId` and stay credential-shaped and free to multiply | **one KV kind** | one `get` on the reads that need it. Estate-scoped, so it does not port across estates (see the tension below) | **high** — additive; deleting the row loses only the name |
| **c** | a **cross-estate** person store, outside every estate | one store + a new isolation boundary | ⛔ breaks data-model §2 rule 1 (*one database per estate, isolation by construction*) and creates the single artifact that joins **people to places** — which is precisely what C5 8a moved into the never-public sibling. **Reject** | — |

**Recommendation: (b), and mint it at the same time as ④, not before.** The reason is not elegance, it is
the direction of the mistake: (a) is cheaper *today* and becomes a data migration the moment device-join
lands, while (b) is one additive KV kind that costs a single `get` and is deleted by deleting a row. Adding
a row you can drop beats extracting a field out of N rows you cannot.

⚠️ **The tension (b) creates, stated rather than discovered.** Data-model §2c puts a person's own name and
reading posture in **C-person** — *"travels with her — SHOULD port."* An estate-scoped `person:` row does
**not** port: Mom would supply her name again at the condo. Two honest readings, and it is Paul's (Q3):

- **Accept re-entry.** At n=2 estates the port mechanism is *a person* — the administrator, who is the same
  answer this project already gives for recovery (ux F2) and for the new phone (activation §5.1(b)). One
  act, done in conversation, no new store.
- **Build (c) later**, when a third estate makes re-entry expensive enough to pay for a cross-estate
  boundary. ⭐ **Nothing in (b) forecloses (c)** — a later cross-estate store can seed the per-estate rows.

**Recommend accept re-entry.** Building an isolation-breaking store to save one typed word at n=2 is the
over-engineering this seat is told to push back on, and it is easy to add later and hard to remove.

### And a naming consequence that is not cosmetic

`estate` never reaches a user-facing surface (`VOCABULARY.md` §2). `person`, `grant`, `capability` are
schema words. **On the surface, this thing is called nothing** — `content-steward`'s standing verdict, and
`VOCABULARY.md` §3b's *"your homes"* is a greeting, not a container name. So the setup journey has a
**schema** vocabulary (person · grant · estate · module) and a **surface** vocabulary that names places and
people and never the categories they belong to. A plan that writes *"Account settings"* into a heading has
crossed the line without noticing.

---

## §2 · THE SELF-SUPPLIED NAME — where it may live, and what actually enforces it

### The constraint, in its ratified form

> ⛔ **"Her name, in anything tracked"** — `[paul-ratified 2026-09-02]`, activation-journeys §6:
> *"not in `viewer.html`, not a card, not a profile label, not a commit message. A display-name field puts
> it in the UI and in public git by construction."*

And the permission that makes ② possible at all, `VOCABULARY.md` §3b:37 — *"A name a person supplies at
activation and sees rendered back is hers, held in her instance's data and never in the engine."*

⚠️ **Those two sentences do not compose as written, and the seam is a real hazard.** *"Her instance's data"*
reads naturally as `instance/fernwood.json` — which is **tracked, public, and inlined into `viewer.html` by
`build-viewer.py`** (§0 #14). A reader following §3b literally would put her name in a tracked file and
believe the rule permitted it. **Recommend the phrase be tightened to *"the estate's runtime record (KV) or
the person's own device — never a tracked file."*** That is a one-line edit to `VOCABULARY.md`, Paul's or
`content-steward`'s to make, not mine.

### Where the name MAY live

| # | home | job | why it is allowed |
|---|---|---|---|
| 1 | **her own device** (`localStorage`, per origin) | ⭐ **authoritative for render** | never leaves the browser; and it is the only home that survives first paint with no fetch (the M3 lesson: anything fetched arrives after the words have rendered) |
| 2 | **`<estate>:person:<personId>` in KV** | **backup, restored at binding** | Cloudflare, not git. The administrator can already read everything in the estate; this adds no new disclosure |
| 3 | **`~/Developer/fernwood-private/`** | the needle a check greps for; anything a tool must print | `guard-secret-push.py` `NEVER_PUBLIC` — verified `fernwood-private` is on the roster |
| 4 | **`.private/`** in this repo | scratch, transcripts, staged material | gitignored |

### Where it may NOT live — and the list is longer than "viewer.html"

`viewer.html` · `instance/fernwood.json` · `tools/people.json` · `estate.json` · any canon JSON ·
`worker/digest.json` · `RELEASE_NOTES.md` · **`BACKLOG.md`** · **`MOM-CYCLE-LOG.md`** (169 KB, tracked, and
routinely fed by pasted tool output) · `feedback-log.json` dispositions · `.plans/` · `.engineering/` ·
`.ux-reviews/` · `.user-research/` · **commit messages** · **release notes**. 717 tracked files; the rule is
*all of them*, not a list.

### What enforces it — today, nothing deterministic

The only control that has ever caught this is **a person looking**: on 2026-07-26 her self-description was
committed into this public repo and rewritten out of history *pre-push* because someone checked.
`.gitignore` covers `.private/`; `guard-secret-push.py` stops the sibling being pushed; neither of those
looks at content in a tracked file.

**The mechanism that should carry it already exists and needs two changes.** `check-public-build.py` is a
roster of value-classes with a detector, a disposition and an `enforce` flag. A supplied name is not
regex-detectable in general — **but it is detectable as a needle**:

```
row  id: supplied-names        disposition: ruled-private        enforce: True
     needle source: fernwood-private/  (the names, held where names may be held)
     detect: literal, case-insensitive, word-boundary, per name
     scope:  every tracked file (git ls-files), NOT the six SERVED artifacts
     absent sibling: report UNCHECKABLE and exit non-zero — never green
```

**Why the needle shape rather than a heuristic** — a heuristic for "is this a person's name" is a model
read, and a model read is a hypothesis, not a check. A literal needle held privately is deterministic, is
provable by mutation before any real name exists, and is the same shape `momlib._people()` already uses to
merge the private device register.

**Why the sibling-absent case must fail loud** — a check that passes because it could not look is this
repo's own most-repeated failure (`momlib._people()` reads UNMAPPED rather than silently attributing;
`check-live.py`'s drift guard; the 08-08 recorder that broke green for four days).

⚠️ **Two limits, stated so the row does not read as more than it is.** (i) It finds only names it knows —
a third household's contributor is invisible until their name is fed in, so **the act that captures a name
must also register the needle**, or the check degrades exactly where a new estate makes it matter most.
(ii) **It cannot un-publish.** A name that reached a push is public forever; the check's job is to sit
*before* the first capture, not to clean up after.

### Would any existing writer violate it today? — measured: no, and here is the actual leak path

I traced every writer that could carry a record field into a tracked file:

| writer | writes | verdict |
|---|---|---|
| `read-mom-feedback.py --address` | `feedback-log.json` (tracked) | ✅ safe — the `disposition` string is **hand-typed**; the file's own `_meta` says *"Never her words"* |
| `fold-answer.py` | canon JSON + `MOM_ACK_DATA` in `viewer.html` | ✅ safe — a *"Not quite"* correction is **printed** for hand-application (`fold-answer.py:85–86`), never written |
| Worker `promote-species` | canon JSON in the **public repo** via the GitHub Contents API | ⚠️ the one automated public-repo writer, but human-gated by a tap on a drafted suggestion |
| `read-mom-feedback.py --pickup` · `read-mom-funnel.py` · `analyze-fernwood.py` · `read-mom-engagement.py` | stdout | ⚠️ **this is the path** |

> ⭐⭐ **THE FINDING: no automated writer leaks a name. Prose does — and the day a name exists, every
> pickup tool starts printing it into a terminal whose output is routinely pasted into `MOM-CYCLE-LOG.md`.**

**The structural fix, and it is one rule, not a policy:**

> **A supplied name is never returned by a read API and never printed by any tool. It is written once, at
> setup, and read back only by the browser of the person who supplied it.** Attribution everywhere else is
> the opaque `personId` → the public-safe handle in `tools/people.json`.

That makes the leak path *unreachable* rather than *policed*, which is strictly better than a check, and it
costs nothing — because nothing in the loop needs her name. `read-mom-feedback.py` has printed `mom` for
two months and lost no information. (Q6.)

---

## §3 · ATTRIBUTION KEYED TO THE ACCOUNT — the write paths, and the seam

### The five write paths, and what each needs

| route | gated today? | handler | what changes |
|---|---|---|---|
| `POST /api/feedback` | ⛔ **ungated by design** (2026-07-15 loss) | `worker.js:2472` | read `X-Grant` **opportunistically**; never require it |
| `POST /api/zone-audio` | ⛔ ungated by design | `worker.js:1214` | same |
| `POST /api/door` | ⛔ ungated by design | `worker.js:300` | same |
| `POST /api/observations` (field notes) | ✅ behind `authOk` | `ObservationStore.save()` | grant replaces the shared token — **and see the doctrine question below** |
| `/api/conversations` (Guru turns) | ✅ behind `authOk` | `worker.js:1452` | grant replaces the shared token |
| `/api/zone-feedback` | ✅ behind `authOk` | `worker.js:2939` | grant replaces the shared token |

### Four changes, in the order they bind

**1 · `declarePerson()` becomes a guard.** Privacy F9 is **not applied** (§0 #7): the `record` argument
still wins, and `handleFeedback` already spreads `body.context` through verbatim. Three lines:

```
declarePerson(record):        if ("personId" in record) throw — this function declares ABSENCE
attributeTo(record, grant):   the ONLY writer of a non-null personId; takes a RESOLVED GRANT ROW,
                              never a request, never a body
```

⭐ **This must ship before the first non-null person is ever written**, and it ships alone today — no
credential, no surface, no Mom. It is the mechanical route by which *"identity applied backwards with a
stronger-looking warrant"* recurs, and it costs three lines to close while the cost is still three lines.

**2 · `personSource` on the write side.** The read side already emits it (`momlib.attribute()`, §0 #8).
`personId: "p-…" | null` beside `personSource: "grant" | "device-inference" | null`. **`grant` is a claim;
`device-inference` is a guess with a standing disclaimer; `null` is honest silence** — and no count may
ever mix them without saying so.

**3 · ⛔ The router-order defect, and it is not cosmetic.** Measured (§0 #4): a capture POST from an
**unpaired** device returns at `2580/2589/2600` and **never reaches** the grant block at `2607`; the same
request from a **paired** device does. So today *whether a grant is even looked at depends on whether the
device also holds the estate master token* — which is precisely the coupling ④ exists to remove. Wiring
account attribution therefore requires an explicit, ordered decision at those three routes.
Privacy F15 already found that *"the router's security-relevant order is not written down"*; this is the
second instance and the first one that produces a wrong *record* rather than a wrong response.

**4 · ⛔ The rule that must be written before any of it is built:**

> **A grant, when present, UPGRADES attribution. Its absence never blocks capture.**

Two independent doctrines force it. The 2026-07-16 failure — per-device pairing turning her primary device
into a **silent void**, invisible to Paul because a dark device looks like disengagement. And the site's
physical premise — *"in the field, capture must be entirely local, with sync deferred."* A capture path
that requires a credential is a capture path that can lose her words while appearing to succeed.

### What happens to records already written under a `deviceId`

> **Not a migration. Not a mapping. A permanent, declared, four-stratum seam.**

| stratum | the record carries | how a person is reached | may it change? |
|---|---|---|---|
| before C5 1a (pre-2026-09-03) | **no** `personId` field at all | read-side `momlib.attribute()` → `personSource: "device-inference"`, and only on/after `fullyValidFrom` **2026-07-28** | ⛔ **never** |
| C5 1a → account exists | `personId: null` — **declared**, not absent | same | ⛔ **never** |
| after the account, grant presented | `personId: "p-…"`, `personSource: "grant"` | the record itself | — |
| after the account, no grant (unbound device, offline flush) | `personId: null` | read-side inference | ⛔ **never backfilled** |

⛔ **NO BACKFILL, EVER — and it is the one irreversible act in this entire item.** Activation research
§1.3 and `PRODUCT-ENGINE.md` § minimum both say it: *"the day identity exists, someone will retro-attribute
the archive… or the 2026-08-01 retraction recurs with a stronger-looking warrant."* The plan should carry
it as a **falsifier**, not a paragraph:

> *Any record whose timestamp precedes its grant's `issuedAt` and carries a non-null `personId` is a
> failure.* Measured by a scan, not by intent.

**And the seam has to be READABLE, or it will be read wrong.** Any tool that says *"she made 40 inputs"*
across the strata is minting a stronger claim than the record supports. **Recommendation: one function in
`momlib` returns the split (grant-backed · device-inferred · unattributable), and every consumer reads it.**
One source, N readers — the same discipline that keeps the weather completeness check from growing a second
threshold.

### ⛔ And what must NOT be built — the `hers` bucket

`momlib.split_arrivals()` splits by ORIGIN into `bench` and `unresolved`, **deliberately with no `hers`**,
and fails open (§0 #9). A grant-backed `personId` is a *stronger* claim than a device inference, and it
**will** be read as licence to add the third bucket. It is not, for two reasons:

1. **A grant proves which credential was presented, not which human held the phone.** It is the browser-
   bucket problem one layer up, and it re-opens the moment two people share a device — which
   `tools/people.json` records as having happened until 2026-07-28.
2. **The mom-loop's firing rule keys on `unresolved`.** A `hers` bucket would make the loop fire on
   *identity* rather than on *unread input*, and the whole point of the two-bucket split is that the board
   stays lit on anything nobody has looked at.

> **A grant changes `personSource`. It never changes the bucket set.**

---

## §4 · DEVICE JOIN — replacing the hand-pasted `sync.v1` token

### What the token actually is, and why this is not ergonomics

`tateTracker.sync.v1` = `{workerUrl, token}` where `token` is the **estate-wide `SHARED_TOKEN`** — one
value, every device, every person, full read of everyone's notes, recordings and conversations. It is
simultaneously **(a)** the device-join mechanism and **(b)** the estate master key, and it is transferred
by a human pasting a secret into a text field.

**And §0 #5 is the part nobody has written down.** On a new phone, before Paul pastes it, Mom has:

| surface | on an unbound device |
|---|---|
| the glance — weather, plants, wildlife, the whole dashboard | ✅ works (inlined data + ungated `/api/ambient`) |
| Mama's Perspective confirm answers | ✅ works (ungated POST) |
| zone voice recordings | ✅ works (ungated POST) |
| **field notes (the Almanac)** | ⚠️ saved **local-only**, honestly labelled, pushed on the first sync after binding — but they never leave that phone until someone binds it |
| **Garden Guru** | ⛔ **absent, silently** — `WorkerAPI` throws `worker-not-configured` and *"the feature hides"* |
| **zone feedback** | ⛔ absent |
| her text size | ⛔ resets to `normal` — **M3, still live tonight** (§0 #10) |

> ⭐⭐ **M3 is the same wound at a smaller radius. The words get smaller AND the Almanac stops following
> her AND Garden Guru is simply not there — and every one of those failures is silent.** Lap 8 measured
> **4 Guru turns and 4 saved notes** from her in one window against **zero** taps on anything that asks
> her a question. The channels she actually opens are exactly the ones a new phone takes away.

### Physical-premise test, applied first

`CLAUDE.md` § THE SITE'S PHYSICAL PREMISE: no cell reception, Wi-Fi from the house only, coverage falls off
with distance, heavy canopy, **permanent**. Two consequences that eliminate options before they are costed:

1. **Binding is a network act, so binding happens at the house.** Any design whose join step could be
   needed in the field is disqualified. ✅ All four options below bind at the house.
2. ⛔ **Capture may never depend on the join having happened.** ✅ The precedent already exists and works:
   `feedbackOutbox` (durable, held until a 2xx), the zone-audio outbox, and `ObservationStore`'s local-only
   mode that pushes accumulated entries on the first successful sync. **The device-join does not build the
   deferred-sync half — it makes the half that already exists reachable.**

### The options

| | option | what it costs | what it buys | fails where |
|---|---|---|---|---|
| **a** | **Administrator binds in person** — today's act, formalized and written down as a journey | **zero code** | honest at n=1–3; it is activation §5.1(b)'s own remedy (*"a new-phone journey is a person, exactly like recovery"*) | ⛔ **J4.** Paul touching Bob's contributor's phone is the *unconsented act* the cross-journey finding names — he holds **capability** there and **no relationship** |
| **b** | ⭐ **A minted, single-use claim code** — `<estate>:invite:<sha256(code)>` → `{personId, estateId, relationship, capability}`. The device posts the code once to `POST /api/invite/claim`, receives a minted grant token, stores it, and presents `X-Grant` thereafter | one KV kind · one route · one small field on the surface · **the client change to send `X-Grant` at 7 call sites** (privacy F14) | **①, ③ and ④ in one mechanism.** Retires the master token from every non-administrator device. **Per-device revocation is free** — `grantFor` already honours `revokedAt` (§0 #1). Works for J4 without anyone touching anyone's phone | needs a delivery channel — and there is none: ⛔ no email, ⛔ no phone. **The delivery channel is a conversation**, which is consistent with *recovery is a person* but must be stated, not discovered |
| **c** | **QR / short code displayed on an already-bound device** | (b) plus a rendering surface | better ergonomics | ⛔ requires the old device to still work — which fails **exactly the case that motivates this** (lost, broken, replaced phone) |
| **d** | **Passkeys / WebAuthn** | large: a new credential model, platform-dependent sync, a user-verification prompt at bind | genuine cross-device sync inside one Apple household | ⛔ **it is a login ceremony, and Mom must never meet one** (activation §J2: *"if she can tell anything happened, the retrofit was designed wrong"*). Named here so it is not re-proposed as the obvious modern answer |

### Recommendation — **(b), with (a) as the delivery channel**

> ⭐ **One mechanism, two hands.** The claim code is *claimed* on the device either by **Paul, holding her
> phone** (Mom's retrofit — she sees nothing) or by **the person themselves, from a code Paul read them
> aloud** (Bob's contributor — nobody touches anyone's phone).

That is the cleanest resolution I can find to the cross-journey finding, which is otherwise a real problem:
*the shortcut that makes ② kind is the exact act ④ forbids.* Under (b) the two journeys are **the same
code path** and differ only in whose finger. Under (a) they are different acts, and one of them cannot be
performed at instance 2.

**Four disciplines the claim code inherits, none negotiable:**

1. ⛔ **No TTL, no clock.** C6's own falsifier is *"trust is revoked by a clock — a `Date` comparison
   inside `grantFor`, or a TTL on a `grant:` key."* **Single-use is a state change, not a clock**, so it is
   compatible: the invite row is deleted on claim. An unclaimed invite sits there until someone revokes it.
2. **The minted grant is opaque** — privacy Q5, settled. The claim code is likewise minted, not chosen.
   It is short enough to read aloud only if Paul accepts the entropy trade, and **privacy F11's rate limit
   is the stated precondition on any low-entropy value** (nothing rate-limits a credential attempt today;
   the only two buckets sit on ungated POSTs). If the code is short, the bucket is not optional.
3. **One grant row per bound device**, all pointing at one `personId`. That is why §1 recommends (b)'s
   separate `person:` row — the name must not live on a record that multiplies.
4. **`hostAgrees` is a routing check, not access control** (privacy F4). The grant row's `estateId` is what
   isolates estates, and nothing else. The claim route inherits that and adds nothing.

### ⛔ The prerequisite nobody has named, and it may be the whole finding

Even with (b) shipped perfectly, **a device that has not joined still has no Garden Guru and no field-note
sync**, because those sit behind `authOk`. So *"streamline the syncing"* has a defect underneath it:

- **`POST /api/observations` and `POST /api/zone-feedback` can adopt the write-only-no-token doctrine** —
  write-only, GET stays gated, exactly as `/api/feedback` did after the 2026-07-15 loss. Then her field
  notes reach the record from any device she ever opens, joined or not, and the join makes them
  *readable back*, not *savable*.
- ⛔ **`/api/chat` cannot.** An ungated model call is an unmetered bill, and the QA Worker already carries a
  `CHAT_DAILY_BUDGET_USD` ceiling precisely because that is real. **Guru genuinely needs the join** — which
  is the strongest single argument for building ④ at all, and the honest answer to *"why not just leave the
  token paste alone."* (Q7.)

---

## §5 · DEPENDENCY AND SEQUENCING

### What must land first

| # | prerequisite | state |
|---|---|---|
| P1 | C5 1a/1b/2b/2c/6a — `personId: null` declared at the write sites; the resolver; the opaque ids; the grant register; estate-prefixed keys | ✅ **shipped** |
| P2 | C6 3b/3c — the grant check in the router, `/api/grant/whoami` | ✅ **shipped to QA tonight** |
| P3 | C6 3a — grant rows actually **minted** into KV from `grants.json` (`entry`, `vault`, `credential.hash`) | ⏳ Paul's stamp; fixtures on QA |
| P4 | C6 4b — the client presents `X-Grant` on Paul's own device | ⏳ **inside C6's build, not this item** |
| P5 | C4's QA origin + QA Worker as the build target | ✅ shipped; the FOCUS FREEZE makes it the only target |
| P6 | ⭐ **M3-a** — the served default for a new device | ⛔ **NOT shipped** — `DEFAULT_SIZE = "normal"` measured tonight. A device-join journey that ends with her words smaller has made the new-phone experience *worse*, not better |
| P7 | Paul's rulings — Q1 (the word) · Q2 (where the name lives) · Q3 (does it port) · Q5 (the join mechanism) · Q8 (does Mom go through setup) | ⏳ |

### ⭐ What ships INDEPENDENTLY of everything — no credential, no name, no Mom, no ruling

The last batch found these were the most useful output, so they are named explicitly and ranked by value.

| # | step | why it stands alone | effort |
|---|---|---|---|
| **I1** | ⭐⭐ **`declarePerson()` becomes a guard; `attributeTo(record, grant)` is the only non-null writer** | privacy F9, still unapplied. Three lines. **Must precede the first non-null person**, so its window is *now* and it closes forever once one is written | low |
| **I2** | ⭐ **The `supplied-names` needle row in `check-public-build.py`, with the scan widened past the six SERVED artifacts, and UNCHECKABLE-when-the-sibling-is-absent** | provable by mutation **before any real name exists**; and the widened scope fixes a live gap for the breaker-directory and phone rows too | medium |
| **I3** | **`personSource` written by the Worker** (the read half already exists) | additive field, no reader required | low |
| **I4** | **The stratum-split reader in `momlib`** — grant-backed · inferred · unattributable | read-only, pure, testable offline | low |
| **I5** | ⭐ **`POST /api/observations` + `POST /api/zone-feedback` adopt the write-only-no-token doctrine** | a defect fix with its own justification (an unbound device's notes never leave the phone). Independent of identity entirely | medium |
| **I6** | **Fix the false `STORAGE_KEYS` comment** — it says `textSize` is *"no longer read"*; `viewer.html:21321` reads it | one comment; the exact *document-asserts-what-the-world-does-not-do* shape this batch keeps finding | trivial |
| **I7** | **Write the router's security-relevant order down** (privacy F15, second instance — §0 #4 is a *record* consequence, not just a response one) | a comment block + a grep-able assertion | low |

**I1 and I2 are the two that have a closing window.** I1's cost rises the instant a non-null person is
written; I2's cost rises the instant a name is captured, and after a push it is not a cost, it is a
permanent publication.

---

## §6 · COST, REVERSIBILITY, AND THE IRREVERSIBLE STEPS

### Calibration

A family app, **one vulnerable user**, ~2 people, **no motivated adversary**. Two things raise the floor
and neither raises it to enterprise: the **private tier is real** (receipts, contractor numbers, the
breaker directory), and a **third household is one item away** — which converts "Paul can see everything"
from a family arrangement into someone else's household, with a consent gate already ratified.

### Cost

Small, and the code is not the expensive part.

- **2 new KV kinds** (`person:`, `invite:`), **2 new routes** (`POST /api/invite/claim`; widening
  `/api/grant/whoami` to return the profile), **1 client change** at 7 `X-Grant` call sites, **1 small
  surface** (a code field, which Mom never sees).
- **No new dependency, no build step, no framework.** Everything sits inside the existing Worker + inlined-
  viewer stack.
- The real cost is **five rulings** and the **discipline** of not backfilling.

### Reversibility

| step | reversible? | how |
|---|---|---|
| I1 · `declarePerson` guard, `attributeTo` | ✅ high | pure code; revert |
| I2 · the needle row | ✅ high | a roster row; `enforce: False` softens it |
| I3 · `personSource` | ✅ high | additive field |
| I5 · ungating two write paths | ⚠️ medium | reversible in code, but **once an unbound device has written, those records exist** — which is the intended outcome |
| §1 (b) · `person:` KV row | ✅ high | delete the row; the name is lost, nothing else is |
| §4 (b) · invite/claim + per-device grants | ✅ high | revoke rows (`revokedAt` already honoured); the master token still works until it is rotated |

### ⛔ The irreversible steps, marked

1. ⛔⛔ **Backfilling `personId` onto pre-account records.** The only truly irreversible act in the item,
   and the recommendation is **never do it**. It is irreversible in the way that matters — not because the
   bytes cannot be changed back, but because every downstream count, chronicle and design decision taken
   over an attributed archive inherits a claim the record cannot support, and the 2026-08-01 retraction is
   what that looks like from the other side.
2. ⛔ **The first supplied name reaching a tracked file, followed by a push.** Reversible in KV; reversible
   in an unpushed commit; **irreversible after a push, because this repo is public and a push is
   publication.** ⭐ **This is the one place in the item where "reversible" is false in the direction that
   matters — which is why I2 must exist before the first name is captured, not after.**
3. ⚠️ **Rotating `SHARED_TOKEN`.** Reversible per device (re-paste), but the *rotation event* is not: every
   device that has not joined loses Guru and field-note sync simultaneously, and the 08-08 Ambient rotation
   is the worked example of a correct rotation that broke a consumer nobody had migrated, silently, for
   four days. **Sequence: join every device first, verify from `/api/metrics` that no device is presenting
   the old token, and only then rotate** — the same discipline as C4 4c's *seven days of zero traffic
   before deleting the old Worker script*.

### Severity, in this project's terms

Nothing here is `critical` as a *security* matter — there is no motivated adversary and the presented
credential is 256 bits. The two findings I would call `critical` **at these stakes** are both about the
record telling Paul something untrue: **I1** (the route by which retro-attribution recurs with a
stronger-looking warrant) and **the `hers` bucket** (a wrong claim about a person, on the surface this
project exists to protect). The name rule is `critical` for a different reason again — not risk, but
**irreversibility**.

---

## §7 · QUESTIONS FOR PAUL

```
Q1 · framing · Your ask names an "account" and a "profile." VOCABULARY.md §3 ratifies `person` with
     "never 'user,' never 'account'", and §4 rejects `profile` as a new noun ("exactly `person` +
     their `grants`"). Which gives?
   options: keep the ratified words (person · grant · estate) and treat "account" as your shorthand
          | overrule §3/§4 and ratify "account" as a real word with a real record
          | keep the ratified words in schema, and let the surface call it nothing (content-steward's
            standing verdict) — the two vocabularies stay separate on purpose
   recommend: the third — schema stays `person` + `grant`, the surface names people and places and
        never the category, because §4's own reason is that a third word for a two-word thing is how a
        fork starts, and this is the moment the fork would start
   caveat: this is your vocabulary; a plan may not settle it by writing code that picks a word.
   blocks: nothing today — I1–I7 all ship under either answer. It blocks the first line of schema
        that has to be named.

Q2 · assent · Where does a self-supplied name live? (§1)
   options: a) fields on the grant row (zero new shapes, duplicates once devices multiply)
          | b) a new `<estate>:person:<personId>` KV row, grants point at it by personId
          | c) a cross-estate person store outside every estate
   recommend: (b) — one additive KV kind, deleted by deleting a row, and it does not become a data
        migration the day one grant row per device exists. (c) breaks "one database per estate,
        isolation by construction" and rebuilds the people↔places map C5 8a just moved to the sibling.
   caveat: (b) is the cheap answer only if you also accept Q3's cost.
   blocks: the `person:` row's shape — nothing ships on it before ④.

Q3 · assent · Does the name (and her reading posture) PORT to her condo? Data-model §2c says C-person
     "travels with her — SHOULD port"; an estate-scoped row means she supplies it again.
   options: accept re-entry — the port mechanism is a person, the same answer already given for
            recovery and for the new phone
          | build the cross-estate store now so it ports by construction
          | defer and decide when a third estate exists
   recommend: accept re-entry — at n=2 estates, building an isolation-breaking store to save one typed
        word is the over-engineering that is easy to add later and hard to remove, and nothing in (b)
        forecloses it
   caveat: it does contradict §2c as written, so §2c should gain a line rather than be silently broken.
   blocks: nothing. §2c stands as written until you rule, and no code depends on it yet.

Q4 · assent · Ratify NO BACKFILL as a checked falsifier, not a paragraph: "any record whose timestamp
     precedes its grant's issuedAt and carries a non-null personId is a failure."
   options: ratify as a falsifier with a scan | keep it as doctrine in prose | rule that some window
            may be backfilled
   recommend: ratify with the scan — this is the one irreversible act in the item, and PRODUCT-ENGINE
        already warns that "someone will retro-attribute the archive" on the day identity exists. A
        prose rule has already been the control here and the 2026-08-01 retraction is what it cost.
   caveat: none.
   blocks: the plan's `## Falsifier` section. Until you rule, the standing rule is the activation
        research's — pre-identity records stay unattributed permanently.

Q5 · assent · The device-join mechanism (§4).
   options: a) administrator binds in person, formalized and written down (zero code)
          | b) a minted single-use claim code → `POST /api/invite/claim` → a per-device grant token
          | c) QR from an already-bound device
          | d) passkeys / WebAuthn
   recommend: (b), with (a) as the delivery channel — "one mechanism, two hands." It is the only option
        where Mom's retrofit and a contributor at Bob's house are the SAME code path, differing only in
        whose finger claims the code; (a) alone cannot be performed at instance 2 without the
        unconsented act the cross-journey finding names; (c) fails the broken-phone case that motivates
        the item; (d) is a login ceremony she must never meet.
   caveat: there is no delivery channel — no email, no phone, both ruled to have no job — so the code
        travels by conversation. That is consistent with "recovery is a person," but it should be
        designed as the channel, not discovered as a gap.
   blocks: the shape of ④. Until you rule, `sync.v1` stands and I1–I7 are unaffected.

Q6 · assent · Is a supplied name ever returned by a read API or printed by a pickup tool? (§2)
   options: never — write-once, read back only by its owner's browser
          | yes, to Paul's tools, because a name reads better than a handle in a report
   recommend: never. It makes the leak path structurally unreachable instead of policed, and it costs
        nothing measurable — `read-mom-feedback.py` has printed the handle `mom` for two months and no
        reading has been worse for it. The realistic leak is pasted tool output landing in
        MOM-CYCLE-LOG.md, which is tracked and public.
   caveat: none.
   blocks: nothing. It blocks the first read route that would return a profile.

Q7 · assent · Do `POST /api/observations` (field notes) and `POST /api/zone-feedback` adopt the
     write-only-no-token doctrine, so an unjoined device is not silently half-dead? (§4)
   options: yes, both — write-only, GET stays gated, exactly as /api/feedback did after 2026-07-15
          | no, they wait for the device-join
          | yes, but only field notes
   recommend: yes, both. Measured tonight: on an unbound device her Almanac notes never leave the
        phone and Garden Guru is silently absent. Field notes and zone feedback are cheap writes with
        no cost exposure. ⛔ `/api/chat` CANNOT join them — an ungated model call is an unmetered bill,
        which is exactly why the device-join has to exist at all.
   caveat: this raises the abuse ceiling on two more routes; the existing rate-limit shape covers it,
        and privacy F12 already established the ceiling is denial-of-capture, not graffiti.
   blocks: nothing — it is I5, and it ships alone.

Q8 · assent · Does Mom go through the setup phase, or is her retrofit the exception?
   options: she goes through it — she types her own name, per your own words ("allow people to set
            their own name")
          | her retrofit stays "no visible change" and Paul supplies everything on her device
          | she goes through a two-minute version of it, in person, with Paul beside her
   no-recommendation: this is yours, and the brief says so. Both readings are internally consistent and
        each is supported by something you ruled: the setup ask is your own words from today; "if she
        can tell anything happened, the retrofit was designed wrong" is the user-researcher's falsifier
        from yesterday. An engineering seat picking between them would be settling a product question
        by choosing a code path.
   caveat: ⭐ under Q5's recommended mechanism you do NOT have to choose in order to build — the claim
        code is the same code path either way, and the only difference is whose hand claims it. Rule it
        when the surface is designed, not when the plumbing is.
   blocks: the setup SURFACE. It blocks nothing in §1–§4's plumbing.
```

---

## §8 · OVERLAPS — cited, and left where they belong

- **`user-researcher` → `.user-research/2026-09-03-setup-journey.md`** owns: the four journeys through
  setup, what a person is actually asked and in what order, the human side of the name (whether being
  asked for it is welcome or a demand), and Mom's exception. **I have stated only where a name may live
  and what may print it — not whether asking for one is kind.**
- **`content-steward`** owns: what the setup surface says, and the standing verdict that the shell is
  called nothing to a reader (`VOCABULARY.md` §3b). Q1's third option depends on that verdict holding.
- **`ux-expert`** owns: `.ux-reviews/2026-09-02-login-door-and-selector.md` F1a — *the glance renders to
  completion with zero authorization round-trips* — which is the constraint that kills any design where a
  profile fetch precedes first paint. §1 (b) and §2's *"device is authoritative for render"* are both built
  to satisfy it; **verifying they do is that seat's, not mine.**
- **The privacy seat** owns F9, F11, F14 and F15, all of which this item inherits. **F9 is unapplied and is
  I1** — I have flagged it rather than treated it as done.
- **Paul's, not any seat's:** Q1, Q3, Q5 and Q8, and the *does Mom go through setup* collision recorded in
  `PRODUCT-ENGINE.md` § THE SETUP JOURNEY.

## §9 · FALSIFIERS FOR THIS EVALUATION

1. **The account really is new.** If a reader can name a field the setup journey needs that is not already
   carried by `person` × `grant` × `people-devices` × `estate` + one profile row, §1's central claim is
   wrong and the item is bigger than described.
2. **A grant is present at capture time more often than not.** §3's *"upgrades, never blocks"* rule assumes
   the ungated capture paths matter. If, after ④, every real capture carries a grant, the opportunistic
   read is dead weight — measured as: `personId: null` on fewer than 1 in 50 new feedback records.
3. **The name never needs to be printed.** If the first month of use produces a report Paul cannot read
   without the name, Q6's recommendation is wrong and the needle check becomes the primary control rather
   than the backstop.
4. **The claim code is not one mechanism.** If Mom's retrofit and Bob's contributor end up needing
   different routes, §4's "one mechanism, two hands" has failed and (a)+(b) are two designs, not one.
5. **This evaluation was ceremony** (readiness §5). Measured in the eventual plan's `## Retro`: steps that
   exist only because this seat measured something. My candidates are **I1** (F9 unapplied), **I5** (the
   three-of-five gated channels), **§3's router-order defect**, and **§2's "never printed" rule** — if none
   of those changes the build, this seat's contribution was restatement.
