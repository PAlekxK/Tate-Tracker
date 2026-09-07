# THE AI BOUNDARY — what is computed, what is said, and what a person confirmed

- seat: **ai-advisor** · mode: consult · date: 2026-09-06 (late evening)
- raised: `[paul-stated 2026-09-06, voice]` — *"One thing we need to determine is the differentiation
  between the generative AI non-deterministic side of it — like the content, the research that's
  cleaned up for a given plant — versus the deterministic functions and all that."*
- **scope: the AI boundary only.** Environment topology and the promotion *sequence* belong to
  engineering-partner (`.engineering/2026-09-06-environment-pipeline.md`,
  `.plans/2026-09-06-one-environment-DECISIONS.md`). Where the two touch, this file states what the
  AI half requires and hands the mechanism over.
- **writes: this file only.** No product code, no config, no `VOCABULARY.md` edit, no BACKLOG row.
- read before classifying: `CLAUDE.md` (§ AI-creep, :446), `PRODUCT-ENGINE.md`, `VOCABULARY.md`
  (§3d, §6, §7), `.plans/2026-09-06-one-environment-DECISIONS.md` (all sections),
  `worker/worker.js` (all five model call sites), `worker/wrangler.toml` (all six envs),
  `tools/{build-digest.py,deploy-worker.sh,pages-deploy.py,guru-facts.py,guru-probe.py,guru-replay.mjs}`,
  `plants.json`.
- **verified live tonight, not inferred:** `/health` on all five reachable Workers; HTTP probes on
  `fernwood-home.pages.dev` bare and cache-busted.
- external research authorised in the brief. Sources cited inline, graded at §2a.

---

## 0 · FOUR MEASUREMENTS THAT CHANGE THE QUESTION. READ THESE FIRST.

All four were read off the running system or off source tonight.

### ⭐ 0a · No generative surface is reachable on any production household origin, today.

`tools/pages-deploy.py:66` puts `home`, `bob` and `paul` in `HOUSEHOLD`, which ships a five-file
allow-list (`:67`). Grepped for API calls, those five files reach exactly:

| file | endpoints it calls |
|---|---|
| `onboarding/index.html` | `/api/account` `/api/feedback` `/api/grant` `/api/onboarding-metrics` `/api/profile` |
| `estate/index.html` | `/api/feedback` `/api/grant` `/api/onboarding-metrics` |
| `homes/index.html` | `/api/feedback` `/api/grant` |
| `settings/place/index.html` | `/api/profile` |
| `settings/account/index.html` | `/api/grant` `/api/profile` |

**Zero AI endpoints.** Every model call site in the product — Guru, today-line, classify, the
promote drafter, the sound-ID — is reached only from `viewer.html`, which the household export
deliberately excludes. Probed live: `https://fernwood-home.pages.dev/viewer.html` returns **308**,
bare *and* cache-busted.

> ⛔ **So the "production has no Anthropic key" parity gap is LATENT, not live.** Nobody can hit it.
> It becomes live the moment the first AI-bearing screen ships to a household origin — and that is
> the moment to have decided §3, not before and not after.

### ⛔ 0b · The gap is not an AI gap. It is a secrets-provisioning gap, and AI is one third of it.

`/health` at ~23:10 UTC:

| worker | anthropic | openai | airnow | ambient | github |
|---|---|---|---|---|---|
| `fernwood` (legacy prod) | ✅ | ⛔ | ✅ | ✅ | ✅ |
| `fernwood-qa` | ✅ | ⛔ | ✅ | ✅ | ⛔ |
| `fernwood-home` | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |
| `myhome-bob` | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |
| `myhome-paul` | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |

The three new households have **no secrets at all**. Framing this as "production needs an Anthropic
key" would fix one of three and leave the air-quality proxy and the weather station — both
**deterministic** — just as dark. ⭐ **The deterministic capabilities are missing from production
too, and they are the ones with a ratified rule saying they must have a door.**

### ⚠️ 0c · `openai: false` on every environment, including legacy production.

Phase H (audio sound-ID, `worker.js:1554–1630`) is documented in the header block, wired at
`/api/audio-upload`, and **has never been configured anywhere**. It is not a parity question; it is
a feature that is described in the record and absent from the world. Flagging, not deciding.

### ⭐ 0d · The third class already exists in canon and already has a rule.

`CLAUDE.md:446` `[recorded]`:

> *"A card prompt is neither ask-path nor capture-path but a **THIRD category — authored content** —
> so the rule is 'human-confirmed before it reaches Mom,' not 'AI-free' (Fernwood already AI-drafts
> authored content behind Paul's approval, e.g. promote-species)."*

**The question Paul asked tonight is not open. It is half-answered in his own canon and never
generalised.** What follows is the generalisation, not a new model.

---

## 1 · THE LINE — and why "deterministic vs generative" is the wrong cut

The two-way cut fails on the case Paul named in his own sentence. *"The research that's cleaned up
for a given plant"* was **produced by a model** — so it is generative — and it now sits in
`plants.json`, in git, read identically by every reader forever — so it is deterministic. Both
answers are true, which means the axis is wrong.

The axis that works is **what the output becomes**, not whether a model touched it.

### The three classes

| class | what it is | may a model author it? | does it persist? | reproducible? |
|---|---|---|---|---|
| **Computed** | a value the rules force | ⛔ never | yes — or recomputed on demand | ✅ byte-identical |
| **Said** | one answer, to one reader, in one moment | ✅ that is its whole job | no — cached at most, never read back as fact | ⛔ and that is correct |
| **Authored** | a model drafted it, **a person confirmed it**, it entered the record | ✅ as a draft only | **yes, permanently, with provenance** | ✅ because it never runs again |

### ⭐ The falsifier — one question, and it sorts every surface

> **If two runs disagreed, would that be a bug?**
>
> - **Computed** — yes, a bug. Something is wrong.
> - **Said** — no, expected. Two readers get two answers and both are right.
> - **Authored** — the question is malformed. It runs once, by construction. *If you can ask it, the
>   thing is not Authored — it is a cache pretending to be a record.*

That last clause is the load-bearing one and §4 is entirely about it.

### How this composes with what is already ratified — it adds an axis, it does not move one

- **Ask-path vs capture-path** (`[paul-stated]`, global) governs *where a model may write*. Untouched.
- **Deterministic things need a non-AI door** (`[paul-stated 2026-08-02]`) governs *whether a model
  is the only way in*. Untouched — and §0b says production currently fails it in the boring
  direction: the doors are shut for everyone.
- **The forced-answer test** (playbook, 2026-06-08) asks *should a model touch this field at all?*
  It runs **first**, and it is the thing that keeps the Computed column honest.
- **This** asks the next question down: *given a model did touch it, what happens to the output?*

⚠️ **One place it corrects a loose reading, stated plainly as the methodology requires.** "AI on the
ask path" is sometimes read in this repo as "AI output is ephemeral." It is not, and never was —
`promote-species` has been committing model-drafted prose to `plants.json` since Phase F, with
Paul's canon blessing it at `CLAUDE.md:446`. The rule that governs Authored content is
**human-confirmed**, not **AI-free**, and conflating the two would either freeze a working feature
or quietly license an unconfirmed one.

---

## 2 · THE SURFACE CENSUS

Load-bearing for a **release gate** = *"QA passed, therefore production will pass"* is a sentence
you are entitled to say about it.

| # | surface | where | class | gate-bearing? |
|---|---|---|---|---|
| 1 | **Observation capture** (`/api/observations`) | `worker.js:3468` | **Computed** | ✅ **yes — the highest.** Deterministic, AI-free by ruling. A regression here is silent data loss. |
| 2 | **Zone geometry** (`/api/zone-save`, `sanitizeZone`) | `:3640` | **Computed** | ✅ **yes.** `validVertex` **rejects, never clamps** (`:3529`) — a deliberate fix to the 3rd member of the 2026-07-15 write-loss family. |
| 3 | **Zone audio** (`/api/zone-audio`) | `:1673` | **Computed** | ✅ **yes.** Header says it: *"we store the AUDIO, never a transcript… and never an AI interpretation."* No transcription anywhere in the path. **This is the cleanest instance of the boundary in the codebase.** |
| 4 | **Weather / AQI / drought / almanac** (`/api/airnow`, `/api/drought`, ambient, sun-horizon) | `:1100–1160`, `tools/gen-sun-horizon.py` | **Computed** | ✅ **yes.** Cached proxies over third-party truth + computed astronomy. Zero model turns. |
| 5 | **Grants, capability, budget, `/health`, metrics, cost-log** | `:3465`, `:3152` | **Computed** | ✅ **yes.** The tenancy falsifiers (`T1`–`T4`) live here. |
| 6 | **The digest build** (`build-digest.py` → `digest.json`) | `tools/build-digest.py` | **Computed** ⭐ | ✅ **yes — and this is the load-bearing one nobody would guess.** It is a deterministic strip-and-repack of the source JSON. `check-digest-fresh.py` asserts the on-disk artifact equals a fresh rebuild, and **that check only works because nothing generative runs at build time.** See §4c. |
| 7 | **Guru lookup tools** (`dispatchTool`, `CORE_TOOLS`, `LOOKUP_STRINGS`) | `:100–…` | **Computed** ⭐ | ✅ **yes.** Complete records, deterministically sorted, counted when truncated, never a model-chosen top-k; refusals are the *record's* words, not the model's. `guru-replay.mjs` already proves all of it offline. **This is the substrate under the generative surface, and it is the gate.** |
| 8 | **Onboarding copy** | `onboarding/index.html` | **Authored (human)** | ✅ **yes.** Static, hand-written, no model at runtime. A copy regression is a diff. |
| 9 | **Garden Guru chat** (`/api/chat`) | `:2010` | **Said** | ⛔ **no, on content.** ✅ **yes, on invariants** — refusal strings, tool-call correctness, fence shape, budget, auth. |
| 10 | **Today-line** (`/api/today-line`) | `:1177` | **Said** | ⛔ **no.** 36h KV cache, keyed by date + estate. If it were lost, tomorrow just gets a different line and nothing downstream notices. |
| 11 | **Classify from text** (`/api/classify`) | `:1246` | **Said → routed** | ⚠️ **partial.** Output is squeezed through a closed enum (`ALLOWED`, `:1281`) — a good post-check. Its *result* is a suggestion, never a stored fact. |
| 12 | **Species classification from a photo** (Guru vision → suggestion) | `:2010` path | **Said** | ⛔ **no.** A model read. Ratified: `[[model-read values are hypotheses until verified]]`. |
| 13 | **Species promotion** (`/api/promote-species`) | `:2518` | ⭐ **Authored** | ✅ **yes — on the GATE, not the prose.** Gate-bearing assertions: two human confirmations happened; the drafter's output parsed as JSON or the write was refused (`:2606`); `_provenance` was stamped; the viewer read-back self-check (`3b`) passed. **Never** "the drafted entry was good." |
| 14 | **The cleaned-up plant research** (`guide`, `care`, `seasonNotes` in `plants.json`) | `plants.json` | ⭐ **Authored** | ✅ **yes — as a file diff, exactly like any other source file.** 12 of 40 entries carry `_provenance` naming the model read. Once committed **this is not AI output any more. It is the record.** |
| 15 | **Zone naming** | `.plans/2026-08-31-zones-traced-with-mom.json`, `/api/zone-feedback` | **Computed / human** | ✅ **yes.** Sixteen names a person gave unprompted. `/api/zone-feedback` queues her words; Paul draws the polygon by hand. No model in the path, and per today's mapping scan **none can be** — *imagery proposes an extent, only a person supplies an identity.* |
| 16 | **Audio transcription — Mom's zone voice** | — | **does not exist** | n/a. Deliberately. See #3. |
| 17 | **Audio sound-ID** (Phase H, `gpt-4o-audio`) | `:1554` | **Said** | ⛔ no — **and unconfigured everywhere** (§0c). |

### 2a · What this census says in one line

> **13 of 17 surfaces are gate-bearing, and every one of them is gate-bearing for a deterministic
> reason.** Not one release gate in this product depends on a model producing good prose. That is
> not a limitation — it is the thing to protect.

---

## 3 · CAN A NON-DETERMINISTIC CAPABILITY BE PART OF A PROMOTION GATE?

**Short answer: yes, but never on its output.** A generative surface is gateable on three things and
no others: **its substrate, its refusals, and its invariants.**

### 3a · What the field actually does — and how much of it applies here

The 2026 practitioner stack for gating LLM features is now fairly settled, and it is a ladder:

1. **Assertions / unit tests** — cheap, deterministic, run on every change. Hamel Husain's Level 1;
   Rechat runs "hundreds," continuously grown from observed failures.
   ([hamel.dev](https://hamel.dev/blog/posts/evals/))
2. **Golden dataset + eval gate in CI** — a curated input→known-good set, scored, with a merge
   blocked when a metric drops below a production baseline (commonly ~2%). Build the golden set from
   real production failures, not happy paths; gate on a tail metric, not only the mean.
   ([futureagi](https://futureagi.com/blog/ci-cd-llm-eval-github-actions-2026/),
   [myengineeringpath](https://myengineeringpath.dev/genai-engineer/llmops/))
3. **Property-based / invariant testing** — the complement to a fixed example set: *"eval datasets
   tell you whether your LLM passes a fixed set of examples; property-based testing tells you whether
   it obeys a contract across the entire input space."* Assert *it parses · it is grounded in the
   source · forbidden fields are absent · bounds hold*, and sample repeatedly.
   ([tianpan.co](https://tianpan.co/blog/2026-04-12-property-based-testing-for-llm-systems))
4. **Shadow mode** — the new version runs on real input, is scored offline, and serves nobody.
5. **Canary** — 1–10% of live traffic, with the **rollback threshold pre-registered before traffic
   touches it**, alarming on a *sustained* delta rather than a single spike so a brittle judge call
   doesn't roll back a working build.
   ([tianpan.co](https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing),
   [futureagi](https://futureagi.com/blog/llm-eval-shadow-traffic-canary-2026/))
6. **A/B** — Hamel's Level 3, explicitly *"reserved for mature products"* and only once you're
   convinced the product suits real users.

**Grading for this project.** (1) and (3) apply directly and are cheap. (2) applies *only in its
assertion form* — a scored golden set needs a judge, and a judge at n≈5 users is a second
non-deterministic system introduced to grade the first. (4), (5) and (6) all require **traffic
volume this product does not have and will not have** — a 5% canary of a household is nobody, and a
sustained-delta alarm needs a baseline distribution to be sustained against. Recommending them here
would be importing enterprise ceremony onto a family tool, which is exactly the calibrate-to-stakes
error this seat is on the record for avoiding.

### 3b · ⭐ The recommendation — and most of it is already built

**The gate for the generative surface is: the substrate is identical and the refusals hold.** That
sentence is not a compromise; it is a direct consequence of Paul's own ratified finding that *AI
output breaks environment parity — diff the deterministic substrate*. He already decided this. It
has not been wired.

**Tier 0 — `guru-replay.mjs` becomes a deploy gate. This is the single highest-value change here.**
It drives `dispatchTool` on the committed digest with **no network and no model**. It already
asserts tool order, completeness, deterministic sort, truncation counts, verbatim caveats,
`{found:false, reason}` in the record's words, the vault door staying shut, byte-identical repeat
calls, and that the six client fence parsers resolve against canon. **That is a property-based
invariant suite for a generative surface, and it exists, and nothing runs it before a deploy.**
`tools/deploy-worker.sh` runs digest rebuild → `check-digest-fresh.py` → `wrangler deploy` →
`/health`. Adding one line before step 3 converts a report into a gate.
(⚠️ F1 in the DECISIONS file says the same thing about the Worker deploy from the tenancy side.
Same missing hook, two seats found it independently — that is corroboration, not duplication.)

**Tier 1 — a post-check at each model call site. One is missing and it is the one Mom reads.**
Playbook, `[paul-stated 2026-07-20]`: *wrap the AI seam in cheap deterministic guards.* Present state:

| site | pre-gate | post-check | verdict |
|---|---|---|---|
| `/api/classify` | body non-empty | ✅ closed enum + `null`-coerce (`:1281`) | good |
| `/api/promote-species` | two human confirms, kind in `KIND_TARGETS` | ✅ JSON parse or 502; viewer read-back `3b` | good |
| `/api/chat` | budget, auth, size | ✅ fences parse or don't render | adequate |
| **`/api/today-line`** | date only | ⛔ **none** | ⚠️ **gap** |

Today-line's system prompt says *"one or two sentences · two short sentences max · no headlines, no
bullets, no markdown."* Nothing checks it. A model that returns four paragraphs of markdown gets a
`200`, a 36-hour cache, and top billing on the dashboard. The check is four lines — length ceiling,
sentence count, no `#`/`-`/`*` at a line start, no `"Recommended:"`/imperative opener (the ratified
*mood is the fence* rule, mechanised). On failure: **fall back to no line**, which the client
already renders correctly (`viewer.html:6400` starts `hidden`).

**Tier 2 — `guru-probe.py --live` runs on a cadence and is READ, not enforced.** It already refuses
anything that isn't the QA Worker on the QA namespace before spending a cent, and its grading is
already inverted correctly (a row is red if the answer carries the stale-self or the confusable
sibling, *even when the right number is also present*). That is Hamel Level 2 done properly.
⛔ **Do not make it blocking.** At its n it will flake, and a gate that flakes is a gate Paul learns
to wave through — which is worse than no gate, because it launders a red into a habit.

**Tier 3 — explicitly declined, so it is not re-proposed in three weeks:** LLM-as-judge scoring,
a scored golden dataset with a numeric merge threshold, shadow traffic, percentage canaries,
auto-rollback, A/B. All standard; all wrong at this scale. **Revisit trigger, pre-registered:** more
than ~50 real Guru turns per week from people who are not Paul.

**The human gate is already the right one and already ratified.** The release cascade — *synthetic
persona → Paul → Mom*, with Mom as gate 3 and never gate 1 — **is** the content gate for Said
surfaces. Nothing mechanical replaces it and nothing should try.

### 3c · What "QA passed" is entitled to mean, per class

| class | the sentence QA earns |
|---|---|
| **Computed** | *"It will behave identically in production."* Full strength. |
| **Authored** | *"The gate fired and the artifact is byte-identical."* Full strength — because the artifact, not the model, is what promotes. |
| **Said** | *"The substrate is identical, the refusals hold, the invariants hold, and the budget is capped."* **That is the whole entitlement.** It does not extend to "the answers will be good," and no amount of QA will make it. |

⚠️ This is `VOCABULARY.md` §3d's declared `qa` double-booking, arriving from a third direction: the
pipeline stage `qa` is falsified by *the change being wrong*; the mom-cycle leg 7-QA by *the change
being right and not arriving intact*. A Said surface adds a third falsifier — *the change being
right, arriving intact, and answering differently anyway* — and **no environment can host it.**
Worth recording at §3d as a third instance rather than a new word.

---

## 4 · PARITY, AND WHERE GENERATED CONTENT LIVES

### 4a · ⭐ Recommendation: a declared capability flag, one key everywhere. Not environment-gating.

**Why not environment-gating.** Right now the absence of the secret *is* the flag — an
**undeclared** one whose failure shape is a `503`, i.e. an outage, not a product decision. Martin
Fowler's toggle guidance is direct about this class of thing: *"any environment-specific overriding
runs counter to the Continuous Delivery ideal of having the exact same bits and configuration flow
all the way through your delivery pipeline"*; prefer static configuration in source control, flowing
identically. ([martinfowler.com](https://martinfowler.com/articles/feature-toggles.html)) A missing
secret is the *worst* form of environment override, because it is invisible in the repo — you learn
it from a live probe, which is exactly how it was learned tonight.

**Why the cost argument does not rescue environment-gating.** Cost is real and it is the honest
motive, but **the cost control already exists and is better**: `CHAT_DAILY_BUDGET_USD` is declared
per environment in `wrangler.toml` (`10.00` on home, `5.00` on bob/paul) with a stated rationale —
*"it exists to stop a BUG, never to stop HER."* Using key-absence as a second, cruder cost brake
duplicates a control that is already declared, already tuned, and already legible.
⚠️ One real defect the DECISIONS file already caught and this recommendation depends on: under one
production environment the chat budget becomes **one shared pot**, so one household's runaway takes
Guru down for everyone. **The budget must split per estate before the flag is worth turning on.**

**The shape.** One `ANTHROPIC_API_KEY` in every environment that runs the product. A declared
`[vars]` capability flag per environment saying whether the generative surface is on. The budget
stays the brake. `/health` keeps reporting `configured`, and the flag joins it — so *"is the Guru on
here?"* is answerable **without asking the Guru**, which is the ratified non-AI-door rule applied to
the AI feature's own status.

**Under one production environment this gets simpler, not harder** — there is exactly one production
key to provision, and the flag stops being per-environment at all and becomes per-feature. That is
an argument for deciding the shape now and provisioning once, rather than provisioning three
household workers that are about to be consolidated. **Sequencing is engineering-partner's; the
requirement is that the flag be declared and readable, never inferred from a 503.**

**⚠️ And "parity" on a Said surface is a category error worth naming out loud.** Paul's own
`[paul-stated 2026-09-05]` finding stands: dev ≠ qa by construction on a generative surface. Turning
the flag on in production does **not** make production's today-line equal QA's, and if anyone ever
diffs those two strings expecting a match, this document failed. Parity means: **same key, same
model snapshot, same digest sha, same prompt bytes, same budget policy, same refusals.** Never same
output.

### 4b · Where generated content lives — one rule per class

| class | destination | lifetime | today |
|---|---|---|---|
| **Said** | KV **cache** or a conversation transcript | expires; loss is a non-event | ✅ today-line 36h TTL keyed by date+estate; Guru turns as `conversation:<uuid>` |
| **Authored** | **git, as content-of-record, with `_provenance`** | **permanent; never regenerated** | ✅ `plants.json` — 12 of 40 carry `_provenance` |
| **Computed** | source JSON → deterministic build artifact | rebuilt on demand, byte-identical | ✅ `digest.json` + `check-digest-fresh.py` |

**So the direct answer to Paul's question: the cleaned-up plant research is *content-of-record*, not
a cache and not a build artifact — and it already is.** The artifact-management literature converges
on the same stance from the ops side: pin exact digests including prompts; prefer immutable
snapshots over moving aliases, because with an alias *"weights, prompts, and safety filters can
change without notice"*; and **never overwrite an artifact in place — overwriting destroys the audit
trail and makes rollback impossible.**
([cloudsmith](https://cloudsmith.com/blog/llmops-vs-devops-what-llmops-means-for-artifact-management),
[atlan](https://atlan.com/know/ai-model-versioning-best-practices/))
This repo is already compliant on the sharpest edge: every call site pins
`claude-haiku-4-5-20251001`, a dated snapshot, not `claude-haiku-4-5`.

Two details already right and worth protecting because both are the kind of thing a cleanup deletes:

- **`_provenance` is deliberately NOT stripped from the digest** (`build-digest.py`, comment at the
  strip list): it carries *"species ID model-read"*, *"local phenology unobserved"* — the markers
  that make Guru **hedge instead of assert** on exactly the 12 entries a model read. That is the
  `[[AI verification flags, never clears]]` rule surviving all the way from the drafter into the
  reader's answer, at a cost of a few hundred bytes.
- **The drafter is instructed to be born honest-and-thin** — the reader's own notes SUPERSEDE book
  knowledge, and it is told not to fabricate local phenology (`worker.js:2570`). Authored content
  entering the record already knows what it doesn't know.

### 4c · ⛔ The one thing that must never exist, and what breaks if it does

> **A regenerating cache of Authored content.**

Concretely: any future feature that *re-generates* a plant's `guide`/`care`/`seasonNotes` — on read,
on build, on a nightly refresh, on "seasonNotes changed so let's redraft." It is the single most
natural next feature in this area and it would break four things at once:

1. ⭐ **Paul's frozen instance stops being a data control.** A control has to hold everything except
   the thing under test constant. If prose redraws itself between two instances, a difference can no
   longer be attributed to the change — and the freeze register, `archive-frozen-estate.py` and the
   175-key archive all become a comparison you cannot make. *This is the reason the question was
   asked this week, and it is the reason the answer has to be "never."*
2. **`check-digest-fresh.py` goes red — or, far worse, gets relaxed.** It asserts the on-disk digest
   equals a fresh rebuild. That assertion holds **only because `build-digest.py` is a pure
   strip-and-repack.** Put one model call in the build and the check becomes permanently red, and
   the pressure will be to loosen the check rather than remove the call. The repo has a name for
   that shape: an instrument that reports green over nothing.
3. **Git stops recording what a reader was actually shown.** The `plants.json` diff is currently the
   honest answer to *"what did Mom read on 2026-08-14?"*
4. **A model read becomes a fact with no human in between** — the ratified verification rule
   violated through the most innocuous door available, a cache that outlived its purpose.

**The cheap guard, matching the shape this repo already trusts:** a check asserting **no model call
site exists in any build-time tool** — `git grep -l 'api.anthropic.com\|api.openai.com' -- tools/`
must return empty, and the check must read **UNCHECKABLE rather than green** if it cannot resolve
the tools roster (the F2 control shape, derived-not-typed). One line, in the class of guard that has
already caught three write-loss defects here.

⚠️ **Related, smaller, same family:** nothing today stops a future feature from reading a stored
Guru reply back out of `conversation:<uuid>` and treating it as a property fact. Transcripts are a
record of *a conversation*, never a record of *the place*. Worth one sentence wherever the
conversation store is documented.

---

## 5 · THE LINE FOR `VOCABULARY.md`

Register per §6 (*cite, never restate*) and per the product rule that internal vocabulary never
reaches a reader — so the line uses the reader's word for the record (*the Almanac*, per
`JOURNAL_WORD`) and names no model, no endpoint, no class name.

> ### 5x · SAID, NOT STORED `[agent-proposed 2026-09-06]`
>
> **What the Almanac *says* is said once, to one reader, in one moment, and is never the record;
> what the record *holds* is computed, or confirmed by a person before it was written — and it reads
> the same to everyone, every time.**
>
> *Cites, does not restate:* `CLAUDE.md` § design-time defaults (ask-path / non-AI-door) and
> `CLAUDE.md:446` (authored content is *human-confirmed*, not *AI-free*).
> *Falsifier:* if anything a reader was **told** can be found later being **read back as a fact**,
> the line has been crossed.

(Section number left as `5x` deliberately — §5 is the live `group` defect and I am not renumbering
around it. Placement is Paul's call; §3 is where ratified terms live.)

---

## 6 · WHAT ONLY PAUL CAN DECIDE

Ordered. Each is a ruling, not a task.

1. **Ratify the three classes and the falsifier** — *Computed · Said · Authored*, sorted by *"if two
   runs disagreed, would that be a bug?"* Everything else here depends on it. (§1)
2. **Rule the gate for Said surfaces:** *the substrate is identical and the refusals hold* — and
   accept what it does **not** buy, which is any promise about answer quality. (§3c)
3. **Rule whether `guru-replay.mjs` blocks a deploy.** This has a real cost: a red replay stops a
   ship. That is the point, and it is his to accept. (§3b Tier 0)
4. **Rule: Authored content never regenerates.** Saying it now pre-declines the "refresh the guide"
   feature before someone builds it and discovers the frozen control is worthless. (§4c)
5. **Rule the gating mechanism: declared capability flag with one key everywhere, or environment.**
   My recommendation is the flag; the budget stays the brake. Not urgent — §0a says nobody can reach
   an AI surface in production today — but it must be settled **before** the first AI-bearing screen
   ships to a household. (§4a)
6. **Decline Tier 3 out loud** — no LLM-judge, no scored golden set, no shadow, no canary, no A/B —
   with the ~50-turns-a-week revisit trigger on the record. (§3b)
7. **Two flags, not decisions:** the three new households have **no secrets at all**, deterministic
   ones included (§0b — engineering-partner's mechanism, his provisioning call); and Phase H
   audio sound-ID is `openai: false` **everywhere**, documented and never configured (§0c) — keep,
   or retire it from the record.

---
