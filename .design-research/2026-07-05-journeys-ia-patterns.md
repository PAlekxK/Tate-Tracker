# Fernwood — Journey-Driven IA & Pattern Candidates

**Date:** 2026-07-05
**Author:** ux-expert
**Method:** Journey inventory → information organization → UX pattern candidates → coherent IA concepts. Grounded in the real `.user-research/` artifacts + established telemetry, and pattern-matched against interaction-design *authorities* (Apple HIG, NN/g) rather than genre/aesthetic sites.
**Supersedes (in approach):** the 2026-07-05 benchmark-gallery doc, which Paul rejected as too genre-anchored. This doc keeps what that work established — the telemetry, the identity constraints, the two-intent (Save vs Ask) tension, and the look-fors flywheel concept (Paul liked the *idea*, not the gallery) — and re-founds the rest on journeys.
**Status:** Working material for a working session. Not committed, not a decision.

**One critical grounding fact carried throughout:** the 2026-07-02 Garden Guru conversational redesign already **shipped** (chat-model composer; verbatim log-an-observation with an unmissable "Noted ✓"; add/remove-a-plant from conversation; a single pull-not-push follow-up chip). So "the composer" below is not a proposal — it's a live surface these concepts must *place*, not invent.

---

## Part 1 — Journey inventory (ground truth)

The actual journeys, combined from the persona/JTBD artifacts and the telemetry. Frequency and evidence tags kept honest: `validated` = behavioral data; `inferred-strong` = data-consistent but not isolated; `inferred` = artifact/logic only; `contested`/`out-of-scope` flagged.

| # | Journey | Actor | Trigger | Frequency (evidence) | Device / context | "Done" feels like | Tag |
|---|---------|-------|---------|----------------------|------------------|-------------------|-----|
| **J1** | **Daily glance** — scan what the place is doing, leave | Mom | Morning coffee / evening wind-down, phone in hand | **Dominant. 51 of 91 sessions expand zero cards; active 29/35 days; historically ~4.5 sessions/day** | iPhone, one-handed, reclined, half-engaged, **no glasses** (22 A/A+ toggles), often off-property | "I saw what the place is doing and felt connected — put the phone down" | `validated` |
| **J2** | **Ask the property** — a stewardship question or an ID | Mom | Sees something she can't name; a fertilize/transplant/amend/diagnose question | **Emerging pattern. 16 conversations / 40 days; one-shot (15/16 single-turn — now understood as *satisfied*, not blocked)** | iPhone, on- or off-property | "Got a good answer in *this-property* voice" | `validated` |
| **J3** | **Log an observation** — note a seasonal change on a known plant | Mom | Notices something changing (lily-pad dieback) and wants to record + ask in one breath | **Emerging (drove the shipped Phase 2). Real gap was logging-*with-confidence*** | iPhone, often on-property | "I told Fernwood what I saw and I'm **sure** it's logged" (the "Noted ✓" now closes this) | `validated` (job) / shipped-fix |
| **J4** | **Leisure browse** — open with no aim, take a contemplative moment | Mom | No specific goal; morning/evening; "just look at the place" | `inferred-strong` — Celestial 47 views though purely contemplative; Almanac highest expand-rate | iPhone, leisure posture | "That was nice" — no task, no obligation | `inferred` |
| **J5** | **Revisit a saved thing** — find something read before | Mom (mostly) | An entry/plant/note/answer caught her attention before | **Validated at scale. 77 `entry_revisited` events; 0 stars** — revisit-not-mark is the behavior | iPhone | "Found it again without having to organize anything" | `validated` |
| **J6** | **Reference lookup** — retrieve a specific durable fact | Paul | Needs a vehicle spec, a service contact to call, a property fact, a source | `inferred` — rich vehicles/sources data + build behavior; low-frequency, deliberate | Both; on-property (mobile) or desk (desktop) | "Got the spec / made the call" | `inferred` |
| **J7** | **Planning session** — decide plantings, follow a research thread | Paul | Planning what to plant; a research thread; a build session | `inferred` — episodic, desk, desktop | "Decided what could grow here / integrated a thread" | `inferred` |
| **J8** | **Show the place to a visitor** | Paul-mediated | A friend/family member visiting asks about Fernwood | `inferred` / **likely out-of-scope** — Paul has deliberately scoped personal | Either | "Shared the place without explaining from scratch" | `inferred` — **flag, don't design** |

**Two load-bearing reads from the inventory:**
1. **The dominant journey (J1) has no designed home.** Mom's most frequent act is a *time-slice glance* — and the app answers it with an 11-category accordion she has to scan header-by-header. Every concept in Part 4 is judged first on how well it serves J1.
2. **Paul-as-daily-user has largely become Paul-as-builder** (telemetry: his mapped iPhone went quiet). J6/J7 are real but *deliberate and infrequent* — which is exactly the argument for putting durable reference somewhere retrievable-on-demand rather than on the daily surface.

---

## Part 2 — Information organization (by kind, independent of current cards)

Classifying what actually lives in the 11 cards by **information kind** — because the current card boundaries are drawn by *category* (weather, plants, wildlife…), and the journeys cut across those boundaries by *kind* and *time*.

| Kind | What it is | Lives today in (cards) | Which journeys touch it |
|------|-----------|------------------------|-------------------------|
| **Live status** | Changes hour-to-day: current temp/condition, radar, rainfall, conditions | Weather | J1, J4 |
| **Cyclical / seasonal reference** | Predictable by season: plant care windows (`peakWindow`/`narrow`/`months`), "this month" plants, bird/amphibian presence (`monthsPresent`), celestial events, turf, frost dates | Plants, Wildlife, Sky & Stars, The Fairway | J1, J4, J2 (context) |
| **Durable reference** | Rarely changes: property identity (elevation, soils, watershed, microclimate, Cherokee history), vehicle specs + restoration lists + service contacts, sources, candidate plants | Fernwood/Property, Vehicles, Sources, Worth considering | J6, J7 |
| **Records / logs** | Accretes, personal: almanac field notes, Guru conversations, promoted species, observations | The Almanac | J2, J3, J5 |
| **Meta** | About the app itself | Recent updates | (none — near-zero telemetry) |

**Where the current boundaries misfire — the real output of Part 2:**

- **J1 needs a *slice across kinds*, but the cards are cut by category.** The glance wants: live status (weather now) + the 2-4 cyclical things happening *this week* (a bloom opening, a bird arriving, a meteor shower) + maybe a fresh record. That slice is spread across **four different cards**, so "the glance" degrades into "scan 11 headers." **The card taxonomy is orthogonal to the dominant journey.** This is the core IA finding.
- **Durable reference sits at the same visual tier as living surfaces.** Property, Vehicles, Sources, Worth-considering (all *durable reference*, touched only by Paul's deliberate J6/J7) occupy the same daily real estate as Weather and Plants (*live/cyclical*, touched by Mom's dominant J1). A kind-mismatch on the daily surface.
- **Cyclical reference is scattered with no cross-category "this week."** Plants has a "this month" view; nothing composes *this week across plants + wildlife + sky*. The look-fors flywheel is precisely a cross-category cyclical-reference surface — which is why it has no home in the current taxonomy.
- **The Almanac card correctly co-locates two kinds** (records + the ask/log composer) — that pairing is coherent (the conversation *produces* the record) and shipped. Worth preserving as a unit.
- **Meta (Recent updates) is dead weight** on the daily surface (2 expansions/35 days).

---

## Part 3 — UX pattern candidates per journey

Sources here are interaction-design authorities, not aesthetics: **Apple HIG** (the grammar Mom already owns on her iPhone) and **NN/g** (progressive disclosure + information scent). Verified references in Sources.

### J1 — Daily glance (the priority)

- **"Today"/widget summary surface** (Apple HIG — Today view & Home-Screen widgets). A composed, glanceable, *no-tap* summary that aggregates a time-slice across sources. This is the exact grammar Mom operates daily: a widget shows the answer without being opened. **Fit:** serves the 51/91 measured behavior directly; Mom-access strong (large type, no tap targets, meaning by size/position not small labels); identity: "looking out at the land," not a control panel. **Vanilla weight:** medium — a compose function over the summaries the teaser strip already computes.
- **Widget stack / at-a-glance row** (Apple HIG — widget stacks). The existing 4-tile teaser strip is a proto-widget-row; promote it to the *primary* surface rather than a teaser above the "real" cards. **Weight:** low-medium.
- **Strong information scent into the cards** (NN/g — information scent is the key success factor for progressive disclosure). Whatever the glance shows must clearly signal what's deeper, so tapping in is confident. **Weight:** low (copy + affordance discipline).

### J2 / J3 — Ask the property / Log an observation

- **Composer-as-primary (universal chat model)** — *already shipped 7/2*. The pattern is validated and is her #1 destination. The design task is *placement*, not invention: how prominent, and where relative to the glance. **Fit:** strongest evidence in the app. **Weight:** none (built) — placement only.
- **Sheet with detents** (Apple HIG — Sheets: "a scoped task closely related to the current context"; resizable detents since iOS 16). The ask/log could rise as a bottom-sheet over the glance — present when invoked, dismissable, never a card buried eight scrolls down. **Fit:** matches the "quick ask then back to looking" rhythm; keeps the composer reachable from *anywhere* without living permanently in the stack. **Weight:** medium (a vanilla bottom-sheet is doable; interaction-state care needed).
- **Seeded prompts as information scent** (shipped; NN/g scent) — lowers "what do I say?" for J3's leisure posture. Pull, not push. **Weight:** none (built).

### J4 — Leisure browse (contemplative)

- **"For You" / Memories composition** (Apple HIG — Photos' For You surfaces a curated, no-query-required thing to look at). For a user with *curiosity but no formed question*, compose "here's something from the place right now" — the seasonal look-for, tonight's sky, a resurfaced past note. **Fit:** exactly J4's shape; identity-strong; Mom-access strong (no query, no small labels). **Weight:** medium (a selection/rotation function). This is also the natural home for Celestial's contemplative draw, which today is stranded in a low-expand card.
- **Gentle single-scroll editorial** — keep, but restraint over spectacle. **Weight:** low.

### J5 — Revisit a saved thing

- **Recents / passive resurfacing** (Apple HIG — Recents; Photos resurfacing; NN/g — recognition over recall). The behavior is *revisit, not mark* (77 revisits, 0 stars). Stop asking her to curate; instead surface "you came back to this" and keep recently-touched entries reachable. **Fit:** matches validated behavior precisely; retires the dead star. **Weight:** low-medium (revisit data already captured).
- **Conversation-on-the-entry** (from unserved Job 9) — a Guru conversation about the lily pads lives *on* the lily-pad record, not in a separate chat history (which the eval rubric explicitly wants to avoid feeling like). **Fit:** memory-shaped not database-shaped; solves the write-only-conversation gap. **Weight:** medium.
- *(Rejected: query search — Mom doesn't retrieve by typing a query; low fit.)*

### J6 / J7 — Paul's reference lookup & planning

- **App Library "curated-first-screen + everything-in-a-drawer"** (Apple HIG — the Home Screen shows what you use; the App Library holds *everything*, one swipe away). Durable reference (Vehicles, Property, Sources, Worth-considering, Recent updates) goes behind **one** drawer entry; the daily surface stays living. **Fit:** the two-tier split, justified by journey frequency (J6/J7 are deliberate + infrequent); Mom never has to see it, Paul reaches it on purpose. **Weight:** low (regroup existing cards + one collapsible entry).
- **Tab bar for top-level kinds** (Apple HIG — tab bars = top-level sections). If the app ever needs more than a drawer, a small tab bar ("Today / Almanac / Reference") maps cleanly to the kind taxonomy from Part 2. **Fit:** Paul's deliberate retrieval; **Mom caution** — a persistent tab bar adds chrome and a navigation decision she may not need. **Weight:** medium.
- **Search / jump-to (Spotlight-style)** for Paul's goal-directed lookups only — not on Mom's surface. **Weight:** medium.

### J8 — Show a visitor
**Do not pattern-match.** Flag to Paul as a scope question, not a design one (his deliberate personal-scope choice argues against it). Named here only so it isn't silently designed for.

---

## Part 4 — Coherent IA concepts

Three whole-app concepts. Each = **first screenful + navigation model + where each info-kind lives**. Scored against the journey inventory below.

### Concept A — "Today + Reference Drawer" (the App Library model)
- **First screenful:** a composed **Today at Fernwood** glance — live weather status + 2-4 cyclical *look-fors* for this week (the flywheel surface) — with the shipped **composer** directly beneath it (reachable, or rising as a sheet).
- **Navigation:** below the glance, the ~5 *living* cards (Weather, Plants, Wildlife, Sky, Almanac) in a single calm scroll; **all durable reference** (Property, Vehicles, Sources, Worth-considering, Recent updates) behind **one** "Reference / The Ledger" drawer entry.
- **Where each kind lives:** live + cyclical → the glance and living cards; records → the Almanac (with the composer); durable → the drawer; meta → the drawer.
- **Why it fits:** serves the measured dominant journey (J1) with a purpose-built surface, absorbs the shipped composer (J2/J3) and the look-fors idea, retires dead weight, and honors Mom-accessibility (glance-first, no new chrome). **Lowest-risk, highest-yield.**
- **Weight:** low-medium. **Main risk:** the glance becomes a dumping ground — needs an editorial rule ("only what's *doing something* this week").

### Concept B — "Time-first Almanac" (temporal spine)
- **First screenful:** **This week at Fernwood** — the glance *is* a time-slice composed across all categories (what's blooming, arriving, in the sky, what the turf needs), with the composer.
- **Navigation:** the **primary axis is time** (this week → this month → the year); **category becomes a secondary "by subject" lens** over the same data; durable reference in a drawer as in A.
- **Where each kind lives:** cyclical reference is *promoted to the organizing principle*; live status leads each time-slice; records in the Almanac; durable in the drawer.
- **Why it fits:** the deepest expression of the field-journal identity (Leopold is month-by-month) and the strongest answer to J1 and J4 — the glance and the contemplative browse are both time-slices. **Weight:** high (re-slices existing per-category data by time — feasible, since `months[]`/`peakWindow`/`monthsPresent` already exist, but real work). **Main risks:** aseasonal content (Vehicles, Property, Sources) has no natural place on a time axis — so B *must* be combined with A's drawer; and it asks Paul's J6 reference lookups to route through a subject-lens (mild friction).

### Concept C — "Conversation-first" (composer as home)
- **First screenful:** the composer as the front door + a light glance; cards demoted to what Guru surfaces or a browse-shelf.
- **Navigation:** ask-first; content pulled up conversationally.
- **Where each kind lives:** records/conversation central; everything else is context the engine reads.
- **Why it (mostly) doesn't fit:** it optimizes J2/J3 — but **Mom's dominant job is the glance (J1), and she's a *satisfied one-shot* asker, not a conversationalist.** A composer-home spends the whole first screenful on her *rarer* behavior and gives her contemplative/glance jobs a cold "ask me anything" open. **Presented for completeness and rejected as a whole-app model** — its one true insight (composer prominence) is already captured inside A and B. **Weight:** medium. **Main risk:** builds for the behavior the telemetry says is *not* dominant.

### Concept × Journey matrix

| | J1 glance | J2 ask | J3 log | J4 leisure | J5 revisit | J6 Paul ref | J7 Paul plan |
|---|---|---|---|---|---|---|---|
| **A — Today + Drawer** | ✅ serves well | ✅ | ✅ | ➖→✅ | ➖ | ✅ (drawer) | ✅ |
| **B — Time-first** | ✅ serves well | ✅ | ✅ | ✅ serves well | ➖ | ➖ (via subject lens) | ✅ |
| **C — Conversation-first** | ❌ harms | ✅ serves well | ✅ | ➖/❌ | ✅ if browsable | ➖ | ➖ |

✅ serves well · ➖ neutral · ❌ harms

### Recommendation

**Ship Concept A now; hold Concept B as the identity-forward next step.**

- **A is the correct near-term move** because it serves the *measured* dominant journey (J1) at low-medium cost, cleanly places the already-shipped composer (J2/J3), gives the look-fors flywheel its first real home, retires the dead star (J5 → passive resurfacing) and the dead meta card, and adds *no* new navigation burden for Mom. It's an evolution of surfaces the app already has (teaser strip → glance; 11 flat cards → 5 living + 1 drawer), not a rebuild.
- **B is where A wants to grow.** Once the glance surface proves out, promoting *time* from "a thing inside cards" to "the organizing axis" is the move that most deepens the field-journal identity — but it's a data-re-slice worth doing only after A validates that a composed glance is what Mom's J1 actually wanted. B also structurally depends on A's drawer for aseasonal content, so A is a prerequisite either way.
- **C is rejected as a whole-app shape** (it contradicts the glance telemetry) but its composer-prominence lesson is already inside A and B.

**The through-line:** the fix isn't a prettier card stack — it's re-cutting the app so its primary surface matches its primary journey. Today the taxonomy is *category*; the dominant journey is a *time-slice glance*. Concept A closes that gap cheaply; Concept B closes it completely.

---

## Sources
- Apple Human Interface Guidelines — [Navigation & search](https://developer.apple.com/design/human-interface-guidelines/navigation-and-search) · [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) · [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)
- Nielsen Norman Group — [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) · [Information Scent](https://www.nngroup.com/videos/information-scent/) · [Managing Visual Complexity](https://www.nngroup.com/videos/managing-visual-complexity/)
- Fernwood internal (not external): `.user-research/` persona-mom, persona-paul-co-steward, jtbd-2026-05-27, journey-unified-field-assistant, 2026-07-02-mom-behavior-interpretation; the established KV telemetry; project `CLAUDE.md` (7/2 shipped redesign).
