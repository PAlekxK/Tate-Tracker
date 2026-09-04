# LANE D — Tier 1 render fix (map regions)


## STATUS: OPEN — working.
Read `_PREAMBLE.md` first. It binds. **You are the QA-HOLDING lane for this run** — see §QA.

`[paul-greenlit 2026-09-04]` *"yes, greenlight tier 1 as its own lane."*

## ⛔ SCOPE — Tier 1 is THREE steps and you own TWO

Lane B caught that the greenlight bundles a decision Paul has not made. You own steps 1–2:

1. **`stroke-linejoin: round` + `stroke-linecap: round` on `.pmap-zone`.** One CSS declaration,
   zero data risk.
2. **Chaikin, 2 iterations, at RENDER TIME**, mirroring the tracer's implementation in
   `b661d59`. ~15 lines.

**Step 3 — THE DASH — is NOT yours.** All 23 zones are `status: draft`, so the whole map renders
dashed and the draft signal carries no information. That is Paul's **authoring** call, and the
real fix is probably confirming the zones he trusts — a `status` edit, not a geometry one. ⛔ **The
honesty rule that put the dash there must not be reversed by an agent.** ASK him; do not act.

## OWNS
- `engine/viewer.template.html`
- `viewer.html` — **only as the rebuild output**, never hand-edited (see below)

## MUST NOT TOUCH
`zones.json` · any file under `data/` · `tools/area-trace.html` · `BACKLOG.md` ·
`property.json` · `.plans/2026-09-04-map-region-smoothing-PLAN.md` (lane B's, read-only).

## ⚠️ THE EDIT TARGET — the trap lane B flagged against its own plan
**`viewer.html` is GENERATED.** Lane B's plan says *"viewer.html ~line 9995"* — that is correct
as a **render-site locator** and **wrong as an edit target**; the plan predates knowing the file
is generated. Editing `viewer.html` directly goes red on `--check` and is absorbed on the next
`--extract`. **Edit `engine/viewer.template.html`, then rebuild, then prove
`python3 tools/build-viewer.py --check` is byte-identical.** Lane C hit this today; do not
rediscover it.

## ⛔ CHAIKIN IS RENDER-ONLY, AND THIS IS THE LOAD-BEARING CONSTRAINT
It must never be written to the data. Three independent reasons, the third measured by lane B:
it is **area-biased inward on small convex rings** — `western-fern-azalea-garden` **−10.5%**,
`house` **−7.7%** — so every distance check reads green while the smallest zones shrink.

**Proof obligation, inherited from `b661d59`:** assert the stored vertex array is **byte-identical
before and after**. Ship that assertion, don't just observe it once.

Displacement budget, measured by lane B on the current 23 zones: median **0.10 m**, p90 **0.55 m**,
max **2.79 m**, against the record's own **±9.1 m** accuracy budget.

## Acceptance
**"Does it render on `viewer.html`."** Never *"does the tracer do it"* — that inversion is the
entire finding of `bebbfe3`: the 2026-08-31 snapping and smoothing landed on the authoring
surface and never reached the reading one.

## §QA — you hold QA, and you still do not push
`[standing rule, practice-steward audit 2026-09-04]` **At most one lane holds QA for a whole
run.** That is you. No other lane touches it.

**You still do not push.** Prod is FROZEN and Mom's feedback is HELD. Verify **locally** — build,
then open `viewer.html` in a browser and look at the map. The file is self-contained, so a local
open is a real check, not a proxy. The push to QA is Paul's call after he has seen it.

## GATE (stop here and report)
A **before/after Paul can look at** — the map rendered both ways, staged so he can open it
without a terminal. Plus: `--check` byte-identical, the vertex-identity assertion passing, and
**the dash question asked, not answered**.
