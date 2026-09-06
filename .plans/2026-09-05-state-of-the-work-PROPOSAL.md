# STATE OF THE WORK — what is ruled, what awaits Paul, what disagrees with itself · PROPOSAL

- row: process (no BACKLOG row yet — same posture as the 09-03 readiness, 09-05 cascade, 09-05 registry proposals)
- objective: O5
- class: engine · must-not-diverge (a second place that says "what is ruled" is the defect this exists to prevent)
- seats: practice-steward (this file)
        engineering-partner → deferred: §2's overload and §3's rename have code consequences; nothing is designed here
        content-steward → deferred: §3's `legacy` question is a naming ruling, its and Paul's
        ux-expert · ai-advisor · user-researcher → waived: no surface, no model, no person is studied here
- depends-on: .plans/2026-09-04-process-wiring-AUDIT.md
- depends-on: .plans/2026-09-05-release-cascade-tracking-PROPOSAL.md
- ready: agent-proposed 2026-09-05 — **Paul rules**
- stage: draft   ⚠️ not a legal `stage:` word until process-wiring-AUDIT §B.1 is ruled; see §4

> **Method only.** This file ranks no feature, decides no migration, and designs no tenancy. Where a
> call turns on real-world context only Paul has, it is named and declined (§8).

---

## ⚠️ 0 · READ THIS FIRST — HEAD MOVED UNDER THIS AUDIT, AND IT CHANGED A FINDING

At the start of this pass `git log` topped at **`cd92a5a`**. At the end it topped at **`cb29e08`**
("Fernwood dev: lab binds est-3c9f1a — and that killed G3, so G3b asks the destination who it is").
`worker/wrangler.toml:81` read `ESTATE_ID = "est-lab0001"` on my first read and reads
`ESTATE_ID = "est-3c9f1a"` now.

⭐ **That commit resolves the exact question I was two paragraphs from filing as open** — *"whether an
estate id names a household or a household-in-an-environment"*, which `d3ef1cc`'s body had recorded as
*"untouched and still Paul's."* Had I written from the first read, this file would have opened by
asking Paul to rule something he had already ruled and that had already shipped.

Two things follow, and only the second is about the tooling:

1. **Every claim below is stamped to `cb29e08`.** Any reader should re-verify against HEAD before
   acting, exactly as `handoff-onboarding-journey-testing.md`'s own header demands.
2. **This is the concurrent-writer condition, and it fired without anyone noticing.** Global doctrine
   (`~/.claude/CLAUDE.md` § Concurrent-session guard) says stop and confirm when HEAD moves under you.
   Nothing here has a detector: a subagent reads a tree, works for twenty minutes, and writes findings
   against a state that no longer exists. **A stale audit and a current one print identically.** That
   is this corpus's own named failure shape, arriving in the audit function itself.

---

## 1 · THE CLEAN LAYOUT — and it is not a new document

**The four states already have four homes.** Nothing needs to be created. Two of the four are
unreachable, and that is the whole defect.

| state | where it already lives | reachable? |
|---|---|---|
| **RULED** | `BACKLOG.md` § FOCUS FREEZE (:69–126) for the migration workstream · `PRODUCT-ENGINE.md` for engine rulings · `VOCABULARY.md` §2/§3 for words · `estate.json`, `wrangler.toml` for schema | ✅ yes, and this is the strongest part of the record |
| **PROPOSED, awaiting Paul** | the `- ready: agent-proposed … Paul rules` line in each `.plans/` header | 🔴 **NO — see below** |
| **ASSUMED but unstated** | nowhere by construction | 🔴 no home exists |
| **CONTRADICTED** | `VOCABULARY.md` §3d (declared collisions) and §5 (live defects) | ✅ the pattern exists; it is under-used |

### 1a · Why PROPOSED is unreachable, measured

`tools/check-backlog-ready.py:132` and `:217` glob **`.plans/*-PLAN.md`**. Every artifact whose whole
purpose is to await a ruling is named `*-PROPOSAL.md` and is therefore **outside the glob of the one
instrument that renders in-flight and unstamped work.**

Nine `*-PROPOSAL.md` files carry `ready: agent-proposed — Paul rules`. **The checker sees none of
them.** Verified by execution: its 25 flags name only `-PLAN.md` files.

The second surface fares no better. `~/.claude/tools/focus.py` renders Paul's queue from BACKLOG rows,
and each of today's proposals declares in its own header `row: process (no BACKLOG row yet)`. Of the
five stacked proposals, **one** reaches focus.py ("The journey-test cycle — practice-steward's design,
unruled"), and it arrives via the claude-meta anchor, not via Fernwood.

And `BACKLOG.md` § **WAITING ON PAUL** (:128–165) — the section built for exactly this — carries 27
rows, of which **one** is from today (ADDRESS VALIDATION, :163). The other 26 are Track A/B content
items, 13 of them photo-organizer inbounds. **The engine work Paul spent the day ruling on is absent
from the section named for what he owes.**

### 1b · The proposal — three edits, no new file

1. **Widen the glob to `.plans/*-{PLAN,PROPOSAL}.md`, and grade a PROPOSAL on the header only** —
   `row:` · `objective:` · `ready:` · `stage:` · `depends-on:`. ⛔ Not on `## Files touched` /
   `## Sequence` / `## QA`; a proposal has none by definition and requiring them would make the
   control red forever, which is the thing Paul has ruled against twice in writing
   (`check-vocabulary.py:36-40` cites the same rule). **Falsifier:** if widening makes the checker
   red on a healthy proposal, the grading split is wrong and the glob should revert.
2. **Give `BACKLOG.md` § WAITING ON PAUL a derived head line**, not a hand-kept list: the checker
   already knows every unstamped plan and its `depends-on` edges, so it can print
   *"N proposals awaiting a ruling; roots: X, Y"*. The section keeps its hand-written rows for
   real-world items; the process queue is computed. ⚠️ **The failure to avoid is a second tracker** —
   this must be a pointer to the derivation, never a copy of it (`BACKLOG.md:40`, "This is a POINTER
   list, not a second tracker").
3. **ASSUMED gets one row-type in `VOCABULARY.md` §5, not a document.** §5 is already
   *"one live defect"* — a measured contradiction awaiting a decision. That is exactly the shape of an
   assumption: something the code acts on that nobody ruled. Rename nothing; add rows. Today's
   candidates are in §2 and §3.

⛔ **What I am not proposing: a state-of-the-work document.** It would be fork number eight. Every
state above already has an owner, and a new file would become the ninth thing that has to be true.

---

## 2 · THE ENVIRONMENT / ESTATE MODEL, STATED ONCE

### 2a · The model, as it now reads at `cb29e08`

> An **estate** is a place. Its `estateId` is a **coordinate, not a label** — `estate.json:_meta.rule`,
> declared 2026-09-03: *"renaming the place does not rename the estateId."*
> An **environment** is a copy of the running system for one estate. It is named by `ENV_NAME`, and
> what actually separates two environments is that **each binds its own KV namespace**
> (`wrangler.toml:66-67`: *"the environment is the NAMESPACE"*).
> ⭐ **The two axes are orthogonal, and `[paul-ruled 2026-09-05]` makes that binding:** *"an estateId
> names an ESTATE, not an estate-in-an-environment"* — so Fernwood's dev, qa and production all carry
> `est-3c9f1a` and differ only by namespace.

### 2b · What is coherent today — measured against `worker/wrangler.toml` at `cb29e08`

| deployment | `ENV_NAME` | `ESTATE_ID` | namespace | reads under the ruling |
|---|---|---|---|---|
| `[vars]` | `production` | `est-3c9f1a` | `100f2b95…` | ✅ Fernwood production |
| `[env.lab]` | `lab` | `est-3c9f1a` | `1e0bd883…` | ✅ Fernwood dev (`:63-77`) |
| `[env.qa]` | `qa` | **`est-qa0001`** | `a0cf82b6…` | ⛔ **not Fernwood's QA** |
| `[env.home]` | `home` | **`est-e6696a`** | `79464451…` | ⚠️ a *different estate's* production-in-waiting |

**Two of the three environments Paul named are Fernwood's. The third is not.** `est-qa0001` names a
fixture estate, not a place — the `0001` is a sequence number inside an environment. Under the
ruling's own test (*would only renaming the place ever change this id?*), `est-3c9f1a` passes and
`est-qa0001` / `est-lab0001` do not. `cb29e08`'s own body says so: *"qa and home still bind their own
estates. Whether they follow… is Paul's."*

### 2c · The thing that has to change, and it is not a rename

⛔ **`ESTATE_ID` is carrying two jobs, and the ruling made that visible rather than causing it.**

- Job 1, the ruled one: **name the place.**
- Job 2, undeclared: **fence credentials between environments.** `wrangler.toml:46-47` records it
  verbatim, from `.engineering/2026-09-03-c6-privacy-seat-review.md:191` — *"QA carries its OWN estate
  id, so a QA credential is never shaped like a prod one."*

Job 2 is why `est-qa0001` exists. It is not sloppiness; it is a control. And `cb29e08` demonstrated —
by doing, not by reasoning — that job 1 **destroys** job 2: once lab and prod both bind `est-3c9f1a`,
`grant-mint`'s G3 comparison is always true and *"CAN NEVER FIRE"*; the identical mint was accepted for
`--env lab` and `--env prod` minutes after the change (`tools/grant-mint.py:181-189`).

⭐ **The repair pattern is already built and already proven**, and it generalizes: G3b asks the
destination who it is, by reading the `env-canary` key **through the same `--env` routing the write
will use** (`grant-mint.py:191-213`). *A fixture must assert its own destination; so must a
credential.* Anything that today derives an environment fence from `ESTATE_ID` has the same repair
available to it.

**So the coherent statement, and the one open edge:**

> `estateId` names the place. `ENV_NAME` + the bound namespace name the environment. **No control may
> read `estateId` to learn which environment it is in** — that is the overload, and G3 is the worked
> example of what it costs. Whether `qa` and `home` follow `lab` onto their real estates is Paul's,
> and each carries a distinct question: **qa** is a fence question (what replaces `est-qa0001`'s
> credential-shape guarantee), **home** is a *whose place is it* question, which is §2d.

### 2d · `est-e6696a` and the legacy version — what the ids can and cannot say

- `est-e6696a` is **`[paul-decided 2026-09-05]` a PLACEHOLDER** —
  `handoff/handoff-onboarding-journey-testing.md:35`: *"a fresh estate id is minted when the real
  property record is authored, not before."* No `instance/` file exists for it
  (`handoff-fernwood-onboarding-link.md:38`), which is recorded as correct.
- It is the **only id wearing a real-place shape while naming no place.** `est-3c9f1a` and `est-e6696a`
  are indistinguishable by construction; `est-qa0001` and `est-lab0001` announce themselves as
  fixtures. **A placeholder that looks exactly like a real coordinate is the one that gets promoted by
  accident.** Method fix, no ruling needed: a placeholder id should be shaped so it cannot be mistaken
  for a coordinate, or `estate.json`-style declaration should exist for it saying it is one.
- **The "legacy version" is the frozen GitHub Pages production instance.** Under this model it is not a
  fourth environment — it is `production` for `est-3c9f1a`, and `wrangler.toml:96-99` already says the
  `production` **role** transfers to `home` when it retires.

### 2e · What the model implies and nobody has costed — flagged, not decided

`[paul-ruled 2026-09-05]` *"dev, qa and production for every home"* × one-estate-per-deploy
(`worker.js:387`, `.plans/2026-09-04-three-environments-PLAN.md` § the constraint) = **3 deployments
per estate**, each needing its own KV namespace, `ESTATE_ID`, `LEGACY_BEFORE`, budget, `FAMILY_HOSTS`,
Pages project and deploy command — **seven artifacts × 3 × N**. `c88c486`'s own body names this as *"the
one-estate-per-deploy welding, recorded as `until` not `by-design`."* ⛔ Whether every estate really
needs three environments, or only the engine does, is Paul's; I note only that the ruling and the
welding multiply.

---

## 3 · THE NAMING REPAIRS

### 3a · `legacy` — the second booking has NOT happened in a tracked file. Do not make it.

**Measured, two methods.** `git grep "legacy version"` → **0**. A filtered read of every `legacy`
occurrence in every tracked `*.md` → 0 uses meaning *the GitHub Pages viewer*. It appears **once**, in
`cb29e08`'s commit body: *"the env that BECOMES production when the legacy version retires."*

**What the word already means, in running code:** `LEGACY_BEFORE` is a **deployed, non-inheritable
binding in all four environments**, and `legacyBefore()` **throws** without it
(`worker/worker.js:439-443`). It means *KV keys written before the estate-prefix cutover* — 31
occurrences in `worker.js`, plus `listBothEras()` and the era-routing in `dateKey`/`blobKey`. **That
word cannot move.**

**And a name already exists for the thing Paul meant:** `production` is a **ROLE that transfers**
(`wrangler.toml:97`, content-steward 2026-09-04). The frozen instance holds it today. So *"the frozen
production instance"* / *"Mom's current production Fernwood"* — both already in use in `BACKLOG.md` —
say it with no new word.

⛔ **Whether to adopt "legacy version" anyway is Paul's — he said it, and it is a good plain word.**
If he does, the method requirement is narrow: it goes into `VOCABULARY.md` as a **declared
double-booking in the §3d `qa` style, never a rejection**, with the falsifier §3d already uses — *if a
reader cannot tell which act "legacy" means, the newer sense renames and the binding never does.*

### 3b · `household` — 644 hits, three senses, and only one is a defect

| sense | count | verdict |
|---|---|---|
| **`household system(s)` / `household-system`** — Mom's coined term; a live `group` value in `vehicles.json`, a card in `viewer.html`, `BACKLOG.md` § B6, `OBJECTIVES.md` O4 | **301** | ✅ **PROTECTED. Do not touch.** `CLAUDE.md`: *"Adopt her words, never improve them… If she names a thing, that is its name."* |
| **`household` as a module-bundle name** | — | retired `VOCABULARY.md:54` `[paul-stated 2026-09-03]` in favour of `house-systems` |
| ⛔ **`household` as a synonym for `estate`** — today's misuse | see below | the defect |

**Where the misuse actually is, enumerated:**

- **4 commit messages of 2026-09-05** — `6325ed4` (9), `d3ef1cc` (11), `a696589` (10), `cd92a5a` (13);
  three of them carry it in the **subject line**. Measured with `git show -s --format=%B | grep -oci`.
- **13 comment lines in `worker/worker.js`** — `:348, 349, 356, 369, 410, 411, 413, 423, 428, 429, 448,
  449, 450`. (`:1259, 1264, 1279` are the *protected* sense, inside the Guru prompt.)
- **`tools/household-export.py`** — the filename, the docstring, and 4 print strings.
- **162 mentions across two UNTRACKED engineering briefs** —
  `.engineering/2026-09-05-multi-household-tenancy.md` (80) and `-tenancy-adversarial-read.md` (82),
  both `?? ` in `git status`.

⭐ **Zero identifiers.** `worker.js` uses `estateId` / `estate` / `scope.id` throughout;
`household-export.py`'s own variable is `estate` (`:96`, `:105`). **This is a prose-and-filename
repair, not a migration** — which is exactly why it is cheap, and exactly why `check-vocabulary.py`
reported clean.

**Proposed repair, in order of cost:**

1. `git mv tools/household-export.py tools/estate-export.py`, fix callers, rewrite its 9 strings.
2. Rewrite the 13 `worker.js` comment lines. No behaviour changes; the diff is greppable.
3. The two untracked briefs: they are **untracked in a public repo** and the same handoff already flags
   an untracked `.user-research/2026-09-04-condo-dweller.md` as *"a privacy question, not
   housekeeping."* Their disposition (track / move to the private sibling / discard) is Paul's; the
   word repair rides on whatever he decides.
4. **Commit messages are immutable and must not be rewritten.** The honest move is a dated line in
   `VOCABULARY.md` §4 recording that the 2026-09-05 tenancy commits use `household` where canon says
   `estate`, so a future `git log` grep resolves instead of forking.

### 3c · Does `VOCABULARY.md` need rows? Yes — two, and here is what they do NOT buy

**Verified by executing the checker's own parser** (`parse_vocabulary`): `household` is in **neither**
the canonical nor the rejected set. It is invisible to `check-vocabulary.py` today.

- **A §4 row for `household`** — *"rejected as the tenant noun (it is `estate`), and already TAKEN by
  Mom's `household system`."* This makes V1 fire if the word is ever minted as an **identifier** in a
  schema surface.
  ⚠️ **It would not have caught what happened today.** V1's N8 guard restricts to **4 schema
  surfaces** (`check-vocabulary.py:58-64`) precisely so it is not red forever; prose, filenames and
  commit messages are out of scope **by design**. Say that at the row rather than selling it as a fix.
- **A §3d-style declared-collision row for `legacy`**, only if §3a is ruled to adopt the new sense.

**And one instrument defect found on the way, small and real:** §4 has **7** rejected rows; the parser
returns **6**. `"Almanac" as a portable noun` is silently dropped — the `ROW` regex
(`check-vocabulary.py:71`) does not survive an internal closing quote. **A rejected term the rejection
checker cannot see** is the shape the file exists to prevent. One-line regex fix; hand to
`engineering-partner`.

---

## 4 · THE RULING ORDER — and what can sit indefinitely

**Derived from the `depends-on:` edges the files themselves declare.** Nothing here is a value ranking.

### 4a · The DAG, as written

```
2026-09-03-qa-test-vs-ux-review-PROPOSAL  ─┐
2026-09-04-process-wiring-AUDIT  ──────────┼─→ release-cascade-tracking ─┬─→ journey-test-cycle ─┐
2026-09-04-three-environments-PLAN ────────┘                             │                      ├─→ journey-as-prioritizer
                                                                         └─→ process-registry    │
2026-09-03-c4-process-PROPOSAL ──────────────────────────────────────────────────────────────────┘
```

⭐ **The roots are the two OLDEST unruled artifacts, and the leaves are the two newest.** Ruling
yesterday's proposals before the 09-03/09-04 ones they cite would be ruling over an unruled premise.

### 4b · Must be ruled first, because others cannot be legal without it

1. **`process-wiring-AUDIT` §B.1 — does `draft` join the `stage:` enum?**
   `check-backlog-ready.py:44` declares `STAGES = ["ready","concept","build","qa","shipped","retro"]`.
   **Three of the five stacked proposals already write `stage: draft`**, and the AUDIT's own header
   says so in its own text (`:491`: *"legal only if B.1 is ruled"*). This is the cheapest ruling on the
   board and it unblocks the header format everything else is written in. **It is one word.**
2. **`2026-09-04-three-environments-PLAN.md` needs a header at all.** Verified: it carries **no**
   `row:`, `objective:`, `class:`, `stage:` or `seats:` — 10 of the checker's 25 flags are this one
   file. It is the plan of record for the environment work Paul ruled on today, and no instrument can
   see it. Same for `2026-09-04-map-region-smoothing-PLAN.md` (9 flags). ⛔ **Not a ruling — a
   completion.** An agent can draft the header; Paul stamps `ready:`.
3. **`release-cascade-tracking`** — the DAG root of the five. Three depend on it; it depends on none of
   them. Ruling any of the other four first means ruling on a definition of *"this gate passed"* that
   does not exist yet, which is the `must-not-diverge` risk each of them declares in its own header.

### 4c · Can wait, and here is the cost of waiting — stated so it is not manufactured

| proposal | can it sit? | what accrues |
|---|---|---|
| **journey-test-cycle** | **Yes.** Gate 1 already ran once without it — `.plans/walks/2026-09-05-onboarding-gate1.json`, and it caught a P0 (`step()` threw on every call). The *capability* exists unruled | each further walk leaves an artifact with no defined home. Slow, visible, recoverable |
| **journey-as-prioritizer** | **Yes, indefinitely.** A leaf; nothing depends on it. Its own §1e defers the stage list to `user-researcher` and Paul anyway | nothing decays |
| **process-registry** | **Yes, indefinitely — and it may not belong here at all.** Its own header: *"this file is written in Tate-Tracker because that is where the seat was standing. The thing it proposes does not belong here."* Its §1 finds `~/.claude/handoff/doors.json` already carries the axis Paul asked for | nothing decays |
| **the two untracked tenancy briefs** | **No — but not because they are urgent.** They are untracked in a **public** repo (§3b·3). That is a disposition question, not a ruling | it is a state, not a clock |

⛔ **I am not saying release-cascade-tracking is more important than the others.** I am saying three
files declare a dependency on it and none declares one on them. That is a sequence claim and nothing
more.

---

## 5 · WHERE TODAY'S RULINGS LIVE — and would a reader find them next month?

| ruling | where recorded | findable in a month? |
|---|---|---|
| Full registration; *"nobody signs up"* RETIRED | `PRODUCT-ENGINE.md` § ACTIVATION (:552), with the 09-02 model kept as `#### 🗄 HISTORICAL` (:598) | ✅ **Yes, and this is the model.** The superseded version sits beside the ruling, labelled |
| Master token retires when accounts supersede it | `PRODUCT-ENGINE.md` § THE MASTER TOKEN (:15-54) + `a696589` | ✅ yes |
| The end goal | `PRODUCT-ENGINE.md` § THE END GOAL (:55-94), with an 8-row dependency table | ✅ yes |
| `estateId` names an estate, not an estate-in-an-environment | `wrangler.toml:63-77` · `grant-mint.py:181-195` · `cb29e08` | ✅ yes — **in code, where it binds.** Best possible home |
| Feedback traces to individual AND estate | `worker.js:348-356`, `:369` + `6325ed4` | 🟡 code-only; no prose surface names it |
| **One account holds grants on several estates; an estate carries grants for several people** | **only** in `.engineering/2026-09-05-multi-household-tenancy.md`'s YAML `settled_and_not_relitigated:` — an **untracked file** | 🔴 **NO.** A ratified tenancy rule living in an uncommitted file |
| **"Dev, qa and production for every home"** | `wrangler.toml:63` quotes the *"Fernwood dev, qa, production"* half. The *"for every home"* half — the multiplier in §2e — is **nowhere** | 🟡 half recorded |
| **The GH-Pages viewer is "the legacy version"** | **nowhere in a tracked file** (verified two ways); one commit body | 🔴 no |
| `est-e6696a` is a placeholder | `handoff/handoff-onboarding-journey-testing.md:35` | 🟡 **wrong home.** A handoff is a per-mission artifact, consumed and superseded; `estate.json`-class facts should not live in one |

⭐ **The pattern is clean and it is worth stating as a rule:** *every ruling that landed in
`PRODUCT-ENGINE.md` or in a binding is findable; every ruling that landed only in a commit body, a
handoff, or an untracked file is not.* `PRODUCT-ENGINE.md` **is** the right home for engine rulings and
today it was used well — the ACTIVATION section's preserved-historical block is the best artifact
produced today by this measure, because it makes a supersession legible instead of erasing it.

**One structural gap this exposes, and it is the founding finding of this seat arriving here:** the
richest reasoning today — *why* the token sequencing matters, *why* a signature change beat a deleted
default, the false-green in G3b's first run, the *"47 counted LINES"* correction — lives in commit
bodies and in two untracked briefs. **A chronicle records what a lap did; a commit records what the
author considered.** Four of today's commit bodies are better documents than anything tracked.

---

## 6 · PROCESS DEFECTS — direct, as asked

**D1 · Four instrument misreads in one day is not four incidents; it is one.**
A zsh word-split, a buffered pipe, a truncated `kv key list`, a loose grep. Every one is *the
instrument answered plausibly instead of erroring*. That is the corpus's most-cited failure shape
(`reference_match_payload_not_container`) and it fired four times without anyone noticing it was the
same shape four times. ⭐ **The method fix is not more care — it is that a reading which will be acted
on gets a second method before it is acted on**, which is what `d3ef1cc` did correctly with
`household-export` (listing said 4, GET said 2, and *the gap reconciled exactly*). The good instance
and the four bad ones happened the same day.

**D2 · A green check right after an edit was treated as evidence the edit landed.**
Self-reported in `d3ef1cc`'s body: *"My first attempt had a quote-escaping bug and NONE of it applied —
and the tool's selftest passed anyway, on the unmodified file."* Correctly caught, correctly recorded,
and **the note lives only in a commit message.** It is a general rule and it belongs in the principle
library, not in `d3ef1cc`.

**D3 · Same shape again in G3b — a fail-closed control that could never pass.**
`cb29e08`: the missing `cwd=worker/` made every read fail, so the negative control "caught" the planted
defect *for the wrong reason*. **A control proven only by its refusals is not proven.** This is the
third instance today of *X and not-X print the same*, and again the record is a commit body.

**D4 · A retired word was introduced 43 times in commit subjects before anyone checked the glossary.**
`VOCABULARY.md` exists, `check-vocabulary.py` runs at every pickup, and neither was consulted before
minting a tenant noun. ⛔ **And the checker could not have helped** — §3c. The defect is not the tool;
it is that **a new noun entered four commit subjects with no step between coining and committing.**
The cheapest possible fix is not a tool: it is that a word appearing in a commit *subject* for the
first time gets one `git grep` against `VOCABULARY.md` §4. That is ten seconds and it is not automatable
without a permanently-noisy hook.

**D5 · The claim-then-verify ordering in `cd92a5a`.**
The body says *"My first pass converted 41 of what I had counted as 47; the '47' counted LINES."* The
correction is admirable and it is **in the artifact**, which is the right outcome. But the number 47
had already been published in `PRODUCT-ENGINE.md` § WHY THIS SEQUENCES (*"the 47 key-building sites"*)
and in `a696589`'s body **before** the grep settled it. **A count that has not had its predicate
checked should not leave the session it was computed in** — this is the corpus's own rule
(*"6.37 MB across 27 repos with trailers"*), applied to itself.

**D6 · Two engineering briefs sit untracked in a public repo.**
`.engineering/2026-09-05-multi-household-tenancy.md` and `-tenancy-adversarial-read.md`, 892 lines
between them, containing the adversarial security read (L2/L3 KV leak paths) and a ratified tenancy
rule that exists nowhere else (§5). **Untracked means no history, no backup, and no decision about
whether a leak analysis belongs on a public origin.** This is the same class as the
`condo-dweller.md` row the onboarding handoff already flagged — **second instance, same day, and the
first one's flag did not prevent the second.**

**D7 · The concurrent-write, and it is the one I would fix first.**
§0. An audit ran for twenty minutes against a tree that moved, and would have filed a resolved question
as open. ⚠️ **The general form: a subagent has no idea whether HEAD moved under it.** The parent knows;
the subagent does not; and its output reads identically either way. **Falsifier / cheapest test:** have
any agent that produces findings stamp `git rev-parse HEAD` at the start and re-read it at the end, and
say so in its return. Two commands. If that never differs across a month of subagent runs, this is
over-engineering and should be dropped.

**D8 · Not a defect — worth saying, because you asked for the process read and this is part of it.**
Twenty-one commits, four expert returns, a P0 caught by a gate that had never run before, a guard
demonstrated broken *by doing rather than by reasoning*, and a superseded doctrine preserved rather than
overwritten. The defects above are all one shape (an instrument that answers instead of erroring) and
all of them were caught **by you, in the same session**, and written down. The record's problem today
is not rigor. It is that **the best of it is in commit bodies and untracked files**, and that the
surface named `WAITING ON PAUL` does not know any of it happened.

---

## 7 · FALSIFIERS

- **§1b** — if widening the readiness glob to `*-PROPOSAL.md` makes the check red on a healthy
  proposal, the header-only grading split is wrong; revert the glob.
- **§2c** — if a control other than G3 is found reading `estateId` to learn its environment, the
  overload is wider than one guard and the repair is not local.
- **§3a** — if any tracked file already uses `legacy` to mean the GH-Pages viewer, "the second booking
  has not happened" is false. Checked two ways; zero hits at `cb29e08`.
- **§3b** — if `household` is found as an **identifier** anywhere (not a comment, not a string, not a
  filename), this is a migration and not a prose repair. Checked; zero.
- **§4** — if Paul rules a leaf proposal first and nothing breaks, the declared `depends-on:` edges are
  decorative and should be removed rather than trusted.
- **§6·D7** — if `git rev-parse HEAD` never differs across a month of subagent runs, drop the stamp.

---

## 8 · NOT MINE — named and declined

1. **Does Mom migrate over `est-3c9f1a` or to a new estate?** The record holds **both answers, in the
   same `BACKLOG.md` section**: `[paul-stated 2026-09-04 ~10:45 AM]` *"pour in any of Mom's feedback…
   into the **new instance**"*, and the fast-forward procedure `git push origin staging:main` — same
   origin, same prod Worker, same namespace, **her data untouched**. The 11:55 AM amendment separates
   them (*"the fast-forward stays the deploy mechanics"*, but *"her data reaching the **new estate**
   server-side"*) — which describes one event with two destinations. ⛔ **Reporting the contradiction;
   not resolving it.** It turns on whether her history has to be continuous, which is a call about her.
   ⭐ **What is method, and is available now regardless of which way he rules:** `tools/estate-export.py`
   (today `household-export.py`) has been run against **lab only**. Running it read-only against prod's
   namespace prejudges nothing and makes **either** answer cheaper. That is evidence-gathering, not a
   decision.
2. **Whether `qa` and `home` follow `lab` onto real estate coordinates** — §2b/§2c. Each has a distinct
   cost and neither is a method call.
3. **Whether "legacy version" is adopted as canon** — §3a. Paul said it; it is his word to keep.
4. **Whether every estate really gets three environments** — §2e.
5. **The disposition of the two untracked briefs** — §3b·3, §6·D6. A public-repo privacy call.
6. **Which of the five proposals to rule at all.** §4 gives the order *if* he rules them. It does not
   say he should.

---

*Written at `cb29e08`, 2026-09-05. `practice-steward`. Nothing in this file was applied; no plan,
tool, `worker.js`, `VOCABULARY.md` or sibling-repo file was edited.*
