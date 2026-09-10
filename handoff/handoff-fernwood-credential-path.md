# Handoff: the credential / account path — lane `tate-tracker-ec`

<!-- generated 2026-09-10 ~5:30 PM ET · Tate-Tracker@15b4f9a · RECEIVER: verify shas vs HEAD before trusting any status here -->

**The target the next session is driving at** `[paul-stated 2026-09-10]`: *"QA deploy with
synthetics walking in and then walking. It is a big test, and that's where I want to go before
we start onboarding folks more and sending them out links."*

Everything below is framed against that.

## 0. ⭐ THE ONE MEASUREMENT THAT MOST CHANGES YOUR PLAN

**The founding path exists at `qa` and `lab` ONLY.** Measured just now, `POST /api/estate` with
no credential:

| env | worker | `/api/estate` | reading |
|---|---|---|---|
| **qa** | `fernwood-qa` | **404** | ✅ new code — the route exists and refuses a caller with no credential |
| **lab** | `fernwood-lab` | **404** | ✅ new code |
| home | `fernwood-home` | 401 | ⛔ **OLD CODE** — route absent, outer auth gate answers first |
| bob | `myhome-bob` | 401 | ⛔ OLD CODE |
| paul | `myhome-paul` | 401 | ⛔ OLD CODE |
| legacy | `fernwood` | 401 | ⛔ OLD CODE — **deliberately frozen, leave it** |

⭐ **Good news for the target: QA already has the code the test needs.** A synthetic can found an
estate at qa today.
⛔ **But nothing I did today is live at `home`, `bob` or `paul`.** If you read a plan saying "the
founding path ships", it ships *at qa and lab*. **Do not infer deployment from a commit.**
⚠️ `home` is Mom's; deploying it needs Paul's explicit word AND gate ① (`release-gate.py`).

## 1. What landed today (this lane)

- **`grantFor()` is a ROUTER.** `route:<sha256(token)>` → `{estateId, personId}` → then
  `<estateId>:grant:<hash>`, verifying the row's own `estateId` agrees. **A dangling route is a
  404, never a fall-back to the deployment's estate.** A legacy fall-back path remains for
  credentials minted before the router (see §3.1 — it is load-bearing, do not delete it casually).
- **`personFor()`** — identity, deliberately NOT a mode of `grantFor`. Authority and identity are
  two lookups on purpose.
- **`canonFor(env, scope)`** — per-request canon, replacing `canonIsThisEstate(env)`.
  **`CANON_FOREIGN_OK` was DELETED**; do not reintroduce it (it would feed Fernwood's canon into
  someone else's estate).
- **`POST /api/estate`** (`handleEstateFound`) — founding. Writes place → grant → route, in that
  order. Refusals: 404 no credential · 501 unknown verb · 409 already has an estate.
- **Cross-estate invite escalation fixed** — an invite minted at estate A conferred capability at
  estate B. Proven live BEFORE the fix, then proven fixed.
- **`nigel` / `aida` destroyed** (`4f7c04f`) — Workers, KV namespaces, env blocks, instance files.
  Verified empty at `wrangler exit=0` with a literal `[]` first. **`est-76012d` and `est-92e588`
  are RETIRED, NEVER REUSED.**
- **Canon ingestion PROPOSAL** (`d6c2f37`) — Paul's question answered as text. Not ruled.

## 2. ⛔ PARKED — do NOT start these half-way

### M1 + M2 — ONE commit, NOT STARTED, nothing written
Two writes are missing from `POST /api/estate` and the commit body of `6414435` names them:
1. **`grant:<personId>:<estateId>`** — the edge that would enable `grantsFor(personId)`. The ruled
   table says it "ships with `POST /api/estate`". It does not. **This is my omission, not a
   design gap.**
2. **The route value should carry `{personId}` alone.** It still carries `estateId` too, which is
   a second writer of a fact `<estateId>:grant:<hash>` already holds.

⭐ **Why they are ONE commit:** dropping `estateId` from the route value breaks `grantFor`'s
router read unless the grant edge exists to replace it. **Landing either alone leaves the
credential path in a state that resolves differently depending on which rows are old.** That is
the single worst thing to hand a successor, which is why it is parked unstarted rather than
half-done.

### The founding digest composer — NOT STARTED
Compose the digest inline at founding. ⚠️ **It creates TWO WRITERS OF ONE FACT** — the Worker
inline, and `tools/publish-digest.py` locally. They must produce **byte-identical** output, and
the drift-lint must compare **FIELD BY FIELD**, not by fingerprint: a fingerprint tells you
*that* they diverged and never *where*. `publish-digest.py` already has `fingerprint()` and
`body_of()` (which correctly excludes `rebuiltAt` — a timestamp is not drift).

### `via:` on the remaining write paths — NOT STARTED
`stampVia()` covers 3 of 6 authored write paths. `conversation` and `observations` need signature
changes. **`door` is correctly EXCLUDED** — a door record carries `personId:null` by
construction, and that is Paul's ruling working, not a gap to close.

## 3. ⭐⭐ BLIND SPOTS — what I know that a fresh session will not

### 3.1 The legacy fall-back in `grantFor()` is load-bearing and looks like dead code
`grantFor()` tries the router first, then falls back to the pre-router lookup. **Every credential
minted before the 2026-09-10 backfill depends on that fall-back.** It reads like a leftover.
⛔ Deleting it kills live credentials, including Mom's and Bob's. It comes out only after a
backfill that is *proven* to cover every grant — and the backfill iterates the STORE, so a
register-only row (`p-paul @ est-e6696a` is exactly that shape) is **silently uncovered**.

### 3.2 `/api/profile` writes to the ACCOUNT; `whoami` reads the GRANT
**This is the likeliest cause of the 🔴 `USERNAME renders empty on a credential whose door says
it has one`** found in the `handover` walk. They are two records of one fact and nobody made them
agree. I did not verify it — it is a hypothesis with an obvious probe: set a username via
`/api/profile`, then read `whoami` for the same credential.

### 3.3 My own falsifier cannot see the class it is trusted for
`tools/falsifier-tenancy.py` — **every clause is estate-A-vs-estate-B.** C3 ("B is B's own row")
reads like a person test and is **not**; it is an estate test wearing a person's name. So
**nothing in this project can see WITHIN-ESTATE, CROSS-PERSON isolation**, and the security lane
reports all three of today's 🔴s were exactly that class.
⛔ **It becomes structurally guaranteed the moment a household has two people** — which is what
invites create. **Close it before the invite feature lands, or it never gets closed.**
⭐ This is CLAUDE.md's own *"a control can be entirely correct and still not cover the thing you
rely on it for"* — applied to a file I wrote, by its author, which is the hardest case to see.

### 3.4 An estate with no `<estate>:place` row gets NO digest, by design
`publish-digest.py`'s canon **election** was removed in favour of reading `<estate>:place`
directly. The election was a real defect — it picked whichever member had an address, and at
`est-qa0001` it chose a real person's home, so QA's Guru answered *"clear skies over Mead
Street."* ⛔ **Do not restore an election to "fix" a missing digest.** The absent place row is the
thing to fix.

### 3.5 `derive-property.py` REFUSES to write anywhere git tracks
It checks `git ls-files`, because this repo is **public** and a household's address must never
reach it. That refusal is the feature. Its selftest probes a tracked path expecting `SystemExit`
— I repointed that probe at `instance/fernwood.json` today when I deleted `instance/nigel.json`.

### 3.6 `wrangler kv` defaults to the LOCAL simulator
**Always pass `--remote`.** A bare `kv key list` returns `[]` for a populated namespace and reads
as "empty estate". ⚠️ And `kv key list` is **eventually consistent** — a write you just made may
not appear. Do not conclude absence from one listing.

### 3.7 `est-qa0001` holds Paul's REAL accounts mixed in with fixtures
201 account rows, 174 carrying a place under 5 distinct place names. **Any teardown keyed on the
estate deletes his.** `household-fixtures.py --teardown` correctly refuses by default.

## 4. ⚠️ WHAT I TRIED THAT DIDN'T WORK — the half a successor pays full price to rediscover

1. **A patch whose replacement string CONTAINED the string it replaced.** The second substitution
   matched *inside* the first, leaving a duplicate write referencing `acct.personId` in a scope
   where it does not exist — **a runtime ReferenceError that parses fine.** Caught only by reading
   the file afterward. The coordinator made the identical mistake the same day. **Read the file
   after every patch; never trust a reported success.**
2. **Editing `people.json` by string replacement with an escaped quote.** Produced invalid JSON.
   Build the replacement through `json.dumps()` and strip the outer quotes, or use typographic
   quotes. **Always re-parse the file in the same command.**
3. **Three stale-edge probes.** I filtered deploy output to the health line, never saw the upload
   size, probed a build that had not shipped, and blamed the code. **Verify the upload, then
   re-probe against what is actually live.**
4. **A first placement fix that would have skipped the rows needing it** — it looked up
   `account:<personId>`, so an account written before the change read *absent* and was silently
   left alone. **A migration's repair path has to reach the un-migrated.**
5. **`except Exception: return None`** in `household_property()` — my own green-by-absence, written
   an hour after I flagged the same shape in three other tools. It **inverted** an earlier report
   of mine: six "correct, not a fault" lines were untrustworthy and the one UNREADABLE was the
   honest one.
6. **A backfill that filed un-upgraded rows as conflicts**, printing `points at 'est-e6696a', not
   est-e6696a` — the same string twice, because it compared the PAIR and reported one half.
7. **A first W6 pass that degraded Mom's Guru four ways** (dropped "inside Tate Mountain Estates",
   broke `2,800`→`2800`, replaced the anchoring examples, gutted 400 chars of habitat guidance).
   Caught by a byte-identity diff. **That content is CANON, not engine.**

## 5. Two LIVE FERNWOOD DEFECTS found while writing the ingestion proposal
⛔ **These are Fernwood-today problems, NOT multi-tenancy ones.** Forwarded to the registrar.

1. **`fold-answer.py`'s digest rebuild is opt-in behind `--deploy` (`:131`).** Without the flag a
   confirmation lands, retires its card, advances the watermark and refreshes the ribbon — **while
   canon never learns it.** Every surface that reads the loop reads *closed*; Garden Guru keeps
   answering from the old record.
2. **Retraction has no path.** Every ingestion route is additive, so *"she confirmed it and was
   wrong"* cannot be expressed. **"Everything is changeable" is already live on Mom's surfaces**
   `[paul-stated 2026-08-04]`, and that doctrine's own caveat is *never call a thing changeable
   and then make changing it costly.* Right now it is not costly — it is **impossible**.

## 6. Guardrails that stay in force
- ⛔ Never `git push origin main` — Mom's frozen production, ~695 commits divergent. "Full push"
  means `origin/staging`.
- ⛔ Invites are outbound and **Paul's alone**.
- ⛔ `home`, the condo and production deploys require Paul's explicit word.
- ⛔ `est-76012d` / `est-92e588` RETIRED, never reused.
- ⛔ Her words stay in `.private/`; an agent never fetches Mom's words from a channel she did not
  route to Fernwood.
- ⚠️ Deploys need the Bash sandbox disabled (wrangler needs network).
- ⚠️ Stage explicit paths; `git add -A` is hook-blocked (shared tree). Commit messages via `-F -`
  with a QUOTED heredoc.
- ⚠️ **The tree is shared with other live lanes.** `cycle/release/cycle-state.json` and
  `worker/digest.json` are generated artifacts that other lanes rewrite — they are not yours and
  are not drift.
