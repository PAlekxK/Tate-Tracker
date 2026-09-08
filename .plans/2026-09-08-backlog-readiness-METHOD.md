# READINESS FOR BACKLOG **ROWS** — what is ready to build now, and what is far off · METHOD

- row: process (no BACKLOG row — same posture as `.plans/2026-09-07-epic-tracking-DESIGN.md`)
- objective: O5
- class: engine · declared (process machinery; nothing here is ranked)
- kind: design
- seats: practice-steward — the whole file
        engineering-partner → **owed if §4's reader is built; designed here, not scoped**
        product-steward → **not dispatched.** It is running beat 5 GROOM & BUCKET at this moment;
          this file is the METHOD for grading readiness, never this lap's board
        ux-expert · content-steward · user-researcher · ai-advisor → waived: no surface, no word that
          reaches a person, no journey, no model on any path in this file
- depends-on: .plans/2026-09-03-backlog-readiness-PROPOSAL.md
- depends-on: .plans/2026-09-07-epic-tracking-DESIGN.md
- gate: ⛔ **NOTHING SHIPS FROM THIS SESSION.** Read-only; no tracked file outside this one was edited,
  no tool changed, nothing deployed. ⛔ **Nothing is ranked.** Every ordering below is dependency,
  evidence or reachability. Where a call needs real-world context it is named as Paul's and stopped at.
- stage-note: 2026-09-08 ET — ⚠️ **`-METHOD` is in neither `DOC_SUFFIXES` nor `KINDS`**
  (`tools/check-backlog-ready.py:69-83`), so **this file is invisible to every instrument in the repo
  while looking exactly like a governed document** — the `-CONSOLIDATION` hole of 2026-09-07, one day
  later, in a file about grading. It declares `kind: design` anyway. Whether `-METHOD` should be added
  belongs to whoever owns that tool, not to a document that would be grading itself.

**Paul's ask, 2026-09-08** *(voice)*: *"we should be able to do some triage on the backlog and just say,
what's ready to build now? And what's very far off from that — right, kind of the different iterations
or versions of readiness… there are plenty of best practices that some Internet research in the process
steward could bring in."*

**Grades used below:** `measured` (run or read at HEAD today) · `inferred` (derived from two measured
facts) · `proposed` (mine, and marked as such).

---

## 0 · WHAT IS ALREADY HERE, MEASURED — and the gap is narrower and sharper than "rows have no stage"

Run at HEAD, 2026-09-08:

| fact | value | how |
|---|---|---|
| the ladder exists and is ratified | `STAGES = draft·ready·concept·design·journey·build·qa·shipped·retro` | `tools/check-backlog-ready.py:59` `measured` |
| WIP is banded, not single-capped | `design 2` · `build 1`; `concept` **deliberately uncapped** | `:88-101` `measured` |
| it grades **documents**, and says so | live run: *"🧭 In flight: …-PLAN.md @ build …"* — 17 files, 0 rows | `measured` |
| rows CAN carry readiness, and 12 lines do | `→ READY · .plans/…` — of which 4 are in the ▶️ NEXT tiers | `grep -c '→ READY' BACKLOG.md` = 12 `measured` |
| the live region | 56 tier rows · **34 not struck** · **4 carry a readiness pointer** | script, §0.1 `measured` |
| **TIER 1 · FIX NOW** | **10 not-struck rows · 0 readiness pointers** | `measured` |
| backlog size / drift | 4,257 lines; ranked list **672 lines below its own head** (limit 400); 76 commits since 09-03 | `check-backlog-drift.py` `measured` |

⚠️ **One correction to the brief I was handed.** *"Zero rows marked READY"* is the PROPOSAL's own
2026-09-03 status line and **is no longer true at HEAD** — 12 lines carry the pointer, 4 of them in the
tiers. It was true on the day it was written. The stale-claim shape, in the file that defines readiness.

### 0.1 ⭐ The actual defect: **absence of a plan file is DEFINED as "fresh request," and Tier 1 asserts the opposite for ten rows**

`check-backlog-ready.py:12-13`, verbatim: *"one file per item that has EARNED one (an IDEATION row has
none — **that absence is the deterministic reading of 'fresh request'**)."*

`BACKLOG.md:692`, Tier 1's own header, verbatim: *"**Nothing blocks these. All agent-drivable.**"*

Both are ratified. Both are about the same ten rows. **They disagree**, and I do not resolve it — which
one should win is a content call. `inferred`, from two `measured` lines.

> ### The structural statement, which IS mine
> **An ungraded row and a raw idea produce the same observation.** So does an ungraded row and a row
> that is unblocked, understood, and buildable this hour. The board cannot distinguish them, and
> therefore **cannot answer either half of Paul's question** — not *what is ready now*, and not *what
> is far off*. This is the corpus's most-repeated failure shape (`practice-steward` foundation, § the
> unnamed shape), sitting inside the instrument built to prevent it.

⛔ **CRITICALITY, in my lane, with the test applied.** *"The readiness instrument cannot see the rows
Paul reads for what to build next"* stays true with every row's business value set to zero — it is a
statement about coverage, not worth. It is **the** finding of this file. It ranks nothing.

### 0.2 Two things a per-row instrument cannot be built over until they move

1. ⛔ **Row addresses collide.** `TIER 1 · 11` (sound pipeline) and `TIER 2 · 11` (weather card) are
   both *"row 11."* `measured`. A stage cannot be attached to an unaddressable row, and this ambiguity
   already produced a real mis-citation in a tracked file today. The PROPOSAL's own `row:` key is
   already tier-qualified (`§ <section> · <label>`, `:1.3`) — **so the fix is to USE that form in prose
   too (`T1·11`), not to renumber.** Renumbering breaks every existing citation.
2. ⚠️ **`✅`-in-text is not `~~struck~~`.** 3 of Tier 1's 10 not-struck rows already read ✅ in their own
   first line (`T1·14` RULED · `T1·18` GUARDED · `T1·16` FIXED + DEPLOYED) `measured`. Any count of
   "open rows" that trusts the strike-through over-reports by ~30% in Tier 1 — `~/.claude/CLAUDE.md`
   § *"An unchecked box is not open work,"* on this file. **A grading reader must exclude them by a
   second predicate, or it will grade closed work.**

---

## 1 · WHAT OUTSIDE PRACTICE ACTUALLY OFFERS — and what is cargo here

The literature assumes a team, a cadence, and several people negotiating. This is one operator, agent
seats, and a loop that rests and fires on a signal. Sorted by whether it survives that translation.

### 1.1 ✅ SURVIVES — **the commitment point** (upstream/downstream Kanban)

Patrick Steyaert's *Essential Upstream Kanban*: the value stream splits at a **commitment point**.
Upstream holds **options** — cheap, plentiful, discardable, *deliberately uncapped*. Downstream holds
**commitments** — WIP-limited, gated, "no longer optional" once crossed
([Nave](https://getnave.com/blog/upstream-kanban/) · [Businessmap](https://businessmap.io/blog/patrick-steyaert-customer-kanban) ·
[Aktia](https://aktiasolutions.com/discovery-kanban-upstream-kanban/) ·
[Steyaert, LKNA17 PDF](https://ku-training-materials.s3-us-west-2.amazonaws.com/LKNA17/End-to-End+Flow+with+Customer+and+Upstream+Kanban_Patrick+Steyaert.pdf)).

⭐ **Paul has already built both halves and the line between them, and has no name or reader for it.**
`concept` is uncapped *by ruling*, with the reason stated on its face — *"a concept costs nothing to
hold, and capping it pushes ideas out of the record"* (`:93-95`). `build`/`qa` is capped at 1. The gap
between them **is** the commitment point. It needs no import except the word and an instrument.

Why it survives solo: it is not a coordination protocol. It is a statement about which side of a line a
thing sits on, and it is answerable by one person about their own work.

### 1.2 ✅ SURVIVES — **"detailed appropriately"** (DEEP), i.e. readiness is a GRADIENT, not a gate

Pichler/Cohn's DEEP: *higher-priority items are more granular and detailed; the lower the priority, the
less detail it carries* — the iceberg
([Mountain Goat](https://www.mountaingoatsoftware.com/blog/make-the-product-backlog-deep) ·
[ProductPlan](https://www.productplan.com/glossary/deep-backlog)).

This is exactly Paul's *"different iterations or versions of readiness."* The import is **one sentence,
and it is a licence rather than a burden**: a row far from build is *supposed* to be thin, and thinness
is therefore **not a defect to flag**. That single line is what stops any readiness reader from becoming
the permanently-red control Paul has ruled against.

⛔ **Estimated** and **Prioritized** — two of DEEP's four letters — are **not imported.** Estimation is
team-throughput machinery, and prioritisation is Paul's alone. Taking two letters of a four-letter
acronym is the honest translation, not a partial one.

### 1.3 ⚠️ SURVIVES ONLY RISK-TIERED — **Definition of Ready**

The practice's own literature is the case against it. Robert Galen, *Definition of Ready as an
Anti-pattern* ([rgalen.com](https://rgalen.com/agile-training-news/2016/11/8/definition-of-ready-as-an-anti-pattern));
Agile Pain Relief: *"beware of turning such a practice into a dogmatically applied approval gate… only
cover the details that are currently causing problems, and hold on to the definition lightly"*
([agilepainrelief.com](https://agilepainrelief.com/glossary/definition-of-ready/)); Scrum.org on backlog
anti-patterns ([scrum.org](https://www.scrum.org/resources/blog/product-backlog-anti-patterns-your-questions-answered)).
The named failure is that work gets stuck **because it does not meet the criteria**, not because it is
not understood.

⭐ **This repo already has the antidote, from a different tradition**: `~/.claude/CLAUDE.md`, `[paul-ruled
2026-09-04]` — *"the gate sits on irreversible acts, never on work."* Applying it to readiness gives the
**risk-tiered DoR** of GitHub's Minimum Viable Governance model (this seat's reference library): **the
evidence burden scales with what a mistake costs, never with what the item is worth.** That is §2's
whole design, and it is the one thing that keeps a heavy plan-file requirement from suffocating a
ten-minute Tier 1 fix.

### 1.4 ✅ SURVIVES, as a warning — **Shape Up's "no backlog"**

Basecamp discard un-bet pitches outright; *"if it matters enough, someone will re-pitch it"*
([Bets, Not Backlogs](https://basecamp.com/shapeup/2.1-chapter-07) ·
[The Betting Table](https://basecamp.com/shapeup/2.2-chapter-08)).

⛔ **Explicitly rejected for this corpus, and the evidence is local:**
`.plans/2026-09-07-dropped-ideas-MINE.md` exists *because ideas leaked once already*, and the uncapped-
`concept` ruling names that as the one failure this record cannot afford. Shape Up's discard rule assumes
a company that regenerates ideas from many heads. **One operator's dropped idea does not come back.**
What survives is only the *distinction*: **shaped vs. unshaped**, which is §1.1's line under another name.

### 1.5 ⛔ CARGO — do not import

| practice | why it does not translate |
|---|---|
| refinement / grooming **ceremonies** on a cadence | the loop rests and fires on a signal (`MOM-CYCLE-MAP.md`); a scheduled refinement converts it to a backlog-driven loop — the exact thing `check-backlog-drift.py`'s own doctrine forbids |
| story points, velocity, burndown | measure a team's throughput against itself; n=1, and Paul's corpus contains zero occurrences of any of them |
| WSJF / RICE / Cost-of-Delay scoring | **value ranking. Out of my lane entirely.** Paul's, at COMMIT, and the cycle map says no instrument is ever built for it |
| a "Ready" column on a board | Personal Kanban's own guidance is *"avoid columns unless each column changes what you do next"* ([super-productivity](https://super-productivity.com/blog/personal-kanban-for-developers/)); this repo has a ladder already |
| two-way "business commits / team confirms" handshake | both parties are Paul |

**And Real Options** ([InfoQ](https://www.infoq.com/articles/real-options-enhance-agility/)) — *options
have value, options expire, never commit early unless you know why* — is **already ratified here in
Paul's own words**, one clause per rule: DEFERRED rows carry *"the gate that would unblock it"*
(`BACKLOG.md:12`). It is cited as corroboration, not imported as a method.

---

## 2 · THE PROPOSAL — one reader, one line, zero new vocabulary

> ### The design in one sentence
> **Reuse `STAGES` exactly as written; make the ladder read ROWS as well as documents; make
> `⬜ ungraded` PRINT instead of being silence; and tier the evidence burden by REVERSIBILITY so the
> plan file is required where a mistake is expensive and not where it is not.**

### 2.1 The three bands Paul asked for, mapped onto rungs that already exist

| Paul's phrase | rung | side of the commitment point |
|---|---|---|
| **"ready to build now"** | `ready` | at the line — the last upstream rung |
| **"the different iterations between"** | `draft` → `concept` → `design` → `journey` | upstream (options; uncapped by ruling) |
| **"very far off from that"** | `⬜ ungraded` — nobody has looked, **and the board now says so** | upstream, unassessed |
| *(past the line, not asked about)* | `build` → `qa` → `shipped` → `retro` | downstream (commitments; WIP 1) |

⭐ **`⬜ ungraded` is the only new thing, it is not a new word, and it is already rendered.** The tool
prints exactly this today for documents: *"⬜ 8 typed document(s) carry NO header block at all — **not
graded, and NOT clean**"* (`measured`, live run). **The whole proposal is: extend that one rendering to
the live backlog region.** `unknown` is never counted as healthy — the epistemic primitive Paul already
runs everywhere else.

### 2.2 The commitment point is an INVARIANT, not a policy

> **A row with no plan file can never be graded past `ready`.**

Checkable, derived, needs nobody's honesty. It gives the upstream/downstream line a deterministic
reading, and it is *already true in practice* — every stage past `ready` is currently derived from a
plan file's `stage:` key and from nothing else (`measured`).

### 2.3 ⚠️ Risk-tiered evidence — the one place I propose changing a ratified rule, and the argument

Today `ready` has **one** evidence standard: five fields + declared seats + a plan file + Paul's stamp
(PROPOSAL §1.2). That standard is correct for `T2·12` (per-estate canon store, engine · must-not-diverge)
and is **the reason Tier 1's ten rows are ungraded** — none will ever earn a plan file, so none can ever
be graded, so the board is permanently silent about exactly the rows it labels *FIX NOW*.

**Proposed:** two lanes, chosen by a **derived** predicate, not by judgment.

| lane | fires when | `ready` costs |
|---|---|---|
| **HEAVY** *(unchanged — do not touch it)* | `class: engine`, **or** anything reaching a person's surface, **or** anything irreversible/multi-file | the existing five-field plan file + seats + `ready: [paul-approved …]` |
| **LIGHT** *(new)* | everything else — `instance`/`config`, reversible, no surface reaching Mom | **one line on the row**: `→ ready · O<n> · <the check that proves it landed>` |

The light lane's two tokens are not ceremony: `O<n>` is the alignment trace Paul commissioned
`OBJECTIVES.md` for, and *the check* is already **ruled mandatory for every item** — `CLAUDE.md`
§ *EVERY ITEM SHIPS WITH AN ASK, A CHECK AND AN ATTRIBUTION* `[paul-ruled 2026-09-07]`, whose own
load-bearing clause is *"an event with no reader is not instrumentation."* ⭐ **The light lane asks for
nothing new. It asks for the 09-07 ruling to be written down at the moment the row is picked up rather
than after the build.**

⛔ **Lane assignment is derived, never chosen.** The class label already exists on rows
(`[paul-ratified 2026-09-02]`). A row with no class label is **HEAVY by default** — fail-closed.

### 2.4 ⛔ What I did NOT propose, and why

- **No new status word.** `READY` was minted 09-03 against a stated test; nothing here needs a second.
- **No `epic:` key.** `.plans/2026-09-07-epic-tracking-DESIGN.md` §1.4 forbids it; the objective is the
  epic key, and §2.3 uses `O<n>` for exactly that reason.
- **No retrofit of ~344 rows.** The PROPOSAL forbade it (`:1.3`) and it was right. **Only the ▶️ NEXT
  live region is graded — 34 rows** — and only lazily (§3.2).
- **No reordering of anything.** `product-steward` is running beat 5 GROOM & BUCKET at this moment.

---

## 3 · HOW A ROW EARNS A STAGE — checkably, and mostly without anyone typing

### 3.1 Derived first — four of the six rungs need no human token at all

| rung | earned by | verifiable |
|---|---|---|
| `⬜ ungraded` | **the default.** No pointer, no gate line, no plan | trivially |
| `draft` | the row **names its gate** — what would have to be true. The `DEFERRED` taxonomy already requires this (`BACKLOG.md:12`); a Tier-3 row's `question:` + `capture:` columns are the same thing under another name | presence of a gate/question token |
| `ready` | HEAVY: the plan file passes the existing check. LIGHT: the one-line token of §2.3 | file + fields, or the token |
| `concept`…`retro` | **read off the plan file's `stage:`**. Nothing typed on the row | already implemented |

`measured` (script, HEAD 2026-09-08): this derives **19 of the 34** live rows on day one at zero typing
cost — **4** plan pointers (all in Tier 2) + **15** rows carrying a gate or a Tier-3 question line
(T1 2 · T2 7 · T3 6). The other **15 print `⬜ ungraded`**, and **8 of those 15 are Tier 1** — the band
the board labels *FIX NOW*. That asymmetry is the finding, not the total. ⚠️ The gate predicate is a
keyword read over prose and will over-count; a built version must anchor on a declared token, and until
it does, **19 is an upper bound.**

### 3.2 ⭐ Grading is LAZY — a row earns its grade when it is picked up, never in a sweep

This is the PROPOSAL's own ratified principle (*"a row earns its file when picked up"*) extended one
step. It matters for three reasons:

1. It makes the scheme cost **one line at the moment someone is already reading the row**, not a
   grooming pass. No ceremony is created, which is §1.5's whole warning.
2. It means `⬜ ungraded` **decays as work happens** rather than needing a campaign.
3. ⛔ It is the only version that cannot become permanently red — see §4.

### 3.3 Who promotes, and what no tool may claim

| act | who |
|---|---|
| derive a rung from a file that exists | the tool |
| write a LIGHT `→ ready` token | any seat or session picking the row up |
| write a HEAVY `ready: [paul-approved …]` stamp | **Paul, or on his explicit go.** Unchanged |
| decide a row's tier, priority, or which of two rows goes first | **Paul.** Not modelled here, and no instrument is proposed for it |

⛔ **What the reader may never claim:** that a grade is *right*, that a gate is *real*, or that anyone
*understood* the row. It reports that a token exists and what backs it. Judgment stays with the seats
and with Paul — the boundary the 09-03 check already states on its own face (`:32-34`).

---

## 4 · WHAT IT PRINTS — three numbers, no verdict, no exit-1

One block, in the session-start pickup, beside `check-backlog-drift.py`:

```
📊 Backlog readiness — ▶️ NEXT live region, 34 rows
   ✅ ready to build now ....  N   (M heavy · K light)
   🔧 in the iterations ....   N   draft · concept · design · journey
   ⬜ ungraded ............... N   nobody has looked — NOT clean, and NOT a defect
   ⛔ 3 not-struck rows read ✅ in their own text — closed, or the record is behind
```

⚠️ **`ungraded` is COUNTED, NEVER GRADED — and this is the load-bearing constraint.** It is a coverage
line, exactly as `~/.claude/rituals/CYCLE-SPINE.md` treats spine conformance, and for exactly Paul's
stated reason: *he will not install a metric that reads red forever, even a true one.* A backlog with
20 unassessed rows is **healthy** — that is DEEP's *detailed appropriately* (§1.2). The reader therefore
**exits 0 always** and prints no ⚠️ on the ungraded count at any threshold.

⛔ The **one** line that may go red is the last one, and it is not about readiness — it is the
`✅`-in-text-but-not-struck contradiction of §0.2, **reported, not resolved**: closed work and a stale
record produce the same text, and which is true needs a probe against the world.

---

## 5 · FALSIFIER, AND WHAT THIS COSTS

**Falsifier (primary), read at the next lap close, not by argument:**
> If, after one full lap, **no row was promoted at pickup** and the `⬜ ungraded` count is unchanged,
> then grading is happening nowhere, the reader is decoration, and **it should be deleted rather than
> tuned.** This is the PROPOSAL's own falsifier shape, applied to its successor.

**Falsifier (secondary), and it is the sharper one:**
> If a row is graded `ready` and then the next build is picked **without anyone reading the grade** —
> i.e. the board's readiness column changes nothing about what happens next — the scheme is
> *descriptive*, not operative. A description of readiness that never routes a decision is ceremony
> with a tool attached.

**Falsifier for §2.3 specifically:**
> If any LIGHT-lane row's `→ ready` token is written **after** its build, to make the count look right,
> the light lane is a rubber stamp and the HEAVY standard should be restored for everything.

**Cost, stated honestly:**

| where | cost |
|---|---|
| per lap | one reader in the pickup block; ~1 s; **zero** typing if nothing is picked up |
| per row picked up | **one line**, LIGHT lane — and both of its tokens are already ruled mandatory (§2.3) |
| HEAVY lane | **unchanged.** No new burden anywhere |
| build | one tool, sited beside `check-backlog-drift.py`; selftest by mutation, per this repo's convention |
| prerequisite | tier-qualified row labels in prose (`T1·11`), §0.2 — **not** a renumber |

⚠️ **The honest risk:** the live region moves fast (76 commits to `BACKLOG.md` in 5 days, `measured`), so
a reader that parses tier tables by line offsets will break on the next rationalization. It must anchor
on the `## 🔥 TIER` / `## ✅ TIER` / `## 🧭 TIER` headings and **fail CLOSED** — an unparseable region
prints UNREADABLE, never zero. Never green by absence.

---

## 6 · WHAT IS PAUL'S, AND IS STOPPED AT HERE

1. **The Tier 1 contradiction (§0.1).** *"Nothing blocks these"* vs *"absence of a plan file means fresh
   request"* — both ratified, both about the same ten rows. **Reported, not resolved.**
2. **Whether the LIGHT lane exists at all.** It relaxes a rule he approved five days ago. My argument is
   §1.3 + §2.3; the call is his.
3. **Whether `-METHOD` joins `DOC_SUFFIXES`** (this file's own header note).
4. ⛔ **Every priority, tier and ordering question.** Nothing in this file ranks anything, and no
   instrument is proposed that could.

**Adjacent Paul-voiced support for the whole shape, cited as adjacent and not as demand:** `C08-052`,
2026-08-17 — *"a ready to fire, right, or a trigger column."* And `BACKLOG.md:4245` (`P-27`, an existing
agent proposal, unaccepted): *every deferred gate needs a reader* — §3.1's `draft` rung is the same
mechanism arriving from the other direction, and if Paul takes one he should look at both together.
