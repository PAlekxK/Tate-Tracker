# Scoping seed — "prompt Mom for input" as a Fernwood capability

**Status:** LOGGED 2026-07-13, not started. Input brief for the expert panel
(user-researcher · ux-expert · ai-advisor · engineering-partner). This is the *frame*,
not the answer — the panel proposes how it works and how we learn from it.

## The trigger (real, 2026-07-13)
Mom, out on the property, sent photos of a weed growing in a rock seam and asked **what it is
and whether there's a good way to control it.** (Best-read ID: common blue violet — native,
fritillary host — with a crush-test to settle violet vs. ground ivy; control advice hinges on
that ID *and* on the native-vs-nuisance judgment.)

Paul's read: **this is a good example of something we should proactively prompt Mom for input on** —
turn a one-off "what is this?" into a repeatable loop the app runs.

## Why it's interesting (connects to existing doctrine)
- It's the **loop / flywheel** from the governing design principle (glance → repository → *invite
  the input only someone standing on the property can give* → fold it back in). But note the
  **inversion**: the canonical loop invites ground-truth to sharpen *our* model; here Mom initiates
  with a *need* ("help me with this weed"). The panel should decide whether these are one mechanism
  or two.
- It extends **observations-as-a-knowledge-layer** ([[project_tate_tracker_observations_feedback_loop]])
  — a weed sighting + its location + Mom's control decision is exactly the kind of note that should
  feed back.
- It must honor **capture stays AI-free / AI on the ask-path** ([[feedback_no_ai_on_capture]]) and
  **defer affordances pending signal** ([[feedback_defer_affordances_pending_signal]]) — this is
  ONE real Mom-initiated instance, not yet a validated demand for a standing feature.

## Questions for the panel
1. **What's the prompt?** When/where does the app ask Mom for input, and about what (weeds? anything
   she photographs? seasonal "what's spreading?" nudges)? Calm field-journal, never naggy.
2. **Capture vs. ask split.** The ID + control advice is the AI ask-path; the logged record (the
   weed, where, what Mom decided) is deterministic capture. Where's the line?
3. **The stewardship nuance.** "Control this weed" advice for a *native* plant (violet) is a
   value judgment, not just horticulture — contain-vs-eradicate. How does the app handle
   native/beneficial "weeds" without reflexively recommending removal? (Fernwood ethos.)
4. **How do we learn from it?** What gets folded back — a weed layer on the property map? a
   "what's spreading where" view? Does confirming an ID promote it into canon (the Phase-F path)?
5. **The verification discipline.** Photo IDs are inferences until Mom's ground-check (crush-test)
   or a deterministic source clears them ([[feedback_verify_scanned_image_inferences]]).

## Not deciding here
Whether to build it, what surface it lives on, or whether it's a standing affordance vs. a
contextual nudge. That's the panel's job. Seed only.
