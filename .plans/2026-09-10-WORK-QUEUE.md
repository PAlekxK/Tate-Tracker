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
| **Delete `nigel` and `aida`** | irreversible, and free — but still a deletion |
| **The C-phase migration** | copying estate rows across namespaces, retiring `bob`/`paul`, `ENV_NAME`, `legacy`'s data. Every step is irreversible and the plan already says step 5 is yours |
| **Close lap 5** | beat 11 is the release event. Nothing is released before it |
| **Ratify the `route:` key noun** | I chose it over the plan's `credential:` to avoid a double-booking, and you have not ruled. **Cheap to change now, expensive after A1** |

---

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
