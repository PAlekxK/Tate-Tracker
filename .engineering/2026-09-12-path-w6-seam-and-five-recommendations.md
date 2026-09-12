# PATH EVALUATION · the W6 seam, four open rows, and how engine work gets tested

- role: **engineering-partner**, mode path-evaluation. Asked for **a pick on each, not options** — plus,
  mid-flight, **how each one is tested**, and a structural answer on the four-field contract.
- repo state: read at HEAD **`82398261`** (`backlog: W6 RULED — everything is specific to the instance`).
  Every citation below was re-read at that sha.
- ⛔ **NO CODE WRITTEN, NO `BACKLOG.md` EDIT, NO DEPLOY, NO REQUEST TO ANY DEPLOYMENT.** Read-only
  instruments (`check-canon-scope.py`, `publish-digest.py --check`) plus greps, `git log`, and local
  JSON measurement.
- ⛔ **PUBLICATION CONSTRAINT.** `.engineering/` is tracked, `origin` is public. **No place string,
  address, coordinate or credential appears below.** Two findings need them; they are named by symbol
  and **routed to `fernwood-private`**, marked ⚑.

---

# THE TEST VOCABULARY I USE BELOW — three tiers, and one of them is not a test

Paul's mid-flight ask is the right one and the repo is better equipped for it than the brief implies.

| tier | definition | this repo's existing exemplars |
|---|---|---|
| **WALK** | a seat, a screen, a sha. Needs a person or a persona | `journey-walk.py` · `qa-walk.py` · `walk-fixtures.py` · `release-gate.py` gate ① |
| **CHECK** | deterministic, runnable at any sha, exits 0/1, **and can prove it can fail** (`--selftest`) | `check-household-isolation.py` · `check-storage-keys.py` · `check-digest-fresh.py` · `check-data-inline.py` · `check-canon-scope.py` |
| **PROBE** | a CHECK that must touch a live deployment, with a **positive AND a negative control** | `qa-write-probe.py` (refuses before writing unless `/health` says `qa`/`qa`) · `falsifier-tenancy.py` (`--setup`/`--teardown` fixtures at `dev`) |
| **PROOF** | a property argued from code | ⚠️ **NOT A TEST.** Every time I use this word below I say so on its own line |

⭐ **The parenthetical in Paul's question — *"some of it is not user facing that I can walk through"* —
is answered by CHECK and PROBE, and this repo already invented both tiers.** The gap is not that engine
work is untestable; it is that **`release-gate.py` certifies only the WALK tier**, so a check that exists
and is green is not visible to the thing that says a lap is done. That is the structural finding, and
§⑥ turns it into a recommendation.

⛔ **Standing discipline applied to everything below, from this repo's own audit** (24% of falsifiers
naming an instrument name one that cannot be run; two named tools that never existed): **every tool I
name below was verified to exist by `ls` at `82398261`, or is explicitly marked ⬜ NEW with a size.**

Verified present: `walk-fixtures.py` · `journey-walk.py` · `release-gate.py` · `guru-probe.py` ·
`check-household-isolation.py` · `falsifier-tenancy.py` · `qa-write-probe.py` · `check-estate-neutral.py` ·
`read-glance-order.py` · `check-telemetry.py` · `post-deploy.py` · `pages-deploy.py` · `reinline.py` ·
`check-digest-fresh.py` · `check-data-inline.py` · `check-storage-keys.py` · `publish-digest.py` ·
`build-digest.py` · `check-canon-scope.py`.
⛔ **Verified ABSENT: `tools/deploy-worker.py`.** There is no Worker-deploy wrapper at all. That single
fact decides §③.

---

# ① ⭐⭐ THE W6 SEAM — where care knowledge lives

## What I measured, before recommending anything

`plants.json` at `82398261`:

| measurement | value |
|---|---|
| plant records | **40** ⚠️ *(the brief says 26. **26** is the count carrying a `bloom` field. Worth correcting at source — a number with the wrong predicate is how row 86 got 108.)* |
| records carrying at least one place literal | **31 of 40** |
| total place-literal occurrences | **261** |
| by field | `care` **87** · `soilNotes` **77** · `frostSensitivity` **38** · `currentSeasonNote` **27** · `aspectPreference` **16** · `guide` **10** |
| inside `care`, by subfield | `description` **72** · `peakWindow` **14** |
| care entries | **234**, across 7 actions (prune · propagate · fertilize · water · repot · inspect · mow) |
| care entries carrying `peakDates` | **234 of 234** — every one |

## ⛔⛔ THE FINDING THAT DECIDES IT: THE "SPECIES RECORD" IS ALREADY AN INSTANCE RECORD

⭐ **`care` — the exact field option (a) would share — is the MOST contaminated field in the file.** Its
windows are not species facts with a place annotation; they are `peakDates` computed for one elevation
and one frost calendar. All 234 of them.

⛔ **So option (a) is not a pointer away. There is nothing to point at.** `instance/neutral-canon/` holds
exactly two files (`estate.json`, `property.json`). **No species reference library exists anywhere in
this repo.** Building (a) means de-placing 261 literals across 6 fields in 40 plant records — then
repeating for birds · mammals · insects · snakes · amphibians · lizards · fishing · weeds · turf ·
vehicles. **That is an authoring project, not a migration.**

⭐⭐ **And the second-order problem is worse than the cost.** A *correctly* de-placed shared record for
"prune azalea" says **"after flowering."** That is general gardening knowledge — which this product
forbids by name: the `CORE_SUBSTRATE_NOTE` instructs the model *"never fill the gap from general
knowledge,"* and the depth filter's whole job is refusing exactly that sentence. **A shared reference
library, done right, converges on the thing the Guru exists not to say.**

## ⭐ RECOMMENDATION — (b), and specifically **DERIVED per instance, not COPIED per instance**

**Pick: every household's care knowledge is its own record, PRODUCED BY A DERIVATION, not copied.**

The genuinely shareable layer is **not a record library** — it is a small, honestly place-free **species
parameter table**: phenology anchor (prune relative to *flowering*, not to a date), a bloom-offset model
per unit elevation, a frost-sensitivity class, a soil-pH tolerance range. Then a per-estate derivation
turns that into **that household's own `peakDates`** using facts the code **already derives per estate** —
`factsFor()` returns elevation, frost dates, hardiness zone and region for whatever digest `canonFor`
hands it, and does so today at `home`, `paul` and `dev`.

⭐ **Why this is the pick and not a compromise:**

1. **It satisfies W6 literally.** The output is a per-instance record. Two households with the same
   species hold two different records, because their windows genuinely differ.
2. **It is the only shape whose shared layer contains no place.** The parameter table has no prose, so
   the leak class row 15 measured cannot travel through it.
3. **It matches the accretive-corpus thesis**: generic knowledge held *against* ground truth. The
   parameters are generic; the answer is the place's.
4. ⭐ **Fernwood's existing 40 records become the ANSWER KEY, not the seed** — the same move Z-13 already
   made with the cleaned 23. You have 234 hand-authored windows for one known elevation and frost
   calendar; that is a validation set most products would not have.
5. **It is the only option that gets cheaper as households are added.** (a) pays authoring once and
   correctness never; (b)-as-copy pays authoring per household forever.

**⛔ What would change my mind** — stated so this is falsifiable and not a preference:
- ⭐ **If ai-advisor's half finds no sourceable per-species phenology parameters**, the derivation has no
  input and the pick collapses to (b)-as-copy-at-add-time. **In that case one thing is mandatory:**
  a copied `peakDates` must be marked **inherited, not derived**, on its own face — an unmarked copy is a
  model-read value promoted to canon, which is the rule this repo breaks most often.
- **If Paul wants households to learn from each other's observations**, that is a *different* feature
  (cross-estate learning) with its own consent ruling, and it does not argue for (a) — a shared
  *authored* library and a shared *observed* corpus are unrelated problems.

## What breaks — named, with the honest severity

| thing | what actually happens | severity |
|---|---|---|
| `check-data-inline.py` | ⚠️ **Not broken — its PREMISE becomes inapplicable.** It compares `plants.json` ↔ `PLANTS_DATA` inlined in `viewer.html`. That is one repo file against one viewer. For every household but Fernwood, the source moves to the estate's store and this check covers nothing while still exiting 0 | ⛔ **important** — a green check covering nothing is the class already flagged in `sanitizeZone`'s own comment |
| `build-digest.py` | ✅ **Mostly fine.** `digest_plants()` reads through the canon chain, which already handles the young-estate case (neutral-canon → materialised empty, R5). Per-instance records fit unchanged **if the store stays file-shaped**. If 1b's store is KV, `build-digest` needs a KV source — **that is the real new code** | important |
| `publish-digest.py` | ⚠️ Shape unaffected; **role changes.** Today it is the *only* writer of `<estateId>:digest` and runs by hand. Under 1b, an in-product write must recompose or invalidate. This is 1b's actual integration point | important |
| `check-digest-fresh.py` | ⚠️ Rebuild-and-diff against `worker/digest.json` — **one estate's artifact.** Per-estate it becomes N diffs and needs `--estate`. ⛔ Without that it silently keeps guarding only Fernwood | important |
| digest size / prompt cost | ✅ **Not a problem, and the fear is misplaced.** `worker/digest.json` is **611,710 bytes**, of which `plants` is **233,699 (36.7%)** — but the digest does **not** go into the system prompt. `factsFor()` extracts a small object, `core` (28,409 B, 4.5%) is the names-only substrate, and the record is reached by **tools**. Per-instance records are *smaller* per household, not bigger (a new household holds 3 plants, not 40). KV's value ceiling is far above this | ✅ non-issue — **stated so it is not re-raised** |

## ⭐ HOW ① IS TESTED

| | |
|---|---|
| **tier** | **CHECK**, plus one **PROBE** |
| **the check** | ⬜ **NEW: `tools/check-species-placeless.py`** — size **S**. Asserts: every record in the *shared* layer scores **0** against `check-estate-neutral.py`'s 311-needle list **and** 0 against `check-canon-scope.py`'s *every-other-estate's-own-place* reading. `--selftest` plants a literal and must FAIL |
| ⛔ **what it does NOT cover, on its own face** | **Semantic place-dependence.** A `peakDates` window derived for one elevation carries **no literal** and is still wrong everywhere else. This check cannot see that, and **must say so in its own docstring** — otherwise it becomes the seventh unrunnable-or-hollow falsifier |
| **the probe** | ⬜ **`guru-probe.py --env`** — size **S** (the tool exists and grades answers well; it is hard-refused unless `/health` says `qa`). Adding `--env` plus a per-estate expectation set is the cheap half and is currently unfiled |
| **the FALSIFIER** | ⭐ **A household at a different elevation, asked when to prune its azaleas, is given Fernwood's window** — or is given "after flowering" with no date at all. **Both are failures, in opposite directions**, and that is what makes it a good falsifier: (a) fails one way, (b)-as-copy fails the other |
| **who runs it, when** | `check-species-placeless` at **every build commit that touches a canon file** (it is cheap and deterministic — same cadence as `check-data-inline`). `guru-probe --env` at a **deploy**, per estate |

---

# ② R1 — what the ratification actually has to say

The coordinator has already edited the chain. ⭐ **My concern was never the edit; it was that a lane six
weeks from now re-derives the gate from a row.** So the ratification needs five clauses, and it is the
fifth that does the work:

1. **The claim, dated and measured.** *"Layer 2 depends on 1a (the per-estate canon READ store), which is
   SHIPPED. It does not depend on 1b (the canon WRITE path)."* With the measurement: `canonFor` reads
   `keyFor(scope,"digest")` via `scopeFor` at `worker.js:4877`; `check-canon-scope.py` 2026-09-12.
2. **What comes off the gate, by row.** TIER 2 · **15** and **20**. ⛔ **Row 16 was never gated** (a
   standing epic). ⛔ **Row 12 does not move** — it *is* 1b's row.
3. ⛔ **What does NOT come off, and this is the clause most likely to be missed.**
   `handlePromoteSpecies` is **both** a layer-2 guard site *and* the layer-3 write. Row 15's work on the
   `SCHEMA_DRAFTER_SYSTEM` prompt is layer 2 and is released; **the promotion it drafts for is layer 3
   and is not.** A lane that reads "row 15 is unblocked" and ships promotion has violated the chain
   while obeying the ratification.
4. ⭐ **SCOPED, not global.** 1a is "shipped" only *where a digest is published*. **`qa` is DARK right
   now.** So the clause is *"layer 2 is reachable at the estates where 1a is live,"* and the list is a
   measurement, not a constant.
5. ⭐⭐ **A RUNNABLE falsifier, which the chain's current one is not.** *"If `configured.canon` reads
   true at a household and a layer-2 item still cannot ship, layer 2's gate was never layer 1."*

## ⛔ What moves with it — and the honest answer is: operationally, nothing yet

Two couplings Paul should hear before ratifying, because ratifying without them is a paper win:

- **R1's falsifier depends on `configured.canon`, which does not exist.** R1 and the `/health` field are
  one decision, not two. Ratify them together or R1 ships with an unrunnable falsifier — the exact
  defect my own audit measured at 24%.
- ⛔ **The design WIP band is `2/2`** (`capture-write-path` + `zones`). TIER 2 · 15 becoming *plannable*
  does not make it *plannable now*. **R1 changes what is reachable; it does not open a slot.** Paul
  either takes a `wip-exception:` or R1 is a correction to the record that changes no one's week. **Both
  are fine — but he should choose knowingly.**

## ⭐ HOW ② IS TESTED

| | |
|---|---|
| **tier** | **CHECK** — and it already half-exists |
| **the check** | `python3 tools/check-canon-scope.py` (exists, run today). It is the reader that answers *which estates have 1a live*. ⬜ **NEW, XS:** have it **exit 1 when an estate declaring model routes has no published record**, so "qa is DARK" stops being a line someone reads and becomes a failure someone gets |
| ⛔ **what it does NOT cover** | It reads the **digest** — the input. It cannot tell you whether the answer that comes back is right. That is `guru-probe.py`'s job and it is QA-only |
| **the FALSIFIER** | clause 5 above — **and it needs `configured.canon` to exist.** Stated explicitly rather than assumed |
| **who runs it, when** | at a **lap boundary** and at every **deploy** (it is already in `CLAUDE.md`'s command list; what it lacks is a caller and a non-zero exit) |

---

# ③ ROW 86 — the legacy Worker

## The fact that decides this, and it is not in the row

⛔⛔ **There is no `tools/deploy-worker.py`. There is no Worker-deploy wrapper of any kind.** Verified by
`ls` at `82398261`. `pages-deploy.py` and `post-deploy.py` exist; the Worker is deployed by a bare
`wrangler deploy`.

⭐ **That kills option (b) as stated.** *"Declare legacy permanently undeployable"* has **no mechanism to
attach to** — there is nowhere to put the refusal. Declaring it would replace protection-by-inaction with
protection-by-inaction-plus-a-sentence, and Paul's own rule already names that shape: ⛔ *a hold names the
WORK, not the mechanism; "indefinite" is abandonment with manners.*

## ⭐ RECOMMENDATION — **(a), SCOPED. Not all 55.**

**A minimal reviewed release, cut from a branch pinned at the last deployed sha (`2026-09-08T13:22:45Z`),
carrying the `ENV_NAME` stamp correction and nothing else.**

**The reasoning, and the part the three-way framing hides:**

- **(c) is strictly dominated.** The payload only grows and the trigger is an accident. Nobody should
  defend it and the row already says so.
- **(b) has no mechanism** (above), *and* it costs something real: it makes Mom unreachable by any fix,
  forever, at the deployment with **435 sessions**.
- ⛔ **But (a) taken as "deploy the 55" destroys something load-bearing: legacy is the DATA CONTROL for
  the QA-parallel ruling.** Shipping 55 commits of behaviour change — signup, founding, per-request canon
  scoping, sign-out, credential stamping — to the control **is** the experiment contaminating its own
  control group. The Fifth Lens's *"why the exception is safe — legacy exists to compare against"* stops
  being true the moment legacy runs today's code.

⭐ **So the three options were the wrong three.** The scoped release is the only one that holds all three
things at once: **the stamp gets corrected · legacy's behaviour does not change · the accident stops
being possible.**

**And build the mechanism regardless** — ⬜ **NEW: `tools/deploy-worker.py`**, size **S**. A wrapper that
(i) reads the target's last deployment timestamp, (ii) prints `git log --since=<that>` as the payload,
(iii) **refuses** when the target is `fernwood` (legacy) unless `--release-reviewed <sha>` is passed.
⭐ That is what turns "protected by inaction" into a control — and it is the same shape as
`qa-write-probe.py`'s refuse-before-step-2, which this repo already wrote once and can copy.

⛔ **Sequencing matters and is easy to get backwards: build the wrapper FIRST, then use it to perform the
scoped release.** Otherwise the first act under the new rule is the one act that bypasses it.

⚑ **Routed to `fernwood-private`:** nothing here. The `ENV_NAME` value and the sha are public-safe.

## ⭐ HOW ③ IS TESTED

| | |
|---|---|
| **tier** | **CHECK** (the wrapper) + **PROBE** (the release) — ⛔ **never a walk**; there is no screen and the act is unrepeatable |
| **the check** | `tools/deploy-worker.py --selftest` — must prove it **refuses** on the legacy target without the flag, and prints a payload it can be diffed against. The refusal is the feature; a wrapper that cannot demonstrate refusing is decoration |
| **the probe, before** | `GET <legacy>/health` → record `env` + `build_sha` + `worker_blob`. ⚠️ **Send a User-Agent** — the edge rejects UA-less `urllib` before the Worker runs |
| **the probe, after** | same three fields. ⭐ **`worker_blob` is the payload check** (H5, lap 7) — `post-deploy.py` already compares the blob, so this reuses a built instrument rather than inventing one |
| ⛔ **what it does NOT cover** | ⛔⛔ **`/health` returning `env: legacy` proves the STAMP moved. It proves nothing about Mom's app still working.** The only instrument that would is a walk at legacy, which **does not exist and should not be built for a frozen deployment.** ⭐ **This is the residual risk and it must be stated to Paul rather than engineered away** — it is the strongest argument for keeping the payload to one commit |
| **the FALSIFIER** | **`worker_blob` changes by more than the one reviewed commit's build**, or legacy's next session count drops against `read-glance-order.py`'s 435 baseline |
| **who runs it, when** | Paul, at the release. ⛔ **Not an agent's act** — the row already rules this |

---

# ④ ROW 79 — migration order, ids, namespace

## ⭐⭐ THE FINDING REFRAMES THE QUESTION: THE MIGRATION IS A RE-FOUNDING, NOT A COPY

The `<estate>:place` finding is **not upstream of the migration. It defines its shape.**

- `writeEstatePlace()` has exactly one caller: `POST /api/estate`, at founding. By ruling: *"No election,
  no hand-declaration, no backfill by a different path."*
- So the only act that produces a reproducible digest **is founding.**
- ⛔ **Therefore a migration that copies KV rows carries the unreproducible digest into production and
  makes it permanent there.** A migration that re-founds writes `<estate>:place` correctly and
  `publish-digest.py` can rebuild forever after.

⭐ **That is the whole ruling, and everything below follows from it.**

## RECOMMENDATIONS

**The ORDER: Paul's condo first. Mom second. Four reasons, and the first is Paul's own rule.**

1. ⭐ **The release cascade is persona → Paul → Mom, and Mom is gate 3, never gate 1.** A re-founding is
   an unrehearsed user journey; running it first on the person who can debug it is the cascade working.
2. **Less to lose, measured:** `read-glance-order.py` reads `paul` at **2 sessions / 1 served order**
   against `home`'s **13 / 0**.
3. **The Fifth Lens already names the condo as the working model by use.** This is what it is for.
4. ⛔ **Mom cannot be asked to found twice.** Whatever she walks must be the version that works. That is
   an argument for her going last, not for her being skipped.

**Do the estate ids survive? ⭐ Recommend NO for both — with `migratedFrom` recorded on the new row.**

- Keeping an id is what invites a KV copy, which is the shape being rejected. A new id makes the
  re-founding honest by construction.
- ⛔ **But a bare new id breaks continuity** — `read-glance-order.py`, the door records and the feedback
  log all key on the old one. **`migratedFrom: <old estateId>` on the new estate row** keeps the history
  joinable without the id being load-bearing. One field, written once, at the only moment it is knowable.
- ⭐ **And it retires TIER 1 · 88 rather than answering it.** *"Which Mom migrates"* only has to be
  answered if an id survives. If neither does, the question is: *which record does she re-found from* —
  and the Fifth Lens already ruled that (she stands it up; we help pre-fill; legacy stays the control).
  ⚠️ Flagging that as a **consequence Paul should confirm**, not as 88 being closed by inference.

**The KV namespace: a NEW one, created and its id PINNED before the env block is declared.**

- ⛔ **Row 87's finding is the constraint and it is not optional:** a `[env]` block with no KV id
  *parses, deploys, and binds nothing* — a deployment that silently has no store.
- A fresh namespace is also what keeps the two existing ones usable as **controls you can diff against**.
  Reusing one destroys the before-state on the first write.
- On the **title**: cosmetic (row 91), so match the deployment (`myhome-prod`) and stop there.

**Where the `<estate>:place` work lands in the order:** ⭐ **nowhere — it is not a work item.** It is
discharged *by* the re-founding. The only thing it adds to the plan is a **precondition on the old
deployments: do not retire `home` or `paul` until the new estate's digest has been rebuilt from its own
`:place` at least once.** Retiring first leaves you with an unreproducible artifact and no source.

## ⭐ HOW ④ IS TESTED

| | |
|---|---|
| **tier** | **CHECK** + **PROBE**, both of which **already exist** — this is the best-instrumented item of the five |
| **the checks** | `python3 tools/check-household-isolation.py` — ⭐ built **for exactly this**, `[paul-ruled 2026-09-06 R3]`: *"a boundary needs no test to be true; a prefix does."* · `python3 tools/check-storage-keys.py` — the origin move strands `tateTracker.*` keys unless the migration knows about them |
| **the probe** | `python3 tools/falsifier-tenancy.py --setup` / run / `--teardown` at `dev` — two estates in one deployment, every cross-read a 404. ⭐ **Run it BEFORE the migration, not after.** It is the rehearsal |
| **the reproducibility check** | `python3 tools/publish-digest.py --check` must read **in sync** (not *cannot build*) for the new estate. ⭐ **That single line is the whole `<estate>:place` finding, expressed as a test** |
| ⛔ **what none of them cover** | **The re-founding journey itself** — a person creating an estate through the product. That IS a walk, it has a screen, and `walk-founding.py`'s clause B + the 409 reversal are already named for it in the lap-9 readiness. ⛔ **Do not let the check tier's completeness here disguise that the user-facing half still needs a seat** |
| **the FALSIFIER** | ⭐ **Two accounts on `myhome-prod`, each having founded, where every read one makes for the other's estateId returns 404 — and a grant presented for A cannot name B by any route.** That is `falsifier-tenancy.py`'s own claim, verbatim, and it is already written down |
| **who runs it, when** | the checks at **every build commit** of the migration · `falsifier-tenancy` at `dev` **before** the first production founding · `publish-digest --check` **after each estate lands and before the old deployment is retired** |

---

# ⑤ ROW 90 — Worker naming

## ⛔⛔ I AGREE WITH COORDINATION, AND I FOUND THE REASON IT IS MORE URGENT THAN A NAMING QUESTION

`grep '^\[env\.\|^name = ' worker/wrangler.toml` at `82398261`:

```
name = "fernwood"          ← top-level
[env.qa]                   ⛔ NO `name =`   → derived: fernwood-qa
[env.dev]  name = "fernwood-lab"       ✅ pinned
[env.home]                 ⛔ NO `name =`   → derived: fernwood-home   ← MOM'S
[env.paul] name = "myhome-paul"        ✅ pinned
```

⛔⛔ **`[env.qa]` and `[env.home]` do not pin their Worker name.** Wrangler derives it from the top-level
`name`. ⭐ **So renaming the top-level Worker `fernwood` → `myhome` would silently rename `fernwood-qa`
AND `fernwood-home` at the next deploy — orphaning Mom's deployment and everything in its namespace.**

⭐ **This reframes coordination's recommendation.** *"Let top-level `fernwood` keep its name because it is
the only accurate one"* is correct — but it is **not an aesthetic preference. It is currently the only
thing standing between a tidy-up and an orphaned deployment of Mom's.** Nobody wrote that down, and the
row's warning (*"an unpinned rename orphans a deployment"*) is about the env being renamed, not about the
**two envs that would be renamed as collateral.**

## ⭐ RECOMMENDATION — split it in two, and only the first half happens now

**NOW (XS, zero risk, do it independent of any naming decision): pin `name =` explicitly in `[env.qa]`
and `[env.home]`.** Two lines. It changes no deployed name — it *freezes* the current ones. After it,
the top-level name is a normal decision instead of a trap.

**LATER: agree with coordination — `myhome-*` for qa/dev, `fernwood` keeps its name — but DEFER THE ACT
into the `myhome-prod` build-out.** The honest cost is why:

⛔ **A Worker rename is not a rename. It is a new Worker.** The old one keeps its routes, its secrets and
its namespace binding; the new one has none. Per environment that means: create · re-put every secret ·
re-bind the namespace · re-point the route · verify by use · delete the old — with a window where both
exist and only one is bound. ⭐ **Marginal inside a migration that is already creating a Worker and a
namespace. Standalone, it is pure cost for a name.**

## ⭐ HOW ⑤ IS TESTED

| | |
|---|---|
| **tier** | **PROOF** for the pinning · **PROBE** for any rename ⚠️ **and the proof is not a test — saying so** |
| **the pinning** | ⚠️ **PROOF ONLY.** `wrangler deploy --dry-run --env qa` prints the resolved Worker name. That is a **property read off a tool's output**, not an assertion anything keeps. ⬜ **Make it a CHECK, XS:** extend `check-config-derivation.py` (exists) to **fail when any `[env.*]` block lacks `name =`.** Same shape as `check-storage-keys.py`'s roster-drift guard: a hand-kept convention rots silently, and the guard is what stops it |
| **the rename probe** | `GET /health` on the NEW name must return the expected `env` **and** `kv_canary` (the canary is per-namespace, seeded with its own name — ⭐ **a mis-bound namespace shows up here as a mismatch rather than as a quiet write into the wrong estate's data**). `qa-write-probe.py` already refuses before writing unless both agree |
| ⛔ **what it does NOT cover** | ⛔ **Secrets.** `/health.configured.*` reports booleans — it will say `anthropic: true` on a renamed Worker carrying a *different* key. ⚠️ **And TIER 1 · 72 is the live proof that a present-but-incomplete binding reads as configured.** After any rename, at least one model route must be exercised by use |
| **the FALSIFIER** | **`kv_canary` on the new name does not equal the env it claims**, or `read-glance-order.py` shows an estate's session history stop at the rename |
| **who runs it, when** | the check at **every commit touching `wrangler.toml`** · the probe at the rename, by whoever performs it |

---

# ⑥ ⭐⭐ THE STRUCTURAL ANSWER — is the four-field contract wrong for engine items?

**The four fields** `[paul-ruled 2026-09-07]`: *the ask* · *the telemetry event AND its reader* · *the
ribbon line + hyperlink* · *the release note*.

## RECOMMENDATION: **the contract is not wrong. Three of four fields already transfer. ONE does not — and the fix belongs in that field's slot, not in a fifth field.**

| field | does it transfer to engine work? |
|---|---|
| **the release note** | ✅ **Yes, unchanged.** The contract already says *"for everything else"* |
| **the ribbon line** | ✅ **Yes, unchanged.** Already conditional — *"only where the item traces to feedback"* |
| **the telemetry event AND its reader** | ✅⭐ **Yes — and it is the STRONGEST clause for engine work, not the weakest.** *"An event with no reader is not instrumentation"* is precisely the engine failure mode. **`configured.canon` on `/health` IS this field, correctly filled for an engine item**: the state, plus the thing that can read it |
| **the ask** | ⛔ **No. An engine item asks nobody anything.** This is the only real gap |

⭐ **And the contract already demonstrates its own degenerate case** — TIER 1 · 23 carries
`ask: none — a process item, no person-facing surface · telemetry: none — nothing fires; the reader is
release-state.py · check: … · note: none`. **Three of four are "none," and the row is still legible.**
So the contract survives engine work today by degrading to blanks.

## ⛔ But degrading to blanks loses the thing engine work most needs a field for

**The engine analogue of an ask is: WHAT DOES THIS ITEM REQUIRE AN ENVIRONMENT OR ESTATE TO DECLARE, AND
WHAT DOES IT DO WHEN THE DECLARATION IS ABSENT?**

An ask is *what the item needs from a person before it can be correct.* For engine work the equivalent is
*what the item needs from a deployment before it can be correct.* ⭐ **And this repo has been bitten by
exactly that, three times, all measured, all within two weeks:**

- `CANON_FOREIGN_OK` still declared at two envs for a var **the code no longer reads** — a var that
  survived its feature, teaching the next reader a wrong model.
- **Row 87** — an `[env]` block with **no KV id parses, deploys, and binds nothing.**
- **The `<estate>:place` finding** — three estates hold digests that **cannot be rebuilt** because a
  record nothing declares is absent, and the failure is invisible until you run the right `--check`.

⛔ **Not one of those would have been caught by an ask, a ribbon, a telemetry event or a release note.**
All three are missing-declaration failures.

## THE PROPOSED SHAPE — one line, in the ask slot, only on engine rows

```
ask: none — engine
declares: <what the environment/estate must declare> · <the behaviour when it is absent> · <the reader that can see it>
```

⭐ **Why in the ask's slot and not as a fifth field.** A fifth field puts a permanent blank on every
person-facing row, and blank-field decay is exactly what `check-backlog-ready.py` already spends its
effort fighting. **The two never co-occur** — an item is person-facing or it is engine — so they are one
slot with two forms, not two slots.

⭐ **And the third clause (`the reader that can see it`) is the one that makes this enforceable**, because
it is the same discipline the telemetry field already carries and has already proved: *an event with no
reader is not instrumentation* → **a declaration with no reader is not a contract.**

## ⛔ THE SECOND HALF, AND IT IS THE ONE THAT PROBABLY MATTERS MORE

**`release-gate.py` certifies the WALK tier. Nothing certifies the CHECK tier.**

So a lap can close with `check-household-isolation.py` **never run** and nothing notices — the gate was
not asked. ⭐ That is why engine work *feels* untestable when it demonstrably is not: **this repo has an
excellent check tier and no gate that reads it.**

⬜ **Recommend, size S:** `release-gate.py` gains a **CHECK BATTERY** section — the list of checks a lap's
committed rows declared in their `check:` field, run at the gate, exit non-zero on any failure, and
⛔ **on any check it could not run**, which is the 24%-unrunnable-falsifier finding turned into a gate
rather than an audit.

⭐ **This is the reusable half the coordinator predicted, and I agree it outlives all five decisions.**

## ⭐ HOW ⑥ IS TESTED

| | |
|---|---|
| **tier** | **CHECK** — the contract checking itself |
| **the check** | `tools/check-backlog-ready.py` (exists) gains: **an `⚙️ engine` row whose `ask:` reads `none` must carry a `declares:` line**, and a `declares:` line must name a reader. Same family as its existing *"an engine item must name its divergence tier"* rule, which already works |
| ⛔ **what it does NOT cover** | **Whether the declaration is TRUE.** The check reads the row, not the environment. Closing that needs the environment-side reader the `declares:` line names — ⭐ **which is the point: the field exists to force one to exist** |
| **the FALSIFIER** | ⭐ **An engine item ships, its declaration is absent in some environment, and nothing reports it until a person notices a symptom.** ⛔ **That falsifier has already fired three times** (above) — so this is a rule proposed from measured failures, not from tidiness |
| **who runs it, when** | at the **build commit** (`check-backlog-ready.py` already runs there) and at the **lap gate** once `release-gate.py` reads the battery |

---

# ⑦ WHAT I COULD NOT VERIFY — stated rather than smoothed over

- ⛔ **No request was made to any deployment and nothing was POSTed.** Every environment reading came from
  local instruments over `wrangler kv`. The `qa`-is-dark conclusion remains a code + KV read: deterministic,
  one step short of *seen*. **Confirming act: one `/api/today-line` POST at `qa`, with a User-Agent.**
- ⚠️ **The phenology-parameter half of ① is ai-advisor's** and my recommendation is conditional on it.
  I have not established that per-species phenology anchors are sourceable.
- ⚠️ **I did not read `walk-founding.py`** — I cite it only as the lap-9 readiness names it.
- ⚠️ **Legacy's last-deployment timestamp** is carried from row 86's own re-measurement, not re-run here.
  ⭐ Row 86's own lesson applies to this line: **independent corroboration of a shared predicate is not
  verification.** Re-run `wrangler deployments list` before acting on ③.
- ⚠️ **Row 91 (KV namespace titles) I read only via its row header**, not its body.

---

# ⑧ THE PICKS, ON ONE PAGE

| # | recommendation | tier of its test | the tool | exists? |
|---|---|---|---|---|
| **①** | **(b) DERIVED per instance** — a place-free species *parameter* table + per-estate derivation; Fernwood's 40 records become the **answer key** | CHECK + PROBE | `check-species-placeless.py` · `guru-probe.py --env` | ⬜ NEW **S** · ⬜ `--env` **S** |
| **②** | Ratify R1 with **five clauses** — scoped to estates where 1a is live, excluding promotion, with a **runnable** falsifier. ⛔ Ratify it *together with* `configured.canon` | CHECK | `check-canon-scope.py` + a non-zero exit | ✅ · ⬜ XS |
| **③** | **(a) SCOPED** — a one-commit reviewed release from the last-deployed sha. ⛔ **Build the deploy wrapper FIRST** | CHECK + PROBE | `tools/deploy-worker.py` · `/health` `worker_blob` | ⛔ **NEW S** · ✅ |
| **④** | **Re-found, don't copy.** Paul first, Mom second · **new ids both**, `migratedFrom` recorded · **new namespace**, id pinned before the env block | CHECK + PROBE | `check-household-isolation.py` · `falsifier-tenancy.py` · `publish-digest.py --check` | ✅ ✅ ✅ |
| **⑤** | **Pin `name =` in `[env.qa]` and `[env.home]` NOW** (two lines) · agree with the `myhome-*` convention but **defer the act into the migration** | PROOF → make it a CHECK | `check-config-derivation.py` + a name-pinning rule | ✅ · ⬜ XS |
| **⑥** | Contract is **right**; the **ask field gets an engine form (`declares:`)**, not a fifth field. ⭐ And `release-gate.py` gains a **check battery** — nothing today certifies the CHECK tier | CHECK | `check-backlog-ready.py` · `release-gate.py` | ✅ · ⬜ S |

⛔ **Every one of these is flagged, not ruled. Paul decides.**
