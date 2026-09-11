# UX — the card-intro ask: SURFACE AND PLACEMENT

`ux-2026-09-11-ask-design-surface` · review mode · **recommendations only, Paul rules** · no surface was edited.
Review level: **screen-component**, stated to generalize (the playbook needs a rule, not a weather decision).

## THE RECOMMENDATION, first

**(E) the two-moment split — but drawn one notch later than the weather plan draws it.**

| moment | what it may ask | why there |
|---|---|---|
| **setup, beside the address** (W-10's ruled site) | only asks that must be answered **before the card can render honestly** — a credential (your own station), a fetch we will not make unasked (radar), an applicability fact the address cannot give | the promise is made there; these have no referent on a screen and never will |
| **the card's own face, first appearance, born open** (A) | **which sub-components to show** — UV · pollen · air quality · frost · wind · … | the referent is on the screen. Paul's own sentence is *"when we first introduce a card"* |

⚠️ **This is a recommendation against a line in the weather plan, not against a Paul ruling.** W-10 (*"Six sounds good"*) rules the site of **the two existing opt-ins** (radar · station). *"one multi-select at setup plus a free text"* for the **eight advisory classes** is `0-PRIME-C`'s extrapolation of that ruling, and it is the part I would move. Eight abstractions at setup asks a person to rank things they have never seen — recall, not recognition (Nielsen #6) — from inside an onboarding that already carries recognised · address · contact · email · interests · wait. At the card, each chip has a thing on the screen next to it.

**Rejected, with reasons:** **(B) a row above the card** — a second altitude for the same subject, and *Source-hierarchy drives layout* says the card's own preference belongs in the card, not stacked over it. **(C) everything at setup** — above. **(D) the confirm queue** — three disqualifiers: an intro ask has no `entityRef` and no `_foldTarget`, so it would ship as a `reflective` card and **pin the feedback watermark by design** (CLAUDE.md's named one-state-that-cannot-clear-itself); the effective visible set is **1**, so every intro ask costs the one canon question we get; and the queue is where we ask about *the world*, while this asks about *the app* — two different acts at one door.

---

## 1 · THE OPTIONS, read against the measured reader

Measured, and it governs everything below: **depth-2 and depth-3 are zero** — she reads card faces and does not open individuals. **Every ask-shaped affordance is 0-for-35; the jump strip, which only moves her, took 5/5.**

| | depth | affirmative grammar | cost to the 1-slot cap | at 414 × A+ | failure mode |
|---|---|---|---|---|---|
| **A · on the card's face, born open** ⭐ | **face** (body of an `expanded` card — the `renderEmptyCards` born-open precedent) | chip set; chosen chip = **`gg-suggest-btn-yes`** (filled green + ✓, persistent); unchosen = outlined neutral | **zero** — it is not in the queue | 5 chips ≈ 4 rows ≈ 216px + title/why ≈ **300px**, most of the fold under a 90px header. **8 chips is a wall** | the face becomes a form; the card's content is pushed below the fold on the one screen where it should be showing what it holds |
| **B · a strip above the card** | face, but a **second** face | same | zero | steals the card's own top | two altitudes for one subject; reads as chrome, and chrome is what she scrolls past |
| **C · setup, beside the address** | face (a step is all face) | the existing numbered ranked rows (`.interest[aria-pressed]`) | zero | fine — a step owns the viewport | asked before the referent exists; and every field added here is a field `elicitation-lens` counts against the **derived-facts-per-asked-field** ratio at the step that can least afford it |
| **D · the confirm queue** | face (queue is at top) but **one at a time** | ratified already | **total** — it *is* the slot | watermark pin · starves canon questions · wrong act at that door |
| **E · the split** ⭐ | both, each at its own depth | both of the above | zero | each moment carries ≤5 | the seam: a person who declined radar at setup must not be re-asked at the card — one declaration, two doors |

**Not an option: a disclosure.** Anything behind "Open ▼" is content she has not seen. If it will not fit on the face, cut the chip set — do not fold it.

---

## 2 · THE CLOSE

**a · "you asked for this" — in the card, immediately, at runtime.** The tap must change the thing under her thumb: the sub-component appears **in place in the same card**, and carries a quiet first-run tag — *"You asked for UV."* — that decays after a set number of opens. This satisfies the toolchain inventory's clause (*if a tap switches a card on, say so on the screen*) and Norman's feedback primitive at the only moment it is cheap.

⛔ **Do not gate the close on the acknowledgment ribbon.** The ribbon is a **build-time literal**; there is no per-household runtime ribbon until lap 8 row G lands its instance seam. A ribbon line is the *right* second receipt (her event, her attribution, `links:[{phrase,card}]` straight to the card) and it should be filed as owed — but a close that requires a rebuild is not a close.

**b · the none-chosen state.** *None is the honest empty.* Chose nothing → **no ribbon line, no told-row, no "you chose nothing"** (the existing rule already reads *an empty ranking is not a missing one*), and the card renders its base set in its ordinary voice. And the ask **retires after its second appearance** — otherwise it becomes the standing *"add data"* button the governing principle forbids by name, on the face, for a reader who is 0-for-35 on asks.

**c · where she changes it later — name the control.** Two sites, one editor:

1. **canonical — the card.** After the ask retires, it demotes to one quiet line at the foot of the card body: *"Showing: UV · pollen · **Change**"*. Meet the user at the action.
2. **mirror — `/settings/place/`**, which already holds name · journal name · colour and is the right home for the **full** list, including classes the card is not showing.
3. **`What you told me` (`#card-told`) gets a read-only receipt row that LINKS to (1)** — it is a reference, not a second editor (the 09-08 ruling on that card).

⛔ **The trap that makes EVERYTHING IS CHANGEABLE false: turning a thing OFF must never remove its own control.** If "no pollen" deletes the pollen row, the control is gone with it — hence the Settings mirror is not optional, it is what makes the claim true. **This is already broken once today:** `#card-told` tells a person their contact preference is *"The default — change it whenever you like"* and **no control exists at either site**.

---

## 3 · THE CAP, as a rule the playbook can enforce

Stated on the **existing** axis — `questions.json _ordering`: *an answer that unblocks a BUILD > one that fills a canon gap > a verdict on our own guess.* No new axis is minted.

1. **One ask per screen.** Not per card — per screen. Precedent is already in code (*ONE INVITATION PER MODULE*, written because the seats counted six asks on one screen).
2. **One introduction at a time.** A household is introduced to one module at a time, in `READER_RANKING` order, which already exists. The intro ask rides the introduction and dies with it.
3. **A card-intro ask is BUILD-class**, so it outranks canon-gap and verdict cards — **and therefore it suppresses the confirm queue for that load**, rather than sitting beside it. The effective visible set is 1; two asks on one screen is a 1-slot budget spent twice.
4. **Bounded by construction:** an intro ask is offered at most twice, only while its card is being introduced, and never again. That bound is what keeps rule 3 from starving the canon queue.
5. **Open at once, per household: at most one.** Anything beyond it benches, through the existing bench + `--approve` human gate. No second queue.
6. **≤5 chips on a face**, filtered by applicability first (W-9's address-derived source rule — do not offer fire-weather where it does not apply). Five is `MAX_VISIBLE`, borrowed rather than invented. The remainder lives in Settings, never on the face.

---

## 4 · `renderAskNext()` — same component, two hosts

**Keep** (it is closer to Paul's ask than anything else in the repo): born-open card · chips from a declared copy table · **per-tap commit** (no Save button, nothing to lose) · deterministic AI-free POST with a typed `context` · grant attribution · re-render on tap · placement after the reader's own cards.

**Change:**
- **the chips have no selected state** — a tap makes the chip *vanish* from the choice set. Give it the ratified grammar: chosen = `gg-suggest-btn-yes` (filled green + ✓), unchosen = outlined neutral, **the literal components, not lookalikes**.
- **a tap says nothing on the screen about what it switched on** — the new card appears elsewhere in the list, possibly below the fold.
- **it is unreachable in both branches** (`:18525` returns when `__HOUSEHOLD_NAME` is truthy; `:18527` returns when it is falsy). The resting is deliberate; the second gate is not what the comment describes. Flagged, not touched.
- **the answer has no durable landing** (module state is a build artifact) and **no reader**. Both are the four-field contract, not cosmetics — see F7.

**Same component or sibling? One component, two hosts.** Two ask components is two affirmative grammars drifting apart, which is precisely what the 07-29 standing rule forbids. Extract one block — *title · one-line why · chip set · per-tap commit · persistent selected state · the "what this switched on" line · one open-text door* — and host it (i) as its own card at **module** scope, (ii) inside a card at **sub-component** scope. The single real difference: the module-scope ask changes something **elsewhere** and therefore owes a pointer; the card-scope ask changes the card under the thumb and does not.

**The open door stays a door, not a box.** W-13's shape (b) — the free text that produced *"Houseplants!"* and feeds `read-onboarding`'s WHAT'S MISSING line — should reuse the existing `.empty-invite-ask-btn` → `FeedbackRibbon.open({section:"card:<mod>"})` pattern: one underlined italic line, scoped to the card. A textarea on the face is a sixth input affordance in front of a reader who has taken zero of thirty-five.

---

## 5 · FINDINGS

| id | sev | claim | evidence | fix | falsifier |
|---|---|---|---|---|---|
| **F1** | critical | A tap on an ask chip produces **no persistent state and no on-screen consequence** — the chip disappears and the result may be off-screen | `template:18538–18557` (chip removed by re-render; no selected class) · toolchain INVENTORY §4 *"if a tap switches a card on, say so"* · Norman: feedback | selected state in the ratified grammar; the change happens **in place**; a named pointer only if it cannot | a seat taps a chip and can say what changed **without scrolling** |
| **F2** | critical | **EVERYTHING IS CHANGEABLE is claimed with no control.** `#card-told` says *"change it whenever you like"*; `/settings/place/` holds only name · journal · colour | `template:19989` · `settings/place/index.html:89–113` | name the control at both sites before any new preference ships; **an off state keeps its own control** | every line on `#card-told` that says a thing is changeable resolves to a tappable control in ≤2 taps |
| **F3** | important | Eight advisory classes **at setup** asks for decisions before the referent exists | Nielsen #6 recognition-over-recall · the setup already runs 6 screens · `0-PRIME-C` extrapolates W-10 (which ruled only radar + station) | split: source/credential asks at setup, presentation asks at the card's first appearance. **Paul rules** | a setup walk shows a seat who can restate what "pollen advisory" will look like on their card |
| **F4** | important | **Two asks can be live in one load** with no rule — queue head + intro ask — against an effective visible set of **1** | `questions.json:450` (*every offer position 0; `momqueue_tapped` 3 in 60 days*) | §3 rules 1–4: intro ask is build-class, suppresses the queue for that load, bounded to two exposures | a walk on the introduction load counts exactly one ask-shaped affordance on screen |
| **F5** | important | At **414 × A+**, 8 chips ≈ 300px of ask above the card's content | `body.text-lg` chips 17px / 44px min-height; 382px usable width | ≤5 chips, applicability-filtered; remainder to Settings | `herConditions()` shows the card's first content row above the fold with the ask present |
| **F6** | important | `renderAskNext()` **returns in both branches** — dead even after the rest is lifted | `template:18525` and `:18527` | flag to Paul before anything is built on it (not touched — three windows live) | the function renders for exactly one of the two flag states |
| **F7** | important | The ask **promises persistence it does not have** — module state is a build artifact, `ask_next_added` has no reader | INVENTORY §4 items 4–5; `/api/door` is the named precedent | a declaration the next load reads, plus one command that prints who was asked and what they chose — **before** the ask ships | a tap changes the **next page load**, and one command prints the answers |
| **F8** | important | In a shared household the ask **does not say whose view it changes** | `elicitation-lens` CONTRACT `who-sees`; J7 second-member is ruled future | one clause on the ask: whose screen this changes, and whose it does not | a second-member walk's stop carries the `who-sees` clause |
| **F9** | nice-to-have | The ask block risks shipping without the **four contract clauses** (use · not-use · who-sees · reversible) | `tools/elicitation-lens.py:43` | one line under the title carrying *use* + *reversible*; the who-sees clause per F8 | `elicitation-lens` reads the intro stop and finds all four |
| **F10** | nice-to-have | An unretired intro ask becomes the **standing "add data" button** | CLAUDE.md § the glance and the repository (affordance-without-signal) | retire after the second appearance; demote to the *"Showing: … · Change"* line | the ask is absent on the third load, and the control is still reachable |

---

## OPEN QUESTIONS FOR PAUL

1. **F3 is the one that needs your word:** do the advisory classes move from setup to the card's first appearance, or does W-10's site absorb them as the plan assumed?
2. Does a preference ever earn a **ribbon line**, or is the ribbon reserved for answers about the world? (It is her event and it is attributable — but the ribbon has no runtime path until row G.)
3. Is the interest declaration **per person** or **per household** when a second member arrives? F8 cannot be worded until this is ruled.

## PRINCIPLES TO PROPOSE (not written to the library — your call)

- **fernwood** · *Ask at the referent.* A preference question is asked where the thing it governs is on the screen; asked earlier it is recall, and recall is where a reader whose fear is being wrong stops answering.
- **cross-project candidate** · *A claimed-reversible needs a named control, and turning a thing off must not remove it.* (Second occurrence of the shape: the contact-preference line, and now the interest chips.)
- **cross-project candidate** · *One ask per screen; an ask that changes the app outranks an ask about the world, and pays for it by suppressing the other.*
