# Handoff: fernwood-onboarding-link
<!-- generated 2026-09-05 ~12:55 AM ET · sources: Tate-Tracker@e86d902, ~/.claude@5455d49, fernwood-private@48b2798 · RECEIVER: verify shas vs HEAD before trusting any status below -->

## 1 · Mission
Get to a **link Paul can send Mom tonight** — she opens it cold on her phone, the app knows who she is, it asks her one thing (her address), and it tells her what happens next.

## 2 · Read first (point, don't re-derive)
- `.plans/2026-09-04-roles-and-access-REQUIREMENT.md` — the ratified journey, and ⛔ the chooser blocker at the end. **Read the "IT DOES NOT BLOCK MOM" subsection before worrying about it.**
- `.plans/2026-09-04-three-environments-PLAN.md` — environment shape and its ordering rules.
- `VOCABULARY.md` **§3e (AUTHORITY)** — who may author a grant. Binds everything below.
- `fernwood-private/.user-research/2026-09-04-onboarding-journey.md` — the 9-stage journey. ⚠️ Written before Paul's restructure; stages 1–3 still hold, 4–9 were reordered.

## 3 · Next steps (ordered — the first three are verified blockers)
1. **`tools/grant-mint.py:295` — `--env` takes `choices=("qa","prod")`.** It cannot mint into `home`. Add it, and check how the namespace is resolved (line ~126 shells `wrangler kv ... --binding OBSERVATIONS`).
2. **`engine/viewer.template.html:6990` `PAGES_WORKERS` has no `fernwood-home` entry.** The map fails closed by design (`WORKER_BASE = ""`), so her page would reach no Worker. Add it, `python3 tools/build-viewer.py`, confirm `--check` byte-identical.
3. **No Pages project for `home`** — `wrangler pages project list` shows only `fernwood-qa`. Create `fernwood-home`.
4. **Client: accept a credential from the link.** Read a token from the URL, keep it (localStorage), send it as header `X-Grant`. ⭐ The server half is done and ratified — `worker.js:497` `GRANT_HEADER`, `grantFor()` hashes and validates.
5. **Three screens.** (a) she is recognised · (b) confirm the address · (c) what happens next. ⛔ **Not nine** — see §7.
6. **Mint her grant** (`grant-mint.py mint --person … --estate est-e6696a --env home --entry`) and hand Paul the URL. **Paul sends it. Nothing here sends anything** — the Worker has zero send capability.

## 4 · State & pointers
| env | Worker | estate | KV namespace | ceiling |
|---|---|---|---|---|
| lab | `fernwood-lab` | `est-lab0001` | `1e0bd883e9824388af66563775c96d56` | $3/day |
| qa | `fernwood-qa` | `est-qa0001` | `a0cf82b615c648ff972961c46ce42661` | $3/day |
| **home** ← Mom's | `fernwood-home` | `est-e6696a` | `79464451e3a7497594b17d8c60c7254d` | $10/day |
| frozen Fernwood | `fernwood` | `est-3c9f1a` | `100f2b95e4be4c088a0000f917cf987b` | none |

- All four namespaces distinct (verified). `home` holds exactly **one** key: `env-canary`.
- ⚠️ **`wrangler` needs `CLOUDFLARE_ACCOUNT_ID=ba5a4c09cc277515966e1b7dbb0779e1` exported** — namespace creation fails with a bare auth error without it, and wrangler warns its OAuth token is stale.
- Grant register: `~/Developer/fernwood-private/grants.json` — 2 rows, both on `est-3c9f1a`, both `entry:false vault:false`, no consent, no credential. View it with `python3 tools/access-map.py`.
- **UNCOMMITTED:** `.user-research/2026-09-04-condo-dweller.md` (untracked, predates tonight, not ours). **13 commits ahead of `origin/staging`, unpushed.**
- ⚠️ Local branch `main` tracks `origin/staging`. `prod` tracks `origin/main`. A bare `git push` reaches QA.

## 5 · Guardrails
- ⛔ **Never touch `main` / `origin/main` / the `fernwood` Worker / prod's KV.** Mom's live page is frozen and is the control dataset for the generated-vs-hand-built comparison.
- ⛔ **No condo canon in Tate-Tracker.** It is public and Pages serves every byte. Mom's estate is born in **KV**, through the flow — not authored in a repo file.
- ⛔ **Nothing may be decided for her.** No `instance/` file exists for `est-e6696a`, and that is correct. The flow must write her answers, never pre-fill "sensible defaults."
- ⛔ **The environment marker stays operator-only** (`?operator=1` → `fw-operator` in localStorage). It was briefly computed from the Pages project name, which would have shown her "· QA" in her own tab.
- ⛔ **AI boundary:** the administrator's eyes sit between the model and the estate's people, both directions. Nothing drafted reaches her except through Paul.
- ⛔ **Do not build the multi-estate chooser.** It cannot be rendered (one KV binding per deployment). Mom holds one grant in `home`'s own silo, so her chooser has one entry.
- **Bare `git push` only** — a long `&&` chain around it trips the permission classifier.
- Commit messages: `-F -` with a quoted heredoc. `-m` with `$(…)` or backticks is hook-blocked.

## 6 · Done when
Paul holds a URL that, opened cold on a phone with no prior state: recognises Mom without her typing a password, asks for her address, records it into `est-e6696a`'s silo, and tells her when to expect something back. Verified by **actually opening it**, not by a passing check.

## 7 · Un-sealed judgment (not yet on disk anywhere)
- ⭐ **The minimum is three screens, not nine.** Zones are impossible in round one — they are drawn on a registered basemap and there is no basemap for an address we do not have (Paul's own point). And once zones are out, colour / text-size / icon / interests / module-ranking follow: they are all things you choose *for a place*, and there is no place yet. Not hard — **premature**.
- ⭐ **The flow ends in a WAIT, not a place.** Fernwood had months of research behind it before Mom ever opened it; the condo has nothing. So the last screen is the most important one in the sequence and it exists in none of the 27 mocks.
- ⭐ **The rhythm is ask-one-thing → build → show her → ask the next.** That is Paul's "gamified unlocking," except honest: the next question is unlocked by us having actually built the last answer into her place. Satisfies never-surface-an-empty-module by sequence rather than by hiding.
- Paul set the cadence at **~3 days** and framed it as the interim of a vision with no wait at all. He also said *"if it is still three days in six months, the generator did not happen"* — treat that as a live measurement, not a turn of phrase.
- The acknowledgment ribbon is the natural mechanism for those updates during build-out — its rule is "refreshes on HER events," and during onboarding the updates genuinely are caused by what she gave.

## 8 · Trust status (per open item)
| item | status |
|---|---|
| The three blockers in §3 (1–3) | ✅ **hub-verified tonight** by reading the code and listing the Pages projects |
| Environment table, KV ids, canaries | ✅ **hub-verified** — every environment asserted `/health`, not printed it |
| The chooser cannot span silos | ✅ **hub-verified** — 56 `env.OBSERVATIONS` sites, one binding, declared once per env |
| "Mom is unaffected by it" | ⚠️ **model-reasoned, NOT executed.** Sound, but nobody has minted a grant into `home` and logged in |
| grants.json contents | ✅ verified via `access-map.py` |
| The 9-stage journey doc | ⚠️ **written before the restructure** — stages 4–9 are superseded |
| `wrangler kv` per-prefix delete | ⛔ **UNVERIFIED** — practice-steward flagged it; matters only for the weld work, not tonight |
| content-steward / practice-steward `VOCABULARY.md` diffs | ⚠️ **proposed, NOT applied.** Three audits under `~/.claude/agents/audits/2026-09-04-*` |
