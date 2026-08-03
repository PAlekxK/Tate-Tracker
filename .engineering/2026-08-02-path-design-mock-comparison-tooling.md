# Path evaluation — design-mock comparison tooling (2026-08-02)

*Engineering-partner consult, returned in-session during the button-system evening;
persisted here by the main session per the agent's request. Companion consults the
same night: ai-advisor (skill/tool staging + AI boundary) and ux-expert (exhibit
rules + compare layout), both returned in-session. Outcome: `~/.claude/tools/
exhibit.py` + the `/design-options` skill — Paul overrode the staged promotion
("just make it a skill") and replaced the run-count gate with a measured
Refinement log in the skill.*

## Decision: Path A, modified — the labeled PNG stops existing

The tool takes **raw** screenshots plus labels-as-data and composes labels in HTML.
Baking text into a raster imports font discovery, measurement, wrapping and clipping
as failure modes, and freezes the label at capture time. In HTML the label wraps,
never clips, stays editable, and can be sticky while scrolling a ~1,400px exhibit.

**Decisive environment finding:** Playwright is NOT installed as a package on this
machine — no python module, no `~/.cache/ms-playwright`, no node_modules. It exists
only as the agent-driven MCP plugin. So the tool must not own capture; the seam is:

> **The agent captures; the tool composes.** Browser/app orchestration is
> project-specific and churns; deterministic composition is generic and stable.

## Paths considered

- **A (chosen, modified):** agent captures via MCP; ~200-LOC stdlib-only Python
  composes a self-contained compare.html (base64-inlined images — AirDrops intact),
  manifest `exhibits.json` carries identity/order/labels, archived options render
  collapsed + dimmed with the stated reason. One loud guard: warn on capture-width
  mismatch (silently meaningless comparisons).
- **B (rejected):** tool owns capture too — requires installing Playwright + ~400MB
  Chromium to duplicate what the agent already drives; ~600+ LOC; wrong seam.
- **C (rejected):** live iframes, no images — elegant but not portable (dies with
  the local server, nothing AirDrops), N live app copies drift into N states
  (carousel, weather) so you stop comparing like with like, and no history.
  Right shape for a different job (reviewing ONE option interactively).
- **D (rejected):** checklist only — codifies the composition labor instead of
  removing it; PNGs still get opened one at a time.

## OSS sanity check (the sanity-check-before-build rule)

Visual-regression tools (BackstopJS, reg-suit, Margara, BrowserStack) do
baseline-vs-candidate pixel diffs — regression detection, not N-option ideation;
a pixel diff of "pills vs rectangles" is noise. Capture CLIs (capture-website-cli,
htmljet) do the half the agent already does. Contact-sheet generators emit
thumbnail grids (unreadable at 366×1400), mostly want ImageMagick (not installed),
label by filename, no round/archive model. Storybook is a build system for a
project that has neither. The gap is real and small — which licenses ~200 custom
LOC rather than 2,000.

## v1 deliberately omits

Screenshot capture (agent's job) · baked-in PNG banners (gone entirely) · pixel
diffing (wrong job) · thumbnails/downscaling (warn above ~8MB, don't solve) ·
cropping (agent element-screenshots the region).

## Deviations from the consult, with reasons

- **Location:** the consult said `Tate-Tracker/tools/` first, promote on the
  rule of three. Paul's "just make it a skill" pulled the tool straight to
  `~/.claude/tools/exhibit.py` — the skill is global, so its one mechanical
  dependency is too. The interface-will-move-twice risk the consult flagged is
  absorbed by the skill's measured Refinement log instead of a promotion gate.
- **`--pair` phone mode:** deferred; compare.html's 88vw columns already give a
  one-per-screen swipe on a phone. Revisit if a parameter-tuning round on a phone
  actually hurts (the log will say).

## Proposed principles — ✅ ALL FIVE PAUL-RATIFIED 2026-08-02 ("I'm good with all of these")

Written into their libraries the same night: #1–2 below → `engineering-principles/
cross-project/architecture-and-seams.md`; "mock in the medium" → `ai-playbook/
cross-cutting/tooling-and-promotion.md`; the two ux candidates → `design-principles/
cross-project/honest-surfaces.md` + `ordering-and-layout.md`. The menu-order/place-vs-
ranking principle also moved off watch status (second occurrence: this session's
exhibit-folder numbering). Original proposals kept below as the record.

## Proposed principles (as originally flagged)

1. **Compose the annotation in the viewer, not into the pixels** — bake text into
   a raster only when the consumer is out-of-band (a model's context, someone
   else's inbox); layer it when viewing through a surface you control. Does not
   contradict `ask_image.py`, where baking the question on the crop is the point.
2. **The agent captures; the tool composes** — the seam rule above; it is what
   keeps the tool promotable and gives it a non-AI door.

Also proposed the same night: ai-advisor's **"Mock in the medium, on real data"**
(playbook candidate) and ux-expert's **"An artifact must carry its own status in
its pixels"** + **"Juxtapose large differences; superpose small ones"**
(design-principle candidates). ~~None filed to the libraries — flagged for Paul.~~
*(Superseded by the ratification header above — all five are now filed.)*
