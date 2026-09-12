# HANDOFF — the CAPTURE WRITE PATH · the DESIGN PASS (concept → design)

<!-- generated 2026-09-12 · source: Tate-Tracker@b10cc02f · main · CLEAN TREE
     RECEIVER: verify the sha against HEAD before trusting any status below.
     ⛔ Cite the SYMBOL, stamp the sha, and re-read the file you cite immediately before the
        commit — not only before the edit. A file:line here has a half-life measured in minutes
        when several lanes are live (measured under ten on 2026-09-11). -->

## 1. Mission — what this window IS

**You are the DESIGN PASS for the per-estate capture write path.** `[paul-picked 2026-09-12]`

`.plans/2026-09-07-capture-write-path-PLAN.md` sits at **`stage: concept`**, stamped
`ready: [paul-approved 2026-09-07]`. `check-backlog-ready.py --ladder` says the one thing standing
between it and a build is **a design pass (concept → design)**. **That is your whole job.**

⭐ **The readiness doc's §8 flags this row's real problem: *"Nobody's beat owns the pass."*** It has
been ready and unowned for five days. You are that owner now.

⛔ **You are NOT a build lane.** You produce a design-stage artifact. No feature code ships from here.

## 2. The windows — and which you are

| window | job | never |
|---|---|---|
| **coordination** — `tate-tracker` main | routes, sequences, holds the commit-phase freeze, runs laps | writes a feature |
| **backlog** (standing, LIVE — it opened you) | refines `BACKLOG.md` with Paul in real time; **SOLE WRITER of `BACKLOG.md`** | commits code |
| **this one — design pass** | takes capture-write-path from `concept` to `design` | ⛔ **writes `BACKLOG.md`** · ships feature code · stamps its own `ready:` |

⛔⛔ **DO NOT EDIT `BACKLOG.md`. A standing window is its sole writer and is live right now.** Row
changes you want (TIER 2 · 8, TIER 1 · 71) are **routed back to it**, not made here. This is not
bureaucracy — a plan written by a window that cannot file its own row is how the repo's orphan
problem started, and the backlog window files the pointer for you as a matter of course.

## 3. ⛔ READ FIRST — and the old brief is a TRAP

1. **`.plans/2026-09-07-capture-write-path-PLAN.md`** — the plan of record, 409 lines. Read it whole.
   Its §1 (why KV-only is not a durability downgrade), §3 (the 7-step sequence), §4 (what it does
   NOT do) and **`## What I could not verify`** are the live material.
2. ⛔⛔ **`handoff/handoff-capture-write-path.md` IS FIVE DAYS STALE AND ITS GATE PARAGRAPH IS FALSE.**
   It was written 2026-09-07 at `a95f4d2` and says *"carries `stage: concept` and NO `ready:` stamp…
   Stop at the stamp and hand back."* **Paul stamped it that same evening** and the `ready:` line is
   in the plan header now. **Read it only as history.** *(It is left in place rather than deleted —
   the strike is recorded, not silently swept.)*
3. ⚠️ **The plan contradicts itself on this exact point and nobody has fixed it:** its header carries
   `ready: [paul-approved 2026-09-07]` while a blockquote ~20 lines below still says *"THE `ready:`
   LINE IS DELIBERATELY ABSENT AND MUST STAY ABSENT."* **The header is right; the blockquote is
   stale.** ⭐ Fixing that contradiction is legitimately yours — it is inside your plan.
4. `BACKLOG.md` **TIER 2 · 8** (this row, corrected today) and **TIER 1 · 71** (filed today, and it
   widens your scope). Read, never edit.

## 4. ⭐⭐ WHAT MOVED TODAY — measured at `b10cc02f`, and it reshapes the sequence

The plan is five days old. **Three of its load-bearing claims were re-measured today by the backlog
window.** Do not re-derive these; do verify any you intend to build on.

### ⭐ A · The bindings are FORBIDDEN BY DESIGN — not missing. This is the big one.

`handleZoneSave` returns **503** before anything else when `GITHUB_TOKEN` or `GITHUB_REPO` is absent
(`worker/worker.js:5050–5052`). Measured bindings: **`legacy` holds them; `home`, `qa`, `lab` and
`paul` hold none.**

⛔⛔ **AND `wrangler.toml` REFUSES THEM BY NAME, PERMANENTLY, IN THREE PLACES, WITH THE REASON BESIDE
EACH** — qa `:40`, lab `:66`, home `:146` — because `GITHUB_BRANCH` defaults to `"main"`
(`worker.js:3232`, `:3281`), so **a token at any household would promote species straight onto Mom's
live branch.**

⭐ **What this does to your plan, and it is a strengthening, not a refutation:** §1's KV-only argument
was written as the *cheaper* path. It is now the **only** path — "commit to git when a token exists"
is **dead code at every household, permanently, by ruling.** ⛔ **So the KV durability question stops
being a trade-off and becomes load-bearing.** Which makes the plan's own unreached source the single
most important thing you owe (§5 below).

### ⭐ B · Falsifier 2 has effectively FIRED — by code read, and step 2 downgrades

The plan's falsifier 2: *"Before her first save, `home` would be served Fernwood's zones… If it
returns empty, I am wrong about the fallback and **step 2 downgrades**."*

**Measured:** `handleZonesGet`'s git fallback is gated `if (env.GITHUB_TOKEN && env.GITHUB_REPO)`
(`worker.js:5259`); `home` has neither; so a cold KV falls through to `data = { _meta: {}, zones: [] }`
(`:5267`). **She gets an EMPTY map, not Fernwood's 23.**

⚠️⚠️ **BUT THE PLAN ATTACHED A CAVEAT TO THIS RESULT AND YOU MUST RULE ON IT, NOT INHERIT IT:** it
says containment *"is held by the missing token, i.e. by the very thing step 1 removes — so a green
result is about the read path only and does not survive step 1."* ⛔ **That reasoning looks wrong to
the backlog window and is NOT being asserted as settled:** step 1 moves the gate inside
`handleZoneSave`; it does **not** grant a binding. `handleZonesGet` reads the same absent binding
after step 1 as before. **If that holds, containment is durable and step 2 downgrades further than
the plan allows. Adjudicate it explicitly — it decides whether step 2 exists at all.**

⭐ **The CLASS stays real either way:** the leak fires wherever those bindings DO sit beside a cold KV
— `legacy` is the one deployment that holds them. Step 2's per-env switch may still be right, aimed
at a different env than the plan aimed it.

### ⚠️ C · Falsifier 1 is STILL UNRUN and is NOT anonymous-cheap

*"POST each of the five capture endpoints against `home`"* — still not done. `GET /api/zones` at
`home` and `qa` returns **`401 {"error":"unauthorized"}`**: it needs a grant token, so it is a
gate-kit act, not a session's. **(TIER 1 · 74.)**

⛔ **This is the falsifier the plan says must run BEFORE step 1** — *"if more than `zone-save` is
broken, this plan's whole scope correction is wrong and it should be rewritten, not patched."*
**Name how it gets run; do not quietly proceed past it.**

⚠️ **And the trap that cost a probe:** `fernwood-home.pages.dev/api/zones` returns **HTTP 200 with the
SPA shell's HTML** — Pages serves `index.html` for unknown paths, so a status check against the wrong
host reads **GREEN** for an endpoint that is not there. *Match the payload, not the container.*

## 5. ⭐ THE ONE SOURCE THIS PASS OWES

The plan's own words: *"**Cloudflare's own KV durability/SLA page — NOT FETCHED.** My consistency
claims (60-second propagation; unsuited to write-heavy same-key workloads; suited to read-heavy
config-shaped data) are from search summaries… **If KV-only durability is going to carry a
household's record, read that page directly before the stamp.**"*

⭐⭐ **Finding A promotes this from prudent to REQUIRED.** KV-only is no longer the cheaper option
being weighed — it is the permanent architecture for every household. **Fetch
`developers.cloudflare.com/kv/concepts/how-kv-works/` directly and rule on whether KV alone may carry
a household's record.** If it may not, that is a finding worth the whole pass.

## 6. Seats — two are OWED, and the waivers are SCOPED

From the plan's own header — carry them, do not re-derive:

- **engineering-partner** → `.engineering/2026-09-07-zones-v1-path.md` (exists)
- ⛔ **ux-expert → WAIVED for steps 1–4, NOT WAIVED for step 5.** The honest-response field changes
  what the sync chip can say, and **the chip is Mom-facing.**
- ⛔ **content-steward → OWED, not waived, at step 5 only.** If the sync chip gains a state, its words
  reach Mom. **No copy is drafted in the plan.**
- **ai-advisor** → waived: nothing here invokes a model. ⭐ **Capture stays deterministic and AI-free
  by standing doctrine** — this plan moves only where a write LANDS, never what is written. **Do not
  put a model on this path.**
- **user-researcher** → waived: changes no journey.
- **practice-steward** → waived: a product defect, not a loop.

## 7. ⛔ Guardrails

1. ⛔ **Never edit `BACKLOG.md`** — the standing backlog window is its sole writer and is LIVE.
2. ⛔ **Never write your own `ready:` stamp.** Paul alone writes it. An agent stamping its own
   readiness is the one thing the gate exists to prevent.
3. **You may edit `.plans/2026-09-07-capture-write-path-PLAN.md`** — it is your plan of record, and
   moving it `concept` → `design` is the deliverable.
4. ⛔ **Do not deploy, merge, or push.** QA serves `87c7aae`, **150 commits behind HEAD**.
5. **An unchecked box is not open work.** Probe the world before acting on any status prose — today
   produced four fresh instances of documents over-reporting open work, including this plan's own
   handoff and the "nine needles" that were already fixed.
6. **You flag; Paul clears.** Never promote a model-read value to fact.
7. **Mom's words stay in `.private/`.**

## 8. Trust status — per claim you are inheriting

| claim | status |
|---|---|
| The plan is stamped `ready: [paul-approved 2026-09-07]` | ✅ **human-cleared** — in the plan header |
| Bindings absent at home/qa/lab/paul, and forbidden by design | 🔵 **model-verified**, code + config read at `b10cc02f`. Nobody has signed it |
| `handleZonesGet` serves EMPTY at `home`, not Fernwood's 23 | 🔵 **model-verified** (gate + binding list). ⛔ No POST was made |
| "Containment does not survive step 1" (the plan's caveat) | 🔴 **DISPUTED by the backlog window, UNSETTLED.** Yours to adjudicate — §4·B |
| Only `zone-save` is broken at a household | 🟠 **the plan's own scope correction, and its falsifier is UNRUN** |
| KV-only is durable enough to carry a household's record | 🔴 **UNVERIFIED — the source was never fetched.** §5 |

## 9. Done when

**The plan moves `concept` → `design`** with: the step-2 question in §4·B adjudicated · the KV
durability source actually read and ruled on · the two owed seats convened or explicitly scoped out
with a reason · falsifier 1's running named · and the plan's stale `ready:` blockquote corrected.

⛔ **Then hand back — do not build.** The `build` WIP band reads **1/1 with four declared
exceptions**; whether this takes a fifth or waits is **Paul's ruling** and is not pre-empted here.

**Route to the backlog window:** any row change you want on TIER 2 · 8 or TIER 1 · 71.
**Route to coordination:** anything that is a lap decision or a ruling for Paul.
