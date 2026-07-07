# Garden Guru × machines — action plan

**Created:** 2026-07-07 · **Source:** three-expert panel (ai-advisor, ux-expert, engineering-partner) on the 2026-07-03 motorcycle refusal (KV `conversation:mr55wd27-sommb`, 12:42pm ET).
**Expert artifacts:** `.ux-reviews/2026-07-07-garden-guru-machine-register.json` · `.engineering/2026-07-07-review-garden-guru-vehicles.json`

## The through-line
The 7/3 fix expanded Guru's *voice* (dual register) but not its *knowledge scope* or its *capture path*. Result: the real starter question would **still** be refused today, and "log that as a backlog item" has nowhere to land. Fix = let general **know-how** in (keep **specs** curated) + close the **capture loop** to the vehicle's backlog. **No classifier** — the fused real message is the argument against routing.

---

## Phase 0 — Clear what's broken in production *(no decision needed; safe; do first)* — ✅ DEPLOYED 2026-07-07
Each redeploy is gated on Paul's explicit go. **Green-lit + deployed: Worker version `ebfb4f6f-525c-4f94-80a1-810e2ed551ff`.**

- [x] **0a — Live digest was stale.** Confirmed via structural diff: deployed digest built 2026-07-04T03:14Z; `plants` + `fishing` sections had drifted (all other sections in sync). Rebuilt (~75K tokens) + deployed. Guru now serves fresh plant/fishing knowledge.
- [x] **0b — Confidence-check bug fixed.** `tools/build-digest.py:114` now `if m.get("confidence") != "verified":`. Latent as expected — `[unconfirmed]` marker count held at 32 (no non-verified spec is currently exposed in the digest), so no behavior change today; closes the gap for any future novel tag.
- [ ] **0c — Live E2E verify (owner: Paul).** `/api/chat` is `X-Tate-Token`-gated (secret, not readable here). Confirm on phone: ask Guru "what's at peak this week?" + a fishing question → fresh data. *(Fix is deterministic — bundled digest = the fresh file — so this is a belt-and-suspenders eyeball, not a blocker.)*
- ⚠️ **Uncommitted:** the deployed change (build-digest.py + digest.json) is live but not yet committed — awaiting Paul's go to commit (alongside the expert artifacts + this plan).

## Phase 1 — Decision gate *(Paul)* — ✅ RATIFIED 2026-07-07
Blocks the entry-point design in Phase 3, not the plumbing.

- [x] **1a — The fork. LOCKED: the reconciliation.** One conversational assistant for the ASK (don't split the conversation) + machine CAPTURE routes to the Vehicles-card backlog. Machine-ask stays inside Garden Guru.
- [x] **1b — Discoverability: YES, design for Mom.** Paul: "Mom may wanna ask questions about the machines, absolutely, and vehicles." → machine-ask is a *discoverable* feature, not a Paul-only convenience. Raises priority of 3-entry-point discoverability + 4a accessibility. *(Clarifying-vs-jarring left open; 2c "one caretaker's range" reframe mitigates it either way.)*
- [ ] **1c — Confirm principles** the experts want to add (see Phase 5).

## Phase 2 — Core scope fix *(the fix that answers the original question)* — ✅ DEPLOYED 2026-07-07
Independent of the fork as long as ASK stays in Guru (true for recommendation + option A). **Deployed: Worker version `337cc4f0-ba74-4710-bf2f-9a80f98ff4e7` (prompt-only; digest already fresh from Phase 0).**

- [x] **2a — Specs-vs-know-how rule.** `worker/worker.js` SCOPE + new "MACHINES — specs vs. know-how" block: property-specific **specs** come only from the digest ("not logged — check the manual"; recalled specs dangerous when modified — GTI 91+ because APR-tuned); general **know-how** (cold-start, hold-vs-tap, premix) answered plainly.
- [x] **2b — Few-shot exemplars** — new "MACHINES — a few worked examples" block: living-for-contrast, spec-logged, spec-NOT-logged, know-how, both-in-one-message.
- [x] **2c — Reframe REGISTER** to "one caretaker's range — match words to the thing." Dropped "DROP the field-journal voice entirely" + "never blend the two registers."
- [x] **2d — Refusal rule** added to UNCERTAINTY + NEVER: decline the actual question, never substitute an easier adjacent one as help.
- [ ] **2e — Verify (owner: Paul, phone):** ask the starter question ("hold or tap on a cold start?") → answered plainly; ask "what oil does the lawnmower use?" → logged spec or honest "not logged."

## Phase 3 — Close the capture loop *(the unshipped half)* — DESIGN RATIFIED 2026-07-07
Design pass: ux-expert `.ux-reviews/2026-07-07-machine-note-capture-surfacing.json` + engineering-partner `.engineering/2026-07-07-review-vehicle-note-capture-path.json`.

**Ratified decisions (Paul 2026-07-07):**
- **Mechanism = private notes store + hand-promote** (NOT Git-commit-to-`vehicles.json`). Note → ObservationStore (local + KV) tagged `vehicleId`, instant save; surfaced on the vehicle card as **"Field notes — to sort"**; Paul promotes keepers into the formal `restoration[]` list by hand in the terminal. Reasons: public-repo PII (VIN-purge inversion), the `restoration[]` status requirement would force AI-on-capture or form-friction, and re-inline/commit drift.
- **Mode = ask-then-log** → ship the conversational fence only. **On-card per-vehicle input DEFERRED** (build only if cold-log signal appears).
- **Machine-capture is Paul-primary** (Mom's machine interest is ask-only).

**BUILT + browser-verified 2026-07-07 — awaiting deploy/push (worker + GH Pages).**
- [x] **3b — Fence:** `worker.js` new "WHEN THE READER WANTS TO LOG SOMETHING ABOUT A MACHINE" section emits `suggest-log` with `noteType:"vehicle-note"` + the specific vehicle name; verbatim guarantee mirrored.
- [x] **3c — Resolver:** `resolveVehicleByName` added — exact id/name/nickname, then contains-scan that *collects all hits* so 2+ reads as ambiguous (returns null/ambiguous, never first-matches). Verified: "Desert Storm"→DR-Z, "DR-Z400S"→unique, "the Suzuki"→no-guess, "spaceship"→null.
- [x] **3d — Writer:** `fnSaveNoteOnVehicle` + `parseLogFence` extended; entry carries `vehicleId`/`vehicleName`/`source:"guru-vehicle-log"`; save is instant (local+KV), `sanitizeEntryForStorage` spreads it through untouched. logBtn branches on noteType; ambiguous/no-match saves name-only (never lost, never misfiled).
- [x] **3e — Card render:** "field notes — to sort" collapsible panel on each vehicle card, reads `fnLoadAll()` by `vehicleId`, newest-first; re-renders on `ObservationStore.onChange` (cross-device). Verified rendering a note end-to-end.
- [x] **3f — Data fix:** nickname "Desert Storm" added to `drz400s-2001`; `VEHICLES_DATA` re-inlined; digest rebuilt (only `vehicles` changed; "Desert Storm" now in digest).
- [ ] **3g — Verify (owner: Paul, phone):** replay turn 2 ("log that as an improvement area in the backlog") on the live app → lands as a DR-Z field note on the card.
- Deferred: optional `tools/*.py` lister for un-promoted notes; on-card per-vehicle input (ask-then-log makes it unneeded for now); "which one?" disambiguation chip (name-only fallback covers the rare ambiguous case).

## Phase 4 — Polish & hardening
- [ ] **4a — Machine-answer visual treatment** (Mom / no-glasses): render specs in a block echoing the Vehicles spec-table, not prose identical to a nature reply.
- [ ] **4b — Hedge placement:** move "[unconfirmed — verify…]" from a droppable *trailing* suffix to a *leading*, non-optional token.
- [ ] **4c — Digest drift alarm:** rebuild-and-diff `digest.json` at session-start (there's a drift check for `viewer.html` inlines but none for the digest). Document the rebuild→commit→deploy ritual.
- [ ] **4d — Token headroom note:** digest ~75K vs. the 80K tool-use-migration trigger (~5K headroom); plants prose is where slack lives if needed. No action now.

## Phase 5 — Verify end-to-end + principles
- [ ] **5a — Replay** the full real transcript (turns 0–3) against the new Guru; both refusals should now resolve.
- [ ] **5b — Principles to confirm + add:**
  - ux: promote *"A correct 'no' still owes a next move"* to cross-project (2nd occurrence).
  - ux (Fernwood): *Register is carried by chrome, not just words — esp. for the no-glasses reader.*
  - ux (cross-project): *Decline the question asked — don't answer an easier adjacent one.*
  - ux: *A bolted-on register is a sign of a bolted-on job.*
  - ai-advisor (candidate, needs 2nd occurrence): *Downgrade trust in code at the build/storage boundary; let the model only narrate the downgrade.*
  - eng: *Bundled context needs a drift alarm* (Fernwood) · *Fixing the ask half implies the log half* (cross-project).

## Gates & guardrails
- Every `wrangler deploy` waits on Paul's explicit go (production, outward).
- All capture writes stay deterministic/AI-free (fence offers, client writes on confirm).
- Phase 0 is independent and can ship before the Phase 1 decision.
