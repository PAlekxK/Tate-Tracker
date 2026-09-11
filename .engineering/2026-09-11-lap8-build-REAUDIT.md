# RE-AUDIT of `.plans/2026-09-11-lap8-build-PLAN.md` — the door rows, behind row T

- **Filed:** 2026-09-11 11:15 EDT (from `date`, never authored)
- **Seat:** engineering-partner. **Mode:** path-evaluation (second pass over my own return).
- **Serves:** the lap-8 build window's brief. ⛔ **This file changes no code, writes no `BACKLOG.md` row, and is not a ruling.** It re-measures, re-sequences, and says where I now think the plan is wrong.
- **Read at sha:** `e354ed04` (start) → **`0a6c3684`** (end). ⚠️ **HEAD MOVED UNDER ME MID-READ**, one commit: *"row T is 24 STEPS, not 21."* I diffed it — it touches `.plans/2026-09-11-testing-revamp-PLAN.md` and `.engineering/2026-09-11-testing-revamp-SIZING.md` **only**. **No `worker/`, no `tools/`, no served page moved**, so every measurement below holds at both shas. Reported rather than silently absorbed, per the concurrent-session guard.
- **Tree at close:** clean but for one untracked file (`handoff/handoff-lap8-rowT-build.readback.md`) — not mine.

**What I read, each one opened:** the build plan whole (1,140 lines) · `.ux-reviews/2026-09-11-lap8-door-surfaces.md` whole, §0 first · `.plans/2026-09-11-testing-revamp-PLAN.md` §1 §3 §4 §9 §10 §11 §12 §13 § Sequence § Falsifier § QA · `.engineering/2026-09-11-testing-revamp-SIZING.md` §T10–T16, §C1–C3, §D · `cycle/release/CYCLE-LOG.md` § Lap 8 (`:4005–4378`) whole · `worker/worker.js` (the regions cited below) · `worker/wrangler.toml` · `homes/index.html` · `onboarding/index.html` (the cited lines) · `settings/account/index.html` · `engine/viewer.template.html` (the four cited regions) · `instance/*.json` (`absent` arrays) · `tools/journey-walk.py`, `tools/journey-view.py`, `tools/release-gate.py`, `tools/falsifier-tenancy.py`, `tools/walk-founding.py` (symbol tables).

**Run read-only:** `git rev-parse`, `git log`, `git diff --stat`, `git status`, greps and `sed` over the tree, one Python pass over `worker.js` to build the key-kind histogram. **No network probe, no KV read, no deploy, no browser.**

---

# 0 · THE HEADLINE — three things changed since `06c2a16`, and only one of them is a ruling

1. ⭐ **§2 A1 — the plan's ONE 🔴 BLOCKING finding — IS DISCHARGED. B1, B2 and B3 all landed in lap 7.** The plan's entire A1 argument, its slip-table row, its **A0a/A0b fallback steps** and **Q6** are stale. `measured` below. This is the single largest change to the plan and it makes the lap *smaller*, not larger.
2. ⛔ **The conversion surface GREW BY FIVE SITES AND ONE WHOLE KEY KIND IN ONE LAP** — 55 → **60** non-comment `scopeOf(env)` sites, and a `recovery` kind that did not exist when the histogram was built. That is the strongest possible argument for A0 (`check-scope-sites.py`) and it also **falsifies A0's own delete-clause as written** (§6·2).
3. ⭐ **ux-expert's F1 is real, and A9 in two literals does NOT fix it.** I traced the render path: `homes/index.html:374` is `renderHomes(empty ? [] : [merged])` — it builds **exactly one row from single-place fields and never reads `d.estates` for rendering at all.** Put `estates` on the grant-resolved `whoami` and a two-home person still sees one row; the array becomes *correct and unread*. **A9 is three changes, not two.** §3·F1.

---

# 1 · THE RE-SEQUENCED ROW ORDER — T first, every door row behind it

**The order I now recommend, and it is not the order §3 of the plan declares:**

> **T (whole, 24 steps) → P → A0 → A1 → A2–A4 → A5+A6 → A7 → A8 → A9 → A10 → A11 → A12 → A13 → H1 → H2 → H3 → C → E → F → G → R1 → R2 → R0 → A14 → A15 → [Paul's word] → B**

**Four changes from the draft's `P → A → C → E → F → G → riders → H … A15 … B`:**

| change | why |
|---|---|
| ⭐ **H1–H3 move UP, to sit immediately after A13 and BEFORE C/E/F/G** | The draft puts H last. But **C5 is a stop inside `journey_lifecycle`**, and **H2's J9 is a battery journey** — both are harness work that the C/E/F/G rows' own checks depend on. More sharply: **H1 is the only thing that can read row A's done-means** (§2 A6, which I re-confirm). Building A, then C/E/F/G, then discovering H1's second context collides with T14's factory, is the one sequencing mistake that costs a re-walk of the whole battery. **Build the instrument the moment the thing it measures exists.** |
| **A0a/A0b are DELETED** | B2/B3 landed (§3). There is nothing to absorb. |
| **A13 loses its "regardless" half** | `probeRateLimitOk` shipped (§3). A13 is now **only** what security-steward rules. |
| **R0 (the ask ledger) STAYS, re-pointed** | ⛔ **I first wrote that it should move out, on a premise I had not measured. §6·5 carries the strike.** Its spec is complete at `.plans/2026-09-11-ask-design-PLAN.md` **§9** — ⚠️ **not §4, which is where the draft's R0 step points.** R0 sits after R1 (its precondition). |

## 1a · The three seams with row H, by symbol — SIZING §C1's rebase points, re-measured

### ⭐⭐ SEAM H1 ← T14 — and T14 AS WORDED CANNOT BE REUSED BY H1. This is the one I would fix in row T.

`measured` at `0a6c3684`, `tools/journey-view.py:63–67`:

```
const ctx = await b.newContext({
  viewport: { width: 414, height: 848 },
  deviceScaleFactor: 3, isMobile: true, hasTouch: true,
});
```

It is an **inline single call**, and everything downstream is bound to it: `ctx.setDefaultTimeout` (`:68`), `cfg.cookie` (`:69`), `const page` (`:70`), the `out` accumulator (`:72`), and **three event handlers** — `console`, `pageerror`, `response` (`:77–89`) — all registered against that one `page`.

**SIZING T14 says the fix is that *"the cfg surface grows by three keys"* and *"every one of these lands in the existing `newContext` call."*** ⛔ **A grown argument object is not a factory.** H1 needs a *second* context inside one run, which means a second `page`, its own three handlers, and a `context` label on every `out.steps` entry so a reader can tell which browser did what. If T14 ships as literally worded, **H1's only options are to duplicate the block (the parallel `newContext` the ruling forbids by name) or to refactor T14's output in row H** — i.e. to re-open a step from a pre-authorized, already-landed commitment.

⭐ **Recommendation, and it is a one-hour amendment INSIDE T14, not a new step:** T14 extracts

```
async function mkContext(browser, cfg, label)  →  { ctx, page, label }
```

with the timeout, the cookie, and all three handlers registered **inside it**, and `out.steps` entries carrying `label` from day one (single-context runs write `"a"` and nothing reads it until H1). **Why this is the right shape and not gold-plating:** the `class: engine · must-not-diverge` line on row T means *one definition of the conditions a walk ran in*. A function is that definition; an argument object is a call site that has to be copied. And the cost of getting it wrong is not a refactor — it is **two definitions of "the conditions this walk ran in" inside the lap whose whole deliverable is the judge.**

⚠️ **Hand this to the row-T build window, not to row H.** It is an amendment to a pre-authorized commitment's *shape*, not its scope, and it is cheaper before T14 lands than after.

### SEAM H2 ← T10 + T3

- **T10 adds four required keys** to every `JOURNEYS` entry (`routes` · `pages` · `expectsAppEvents` · `arrivalState`) **with a selftest clause enforcing them**. **J9 must declare all four or `--selftest` fails — which is the design working.** `measured`: `JOURNEYS` is at `journey-walk.py:890` (SIZING cites `:876`; the draft plan cites `:781`), `JOURNEY_IDS` at `:322` (both cite `:308`), `NAMED_UNBUILT` at `:968` (SIZING cites `:954`). **journey-walk.py has drifted +14 lines since SIZING was written. Re-cite at build.**
- **T3's declared cell list:** J9 must be in `cycle/release/cells/lap-8.json` or the gate prints it **UNWALKED**. The row-T plan's §4 proposal already carries J9 as **cell 7**, *"as H declares — carrying T10's four keys."* ✅ The seam is already declared from T's side; **H2's obligation is to fill it, and the gate's UNWALKED print is what makes failing to do so visible.**
- ⭐ **AND ONE J9 STOP CHANGES MEANING BECAUSE B2 LANDED.** The draft's **X06** — *"context 1's original token 404s"* — was written as the only honest assertion of an unbuilt B2. `measured`: B2 shipped (`worker.js:1022`, revoking at `priorScope` and deleting the route row with it). **So X06 is now a REGRESSION stop over shipped behaviour, not a new assertion.** That is strictly better — it should pass on the first run, and a red there is a real finding rather than an expected gap. **Say so in H2's step, or a window will read a green X06 as the harness not reaching it.**
- ⛔ **The id-collision check still stands and I re-confirm it:** J7 is spoken for in prose as *second-member*, J8 is lap 7's lifecycle. J9 is free.

### SEAM H3 ← T18 + A11

T18 (`check-href-controls.py`) covers `href="#"` controls **statically, from tracked engine source**, and its own stated shortfall is that it cannot see a region change. **The region-change stop that actually covers W2 lands in row H, against A11's page — not the page A11 replaces.** `measured`: T18's count is *"8 controls today (onboarding ×7, settings/account ×1)"*; **A11 rewrites `onboarding/index.html`'s door**, so **7 of the 8 are in the file row A is about to change.** ⛔ **Consequence the plan does not carry: if T18 lands before A11 and nobody re-runs it after, its allow-list describes a page that no longer exists.** T18's selftest must be re-run as an A11 acceptance check — put it in A11's step, not in row T's.

### H3's other half — `falsifier-tenancy.py` C2 and `X-Estate`

`measured`: C2 is at `tools/falsifier-tenancy.py:203`, five clauses C1–C5 present, selftest at `:290`. **Row T touches none of it** (SIZING §C1 agrees). H3 is unchanged by the re-sequence.

---

# 2 · WHAT EACH DOOR ROW INHERITS FROM ROW T — and what breaks if it does not

⛔ **I am not re-sizing row T. SIZING §A owns that.** This is the inheritance ledger, in this plan's terms.

| door row | what it inherits from T | what breaks without it |
|---|---|---|
| **A2–A4** (the conversion) | **T11 `change-scope.py`**, resolver ② — *worker routes*. The conversion touches ~30 handler sites across the dispatch table. | Without T11, **every re-sha after a conversion batch re-runs the full cell list** — battery cost scales with the number of batches, which is the exact cost curve Paul ruled against in the brief. With T11, a batch touching only `zones` keys carries every journey that declares no zones route. |
| **A5+A6** (`route:` + `grantsFor`) | **T11's UNSCOPED fail-closed default.** `grantFor`/`personFor`/`scopeFor` are shared helpers; T11 classifies them UNSCOPED **by construction** → full list. | ⭐ **This is the inheritance that matters most and it is the one that looks like a cost.** A5+A6 land in the auth path; a classifier that tried to be clever there would carry a cell forward over a credential change. **T11's refusal to be clever IS row A's safety.** If someone cuts T11 to resolver ① (page bytes only, the §3 cut option), **A5+A6 carry forward on a Worker-only change** — and that is precisely the change most able to kill every live credential. ⛔ **Do not take the T11 cut option in a lap that contains row A.** |
| **A9 / A11 / A12** (the door surface) | **T10's `routes`/`pages` declarations + the subset selftest.** | §5 — the whole of it. |
| **A11** | **T18's href allow-list**, re-derived against the new page. | A control that looks wired and is not, on the one surface every person meets. |
| **A12** (the shelf, 2+ branch) | **T3's UNWALKED print.** The 2+ case has no fixture (the plan says so at A12 and ux-expert re-says it at F1). | ⭐ **Without T3 the 2+ branch is INVISIBLE.** The draft's answer — *"walk it at lab with two hand-founded estates as a mechanism test, declared as such"* — is now the **wrong shape**: a mechanism test outside the matrix is a reading nothing reads. **With T3, the honest move is a DECLARED cell that prints `UNWALKED · no two-estate fixture`.** That is cheaper, more honest, and it is the pattern `NAMED_UNBUILT` already establishes. |
| **C5** (the editor stop) | **T9's recorder fix** — `record["answers"]` holds only what the journey typed. | ⛔ **C5's whole assertion is "the person typed a new address and it was refused / accepted."** At HEAD the recorder writes the **loaded fixture** into `transcript.answers` regardless of what was typed (row-T §1·3). **Without T9, C5 cannot distinguish a typed address from a fixture address, and its falsifier is unreadable.** This is the sharpest T→door dependency in the lap and the draft plan does not name it. |
| **F** (the fixture stamp) | ordering only, not a dependency (SIZING §C1 agrees). `fixture` already flows from the invite (`worker.js:803`, `measured`); **`OPEN_SIGNUPS_ARE_FIXTURES` is absent from `wrangler.toml` (`measured`)**, so F1/F2 are genuinely unbuilt. | Nothing in T breaks; but the `fixtureRun` id should land **before the first battery mints at scale**, per SIZING. |
| **the whole candidate** | **T16's viewport coverage line** and **T3b's tier check**. | The battery's coverage claim is about what the tool is *configured* to do rather than what the walks *did*. ⚠️ **See §6·7 — T16 as specified reads a hand-typed literal.** |

---

# 3 · EVERY MEASURED LINE, RE-MEASURED — stale value beside new

⛔ **Stamped `0a6c3684`. Every line number in the draft plan is `06c2a16` and every one of them has moved.**

## 3a · The counts

| what | plan says (`06c2a16`) | **measured (`0a6c3684`)** | note |
|---|---|---|---|
| raw `scopeOf(env)` | 66 | **70** | |
| **non-comment `scopeOf(env)`** | **55** | ⛔ **60** | +5 in one lap |
| `keyFor(` | 41 | **43** | |
| `env.OBSERVATIONS` | 104 | **115** | |
| `scopeFor(` sites | 3, one discarding its result | **3, one discarding its result** (`:4643` `eslint-disable-line`, `:4877`, plus the definition `:1108`) | unchanged in substance |
| `worker.js` total lines | — | **5,324** | |
| the multi-tenancy plan's *"60 call sites"* | 60 | **60** | ⭐ **the plan's own stale number is now arithmetically correct, by coincidence.** It was 60 when written, 55 at `06c2a16`, 60 today. ⛔ **Do not read this as the number being right — read it as the reason A3's "make the count a tool's output" recommendation stands.** |

## 3b · The key-kind histogram — RE-DERIVED, not carried

`measured` at `0a6c3684`, by parsing every non-comment `scopeOf(env)` line:

| kind | sites | lines | the draft's figure |
|---|---|---|---|
| `ratelimit` | **5** | 1197 · 1754 · 1775 · 1788 · 4467 | 3 — ⛔ **grew by 2** (`probe`, `recover`) |
| ⭐ `recovery` | **2** | 1700 · 4573 | ⛔ **A KEY KIND THAT DID NOT EXIST.** Lap 7's B6r. |
| `cache` | 4 | 1987 · 2036 · 2077 · 2123 | 4 ✅ (all four moved ~137 lines) |
| `zones` | 3 | 5132 · 5252 · 5295 | 3 ✅ |
| `pending-species` | 3 | 3378 · 3410 · 3427 | 3 ✅ |
| `library` | 3 | 229 · 233 · 238 | 3 ✅ |
| `audio-blob` | 3 | 2617 · 3026 · 3726 | 3 ✅ |
| `feedback` · `metrics` · `cost-log` · `zone-audio` · `zone-audio-blob` · `zone-feedback` · `zones-last-seen` · `chat-budget` · `door` · `grant` | 2 each | — | ✅ each |
| `conversation` · `onboarding-metrics` | 1 each | 2931 · 4044 | ✅ |
| **unparsed / handler-level** | **15** | 1102 · 1112 · 1155 · 1579 · 1807 · 1818 · 4260 · 4271 · 4498 · 4528 · 4588 · 4592 · 4686 · 4723 · 4748 | includes the two `OBS_KEY` observation sites (`:1807`, `:1818`) the draft counted as `observations` 2 ✅ |

⛔ **TWO RE-CLASSIFICATIONS THE DRAFT GETS WRONG:**

1. ⭐ **`grant` is not two legacy-fallback READS. One of them is a WRITE.** `worker.js:4688` — `env.OBSERVATIONS.put(keyFor(scopeOf(env), "grant", …))`, inside `whoami`'s W0 geocode retry. The draft files `grant 2` under **B-DEPLOY** (*"grantFor's legacy fallback"*, correct-as-is). ✅ **The code already knows**, and its own comment at `:4680–4681` sequences it: *"read-only handlers move onto scopeFor FIRST, and writers LAST… This branch WRITES, so it stays on the binding until the writers' slice."* **So it is a deliberate deferral, not an oversight — and it is B-CALLER, not B-DEPLOY.** Under one origin it writes another estate's grant row into the deployment's prefix. **Move it to the B-CALLER table with the code's own comment as its authority.**
2. **`recovery` (2) has no row in the draft's histogram and is NOT self-evidently deployment-scoped.** A recovery request names a person. ✅ **The ruling settles it** — `[paul-ruled 2026-09-11]` the record lands in *"its own admin-only key with its own reader"*, so **B-DEPLOY with the ruling as its written reason.** ⛔ But note the shape: **one lap added a key kind whose classification is a ruling, not a reading.** That is A0's whole case.

**Re-derived batch sizes:** B-CALLER ≈ **31** (30 + the `:4688` write) · B-CACHE **4** · B-DEPLOY ≈ **17** (was ~13; +2 ratelimit, +2 recovery, −1 the grant write, +1 `accountFor` at `:4528`).

## 3c · §2 A1 — ⛔ THE BLOCKING FINDING IS DISCHARGED

| step | the plan's claim at `06c2a16` | **measured at `0a6c3684`** |
|---|---|---|
| **B1** | `:1008` — `estates: [{ estateId: scope.id, … }]` (the deployment's) | ✅ **LANDED.** `:1064–1065` — `estates: grantRow.estateId ? [{ estateId: grantRow.estateId, relationship, capability }] : []`, with a comment naming the exact defect (*"the sweep's account founded est-gndlvf while its sign-in response said est-qa0001"*) and naming `[]` as **the empty shelf, normal, not an error**. |
| **B2** | `:977` — `delete(keyFor(scope, "grant", acct.tokenHash))` (the deployment's) | ✅ **LANDED.** `:1022` — `delete(keyFor(priorScope, "grant", acct.tokenHash))`, and `:1023` deletes the stale route row with it. |
| **B3** | `:979` — direct `env.OBSERVATIONS.put(accountKey(...))` | ✅ **LANDED.** `:1028` routes through `putAccount` when `acct.personId` exists; `:1029` keeps the bare put **only** for legacy rows with no personId, with its reason in the comment. |

⭐ **Consequences, all of them shrinking the lap:** §2 A1's 🔴 BLOCKING grade is void · **P1 becomes a one-command confirmation, not a gate** · **A0a/A0b are deleted** · **Q6 to Paul is withdrawn — it is answered by measurement, not by his word** · the §7 risk-4 slip table's B1/B2/B3 rows are void · **A9 still rewrites `:1064`**, because B1 landed as *the grant's single estate*, not as `grantsFor()`.

## 3d · Symbol drift — every plan citation, re-located

| plan cites | actual at `0a6c3684` | Δ |
|---|---|---|
| `handleSession` `:1008` / `:963` / `:1000` | **`:876`** (def) · estates literal **`:1064`** · route write **`:1011`** · `email:` **`:1037`** | +56 |
| `handleEstateFound` `:1387` · 409 `:1403–1407` · grantRow `:1466` · `writeEstatePlace` `:1481` · grant write `:1483` · route write `:1493–1495` | **`:1443`** · **`:1456–1464`** · grant/place region **`:1520–1590`** · route write **`:1562`** · `estates` literal **`:1587`** | +56 |
| `estateId(env)` `:1044` | **`:1083`** | +39 |
| `scopeFor` `:1052` | **`:1108`** | +56 |
| `scopeOf(env)` def `:—` | **`:1102`** | — |
| `assertScope` | **`:1093`** | — |
| `scopeOfRoute` | **`:1117`** · `keyFor` **`:1120`** · `dateKey` **`:1129`** · `blobKey` **`:1145`** | — |
| `ROUTE_PREFIX` `:1519` | **`:1597`** | +78 |
| `grantFor` `:1565–1582`, fallback `:1590` | **`:1637`** (def) | +72 |
| `personFor` `:1540` | **`:1622`** | +82 |
| `hostAgrees` `:1596` | **`:1679`**; `FAMILY_HOSTS` read **`:1684`** | +83 |
| `handleAccountCreate` `:643`; invite fixture stamp `:803` | **`:643`** ✅ · **`:803`** ✅ | 0 — ⭐ the only two that did not move |
| `/api/account/available` `:4374–4384`, bucket `:4377` | **`:4521–4528`**; bucket is now **`probeRateLimitOk`** at **`:4524`** | +147, **and the symbol changed** |
| `feedbackRateLimitOk` | **`:1785`** (def), used at `:4244`, `:4612` | — |
| cache sites `:1850 / :1899 / :1940 / :1986` | **`:1987 / :2036 / :2077 / :2123`** | +137 |
| B-DEPLOY `ratelimit :1141 :1651 :4324` · `door :1159 :1640` · `chat-budget :2948 :4084` · `accountFor :4381` | **`:1197 :1754 :1775 :1788 :4467`** · **`:1215 :1736`** · **`:3085 :4222`** · **`:4528`** | see 3b |
| `canonFor` per-request `:132–147` | **`:132`** ✅ | 0 |
| `wrangler.toml` `[env.paul.vars] ESTATE_ID = "est-d93508"` `:206` | **`:206`** ✅ | 0 |
| `onboarding/index.html:1217` `location.href="/viewer.html"` | the branch is **`:1295–1296`** (`var n = Array.isArray(d.estates) ? … ; location.href = (n === 1 \|\| n === null) ? "/viewer.html" : "/homes/"`) | ⭐ **the branch already exists and already reads `estates`.** A12 is smaller than the plan thinks. |
| `engine/viewer.template.html:12022` `MOM_ACK_DATA` | **`:12042`** | +20 |
| gates `:12555` / `:13583` | `hasAckContent` **`:12575`** · the questions early-return **`:13603`** | +20 |
| `journey-walk.py` `JOURNEY_IDS :308` · `JOURNEYS :781` · `refresh() :67` | **`:322`** · **`:890`** · **`:67`** ✅ | +14 |
| `release-gate.py` `report() :258` · `CLAUSES :205` · `ux_clause :247` · `VIEWPORT_RX :45` · `walk_viewport :51` | **`:258`** ✅ · **`:205`** ✅ · **`:247`** ✅ · **`:48`** · **`:51`** ✅ | ~0 |
| `journey-view.py` `newContext :63–67` · geometry `:71` | **`:63–66`** ✅ · **`:72–73`** | ~0 |

## 3e · Existence facts, re-checked

| the plan says | **measured** |
|---|---|
| `tools/household-export.py` exists, `household-import.py` does not | ✅ **still true.** 15,922 bytes / absent. **§2 A11 stands.** |
| `tools/check-scope-sites.py` — to be built (A0) | ✅ **absent.** |
| `tools/read-glance-order.py` *"does not exist yet"* (Q7, row D's threshold) | ⛔ **STALE. IT EXISTS** — 12,376 bytes, shipped `c38f2319`, **2026-09-10**, as lap 7 · C7, *"THE READER for G6/G2."* §4·4. |
| `/api/account/available` shares the household's capture bucket | ⛔ **STALE. B0 LANDED.** `probeRateLimitOk` (`:1751`) is its own bucket, wired at `:4524` with the comment `// B0 — its own bucket`. |
| `OPEN_SIGNUPS_ARE_FIXTURES` on qa/lab (F1) | ✅ **absent from `wrangler.toml`.** F1/F2 genuinely unbuilt. |
| the 409 `already-has-an-estate` (A10) | ✅ **`worker.js:1456–1464`**, comment intact. `walk-founding.py:260` clause **B** intact. **§2 A7 stands unchanged.** |
| `tools/change-scope.py` · `ask-ledger.py` · `check-href-controls.py` · `walk-notes.py` | ✅ **all absent** — row T's new tools, correctly unbuilt. |
| **Row T is 21 steps, ≈28 h** | ⛔ **STALE AS OF `0a6c3684`: 24 steps (T0–T23, incl. T3b), T22/T23 UNCONDITIONAL** `[paul-ruled §13 P8]`. **The CYCLE-LOG beat-6 entry at `:4023` still says 21.** Not mine to fix; named so the build window does not read 21 as the commitment. |

## 3f · ⭐ THE ONE HANDED TO ME BY NAME — F1, traced to the render

**ux-expert's F1, first half: ✅ TRUE at HEAD, exactly as the coordination window verified.** The grant-resolved `whoami` literal (`worker.js:4751–4783`) carries **18 keys** — `personId · estateId · capability · email · phone · contactRead · relationship · entry · vault · name · accent · address · addressParts · ranked · contactPref · profileAccent · coordinates · hasAccount` — **and no `estates`.** `estates` appears at `:832` (signup), `:4658` and `:4797` (both **zero-estate, person-resolved**), never on the grant-resolved branch.

**ux-expert's stated mechanism — *"falls through to its declared fallback, which builds an array of one"* — ⛔ WRONG, and the coordination window is right to correct it.** The fallback governs **emptiness only**: `homes/index.html:372–373`, `told = Array.isArray(d.estates); empty = told ? d.estates.length === 0 : !(merged.name || merged.addressParts)`.

⛔ **AND THE COORDINATION WINDOW'S OWN CORRECTION IS ALSO TOO BROAD. I could not reproduce it as stated.** Its claim: *"an estate-less account whose browser still holds a cached place name renders a home it does not have."* For the localStorage inference to run at all, `told` must be **false** — and `told` is false **only on the grant-resolved branch**, which by definition serves a person who **has** an estate. An estate-less account resolves through `personFor` on `:4658` or `:4797`, **both of which carry `estates: []`** → `told` true → `empty` true → **the empty shelf renders correctly.** The `read(K_NAME)` fallback at `:355` is, for that population, **dead code on the success path.**

⭐ **THE DEFECT IS REAL BUT IT LIVES ON THE FAILURE PATH, AND THAT IS WHERE IT PERSISTS.** Two sites:
- **`homes/index.html:315–317`** — `cached` is built from `read(K_NAME)` and `renderHomes(cached)` is called **before any fetch**. An estate-less account with a stale cached place name gets a phantom row **at first paint**, cleared a moment later. A flash.
- ⛔ **`:330`** — the B15 quarantine: `if (!d) { … renderHomes(cached.length ? cached : []); return; }`. **On a refused or broken or unknown whoami, the phantom row PERSISTS**, with no control to retry (**which is ux-expert's own F7, on the same screen**). **So the honest statement is: an estate-less account, on a device holding a cached place name, whose `whoami` does not resolve, is shown a home it does not have and given no way to re-ask.** That is a real defect at Mom's own physical premise — Wi-Fi from the house, coverage falling with distance.

### ⭐⭐ AND THE FINDING NEITHER SEAT REACHED — **A9 IN TWO LITERALS DOES NOT FIX F1's HEADLINE**

`homes/index.html:374` is:

```
renderHomes(empty ? [] : [merged]);
```

**`renderHomes` is passed a hand-built array of ONE, always. `d.estates` is never read for the rendering — only for the emptiness test.** The file's own comment at `:332–335` says so and calls it safe: *"A credential resolves to exactly one estate today… Rendering an array of one keeps this page correct the day there are two, with no second shape to build."* ⛔ **That sentence is the defect.** The day there are two, this page renders one — and it renders the one assembled from the *single-place* fields `name`/`accent`/`addressParts`, which do not even come from the estates array.

**So A9 is THREE changes, in one commit:**

| # | site | change |
|---|---|---|
| **(i)** | `worker.js:1064` | `estates: await grantsFor(env, acct.personId)` — as the plan already says |
| **(ii)** | `worker.js:4751` (grant-resolved `whoami`) | the **same** call, same shape — ux-expert's F1 fix |
| **(iii)** | ⭐ `homes/index.html:374` | `renderHomes(told ? d.estates.map(...) : (empty ? [] : [merged]))` — the shelf renders **the array**, merging device-cached fields **only onto the row whose `estateId` matches**, and keeping the `[merged]` path strictly as the pre-`estates` Worker fallback |

⛔ **Without (iii), (i) and (ii) make the array correct and unread — which is worse than today**, because `told` flips to true for every caller and the emptiness test stops being backed by a render that agrees with it. **Answering the question I was asked: yes, A9 lands in two Worker literals in one commit — and it is not the right fix on its own.**

⭐ **This strengthens ux-expert's "One engine, one verdict, fourth occurrence" rather than weakening it**, and it lands on the file's own instruction for a fourth: *the two functions should have been one.* The count is produced in one place and consumed in three (`onboarding:1295`, `homes:373`, `homes:374`), and only one of the three reads the array.

## 3g · THE SECOND ITEM HANDED TO ME BY NAME — what `render()` does at an instance declaring `questions` absent

**Answer: `render()` never runs.** `MomQueue.start()` returns at `engine/viewer.template.html:13603` — `if (… ABSENT_DOMAINS.includes("questions")) return;` — **before** the fetch, before `render()` (`:13608`) and before `syncServerAnswers()` (`:13609`). So *"Nothing to settle just now — the place is just growing."* (`:13046`) **does not fire** at a questions-absent instance.

**And the envelope:** `:18607` — `if (ABSENT_DOMAINS.includes("questions") && ABSENT_DOMAINS.includes("ack")) { #mp-master.style.display = "none"; }`.

`measured` across `instance/*.json`: **`home.json`, `paul.json` and `qa.json` all declare BOTH `ack` and `questions` absent** (a 19-entry `absent` array each). **`fernwood.json` declares `absent: []`.**

⭐ **So ux-expert's F5 recommendations (1) and (2) — *render nothing; the envelope is ABSENT until the first entry* — are ALREADY THE SHIPPED BEHAVIOUR at every non-Fernwood instance.** G2 is not a design decision waiting to be made. **§6·4 says what it should become instead.**

---

# 4 · WHAT THE THREE POST-`06c2a16` RULINGS CHANGE, ROW BY ROW

## 4·1 — ROW T IS FIRST AND WHOLE (24 steps, ≈28 h, none moving the candidate)

| row | what changes |
|---|---|
| **A** | ⭐ **A11/A13/A7/A9 acquire a duty they did not have** — re-deriving `routes`/`pages` in their own commits (§5). **A12's 2+ branch becomes a declared UNWALKED cell**, not an undeclared lab mechanism test (§2). **A11 acquires a T18 re-run** (§1a). |
| **C** | ⛔ **C5's falsifier becomes readable only because of T9.** Today the recorder writes the loaded fixture into `transcript.answers` regardless of typing — **C5's whole assertion is about what was typed.** Name T9 as C5's precondition in the step. |
| **H** | the three seams of §1a. H moves up in the order. |
| **G** | unchanged by T. |
| **E · F · riders** | unchanged by T. |
| **B** | unchanged by T. ⚠️ But row T's own QA section states the boundary: *"nothing here tests the door."* **Row T raises the quality of the door's evidence; it does not shorten row B's gate.** |
| **the battery (§5 of the plan)** | ⛔ **SUPERSEDED WHOLESALE.** The draft's *"five seats × five journeys, `release-gate.py --sha`"* is the **pre-T** gate. The unit is now the **`(journey, lens)` cell**; the roster is **`mom · wide-eyed · conformance · successor`** (`owner` **retired as a lens**, `strict`→`conformance`) `[paul-ruled §13 P1]`; the cell list is **`cycle/release/cells/lap-8.json`**, Paul's at beat 6. **Rewrite §5 of the build plan against row T's §4 before the build window reads it.** ⛔ **The draft's "Seats: five — `mom` · `owner` · `strict` · `wide-eyed` · `handover`" is a roster that no longer exists.** |
| **§8·6 (the pre-candidate checks)** | gains `change-scope.py --selftest`, `check-href-controls.py --selftest`, and **T21's committed before-image**. |
| ⛔ **J3** | **REFUSED for all five seats** (row T's QA, re-measured at lap 8's open) and it sits in the proposed cell list **three times**. **This is a lap-8 battery blocker, not a row-T one** — the door's battery cannot run J3 until the fixture is repaired. **Name it in the build brief with the repair sized, or declare those cells UNWALKED with the blocker named.** |

## 4·2 — THE ACCOUNT-FIRST RULING (*"the account is always the first layer"*; zero estates is NORMAL)

| row | what changes |
|---|---|
| **A11** | ⭐ **The door leads with the ACCOUNT, and F2 is the finding that follows.** `measured`: `onboarding/index.html:7` `<title>My Home</title>` · `:313` `<h1 id="head">My Home</h1>` · `:398` `<p class="lede">Your place, on any phone.</p>` · the two doors `:400` `#sd-setup` *"Set up my place"* / `:401` `#sd-signin` *"I've been here before"* — ✅ **already correct and account-first**; it is the masthead and the lede above them that are not. **And a fourth site the plan does not carry: `:1513` `el.head.textContent = read(K_NAME) \|\| "My Home"` — the masthead is fed by localStorage on the signed-out screen.** That is the same device-authority defect as F1's phantom row, one page over. |
| **A12** | *set up a place* moves INSIDE, to the empty shelf. ✅ **The shelf's reached-and-empty branch already exists and is already correct** (`homes/index.html:188–260`, with the four-state resolver and its own history). **A12 is now mostly the branch at `onboarding:1295–1296`, which already reads `estates`** — so A12 is a smaller step than the draft sizes it. |
| **A9** | the `[]` return is already ruled and already shipped at `:1064`. **A9 is the array, not the empty case.** |
| **D7/B2 founding-first on the bare door** | superseded. ⚠️ **`journey_bare_door()` (J5) walks the pre-ruling door.** `measured`: `journey-walk.py:750`. **J5 is already UNWALKED/blocked** (no seat has an account to sign back in as) — so the collision is latent, not live. **Name it: A11 changes what J5 would walk, and J5's declaration must move with it (§5).** |
| **G2** | ⭐ **the ruling is what makes §3g decisive.** *"An account may hold zero estates and the empty shelf is NORMAL"* is the same sentence as *"a household with nothing acknowledged is normal."* The ribbon's absence is not an edge case; **it is the state every new household starts in.** |

## 4·3 — THE APEX DOMAIN (`myhome.place`; B6a–B6d; the link Mom receives is the apex)

| row | what changes |
|---|---|
| **B** | +4 steps, as the plan already carries. ⚠️ **I did not verify the zone, the DNS state or the 0-record claim — relayed, and I ran no network probe.** |
| **A11** | ⭐ **THE NAME BLOCK MOVES, AND ux-expert IS RIGHT.** The plan's **Q0** says *"rule both before B6c, not before A — A ships nothing Mom receives."* **That is true of the LINK and false of the SCREEN.** A11 is the surface that prints the product's name, and there is no name. ⛔ **I endorse F2's correction and I am not deciding it — §8·Q0.** |
| **B6c** | the grep stands. |
| **SEAM-4a** | stands, and gets sharper: a permanent link raises the cost of a late name. |
| **`pages-deploy.py` / `post-deploy.py` ORIGIN maps** | **not verified by me at HEAD.** §7. |

---

# 5 · ⭐ THE DUTY T OWES A — WHERE IN ROW A THE RE-DERIVATION HAPPENS

**T10 gives every `JOURNEYS` entry four keys and a selftest clause asserting that every route and page literally present in the action list is a SUBSET of the declaration.** The clause **cannot prove completeness** (an implicit call made by the page's own JS is invisible to a regex over the action list) and **says so on its own face**. It proves the declaration is not **stale** — which is exactly the failure row A creates.

⛔ **"Row A re-derives the declarations" is not a step. Named as a row-level duty it will be done once, at the end, by whoever remembers.** Here is where it lands, concretely, per commit:

| row A step | what it moves | the re-derivation, in the SAME commit | the journeys affected |
|---|---|---|---|
| **A7 · `X-Estate`** | adds a **header**, not a route | ⛔ **No `routes` entry changes — and that is the trap.** T10 declares routes, not headers. **A7's own check must extend `falsifier-tenancy.py` C2 (H3), because T10 cannot see this change at all.** ⭐ **Name this explicitly or a window will assume T10 covers it.** | none by T10; **all** by C2 |
| **A9 · `/api/session` returns the array** | changes a **response shape**, not a path | same as A7: **T10 cannot see it.** A9's own check is the journey stop (`[]` vs length 1) plus **(iii)** of §3f. | none by T10 |
| ⭐ **A11 · the single sign-in page** | **replaces `onboarding/index.html`'s door section** | ⛔ **THE BIG ONE.** Every journey whose action list clicks `#sd-setup` / `#sd-signin` / `#si-*` / `#s-nolink` must have its `pages` **and** its `routes` re-derived. `measured`: `journey_returning` (`:556`), `journey_resuming` (`:626`), `journey_lifecycle` (`:677`), `journey_bare_door` (`:750`) all enter through this page. **Run `journey-walk.py --selftest` in the A11 commit; a red there is the design working.** | **J0 · J2 · J3 · J5 · J8** — and **J9**, once H2 declares it |
| **A12 · the landing branch** | changes **where the door sends you** — `/homes/` vs `/viewer.html` | ⛔ **`pages` changes for any journey that lands.** A journey declaring only `/onboarding/` and `/viewer.html` that now routes through `/homes/` has a **stale declaration that mis-scopes its own re-run** under T11. | **J0 · J3** at minimum |
| **A13 · `/api/account/available`** | the route exists; its **behaviour** may change on security-steward's ruling | if the seat **removes** the route, every journey declaring it must drop it — **`routes` shrinks, and the subset clause does not catch a shrink** (a subset of a superset still passes). ⛔ **A removal is the one direction T10's clause is blind to. Say so in A13's step.** | J0's signup path |
| **A2–A4 · the conversion** | changes **no route and no page** | ✅ **nothing to re-derive** — and this is why T11 classifies shared helpers **UNSCOPED** rather than trying. | none |

⭐ **The one-line rule for the build brief:** **every commit that touches a served page under `onboarding/`, `homes/`, `estate/` or `settings/account/` runs `python3 tools/journey-walk.py --selftest` in the same commit, and a red is the tripwire firing, not a blocker to route around.**

⛔ **And the blind spot, stated because a control that cannot say it is out of scope is already trusted for it:** T10's clause sees **routes named literally in an action list**. It sees **nothing** of (a) a header, (b) a response-shape change, (c) a route **removed** from a declaration, (d) a call the page's own JS makes. **A7, A9 and A13 are three of the four.** Their cover is `falsifier-tenancy.py` C2 (H3) and the journey stops — **not T10.**

---

# 6 · WHAT I NOW BELIEVE SHOULD NOT BE BUILT, OR SHOULD CHANGE SHAPE

## 6·1 ⛔ **A0a / A0b — DELETE.** B2 and B3 landed (§3c). Nothing to absorb. **Q6 is withdrawn from Paul's list.**

## 6·2 ⚠️ **A0 (`check-scope-sites.py`) — KEEP, and REWRITE ITS FALSIFIER. The one it has would have deleted it.**

The draft's falsifier: *"if the conversion lands, the falsifier passes at lab, and the checker never once goes red across lap 8 and lap 9, delete it — it measured nothing."*

⛔ **That is the wrong predicate, and I can now show it.** `measured`: the surface grew **55 → 60 sites and gained a whole new key kind (`recovery`) in ONE lap** — while the tool did not exist. Had it existed, it would have gone red the moment `recovery` appeared, **and it would have gone red on work that was entirely correct** (lap 7's B6r, ruled and shipped). A red on a legitimately-new site is the tool **working**, not the conversion failing — so the draft's clause counts the tool's successes as evidence to delete it.

⭐ **Recommendation, and it is a two-line change to A0:** the falsifier becomes **"if no site is ever added, moved or re-classified without the register learning about it across laps 8 and 9, delete it."** Same spirit, right predicate. And **its first run at lap 8's open is the baseline** — 60 sites, ~31/4/17 — committed, so the register has a pre-image the way T0 gives T21 one. **Why this matters beyond the tool:** a control whose delete-clause fires on its own successes is a control nobody will defend at the moment it is inconvenient.

## 6·3 ⚠️ **A12's 2+ branch — CHANGE SHAPE.** Not *"walk it at lab as a mechanism test, declared as such."* **A DECLARED CELL IN `cells/lap-8.json` THAT PRINTS `UNWALKED · no two-estate fixture`.** With T3 landed, a mechanism test outside the matrix is evidence nothing reads; a declared UNWALKED cell is the coverage print doing its job, and it is the pattern `NAMED_UNBUILT` already establishes in this repo. **Cheaper and more honest.**

## 6·4 ⭐⭐ **G2 — CHANGE SHAPE ENTIRELY. It is not a design question, and the real finding is one layer down.**

§3g measures it: **the absent-envelope behaviour ux-expert recommends is already shipped**, and every non-Fernwood instance already declares both `ack` and `questions` absent.

⛔ **But both gates read a BUILD-TIME declaration.** `ABSENT_DOMAINS` comes from `{{IDENTITY:absentJs}}` (`:7508`) — an **instance file**, baked into `viewer.html` at build. So:

> **A household that gives its first piece of feedback does not get an acknowledgment ribbon until somebody hand-edits its `instance/<env>.json` and rebuilds the page.**

**The envelope's first appearance is a DEPLOY, not an event.** ⭐ **And G1 entrenches it**: moving `MOM_ACK_DATA` into the instance makes the ribbon's *content* instance-supplied on the same build-time axis as its *existence*.

**Recommendation:** G2 stops being *"what does the empty ribbon say"* and becomes **"the envelope's appearance is a runtime read of the household's own record, not a build-time declaration."** ⚠️ **I am not sizing that here** — it is a real design change with a real cost, and it may be right to accept the build-time gate for lap 8 and name the limit on the release note. **What must not happen is G2 shipping a second empty state for a case that cannot arise, while the case that WILL arise — a household's first feedback landing into a page that cannot show it — goes unnamed.** §8·Q9.

## 6·5 ⛔⛔ **R0 (the ask ledger) — I GOT THIS WRONG AND THE CORRECTION IS RECORDED, NOT REWRITTEN AWAY.**

**What I first wrote here, and it is struck:** *"`tools/ask-ledger.py` is absent and I found no `.plans/2026-09-11-ask-design-PLAN.md` in the tree at `0a6c3684` — move R0 to lap 9."*

⛔ **THE PLAN EXISTS. I ASSERTED AN ABSENCE I HAD NOT MEASURED** — I listed `tools/` and never listed `.plans/`, then wrote the absence as a finding. **That is this repo's own named class, committed by the seat auditing for it**, and the strike is recorded rather than the text deleted, because a rejected recommendation nobody wrote down gets re-proposed.

**What is actually true, `measured` at `0a6c3684`:**

| | |
|---|---|
| `.plans/2026-09-11-ask-design-PLAN.md` | **EXISTS**, six seats filed, and it names **engineering-partner "owed, not waived"** for exactly this |
| the spec's location | ⛔ **§9, not §4.** The lap-8 draft plan's R0 step points at *"§4"* — **§4 is THE FOLD.** ⭐ **A build window following the draft's pointer lands on the wrong section of the right file**, which reads like a spec and is not one. **Correct the pointer in the build brief.** |
| the spec's completeness | **Full.** §9.1 inputs-by-file each with its UNREADABLE condition · §9.2 output shape, **per ENV and ⛔ never per estate at any size** · §9.3 exit codes + selftest mutations · §9.4 falsifiers |
| the authority | the plan states it: *"the build is lap 8 R0; **this spec wins where they disagree**"* — which is exactly what the draft's placeholder said to expect |

⭐ **So my recommendation flips, and the reason is better than the one I had.** `measured` from §9.1: **five of the seven inputs are UNREADABLE at lap 8** — the P2 carrier is unbuilt, `engine/asks.json` is **PROPOSED and does not exist**, `GET /api/onboarding-metrics` is **R1** (so `UNREADABLE — R1` until R1 lands), the declarations route is **lap 9 · A**, and `.private/feedback-log.json` may be absent.

⛔ **That is NOT an argument to defer — it is the spec working.** The whole posture of this repo's readers is *exit 3 = UNREADABLE, never green by absence*, and **a ledger that prints five UNREADABLE rows with each blocker named is the most useful thing lap 8 can produce about its own asks.** It is the `walk-fixtures.py` pattern: *a hole prints LOUD*.

**Recommendation: BUILD R0 IN LAP 8, with three corrections to the draft's step.**
1. **Re-point it at §9**, not §4.
2. ⚠️ **`engine/asks.json` is PROPOSED, not existing** — R0 either creates it (an empty register with its schema) or prints `no card-intro asks registered`. **The draft's step does not name this file at all.** ⛔ **Do not let a build window infer a new engine file into existence from a ledger's input table.**
3. **R1 stays R0's precondition**, unchanged — and it is now the *only* one of the five blockers lap 8 can clear.

⚠️ **The honest cost, said once:** lap 8 is **24 row-T steps + ~40 door steps**, and R0 adds a tool whose output is mostly UNREADABLE for two laps. **If Paul wants the lap smaller, R0 is still the cheapest thing to drop** — but drop it as a *sizing* decision with the spec sitting ready, **not on my false premise that it had no spec.** §8·Q11.

## 6·6 ⚠️ **§5 of the build plan (THE BATTERY) — REWRITE, do not amend.** §4·1. Its seat roster no longer exists and its unit is the pre-T one.

## 6·7 ⛔ **A DEFECT IN ROW T ITSELF, found while tracing the T↔H seam — T16 replaces one typed value with another.**

SIZING T16 says: *read each run's own recorded geometry from `_view.json` rather than regexing the tool's source*, citing `journey-view.py:71` as *"already writes `out.geometry`."*

`measured` at `journey-view.py:63–73`:

```
const ctx = await b.newContext({ viewport: { width: 414, height: 848 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true });
...
const out = { …, geometry: { width: 414, height: 848, deviceScaleFactor: 3, isMobile: true } };
```

⛔ **`out.geometry` is a HAND-TYPED LITERAL that duplicates the object above it.** It is not derived from the context. So T16 as specified **swaps a regex over the tool's source for a constant typed ten lines below that source** — and once T14 makes `engine`, `storageState` and `initScript` configurable, **the two can disagree silently.** ⭐ **This is the fourth instance of the rule T16's own write-up invokes** (*"READ, NEVER TYPED"* — and the implementation typed it).

**Recommendation, ~10 minutes inside T16:** build the context options as a named object and spread it into both `newContext(opts)` and `out.geometry`, so there is **one literal**. ⚠️ **This is row T's to fix, not row H's or row A's — hand it to the row-T build window.** Without it, T16 lands, prints a geometry set, and the set is a claim about a constant rather than about the walks.

## 6·8 ⚠️ **NOT A LAP-8 ITEM, but it belongs in the door's security read: `settings/account/index.html:114` carries a named individual's literal contact address**, in a page served to **every** household under the single-origin door. `check-estate-neutral.py`'s 311 needles are **Fernwood's**, so it cannot see this — the same class as the 09-07 gauge leak (*"the leak was numbers, not names"*). **It may well be correct** — Paul administers every estate, and the line is the honest recovery path. **But it is a person's contact value in an engine file, and it should be a ruling rather than an inheritance.** ⛔ Not mine to decide; handed to security-steward alongside A13.

## 6·9 ⭐ **CONFIRMED, NOT CHANGED — the draft's four best calls stand, and I re-verified each**

- **A4's sentinel recommendation** — `wrangler.toml:206` still binds `est-d93508`. The argument holds and gets stronger with 60 sites: a missed write should land somewhere findable.
- **A5+A6 as ONE commit** — re-verified. `:1011`, `:1562` and `:1626`/`:1644` are four reader/writer pairs on `route:`; splitting them kills every live credential. ⭐ **And it is now SMALLER than the draft thinks:** `:772` (signup) **already writes `{ personId }` alone**, the ruled shape. **M1 is two sites, not four.**
- **A7's "leave the 409 standing, rewrite its comment"** — `worker.js:1456–1464` and `walk-founding.py:260` both intact. Unchanged.
- **A10's `--fix` / `--extract` tripwire on row G** — unchanged and still the right shape: in the step, per run, not in a note.

---

# 7 · WHAT I COULD NOT VERIFY — on its own face

| | why |
|---|---|
| **The apex zone, its DNS records, the 0-record claim, and any Pages binding** | **relayed to me; I ran no network probe and read no Cloudflare state.** Every B6a–B6d measurement in this file is inherited, not measured. |
| **Anything in KV, at any environment** | no store read. The `home` account/grant row, the 174 unmarked qa rows, `est-qa0001`'s digest — **all inherited from the chronicle.** |
| **Any rendered surface** | ⛔ **I loaded no page, ran no browser, took no screenshot and measured no geometry** — the same boundary ux-expert declared. Every prominence, weight and ordering claim I carry from F2/F4/F7 is **their source-read, re-checked as source**, never as a render. **Nothing here was measured at 414 × 848 × A+.** |
| **`tools/household-export.py`'s code** | I verified it exists (15,922 bytes). **I did not read what it exports**, so §2 A11's *"row B cannot start without an import"* is re-confirmed on the import's **absence**, not on the export's contents. |
| **`tools/pages-deploy.py`'s `ORIGIN`/`PROJECT`/`HOUSEHOLD` maps and `post-deploy.py`'s host map at HEAD** | **not opened.** Every B6b/B6 line number in the draft is carried unverified. |
| **`release-gate.py`'s `judge()` and `report()` behaviour under T1** | I read the symbol table (`seats():78`, `judge():91`, `CLAUSES:205`, `report():258`) and **did not simulate the re-key.** The 22-runs / 12-failed-actions / 0-red-cells measurement is **practice-steward's and coordination's, twice, and I did not reproduce it.** ⚠️ And **the cell count is still undetermined** — 15 under one grouping, 10 under the other. **No cell count in this file is quoted as fact.** |
| ⛔ **`.plans/2026-09-11-ask-design-PLAN.md`** | **I claimed it was absent WITHOUT LOOKING, and it exists.** §6·5 carries the strike. I have now read its header and §9; **I have NOT read §§0–8 or §§10–13**, so my sizing of R0 rests on its spec section alone. |
| **Timing side-channels on the door** | **UNCHECKED**, as the draft's risk-3 already says — **and this is the fourth consecutive artifact to assert it without measuring it.** Marked unchecked rather than asserted. |
| **Whether A12's 2+ branch renders correctly** | **cannot be verified by anyone** — no fixture, no person has ever held two places. §6·3. |

---

# 8 · WHAT PAUL MUST RULE — question · recommendation · alternatives

⛔ **I am deciding none of these.** Two are new; the rest are the draft's §9, re-priced.

| # | question | recommendation | alternatives |
|---|---|---|---|
| **Q0** ⭐ | **Does A11 ship nameless?** The apex ruling settles the **address**; the **product name** and the **family door** are still empty slots. The draft blocks the name at **B6c**; ux-expert's F2 says **A11 is the surface that cannot ship nameless**, and I verified four sites where the page names a place before a credential resolves (`onboarding` `:7`, `:313`, `:398`, `:1513`). | **Rule the name before A11.** A11 is the first surface every person meets and the apex makes the link permanent, so a late name costs more, not less. | (a) A11 ships a **place-neutral lede + neutral wordmark**, name as a named follow-up before B6c — cheap, unblocks A, leaves the front door nameless. (b) Keep the draft's ordering and accept "My Home" on the door for one lap — ⛔ I recommend against; it is the one screen where the account/place inversion is visible. |
| **Q1** | **`ESTATE_ID` at the single production origin** — a sentinel, or the condo's binding? | **The sentinel.** Re-confirmed at 60 sites: a missed write should land where it is findable, not inside a real person's namespace. | keep the condo binding (zero cost, and every missed site is camouflaged). |
| **Q2** | **`X-Estate` in lap 8?** | **Build the header, keep the 409.** Unchanged. ⚠️ **And note it is invisible to T10** (§5) — its only cover is C2. | build neither; build both header and second-founding surface (lap 9 · C's work pulled forward). |
| **Q3** | **What may the door SAY about what it reveals?** | Unchanged: **ship the true sentence, not the reassuring one.** security-steward rules before A13. ✅ **The rate-bucket half is now BUILT, not owed** — `probeRateLimitOk`. ⭐ **And ux-expert's F8 adds a placement recommendation I endorse: the username clause belongs on the username FIELD, not as a second privacy sentence on the door.** | one consolidated privacy line (⛔ turns the door into a policy page). |
| **Q4** | **Does the email editor need anything beyond re-auth?** | Unchanged: **(i) the password, (ii) no verification this lap, stated honestly.** ⭐ **ux-expert's F3 adds a shape constraint I endorse on engineering grounds: the recovery address gets its OWN card with its OWN commit.** A conditional challenge on a shared Save is a half-save a person cannot predict — and a half-save on the field that gets them back in is the worst place in the product for one. | one Save, whole page gated when the address is dirty (cheaper; prices a colour change at a password). |
| **Q5** | **s3 — declare it out of lap 8?** | **Yes, by name**, as L13 is. ⛔ Not a hand-minted grant. Unchanged. | pull INVITE & JOIN's build into lap 8 (contradicts 9·4). |
| ~~**Q6**~~ | ~~B2/B3 into lap 8 if lap 7 slips~~ | ✅ **WITHDRAWN — answered by measurement.** All three landed (§3c). | — |
| **Q7** | **Row D's 10-session threshold** | ⭐ **Re-priced: `read-glance-order.py` EXISTS** (shipped 09-10). The recommendation is unchanged and now **actionable rather than hypothetical** — *state the window's start, not just the count*: 10 sessions **since G6 deployed**. | count-only (⛔ the reading this loop has been burned by twice). |
| **Q8** | **Row B's export scope** | **Everything under the estate prefix.** Unchanged. | the account row only (⛔ a data loss that reports success). |
| ⭐ **Q9** *(new)* | **Is the acknowledgment envelope's appearance a BUILD-TIME or a RUNTIME fact?** (§6·4) Today it is build-time: a household's first feedback cannot raise the ribbon until someone edits its instance file and rebuilds, and **G1 entrenches that**. | **Accept build-time for lap 8 and NAME THE LIMIT ON THE RELEASE NOTE**; scope the runtime read as a lap-9 row. **Why:** the runtime read is a real design change with a real cost, and lap 8 already carries 24 + ~40 steps. **What is not acceptable is shipping G1 without anyone knowing the ribbon cannot appear on its own.** | (a) build the runtime read in lap 8 as part of G — honest, and it grows row G from 4 steps to ~7 in a lap that is already the largest on record. (b) Ship G1 and say nothing — ⛔ recommend against: it makes an attribution surface that Paul must deploy in order for a person to be acknowledged. |
| ⭐ **Q11** *(new)* | **Does R0 (the ask ledger) build in lap 8?** Its spec is complete (`ask-design-PLAN` §9) and **five of its seven inputs are UNREADABLE until lap 9**. | **Build it.** A ledger printing five UNREADABLE rows with each blocker named is the loudest thing lap 8 can say about its own asks, and it is the `walk-fixtures.py` pattern this repo already trusts. ⚠️ Re-point the step at **§9**, and rule whether R0 **creates** `engine/asks.json` or prints *no card-intro asks registered*. | Defer to lap 9 as a **sizing** call — legitimate in the largest lap on record, and the spec keeps. ⛔ Not as a coverage call: the asks are already being made. |
| ⭐ **Q10** *(new)* | **A9 in three changes, not two** (§3f·iii) — the shelf must render `d.estates`, not a hand-built array of one. | **Yes, three, in one commit.** Two literals leave the array correct and unread, which is worse than today because `told` flips true for every caller while the render still ignores it. | Two literals now, the shelf's plural render in lap 9 · C (with the second house) — ⛔ recommend against: it ships a door that routes to a chooser the same lap the chooser is known to drop a house. |

---

# 9 · FALSIFIER FOR THIS RE-AUDIT

- **If the build window finds that B1, B2 or B3 is NOT landed at the candidate sha, §3c is wrong and §1's deletion of A0a/A0b is wrong with it.** One command settles it: `grep -n "estates: grantRow.estateId\|priorScope, \"grant\"\|if (acct.personId) await putAccount" worker/worker.js` → three hits.
- **If A9 lands in two literals and a two-estate person at lab sees two rows on the shelf, §3f·iii is wrong** and I have over-sized A9. (I do not believe this: `homes/index.html:374` builds the array by hand.)
- **If T14 lands as a grown argument object and H1 builds a second context without either duplicating `newContext` or refactoring T14, §1a's seam finding is wrong.**
- **If a household gives its first feedback and an acknowledgment ribbon appears without anyone editing an instance file or rebuilding, §6·4 and Q9 are wrong.**
- ⛔ **§6·5 already fired once: I asserted an absence I had not measured.** The general form — **if any "X does not exist" in this file was not produced by an `ls` or a `git log` printed above in §10, it is an assertion, not a measurement.** Three were (`household-import.py`, `check-scope-sites.py`, `OPEN_SIGNUPS`); one was not, and it was wrong.
- **If `check-scope-sites.py` is built, runs across laps 8 and 9, and never once reports a site the register did not already know about, §6·2's replacement falsifier fires and the tool should be deleted** — on the new predicate, not the old one.
- ⛔ **And the one that catches this file:** every count above is `0a6c3684`. **If the build window reads a number from here rather than re-running §10, this re-audit has become exactly what it was written to correct.**

---

# 10 · QA — how to re-check every measured line in this file

```
git rev-parse --short HEAD                                     # this re-audit is stamped 0a6c3684
grep -c "scopeOf(env)" worker/worker.js                        # 70 raw
grep -n "estates: grantRow.estateId" worker/worker.js          # B1 LANDED (:1064)
grep -n "priorScope, \"grant\"" worker/worker.js               # B2 LANDED (:1022)
grep -n "if (acct.personId) await putAccount" worker/worker.js # B3 LANDED (:1028)
sed -n '4751,4783p' worker/worker.js                           # the grant-resolved whoami — 18 keys, no `estates`
grep -n "estates:" worker/worker.js                            # :832 :1064 :1587 :4658 :4797
sed -n '315,317p;330,331p;372,374p' homes/index.html           # the cached pre-paint, the B15 quarantine, the render
grep -n "probeRateLimitOk" worker/worker.js                    # B0 LANDED (:1751 def, :4524 use)
grep -n "OPEN_SIGNUPS" worker/wrangler.toml                    # F1 unbuilt — no output
ls tools/household-import.py tools/check-scope-sites.py        # both ABSENT
ls .plans/2026-09-11-ask-design-PLAN.md engine/asks.json        # the plan EXISTS (§6·5); asks.json does NOT
ls -l tools/read-glance-order.py                               # EXISTS — Q7 re-priced
sed -n '13601,13609p;18605,18610p' engine/viewer.template.html # render() never runs; the envelope's two-domain gate
python3 -c "import json;[print(f,json.load(open(f)).get('absent')) for f in ['instance/fernwood.json','instance/paul.json','instance/qa.json','instance/home.json']]"
sed -n '63,73p' tools/journey-view.py                          # the inline newContext + the TYPED out.geometry
grep -n "^JOURNEY_IDS\|^JOURNEYS\|^NAMED_UNBUILT" tools/journey-walk.py   # :322 :890 :968
sed -n '7p;313p;398p;400,401p;1295,1296p;1513p' onboarding/index.html     # F2's four sites + the landing branch
```

⚠️ **What this QA does NOT cover, on its own face:** anything **rendered**, anything in **KV**, anything on a **network**, and anything about the **apex**. Every line above re-checks a source read at one sha. **None of it establishes that any of these surfaces behaves this way in a browser at 414 × 848 × A+** — and three of the four door surfaces still do not exist.
