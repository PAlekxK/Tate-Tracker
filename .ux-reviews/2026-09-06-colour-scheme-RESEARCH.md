# Colour SCHEMES — research foundation for Fernwood's chosen colour

**Mode:** principles / research · **Date:** 2026-09-06 · **Seat:** ux-expert (research seat)
**Scope:** what a colour scheme IS in current practice, which roles derive from a seed and which must not,
accessibility incl. a monochrome scheme, and a recommended model for Fernwood.

⚠️ **This is the FOUNDATION, not the inventory.** A sibling seat is writing
`.ux-reviews/2026-09-06-colour-scheme.md` (inventory of today's hardcoded greens + a first derivation for
tonight). That file should be **re-based on this one**, not merged with it. Nothing here edits a page.

**Tags on every claim:** `sourced` (a cited primary doc says it) · `inferred` (my derivation from code or
from a cited fact) · `proposed` (my recommendation, nobody has ratified it).

---

## 0. What is on the ground today (read, not researched)

| thing | value | tier |
|---|---|---|
| seed | one of 7 hexes, `fw-accent` in localStorage (`engine/palette.json`) | engine set, instance choice |
| masthead | `--hdr-1/2/3` = `mix(-0.45)` / seed / `mix(+0.28)`, naive sRGB lerp (`viewer.template.html:6395–6402`) | derived |
| affirmative | `--green-primary` = seed, `--green-press` = `mix(-0.22)` (added tonight, `:6408–6409`) | derived |
| onboarding | `--accent` seed, `--accent-on` / `--accent-ring` via `color-mix(in srgb …)` (`onboarding/index.html:69–81`) | derived |
| ground | `#e6f0db` + a 3-stop green wash + SVG noise, `background-attachment: fixed` (`:326–333`) | **hardcoded** |
| card | white, green hairline | **hardcoded** |
| outlined-button edge | `--edge-secondary #8a7a4a` — a gold that belongs to no seed | **hardcoded** |
| semantics | plant-care types, status pills (synced/local/error) | **hardcoded** |
| the check | `tools/palette.py --check` — seed vs white text, seed vs ground as ink, bar = AAA 7.0 | seed only |

⭐ The one affirmative grammar (CLAUDE.md standing rule §1): **filled + ✓ = affirmative, outlined + × =
negative.** Any scheme model must keep that grammar legible for *every* preset, or it is not a scheme —
it is a paint job with seven finishes.

---

## 1. What a colour scheme IS in current practice

Five systems, examined for their **shape**, not their palettes. They disagree on almost everything except
the shape, and the shape is the finding.

| system | the unit | the pipeline | distinctive contribution |
|---|---|---|---|
| **Material 3** | seed → HCT tonal palettes → roles | 1 source colour → 5 key colours → 13 tones each (0,10,20,30,40,50,60,70,80,90,95,99,100) → named roles | tone-as-contrast: **"a contrast ratio of 3:1 or higher if they are 40 or more apart… 4.5:1 or higher if they are 50 or more apart"** `sourced` |
| **USWDS** | family + **grade** | token = `family-grade`, grade 0 = white … 100 = black | the same idea, stated as "magic numbers": grade diff **40 → AA Large, 50 → AA, 70 → AAA** `sourced` |
| **Radix Colors** | one hue → **12 steps**, each with a fixed job | steps are roles, not shades | the most explicit role-per-step contract in the industry (table below) `sourced` |
| **shadcn / Tailwind** | **background/foreground pairs** | `primary` + `primary-foreground`, etc. | *"The base token controls the surface color and the `-foreground` token controls the text and icon color that sits on that surface."* `sourced` |
| **Apple HIG** | one **tint/accent** + **semantic** system colours | the OS supplies the tonal work | the app owns one accent; everything else is the platform's, and adapts to the user's accessibility settings `sourced` (page is JS-rendered; guidance summarised, see §3) |

**Radix's 12 steps, verbatim uses** `sourced`:

| step | job | step | job |
|---|---|---|---|
| 1 | app background | 7 | UI element border & focus rings |
| 2 | subtle background | 8 | hovered UI element border |
| 3 | UI element background (normal) | 9 | **solid backgrounds** — "highest chroma of all steps" |
| 4 | hovered UI element background | 10 | hovered solid background |
| 5 | active / selected UI element background | 11 | low-contrast text |
| 6 | subtle borders & separators (non-interactive) | 12 | high-contrast text |

### ⭐ The shared shape, in one line

> **seed → a tonal scale (one hue, many lightnesses) → a small set of NAMED ROLE TOKENS, where a role is
> defined by its JOB and filled by its TONE.** `sourced` (all five)

Three consequences every one of them holds, and Fernwood currently holds none of cleanly:

1. **A role is a job, not a colour.** "Primary" is not a green; it is *the fill of the one main action*.
   M3 assigns it a tone (tone 40 of the primary palette in the light scheme, on-primary tone 100)
   `sourced`, Radix assigns it step 9, shadcn assigns it `primary` + `primary-foreground`.
2. **Contrast is guaranteed by the TONE GAP, not by inspecting each pair.** M3's 40/50 rule and USWDS's
   magic numbers are the same claim, arrived at independently: if you fix the lightness targets, contrast
   holds *for every hue you ever seed with* `sourced`. This is the single most useful idea for Fernwood.
3. **Foregrounds travel with their backgrounds.** Never a lone fill; always the pair `sourced` (shadcn,
   M3's `on-*`, Carbon's `text-on-color`).

⚠️ **What none of them do:** encode role in shape, or let the seed touch semantic colours. Both matter here
(§2). And Fernwood already learned the first one — the 2026-08-02 v2 button system, which the template's
own comment records as confirmed by an earlier research pass.

---

## 2. What is a highlight and what is not — roles, and which ones derive

**The rule the systems converge on** `sourced`: the seed owns **identity and emphasis**; it never owns
**meaning**. M3 keeps `error` out of the seed-derived key colours; shadcn gives `destructive` its own
token outside the primary family; Carbon separates `support-error/success/warning/info` from `interactive`.

**Why it is load-bearing here, not theoretical** `inferred`: Fernwood's seven seeds include **Clay
(#7A3E2A, a red-brown)** and **Dusk (#6B4676, a purple)**. Tonight's change makes the seed the fill of the
**affirmative ✓ control**. On a Clay estate, the "yes, that's right" button becomes a red-brown filled
control sitting on a card that may also carry a red error pill. The ✓ glyph is what rescues it — which is
precisely why standing rule §1's *fill + glyph* grammar, not fill alone, is the ratified part. **A scheme
that recolours the affirmative fill makes the glyph load-bearing rather than reinforcing.** That is a
real trade, and it is Paul's to make, not a check's (Q1).

### The role table — derive vs fixed `proposed`

| role token | job | seed? | why |
|---|---|---|---|
| `--brand-deep` / `--brand` / `--brand-lit` | masthead gradient, 3 stops | **derive** | pure identity; carries no meaning `sourced` (Apple: one tint) |
| `--accent` | the ONE filled affirmative / main action | **derive, tone-clamped** | emphasis. Clamp so every seed lands in one tone band |
| `--accent-press` | its pressed state | **derive** | must move with its parent or one value in ≠ one value out |
| `--on-accent` | label/glyph on `--accent` | **derive (white or ink, by tone)** | the pairing rule `sourced` (shadcn) |
| `--accent-ring` | focus ring | **derive** | identity + must clear 3:1 (1.4.11) `sourced` |
| `--edge-secondary` | outlined-button border | **derive at a FIXED tone** | today a gold owned by no seed; hue should follow, tone must not |
| `--ground-a` / `--ground-b` | page wash | **derive, chroma-clamped** | see §4; the biggest open question |
| `--surface` | card fill | **fixed white** | the constant the whole tone system is measured against |
| `--edge-hair` | card hairline | **derive, chroma-clamped** | decorative, must clear 3:1 only if it is the sole boundary `sourced` (1.4.11) |
| `--ink` / `--ink-soft` | body / secondary prose | **fixed near-neutral** | 162 text colours is already the recorded defect (fernwood.md, 08-24) |
| `--error` `--warn` `--ok` `--info` | status pills, sync state | ⛔ **FIXED** | meaning, not identity `sourced` (M3/shadcn/Carbon all exclude these) |
| plant-care type colours | categorical taxonomy | ⛔ **FIXED** | a category set must stay stable across estates or the vocabulary moves per household |

**Ten derived + four fixed semantic + two fixed neutral ≈ 16 tokens.** That is the right order of
magnitude: Radix ships 12 steps per hue, shadcn ~14 named pairs `sourced`.

### ⚠️ A measured gap in today's derivation

`palette.py --check` scores **the seed** — vs white text, vs the ground as ink, at AAA. It does not score
**the tokens the seed produces**, which is where the reader's contrast actually lives. Arithmetic from the
shipped `mix()` and the shipped hexes `inferred` **(computed by hand, not executed — re-run before acting)**:

| seed | `--hdr-3` = mix(+0.28) | white text on it |
|---|---|---|
| Dusk #6B4676 | #947A9C | **3.80 : 1** |
| Stone #3F5266 | #758291 | **3.92 : 1** |
| Clay #7A3E2A | #9F7466 | **4.07 : 1** |
| Fern #2C4A2C | #677D67 | **4.54 : 1** |

Two findings, one cause. **(a)** White normal-size text over the lightest gradient stop fails AA 4.5:1 on
at least three of seven seeds — the `.hh-utility a` links are 14px at .92 opacity, which is normal text
under 1.4.3 `sourced`. The `h1` is large text and clears 3:1. **(b)** The spread — 3.80 → 4.54, ~19% — is
the signature of a **fixed-ratio sRGB lerp**: the same `+0.28` produces a different perceived lightness
per hue. A tone-target derivation removes both by construction. This is the same class of bug the
onboarding file already records against itself at `:70–77` (`--accent-on` hardcoded while `--accent` moved).

---

## 3. Accessibility

### Contrast — the two standards, and where they part

| | WCAG 2.2 (normative today) | APCA (candidate for WCAG 3) |
|---|---|---|
| unit | contrast **ratio** | **Lc**, lightness contrast, 0–105+ |
| text | **4.5:1** normal, **3:1** large (≥18pt / 14pt bold) — SC 1.4.3 AA `sourced` | Lc 90 preferred body, Lc 75 min body, Lc 60 non-body `sourced` |
| UI / non-text | **3:1** for controls, states, boundaries, meaningful graphics — SC 1.4.11 AA `sourced` | Lc 15 absolute floor non-text `sourced` |
| accounts for font size/weight | no | **yes** `sourced` |
| dark polarity | criticised: *"far overstates contrast for dark colors to the point that 4.5:1 can be functionally unreadable"* `sourced` | designed for it |

**Where they diverge, for Fernwood specifically** `inferred`: Fernwood is a **light-polarity** app with
**dark seeds on white/near-white**. That is the region where WCAG 2 and APCA agree best; the divergence
bites in dark mode and on near-black, which Fernwood does not ship. **Recommendation: stay on WCAG 2.2
ratios as the gate** (the existing `palette.py` AAA bar is already stricter than required), and treat APCA
as a **tie-breaker for secondary prose at A+**, where the ratio-only rule under-serves. `proposed`

⛔ **Do not use the large-text 3:1 exception when the reader turns on A+.** The A+ toggle is a *statement
about the reader's vision*, not a licence to spend the contrast the larger type just earned. `proposed`

### Never colour alone

SC 1.4.1 Use of Color (Level **A**, the strictest conformance tier): *"Color is not used as the only
visual means of conveying information, indicating an action, prompting a response, or distinguishing a
visual element."* `sourced` Colour-vision deficiency: **1 in 12 men (8%), 1 in 200 women**, ~300M
worldwide; red/green most common, and the common myth is that it is *only* red/green — *"people with it
can easily confuse any colours which have some red or green as part of the whole colour"* `sourced`.

Fernwood already complies where it matters most: **✓ / ×** on the affirmative grammar. The exposure is the
**plant-care type colours and the status pills** `inferred` — if a pill's only difference from its
neighbour is hue, that is a 1.4.1 failure regardless of any scheme.

### The older reader — what a generic system does not say

W3C WAI's literature review `sourced`: *"an 80 year old typically has 80% less contrast sensitivity than a
20 year old"*; lens yellowing means *"less violet light is registered, making it easier to see reds and
yellows than blues and greens, and often making dark blue and black indistinguishable."*
NN/g `sourced`: interface text on mobile was *"often too small and lightly colored for older adults to
read comfortably"*; usability declines ~0.8%/year between 25 and 60.

⭐ **Three consequences the design systems will not tell you** `inferred` / `proposed`:
1. **Dark blue vs black is a documented confusion for this reader.** Fernwood's default seed is **Stone
   #3F5266, a dark slate-blue**, and Lake #2C5674 is close behind. Against near-black `--ink`, a
   *derived* dark stop (`mix(-0.45)`: Stone → ~#222D38) may be indistinguishable from body text for her.
   Falsifier: put Stone's `--hdr-1` beside `--ink` at 414px and A+ and ask her if they are the same colour.
2. **Warm hues are the easier end.** Clay, Fern and Pine sit better with a yellowed lens than Dusk or
   Lake. That is an argument for offering warm seeds, **not** for removing cool ones — but it is an
   argument for the *default* being warm-ish or neutral rather than blue.
3. **The 08-24 finding compounds it.** `rgb(44,74,44)` (30 uses) and `rgb(42,74,42)` (20 uses) differ by
   two units on one channel (fernwood.md). For a reader with 80% less contrast sensitivity, *any* pair
   under ~5 units is one colour. The tokenisation is an accessibility fix, not a tidiness fix.

### System-level contrast preferences — respond, don't reinvent

| mechanism | what it is | what Fernwood should do |
|---|---|---|
| `prefers-contrast: more / less / custom` | fires from macOS *Increase Contrast*, Windows high contrast; **Baseline widely available since May 2022** `sourced` | **respond**: raise `--ink-soft` to `--ink`, thicken `--edge-hair`, drop the noise texture `proposed` |
| `forced-colors: active` | Windows High Contrast; overrides colour **at paint time**, forces `box-shadow`/`text-shadow`/`background-image` to `none`, supplies `Canvas`/`CanvasText`/`ButtonText`/`ButtonFace`/`Highlight`; Baseline since Sept 2022 `sourced` | **small targeted tweaks only.** MDN: *"Don't create separate designs for forced colors mode users"* and don't use `forced-color-adjust: none` broadly `sourced`. ⚠️ Fernwood's filled-green affirmative loses its fill here — the **✓ glyph is the only surviving signal**, which is a second argument for the glyph grammar `inferred` |
| `prefers-color-scheme` | dark mode | **out of scope tonight.** A dark scheme is a second tonal mapping, not a preset; it doubles the derivation surface `proposed` |
| `@media (monochrome)` | monochrome output device / print; Baseline since Jan 2020 `sourced` | useful for **print**, useless as the door to a Plain preset — the reader's phone is not monochrome |

⭐ **The reader will not find the OS setting.** iOS *Increase Contrast* is three levels deep in Settings →
Accessibility → Display & Text Size. Responding to `prefers-contrast` is necessary and **not sufficient**:
Fernwood needs an in-app door too, which is what the presets in §4 are for. `proposed`

### A monochrome scheme — how systems actually offer one

- **Apple:** *Increase Contrast* and *Differentiate Without Color* — the OS restyles; apps respond `sourced`
  (HIG page is JS-rendered; corroborated by `prefers-contrast` mapping on MDN `sourced`).
- **Android:** *High-contrast text* forces text black or white with an outline; **"other user interface
  elements such as toggles, icons and buttons are not affected"** and the feature is *"still
  experimental"* `sourced`. So on Android an app cannot rely on the OS to fix its own controls.
- **GOV.UK:** no monochrome preset at all — it holds one palette, mandates WCAG 2.2 1.4.3 AA, and reserves
  the yellow `#ffdd00` focus colour for exactly one job: *"Only use this colour to indicate which element
  is focused on"* `sourced`. The lesson is the reservation, not the absence.

⭐⭐ **The finding worth the whole section** `proposed`: **a monochrome scheme is not a special case — it is
a seed with chroma zero.** If the derivation is tone-based, "Plain" needs no branch, no second stylesheet
and no exception list. It falls out of the same pipeline. And it is self-checking: **any signal that
disappears in Plain was carried by colour alone** — a permanent, runnable audit of SC 1.4.1 that costs one
extra swatch. If Plain requires special-casing, the derivation is wrong; that is the falsifier for the
whole model.

---

## 4. Recommendation for Fernwood

### The model, in the shape §1 found `proposed`

```
ONE SEED (hex)
  → normalise to a hue + a chroma, discard its lightness
  → a 6-stop TONE SCALE at fixed lightness targets:  96 · 88 · 62 · 40 · 28 · 16
  → ~16 ROLE TOKENS, each pinned to a stop (table in §2), foregrounds paired with backgrounds
```

**Six stops, not thirteen.** M3 ships 13 tones because it serves containers, elevation and dark mode
`sourced`; Fernwood ships a light-only app with one filled control. Six covers ground · hairline · edge ·
accent · press · deep, and 4 of the 6 are ≥40 apart from `--surface`, so contrast is structural `inferred`.

**Derivation rules** `proposed`:
1. **Target the tone, never a mix ratio.** Replace `mix(±t)` with "produce the seed's hue at lightness L".
   `color-mix(in oklab …)` or an explicit OKLCH lightness is the cheap version; the fallback-hex pattern
   already in `onboarding/index.html:75–77` is the right shape to copy for Safari <16.2.
2. **Clamp chroma per role.** Ground and hairline get chroma ≤ ~15% of the seed's; accent keeps full
   chroma; ink keeps none. This is Radix's step-1/2 vs step-9 split, restated `sourced`.
3. **Foreground follows tone, not taste.** `--on-accent` = white above the accent's tone threshold, ink
   below. One rule, seven seeds, no per-seed judgment.
4. **Semantics never take the seed** (§2 table).
5. **Extend the check to the DERIVED tokens.** `palette.py --check` scores the seed today; the contract
   lives on `--hdr-3`, `--accent-press`, `--accent-ring`, `--edge-secondary`, `--on-accent`. **Every
   derived token × every preset, or the check is measuring the wrong object.**
   *Falsifier for the whole model: run it. If any preset needs a hand-tuned exception, the model is wrong.*

### The preset list `proposed`

| preset | seed | notes |
|---|---|---|
| Stone · Pine · Lake · Clay · Dusk · Spruce · Fern | the seven hexes, unchanged | ⚠️ the palette's own `_known_trade` (three greens, widened band) is **untouched by this** — a tone-based scale narrows the *derived* spread, not the *chip-selection* discrimination task |
| **Plain** | chroma 0, warm-neutral hue | the monochrome preset. Ships as a swatch, works as the 1.4.1 audit |
| **Strong** | any seed + a raised contrast target (ink for secondary prose, thicker edges, no noise) | the in-app door to what `prefers-contrast: more` gives OS-side |
| *(automatic)* | `prefers-contrast: more` → Strong's rules; `forced-colors: active` → targeted tweaks only | never a separate design `sourced` |

⚠️ **Strong is a MODIFIER, not a ninth colour.** Presented as a ninth swatch it forces a false either/or —
"my place's colour" vs "I can read it." Presented as a toggle beside the seven, it composes. `proposed`

### The green ground — the one I would put to Paul rather than decide

**Recommendation: derive a chroma-clamped tint from the seed, and hold the ground↔card lightness step
constant at today's value.** `proposed`

The argument is already written down in this repo, in the onboarding file's own comment (`:50–58`): the
page was deliberately made *not* green because *"green is FERNWOOD'S identity… she is not arriving at
Fernwood — she is starting a place of her own."* **That reasoning does not stop at the onboarding
boundary.** A Clay household that finishes setup and lands on a green ground has been told its colour was
decorative. The ground is the largest single surface in the app; leaving it fixed green makes the seed a
trim colour, which is the "single main colour" outcome Paul asked to move past.

**Falsifiers, all cheap:**
- If a chroma-clamped tint at ground tone is indistinguishable from white for the older reader, the ground
  is doing no work and should go neutral instead. *Test: Mom, 414px, A+, on her own phone.*
- If white cards stop separating from the ground (the step drops below what she can see), the ground moves
  or the card gets a stronger hairline — the step is the constraint, not the hue.
- If the noise texture reads as dirt on a warm tint (Clay) where it reads as moss on a green, the texture
  is instance-tier and must not travel with the engine.

### What the 414px / A+ reader needs that no design system says `proposed`

1. **A 3-stop gradient across 414px is identity, not information.** It is ~2px of transition per unit of
   perceived change. Keep it — it is the "this is mine" signal — but **do not let the gradient's lightest
   stop carry normal-size text.** See §2's measured 3.80–4.54 spread.
2. **A+ should promote contrast, not just size.** `body.text-lg` raising `--ink-soft` to `--ink` costs one
   rule and directly answers NN/g's *"too small and lightly colored"* `sourced`.
   *Falsifier: if A+ turns out to be used by people who simply prefer big type (Paul on a laptop),
   coupling contrast to size is wrong — check the telemetry split before shipping it.*
3. **Chip selection at 414px is a colour-discrimination task with no labels to lean on.** The palette
   already carries this as a `_known_trade`. A tone-based scale does **not** fix it; only naming and
   spacing the chips does. Do not let this work be read as having closed that trade.
4. **`background-attachment: fixed` + a derived tint is a repaint cost on old phones.** Verify on her
   actual device, not a simulator.

---

## 5. Questions only Paul can answer

1. **Does the seed own the affirmative ✓ control, or only identity surfaces?** Tonight's change says it
   does. On Clay, "yes" becomes red-brown; on Dusk, purple. The ✓ glyph carries it either way — but that
   makes the glyph load-bearing rather than reinforcing. **Keep it, or hold one fixed affirmative green
   across all seven and let the seed own masthead + ring + edges only?**
2. **Does the green ground follow the seed?** My recommendation is yes, chroma-clamped (§4). It is the
   single largest visual change and it touches Mom's frozen instance's *look* if it ever unfreezes.
3. **Are Plain and Strong swatches, or a separate accessibility control?** My recommendation: Plain is a
   swatch, Strong is a toggle. Both readings are defensible and it changes the onboarding screen.
4. **Is the seven a closed set, or does the model need to accept an arbitrary colour later** (a wheel, a
   photo-picked colour)? A tone-based model supports it for free; a hand-tuned one does not. Worth knowing
   now, because it decides whether the check must run on 7 presets or on any hex.
5. **Whose choice is it — the household's or the reader's?** If two people share an estate and one needs
   Plain, is that a per-device override on top of the household's colour? This decides whether the seed
   lives on the account or in localStorage, which is a data-model question, not a colour one.

---

## Sources

All fetched 2026-09-06.

- Material 3 — colour roles: https://m3.material.io/styles/color/roles · scheme: https://m3.material.io/styles/color/choosing-a-scheme
- Material Color Utilities (HCT, TonalPalette, DynamicScheme): https://github.com/material-foundation/material-color-utilities
- M3 in Compose (roles + dynamic colour): https://developer.android.com/develop/ui/compose/designsystems/material3
- M3 tone/contrast rule (40 → 3:1, 50 → 4.5:1), secondary summary of the M3 spec: https://note.com/pajero/n/ne34d4797a35e
- Wear OS colour roles & tokens: https://developer.android.com/design/ui/wear/guides/styles/color/roles-tokens
- Radix Colors — understanding the scale: https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale
- shadcn/ui theming (background/foreground convention): https://ui.shadcn.com/docs/theming
- USWDS colour tokens, grade & magic numbers: https://designsystem.digital.gov/design-tokens/color/overview/
- Apple HIG — Color: https://developer.apple.com/design/human-interface-guidelines/color *(JS-rendered; not directly extractable — guidance corroborated via MDN's `prefers-contrast` OS mapping)*
- GOV.UK Design System — Colour: https://design-system.service.gov.uk/styles/colour/
- WCAG 2.2 SC 1.4.3 Contrast (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- WCAG 2.2 SC 1.4.11 Non-text Contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- WCAG 2.2 SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- APCA — Why APCA (Lc values, WCAG 2 critique): https://git.apcacontrast.com/documentation/WhyAPCA.html
- MDN `prefers-contrast`: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-contrast
- MDN `forced-colors`: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors
- MDN `monochrome`: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/monochrome
- Android high-contrast text (Google Accessibility Help + AbilityNet): https://support.google.com/accessibility/android/answer/6151855 · https://mcmw.abilitynet.org.uk/android-7-nougat-high-contrast-text
- W3C WAI — Web Accessibility for Older Users, literature review: https://www.w3.org/WAI/older-users/literature/
- NN/g — Usability for Senior Citizens: https://www.nngroup.com/articles/usability-for-senior-citizens/
- Colour Blind Awareness — prevalence & types: https://www.colourblindawareness.org/colour-blindness/
