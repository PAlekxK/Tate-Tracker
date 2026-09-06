# One production environment — the decisions `[paul-ruled 2026-09-06]`

Companions: `.engineering/2026-09-06-one-production-environment.md` (architecture),
`.plans/2026-09-06-conversion-method-DESIGN.md` (method). This file is the **rulings only**,
so a later session can act without re-reading either.

---

## 0 · What Paul stated, and what it turned out to mean

> *"One production environment with many households and users, and it's kind of the cleanest,
> especially if we're gonna have shared households between users. I want y'all to weigh in on
> that, though."* — 2026-09-06

⭐ **"Shared households" is NOT a new requirement — it is the Q11(a) model already ratified
2026-09-03.** Two readings wear the phrase and only one was ever declined:

| reading | status |
|---|---|
| **Two people each holding their own grant to one estate** | ✅ **RATIFIED 09-03.** `2026-09-03-onboarding-model.md`: *"it is simply two people with different grants"* — *"needs no special handling at all."* |
| **A family door — a menu rendering a union derived from who you are RELATED to** | ⛔ **DECLINED 09-03, in writing** (not deferred). Requires the family→estates map this project has declined to build twice. |

What Paul described is the ratified one. **No new model, nothing to re-ratify.** The collision
is in the words, not the design. `VOCABULARY.md` is untouched by this.

✅ **Verified, not assumed** (main session, 09-06): the defect that ruling names — *anything
reading `relationship` to decide reachability* — **does not exist**. `relationship` is reported
at 6 sites and read for access at none; `capability` alone gates, at `worker.js:3465`.

---

## 1 · The architecture — ONE production environment

**Ruled: build it.** But the reason is on the record, because it is not the reason in the
sentence above.

⚠️ **"Cleaner" is NOT sufficient on its own.** At n≤10, N Cloudflare projects buys the strongest
isolation available — one that needs no test to be true. Had the requirement stayed
one-owner-per-household, engineering-partner would have held its morning answer (`A now, B next`)
and called the instinct aesthetic.

⭐ **Sharing is what decides it.** Deployment-per-household cannot express two-people-one-estate
at ANY n, including n=2 — **fatal, not awkward**:
- **There is no *person*.** `personId` is minted inside a namespace, so Bob-at-house-1 and
  Bob-at-house-2 are unrelated ids with two password hashes that drift.
- **You cannot invite someone into your house** — an invite is a grant for a person who does not
  exist in that namespace.
- **The only shelf it permits is a device-local list of `(origin, token)` pairs** — which
  re-commits one layer up the bug fixed this week: copy that clearing your browser turns into a lie.
  It fails to express `homes/index.html`, built 09-06 14:22.

Shape A did not become wrong. **The requirement moved outside its reach.**

### Already latent, so the work is smaller than a redesign
- `personId` is first-class and separate from `estateId` (`worker.js:357`).
- The wire already returns **`estates: [ ]` — an array** (`:515`, `:626`); always length 1 today.
- Per-estate role exists and is **enforced**: `relationship`/`capability`, real 403 at `:3465`.
- Revocation is fully built with a selftest (`grant-mint.py` stamps `revokedAt` AND deletes the row).
- `declarePerson`/`attributeTo` already **throw** if a household comes from a literal or the deploy
  binding rather than the resolved grant — ⚠️ but called at **1 of 4** `declarePerson` sites.

### The two real gaps
1. ⛔ **The lookup.** A grant is stored at `<estate>:grant:<hash>` — you must know the estate to
   find the grant that names the estate. **Do NOT build a global pointer index** (my sketch,
   rejected by engineering-partner): it is a modelling error, not a missing lookup. A grant is now
   an *edge* between a person and an estate. **Move the row out of the estate prefix; do not index
   it.** No second writer, no disagreement mode. Estate data keeps its prefix; only identity leaves.
2. ⛔ **The login path is the harder half, and was not in the brief.** `handleSession` reads
   `accountKey(scope, username)`. A person typing a username and a password supplies **no estate
   hint at all** — you can prefix a token, you cannot prefix what a human types.
   **Global accounts is forced, not chosen.**

### Hardening — the answer to "the check catches FORGOTTEN, never WRONG"
- **Attenuated KV handle:** hand handlers a prefix-bound `store`, never `env.OBSERVATIONS`. A
  handler then *cannot address another household because the handle it holds cannot name one.*
  Correctness moves from "all ~30 conversions were right" to "one wrapper is right."
- **Type-split the scope:** delete `scopeOf(env)`; `deploymentScope(env)` typed `"deployment"`;
  `keyFor`/`dateKey`/`blobKey` throw on it. A forgotten site then produces **no valid key**, and
  the greppable roster goes to zero instead of being a hand-maintained count.
- ⚠️ **`hostAgrees` stops being a tenancy control** under one origin. Do not count it in the stack.
- ⚠️ **The chat budget becomes one shared pot** (`dateKey(scopeOf(env),"chat-budget",…)`) — one
  household's runaway takes Guru down for everyone. Needs a per-estate split.

### The falsifier — four tests, four mutations
`T1` two grants/two estates/**raw KV keys** · `T2` sharing (two grants, ONE estate, both see it,
a third does not) · `T3` a person in TWO estates — *"authorized for some estate" leaking into
"authorized for this estate"* is the sneakiest bug in the design and no one-person fixture catches
it · `T4` revocation. ⭐ **T1 and T2 are each other's negative control** — T1 alone passes if you
accidentally key by person instead of estate. Mutations: M1 revert a handler → T1 red · M2 key by
`personId` → T2 red · M3 authorize by listing → T3 red · M4 cache capability on session → T4 red.

---

## 2 · Paul's rulings, 2026-09-06

### R1 · Bob — **HOLD until one production environment lands** `[paul-ruled]`
Not sent this week; he meets the final shape once and never receives a second link.

⭐ **RELEASE CONDITION** (a hold names the work, and "indefinite" is abandonment with manners):
> **Bob is released when one production environment is live AND the paired-walk gate (`T2`) has
> passed on synthetics.**

Consequences: `myhome-bob` stays **empty** · the export/restore round-trip is **no longer
blocking** (still worth building) · the 09-07..09-10 window question is **closed** · the only
outside feedback before Mom is now synthetic.

### R2 · `myhome-paul` + `myhome-bob` — **KEEP BOTH as declared test rigs** `[paul-ruled]`
Coherent *because* of R1: both stay empty, so they are two real deployments with no real data —
exactly what a store-diff target should be. Migrating two empty estates is a **no-op and must not
be reported as work.**

⛔ **The accepted cost is a staleness control, and it is already overdue:** `myhome-bob` served a
build **20 commits behind HEAD** within 2h40m of being created, and nothing noticed. Keeping the
rigs without this control is keeping a lie.

### R3 · Conversion order — **build the two-household store diff FIRST** `[paul-ruled]`
Stand up the store-level falsifier against `bob` and `paul` as they exist today, so a working
instrument exists **before** the blind stretch. Costs roughly a session before slice ②.

**Why there is a blind stretch at all** — the two experts pull apart here, and both are right:
- *engineering-partner:* readers first, **producer/lookup LAST**. Flipping the lookup with one
  reader unconverted is the one ordering that **leaks silently instead of failing loudly**.
- *practice-steward:* **nothing before the lookup change is falsifiable** — a converted site and an
  unconverted one behave identically on every walk, so those slices buy code, not evidence.

Reconciled: readers convert blind but safe; the lookup flips as the single step that finally
produces evidence. R3 is what makes the blind stretch acceptable rather than merely tolerated.

---

## 3 · Findings that outlived the question

### ⛔ F1 · There is no deploy gate on the Worker at all
`tools/deploy-worker.sh` is 59 lines, takes **no `--env`**, and a bare `wrangler deploy` targets
the legacy estate. It checks digest freshness and `/health` only. **Every control built 09-06
guards the *Pages* export — and the entire conversion lives in `worker.js`.** This blocks R3's
value: a falsifier you cannot gate a deploy on is a report.

### ⭐ F2 · The blind-check pattern is a MISSING CONTROL — not velocity, not review
Measured on the commit record, the window between building a surface and the check covering it:
**40h 08m → 2h 32m → 0 → 0** (`homes/` and both `settings/` were widened *in the commit that
created them*). Velocity would widen that window; it closed. Review failure means a defect
survives review; the last two survived nothing.

> **The control: an instrument's scope must be DERIVED from whatever declares reality, and a
> derivation that finds nothing must read UNCHECKABLE — never green.**

`check-storage-keys.py` reached that shape 09-06 14:32 and carries it. **The shape is not
generalised**, and the siblings are measurable — `wrangler.toml` declares six environments:

| instrument | environments covered |
|---|---|
| `pages-deploy` | 6 / 6 |
| `read-onboarding` | 4 / 6 |
| `journey-walk` | 3 / 6 |
| `synthetic-identity` | 3 / 6 |

⚠️ **"The harness cannot target household origins" is not a separate backlog row — it is this
item.** The honest reason it matters: the two saves happened because the same author was in the
same session and remembered. **That does not survive the session.**

### ⚠️ F3 · The walk evidence is not at the build it was reported at
`walk-integrity` at `efaae6b`: 47 runs · 12 countable · 4 seats · 4 distinct inputs — but the
countable runs sit at `3b7d7be` / `fae767e` / `9112b4b`. **Exactly one run exists at `ebdf172`
and it is REFUSED** (report-unwritten). The main session carried "four seats walked at `ebdf172`"
into an expert brief as fact. **Nothing between the instrument's output and a summary re-reads
the instrument** — this is the ratified *evidence expires when the build moves* rule catching the
session that proposed it.

### ⚠️ F4 · `--env prod` is a naming trap (NOT a security hole)
An earlier claim that dev/qa/production all bind `est-3c9f1a` is **false** — verified by parsing
`wrangler.toml`: `prod→est-3c9f1a` · `qa→est-qa0001` · `lab→est-lab0001` · `home→est-e6696a` ·
`bob→est-9a74df` · `paul→est-d93508`. G3 reads this table and fires correctly. **The real trap:**
`prod` is the toml's *top level* — the **dev** worker — while the family's production is `home`.
Reaching for the word "prod" gets the wrong deployment. G3 catches it; it costs a confusing hour.

### F5 · The front end has a bigger tenancy problem than the Worker
`pages-deploy.py` ships bob/paul a neutral allow-list, but `home` ships **everything, including
`viewer.html` with the street address**. ⭐ The neutral shell is already estate-neutral, so **one
production environment is reachable for the new product without touching `viewer.html`** — which
makes *"Mom's production home is the neutral shell; the legacy viewer stays where it is"* a
sentence Paul has to say out loud before the merge.

### F6 · Cascade gate ③ splits in two
A pass now needs a second clause — *no other household's store changed while they walked* — which
is **untestable until the conversion lands**. And Paul's gate-③ walk expires at migration by his
own rule, so it records as **③-pre** (the journey; expires by construction) and **③-post** (his
answers survived the conversion). Only the second is about tenancy.

---

## 4 · Still open — Paul's, not mine
- **R1's release condition** — stated above; needs his yes or a different trigger.
- **F5's sentence** — is the legacy viewer left in place at `home`?
- Three cheap ones carried from practice-steward: the `.plans/` stage enum (fifth instance) ·
  whether the offsite verifier hands to `/team-audit` · whether the chronicle "not-a-lap"
  assertion is re-made for today's 35 commits.
