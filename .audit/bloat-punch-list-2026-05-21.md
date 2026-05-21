# Fernwood CLAUDE.md — bloat punch list (2026-05-21)

**Source audit:** `~/.claude/agents/audits/2026-05-21-portfolio-audit.md`
**Current size:** 495 lines / 69K
**Target size:** ~220 lines after trim
**Execute when:** During W2 (Fernwood surface polish) — folded in per the audit recommendation. Surface polish on the *project* warrants surface polish on its *spec*.

---

## Why this needs trimming

Fernwood's CLAUDE.md has **four parallel "next steps" sections** plus **two adjacent Paul-asks sections.** When Paul (or any agent) opens the file, the question "what's actually next?" has multiple competing answers. The Pickup point at the top is the de facto source of truth; everything below is archaeology. This violates `feedback_single_source_of_truth.md` in the most direct way possible.

Specifically:
- `## Next steps` (line 139) — mostly ✓ Done sub-sections
- `## Pending design improvements (prioritized)` (line 402) — all ✓ Done
- `## Forward direction — toward a field assistant (Phases D / E / F)` (line 423) — partially current
- `## Next steps after the drafts go live` (line 475) — drafts went live 2026-05-13
- `## Deferred for Paul` (line 461) + `## Outstanding asks for Paul` (line 465) — two adjacent sections doing the same job

---

## Trim targets — concrete sections to remove or relocate

### 1. `## Next steps` (lines 139–363) — move to history
~225 lines of `~~Done~~ ✓` items dating back to early May: Phase 1–6 weather work, photos work, sounds work, hourly forecast strip, gardener-insight fallback, icon audit, etc. All shipped.

The only live items in this section are:
- "Additional live data sources + dynamic summarization" (still aspirational — keep, but move into Forward direction section)
- The deferred Cherokee/Etowah callouts (already living in the Pickup point "Open editorial follow-up" line — delete duplicate)

**Action:** Move the section verbatim to `Tate-Tracker/.history/CLAUDE-history-2026-05-21.md` with a header "Archived 2026-05-21 from CLAUDE.md (W1a audit)." Delete from CLAUDE.md. Pull the one live item into the existing Forward direction section.

**Trim:** ~225 lines.

### 2. `## ~~Next major pass — holistic UX + copy review~~ ✓ Done 2026-05-18` (line 377) — delete
Entirely done. The struck-through heading itself is the signal.

**Action:** Append to the history file. Delete from CLAUDE.md.

**Trim:** ~25 lines.

### 3. `## Pending design improvements (prioritized)` (lines 402–410) — delete
All 7 items ✓ Done.

**Action:** Append to the history file (date-stamped). Delete from CLAUDE.md.

**Trim:** ~10 lines.

### 4. `## Active drafts (not yet promoted to live data)` (lines 412–417) — delete
Both drafts promoted 2026-05-13.

**Action:** Append to history. Delete from CLAUDE.md.

**Trim:** ~7 lines.

### 5. `## Uncommitted work in progress` (lines 419–421) — delete
Currently reads "(None)." Section serves no purpose when empty. If kept as a convention placeholder, it'll drift the moment Paul commits.

**Action:** Delete entirely. Git status answers the question this section was trying to answer.

**Trim:** ~3 lines.

### 6. `## Next steps after the drafts go live` (lines 475–481) — delete
Drafts went live 2026-05-13. The two remaining sub-items belong in:
- Outstanding asks for Paul (#1–3)
- Pickup point's editorial follow-up

**Action:** Verify those two items are captured in the surviving sections, then delete this section. Append to history.

**Trim:** ~7 lines.

### 7. Merge `## Deferred for Paul` (line 461) + `## Outstanding asks for Paul` (line 465) → single section
Two adjacent sections doing the same job (things Paul needs to do or decide). Single-source-of-truth violation in miniature.

**Action:** Merge into one section. Recommended title: **`## Outstanding for Paul`** (covers both "decide" and "do"). Reorder the merged items by priority.

**Trim:** ~5 lines + reduced reader confusion.

---

## Keep as-is (load-bearing — do NOT trim)

- `## Pickup point — last session ended 2026-05-19` (the canonical "where are we" surface — promote to *the* current-state section)
- `## Project purpose & tone`
- `## How to run`
- `## Architecture`
- `## Design system`
- `## Elevation calibration` (a guardrail callout — keep it loud; easy to drift back to wrong number)
- `## Forward direction — toward a field assistant (Phases D / E / F)` (live, currently driving Phase E follow-on work — keep, but verify it's the only "next" surface remaining after the trim)
- `## Location constants` (reference table)

---

## Net effect

- **Lines trimmed:** ~275 (225 + 25 + 10 + 7 + 3 + 7 — minus a few lines pulled into surviving sections)
- **Final size:** ~220 lines
- **Sections after trim:** Pickup point → Project purpose & tone → How to run → Architecture → Design system → Forward direction (Phases D/E/F) → Outstanding for Paul (merged) → Elevation calibration → Location constants
- **History preserved at:** `Tate-Tracker/.history/CLAUDE-history-2026-05-21.md`

**Reader-time payoff:** Every session-start opens with "where are we?" Today, Paul (or an agent) has to scan four "next" sections and decide which is current. After trim, there's one — the Pickup point — with the Phases D/E/F roadmap as the only behind-it source.

---

## Sequencing within W2

Suggested order:
1. (W2 step 1) Slope grep + rewrite
2. (W2 step 2) Helper text + seeded chips removal
3. **(NEW, fold-in) CLAUDE.md trim per this punch list**
4. (W2 step 3) Mammal photos pipeline
5. (W2 step 4) Wire mammals
6. (W2 step 5) Amphibian sounds
7. (W2 step 6) Mammal sounds (5 curated)
8. (W2 step 7) RELEASE_NOTES.md
9. (W2 step 8) Recent updates card
10. (W2 step 9) Playwright regression + Paul eyeball + Garden Guru E2E smoke test (5 questions, bundled per audit recommendation)

The trim is best done after the slope/helper-text/seeded-chips work lands but before the photo/sound pipeline runs — that way the CLAUDE.md updates (like "Recent updates card spec" or any new section the W2 work adds) get added to the *post-trim* file rather than the bloated one.
