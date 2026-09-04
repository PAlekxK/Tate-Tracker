# LANE B — map-region smoothing

Read `_PREAMBLE.md` first. It binds.

## OWNS (the only paths you may write)
- `~/Developer/Tate-Tracker/.plans/2026-09-04-map-region-smoothing-PLAN.md` (new file)

## MUST NOT TOUCH
`data/zones.json` · `viewer.html` · any tracked data file · `BACKLOG.md` ·
`property.json`. **This lane writes ONE new plan document and nothing else.**
No code. No geometry edits. The 23 drawn zones are canon and are not yours.

## Read FIRST (all three — this ground is already covered, do not re-probe it)
- `BACKLOG.md` row **W2** — zones drawn 2026-07-17, 9 canonical, the reconciliation.
- `BACKLOG.md` row **W2-SCHEMA** — ⭐ vertices are real WGS84 `[lon,lat]`; the
  basemap is a swappable VIEW. A better basemap is a **re-registration, not a
  redraw**. This is what makes your work durable.
- `BACKLOG.md` **§478** — basemap pixelation + the SHADOW finding + the 2026-08-31
  source probe (Georgia 6-inch imagery is licence-gated and unavailable; USGS 3DEP
  LIDAR is free and has no shadows; Pickens coverage unconfirmed).

## ⭐ Scope — this is a DIFFERENT defect from §478
§478 owns **image quality** (resolution, shadows, zoom tiles). You own **polygon
topology**: the gaps between adjacent regions, and vertices that don't read as
smooth. A perfect basemap would not fix what Paul is describing. Do not merge the
two rows and do not re-litigate the imagery question.

Paul's words (transcribed 2026-09-04 1:54 PM ET, memo at `.private/voice-memos/`):
gaps between regions, not always smooth; wants an **automated and iterative**
cleanup; asks whether contour lines, elevation, or a visual read of big landscape
shapes from overhead footage could refine the boundaries; explicitly says **don't
reinvent the wheel — look at what's already out there**; notes these are regions of
*landscape* so physical indicators likely exist. And the closing frame, which is
the actual acceptance criterion:

> accuracy is bounded by the margin of error of satellite, GPS and pixels anyway —
> past that, **the remaining job is just making it clean.**

He also owns part of it himself: *"a lot of that is on me for the vertices I selected."*
So a fix that only says "redraw more carefully" is not an answer.

## What the plan should contain
1. **Prior art first.** Named techniques with tradeoffs — shared-edge / topological
   models (gaps become structurally impossible vs. cosmetically closed), snapping
   tolerance, Chaikin / Douglas-Peucker / spline smoothing, and how each interacts
   with WGS84 vertices at this scale. Cite what exists; don't invent a method.
2. **The gap question specifically** — are adjacent zones meant to share edges? If
   yes, that is a data-model change and the biggest decision in the plan.
3. **Whether terrain data can inform boundaries** — USGS 3DEP LIDAR hillshade is
   already identified as free and shadow-free (§478 ③). Two of Mom's own zone names,
   *"The bank"* and *"The Bluff"*, are terrain features. Assess honestly: ~1m posting
   is not a resolution answer.
4. **A recommendation**, and what it would cost.
5. **What you could not verify**, named.

## GATE (stop here and report)
The plan document, with a recommendation. **No code, no geometry writes.** Paul
reads it and decides whether it becomes a BACKLOG row.
