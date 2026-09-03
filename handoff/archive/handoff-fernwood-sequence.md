<!-- clearing-state: CLEARED THE SEQUENCE steps 1–5 ran 2026-09-01/02; consumed — superseded by PRODUCT-ENGINE § THE SEQUENCE and the C4 plan (close-out 2026-09-03) -->
# Handoff: fernwood-sequence
<!-- generated 2026-09-01 10:20 AM ET · sources: Tate-Tracker@36aca87, .claude@e31d16f · RECEIVER: verify shas vs HEAD before trusting any status below -->

## 1. Mission
Continue Fernwood's ordered sequence. **Fleet lap 2 first**; everything after it is gated on Paul or on a user-researcher interview.

## 2. Read first
- **`PRODUCT-ENGINE.md` → `▶️ THE SEQUENCE`** (top of file) — the ordered path and its gates. Also its `🗂 WHERE THE 2026-09-01 SESSION'S OUTPUT LIVES` index.
- **`BACKLOG.md` → `## 🔧 FLEET LAP 1 — what it raised for Paul`** (Track B) — the five open rows P1–P5.
- **`cycle/fleet/CYCLE-LOG.md` → Lap 1** — beats run, beats held, and beat 7's three proposed amendments.
⛔ Do NOT read the two mine reports end-to-end (734 + ~900 lines). Open a section only when a step needs it.

## 3. Next steps (ordered)
1. **Fleet lap 2.** Probe: `python3 tools/fleet_probe.py`. FIRED on **INBOX 4 · PROVENANCE 3 · STALE-OPEN 3**. Beat 3 drains the door — the 4 rows are the ChatGPT-mine findings (water heater · spark plugs · second Bronco window switch · rounded mower bolt). Each lands on a surface or is refused with a reason. ⚠️ **SEASON was 46d from frost on 09-01 against a 45d window — expect it to fire.**
2. **Ask Paul the six one-line questions** in §5 of this brief's sibling list below (they unblock more than they cost).
3. **Only after Paul answers** — steps 3–5 of THE SEQUENCE (user-researcher interview → agile artifacts → architecture). ⛔ Do not start at architecture.

## 4. State & pointers
- Repo `~/Developer/Tate-Tracker` @ `36aca87`, **clean, 0 unpushed**. 19 commits on 2026-09-01.
- Fleet loop: `cycle/fleet/{CYCLE-MAP,CYCLE-LOG,cycle-state}.json|md` · door `cycle/requests.jsonl` · door state is **`status` field**, `"open"` (or absent) = unread.
- `cycle-state.json`: `last_lap.lap = 1`, **`lap_count` still 0** — it counts CLOSED laps and lap 1 is open at Paul's gates. Do not increment it to tidy the board.
- Mom loop: **lap 7 OPEN at leg 6**, ribbon HELD by Paul. `MOM-CYCLE-LOG.md` § Lap 7.
- 217 staged images: `.private/chatgpt-fleet-images/` (gitignored) + manifest `.plans/2026-09-01-chatgpt-fleet-image-manifest.json`.
- `~/.claude` @ `e31d16f` — memory updated; its other dirty files are a PRIOR session's autosave, not this thread's.

## 5. Guardrails
- **Agent proposes, main session reviews.** No agent writes `vehicles.json`, `TOOLS.md`, `AMAZON-PARTS.md` or a guide.
- **Parts record is wrong in BOTH directions.** Absence ≠ evidence; a stated order ≠ an order; **a stated cancellation is equally unreliable**. Only an ORDER NUMBER clears a purchase.
- **A value read off a photo is a model read.** Never folds on an agent's say-so.
- **Attribute from a conversation's own content**, never a keyword or nearby date. Paul owned the Bronco from **2025-10-07**; anything earlier is a different machine or a pre-purchase look.
- **Mom's surface**: nothing ships without Paul. The ack ribbon is HELD.
- Use `tools/guard-concurrent.py start|check|commit|push` — a bot pushes `weather-history.json` on a schedule.

## 6. Done when
Fleet lap 2 has drained its door, disposed each signal (act/fold/snooze/kill) with a reason, chronicled itself in `cycle/fleet/CYCLE-LOG.md`, and either closed (marked, `lap_count` incremented) or recorded which of Paul's gates it is held at.

## 7. Un-sealed judgment — reads NOT yet on disk
- **The Husqvarna manual may mean an unrecorded machine.** `YTH24V54` (a ride-on tractor) is filed against a Z254F zero-turn. I read it as a wrong document, but "Paul has/had a YTH24V54" is not ruled out and nothing tests it.
- **The zone-walk launcher (293px, 15% of her pre-glance stack) is live while Paul holds the zone thread.** Flagged for a ruling; I did not treat it as a defect.
- **Beat 7's amendment — grade PROVENANCE by severity** — is proposed off ONE lap. One lap is not evidence.
- **My own D4 counterfactual failed and is unreported**; pricing the head-card choice needs a real `MomQueue` re-render.

## 8. Trust status
**Human-cleared (Paul, 2026-09-01):** the card rotation + `q-weed-beggars-lice` approval (shipped, verified live) · the ribbon hold · running the mines · the broad-net archive scope.
**Model-flagged, NOT cleared — treat as hypotheses:** all 4 door rows · the 3 provenance flags · the contractor proposal's 3 moves + 4 questions · the D4 trim observations · beat 7's amendments · every mine finding tagged `ADVISED`/`ASKED`/`PLANNED`.
**Corrected in-session, do not re-derive:** the "Bronco cooling-leak arc" was mine and was wrong (DR-Z ×1, GTI ×3) · `bronco-1989.acquired` is not uniquely null (**6 of 7** vehicles are) · the S-9 order story has a resolution table appended — nothing is outstanding · the UX sweep is **NOT owed** (ran 2026-08-31; the checker was fixed).
