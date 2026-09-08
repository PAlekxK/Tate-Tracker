# Colour — the strategy, not another ruling

**Review date:** 2026-09-08 · **Reviewer:** ux-expert · **Mode:** review → scoped strategy
**Level:** zoom-out (system). Deliberately not screen-component — every one-off ruling you're tired of
*is* a screen-component decision, and that's the problem.

⛔ **Nothing was edited.** Trail only: this file and its JSON sibling.
⚠️ **This seat has no shell.** Every contrast ratio below is hand-computed by the same WCAG formula
`tools/palette.py:26-36` implements. Method validated against a number this repo already holds
(`viewer.template.html:5093` documents white on `#3a8a58` as 4.2:1; mine returns 4.24). **Treat every
ratio as a hypothesis until `palette.py` agrees.** Every *file* claim is `measured` by grep/read at
HEAD `a28e4fe`.

---

## The short version

**One sentence:** *an element's colour belongs to exactly one of four axes, the axis is **declared**
rather than inferred from the hex, and only one of the four may follow a household's choice.*

Everything you've been ruling one at a time is a disguised axis question:

| what you were asked | what you were actually being asked |
|---|---|
| "should the jump strip be mint?" | is the jump strip **identity** or **structure**? |
| "should a fresh house be green?" | is the ground **identity** or **structure**? |
| "should the tan derive?" | is **register** identity or structure? |

Answer the axis once and the individual rulings stop reaching you.

**And there is a live defect to fix before any of that** — see F1. It shipped today.

---

## What I found, worst first

### 🔴 F1 — the jump strip is 2.4:1 on any household that picks a colour. Shipped today.

`engine/viewer.template.html:4220`

```css
.jump-strip a { color: var(--tint-64, #2f5a3a); background: var(--tint-96, #f2f8ec); }
```

`--tint-64` is a **lightening** band — `mix(0.44)`, 44% toward white (`:6508`). Fernwood renders the
fallback `#2f5a3a` and is fine (~7.6:1). **Any seeded household renders the band:**

| seed | ink | ground | ratio | |
|---|---|---|---|---|
| `#2f5d3a` (what the instances declare today) | `#8BA491` | `#F3F5F3` | **2.43** | ⛔ |
| `#4A4640` (the neutral I recommend) | `#9A9794` | `#F4F4F4` | **2.64** | ⛔ |
| after the fix | `#4A4640` | `#F4F4F4` | **8.52** | ✅ |

AA for normal text is 4.5. **It isn't hue-specific — it's the mechanism.** And the rule's own comment
three lines below already knows why: *"The press ink is the DARKENED seed, not a tint band: every band
lightens, so none of the six could ever express it."* The resting ink has the identical problem and
wasn't caught.

Two things make this the top of the list rather than a footnote:

- The jump strip is **the one affordance the record shows working** — 5 offered, 5 tapped, in a window
  where every ask-shaped affordance scored **0 of 35**.
- **You ruled today that every domain card gets a jump-strip entry.** The surface is growing this lap.

**Fix:** `color: var(--accent-ink, #2f5a3a)` — the seed or a slight darkening of it, off the lightening
ladder. Byte-identical for Fernwood. **Do this now; it is not part of the lap.**

---

### 🔴 F2 — the tokenisation isn't a tokenisation. The tokens have ~150 definitions.

The brief said 79% tokenised, 42 literals left. The count was of `var()` **uses**. Here is the count of
**definitions**:

> **Zero.** `grep '--tint-(96|92|88|82|74|64)\s*:'` across the whole repo returns **no matches.**

The six bands are set **only** by six `setProperty` calls in the JS pre-paint block, which run only
when a valid accent exists. So today every band's effective value is its **inline fallback** — and the
fallbacks are not one colour:

| band | uses | distinct fallback hexes | spread |
|---|---|---|---|
| `--tint-92` | 69 | ~46 | `#e0ffe0` … `#dcf0e2` … `#ecf5d8` |
| `--tint-64` | 38 | ~26 | `#80c880` (bright green) … `#c9a878` (**a tan**) … `#2f5a3a` (**a dark green**) |
| all six | **235** | ~150 | |

Line `3313` maps **two different colours to the same band on the same line**.

**What that means, concretely.** For Fernwood: nothing — which is exactly why it passed every check.
For the first household that picks a colour: **all 69 tint-92 surfaces resolve to one value, all 38
tint-64 surfaces to another.** ~150 hand-tuned tones → 6. The layering that makes Fernwood read as a
card system with depth — chip vs inset vs panel vs band — **is carried entirely by the fallbacks.**
A household doesn't get a personalised page; it gets a flat one.

⭐ **The fact that makes this fixable in slices, and it's the most useful thing I learned today:**
because the fallback renders for the un-personalised reader, **removing a token and leaving its literal
is byte-identical for Fernwood, by construction.** De-tokenising is free and ungated. Tokenising is the
direction that needs a gate. That asymmetry is the whole shape of the migration below.

---

### 🟠 F3 — the ruled exclusion list was breached by the mechanism, not by a decision

The 2026-09-06 review named *"the warm machine/spec register"* as must-not-derive: *if the tan takes
the accent, journal and machine collapse into one skin and she loses the visual routing.*

`measured` — six uses are now on the identity ladder anyway:
`var(--tint-74, #d8cda0)` at `:4408 :4433 :4497` · `var(--tint-88, #ede1cc)` at `:4100 :4319` ·
`var(--tint-88, #e6ecd2)` at `:4320`. All creams and tans. Same at `.chorus-now-*`
(`:4010 :4011 :4030 :4031`) — the night inset, also on the list.

✅ **And the counter-evidence matters as much:** the *obvious* semantic exclusions **held**. Care
types, `.peak-state`, seismic severity, all five sync-pill states — still bare literals, correctly. So
the list was understood and applied, and **silently defeated on the non-obvious cases.**

**This is the diagnosis for the whole strategy.** A mechanism that assigns a token by **lightness**
cannot tell a tan from a green. It has no way to express an axis, so every exclusion has to be
re-enforced by a human on every edit — and that is what failed. Two days after a careful seat wrote
the list.

---

### 🟠 F4 — a household's page can never look as good as Fernwood's, by arithmetic

`mix(t)` is `c + (255-c)*t` per channel. Channel *differences* therefore scale by exactly `(1-t)`.
At the ground's `t=0.90`, **a seed's chroma is reduced to 10% of its spread.**

| | spreads (G−R, G−B) |
|---|---|
| seed `#2f5d3a` | 46, 35 |
| derived ground `#EAEFEB` | 5, 4 |
| **Fernwood's hand-tuned ground `#edf7e6`** | **10, 17** |

The 09-06 seat measured this once (*deriving Fernwood's own ground gives `#f0f4f1` — greyer, visibly
different*) and read it as a Fernwood quirk. **It's a property of the function.** Every household's
ground, forever, is flatter than Fernwood's regardless of which colour they pick.

**This does not need fixing now** — if grounds are only ever near-neutral paper, `mix()` is correct and
cheap, and your neutral-gray ruling is entirely consistent with it. It needs *recording*, so that
"why does Bob's house look washed out" has an answer that isn't a search.

---

### 🟠 F5 — the palette is checked; the ladder is not. That's why F1 shipped.

`palette.py --check` recomputes contrast for the seven **input** hexes and fails below AAA. **Nothing
anywhere checks a derived value.**

The proof this is the operative gap: on 09-06 a seat found `--hdr-3` at +28% gave Dusk **3.80:1** under
white masthead text. The fix landed — `:6490` now reads `mix(0.18)` with the reasoning inline. **Two
days later the identical class shipped one screen away at 2.43:1, on a more-used surface.**
*The finding was fixed. The class was not.*

`palette.py`'s own docstring: *"a palette is exactly the kind of list someone extends later with a
colour they liked. This refuses that."* The **ladder** is exactly the kind of thing someone extends
later with a band that looked about right, and nothing refuses it.

---

### 🟠 F6 — "what colour when nobody has chosen" now has **five** answers

| # | source | value |
|---|---|---|
| 1 | `engine/palette.json:6` | `"default": "stone"` → `#3F5266` |
| 2 | `instance/*.json` `identity.theme.main` | `#2f5d3a` (→ neutral, per your ruling) |
| 3 | `viewer.template.html:350-361` `:root` | Fernwood's greens |
| 4 | the four signed-in pages | `--accent: #2f5d3a` hardcoded |
| 5 | **the ~150 inline tint fallbacks** | the real default for 235 surfaces |

⚠️ **Your 09-08 ruling breaks (1) two ways.** In prose it becomes false. And in code: `palette.py:51-53`
**asserts the default is a member of `colors`** — so repointing `default` at a neutral that isn't a
swatch **fails the check**, and leaving it at `stone` leaves a lie in the engine's own declaration file.

**Recommendation:** split the double-booking. `palette.json` gains `"unchosen"` — *the colour of not
having chosen* — deliberately **not** a member of `colors`. `default` is deleted, or demoted to "the
swatch pre-selected in the picker." Everything else reads that one value.

---

### Smaller (detail in the JSON)

- **F7** — fallback literals that disagree with their token (`var(--green-primary, #3a7a3a)` where the
  token is `#2f5a3a`). Harmless today; it's the mechanism by which near-duplicates propagate.
- **F9** — 09-06's tranche 1 landed **partially** and nothing recorded which parts. The hdr-3 fix,
  green-primary derivation, ground and bands all landed. *"The derivation runs in CSS, not JavaScript"*
  did not — it's now **eighteen** `setProperty` calls, up from the three that review flagged as too
  many. The stylesheet has stopped describing the page.
- **F10** — the neutral will read as *unfinished* unless the product says *unchosen*. Good news: the
  copy branch already exists (`settings/place:188`, on `fw-accent-chosen`), and the swatch row already
  rings nothing when the accent isn't a palette member. That degradation is honest. Don't break it.

---

## 1 · The strategy — four axes and where the seam is

| axis | answers | who owns it | may a household change it | what's on it |
|---|---|---|---|---|
| **Identity** | *whose* | household picks the input, **engine owns the derivation** | ✅ **the only axis that follows a seed** | masthead, affirmative fill + press + ring, accent ink (links, chip labels, jump strip), active/current markers, feedback bubble |
| **Semantic** | *what* | **engine, absolutely** | ⛔ never | care types, `.peak-state`, seismic severity, the five sync states, `.pmap-sync`, `.feedback-status`, `.rv-badge` provenance |
| **Structural** | *where am I* | **engine** | tint, **not restructure** | ink, paper/ground/wash, hairlines, the chip→inset→panel→band tonal ladder, outlined-secondary edge, **and the two registers** (journal-green vs machine-cream vs night inset) |
| **State** | *what did I just do* | engine owns the **rule**; the element's axis owns the **value** | transitively | hover, press, focus, disabled, selected |

**Three things this table settles that were previously rulings:**

1. **Semantic's falsifier, unchanged from 09-06:** *if a reader who picked Lake could no longer tell
   "ahead" from her own colour, it should never have derived.* The sync states carry the hardest
   version — under the site's physical premise, amber and red mean *your words may not have left this
   device*. A household accent painting those would make **capture lie**.
2. ⭐ **Structural is the axis the system does not have, and its absence is F2, F3 and F4.** The tint
   bands are *structural* tokens wired to the *identity* input. That single mis-wiring produces all
   three findings. A structural scale needs its **own** declared neutral ladder with its **own** step
   count; the seed may bias it a little and may not flatten it.
3. **A state is never hand-picked.** Press = a fixed darkening of the element's own resting colour.
   72% is the ratio that reproduces Fernwood's shipped `#2f5a3a → #1f4528` within 4 RGB units — which
   means `onboarding/index.html:79`'s **84%** is a second derivation of one idea, on the screen a new
   reader sees immediately before the app.

---

## 2 · The neutral a fresh household wears

### Recommendation: `#4A4640` — a near-neutral graphite with a hair of warmth

Declared **once**, in `engine/palette.json` as `"unchosen"`, **not** a member of `colors`. Instance
files, the four signed-in pages and the viewer `:root` read it; nothing re-types it.

| check (hand-computed) | value | |
|---|---|---|
| white on the fill | **9.37** | ✅ AAA (bar 7.0) |
| as ink on `#fbfcfd` | **9.12** | ✅ AAA |
| masthead light stop `mix(0.18)` = `#6B6762`, white text | **5.61** | ✅ beats every palette member (Dusk 4.83, Fern 5.86) |
| jump strip after the F1 fix | **8.52** | ✅ (before: 2.64 ⛔) |
| ground `mix(0.90)` | `#EDEDEC` | paper |
| wash-1 / wash-2 / edge-card | `#F2F2F2` / `#E8E7E6` / `#DEDEDD` | monotonic ✅ |

**Why warm, and not a true neutral — two reasons, one aesthetic and one discriminative:**

1. The register is a field journal on paper. A true `#4A4A4A` reads as *unstyled*, and your standing
   note is *"I don't wanna be flat or boring or dry."* A hair of warmth reads as **chosen restraint**
   rather than absence.
2. ⚠️ **A cool neutral is a desaturated Stone** (`#3F5266`) — which is `palette.json`'s current default
   and the swatch a reader is most likely to try first. Picking Stone would barely look like anything
   happened. Warm-neutral keeps all seven swatches a **visible** change.

**The honest cost, stated so it isn't discovered later:** per F4, chroma scales by `(1−t)`, so at the
ground's 90% the warmth survives as ~1 RGB unit. `#EDEDEC` is neutral paper, not warm paper. If you
want visible warmth in the ground, that's a change to the **derivation**, not to the seed.

**Alternatives if you want them:** `#4A4A4A` true neutral (cost: reads unstyled) · `#454B52` cool
(cost: the Stone collision above) · `#4A423A` warmer (cost: at that spread it starts making a hue
claim, which is what "neutral until told" is refusing to do).

⭐ **Don't name it, and don't put it on the swatch row.** It is the *absence* of a choice, not a choice
— naming it invites it back as an eighth colour. In code, `unchosen`. VOCABULARY §4's own logic:
*the thing nobody picked is called nothing to a user.* And note its real job is small: the neutral only
ever paints someone who **skipped** the choice — `fw-accent-chosen` already distinguishes the two.

---

## 3 · The evolution path — each step ships alone, none is a repaint

The ordering is driven by F2's asymmetry: **de-tokenising is free; tokenising needs a gate.**

| step | what | moves Mom | size | gate |
|---|---|---|---|---|
| **S0 · stop the bleeding** — *this week, not the lap* | F1's jump strip + F3's six warm-register uses **off** the ladder (`var(--tint-N, X)` → `X`) | **no — byte-identical by construction** | <1 hr | none; it's a defect fix |
| **S1 · one answer to "unchosen"** | F6: `palette.json` gains `unchosen`; `default` deleted or demoted; palette.py checks it without requiring membership; five sources collapse to one | no | ½ day | **your hex** |
| **S2 · THE AXIS REGISTER** ⭐ | `engine/color-axes.json` — every colour-bearing declaration classified *identity · semantic · structural · state*, with a reason for anything non-obvious. F7 fixed in the same pass. **Nothing renders differently — it's a JSON file.** | no | 2 days incl. your rulings | **~20 arguable cases, one table, one sitting** |
| **S3 · THE CHECK** | `tools/check-color-axes.py` + the ladder assertions folded into `palette.py`. Wired **into pages-deploy**, refusing the deploy — the way `check-estate-neutral` is wired — not merely named in the pickup block | no | 1 day | none |
| **S4 · structural earns its own ladder** — GATED | F2's real fix. `structural` uses get a declared neutral tonal scale with its own step count; `identity` uses collapse onto the accent ladder, correctly. Both in `:root` per F9, so the JS sets exactly **one** property | **possibly — release cascade runs here** | 2–3 days | you + cascade (Mom is gate 3, never gate 1) |
| **S5 · chroma-preserving derivation** — not scheduled | F4. OKLCH or a chroma floor. **Only if real households say the flatness matters** | yes | ? | evidence first |

**The lap is S1 → S3. S0 is now. S4 is the lap after** (or the tail of this one if it runs short).

---

## 4 · How it's managed — the enforcement gap, and what closes it

`measured`: **no check in this repo can see a colour leak.**

- `check-estate-neutral.py` — 11 place-name needles + species from canon. No colour concept, and per
  its own `_shipped_pages()` at `:61` it doesn't scan `viewer.html` in its bare form.
- `build-viewer.py --check` — **bytes.** Doesn't parse JS, per CLAUDE.md's own warning.
- `palette.py` — seven **input** hexes (F5).

So the mint band, F1, F3 and F2's flattening are **all** invisible to every green check in the pickup
block.

⭐ **And the same gap is already named one row over.** BACKLOG TIER 2 · 15, on the model prompts:
*"the check is missing too — check-estate-neutral reads shipped PAGES; nothing reads the model's
prompt. A row that ships without extending that check ships without a falsifier anyone can run."*
Colour is the **third substrate of one defect** — names → prompts → colour — and it's the one with no
instrument at all.

### ⛔ Do not build a needle-list colour check

A list of Fernwood's greens has the exact defect the name check has: **it can only find colours
somebody already knew about**, and the mint band was in that category. Build it **structurally**:

> Every colour-bearing declaration in `engine/viewer.template.html` must appear in
> `engine/color-axes.json` with a declared axis. **An unregistered hex literal, or an unregistered
> `var(--*)` colour use, is RED.**

Exhaustive by construction. **What would have caught the mint band:** a household-reachable rule whose
colour is registered `structural` while nothing declares the structural scale — red on the commit that
wrote it, not on Paul's second sighting on his own condo.

**Pre-registered falsifiers** (a check nobody can break is decoration):

1. mutate one rule to a new bare hex → **RED**
2. mutate a semantic literal onto a tint band → **RED**
3. recreate today's jump-strip rule → **RED on contrast**
4. recreate the mint band → **RED**
5. ⭐ **green across two laps AND no colour ruling needed in that window → it measures nothing, delete it**

---

## 5 · The backlog item — draft, yours to file

> ### 🎨 COLOUR HAS FOUR AXES AND THE ENGINE ONLY KNOWS ONE — the axis register, its check, and the neutral a fresh household wears
>
> **Tier:** TIER 2 (engine · must-not-diverge), filed beside rows **14** and **15** — same defect on a
> third substrate: *an instance default shipped as the engine's*. Tier placement is yours to confirm.
>
> **The question it answers:** what does a colour MEAN on each surface, which of those meanings may
> follow a household's choice, and what refuses the next wrong answer **without a ruling**.
>
> **Why now:** `measured` 2026-09-08 — the mechanism that fixed the mint band shipped a **WCAG failure
> on the most-used affordance in the app the same day** (2.43:1), swept the ruled warm-register
> exclusion onto the identity ladder, and **collapses ~150 hand-tuned tones to 6** for any household
> that picks a colour. None of the three is visible to any check in the pickup block. And you ruled
> today that every domain card gets a jump-strip entry — the failing surface is growing this lap.
>
> **Falsifier:** ⭐ a build seeded with a **non-Fernwood** accent, walked at **414 × 848 × A+**, in
> which — (a) every text/background pair clears AA, **checked by tool, not by eye**; (b) no semantic
> colour has moved (care types, `.peak-state`, seismic, all five sync states byte-identical to the
> Fernwood build); (c) journal and machine registers are still visually distinct; (d) card/chip/inset/
> panel tonal separation is still legible — **not one flat colour**. AND, same commit,
> `check-color-axes.py` goes **RED** when any of the four is deliberately mutated.
> ⛔ *Green is impossible today on (a), (c) and (d). Green is the definition of done.*
>
> **Size:** S0 <1hr (**not part of the lap — do it now**) · S1 ½d · S2 2d · S3 1d · S4 2–3d behind the
> cascade. **Lap = S1→S3.**
>
> **Depends on / collides with:**
> - ⛔ **Blocks on you for exactly two things:** the neutral hex, and ~20 arguable axis classifications
>   (one table, one sitting). Everything else is agent-buildable.
> - ⚠️ **Collides with row 19c** — the person-vs-place precedence (`fw-accent` live vs
>   `identity.theme.main` now read). **This item does not settle it and must not appear to.** 19c's own
>   warning stands: *do not build two colour pickers before answering it.*
> - **Shares a shape with rows 14 and 15.** If a general *what is instance / what is engine* check is
>   ever built, these three are its three substrates.
> - **Touches TIER 2 · 10 (the glance consolidation)** — the strip's treatment is in scope for both.
>   **Do the axis classification first** so the strip rebuild inherits a rule instead of minting one.
> - **Not blocked by** zones, weather, or the per-estate canon store. Nothing here needs the store.
>
> **Ask · check · attribution:** no ask to Mom (nothing reaches her before S4, and S4 goes through the
> cascade). **No telemetry event** — an event with no reader isn't instrumentation, so this ships with
> a **check** instead, readers named: pages-deploy refuses on a hit; the pickup block reads it. No
> ribbon line (nothing here traces to her feedback). Release note at S4 only, and only if Fernwood's
> tonal system visibly changes — which it shouldn't.

---

## Surfaces the brief missed

1. ⭐ **The inline fallback literals themselves.** The brief named the tint bands but treated
   tokenisation as ~79% done. **The six bands have zero CSS declarations.** The 235 fallbacks *are* the
   design system today; the token names are a promise about a future one. Largest colour surface in the
   repo, and it has no file.
2. ⭐ **The eighteen derived values** — `hdr-1/2/3`, `accent-press`, `ground`, `wash-1/2/3`, `edge-card`
   and the six bands, computed in JS at `:6483-6508` and declared nowhere. Unreadable from the
   stylesheet, uncheckable by `palette.py`.
3. **`.chorus-now-*`** (`:4010-4031`) and the **cream/tan machine register** (`:4100 :4319 :4320 :4408
   :4433 :4497`) — both on the 09-06 exclusion list, both now on the identity ladder.
4. **`palette.json.default` × `palette.py:51-53`** — a hard breakage path for your neutral ruling, not
   just prose drift.
5. **The five-way disagreement on "unchosen"** — the brief named three.
6. **`onboarding/index.html:79`'s 84% press vs the app's 72%** — one idea, two derivations, on the two
   screens a new reader sees back to back.

---

## Open questions — yours

1. **The neutral hex.** `#4A4640` recommended; three alternatives with their costs above.
2. **Does `palette.json.default` survive, and meaning what?** It will be false the moment your instance
   edits land, and it breaks `palette.py` if repointed.
3. **The ~20 arguable axis classifications.** I'll bring one table. The ones I expect you'll want
   personally: the night inset · the cream machine register · the tab underlines · the focus ring · and
   whether `--edge-secondary` stays neutral (still open from 09-06 — my recommendation is still
   *neutral*; the de-warming numbers are in that file).
4. **S4 changes Fernwood's tonal system if done wrong, and possibly a little even if done right.** Is a
   small, deliberate, cascade-gated change to Mom's tonal separation acceptable in exchange for
   households getting one at all — or is *"Fernwood does not move, full stop"* the constraint?
5. ⚠️ **Row 19c's precedence question is still unruled** and sits upstream of a settings colour picker.
   Not mine; flagged because two steps here touch surfaces that change depending on how you rule it.

---

## Before acting on F1 and F2

⭐ **Walk a seeded build first.** My claims come from reading the pre-paint block, not from a rendered
page — and this repo's most-repeated failure is measuring a proxy and reporting the target. A local
build with `fw-accent` set to any non-green hex, at 414 × 848 × A+, screenshotted, settles both in ten
minutes. Then re-run `python3 tools/palette.py`; every ratio here is hand-computed.

**No user research needed.** This is an engine question, and neither Mom nor Bob has an opinion about
it they could give us.

---

## Principles this review proposes (proposals — your wording, not mine, if they land)

1. **Colour answers one of four questions — *whose · what · where · what-just-happened* — and an
   element may only be on one axis. The axis is DECLARED, never inferred from the colour's value.**
   *Scope: cross-project.* Second occurrence of 09-06's *"a scheme is a monotonic ladder; a semantic
   colour is not on the ladder"* — and the first evidence of why that rule was **insufficient**. It drew
   the line correctly and left a human to enforce it per-edit. Two days later enforcement failed in the
   direction the rule couldn't see: a mechanism that assigns tokens by **lightness** can't tell a tan
   from a green, so a ruled exclusion was swept onto the ladder by a change nobody intended as a colour
   decision. *Falsifier: if a rule's axis can be recovered from its hex, the register is redundant.*

2. **A token with more than one definition is a comment, not a token.**
   *Scope: cross-project.* Six names, 235 uses, ~150 distinct fallbacks, zero declarations. It looked
   79% tokenised by every count anyone ran, **because the count was of uses and not of definitions.**
   The tell is the fallback list: if two uses of one token carry different fallbacks, the token doesn't
   exist yet. *Falsifier: a token whose uses all carry the identical fallback is genuinely a token, and
   this says nothing about it.*

3. **Personalisation is additive over a working default — so REMOVING a wrong token is always free,
   while adding one always needs a gate.**
   *Scope: cross-project.* Sharpens 09-06's *"a personalisation token must default to the literal it
   replaces"* with the operational corollary that makes a large refactor shippable in slices. That
   asymmetry is what lets S0 ship this week and S4 wait for the cascade, and it's the single most useful
   thing I learned here. *Falsifier: if a de-tokenisation ever changes the default reader's page, the
   token wasn't defaulting to the literal it replaced and the 09-06 rule was already violated.*
