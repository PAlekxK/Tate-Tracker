# Free-text capture journeys — user-researcher report (2026-08-02, late)

*Commissioned by Paul mid-session ("what's the natural path for just free text
capture? … we need to think through all the journeys"). Returned in-session; this
file is the persisted record. Paul's disposition, same night: **HOLD everything —
all queued for the 2026-08-10 rationalization** when the clean measurement window
closes and her feedback gets a full analysis. Claims tagged assumption | inferred |
validated per the user-research practice.*

## The doors — FIVE, not three `[validated]`

| # | Door | Mechanic | Lands as |
|---|---|---|---|
| D1 | Almanac composer | inline, log-first | `/api/observations` (Journal) → best-effort Guru |
| D2 | Ack "Write me back" | modal (`FeedbackRibbon`, section `ack-reply`) | `/api/feedback` |
| D3 | Confirm-card "Write me back" | inline `openNote()` — note rides ONLY if opened BEFORE answering | `/api/feedback` + `{questionId, kind}` |
| D4 | 💬 General-feedback FAB | modal, always on screen | `/api/feedback`, section `ribbon` |
| D5 | Zone walk | voice/text | `/api/feedback`, section `zone-describe` |

## The load-bearing findings

1. **The post-answer dead end is confirmed and unrecoverable** `[validated]`:
   `answer()` posts immediately; `showAck()` wipes the host and auto-advances at
   **2600ms**; the question enters `ANSWERED_KEY` and `syncServerAnswers`
   dismisses it durably — she can never revisit that card on that device. The
   ack copy ("Noted — your read's in the record. ✓") is a verbal period too.
2. **The app disagrees with itself about aftermaths** `[validated]`: "Not quite"
   (with `correctionPrompt`) already opens an add-words moment; "That's all of
   them" is terminal; the ack section's `markSeen()` RE-APPENDS "Write me back"
   after "Got it." Three doors, three aftermaths — the confusion is the
   aftermath inconsistency, not the door count.
3. **~~The composer's attachment branches skipped the guaranteed log~~ — FIXED
   same night** (commit `6d742df`): words typed with a photo/audio now hit
   `fnSaveInlineEntry` first, every branch.
4. **`/api/observations` has NO needs-reply lifecycle** `[validated]`:
   `read-mom-feedback.py` reads `/api/feedback` only, so D1 — the composer —
   sits outside the "capture is not a loop" machinery (7/26 standing rule). Any
   consolidation toward the composer is blocked on this. The composer predates
   the rule and has never been tested against it.
5. **Her free-text corpus is TWO notes** (7/26 rainfall, 7/29 follow-up), both
   via the general-feedback path, plus nine Guru conversations. Every
   preference claim rests on that. `[validated as count]` The one clean
   observed day (7/26) shows her using the composer↔FAB split CORRECTLY, once.
6. **No card-attached note from her exists in the artifacts read**
   (searched-negative: feedback-log.json; live Worker NOT queried). `[inferred]`
7. Confirm-card drafts are in-memory only — carousel navigation and the defer
   link preserve typed words; a reload eats them. `[validated]`

## The recommendation (QUEUED for 8/10 — not shipped)

**Option B trimmed by D:** delete the confirm card's pre-answer "Write me back";
after ANY tap (yes / no-sans-correction / defer) render the ack line **with an
open add-context field** pre-bound to the `questionId`, posting a second
sentiment-null `/api/feedback` record (`context.section: "card-addcontext"` —
inherits needs-reply protection for free). **The 2600ms auto-advance dies
whenever the field is showing** — advance on her next action. Draft copy (Mom-
facing → Paul must confirm wording): *"Noted — your read's in the record. ✓
Anything you'd add about this one?"*

Why: her documented frame is "she'll adjudicate, she won't be examined" — a note
that must precede the verdict is an appendage to the verdict and inherits the
examined frame; a post-tap field arrives after the verdict is banked. It removes
the only control in the stack requiring an unstated ordering rule, keeps
provenance, and copies the aftermath the ack section already has — making the
master card internally consistent (the 7/29 one-grammar rule extended from
button paint to what-happens-after).

**Explicitly NOT recommended:** collapsing to one door (the composer/FAB split
has one clean observed use and zero observed failures — more evidence than any
redesign has); a Mom-facing permanent "don't ask me this" (a graded-feeling
choice for a reader afraid of being wrong — the pressure valve is agent-side
rotation to the bench on repeated snoozes, gated on the signal appearing).

**Validation plan once shipped:** one `card-addcontext` record from her device
moves the recommendation from assumption to inferred. None in three weeks while
she still answers confirms → the honest read is that ANY card-attached free-text
invite inherits the examined frame, and the card should carry none.

## Where n binds (say this in the 8/10 session)

- The 7/13–8/01 funnel describes an app that no longer exists (restyled 7/30,
  reorganized + re-systemed 8/02). Do not pool across those lines.
- The confirm-card funnel confounds six variables; 4-of-14-answered does not
  isolate any single cause.
- **Open question the researcher flagged:** does "front door offered 10 →
  tapped 0" name the ack card or the zone launcher? (The repo's own comments
  historically call the ZONE LAUNCHER the front door, which is how the main
  session reads it — meaning journey "she replies to our note" has NO offer
  count and the ack-section pattern being copied is design precedent, not
  validated behavior.) Resolve from `read-mom-funnel.py` on 8/10.
