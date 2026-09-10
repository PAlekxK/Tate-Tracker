# Open items — consolidated across every thread, 2026-09-10 close-out

- row: proposed (this file asks for one; it does not mint it)
- objective: O3
- class: engine
- stage: concept
- depends-on: `.plans/2026-09-10-PLAN-OF-RECORD.md` · `-G1-RULING-PACKET.md` · `-backlog-management-AUDIT.md`
  · `-link-syntax-and-proposal-intent-RECOMMENDATIONS.md` · `-canon-ingestion-PROPOSAL.md`
  · `-onboarding-lane-HANDOVER.md` · `-zones-automation-ASSESSMENT.md`

⭐ **WHY THIS EXISTS.** Six lanes ran for a day and each closed out into its own artifact. **This is the
single list, so the next lap reads one page instead of eighteen.** ⛔ Every row says whether it is
**MEASURED** or **RELAYED** — sixteen relayed claims failed verification today, six of them the
coordinator's, and no row here inherits that.

⭐ **THE NEXT LAP'S TARGET** `[paul-stated 2026-09-10]`: *"QA deploy with synthetics walking in and then
walking. It is a big test, and that's where I want to go before we start onboarding folks more and
sending them out links."* **Every row below is scored against that.**

---

## ⓪ THE ENVIRONMENT MAP — read this first, it caused real confusion today

`measured` from `worker/wrangler.toml` at close:

| deployment | estate id | what it is |
|---|---|---|
| **`fernwood`** (top-level) | `est-3c9f1a` | **Fernwood legacy — the app Mom actually opens.** ⚠️ stamped `ENV_NAME = production` |
| **`home`** | `est-e6696a` | where Mom's **account** was created 12:24 ET today. **Not where she reads** |
| **`paul`** | `est-d93508` | the Grant Park condo. Worker `myhome-paul` |
| **`bob`** | `est-9a74df` | invite minted, **UNSPENT** |
| **`qa`** | `est-qa0001` | synthetic test estate — 174 addressed accounts |
| **`lab`** | `est-lab0001` | 7 households founded through the product today |

⛔ **`nigel` / `aida` DESTROYED** — Workers, KV namespaces, verified at Cloudflare after the act.
Namespaces enumerated **literally empty** first; **zero grants existed, so no credential died.** Ids
`est-76012d` / `est-92e588` **RETIRED, NEVER REUSED.** Tombstone in `wrangler.toml`.

⛔⛔ **STOP SAYING "PRODUCTION" UNQUALIFIED.** It names the legacy deployment *and* the general idea of
live. Say `fernwood-legacy`, or the estate id. ⚠️ **Same class: "main" means `local main` (integration,
tracks `origin/staging`) and `origin/main` (Mom's frozen production, never pushed).** A lane measured
689/24 against the wrong one today and was right to flag the wording, not its own reading.

---

## ① PAUL'S — open rulings

| # | item | state |
|---|---|---|
| 1 | **B3's scope growth** — the Worker composing the digest inline at founding | ✅ **RULED YES**, with the field-by-field drift-lint as a binding condition |
| 2 | **`X-Estate` / the 400 collision** | ⛔ **OPEN.** Superseded in spirit by the multi-household ruling — **`X-Estate` must now be built**, so the "refuse a second estate" workaround is dead. Sequence is `ec`'s (M1 route → M2 edge → M3 array → M4 header + C2 retired **by name, same commit**) |
| 3 | **The interests label SCOPE** | ⛔ **BLOCKING A LANE.** He ruled *"keep `Gardening`"*; the coordinator's relay dropped **the other eight labels and the question sentence.** Three readings, three diffs. `onboarding-ask-b3` holds all nine, merge-clean, correctly refusing to guess on copy |
| 4 | **The product-steward trial** | ⛔ **OPEN, and the question was mis-framed.** It was **absorbed, not renewed** — `CYCLE-MAP.md` grants it beats 4+5 permanently and `grep -c trial` there is **0**. Options: **ratify the absorption** or **reverse it**. ⭐ **The deciding edit is `CYCLE-MAP.md`, not the charter** |
| 5 | **The security seat before invites** | ⚠️ Ratified 09-02 as a **blocking prerequisite on the auth build**; auth shipped. ✅ Paul: *"queue it right after we get to G1 fully tested."* **A `security-steward` seat now exists**; its red-team mode is blocked on a lab-parity instrument (row ⑤·3) |
| 6 | **`anchors.py` at Bob's address** | ⛔ **GATED. No go given.** Never-public address, output to `.private/`, first test outside the answer key |
| 7 | **The condo's return to `fernwood-legacy`** | ⛔ Open. Needs `adopt`. ⛔ **NOT the acceptance test for B3** — it is Paul's *second* estate, an irreversible cross-namespace copy, and it is `adopt` not `found`, so **it cannot exercise the thing the milestone exists to prove** |
| 8 | **Why Paul's home address sits in `est-qa0001`** | ⚠️ Open. Beside 174 synthetics. Its digest was deleted today because Guru answered *"clear skies over Mead Street"* from it |

✅ **RULED TODAY:** signup creates an account only, founding creates the estate and grant · nothing
pre-granted · **an owner token may found as many estates as they want** · `administrator` is
deployment-wide and is Paul, `owner` is per-estate · the place is written **once at founding**, never
elected · ingestion on the **confirmation clock** · `→ PLAN ·` with the bidirectional check · `row:`
normalised to **three states** (`none` · `proposed` · `<pointer>`) · keep `Gardening` · nigel/aida
destroyed.

---

## ② 🔴 LIVE DEFECTS — true right now, at a real household

| # | defect | evidence |
|---|---|---|
| 1 | **`fold-answer.py` recomposes only behind `--deploy`.** A confirmation retires its card, advances the watermark and refreshes the ribbon — **and canon never learns it.** Every surface reads *closed* while Guru answers from the old record | `measured`, `:131`. **Fernwood-today, not multi-tenancy** |
| 2 | **Retraction has no path.** *"She confirmed it and was wrong"* cannot be expressed. ⛔ **"Everything is changeable" is already on her surfaces**, and that doctrine's own caveat is *never call a thing changeable and then make changing it costly* — **it is not costly, it is impossible** | `measured` |
| 3 | **Sentence-case regex matches 1 of 5 `soon` labels.** *"You put Papers and documents first."* renders today. **Owed whichever way ①·3 rules** | `measured` all five. `TIER 2 · 25` |
| 4 | **No household can come up whole** — `bob · home · paul · qa` have **no `<estate>:place`**, so no digest, so **Guru is dark at every real household including Mom's** | `measured`, honest 404s through the repaired discriminator |
| 5 | **`onboarding/index.html:398`'s comment asserts a reversibility clause the rendered markup does not contain** | `measured` by the window that closed; preserved in `VERIFY-82` |

---

## ③ BUILT BUT UNEXERCISED — the gap the next lap closes

- ⭐ **`found` works end to end: 7 households founded at lab.** `measured`. **Zero at qa. Zero real.**
- **The empty shelf and founding screens are merged** — ⛔ **and every verification of them was headless
  Chromium with `/api/grant/whoami` MOCKED.** `onboarding-ask-b3`'s own words: *"ZERO evidence about
  integration… the first synthetic through these screens is their first real integration test."*
  ⚠️ **Its trap for QA:** the shelf's answer depends on the **Worker**, not the page — an estate-less
  account with no founding button means **a stale Worker before it means a broken page.**
- **`＋ Add a home` is LIVE at qa** and **no walk has ever tapped it.** ⛔ There is no person→estates
  enumeration behind it.
- ⭐ **Gate ① is 0 of 5 — and this is STRUCTURAL, not quality.** `handover` passed **all six clauses**
  today, the first time ever, and expired when the tree moved. Main took **107 commits**. Evidence is
  per-sha by design, so **no battery can outlive the session that runs it.** ⛔ **The next lap needs a
  still HEAD as a precondition, not a favour.** Remaining cost: ~4 min walking + four honest reads.

---

## ④ UNBUILT — G1 preconditions

1. **M1 + M2** — `route:` → `{personId}` alone, plus the `grant:<personId>:<estateId>` edge. **One
   change** (the route stops naming the estate; the edge starts naming them all). ⭐ **Conforming to a
   ruling already made** — the design specified `route: → {personId}` and nobody had noticed.
2. **The founding digest composer**, with the field-by-field drift-lint.
3. **`adopt`** — for `home`, `paul`, `bob`, which predate founding. **Two by migration, three by
   founding** — `bob` has no addressed account; nigel/aida now found their own.
4. **`household-import.py`** — unwritten. Export is fixed. ⛔ Nothing in Phase C runs until both exist.
5. **A J0 browser walk.** `walk-founding.py` reads **the record, not a browser**.

---

## ⑤ INSTRUMENTS — gaps, each measured

1. 🔴 **Nothing can see WITHIN-ESTATE, CROSS-PERSON.** `falsifier-tenancy.py` C1/C2/C3/C5 are **all**
   estate-A-vs-B; `check-household-isolation.py`'s docstring says *"the subject is always TWO ESTATE
   PREFIXES."* ⛔ **All three of today's 🔴s were that class.** Becomes structurally guaranteed **the
   moment a household has two people** — which invites create.
2. **`check-vocabulary.py` cannot see reader-facing prose** — correct scope, and **its selftest
   deliberately guards that prose does NOT fire.** ⭐ **A green run is not coverage for that class**, and
   a §4 collision reached a staged screen today.
3. **No lab-parity instrument.** `qa-divergence.py` measures **code** from git; a security test depends
   on KV bindings, secrets, credential classes, Access policy, rate limits, the grant table — **none of
   it code.** ⛔ **A diverging lab produces a FALSE GREEN, worse than no red team.** Blocks
   `security-steward`'s red-team mode.
4. **`product-steward`'s T1/T3 are majority-UNCHECKABLE by their own predicate** (T1 sees 20 of 29, T3
   sees 2 of 10) — **floors reported as counts.** And **a round that ran and failed leaves the same
   trace as one that never ran.**
5. **`check-release-docs.py` never reads `CLAUDE.md`** — which is why `:587` is stale on **3 of 3**
   claims (`groom` has had a beat since 09-08; twelve beats not eleven; wrong section pointer). ⭐ **Add
   that one file and the class closes.**
7. 🔴 **No reader names the `found` event** `[build lane, measured at 318416a, forwarded to TIER 1 · 19]`: the
   address step fires `ev("found", ok|already|refused:<code>|unreachable)` on `/api/onboarding-metrics` and the
   `onboard-address` feedback carries `founded:true/false`, but `watch-door.py` counts rows by an `event` field
   while onboarding posts `{sid, events:[{name, screen, detail}]}` — **the event lands and no reader prints its
   name.** By the ruled rule that is not instrumentation; **a reader is owed.** Same class as ①–⑤: a signal with
   no consumer reads as absent.
6. **`release-gate.py` coverage is 414×848 ONLY** — hardcoded, no flag. **A pass says nothing about
   laptop width.** Unpapered all day; keep it that way.

---

## ⑥ REGISTER & PROCESS

- ✅ **Ruled today, not yet applied:** `→ PLAN ·` + bidirectional check; `row:` three states. **2 false
  pointers to flip** (registrar's, transcription) · **5 stale-prose rows go to their owners** (deleting a
  sentence in someone else's row is authorship).
- ⭐ **The generator, per the audit: the register is DUPLICATED, NOT DERIVED.** Every status fact has an
  instrumented home and a prose home and nothing computes one from the other. **The remedy is this
  repo's own most-proven pattern — one source, N readers, plus a drift check.** Six domains have it; the
  backlog never got it.
- ⚠️ **`BACKLOG.md` is written by at least four writers plus six shadow lap-scoped registers (1,539
  lines), and no cycle map names any of the six.** ⛔ **"Two loops" is a stale count.**
- ✅ **One door — RULED** `[paul-ruled 2026-09-10 evening: "fold it in"]`: the registrar seat is absorbed into the
  standing backlog-refinement window, ONE writer of `BACKLOG.md` with two voices (verbatim scribe for forwarded
  rows · own voice for refinements with Paul). Registrar brief archived in place (`354424e`); the paragraph sits
  beside `BACKLOG.md`'s source-of-truth sentence (`d0cec6f`). Memory: `project_fernwood_backlog_one_door_ruling`.
- **The session-start block is 105 lines / 49 commands**, and its operating-model section is stale on
  3 of 3 claims.
- **10 plans carry *"the orphan flag is expected"*** — six on 09-07, four on 09-10. **A phrasing
  convention for arguing with a checker has formed and is spreading.**

---

## ⑦ PARKED, BY LANE

- **`tate-tracker-ec`** — M1+M2, the composer, the falsifier's cross-person gap, the USERNAME-empty seam
  (`/api/profile` writes ACCOUNT, `whoami` reads GRANT).
- **`onboarding-ask-b3`** — all nine labels held pending ①·3. **Window CLEAN.**
- **walk-harness** — the battery, pending a still HEAD. **J6 `wrong-person` deliberately UNDECIDED**: a
  journey may not assume the answer it exists to measure.
- **zones** — driveway-buffer test · NIR water test · ⛔ Bob's address (gated). **Not worth doing, already
  ruled out by two seats: the CHM without a PDAL install, any ML segmentation.**
- **`backlog-rat`** — the rationalization PROPOSAL, still **unread by Paul**, ⚠️ its own §7.2 stale.

---

## ⑦b ⚠️ LOOSE IN `~/.claude` — NOT this repo, and nobody claims it

`measured` at close by `paulkirschenbauer-3b`, **by name rather than from memory**: **19 uncommitted
files** in `~/.claude`, **up from 18** during the session. ⛔ **None belongs to the lane that found
them.**

**8 modified** — `gmail-draft-ledger.jsonl` · `handoff/finding-ledger/2026-09-08.jsonl` · **`MEMORY.md`**
· `rituals/meta-stack/cycle-state.json` · `tools/.verify-offsite-ledger.jsonl` ·
`tools/autonomous-loop/.seam-log.jsonl` · `tools/show-reminder.log` · `user-research/fernwood.md`
**11 untracked** — `daemon-auth-cooldown` · `daemon-auth-status.json` · five `handoff/brief-*.md` ·
`handoff/fernwood-nanny-checklist.md` · `handoff/finding-ledger/2026-09-10.jsonl` · three `memory/*.md`

🔴 **`MEMORY.md` HAS TWO WRITERS AND NOTHING SERIALISES IT.** Another window edited it **after** that
lane's commit. **No clobber this time** — the row survived and the other session appended cleanly — but
that is luck, not a mechanism. ⚠️ **This directory configures every session Paul runs**, which makes it
worse than the same state in a project repo.

⭐ **Why nobody claims them, and why they persist:** most look like **runtime state and session
artifacts rather than authored work**. ⛔ **The lane deliberately touched none of them** — *"reconciling
another session's working tree is how you lose someone's uncommitted thinking, and I could not tell
authored from generated without opening files that are not mine."* **That was the right call.**
✅ `refs/autosave/latest` holds a recoverable snapshot. **Paul's to triage, nobody else's.**

## ⑧ ⭐ THE LESSON THE NEXT LAP SHOULD READ FIRST

**Sixteen relayed claims failed verification today.** Six were the coordinator's. Three came from one
brief. Every single one was caught by the **receiving** lane measuring rather than accepting.

⭐ **And the sharpest statement of it is `onboarding-ask-b3`'s, offered for Paul directly:**

> *"Every catch came from the same cheap move: open the file, drive the screen. All four were settled in
> under two minutes by looking. What made them expensive was that they'd been **retold** several times
> first, each retelling more confident than the last. **That's a property of how many windows were
> relaying, not of anyone's care.** Worth him knowing when he decides how many lanes to run at once."*

⭐ **Two other forms worth carrying:** **grep, then read the line** — a count locates, it does not
establish. And **verify a reversibility promise against the actual route back before writing it.**

⭐⭐ **AND THE ONE THAT ONLY SHOWS UP AT THIS LANE COUNT — `paulkirschenbauer-3b`'s correction to its own
credit, which is better than the credit was:**

> *"You credit me with reading the plan before designing — true, and the right lesson. But two of my own
> citations were wrong today and both were caught by someone else first, and the repo moved ~270 lines
> under me while we talked, so every `worker.js` line I filed was stale within the hour. **The durable
> lesson is not 'read first' — it is CITE THE SYMBOL AND STAMP THE SHA, because in a repo with this lane
> count a line number has a half-life of about an hour.**"*

⛔ **Every `file:line` in this document and its siblings is subject to that.** `main` took **107 commits
today.** Cite the symbol; stamp the sha; re-derive before acting.

⚠️ **And the failure mode a security-shaped seat will keep generating, named by the seat itself:** it
drafted a finding that a privacy claim had *"propagated by copy during the session convened to catch
it."* **Tidy, alarming, and false** — the second match was a comment **defending** the promise. One
`sed` settled it. ⭐ **A story that good deserves a check before it deserves a reader.**

## Falsifier
If the next lap can state the board without reading this file, delete it. If two lanes give different
answers to *"what is open?"*, it has failed and needs to be shorter, not longer.

## QA
`python3 tools/publish-digest.py --check` · `python3 tools/release-gate.py` · `python3
tools/registrar-sweep.py` · `git -C ~/Developer/Tate-Tracker log --oneline --since=2026-09-10 | wc -l`
