# Work queue — the Journal, tenancy, and the road to one production environment

Written 2026-09-10 at Paul's ask: *"do we have a queue you can queue up… plan everything else we're
gonna do that you can ideally do independently."*

⭐ **The organising split is not by topic, it is by WHO CAN CLOSE IT.** Most of what remains I can
drive alone. A short list cannot be driven alone at any speed, and mixing the two is how a queue
stops being trustworthy.

## 0. Where things actually stand tonight

| | |
|---|---|
| **Mom** | signed up 12:24 PM ET, got in, no door failure after. **First completed household signup in the project** |
| **Bob** | invite **unspent**. Everything that touches the credential path stays behind him |
| **routes** | 230 grants routed, every readable namespace, zero conflicts |
| **`grantFor()`** | routes — **deployed to `lab` ONLY**. `home` · `bob` · `paul` · `qa` still on `36c82bf` |
| **falsifier** | PASSES on lab. Fixtures **still live** in lab's KV (deliberately — it is a standing test) |
| **the Journal** | W1 · W2 · W3 done. A young household's Journal **builds and knows where it is** |
| **lap 5** | Paul's caveated preliminary pass. Gate ① 🔴 0/4 seats. QA 7 commits behind |
| **nigel · aida** | namespaces **empty, never used** |

---

## 1. ⭐ WHAT I CAN DRIVE ALONE — in the order I would do it

Each is reversible, none touches a live request path, and none reaches a person.

### Lane A — the Journal (finish what is started)

| # | item | why now | depends on |
|---|---|---|---|
| **A0** | **derive a property from an onboarding address** — coordinates · elevation · zone · frost dates · watershed, every value marked `inferred` | ⛔ **step 0, not step 7** — `digest_core` refuses a record with no place, so nothing downstream builds without it. `neutral-canon/property.json` already declares the contract | — |
| **A1** | **publish `<estateId>:digest` to KV**, per estate, with a `--check` that says whose record is where | additive; nothing reads it yet | A0 |
| **A2** | **Worker reads canon per request** — `canonFor(env, scope)`, fail-closed; retire `canonIsThisEstate` and **delete** `CANON_FOREIGN_OK` | the cutover. **Prove on lab with two estates first**, exactly as step 3 was | A1 |
| **A3** | **`attributeTo(turn, grant)` on conversation turns** — the household history, per-person | `[paul-ruled]` both members see history and each question records who asked. The door exists with **zero callers** | A2 |
| **A4** | **the 60 place literals** in the model prompts | the long tail; authoring, not plumbing | A2 |

### Lane B — tenancy (the paused work)

| # | item | why now | depends on |
|---|---|---|---|
| **B0** | **finish the `scopeOf(env)` classification** as a reviewable table, then convert **read-only handlers first, writers last** | the code's own ordering rule (`worker.js:3783`); `assertScope` throws on a forgotten conversion, never a wrong one | — |
| **B1** | ⚠️ **carve-out:** `library:*` and `cache:today-line` **must not convert before A2** | converting them early lets a foreign estate read Fernwood's library | A2 |
| **B2** | **`hostAgrees()` / `FAMILY_HOSTS`** demoted to an ordinary CSRF control | with one origin it no longer carries tenancy | B0 |
| **B3** | **`POST /api/estate`** — mints the founder's **own** estate only, structurally incapable of minting for a second person | that is where G2 lives | B0 · A1 |
| **B4** | **the `/homes/` picker** | — | B3 |

### Lane C — hygiene I should just do

| # | item |
|---|---|
| **C0** | reconcile the uncommitted `cycle/release/cycle-state.json` |
| **C1** | **copy the condo backup somewhere durable** — it is session scratch and *will* vanish |
| **C2** | deploy QA to HEAD so it stops drifting behind (it is 7 commits back and no app surface has moved) |
| **C3** | teach `grant-mint.py` to write the router row at mint, so the backfill never has to run twice |

---

## 2. ⛔ WHAT I CANNOT CLOSE ALONE — and why each one is genuinely yours

| item | why it is yours |
|---|---|
| **Deploy `grantFor()` beyond lab** | **Bob's grant is unspent.** The credential path is the one whose failure locks a person out rather than degrading. Your call when, not mine |
| **The consent checkbox WORDING** | it reaches a person. This repo's rule is that authored content is human-confirmed before it ships. I can build the mechanism and draft the line; I may not ship the words |
| **Correct `p-paul @ est-e6696a`** | the register says `relationship: ["owner"]` at an estate **Mom** owns. Today's ruling says your access comes from her invite. Fixing it is a claim about rights |
| ~~**Delete `nigel` and `aida`**~~ | ⛔ **KILLED 2026-09-10 — DO NOT RE-PROPOSE.** The justification (*"namespaces empty, never used"*) was **wrong**. Paul named his four beta testers: **Mom · Bob · Aida · Nigel** — *"Mom has already set up her house in production, and then I want to share with Aida and Nigel next."* Their namespaces are empty because **they have not been invited yet**, not because they are dead. Recorded visibly rather than dropped, so the same stale reading cannot mint this row again |
| **The C-phase migration** | copying estate rows across namespaces, retiring `bob`/`paul`, `ENV_NAME`, `legacy`'s data. Every step is irreversible and the plan already says step 5 is yours |
| **Close lap 5** | beat 11 is the release event. Nothing is released before it |
| **Ratify the `route:` key noun** | I chose it over the plan's `credential:` to avoid a double-booking, and you have not ruled. **Cheap to change now, expensive after A1** |

---

## 2b. ⭐ THE FOUR HOUSEHOLDS — and the register is inconsistent in BOTH directions

⚠️ **CORRECTED 2026-09-10 — IT IS FIVE, AND PAUL IS ONE OF THEM.** `[paul-stated]` *"we can count
my user account and that's the level we should be looking at it — my user account, like Mom, Bob,
Aida, Nigel, are all users and owners."*

⛔ **What this row said before, and why it was wrong:** *"the beta is Mom · Bob · Aida · Nigel. Paul
is not one of them (`p-7f3a2c` carries `excludeFromEngagement: true` — he is the builder)."* That
flag is **telemetry scoping, not roster membership** — it keeps his own taps out of engagement
counts, and I read it as excluding him from the beta. Recorded rather than rewritten because the
scoping session found the same conflict independently and filed it as a card, so the wrong version
has already been read by someone as authoritative.

⭐ **AND THE UNIT IS THE USER, NOT THE ESTATE.** Every artifact in this repo counts estates, envs and
namespaces; Paul counts **people**, and says each of the five is *a user AND an owner*. The question
is therefore not *"do five estates exist"* but *"does each of these five people own a household that
works."*

| owner | estate | person record | state |
|---|---|---|---|
| **paul** | `est-d93508` (condo) | ✅ `p-7f3a2c` · account `pkirsch` = `p-yjnw9lt41nww` | ✅ owns an account and a household |
| **mom** | `est-e6696a` | ✅ | ✅ **signed up today**, empty by design, rebuilding |
| **bob** | `est-9a74df` | ✅ `p-2f4735` | invite out, **UNSPENT** — the credential path must work when he spends it |
| **aida** | `est-92e588` ✅ | ⛔ **NONE** — zero mentions in `tools/people.json` | estate without a person |
| **nigel** | `est-76012d` ✅ | ✅ `p-5cf094` | person without a grant |

⚠️ **And one note was stale in the alarming direction.** `people.json` said of nigel *"HAS NO ESTATE
YET — there is no `nigel` env in worker/wrangler.toml"*. There is one, since `c1ae9bb` the same day.
Corrected 2026-09-10. **A register that misreports in either direction is the instrument problem this
repo keeps paying for** — the stale note would have had someone provision an estate that already
existed.

⭐ **NIGEL IS THE MOST VALUABLE THING TO BUILD TOWARD.** He is the only household that would go
end-to-end through the new path — a link, onboarding, an estate created from nothing — which is
exactly the goal state. That makes **B3 (`POST /api/estate`) critical path, not a late item.**

⛔ **Do not provision or invite anyone.** Inviting is outbound and Paul's. Build the path.

## 3. WHAT I WOULD DO NEXT, if you want one answer

**A0 → A1 → B0.**

A0 unblocks the whole Journal lane and is the thing that makes a new household real rather than
theoretical. A1 is additive and safe. B0 is the largest remaining body of work and it can proceed in
parallel with the Journal because its risky half (the library carve-out) is explicitly gated on A2.

⚠️ **And one thing I would NOT do next, despite it being tempting:** convert the writers in B0. The
code's own rule puts them last for a reason — a forgotten read is a 404, a forgotten write lands in
the wrong household silently.

## 4. THE STANDING RISK, stated once

**Isolation is still enforced by separate hardware.** `grantFor()` routes on lab only; every real
household is still one-estate-per-deployment. Nothing in this queue changes that until **A2 + B0**
ship together — and until they do, the falsifier's pass is a statement about lab, not about
production.
