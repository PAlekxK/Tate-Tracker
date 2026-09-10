# ③ the link syntax and ④ what a `-PROPOSAL` is — two rulings, dug, with a recommendation each

- row: none — a ruling packet for Paul; the ruling is an EVENT (`.decisions/fernwood-22`, G1 packet ④/⑥), not an item. ⚠️ Written in the three-state `row:` vocabulary this file proposes, so today's checker will flag it — that is the worked example, not an oversight
- objective: O5
- class: engine · declared
- kind: decisions
- stage: draft
- ready: agent-proposed 2026-09-10 — **Paul rules.** Nothing below is applied.
- commissioned: `tate-tracker-af` on Paul's ask, 2026-09-10 — *"ruled so you can move… a recommendation with the digging actually done"*
- seats: practice-steward → **not consulted; its audit ran independently** (`.plans/2026-09-10-backlog-management-AUDIT.md`, `0fe685a`) and is compared in §5, unsmoothed · engineering-partner → **waived**: the cost lines are the registrar's own counts and are to be re-measured at build
- depends-on: `.decisions/fernwood-22.md` · `.plans/2026-09-10-G1-RULING-PACKET.md` · `.plans/2026-09-10-backlog-registrar-PROPOSAL.md`
- author: the backlog registrar (`tate-tracker-4c`), measured 2026-09-10 ~5:00–5:30 PM ET while HEAD moved `2488394` → `d6c2f37` under the session (three lane merges and the audit landed mid-reading; `BACKLOG.md` itself changed only by the registrar's own commits in that span, `git diff --stat`)

> ⛔ **FLAG AND PROPOSE.** Every count below was measured this session by the command beside it. A count locates; the line was then read. Paul's lean on ③ was **tested, not justified** — it survives, with one amendment that decides whether it lasts.

---

## 0 · The two recommendations, one screen

| | recommendation | one-line evidence | cost | falsifier |
|---|---|---|---|---|
| **③ link syntax** | ✅ **Adopt `→ PLAN ·` as the status-free link, keep `→ READY ·` for the stamped — AND make the checker read BOTH directions against the plan header.** Without the second half, `→ PLAN ·` decays exactly as `→ READY ·` did | 12 pointers measured against their own plan's `ready:` line: **2 false, 5 true with stale prose, 5 consistent.** The checker compares a pointer to its header in **zero** directions today (`check-backlog-ready.py:281-285`) | ~35 lines in one tool, 1 definition sentence, 2 pointer flips | after landing, the orphan count may fall **only** through `→ PLAN ·` pointers, never new `→ READY ·` ones; the checker prints 2 READY-vs-header mismatches today and 0 after the flips |
| **④ `-PROPOSAL`** | ✅ **Neither document nor item — the file DECLARES its intent in the `row:` it already carries**, normalised to three states: `none` · `proposed` · `<pointer>`. The suffix stops being the axis | 21 proposals are **three kinds**: 7 consumed records with no header, 11 process items-in-waiting that say *"this proposes one"*, 3 product items naming the row they want. The intent is already written in 21 files in ~11 phrasings | ~40 lines in the checker, 21 one-line header edits (scripted, diff for Paul), one `UNGRADED_BY_DESIGN` entry retires | the 14 `proposed` files print as AWAITING and no longer as orphans; if a `row: none` file is ever built as an item, the intent was mis-declared (R4's own falsifier) |

⭐ **Both recommendations are the same shape**, and it is the shape this repo already trusts six times over (`check-data-inline`, `build-viewer --check`, `check-domains`…): **one source, N readers, a drift check.** The source is the plan header. The register's link is a reader. Today it is a second writer.

---

## 1 · ③ THE LINK SYNTAX — what was measured

### 1a · All twelve `→ READY ·` occurrences, classified against the plan's own `ready:` header

`grep -n '→ READY ·' BACKLOG.md` → 12 (line numbers as of `ea63a0e`, after the registrar's 27-line insertion; the handoff's `:1129`/`:1441`/`:2971`/`:3016`/`:3281`/`:3297` are the same rows at `27d4f1a`). ⛔ The classification axis is **the plan header**, because `BACKLOG.md:14` itself says the header *"carries the five-field readiness record."* The row is a reader of it.

| line | plan | plan `ready:` | plan `stage` | what the row's prose says | verdict |
|---|---|---|---|---|---|
| :14 | — | — | — | the definition | **definition, not a use** |
| :139 (1st) | onboarding | `[paul-approved 2026-09-05]` | qa | *"Paul rules on the plan"* | pointer **TRUE**, prose **stale** (stamped five days ago) |
| :139 (2nd) | vocabulary-nicknames | `DRAFT — Paul has not stamped` | concept | *"awaiting Paul's stamp — the pointer is the readiness check's row shape, not a claim"* | 🔴 pointer **FALSE**; prose honest |
| :248 (row 7) | zones | `[paul-approved 2026-09-07]` *"authorises the STAGE, not the build"* | design | *"stage `design`, awaiting Paul's `ready:` stamp"* | pointer **TRUE**, prose **stale** |
| :249 (row 8) | capture-write-path | `[paul-approved 2026-09-07]` same caveat | concept | *"the `build` call is Paul's when it gets there"* | **consistent** — the prose names the build gate, a different gate (the coordinator was right) |
| :250 (row 9) | derived-first-draft | `[paul-approved 2026-09-07]` same caveat | concept | *"Scoping is Paul's"* | **consistent** — same |
| :252 (row 11) | weather-card | `[paul-approved 2026-09-08]` | concept | *"the `ready:` stamp waits on it"* | pointer **TRUE**, prose **stale** (stamped 09-08, §0-PRIME-H) |
| :1156 | frozen-fernwood-catchup | `agent-proposed 2026-09-07 — Paul rules` | concept (declared exception) | *"now has a plan of record"* — **no disclaimer at all** | 🔴 pointer **FALSE**; prose silent — **the only row that lies to the instrument with nothing in prose to catch it** |
| :1468 (A6) | guru-retrieval | `[paul-approved 2026-09-03]` | build | *"✅ STAMPED … Not stamped."* | pointer **TRUE**; prose **self-contradicting** — *"Not stamped."* sits directly before a Paul quote from **07-28**, i.e. it is the pre-stamp sentence never deleted |
| :2998 (C4) | c4-environments | `[paul-approved 2026-09-03]` | build | *"✅ READY"* | **consistent** |
| :3043 (C5) | c5-record-prep | `[paul-approved 2026-09-03]` | retro | *"✅ STAMPED"* | **consistent** |
| :3308 (C6) | c6-door-for-paul | `[paul-approved 2026-09-03]` | build | *"✅ STAMPED"* | **consistent** |
| :3324 (C7) | c7-condo-paper-model | `[paul-approved 2026-09-03]` | ready | *"✅ STAMPED … Not stamped."* | pointer **TRUE**; prose **self-contradicting** — same leftover shape as A6 |

**Tally: 2 false pointers · 5 true pointers under stale or self-contradicting prose · 5 consistent.** ⚠️ **The handoff's "four rows that write it and disclaim it" was the wrong predicate.** Three of its four (`:139`, `:248`, `:3297`) are rows whose *prose* is behind a *true* stamp — the register is not lying to its instrument there, it is lying to its **reader**. The instrument-lie is two rows, and one of them (`:1156`) has no prose disclaimer at all, so it was invisible to the predicate that produced "four."

⭐ **On `:3297`/`:3324` and `:1468`, the coordinator's sharpest question:** *a row asserting both states in one line.* Read against the header it is not a paradox — the stamp is real (`2026-09-03`), and *"Not stamped."* is the sentence from **before** the stamp, left standing. That is a **stale-prose** defect, the same class as `:139`/`:248`/`:252`, not a new class. It does change what the fix has to do in one respect: **nothing mechanical can repair prose.** A checker can flag *"the row's prose says 'not stamped' and its header says stamped"* (a two-token grep) — and that flag is worth adding — but the sentence is a lane's or Paul's to delete.

### 1b · The stage ladder settles "is a stamped concept-stage plan READY?"

`check-backlog-ready.py:60` — `STAGES = draft · ready · concept · design · journey · build · qa · shipped · retro`. **`ready` precedes `concept`.** The stamp is the gate *into* the ladder, not the gate into build, and the checker already enforces it that way (`:421` — *"stage concept with no paul-approved stamp — built without the gate"*). So the three 09-07 plans stamped *"as it is"* are READY in the ladder's sense, whatever the caveat in their header says about the build. **`:14`'s prose definition** (*"cleared by Paul; waiting its turn"*) reads compatibly. The ambiguity I opened this reading with dissolves; I record it because the next reader will open it too.

### 1c · What else consumes `→ READY ·`

`grep -rn 'READY ·' . ~/.claude --include='*.py' --include='*.md' --include='*.sh' --include='*.js'` (quoted; the unquoted form returns nothing under zsh — measured):

- **Exactly one parser:** `POINTER_PAT`, `tools/check-backlog-ready.py:114`, plus its four selftest fixtures (`:540`, `:654`, `:660`, `:673`). Nothing in `~/.claude`. No sweep, hook or skill.
- **Prose mentions, 14 files:** `MOM-CYCLE-MAP.md:128` (describes the check) · `.plans/2026-09-03-backlog-readiness-PROPOSAL.md:177` (defines it) · `.plans/2026-09-08-backlog-readiness-METHOD.md:43` · five plans' *"At the stamp: § X gains `→ READY ·`"* procedure lines (C4, C5, C6, C7, guru — **still true after the change**; a stamp still adds READY) · two plans that embed the pointer text inside a proposed row (`derived-first-draft-PLAN.md:306`, `capture-write-path-PLAN.md:317`) · `c3-trace-query-PLAN.md:98,171` · `product-name-PLAN.md:283` · `testing-architecture-PLAN.md:16,484` · `fernwood-22` · both registrar documents · the audit.

**So a second syntax costs one regex, not a migration.** The prose mentions describe the READY case and stay correct.

### 1d · What `→ PLAN ·` actually buys, in names

The 29 orphans (`check-backlog-ready.py`, this session) are 29 files that today **cannot link to a row without claiming readiness.** That is the whole generator of the *"orphan flag is expected"* habit — **12 plans now carry that sentence in their header** (`grep -li orphan` over the first 40 lines; the audit counts 10 by a narrower phrase). The register taught its authors to argue with the checker because the checker offered no honest verb.

After the change, a draft-stage plan links with `→ PLAN ·` and is neither an orphan nor a liar. The two false pointers flip to `→ PLAN ·`: `:139` vocabulary-nicknames and `:1156` frozen-fernwood-catchup. Nothing else moves.

### 1e · Cost of `fernwood-22` option (c), counted

| what | where | size |
|---|---|---|
| accept both keywords and capture which | `POINTER_PAT` `:114` | 1 line |
| **READY pointer → header must be stamped** (new finding) · **PLAN pointer → header must NOT be stamped** (new finding: *"promote the link"*) · prose *"not stamped"* beside a stamped header (new finding) | `check()` after `:285` | ~20 lines |
| orphan predicate reads either keyword | `:281`, `:340` | 2 lines |
| selftests: false READY flagged · stale PLAN flagged · PLAN pointer is not an orphan | `selftest()` | ~12 lines |
| define `→ PLAN ·` beside READY | `BACKLOG.md:14` | 1 sentence |
| flip the two false pointers | `BACKLOG.md:139`, `:1156` | 2 tokens |
| describe the second syntax | readiness-PROPOSAL `:177`, METHOD `:43`, MOM-CYCLE-MAP `:128` | 3 one-liners, optional |
| close the card | `fernwood-22` → an event in operating-layer's `decisions.jsonl`, never the card file | 0 lines here |

**~35 lines of tool, ~6 of prose, one sitting.** ⛔ **The five stale-prose rows are NOT in this cost** — they are flagged to their owners, not rewritten by the registrar.

### 1f · Steelman for leaving it alone — and why it loses

**The case:** two syntaxes are two things to get wrong. *"A row with no plan file is a fresh request by construction"* (`:14`) is a real, load-bearing property today, and READY-as-the-only-link is what makes it true. And the flags might simply be the honest price of a strict rule.

**Why it loses, measured:** (1) the property survives — under the change it reads *"a row with no `→ PLAN ·` or `→ READY ·` is a fresh request,"* which is the same sentence with one more word. (2) The flags are **not** the honest price of the rule: 13 of the 29 orphans self-declare that no row should exist yet, so the alarm is asking a question that does not apply — a red the population has learned to immunise itself against, which is the state `check-backlog-ready.py:398-402` already rules against for other flags. (3) **The one-syntax world is the one that produced the two false pointers.** With only READY available, a writer who wanted a link wrote READY and disclaimed it — or, at `:1156`, did not. Two syntaxes with a checker that reads both directions can be *wrong and caught*; one syntax could only be *wrong and disclaimed*.

⭐ **And the amendment that decides whether Paul's lean lasts:** `→ PLAN ·` alone reproduces the disease with a new word — a plan gets stamped and its `→ PLAN ·` link stays, and a year from now someone finds "eleven PLAN pointers on stamped plans." **The bidirectional check is not optional; it is the part that makes the syntax derived instead of typed.** If the checker cannot be extended, do not add the syntax.

### 1g · Falsifiers for ③

1. **The audit's own (`AUDIT.md:440`), adopted:** if the orphan count falls after landing *because new `→ READY ·` pointers were added* rather than because `→ PLAN ·` and the bidirectional predicate landed, that is false clearance and the ruling is being gamed.
2. `check-backlog-ready.py` prints **2** READY-vs-header mismatches the day it learns to look (`:139`, `:1156`) and **0** after two token flips. Any other number means the classification in §1a is wrong.
3. Within 14 days of landing, if a `→ PLAN ·` pointer is found on a stamped plan **without** a flag, the bidirectional half failed and §1f's warning was right.
4. If any lane writes a **third** keyword, the two-keyword design under-modelled the states and the audit's *"the schema has fewer states than the work"* applies to this fix too.

---

## 2 · ④ WHAT A `-PROPOSAL` IS — what was measured

### 2a · The coordinator's reframe, tested: it holds

*"The real axis is INTENT — whether anyone means to do the thing."* Measured on all 21 `-PROPOSAL` files by reading each header's `stage:` · `ready:` · `kind:` · `row:` (script in this session; table below). **Three kinds wear the suffix, and each file already says which it is, in its `row:` line, in free prose.**

| kind | n | files | what their `row:` says today | what they are |
|---|---|---|---|---|
| **A · consumed record** — no header at all | **7** | 07-29-rationalized-backlog · 09-02-rationalization · 09-02-vocabulary · 09-03-backlog-readiness · 09-03-c4-process · 09-03-c5-manifest-check · 09-06-maps-and-zones | *(none)* | proposals that were **applied and superseded** — `a6c89a8` applied the first; `VOCABULARY.md` is `paul-ratified`; `BACKLOG.md:14` is the readiness one stamped; `tools/check-engine-manifest.py` exists; maps-and-zones is cited by its own `-STATE` successor. **Documents. They never wanted a row.** |
| **B · process item-in-waiting** | **11** | 09-03-grooming-conversation · 09-03-privacy-scrub · 09-03-qa-test-vs-ux-review · 09-05-journey-as-prioritizer · 09-05-journey-test-cycle · 09-05-process-registry · 09-05-release-cascade-tracking · 09-05-state-of-the-work · 09-06-user-feedback-cycle · 09-07-lap3-PROCEDURE · 09-10-backlog-registrar | *"process (no BACKLOG row yet — **this proposes one**)"* or *"same posture as …"* — 11 phrasings of one state; every `ready:` reads *agent-proposed — Paul rules* | **items somebody means to do, awaiting Paul.** Not orphans: an orphan is a file that claims a row that is not there |
| **C · product item naming its row** | **3** | 09-03-c3-trace-query · 09-07-input-to-value-matrix · 09-07-sign-in-door | *"`BACKLOG.md` § C3 …"* · *"§ FOUR RULINGS · rule 5"* · *"§ C6 (ROW TO ADD)"* | **items that name the section they want a row under.** Two of the three are what the audit calls *"a real row the predicate does not read"* |

⭐ **The suffix is the wrong axis and the header is the right one — and the header is already there.** Nobody has to decide what a proposal *is*; 21 authors already decided, per file, and wrote it where the checker does not look.

### 2b · What each option does to the twenty-one, by name

| option | A (7 consumed) | B (11 in-waiting) | C (3 naming a row) | net |
|---|---|---|---|---|
| **"a `-PROPOSAL` is a DOCUMENT"** | correct — become `kind:` records | 🔴 **lose their standing**: eleven things somebody means to do become invisible to the readiness instrument; the registrar's own file among them | 🔴 same | fixes 7, hides 14 |
| **"a `-PROPOSAL` is an ITEM"** | 🔴 **7 rows manufactured** for things already applied — *two of everything*, the file's recorded failure | rows authored before Paul rules — 11 unruled rows in the register | 3 rows, plausibly right | fixes 3, manufactures 18 |
| ✅ **"the file declares its intent: `row: none` · `row: proposed` · `row: <pointer>`"** | `row: none` + `kind:` → documents, never flagged | `row: proposed …` → listed **AWAITING** (the sweep's ⬜ state, one vocabulary across both instruments), never an orphan | `row: proposed — § C3 …` until Paul rules, then a `→ PLAN ·` pointer lands and the file's `row:` becomes the pointer | **0 orphans among proposals; 0 rows authored; 21 one-line edits that only make explicit what each file says** |

### 2c · Does it generalise to `-SCOPE`, `-DESIGN`, `-ASSESSMENT`, `-AUDIT`? — yes, and say it loudly

The three-state `row:` is a property of a **file**, not a suffix. Every one of the 29 orphans is discharged by the same field: the 13 PLAN/other orphans that declare `process (no BACKLOG row …)` become `proposed` or `none`; the 6 that *"declare a real row the predicate does not read"* (audit §2·B) are placed or corrected the moment the predicate reads their side. ⛔ **The 23 "graded by nothing" suffixes are a DIFFERENT question** — R4's *"say what it IS"* (`kind:`) — and stay open. This ruling settles the **orphan** question for every suffix and settles nothing about `kind:`. ⭐ The checker's own comment already names the fix for that one: the `DOC_SUFFIXES` allowlist *"fails open, and that is the defect"* (`:82`). Separate row.

### 2d · The worked example — the registrar's own file

`.plans/2026-09-10-backlog-registrar-PROPOSAL.md` reads `row: BACKLOG.md § ▶️ NEXT (process; no row yet — this proposes one …)`. Under the ruling it becomes `row: proposed — § ▶️ NEXT …` and prints as **AWAITING** until G1 packet ⑧ rules on the seat; if ⑧ rules yes, the row the ruling creates carries `→ PLAN ·` (stage `draft`, never READY until stamped) and the file's `row:` becomes that pointer. **This file** carries `row: none` from birth because a ruling packet is a document. Both are flagged by today's checker and correct under tomorrow's.

### 2e · Cost, counted

| what | where | size |
|---|---|---|
| parse `- row:` into `none` / `proposed` / pointer, **generously** (the sweep's `none`-after-an-em-dash lesson: an instrument that only works when its users are precise measures its users) | `check-backlog-ready.py` near `:206` `parse_plan` | ~15 lines |
| orphan = *pointer declared and not found* **or** *BACKLOG points at a plan whose `row:` disagrees* — the bidirectional predicate the audit also asks for | `:340` | ~10 lines |
| `proposed` files print under one **AWAITING** header, named, never counted alone | `report` | ~8 lines |
| selftests: `none` is quiet · `proposed` is AWAITING · a declared pointer that is absent is an orphan · a BACKLOG pointer to a `row: none` file is a disagreement | `selftest()` | ~12 lines |
| retire the `-PROPOSAL` line in `UNGRADED_BY_DESIGN` | `:95` | −1 line |
| normalise 21 proposal headers (+ the 13 other orphans if desired) — scripted, **a diff for Paul**, prose preserved after the keyword | `.plans/*.md` | 21–34 one-line edits |

**~45 lines of tool, one scripted header pass.** ⛔ The header edits are transcription of what each file already says; anything a script cannot classify prints as UNCLASSIFIED and waits for a human, never defaults.

### 2f · Falsifiers for ④

1. After landing, `check-backlog-ready.py` lists **14** proposals as AWAITING and **0** as orphans; the orphan list shrinks to files that claim a row that is not there (≤ 6 today). Any other numbers mean §2a's classification is wrong.
2. **R4's own falsifier, inherited:** if a `row: none` file is ever tracked through build → shipped, its intent was mis-declared and the axis mis-read for that file.
3. If a file gains a `BACKLOG.md` row while its `row:` still says `proposed`, the field is decorative — and the registrar sweep will show it, because the placement prints against a file that still claims to be waiting.
4. If lanes keep writing *"orphan flag is expected"* into headers **after** landing, the alarm was not the generator of the habit and the audit's mechanism-1 (*"the schema has fewer states than the work"*) is still true somewhere this did not reach.

---

## 3 · What is NOT in this packet, on purpose

- **The five stale-prose rows** (`:139` onboarding, `:248` zones, `:252` weather, `:1468` guru, `:3324` C7) — flagged here, owed to their lanes or Paul; the registrar rewrites no prose it did not transcribe.
- **The 23 ungraded suffixes / `kind:`** — R4's question, a separate row (§2c).
- **Who owns the register** (G1 ④, the mom + fleet loops) — the audit §3·B challenges the *evidence* offered for a sole writer, not the ruling; both are Paul's and unchanged.

## 4 · What Paul is asked to say

- **③:** *"(c), with the bidirectional check"* — or *"leave it"*, in which case §1f's third point is the cost accepted.
- **④:** *"intent, three states"* — or *"document"* / *"item"*, in which case §2b's row says what happens to the 21 by name.
- Either way: **who flips the two false pointers and who normalises the 21 headers.** The registrar can do both as transcription; it will not do either unruled.

## 5 · Where the practice-steward audit and this packet agree and differ — unsmoothed

`.plans/2026-09-10-backlog-management-AUDIT.md` (`0fe685a`) was **not consulted while digging** and was read after.

| point | the audit | this packet |
|---|---|---|
| ③ remedy | two syntaxes, `→ PLAN ·` + `→ READY ·`, orphan check reads both (§5 `:373`, `:417`) | **same**, plus: the checker must compare *each* pointer to its header in both directions or the new syntax decays |
| ③ count | *"12 pointers; only 3 are clean"* (`:41`) | **5 consistent, 5 true-under-stale-prose, 2 false** — the difference is whether stale prose beside a true stamp counts as "unclean." It is a reader defect, not an instrument defect; the remedy differs (delete a sentence vs. flip a token), so the split matters |
| ④ | 13 self-declare no row · 6 declare a real row unread · 10 no `row:` (§2·B); *"make the link predicate bidirectional"* | **same population, classified by intent per file**; the concrete three-state field and the per-option consequences by name are this packet's addition |
| the generator | *"the register is duplicated, not derived"* (§2·C) | agreed; §0's last line is the same claim |
| sole writer | the evidence offered does not survive (§3·B) | not this packet's question; noted so Paul sees the disagreement exists |

⛔ Where these two differ, that is information for Paul, not a thing to reconcile here.
