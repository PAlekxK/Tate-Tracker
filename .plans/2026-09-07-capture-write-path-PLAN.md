# capture-write-path · The per-estate write path — what lets a household keep what it makes

- row: BACKLOG.md § ▶️ NEXT · the per-estate capture write path (**ROW TO ADD** — see § Row to add; the orphan flag is expected until it lands)
- objective: O3
- class: engine · must-not-diverge
- question: at a household that holds no GitHub credential and never will, what happens to the things that household creates — and which of those things is actually broken?
- seats: engineering-partner → .engineering/2026-09-07-zones-v1-path.md
         ai-advisor → waived: nothing on this path invokes a model. Capture stays deterministic and AI-free by standing doctrine; this plan moves only where a write LANDS, never what is written
         ux-expert → ✅ **CONVENED 2026-09-12** → `.ux-reviews/2026-09-12-zone-save-honest-response-and-outbox.json`; it REFUTED step 5's premise (DESIGN PASS §E). Original waiver preserved: waived for steps 1–4 — they change no surface — the only user-visible difference is that a save which used to 503 now succeeds. ⛔ NOT waived for step 5, which is why the waiver is scoped: the honest-response field changes what the sync chip can say, and the chip is Mom-facing
         content-steward → ✅ **CONVENED 2026-09-12** — copy drafted for every state plus the failure sentence (~80% verbatim reuse); independently reached the same refutation as ux-expert (DESIGN PASS §E). Return not yet filed; filing is a step-5 act. Original: OWED, not waived, at step 5 only: if the sync chip gains a new state, its words reach Mom. No copy is drafted here
         user-researcher → waived: this plan changes no journey. The journeys that depend on it are scoped at .user-research/2026-09-07-zones-plants-v1-journey.md
         practice-steward → waived: this is a product defect, not a loop
- depends-on: .plans/2026-09-06-maps-and-zones-PROPOSAL.md
- stage: design
- ready: [paul-approved 2026-09-07] — *"I'm good to stamp everything as it is; obviously we can adjust as we learn more and actually progress."* ⚠️ **A stamp on a `concept`-stage plan authorises the STAGE, not the build.** Nothing merges, deploys or reaches an origin without its own gate — and for this plan the handoff's own gate stands: verify, prepare and stage; do not merge.
- stage-note: 2026-09-07 — written in the design lane of release lap 3. NOTHING SHIPPED. No code was written and no tracked file outside this one was edited.
- stage-note: 2026-09-12 late — ⭐ **BUILD PLAN FILED** → `.engineering/2026-09-12-capture-write-path-build-PLAN.md` (engineering-partner, per `[paul-stated 2026-09-10]`). It CORRECTED this pass on three points, each re-verified here: the CAS round trip does **not** exist (the client sends `{zones, _deleted, deviceId}` and never `_meta`, so the `stale-client` 409 has **NEVER FIRED**); *"git as a write-only mirror"* is unachievable (`ghPutFile` needs the blob sha from the read at `worker.js:5089`, and the second read supplies the file body); and `validVertex`'s envelope (lat 34.52–34.58, lon −84.40…−84.33) is Fernwood's own neighbourhood, so a household outside it fails **every** vertex. ⭐⭐ **PAUL RULED 2026-09-12 — (R5)** zones are **NAMEABLE now, DRAWABLE later**: the envelope is its own row, lifted with §5's basemap deferral, so ⛔ **this build does NOT make a household's zones drawable and must not be described as if it does**; **(R3)** the build window opens **only after the `design` band actually clears** (multi-tenancy leaves it when lap-8's P2 body half lands) — ⛔ **no build exception is taken and his 09-07 `concept`-stage stamp is NOT spent.** R1/R2/R4 were taken by the agent on the recommendation and are marked as such in the build plan, never as his. **R6** (the resident-facing noun) stays open.
- stage-note: 2026-09-12 late — ⚠️ **CITATION SWEEP, not a finding of this plan:** a concurrent lane renamed the env label `lab` → `dev` `[paul-stated 2026-09-12]`, shifting `wrangler.toml`'s home comment `:146` → `:154` (the `:66` one is above the insertion and did not move). ⭐ **The deployment name is PINNED `fernwood-lab` (`:111`), so every runtime measurement in §A — taken against `fernwood-lab.paul-kirschenbauer.workers.dev` — still holds.** The label moved; the host did not.
- stage-note: 2026-09-12 — **DESIGN PASS (`concept` → `design`).** Still NOTHING SHIPPED: no feature code, no deploy, no `BACKLOG.md` edit. Five runtime measurements were taken (all read-only or provably non-mutating) and the owed KV source was fetched. ⛔ **The stage moved AFTER Paul's `ready:` stamp, which he wrote against `concept` on 2026-09-07. Whether that stamp carries to `design` is HIS call, not this pass's** — it is preserved verbatim above and has not been reinterpreted.

> ### ⛔⛔ STRUCK 2026-09-12 — THIS BLOCKQUOTE IS FALSE AT HEAD. Read it as history only.
>
> ~~*"THE `ready:` LINE IS DELIBERATELY ABSENT AND MUST STAY ABSENT UNTIL PAUL STAMPS IT… Nine plans
> carry this flag today; this is the tenth, honestly."*~~
>
> **Paul stamped it the same evening it was written** and the `ready:` line is in the header above.
> The blockquote and the header have contradicted each other for five days and every reader inherited
> the contradiction. ⭐ **The strike is RECORDED rather than the paragraph deleted**, per this repo's
> standing practice — and because it is stale in the DANGEROUS direction: a reader who believed it
> would conclude the plan is ungated and either stop, or "correct" the header by removing a stamp only
> Paul may write.
>
> ⛔ **The rule the paragraph states is still true and is NOT struck:** an agent never writes its own
> `ready:`. Only the factual claim about THIS plan is struck.

> ✅ **WIP: THIS NEEDS NO EXCEPTION AND WAITS ON NOTHING.** Measured at HEAD —
> `🚦 WIP bands: · design 1/2 · build 1/1 (+3 excepted) · concept 9 (uncapped by ruling)`.
> `WIP_BANDS` caps `design/journey` at 2 and `build/qa` at 1; **`concept` is deliberately uncapped**
> (*"a concept costs nothing to hold, and capping it pushes ideas out of the record"*). So this
> enters at `concept` freely. ⛔ **It cannot enter `build` today** — that band reads 1/1 and already
> carries three declared exceptions. **Whether it takes a fourth exception, or waits for
> `c4-environments` to leave `build`, is Paul's ruling and is not pre-empted here.**

---

## ⭐⭐ DESIGN PASS — 2026-09-12 · `concept` → `design`

**Everything below was produced in one window whose only job was this transition.** The material
above is the CONCEPT as written on 09-07 and is left intact; where this pass contradicts it, **this
section wins and says so by name.**

### A · What was MEASURED at runtime — the concept was entirely code-read

The 09-07 plan's own § *What I could not verify* opens *"Nothing was executed against a deployed
Worker."* That is now closed for the load-bearing claims. `GET /health` is **unauthenticated**
(`worker.js:4195`; the file header reads *"all under X-Tate-Token auth except /health"*) and publishes
`configured.github = !!(env.GITHUB_TOKEN && env.GITHUB_REPO)` at `:4231` — **the identical predicate
`handleZoneSave:5050` gates on.** So the binding question was answerable for free all along.

| deployment | `env` | `estateId` | `configured.github` |
|---|---|---|---|
| `fernwood` | `production` (the frozen legacy Fernwood) | `est-3c9f1a` | ✅ **true** |
| `fernwood-home` | `home` | `est-e6696a` | ⛔ false |
| `fernwood-qa` | `qa` | `est-qa0001` | ⛔ false |
| `fernwood-lab` | `lab` | `est-lab0001` | ⛔ false |
| `myhome-paul` | `paul` | `est-d93508` | ⛔ false |

⭐ **Corroborated by a second, independent instrument**: the coordination window ran `wrangler secret
list` per deployment and got the same answer — `GITHUB_TOKEN`/`GITHUB_REPO` on `legacy` and nowhere
else. Two instruments, one result. **Exactly one deployment can reach git, and it is the frozen one.**

⚠️ **A correction to how this is usually stated, and it matters for step 3.** `wrangler.toml` carries
the ⛔ *NO GITHUB_TOKEN* ruling at **`:66` (dev) and `:154` (home) only**. **`qa` and `paul` carry no
such comment.** So *"forbidden permanently by ruling"* is true of two deployments; at `qa` and `paul`
the absence is **today's configuration, not a written rule.** ⛔ And note what `wrangler.toml` can
enforce: **nothing.** `GITHUB_TOKEN` is a *secret*, never a var — it appears in that file **zero**
times. The prohibition is a comment, and a comment does not survive `wrangler secret put`.
**Step 3 should therefore write the missing comments AND `check-*` should assert the binding via
`/health`, which is the only reader that sees the real state.**

**Two runtime probes, both provably non-mutating:**

- `POST /api/zone-save` at **`qa`** with qa's shared token → **HTTP 503 `{"error":"github-not-configured"}`**.
  The gate is the second statement in the handler, **above `request.json()`**, so nothing was parsed,
  sanitized or written. Proven rather than asserted: `GET /api/zones` at qa after the probe still
  reads `zones=0, _meta={}`.
- `POST /api/zone-save` at **`lab`** → **`{"error":"unauthorized"}`**. ⛔ **`lab` holds no secrets at
  all, so `authOk` (`:453`, `env.SHARED_TOKEN && tok && tok === env.SHARED_TOKEN`) is falsy for every
  request and the 503 is UNREACHABLE there.** Recorded because lab is the obvious place to send a
  prober and it cannot answer this question. **`qa` is the only non-legacy deployment where the gate
  is reachable.**

### B · ⭐ ADJUDICATED — the step-2 question. **The concept's caveat is WRONG.**

Falsifier 2 predicted *"before her first save, `home` would be served Fernwood's zones."* **Run today,
on both arms of the branch:**

| | `configured.github` | `GET /api/zones` |
|---|---|---|
| `qa` (cold KV, no binding — structurally identical to `home`) | false | **`{zones: [], _meta: {}}` — EMPTY** |
| `fernwood` (warm KV, binding present) | true | 18 zones: *The bank · Eastern Woodlands · Western Garden …* |

⛔ **Falsifier 2 is FALSIFIED, and the concept's attached caveat does not survive.** The caveat reads:
*"containment is held by the missing token, i.e. by the very thing step 1 removes — so a green result
is about the read path only and does not survive step 1."*

**That conflates a reader of the binding with the binding itself.** `handleZonesGet` gates its git
fallback on `env.GITHUB_TOKEN && env.GITHUB_REPO` at **`:5259`** — an *independent* consultation of the
same absent secret. Step 1 edits **`handleZoneSave` only**; it moves an early return, it does not
grant a binding. After step 1, `handleZonesGet` reads exactly the same absent secret it reads today
and falls through to `data = { _meta: {}, zones: [] }` at `:5267`. **Containment is durable across
step 1.**

> ### ⭐ THE RULING
> **Step 2 is NOT a co-requisite of step 1, and §3's "Steps 1 and 2 are ONE COMMIT" is withdrawn.**
> Step 1 cannot arm the leak. **Step 2 is a guard against the REJECTED ALTERNATIVE** — the fix that
> grants a household a `GITHUB_TOKEN` to make saving work is *precisely* what converts the empty map
> into Fernwood's 23. That is a real and permanent hazard, so **step 2 still ships** — but as
> independent hardening whose justification is *"default OFF fails in the right direction"* (falsifier
> 7), **not** as a same-commit dependency of step 1.

⭐ **Why this is a strengthening, not a demotion.** Coupling them was costing the plan its cheapest
property: step 1 alone is a genuinely isolated change whose blast radius is one handler at four
deployments that are already 503-ing. Decoupled, step 1 can land and be verified on its own.

⚠️ **One measured divergence recorded in passing, not chased:** git's `zones.json` holds **23** zones
and the frozen deployment's KV serves **18**. The store the product actually reads and the store the
plan calls "long-term canon" **do not agree today**. Not this plan's defect; it is squarely the
concern of anyone who still believes git is the durable copy.

### C · ⭐⭐ THE KV RULING — the owed source, FETCHED

`developers.cloudflare.com/kv/concepts/how-kv-works/` was read directly, as the concept required.

**On consistency the concept is CONFIRMED, verbatim:** *"KV achieves high performance by being
eventually-consistent"* · *"Changes may take up to 60 seconds or more to be visible in other global
network locations"* · ideal for *"read-heavy, highly cacheable workloads… Storing application
configuration, Storing user preferences"* · not ideal for *"write-heavy Redis-type workload where you
are updating the same key tens or hundreds of times per second."* §1's three claims stand as written.

⛔⛔ **But the page makes NO DURABILITY GUARANTEE AT ALL — it does not mention durability, data loss,
or concurrent writes.** The source this plan was told to read **cannot answer the question it was
fetched to answer.** That is itself the finding, and it is why *"read the page before the stamp"* was
the right instruction: the answer is that the page is silent.

**Ruled, from the wider record:** durability-as-data-loss is **not** the risk. Cloudflare's own
engineering writing describes KV as persisting data in central stores with **three-way replication**.
Nothing suggests KV loses committed writes.

> ### ⭐ THE RULING: **KV alone MAY carry a household's record.** The risk was never durability.
> **It is CONSISTENCY meeting a whole-record overwrite**, and the concept's §1 argues the right
> conclusion from a premise that is about to expire. Two exposures, neither of them data loss, both
> unaddressed by the concept:

**C1 · Negative caching on first run — bounded, and it looks exactly like data loss.**
The page: *"Negative lookups indicating that the key does not exist are also cached, so the same delay
exists noticing a value is created."* At a household, `zones:all` does not exist before the first save,
and **every `GET /api/zones` before that save caches the miss.** After her first save, a read served
from another location can return the cached negative for **up to 60 seconds or more** →
`handleZonesGet` falls to `{zones: []}` → **the blank first-run map, again.** ⛔ There is no error
state: *"you have no places yet"* and *"your places are 40 seconds away"* render **identically**. On a
property whose premise is *coverage falls off with distance from the house*, reload-after-walking-back
is the normal motion, not the edge case. **This is `capture must not lie`, and the concept does not
mention it.**

**C2 · Whole-record last-write-wins, with no compare-and-swap and — after step 1 — no revert.**
`handleZoneSave`'s own comment: *"ALL-OR-NOTHING. The sanitized array below becomes the ENTIRE file."*
The client PUTs the whole array it last read; the server merges nothing. **Two members editing inside
the propagation window: the second save silently destroys the first.** Today git gives that a
`git revert`. **After step 1, at a household, nothing does.** The concept flags *"no version history at
a household"* but frames it as a lost audit trail — *"per-zone provenance is intact"* — and offers
`zones:prev`, **one undo deep**, which a second bad save consumes.

⛔ **And §1's load-bearing word is `single-writer`, which has a SCHEDULED EXPIRY inside this very
plan.** Step 6 adds identity to the write path *because more than one person writes*; the account/estate
work carries *"people can invite each other"* and a second household member. **The premise that makes
KV safe here is one the roadmap removes.**

> ### ⭐ THE RECOMMENDATION, and it is cheap because the pattern is already in the handler
> **Add an application-level compare-and-swap, reusing the `stale-client` 409 that already exists
> (`:5107`–`:5117`).** That block already refuses a write whose `body._meta.schemaVersion` disagrees
> with the server's — *"A stale client is a rejected write, not a silent downgrade."* **Extend the
> same guard to `_meta.lastBuiltAt`.**
>
> ⛔⛔ **CORRECTED 2026-09-12 by the build audit — I claimed the round trip already existed. IT DOES
> NOT, and the error mattered.** Measured: `syncZonesNow`'s payload is exactly
> `{zones, _deleted, deviceId}` (`engine/viewer.template.html:14253`) and **`_meta` appears ZERO
> times** in the whole sync region (13900–14450). The client RECEIVES `lastBuiltAt` and never sends
> anything back. So the CAS needs a **client change**, shipped **client-first with a deploy between**,
> or it 409s every save in the field — including at the frozen Fernwood. **Sizing was understated and
> the recommendation stands only with that sequencing.**
>
> ⭐ **And the same measurement reveals a live defect worth more than the correction:** because
> `body._meta` is never sent, `clientSchema` at `:5108` is always `undefined`, so the `stale-client`
> 409 guard **has never fired once.** It was written to police the v2→v3 schema move and was inert
> for all of it. ⛔ A guard nobody can trip is not a guard — and this plan came within one step of
> building a durability control on top of it. A save built on a stale read is refused with a named
> error instead of overwriting somebody. ⛔ Without this, KV-only is safe **only while exactly one
> person edits zones**, and that is a promise this plan's own step 6 breaks.

### D · ⛔ STEP 1 IS NOT "XS", AND THE FILES-TOUCHED TABLE UNDERCOUNTS THE GIT SITES

The concept says *"move the gate from `:3850` to wrap the commits at `:3955`/`:3969`"* — **two** sites.
Re-run at HEAD, attributing every `ghPutFile`/`ghGetFile` call to its handler, `handleZoneSave` has
**FOUR**:

| line | call | note |
|---|---|---|
| **`:5089`** | `ghGetFile("zones.json")` | ⛔ **a git READ, and it sits ABOVE the KV write at `:5131`** |
| `:5155` | `ghPutFile("zones.json")` | commit 1 |
| `:5158` | `ghGetFile("viewer.html")` | ⛔ a second git READ |
| `:5169` | `ghPutFile("viewer.html")` | commit 2 |

✅ **It does not crash** — I expected `ghGetFile` to throw at a household (`Bearer undefined`) and
**verified instead of asserting: GitHub returns 404, not 401**, so `ghGetFile` takes its clean
`{exists:false}` branch at `:3234`. Recorded because the opposite is the intuitive guess.

⛔ **But the consequence is a real design hole the concept never reaches.** `existingData` comes from
that git read, and **`_meta` comes from `existingData`** (`:5102`) — the georeference: `baseImage`,
bounds, image dimensions. The comment above it is emphatic: *"THE SERVER OWNS `_meta`… infrastructure,
not user data, and no drawing tool has any business rewriting it."* **At a household there is no git
read, so `meta = {}` — and the server owns an empty object.** Every household zone record would carry
**no georeference at all**, written fresh on every save.

> ### ⭐ THE RESHAPE — and it is a better step 1 than the one in §3
> **Step 1 is not "move a gate." It is: make the handler read its prior state from the store it
> writes to.** `existingData` should come from **KV** (`keyFor(scope, "zones", "all")`) — the
> *declared primary read path*, per the handler's own comment — with git demoted to a **write-only
> mirror** where a token exists. That change (a) removes both git reads from the household path, (b)
> gives `_meta` a real household source, (c) makes the handler's read and write halves agree about
> which store is authoritative, and (d) is the precondition for C2's compare-and-swap, which needs a
> live read of the current record. **Sizing moves XS → S.**

⚠️ **`_meta` at a household still needs an ORIGIN even after that** — a household's first save has no
prior KV either. That ties directly to §5's deferred basemap: §5 defers `images/` because *"no
household has a basemap to serve,"* which is true, **but `_meta` is not the image — it is the
georeference, and it is absent for a different reason.** ⛔ **Unresolved, and named rather than
guessed.**

### E · THE TWO OWED SEATS — CONVENED. **Both refuted step 5's premise, independently.**

ux-expert (waived 1–4, **owed at 5**) and content-steward (**owed at 5**) were run separately and
without sight of each other. **They converged on the same finding, and it contradicts this plan, the
handoff brief that commissioned this pass, and the brief I wrote them.**

> ### ⛔⛔ THE CHIP WAS NEVER A KV→GIT PROGRESSION. Step 5's premise is a misreading.
> `handleZonesSyncStatus` computes `allCaughtUp` **entirely from KV** — canon is `_meta.lastBuiltAt`
> written by the KV put at `:5131`; device stamps are `zones-last-seen:<id>` written by `GET /api/zones`
> at `:5275`. **Git appears nowhere in that path.** The three states already mean *saving → the Worker
> has it → your other phones have it*, and **all three are reachable at a household the moment step 1
> lands.**
>
> ⭐ **So `kv` vs `kv+git` is not a distinction the chip was ever making, and the "honest response"
> field does not need a new chip state.** What is actually false is a **code comment** —
> `engine/viewer.template.html:14054` describes `synced` as *"commits live on git + KV."* **Fix the
> comment; the labels need no new state.** ⛔ **Neither seat's waiver could have caught this — it took
> convening them.** This is the strongest argument in the file for not scoping seats out by default.

**⛔ CRITICAL — and it is the one item I would not let step 5 ship without.** Verified independently
at HEAD:

- `getZoneAudienceMode()` defaults to **`"quiet"`** (`:14045`), and `render()` hides the chip in every
  state **except `failed`** (`:14135`). **So the only chip state a resident can ever see is the failure
  one.**
- On failure, `renderDetails()` prints `escapeHtml(String(lastError))` raw (`:14155`), and `lastError`
  is built at `:14267` as `"HTTP " + status + ": " + body.slice(0,300)`.
- At a household that string is therefore:
  **`HTTP 503: {"error":"github-not-configured","hint":"set GITHUB_TOKEN and GITHUB_REPO worker secrets"}`**

**The single visible sync state on the resident's surface instructs her to set Worker secrets — a
thing forbidden at her deployment by ruling.** ⭐ Step 1 removes the 503; **the raw-error-reaches-the-
resident path survives it**, and is worth fixing on its own terms.

⚠️ **SEVERITY CALIBRATED — it is LATENT, not live.** `instance/home.json` lists **`zones` in its
`absent` array** (line 31), so the zone surface does not render at a household and **no resident has
ever seen this chip.** It is a wall the moment zones are un-absented, which is exactly what this plan
unblocks. *(Stated precisely because "Mom is being shown a raw 503" would be false, and this repo's
most repeated defect is a status claim nobody re-ran.)*

**Also verified, and it survives into `design`:** `"✓ live everywhere"` **over-claims**. `allCaughtUp`
requires only `devices.length > 0` and **`handleZoneSave` stamps the editing device itself** before
returning — so on a one-device household, *"everywhere"* resolves true by counting **the phone that
just made the edit**. The device set carries a **30-day TTL** (`:5278`), so the claim gets *easier to
satisfy as coverage gets worse.*

**Both seats independently recommend AGAINST a new IndexedDB outbox for zones** — the concept's
*"reuse `ZoneAudioOutbox`"* is the right instinct on the **sentence** and the wrong one on the
**mechanism**: audio is a per-item append stream where losing an item loses words; zones are a
whole-document last-write-wins object, so a queue would hold N copies of one file. Zone edits are
**already** persisted to `localStorage` before the sync is scheduled (`:14019`). ⭐ **The real gap is
narrower and cheaper: zones retry only on a full page load, while audio flushes on `online` and
`visibilitychange` (`:11439`–`:11441`). Take the flush triggers and the sentences; leave the queue.**

⚠️ **Raised by ux-expert, verified, and OUT OF STEP 5's SCOPE — routed, not absorbed:**
`tateTracker.zones.v1` and `tateTracker.zones.lastSyncedAt.v1` are rostered in `STORAGE_KEYS`
(`:7442`–`:7443`) but are **NOT in `STORAGE_KEYS_PER_ESTATE`** (`:7450`, which holds only the four
`momQueue*` keys) and are read bare (`:11476`, `:14040`). **On a device that opens two estates that is
one shared zone cache and one shared watermark.** → engineering-partner, before this path reopens.

**Full seat artifacts:** `.ux-reviews/2026-09-12-zone-save-honest-response-and-outbox.json` (ux-expert,
written). Content-steward's copy options — three states plus the failure sentence, each with the
trade-off named, ~80% verbatim reuse of shipped sentences — are in its return and are **not yet
filed**; filing them at `.content/2026-09-12-sync-chip-copy-DRAFT.md` is a step-5 act, not this pass's.

⛔ **Content-steward's open question, which no agent may answer:** the resident-facing noun for a zone
edit ("change"? "edit"? neither?) is unsettled, and three of its drafts wait on it. **Paul's.**

### F · FALSIFIER 1 — how it gets run, and the half that is now FREE

The concept requires falsifier 1 **before** step 1: *"POST each of the five capture endpoints against
`home`… if more than `zone-save` is broken, this plan's whole scope correction is wrong."*

⭐ **Its expensive half is now discharged statically, at HEAD, with no writes.** Re-running the
`ghPutFile`/`ghGetFile` attribution and bounding each handler:

| handler | true bounds | git references |
|---|---|---|
| `handleFeedback` | `4085`–`4181` | **NONE** |
| `handleObservations` | `1874`–`1906` | **NONE** |
| `handleConversations` | `3930`–`4023` | **NONE** |
| `handleZoneFeedback` | `5182`–`5246` | **NONE** |
| `handleZoneAudio` | `2643`–`2748` | **NONE** |
| `handleZoneSave` | `5048`–`5181` | `ghPutFile` ×2, `ghGetFile` ×2, `GITHUB_TOKEN`, `GITHUB_REPO` |

⚠️ **A first pass of this attribution reported `handleFeedback` as touching git. It does not** — a
crude col-0 function matcher had swallowed the router, and the hit was `/health`'s own
`configured.github`. Bounded properly, it is 97 lines and clean. *Recorded because the wrong answer
looked exactly as authoritative as the right one.*

**So the scope correction holds on the token question: five of six capture handlers contain no git
reference at all and cannot 503 for the reason `zone-save` does.** ⛔ **What the static read CANNOT
answer** is whether any of them fails for an unrelated reason (rate limit, payload, auth, a KV
binding) — that still needs the live POST.

**How the remaining half gets run — named, per the brief:**
1. ⛔ **Not from this session, and not at `lab`.** `lab` holds no `SHARED_TOKEN`, so every gated
   endpoint there answers `unauthorized` (measured above). **`home` is the target and no `home`
   shared token exists locally** (`.private/` holds `fernwood-token` and `fernwood-token-qa` only).
2. ✅ **`qa` is a faithful stand-in for every binding-dependent claim** — same `configured.github:
   false`, same code, its own estate and KV — and this session already used it to run falsifier 2 and
   the 503 probe. **But the five capture endpoints WRITE**, and `est-qa0001` is the namespace that
   already holds 201 account rows with **nothing provably a fixture and `--teardown` refusing by
   design**. ⛔ **Adding five unprovable rows there to test a claim would worsen the exact problem
   `household-fixtures.py` exists to name.** Not done, deliberately.
3. ⭐ **The clean route is the gate kit** — the five POSTs go in the next gate-kit run against `home`
   with a real grant, where the writes are attributable and expected. **It is a gate-kit act, not a
   session's**, and it is the one remaining thing standing between step 1 and a build.

### G · What this pass did NOT settle — Paul's, and not pre-empted

1. ⛔ **Whether `ready: [paul-approved 2026-09-07]` carries to `design`.** He stamped it against
   `concept`. The stamp is preserved verbatim and untouched.
2. ⛔ **The `design` WIP band is now over its cap** — measured after this transition:
   `⚠️ design 3/2` (this plan, `2026-09-07-zones-PLAN`, `2026-09-10-multi-tenancy-PLAN`). **This pass
   consumed the slot that took it over.** Whether this carries a `wip-exception:`, or another plan
   leaves the band, is his ruling.
3. **The resident-facing noun for a zone edit** (§E).
4. ⭐ **The standing question this plan cannot answer about itself:** `zones` is `absent` at every
   household, so **no resident has ever used this surface** — and the loop's own rule is *before any
   finding about her behaviour becomes an organising claim, ask Paul what she has asked him for
   lately.* **He has said she asks about zone layout by name.** That is the demand signal this plan
   is built on, and it is the one input no instrument here can read.

**Routed to the backlog window (not written here):** TIER 2 · 8's framing — *"move the gate down"* —
is measurably incomplete (§D), and the row's *"exactly one create is broken"* is right about
`zone-save` and understates that saving is dead at **four of five deployments** (§A).

---

## ⭐ THE FINDING THAT RESHAPES THE SCOPE

The framing this plan was commissioned under was:

> *"On the instance Mom will actually use, nothing she creates can be saved."*

**That is wrong, and the correction makes the work much smaller and much better-shaped.** Measured
at HEAD by enumerating every `ghPutFile(env, …)` call site and attributing it to its handler:

```
2476: ghPutFile              ← the definition
2832 · 2858 · 2906 · 2933:   handlePromoteSpecies
2993 · 3006:                 handleRemoveSpecies
3955 · 3969:                 handleZoneSave
```

**Three handlers write to git. That is all of them.** And of the five handlers that receive what a
household actually creates:

| handler | writes git? | works on `home` today |
|---|---|---|
| `handleFeedback` — her card answers | **no** | ✅ |
| `handleObservations` — her field notes | **no** | ✅ |
| `handleConversations` — her Guru turns | **no** | ✅ |
| `handleZoneFeedback` — "describe a place" | **no** | ✅ |
| `handleZoneAudio` — her voice recordings | **no** | ✅ |
| `handleZoneSave` — zone geometry + names | **yes** | ⛔ **503** |

⭐ **So everything Mom *contributes* already saves fine at a household. Exactly one thing does not,
and it is not a contribution path — it is a CANON-EDITING path.** `promote-species`,
`remove-species` and `zone-save` all write to the repo because they edit the record **that ships in
the build**. That is a curator act, not a resident act, and the `GITHUB_TOKEN` gate in front of them
is not an accident — it is the right instinct pointed at the wrong granularity.

**And at a household there is no shipped canon to edit.** `instance/home.json` declares 18 domains
`absent`; `instance/neutral-canon/` holds two files. A household's zones were never going to be
canon in this repo. **The git half of `handleZoneSave` is meaningless at a household by
construction** — it is not a capability being withheld, it is a capability with nothing to act on.

> ### ⛔ THE SCOPE CORRECTION, STATED ONCE
> This is **not** "build a per-estate capture write path." The per-estate write path **already
> exists, is already per-estate-scoped, and is already the declared primary read path.** `handleZoneSave`
> writes `keyFor(scopeOf(env), "zones", "all")` and its own comment reads: *"KV write — primary read
> path. Devices fetch zones from GET /api/zones which reads this key, bypassing the GH Pages deploy
> tail. Git commits below remain as long-term canon + cold-start fallback."*
>
> **The entire defect is that the `GITHUB_TOKEN` gate sits at the top of the handler (`:3850`)
> instead of around the git half (`:3955`–`:3969`) — and the KV write it blocks is at `:3932`.**
> An early return guarding a *later, optional* side effect. That is the whole bug.

**Why this is worth stating so loudly:** the expensive framing ("stand up a write path") and the
cheap one ("move a gate down 100 lines") produce the same *sequence position* — LEG 0, before both
zones and plants — but wildly different *cost*, different *risk*, and a different answer to whether
it can share a lap with other work. Getting the framing right is most of the value in this file.

---

## §1 · IS THE WRITE PATH REALLY LEG 0?

**Yes on position. No on size.** It is LEG 0 because both legs of Paul's re-sequenced order —
*define zones first, then add plants* — begin with a household **creating** something, and creating
a zone is the one create the household cannot complete. But it is a gate-move, not a build.

### The cheaper path, stated concretely

Replace the early return at `handleZoneSave:3850` with a conditional around the two git commits:

- **Today:** no token ⇒ `503`, before parsing, before sanitizing, before the KV write.
- **Proposed:** always sanitize, always write KV, and commit to git **only if a token is present**.
  The response reports which of the two happened.

On `home`: her zones save to KV, `/api/zones` reads them back, they persist across devices. On
prod-frozen (the only env holding a token): **byte-identical behaviour to today.**

### Why KV-only is not a durability downgrade — the objection I expected to raise and cannot

I went looking for the reason this would be irresponsible and the repo answered it:

1. **KV is the only storage this product has.** `wrangler.toml` declares **zero** `d1_databases`,
   `r2_buckets` and `durable_objects` bindings across all five envs. There is no better store being
   passed over.
2. **Every other thing she creates is already KV-only with no git backstop** — her feedback, her
   observations, her Guru turns, her zone-audio recordings, her account, her grant. **Zones being
   the one domain that demands a git commit is the anomaly, not the safety.** A design where her
   voice recordings are KV-only but her zone names require a repo commit is not defensible as a
   durability argument; it is a leftover from when this repo *was* the product.
3. **The consistency model is adequate for this shape.** Workers KV is eventually consistent —
   changes may take **up to 60 seconds** to propagate to other locations, and it is a poor fit for
   write-heavy same-key workloads. A household's zone record is a **single-writer, low-frequency,
   read-heavy** object. That is squarely inside KV's intended envelope (*"configuration data,
   feature flags, and similar"*), and it is the same envelope her notes already live in.

⚠️ **Two honest costs, and neither is a blocker but both must be written down rather than
discovered:**

- ⛔ **The cold-start fallback disappears at a household.** Today a device with no Worker reachability
  falls back to `ZONES_DATA` inlined in `viewer.html`. At `home` that constant is empty. So a
  household device that cannot reach the Worker shows **no zones** rather than stale ones. That is
  the *honest* state and I would not fix it — but it interacts directly with the site's physical
  premise (**no cell reception; coverage falls off with distance from the house**). **A zone drawn
  or renamed out at the pond and then closed before walking back into range must not be lost.**
  ⭐ **The pattern already exists in this codebase and should be reused, not reinvented:**
  `ZoneAudioOutbox` already queues her recordings offline and flushes on return, and `ZonePanel.open()`
  already tells her *"N recordings are still on your phone — they'll go to the record when you're back
  on Wi-Fi."* **Zone saves want the same outbox and the same sentence.** Reusing it is also what keeps
  one consistent world — *your phone · the record · Wi-Fi* — instead of minting a second story.
- ⚠️ **No version history at a household.** Git gave zone edits a free audit trail. KV does not.
  `zone.history[]` is in the record itself and survives, so per-zone provenance is intact — but a
  bad whole-file overwrite has no `git revert`. **Mitigation is cheap and I would take it:** on each
  save, write the previous value to `keyFor(scope, "zones", "prev")` before overwriting. One extra
  KV put; one undo deep. Not a versioning system, and it should not be called one.

### What I could NOT make cheaper, and where the framing survives intact

**The 503 is currently doing accidental containment work, and removing it removes that.** Today, two
independent things stop `home` from serving or overwriting Fernwood's zones: the missing token, and
`ABSENT_DOMAINS.includes("zones")` on the client. **This change removes the first.** And before her
first save, `home`'s KV holds no `zones:all` key — which is precisely the condition that makes
`handleZonesGet` fall through to `ghGetFile(env, "zones.json")` and serve **Fernwood's 23 zones**.

⛔ **So R-Z6 (B) is not an adjacent nicety — it is a hard co-requisite of step 1 and must land in the
same commit.** Unblocking the write without gating the read fallback means a household's very first
map load shows *"The bank"*, *"Eastern Woodlands"*, *"St Francis Garden"* — and ruling Z-10 says the
new instance starts with **none of that data**. The whole point of the re-sequence is defeated by
the one step that enables it.

---

## §2 · WHERE THE COMMISSIONING BRIEF WAS WRONG

Stated plainly, because three of these were load-bearing.

1. ⛔ **"Nothing she creates can be saved."** Five of six household-facing capture handlers write no
   git and work today. Only `zone-save` is broken, and it breaks because it is a canon-editing path
   wearing a capture path's clothes. (§ above.)
2. ⚠️ **"All eight `ghPutFile` sites are the same story."** They are the same *mechanism* and not the
   same *story*. Six are species promotion/removal — **operator acts on Fernwood's canon, with no
   household meaning at all**, and the right disposition for them at a household is *stay 503, and
   say why*, not *make them work*. Only the two zone sites want the conditional. Treating all eight
   alike would build a household-scoped species-promotion path nobody asked for.
3. ✅ **"`handlePromoteSpecies` opens with a 503 on a missing token"** — exact, `:2679`.
   `handleRemoveSpecies` `:2967` and `handleZoneSave` `:3850` are identical in shape.
4. ✅ **`home` holds no `GITHUB_TOKEN` deliberately and permanently** — `wrangler.toml:115` verbatim:
   *"⛔ NO GITHUB_TOKEN, ever: GITHUB_BRANCH defaults to 'main', so a token here would promote species
   onto Mom's live branch."*
5. ✅ **The identity counts are exact.** 42 history entries: `paul` 24 · `paul-area-trace` 7 ·
   `device` 6 · `reconciliation` 4 · `agent-claude` 1. `lastEditedBy` present on 23 of 23. `namedBy`
   in 22 details.
   ⚠️ **One correction that matters for the field design:** `lastEditedBy` is `"paul-area-trace"` on
   **all 23** — that is a **tool name, not a person**. And of the six non-`paul` writers, `device`
   (6) *and* `reconciliation` (4) are both machine-written. So the honest read is **31 entries name a
   human or a human's tool, 10 name a machine process, 1 names an agent** — not "36 name a real
   author". The distinction is the whole reason the new field must be labelled carefully (§3, step 6).
6. ✅ **"A wiring gap, not a missing layer"** — correct and well put. `/api/grant/whoami` exists
   (`worker.js:3605`, rostered in `/health`'s endpoint list), and `handleZoneSave` reads
   `scopeOf(env)` plus a free-text `body.deviceId` while never asking who is signed in.

---

## §3 · SEQUENCE

~~⛔ **Steps 1 and 2 are ONE COMMIT.** Separating them opens a window in which a household can write
zones while still being served Fernwood's.~~ ⛔⛔ **WITHDRAWN 2026-09-12 — see DESIGN PASS §B.**
Falsifier 2 was RUN and returned EMPTY: `handleZonesGet`'s fallback consults the absent binding
independently (`:5259`), and step 1 does not grant one. **Step 2 still ships — as independent
hardening against the rejected grant-a-token fix, not as a same-commit dependency.** Every step is
independently landable.

| # | step | why here | size |
|---|---|---|---|
| **1** | ⚠️ **RESHAPED 2026-09-12 (DESIGN PASS §D) — NOT a gate move.** `handleZoneSave` touches git in **FOUR** places, not two, and one is a READ (`:5089`) above the KV write that supplies `_meta`. The step is: **read prior state from KV — the declared primary read path — and demote git to a write-only mirror where a token exists.** | The whole defect. Everything downstream of Z-10 is blocked on it. | ~~XS~~ **S** |
| **2** | ⛔ **R-Z6 (B) — a declared per-env switch, default OFF, gating `handleZonesGet`'s git fallback.** Read it from a `vars` entry (e.g. `ZONES_GIT_FALLBACK`), never from an estate id. | Co-requisite of 1 (§1). Without it, step 1's first beneficiary is served Fernwood's 23 zones. | **XS** |
| **3** | **R-Z6 (C) — name zones in the `GITHUB_TOKEN` comment in all five env blocks.** | The comment is the only place the constraint is explained, and it currently explains the wrong half. | **XS** |
| **4** | **R-Z6 (D) + `build-digest.py`'s unguarded `load()`** — a check asserting every non-frozen env returns an empty zone list, and an absent-aware digest loader. | Both are "the tool must tolerate a household that has nothing yet." Same shape, same lap. | **S** |
| **5** | **The honest response + the offline outbox.** `zone-save` reports what actually persisted; `ZonePanel` reuses `ZoneAudioOutbox`'s queue and its sentence. | ⚠️ ux-expert + content-steward seats bind here. | **S** |
| **6** | **Identity as a field on the write path** — `by: "account:<username>"` from the presented grant. | Independent of 1–5. Closes the one writer that cannot attribute itself. | **S** |
| **7** | **`zone.geometry` as a literal RFC 7946 Geometry object**, with `sanitizeZone` extended in the same commit. | Deferred until the zone-drawing work actually needs lines. Recorded here so the shape is not re-decided. | **M** |
| — | **`images/` on the household allow-list** | ⛔ **EXPLICITLY DEFERRED.** See §5. | — |

### Step 2 in detail — why "never a hardcoded `est-3c9f1a`" is the load-bearing clause

**This repo has embedded Fernwood literals in engine code at least three times**, and each one was
correct when written and false the moment a second estate existed:

- `validVertex`'s `ZONE_LON_MIN/MAX` — a ~6.4 × 6.7 km box around Fernwood, applied to every estate.
  Its own comment calls it *"the property's neighbourhood, generously padded"*, which is a
  single-estate sentence in a multi-estate function.
- `tools/area-trace.html` and `tools/zone-capture.html` — both built against Fernwood's basemap.
- `renderPropertyMap`'s `FALLBACK_*` paths, already flagged in the C7 stage-notes as *"a derivation
  leak noted for retirement."*

⭐ **The general rule, which is worth more than this fix:** *a constant that is true of exactly one
instance belongs in that instance's declaration, not in the engine.* A per-env `var` is checkable by
`check-engine-manifest.py` and greppable across all five envs; an estate-id comparison buried in a
handler is neither. **And it fails in the right direction:** default OFF means a new env that nobody
thought about serves an empty list, not somebody else's places.

### Step 6 in detail — the identity field, and the label it must carry

⚠️ **`by: "account:<username>"` names a SESSION, never a person.** This repo's standing line is *a
deviceId is a browser bucket, not a person*, and an account row is a **stronger** claim than a device
bucket but still not a claim about who was holding the phone. Mom's phone, signed in as Mom, handed
to Paul, is Paul editing as Mom — and the record must not be able to say otherwise.

**So the field records who the write was AUTHENTICATED AS, and every surface that renders it must
say that and not more.** Concretely: `"account:mom"` is legible and honest; *"Mom named this"* is a
claim the field cannot support. The record already attributes 22 zones by hand with an explicit
`details.namedBy`, precisely because a human asserted it — **that hand-written assertion outranks
this derived field and must not be overwritten by it.** Two fields, two epistemic statuses, and the
derived one never silently replaces the stated one. This is the same shape as
`[transcript-UNVERIFIED]` on zone audio: a machine-derived attribution may *support* a claim and may
never *promote* one.

---

## §4 · WHAT THIS PLAN DOES NOT DO

- ⛔ **It does not make `promote-species` or `remove-species` work at a household.** They edit
  Fernwood's canon and have no household meaning. **Their 503 is correct** — but its `hint` should
  say *"canon editing is not available at this household"* rather than *"set GITHUB_TOKEN and
  GITHUB_REPO worker secrets"*, which reads as a misconfiguration a household admin should fix.
- ⛔ **It does not touch `ghPutFile` itself, and it does not make git multi-tenant.** After step 1,
  git is reached only from envs holding a token — today exactly one, the frozen Fernwood — so the
  *"eight call sites, one repo"* problem stops being on the critical path. **It is not solved. It is
  made irrelevant to households**, which is a different and much cheaper claim. Whoever later binds
  a GitHub credential to a household Worker re-opens all of it at once.
- ⛔ **It does not settle R-Z5** (whether v1 ships to the condo or to production Fernwood). Paul has
  parked that: *"we'll have a lot of work defining and playing with this in dev before we even try to
  promote it to QA."* This plan is deliberately upstream of that choice and is required either way.
- ⛔ **It does not design the zone-drawing surface.** That is `.plans/2026-09-07-zones-PLAN.md`.

---

## §5 · `images/` AND THE BASEMAP — EXPLICITLY DEFERRED, WITH THE REASON

**Measured at HEAD.** `tools/pages-deploy.py:67` — `HOUSEHOLD_ALLOW` is nine named paths and
**contains no `images/`**; `HOUSEHOLD = {"bob", "paul", "home"}`. Anything outside the list is
deleted from the export **and tombstoned** at the origin. **So a household origin cannot serve a
basemap today**, and the deploy refuses on a violation by design.

⛔ **The obvious fix is the wrong one, and the file says why in its own comment.** Adding `images/`
as a prefix would ship all of `images/property-map/` — Fernwood's NAIP frames, the lidar hillshade
and slope rasters, the historical topo crops — **to Bob's origin**. That is exactly the failure the
allow-list was written for: *"`onboarding/` as a prefix shipped `onboarding/invite-message.md`"*, an
unsent outbound draft, publicly readable, measured 2026-09-06. **An exclude-list is a promise that we
thought of everything; an allow-list fails toward serving too little.**

**Deferred, for three reasons that are about sequencing, not difficulty:**
1. **No household has a basemap to serve.** `renderPropertyMap` already returns nothing when the
   zones record declares no basemap, and Paul's rule is *"better to not display something rather than
   display something that's empty."* There is no gap in the product today.
2. **Z-10 says define zones first at the new instance** — and a zone record with a name and no
   geometry is a first-class state (`sanitizeZone:3751`: *"An EMPTY vertex list is valid: a named
   place that has no boundary drawn yet… It must round-trip."*). **Naming places needs no basemap.**
3. **The right shape is a per-instance named path, not a directory prefix** — the instance declares
   its own basemap filename and the allow-list is *derived* from that declaration, so Bob's origin
   ships Bob's frame and nothing else. That is a small design and it should be designed when a
   household actually has an image, not speculatively.

⚠️ **Recorded so it is not re-discovered:** the day a household gets a basemap, this is a blocker,
and it is a **deploy-refusal** blocker, not a silent one. Good failure mode; still a wall.

---

## Files touched

**Nothing has been touched. This session wrote this file and nothing else.** Below is what an
implementation would touch, per step.

| file | change | step |
|---|---|---|
| `worker/worker.js` `handleZoneSave` (`:3848`–`:3980`) | move the token gate from `:3850` to wrap the commits at `:3955`/`:3969`; KV write at `:3932` becomes unconditional | 1 |
| `worker/worker.js` `handleZonesGet` (`:4046`–) | gate the `ghGetFile` fallback on a declared per-env var, default OFF | 2 |
| `worker/wrangler.toml` | the new var in all five env blocks; **and the `GITHUB_TOKEN` comments** — ⚠️ measured: `qa`/`lab`/`home` have one and **`bob`/`paul` have none at all**, and **zero of the three mention zones** | 2, 3 |
| `tools/check-*` (new or extended) | assert every non-frozen env returns an empty zone list | 4 |
| `tools/build-digest.py` | absent-aware `load()`; conditional `CORE_INCLUDES`; selftest case | 4 |
| `worker/worker.js` `handleZoneSave` response | report what persisted (`kv` / `kv+git`) instead of a bare `{ok:true}` | 5 |
| `engine/viewer.template.html` — `ZonePanel` / a zone-save outbox | reuse `ZoneAudioOutbox`'s queue + its existing sentence. ⛔ **NOT this session** — the file is uncommitted under another live lane | 5 |
| `worker/worker.js` `sanitizeZone` (`:3745`) | accept and preserve `by`; later, `geometry` | 6, 7 |
| `worker/worker.js` `handlePromoteSpecies` / `handleRemoveSpecies` | reword the 503 `hint` only — **no behaviour change** | 4 |
| `BACKLOG.md` | § Row to add | on stamp |

### Row to add

> **⭐ THE PER-ESTATE WRITE PATH — a household cannot keep the zones it makes.** `handleZoneSave`
> returns 503 without a `GITHUB_TOKEN`, and `home` holds none deliberately and permanently. But the
> KV write it blocks is the *declared primary read path*, and five of six household capture handlers
> already write KV with no git at all. **The gate guards the wrong half.** LEG 0 for Z-10's
> *define-zones-first* sequence. → READY · `.plans/2026-09-07-capture-write-path-PLAN.md`

## Sequence

See §3. In one line: **move the gate and gate the fallback (one commit) → name zones in the env
comments → the empty-list check and the digest guard → the honest response and the offline outbox →
identity as a field → geometry, when lines are actually needed.** `images/` is deferred with its
reason recorded (§5).

## Falsifier

Each is refutable by evidence, not by argument.

1. **"Only `zone-save` is broken at a household."** → FALSIFIED if any of `/api/feedback`,
   `/api/observations`, `/api/conversations`, `/api/zone-feedback`, `/api/zone-audio` returns non-2xx
   against the `home` Worker. **Test:** one POST at each. ⚠️ Do this **before** step 1 — if more than
   `zone-save` is broken, this plan's whole scope correction is wrong and it should be rewritten, not
   patched.
   ⭐ **HALF-DISCHARGED STATICALLY 2026-09-12, with no writes:** all five capture handlers contain
   **zero** git references at HEAD, so none can 503 for `zone-save`'s reason (DESIGN PASS §F, with the
   bounds). ⛔ The live POSTs are still owed for non-git failure modes and are a **gate-kit act** —
   `lab` cannot answer (no `SHARED_TOKEN`), and spending five unprovable fixture rows in `est-qa0001`
   to fake it is refused. See §F.
2. ⭐ **"Before her first save, `home` would be served Fernwood's zones."** → **Test:** `GET /api/zones`
   against `home` **today**, whose KV holds no `zones:all` key. If the response carries *"The bank"*,
   step 2 is proven necessary. **If it returns empty, I am wrong about the fallback and step 2
   downgrades** — I read the code path and did not exercise it. ~~*(Containment today is real but is
   held by the missing token, i.e. by the very thing step 1 removes — so a green result here is
   about the read path only and does not survive step 1 on its own.)*~~
   ⛔⛔ **RUN 2026-09-12 — IT RETURNED EMPTY, so the author was wrong about the fallback and step 2 HAS
   downgraded.** `qa` (cold KV, no binding, structurally identical to `home`) returns `{zones: [],
   _meta: {}}`; the frozen deployment returns 18 zones led by *"The bank"*. **The struck caveat is
   withdrawn too** — it conflates a READER of the binding with the binding itself. Full adjudication:
   DESIGN PASS §B.
3. **"Moving the gate does not change prod-frozen behaviour."** → **Test:** a `zone-save` against the
   frozen env before and after; both must produce the same two commits and the same response. Any
   difference falsifies the change, not the plan.
4. **"KV-only is not a durability downgrade."** → FALSIFIED if any *other* household-created record
   turns out to have a git backstop. **Test:** the `ghPutFile` attribution above, re-run. If a fourth
   handler appears, the argument weakens.
5. **"A zone saved out of Wi-Fi range is not lost."** → **Test:** draw a zone with the Worker
   unreachable, close the app, return to range, confirm it lands. ⛔ **This is the falsifier that
   matters most**, because the site premise guarantees the condition will occur and because
   *capture must not lie* is the one rule her surfaces are built on.
6. **"The digest failure is a guard, not a floor."** → ALREADY TESTED, HOLDS: `compose()` raises
   `FileNotFoundError` with `zones.json` absent, and core tokens without zones = **16,125** against a
   4,096 floor and a 24,000 budget — **zones is 489 of 16,614, i.e. 2.9%.** Re-run if the budget moves.
7. **"Default OFF fails in the right direction."** → **Test:** add a sixth env with no vars at all;
   `GET /api/zones` must return `{zones: []}`, not Fernwood's.

## QA

- **Gate ① `tools/release-gate.py`** — per-sha, every seat walked in Chrome, zero failed actions.
  Evidence expires when the build moves.
- **`bash tools/deploy-worker.sh`** with the Bash sandbox disabled; a deploy is done when `/health`
  says so. ⚠️ Steps 1–3 are **Worker** changes — `check-live.py` verifies `viewer.html` and says
  **nothing** about the Worker. Do not read a green `check-live` as evidence this shipped.
- **`python3 tools/check-engine-manifest.py`** — the new env var is engine config and must classify.
- **`python3 tools/check-storage-keys.py`** — if the outbox (step 5) mints a browser-storage key, it
  is rostered, or it is a key she loses at the origin move.
- **`python3 tools/check-estate-neutral.py --url <origin>`** — ⚠️ the bare form **does not scan
  `viewer.html`** (`_shipped_pages():61`), and it tests for **names only**. It would catch Fernwood's
  zone names reaching a household origin, which is exactly falsifier 2's failure — so it is real
  coverage *here*, narrowly.
- **`python3 tools/check-data-inline.py`** after anything that re-inlines `ZONES_DATA`.
- **Two-estate assertion:** run falsifier 7 against `home` **and** `bob`. A single-estate green is how
  every one of the three embedded-Fernwood-literal defects passed review.
- **Playwright flow worth saving:** *sign in at a household origin → open the map → create a named
  place with no geometry → reload → assert it persisted → assert no Fernwood zone name appears
  anywhere in the DOM.* Five assertions; covers steps 1, 2 and 6, and the last one is the ruling-Z-10
  guard.
- ⛔ **Before merging step 1, run falsifiers 1 and 2 against the live `home` env.** Both are single
  requests, both are read-only, and between them they either confirm this plan's scope or refute it.

---

## What I could not verify

1. **Nothing was executed against a deployed Worker.** Every claim about `home`'s runtime behaviour
   is read from `worker.js` and `wrangler.toml` at `c1fec39`. Falsifiers 1, 2 and 3 exist precisely
   because I could not run them from this seat.
2. **Whether `home`'s KV namespace is genuinely empty of a `zones:all` key.** I read that a fresh
   estate has no pre-cutover era (`LEGACY_BEFORE = "1970-01-01"`); I did not list the namespace.
3. **Whether `/api/grant/whoami` returns a stable username usable as `by:`.** I confirmed the
   endpoint exists and is rostered; I did not read its response shape.
4. **The frozen instance's repo identity.** `GITHUB_REPO` is a Worker secret; I read no secret. My
   claim that git-writing is confined to one env rests on the token comments in `wrangler.toml`, not
   on the secret store.
5. ⚠️ **Concurrency.** HEAD moved twice while I worked and `viewer.html` /
   `engine/viewer.template.html` are uncommitted under another live lane. **I touched neither**, and
   step 5's viewer work is explicitly marked not-this-session for that reason.

**Sources I could not reach** (per the standing instruction — these want a browser-driven fetch):
- ⛔ **Cloudflare's own KV durability/SLA page — NOT FETCHED.** My consistency claims (60-second
  propagation; unsuited to write-heavy same-key workloads; suited to read-heavy config-shaped data)
  are from search summaries of `developers.cloudflare.com/kv/concepts/how-kv-works/`, not from the
  page itself. **If KV-only durability is going to carry a household's record, read that page
  directly before the stamp.**
- ⚠️ Carried forward from `.engineering/2026-09-07-zones-v1-path.md` and still unreached: Mortensen &
  Barrett 1995 (TLS failure on the Drexel mirror; ACM paywalled), GeoPlanar 2026 (SAGE HTTP 403),
  IEEE 2001 confidence-measure (paywalled), Google Solar coverage for Pickens County (interactive map
  and GeoJSON coverage files unfetchable). **None of them bears on this plan** — they belong to the
  geometry work at step 7.
