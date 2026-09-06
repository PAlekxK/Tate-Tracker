# MAPS & ZONES — where this feature sits in the concept-to-testing pipeline, and the artifact shape that would hold it · AUDIT + METHOD RECOMMENDATION

- row: process (no BACKLOG row yet — same posture as the 09-03 readiness, 09-05 registry and 09-05 journey proposals)
- objective: O5
- class: engine · declared (process machinery; no Fernwood content is ranked here)
- seats: practice-steward (this file)
        user-researcher → cited, not commissioned: `.user-research/2026-07-17-zone-journey-panel-synthesis.md` — §2 reads its SHAPE and its expiry, never its findings
        engineering-partner → deferred: F6's tenancy leak and M4/M5/M6 have code consequences; nothing is designed here
        content-steward → deferred: the `map-zones` onboarding promise (§6b) is a wording ruling, its and Paul's
        ux-expert · ai-advisor → waived: no surface is proposed and no model is on any path in this file
- depends-on: .plans/2026-09-06-one-environment-DECISIONS.md
- depends-on: .plans/2026-09-04-map-region-smoothing-PLAN.md
- depends-on: .plans/2026-09-05-journey-as-prioritizer-PROPOSAL.md
- depends-on: .plans/2026-09-05-state-of-the-work-PROPOSAL.md
- ready: agent-proposed 2026-09-06 — **Paul rules**
- stage: audit — ⚠️ **SIXTH file to need a `stage:` word that does not exist.** `tools/check-backlog-ready.py:46` reads `STAGES = ["ready","concept","build","qa","shipped","retro"]`. §5c proposes the two words that would end this, and it is the smallest edit in the file.

> **Method only. This file ranks no feature, no zone and no finding.** It says where map/zone work sits
> against the pipeline this repo actually runs, what that pipeline is missing, and what artifact shape
> would hold a feature that has a vision, a current state, and both investigations and improvements.
> ⛔ It never says which thread should be built, whether the zone hold should lift, or which of the
> eleven slivers abut. Where a call turns on real-world context only Paul has, it is in §8.
>
> **Nothing here is committed and nothing outside this file is written.** Another session holds this
> repo tonight.

---

## 0 · THE ONE-SENTENCE ANSWER

> ### Map & zone work sits at a stage the pipeline does not have a word for, is measured by an instrument no procedure runs, and is gated by a hold whose own written trigger fired six days ago and was never re-read.

Everything below is that sentence with evidence, plus the artifact Paul asked for in the mid-session
amendment, which turns out to be the answer to why all three are true at once.

---

## 1 · THE PIPELINE AS IT ACTUALLY EXISTS

⭐ **C2 says *"there is no feature development process."* Measured today, that is half right, and the
half it gets right is the half map/zone work lives in.**

### 1a · There are FOUR pipelines, and only one of them is executable

| # | pipeline | declared where | enforced by | covers |
|---|---|---|---|---|
| **P1** | `ready → concept → build → qa → shipped → retro` | `tools/check-backlog-ready.py:20`, `:46` | ✅ **executable** — `:209` illegal stage, `:212` stage past `ready` with no `ready: [paul-approved …]` stamp, `:215` `shipped`/`retro` with no `## Retro` | `.plans/*-PLAN.md` **only** |
| **P2** | the **release cascade** — gate 1 synthetic/bare-logic → gate 2 Paul in lab → gate 3 Mom | `.plans/2026-09-04-three-environments-PLAN.md` § RELEASE CASCADE | partial: `journey-logic.py`, `walk-integrity.py`, `qa-divergence.py`, `check-live.py` | onboarding journey; **no zone surface is in the journey set** (`journey-test-cycle` §1c lists six files; none is `zones.json`, `area-trace.html` or the map renderer) |
| **P3** | **concept review** — `/design-options` exhibits on the live app | `CLAUDE.md` ×1, `BACKLOG.md` ×3, `MOM-CYCLE-MAP.md` ×1 | ⛔ **nothing.** No checker, 0 mentions in the `/mom-cycle` procedure (C2, and its own correction: ~3 runs, last 2026-08-14, **every one Paul-initiated**) | nothing, currently |
| **P4** | **holistic UX sweep** — un-primed pass + principles-informed pass | `CLAUDE.md`, `MOM-CYCLE-MAP.md` | ✅ `check-ux-sweep.py` (accumulation trigger) | the viewer surface generally |

### 1b · The defect is not coverage. It is that P1's first two words have no instrument behind them.

`ready` is a human stamp. `concept` is accepted by the parser and checked by nothing. Every mechanical
gate in P1 fires at `build` or later (`:212` requires the stamp *past* ready; `:215` requires a retro at
`shipped`). **So the pipeline is a DELIVERY pipeline wearing a concept-shaped first half**, which is
exactly what Paul described on 2026-09-02: *"approved backlog row → design and concept → code →
implementing and testing it fully in the larger stack."* The back three arrows are instrumented. The
first one is not.

**Measured stage distribution across all 50 `.plans/*.md` (`grep -h "^- stage:"`):**

| word | count | legal? |
|---|---|---|
| `concept` | 5 | ✅ |
| `ready` | 4 | ✅ |
| `draft` | 6 | ⛔ **illegal** (2 self-flag it in their own header) |
| `build` | 3 | ✅ |
| `audit` | 3 | ⛔ **illegal**, all three self-flag |
| `design` | 1 | ⛔ **illegal**, self-flags |
| `qa` | 1 | ✅ |
| `retro` | 1 | ✅ |
| `shipped` | **0** | — |

⭐ **Ten files carry a word the enum does not have, every one of them announces that in its own text,
and the enum has not moved since 2026-09-03.** A self-indicting document is this corpus's own idiom and
it is working — the flag is loud and nobody has ruled. **That is a gate-capacity finding, not a
discipline finding**, and §5d is where it lands.

### 1c · And the instrument cannot see the artifacts that await a ruling

`check-backlog-ready.py:132` / `:217` glob **`.plans/*-PLAN.md`**. There are **16 `*-PROPOSAL.md`** files
and **15 files carrying `ready: agent-proposed … Paul rules`**. Verified by execution: the checker's
flags name only `-PLAN.md` files.

**This is already reported** — `.plans/2026-09-05-state-of-the-work-PROPOSAL.md` §1a, whose fix is three
edits and no new file. ⭐ **And that proposal is itself unruled, which makes it an instance of its own
finding.** I do not re-derive it; I note that map/zone's single largest artifact
(`2026-09-04-map-region-smoothing-PLAN.md`) *is* in the glob and *is* invisible for a different reason:
it carries no `- stage:` and no `- objective:` header at all.

---

## 2 · THREAD-BY-THREAD PLACEMENT

**Reading key.** *Stage* is placed against P1's enum where one fits and named honestly where none does.
*Gate passed / not passed* names the specific act, not a judgment of importance.

### T1 · Basemap acquisition
- **Stage:** `build`, blocked on a flaky third-party dependency (Earth Web wedges on splash; recovers in 60–90 s, did not on three attempts).
- **Where it lives:** `BACKLOG.md` § BASEMAP & LAND-DATA SESSION (:769) — a session dump with its own ordered queue, "🔜 OWED — next steps, in the order they are worth doing," items 0–7.
- **Passed:** the finding that reframed it (at 34.55°N leaf-off and overhead sun cannot co-occur; 1 of 7 NAIP flights is leaf-off, at the lowest sun of all seven, 1.52× shadows). The arithmetic for the fix (one ~350 m capture at 0.22 m/px covers all 23 zones). Registration solved and reusable (`register-gearth-frame.py`).
- **NOT passed:** ⛔ **no gate exists to pass.** No plan file, no `- stage:`, no `- objective:`, no `ready:` stamp. It is a BACKLOG prose section, so P1 cannot see it and P2 does not cover it.
- **Structural note:** item 1 records *"the 2018 frame covers 74%, not 100%"* with an explicit **"Decide which before trusting it for the northern zones"** — a decision with no decision-maker named and no artifact that would carry the answer.

### T2 · Polygon tracing
- **Stage:** the *act* is done; the *feature* has never left `concept` by its own field.
- **Measured at HEAD:** 23 zones · 437 vertices · schema v3 · **23 of 23 `status: draft`** · 6 tombstones · median segment 2.57 m against a stated ±9.1 m budget.
- **Passed:** trace, fold, round-trip (`kml-to-zones.py` dry run reports no geometry change against `exports/fernwood-zones.kml`), boundary sanitization in the Worker (reject-never-clamp).
- ⛔ **NOT passed — and this is the cleanest unfired gate in the whole feature: `status` IS the confirmation gate, and it has never fired once.** Not one zone has moved `draft → confirmed` since the field existed. Every downstream consequence flows from it: the whole map renders dashed (`.pmap-zone.is-draft`, dash `10 7`), which BACKLOG:133 records as a defect and which the map-smoothing plan §7 step 3 records as *"Paul's authoring call, not an agent's."*
- **Reachability:** `tools/area-trace.html` is named in 7 `.md` files and **0 skills, 0 commands, 0 procedures**.

### T3 · Zone naming
- **Stage:** `shipped` (data), and the loop leg that closes it is open.
- **Passed:** capture (2026-08-30, sixteen areas named unprompted), fold to canon (08-31), tombstones so cached devices drop retired ids, live verification (`/api/zones` served 18 with `_deleted` intact).
- ⛔ **NOT passed — Z-ACK.** BACKLOG:1453: the largest single contribution Mom has made has never been acknowledged. Gated on **"zone work ready to distribute."**
- ⚠️ **The release condition has no definition and no owner.** Nothing in the repo says what "ready to distribute" means, nothing computes it, and no tool reports it. Compare `.plans/2026-09-06-one-environment-DECISIONS.md` R1, which states a release condition in testable form (*"one production environment is live AND `T2` has passed on synthetics"*). ⭐ **That is the shape a hold's release condition takes in this repo when it is written well; Z-ACK's is not written that way.** Whether it should lift is Paul's; that its trigger is unevaluable is method.
- **And it has no arrival record at all** — no id, no timestamp, no channel; it happened on paper at a kitchen table. This is the biggest instance of the standing "Paul-relayed input has nowhere to live" finding (BACKLOG:133 region, lap 4).

### T4 · Zone rendering (the reading surface)
- **Stage:** `qa`. Tier-1 steps 1–2 built, verified, deployed to `fernwood-qa` (`cb18ade`; origin serving `e8f1b78abb82`, byte-matching HEAD, 2026-09-04 ~3:25 PM ET). Lane D **CLOSED**.
- **Passed:** the lane's own gate; the edit-target trap was caught in-lane (`viewer.html` is generated — edit `engine/viewer.template.html`, rebuild, prove with `build-viewer.py --check`).
- **NOT passed:** production. And **step 3 — the dash — was deliberately excluded and has not been asked.** Lane D: *"⛔ The honesty rule that put the dash there must not be reversed by an agent. ASK him; do not act."* The ask has no owner and no artifact.
- ⭐ **This thread is the only map/zone work in the last two months that ran through a declared gate with a written release** — because Paul greenlit it as its own lane (`[paul-greenlit 2026-09-04]`). That is evidence the machinery works when work is admitted to it.

### T5 · Topology / smoothing
- **Stage:** `concept` for Tier 2, held for Tier 3. Research complete and reproducible.
- **Passed:** a measured plan with a positive control; a ruling that pre-empts the obvious wrong move (snap tolerance is bounded by *vertex spacing* ~0.5 m, not by the ±9.1 m accuracy budget — at 2 m one cluster swallows 119 of 437 vertices and drags points 20 m); Paul's own ruling that the 11 slivers are a genuine mix, which **removes any global tolerance as a legal option**.
- **NOT passed:** Tier 2 (a reviewed data pass) is unruled. Tier 3 is blocked on adjacency + lines + a seven-consumer schema migration.
- ⭐⭐ **And the instrument he asked for EXISTS and is unreachable.** `tools/zone-topology-report.py`, added 2026-09-04 (`e99cb49`), consolidates the four throwaway scripts that produced the plan's numbers, carries a positive control (`the-green` inside `the-turf` = 60%, matching the record's own claim), and is READ-ONLY by design. **It is named in 0 `.md` files, 0 skills and 0 commands** — verified two ways (a `--include='*.md'` grep across the repo, and a filename-stem grep of `~/.claude/skills` and `~/.claude/commands`). It runs correctly today; I ran it.

### T6 · Linear features (walls, paths, the driveway)
- **Stage:** captured, **not in canon**. This is a deferral whose gate has fired.
- **Evidence:** `.plans/2026-08-31-zones-traced-with-mom.json` carries a top-level `lines` key (verified). `zones.json` does not (`'lines' in data → False`). `_meta.fold_2026_08_31` defers lines *"until a schema v3 adds them."* **`_meta.schemaVersion` reads 3. v3 shipped, added `partOf`, and did not add lines.**
- **Passed:** drawing (open polylines with snapping, `badf097`), and the modelling finding that governs it (*"a shared border IS a line"* — 87% of all measured overlap was The Path, a line modelled as a polygon).
- **NOT passed:** the save path. `handleZoneSave` rebuilds `{_meta, zones}` wholesale, so any other key is silently dropped on the next editor save. **A save-path problem, not a drawing problem.**

### T7 · Point annotations
- **Stage:** Paul scoped it 2026-09-04 as *"probably worth its own individual discovery research journey"* `[transcript-UNVERIFIED]`. Captured in `PRODUCT-ENGINE.md` §⑤. **Not started.**
- ⭐ **But the taxonomy already exists, built before he asked for it.** `tools/zone-capture.html:224-233` declares eight types — `structure · water · access (road/gate) · utility · planting (tree/bed) · boundary · terrain · story` — each with a key binding and a colour, plus `mode = "point"` (`:237`, `:593`). Added 2026-08-31.
- **NOT passed:** nothing. It is in an operator tool, has no representation in canon, no renderer on `viewer.html`, and no path to either.

### T8 · Photo → zone join
- **Stage:** `retro` in substance — investigated, measured, ruled, closed with a negative result.
- **Passed, and this is the strongest closing act in the whole feature:** the join has a measured floor (`st-francis-garden` ↔ `eastern-patio` centroids 5.9 m apart, less than either zone's own width, against a ±9.1 m budget; **12 of 18 zones sit in at least one such pair**), and Paul ruled 22 cards in one sentence that falsified the polygon's answer. The three limits were separated (polygon accuracy / resolution / camera≠subject) with an explicit warning that conflating (1) and (2) produces a re-trace that feels like progress and changes nothing.
- **NOT passed:** the **reverse join** — *"a photograph he has attributed is evidence about where a boundary actually runs"* — recorded in the BACKLOG's own words as *"a real proposal and nobody has built it."* It has no row, no stage, no owner.

### T9 · Zone audio / feedback capture
- **Stage:** `shipped` and **wired**. The only map/zone thread inside a running procedure.
- **Passed:** durable AI-free capture (`/api/zone-audio`); in the `CLAUDE.md` session-start block since 2026-08-14 by Paul's instruction; per-record dispositions enforced since 2026-08-28 (`check-arrival-dispositions.py`, keyed on `(channel, record id)` so a watermark cannot step over one); `ZoneAudioOutbox` (IndexedDB) so a failed recording is queued, not lost.
- **NOT passed:** photos. `attachedImage` is an in-memory dataUrl with no key in `STORAGE_KEYS` — durability not established either way (BACKLOG W3 amendment, 2026-09-05).
- ⭐ **Why this one is wired and the other nine are not is the whole audit in one comparison:** it was named in the session-start block by an explicit Paul instruction after a channel went three-recordings-unlistened. Nothing generalised from that fix to the rest of the feature.

### T10 · Zone journey / front door (the experiment)
- **Stage:** `shipped` (v1, 2026-07-17, `b52ce03`, `flowId` funnel live — 18 occurrences in the template) with a **pre-registered verdict that has never been recorded.**
- ⛔ **TWO windows and TWO verdict schemes exist for one experiment, and neither has produced a verdict:**

| scheme | window | verdicts | where |
|---|---|---|---|
| original | 4 weeks from **2026-07-13** → closed **2026-08-10** | GROW / HOLD / KILL | `.user-research/2026-07-17-zone-journey-panel-synthesis.md`; implemented in `tools/read-mom-funnel.py:88-90` (`TIMEBOX_START="2026-07-13"`, `TIMEBOX_WEEKS=4`) |
| restack | 2026-07-29 → **2026-09-09** (6 weeks), session-grain denominator, ≥15 qualifying exposures | GROW / KILL / **HOLD** / **INVALID** | `research/2026-07-28-zone-journey-restack.md` — proposed to Paul as a decision, never answered |

- **The tool implements the retired one.** `weeks_left = max(0, 4 − day_n/7)` has read `0.0` since 2026-08-10 and will forever.
- ⭐⭐ **And the verdict is unreachable from the loop's own procedure.** `CLAUDE.md`'s session-start block calls `read-mom-funnel.py --rotation`. `--rotation` branches at `:480` and **returns before** the scorecard, the verdict and the time-box line are ever printed. So the session that runs every check in the block still never sees H1–H5.
- **The window that is still live closes in three days** (2026-09-09), and its `INVALID` clause fires if `metricsExclude` was never set — which the restack says was *"provably never applied."* Deterministic exclusion later shipped via `people.json` `excludeFromEngagement`, so the clause may be moot; **nothing has checked.**
- ⚠️ **One claim in BACKLOG:133 that I checked and that SURVIVED:** *"the front door has 0 taps from her device."* The 2026-07-28 attribution correction changed the *denominator* (offered 5, not 33) but not the tap count. I flag it because the row's neighbouring "10 zones" figure did not survive (§3, F5) and it would have been easy to condemn both.

### T11 · Zone as an onboarding module
- **Stage:** promised on a live QA surface. `onboarding/index.html` — `map-points` "Marking spots on the map" (`:874`, `soon: true`) and `map-zones` "A map you draw yourself · Trace your own areas onto a photo of your place, then fill them in" (`:877`, `soon: true`).
- ⚠️ **And a third one is NOT gated:** `garden` (`:865`) declares `builds: ["plant","weed","zone","care-calendar"]` with **no `soon` flag** — so `zone` is a build target on a row presented as available.
- **Passed:** it is instrumented (`read-onboarding.py` reports what people ranked).
- **NOT passed:** nothing behind it is per-household (F6), and §6 shows Paul's 09-06 ruling has just made `map-zones`'s own sentence describe the long-term product rather than the near-term one.

### T12 · Zone consolidation (Z2)
- **Stage:** surveyed 2026-09-02, **nothing consolidated, nothing written.**
- **Passed:** the survey, plus a near-miss caught before it propagated (*"the card Mom is most likely to see asks about a deleted zone"* — checked, false, `entityRef` is a plant).
- **NOT passed:** Paul's "recent draws" are still unlocated (not in the KML, not in `.private/zone-capture`); the rename pairs are unresolved; and the fairway retirement's downstream — **78 orphaned photo tags, a routed species, a roster entry, a card id** — is unruled. The generalisable finding is already stated there: **retiring a zone is not one act.**

---

## 3 · STRUCTURAL FINDINGS

### F1 · ⭐⭐ The feature is unreachable by the loop's own procedures — and the CONTROL that exists to catch that is blind to it by construction

`tools/check-cycle-map.py:41` declares `TOOL_GLOBS = ("check-*.py", "read-*.py", "test-feedback-cycle.py",
"fold-answer.py", "mom-cycle-status.py", …)` plus `.js`. **Every map/zone tool is outside it by filename
shape:**

| tool | added | named in `.md` | in a skill / command | in a procedure |
|---|---|---|---|---|
| `zone-topology-report.py` | 2026-09-04 | **0** | 0 | 0 |
| `area-trace.html` | 2026-08-31 | 7 | 0 | 0 |
| `zone-capture.html` / `.py` | 2026-08-31 | 4 / 2 | 0 | 0 |
| `zones-to-kml.py` | 2026-09-01 | 5 | 0 | 0 |
| `kml-to-zones.py` | 2026-09-01 | 4 | 0 | 0 |
| `register-gearth-frame.py` | 2026-09-01 | 2 | 0 | 0 |
| `fetch-trace-hires.py` | 2026-09-01 | 2 | 0 | 0 |
| `fetch-basemap.py` | — | 4 | 0 | 0 |
| `fetch-historical-topo.py` | 2026-09-01 | 3 | 0 | 0 |
| `draw-zones.py` | 2026-05-19 | 3 | 0 | 0 |

**Ten tools. Zero flagged.** Running `check-cycle-map.py` today returns three findings, all about
`check-*`/`read-*` files, none about any of the above.

⭐ **This is the SIXTH recorded instance of the shape `CLAUDE.md` names three times in its own text**
(`/ux-sweep` unreachable for 21 days · `telemetry-walk.js` unnamed for 16 · weather completeness outside
the loop · the four onboarding tools caught same-day 2026-09-06). **The difference here is that the
detector was already built and could not see it** — its predicate is a *filename pattern* standing in
for a *semantic* question ("does this serve a procedure?"). Map/zone tools are `.html`, `zone-*`,
`fetch-*`, `draw-*`, `register-*` and `kml-*`. Not one starts with `check-` or `read-`.

⚠️ **Falsifier for the fix, stated because widening a glob is the obvious move and may be wrong:** if the
glob is widened and it fires on `draw-zones.py` (a 2026-05 fractional-coordinate prototype that is
genuinely finished), the glob is still the wrong predicate and the right one is a per-tool header
declaration (`# loop: no — <reason>`), read the way `NOT_IN_LOOP` is read today.

### F2 · ⛔ A deferral whose gate has FIRED — three times in one feature, all failing in the safe-looking direction

| # | the park | its own stated trigger | did it fire? | did anything notice? |
|---|---|---|---|---|
| **a** | `BACKLOG.md:133` — *"hold this AND every other zone thread"* `[paul-stated 2026-07-31]` | **"a zone named or corrected in her own words"** (also: a zone-audio recording she initiates · a Guru question about a zone · anything she says to Paul about the map) | ✅ **2026-08-30 — sixteen areas, unprompted, folded to canon 08-31** | ⛔ **No.** The row still reads `⏸ HELD` and still carries its 2026-07-31 evidence line: *"none of her four real inputs has ever been about a zone."* |
| **b** | `zones.json _meta.fold_2026_08_31` — lines deferred *"until a schema v3 adds them"* | schema v3 | ✅ v3 shipped | ⛔ No — v3 added `partOf` |
| **c** | `_meta.sharedBorders` — *"traced independently, with no vertex snapping"* | n/a (a stale fact, not a park) | — | ⛔ No — **58 coordinates are exactly shared across 20 zone pairs** |

⭐ **The general shape, and it is the one worth naming:** this repo has tooling that flags a **gateless**
park. It has nothing that flags a park whose **gate has been satisfied**. *A gated deferral reads more
responsible than an ungated one right up until its gate quietly passes* — the map-smoothing plan §8
reached this independently and filed it as a class. **This is the third file to derive it.**

⛔ **I do not rule on whether the hold should lift.** Three outcomes are all legitimate and all Paul's:
lift it · restate the trigger because the naming session is not the demand signal he meant · or record
that the trigger was written wrong. **Only silence is not a legitimate outcome, because silence and a
deliberate decision to keep holding print identically.**

### F3 · The authoring surface keeps getting capabilities the reading surface never gets — three instances, one feature

| capability | built on | reached the reader? |
|---|---|---|
| vertex snapping (`SNAP_PX=11`) + Chaikin smoothing | `area-trace.html`, 2026-08-31 | ⛔ not for 34 days; reached **QA only** 2026-09-04 (lane D) |
| the 8-type point/line taxonomy (`zone-capture.html:224`) | `zone-capture.html`, 2026-08-31 | ⛔ never — no canon type, no renderer |
| `zoneRulings` — per-zone confirmation with *"What does she call it?"* and *"Note (her words)"* (`zone-capture.html:472-507`) | `zone-capture.html`, 2026-08-31 | ⛔ never — no counterpart on her surface, no path to canon |

The map-smoothing plan §7 already named the first one: *"the capability exists, is proven, and is
pointed at the wrong surface."* **Three instances in one feature is not a coincidence; it is the profile
of a feature whose only maintained surface belongs to the operator.** §6 turns that from a defect into
the near-term plan.

### F4 · Five ordered sequences for one feature, none authoritative

1. `BACKLOG.md` §BASEMAP (:769) — *"🔜 OWED — next steps, in the order they are worth doing"* (0–7)
2. `BACKLOG.md` §Z2 (:2381) — *"Scope, if this becomes its own task"* (1–4)
3. `BACKLOG.md` §THE FOLD (:901) — three riders open
4. `.plans/2026-08-31-field-capture-queue.md` — STEP 0 / 1 / 2, *"a SEQUENCE, not a second tracker"*
5. `.plans/2026-09-04-map-region-smoothing-PLAN.md` §7 — Tier 1 / 2 / 3, **plus §4b recording Paul inverting the order**

Plus two verdict schemes for one experiment (T10) and two contracts (`lane-b` OPEN-at-gate,
`lane-d` CLOSED). Each is individually well written. **Together they mean no reader — human or agent —
can answer "what is the next map/zone act?" from any single file**, and `BACKLOG.md` names `zone` 142
times across a 3,449-line document whose measured defect is re-growth by append.

### F5 · Record and reality disagree — reported, not resolved

| claim | where | measured |
|---|---|---|
| *"All 10 zones are `status: draft`"* | `BACKLOG.md:133` | **23** zones, 23 draft |
| *"no vertex snapping"* | `zones.json _meta.sharedBorders` | 58 coordinates exactly shared, 20 pairs |
| lines deferred *"until a schema v3"* | `zones.json _meta.fold_2026_08_31` | schema v3 shipped without them |
| *"relief displacement at **2,959 ft**"* | `zones.json _meta.accuracyHonesty` | `property.json` / `CLAUDE.md`: **2,873 ft**, measured from USGS 3DEP lidar 2026-08-31; 2,959 was the Open-Meteo figure that reads 86 ft high on this spur |
| 23 canon / 24 capture / 17 roster | `BACKLOG.md` §Z2 | unresolved since 2026-09-02 |

⛔ **Which should win in each case is a content call and is not mine.** The one that is method: the
accuracy note is the record's own honesty statement about how far a boundary can be trusted, and it
now cites a superseded elevation in its own error budget.

### F6 · ⛔ TENANCY — the zone write path is single-repo, and the conversion ledger's own predicate cannot see it

`handleZoneSave` (`worker/worker.js:3617`) does **two** writes with **two different tenancy models**:

| write | line | scoped? | inside the conversion inventory? |
|---|---|---|---|
| KV canon | `:3701` `env.OBSERVATIONS.put(keyFor(scopeOf(env), "zones", "all"), …)` | ✅ per-estate | ✅ yes — it carries `scopeOf(env)` |
| device watermark | `:3714` `keyFor(scopeOf(env), "zones-last-seen", …)` | ✅ | ✅ |
| **git canon** | `:3724` `ghPutFile(env, "zones.json", …)` | ⛔ **no scope token at all** | ⛔ **no** |
| **re-inline** | `:3738` `ghPutFile(env, "viewer.html", …)` | ⛔ **no scope token at all** | ⛔ **no** |

`ghPutFile` addresses `${GH_API}/repos/${env.GITHUB_REPO}/contents/…` (`:2317`) — a single
deployment-level binding. **Under one production environment, household B saving a zone commits to
Fernwood's repo and re-inlines `ZONES_DATA` into the file that `2026-09-06-one-environment-DECISIONS.md`
F5 says carries the street address.**

⭐ **And the control designed to catch exactly this is structurally blind to it.** That file's **G1** —
*"Every `scopeOf(env)` code site is classified… an unclassified site is RED"* — has a **greppable
predicate**, and this leak carries no `scopeOf(env)` to grep. There are **9 `ghPutFile` call sites** in
`worker.js` (`:2672 :2698 :2746 :2773 :2833 :2846 :3724 :3738`, definition at `:2316`), spanning
promote-species, photo, audio and zone-save. **`grep -i zone` on
`.plans/2026-09-06-conversion-method-DESIGN.md` returns zero** — verified, then re-checked by the second
method the methodology requires: the KV sites *are* covered, via the `scopeOf` inventory, without being
named. So the honest statement is precise: **the KV half is covered by predicate; the git half is
covered by nothing, and the ledger will read green over it.**

### F7 · Objective coverage — counted, never graded

Of the 25 `.plans/` headers carrying an `objective:` — **O5: 14 · O3: 10 · O2: 1 · O1: 0 · O4: 0.**

⛔ **This is a coverage read and it is not a criticism.** O1 is *"Mom uses Fernwood as her field journal,
on her own initiative"*; the plan corpus is currently engine and process work by Paul's own explicit
sequencing (*"do the product and engine territory work and then we prove that by using it for
Fernwood"*), and her channels are held. **The number is here because Paul named alignment as this
seat's job**, and because a zero on the objective that names the make-or-break user is the kind of thing
that should be visible rather than derived by whoever next asks.

---

## 4 · ⭐⭐ THE METHOD RECOMMENDATION — the artifact for a feature with a vision, a current state, investigations and improvements

> **Paul, 2026-09-06:** *"this feature… should have kind of a vision and a current state and then a
> series of improvements and investigations we do to get there… that's where the practice steward can
> bring in some agile best practices in terms of how do we document this and improve our
> concept-to-feature pipeline."*

### 4a · Name the practice, and the finding first

**He is describing dual-track agile.** The delivery track carries **improvements**; the discovery track
carries **investigations**. The vocabulary is settled and old: *spike* is XP's word (Beck) for a
timeboxed investigation whose deliverable is an answer rather than an increment; *dual-track* is
Desirée Sy's, popularised by Marty Cagan; Teresa Torres's *Continuous Discovery Habits* supplies the
opportunity-solution tree, which is the closest published thing to "vision → the questions in the way →
the increments that answer them."

> ### ⭐ The finding: **this repo already runs dual-track at high volume and has never named the discovery track — which is why the track has no closing rule.**

Evidence: 50 `.plans/*.md`, of which 16 are `*-PROPOSAL.md` and 12 declare `row: process`. That corpus
*is* a discovery track. `check-backlog-ready.py`'s `STAGES` is a **delivery** enum, so ten files have had
to write words it does not have (§1b). **The words are missing because the track is unnamed.**

⛔ **What I am NOT importing.** No RICE, no WSJF, no story points, no now/next/later board, no epic
hierarchy. Two reasons, both this repo's own: every one of those is a *prioritisation* device and
prioritisation is not mine; and word-boundary greps across Paul's whole corpus return **zero**
occurrences of framework vocabulary. Importing a scoring scheme here would be visibly foreign — and
`PRODUCT-ENGINE.md` already warns *"a full ceremony set for a two-person app is its own kind of drift."*

### 4b · ⭐ Investigations vs improvements — and what a spike here is actually missing

The coordinator's hypothesis was *"a spike produces a beautiful document and no decision, and nothing
tracks whether the question it opened was closed."* **I checked it, and it is half right in a way that
matters.**

**Wrong half — the queue is not aged.** All 15 files carrying `ready: agent-proposed … Paul rules` were
first committed between **2026-09-03 and 2026-09-06** (`git log --diff-filter=A`). Zero to three days
old. **There is no rotting backlog of unruled spikes**, and reporting one would be exactly the
permanently-red control Paul has ruled against.

**Right half, and it is structural: a spike has no closing ACT, so a ruling does not land on the thing
it ruled.** The worked example is this thread:

- `.plans/2026-09-04-map-region-smoothing-PLAN.md:3` still reads
  **`status: RESEARCH + RECOMMENDATION. Not a queued row. Paul reads this and decides whether it becomes one.`**
- Paul decided **the same day**: `[paul-greenlit 2026-09-04] "yes, greenlight tier 1 as its own lane."`
- Lane D built it, shipped it to QA, and **CLOSED**.
- **The plan's own status line has not moved, and nothing joins the two.**

The same shape, three more times: T10's verdict was pre-registered twice and recorded zero times; the
restack's two direct questions to Paul (*"which device is Mom's"* — answered elsewhere, never written
back; *"does the time-box extend to 09-09"* — never answered); and `2026-09-05-state-of-the-work` §1a,
unruled, which is the file that says unruled files are invisible.

> ### So the missing thing is not discipline and not a tracker. It is a **field**: the place a ruling lands, inside the artifact that asked for it.

### 4c · The recommendation — ONE artifact, and it is a shape this repo has already ratified twice

> ### `features/<slug>.md` — one file per feature. It is `OBJECTIVES.md`'s shape pointed at a third axis. Stable ids, edited in place, never renumbered, never deleted.

Nothing is invented. `OBJECTIVES.md` `[paul-approved 2026-09-03]` proved the pattern (19 plans cite it;
`check-backlog-ready.py` resolves every id). `journey-as-prioritizer` §1a proposed the same shape for a
second axis. **This is the third, and if the journey spine is ratified the three join on the plan
header rather than competing.**

```
# <feature> — <one line a stranger would understand>
- id: F<n>                     stable; never renumbered, never deleted (strike + date to retire)
- objective: O<n>              existing key, existing resolver
- journey: J<n>.<n> | unplaced — <what the person is doing> | none — <reason>   [if the spine lands]
- owner: paul | agent | shared
- reachable-by: <the procedure or act that RUNS this feature's tools>   ← the anti-F1 field
- vision-set: <date>           when the vision paragraph was last asserted

## Vision
Two to five lines. ASSERTED, dated, in Paul's words where they exist. What is true when this is done.

## Falsifier
What evidence would say the vision is wrong. (Standing repo rule: no recommendation without one.)

## Current state
⛔ NO hand-typed status. One line per artifact, each with a RESOLVABLE ANCHOR — a path, a line
number, a command, or a commit sha. A line with no anchor is deleted, not marked stale.

## Open questions — THE DISCOVERY TRACK
| q-id | the question | who can answer | what would close it | closed-by |
A row with an empty `closed-by` is STATE, counted, never graded.

## Improvements — THE DELIVERY TRACK
| i-id | the increment | plan | stage |
One row per increment, each pointing at a `.plans/*-PLAN.md` that carries the real header.
This table CITES stages; it never restates them.

## Superseded
What this feature used to believe, what moved it, and when. (The map-smoothing plan's §4/§4b
pattern: keep the superseded reasoning, mark which one is live.)
```

**Three rules make it different from a status document, and they are the whole design:**

1. ⭐ **`## Current state` is DERIVED or it is absent.** The precedent is ratified twice —
   `journey-as-prioritizer` §1b (*"THE COLUMN THAT IS DELIBERATELY ABSENT IS `state`… A stage's state is
   derived from whether its `anchor` resolves, or it is not published"*) and `check-backlog-drift.py`'s
   rule that the clock is read from evidence, never a hand-typed line. **For maps/zones every derivation
   already exists and is one command each:** `python3 tools/zone-topology-report.py` (geometry) ·
   a one-line status count over `zones.json` (23/23 draft) · `git log -1 -- zones.json` ·
   `python3 tools/check-live.py` (did it ship) · `python3 tools/build-viewer.py --check` (does the
   reading surface match its sources).

2. ⭐⭐ **A question is closed by NAMING what answered it, never by deleting the row.** `closed-by:` takes
   a commit sha, a `.plans/` path + section, or `[paul-ruled <date>]`. **This is the missing closing
   act.** The check is one grep and needs no new tool: a `closed-by` naming a path that does not resolve
   is a flag, by the identical mechanism that already flags an unresolvable `objective:` id (`OBJ_PAT`,
   `check-backlog-ready.py`). ⛔ **An open question is never a flag** — most questions are open most of
   the time, and a control red on that is on from day one.

3. **`reachable-by:` is required and may be `none — <reason>`.** This is the F1 fix at the artifact
   level: a feature whose tools no procedure runs must say so in one line, on its own face. ⭐ **And the
   better form is `pages-deploy.py`'s, not a document's** — that script does not merely *name*
   `check-estate-neutral`; it imports and calls it and refuses the deploy on a hit (`:151`). **Where a
   check guards a specific act, wire it into the act.** `reachable-by:` is the index, not the
   enforcement.

### 4c-i · The stage enum — two words, not a second system

Add to `check-backlog-ready.py:46`:

- **`investigate`** — a spike in flight. ⭐ **Legal WITHOUT a `ready: [paul-approved …]` stamp.** Today
  `:212` flags any stage past `ready` with no stamp; if investigation inherits that, the discovery track
  is gated on the delivery gate and no spike can legally start. **That single exception is what makes
  dual-track expressible in the enum at all.**
- **`ruled`** — the terminal state of an investigation. **Not `shipped`; a spike ships nothing.**
  Requires a `closed-by`, the same way `shipped`/`retro` already require a `## Retro` at `:215`.

Result: `ready · investigate · concept · build · qa · shipped · retro · ruled` — eight words, and the
ten illegal-word self-flags (§1b) are retired in one edit. **Proven by mutation, this repo's standard:**
an `investigate` with no stamp must pass · a `ruled` with no `closed-by` must fail · a `closed-by`
naming an unresolvable path must fail · an open question row must NOT flag.

### 4d · Where it lives — and the BACKLOG constraint is a test, not a caveat

**`features/` at repo root.** ⛔ Not `.plans/` — those are dated and terminal by convention (a lap
artifact: *"a record of what was true when someone looked"*), and a feature file is standing. ⛔ Not
`BACKLOG.md`, which is 3,449 lines with a measured re-growth-by-append defect that
`check-backlog-drift.py` exists to flag.

**The BACKLOG relationship is one pointer row per feature**, exactly as `BACKLOG.md` already does for
`PRODUCT-ENGINE.md` (*"This section is now its own file. Do not re-grow it here."*).

> ### ⭐ The acceptance test for the whole artifact type, and I would hold it to this: **`features/maps-zones.md` must REMOVE more `BACKLOG.md` lines than it adds.**

For this feature that is achievable and not a stretch: five scattered sequences (F4) collapse into one
`## Improvements` table, and the three BACKLOG map/zone sections plus the HELD row become a pointer.
**A new artifact type that grows the file the drift checker watches has failed on delivery.**

⚠️ **Register it in `ENGINE-MANIFEST.md`.** An unclassified root path falls to `markdown_default` →
`class: instance`, silently — the drift `journey-as-prioritizer` §0a measured on `OBJECTIVES.md` itself.
`features/` is engine; the tier is Paul's.

### 4e · Falsifiers for this recommendation

| # | falsifier | observed | consequence |
|---|---|---|---|
| 1 | ⭐ **`closed-by` stays empty** | after ~10 features, the questions table is only ever appended to | the artifact is a second backlog — **delete it**; the `.plans/` corpus was enough |
| 2 | **the current-state section is hand-typed** | any line without a resolvable anchor survives a month | rule 1 broke; strip the section and keep vision + questions only |
| 3 | **it grows BACKLOG.md** | the first file adds more lines to `BACKLOG.md` than it removes | §4d's test failed; revert |
| 4 | **Paul overrides a `features/` placement twice** | as stated | **my defect.** Strip every derived field; keep the vision paragraph and nothing else |
| 5 | **`investigate` is never used** | every spike still writes an illegal word or `draft` | the enum was not the constraint; revert the two words |
| 6 | **it becomes a nag** | anything prints that a question is *overdue*, *late* or *stale* | rule 2's counted-never-graded posture broke; revert |

---

## 5 · ⭐ THROUGHPUT — *"we don't get bogged down in keeping a pipeline of features we can deliver to Bob and Mom"*

### 5a · The measurement, with its predicates attached

| month | user-facing release notes | `.plans/*.md` created |
|---|---|---|
| 2026-05 | 5 | — |
| 2026-06 | 6 | — |
| 2026-07 | **68** | 8 |
| 2026-08 | 21 | 3 |
| 2026-09 (through 09-06) | **2** | **42** |

⚠️ **Two predicates ride with this table and without them it says something false.**

1. **Production is frozen by Paul's own ruling.** Features hold lifted **on QA only** (2026-09-04);
   Mom's channels are held; a prod-needed fix goes by cherry-pick. **A low release-note count in
   September is the freeze working, not a throughput failure**, and reporting it as one would be exactly
   the misreading this seat exists to prevent.
2. **Line counts are not the instrument.** `git log --numstat` since 2026-08-25 reports 47,345 lines
   under `.js/.py/.html` against 21,863 under `.plans/` — but `viewer.html` is generated and its inlined
   `*_DATA` constants are single enormous lines. **The count is real and the comparison is not.**

### 5b · What CAN be said structurally

Not *"too much investigation"* — that is a value call and it is not mine. What is structural:

- **The discovery track has exactly one gate and it is one human.** 15 artifacts await a ruling; 16 are
  invisible to the instrument that renders in-flight work (§1c); 14 of 25 declare `objective: O5`.
  **Discovery output scales with agents. The gate does not.** That is a capacity asymmetry, and it is
  the same asymmetry Paul already named in his own doctrine.
- **The ten illegal `stage:` words (§1b) are the visible form of it.** Every one self-flags, the fix is
  one line, and the enum has not moved in three days. **Nothing is wrong with the discipline; the
  ruling queue is the constraint.**

### 5c · ⭐ The counterweight — Paul's own rule, applied

> *"When a backlog needs draining, run more GATE, never more LAP."*

The constraint is ruling capacity, so **the move is to make ruling cheap, not to make discovery
slower.** Three edits, in order of size:

1. **Widen `check-backlog-ready.py`'s glob to `*-{PLAN,PROPOSAL}.md`, grading a PROPOSAL on its header
   only.** Already designed with its own falsifier (`state-of-the-work` §1b). Until this lands, an
   unruled proposal and a nonexistent one print identically.
2. **Every `*-PROPOSAL.md` carries a `## Rule this` section: a numbered list of yes/no decisions with a
   recommendation each.** Then a ruling is a reply, not a re-read of 40 KB. *(This file's §8 is written
   that way deliberately, as the worked example.)*
3. **`closed-by`, so a ruling lands in the artifact it rules on** (§4c rule 2). Without it, ruling costs
   Paul a decision *and* a filing act, and the filing act is the one that does not happen.

⛔ **What I refuse, named so it is not re-proposed:** a cap on investigations · a WIP limit on `.plans/`
· any rule that a spike must produce a shippable increment. **All three would have blocked
`zone-topology-report.py`, which is the best instrument this thread has.** Falsifier for that refusal:
if Paul finds himself unable to name the next map/zone act *after* `features/maps-zones.md` exists, the
constraint was never the gate and this whole section is wrong.

⭐ **And the throughput claim's own falsifier:** if Paul rules on the 15 within a week, the gate is not
the constraint and §5b/§5c should be struck.

---

## 6 · ⭐⭐ RE-PLACEMENT under the 2026-09-06 ruling — *"you and I defining the zones and presenting them for confirmation"*

`[paul-stated 2026-09-06, voice — interpreted for meaning, not quoted as canon]`

### 6a · What drops out of the near-term path

Not cancelled — **not next**, and the distinction matters because the record should not read as though a
capability was killed:

- **self-serve mobile tracing UI** — never existed as a thread; under the old reading it would have had
  to. It does not now.
- **Model A (the polygonal coverage, Tier 3)** — its blocking prerequisite was an *adjacency statement*
  the household would have had to supply. Under operator-drawn, adjacency is decided **at trace time by
  the person holding the tool**. The blocker does not disappear; it relocates to someone who can answer
  it.
- **`map-zones` as a self-serve onboarding promise.** `onboarding/index.html:877` reads *"A map you draw
  yourself · Trace your own areas onto a photo of your place, then fill them in."* ⚠️ **That sentence now
  describes the long-term product and not the near-term one, and it is live on QA.** ⛔ **Whether to
  reword it, keep it as a genuine long-term signal, or leave it under `soon: true` is a content and
  product call — content-steward's and Paul's, explicitly not mine.** I report only that the ruling and
  the sentence have diverged.

### 6b · What becomes REACHABLE that was blocked

- **Tier 2, the eleven slivers.** The blocker was *"several are sub-pixel on the current basemap; some of
  these pairs are settled only by standing there."* **Under operator-drawn, the person standing there is
  the tracer.** Eleven review-time adjudications become eleven trace-time observations.
- **Lines in the schema (T6).** §4b of the smoothing plan already argued that drawing the wall between
  two zones *is* answering the adjacency question, and yields a record rather than an opinion. The
  ruling makes that the normal path rather than a proposal.

### 6c · ⭐ The critical path this creates — and it has NO stage, NO gate and NO owner

> ### An operator production process: **acquire a basemap for an arbitrary address → trace → name → present for confirmation → fold to THAT household's canon.**

**Verified absent** by two methods: `grep -rn -i "back-office|backoffice|operator-drawn"` across all
`.md` returns **0**; and no `.plans/` header, no BACKLOG row and no objective names it. Under the
previous reading it was not a thread. Under this ruling it is **the** thread, and it is the one thing in
this audit that has no home at all.

⭐ **But it is roughly 70% built, and nobody has called it that.** `tools/zone-capture.py`'s own docstring
is the process, written 2026-08-31:

> *"A co-located capture session. Mom talks, Paul clicks. The screen shows the georeferenced NAIP
> leaf-off aerial of the property… and every click records a real WGS84 point or polygon with the name
> she gave it and, ideally, HER WORDS about it."*

| step of the process | what already exists |
|---|---|
| acquire | `fetch-basemap.py` · `register-gearth-frame.py` · `fetch-trace-hires.py` · `fetch-historical-topo.py` |
| trace | `area-trace.html` (snapping, Chaikin, seven ground frames) · `zone-capture.html` (`mode: point`/`area`, 8-type taxonomy) |
| name | `zone-capture.html` records the name and her words at click time |
| **confirm** | ⭐ `zone-capture.html:472-507` — a **per-zone ruling pane** with *"What does she call it?"* and *"Note (her words)"* |
| inspect | `zone-topology-report.py` (read-only, positive control) |
| round-trip | `zones-to-kml.py` / `kml-to-zones.py` (byte-exact no-op across all 23) |
| fold | `handleZoneSave` + `zones.json` + the `status: draft` field |

**Six tools, one named discipline, zero procedures — and the confirmation half already exists in the
operator's hand.**

**The three real gaps, all structural, none of them a UI:**

1. **Acquisition is Fernwood-specific and manual.** One anchor, a flaky Earth Web dependency, the
   northern-strip decision unmade (T1). For a second household this is the first thing to break, and it
   breaks silently — Esri z20/z21 return HTTP 200 with a grey "Map data not yet available" tile, already
   recorded as one of the three measured traps.
2. **The save path is single-repo (F6).** An operator drawing Bob's zones today would commit them into
   Fernwood's `zones.json` and re-inline them into Fernwood's `viewer.html`.
3. ⭐ **The confirmation is the operator's record of what she said, not her own act.** `zoneRulings`
   captures Paul's read. Under the AI-boundary's administrator gate that is entirely legal — *the
   administrator's eyes sit between the model and the estate's people, both directions.* ⛔ **Whether
   "presenting them for confirmation" means her tap on her surface or his transcription in the operator
   tool is Paul's ruling, and the whole near-term deliverable turns on it.** They are different builds:
   the first needs a confirm affordance on `viewer.html` and a `status: draft → confirmed` write path;
   the second needs nothing new at all.

---

## 7 · HOW THIS FEATURE HAS ACTUALLY BEEN DEVELOPED — the process read

*(The narrative is being written elsewhere. This is only the judgment of the method, as asked.)*

**Every advance came from a co-located session or a Paul memo. None came from a loop.**

| date | advance | initiated by |
|---|---|---|
| 2026-05-19 | `draw-zones.py` prototype | Paul |
| 2026-07-16 | NAIP basemap, WGS84 vertices | Paul |
| 2026-07-17 | zones drawn + zone-audio + front door v1 | Paul |
| 2026-08-30 | **Mom names sixteen areas** | a session with her |
| 2026-08-31 | fold to canon, capture tools, lines traced | Paul |
| 2026-09-01 | basemap session, KML round-trip, seven frames | Paul |
| 2026-09-02 | Z2 survey | Paul |
| 2026-09-04 | smoothing memo → lanes B and D | Paul |
| 2026-09-06 | the operator-drawn ruling | Paul |

**Nine advances, nine human initiations, zero trigger-initiated.** That is not a criticism of the work —
it is the *definition* of an unwired capability, and it predicts F1, F2 and F3 exactly. A feature that
only ever advances when a person remembers it will only ever be as current as the last time someone
remembered.

> ### ⭐ The judgment, in one line: **this feature is excellent at learning and has no mechanism for closing.**

It has produced a 512-line measured plan with bounds rather than guesses; a reproducible instrument with
a positive control; a five-lens research panel with **pre-registered** verdicts; a measured floor that
killed an obvious wrong move before it was built (the photo→zone join); a near-miss caught before it
propagated (Z2); and a refusal to bake in a smoothing that would have shrunk the smallest zones by 10%
while every distance check read green. **On evidence quality this is the strongest thread in the
repo.**

**And in the same period it has not produced:** one zone leaving `draft` · one recorded verdict on
H1–H5 · one acknowledgment to the person who named the map · one line in canon.

That gap is precisely what a dual-track artifact supplies, which is why §4 is the real answer to a
question that arrived as a placement audit.

---

## 8 · ⭐ RULE THIS — the decisions this file surfaces, each with a recommendation

*(Numbered so a ruling is a reply. Each is Paul's; my recommendation is a recommendation.)*

| # | the decision | mine? | recommendation |
|---|---|---|---|
| **1** | Does `features/<slug>.md` exist, in the shape of §4c? | method — mine to propose | **Yes**, and write `maps-zones` first as the worked case. Held to §4d's test |
| **2** | Add `investigate` + `ruled` to `STAGES` (§4c-i)? | method — mine | **Yes.** Retires ten self-flags in one line |
| **3** | Widen `check-backlog-ready.py`'s glob (§5c-1)? | method | **Yes** — already designed with its own falsifier in `state-of-the-work` §1b |
| **4** | Fix the F1 blindness: widen `TOOL_GLOBS`, or a per-tool `# loop:` header? | method | **The header.** The glob is a filename predicate standing in for a semantic one |
| **5** | **Does the zone hold lift?** (F2a — the trigger as written has fired) | ⛔ **Paul's, entirely** | **No recommendation.** Lift · restate the trigger · or record that the trigger was wrong. All three are valid; **only silence is not** |
| **6** | Record a verdict on the zone-journey experiment before 2026-09-09, or restate the window (T10) | ⛔ Paul's | **No recommendation on the verdict.** Method: two schemes and two windows exist, the tool implements the retired one, and `--rotation` cannot reach either |
| **7** | Does "present for confirmation" mean her tap, or the operator's transcription? (§6c-3) | ⛔ Paul's | **No recommendation.** The near-term build differs completely between the two |
| **8** | What does Z-ACK's *"zone work ready to distribute"* mean, in testable form? | ⛔ Paul's | Method only: R1 in the one-environment decisions is the shape a release condition takes here when written well |
| **9** | The `map-zones` onboarding sentence vs the 09-06 ruling (§6a) | ⛔ content-steward's + Paul's | Reported, not resolved |
| **10** | Classify the 9 `ghPutFile` sites in the conversion ledger (F6) | engineering-partner's design; the *gap* is mine to report | **Yes, classify them.** G1's predicate cannot see them, so it reads green |
| **11** | Which of the five stale `_meta` / BACKLOG facts get corrected, and by whom (F5) | ⛔ mixed; the elevation one is mechanical | Report only. This seat does not edit canon |

---

## 9 · METHOD MOVES THAT WOULD MAKE THIS TESTABLE — smallest first

1. **Write `features/maps-zones.md`.** It replaces five sequences with one and makes moves 2–6 possible.
   *Falsifier: if it does not remove more `BACKLOG.md` lines than it adds, the artifact type is wrong.*
2. **Re-read `BACKLOG.md:133` against its own un-park trigger and record a verdict** — any of the three
   in §8-5. *Falsifier: if Paul finds re-reading fired triggers is busywork, the whole "gate satisfied"
   class is not worth a mechanism and F2 should be filed as three incidents, not a class.*
3. **Record a verdict on H1–H5, or restate the window, before 2026-09-09.** *Falsifier: if the answer is
   "the experiment is moot because the front door is being redesigned," that is a legitimate close and
   should be written as one.*
4. **Wire `zone-topology-report.py` into the act it guards, not into a document.** Copy
   `pages-deploy.py`'s model: a `zones.json` write calls it and refuses on a hard fail. *Falsifier: if it
   refuses a write Paul wants twice, it is the wrong siting and belongs in the session-start block as a
   report.*
5. **Two enum words (§4c-i), proven by the four mutations named there.**
6. **Classify the 9 `ghPutFile` sites** (F6) so the conversion ledger stops reading green over the git
   write path.
7. **Name the operator production process (§6c) and give it one home** — with `reachable-by:` filled in,
   since six of its seven steps already have tools and none of them is in a procedure.

---

## 10 · WHAT I COULD NOT VERIFY, AND WHAT I DECLINED

**Could not verify:**
- **I rendered nothing.** No claim here rests on looking at the map. T4's QA state is read from lane D's
  own close-out line, not from loading `fernwood-qa`.
- **The `/design-options` run count** is taken from C2's own correction (~3 runs, last 2026-08-14, all
  Paul-initiated). I did not re-read the skill's Refinement log — and C2 records that counting artifacts
  instead of reading that log is exactly how the number went wrong the first time.
- **Whether the T10 `INVALID` clause is moot.** `metricsExclude` was *"provably never applied"* per the
  restack; deterministic exclusion later shipped via `people.json` `excludeFromEngagement`. Whether that
  satisfies a clause written against a different mechanism is a judgment about the experiment's
  validity, and I did not make it.
- **Whether any downstream consumer publishes per-zone area.** If one does, the Chaikin area-shrink
  finding (−10.5% on `western-fern-azalea-garden`) is a correctness issue and not a caution. Not traced —
  the smoothing plan flagged the same gap and it is still open.
- **The two launchd watchers** (`com.fernwood.momfunnel-watch`, `com.fernwood.momqueue-watch`) are
  registered and last exited 0. I did not verify either has actually run recently — *a quiet watcher and
  a dead one must never read the same*, and I cannot presently tell them apart.

**Declined, and each is Paul's:** whether the hold lifts · whether points matter more than smoothing ·
which of the eleven slivers abut · whether Mom is acknowledged now or at distribution · whether the
legacy viewer stays at `home` · whether `map-zones`'s promise is reworded · which map/zone thread is
next. **Every one turns on real-world context this seat does not have and cannot acquire.**

---

*Every repo claim above was read in the named file or produced by executing the named command against
the working tree on 2026-09-06. `git status` at the time of writing showed one modified file
(`.plans/2026-09-06-conversion-method-DESIGN.md`) belonging to another session; **HEAD may have moved
under this audit** — re-verify before acting, per this repo's own concurrent-writer rule. Nothing outside
this file was written, and nothing was committed.*
