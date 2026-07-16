# Mom's 7/15 feedback — Paul's relay (NOT verbatim)

**Date of her session:** 2026-07-15 · **Recorded:** 2026-07-16
**Provenance: `paul-relayed`.** Her actual words were LOST (see "The capture failure"
below). Everything in "What she said" is Paul's recollection of what she told him,
not her verbatim text. Treat every item as **[relayed]** — a faithful report of
Paul's memory, one remove from the source. Do not quote any of it as her words.

---

## The capture failure (why this document exists)

On 2026-07-15 Mom used the app and submitted substantive feedback, including via the
general-feedback field. **Zero records exist on the server for that day, across all
four independent streams:**

| Stream | Captures | Records 7/15 |
|---|---|---|
| `/api/feedback` | Mama's Perspective + general feedback | 0 |
| `/api/observations` | "Add a note" / Almanac | 0 |
| `/api/conversations` | Garden Guru | 0 |
| `/api/zone-feedback` | "Describe a place" | 0 |

Verified not-an-artifact: the same query returns her two 7/13 confirms correctly;
`/health` is green; the deployed Worker (2026-07-14 00:59) postdates the 7/13
validation relaxation, so a note-only record would have been accepted. Her 7/13
answers prove her device was configured and posting two days earlier.

### ROOT CAUSE — SOLVED 2026-07-16 (deterministic)

**She was on her MacBook** (Paul, 2026-07-16). That device was never configured with
the Worker token — only the phones were paired. On an unconfigured device the entire
write path silently no-ops:

- `viewer.html:13149` — `function isConfigured() { return !!cfg(); }` (cfg = per-device localStorage)
- `viewer.html:13232` — `MetricsCollector.flush()`: `if (flushing || isExcluded() || !WorkerAPI.isConfigured()) return;`
- `viewer.html:8697` — `postFeedback()` gates on the same `isConfigured()`
- `viewer.html:8691` — `sendGeneral()` calls `showAck("Noted — it's in the record. ✓")` **unconditionally**

Corroborating telemetry (`/api/metrics`, 7/13–7/16): exactly **three deviceIds have
ever existed** — `mpfrqkme` (Mom's iPhone; it fired the two `momqueue_answered` events
on 7/13), `mpevr35o` (Paul's; it posted the "Test by Paul" observations), `mpeuqnyg`
(third, 7/14 only). On 7/15, **only Paul's device was active**; Mom's iPhone shows zero
events, and no unknown device appears — *because an unconfigured device cannot appear.*

**So: she typed real feedback into an app that had no ability to send anything, and it
told her "Noted — it's in the record. ✓".** Her words went to
`localStorage['tateTracker.momQueue.general.v1']` on the MacBook and nowhere else.

Two properties make this worse than a flaky-network bug:
1. **It is not transient.** An unconfigured device can *never* sync. Await/retry/outbox
   would not have saved her. The device is permanently dark.
2. **The failure is invisible to Paul by construction.** He cannot see that she tried.
   **Silence from a dark device is indistinguishable from disengagement** — this bug was
   positioned to make him conclude she wasn't using the app, at the exact moment he was
   deciding whether she engages. It nearly cost her the verdict.

**Per-device token pairing is the real defect.** Mom is a Claude-on-her-laptop power
user; her MacBook is a *primary* device, not an edge case. Every new device she opens is
a silent void until Paul manually pairs it.

**This is the second lost-capture incident** (first: 2026-07-03) — the same root shape:
capture that fails silently while the UI acknowledges success it never verified.

**Recovery:** her verbatim words are very likely still in Safari's localStorage on that
MacBook. Paul's 2026-07-16 call to skip recovery was made when we believed it was a
locked-down phone; a Mac makes it materially cheaper. **Re-open this.**

---

## What she said [all items: relayed]

### 1. The end-state ask — every plant should carry (her stated bar)
- **a picture she selects** (emphasis: *she* chooses it)
- **a clear description**
- **location data, leveraging the zones already defined**

### 2. A general feedback field, clearly labeled as such
She asked for this explicitly and unprompted.

### 3. Three stacked text boxes is confusing
"Add a note", "submit feedback", and the Garden Guru box stacked on top of each other
— she could not tell them apart or tell which to use.

### 4. Confirm cards must show a picture of the plant
When a Mama's Perspective card asks her to confirm yes/no about a specific plant, the
card should carry **a picture of that plant**, so she can actually see what's being
asked about.

**Verified 2026-07-16, two ways:**

1. **The card is text-only by construction.** There is not one `<img>` or `photo`
   reference anywhere in the `MomQueue` block (`viewer.html` ~8500–8900). No confirm
   card has ever shown her a picture of anything. This is not a data gap — the card
   type has no photo affordance at all.
2. **And the underlying records are photoless anyway.** At commit `02275a1` (the 7/13
   state she answered against): `crocosmia` — no photo; `hydrangea-panicle` — no photo;
   `lizards-tail` — no photo.

So she was asked *"is this crocosmia 'Lucifer'?"* — **a question about a photograph we
read the variety off of** — while being shown no photograph, of a plant we hold no
photograph of. And she answered Yes.

This is the same ask as #1, arriving from the other direction: **she cannot give ground
truth about a thing she isn't shown.** It also puts a question mark over the two answers
we *did* fold to canon on 7/13 — see "Open" below.

---

## What the data says (verified 2026-07-16, deterministic)

Her ask is not feature creep. She is describing gaps that measurably exist:

| Her ask | Schema | Reality |
|---|---|---|
| Picture she selects | `photo` + `attribution` | **18 of 26 plants carry a Wikimedia stock photo** — a stranger's photo of the *species*, not of the plant at Fernwood. Only **2** are real property photos (`source: "Phase F submission"`, from her own Guru photo workflow). **6 have no photo at all** — incl. `crocosmia` and `hydrangea-panicle`, the very plants the queue is asking her about. |
| Clear description | `guide`, `currentSeasonNote`, `soilNotes`, … | Present on 26/26 — but written *about the species*, sourced from reference material. |
| Location via zones | `zoneId` | **24 of 26 plants have `zoneId: null`.** Only `fairway-turf` and `fairway-meadow` are placed. |
| The zones themselves | `/api/zones` | **8 real, drawn, named zones exist and are live**: Fairway, Fairway Fringe, Western Garden, Eastern Garden, Pond Area, Lower 40, Stable Grounds, Parking Bank. |

**The synthesis:** the zones exist and the plants exist, but *the link between them was
never made*. The photos are generically sourced. So the record claims to be a journal of
**her** property while being, field-by-field, a species encyclopedia that could describe
anyone's garden.

She is the only person who can fix that — she's the one standing on the ground who knows
which hydrangea is in the Eastern Garden and what it actually looks like. Read this way,
her three asks are one ask: **"your record of my place isn't actually about my place —
give me the means to make it true."** That is a request for ownership, not features.

---

## Standing doctrine this challenges

- **"Open feedback → DON'T BUILD (she texts Paul out-of-band, that's fine)"**
  — from the 2026-07-13 panel. She has now asked for it, unprompted, in her own words.
  The doctrine was a reasonable inference; she has contradicted it. Per
  [[feedback_agent_proposals_not_validated]], her direct ask outranks a panel inference.
- **[[feedback_defer_affordances_pending_signal]]** — "ship simplest, promote on observed
  behavior." This *is* the observed behavior/signal that gate was waiting for.

## Open (not answered by this document)

- Whether items 1–3 are the *complete* set of her 7/15 feedback, or only what Paul
  recalled. **Assume incomplete.**
- Her exact words on any of it. Unrecoverable by decision.
