# HOW A TENANCY CONVERSION IS RUN — gates, the unit of work, the control that was missing all day, and what the cascade means once everyone lands in one production environment · DESIGN

- row: process (no BACKLOG row — same posture as the 09-04 wiring audit and today's two audits)
- objective: O5
- class: engine · declared (process machinery; no Fernwood content is ranked here)
- seats: practice-steward (this file)
        engineering-partner → **owns the architecture in parallel; nothing here designs the conversion's code.** §1 states gates and units of work, never mechanisms
        ai-advisor · ux-expert · content-steward · user-researcher → not commissioned
- depends-on: .plans/2026-09-06-cascade-and-release-state-AUDIT.md
- depends-on: .plans/2026-09-06-state-and-next-steps-AUDIT.md
- ready: agent-proposed 2026-09-06 — **Paul rules**
- kind: design

> **Method only.** Nothing here ranks a feature or moves a date. Where a call turns on real-world
> context only Paul holds, it is named and declined — §7.

---

## 0 · THE STAMP AND THE ONE CONTRADICTION I HAVE TO OPEN WITH

**Opened and closed at `efaae6b`. Working tree clean** (`git status --porcelain -uall` → empty).

⛔ **The brief I was given says *"Four seats walked the full 12-stop journey on QA today at `ebdf172`."*
The instrument disagrees, and I am reporting it rather than resolving it.**

`python3 tools/walk-integrity.py` at `efaae6b`:

```
runs: 47 · countable: 12 · refused: 35
seats with a countable run: 4 · DISTINCT INPUTS AMONG THEM: 4
🔴 THE NEWEST RUN IS REFUSED for: owner, wide-eyed
```

| seat | newest COUNTABLE run | build it walked | behind HEAD | newest ATTEMPT |
|---|---|---|---|---|
| mom | 2026-09-06T144204 | `9112b4b` | **4 commits** | same, countable |
| strict | 2026-09-06T144042 | `9112b4b` | **4 commits** | same, countable |
| wide-eyed | 2026-09-06T144115 | `9112b4b` | **4 commits** | `2026-09-06T145045` @ `ebdf172` — **REFUSED, report-unwritten** |
| owner | 2026-09-06T143904 | `6674a02` | **6 commits** | `2026-09-06T144607` @ `9112b4b` — **REFUSED, report-unwritten** |

> ⭐ **Exactly one run exists at `ebdf172` and it is refused. No seat has a countable run at `ebdf172`,
> and none at HEAD.** The 12/47/4/4 counts in the brief are right; the *build* attached to them is not.
>
> **This is the failure the walk corpus was built to make impossible, arriving one level up:** a
> refused run and a countable run at the same seat, an hour apart, summarised as one fact. The
> instrument caught it. The summary of the instrument did not. **Nothing between `walk-integrity`'s
> output and a coordinator's brief re-reads the instrument** — and §2 is about precisely that gap.

**Second-method check, because a single tool's output is a claim:** the ✅ lines were re-read directly
from the tool and each build sha independently counted against HEAD with `git rev-list --count`. Both
agree.

---

## 1 · A · HOW A CONVERSION LIKE THIS IS RUN SAFELY

### 1.0 · Measured position, with the predicate stated

| reading | value | predicate |
|---|---|---|
| `grep -c "scopeOf(env)" worker/worker.js` | **55** | lines containing the token, **prose included** |
| actual **code call sites** | **50** | the 55 minus 5 comment lines |
| code call sites at `b784dc9` (this morning) | **50** | same predicate |
| code call sites **converted** since | **0** | `scopeFor(` has exactly **one** caller, `worker.js:3409`, marked `// eslint-disable-line no-unused-vars` |

⚠️ **The declared inventory is already wrong, and the commit that declared it is what broke it.**
`worker.js:662` reads *"Every remaining `scopeOf(env)` at a call site is therefore an exact, greppable
inventory of the sites that still take the household from config."* Slice ① (`79f426e`) wrote the token
**four more times into its own comment**, moving the grep from 51 → 55 while changing **zero** call
sites. `git diff 382b1d0 79f426e -- worker/worker.js` shows the four additions are all comment prose.

> ⛔ **This is not pedantry. It is the instrument the conversion's progress will be reported from.** A
> count that moves when nobody converts anything is a count that cannot show a conversion stalling —
> and it moved in the *wrong direction* on day one. **The predicate is one `grep -v` away from correct;
> the finding is that the inventory was a convention, not a mechanism.**
>
> **Falsifier:** if the conversion's progress is never quoted from this grep, the finding is cosmetic.

### 1.1 · The unit of work is the READ/WRITE CLASS, and the ordering is already written down and correct

Slice ①'s commit message contains the sequencing rule, and it is right and counter-intuitive enough
that it must not be rediscovered:

> *"`assertScope` catches a FORGOTTEN conversion, never a WRONG one. A site still calling
> `scopeOf(env)` passes it perfectly — valid scope, wrong household. So the identity doors go LAST."*

**Everything in §1 follows from that one sentence**, because it says the runtime cannot be the gate.
`assertScope` throws on a *shape* error. The failure mode Paul actually fears — a cross-household read
— produces a **perfectly valid scope with the wrong id**, and throws nothing, logs nothing, and returns
a 200. *X and not-X produce the same observation*, one more time.

**So the gate must be STATIC and TOTAL, not runtime and sampled.**

### 1.2 · ⭐ THE HARD SEQUENCING FINDING — most of the conversion is unfalsifiable by construction, and slice ① already knew why

`79f426e`'s own message, recorded at the time:

> *"`grantFor` looks the grant up at `keyFor(scopeOf(env), "grant", …)` BEFORE checking its estate. So
> a foreign grant fails TWICE… Both must change, and the LOOKUP is the harder half."*

Compose that with the deployment model (`wrangler.toml`: one `ESTATE_ID` per environment) and the
consequence is exact:

> **Until the grant LOOKUP is estate-agnostic, no deployment can be handed a request for a second
> household. So there is no failing case available. A converted site and an unconverted site produce
> byte-identical behaviour, every time, on every walk.**

⭐ **Therefore: every slice before the lookup change is a declared no-op, and none of them may be called
"verified" on a walk.** Slice ① was honest about exactly this (*"a deliberate no-op, proven not
assumed"*) — the risk is that slices ②..n inherit the *word* "verified" from a green walk that could
not have gone red.

**What this means for how the work is run, and it is the whole of §1's answer to "what is the unit":**

| | |
|---|---|
| **Unit of work** | one **read/write class** (all reads of kind K, then all writes of kind K), never one file and never one endpoint — because a handler that reads under B and writes under A is the leak, and a per-endpoint slice can create it inside one commit |
| **Ordering** | (i) resolve once at the gate ✅ **done, `79f426e`** → (ii) **the grant lookup** — the falsifier-enabling step, and the hardest → (iii) read paths → (iv) write paths → (v) **identity doors last**, per the rule above |
| **Why (ii) moves up from "hard, so later" to "second"** | not because it matters more. **Because every slice landed before it is untestable, and untested work accumulates in a store that has no eraser after Mom onboards** (`reset-production-estate.py`: *"After Mom onboards it must never be run again"*) |

⛔ **I decline the schedule.** Whether (ii) is worth its risk this week against Bob's window is Paul's.
What is method: **the falsifier arrives with (ii), and every slice before it buys code, not evidence.**

### 1.3 · The gates — four, and three of them are this repo's own machinery pointed at a new target

**⛔ None of these is a new ritual. Every one has a working precedent in this repo, named.**

| # | gate | what it refuses | reused from |
|---|---|---|---|
| **G1** | ⭐ **The conversion ledger — TOTAL, not a count.** Every `scopeOf(env)` **code** site is classified into exactly one of `converted` · `deployment-correct-by-design` (health, cron, cross-estate admin) · `pending`. An **unclassified site is RED** | a site nobody has thought about, which is indistinguishable today from one deliberately left alone | `check-engine-manifest.py` — *"is every tracked file CLASSIFIED engine/config/instance?"* Same shape, different axis |
| **G2** | **`pending` must not INCREASE across a commit.** | feature work quietly adding household-bound sites while the conversion is open. ⚠️ **This already happened in a weaker form today** — see §1.0 | stop-the-line. And it satisfies Paul's rule: **a countdown is a count, never a grade; the monotonicity is the only green/red** |
| **G3** | ⭐ **The two-household negative control.** After any walk in household A, household B's store must be **byte-unchanged**, read before and after | the leak itself — and it is the only gate that can. ⛔ **It cannot be built until §1.2(ii) lands**, and saying so is the point | `check-estate-neutral.py`'s falsifier, moved **from the page to the store**: *"load the surface a brand-new estate is served and grep it… zero hits, or it is not shipped"* |
| **G4** | **The Worker deploy gate.** | ⛔ **There is nothing here today.** `tools/deploy-worker.sh` is 59 lines, takes **no `--env`**, runs bare `npx wrangler deploy` (→ the top-level/legacy estate), and checks exactly two things: digest freshness and `/health`. **Neither can see a scope defect.** Whatever deployed `qa`/`home`/`bob`/`paul` is not this script and is in no procedure | `tools/pages-deploy.py` is the model and it is in the same directory: it **calls** `check-estate-neutral` and **refuses the deploy on a hit**. The pages path is gated; the Worker path — *where the entire conversion lives* — is not |

> ⭐ **G4 is the sharpest gap in this section.** Every control built today guards the **pages** export.
> The conversion is 100% in `worker.js`. `pages-deploy.py` walks the whole pruned export and refuses on
> any household-specific token (`tools/pages-deploy.py:118`–`:152`, verified by reading — it walks
> `export`, not one file). `deploy-worker.sh` refuses on nothing that could see a household.

**What stops a half-converted state shipping: G2 + G4, and nothing else can.** G1 makes the state
legible, G3 makes it falsifiable, but only a gate wired into the deploy act can *stop* it — and this
repo already recorded why, at `CLAUDE.md`: *"A check wired into the thing it guards cannot be
forgotten; a check listed in a document can."*

**Falsifier for §1.3:** if a `pending`-count gate fires on a commit Paul overrides as noise twice, G2's
predicate is wrong and the classification should absorb it the way `qa-divergence.py`'s `NOT_SURFACE`
absorbs `engine/place-claims.json`. If G1 reads red for a week with no way to reach green, delete it —
that is Paul's own rule and it outranks my recommendation.

---

## 2 · ⭐⭐ B · THE RULING YOU ASKED FOR — velocity, review, or missing control?

### 2.1 · The measurement first, because it changes the answer

`check-storage-keys.py` was built 09-03 (`5e216bd`, `fa51999`) scanning `viewer.html` only. Here is
every surface it was supposed to see, when the surface landed, and when the check learned to see it —
**all from the commit record, not from the session's memory of itself:**

| surface | created | check widened | **blind window, on the committed record** |
|---|---|---|---|
| `onboarding/index.html` (8 `fw-*` keys) | `adde066` **09-04 21:22** | `3249595` 09-06 13:30 | ⛔ **40h 08m** |
| `estate/index.html` | `4ea8e23` 09-06 10:58 | `3249595` 09-06 13:30 | ⚠️ **2h 32m** |
| `homes/index.html` | `71ee759` **09-06 14:22** | `71ee759` — **same commit** | ✅ **0** |
| `settings/place/index.html` | `6674a02` **09-06 14:32** | `6674a02` — **same commit** | ✅ **0** |
| `settings/account/index.html` | `6674a02` **09-06 14:32** | `6674a02` — **same commit** | ✅ **0** |

*(Verified by `git log --diff-filter=A` per file and by diffing `tools/check-storage-keys.py` at each
of the four commits that touched it today.)*

> ⭐ **The blind window went 40h → 2.5h → 0 → 0. Two of the three "misses" never existed in a committed
> state at all** — the widening and the surface landed in the same commit, both times.

### 2.2 · The ruling

**It is not a velocity problem.** Velocity would show as the blind window *widening* under load. It
narrowed to zero across the busiest two hours of the day.

**It is not a review problem.** A review failure is a defect that survives review. The last two
survived nothing — they were never committed as misses. And the one that *did* survive is the 40-hour
one from 09-04, which happened at low velocity, in a quiet window, and was caught by a different seat
two days later.

> ### ⛔ **IT IS A MISSING CONTROL, AND THE CONTROL IS NOT "REVIEW THE CHECK."**
>
> **It is: an instrument's SCOPE must be DERIVED from whatever declares reality, and a derivation that
> finds nothing must read UNCHECKABLE, never clean.**

`check-storage-keys.py` **reached that shape at 14:32 and now carries it in its own text** — the
recursive discovery at `:49`, and at `:71`: *"UNCHECKABLE — no household surfaces found; a scan that
finds nothing must never read as clean."* ✅ **The instance is closed.** The file even indicts itself in
three stacked comments, which is this corpus's best habit.

**What is NOT closed is the shape, and it has measurable siblings still in the un-generalised form.**
`wrangler.toml` declares **six** environments (top-level/legacy, `qa`, `lab`, `home`, `bob`, `paul` —
`grep -nE "^\[env\.|ESTATE_ID"`). Against that declaration:

| instrument | how it knows its scope | covers |
|---|---|---|
| `tools/pages-deploy.py:29-34` | hand map | ✅ **6 of 6** |
| `tools/read-onboarding.py:33-41` | hand map | **4 of 6** — no `bob`, no `paul` |
| `tools/journey-walk.py:284` | `choices=["qa","lab","home"]` | **3 of 6** |
| `tools/synthetic-identity.py:39-43` | hand map | **3 of 6** |
| `tools/check-estate-neutral.py:31` | `PAGE = estate/index.html`, **singular** | **1 of 5** shipped household surfaces, run standalone. *(The deploy gate walks the whole export, so the ENFORCED surface is complete — checked by reading `pages-deploy.py:118`. It is the session-start block's green that is narrower than it reads.)* |

> ⭐ **Four hand-kept environment rosters. One authoritative declaration. Zero derivation.** This is the
> same defect as the surface roster, one axis over — and **"the harness cannot target household
> origins" is not a separate carry-forward item, it is this item.** Both were fixed instance-by-instance
> today; neither was fixed as a shape.
>
> ⚠️ **The safe direction is worth naming:** the *deploy* paths are the complete ones and the *test and
> read* paths are the partial ones. That is the right way round for a leak, and the wrong way round for
> learning anything.

### 2.3 · What the gate is, and where it goes

**One check, small, in the session-start block:** `wrangler.toml`'s `[env.*]` blocks are the
environment roster; any tool holding an env→URL map that omits a declared env is flagged, with the
line. Zero declared envs = UNCHECKABLE, never clean.

⛔ **What I am NOT proposing: a rule that every roster must be complete.** `journey-walk` may have a
perfectly good reason never to walk `legacy`. **So it must CLASSIFY, not demand** — `qa-divergence.py`
already owns that pattern with `NOT_SURFACE`. A tool declares which envs it deliberately excludes; an
env in neither list is the finding. Otherwise the control is red forever the day someone adds an env
they never intend to walk, which is the one thing Paul's practice forbids installing.

**And the honest reason this is worth the file, stated plainly rather than as a scolding:**

> **The reason two of the three misses cost nothing is that the same author was in the same session and
> remembered.** That is not reproducible. Alignment does not accumulate across agent sessions — every
> spawn starts from what is written down, and today's two saves are written down only as three
> self-indicting comments in one file. **A control is what converts a session's memory into the
> project's.** The argument is not "you failed today"; it is *"today's saves do not survive the
> session."*

**Falsifier — and it is a clean one:** the next new surface or new environment that ships blind, where
the author does **not** catch it in-session, confirms the control was needed. If instead Paul overrides
a roster-drift flag twice as noise, the predicate is wrong and it should classify rather than flag.

---

## 3 · C · THE CASCADE UNDER ONE PRODUCTION ENVIRONMENT

### 3.1 · What a gate PASSING means now — and it is TWO clauses where it was one

My morning definition, which stands and is not enough:

> *A gate is PASSED when its walker met the build that the next gate will meet and their findings were
> dispositioned.*

Under one production environment, **a second clause becomes mandatory, because a new thing is under
test that was previously guaranteed by the deployment boundary:**

> ⭐ **A gate is PASSED when (a) its walker met the build the next gate will meet and their findings
> were dispositioned, AND (b) no other household's store changed while they walked — read before and
> after, not inferred from the walker not noticing.**

**Why (b) is new and not pedantic.** Today `home`, `bob` and `paul` are separate Workers with separate
KV namespaces. A gate-③ mistake **cannot physically reach** gate-⑤'s data; isolation is a property of
the infrastructure and no gate has to test it. In one production environment isolation becomes a
property of **50 call sites**, and the gate is the only place it gets exercised by a real journey.

### 3.2 · What becomes untestable until the conversion lands — precisely

| gate | clause (a) today | clause (b) today |
|---|---|---|
| ① synthetics | ✅ testable, and testing | ⛔ **untestable** — four seats, four estates, and on `qa` they share `est-qa0001` by deployment, not by grant, so a "leak" there is the intended behaviour |
| ③ Paul in production | ✅ testable **as a single-household walk** | ⛔ **untestable** — nothing else lives in his deployment to leak into |
| ⑤ Mom | ✅ | ⛔ same |
| ⑥ Bob | ✅ | ⛔ same |

> ⛔ **THE STRUCTURAL CONSEQUENCE, and it is the sharpest thing in this file: under the new shape the
> conversion is UPSTREAM of gates ②–⑥, not parallel to them.**
>
> **Not because it matters more — I do not rank.** Because clause (b) has no failing case available
> until it lands, so every gate run before it produces evidence that is silent on the exact dimension
> the new architecture introduces. **A gate ③ passed today and a gate ③ passed after the conversion are
> different gates wearing the same name.**

### 3.3 · Paul walks a household that will be migrated — and his own ruling settles it

Paul ruled today: **evidence EXPIRES when the build moves.** A migration is a build move of the most
consequential kind — it moves the *data*, not the code. So:

> **His gate-③ evidence expires at migration, by his own rule. Unless the migration is the thing under
> test — in which case it is a better gate than the one he would otherwise get.**

⭐ **So walking now is not wasted, and this is the constructive half:** an empty estate cannot be
migrated, and a migration with nothing to lose proves nothing. **His walk is the only way to have
something whose survival is worth asserting.** The method requirement is that the corpus record **two**
gates, not one:

| | what it asserts | expires |
|---|---|---|
| **③-pre** | the journey works, at his real conditions, in production | at the conversion — **by construction, and stamped that way when it is recorded** |
| **③-post** | **his answers, his ranking, his place name and his colour survived the conversion intact** | when the build moves again |

⛔ **Only ③-post is about the product's tenancy.** Recording them as one gate is how a re-walk that
finds a defect gone becomes indistinguishable from a re-walk that never met it — the corpus's dominant
failure shape, already named at §5.2 of the morning audit.

### 3.4 · ⭐⭐ SHARED HOUSEHOLDS — and the record already holds this question, ruled, three days ago

**⚠️ This is the finding I most want read, and it is not the one I expected to write.**

`git grep` across tracked `.md` for the concept returns **four hits, all pre-dating today**, and two of
them are a dated ruling:

| where | what it says |
|---|---|
| `.engineering/2026-09-03-onboarding-model.md:525` | *"⭐ **What a FAMILY door means** — Q11. Shared household hub, or an address several private views sit behind. That decides the menu, and it is a product stance, not a mechanism."* |
| `:605` | **`## ✅ RULED — Q11, what a menu renders [paul-stated 2026-09-03]`** → *"a menu renders THIS VIEWER'S GRANTS."* |
| `:625` | ⛔ *"**What this closes:** the alternative was a coherent, different product — **a family door as a shared household hub** — and it is now **declined, not deferred.**"* |
| `:632` | **`### ⭐ Q11 SHARPENED — family membership is NOT a source of access [paul-stated 2026-09-03]`** → *"it should not render in an estate just because they're in that family somehow. They need to be invited."* |
| `:650` | *"he and Mom share a family and hold **disjoint** condos… Under this ruling the case needs no special handling at all — **it is simply two people with different grants**."* |
| `VOCABULARY.md:229` | the invariant, promoted: *"**A person's estates are exactly the grant rows minted for them — never a set derived from who they are related to.** There must be no code path, and no derivation, in which a family relationship produces or implies an estate grant."* |
| `.user-research/2026-09-03-setup-journey.md:118` | *"**An administrator can tell two people apart at one estate.** … it is **still unasked.**"* — tagged **`gap`**, three days old, untriggered |

**⛔ I report the collision and I do not resolve it, because resolving it is a product call.** Stated as
precisely as I can:

> **Two different things are called "shared household" in this project, and one of them is ratified
> while the other is explicitly declined — in the same paragraph, using the same words.**
>
> - **Reading A — two grants at one estate.** Bob's daughters as contributors at Bob's estate; Mom and
>   Paul both holding a grant at Fernwood. ✅ **Already ratified.** `VOCABULARY.md:48-50` defines
>   `grant` as *"the person↔estate edge"* with `relationship` a **set** and `capability` a **single
>   value** per edge; `VOCABULARY.md` §3f contemplates exactly this. **Nothing reopens.**
> - **Reading B — a family door rendering a union of the family's estates.** ⛔ **Declined 09-03**, on
>   two independently-converging arguments (privacy: the Worker's byte-identical 404 exists so a
>   response cannot be an existence oracle; capability: Paul's own — viewer-scoped is the *more*
>   expressive option). Re-opening it means building the family→estates map this project has declined
>   to build **twice**.

⭐ **On the most natural reading of Paul's sentence today — *"shared households between users"* — he
means A, and A is already his own ratified model. But that is my inference and it is exactly the kind I
am not allowed to bank.** What I *can* say without inferring anything:

> **The next session will not hear him say it. It will read `onboarding-model.md:625` and find
> "declined, not deferred."**

### 3.5 · ⭐ THE RULING YOU ASKED FOR — what a requirement arriving mid-conversion obliges, procedurally

**It obliges exactly one act, and it is one dated block of writing — not a ratification ceremony.**

⛔ **A spoken line absolutely MAY steer a build.** Paul rules by speaking constantly and half this
repo's doctrine is his verbatim; a seat that demanded a ceremony before he could redirect his own
project would be the performative failure this role exists to avoid. **That is not the issue here.**

**The issue is narrower and it is real:** *this specific phrase already carries a dated, ratified,
opposite meaning in the file the next session reads.* An ambiguity in a WORD is worse than a gap,
because a gap gets discovered and an ambiguity gets acted on.

**So, procedurally:**

| | |
|---|---|
| ✅ **Obliged, before the conversion is designed against it** | one dated block at `.engineering/2026-09-03-onboarding-model.md` §Q11 saying **which reading is live**. ⭐ **The model already exists in this repo and my own morning audit praised it: `engine/palette.json`, where the Fern rename kept the superseded ruling visible above the new one.** Same act, one file over |
| ✅ **The stamp: `paul-stated 2026-09-06 · OPEN — seats asked to weigh in`** | ⛔ **not `paul-ruled`.** He said *"I want y'all to weigh in on that, though."* **A line explicitly opened for argument is not a ruling, and stamping it as one is a fabrication the next session cannot detect.** This repo's stamp vocabulary already distinguishes these and nothing new is needed |
| ⛔ **NOT obliged** | touching `VOCABULARY.md`. Its §229 invariant may or may not be what changes, its own §6 governs how it changes, and writing a provisional line into the ratified vocabulary is precisely the drift it exists to prevent. **VOCABULARY moves after the reading settles, not before** |
| ⛔ **NOT obliged** | re-running anything, re-ratifying the cascade, or pausing the conversion. Reading A changes **nothing** in the ratified model |

### 3.6 · Does the cascade need a new gate SHAPE? Yes — and it is a pair, not a seventh gate

**A shared household is, by construction, a gate one seat cannot walk.** The thing under test is a
*relation between two walkers* — what each can see and do at one estate — not a property of one.

⚠️ **The harness cannot express it at all today.** `tools/synthetic-identity.py` mints one identity per
`role@env` (`.private/synthetic-identities.json` is keyed exactly that way, verified). **Every seat gets
its own account and, on a household deployment, its own estate.** There is no way for two seats to hold
grants at one estate.

> ⭐ **THE NEW GATE SHAPE — a PAIRED WALK, and its assertion is on the DIFFERENCE:**
>
> **Two seats, one estate, run as one unit. It PASSES when each seat's view matches its own grant, and
> FAILS in two directions that must BOTH be able to fire:**
> - **over-share** — the two views are identical, so the grant boundary did nothing;
> - **under-share** — one seat's write is invisible to the other, so a shared household is not shared.
>
> A gate that can only fail one way has proven half of nothing. This is the repo's own matched
> positive/negative control standard, applied to a journey instead of a function.

**⛔ Where it sits: at gate ①, with the synthetics. Not as a gate ⑦ at the end.**

The reasoning is sequencing, not priority: **it is the one gate shape that can be run entirely on
invented people and stay honest.** Every other gate needs a real person's real household. If the pair
gate runs after Bob, **the first two-person household in the system is a real family's**, and the
over-share failure mode is discovered by the person it happens to.

**Cost, stated because nothing here is free:** it needs `synthetic-identity.py` to mint an identity that
takes a grant at an estate another identity founded — a change to the identity model, not a new tool.
**That is engineering-partner's to design and I am not designing it.**

---

## 4 · D · `myhome-paul` AND `myhome-bob` — retire, keep, or migrate

### 4.1 · Measured live, 2026-09-06, with a User-Agent (the edge 403s UA-less requests)

| origin | serves | built | env / estate | walked | **behind HEAD (`efaae6b`)** |
|---|---|---|---|---|---|
| `myhome-paul.pages.dev` | `ebdf172` | **14:52 EDT** | `paul` / `est-d93508` | **never** | 2 commits |
| `myhome-bob.pages.dev` | `b784dc9` | **12:12 EDT** | `bob` / `est-9a74df` | **never** | ⛔ **20 commits** |
| `fernwood-home.pages.dev` (Mom's) | `c111417` | 09-05 23:31 | `home` / `est-e6696a` | Paul, 09-05 | 46 commits |

> ⭐⭐ **`myhome-bob` reproduced the deployment-per-household failure mode in two hours and forty
> minutes, on a brand-new instance, with nobody noticing.**
>
> My morning audit named silent sha-rot as the cost of option 2.3(a) and cited `home` (26 commits
> behind) as the precedent. **The precedent was not history. It happened again today, same day, faster.**
> No instrument reports which code any Worker is serving (§5.1 of the morning audit, still unchanged),
> so this was found by reading `qa-build.json` off the origin by hand.

### 4.2 · Under shared households they cannot express the requirement — and the proof is a surface built at 14:22 today

`homes/index.html` — **"the shelf"** — renders **this viewer's grants**. A grant is a row in **one
deployment's KV namespace**. Two deployments are two namespaces, therefore two disjoint grant sets,
therefore:

> **A person holding a household in `myhome-paul` and a household in `myhome-bob` has two accounts, two
> credentials, and two shelves — neither of which can list the other's household. Deployment-per-
> household does not merely fail to express shared households; it fails to express the shelf that
> shipped this afternoon.**

This is mechanical and checkable, not a preference. **Falsifier:** if a grant row can be resolved across
KV namespaces, this is wrong — and `worker.js`'s `grantFor` looks a grant up at
`keyFor(scopeOf(env), "grant", …)`, inside one namespace, which is the same wall slice ① recorded.

### 4.3 · What makes each option HONEST and what makes each a LIE — method, not preference

| option | HONEST if | A LIE if |
|---|---|---|
| **Retire** | the Pages projects, the KV namespaces, `[env.bob]`/`[env.paul]` in `wrangler.toml:152,183`, and **all five entries** across `pages-deploy.py`'s `PROJECT`/`BRANCH`/`ORIGIN`/`HOUSEHOLD` maps go **together**; and `est-9a74df` / `est-d93508` are recorded as founded-and-never-populated so they are not re-minted | **any artefact survives.** ⛔ **A URL that resolves is a promise.** `myhome-bob.pages.dev` is a name Paul could plausibly have sent to Bob; a live origin with no deploy path and no walker is `home`'s 26-commit rot with nobody even nominally watching |
| **Keep as test rigs** | they are **declared** rigs in a file; **the harness can reach them** — it cannot: `journey-walk.py:284` is `choices=["qa","lab","home"]`, and neither `synthetic-identity.py` nor `read-onboarding.py` has an entry for either; and **something fails when they go stale** | kept "just in case" with no walker and no staleness control. ⚠️ **That is today's state, and `myhome-bob` is already 20 commits of evidence for what it costs.** A rig nothing runs is not a rig; it is an unowned live origin |
| **Migrate** | ⭐ **both estates are EMPTY — verified: never walked, no account, no grant.** So "migrate" costs nothing and means nothing; it is a rename | it is **described** as migration work. **Migrating two empty estates manufactures a milestone.** ⚠️ And it teaches nothing about the real migration — Mom's populated `est-e6696a` — because a migration's entire risk is the data, and there is none here |

> ⭐ **The method claim, and it is reachability rather than preference: only two of the three are
> currently reachable at their honest cost.** Keep-as-rig is not free — it costs five map entries plus a
> staleness control that does not exist for any environment. Retire is a coordinated removal across two
> files. Migrate is a no-op that must not be reported as work.
>
> ⛔ **Which one is Paul's, and it turns on whether Bob's 09-07..09-10 window still stands — a date given
> to a person, which I cannot weigh.**

---

## 5 · E · CARRY-FORWARD, with today's additions

### 5.1 · Still open from the morning, re-measured

| # | item | state at `efaae6b` |
|---|---|---|
| **C1** | **Harness cannot target household origins** | ⛔ open — **and it is an instance of §2.2, not a separate defect.** `journey-walk.py:284` · `synthetic-identity.py:39-43` · `read-onboarding.py:33-41`, all against `wrangler.toml`'s six envs |
| **C2** | **Cycle chronicles behind head** | ⛔ open. `MOM-CYCLE-LOG.md` and `cycle/fleet/CYCLE-LOG.md` last written at `7a3a2cc` **09-06 00:31**; **44 commits since, 35 of them human.** ⚠️ **Predicate note: this repo holds TWO chronicle files, not four** — the "four" in the brief is `cycle-docs-check`'s cross-repo count, a different predicate, and both are true |
| **C2b** | ⚠️ **and the clearing mechanism is a hand-written assertion with no trigger** | `7a3a2cc`'s own text: *"The marker is an ASSERTION, not a measurement… overturnable by deleting this block."* It cleared the flag for 09-05/06 **at 00:31, before today's 35 commits existed.** So the same assertion must be re-made every day the repo moves without a lap. ⭐ **Second instance today of the same class as `qa-divergence`'s two back-merges: a control whose remedy has become a chore on someone else's clock** |
| **C3** | **Offsite verifier DOWN** | ⛔ unchanged. `launchctl list` → `com.paul.verify-offsite` exit **1**; `PermissionError: Operation not permitted: …/CloudDocs/Backups/git`. A TCC grant, not code → `/team-audit` |
| **C4** | **`handover` seat registered and unwalkable** | ⛔ open, and now **committed** (`synthetic-identity.py:55`), so it is a registered capability with **no instance** — `.private/synthetic-identities.json` holds none. **Same shape as `scopeFor`'s zero callers, and it was created deliberately for the one ranking option no seat had ever walked** |
| **C5** | **Auto-memory records a three-gate cascade** | ⛔ open, and ⭐ **the highest re-litigation risk on this list.** `feedback_release_cascade_persona_paul_mom.md:3`: *"three gates in order — synthetic persona in QA, then Paul in lab, then Mom."* **Wrong three ways now** — the count (six named today), the place (`Paul in lab`; gate ③ is production), and the shape (one production environment). **An agent tomorrow reads memory, not `.plans/`** |
| **C6** | **`.private/current-runs.json` does not exist** | ⚠️ open, and ⭐ **I am downgrading my own morning urgency on this.** `walk-integrity` now prints `🔴 THE NEWEST RUN IS REFUSED for: owner, wide-eyed` — **the derivation is visibly doing the job it was designed for**, on live data, the day it was ruled: a run that fell over did not become the authority by being late. **Derived-with-override is behaving as designed; the override is a fallback, and an untested fallback is a smaller debt than an unbuilt gate.** Paul's ruling 3 stands unamended by me |
| **C7** | `qa-divergence` red on a timer | ⛔ open, content call, declined |
| **C8** | `.plans/` stage enum | ⛔ open — **fifth instance.** One word |

### 5.2 · New today

| # | item | evidence |
|---|---|---|
| **N1** | ⛔ **The declared conversion inventory is unreliable.** `grep -c "scopeOf(env)"` → 55; **50 code, 5 prose**, four of which slice ① wrote itself | §1.0 |
| **N2** | ⛔ **No seat has a countable run at `ebdf172` or at HEAD.** Newest countable: `9112b4b` ×3, `6674a02` ×1; two seats' newest attempt refused | §0 |
| **N3** | ⛔ **`tools/deploy-worker.sh` gates nothing that could see a household**, takes no `--env`, and bare `wrangler deploy` targets the **legacy** estate. The conversion lives entirely in the file this script ships | §1.3 G4 |
| **N4** | ⚠️ **`check-estate-neutral.py` standalone covers 1 of the 5 shipped household surfaces.** The deploy gate covers all five (verified by reading `pages-deploy.py:118`). **The enforced surface is complete; the session-start block's green is narrower than it reads** | §2.2 |
| **N5** | ⛔ **`myhome-bob` is 20 commits behind after 2h40m**, with no instrument able to report it | §4.1 |
| **N6** | ⛔ **`.user-research/2026-09-03-setup-journey.md:118` has carried the shared-household question tagged `gap` for three days, unasked, with no trigger.** It came back today because Paul happened to say it — **not because anything surfaced it.** ⭐ *The process produced the right question, parked it correctly, and had no mechanism to return it when it became load-bearing* | §3.4 |

---

## 6 · FALSIFIERS

1. **§1.2** is wrong if a second household's request can reach a deployment before the grant-lookup change. I read `grantFor`'s lookup order from `worker.js` and from `79f426e`'s own message; I did not construct the request.
2. **§1.3 G2** is wrong if a `pending`-increase flag is overridden as noise twice. Then it is a nag and should classify, not flag.
3. **§2.2's ruling** is confirmed by the next surface or environment that ships blind with the author not catching it in-session; it is falsified if Paul overrides a roster-drift flag twice.
4. **§3.4** is wrong if Paul rules that "shared household" today means Reading B, in which case the 09-03 ruling is genuinely reversed and `VOCABULARY.md:229` moves with it. **I state both readings and pick neither.**
5. **§3.6's placement at gate ①** is wrong if a paired walk cannot be made honest with two synthetic seats — e.g. if the over-share failure only manifests against real cross-device credentials. Untested; I have no counter-example either way.
6. **§4.2** is wrong if a grant can resolve across KV namespaces. `grantFor` reads inside one; I did not test a cross-namespace lookup.
7. **§0's contradiction** is wrong if `walk-integrity` mis-parses a build sha. I re-read its ✅ lines directly and counted each sha against HEAD with `git rev-list`; both methods agree.

## 7 · WHAT I DECLINE

- **Whether the grant-lookup change happens this week.** §1.2 states that the conversion's falsifier arrives with it; the schedule against Bob's window is Paul's.
- **Which reading of "shared household" is live.** §3.4. Both are coherent products and only he wants one.
- **Retire / keep / migrate.** §4.3 states what makes each honest. The choice turns on a date given to a person.
- **The conversion's architecture, storage, and command surfaces.** engineering-partner's, in parallel, and nothing here designs them.
- **Ranking any open item against any other.** Not mine, ever.

## 8 · WHAT THIS FILE DID NOT DO

- **Did not read any production store.** No token exists for `home`, `bob` or `paul` (`read-onboarding.py:40`); the `reset-production-estate.py` dry run is still unrun, still punch-list row 1, now two days old.
- **Did not construct a two-household request.** §1.2's claim is read from source, not exercised.
- **Did not spawn a fresh session** to test §2's reachability claims. Measured by grep and by reading, as this morning.
- **Did not edit `CLAUDE.md`, `VOCABULARY.md`, `BACKLOG.md`, `onboarding-model.md`, or any plan's stage-note.** Flags, never edits.

---

## ⛔ PAUL MUST RULE — FOUR, ORDERED. Two are new; two are carried and **one carried item is dropped from the list**

⭐ **Dropped from the morning's list of five: #3 (derived-vs-human-stamped run authority).** `walk-integrity`
demonstrated the derived model working correctly on live data today (§5.1 C6). **It no longer needs your
attention; your ruling stands and I withdraw the question.** That is what makes room for #2 below.

| # | ruling | blocks | §
|---|---|---|---|
| **1** | ⭐ **WHICH "SHARED HOUSEHOLD" DO YOU MEAN?** (A) **two grants at one estate** — already ratified 09-03, nothing reopens, the conversion is designed against your existing model; or (B) **a family door rendering a union** — declined 09-03 in writing, and re-opening it means building the family→estates map this project has twice declined. ⚠️ **The same words already mean B in `onboarding-model.md:625`, so the next session will read "declined, not deferred."** One sentence settles it | the conversion's design, gate ⑦'s shape, and whether `VOCABULARY.md:229` moves | §3.4–3.5 |
| **2** | ⭐ **NEW — `myhome-paul` / `myhome-bob`: retire, or keep as declared rigs?** They cannot express shared households at all (§4.2), `myhome-bob` is already 20 commits stale after 2h40m, and **keep-as-rig costs five map entries plus a staleness control that exists for no environment.** ⛔ Migrate is a no-op on two empty estates and must not be reported as work | Bob's window; how §1's gates are exercised | §4 |
| **3** | **Does the grant LOOKUP move to second in the conversion order?** Everything before it is unfalsifiable by construction — no second household is reachable, so a converted site and an unconverted one behave identically. **Not a claim it matters more; a claim that slices before it buy code, not evidence** | every later slice's meaning | §1.2 |
| **4** | **The Bob window (09-07..09-10)** against a cascade whose ②/③ have not run and whose deployment shape you have now ruled against. **Carried unchanged from this morning; still yours; still the one I cannot weigh** | ⑥, and how ④ is scoped | morning §2.2 |

**Three cheap ones, one word each, not blocking:** the `.plans/` stage enum (**fifth** instance) · whether
C3 (offsite verifier, a TCC grant) hands to `/team-audit` · whether the chronicle "not-a-lap" assertion
gets re-made for today's 35 commits or the flag is accepted-and-documented.

**Not rulings — an agent can drive these unattended:** fix the `scopeOf` inventory predicate (one
`grep -v`) · add `bob`/`paul` to `read-onboarding`, `journey-walk` and `synthetic-identity`'s maps ·
mint the `handover` identity · run `reset-production-estate.py` with no flag · re-deploy `myhome-bob`
or retire it, per #2.

---
---

# ADDENDUM · 2026-09-06 evening — THE LEGACY ERA

**Appended, not merged. §§0–8 above are left exactly as written**, because the fact that the design
was made without this is part of the record and the most useful part of it: **§1 reasoned carefully
about 50 call sites and never once asked what the keys those sites build actually look like.**

**Written at `5ec0746`.** Every claim below re-derived from source; nothing taken on report.

## A0 · WHAT I VERIFIED, AND TWO THINGS I HAVE TO CORRECT

✅ **The finding stands, and it is worse-shaped than a defect.** `worker.js:695` —
`return date < scope.legacyBefore ? \`${kind}:${date}\` : keyFor(scope, kind, date);` — routes by the
**record's** date, reads and writes alike. `blobKey` (`:704`) is the same shape.
`python3 tools/check-household-isolation.py` at `5ec0746` reproduces exactly what was briefed:
`production` (2026-09-04) and `qa` (2026-09-03) each share **one unprefixed key across households on
19 kinds**; `bob`/`home`/`lab`/`paul` at `1970-01-01` are clean.

✅ **Six environments, six DISTINCT KV namespace ids** (`wrangler.toml:14, 56, 106, 137, 167, 193`).
The correction to my §1.3 G3 is right and it is the coordinator's to have made: a `bob`-vs-`paul`
store diff is **guaranteed by the boundary the conversion exists to stop relying on**, so it proves
nothing. **The gate survives; its target was wrong and is now two prefixes in one namespace.**

⭐ **Second-method check on the checker's own declared blind spot, because an unknown is never
counted healthy.** It reports *"1 kind built from a variable, so NOT covered: `OBS_KEY`"*. Read at
source: `worker.js:314` `const OBS_KEY = "observations"`, used at `:871` and `:882` through
**`keyFor(scopeOf(env), OBS_KEY)` — never `dateKey`.** ✅ **Observations have no legacy era at all**;
they are always estate-prefixed. **The caveat resolves clean, and 19 is the whole set.** *(They are
still two of the 50 pending conversion sites — a different axis.)*

### ⚠️ Correction 1 — the escape hatch is not the one named in the brief

> *"it is the one step where 'delete the namespace' is still available as an escape hatch."*

**Not for the namespace that matters.** `100f2b95…` (top-level) holds **Mom's entire May→09-04
history**. Deleting it is not an escape hatch; it is the loss.

**What is actually reversible today, and it is better:** ⭐ **the bare keys are untouched and a copy is
purely additive.** `worker.js:707` already says so — `listBothEras` *"is a union of what exists, not a
lookup that could mask a miss — so legacy keys stay visible until the separate deletion"* — and
`:644`: *"Unprefixed keys are DELETED in a separate later act, never here."*

> **The repo already designed the safe shape and wrote down that it is TWO acts. Nobody has ruled it.**

### ⚠️ Correction 2 — my §1.2 claim was scoped, and I did not say so

I wrote *"nothing before the grant lookup is falsifiable."* **That claim was about the conversion of
call sites. Read as a claim about the programme, it is wrong, and the omission is mine.** A data
migration is not a call-site slice and was never inside it. **§A2 says why that does not rescue the
inference the brief drew from it.**

---

## A1 · Q1 — SLICE, OR PREREQUISITE?

⛔ **Neither, as stated. It is a PREREQUISITE OF THE MERGE, not of slice ②, and it is TWO ACTS with a
gate between them.**

**Three separations, each mechanical:**

**(i) It is not a slice, because a slice has a next slice and this has a point of no return.** Every
other unit in §1.1 is reversible by reverting a commit. Moving `LEGACY_BEFORE` and deleting bare keys
is not revertible by git. **The ordering rule that governs slices — *identity doors last* — is a rule
about code and does not reach data.**

**(ii) It gates the MERGE, not slice ②.** Slice ② converts readers; the deployment binding still
supplies the estate, so **no second household enters the namespace.** What admits a second household
is the *merge*. So the re-key must precede the merge and **need not precede slice ②** — which
matters, because putting it before ② stalls the conversion behind a data migration that the
conversion does not require.

**(iii) ⭐ It is two acts, and only the second is a gate** — the shape `worker.js:644` and `:707`
already describe:

| act | reversible? | what it is |
|---|---|---|
| **copy** every bare `kind:date` to `est-…:kind:date`, bytes identical, **bare keys left in place** | ✅ **fully** — additive, and `listBothEras` already unions both prefixes so nothing changes for a reader | not a gate. An agent can run it, verify it, re-run it |
| **close** — move `LEGACY_BEFORE` to `1970-01-01` and delete the bare keys | ⛔ **no** | ⭐ **the gate.** Paul's standing doctrine already places it: *the gate sits on irreversible acts, never on work* |

> ⭐ **This is why "slice or prerequisite" was the wrong question shape, and saying so is the useful
> part: the act everyone is worried about is the second one, and it is not a migration step at all —
> it is a deletion.** The migration half is safe, resumable, and needs no ruling.

---

## A2 · Q2 — DOES IT CHANGE THE ORDERING ANSWER? ⛔ NO, AND "FALSIFIABLE" IS THE WRONG REASON

**My scoped claim is unamended** (§A0). But the inference drawn from it — *the re-key is falsifiable
today, so it may be the one early slice that produces evidence* — **does not hold, and the reason is
the one this repo pays for most often.**

> ### ⛔⛔ `check-household-isolation.py` GOES GREEN IN THE STATE THAT LOSES MOM'S HISTORY.
>
> It reads `LEGACY_BEFORE` from `wrangler.toml` and reports a **live legacy window**. Setting
> `LEGACY_BEFORE = "1970-01-01"` turns it ✅ **instantly, with zero bytes moved** — and every
> pre-09-04 record becomes unreachable by point lookup, because `dateKey` would then compute
> `est-3c9f1a:kind:2026-05-15` for a record stored at `kind:2026-05-15`.
>
> **Green-after-a-correct-re-key and green-after-a-one-character-edit-that-strands-eight-months are
> the same observation.** *X and not-X*, on the control built today to catch this class.

⛔ **This is NOT a defect in the checker and I am not filing it as one.** Its own output says exactly
what it measures: *"THIS IS A CONSTRAINT ON THE MERGE, NOT A DEFECT IN THE CODE."* It measures the
**merge constraint**, faithfully. **The error would be reading it as a PROGRESS signal for the
re-key**, and that is the reading the brief proposes.

**So the ruling, and it generalises:**

> **Falsifiability is a good reason to move a CODE slice earlier and a bad reason to move a DATA
> migration earlier — because for data the falsifier must be the DATA, never the config that routes
> to it.** A config value is a claim about where bytes are; only a count of bytes is evidence.

**The re-key's honest falsifier does not exist yet and is small:** *every bare `kind:date` in the
namespace has a prefixed twin with identical bytes* — counted **before** anything is deleted and
**before** `LEGACY_BEFORE` moves. It needs a live KV read, which is exactly the read door that does
not exist for `home` (§5.1 C6 of the morning audit, still open).

⭐ **And it has a free negative control**, which this repo's standard requires: run it *before* the
copy and it must report the full count missing. **A twin-count that has never been seen red has
proven nothing.**

**Where the re-key sits is therefore set by the irreversibility gate (§A1), not by its
falsifiability.** ⛔ **Whether R3's store diff or the re-key's copy runs first is a sequencing call
between two things Paul has now ruled onto the near path; I decline it** — it turns on how much
session time he has before the merge, which only he knows.

---

## A3 · Q3 — WHICH NAMESPACE IS "PRODUCTION"? ✅ DETERMINED, AND THE ANSWER IS THAT THE WORD NAMES TWO DIFFERENT THINGS

**Not UNCHECKABLE. The record settles it, three independent ways.**

`viewer.html:7041-7043` — the file Mom loads:

```js
const WORKER_BASE = IS_PREVIEW_ORIGIN
  ? (PREVIEW_KNOWN ? PAGES_WORKERS[PAGES_LABEL] : "")
  : "https://fernwood.paul-kirschenbauer.workers.dev";
```

She loads `palekxk.github.io/Tate-Tracker/viewer.html`. `palekxk.github.io` fails `/\.pages\.dev$/`,
so `PAGES_LABEL = null` → `IS_PREVIEW_ORIGIN = false` → **the top-level Worker.** The block's own
comment agrees: *"Non-preview origins (GitHub Pages, a custom domain, a local file) are untouched and
still resolve to production."*

**Second method** — `viewer.html:7028`: *"⚠️ `fernwood-home` is **MAPPED BUT NOT YET SERVED THIS FILE**
(2026-09-05). The home origin carries the onboarding page only; **this viewer is NOT in its deploy**."*
**Third** — `pages-deploy.py:50`'s `HOUSEHOLD_ALLOW` does not contain `viewer.html`.

| | **the app Mom uses daily** | **the destination the cascade calls production** |
|---|---|---|
| origin | `palekxk.github.io/Tate-Tracker/viewer.html` | `fernwood-home.pages.dev` |
| Worker | `fernwood.…workers.dev` (top-level) | `fernwood-home.…workers.dev` |
| estate | `est-3c9f1a` | `est-e6696a` |
| **KV namespace** | **`100f2b95…`** | `79464451…` |
| `LEGACY_BEFORE` | ⛔ **2026-09-04 — live legacy era** | ✅ 1970-01-01 |
| history it holds | ⭐ **May → 2026-09-04, unowned, 19 kinds** | **none. It is empty** |
| `ENV_NAME` | **`"production"`** (`wrangler.toml:25`) | `"home"` |

> ⭐⭐ **`home` is not clean because it was built well. It is clean because it is EMPTY** — a 09-05
> deployment serving the onboarding page only. **`est-e6696a` has never held one of Mom's records.**
>
> ⛔ **And the unpaid rename is what made this question hard.** My morning audit's §5.2 flagged
> `ENV_NAME = "production"` still bound to the legacy estate. **The environment literally named
> `production` is the legacy one; the one the cascade calls production is named `home`.** A
> bookkeeping debt filed as cosmetic turned out to be sitting on the identity of the merge target.

**⛔ Which namespace the merge uses is Paul's, and it is the SAME DECISION as F5's sentence.** The
structural costs, stated and not ranked:

| target | what it costs, structurally |
|---|---|
| **`100f2b95…` / `est-3c9f1a`** (Mom's incumbent) | Mom never migrates; her app already points here. **Pays the full re-key on a live household**, and the reversible window (§A1) is the only safety it has |
| **`79464451…` / `est-e6696a`** (`home`) | No re-key — there is no legacy era. But **Mom's entire May→09-04 history migrates ACROSS namespaces**, which is strictly more than a re-key within one, **and her app must be repointed** |
| ⭐ **a third, empty namespace** — named because nobody has | Both households migrate; **nobody has an incumbency advantage**; and it is the **only option under which "delete it and start again" stays available through the whole merge**, because it holds nothing anyone would miss. Costs two migrations instead of one, and a repoint |

⛔ **I decline the choice.** It trades Mom's app being repointed against a live re-key, and both halves
are real-world context. **What is method: the third option is the only one that preserves an escape
hatch, and it had not been named.**

---

## A4 · Q4 — DOES ③ NEED A THIRD CLAUSE? YES — AND IT IS NOT A WALK CLAUSE

§3.3 split gate ③ into **③-pre** (journey) and **③-post** (survived the tenancy conversion). The
re-key is a change to the **key space under the same records**, so:

> **③-post splits again: (i) his answers survived the CODE conversion; (ii) his answers survived the
> RE-KEY.**

⭐ **But (ii) must NOT be written as a clause a walker can pass, and this is the whole of the answer:**

> **A walk cannot prove a re-key.** A walk shows what the app renders. A re-key's failure mode is *a
> record that still exists under the old key and is no longer reachable* — and **the app renders
> "nothing here" identically for *never written* and *written and now unreachable*.** Putting clause
> (ii) on the walker makes it unfalsifiable by the walker, and it would pass.

**So clause (ii) is a COUNT, taken outside the app, before and after: every legacy key has a prefixed
twin with identical bytes** (§A2's instrument, the same one). ⛔ **Only the count may close it; a
green walk is not evidence for it and must not be recorded as if it were.**

⭐ **This is Paul's own "evidence expires when the build moves," meeting a build move no walk can
measure** — and it is the first one. Every prior expiry was a code change a walker could meet.

---

## A5 · WHAT THIS ADDENDUM ADDS TO THE CARRY-FORWARD

| # | thing | evidence |
|---|---|---|
| **N7** | ⛔ **`check-household-isolation.py` exits 0 while printing ⛔ on two environments.** Correct today (it is a merge constraint, not a live defect) — but it means **the constraint it names is the one thing it cannot enforce.** It needs a mode that exits nonzero when a namespace with a live legacy era is the merge target, or it is a document. **Fourth instance of flags-and-exits-0** after `check-backlog-ready` | run at `5ec0746` |
| **N8** | ⚠️ **The household surfaces default to the TOP-LEVEL Worker off `*.pages.dev`.** `estate/index.html:202-204`, same in `onboarding/` and `homes/`: not a `.pages.dev` host → `https://fernwood.paul-kirschenbauer.workers.dev`. ⭐ **The C4 custom-domain move would therefore point every household surface at `100f2b95…` — the namespace with the live legacy era.** Latent, not live | read at source |
| **N9** | ✅ **`OBS_KEY` resolved clean by a second method** — `keyFor`, never `dateKey`, so observations have no legacy era. An `unknown` converted to a `clean` rather than counted as one | `worker.js:314, 871, 882` |

---

## A6 · FALSIFIERS FOR THIS ADDENDUM

1. **§A2's central claim** is wrong if `LEGACY_BEFORE = 1970-01-01` leaves pre-09-04 records reachable by point lookup. I read `dateKey`'s branch; **I did not execute it against live KV**, and no read door exists for `home` to do so.
2. **§A3** is wrong if Mom loads Fernwood from somewhere other than `palekxk.github.io` — a bookmark to a `.pages.dev` host would resolve differently. I read the resolution logic and two corroborating comments; **I did not read her device.**
3. **§A1's two-act split** is wrong if `listBothEras` does not cover every read path a household needs during the window. It is a **listing** union (`worker.js:707`); a point lookup during the window still routes by date, which is why the bare keys must stay.
4. **§A4** is wrong if a walker can distinguish *never written* from *unreachable*. I know of no surface that renders the difference.

---

## ⛔ PAUL MUST RULE — RESTATED · THREE, ORDERED

⭐ **All four items from §"PAUL MUST RULE" above are DISCHARGED at `8bbe8a5`** — shared-household
reading (A, verified), the household rigs (R2, kept), conversion order (R3, reconciled), Bob's window
(R1, held with a release condition). **This addendum displaces nothing; the previous list is empty.**

| # | ruling | why now |
|---|---|---|
| **1** | ⭐ **WHICH NAMESPACE IS THE MERGE TARGET — and it is the same decision as F5's sentence, so answer them as one.** Mom's incumbent `100f2b95…` (no migration for her, full live re-key) · `home`'s `79464451…` (no re-key, but her history crosses namespaces and her app repoints) · **a third empty one — the only option that keeps "delete it and start again" available through the merge, and nobody had named it.** ⚠️ **`home` is clean because it is EMPTY, not because it is ready** | blocks the merge, the re-key's target, and whether the legacy viewer stays put |
| **2** | **CONFIRM the re-key is TWO acts with your gate on the second** — copy (additive, reversible, agent-drivable, bare keys untouched) then close-and-delete (irreversible). ⭐ **Your own doctrine already answers this** — *the gate sits on irreversible acts, never on work* — and `worker.js:644` already says the deletion is *"a separate later act."* **This needs a yes, not a deliberation** | blocks nothing if you say yes; blocks the copy if the split is wrong |
| **3** | **R1's release condition, carried from `2026-09-06-one-environment-DECISIONS.md` §4** — *Bob is released when one production environment is live AND the paired-walk gate (T2) has passed on synthetics.* Needs your yes or a different trigger | Bob |

**Cheap, one word each, unchanged and still unruled:** the `.plans/` stage enum (**fifth** instance) ·
whether the offsite verifier hands to `/team-audit` · whether the chronicle "not-a-lap" assertion is
re-made for today's 35 commits.

**Not rulings — an agent can drive these unattended:** build the twin-count instrument (§A2) **with its
negative control run first** · give `check-household-isolation.py` a nonzero merge-gate mode (N7) ·
mint a read token for `home` so the twin-count has a door at all · pay the `ENV_NAME = "production"`
rename that made §A3 hard to answer.

---

# ADDENDUM 2 · 2026-09-06 late — PAUL RULED THE TARGET, AND THE TARGET IS NOT EMPTY

**⛔ Re-key work STOPPED. §§A1, A3 and A4 are superseded by his ruling and are left standing as the
record of what was designed before it.** ✅ **Q1, Q3 and Q4 of the previous brief are correctly
withdrawn — there is nothing to sequence, nothing to determine, nothing to gate.**

---

## B1 · ⛔⛔ "HOME IS A BLANK SLATE" IS CONTRADICTED BY THE RECORD — SAYING THIS LOUDLY, AS ASKED

**You asked me to say so if my reading contradicts it. It does, and the file that contradicts it was
written by this project about itself.**

`.private/synthetic-production-manifest.json`, mtime **2026-09-05 21:42**, its own first line:

```
"note": "synthetic rows written to PRODUCTION (est-e6696a). Remove before Mom's invite."
```

**Four accounts, named, with personIds and creation timestamps:** `syn-owner-0151` ·
`syn-mom-d940` · `syn-wide-eyed-ddcd` · `syn-strict-b1c8`. Corroborated independently by
`.private/synthetic-identities.json`, which holds `owner@home`, `mom@home`, `wide-eyed@home`,
`strict@home` with matching personIds.

**And `walk-integrity` records THIRTEEN runs against `home` on 2026-09-05** (builds `090a42a` and
`bce212a`) — 3 mom, 4 owner, 3 strict, 3 wide-eyed. ⚠️ **All refused, and that is about the REPORT
artifact, not the app.** `report-unwritten` means nobody wrote a REPORT.md; **it does not mean the
walk failed to drive the onboarding flow and post answers.** `answers=unrecorded` means the run did
not record *which answer file* it used — not that nothing was written.

| what `est-e6696a` holds | state |
|---|---|
| **4 synthetic accounts** | ⛔ **named and removable** — the manifest is exactly the artifact for this |
| **their 4 grants** | ⚠️ **not named anywhere.** `handleAccountCreate` writes an account row *and* a grant row; the manifest records only `"kind": "account"` ×4. **A leftover grant row is a live credential** |
| **answer rows from 13 walks** | ⛔ **UNKNOWN, and unknowable from here.** No read token for `home` exists (`read-onboarding.py:40`), and those walks **pre-date run identity** (`bb21863`, this afternoon), so nothing on the rows says they are ours |

> ⭐⭐ **THE STAKES INVERTED WITH HIS RULING, AND THAT IS THE WHOLE FINDING.** Yesterday `home` was a
> staging deployment and synthetic junk in it was bookkeeping. **Today `home` IS Mom's blank slate —
> the live production environment.** The same four rows are now **live credentials in production**,
> and the manifest's *"Remove before Mom's invite"* moved from a tidy-up note onto the critical path
> without anyone touching it.
>
> ⚠️ **`home` is not clean and it is not dirty — it is `unknown`, and this repo never counts `unknown`
> as healthy.** Two of the three rows above can be settled by an agent; the third cannot be settled at
> all until a `home` read token exists.

⭐ **This is my morning §2.4 landing, inverted.** I wrote then: *"a synthetic ANSWER is findable; a
synthetic ACCOUNT and its GRANT are not."* **It is now the other way round** — the accounts are named
by the manifest, and the answers from those 13 walks are the unfindable half, because the marker that
would identify them shipped six hours after they ran.

**⛔ I am not calling this a reason to reopen the merge target.** His ruling settles which namespace.
**It is a reason that "production starts empty" is a promise nobody has verified**, and the dry run
that would verify it — `python3 tools/reset-production-estate.py` with no flag — has now been punch-list
row 1 for **two days**, blocked once by the sandbox and unrun since.

**Falsifier, and it is cheap:** mint `fernwood-token-home`, run `read-onboarding.py --env home`. If it
returns zero rows, the answer half of this finding is wrong and only the accounts and grants remain.
**Until that runs, `home`'s contents are `unknown` and must be reported that way, not as empty.**

---

## B2 · Q2 NARROWED — ✅ CONFIRMED, ORDERING RULING UNCHANGED

**Your reading is correct on both halves and I confirm it.**

**Nothing before the grant lookup is falsifiable, and the removal of the migration does not touch that
claim** — it was always scoped to call-site conversion (§A0, Correction 2), and the migration was never
inside it. Removing something that was outside a claim leaves the claim where it was.

✅ **And the isolation checker is an instrument standing ready, not an early source of evidence** —
which is exactly what §A2 argued and what its own output says (*"a constraint on the MERGE, not a
defect in the code"*). ⭐ **With the re-key gone, §A2's central warning also goes quiet rather than
being answered:** there is no longer a config edit that could turn it green while stranding data,
because `home` has no legacy era to strand. **The warning was correct and is now moot. Both are true
and it is worth recording which.**

⚠️ **One live consequence survives, and it is `check-household-isolation.py`'s own output:** `qa` still
binds `LEGACY_BEFORE = 2026-09-03` and still reports ⛔ on 19 kinds. **QA is where gate ① runs.** So
the paired-walk gate (T2) will be exercised in an environment that *has* the shared-legacy-era
condition, against a production environment that does not. **That is not a defect; it is a fixture
mismatch, and a fixture that differs from production in the exact dimension under test is worth
knowing before T2's result is trusted.** → engineering-partner; I state it, I do not design it.

---

## B3 · BOB — the release condition simplifies, and R1's second clause should stay

His ruling: *"He hasn't even been set up in the system. He would need to set himself up."* So nothing
is pre-created, `myhome-bob` never holds his data, and **the export/restore round-trip is not on his
path at all.**

⭐ **One method note, and it is the only thing I would argue for keeping:** R1's condition had **two**
clauses — *one production environment exists* **AND** *the paired-walk gate (T2) has passed on
synthetics*. The new framing states only the first. **Dropping the second makes Bob the first
two-person-capable household anyone meets**, which is precisely what §3.6 argued against on sequencing
grounds: the over-share failure mode would be discovered by the person it happens to.

⛔ **Whether T2 stays in the condition is Paul's** — it trades a date against evidence and I cannot
weigh the first half. **What is method: if it is dropped, it should be dropped deliberately and
recorded, not lost in a restatement.** That is the whole of my ask here.

---

## B4 · ⭐ `live` / `legacy` / `artificial` — WHERE IT IS DECLARED, AND WHY THE STALENESS CONTROL RETIRES

### B4.1 · Where the status is declared

**⭐ `worker/wrangler.toml`, as `ESTATE_STATUS` in each `[env.*.vars]` block — and this is the same
answer as §2.2's, arrived at from the other side.**

| why there | |
|---|---|
| **It is already the authoritative declaration** | §2.2 measured it: six `[env.*]` blocks, and **four tools hand-copy it** (`pages-deploy` 6/6, `read-onboarding` 4/6, `journey-walk` 3/6, `synthetic-identity` 3/6). Adding a fifth hand-kept list somewhere else is the defect this file spent §2 on |
| **It sits beside the facts it qualifies** | `ESTATE_ID` and `LEGACY_BEFORE` are already per-env vars in that block. A status that lives anywhere else can disagree with the id it describes |
| ⭐ **It becomes derived for free** | `/health` already returns `env · kv_canary · estateId · legacyBefore · budget`. One field and **every environment reports its own status by use**, which is the only reading that cannot drift from the binding |
| ⭐⭐ **It retires the naming trap, and that trap has now cost twice today** | `wrangler.toml:25` still binds `ENV_NAME = "production"` to the **legacy** estate. That unpaid rename is what made §A3 hard to answer and it is `2026-09-06-one-environment-DECISIONS.md` F4. **A declared status ends the inference from a name** — `legacy` is a field, not a guess about what `ENV_NAME` meant |

**Applied:** `home` → `live` · top-level `fernwood` → `legacy` · `bob`, `paul`, `lab` → `artificial` ·
`qa` → ⛔ **the one that does not fit, and I will not force it.** QA is not artificial (real gate-①
evidence comes from it), not legacy, and not live. **Report, do not resolve** — a fourth word, or `qa`
declared `artificial` with its evidence role stated separately, are different answers and both are
Paul's. ⚠️ **The enum's first real test is the environment it was not coined for**, which is the normal
way a vocabulary finds its edge, and `VOCABULARY.md` §6 governs what happens next.

### B4.2 · ⛔ The staleness control does NOT apply to `artificial` — RETIRE IT

**You were about to build it. Don't. The label does the work, and I am withdrawing my own §4.3 line
that made it the price of keeping the rigs.**

Ask what harm a staleness control prevents, and both candidates dissolve:

| harm | under `artificial` |
|---|---|
| **a real person loads an old build** | ⛔ **cannot happen by definition** — nobody is sent to an artificial origin. That is what the label declares |
| **a walk produces evidence at a build we think is current** | ⭐ **real — and already controlled.** `walk-integrity` records the build sha per run, and Paul ruled today that **evidence expires when the build moves.** The control exists, it ran in §0 of this file, and it is the reason we know no seat walked `ebdf172` |

> **So a staleness control on an artificial deployment would fire whenever a rig has not been
> redeployed — which for a rig is the NORMAL state, since you deploy it when you want to walk it.**
> **That is a control red on a timer, and Paul's own practice forbids installing one.** It is also the
> third instance today of that shape, after `qa-divergence`'s two back-merges and the chronicle
> not-a-lap assertion.

⭐ **The honest replacement is a sentence, not a control:** *a walk against an artificial origin
deploys first, or records the sha it actually met.* **The second half already happens.** ⛔ **`myhome-bob`
being 20 commits behind is not a defect once it is labelled `artificial` — it is the expected state of
a rig between walks, and my §4.3's "keeping the rigs without this control is keeping a lie" was wrong.
The label is what makes it honest; a control was never what would.**

⚠️ **One residual that is NOT staleness and should not be swept into it:** `myhome-bob` is a public
resolving URL whose *name* reads like a person's household, and under his new ruling **it will never
hold Bob's data.** An artificial deployment named after a real person is a name someone could
plausibly send. **Naming is content-steward's and Paul's, not mine** — I note only that the label and
the hostname now say different things.

**Falsifier for B4.2:** if a walk is ever run against an artificial origin and its findings are acted
on *without* anyone checking the recorded sha, the sha stamp was not sufficient and a deploy-time gate
is owed after all. That is observable in the walk corpus.

---

## ⛔ PAUL MUST RULE — RESTATED · TWO, ORDERED

⭐ **All three items from Addendum 1's list are DISCHARGED:** the merge target is ruled (`home`; the
current `fernwood` stays as it is, data intact), the re-key is withdrawn, and R1's release condition is
answered. **This list is new, and B4 retires work rather than adding it.**

| # | ruling | why it is yours |
|---|---|---|
| **1** | ⭐ **`home` IS NOT EMPTY, and "production starts empty" is now a promise nobody has verified.** It holds **4 named synthetic accounts** (removable), **4 unnamed grants** (live credentials), and **an unknown number of answer rows from 13 walks** that pre-date run identity and sit behind a read door that does not exist. **Does the cleanup gate Mom's invite — and if the answer rows cannot be told from hers, does the promise move instead?** ⚠️ The manifest's *"Remove before Mom's invite"* is an **agent-written line, not your ruling** | it is your sentence about what you are handing her, and only you can weigh a promise against a delay |
| **2** | **Confirm `ESTATE_STATUS` in `wrangler.toml` is where the three-way status lives** — beside `ESTATE_ID` and `LEGACY_BEFORE`, reported by `/health`, so it is derived by use and never typed twice. ⛔ **And rule the one that does not fit: `qa` is neither live, legacy, nor artificial** — a fourth word, or `artificial` with its evidence role stated separately | a vocabulary promotion, and `VOCABULARY.md` §6 is yours |

**One thing I am asking you NOT to decide, because it should not cost you a thought:** the staleness
control for the rigs. **B4.2 retires it. Labelling them `artificial` is the fix; `walk-integrity`'s
build stamp already covers the only harm that survives the label.**

**Cheap, one word each, still unruled and now three days old on the first:** the `.plans/` stage enum
(**fifth** instance) · whether the offsite verifier hands to `/team-audit` · whether the chronicle
"not-a-lap" assertion is re-made for today's commits.

**Not rulings — an agent can drive these unattended, and the first one unblocks ruling #1:**
mint `fernwood-token-home` and run `read-onboarding.py --env home` · run
`reset-production-estate.py` with **no flag** (punch-list row 1, **two days old**) · extend the
manifest to name the four **grants**, not only the accounts · pay the `ENV_NAME = "production"` rename
that has now cost twice in one file.

---

# ADDENDUM 3 · 2026-09-06 night — AUDIT: ARE THE GATES AND THE CASCADE CLEAR?

**MODE: audit.** Written at `2a476f4` with a mint dry-run held on screen. Paul: *"be sure that our
release gates and cascade and intentions are clear."*

## ⭐ THE HEADLINE, FIRST, BECAUSE HE WANTS TO WALK TONIGHT

> **He can walk now. The production-synth question is separable, and on the evidence below it should
> be dropped from tonight entirely — not deferred, dropped.** ⛔ **Do not mint the grants.** The gate
> you are about to quiet is firing for a bookkeeping reason, and quieting it would put a consent
> record into the register that answers a question nobody asked.

**And the honest answer to the question Paul caught you on — did the synthetics onboard in
production, in Chrome, with a UX review — is that "no" is only half the story. The other half is that
NOTHING WROTE DOWN WHAT "TESTED" MEANT, so there was nothing for the answer to be measured against.**
That is §D4, and it is the audit's actual finding.

---

## D1 · Q1 — ⛔ YOU ARE NOT ABOUT TO LAUNDER A CONSENT GATE. YOU ARE ABOUT TO QUIET A BROKEN ONE

**Measured by execution, not by reading.** `grant-mint.py`'s `gated()` loaded against the live
register (`~/Developer/fernwood-private/grants.json`):

```
administrators(reg) = ['p-7f3a2c', 'p-dev-synth-owner', 'p-paul', 'p-paul-home', 'p-vfy']

  gated(est-3c9f1a) = True      gated(est-e6696a) = True
  gated(est-qa0001) = True      gated(est-d93508) = True
  gated(est-lab0001) = True     gated(est-9a74df) = True
```

> ⛔⛔ **G2 IS ARMED AT EVERY ESTATE IN THE REGISTER — INCLUDING THE TWO WHERE PAUL DEMONSTRABLY HOLDS
> `administrator` + `relationship: ['owner']`.**

**Why**, from `grant-mint.py:118-129`: `gated()` iterates **every** administrator personId and returns
`True` if **any one of them** lacks a row at that estate. The register holds **five** administrator
ids, and **at least three of them are Paul** — `p-7f3a2c` (the frozen Fernwood), `p-paul`
(production), `p-paul-home` (the artificial rig) — plus `p-vfy` and `p-dev-synth-owner`.

**`p-7f3a2c` will never hold a relationship at `est-e6696a`, because that id belongs to an estate
Paul has just deliberately frozen.** So the predicate cannot return `False` at any estate, ever.

### ⭐⭐ And the cause is a word that was split TODAY and not propagated into the code

`VOCABULARY.md` §3f, `[paul-ruled 2026-09-06]`:

| word | who | scope |
|---|---|---|
| **application administrator** | whoever runs the service | ACROSS estates — the master token |
| **estate owner** | founded a household, answers for it | ONE estate — a grant with `capability: administrator` |

**`administrators(reg)` reads `capability == "administrator"` — which is now the ESTATE OWNER
capability — and treats every holder as an APPLICATION ADMINISTRATOR whose reach must be consented
to.** The word was doing two jobs, Paul separated them this morning, and the function that gates
every mint still runs on the old reading. **The vocabulary moved; the code did not.**

### What this means for the act you were about to take

⛔ **The consent would be true-looking and would answer nothing.** `grant-mint.py:29` warns that *"a
`relationship` declared to quiet the gate defeats the gate."* **This is that warning from the other
side: a MISSING relationship arming it.** Quieting it with a consent entry is worse than the declared-
relationship case the file already forbids, because it leaves a **record** asserting a consent
transaction that never had a subject.

⭐ **And the durable cost: if G2 is red everywhere for a structural reason, every future mint gets a
consent entry to quiet it — so on the day one is GENUINELY owed (Bob's daughters at Bob's estate,
`VOCABULARY.md` §3f's own example), the gate will have been rubber-stamped so often that nobody reads
it.** That is the gate dying of routine rather than of disagreement.

### The literal question, answered for the record because it will come back

**Yes, synthetic self-consent into a real household is a DIFFERENT act.** At a synthetic estate the
consenting party and the party the gate protects are the same fiction, so the entry is a formality
with no subject. At `est-e6696a` the party being consented to is **Paul**, and the party consenting is
**a fiction Paul authored**. **A consent with the same author on both sides is a note, not a consent.**

⛔ **Whether that matters at HIS OWN estate is his call — there is no third party to protect there, and
"fine at my own house" is a defensible ruling.** ⚠️ **What must not happen is that it becomes the
precedent carried to an estate where there IS a third party.** I state the distinction; he rules it.

**Falsifier:** if `gated()` returns `False` at any estate after the administrator roster is scoped to
the application administrator, this finding is a bookkeeping artifact rather than a design defect —
and that is exactly the fix. → **engineering-partner. I do not design it.**

---

## D2 · ⚠️ A SECOND REGISTER FINDING, FOUND WHILE VERIFYING THE FIRST

**Two rows at `est-e6696a` carry `capability: administrator`, `relationship: ['owner']`, and
`consent: []`.** `p-paul` and `p-vfy`.

`grant-mint.py` **G1** requires *"a founding owner grant needs a `founding-request` entry whose
agreedBy IS the person."* **Neither row has one.** Compare `p-7f3a2c` at `est-3c9f1a`, which does.

> **The register does not currently describe an estate that its own gates would have produced.** Both
> rows may pre-date G1, or came through a path that does not write consent. **Either is fine as
> history and neither is fine as a precedent** — because the gates are now being consulted about an
> estate whose two existing rows would have been refused by them.

⛔ **Report, do not resolve.** Backfilling a `founding-request` for a grant that was not requested
would be the fabrication G1 exists to prevent. → engineering-partner + Paul.

---

## D3 · Q2 — WHAT GATE ① CERTIFIES NOW, AND WHETHER A PRODUCTION SYNTH WALK IS EVIDENCE

**Your framing is right and I will sharpen it.** Production has exactly **one** household until the
conversion lands, so a synth there **joins Paul's household** rather than founding its own. The
journey a production synth can walk is therefore **not the journey Paul will walk.**

| | certifiable today | why |
|---|---|---|
| **the journey MECHANICS** — forms accept, POSTs land, a session is obtained, screens render, the handoff crosses | ✅ **and QA already certifies it** | same code, same build. Nothing about production changes it |
| **that the PRODUCTION DEPLOYMENT is wired** — its Worker, its KV, its Pages export, its Access posture, its grant path | ✅ **only production can certify this** | this is **smoke**, and smoke is real evidence |
| **which household a record lands in** | ⛔ **not certifiable** | one household ⇒ no failing case. §3.2's clause (b), unchanged |
| **the FOUNDING journey** (Paul's actual journey) | ⛔ **not certifiable by a synth** | a synth joins; Paul founds. Different screens |
| **two people at one estate** (T2) | ⛔ **not certifiable** | needs the conversion |

> ### ⭐⭐ SO: A PRODUCTION SYNTH WALK IS EVIDENCE OF EXACTLY ONE THING — THAT PRODUCTION IS WIRED — AND THEATRE FOR EVERYTHING ELSE.
>
> **And that one thing does not need four seats, does not need synthetic accounts to persist, and does
> not need a consent record. It needs ONE traversal that reaches a session and stops.**
>
> ⭐ **Paul walking his own onboarding tonight IS that traversal.** His walk **subsumes the entire
> evidentiary value** of the production synth battery — and it is a walk of the journey that actually
> matters, which theirs is not.

**Falsifier:** if Paul's walk cannot reach a session, production is not wired and a synth walk would
not have told us anything his did not. If it reaches one, the smoke question is closed and the synth
question reduces to gate ②, **which is structurally void until the conversion regardless.**

---

## D4 · Q4 — THE THREE EXPECTATIONS. ⭐ ALL THREE ALREADY HAVE MECHANISMS. NONE IS NAMED IN A GATE

**This is the audit's finding, and it is why "tested" drifted.**

| what Paul expects | the mechanism, which EXISTS | why it did not fire |
|---|---|---|
| **(a) watchable in Chrome** | `journey-walk.py:274` — `--watch`, carrying **`paul-stated 2026-09-06`: *"I like being able to watch the walk through in chrome."*** And `:358` already writes **`"watched": bool(a.watch)`** into every run record | **the field is recorded and NO GATE READS IT.** A dated Paul statement, in the code, the same day, and the battery ran headless |
| **(b) a UX review on the build** | `check-ux-sweep.py`, in the session-start block; `/ux-sweep` is the two-pass ritual | ⚠️ **and `CLAUDE.md` explicitly rules it a TRIGGER, not a per-lap beat** — *"running it every lap spends real attention on a surface that has not moved."* **So a per-release UX gate would contradict a ratified design** |
| **(c) seats reading their own walks** | ⭐ **`walk-integrity` ALREADY ENFORCES IT.** `report-unwritten` is exactly this refusal — and **it is refusing all four of tonight's HEAD runs right now** | **the mechanism works and no gate names it as a release condition** |

> ### ⛔⛔ THE ROOT CAUSE: THERE IS NO GATE DEFINITION FILE.
>
> The cascade lives in **an auto-memory row that says three gates** (wrong on the count, the place and
> the shape), **three `.plans/` proposals parked at illegal stage words**, and **this file.** Nothing
> states what gate ① certifies. **So "tested" drifted to mean *mechanically traversable on QA* — not
> because anyone lowered the bar, but because the bar was never written.**
>
> ⭐ **This is the fourth-instance shape from §2 and §3.1, arriving at the gates themselves.** A
> capability the loop cannot reach is not a capability the loop has — and **a gate whose pass condition
> is not written down is not a gate, it is a habit.**

### How each is stated so it can pass or fail — reusing what exists, adding nothing

- **(c) first, because it costs nothing:** *gate ① passes when `walk-integrity` reports ≥N **countable**
  runs at the build under test.* **That line is already printed by the tool.** ⛔ **By it, gate ① has
  NOT passed at HEAD** — four runs, four refusals, zero countable.
- **(a):** *`walk-integrity` reports the watched/headless split; the gate definition names which it
  requires.* ⚠️ **Do NOT make headless retroactively uncountable** — that invalidates 12 countable runs
  and installs a control that reads red over history it cannot change.
- **(b):** *gate ① reads `check-ux-sweep.py` and does not pass while a sweep is **owed**.* ⭐ This
  respects the ratified trigger design — it never mandates a fresh sweep, it refuses to release over an
  outstanding one.

---

## D5 · Q3 — THE CASCADE TODAY, ONE LINE EACH

| gate | what it means TODAY | reachable? |
|---|---|---|
| **① synthetics** | the journey's MECHANICS traverse at the build under test, on QA, **read by the seat that walked it** | ✅ reachable — ⛔ **NOT passed at HEAD: 4 runs, 4 refused, 0 countable** |
| **② durable synthetic households in production** | ⛔ **structurally void.** Production has one household; a synth cannot found one. **The gate as written cannot be satisfied and should be retired or restated, not scheduled** | ⛔ unreachable until the conversion |
| **③ Paul in production** | ③-pre: the founding journey works at his real conditions — **and it carries ②'s only real value, the smoke test** | ✅ **reachable tonight** |
| **③-post** | his answers survived the tenancy conversion | ⛔ unreachable until the conversion |
| **④ action all feedback** | dispose everything gates ①–③ produced | ⚠️ **partial** — still no `fernwood-token-home`, so production's rows have no reader |
| **⑤ Mom** | ⭐ **REDEFINED: a COLD START on `home`.** Her Fernwood is frozen as a data control, so this is a first-run, **not a migration** | ⛔ gated on ③ and ④ |
| **⑥ Bob** | he creates his own account in the one production environment; nothing pre-created | ⛔ held |

⚠️ **Two gates changed meaning today and neither changed in writing: ② became unsatisfiable, and ⑤
stopped being a migration.** That is exactly what a gate definition file would have caught.

---

## D6 · Q5 — SEQUENCING. ⛔ I CORRECT IT: PAUL FIRST

**Proposed:** synths → clean → Paul. **Corrected:** **Paul → (stop and look) → decide whether synths in
production are wanted at all.**

**The method reasons, all from above:**
1. **A production synth walk is smoke, and Paul's walk is the same smoke on a better journey** (D3).
2. **Minting synths requires quieting a gate that is firing wrongly** (D1) — a defect you would be
   working around rather than through.
3. **The reset is a DELETE against a live estate.** Under Paul's own doctrine the gate sits on
   irreversible acts — so the order that runs zero deletes is strictly better when it costs nothing.
4. **If his walk fails, you learn it having minted nothing and deleted nothing.**

### What must be TRUE before he creates the first real account

**After it exists the reset tool refuses by design, so this is the last moment several things are
available.** Four, and only one is open:

| # | | state |
|---|---|---|
| 1 | **Empty verified by a GET, not a listing** — the tool's own point 4 (*"a listing cannot prove absence"*) | ✅ **you did this, twice.** ⭐ **Record the METHOD with the claim**, because *"the listing was empty"* and *"I fetched the keys"* are this repo's most-repeated confusion |
| 2 | ⚠️ **`household-export.py --env home` must have RETURNED** | ⛔ **THE ONE OPEN ITEM.** You said it had not returned. **An export that has not returned is not a backup**, and the pre-state must be captured while the estate is still resettable |
| 3 | **The 09-05 synthetic accounts resolved** | ✅ **CLOSED by your evidence, and I am withdrawing Addendum 2 §B1.** Two direct verifications beat my inference from a manifest. ⚠️ **Residual: `.private/synthetic-production-manifest.json` and `synthetic-identities.json` still NAME four `@home` accounts with no removal record** — the register over-reports credentials that no longer exist, which is `2fc2b71`'s own subject. Reconcile the files, or they will be read as live tomorrow |
| 4 | **The `unknown` bucket is understood** | ✅ **understood, and benign.** One `onboarding-metrics` row classifies `unknown` (*"no identity to judge by"* — the tool's own selftest fixture). After Paul onboards, `real` aborts every run, so **it becomes permanent.** A metrics row with no identity is harmless; **naming it now means nobody rediscovers it as a mystery** |

⭐ **And say plainly what gate ③ certifies when he walks, so it cannot drift the way ① did:**
*Paul founded a household in production, in Chrome, on build `2a476f4`, and read his own walk.* **The
first two are automatic because he is a person at a browser. The third is the one that has never
happened in this project's history — twelve countable runs and not one seat has read its own walk
before the finding was reported.** He is the only walker who cannot skip it.

---

## D7 · WHAT I DID NOT DO

- **Did not read production's KV.** No `fernwood-token-home`. Every claim about `est-e6696a`'s contents in D6 is **yours, cited as yours**, not re-derived.
- **Did not touch `grant-mint.py`, the register, or any tool.** The `gated()` finding was produced by importing the module and calling it read-only.
- **Did not duplicate** `paulkirschenbauer-06`'s freeze work or `tate-tracker-de`'s maps/zones work.
- **Did not re-litigate the merge target.** Ruled.

---

## ⛔ PAUL MUST RULE — TWO. THE FIRST IS ONE WORD AND UNBLOCKS TONIGHT

⭐ **Addendum 2's list is discharged** — the merge target is ruled, and §B1's "home is not empty" is
**withdrawn by better evidence** (D6 row 3).

| # | ruling | |
|---|---|---|
| **1** | ⭐ **DROP the production synth battery from tonight — walk your own onboarding instead.** It is not a deferral: a production synth walk is evidence of **one** thing (production is wired) and **your walk is that same evidence on the journey that actually matters.** The synth question then reduces to gate ②, which is **structurally void until the conversion lands.** ⛔ **The blocker is that minting them needs a consent record that answers nothing** — G2 is armed at *every* estate, including two where you already hold owner, because `administrators()` still reads the pre-§3f meaning of the word you split this morning (D1) | **one word. Then walk** |
| **2** | **Does the cascade get a GATE DEFINITION FILE, and does gate ① take the three clauses?** Today ① means *mechanically traversable on QA* because **nothing wrote down what it should mean** — which is why "in production, in Chrome, with a UX review" was a fair catch with no artifact to check it against. All three mechanisms **already exist**: `walk-integrity`'s countability (c), its recorded `watched` field (a), and `check-ux-sweep`'s owed-clock (b). ⚠️ **Two gates silently changed meaning today** — ② became unsatisfiable, ⑤ stopped being a migration | **not tonight** |

**One thing NOT to decide, so it does not cost you a thought:** whether synthetic self-consent is
legitimate **at your own house**. D1 shows the gate is misfiring, so the question is not live. If it
becomes live at *someone else's* house, it is a genuinely different act and D1 says why.

**Cheap, carried, still unruled — the first is now three days old:** the `.plans/` stage enum (**sixth**
instance, this file included) · the offsite verifier → `/team-audit` · the chronicle "not-a-lap"
assertion for today's commits.

**Unattended, and #2 of these gates ruling #1:** reconcile the two `.private/` files that still name
four removed `@home` accounts · **let `household-export.py --env home` finish before Paul creates an
account** · mint `fernwood-token-home` so gate ④ has a reader at all.

---

# ADDENDUM 4 · 2026-09-06 night — THE RELEASE LOOP, PULLED TOGETHER

**Written at `1a7cd7c`, after reading `2026-09-06-one-environment-DECISIONS.md` §5–§7.**

> ⭐ **THE BLOCKING QUESTION IS ALREADY ANSWERED — see §D1 above, verified BY EXECUTION, not by
> reading.** `gated()` loaded against the live register returns **`True` at all six estates**,
> including the two where Paul holds `administrator` + `relationship: ['owner']`. **You are not about
> to launder a consent gate; you are about to quiet one misfiring because `administrators()` still
> reads the pre-§3f meaning of a word Paul split this morning.** ⛔ **Do not mint. Nothing else in
> this addendum changes that.**

---

## E1 · ⭐⭐ THE RELEASE LOOP IS A LOOP, AND THIS PROJECT ALREADY HAS A STANDARD FOR LOOPS

**Paul described a loop. `~/.claude/rituals/CYCLE-SPINE.md` states what every loop must carry, ratified
2026-08-29. The release loop has never been measured against it. That is the reconciliation the
"pull it all together" ask is really about.**

**Counted, never graded** — S3's own rule, and the spine's own clause *"it does not retrofit any loop;
each adopts on its own next lap."* This is coverage, not a score:

| | element | supplied by | present |
|---|---|---|---|
| **S1** | state schema — `state`, `generated_at`, `generated_by`, `last_lap` as a dict | ⛔ **nothing.** `walk-integrity` computes state at runtime and persists none of it | **absent** |
| **S2** | ≥1 blocking human gate, machine-visible on an awareness surface | ⭐ **the gate EXISTS and Paul just named it** — *"once I clear it, it is truly released."* ⛔ **Nothing records that he cleared it.** The human half is ruled; the machine-visible half is not built | **half** |
| **S3** | ≥1 deterministic check **seen to fail**, sited at the measured risk | ✅ **`walk-integrity`, and it is the strongest element in the loop** — 35 of 47 runs refused, four distinct refusal classes, and it refused all 20 runs that predated it on its first pull | **present** |
| **S4** | machine-checkable closing condition — a lap that closed is MARKED closed | ⛔ **no chronicle for this loop exists.** `MOM-CYCLE-LOG.md` is the feedback loop's; `cycle/fleet/CYCLE-LOG.md` is Track B's | **absent** |
| **S6** | the map PARSES — beats readable as `\| N · NAME`, gate glyph on the gated row | ⛔ **there is no map.** No `cycle/release/CYCLE-MAP.md` | **absent** |

> ⭐ **One of five present, one half — and it is the loop that gates everything that reaches Mom.**
>
> ⛔ **And this explains tonight without blaming anyone.** A loop with no map, no chronicle and no
> state artifact **cannot tell you it only ran once.** Paul's *"until it no longer fails"* has no
> surface that could have said *"it failed, and then it ran once more, and that was all."* **The
> single-battery pass was not a lapse of care; it was the predictable output of a loop missing the
> four elements that would have made the shortfall visible.**

**Falsifier:** if a fresh session, given only `CLAUDE.md`, can say how many synthetic laps a build has
had and whether Paul cleared it, this finding is wrong. There is no artifact that answers either.

---

## E2 · ⭐ GATE ① WRITTEN FROM PAUL'S OWN WORDS, SO IT CAN FAIL

**Source — his exit condition, verbatim tonight:**

> *"all the synthetics have gone through it in Chrome, documented their experiences, and it's gated
> on my review and walk-through"*

plus the loop's exit condition from §5: *"until it no longer fails."*

```
GATE ① PASSES for build <sha> when, for EVERY declared seat:

  (a) a run exists at <sha>                    walk-integrity already records the build sha
  (b) that run has  watched: true              journey-walk.py:358 already WRITES this field
  (c) that run is COUNTABLE                    walk-integrity's existing predicate.
                                               ⭐ "documented their experiences" IS report-written
  (d) that run had ZERO failed actions          "until it no longer fails"
AND
  (e) no UX sweep is OWED                       check-ux-sweep.py, existing

GATE ① is UNCHECKABLE — never a pass — if no seat roster is declared.
```

> ⭐⭐ **Every one of the five clauses is ALREADY COMPUTED by a tool in this repo. Not one is read by a
> gate.** That is the whole finding, and it is the fifth instance today of *a capability the loop
> cannot reach by running its own procedure.*

**It can fail, and it fails right now.** At HEAD: four runs, **(b) false** (headless — `--watch` exists
and was unused), **(c) false** (all four refused, `report-unwritten`). **Gate ① has not passed at
HEAD**, and by this wording it says so in one line instead of requiring a person to notice.

**Two design constraints, both from Paul's own practice, so the gate does not become the thing he
forbids:**

- ⚠️ **(b) must NOT be applied retroactively.** Making headless runs uncountable would invalidate 12
  countable runs and install a control red over history it cannot change. **Report the
  watched/headless split; let the gate bind going forward.**
- ⚠️ **(e) reads the sweep's OWED clock; it never mandates a fresh sweep.** `CLAUDE.md` explicitly
  rules the sweep *"a TRIGGER, not a per-lap beat — running it every lap spends real attention on a
  surface that has not moved."* **A per-release UX gate would contradict a ratified design; an
  owed-sweep refusal does not.**

---

## E3 · PERSONA LIFECYCLE — what `[paul-stated §6]` obliges

> *"they should be personas that have their own profile that they establish in a household."*

**⚠️ One correction to the brief, measured: `--fresh` is NOT the default.** `journey-walk.py:270` is
`action="store_true"` — opt-in. **The dozens of one-shot accounts came from routine USE of a
non-default flag, not from a default.** That matters, because the fix is a practice rule, not a code
change.

**Four rules, each grounded in a mechanism that exists:**

1. **A persona's identity is an ASSET, not a fixture.** One account per (persona, estate), created
   once, reused. `.private/synthetic-identities.json` is already keyed `role@env` — **the store
   already assumes durability; the walker does not.**
2. ⭐ **`--fresh` stops being a routine mode and becomes a NAMED TEST of the SIGNUP journey.** A
   returning walk tests the *returning* journey. **These are two different journeys, and running
   `--fresh` every time means the returning journey has never been walked by anyone** — which is
   exactly the class of gap the `handover` seat was created to close.
3. ⛔ **Deletion must be ATOMIC with the register.** Tonight the production seats' grants were deleted
   by a reset **while the register still read them live** — a register claiming a credential that does
   not exist. `2fc2b71`'s own subject already names this (*"say when a delete leaves the register
   claiming a live credential"*). **A persona's record and its register row are deleted by one act or
   the register lies in the dangerous direction.**
4. ⭐⭐ **A durable persona in a REAL household is a different object, and this is where §6 and the
   production-synth question turn out to be ONE question.**

> **Durable personas + production has exactly one household = the personas become PERMANENT MEMBERS OF
> PAUL'S HOME. And there is no removal path that survives his onboarding** — `reset-production-estate.py`
> aborts entirely on any `real` record, by design, and Paul's account is that record.
>
> ⛔ **So "durable personas" and "synthetics in production" cannot both be adopted before the tenancy
> conversion without creating members of his household that nothing can remove.** §D3's answer already
> covers it: drop the production battery, and the conflict does not arise.

---

## E4 · ⭐ DATA ENDURANCE — THE POLICY, AND IT IS 90% ALREADY RULED BY TOOLS

**Paul: *"we talked at length… and it is written nowhere."* He is right that no document states it —
and the reconciliation finding is that FIVE MECHANISMS ALREADY RULE IT, each in its own file.** This
writes down what they already do; it invents one cell.

| | `lab` | `qa` | `home` (live) | `est-3c9f1a` (frozen) |
|---|---|---|---|---|
| **a cycle that FAILS** | ⭐ **KEPT as trail, never deleted** — `walk-integrity`: *"35 run(s) refused and kept — a consolidation must exclude them by dir, not by seat name. **That is the trail, not a fault**"* | same | same on the run side; the estate-side rows classify `synthetic` and are deletable | ⛔ n/a — nothing runs there |
| **a run SUPERSEDED by a later one** | ⭐ **KEPT and MARKED**, never deleted — `bb21863`'s four standings (`current`/`superseded`/`unlinked`/`pre-date`), authority **derived** as the newest *countable* run, `.private/current-runs.json` as Paul's override. **Kept because "which of ours counts" is revisable, and the trail is what makes it revisable** | same | same | n/a |
| **a durable PERSONA's own record** | permanent — it is the persona's home | permanent | ⛔⛔ **THE ONE OPEN CELL** — see §E3.4. Permanent members of Paul's household with no removal path | n/a |
| **the ENVIRONMENT itself** | resettable freely | resettable freely | ⭐ **`reset-production-estate.py`: `synthetic` deleted · ONE `real` record ABORTS THE WHOLE RUN · `unknown` KEPT unless `--include-unknown`.** Never guesses toward synthetic | ⭐⭐ **PERMANENT, READ-ONLY — a DATA CONTROL** `[paul-ruled 2026-09-06]`, kept so a from-scratch build with Mom can be compared against the hand-built one. `archive-frozen-estate.py` |

⭐ **The frozen estate's rule is the strongest in the table and it is hours old:** it is not "old data we
haven't deleted," it is **an experimental control with a stated purpose.** Nothing may write to it, and
"clean it up" is now a category error. **That sentence existed only in a transcript until tonight.**

⛔ **The single open cell is the one blocking the coordinator, and §D3/§E3.4 resolve it by not creating
it.** Everything else in this table is a restatement, not a proposal — **which is the useful finding:
the policy was already ruled; it was just never in one place, so it read as missing.**

---

## E5 · TESTING THE "THEATRE" FRAMING — ⛔ RIGHT IN HALF, AND THE OTHER HALF WOULD HAVE STOPPED TONIGHT

**You asked to be tested rather than agreed with.**

✅ **The "theatre" half is right and §D3 already states it**: a production synth walk is evidence of
exactly one thing — that production is wired — and theatre for the journey, because a seat there joins
Paul's household rather than founding its own.

⛔ **The "his release loop cannot close on production until the conversion lands" half is NOT
established, and I think it is wrong.** **Paul's loop never required synthetics in production.** His
own words, both tonight:

> *"by the time we get to production — **not to mention the other environments** — we have a build, we
> run it through our synthetic testers until it no longer fails, **and then I run it**."*
>
> *"QA is essentially a mirror of production where I am testing out the latest and greatest."*

**He is describing the synthetic loop as running in QA and HIMSELF as the one who runs production. The
loop closes on production THROUGH PAUL, not through synthetics in production.** So the conversion
gates gate ② and clause (b) of gate ③-post — **it does not gate the release loop.**

⚠️ **One thing genuinely unresolved, and it is checkable rather than arguable:** whether a seat can be
given a **founding** invite at QA. The register shows `p-qa-synth-1 / est-qa0001 / member /
['owner'] / consent [founding-request, administrator-reads]` — **a founding-request already exists at
QA**, which suggests the founding path IS rehearsable there. If it is, the "cannot close" claim
dissolves completely. **→ engineering-partner; it is one check, not a debate.**

**Why the correction matters tonight:** "cannot close until the conversion" would stop him walking.
**Nothing in his stated loop does.**

---

## E6 · ⚠️ "QA IS A MIRROR OF PRODUCTION" — MEASURED FALSE, IN THE ONE DIMENSION THAT MATTERS

`python3 tools/check-household-isolation.py`:

```
⛔ qa    LEGACY_BEFORE=2026-09-03 → 19 kinds share ONE unprefixed key across households
✅ home  LEGACY_BEFORE=1970-01-01 → no legacy era; every key carries its estate
```

> **QA and production differ in EXACTLY the variable the tenancy conversion is about.** Under Paul's
> mirror framing this stops being a curiosity (Addendum 1 §B2) and becomes a **process defect**: a T2 /
> sharing result obtained on QA is obtained in a fixture that differs from production in the variable
> under test.

⛔ **The remedy is an environment-topology call → engineering-partner, per the scope split. I state the
defect and hand it.**

⚠️ **And a vocabulary miss worth one line, because it is mine:** Paul said *"dev is separate."*
**`wrangler.toml` declares no `dev`.** It declares top-level, `qa`, `lab`, `home`, `bob`, `paul`. **`lab`
is presumably what he means by dev, and the word he used does not exist in the config** — the same
class as `ENV_NAME = "production"` naming the legacy estate, which has now cost three times in this
file.

---

## E7 · THE RECONCILIATION — WHERE THE DOCUMENTS DISAGREE

**Census: `git grep -lniE "gate ①|cascade|release.*gate" -- '*.md'` → 30 tracked files.** Naming the
disagreements, not resolving them:

| # | disagreement | |
|---|---|---|
| **1** | ⛔ **auto-memory `feedback_release_cascade_persona_paul_mom` says THREE gates, *"Paul in lab"*** — vs six gates, Paul in production, and a LOOP rather than a cascade. **Wrong on the count, the place and the shape.** ⭐ **Highest re-litigation risk in the corpus: an agent tomorrow reads memory, not `.plans/`** | carried 3 addenda |
| **2** | **`.plans/2026-09-05-release-cascade-tracking-PROPOSAL.md` was COMMISSIONED to hold exactly this and is `stage: draft`, unruled since 09-05** — an illegal stage word, so no instrument reads it | |
| **3** | **"production starts from nothing but a text to Mom"** (`2026-09-05-production-promotion-PLAN.md` §S6) vs **durable synthetic households in production.** ⭐ **Now resolved in fact but not in text** — Paul's freeze ruling makes Mom a cold start on `home`, and §D3/§E3.4 drop the production synths. **Both files still say the old things** | |
| **4** | **"QA is a mirror of production"** vs `qa`'s legacy era | §E6 |
| **5** | **`dev`** (Paul's word) vs **`lab`** (the config's) | §E6 |
| **6** | **`walk-integrity` REQUIRES a read report for countability; no gate names it as a release condition** — the mechanism outranks every document, and no document knows | §E2 |
| **7** | **`.plans/` stage enum — SIXTH instance**, this file included. `check-backlog-ready.py:46` unmoved since 09-03; **20+ older `.plans/` files carry no `stage:` line at all**, so the enum governs a minority of the directory | |
| **8** | ⛔ **The release loop is measured against no standard**, while `CYCLE-SPINE.md` has stated the standard for every loop since 08-29 | §E1 |

---

## E8 · ⭐ THE STANDING DOCUMENT — DO NOT INVENT ONE. INSTANTIATE THE FORM THAT EXISTS

**Yes, the reconciliation warrants one place to read. ⛔ It should NOT be a new document type.**

> **The release loop is a loop. This project has a form for loops, ratified, checkable and already
> instantiated twice: `MOM-CYCLE-MAP.md` (richest) and `cycle/fleet/CYCLE-MAP.md` (newest).**
> **The answer is `cycle/release/CYCLE-MAP.md`, not a novel artifact.**

**What that buys, mechanically rather than tidily:**
- it **parses under S6 for free** (`render.py:783` reads `\| N · NAME` beats and the 👤 gate glyph), so
  the loop appears on the awareness surface the other loops appear on;
- `cycle/release/CYCLE-LOG.md` supplies **S4** — the chronicle that would have said *"it ran once"*;
- a `cycle-state.json` beside it supplies **S1**, matching `cycle/fleet/`'s existing layout;
- **S2's machine-visible half becomes a field**: *Paul cleared build `<sha>` on `<date>`* — the release
  event he named, recorded where a tool can read it;
- **S3 is already satisfied** by `walk-integrity` and simply gets sited.

**It would ABSORB** (Paul rules whether that is supersession or citation — I propose destinations, not
retirements): the release-cascade tracking proposal · the journey-test-cycle proposal · §5–§7 of the
DECISIONS file · gate ① as written in §E2 · the persona lifecycle §E3 · the endurance table §E4.

**It would NOT absorb** and must keep citing: `CLAUDE.md` (session-start machinery) · `VOCABULARY.md`
(the words) · `CYCLE-SPINE.md` (the standard it conforms to) · this file and the three audits (the
evidence trail).

⛔ **I am proposing the destination and the form. I am not writing it in this pass** — it is a
governing artifact for a loop Paul has just defined in his own words, and it belongs at his gate, not
appended to an addendum at the end of a long day.

---

## ⛔ PAUL MUST RULE — THREE. THE FIRST IS ONE WORD AND UNBLOCKS TONIGHT

⭐ **Addendum 3's list stands; #1 below IS that list's #1, unchanged and now further supported.**

| # | ruling | |
|---|---|---|
| **1** | ⭐ **DROP the production synth battery tonight and walk your own onboarding.** ⛔ **Do not mint the grants:** G2 is armed at **every** estate — including two where you already hold owner — because `administrators()` still reads the pre-§3f meaning of the word you split this morning (§D1, verified by execution). **And durable personas + one household in production = permanent members of your home with no removal path** (§E3.4). Your walk carries the only real evidence a production synth walk could (§D3), on the journey that actually matters. ⚠️ **§E5: your release loop does NOT need synthetics in production — your own words put them in QA and you in production.** Nothing here stops you walking | **one word, then walk** |
| **2** | **Does the release loop get `cycle/release/CYCLE-MAP.md` + `CYCLE-LOG.md`** — the same form as the fleet and mom loops, so it parses onto the awareness surface, so *"it ran once"* becomes visible, and so **"Paul cleared build X" is recorded rather than remembered**? ⭐ **Measured: of the spine's five mandatory elements this loop has one, plus half of the human gate — and it is the loop that gates everything reaching Mom.** §E2's gate ① text is ready to drop in, written from your words, and it **fails at HEAD today** | **not tonight** |
| **3** | **Persona lifecycle: is `--fresh` a NAMED TEST of the signup journey rather than the routine mode?** Today it is opt-in but routinely used, so dozens of one-shot accounts exist and **the RETURNING journey has never been walked by anyone.** ⭐ Your §6 ruling implies it; this makes it checkable | **not tonight** |

**Cheap, carried, unchanged:** the `.plans/` stage enum (**sixth** instance; and 20+ older files carry
no stage line at all, so the enum governs a minority) · the offsite verifier → `/team-audit` · the
chronicle "not-a-lap" assertion for today's commits.

**Handed to engineering-partner, not to you:** the `administrators()` scoping fix (§D1) · whether a
seat can take a FOUNDING invite at QA (§E5 — one check, and it closes the "cannot close on production"
question) · QA/production parity in the legacy-era dimension (§E6).

**Unattended, and the first still gates your first account:** let `household-export.py --env home`
finish · reconcile the two `.private/` files still naming four removed `@home` accounts · mint
`fernwood-token-home`.
