# Handoff: onboarding-journey-testing
<!-- generated 2026-09-05 ~5:20 AM ET · re-stamped ~5:35 AM after the final close-out commits ·
     sources: Tate-Tracker@0315796 (+1: THIS commit moves it, by construction), fernwood-private@ffc89d5, ~/.claude@f44c3e7
     ALL THREE REPOS WERE VERIFIED CLEAN AND FULLY COMMITTED AT THIS STAMP — `git status --porcelain` empty in each,
     Tate-Tracker pushed to origin/staging, the other two local-only by design (no remote, nothing to push).
     RECEIVER: verify shas vs HEAD before trusting any status below. A one-commit gap on Tate-Tracker whose only
     delta is this file is EXPECTED; anything more means work landed after the handoff and the status is stale. -->

## 1 · Mission
Stand up **iterative cycles of testing the onboarding journey** — logic and function proven *before it reaches Paul*. `[paul-stated 2026-09-05 ~5:15 AM ET]`: *"I really hope we can start running some iterative cycles of testing out the journey and its functionality, using the UX review skill — and call practice-steward to figure out exactly how to do it. Be sure that things are proved out from a bare-logic point of view and a functional point of view before it gets to me. And that should really be the full onboarding journey."*

## 2 · Read first (point, don't re-derive)
- `.plans/2026-09-04-three-environments-PLAN.md` **§ THE RELEASE CASCADE** — the three gates Paul ruled (synthetic persona → Paul → Mom). **This mission is gate 1, made repeatable.**
- `.plans/2026-09-05-release-cascade-tracking-PROPOSAL.md` — practice-steward's design for how a gate walk leaves *derived* evidence. ⚠️ **PROPOSED, not ruled.**
- `.plans/2026-09-04-process-wiring-AUDIT.md` **§A.3 + §B.5** — the E2E journey-test procedure already designed, including why it **cannot be filed as a `/ux-sweep` run** (its setup step forbids the acts a journey test requires) and the `check-journey-walk.py` sketch.
- `../fernwood-private/.ux-reviews/2026-09-05-account-creation.md` + `.json` (22 findings) — the current UX read of the flow.
- `onboarding/index.html` — the artifact. Four views, all comments are load-bearing rationale.

## 3 · Next steps (ordered)
0. **Verify the tree is clean before you trust anything** — `git status --porcelain` in `Tate-Tracker`, `../fernwood-private` and `~/.claude`. All three were **empty** at the stamp above. Anything dirty now landed after this brief was written, so reconcile it from git before acting on any status here. ⚠️ The two siblings have **no remote by design** — "unpushed" is not a defect there; "uncommitted" is.
1. **Ask `practice-steward` how to run this**, per Paul's explicit instruction — it already holds the cascade design. The question is the CYCLE: what fires a lap, what a lap does, what it leaves behind, and how gate 1 differs from a `/ux-sweep`.
2. **Separate the two proofs Paul named — they are different tests.** *Bare logic*: does every path resolve (bad grant · revoked · offline · duplicate submit · cleared storage · new device)? *Functional*: does a person walking it get where they're going? Do not let one stand in for the other.
3. **The journey runner needs its own assertion.** ⛔ `qa-walk.py` asserts `.main-card`, which `onboarding/index.html` has **zero** of — a tokenless run would walk the Cloudflare Access login page, which returns **HTTP 200**, and report clean. Assert `<title>My Home</title>` / `#s1`–`#s4`.
4. **Gate 1 belongs on QA, not lab** — `qa-walk.py` already passes through Access on the service token. ⛔ lab returns the identical 19,621-byte document for **every** path including `/nonexistent`, so a routing defect is undetectable and `servedSha` is unresolvable there.
5. **Then the account step**, which is the biggest hole in the journey: `.engineering/2026-09-05-account-credential.md` has the design (account row alongside the grant; `grantFor()` untouched). ⚠️ Ship the **A+ base size first** — activation research says the loudest new-phone failure is the words getting smaller, and login would get blamed for it.

## 4 · State & pointers
| env | Pages | Worker | estate | notes |
|---|---|---|---|---|
| lab | `fernwood-lab.pages.dev` | `fernwood-lab` | `est-lab0001` | onboarding deployed; **no Access**; Paul's gate-2 grant is LIVE |
| qa | `fernwood-qa.pages.dev` | `fernwood-qa` | `est-qa0001` | behind Access (`tools/qa_access.py`); onboarding is at **`/onboarding/`** |
| home | `fernwood-home.pages.dev` | `fernwood-home` | `est-e6696a` | **Mom's. Holds NO grant. Correct — she is gate 3.** |

- **UNCOMMITTED, not mine, needs a ruling:** `.user-research/2026-09-04-condo-dweller.md` is untracked **in the PUBLIC repo** — a privacy question, not housekeeping. `../fernwood-private/.grants.json.bak-20260905` is a backup I took before removing a phantom row.
- ⛔ **`est-e6696a` is now a PLACEHOLDER** `[paul-decided 2026-09-05]` — a fresh estate id is minted **when the real property record is authored**, not before.
- `~/.claude` has **no remote by design** — local-only, nothing to push.

## 5 · Guardrails
- ⛔ Never touch `main` / `origin/main` / the `fernwood` Worker / prod KV. Local `main` tracks `origin/staging`; a bare `git push` reaches QA.
- ⛔ **Nothing reaches Mom.** She is gate 3. The Worker has zero send capability; the invite is Paul's own act.
- ⛔ **Copy is authored content** — Paul's eyes sit between the model and the estate's people, both directions.
- ⛔ **No third-party request on page load.** The page currently makes NONE (webfonts were removed for exactly this). A map EMBED would break the "Paul is the only other person who sees it" promise; a LINK does not.
- Commit messages: `-F -` with a quoted heredoc. Bare `git push` only.
- ⚠️ `~/.claude` is shared — stage explicit paths, never `git add -A`.

## 6 · Done when
A gate-1 walk of the **full onboarding journey** can be run on QA on demand, leaves evidence a later reader can check without re-walking it, asserts the right document, and has been **seen to fail** at least once on a real defect. Paul sees the journey only after it passes.

## 7 · Un-sealed judgment
- ⭐ **Gate 1 already earned its keep and this is the argument for the cycle.** Its first run caught three real defects, one of which was introduced *by the fix for the first one*: keying the write on the credential alone made a corrected address a silent no-op while the page said "saved."
- ⚠️ **A gate that has never failed is unproven, not validated.** The cycle needs a mutation habit — plant a defect, confirm the walk catches it.
- ⭐ **The `--dry-run` defect is the shape to watch for elsewhere:** a flag that *claims* inertness while writing. Worth grepping other tools for the same pattern.
- ⚠️ **The keyboard ledger is measured for the CURRENT form only.** At 414×848 A+: first field 275–327 visible, ZIP 567–619 and the button 651–705 **below an iOS keyboard**. Fine for a form (browsers auto-scroll) — **re-measure when the account step lands**, because that screen may not be a form.

## 8 · Trust status
| item | status |
|---|---|
| The four views, walked end-to-end at 414×848 A+ | ✅ **executed**, incl. correction-lands and replay-dedups proven by mutation |
| A minted grant opens the door; another estate's 404s identically | ✅ **executed** against both QA and lab Workers |
| Zero third-party requests on load | ⚠️ **static analysis of the served bytes**, every element type — NOT a live request log (Playwright dropped) |
| Gate 1 must run on QA, not lab | ✅ practice-steward **measured** lab's identical-response defect |
| Cloudflare Access does not block gate 1 | ✅ **corrected** — `qa-walk.py` passes on the existing token; my earlier claim was wrong |
| The account credential design | ⚠️ **model-recommended, NOT built, NOT ruled.** Entropy objection is answered *structurally*; Paul has not ruled |
| The operations-vs-handover fork | ⛔ **UNRESOLVED and Paul's.** Gates every commercial number |
| `business-analyst`'s output | ⚠️ **the seat is UNSTAMPED** — its onboarding interview never ran; it says so on its own face |
| All copy on the page | ⚠️ **DRAFTED by a model, not approved.** Paul reads before anything is sent |
