# Field capture & the offline premise — the work queue
**Opened 2026-08-31** from Paul's ask: *"set up a queue to work through all of this."*
Sources: two expert seats (`.engineering/2026-08-31-path-field-capture.md`, user-research
in-session), my own verification of every load-bearing claim against the code, and Paul's
stated site premise (`CLAUDE.md` → *The site's physical premise*).

**This file is a SEQUENCE, not a second tracker.** Status for anything durable stays in
`BACKLOG.md`. Read this for *what order and why*; read that for *what is true*.

**The premise everything below is built around** `[paul-stated 2026-08-31]`: no cell
reception, Wi-Fi from the house only, coverage falling off with distance, heavy canopy,
permanent. Connectivity is *inversely* correlated with distance from the house.

**The verdict both seats reached:** Avenza is Paul's **finite geometry** tool. No job in it
for Mom. It must not be routed through Track A, and it must not un-park the zone hold.

---

## ⛔ Gate before anything ships to her surface
Steps 0a–0c touch Mom's live surface. Nothing here reaches her without Paul's explicit go,
per the standing rule on her surfaces.

---

## STEP 0 — the offline holes in what already ships  ·  **Track A defect, do first**

> **STATUS 2026-08-31: 0a, 0b, 0c BUILT and verified in the browser — `5878735` + the
> `recordedAt` commit. Wording DONE — drafted by content-steward, including the two
> genuine-loss lines and a drift catch on copy that already shipped. NOT DEPLOYED; nothing
> reaches her until Paul pushes and deploys the Worker. 0d DEFERRED by Paul — not blocking.
> **STEP 0 IS COMPLETE. Next: Step 1, per-vertex provenance.**
>
> Parked from the content seat, surface questions rather than copy ones: the arrival line
> only fires if she happens to open a zone panel while in range, so the promise is usually
> kept silently and she never learns it was — possibly the ack ribbon's job. And the acks
> say "the record" while the surface she can look at is the **Journal**, her word.**

> Not a field-capture feature. A live defect that the premise turned from theoretical into
> certain. She cannot use her own surface where the job is.

### 0a · `close()` loses her recording without telling her `[VERIFIED in code]`
`viewer.html:10381` — `close()` removes `.open` from the panel and *then* fires
`stopAndUploadGrow()` un-awaited. The failure line writes into a sheet that is already shut.
Online: harmless. Offline: she closes mid-recording, the upload fails, **she is never told**.
The comment above it reads *"Capture-first: if she closes mid-recording, save what she said
(don't lose it)."* Right intent; the premise inverts it.
- **Done when:** a failure that happens during/after close is still surfaced to her, or 0b
  makes it moot by queuing instead of failing.
- **Owner:** me. **Gate:** Paul, before it reaches her surface.

### 0b · Give audio an outbox `[the real fix; 0a falls out of it]`
The text path holds submissions in `tateTracker.feedbackOutbox.v1` *"until a 2xx"* and flushes
on `online` (`flushOutbox`, viewer.html:11971). **Audio has no outbox at all** —
`uploadZoneAudio` (10216) is a single `fetch` and the blob is discarded.
⚠️ The stated reason measured the wrong instrument: *"too big to buffer in localStorage"* is
true of a ~5 MB **string** quota and false of the browser. **IndexedDB stores Blobs natively**;
a 30-second Opus clip is ~60–250 KB.
- The ack gets **truer**, not weaker: *"Set down — it'll reach the record next time you're
  near the house ✓"* is honest, and it is what actually happens.
- **Done when:** a recording made with the network unreachable survives, reaches the server on
  return to Wi-Fi, and the wording never claims a save that has not happened.
- **Owner:** me. **Gate:** Paul (her surface + her wording).

### 0c · `navigator.onLine` is not a route test
At the edge of house Wi-Fi the phone reports online while requests time out. Classic
*match the payload, not the container*. Flush on panel open and on `visibilitychange`, not on
the `online` event alone.
- **Owner:** me, folds into 0b.

### 0d · An offline shell — **DECISION, not a task** `[Paul's call]` · ⏸ **DEFERRED 2026-08-31**
*Paul: decide later, it isn't blocking. Step 1 goes ahead of it.*
No service worker, no manifest, no `sw.js` — verified, zero matches. Off Wi-Fi the surface does
not degrade, **it does not load**. A cache-first SW fixes that and introduces a stale-app mode,
which is this repo's most-repeated bug class (the reason `check-live.py` exists).
- **The question:** is "she can open it in the garden and see the record" worth a stale-app
  failure mode on a surface she cannot debug?
- **Not blocking 0a–0c.** Those are worth doing whether or not this ships.

---

## STEP 1 — per-vertex provenance  ·  **before the first GPS vertex lands**

> Retrofitting provenance onto an already-mixed set is the expensive version of this job.
> It is a schema bump today and a migration later.

`zones._meta.accuracyHonesty` currently says *"if a GPS track disagrees, BOTH can be right —
different frames."* Sound hedge, but it is a statement about a **zone** and the disagreement is
about a **vertex**.

### 1a · Schema v3: provenance per vertex
`traced-naip | gps | snapped | plat`, plus reported accuracy and fix time for GPS vertices.

### 1b · A polygon's accuracy is DERIVED from its worst vertex
Never hand-written. A hand-written accuracy number is how the 86 ft elevation error survived
four months stamped `confidence: "confirmed"`.

### 1c · GPS does not automatically win
It supersedes a traced vertex **only** where its reported accuracy beats the ~±30 ft trace
budget. Open ground at 1–4 m: yes. Closed canopy at 3–11 m: **no — the trace stands.**
⚠️ Reported accuracy is a *claim*, not a measurement. iOS `horizontalAccuracy` is a ~68% model
and is routinely optimistic under canopy. **Check seen to fail:** stand still, three fixes a
minute apart; scatter wider than the reported figure means the figure is lying.

### 1d · Disagreement is RECORDED, not resolved at ingest
Same shape as `property.json` → `elevation.supersededValue`, which kept the old number, the
error, the source and the lesson. Use it as the template.

### 1e · Lines need a home in canon
`zones.json` holds polygons only. The wall, the path and the driveway currently live only in
the capture file. Canon needs a line type before the fold.
- **Blocks the fold.** ⛔ Do not fold The Path back in as a polygon to tidy the set.

---

## STEP 2 — adopt Avenza  ·  **finite, geometry only, Paul-facing**

### 2a · Verify the free tier before committing
Which export formats are free vs Pro (GeoJSON in particular) — it decides what the parser
reads. Free tier historically caps imported maps. **Fallback: QField** (open source, GeoJSON
and GeoPackage both ways) if the tier disappoints.

### 2b · Build the georeferenced export
Basemap + the 16 areas + 3 lines + the plat, as GeoTIFF/GeoPDF for the phone.
⭐ **Stamp it with the commit sha it was built from.** Prevents the stale-phone-map failure:
fold a fix in October, walk against a March export in November.

### 2c · `tools/ingest-field-capture.py`
Export → `.private/field-capture/` (gitignored — a raw track is a record of where a person
walked) → a proposal in the **format `.plans/2026-08-31-zones-traced-with-mom.json` already
uses**. Do not invent a second proposal format.
- **Rule:** the instrument never holds state canon depends on. Exports are **additive
  proposals against a named sha**, never the corrected set. Avenza vanishing then costs
  convenience, not data.

### 2d · The first walk — **the plat**
The highest-value thing GPS can do here. Walk the driveway centreline for a control line;
hunt the corners for survey monuments. Two or three found pins with averaged fixes register
the plat properly instead of by eye, and that improves everything downstream.
⚠️ **Do not plan a "walk the woods boundary" session.** Canopy double-weakness: GPS is worst
exactly where the January leaf-off aerial is also worst. Those edges stay hypotheses.
⚠️ No cell means no A-GPS, so cold fixes are slow — the first minutes of any session are the
worst data in it.

---

### 0e · `recordedAt` — when she SPOKE, not when it arrived `[BUILT 2026-08-31]`
A recording made at 4pm in the garden and flushed at 6pm at the house was being stamped 6pm.
For a field journal the observation *time* is part of the observation — "the hellebores are
up" means something different on the 3rd than on the 10th. The outbox already held the
original moment; the upload simply never sent it.
- The Worker now accepts `recordedAt`, validates it (must parse, and land inside a sane
  window — a client clock can be wrong or hostile), stores it alongside `uploadedAt`, and
  records `heldMs`. It never replaces the server's own arrival stamp; **both are kept and
  the gap between them is the honest record.**
- ⚠️ The dated index stays keyed on the **upload** date on purpose. Filing a late arrival
  under the day she spoke would read truer, but `read-mom-zone-audio.py` advances a watermark
  by date — a recording appearing in an already-passed bucket would never be surfaced, and an
  unheard recording is this project's worst failure class. File by arrival so nothing is
  missed; carry `recordedAt` so nothing is misdated; let the reader sort by it.
- **Follow-on, not yet done:** `read-mom-zone-audio.py` should display and sort by
  `recordedAt` where present, and show the held gap.

## Decisions Paul owes (not work — answers)
| # | Question | Raised by |
|---|---|---|
| D1 | Offline shell: worth a stale-app mode on a surface she cannot debug? | 0d |
| D2 | Should the 07-31 un-park trigger be re-drafted to require **her** initiation on *every* clause? A trigger that fires when you ask for it is an echo of your own question. | user-research |
| D3 | Should the zone mic stay at position 1, given it can only fail where she would use it? | user-research |
| D4 | Is the photo↔zone join the real driver for a *recurring* walk? Measurable before building: count how many of Paul's manual rulings a coordinate would have resolved. | user-research |

## Also open, deliberately not in the spine
- **Paul-relayed input has nowhere to live** (`BACKLOG.md` lap 4). ⭐ The user-research seat
  rates this **higher leverage than Avenza**: 18 names arrived through a conversation — more
  zone content than every capture surface has collected in seven weeks — and that channel has
  no record, no id, no timestamp, nothing `check-mom-ack.py` can see.
- `BACKLOG.md:842` — EXIF→zone auto-placement is killed on two reasons and **one has expired**
  (*"no georeference"* stopped being true at schema v2). The other reason stands and is
  sufficient; the row should say so before someone re-derives it from a dead premise.
- Trace the property line off the plat fit → then every named area can be tested for
  containment, which matters before anything reaches a public surface.
- Three engineering principles **proposed, not added**: per-vertex provenance · honest-vs-safe
  failure · instrument-not-system-of-record.
- Persona amendment + a JTBD card for Paul's record-repair job — offered, not written.

## Explicitly NOT doing
- A field-capture **cycle**. Geometry is finite: burn it down, no CYCLE-MAP, no probe.
- Any **live sync**. There is no network to sync over; deferred file-drop is not a compromise
  here, it is the only correct design.
- A **custom phone page**. `navigator.geolocation` is blocked on non-secure origins, so
  `zone-capture.py` on `192.168.x.x` cannot serve it, and the fix needs network the property
  does not have.
- **Re-tracing the 16 areas** to close 13.5 m² of slivers — 0.5% against a budget worse than
  ±30 ft is noise below the instrument. Snapping handles everything from here.
- A **second accuracy number** anywhere.
