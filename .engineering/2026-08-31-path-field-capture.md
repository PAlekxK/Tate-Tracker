# Path evaluation — phone field capture (Avenza vs. build vs. photos)

**Date:** 2026-08-31 · **Mode:** path-evaluation · **Repo:** Tate-Tracker (Fernwood)
**Asked:** is adopting a third-party field app (Avenza Maps) the right shape, or is it a one-off
that the wider architecture will regret?

## Founding premise, folded in mid-evaluation `[paul-stated 2026-08-31]`

> "we're limited to Wi-Fi coming from the house and don't really get cell reception … as soon as you
> get far from the house, you start to drop from coverage … And there's also heavy tree cover.
> These are all challenges we have to bear in mind and work around. I want that known from the get go."

Treated as hard, permanent constraints — not preferences:

1. **No cell service.** Wi-Fi from the house only.
2. **Connectivity is inversely correlated with distance from the house** — the places worth walking
   to are precisely the places with no network.
3. **Heavy canopy** — a GPS accuracy problem (3–11 m closed vs 1–4 m open) *and* a slower
   satellite-acquisition problem.
4. **Permanent.** Nothing whose remedy is "improve the connectivity."

**Derived criterion, now first-class:** *anything that syncs, authenticates, calls an API, or
fetches tiles at the moment of capture is disqualified in the field.* Capture is fully local;
sync is deferred and happens near the house.

The premise does more than rank the three options. It exposes that **Fernwood has no offline story
at all today**, which is a live Track-A defect, not a Track-B feature request. That comes first.

---

## Part 1 — What the premise breaks in code that already ships

### A. There is no offline shell — the app does not load past the Wi-Fi edge `[issue]`

No service worker, no web app manifest anywhere in the repo (`grep serviceWorker|rel="manifest"`
→ nothing; no `sw.js`). `viewer.html` is a 1.9 MB single file served from GitHub Pages over the
network on every cold load.

**Consequence:** if Mom walks to a zone and the tab is not already open and warm, the surface she
is meant to use *at* the zone does not exist. "Tap a zone and speak" is, today, a house-only
feature. Nothing in the repo states this.

**Why it matters more than it looks:** the whole design premise of the zone-audio journey is that
she is standing in the place she is describing. Under the connectivity premise the app is a desk
journal wearing a field journal's clothes.

**Right shape, with a caveat.** A minimal cache-first service worker over `viewer.html`,
`questions.json`, `zones.json` and the basemap solves it. But a service worker also *introduces*
a stale-app failure mode, and stale-derived-artifact is this repo's single most-repeated bug class
(the Pages async ship, the bundled Worker digest, `check-live.py`'s whole reason to exist). So it
must be stale-while-revalidate with a visible "updated — reload," and `check-live.py` has to learn
that a byte-identical Pages asset no longer proves what Mom's phone is running. **That is its own
decision and deserves its own short path-eval — do not drop a service worker in casually.**

### B. Zone audio is honest but lossy, and the premise makes loss the normal case `[issue]`

`viewer.html:10330` `stopAndUploadGrow()` → on a failed POST:

```
if (r.ok) setGrowStatus("Saved — thank you. ✓");
else setGrowStatus("Couldn't save just now — tap the mic to try again.");
```

with the design note at ~10344: *"Audio blobs are too big to buffer in localStorage like the text
outbox, so the honest ask-to-retry is the safeguard, not a silent queue — the 7/15 rule."*

The honesty is right and stays. Two things changed underneath it:

1. **"Try again" is advice that cannot succeed where she is standing.** It was written for
   *transient* failure. The premise says failure is **geographic and persistent** — retrying in the
   garden fails every time, for as long as she is in the garden. Her thirty seconds is gone. Not
   silently, but gone. *Capture must not lie* is satisfied; *capture must not lose* is not.
2. **The size argument was measured against the wrong instrument.** localStorage's ~5 MB **string**
   quota is the wrong store for a blob. IndexedDB stores `Blob`s natively and is sized in
   tens-to-hundreds of MB. A 30-second Opus clip is roughly 60–250 KB — a dozen of them is
   nothing. "Too big to buffer" is true of localStorage and false of the browser.

**Right shape:** extend the pattern this repo already proved. `MomQueue`'s text outbox
(`flushOutbox`, `viewer.html:11971`) is a durable queue that breaks on the first failure and keeps
the rest — exactly correct. Give audio the same treatment with IndexedDB as the store. The ack copy
then becomes *truer*, not weaker: **"Set down — it'll reach the record next time you're near the
house. ✓"** That is a promise the code can actually keep, and it fits "everything is changeable."

### C. Closing the sheet mid-recording is a genuine silent-loss path `[issue]`

`ZonePanel.close()` (~`viewer.html:10382`):

```
// Capture-first: if she closes mid-recording, save what she said (don't lose it).
if (_growRec && _growRec.isRecording()) { stopAndUploadGrow(); }
```

Fire-and-forget, while the panel is being torn down. `stopAndUploadGrow`'s status line writes into
a sheet that has already lost `.open`. **Online this is harmless. Offline the upload fails and she
never sees the failure** — the one path where the recording disappears without the honest ack the
whole design rests on. The intent ("don't lose it") is right; the premise turns it into the
opposite. The fix falls out of B: with a durable outbox there is nothing to lose and nothing to report.

### D. `navigator.onLine` is not a route test `[suggestion]`

`flushOutbox` is triggered on the `online` event. At Fernwood the phone will associate with house
Wi-Fi at the edge of range and report `onLine === true` while requests time out. This is the repo's
own **match the payload, not the container** — `onLine` reports a *link*; the payload question is
*can I reach the Worker*. `flushOutbox` already handles a failed flush correctly (break, keep the
rest) — that is the load-bearing half and it is right. It needs a second trigger though: flush on
app open and `visibilitychange`, not only on the `online` event.

**Praise, explicitly:** the text-capture path is genuinely well built — durable outbox, three
honest ack states, `keep` on failure so her words are never wiped while being told they are safe,
the `< 1500` byte empty-capture guard. The offline gap is a premise change, not sloppiness.

---

## Part 2 — Finite or cyclical? **Finite.** And the distinction is the load-bearing answer.

Two different things are being bundled under "field capture":

**(a) Fixing the geometry record** — 16 areas, 3 lines, the driveway, the plat registration, the
property line. The wall is not going to move. Each edge is walked once, corrected once, done.
There is a definable end state: *every boundary that matters is either walked or explicitly ruled
not-worth-walking*. → **FINITE. Burn it down.** No CYCLE-MAP, no state file, no probe, no beat 0.

**(b) Observing the property over time** — what is blooming, where the seep appeared, what is
growing here. → **Cyclical, and it already has a loop, a surface, and a channel doctrine.**

**The architecture risk is adopting "a field capture app" as a *category*, because (b) then drifts
into it.** That would stand up an observation channel outside the loop's reach — and this repo has
measured that exact failure three times in a single day (zone audio absent from the session-start
block, `telemetry-walk.js` unnamed for 16 days, weather completeness living outside the loop).
*A channel the loop cannot reach by running its own procedure is not a channel the loop has.*

**Scoping rule:** Avenza carries **geometry and only geometry**. It is never an observation
channel and Mom never touches it.

The premise sharpens this rather than softening it. The tempting shortcut — "her app doesn't work
in the garden, so let her use the field app out there" — would solve her offline problem by moving
her *off* Fernwood, which is precisely what the channel doctrine forbids. **The premise makes
fixing Fernwood's offline story mandatory; it must not become a reason to outsource her.**

Does the premise change finite/cyclical? No. It changes *cadence*: sessions batch — walk with no
network, reconcile at the house. That is not a loop, it is just how a finite burn-down runs here.

---

## Part 3 — The three options against the premise

| | **Avenza Maps** | **Phone page off the local server** | **Geotagged photos only** |
|---|---|---|---|
| Works with **zero network** in the field | ✅ by design — offline raster maps, on-device GNSS | ❌ needs the laptop over Wi-Fi | ✅ camera is fully local |
| Needs the house Wi-Fi at capture | No | **Yes — the thing you are walking away from** | No |
| Secure-context blocker | n/a | ❌ **`navigator.geolocation` is blocked on `http://192.168.x.x`.** `zone-capture.py` is `http.server`; a phone hitting it over LAN gets no geolocation at all. Fix = HTTPS cert or a tunnel — and a tunnel needs network the property does not have | n/a |
| Trace a line / boundary | ✅ | ✅ if built | ❌ |
| Accuracy control (averaging, reported accuracy, re-fix) | ✅ built in | build it | ❌ none exposed; EXIF may carry a stale fix |
| Canopy behaviour | same physics, but shows you the reported accuracy | same physics, hidden | same physics, hidden |
| Dependency held over canon | **none** if ingest is a file drop | none | none |
| Complexity added | one export format + one ingest script | HTTPS, offline tiles, background GNSS, screen-lock, averaging UI | zero |
| Future-Paul-with-Claude legibility | high — one script, one schema, one fold | low — bespoke geo plumbing nobody remembers | high |
| Learning value | moderate and *real* — georeferenced rasters, datums, error budgets, export formats | high but spent on plumbing, not on the problem | low |
| Effort | **low** | **high, and lands on a worse instrument** | zero |

**The custom page is not a close second — it is architecturally inverted against the premise.** It
depends on a laptop server reachable over the Wi-Fi you are deliberately walking away from, and it
cannot even read GPS from an `http://` LAN origin. **Do not build it.**

**Geotagged photos are not a competitor.** They answer a different question ("what is here /
which zone is this in") and stay where they are — the existing photo-organizer contract. Note their
real limit: a photo records *where the photographer stood*, not where the thing is, and phone EXIF
may carry a stale fix. Fine at zone granularity; useless for an edge.

**Avenza is the only option that survives the premise** — and the premise is the strongest argument
*for* a third-party field app, not against one. Offline-first mapping is exactly what those apps
are for, and building it is months Paul would spend not being on the property.

### The dependency question, answered directly

**Avenza is an *instrument*, not a system.** Fernwood already depends on third-party instruments —
the Ambient Weather station, NAIP, USGS 3DEP, Open-Meteo. Paul does not build his own anemometer.
The rule that actually protects the stack is not "avoid third parties," it is:

> *The instrument never holds state that canon depends on. What the instrument said is recorded
> here, deterministically ingested, and the fold is a separate human act.*

Under a file-drop ingest, Avenza disappearing costs a capture convenience, not data. The only way
it becomes a regret is if geometry starts being *edited* there and that copy becomes the truth —
see failure mode 6.

### Two things to verify before committing

- **Free-tier export formats.** Avenza's free plan caps stored maps (3 at a time — fine for one
  property). I am **not certain** which export formats are free vs Pro; placemark export to
  KML/CSV I believe is free, GeoJSON/SHP may not be. Check before writing the ingest — it decides
  what the parser reads. Not fatal either way (KML → GeoJSON is trivial), but do not assume it.
- **Fallback if the tier disappoints: QField** (open-source QGIS field app, offline-first,
  GeoPackage/GeoJSON native). More capable, heavier learning curve, drags QGIS into the stack.

### Getting the basemap in is cheap

`images/property-map/base-naip-2022-01-leafoff.bounds.json` + `zones._meta.bounds` already hold the
georeference, and the NAIP source is a public COG. No GDAL or rasterio installed today, but a
GeoTIFF is a `pip install rasterio` and a dozen lines, or a direct refetch of the COG window.

---

## Part 4 — Ingest, schema ownership, and disagreement

### Where ingest lives

```
Avenza export  →  .private/field-capture/<date>-<session>.<ext>     (raw, untouched, gitignored)
               →  tools/ingest-field-capture.py                      (deterministic, AI-FREE)
               →  .plans/YYYY-MM-DD-<subject>.json                   (plan-shaped PROPOSAL)
               →  Paul folds by hand                                 (the existing reviewed act)
               →  zones.json
```

- **`.private/` is already gitignored** — no change needed, but the *reason* should be written
  down: an export contains a timestamped track of where a person walked. That is location data
  about a human sitting in a public repo's working tree, and this repo has already paid for one
  `filter-repo` (VINs, 2026-06-12).
- **The ingest emits into the shape `.plans/2026-08-31-zones-traced-with-mom.json` already uses.**
  Do not invent a second proposal format — the fold step should be the fold step Paul already has.
- **The exported map file carries the commit sha it was cut from**, in the filename and a sidecar.
  That is the entire defence against failure mode 5.

### Who owns the schema

`zones.json` `_meta` (v2 today). Nothing else mints a coordinate definition. `.plans/*` is staging.

### The thing to build FIRST: per-vertex provenance (schema v3)

`zones._meta.accuracyHonesty` currently says:

> *"If a GPS track ever disagrees with a boundary by metres, BOTH can be right — different frames."*

Good hedge in July. **Insufficient now**, because it is a statement about a *zone* and the
disagreement is about a *vertex*.

**The failure to prevent:** a polygon whose vertices came from two instruments with different error
models, with nothing on the record saying which is which. Such a polygon has **no statable
accuracy**, and the next reader inherits the tightest-sounding number. This repo has already been
burned by exactly that shape — `elevation.confidence: "confirmed"` on an Open-Meteo model read, 86 ft
wrong, held for four months.

**Retrofitting provenance onto an already-mixed set is the expensive version of this job.** Doing
it now, before the first GPS vertex lands, is a schema bump and a script.

Each vertex carries its source — `traced-naip` | `gps` | `snapped` | `plat` — and for GPS the
**reported** horizontal accuracy in metres, the fix time, and (if averaged) fix count and scatter.
Three rules fall out:

1. **A polygon's stated accuracy is DERIVED from the worst of its vertices, always.** Never a
   hand-written per-zone accuracy string. One derived statement, N readers — the same argument
   CLAUDE.md makes for not writing a local weather-completeness check.
2. **GPS does not automatically win.** It supersedes a traced vertex only where its reported
   accuracy beats the trace budget (~±30 ft / 9 m). Open ground at 1–4 m: wins comfortably.
   Closed canopy at 3–11 m: **it does not**, and the traced vertex stands. This is the mirror of
   the rule already in CLAUDE.md ("a measured signal must never be silently replaced by a modelled
   one") — here: *a measured signal must never silently replace another measured signal without
   recording which instrument said what, and how well.*
3. **Disagreement is RECORDED, not resolved at ingest.** Keep both, surface the delta, let the fold
   decide — the same shape as `property.json`'s `elevation.supersededValue`, which kept the old
   number, the error, the source and the lesson. That entry is the best thing in the file and it
   should be the template.

**And the honesty check on the GPS number itself:** reported accuracy is a *claim*, not a
measurement. iOS `horizontalAccuracy` is the device's own ~68% model and is routinely optimistic
under canopy — squarely inside Paul's standing "model-read values are hypotheses until verified."
**Cheap check seen to fail:** on any point that matters, stand still and take three fixes a minute
apart. If they scatter wider than the reported accuracy, the reported accuracy is lying, and the
record should say so. Three minutes, and it is the difference between a number and a measurement.

---

## Part 5 — Failure modes

1. **Silent loss of Mom's zone audio in the field.** Live today (B / C).
2. **The app does not load past the Wi-Fi edge.** Live today (A).
3. **Mixed-provenance polygons with no per-vertex source.** The expensive one. Preventable this week.
4. **The accuracy ratchet** — the stated budget silently tightens from ">±30 ft" to "GPS" because
   GPS *feels* authoritative (seven decimal places), and a downstream consumer (Guru, an acreage,
   a median slope) starts treating an edge as real. Prevented by rule 1 above.
5. **The stale phone map** — corrections folded in October, walked in November against a March
   export, and "corrected" against geometry that was already fixed. Same shape as the Pages-async
   and bundled-digest failures. Prevented by the sha stamp.
6. **The second writer** — geometry edited inside Avenza becomes a divergent copy nobody diffs.
   Prevented by: exports are **additive proposals against a named sha**, never "the corrected set."
7. **Canopy double-weakness** — GPS is worst (3–11 m) in exactly the places the leaf-off aerial is
   also worst (long January shadows, no detail underneath). Both instruments fail in the same
   place. Nothing fixes this. **The wooded edges stay hypotheses**, and nobody should plan a "walk
   the woods boundary" session expecting a resolution it cannot deliver. What GPS actually buys is
   the **open** ground — driveway, patios, parking bank, fairway, the garden complex — where 1–4 m
   is genuinely 3–8× better than the trace.
8. **Location data about a person in the working tree.** Prevented by `.private/`; write down why.
9. **Slow first fix under canopy with no assisted-GNSS.** No cell means no A-GPS almanac download.
   Cold fixes will be slow and the first minutes of a session will be the worst data of it.
   Practical, not architectural: turn the phone's GPS on in the open before walking in, and
   discard the first fix at every stop.

---

## Part 6 — What I would NOT build

- **The phone-friendly page off the local server.** Dead on the secure-context blocker, and
  architecturally inverted against the premise. Drop it.
- **A field-capture cycle.** No CYCLE-MAP, no state file, no probe, no beat 0. This is finite.
- **Any live sync between phone and repo.** There is no network to sync over. Deferred file-drop is
  not a compromise here — it is the only correct design.
- **EXIF → zone auto-placement.** Still killed. ⚠️ **But one of the two reasons it was killed on has
  expired.** `BACKLOG.md:842` gives "no georeference" — zones have been real WGS84 since v2. The
  second reason ("don't automate the highest-ownership moment") stands and is sufficient on its own.
  **Re-state the row** so a future reader does not re-derive it from a reason that is no longer
  true. If it ever returns, the right shape already exists in this repo: the deterministic join
  *proposes*, Paul confirms — the `vehicles.json` ↔ photo-organizer contract.
- **Re-tracing the 16 areas to close the 13.5 m² of slivers.** 0.5% of area on a record whose stated
  budget is worse than ±30 ft — noise well below the instrument. Snapping handles everything from
  here. Drop it.
- **A second accuracy number anywhere.** One derived statement, N readers.

---

## Part 7 — Recommended order

0. **Fix the offline defects on Mom's surface before adding any new field capability.**
   B + C together (IndexedDB outbox for audio + honest deferred-sync ack) — small and self-contained.
   A separately; it needs its own short decision because a service worker adds a staleness mode.
1. **zones schema v3 — per-vertex provenance + derived accuracy.** Before a single GPS vertex lands.
2. **Then Avenza,** narrowly scoped: verify the export tier → make the GeoTIFF → one walk → one
   ingest script → fold by hand.

### The highest-value first walk, concretely: **the plat**

The plat is eye-fitted against the driveway and its bearings are not legible in the photo. GPS on
**open** ground is the one instrument that can improve that registration. Walk the driveway
centreline (open, 1–4 m) for a control line, and hunt the corners for survey monuments — a found
pin with three averaged fixes is a real control point. Two or three of those and the plat is fitted
properly instead of by eye, which improves everything downstream of it. Finite, offline-native,
and neither of the other two options can deliver it.

---

## Principles proposed (NOT added — awaiting Paul's confirmation)

**1. Provenance rides the smallest unit that can disagree** — scope: cross-project
*Statement*: When two instruments can contribute to the same record, provenance and error attach to
the smallest element that can differ between them — a vertex, not a polygon; a field, not a file —
and the record's stated confidence is DERIVED from the worst of its parts, never hand-written.
*Why*: A mixed-provenance record has no statable accuracy, and the next reader inherits the
tightest-sounding number. Retrofitting provenance onto an already-mixed set is the expensive
version of the job. Precedents in this repo: the 86 ft elevation error carried as
`confidence:"confirmed"`, and the traced-vs-GPS vertex problem this evaluation is about.
*Avoid*: A per-record confidence string. Overwriting one instrument's value with another's without
keeping both. Letting the more precise-looking number set the stated budget.

**2. An honest failure is not a safe failure when the failure is structural** — scope: cross-project
*Statement*: "Tell the user it failed and let them retry" is only sufficient when the failure is
transient. Where a failure is determined by the environment (no coverage, no permission, no disk),
retry cannot succeed, and the capture must be made durable locally and synced later.
*Why*: Fernwood's zone-audio path satisfies *capture must not lie* and fails *capture must not lose*
— honest copy, permanently unreachable remedy. The distinction only becomes visible once the
failure's cause is known to be structural.
*Avoid*: Copy that says "try again in a moment" for a condition that will not change. Ruling out a
durable queue on a storage limit measured against the wrong store.

**3. A third-party app may be an instrument, never a system of record** — scope: cross-project
*Statement*: External tools are allowed to *measure*; they are not allowed to *hold* anything canon
depends on. What the instrument said is exported, ingested deterministically into our schema, and
folded by a human. Losing the tool costs convenience, never data.
*Why*: It converts the usual "should we take this dependency" argument into a checkable test —
*if this vendor vanished tonight, what is gone?*
*Avoid*: Editing canon inside the third-party tool. Round-trip sync. Treating the tool's export as
the record rather than as evidence.
