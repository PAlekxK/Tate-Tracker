## fernwood-9 · momack_unfolded — re-wire the dead metric or retire it

- project: Tate-Tracker
- loop: tate-tracker
- source: anchor row "momack_unfolded is UNREACHABLE" + tools/check-telemetry.py (migrated Phase 3a, 2026-08-08)
- options: retire-the-event | rewire-the-fold-into-changes

### Why it's here
The 'Read the rest' fold lives only on the legacy prose branch of the ack ribbon; MOM_ACK_DATA has used changes[] since 08-04, so the fold cannot render and momack_unfolded can never fire (confirmed in the DOM: 4 change bullets, 0 .ack-read-rest). Its sibling momack_followed was deliberately re-wired and survived; this one was missed. Leaving it is the bad state — it reads as a bug forever.

### What it means
- **retire-the-event** — the metric is removed from check-telemetry's expectations with a dated note; if a fold ever returns to the changes[] branch, a new event gets named then. Nothing she sees changes.
- **rewire-the-fold-into-changes** — the changes[] branch gains a fold for long updates and the event fires again; only worth it if you want folding behavior on her ribbon at all.

### Recommendation
**retire-the-event** — the UI it measured no longer exists on the live branch; a metric with no renderable trigger measures nothing. Re-introduce deliberately if a fold ever comes back.
