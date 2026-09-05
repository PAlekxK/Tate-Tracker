# RELEASE-CASCADE TRACKING — how cascade state is DERIVED, per feature, over time · PROPOSAL
- row: process (no BACKLOG row yet — this proposes one, same as the 09-03 QA/UX proposal)
- objective: O5
- class: engine · must-not-diverge (a second definition of "this gate passed" is the defect this exists to prevent)
- seats: practice-steward (this file)
        engineering-partner → deferred: nothing is built until Paul rules; §7 is the handoff
        ux-expert → waived: no surface is proposed here
        ai-advisor → waived: every mechanism proposed is deterministic; the one AI half (a walking agent's report) is already sited by the 09-04 audit §B.5
- depends-on: .plans/2026-09-04-three-environments-PLAN.md
- depends-on: .plans/2026-09-04-process-wiring-AUDIT.md
- depends-on: .plans/2026-09-03-qa-test-vs-ux-review-PROPOSAL.md
- ready: agent-proposed 2026-09-05 — **Paul rules**
- stage: draft

> **Method only. This file ranks no feature, no finding and no surface.** It says how a walk's trail
> becomes state. It never says which feature should walk first, or which gate matters more.
>
> **Assignment** `[paul-stated 2026-09-05 ~1:50 AM ET]`: *"Practice-steward should be sure that we're
> tracking that for each and every feature over time, to be sure that everything goes through a
> rigorous testing process. So it'll probably evolve over time."*
>
> **The ruling being tracked is not re-derived here.** Gate 1 synthetic persona → gate 2 Paul → gate 3
> Mom is settled: `.plans/2026-09-04-three-environments-PLAN.md` § THE RELEASE CASCADE and memory
> `feedback_release_cascade_persona_paul_mom`.

---

## 0 · WHAT EXISTS TODAY — measured, and it is more than the brief assumed

Every claim below was read or executed at ~2:00 AM ET, 2026-09-05.

| capability | where | state |
|---|---|---|
| the release's identity | `.plans/*-PLAN.md`; C4 process proposal §1 *"the plan file is the release's identity"* | ratified |
| per-item stage | `- stage:` header key, enum in `tools/check-backlog-ready.py:47` | live, 8 plans |
| a repeatable per-event LOG on a plan | `- stage-note:`, `REPEATABLE` at `check-backlog-ready.py:48` | live, ~20 in the wild |
| a claim-has-its-trail check, silent at zero, flags-never-edits | `tools/check-backlog-ready.py` | live, in the session-start block |
| a stage-note already read by a second consumer | `tools/qa-divergence.py --check` (sha **or** first 40 chars of the subject) | live |
| the rendered gate as an exit code, Access headers threaded | `tools/qa-walk.py` + `tools/qa_access.py` | live |
| **origin → git sha, read off the running origin** | `qa-build.json` on the QA Pages origin, written by `deploy-worker-qa.yml:113` | live |
| a derived, never-written-down access view | `tools/access-map.py` | live — the posture model for this whole proposal |
| the E2E journey walk's procedure, trail siting and clock | `.plans/2026-09-04-process-wiring-AUDIT.md` §B.5 | proposed, unruled |

**And what does not exist. Verified two ways, because a single grep returning zero is not evidence:**
`grep -rln "cascade\|gate 1\|gate1" tools/` → empty; and no `.plans/*-PLAN.md` carries a gate stamp of
any kind. **There is no cascade tracking today. Tonight's gate-1 findings exist in exactly one place —
the body of commit `ad8d4fc` — joined to nothing.**

⚠️ **And the feature that was walked has no plan file.** `ls .plans/ | grep -i onboard` → empty. Under
the ratified join key (§2) tonight's release has no identity, so it has nowhere to carry state. The
header is already drafted — 09-04 audit §B.6 — and writing it is the cheapest act in this document.

---

## 1 · WHAT A GATE WALK LEAVES, AND WHERE

### 1a · The shape: a POINTER in the plan, and every fact inside an artifact the runner wrote

⛔ **No fact a human types is state.** The header line carries only the join; everything a reader would
be tempted to type — which sha, which environment, who walked, whether it passed — is **read out of the
running origin at walk time** and written by the runner.

Reuse `seats:` verbatim — same parser branch, same continuation-line shape, same
"cites-a-file-that-must-exist" rule already enforced at `check-backlog-ready.py:196`:

```
- gates: 1 → .plans/walks/2026-09-05-onboarding-gate1.json
         2 → .plans/walks/2026-09-05-onboarding-gate2.json
         3 → not walked
```

`not walked` is the only legal non-pointer value, and it is **not** a waiver. (`waived:` is deliberately
excluded: a waivable gate is not a gate, and if Paul wants a waiver it should be his explicit amendment,
not a convention this file smuggles in.)

**Why a new directory rather than `.ux-reviews/` or `.audit/`:** `.plans/walks/` sits beside the file it
joins to, so `check-backlog-ready.py`'s existing `file_date()` and existence machinery work on it
unchanged. `.ux-reviews/` is already ruled (09-04 audit §B.5) as the home for the *judgment* half of a
journey walk — the un-primed agent's prose report. These are the *machine* half. Two different artifacts,
and the pointer in `gates:` is what binds them. `.audit/` is stale since May and is not a live convention.

### 1b · The artifact — what is DERIVED and what is irreducibly ASSERTED

The corpus's own move when a probe cannot exist: `read-mom-feedback.py` prints the claim **labelled as an
assertion** rather than faking a probe. Same here. Two blocks, never merged:

```jsonc
{
  "plan": ".plans/2026-09-05-onboarding-PLAN.md",   // the join key
  "gate": 1,
  "ranAt": "2026-09-05T01:40:00-04:00",
  "derived": {                       // READ OFF THE RUNNING ORIGIN. Nothing here is typed.
    "origin":     "https://fernwood-qa.pages.dev",
    "servedSha":  "ac0affe6e1b...",  // GET /qa-build.json .sha
    "servedSubj": "cascade: Mom is gate 3 — and --dry-run...",   // survives rebase; the sha does not
    "env":        "qa",              // GET <worker>/health .env
    "estateId":   "est-qa0001",      // GET <worker>/health .estateId
    "walker":     "p-qa-synth-1",    // the grant row actually presented
    "exit":       0                  // the runner's own exit code
  },
  "asserted": {                      // a human's word. Labelled, never promoted.
    "by": "p-7f3a2c", "verdict": "pass",
    "findings": ["duplicate address row on a fresh browser", "personId: null on the stored answer"]
  }
}
```

⭐ **`derived.servedSha` and `derived.env` are the load-bearing pair.** They are the two facts a
hand-typed status column structurally cannot fake, and both already have a live producer. A stamp that
claims QA while `env` reads `lab` is caught by construction — which is precisely tonight's situation, and
the tracker would have printed it without anyone remembering to.

### 1c · Per gate — who writes it, and what "derived" can honestly mean

| gate | derived half | asserted half | the honest limit |
|---|---|---|---|
| **1 · persona** | the whole `derived` block; the runner writes the file as its last act | findings prose | a green runner proves traversable, never that the flow reads right |
| **2 · Paul** | `origin` · `servedSha` · `env` · that **his** grant was presented (`/api/grant/whoami`) | his verdict and what he saw | ⛔ *"Paul walked it and it read right"* is **not derivable and must never be rendered as if it were.** The artifact records that a session opened the origin under his grant; the judgment is his word, stamped as his word |
| **3 · Mom** | `check-live.py` (bytes live == the ref) + `read-mom-engagement.py` (her device met that build) | nothing | gate 3 **is the ship**, not a verdict. Its evidence is that the build reached her, never that she liked it |

### 1d · The corroboration channel, and the measured reason it is dark today

An independent second read — `access-map.py`'s posture — is that a walk which really happened leaves the
walker's `personId` on rows in that estate's KV. **That read is unavailable now:** tonight's gate-1
finding (b) is that `/api/feedback` stores `personId: null` even against a presented credential, because
the POST short-circuits ahead of the grant gate (commit `ad8d4fc`).

⭐ **The defect gate 1 caught is the same defect that would make gate-1 evidence self-corroborating.**
Naming it, not fixing it — it is a capability-model call and therefore Paul's. Until then §1b's artifact
is a **single-method** record, and this document says so rather than implying two.

---

## 2 · THE JOIN KEY — the plan file path. Nothing is minted.

C4 process proposal §1, ratified: *"A release is one plan file's change set… The plan file is the
release's identity. No plan file → no release."* The cascade joins on that and adds no second identity.
It also inherits, free, the join `qa-divergence.py --check` already performs, so **one stage-note keeps
serving two readers and no third tracker appears.**

⚠️ **CONTRADICTION — reported, not resolved.** Paul tonight: track the cascade *"for each and every
feature."* C4 §9 Q3 `[paul-approved 2026-09-03]`: loops ship inside their own gates — *"a fold, a ribbon,
a card carries no plan file."* Under this join key, work with no plan file can carry no cascade state,
so those two rulings cannot both hold as written. **Three readings are possible and only Paul can pick:**
(a) *feature* means plan-bearing work and loop work is out of scope; (b) loop work now needs a plan file;
(c) loop work gets a lighter stamp. **I decline to choose — it turns on what he means by "feature," which
is a content call.**

---

## 3 · WHERE THE STATE IS READ — an existing line, extended. No new tool, no new file, no new block line.

**`tools/check-backlog-ready.py`.** It is already in `CLAUDE.md`'s session-start block, already prints
one line of in-flight state, already silent at zero, already flags-never-edits, already Paul-gated on
every judgment. Extend that line:

```
🧭 In flight: 2026-09-05-onboarding-PLAN.md @ qa · gates ①✓ ②· ③·
```

**Four reasons this siting rather than a new tool:**

1. **It is where the identical question is already answered** — *does a row that CLAIMS readiness have
   the trail behind it?* A gate stamp is the same claim one altitude down.
2. **`check-cycle-map.py` globs `check-*.py` and requires every match to be named in
   `MOM-CYCLE-MAP.md`.** A new `check-cascade.py` goes red on delivery. Extending an existing tool costs
   nothing here.
3. **It inherits the anti-nag property by construction.** A feature parked at gate 1 for a month prints
   `①✓ ②· ③·` — a **state**, not an alarm. Nothing computes gate age; nothing may.
4. **It is a non-AI door.** *"Which gates has this feature cleared"* is answerable without a model.

⛔ **IT DOES NOT FIRE A LAP, AND THAT IS THE LOAD-BEARING CONSTRAINT.** `MOM-CYCLE-MAP.md`: *"The loop
rests. HER INPUT is what fires it. Not a schedule, not a backlog, not our shipping cadence."* This
touches nothing in `mom-cycle-status.py` and does not go near `position()`. It is a **pickup-time read,
disposed at the lap's opening gate sweep** (act · fold · snooze · kill) — the exact siting
`check-backlog-drift.py` argues for at length in its own docstring, reused rather than reinvented.

### 3a · The derivation rules — all mechanical, none a judgment

1. A `gates:` pointer whose file does not exist → **VOID** (the existing `seats:` rule, verbatim).
2. `derived.env` ≠ the environment the cascade declares for that gate → **VOID**.
3. `derived.servedSha` is not an ancestor of the sha being shipped → **VOID**. If the sha no longer
   resolves (rebase), fall back to `servedSubj`; if that also misses, read **UNVERIFIABLE**, never valid.
   **Fail closed** — the repo's standing posture.
4. Gate N is valid only if gates 1..N−1 are valid on an ancestor sha. Ordering, not ranking.
5. `stage: shipped` with no valid gate 3 → **FLAG** (a claim without a trail).
6. **Everything else prints as state, never as a flag.** An unwalked gate is not a defect.

Rule 6 is what keeps this off the permanently-red list. **Coverage is counted, never graded.**

---

## 4 · THE CLOUDFLARE ACCESS PROBLEM — narrower than stated, and mostly already solved

### 4a · Measured tonight, by execution

- `python3 tools/qa-walk.py https://fernwood-qa.pages.dev/viewer.html` → **exit 0**, title `Fernwood`,
  15 main cards, 8 tiles, `herConditions()` **clean**, HIGH 0. **A synthetic walk of QA through Access
  works right now**, using `.private/cf-access-service-token.json` via `tools/qa_access.py`.
- Tokenless GET of the same URL → **HTTP 200** at
  `fernwood-qa-pages.cloudflareaccess.com/cdn-cgi/access/login/…` — a login page, not an error.
- `https://fernwood-qa.pages.dev/onboarding/` **with** the token → 200, the real onboarding document.
- The mechanism is not improvised: `.plans/2026-09-03-c4-environments-PLAN.md:12` records Paul creating a
  **Service Auth policy literally named `qa-walk`** on 2026-09-04, and `deploy-worker-qa.yml:148` already
  passes `CF_ACCESS_CLIENT_ID`/`SECRET` in CI. *(Whether those repo secrets are set is **UNVERIFIED** —
  `gh` is unavailable in this sandbox. The 09-04 stage-note says they were Paul's to set and unset then.)*

**So the correct statement of the gap is narrower than "a persona cannot walk QA":**

> The **deterministic runner** reaches QA today. What cannot reach QA is the **agent-driven interactive
> browser** (the Playwright MCP), which opens pages with no `extraHTTPHeaders` and lands on a 200-status
> login page. Gate 1's persona is a multi-step *journey*, and that is the half that ran on lab.

### 4b · ⛔ And lab is a worse gate-1 origin than anyone has stated. Measured:

```
https://fernwood-lab.pages.dev/                     → 200, 19,621 bytes, sha256 d7a51f91b7b6
https://fernwood-lab.pages.dev/viewer.html          → 200, 19,621 bytes, sha256 d7a51f91b7b6
https://fernwood-lab.pages.dev/onboarding/          → 200, 19,621 bytes, sha256 d7a51f91b7b6
https://fernwood-lab.pages.dev/nonexistent-abc123   → 200, 19,621 bytes, sha256 d7a51f91b7b6
```

**Every path on lab returns the same document with HTTP 200.** Three consequences, all structural:

1. **A routing defect is undetectable on lab.** X and not-X produce the same observation.
2. **There is no `lab` branch** (`git branch -a`: `main`, `staging` only), **no `deploy-worker-lab.yml`,
   and no `qa-build.json` on lab.** So `derived.servedSha` — §1b's load-bearing field — **cannot be
   resolved for any walk that runs on lab.** A gate-1 stamp earned there is unverifiable by construction.
3. I nearly recorded lab's `viewer.html` as a viewer because the response *opened* like one. **Match the
   payload, not the container** — the first byte range of the login page and of the onboarding page both
   read as plausible HTML.

**This is the strongest available argument for running gate 1 on QA exactly as Paul ruled it.** I am not
proposing to move a gate; I am reporting that the environment it fell back to cannot produce the evidence
the gate claims.

### 4c · Options, and one recommendation

| | option | verdict |
|---|---|---|
| **A** | **Scripted journey runner carries the existing service token** — extend `qa-walk.py`'s exact pattern (`qa_access.headers()` → Playwright `extraHTTPHeaders`) to drive the onboarding steps | ✅ **works today, proven above.** No new secret, no new policy, CI path already written. Cost: scripted, so it finds only what it was told to look for |
| **B** | **Playwright MCP `--config` with `browser.contextOptions.extraHTTPHeaders`** (schema confirmed in the installed package's README, line ~583) | viable, and it restores the un-primed agent walk on QA. ⚠️ **headers are not host-scoped** — the service token would ride to every host that browser visits. Needs `--isolated` and a QA-only launch |
| **C** | **`--storage-state` warmed once by a token-bearing request**, carrying the `CF_Authorization` cookie | ⭐ **cookies are host-scoped by construction**, so no cross-host leak. Cost: it expires, and a stale state fails to a 200 login page |
| **D** | An Access bypass for the onboarding path or a wildcard | ⛔ weakens a gate Paul installed 30 hours ago. Not recommended |
| **E** | Keep gate 1 on lab | ⛔ §4b. It cannot produce `servedSha`, and every URL returns 200 |

> ### ⭐ RECOMMENDATION
> **A now, for the deterministic half — it is proven and costs nothing.** Then **C over B** for the
> un-primed agent half, on the host-scoping argument alone.
>
> ⚠️ **B and C are changes to the Claude stack, not to the work.** By charter they route to `/team-audit`
> and `engineering-partner`; I name the options and the axis, and do not pick the implementation.
>
> ⛔ **One requirement holds under every option, and it is not optional.** The Access login page returns
> **200**, and `qa-walk.py`'s wrong-document guard keys on `.main-card` — of which `onboarding/index.html`
> has **zero** (`grep -c "main-card"` → 0). **That guard does not transfer to the onboarding page.** A
> journey runner must assert its own identity marker — `<title>Your place</title>` and `#s1`–`#s4` — or a
> tokenless run will walk a login page and report clean. This is the 2026-09-01 GitHub-404 incident with
> a new door.
>
> **Falsifier for the recommendation:** if option A's scripted runner produces zero findings across three
> journey changes while a human walk of the same flow finds any, the script is testing its own
> expectations and the un-primed half is the load-bearing one — invert the priority.

---

## 5 · HOW THE TRACKER ITSELF GETS FALSIFIED

*"A gate that is never seen to fail is not a gate"* applies to this mechanism first.

| # | falsifier | what would be observed | consequence |
|---|---|---|---|
| 1 | **the stamp is a checkbox** | a `gates:` line hand-written with no artifact file, and the check reads green | the derivation is decorative — **delete it and keep the prose stage-note** |
| 2 | **stale-sha carry-forward** | gate 1 stamped on sha A; sha B ships with B not a descendant of A; nothing voids it | rule 3a·3 is not implemented as specified |
| 3 | **it became a nag** | anything prints on a repo with no in-flight plan | silent-at-zero broke; revert |
| 4 | **it is making judgment calls** | Paul overrides a cascade verdict **twice** | strip every verdict; print evidence only. *(A reversal is my defect, not his inconvenience.)* |
| 5 | **the gates are ceremony** | after N features, every cascade passes all three first time with zero findings | the cascade is theatre under this topology — **delete rather than tune**, per C4 §8's own posture |
| 6 | **the reading site is wrong** | a SURFACE commit reaches Mom's origin with no valid gate 3 and nobody noticed at pickup | move the read, or the block is not being read |

**Proof standard, non-negotiable and already this repo's:** every rule in §3a ships with a `--selftest`
case **proven by mutation** — a stamp with a deleted artifact, a stamp with `env: lab` against a QA gate,
a stamp on a non-ancestor sha, and an artifact whose sha no longer resolves (must read UNVERIFIABLE, not
valid). A check that has only ever passed has proven nothing.

### ⭐ The register's own honesty line, to be carried from day one

> **Gate 1 is PROVEN at n=1** — the 2026-09-05 walk caught two real defects (a duplicate address row from
> localStorage-only state; `personId: null` on a credentialed answer) plus one feasibility defect in the
> gate itself. **Gates 2 and 3 have never run and are UNPROVEN.** The first cascade that passes all three
> on the first try is *unproven*, not *validated*, until one of them has caught something.

---

## 6 · WHAT I DELIBERATELY DID NOT DESIGN, AND WHY

1. **What a gate passes ON** — the acceptance clauses per feature. That is content. The `accept:` block
   (09-03 proposal §3a) is the right home and is still unruled.
2. **Which features need which gates.** Paul said *"each and every."* §2 records the contradiction with
   C4 §9 Q3 and leaves the reading to him.
3. **A clock, a cadence or a nag for the cascade.** Deliberate. `check-journey-walk.py` (09-04 audit
   §B.5) is a clock for *the walk*, fired by the journey set changing; the cascade needs none, and adding
   one would convert shipping into a backlog-driven cadence — the exact thing `check-backlog-drift.py`'s
   docstring refuses.
4. **The `personId: null` fix** (§1d). It is the capability model, which is Paul's.
5. **Gate 3's environment.** ⚠️ **Contradiction reported, not resolved:** the three-environments plan's
   own § Target end state table lists three environments with prod = `est-3c9f1a`, while its cascade
   table puts gate 3 at `home` = `est-e6696a`, and `worker/wrangler.toml` declares **four** environments
   (`production` `est-3c9f1a` · `qa` `est-qa0001` · `lab` `est-lab0001` · `home` `est-e6696a`). Which one
   "Mom" means is a migration call.
6. **A new stage word, a dashboard, a status column or a second register.** Everything above is a
   pointer, an artifact a runner wrote, and a line on a tool that already prints.
7. **Gate 2's substance.** Paul's judgment is not a checkable artifact and I will not model it as one.
8. **Anything inside the Playwright MCP.** §4c B/C route to `/team-audit`.

---

## 7 · SMALLEST FIRST VERSION — useful even if everything else here is rejected

> **Write `.plans/2026-09-05-onboarding-PLAN.md`** (header already drafted, 09-04 audit §B.6) **and paste
> tonight's two gate-1 findings into it as one `- stage-note:` line.**

That single act gives tonight's release an identity, gives its findings a home that is joined to
something, and makes `qa-divergence.py --check` able to see the onboarding SURFACE commit. It needs no
tool, no ruling and no build. **Everything else in this file is second.**

Ordered after it: (1) option A's runner, extending `qa-walk.py`; (2) the `gates:` key and §3a's rules in
`check-backlog-ready.py`, with the mutation selftest; (3) §4c's un-primed half, via `/team-audit`.

---

*Every repo claim above was read in the named file or produced by executing the named command at
~2:00 AM ET on 2026-09-05. The four network measurements in §4a/§4b are live reads of the QA and lab
Pages origins. **UNVERIFIED and marked as such:** whether `CF_ACCESS_CLIENT_ID`/`SECRET` are set as
repository secrets (`gh` unavailable here) — check by a workflow run, not by re-reading the workflow.*
