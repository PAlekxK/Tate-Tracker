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

## Phase 2 — Core scope fix *(the fix that answers the original question)*
Independent of the fork as long as ASK stays in Guru (true for recommendation + option A).

- [ ] **2a — Specs-vs-know-how rule.** Replace the machine SCOPE lines in `worker/worker.js` (~L432–441) with the two-part rule: property-specific **specs** come only from the digest ("not logged — check the manual"; recalled specs are dangerous when the machine is modified — cf. the APR-tuned GTI needing 91+); general **know-how** (cold-start, hold-vs-tap, premix) gets answered plainly.
- [ ] **2b — Few-shot exemplars** in the REGISTER block: a living answer, a machine spec-*refusal*, a machine know-how *answer*, and a both-in-one-message answer. (Shown register beats described register for Haiku.)
- [ ] **2c — Reframe REGISTER** from "two voices to toggle / never blend" to "one caretaker's range — match words to the thing." Removes the mode-toggle that invites boundary confusion.
- [ ] **2d — Refusal rule:** decline the *actual* question plainly + point somewhere concrete; never answer an easier adjacent question as if it were help. (Kills the "where do you park it" misdirect.)
- [ ] **2e — Verify:** replay turn 0's starter question — Guru should now answer the technique plainly in shop-hand voice.

## Phase 3 — Close the capture loop *(the unshipped half)*
Destination is the vehicle's `restoration` backlog regardless of fork; entry-point UX depends on 1a.

- [ ] **3a — Interim (near-free, do with Phase 2):** make Guru's prose tell the true fallback so words are never lost ("hit Save and it'll land in the Almanac") until the real writer exists.
- [ ] **3b — Fence branch:** add a vehicle variant to the `suggest-log` fence (`worker.js` ~L531–549), currently plant-only language.
- [ ] **3c — Resolver:** add `resolveVehicleByName(VEHICLES_DATA)` in `viewer.html` (none exists today).
- [ ] **3d — Deterministic writer:** append the note to the vehicle's `restoration` list (AI-free write — capture-path principle holds; the fence *offers*, the client *writes on confirm*).
- [ ] **3e — Verify:** replay turn 2 ("log that as an improvement area in the backlog") → lands on the DR-Z's backlog, not an untagged Almanac note.

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
