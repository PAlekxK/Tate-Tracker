# frozen-fernwood-catchup · Working Mom's frozen Fernwood through her new household, module by module — executable when her production account exists

- row: BACKLOG.md § FOCUS FREEZE rule 6 (2026-09-07) — the catch-up is gated on her production account; rule 1 (the data control) is the ruling it executes
- objective: O3 → O1 (the engine's first household is Fernwood-as-instance; her journal resumes on the new product)
- class: instance · declared — Mom's, with engine requirements handed to the production window (never built here)
- seats: practice-steward → .plans/2026-09-07-frozen-fernwood-catchup-PROCESS.md
         engineering-partner → .engineering/2026-09-07-frozen-fernwood-carry-path.md
         user-researcher → .user-research/2026-09-07-what-carries-what-she-redoes.md
         content-steward → .content/2026-09-07-carried-record-copy.md
         ux-expert → waived: the surfaces belong to the production window; this plan places nothing on a screen. Debt, not judgement — re-seat when a `carry` or `re-collect` row names a surface
         ai-advisor → waived: the AI boundary is settled for this work — capture is deterministic, her words move verbatim or not at all, no model on any path in this plan
- depends-on: .plans/2026-09-06-freeze-register-PROCESS.md
- depends-on: .plans/2026-09-06-migration-readiness-STATE.md
- depends-on: .plans/2026-09-05-onboarding-PLAN.md
- ready: agent-proposed 2026-09-07 — **Paul rules** (§10). Nothing in §4's POST-GATE column may start before G0 and the 🔴 rulings.
- stage: concept
- stage-note: 2026-09-07 ~12:30 PM ET — written at `1b34376` after four seats reported; GATED on G0 (§1). Live KV of `est-3c9f1a` read once this morning (177 keys; archive one arrival behind); no value opened by the main session; nothing written to any household.

> **Ownership `[paul-stated 2026-09-07, relayed by the production window]`:** this window owns Mom's frozen
> instance — the GitHub Pages viewer, her held feedback, this catch-up. The production window owns the new
> product — release loop, QA/home origins, the Worker, onboarding, estate/homes/settings pages, tenancy.
> Everything this plan needs from production is in §11 as a **requirement**, never a design.

---

## 0 · The one-line, and the frame it sits in

**Her old Fernwood is not migrated. It is worked through.** Each module of the new product, as Paul unlocks it,
gets a tranche: her items for that module are sorted into a ledger, Paul rules each one, the deterministic
half executes, the asks become invitations he approves, and the tranche closes with the answer-key comparison
recorded. Her page stays a data control, untouched, until the sunset order in rule 3 runs.

**The five rulings that frame it** (all in `BACKLOG.md` § FOCUS FREEZE, in Paul's words):

| rule | what it fixes for this plan |
|---|---|
| **1** · data control (09-06) | her hand-built Fernwood stays as it is; production `home` is her blank slate; the catch-up is *"a manual process between you and me… clearly labeled and separated and available"* |
| **3** · guided visit (09-06) | the transition happens in person; the control is an ARTIFACT; the sunset order is written (drain her phone → re-archive + verify → rotate `SHARED_TOKEN` → tag → disable Pages, never edit `main` → stop the bots) |
| **4** · hold lifted fully (09-06) | her feedback may be read, dispositioned and acted on — **every action lands on the NEW instance, never the control**; nothing goes back to her without Paul |
| **5** · the map arrives empty (09-06) | zones do not migrate; her 23 zones and 16 names are the **answer key**; general shape: *what we know informs the design, it does not pre-fill her work* |
| **6** · gated on her account (09-07) | every act on the frozen side waits on a real account for Mom on production; this file is the plan of record |

**The sorting rule, made computable** (user-researcher, from rule 5): ⭐ **what carries is what she never gave
us.** A record with a provenance trail to her is answer key and grounding, not pre-fill. A record with no
trail to her (desk research, species profiles, frost dates, licensed photos) is infrastructure and carrying it
spends nothing. ⚠️ Its honest limit, measured: provenance was mostly never written down — `zones.json` carries
`namedBy` (18 hers, 6 Paul's at HEAD); plants, vehicles, notes and conversations carry nothing that names her.
So outside zones the rule is a **judgement per record**, which is exactly why the ledger has a `whose` axis and
Paul rules every row.

---

## 1 · The gate — G0

> **G0 · A household member record positively identified as Mom exists on production `home` / `est-e6696a`.**

Written on the **observable**, not the act: Paul's 09-07 words say *"her link"*, rule 3 says *"a guided visit"*
— two acts, one consequence, and only the consequence has a deterministic signal. G0 cannot be true before
either and is true immediately after.

**G0's precondition** `[R, production window 2026-09-07]`: Mom's link comes only after Paul walks production —
**release-cascade gate 2 precedes G0.** G0 is not reachable today.

⛔ **The candidate signal in rule 6 is the wrong one.** `reset-production-estate.py`'s `real` abort is
fail-**closed** for a delete and fail-**open** for a start gate — an unattributable record would open it — and
with `.private/synthetic-identities.json` absent every record reads `real` (practice-steward, `:87-110`,
measured). Engineering reached the same verdict independently: it is an alarm, not a gate. The predicate must
be its own read-only tool (§11 H1) and today it cannot be evaluated at all: `.private/` holds `fernwood-token`
and `fernwood-token-qa` and nothing for `home` (§11 H3).

---

## 2 · The ledger

**Unit of WORK: the module** (Paul: *"as we unlock different modules"*). `tools/momlib.py` MODULES: garden ·
motor-pool · equipment · house-systems · wildlife · place. **Unit of the LEDGER: the item.** A module
tranche is closed when every item mapped to it has a disposition and a passed check.

**The row set — five sources, classification TOTAL, never filtered** (practice-steward measured **314 rows**
`[R]`): (1) every KV key in the newest archive, by family; (2) every channel arrival in the disposition
ledgers, incl. the 63 baselined; (3) her `namedBy` zone names, derived from `zones.json` history — no model,
no guessing; (4) the 19 `tateTracker.*` browser-local keys in `STORAGE_KEYS` at HEAD; (5) canon records with
any trace of her. A row that maps to no module maps to `unmapped` and is still counted.

**The disposition enum** — proposed, Paul's to adopt (§10 #5):

| word | means | ruler |
|---|---|---|
| `informs-build` ⭐ new | changes what the module IS — design input, copy fix, backlog row on the new product. Lands in the product, never in her data. Rule 5's general shape, given a slot | Paul |
| `re-collect` | only she can supply it; the module asks afresh. Her old answer is grounding for HOW we ask, never the pre-filled answer | Paul |
| `answer-key` (was *stays in the control*) | stays on the frozen control and is **actively used to measure** the from-scratch build at tranche close | Paul |
| `carry` | moves verbatim into the new instance. **An exception under rule 5** — every `carry` row must say why it is not a pre-fill of her work | Paul |
| `drain` | browser-local only; flushed from her phone during the visit, online, before lockout | Paul (his visit) |
| `drop` | ruled not to travel — requires ruler, date, his words | Paul |
| `undecided` | day one; the only value that counts down | the generator |

Plus an orthogonal **`whose`** axis ∈ `hers · paul · instrument · mixed · unknown` — attribution from authored
content only (memory `project_fernwood_device_misattribution`). `metrics`/`cost-log`/`env-canary` are
`instrument` by key family; zones by the `namedBy` predicate; **`conversation:*` is `unknown` until a human
reads it and is never swept into `instrument` to tidy a count.**

**Columns:** id · module · source · family · whose · provenance (key/ledger id/`namedBy`/archive `takenAt`)
· disposition · ruled-by · ruled-at · his-words · exit (`release-loop` for `informs-build`, `mom-cycle ask`
for `re-collect`, the visit for `drain`) · check · checkState (`passed` / `declined` / a named failure).

**Where it lives:** `.private/catchup-ledger/` — gitignored, mode 600, beside the frozen archive. Row content
includes her words' ids and provenance, never their bodies; but the roster of what she said, when, is still
hers, and Tate-Tracker is public. A counted summary (`N undecided of 314`) is the only thing that leaves it.

**What generates it:** `tools/catchup-ledger.py` — deterministic, read-only, **content-free by construction**
(reads key names, ledger metadata, `namedBy`, the roster; never a value body), with a selftest and two
mutation controls: a row with no provenance must be refused, and a synthetic key family must classify as
`instrument`, both **seen to fail** before the tool is trusted. `--record` captures Paul's ruling verbatim
with his name and the date. `--status` prints the burn-down line for the mom-cycle board.

---

## 3 · Dispositions already on the record — the seats' proposals per family

Every row below is a **hypothesis until Paul rules it in the ledger** (T3). Grades are the seats'.

| family (count) | proposal | why | grade |
|---|---|---|---|
| **her feedback** (10 buckets + 1 live) | **`informs-build`** — worked, never carried | rule 4: the *action* lands on the new instance; her old notes written into `est-e6696a:feedback:<old date>` would misdate them and put remarks about a different app into the new one's history | measured (eng) |
| — of which `q-top-categories` (08-03, *"That's all of them"*) | ⭐ already carried, invisibly and correctly: **the module manifest is her confirmed answer**. Her onboarding *ranking* is a new question over her own list, not a re-ask | validated (UR) |
| — of which `q-almanac-name` (07-29, *"Yes, Journal"*) | **carry her word** — ⛔ currently contradicted: `viewer.html:7228-7229` hardcodes `<household> + " Almanac"`, commented *(mom seat, round 3)*. Verified by the main session. **Routed to the production window** — already inside its "naming the record" ruling held for Paul's talk-through (`.user-research/2026-09-06-naming-the-almanac.md:227`) | validated |
| — of which her two rainfall notes | `informs-build` only — the visible actioning is *the rainfall card being right on day one*, never a note reappearing | validated (UR) |
| **Guru conversations** (35: 32 real + 3 probes) | `answer-key` + grounding — a lookup history, ~3 of 35 produced canon; never carry a transcript | inferred (UR); measured count (eng) |
| — the refused motor-pool log | `informs-build` — it is the reason motor-pool and equipment are modules; costs nothing as a design fact | validated (UR) |
| **zone recordings** (3 + 6 blobs) | `answer-key`; the ONLY family with a credible `carry` claim (her voice, cannot be re-created) — playback during the visit is a *use*, not a carry. ⭐ Listen to the three per record before the gate: a batch is not cleared by one member | assumption on content (UR); +2 h if a carry is ruled (eng) |
| **observations** (2) | ⚠️ the one arguable `carry` — a dated bear sighting cannot be re-seen. **Paul's question, §10 #6** | inferred (UR); eng says NO, already folded into canon `[R]` — the seats disagree and the disagreement is reported, not resolved |
| **zones + her 16 names** (2 keys + canon) | **`re-collect` + `answer-key` — RULED** (rule 5). The joint session IS the measurement; showing her the 16 first destroys it irreversibly | validated |
| **canon built with her** (`plants.json` 36 · `vehicles.json` · 64 wildlife) | **`carry` the records** — her fingerprints are ~4 confirmations, 2 promotions, 1 addition; the rest is desk research and Paul's authoring. Turns on §10 #3 (narrow vs broad reading of rule 5) | inferred (UR) |
| **metrics + cost-log** (113 of 175) | **`drop`** — counters about an instrument; and ⭐ the new household's usage numbers are evidence about the product's cold start, which seeding would destroy | measured (eng) |
| **browser-local** (19 rostered) | ⛔ storage is per origin, **nothing crosses** — a loss list, not a decision: **2 `drain`** (`feedbackOutbox.v1`, `door.outbox.v1`, held until a 2xx — exist nowhere but her phone) · **16 abandon** (nothing on the new origin reads `tateTracker.*`) · 1 open (`observations.v1` field notes may be device-only) | validated (UR, eng) |
| — her A+ text size | must be **served by config on day one**: `text_size_served = lg` in 8 of 8 reports, 0 of 37 toggle firings. Verify by USE on a real device at 414 × 848 — §11 | validated telemetry (UR) |
| `env-canary` · `cache:ambient:*` · `zones-last-seen` (4) | `drop` — binding proof, TTL cache, sync bookkeeping | measured |

---

## 4 · Sequence

### 4.1 · The line — in one sentence
**Post-gate is anything that (i) reaches Mom, (ii) writes into `home`/`est-e6696a`, or (iii) touches the
frozen live store.** Everything else is preparation and may run now.

### 4.2 · PRE-GATE — preparation, may run today

| # | act | owner | note |
|---|---|---|---|
| P1 | ✅ the register line (rule 6) — done at `1b34376` | this window | a ruling not in the register is not in force |
| P2 | this plan and the four seat files | this window | done |
| P3 | **build `tools/catchup-ledger.py`** + selftest + the two mutation controls, seen to fail | this window | read-only, local, content-free |
| P4 | ⭐ **the DRY RUN** against the archive on disk — every row lands `undecided`; the denominator (314) is known before the gate | this window | the load-bearing prep act: a burn-down whose N is measured on day one |
| P5 | derive the module enum, the `namedBy` predicate, the storage roster | this window | all local, all measured already |
| P6 | **draft** the `re-collect` invitations and the Z-ACK acknowledgment (§5) — never send | content-steward, Paul approves | rule 4 |
| P7 | the S5 completeness cross-check (~2 h) if ruled — §10 #9 | this window | the control's whole value is completeness |
| P8 | ~~`deploy-worker.sh` bash-3.2 fix~~ ✅ already in the shared tree at `51ed0b8` (eng, measured) | — | rule 3's note is stale in the safe direction |
| P9 | the production window builds the G0 predicate, the existence probe, `fernwood-token-home` (§11) | production window | without these G0 reads UNCHECKABLE forever |

⛔ **Not pre-gate, pending §10 #2:** any further **read** of the frozen namespace. The 09-07 ruling says every
act waits; the measurement that produced it was a live read. Until Paul says which he meant, this window makes
no network call to `est-3c9f1a`.

### 4.3 · POST-GATE — one tranche per module, inside the existing mom-cycle (no new loop)

Ruled by practice-steward as a **FINITE burn-down** run as module tranches inside the mom-cycle's legs: the
set is closed (314 rows), it has no trigger of its own (modules unlock on the production window's schedule),
and a host loop with all six spine elements already owns this content. Memory
`feedback_cyclical_vs_finite_projects` — do not wrap finite work in loop machinery.

| beat | what happens | owner | closes when |
|---|---|---|---|
| **T0 · SWEEP** | read the register; assert G0 PASSED; assert the module is unlocked on the new product; dispose fired item-gates | ai | G0 exits PASSED; the register names the module |
| **T1 · RE-TAKE** | `archive-frozen-estate.py --verify` → 0 GONE → re-archive | ai | `unreadable: []`, `keyCount` ≥ prior |
| **T2 · GENERATE** | `catchup-ledger.py` → this module's rows + the whole-set `undecided` denominator | ai | zero `unclassified` |
| **T3 · 👤 RULE** | **Paul rules every row in the module**, one batched pass; `--record` keeps his words | **Paul** | zero `undecided` in this module |
| **T4 · EXECUTE** | the deterministic half: `carry` writes (via the probe, GET-verified), `informs-build` rows filed to the release loop, `drain` scheduled into the visit | ai | every executed row names its check |
| **T5 · 👤 THE ASK** | `re-collect` rows become invitations; Paul approves the exact words | **Paul** | rule 4: nothing reaches her without him |
| **T6 · 👤 PROVE + CASCADE** | every check run **live at her conditions (414 × A+)**; synthetic → Paul → **Mom is gate 3** | ai → Paul → Mom | every `checkState` is `passed`, `declined`, or a named failure |
| **T7 · CLOSE** | counts to `MOM-CYCLE-LOG.md`; the register's module row; **the answer-key comparison recorded**; pre-registrations discharged | ai | chronicle and state artifact agree the tranche closed |

⭐ **Why T1 sits at beat 1, not beat 6:** a disposition ruled against a stale roster is already wrong by the
time it executes, and there is no eraser after Mom onboards. The archive is made current **by adjacency, not
by cadence** — a cron there is a permanently amber control.

**Two exits, named:** `informs-build` rows leave into the **release loop** (the production window's);
`re-collect` rows leave into the **mom-cycle's own ask machinery**. A row that cannot name its exit is not
dispositioned.

### 4.4 · The tail — rule 3's sunset order, after the last tranche Paul wants before lockout
drain her phone (one online tap, during the visit) → re-archive + `--verify` (0 gone, 0 added) → rotate
`SHARED_TOKEN` (the actual lockout) → tag the sha → disable Pages, **never edit `main`** → stop the bots
(§10 #8 must be ruled first: an archive taken while a cron still writes is not final).

---

## 5 · The words — drafted, not shipped (content-steward; Paul approves every line)

Rule 5 inverts the copy brief: the carried-over notice becomes the exception and the **re-collection
invitation and the acknowledgment become dominant.** Rule 3 moves most of it off the screen and into the room
— each pattern is marked **spoken by Paul** or **on-surface**.

| pattern | one line | register |
|---|---|---|
| **A** carried-over notice (exception) | *Your name for it, August 30.* — a label; changeability carried by a `Change ›` control, never a repeated sentence | orienting · surface |
| **B** invitation + acknowledgment | *"You named these places for me back in August — I wrote every one down and I've still got them. We're starting this one empty because I'd rather build it with you than hand you mine."* Four beats: credited · kept · why empty · invitation. The word *again* is barred | inviting · spoken |
| **B3** Z-ACK, not a rendering of her map | Z1 spoken (necessary, not sufficient) · Z2 one durable surface line · **Z3 a "What you've told me" look-back off the map** — literally what she asked for on 2026-07-26 (*"Is there a way to look back at these, eg in the 'journal'?"*), the reader signal the deferred surface was waiting on | inviting · both |
| **C** "is this right?" | *"Let me read that back to you — is that how you'd say it?"* — the error stays on Paul's side; ⛔ no name is spoken off the unverified vision-read list | confirming · spoken |
| **D** stayed behind / the old page | three windows: still-loads · the **drain line** for the visit (*"there are a couple of things still sitting on your phone that never made it to me"*) · post-sunset (*"That one's put away now. Everything you told me there, I still have."*) — keeping may be promised, reading may not | orienting · spoken |

Forbidden here: task-manager vocabulary · *migrated / imported / data / sync* · any count of unanswered items ·
anything implying she owes work · thanks (credit, don't thank). The decisive register fact from her material:
**she will ask, she will not answer** — the strongest argument for the 09-06 maps ruling B and for rule 5 as
good copy, not just good method.

---

## 6 · What the freeze register changes at gate-lift, in order

| # | row | today | at gate-lift |
|---|---|---|---|
| R1 | Track A · C (channel) | ✅ LIFTED (rule 4) | unchanged — written so nobody re-derives a hold that is gone |
| R2 | Catch-up · W (work) | ⛔ UNDECLARED | → ACTIVE, release condition = G0 |
| R3 | Production · W | 🟢 ACTIVE | gains the tranche as declared work; names the ledger as its state |
| R4 | Track A · P (push) | 🧊 FROZEN | ⛔ **UNCHANGED — FROZEN**, as an explicit row: an unstated row reads as permission, and this is the single most likely wrong act |
| R5 | Bots · destination (S9) | ⛔ UNDECLARED | ruled **before** the final re-take (§10 #8) |
| R6 | The control · currency | 175 keys, 09-06 00:08 | → a dated stamp after the post-gate re-take — last, adjacent to the act |

---

## 7 · Corrections the main session verified against the seats' claims

| claim | verified reading |
|---|---|
| *"her frozen site republishes every six hours"* (register, rule 1) | **Her app is frozen in payload.** `viewer.html` on `origin/main` last moved `79c4bae` 2026-09-03 22:04 ET, Paul's commit; every bot commit since touches only `weather-history.json`, `weather-bias.json`, `worker/digest.json`. The cron republishes weather into an unchanged app. Rule 1's warning stands for the *weather history*, not the app |
| *"one `git push` is a production deploy to Mom's phone"* (eng) | **Narrower.** Local `main` tracks `origin/staging` with `push.default=upstream` — a bare push lands on QA. Her page needs a **typed refspec from Paul's own terminal**; the auto-mode classifier blocks an agent's. The pre-push hook checks fixtures on `main`/`prod` refs but does not refuse. Local `main` is 297 commits ahead of `origin/main`. The guard in §10 #7 is still worth ruling; the exposure is one typed push by Paul |
| `check-storage-keys.py` RED, 5 `fw-*` failures (eng) | **GREEN when run by the main session at `1b34376`** — "every browser-storage literal is rostered." Both readings recorded; re-run at T0 |
| S7 — 11 `account:` + 13 `grant:` keys on her estate (09-06 audit) | **on the LAB namespace** (`1e0bd883…`), not hers; her archive holds zero of either `[R, eng, from the dump's namespace id]`. S7 → hygiene delete on lab. Falsifier: any `grant:`/`account:` key on `100f2b95…` puts S7 back on the critical path |
| `deploy-worker.sh` bash-3.2 fix "still owed" (rule 3 note) | **discharged at `51ed0b8`** on main, line 108 `[R, eng]` |
| 18 browser-local keys (brief) | **19** in `STORAGE_KEYS` at HEAD, 6 phone-only (practice-steward) |
| her 16 zone names (register) | `zones.json` history carries **18** `namedBy: mom` vs 6 Paul at HEAD; the register says 16 of 23. Derivable by predicate, no model — reconcile the count at T2, do not restate either number until then |

---

## 8 · Files touched (when the pre-gate builds run — none yet)

- `tools/catchup-ledger.py` + `tools/tests/test_catchup_ledger.py` (selftest + two mutation controls) — NEW
- `.private/catchup-ledger/` — NEW, gitignored (add the pattern to `.gitignore`)
- `MOM-CYCLE-LOG.md` — one dated line per tranche at T7; `MOM-CYCLE-MAP.md` — the tranche as a named leg variant, parsing per S6
- `BACKLOG.md` § FOCUS FREEZE — rows R2–R6 at gate-lift (this window, by path)
- `.git/hooks/pre-push` — only if §10 #7 is ruled yes (15 min, local, reversible)
- `tools/carry-item.py` — **only if** §10 #4/#6 rule a `carry` that a human cannot type (zone audio, observations): archive-reading, per-item, provenance envelope, GET-verified, refuses on a missing label; 3–5 h + 2 h for blobs
- ⛔ never: `worker/`, `engine/`, `onboarding/`, `cycle/release/`, `.private/synthetic-walks/`, any canon, `viewer.html` on `main`

---

## 9 · Falsifier — the checks that must be SEEN to fail

| check | sited at | proven how |
|---|---|---|
| `catchup-ledger.py` refuses a row with no provenance | the ledger's whole claim | mutation: strip `namedBy` from one zone in a fixture → refused |
| a synthetic key family classifies `instrument`, never `hers` | the `whose` axis | mutation: rename a `metrics:` key → `unknown`, never `hers` |
| G0 reads NOT-PASSED for a synthetic identity on `est-e6696a` | the gate | paired negative control (§11 H1) |
| `archive --verify` reports GONE > 0 | T1 | its positive control already fired once (174/175 on 09-06 00:03) |
| a `carry` is proven by GET on the target, never a listing | T4 | the existence probe (§11 H2) — a listing cannot prove absence |
| the frozen `viewer.html` sha on `origin/main` moves | Track A · P | `check-live.py` — the one row that must stay green until the sunset |
| pre- and post-migration telemetry pooled | measurement | the new origin starts a new browser bucket; the 2026-07-30 rule already forbids pooling |

**Failure modes this repo has already paid for, and the guard each:** checkbox-not-world drift → every row's
`checkState` is a run, not a tick · *routed = invisible* → `undecided` is the only value that counts down and
the summary counts by predicate · rulings living only in a transcript → `--record` with his words, and the
register line first · the safe-looking direction of error → the ledger over-reports `undecided` by design and
never auto-closes a row · a cron writing to a "frozen" surface → R5 ruled before R6.

## 10 · ⛔ PAUL MUST RULE — tiered so the list does not bog you down

### 🔴 Block the plan — four
1. **G0's predicate polarity.** Does `unknown` fail the gate? **Recommend yes** — a start gate needs positive evidence; the reset tool is deliberately the opposite polarity. One sentence settles what the production window builds.
2. **Is read-only MEASUREMENT of the frozen namespace inside or outside the gate?** Your ruling says every act waits; the measurement that produced it was a live read. Fail-closed meanwhile.
3. ⭐ **THE FORK — does "don't prepopulate" cover the MAP only, or the whole record?** Read narrowly, canon (plants, vehicles, wildlife) carries and §3 stands. Read broadly, it all arrives empty. **Recommend NARROW** — rule 5's own justification is the answer key, and the answer key is the map; applying it to desk research re-derives months and measures nothing.
4. **Is the answer-key comparison a measurement you intend to take, and what form does Z-ACK take?** If yes: nothing she authored is shown before she re-produces it, and the comparison is recorded the day of the joint session. Z-ACK options: (a) building it together IS the acknowledgment · (b) show her the frozen map — spends the measurement · **(c) after the joint session, show the old map beside the new** — discharges the debt AND preserves the measurement. **Recommend (c)**, plus content's Z3 look-back. ⛔ Irreversible the first time anything is shown or pre-filled.

### 🟡 Before the visit — six
5. **The disposition enum** — adopt `informs-build`, rename to `answer-key`, narrow `carry` to an exception (§2). Vocabulary is yours.
6. **Observations** (2 keys): part of *her work*, or the *place's history*? The seats disagree; if the latter, they carry.
7. **A site-freeze mechanism** — a local `pre-push` hook refusing `main` unless overridden (15 min, reversible). Exposure verified narrower than reported: one typed refspec from your terminal. **Recommend yes**; it costs nothing.
8. **The weather cron** — disable both workflows from the Actions UI (no commit, reversible) or let it run (now defensible: payload measured weather-only into an unchanged app). Your weather history. Must be ruled **before** the final re-take.
9. **Spend ~2 h on the S5 completeness cross-check before the visit?** "175 keys, 0 unreadable" is what a listing returned, and this repo has measured `kv key list` unable to prove presence or absence. **Recommend yes.**
10. **Confirm metrics + cost-log DROPPED** (113 of 175) — never carried; the cold-start measurement is the decisive reason.

### 🟢 The words, and one small build — three
11. **Person: `I` or `we`.** Drafted in `I` — the strongest case for it in the product; her idiom for the project is *we*.
12. **Is she told her August names are a benchmark? Recommend no** — kept, never scored; her stated reason for not answering is fear of being wrong. And: does the frozen page get a line on it before lockout, or only an answer when she asks?
13. **A relayed-capture path with an arrival record before the gate** — deterministic, AI-free, provenance-bearing, small. Without it the catch-up repeats Z-ACK's own defect: her largest contribution has no id, timestamp or channel. **Recommend yes.**

*(Not on this list, deliberately: which module goes first; any single item's disposition. Both are yours by definition and land at T3.)*

---

## 11 · Handoffs to the production window — requirements only

| # | requirement | why it blocks |
|---|---|---|
| H1 | **The G0 predicate**: read-only, exit-coded, scoped to `est-e6696a` **by derivation** from `wrangler.toml`, positive identity required, `unknown` and `synthetic` both fail, paired negative control proven by mutation, `UNCHECKABLE` when unreachable. **Not `reset-production-estate.py`** | no gate, only a claim |
| H2 | **A read-only per-record existence probe** on `est-e6696a` — "does record R exist?" | every `carry`/`drain` check is unprovable without it |
| H3 | **`fernwood-token-home` in `.private/`** — `read-onboarding.py`'s TOKENS map names it; the file does not exist | H1 and H2 read UNCHECKABLE forever |
| H4 | the invite / visit act leaves a **dated register line labelled an attestation** | an outbound act is not observable from this repo |
| H5 | state **cascade gate 2 as G0's precondition** in the register | otherwise G0 reads reachable today |
| H6 | confirm the landing surface for a ruled `carry` on `home`, and that nothing there is pre-filled ahead of her | a carry with no destination is `undecided` wearing a ruling |
| H7 | target coordinates **derived, not typed**: namespace `79464451…` / `est-e6696a` / `LEGACY_BEFORE 1970-01-01`; home reads only `est-e6696a:`-prefixed keys — an unprefixed write is a silent orphan; `LEGACY_BEFORE` must stay 1970 `[R, eng]` | the one way a carry can land and vanish |
| H8 | **`JOURNAL_NAME`**: her validated 07-29 answer is *Journal*; `viewer.html:7228-7229` ships *Almanac* on a synthetic seat's comment — already inside your "naming the record" ruling; this plan cross-references, does not reopen | her word vs a fixture's |
| H9 | **A+ served by config on day one** — verify `text_size_served = lg` by USE at 414 × 848 on a real device, not by reading the config | 0 of 37 toggle firings; she will not fix it herself |
| H10 | content placement conditions for patterns A–D (in `.content/2026-09-07-carried-record-copy.md` § handoffs) | the words are approved before the surface exists |

Recorded by the production window as a pre-registered lap-2 item at its close-out `[R, 2026-09-07]` so H1 has a
trigger, not a memory.

---

## 12 · QA

- Every `checkState` at T6 is a **live run at her conditions (414 × A+)** on `home`, never a local read.
- The cascade holds: synthetic seats → Paul → Mom, per tranche. Mom is gate 3, never gate 1.
- The tranche does not close on a tool's success line: T7 writes the counts to the chronicle **and** the register's module row, and S4's predicate (chronicle and state artifact agree) is the closing condition.
- Pre-registered retro questions for the first tranche (practice-steward §3.4): did any row change disposition after execution? · did `undecided` ever go UP mid-tranche (a source the generator missed)? · did the answer-key comparison get recorded on the day, or reconstructed later?

## 13 · What this plan does not do
It does not migrate her records. It does not design the gate, the invite, or any surface. It does not run the
sunset. It does not rank modules or items. It does not touch the frozen live store again until §10 #2 is ruled.
It does not claim the archive is complete — only that it was 175/175 by listing on 09-06 and one arrival
behind by listing on 09-07.
