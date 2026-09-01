# Contractor register — a PROPOSAL, not applied

`paul-raised 2026-09-01`: *"the value of just some reference information — like contractors, trusted
contractors, the history that you have with them."*

⛔ **Nothing here is applied.** No change to `vehicles.json`. This is a diff for Paul to rule on,
per `[[feedback_agent_proposes_main_session_reviews]]`.

---

## ⭐ THE HEADLINE: do not build this. It already exists, on ONE vehicle out of twenty-two.

`vehicles.json` already has a **`serviceContacts[]`** array with precisely the fields Paul described
— and it already carries **judgment**, in prose, in his own voice:

| field | example, verbatim from the GTI |
|---|---|
| `id` | `expressoil` |
| `name` | Express Oil Change & Tire Engineers |
| `role` | *"**STOP 1** — Paul's regular oil shop, right down the street; **go here FIRST**"* |
| `role` | *"**PREFERRED specialist** — your actual APR tune shop (did the Stage 1 in Sep 2022), so they hold your performance history"* |
| `role` | *"**ALTERNATIVE** specialist + good second quote"* |
| `phone` · `address` · `hours` · `url` | all present |

It even carries a **self-correction**: *"Earlier notes said the APR tune was done here; the service
records show it was actually Eurofed."*

**That is the artifact Paul is asking for.** The design question is not *what should it look like*.

### ⛔ The actual gap, measured 2026-09-01

- **`serviceContacts` exists on `gti-2016` and NOWHERE ELSE.** 6 entries on one vehicle; **21 of 22
  fleet entities have none** — including the Bronco (28 service rows), every piece of yard
  equipment, and all five household systems.
- The fleet has **61 service rows naming 26 distinct vendors**. **25 of those 26 relationships exist
  only as a free-text string on a service row.**
- ⚠️ **`serviceHistory[].shop` does not reference `serviceContacts[].id`.** The contact `expressoil`
  and the 7 rows reading `"Express Oil"` are **not linked by anything**. The register cannot answer
  *"what has this shop actually done for us"* — which is the "history that you have with them" half
  of Paul's ask.
- ⭐ **It is per-VEHICLE, so it structurally cannot hold a shop that serves the fleet.** Express Oil
  serves the GTI *and* the Tiguan; **Garner Ace Hardware serves two chainsaws** and is the only
  vendor in the record touching equipment. Neither can be expressed today.
- ✅ **`serviceContacts` IS in the digest** (`digest_vehicles` keeps `name`/`phone`/`role`/`address`/
  `hours`). So the assistant can already answer *"who do I call about the GTI"* — **and can answer
  it for nothing else in the fleet.**

---

## The proposal, in three moves

**① PROMOTE `serviceContacts` from a per-vehicle field to a fleet-level register.** Same schema —
it is already right. A vehicle references contact ids; a contact may serve many entities. This is
what lets the house, the mowers and the chainsaws have contacts at all, and it is what Paul's
household ask actually needs.

**② JOIN `serviceHistory[].shop` → `contactId`.** Keep the free-text `shop` (it is the invoice's own
words and is evidence). Add an optional `contactId` beside it. 61 rows become a relationship history
for free, and *"when did we last use them / what did they charge"* becomes answerable.

**③ LEAVE JUDGMENT TO PAUL.** `role` already carries it and he wrote every existing one. A new
contact starts with **no** judgment rather than an inferred one. ⛔ Never derive "trusted" from
frequency — the most-used vendor in the record is one he is currently unhappy with.

---

## ⚠️ THE TRAP: three "collisions" I called out earlier, and two of them are NOT collisions

Re-measured properly. **Merging these would fabricate relationships Paul does not have.**

| strings | verdict |
|---|---|
| `Express Oil` (7×, GTI, 2021→2026) · `Express Oil (Atlanta — Moreland Ave)` (1×, Tiguan, 2026-01-16) | ✅ **SAME** — one business, Paul's regular shop |
| `Express Oil Change & Tire Engineers (Canton, GA)` (4×, **Bronco**, **2018→2023**) | ⛔ **NOT the same relationship.** Different location (Canton, not Atlanta) **and Paul did not own the Bronco until 2025-10-07.** These are the **PRIOR OWNER's** service records. Same chain, someone else's history. |
| `Volkswagen of Marietta` · `Volkswagen of Marietta (parts counter)` | ✅ **SAME** business, split by department |
| `eBay (automaall)` · `eBay (DIY parts)` | ⛔ **NOT a collision.** `automaall` is a **seller**; `(DIY parts)` is a **channel note**. Different kinds of fact in one field. |

⭐ **The prior-owner case is the important one and it generalises.** The Bronco carries inherited
history — the record even has a literal `Prior owner (various)` row. **A contact register must record
WHOSE relationship it is**, or the app will tell Paul he has a ten-year history with a shop he has
never walked into. Proposed: a `relationship` field — `ours` | `inherited` | `one-off`.

---

## And `shop` is holding four different kinds of thing

Normalizing on the string alone would flatten these. The register needs a `kind`:

| kind | examples |
|---|---|
| **repair shop** — what Paul means by "contractor" | Midas · Cannon Automotive · Autohaus Social · Eurofed · Tim's Auto Care · Cherokee Muffler |
| **parts supplier** | Summit Racing · Classic Industries · NAPA · 4 Wheel Parts · Weatherstrip Specialists |
| **dealer** | Jim Ellis VW · Volkswagen of Marietta |
| **authority** (not a vendor at all) | Georgia MVD · GA Clean Air Force |
| **hardware / local** | **Garner Ace Hardware** — the only vendor serving equipment |

⛔ **`DIY (Paul)` (13×), `DIY (Mom)`, `DIY (Amazon parts)`, `DIY (eBay parts)`, `Prior owner
(various)` are NOT vendors** and must not become contact rows. They are *who did the work*, which is
a different field that does not exist. **`DIY (Mom)` is a fact about a person sitting in a vendor
column** — and it is the only record of Mom performing fleet work.

---

## Questions only Paul can answer

1. **Where does the register live?** A new top-level `contacts.json` (fleet-level, its own domain in
   the manifest), or a `contacts` block inside `vehicles.json`? The 08-31 household precedent was
   *"one schema, one renderer, one reinline pipeline"* — which argues for staying inside.
2. **Do phone numbers stay in the public repo?** They are **businesses**, not individuals, and are
   already public — the GTI's six are committed and served today. So this is likely a non-issue for
   vendors. ⚠️ **It becomes a real question the moment a household contractor is an individual** —
   a sole-trader plumber's mobile is personal. See `PRODUCT-ENGINE.md` § the auth reframe.
3. **The Canton Express Oil rows — keep as `inherited`, or drop?** They are real service history for
   the truck, just not Paul's relationship.
4. **Is there a household contractor he can name today?** The **2026-04-23 roof inspection** (in the
   photo-organizer inbound) is the first household service event with no one attached to it.
