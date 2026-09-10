# Handoff: fernwood-multi-tenancy

<!-- generated 2026-09-10 12:06 PM ET · sources: Tate-Tracker@8edcc20, fernwood-private@ac1d414, Tate-Tracker origin/main@e9c9dac (legacy GH Pages) · RECEIVER: verify shas vs HEAD before trusting any status below -->

## 1. Mission
Build multi-tenancy in the Fernwood Worker so an estate is a **row an owner creates**, not a
deployment — per `[paul-ruled 2026-09-10]` — without breaking Mom's and Bob's live signups,
which went out this afternoon.

## 2. Read first
- `.plans/2026-09-10-multi-tenancy-PLAN.md` — **the whole design.** Four changes, the sequence,
  the falsifier, and the timing warning. Read it before touching code.
- `cycle/release/CYCLE-LOG.md` § `## Lap 5` and § `## ⏸ PARKED` — the release loop is open at
  **beat 8/12**; Paul chose to start multi-tenancy *before* closing it.
- `worker/worker.js:774-788` — `scopeOf` / `scopeFor` / `keyFor`. `scopeFor()` already exists
  and is already correct; it is called once (`:3788`) with its result discarded.

## 3. Next steps (ordered)
1. **Confirm Mom and Bob are through the door before touching `grantFor()`.**
   `python3 tools/watch-accounts.py` — their grants flip ⏳ → ✅ when spent. See §5.
2. **Backfill the router rows** for every existing grant: `credential:<sha256(token)>` →
   `{estateId}`. ⛔ The token is not recoverable from the register (it holds the HASH only), so
   the backfill must be built from the KV grant rows themselves — key suffix IS the hash, so
   iterate `<estate>:grant:<hash>` and write `credential:<hash>`. No token needed.
3. **Rewrite `grantFor()`** (`worker/worker.js` — grep `async function grantFor`; the line MOVED this session) to route: read `credential:<hash>` → read
   `<estateId>:grant:<hash>` → verify the row's own `estateId` agrees → return. A router row
   with no grant behind it is a 404, **never** a fall-back to the deployment's estate.
4. **Write the falsifier test** (plan § The falsifier) against two estates in ONE deployment
   on `lab` — before converting any call sites.
5. **Convert the 60 `scopeOf(env)` call sites** in reviewable batches. ⚠️ NOT mechanical: some
   legitimately mean the deployment (`/health`, `env-canary`, the digest guard, the chat budget).
6. `POST /api/estate` + the `/homes/` picker.
7. Migration (step 5 in the plan) is **Paul's call**, not a consequence of 1–6.

## 4. State & pointers
- Repo `~/Developer/Tate-Tracker` @ `8edcc20`. Register `~/Developer/fernwood-private/grants.json`
  @ `ac1d414`. Legacy GH Pages serves `origin/main` @ `e9c9dac` — **not** local `main`
  (they are ~650 commits apart; see memory `reference_fernwood_pages_serves_origin_main`).
- Estates live today: `est-e6696a` production/Mom · `est-9a74df` bob · `est-d93508` paul
  (Grant Park Condo, moved there today) · `est-qa0001` · `est-lab0001` · `est-3c9f1a` legacy
  (frozen) · `est-76012d` nigel and `est-92e588` aida — **Workers + KV only, no Pages origin.**
- ⭐ **WHICH CODE EACH WORKER IS SERVING — recoverable from nothing but this record.**
  `/health` returns `build_sha: null` on every environment (CLAUDE.md already records that gap),
  so no origin can answer this and the successor correctly reported it as unknown.
  **Deployed in the 2026-09-10 session, all carrying `worker.js` as of `36c82bf`** (open door +
  the widened capability gate): `home` · `bob` · `paul` · `qa` · `lab` · `nigel` · `aida`.
  ⛔ **`legacy`/production (`est-3c9f1a`, `fernwood.paul-kirschenbauer.workers.dev`) was
  deliberately NOT redeployed** — it is the frozen data control. **Verified by use at handoff:**
  `POST /api/account` there answers `401 unauthorized`, not the open door's `201` and not even
  `403 invite-required`, so it is running code older than the account carve-out. Leave it frozen.
- Working tree clean at handoff. **No uncommitted work.**
- Local backup of the condo move: `…/scratchpad/condo-backup/` (session scratch — treat as gone).

## 5. Guardrails
- ⛔ **Mom and Bob are live.** Invites sent 2026-09-10 PM; as of `8edcc20` neither had signed up
  (both grants unspent). `grantFor()` is the one path whose failure locks them out rather than
  degrading. Do step 3 behind them.
- ⛔ **Do not "fix" Garden Guru with `CANON_FOREIGN_OK=true`.** It returns `canon-not-this-estate`
  on every household because the bundled 605KB digest is stamped `est-3c9f1a`. That flag would
  feed Fernwood's canon — the address, the plants, the Bronco — into Bob's estate. The real fix is
  a per-estate digest plus per-env bundling.
- ⛔ **Do not flatten grant keys** to solve the lookup problem. That undoes C5 6a.
- ⚠️ `wrangler kv` defaults to the LOCAL simulator. **Always pass `--remote`** — a bare
  `key list` returns `[]` for a populated namespace and reads as "empty estate".
- ⚠️ `pages-deploy.py --env home` is behind gate ①, which is red. Other envs are not.
- Commit messages: `-F -` with a QUOTED heredoc. A backtick in a `-m` string is hook-blocked.
- Stage explicit paths; `git add -A` is hook-blocked (shared tree).

## 6. Done when
Steps 1–4 complete and the falsifier passes: two accounts on one deployment, each having created
their own estate, where every read one makes for the other's `estateId` returns 404 — and a grant
presented for estate A cannot name estate B by any route. Steps 5–7 are the follow-on.

## 7. Un-sealed judgment (NOT yet on disk elsewhere)
- **A `door_failed` landed on Bob's estate at 2026-09-10T15:41:16Z**, reason
  `unknown-or-other-estate`, `serverSide: true`, `deviceId: null`. Timing puts it inside the window
  where his grant was rotated from administrator to owner/member, and it PRE-DATES Paul sending the
  invite — so it is most likely self-inflicted, not Bob. **Not proven.** If it recurs after he
  clicks, that is the "you have no homes" failure and it is urgent. Check `tools/watch-door.py`.
- **The condo move went against the grain of where Paul is heading.** It was right for the live
  privacy problem (Mom could have read his notes once member reads widened), but under the target
  model Grant Park Condo returns to production. Do not treat `est-d93508` as settled.
- **The open door probably turns gate ① green** and was never tested: fresh synthetic walks were
  blocked because they could not get an unspent invite, and they no longer need one. Nobody has run
  the battery since. This may close lap 5 cheaply.
- **Nobody has ever completed a signup on any household estate.** Mom and Bob are both gate 1 on an
  unwalked path. Paul chose to send anyway, knowingly.

### Amended 2026-09-10 after grading the successor's readback

⛔ **THE CONDO BACKUP EXISTS. The readback says it checked "every session scratchpad" and that
`condo-backup/` is "not on disk" — that is WRONG, and it is the one factual error in an otherwise
accurate readback.** All four rows are at
`/private/tmp/claude-501/-Users-paulkirschenbauer/aee5db3e-3857-4788-9ff4-198ad094df4d/scratchpad/condo-backup/`
(verified by `ls` at handoff). It is session scratch and WILL vanish — but the readback's stronger
claim, *"there is now no second copy of those four rows,"* is false today. If a second copy is
wanted durably, copy it somewhere real rather than acting on either statement.

⭐ **Four findings from the readback that are BETTER than the plan and must survive it.** They are
recorded here rather than silently folded into the plan, because the plan is `[paul-ruled]` and
these are not yet:

1. **The backfill is per-namespace × 8, not one sweep.** The router row is deployment-scoped and
   "deployment" today means one of eight distinct KV namespaces; a router row in namespace A cannot
   find a grant in namespace B. **Therefore migration is not merely retiring envs — it is COPYING
   GRANT ROWS ACROSS NAMESPACES into production's store before the router can route them.** That is
   the step that touches live credentials and neither the plan nor the brief said it out loud.
2. **The backfill iterates the STORE, so a register-only row gets no router row and is silently
   uncovered** — `p-paul @ est-e6696a` is exactly that shape. Same shape as the `⚡ DIVERGENT`
   reading CLAUDE.md already records, and the same reason code as Bob's `door_failed`
   (`unknown-or-other-estate`). Not the same incident; not to be treated as cosmetic while building
   the thing that reads that store.
3. **`credential` is about to be double-booked.** `grant-mint.py` already uses `credential` as a
   FIELD inside the grant row (`{hash, issuedAt, issuedBy, revokedAt}`); the plan proposes it as a
   KV KEY noun. That is the collision `VOCABULARY.md` exists to catch. **Pick a different key noun
   before it is written 60 times.**
4. **`POST /api/estate` collides with `grant-mint.py`'s sole-writer claim and its two consent
   gates.** That tool calls itself *"the ONE writer of the grant register and the KV grant store"*
   and enforces G1 (founding-request consent) and G2 (administrator-reads consent) AT THE MINT, per
   `[paul-ruled 2026-09-03]` *"no watcher; enforce at the mint."* A server-side route either
   re-implements both in JS or bypasses them, and either way writes a grant the local register does
   not know about — structurally guaranteeing `⚡ DIVERGENT`. **The plan does not mention consent,
   `grants.json`, or G1/G2 at all. This is its thinnest part and it is change #2, not a corner.**

⚠️ **The readback also raises three live decisions the brief framed only as context** — whether lap 5
closes first, whether Paul keeps an administrator row on Mom's estate, and who mints under
`POST /api/estate`. All three are Paul's, and the third blocks change #2.

## 8. Trust status (per open item)
| Item | Status |
|---|---|
| Open door: no-invite signup → member | ✅ **human-cleared** — Paul ruled it; verified live, `201` + `capability: member` |
| Member = full use of own estate | ✅ **human-cleared** — Paul ruled the widened scope incl. feedback/conversations reads |
| Bob = owner/member (not administrator) | ✅ **human-cleared** — Paul ruled it explicitly |
| Cross-estate isolation holds today | ✅ **verified by use** — each grant is a 404 at the other's Worker |
| Condo move (byte-parity before delete) | ✅ **verified** — all four rows matched pre-delete |
| Legacy banner copy live | ✅ **verified by use** on palekxk.github.io |
| The `door_failed` is self-inflicted | 🚩 **model-flagged, NOT cleared** — timing only |
| Open door turns gate ① green | 🚩 **model-flagged, NOT cleared** — never run |
| `p-paul @ est-e6696a` admin row in register | 🚩 **model-flagged, NOT cleared** — store holds no such grant; whether Paul keeps admin on Mom's estate is his call |
| Nigel/Aida Pages origins impossible | 🚩 **model-flagged** — confirmed twice via wrangler, both orderings; dissolved by this build anyway |
