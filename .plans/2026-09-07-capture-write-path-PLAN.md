# capture-write-path · The per-estate write path — what lets a household keep what it makes

- row: BACKLOG.md § ▶️ NEXT · the per-estate capture write path (**ROW TO ADD** — see § Row to add; the orphan flag is expected until it lands)
- objective: O3
- class: engine · must-not-diverge
- question: at a household that holds no GitHub credential and never will, what happens to the things that household creates — and which of those things is actually broken?
- seats: engineering-partner → .engineering/2026-09-07-zones-v1-path.md
         ai-advisor → waived: nothing on this path invokes a model. Capture stays deterministic and AI-free by standing doctrine; this plan moves only where a write LANDS, never what is written
         ux-expert → waived: steps 1–4 change no surface — the only user-visible difference is that a save which used to 503 now succeeds. ⛔ NOT waived for step 5, which is why the waiver is scoped: the honest-response field changes what the sync chip can say, and the chip is Mom-facing
         content-steward → OWED, not waived, at step 5 only: if the sync chip gains a new state, its words reach Mom. No copy is drafted here
         user-researcher → waived: this plan changes no journey. The journeys that depend on it are scoped at .user-research/2026-09-07-zones-plants-v1-journey.md
         practice-steward → waived: this is a product defect, not a loop
- depends-on: .plans/2026-09-06-maps-and-zones-PROPOSAL.md
- stage: concept
- stage-note: 2026-09-07 — written in the design lane of release lap 3. NOTHING SHIPPED. No code was written and no tracked file outside this one was edited.

> ⚠️ **THE `ready:` LINE IS DELIBERATELY ABSENT AND MUST STAY ABSENT UNTIL PAUL STAMPS IT.**
> `check-backlog-ready.py` will flag *"stage `concept` with no `ready: [paul-approved …]` stamp"*.
> **That flag is correct and expected.** An agent writing its own readiness stamp is the one thing
> the gate exists to prevent. Nine plans carry this flag today; this is the tenth, honestly.

> ✅ **WIP: THIS NEEDS NO EXCEPTION AND WAITS ON NOTHING.** Measured at HEAD —
> `🚦 WIP bands: · design 1/2 · build 1/1 (+3 excepted) · concept 9 (uncapped by ruling)`.
> `WIP_BANDS` caps `design/journey` at 2 and `build/qa` at 1; **`concept` is deliberately uncapped**
> (*"a concept costs nothing to hold, and capping it pushes ideas out of the record"*). So this
> enters at `concept` freely. ⛔ **It cannot enter `build` today** — that band reads 1/1 and already
> carries three declared exceptions. **Whether it takes a fourth exception, or waits for
> `c4-environments` to leave `build`, is Paul's ruling and is not pre-empted here.**

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

⛔ **Steps 1 and 2 are ONE COMMIT.** Separating them opens a window in which a household can write
zones while still being served Fernwood's. Every other step is independently landable.

| # | step | why here | size |
|---|---|---|---|
| **1** | **Move the `GITHUB_TOKEN` gate in `handleZoneSave` from the top of the handler to around the two git commits.** Sanitize and write KV unconditionally; commit only when a token exists. | The whole defect. Everything downstream of Z-10 is blocked on it. | **XS** |
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
2. ⭐ **"Before her first save, `home` would be served Fernwood's zones."** → **Test:** `GET /api/zones`
   against `home` **today**, whose KV holds no `zones:all` key. If the response carries *"The bank"*,
   step 2 is proven necessary. **If it returns empty, I am wrong about the fallback and step 2
   downgrades** — I read the code path and did not exercise it. *(Containment today is real but is
   held by the missing token, i.e. by the very thing step 1 removes — so a green result here is
   about the read path only and does not survive step 1 on its own.)*
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
