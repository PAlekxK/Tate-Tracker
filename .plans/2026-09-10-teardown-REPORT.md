# Teardown — lap 7 row E · 2026-09-10 evening

<!-- teardown lane (a fork of the coordination window) · Paul's word in the coordination window: "Yes. Go on the
     teardown." on the named list; PAK/Homey added by his later word, relayed with the quote by the coordinator:
     "Yep. PAK/Homey can be torn down." · every deletion VERIFIED at Cloudflare after the act (the 4f7c04f procedure)
     · this file names ids, keys and counts — never an address, never coordinates -->

**Three rules held throughout:** delete only what is PROVABLY on the list, verified by reading the row's own
content (a key prefix and a personId that agree), never a username pattern · one unprovable row stops that sub-run
and prints REFUSED · nothing on the KEEP list or in an unnamed env was touched. Envs touched: `bob` (destroyed),
`qa` (keys). `lab` read only. `fernwood` (legacy), `home`, `paul`: never opened for write.

## 1 · The `bob` deployment — DESTROYED, verified

| what | pre-deletion reading | act | verified at Cloudflare |
|---|---|---|---|
| Worker `myhome-bob` | `/health` 200 before | `wrangler delete --name myhome-bob` exit 0 | origin → **404, error 1042** (control: a never-existing name → 404); scripts API → 404 |
| KV `22250acec6fe42e696fe7dc7936b6a2d` (est-9a74df) | **9 keys, `wrangler exit=0`** — NOT empty (nigel/aida were) | `kv namespace delete` exit 0 | **absent from `kv namespace list`** (5 remain: legacy, qa, lab, home, paul) |
| Pages project `myhome-bob` | serving | `pages project delete --yes` exit 0 | `myhome-bob.pages.dev` → **530, error 1016**; absent from `pages project list` (4 remain) |

**The nine keys, exported in full to `.private/teardown-bob-est-9a74df-2026-09-10.json` before the delete**
(gitignored; the only copy): `env-canary` · `est-9a74df:grant:d784a5f7…` (the founding-owner invite for
`p-2f4735`, issued 2026-09-10T15:36Z, unspent) · `route:d784a5f7…` · `est-9a74df:door:2026-09-10` (one
`door_failed` at 15:41Z, five minutes after the mint) · `est-9a74df:onboarding-metrics:2026-09-06 … 09-10` (five
days of arrival-screen sessions — someone reached Bob's onboarding page daily before any invite existed).

⚠️ **The invite `p-2f4735 → est-9a74df` DIED WITH THE NAMESPACE, unspent.** Paul's standing word: it can be
re-minted from a cleaner base. **The register row keeps `revokedAt: null`:** `grant-mint.py revoke` (dry-run
clean, then live) **REFUSED** — *"KV delete failed — revokedAt NOT written (the store is the truth the door
reads)"* — because the store no longer exists. That refusal is correct for a live store and wrong for a dead one;
the one writer needs a verb for *the namespace is gone* (`retire --store-gone`, register-only, stamping the
reason). ⛔ Not hand-edited. **Register/store divergence, for the backlog row.**

**Repo side** (this lane's commit; every other env block parses byte-identical before/after, checked with
`tomllib`): `worker/wrangler.toml` [env.bob] blocks (30 lines) → tombstone naming the ids and why ·
`tools/pages-deploy.py` PROJECT/BRANCH/ORIGIN/HOUSEHOLD lose `bob` · `tools/post-deploy.py` ORIGIN + health URL ·
`tools/deploy-worker.sh` health case · `tools/check-place-values.py` docstring example → `paul.json` ·
`tools/people.json` `p-2f4735` note appended: **the PERSON is HELD, not dropped; est-9a74df is RETIRED, NEVER
REUSED.** ⚠️ `instance/bob.json` was deleted by this lane and **swept into another window's commit `dcbc660`**
(a BACKLOG register commit that staged broadly) — cited, not redone. Selftests after: `post-deploy` ✅ 0 failures ·
`check-engine-manifest` ✅ · `check-place-values` 10/10 · `grant-mint` controls hold · `deploy-worker.sh` `bash -n`.
`pages-deploy.py` has no `--selftest` (it parsed and printed its usage with `{home,lab,paul,qa}`).

## 2 · The Midtown scratch instance — REFUSED (nothing tracked to delete; two live readers)

**What it is:** never a tracked file. No `instance/*midtown*` exists or ever existed (`git log --diff-filter=D`:
zero). "Midtown" survives in the tree only as prose (BACKLOG, plans, C7's stage-notes, one `place-claims.json`
classification note, one `check-data-inline.py` comment). The **scratch build** is `.private/condo-falsifier/`
(`condo.html`, `condo-hook.html`, `tools/`) plus `.private/condo-textsize-scratch.html`; `.private/condo-location.md`
is Paul's own note and is not a scratch instance.

**The 08-14 rule — what else reads it:** `tools/check-condo-falsifier.py` (`SCRATCH` defaults to that dir) and
`tools/place-claims.py` (`LEDGER = .private/condo-falsifier/uniqueness-ledger.json`) — and `place-claims.py
--check` is **in CLAUDE.md's pickup block.** Deleting the directory would break a pickup check. **Retiring
Midtown is therefore a REPOINT, not a delete:** both tools re-run against the Grant Park condo (`instance/paul.json`,
Paul: *"use the Grant Park condo to inform them"*), the ledger regenerated, then the scratch dir `trash`ed (never
`rm`, `~/Developer` is a protected root). That is a build-plan item, not a teardown act. **Nothing touched.**

## 3 · `pkirsch` at qa — DELETED, verified (Paul: *"pkirsch is production-only"*)

Found exactly one key naming it in 8,900+ qa keys: `est-qa0001:account:pkirsch` (personId `p-jhgwhxxz6zce`,
created 2026-09-08T03:43Z, administrator, a placed Grant Park row — **Paul's real account copy at qa**). Its
`tokenHash` resolved to `route:82398cb7…` → `{est-qa0001, p-jhgwhxxz6zce}` (prefix and personId agree); the matching
`est-qa0001:grant:82398cb7…` returned 404 (no grant row). No other key in the namespace carries that personId.
**Deleted 2, verified absent 2.** Neighbour `est-qa0001:account:pak` confirmed present and unread at that moment.

## 4 · PAK / Homey — DELETED, verified `[paul-ruled 2026-09-10, relayed by the coordinator: "Yep. PAK/Homey can be torn down."]`

Was on my KEEP list at spawn; the coordinator first ordered *do not touch in either direction* (obeyed — read as a
neighbour check only), then relayed Paul's ruling with the quote. By content: `est-qa0001:account:pak` → personId
`p-bcjyaldyts`, place 'Homey', `signupVia: invite`, `fixture: false`, tokenHash `5848493e…`; **`est-jfkeea`** is the
house that walk founded — `est-jfkeea:grant:5848493e…` (personId `p-bcjyaldyts`, `how: estate-found`, issued
22:24:44Z), `est-jfkeea:place` ('Homey', declared by the same person), `est-jfkeea:geocode:2af8122a…` (geocoded
22:24:43Z, the founding's own second). A scan of all **239 `route:` values** found exactly one pointing at either id:
`route:5848493e…`. **Deleted 5, verified absent 5; the `est-jfkeea:` prefix now lists `[]`.** `est-qa0002`'s one key
(a 09-04 vault fixture grant, not on the list) remains.

## 5 · The fourteen fixture houses — NOT DELETED by design; the evidence table

`household-fixtures.py --teardown` (report mode): **qa — fixture 0 · person 1 · unmarked 208 → REFUSED the whole
run.** lab — the same shape, 50 unmarked. Its own words: *"the fix is a stamp, not a looser match."* ✅ Correct.

| estate | env | creation record (what names it as founded by a synthetic) | sha | PROVABLE? |
|---|---|---|---|---|
| `est-rihhdp` | qa | `.private/synthetic-walks/owner/2026-09-10T180218/` REPORT.md names it; transcript ×2 | 318416a | ✅ walk-side record |
| `est-d7teqw` | qa | `…/mom/2026-09-10T180634/` REPORT.md names it; transcript ×2 | 318416a | ✅ |
| `est-bzr4gb` | qa | `…/wide-eyed/2026-09-10T180759/` transcript ×2 (REPORT.md does not name it) | 318416a | ✅ (transcript) |
| `est-pr9pwl` | qa | `…/strict/2026-09-10T180920/` REPORT.md names it; transcript ×2 | 318416a | ✅ |
| `est-otzfk2` | qa | `…/handover/2026-09-10T181052/` REPORT.md names it; transcript ×2 | 318416a | ✅ |
| `est-ofd6vk` | qa | `…/owner/2026-09-10T175555/` transcript ×2 (`buildBefore`=`buildAfter`=318416a); **REPORT.md carries WALK-REPORT-UNWRITTEN** | 318416a | ✅ founded, but an UNCOUNTABLE walk |
| `est-gndlvf` | qa | the two-pass sweep's house (`syn-sweep-0910`, account created 22:32:51Z); `.ux-reviews/2026-09-10-founding-flow.md:132,165` | 318416a | ✅ |
| `est-1nq5gr` … `est-zyn5py` (7) | lab | **none.** Named only by `walk-founding.py`'s measurement (*an estate holding keys wrangler.toml never declared was not minted by hand* — product-founded) and the coordination brief. Each holds 2–4 keys (`grant` · `place` · `geocode`); place rows carry `declaredBy: p-…`, `placeSource: self`, no run id | — | ⛔ **product-founded ≠ fixture.** "lab holds only synthetics" is inference from the environment, the class the rule forbids |

⚠️ In qa's namespace each of the seven holds **4–9 keys under its own `est-<id>:` prefix** (`grant` · `place` ·
`geocode`) — the account rows sit under `est-qa0001:account:*`. **Also present and NOT on any list:** `est-qa0002`
(1 grant, 09-04 fixture) · **`est-3c9f1a` — legacy Fernwood's estate id inside the qa namespace, 6 keys**
(`conversation` · `door` · `feedback` · `zones` · `zones-last-seen`). For the backlog.

### The stamp — what exists, and the two gaps `measured`
- ✅ **The stamp already ships.** `grant-mint.py --fixture-out` writes `fixture: true` on the invite row (`:459`);
  `handleAccountCreate` inherits it server-side (`worker.js:803`, *"fixture-ness is inherited from the invite,
  exactly as capability is"*); `household-fixtures.py` reads `FIXTURE_STAMP = "fixture"`.
- ⛔ **Gap 1 — the seats never inherit it.** All seven seat accounts read `signupVia: "open", fixture: false`
  (e.g. `syn-owner-3add-180218`): **J0 walks the OPEN door, so there is no invite to inherit from.** Proposal, server-
  decided not client-claimed: an env var on `qa`/`lab` only (`OPEN_SIGNUPS_ARE_FIXTURES = "true"`) that
  `handleAccountCreate` reads to set `fixture: true` on every open-door signup at those envs — the deployment
  decides, never the applicant; `home`/`paul`/legacy never set it.
- ⛔ **Gap 2 — founding does not carry it forward.** `handleEstateFound` (`worker.js:1387–1470`) contains no
  `fixture`: the founding `grantRow` and `writeEstatePlace` row of a fixture person are unstamped, so a founded
  house is not disposable even when its founder is. Proposal: copy `person.fixture` onto the founding grant row and
  the place row; `household-fixtures --teardown` then sweeps `est-<id>:*` prefixes whose founding grant is stamped.
- With both, tonight's fourteen become tool-deletable **going forward**; the fourteen that exist carry no stamp and
  stay hand-work, each against its row in the table above.

## 6 · Register — which rows should carry this (the backlog window is the one door)
- **Row E / THE FIFTH LENS teardown line:** bob DESTROYED (this report §1) · pkirsch@qa and PAK/Homey DELETED (§3–4)
  · Midtown REFUSED as a repoint (§2) · fourteen houses REFUSED with the evidence table (§5).
- **New:** grant-mint needs a store-gone verb (bob's row `revokedAt: null` against a dead namespace) ·
  `est-3c9f1a` keys inside the qa namespace · `est-qa0002` · the two stamp gaps · `est-ofd6vk` sits behind an
  UNWRITTEN walk report.
- `RELEASE_NOTES.md`: none — infrastructure, no person-facing change.

## 7 · Row 51 — two feedback records deleted by id `[paul-ruled 2026-09-11: "Delete both, by id"]`

**What:** `onboard-address-47neyq` and `onboard-addr-confirm-r3hog5` — PAK's two setup notes (personId
`p-bcjyaldyts`, 2026-09-10 22:24–22:25Z) carrying a real person's street address, which outlived the PAK/Homey
teardown (§4) because feedback is stored **day-keyed**, not per house. The address is not reproduced here.

**Pre-deletion reading:** `est-qa0001:feedback:2026-09-10` fetched `--remote`, exit 0, saved in full to
`.private/qa-feedback-2026-09-10.before.json`. **44 records.** Exactly two carried the target ids, each once;
both carried `personId = p-bcjyaldyts` — read from the fields, not inferred from the id.

**Act:** the list minus exactly those two written back with `kv key put --remote` (exit 0). Before the put, the
remaining 42 were confirmed byte-identical (JSON-normalised) to the before-list minus the two.

**Verified after:** re-`get` → **42 records**, neither id present, remaining 42 identical to before-minus-two.
`kv key list --prefix est-qa0001:` (8,589 keys) names **no per-record key** for either id. `feedback-dispositions.json`
holds neither id, so no disposition is orphaned (not edited — the backlog window's ledger).

**Generalised (row 51's shape):** an `est-<id>:` sweep cannot reach day-keyed feedback, so every fixture teardown
leaves its person's words behind unless the `feedback` channel is swept by personId in the same act.
