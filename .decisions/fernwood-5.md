## fernwood-5 · After the 8/10 window — how lap 2 is timed

- project: Tate-Tracker
- source: anchor row "THE 8/10 WINDOW CLOSES ON AN UNMEASURABLE QUESTION" + D15 (migrated Phase 3a, 2026-08-08)
- options: run-lap-2-calendar-timed-again | time-lap-2-to-her-next-visit | pause-the-cycle

### Why it's here
Your D15 hold stands: the window closes as pre-registered, no extension, no prompting her. What that leaves is the first deliberate cadence decision this loop has made: the window closed UNMEASURED because she never loaded the build containing the thing it was meant to decide — the calendar outran her actual visit cadence.

### What it means
- **run-lap-2-calendar-timed-again** — same shape, another fixed window; risks a second unmeasured zero for the same reason.
- **time-lap-2-to-her-next-visit** — the lap's measurement window opens when telemetry shows a session from her device, not on a date; "does she open it unprompted" stays uncontaminated, and a lap can no longer close on an unmeasured question.
- **pause-the-cycle** — no lap 2 until you redesign the loop wholesale.

### Recommendation
**time-lap-2-to-her-next-visit** — it fixes the exact mechanism that made the 8/10 window unmeasurable, and it changes nothing she sees.
