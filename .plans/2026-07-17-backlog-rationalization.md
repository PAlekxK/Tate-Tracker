# Fernwood backlog — rationalization & unification (intent-first)

**Date:** 2026-07-17 · **HEAD:** `b52ce03` · **Scope:** ALL backlog surfaces (BACKLOG.md + the CLAUDE.md "Backlog — raised" fragments + "Outstanding for Paul" + the Phases-D–G roadmap + fernwood memories). **Posture:** intent-first re-derivation — every disposition below is a PROPOSAL for Paul to ratify (kill/merge/defer are his call).

---

## The headline: Fernwood is now TWO products sharing one repo

This is the single most important thing the exercise surfaced, and it explains why the backlog *feels* like it's accreting even though BACKLOG.md is well-kept.

- **Product 1 — Mom's field journal** (the stated purpose). Mom-facing. Field-journal tone, glance→repository→loop, reading-accessibility, AI-free capture. This is the soul: plants/bloom/wildlife/weather/sky, the property map + zones, Mama's Perspective, the front-door voice walk. Its whole current arc is *"can Fernwood measure + earn Mom's engagement, honestly?"*
- **Product 2 — Paul's fleet & equipment tracker.** Paul-facing. Utilitarian, high-precision, deadline-bearing (registrations, service). It began as one "Vehicles card" and has quietly grown into a co-equal system: restoration lists, the service-records pipeline, manuals corpus, tap-to-call contacts, registration reminders, receipt-mining (Amazon/Gmail/ChatGPT), spare-key sourcing, the 9-item "Outstanding for Paul" data-collection list, the photo-miner seed.

**Why this matters:** the two products have *different users, different tone, different cadence, and different definitions of "done"* — but their backlogs are interleaved under one taxonomy, and most of the recent pickup-points are actually Product 2. That interleaving is the accretion. You can't reason about "is the Mom arc cohering?" while the fleet sub-system's data-collection tasks are scattered through the same list and the same session log.

**The decision this forces (lead with it):** name the fleet tracker as its own **track** so each product's backlog is reasoned about on its own terms. Three levels, choose one:
- **(a) Separate sections in one BACKLOG.md** — cheapest; a "Mom's journal" track and a "Fleet & equipment" track, each with its own intent statement. *Recommended v1.*
- **(b) Separate BACKLOG files** — `BACKLOG-mom.md` + `BACKLOG-fleet.md`; more separation, slight nav cost.
- **(c) Eventually its own surface/repo** — the fleet tracker is genuinely a different app; a future question, not now.

Everything below assumes at least (a).

---

## Fernwood's through-line, re-derived (Product 1)

> *A hyper-personal field journal that helps Mom see and record what only she can know from standing on the ground — and gets more trustworthy the more of her ground-truth it folds back in.* Glance (what's relevant now) → repository (the deep record) → loop (invite the one input only she can give, fold it back visibly). Capture stays deterministic and AI-free; AI lives only on the ask path, behind Paul's gate.

Test every Product-1 item against that sentence. Most pass. The ones that strain (a standing feedback box, a text-add button, the editable plant table) are exactly the ones already KILLED — the doctrine is working.

## Current-state read (what's actually true now, 2026-07-17)
- **The measurement crisis is resolved.** The 7/15 silent-capture lie (W1) is fixed and verified; Fernwood can now measure Mom honestly. This *unblocks the whole validation question* — it's the keystone the rest hangs on.
- **The "record about HER place" work is largely in:** basemap (W0 ✓), zones drawn + reconciled to 9 (W2 ✓), the front-door voice walk just shipped (W3 + today's launcher). The remaining depth item is real: **assign `zoneId` to the 24 null plants** (the W2 payoff) and the **instance-model schema question** (W6) underneath it.
- **Engagement is still n≈2, unvalidated.** Two gimme "Yes" answers; the Grow/Kill gate has never fired. Everything downstream is gated on a *non-gimme answer + a later-day return*.
- **Guru's digest is at ~80K — the tool-use-migration ceiling.** This is the closest-to-triggering infra item; it's a *when*, not an *if*.
- **W-PRIV is decided but not executed** — Mom is still on the public internet; the repo leaks her.

## The accretion diagnosis — why it feels like it's growing
1. **Two products, one list** (above) — the primary cause.
2. **Affordances added faster than measured.** W5/W7/W8 are all "we keep adding input surfaces." The *cure is already doctrine* (defer-affordances) — the fix isn't more items, it's holding the line at the **measurement gate** before adding. The backlog should make that gate a first-class ordering principle, not a footnote.
3. **Parallel surfaces outside BACKLOG.md** — the "Outstanding for Paul" list, the "Backlog — raised 7/05" fragment, and the Phases-D–G roadmap are un-unified. Most are stale (shipped/superseded) but they read as live.

---

## Proposed unified structure

### TRACK A — Mom's field journal
- **A1 · The engagement keystone (measure before you build).** The Mama's-Perspective Grow/Kill gate **+** the new front-door funnel (H1–H5, the `flowId` signals, the 4-week time-box). *Everything else in Track A is gated on this.* **→ the one genuinely-active thing; needs the `read-mom-funnel.py` read tool to be legible.**
- **A2 · The record about her place.** Assign `zoneId` to the 24 null plants (W2 payoff) · the instance-model schema question (W6, blocks the deeper "inventory") · photos-on-confirm-cards (W4).
- **A3 · The loop (invite + fold back).** Bloom ground-truth "is it open yet?" · bloom in the "Worth noticing today" glance · Fairway/change-reactions confirm · Phase G observations-as-knowledge-layer. *All gated on A1 proving the loop is wanted.*
- **A4 · Don't overwhelm her (the solicitation-stack IA).** W8 (umbrella) over W5 (the boxes) + W7 (confirm-card buttons). **Explicitly gated on A1 signal** — run the IA pass once the front-door funnel says something, not before.
- **A5 · Get her off the public internet.** W-PRIV (+ the folded-in password idea). Decided; execute when Paul does the Cloudflare/Pages-plan work.
- **A6 · Guru & capture infra.** Tool-use migration (⚠️ at the ceiling — elevate) · streaming · conversation-browse · durable photo-in-note.

### TRACK B — Fleet & equipment tracker (Paul-facing)
- **B1 · Live obligations (deadline-bearing — the only urgent things in the whole backlog).** GTI + Bolores registrations OVERDUE (emissions + renew) · GTI 90k/DSG + coolant verify · GTI spare-key dealer booking.
- **B2 · The record.** Service-records pipeline durability (off-machine backup R2 vs Drive — the one unbuilt piece) · receipt-mining residuals (CANDIDATE-ROWS verify queue, Gmail/Amazon fold) · per-vehicle mileage/last-service anchors · Tiguan/F-150 profile enrichment.
- **B3 · Data collection ("Outstanding for Paul").** The 9 items — mower belt P/N, Homelite shaft digit, paint codes (Bolores label photos, Tiguan sticker), Mom's county for emissions, NASA moon viz refresh, etc. *This IS a backlog; move it into BACKLOG.md under B3 instead of living only in CLAUDE.md.*
- **B4 · Photo layer.** photo-seed.json → photo-miner (tracked in its own repo; a pointer here).

### TRACK C — Cross-cutting / infra / doctrine
- Worker deploy automation (arm `CLOUDFLARE_API_TOKEN`) · candidate principles awaiting a 2nd sighting · the batch document-mining playbook.

---

## Per-item dispositions (proposals)
**KILL / retire from code** (already dead, still lingering): the ⭐ "this matters" star (0/104), seeded prompts (0 use) — retire on next viewer touch. *(Already KILLED in doctrine; this is the code-cleanup residual.)*
**MERGE:** "is it open yet?" + "bloom in glance" + Fairway/change-reactions → all become **A3 (the loop)**, gated on A1. · The "Backlog — raised 7/05" Save/Ask split → already resolved (one button shipped 7/13); mark resolved, delete the fragment.
**ELEVATE:** Tool-use migration (A6) — digest is *at* 80K now; it's the nearest real infra trigger, promote it from a buried DEFERRED row. · B1 obligations — these are the only *time-critical* items in the entire backlog and are buried; they deserve a visible "live obligations" position.
**DEFER (unchanged, real gates):** W6 instance model (blocks deep inventory) · Phase G (needs A1 + ~50 obs) · Phase H audio (needs a mature ID path + signal) · plants-to-consider gaps (time/source-gated).
**KEEP AS-IS:** the W-series arc (just reframed under A1–A5) · the SHIPPED + KILLED reference tables (they're doing their job — preventing revival).

## Scattered-source cleanup (the "unification" deliverable)
1. **Fold "Outstanding for Paul" (CLAUDE.md) into BACKLOG.md B3** — it's a parallel fleet backlog; unify it, leave a pointer.
2. **Delete the CLAUDE.md "Backlog — raised 2026-07-05" fragment** — all three items shipped/superseded; BACKLOG.md's SHIPPED/KILLED already covers them.
3. **Collapse "Forward direction — Phases D/E/F/G" to a one-line historical pointer** — D/E/F shipped, G is deferred (in BACKLOG); the long prose is a roadmap artifact, not live status.
4. **Archive the CLAUDE.md dated pickup-point log** — it's ~1,500 lines of historical trail (BACKLOG.md header already says it's history, not status). Move to a `PICKUP-LOG-ARCHIVE.md` so CLAUDE.md is lean; git holds it regardless.
5. **Memory hygiene:** update the fernwood entries that still describe held/superseded state ([[project_fernwood_prompt_mom_input]] already flagged); no new memories — this is pruning, not adding.

## The decisions for Paul (ratify before I restructure)
1. **The two-products call** — separate Track A / Track B: (a) sections in one file [rec], (b) two files, (c) future own-repo?
2. **Make the measurement gate (A1) the explicit top of Track A** — everything downstream gated on a non-gimme answer + later-day return. Yes?
3. **Fold "Outstanding for Paul" + prune the stale CLAUDE.md fragments/roadmap into the unified backlog** — go?
4. **Elevate the two buried-but-real items** — tool-use migration (at the 80K ceiling) + B1 live obligations (the only deadline items). Yes?

On your go, I rewrite BACKLOG.md to this structure, prune the scattered CLAUDE.md sources to pointers, and do the memory-hygiene pass — one reconciled pass, no new items added.
