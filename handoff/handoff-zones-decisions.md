# HANDOFF — ZONES, the design session: every decision, and where it lives

- **from:** the zones scoping session, 2026-09-07 evening (design lane of release lap 3, J-g)
- **sha:** `0436b78` was this lane's last commit; HEAD has moved under other lanes since
- **outcome:** zones moved **`concept → design`** with a journey artifact. ⛔ **Nothing shipped. No production
  change, no deploy, no schema migration, no paid call, no credential created.** That was the assignment.
- **register:** `BACKLOG.md` ▶️ NEXT · TIER 2 · rows **7** (the epic) · **8** (LEG 0) · **9** (Process B)

> ## ⭐ START HERE
> **`.plans/2026-09-07-zones-PLAN.md` §0 first.** Four things in that file's own body are **superseded and
> marked**, deliberately not edited away. Reading the body without §0 will mislead you.

---

## The twelve rulings — all Paul's, all verbatim in the plan's §3

| | ruling | where the consequence lives |
|---|---|---|
| **Z-1** | Zones is scoped **as a feature** — the breadth is the job | the plan |
| **Z-2** | It is an **EPIC**: near-term, long-term, and a standing research strand | §7 horizons |
| **Z-3** | ⭐ **v1 = zones × plants** | §6 |
| **Z-4** | The v1 **includes drawing**, Paul draws, **as a test instrument** | §6, journey §W |
| **Z-5** | ⭐ **Structure-first** — points and walls, then subdivide | §5 |
| **Z-6** | A **formatting/beautification step** — refine against the pixels | §5b |
| **Z-7** | Events/neighbourhood start as **LINKS** (membership by rule) ⚠️ **its own siting requirement is UNMET** | §3, and nowhere in code |
| **Z-8** | **Online research authorized**, standing | the two scans |
| **Z-9** | ⭐⭐ The **manual operator step is SCAFFOLDING** with a known expiry | §5d — a spending rule |
| **Z-10** | ⭐⭐ **Zones FIRST; the plant record does not travel** | §6b |
| **Z-11** | ⭐⭐ **THE CASCADE** — address → zones → plants *in* those zones | §6c |
| **Z-12** | ⭐ **Always know the next best question** — with the guard **READY ≠ PUSHED** | §6c-b |

## The six decisions — plan §9

| | outcome |
|---|---|
| **R-Z1** | ✅ **Resolved without a purchase.** The shadow-free lidar layer is already on disk, registered to identical bounds. ⚠️ Google Solar was mis-priced to Paul as $0.075 — there is **no Google credential in this repo**; the real ask is a Cloud project with billing |
| **R-Z2** | ✅ **RULED: free sources only.** County parcels, not Regrid. ⚠️ Free **solves the condo** (Fulton publishes a free REST layer) and **does not solve Fernwood** — no free Pickens GA layer was found, and only ~10 states publish statewide |
| **R-Z3** | ⛔ **WITHDRAWN with its premise** — the cross-project pattern was falsified at the project it came from. Never written to the library |
| **R-Z4** | ✅ **RULED: yes, scheduled.** The 23 zones are the **answer key**; the comparison is a named step. ⚠️ **A wasting asset** — it holds only while the ground matches the 2018–2023 imagery |
| **R-Z5** | 🅿️ **PARKED on Paul's word.** Where the v1 ships, given the condo is `garden: off`. **Do not re-raise as a blocker** |
| **R-Z6** | ✅ **RULED B + C + D** and routed into the LEG 0 plan. ⚠️ **LATENT, not live** — and **still unexercised**: the probe returned `HTTP 401`, so it is **UNCHECKABLE**, never "empty" |

## ⛔ Four things this session RETRACTED — read these before trusting anything older

1. **"The resident steward does not need retrieval."** Carried by **two** research passes, from real telemetry.
   **Paul falsified it:** she knows **location**; she does not know **identity, timing, or THE SET**. ⭐ *She is
   not lost — she is worried about missing one.* → plan §2, journey §R.
2. **"12 plants don't have a place yet, want to say where they are?"** — the line the plan called its best
   feature. **False in her world** (every plant HAS a place; **our record** has none), sentence two is **an
   ask** against 0-for-35, and the whole thing is **migration copy** — at Mom's blank instance there are no
   plants at all. → §0 ②.
3. **"Nothing she creates can be saved."** **False.** Five capture handlers touch no git and work at `home`
   today. **Exactly one create is broken** and it is a gate at the wrong granularity. → §0 ④.
4. **"The empty state lies at n=0."** **Wrong — I checked a string, not a screen.** At n=0 the card is hidden
   by Paul's own beat-3 ruling. ⛔ **The lie fires at n=1**, immediately after she contributes her first plant.
   → journey §S ③.

## The findings that will outlive the v1

- ⭐⭐ **A NAMED PLACE, GEOMETRY OPTIONAL** — reached **four** independent ways, one from production code
  (`digest_zones()` strips ~94% of `zones.json` and keeps name/type/status; the one shipped consumer of the
  zone record has been a **name index** since July).
- ⭐⭐ **The place is the PARTITION, not the answer.** *"For this job, what is the set, and have I done all of
  it?"* — not *"where is X?"*
- ⭐⭐ **The cascade closes the set at capture.** If she names the plants in a zone while standing in it, that
  zone's set is closed **per place, on a date, by the only person who can close it.** The first honest
  completeness denominator this project has had.
- ⛔ **The surface ANSWERS; it never SUMMONS.** With the carve-out that saves it: **the system may count its
  own ignorance; it may never count her outstanding work.**
- ⭐ **The v1 is an AMENDMENT to a shipped surface** — `renderThisMonthPlants()` already groups by care action,
  `This Month` is the default tab, and the jump strip (5-for-5) reaches it. Missing: the place partition and
  the honest gap.
- ⭐ **Structure-first is backed by the record:** The Path as a polygon produced **93.5 m² — 87% of ALL zone
  overlap — from ONE feature modelled as the wrong shape.**
- ⛔ **Two hypotheses are DEAD and recorded as dead:** gradient-magnitude confidence (livewire adheres to the
  strongest edge, which on a 33°-sun January frame **is the shadow**) and multi-frame shadow consensus (NAIP
  shadows do not move, they shorten).

## The standing rules this session added

- **`CLAUDE.md`** — ⭐ **an empty engagement record is not an absent demand.** *Before any finding about her
  behaviour becomes an organising claim, ask Paul what she has asked him for lately.*
- **`BACKLOG.md`** — ✅ the register rule **ratified and NARROWED**: *a **load-bearing** ruling that is not in
  the register is not in force.* ⛔ With its open debt named: `freeze.json` / `tools/freeze.py` were designed
  here and **never built**. ⭐ And its unwritten other half: **a ruling that governs an ACT is sited at the
  act; a ruling that governs a DECISION is sited in the register.**

## What is OPEN, and what is NOT

**Open — and only the first has a session waiting:**
1. **LEG 0 gets built** → `handoff/handoff-capture-write-path.md`. ⚠️ **Its first act should be finishing the
   R-Z6 probe** with `home`'s token via `/secrets` — it may rewrite the plan rather than patch it.
2. **The first walkthrough** — ⛔ **cannot be scheduled.** It starts when *she* asks. Wait for the next
   *"I'm fertilizing, what do I need"* and answer it **with the surface, together**.
3. **Content-steward DRAFTING is owed** — a review has run; the copy has not been written.
4. **Z-12 is a stance, not a design** — needs user-researcher + content-steward before anything is built.
5. **The n=1 defect is live** and the cascade makes it rare, not impossible.

**NOT open — do not re-raise:** Z-ACK (Paul thanks her in person; ⚠️ **that closes a SURFACE, not
attribution** — the provenance chip stays) · R-Z5 · R-Z3 · the Regrid purchase · the 23 zones migrating.

## ⚠️ Repo conditions

- **Multiple lanes live.** Scope every commit: `git commit -- <path>`. `guard-shared-tree` blocks a bare
  `git add -A` and blocked this lane once, correctly.
- ⚠️ **`worker/worker.js` and `worker/digest.json` were modified by another lane** at the time of writing —
  the same file LEG 0 touches.
- ⛔ **Do not touch `.plans/2026-09-07-lap3-PROCESS-AUDIT.md`.**
- **QA serves `fbd5072`, 50+ commits behind HEAD, app surfaces changed.** Nobody walks anything until
  `python3 tools/pages-deploy.py --env qa`.
- ⚠️ **A green `build-viewer.py --check` is not a working page** — it compares bytes, it does not parse JS.

## ⭐ The method lesson, because it cost five corrections

Five claims were reported as verified and were not. All the same shape: **the adjacent claim was checked and
reported as the one that had been asked.** The string exists → *"the screen shows it."* The search returned
results → *"the county publishes it."* The response parsed → *"it is empty"* (it was a **401**).

> **A probe put it better than I did: *true of the layer queried, false of the question asked.*** Healthy
> service, right bbox, well-formed response, worthless answer. **Only a positive control catches it.**

**Three of the five were caught by seats, not by me.** Budget for that, or install the control.
