# MOVING PAUL'S REVIEW GATE FROM PRODUCTION TO QA — the three-rung ladder, what it makes enforceable, and the three things that become unobservable · DESIGN

- row: process (no BACKLOG row — same posture as the 09-04 wiring audit and the 09-06/09-07 audits)
- objective: O5
- class: engine · declared (process machinery; nothing here ranks a feature, a module or an item)
- seats: practice-steward (this file)
        engineering-partner → owed at any build: D1 (`instance/lab.json`), D2 (`journey-logic.py`'s lab refusal), D3 (the `walked-in-qa` clause), D5 (`cleared_sha` as a deploy precondition), D6 (the parity read). **Nothing here designs a mechanism**
        ux-expert · content-steward · user-researcher · ai-advisor → waived: no surface, no copy, no person and no model sits on any path in this file
- depends-on: .plans/2026-09-07-pipeline-flex-point-AUDIT.md
- depends-on: .plans/2026-09-06-cascade-and-release-state-AUDIT.md
- depends-on: .plans/2026-09-06-conversion-method-DESIGN.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- kind: design

> **Method only.** Nothing here executes, nothing here is applied. Where a call turns on real-world
> context only Paul holds — his household, his risk appetite, what a defect is worth — it is named
> and declined. Every claim is graded `measured` · `inferred` · `proposed`, at HEAD `cfd41fb`.

---

## 0 · FOR PAUL — the answer, in six lines

1. **The shape is right**, and for a reason stronger than "it's tidier": it moves your gate from
   *after* the irreversible act to *before* it. That is your own ratified rule (`the gate sits on
   irreversible acts, never on work`) applied to the one loop that was violating it. §1.
2. **It is right as a SEQUENCE and incomplete as a LADDER.** `measured`: the dev rung serves a
   **different product** — `fernwood-lab.pages.dev/viewer` is 2,072,954 bytes and says "Church
   Mountain" 11 times; `fernwood-home.pages.dev/viewer` is 1,181,836 bytes and says it zero times.
   Dev cannot certify what production ships until `instance/lab.json` exists. §5, D1.
3. **The harness currently REFUSES the thing you just asked for.** `tools/journey-logic.py:88` exits
   on lab by name, and its stated reason was repaired by `pages-deploy.py` two days ago and never
   re-read. §2, D2.
4. ⛔ **The one change that makes this enforceable rather than described**: `cleared_sha` exists in
   `cycle/release/cycle-state.json` and **no tool reads it** (`grep cleared_sha tools/release-gate.py
   tools/pages-deploy.py` → zero). Your clear now precedes the deploy, so the deploy must refuse a sha
   you have not cleared. Today it checks the seats and never asks about you. §4, D5.
5. ⭐ **The class that goes dark is not the one in the brief.** It is not mainly "Paul's eyes" — it is
   that **production is the only environment built by a different code path, and nothing compares the
   two outputs.** Three sub-classes, all measured, one of them with *zero* instruments today. §3.
6. **Cheapest thing that keeps it visible: a deterministic post-deploy parity read, not a walk.** ~30
   lines, no browser, derived-not-typed. A smoke *walk* is still owed for the door — but a fresh
   synthetic's, not yours, and that one is a ruling I decline to make. §3.4.

---

## 1 · IS THE SHAPE RIGHT — yes, and here is what makes it right

Not agreement. Three structural properties the new order has and the current one does not.

### 1.1 · It puts the human gate on the irreversible act instead of behind it

`measured` — `cycle/release/CYCLE-MAP.md:43-51`, the beats as written:

| beat | who | today |
|---|---|---|
| 1 | main session | a sha is deployed to **QA** |
| 2 | seats | the synthetic loop, gate ① |
| **3** | **Paul** | **PAUL WALKS IT** |
| 4 | main session → seats | a failure re-enters beat 2 |
| **5** | **Paul** | **PAUL CLEARS IT** — "this is the release event" |

and `CYCLE-MAP.md:182`: *"Synthetics run in QA. **Paul runs production.**"*

⛔ **So beat 3 fires against an origin that is already deployed.** The production deploy is not gated
by beat 3; it *precedes* it. Beat 5 then declares "released" a thing that has been live throughout.
Your standing rule — measured in your own corpus, `~/.claude/agent-foundations/practice-steward.md`
§"the four inversions" #4 — is *the gate sits on irreversible acts, never on work.* **The release
loop is the loop that breaks it.** The new order repairs exactly that: the deploy to `home` becomes
the *consequence* of your clear rather than its precondition.

### 1.2 · It takes the iteration out of the irreversible surface

`CYCLE-MAP.md:51`: *"Beats 2→3→4→2 repeat. **There is no bound on the number of turns.**"* Under the
current wording every turn of that unbounded loop passes through production. `measured`: `home`'s
stamp reads `1e2748d`, built `2026-09-07T17:39:18`, while QA serves `fbd5072`
(`cycle/release/cycle-state.json:candidate_sha`) — production has already been redeployed inside this
lap. **A loop that iterates through the irreversible surface spends the irreversible surface.** This
is the identical reasoning that put synthetics in QA on 2026-09-06 (`CYCLE-MAP.md:180-189`), extended
one rung up. It is not a new principle; it is the existing one, finished.

### 1.3 · It makes the certified artifact and the shipped artifact the same object

`measured` — `instance/qa.json:_meta.ruling`, `[paul-ruled 2026-09-06, R4]`: *"production ships the
full app, built from its own instance, **as the same artifact QA certified**."* And `instance/qa.json`
declares the same neutral `canon: neutral-canon` and the same `absent[]` list as `instance/home.json`
(byte-compared: identical apart from `estate`/`estateId`).

⭐ **Your walking QA is that ruling's missing human half.** Today R4 guarantees the *machine* certifies
the shipped artifact and you inspect a rebuilt copy of it. Under the new shape you inspect the
certified object itself.

### 1.4 · Where it is NOT right, stated with the same force

- **Rung 1 is a different product.** §5, D1. `measured` above.
- **Rung 2 cannot show the arrival path.** `measured`: `GET https://fernwood-qa.pages.dev/qa-build.json`
  → **302** to `fernwood-qa-pages.cloudflareaccess.com`; the same path on `home` → **200**. Your
  caveat 1 is confirmed deterministically.
  ⚠️ **But my read differs from your framing on what that means.** The Access blindness is a property
  of QA and it exists *today*, for the synthetics: `tools/journey-view.py:20-30` mints a
  `CF_Authorization` cookie before the browser ever loads the page, so **all 140 QA walks on record
  arrived pre-authorised.** `measured` — 157 transcripts under `.private/synthetic-walks/`, origins:
  qa 140 · home 14 · lab 2 · unrecorded 1. Moving you to QA does not *create* that blind spot. It
  removes the last observer standing outside it. That is a different, and worse, sentence.
  ✅ **And it has a cheap answer that is not "walk production": `lab` has no Access.** `measured`:
  `GET https://fernwood-lab.pages.dev/qa-build.json` → **200**, no redirect; corroborated by
  `handoff/handoff-onboarding-journey-testing.md:30` (*"onboarding deployed; **no Access**"*).
  **The rung that cannot show you the estate can show you the door, and vice versa.** §5.

---

## 2 · WHAT BREAKS — the file and the line where something now says a false thing

Ordered by how load-bearing the false sentence is, not by effort.

### 2.1 · ⛔ A vocabulary FORK already exists, and this ruling is its third value

This is the finding I did not expect and it outranks the rename. `measured` — three live statements
of where Paul's gate sits, in one repo:

| file:line | what it says | Paul's gate is… |
|---|---|---|
| `tools/journey-walk.py:336` | *"which origin to walk (default qa — gate 1). **lab is gate 2.**"* | **lab** |
| `tools/synthetic-identity.py:61` | *"**Gate 1 is QA and gate 2 is lab**"* | **lab** |
| `.plans/2026-09-05-process-registry-PROPOSAL.md:68` | *"cascade's gate 2: **Paul walks the build in lab**, his own profile"* | **lab** |
| `handoff/handoff-onboarding-journey-testing.md:30` | *"lab … **Paul's gate-2 grant is LIVE**"* | **lab** |
| `cycle/release/CYCLE-MAP.md:182` | *"Synthetics run in QA. **Paul runs production.**"* | **production** |
| this ruling | | **QA** |

⭐ **So the variable already holds two incompatible values and the change would make three.** The work
is not "apply a rename"; it is **close a fork**, and the corpus's own most-repeated failure is that a
claim living in two places gets changed in one — `CYCLE-MAP.md:216`, *"the same failure the audit
found eight times over."*

### 2.2 · The map's own sentences

| file:line | text | state under the new shape |
|---|---|---|
| `cycle/release/CYCLE-MAP.md:45` | beat 1 exit: *"a sha is deployed to **QA** and `qa-build.json` reports it"* | ⚠️ **now the SECOND rung.** Beat 1 becomes "deployed to dev"; a new beat carries the promotion to QA |
| `CYCLE-MAP.md:47` | beat 3 *"PAUL WALKS IT"* | 🟡 unchanged in words, **changed in referent** — and the referent is nowhere in the row |
| `CYCLE-MAP.md:49` | beat 5 *"PAUL CLEARS IT — this is the release event. Nothing is released before it"* | ⭐ **becomes TRUE for the first time.** Today it is false: the build is live at `home` before beat 5. §1.1 |
| `CYCLE-MAP.md:182` | *"Paul runs production"* | ⛔ **false on the ruling.** The two reasons below it (:184-189) argue only against *synthetics in production* and survive intact |
| `CYCLE-MAP.md:167` | *"**Every walk on record uses `--fresh`**, so the RETURNING journey has never been walked by anyone"* | ⛔ **already false, independent of this change.** `measured`: **8 of 157** transcripts carry `fresh: false` — 7 at `qa`, listed below, plus one older run whose `origin` field predates the field entirely — mom `2026-09-05T190326`, `2026-09-07T094426`; owner `2026-09-05T180909`, `2026-09-06T135556`, `2026-09-07T094657`; strict `2026-09-07T094936`; wide-eyed `2026-09-07T095158`. ⚠️ **Reported, not resolved**: all seven carry `signedInAs: null` while every fresh walk carries an id, so whether a returning walk *establishes* a session is a question for engineering-partner, not a sentence for me to rewrite |

### 2.3 · The tools that hardcode the old ladder

| file:line | what it does | breaks how |
|---|---|---|
| ⛔ `tools/journey-logic.py:88` | `if "lab" in QA_ORIGIN: raise SystemExit("never lab — gate 1 runs on QA")` | **the harness refuses the dev rung by name.** Its reason #2 (`:78-82`) — *"Lab is deployed by hand, qa-build.json is never a tracked file, so lab's stamp is whatever some earlier CI run left behind"* — is `measured` **stale**: lab's live stamp reads `"builtBy": "tools/pages-deploy.py"`, `"builtAt": "2026-09-05T22:39:17"`. `pages-deploy.py:14-20` was written to fix exactly this and the refusal never re-read it |
| `tools/journey-logic.py:45` | `QA_ORIGIN = "https://fernwood-qa.pages.dev"` | a constant, no flag. Dev cannot be targeted at all |
| ⛔ `tools/release-gate.py` `judge()` (`:88-190`) | scores `at-sha` · `watched` · `countable` · `no-failed-actions` · `not-rate-limited` | **never reads `origin`**, though `journey-walk.py:405` writes it into every transcript. `grep -n origin tools/release-gate.py` returns only 429-attribution lines. Harmless today (140 of 157 walks are qa); **fatal under a ladder where dev walks are the norm** — a dev walk and a QA walk become indistinguishable to the gate that `pages-deploy.py:280` consults before a production deploy |
| `tools/release-state.py:170` | `served = jw.served_sha("qa")` — the candidate is what QA serves | ✅ **stays correct and gets MORE correct.** Under the new shape "what QA serves" is precisely what awaits your gate |
| `tools/qa-behind.py:19` | `env = sys.argv[1] if len(sys.argv) > 1 else "qa"`; the hook (`.git/hooks/post-commit`) passes `qa` | ✅ **the nag is right; do not touch it.** See §4·caveat 5 |
| `tools/check-cycle-map.py:35` | `MAP = ROOT/"MOM-CYCLE-MAP.md"` | ⚠️ **the release map has no drift control.** This rename touches five files; nothing checks that it reached all five |
| `tools/check-loop-docs.py:56-60` | `SURFACES = [CLAUDE.md, MOM-CYCLE-MAP.md, skills/mom-cycle/SKILL.md]` | same gap, other instrument. Both are mom-cycle-scoped |

---

## 3 · ⭐ THE GAP — my independent read

**Not "Paul's eyes stop looking at production."** That framing makes it a coverage problem, and
coverage problems are solved by looking more. This is a **construction** problem.

> ### `home` is the only environment whose artifact is BUILT BY A DIFFERENT CODE PATH, and no instrument compares the two outputs.

`measured` — `tools/pages-deploy.py:66`: `HOUSEHOLD = {"bob", "paul", "home"}`. Everything at
`:151-238` — the allow-list prune, the tombstoning, the `index.html` rewrite, the neutrality
falsifier — runs **only for that set**. `qa` and `lab` take none of it. So the artifact you certify
and the artifact you ship are produced by two different branches of one script, deliberately, for
reasons that are each correct on their own.

Three sub-classes follow. Each is invisible in QA *by construction*, not by accident.

### 3.1 · The file set — and a tombstone answers 200, not 404

`measured`, live against the production origin just now:

```
GET https://fernwood-home.pages.dev/questions.json        → 200  {"tombstone":true,"note":"This path is not part of this home…
GET https://fernwood-home.pages.dev/zones.json            → 200  {"tombstone":true,…
GET https://fernwood-home.pages.dev/weather-history.json  → 200  {"tombstone":true,…
GET https://fernwood-home.pages.dev/plants.json           → 200  {"tombstone":true,…
```

QA serves the real files at all four paths (`pages-deploy.py:151`, prune is `HOUSEHOLD`-only —
`measured` by code, not by fetch, because Access blocks the fetch).

⛔ **And the production build's own JavaScript fetches four of them at runtime.** `measured` in the
bytes `fernwood-home.pages.dev` is serving right now: `questions.json` at **:13302**, `zones.json` at
**:14063**, `./weather-history.json` at **:20223**, `./weather-bias.json` at **:20241**.

**Why nothing has broken yet, and why that is not reassurance.** All four guard on *shape* —
`Array.isArray(data && data.questions)` (:13305), `Array.isArray(cloud.zones)` (:14066),
`Array.isArray(data.days)` (:20226), `data.headline` (:20245) — so a tombstone degrades calmly. But
each of them also carries `if (!res.ok) return;` **and that line can never fire in production**,
because a tombstone is a 200. The safety is four guards written by four hands, not an environment
invariant. This is `[[reference_match_payload_not_container]]` at the scale of an entire origin: *the
wrapper check returns a plausible answer, never an error.*

**Current observers of this class: two.** `pages-deploy.py:291` loads the pruned export headless and
refuses on `PAGEERROR` — it catches a *thrown* error, and a guarded 200 does not throw. And you,
walking production. **Remove you and it has one, and that one cannot see it.**

### 3.2 · The Worker — the sub-class with ZERO instruments

`measured`, all three `/health` endpoints, live:

```
fernwood      → {"ok":true,"env":"production","estateId":"est-3c9f1a","legacyBefore":"2026-09-04",…}
fernwood-qa   → {"ok":true,"env":"qa","estateId":"est-qa0001","chat_budget":{"ceiling_usd":3,…}}
fernwood-home → {"ok":true,"env":"home","estateId":"est-e6696a","chat_budget":{"ceiling_usd":10,…}}
```

⛔ **No build identifier of any kind.** Not a sha, not a version, not a timestamp. So **no instrument
in this repo can say whether the `home` Worker runs the same code as the `qa` Worker.** And they are
deployed by different mechanisms: `.github/workflows/deploy-worker-qa.yml` fires on push to
`staging`; `home` is a hand-run `wrangler deploy --env home`.

⭐ **Gate ① is per-sha for the PAGE and blind to the WORKER entirely.** `release-gate.py`'s five
clauses all read a walk transcript; none reads a Worker. Under the current shape your production walk
exercised the production Worker *by use* — the only coverage it had. Under the new shape that is
gone, and `[[reference_anthropic_identity_linked_keys]]` is the precedent: prod Guru died with **no
code change**, and the ruling from it was *verify by USE*.

⚠️ Config also differs where the config is the behaviour: `CHAT_DAILY_BUDGET_USD` 3.00 (qa) vs 10.00
(home), `FAMILY_HOSTS` per env, `LEGACY_BEFORE` `2026-09-03` vs `1970-01-01`, `AMBIENT_MAC` a per-env
secret. A defect that is a *missing var in home* is unreachable from QA by construction.

### 3.3 · The estate, and the direction is inverted from the usual worry

Your caveat 2 is right and the shape of it is the opposite of what "synthetic data" suggests.
`measured`: `worker/wrangler.toml` binds **one** estate per environment — `est-qa0001` for qa,
`est-e6696a` for home — and 140 walks have signed up into `est-qa0001`, against 1 real account at
`est-e6696a`. `inferred` (I did not enumerate KV): **QA is the crowded estate and production is the
sparse one.** So walking QA over-exposes you to populated states and under-exposes you to empty ones —
first-run, nothing-here-yet, the single-household case. That is the state your *next* household starts
in, and QA is the worst rung to see it from.

⚠️ **Your caveat 3 does not weaken any of this — it tells you what to compare.** Everything in §3.1–3.3
is in the deterministic substrate: bytes, HTTP status, env vars, estate ids. That is precisely what
`[[feedback_ai_output_breaks_environment_parity]]` says to diff.

### 3.4 · ⭐ The cheapest thing that keeps it visible

**Honest answer, in two parts, because one instrument cannot cover both.**

**(a) A deterministic post-deploy parity read — this is the cheap half and it covers §3.1 and §3.2.**
`proposed`: `tools/env-parity.py`, ~30 lines, no browser, called from `pages-deploy.py` after a
`home` deploy the way `check-estate-neutral` is called before one (`pages-deploy.py:240-262` is the
model — *a check wired into the act it guards cannot be forgotten*).

1. `home/qa-build.json.sha == qa/qa-build.json.sha` → **the artifact you certified is the artifact
   that shipped.** One line, and it is the whole R4 ruling made checkable.
2. For every path the **built** viewer fetches at runtime — **derived by regex from the built bytes,
   never a typed list** (your rule; `release-gate.py:80` names the four times a typed roster bit this
   repo) — `GET` it on the production origin and refuse on `{"tombstone":true}`.
3. `GET <home worker>/health` → assert `env`, `estateId`; and once a build stamp exists there, the
   sha. **Adding that stamp is a one-line engineering change and it is the highest-value line in this
   document**, because it converts §3.2 from *uninstrumented* to *checkable*.
4. Print a **coverage line, counted and never graded** (`release-gate.py:250-258` is the model)
   naming what it did not reach: everything behind the sign-in door.

**FALSIFIER, stated because a recommendation without one is an opinion:** *if this runs at three
consecutive production deploys and never once differs from the QA read, it is measuring nothing and
should be deleted rather than kept green.* And the inverse tell — if step 2 ever fires, §3.1 was live,
not latent.

**(b) A short smoke WALK after deploy — yes, that is the honest answer for the door.** §3.1's read
cannot see the app behind sign-in, and §1.4 established that QA's door is not production's door.

⛔ **But it should not be yours, and whose it is, is your ruling and not mine.** The structural facts
you would rule on, and nothing further:
- `CYCLE-MAP.md:184-189` forbids synthetics in production for **two** stated reasons, and both are
  about a **durable** persona: it "joins his home as a member" and becomes "a permanent member of
  Paul's household with no removal path."
- `CYCLE-MAP.md:154-165` — your own two-classes ruling — already defines the object those reasons do
  not reach: a **FRESH WALKER**, "brand-new, spawned to walk signup once," which "does not endure, and
  that is fine," whose account may vanish while its evidence is retained.
- `measured`: **14 walks already ran at `home`** — owner/mom/wide-eyed/strict, `2026-09-05T214301`
  through `2026-09-06T181454`, all `fresh: true`. None since the 09-06 ruling. So the act is
  demonstrated, and the ruling that stopped it postdates it.
- `tools/reset-production-estate.py` "aborts entirely once any real record exists, by design"
  (`CYCLE-MAP.md:188`) — so the cleanup path for a production walker is **not** established.

**That is the whole of what I can say.** Whether a disposable walker may touch your mother's future
household is a judgment about your family and your data, and it is yours.

### 3.5 · The one thing I am NOT claiming

I am not claiming production defects will now go unfound. Mom is still gate 3 on `home`
(`[[feedback_release_cascade_persona_paul_mom]]`), and a real user is a real observer. I am claiming
something narrower and checkable: **three classes of divergence are unobservable by any instrument
that exists, and the observer being removed is the only one who covered them.** Falsifier: build §3.4a,
and if it never fires, I was wrong about the risk and right about nothing but the instrument's cost.

---

## 4 · WHAT MUST CHANGE BEFORE THIS RUNS — ordered by dependency

Each row names the file. **Nothing here is applied.** D1–D3 are preconditions of the dev rung; D4–D5
are preconditions of the ruling being enforceable at all; D6–D8 are what stops it rotting.

| # | change | file | why it is where it is in the order |
|---|---|---|---|
| **D0** | ⭐ **rule the fork** — one value for *where Paul's gate sits* | `cycle/release/CYCLE-MAP.md:182` is the register; §2.1 lists the four other sentences | Nothing below can be applied consistently while the variable holds three values. **Yours, and it is one word** |
| **D1** | `instance/lab.json` | new file; consumed at `tools/pages-deploy.py:223` | Without it `lab` keeps the **tracked Fernwood** viewer (`:232` refuses only for households). `measured`: lab 2,072,954 B / 11 "Church Mountain"; home 1,181,836 B / 0. **Dev cannot certify what production ships.** → engineering-partner |
| **D2** | lift or parameterise the lab refusal | `tools/journey-logic.py:88`, constant at `:45` | The harness exits on lab **by name**. Reason #2 (`:78-82`) is `measured` stale — lab's stamp says `builtBy: tools/pages-deploy.py`. ⚠️ Reason #1 (lab is not the gate-1 estate) is **not** stale and is a real question about which estate certifies |
| **D3** | a `walked-in-qa` clause on gate ① | `tools/release-gate.py` `judge()` `:88-190`; the field is already written at `tools/journey-walk.py:405` | Once dev walks are normal, **the gate cannot tell a dev walk from a QA walk** — and `pages-deploy.py:280` consults it before a production deploy. One clause, read from a field that already exists |
| **D4** | apply the rename to all five surfaces | `CYCLE-MAP.md:45,47,182` · `journey-walk.py:336` · `synthetic-identity.py:61` · `handoff/handoff-onboarding-journey-testing.md:30` | Do it after D0, in one commit, or this repo's eight-times failure happens a ninth |
| **D5** | ⛔ **`cleared_sha` gates the `home` deploy** | `tools/pages-deploy.py:280` (add beside the gate ① call); value already at `cycle/release/cycle-state.json:last_lap.cleared_sha` | **The change that makes the ruling real.** The human gate now precedes the irreversible act, so the act must refuse without it. `grep cleared_sha tools/release-gate.py tools/pages-deploy.py` → **zero**. Today `home` would happily ship a sha you never saw |
| **D6** | the parity read | new `tools/env-parity.py`, called from `pages-deploy.py` after the `home` deploy | §3.4a. Depends on D5 only in that it is pointless before the ladder is enforced |
| **D7** | a build stamp on the Worker's `/health` | `worker/worker.js` health handler | `measured`: no build identifier in any of the three envs. Converts §3.2 from uninstrumented to checkable. One line; **the best value-per-line in this document** |
| **D8** | a map-drift control for the release map | `tools/check-cycle-map.py:35` is hardcoded to `MOM-CYCLE-MAP.md`; `tools/check-loop-docs.py:56-60` covers three mom-cycle surfaces | ⚠️ **The release map has none, and the map's own conformance table read false for four rows across two laps while a commit edited that very file** (`CYCLE-MAP.md:213-216`). A hand-applied five-file rename with no control is the same bet, taken again |

### Your six caveats, each answered

1. **Access.** ✅ Confirmed `measured` (qa 302 → cloudflareaccess.com; home 200). ⚠️ **But it is not
   created by this change** — all 140 QA walks already arrive pre-authorised via
   `journey-view.py:20-30`. And **`lab` has no Access**, so the door is walkable one rung down. §1.4.
2. **Different estate, different data.** ✅ Confirmed, **direction inverted**: QA is the crowded estate
   (140 walk signups into `est-qa0001`), production the sparse one (1 account at `est-e6696a`). You
   would lose sight of the empty-household case, which is the case every future household starts in. §3.3.
3. **Parity broken on generative surfaces.** ✅ True and **not binding here** — every divergence I
   measured is in the deterministic substrate, which is exactly what that ruling says to diff. §3.3.
4. **The cascade and Mom as gate 3.** `inferred`: it does not change what gate 3 *means*, but it
   **makes the cascade cross an environment boundary between gate 2 and gate 3**, where today both
   meet the same origin. Nothing spans that boundary. That is what D6 is for; whether the residual is
   acceptable is yours.
5. **The `qa-behind` nag.** ✅ **It is right under the new shape and should not be touched.**
   `measured`: `qa-behind.py:19` takes an env and defaults to `qa`; `.git/hooks/post-commit` passes
   `qa` explicitly — so **nothing nags `home` today** and nothing will. QA-behind-HEAD remains beat 1's
   re-entry trigger, unchanged. ⚠️ **The new risk is the mirror of the one you asked about**: nothing
   says when `home` is behind a sha you have **cleared**. That is a missing signal, not a wrong one — D5.
6. **Does the clear travel with the sha?** Three-part answer, and only the first part is sound.
   - ✅ **The seat evidence travels correctly.** `release-gate.py` is per-sha (`at-sha`,
     `:107-113`), and `pages-deploy.py:280` **re-runs it at the home deploy** rather than trusting an
     earlier verdict. Sound.
   - ✅ **One thing genuinely is re-verified at home**: `pages-deploy.py:291` loads the
     *production-built, pruned* export headless and refuses on any page error — so the artifact that
     differs is the artifact that is loaded. Partial cover for §3.1, thrown-errors-only.
   - ⛔ **Your clear does not travel, because nothing carries it.** `cleared_sha` is written
     (`release-state.py --cleared`) and read by no gate. **Unsound, and it is D5.**

---

## 5 · DOES THE DEV RUNG NEED ANYTHING BUILT

**`lab` is the right place and is not yet the rung.** Four things, all `measured`, three of them cheap.

| | state | evidence |
|---|---|---|
| an isolated estate | ✅ **yes** | `worker/wrangler.toml` `[env.lab]` → `ESTATE_ID = "est-lab0001"`, its own KV namespace `1e0bd883…`. Corrected from prod's id on 09-05 |
| a build stamp | ✅ **yes, and this repairs the stated reason it was refused** | `GET fernwood-lab.pages.dev/qa-build.json` → 200, `"builtBy": "tools/pages-deploy.py"` |
| ⛔ the same app production ships | **NO** | lab serves the **tracked Fernwood** viewer — 2,072,954 B, "Church Mountain" ×11 — because `instance/lab.json` does not exist and `pages-deploy.py:223-232` keeps the tracked file for a non-household without one. **D1** |
| ⛔ reachable by the harness | **NO** | `journey-logic.py:88` refuses lab by name. **D2** |
| a staleness signal | **NO** | lab's stamp reads `2026-09-05T22:39:17` / `9ef14d1` — **two days old**, and `qa-behind.py` is only ever invoked with `qa`. "Run in dev until it clears" would run against a two-day-old build with nothing saying so. **One argument to one hook line** |

⭐ **And one asset nobody has named: `lab` has no Cloudflare Access.** `measured` above, corroborated at
`handoff/handoff-onboarding-journey-testing.md:30`. So the two lower rungs have **complementary**
blindnesses, and that is a better ladder than three copies of one:

| | `lab` (dev) | `qa` | `home` (production) |
|---|---|---|---|
| unauthenticated arrival / the door | ✅ **walkable** | ⛔ behind Access | ✅ walkable |
| its own estate | ✅ est-lab0001 | ✅ est-qa0001 | ✅ est-e6696a |
| the production artifact | ⛔ **no — D1** | ✅ same neutral build | ✅ |
| pruned + tombstoned like production | ⛔ no | ⛔ no | ✅ **only here** |
| CI-maintained | no | worker only | no |

`proposed`, and it is one sentence: **walk the door at dev, walk the estate at QA, and let a
deterministic read cover what only production can be.**

---

## 6 · WHAT I DECLINED TO DECIDE

Per the charter, named rather than quietly resolved.

1. **Whether a fresh synthetic walker may walk `home`.** §3.4b. A judgment about your household.
2. **Which estate should certify a release** — `journey-logic.py`'s reason #1 is a real question, not
   a stale one, and it is upstream of D2.
3. **Whether the returning-walk defect (`signedInAs: null` on all 7) is a harness gap or a product
   defect.** Reported at §2.2; → engineering-partner.
4. **Whether the release loop should be its own row on the portfolio board or fold into Fernwood's** —
   `CYCLE-LOG.md` lap 3, beat 0 step 4, already on the record as yours and still open. It is the reason
   this loop's gate sweep read UNCHECKABLE, and D8 does not fix it.
