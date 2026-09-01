> ⛔ **CONSUMED — lap 2 CLOSED 2026-09-01 (`bc4a507`). This brief is HISTORY, not open work.**
> Do not re-run it. Live state: `cycle/fleet/cycle-state.json` (`lap_count 2`, RESTING) and the
> **Lap 2** section of `cycle/fleet/CYCLE-LOG.md`, which is authoritative over anything below.
>
> ⚠️ **TWO CLAIMS IN THIS BRIEF WERE MEASURED WRONG** — kept visible rather than edited out, because
> the sequence is the lesson:
> 1. *"Expect SEASON to fire"* — it did not. 46d against a 45d window; the brief contradicted its own
>    arithmetic, which put the window at 2026-09-02. The probe was right.
> 2. *"the put-away is a natural anchor"* for the Bronco emissions deferral — **false.** The fall
>    put-away exists only on `dr200s-2017` and `drz400s-2001`. **The Bronco has no put-away item.**
>    It is a with-the-BIKES moment. This came from lap 1's chronicle and was repeated to Paul before
>    anyone checked it.
> 3. And §3's *"let the tool refuse"* — beat 0 **did not refuse**. It resolved the wrong machine at
>    61 points to 2. Fixed in `760f9a5` / `6a8f35c`.

# Handoff: fernwood-fleet-cycle
<!-- generated 2026-09-01 11:29 AM ET · sources: Tate-Tracker@a7b2e67, .claude@230931c · RECEIVER: verify shas vs HEAD before trusting any status below -->

## 1. Mission
Run **lap 2** of Fernwood's Track B fleet & equipment cycle. It opens on **an update Paul is bringing in person** — take it at beat 0 before running anything else.

## 2. Read first
- **`cycle/fleet/CYCLE-MAP.md` → the beat table (0–7)** and **`## Beat 1 · the FIELD half`** (why forum takes are quarantined).
- **`cycle/fleet/CYCLE-LOG.md` → `## Lap 1`** — closed 2026-09-01. Read **`👤 Beat 6 RAN`** for Paul's standing rule and **`✅ Beat 7 AMENDMENT APPLIED`** for what changed in the probe.
- **`BACKLOG.md` → `## 🆔 V-SERIES`** — the identifier findings. Do not re-derive them.
⛔ Do NOT read the mom-cycle sections or `MOM-CYCLE-LOG.md` — different track, different loop.

## 3. Next steps (ordered)
1. **Beat 0 GUARD + BRIEF** — `python3 tools/guard-concurrent.py start`, then **ask Paul for his update and run `python3 tools/vehicle-brief.py "<whatever he said>"`**. It resolves loose speech to ONE machine, prints what it rejected, and **refuses on a tie**. ⛔ Do not guess the machine; let the tool refuse.
2. **Beat 2 SWEEP** — `python3 tools/fleet_probe.py`. ⚠️ **Expect SEASON to fire**: it was 46d to first frost on 09-01 against a 45d window, so the fall put-away window opens **2026-09-02**. That is a real signal, not noise — parts lead time is the gate, not the weather.
3. **Beat 3 INTAKE** — `cycle/requests.jsonl`. Door was clear at lap 1 close (`6 filed, all handled`). Anything new lands on a surface or is refused **with a reason**.
4. **Beats 4–6** — per the map. Beat 6 is 👤 Paul's gate.
5. **Beat 7 AMEND — one is already queued:** `cycle/fleet/cycle-state.json` has **no `signals[]` array**, so it does not carry the tri-state `signals[].status` the CYCLE-SPINE S1 amendment ratified 2026-08-31 (the mom cycle's state file has one). That is a **`write_state()` change**, ⛔ never a hand-edit of the artifact.
6. **Close** — mark the lap, increment `lap_count` **1 → 2**, and publish state with **`python3 tools/fleet_probe.py --write-state`**.

## 4. State & pointers
- Repo `~/Developer/Tate-Tracker` @ `a7b2e67`, **clean, 1 unpushed**.
- `cycle/fleet/cycle-state.json` — **RESTING · lap_count 1**, generated 15:19:39Z by the real writer. Lap 1 is the first closed lap this loop has.
- Probe at lap-1 close: `SEASON` quiet · `INBOX` clear (6 filed) · `PROVENANCE` 6 flagged/all acked · `STALE-OPEN` `no open check older than 60d [3 open (0 undated) · 7 closed · 1 deferred]`.
- ⏸ **One deferral is armed:** Bronco emissions hardware, `state: deferred`, **`nextLook: 2026-10-01`**. Three looks close it — EGR valve on the intake? Thermactor air pump on the front? cats underneath? ⚠️ **Paul did not pick that date, the previous session did** — he said *"next time I'm with Bolores."* Move it freely; the put-away is a natural anchor.
- 3 genuinely open items, all `dr200s-2017`: repeated no-start (root cause not established) · **charging output never measured — THE decisive test** · battery age unknown (YTX7L-BS).
- ⚠️ `handoff/handoff-fernwood-sequence.md` is **superseded** — it says "Fleet lap 2 first" over a lap 1 that was still open. Lap 1 has since closed.

## 5. Guardrails
- ⭐ **THE STANDING RULE** `[paul-stated 2026-09-01]`: *"If you're flagging old issues for bolores that come from the old documentation, don't resurface them because they've been resolved."* Engine replaced twice (2016 short block, 2018 long block). ⚠️ **Scope: OLD-DOCUMENTATION items only.** It does NOT license closing a NEW observation without a look.
- **The parts record is wrong in BOTH directions.** Absence is not evidence; a stated order is not an order; **a stated cancellation is equally unreliable.** Only an ORDER NUMBER clears a purchase — see how P7 was cleared (Gmail order `NGK196860`).
- **A value read off a photograph is a MODEL READ** and never folds on an agent's say-so. Highest stakes: **a VIN**.
- **Agent proposes, main session reviews.** No agent writes `vehicles.json`, `TOOLS.md`, or `AMAZON-PARTS.md`.
- **`vehicles.json` inlines into a PUBLICLY SERVED `viewer.html`.** After any edit run `python3 tools/check-data-inline.py --fix` — beat 6's own done-condition is "generated views re-inlined," and the previous session committed before doing it. ⛔ **Never put an unmasked identifier in `vehicles.json`.**
- ⛔ **Never hand-edit `cycle-state.json`'s `state`/`why`/`next`/`generated_at`/`generated_by`** — `write_state()` owns them; only the lap-chronicle fields (`lap_count`, `last_lap`, `_note`) are the lap's. The previous session broke this and had to spend a commit undoing it.

## 6. Done when
Lap 2 has taken Paul's update onto a surface (or refused it with a reason), disposed every fired signal, chronicled itself in `cycle/fleet/CYCLE-LOG.md`, and either closed (marked, `lap_count` → 2, state published by the writer) or recorded which of Paul's gates it is held at.

## 7. Un-sealed judgment — reads NOT yet on disk
- **The V-series is the real open thread and it is bigger than a lap.** 8 of 22 machines carry an identifier across **three** stores nothing joins; the six vehicle cards say *"full VIN in private records"* and **no such record exists** — the values sit in git history at `4e83137`, on the **public** `origin/main`, because the mask two minutes later changed the working tree and not history. Paul's read — that the PII split is causing this and argues for a **login-gated surface** — is recorded but unscoped. **Do not start building that in a lap.**
- **The ChatGPT archive has 217 staged images** at `.private/chatgpt-fleet-images/` incl. a `g22a-2005` directory — a machine with **no identifier at all**. Paul believes he photographed VINs into ChatGPT. Untested.
- **Beat 7's lap-1 proposal to grade PROVENANCE by severity** was made off one lap and never applied. One lap is not evidence.
- The Husqvarna's **YTH24V54 manual is acked but still the wrong document** — replacing it with a Z254F manual is open work nobody has scoped.

## 8. Trust status
**Human-cleared (Paul, 2026-09-01):** the standing rule on old Bolores documentation · 5 Bronco items closed · transmission = C6 (**he read `P R N D 2 1` at the truck**) · emissions deferred · `DR200S` canonical · one Husqvarna, no missing machine · Homelite **decommissioned** · the probe fix.
**Model-flagged, NOT cleared — treat as hypotheses:** every V-series finding · the ChatGPT-mine rows routed at beat 3 (P6/P8/P9 in `BACKLOG.md`) · the claim that the Bronco short cost a **window lift motor** as well as a breaker (read off the register's date sequence, not from Paul) · which mower carries the rounded 5/8" bolt (**deliberately not asserted**).
**Corrected in-session, do not re-derive:** the plugs were never a contradiction — **NGK140052** (2022, R7437-**9**) and **NGK196860** (2025, R7437-**8**) are a three-year sequence, and the record's `-8` was right · lap 1 IS closed and `lap_count` IS 1 · `s4_stale_open` now reads `state`, so a closed item no longer fires.
