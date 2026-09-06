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
- stage: design — ⚠️ **fifth file to need a stage word that does not exist.** `tools/check-backlog-ready.py:46` reads `STAGES = ["ready","concept","build","qa","shipped","retro"]`. Four files now sit at `audit`/`draft`/`design`, all illegal, all self-flagged, the enum unmoved since 09-03.

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
