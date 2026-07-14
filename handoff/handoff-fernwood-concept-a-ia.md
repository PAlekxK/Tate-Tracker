# Handoff: fernwood-concept-a-ia
<!-- generated 2026-07-14 ~1:15pm ET · sources: Tate-Tracker@b972dc0 · RECEIVER: verify shas vs HEAD before trusting any status below. This brief was composed COLD from another session — it POINTS at sources, it does not carry design state. Treat BACKLOG.md@HEAD as truth. -->

## 1. Mission
Pick up the Fernwood **"Concept A" dashboard-IA** thread: resolve the remaining open UX **judgment calls** on the glance / Plants surface and the **Save/Ask button split**, editing the live `viewer.html`. Most of Concept A already shipped — this is the tail.

## 2. Read first (point, don't re-derive)
1. **`BACKLOG.md`** — Fernwood's **status SSOT** (read this FIRST, it wins over CLAUDE.md and over the session anchor). Section **"✅ Just shipped (2026-07-14)"** has what's live + the one live **"Open judgment call (Paul)"** on the Plants tile.
2. **`CLAUDE.md`** → section **"## Backlog — raised 2026-07-05 (Concept A session)"** — the **Save/Ask two-button split** rationale (the richest open design question). Also the **"## Pickup point — … unified-input polish + plant look-fors"** section (tile-prompt judgment).
3. **`viewer.html`** — the live dashboard these judgments touch (Plants tile, composer, Mama's Perspective). Deploys to GH Pages; no Worker involved.

## 3. Next steps (ordered)
1. **Reconcile against BACKLOG.md** — the session anchor snapshots this thread at `d61d47b`; HEAD is `b972dc0`. Much shipped since (look-fors→Plants-tile, peak-this-week, composer order, weather card). The anchor's "look-fors too buried inside Plants" judgment is, per BACKLOG.md, **already answered** (shipped 7/14). Confirm what's genuinely still open before doing anything.
2. **Plants-tile prompt judgment (Paul's call).** The tile shows **one** plant look-for (today the mow/fairway one). Decide: (a) bias toward **flowering plants over turf**, and/or (b) show **two**. Both ~1-line changes in `gatherPlantLookForCandidates(now)` / `plantCheckPrompts()`.
3. **Save/Ask two-button split (design).** Paul isn't convinced the app needs both "Save & ask the Almanac" and a separate path. **Do NOT just remove it** — the split is the on-screen form of the capture-path principle (Save = deterministic/AI-free/verbatim; Ask = the AI path). Collapsing it forces capture-through-AI or intent-guessing (both rejected earlier). Likely resolution = **hierarchy, not removal** (Save primary, Ask quiet secondary) — but **confirm what's actually bugging Paul first** (clutter vs choice-friction vs one-intent-dominates). Consider a `ux-expert` read; this was an evidence-based decision (the 7/2 Mom "wasn't sure it logged" signal).
4. If any **"3× this week in the Plants area"** duplication remains (tile / panel / Worth-noticing), decide merge vs thin — check BACKLOG.md whether it's still live.

## 4. State & pointers
- Repo `~/Developer/Tate-Tracker` @ **`b972dc0`** (clean; the untracked `.engineering/ .ux-reviews/ .playwright-mcp/ __pycache__/` are a *different* concurrent session's — ignore, don't commit).
- Live surface = **`viewer.html` → GH Pages**. Worker/digest untouched by any of this (viewer-only changes).
- **Status SSOT = `BACKLOG.md`.** CLAUDE.md "Pickup point" sections are a *historical log*, NOT current status.
- No uncommitted work on this thread to carry.

## 5. Guardrails
- **Capture path stays AI-free** — Save = deterministic verbatim; AI only on the Ask path ([[feedback_no_ai_on_capture]]). Any Save/Ask resolution must not route capture through AI.
- **`viewer.html` only** — no Worker/digest change. Verify in-browser before commit.
- **Mom reads with difficulty** — meaning via icon + size + color + position, not label text ([[project_fernwood_mom_reading_accessibility]]).
- Fernwood tone: field journal, not task manager — avoid urgency/alert language ([[project_tate_tracker_tone]]).

## 6. Done when
The Plants-tile prompt judgment is **decided + implemented** (or explicitly parked with a gate), the **Save/Ask split has a decision** (hierarchy / keep / remove) with Paul's confirm, and **BACKLOG.md reflects the outcomes**.

## 7. Un-sealed judgment
None carried — this brief was composed cold from another thread, so there is **no hot design intuition here to lose**. Everything is pointed-to from `BACKLOG.md` / `CLAUDE.md` / `viewer.html`. That's the intended shape (pointer, not reconstruction); the reset is safe because nothing lives only in my head.

## 8. Trust status (per open item)
- **"Look-fors too buried inside Plants"** (from the session anchor) — **model-flagged as ALREADY RESOLVED** per BACKLOG.md (shipped 7/14). NOT a fact until the receiver verifies it in BACKLOG.md@HEAD. If truly done, drop it.
- **Plants-tile prompt judgment** + **Save/Ask split** — **Paul-owned OPEN decisions** (human-confirmed still-live this session, 2026-07-14). Real, awaiting Paul.
