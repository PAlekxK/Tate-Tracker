# The colour scheme — how one chosen hex becomes a whole UI

**Review date:** 2026-09-06 · **Reviewer:** ux-expert · **Mode:** review (screen-component + system)
**Subject:** the accent scheme across `engine/viewer.template.html`, `onboarding/index.html`,
`estate/index.html`, `homes/index.html`, `settings/place/index.html`, `settings/account/index.html`

**Paul's ruling this session, verbatim:**

> "Hollow Creek Road has got that blue-grey colour, but the buttons below — Save and consult the
> Almanac — are the original Fernwood dark green. That's where the scheme really comes in: it's not
> just what's the colour of the bar at the top but what's the overall UI scheme of colours. To create
> a cohesive personalised experience, all the elements should be somewhat deterministic based on the
> scheme that's selected — I defer to the UX expert on how best to define that — but let's make sure
> it carries through all the different variations. Make it flexible."

⛔ **Nothing was edited.** This file is a specification. The template and all five pages are untouched.

---

## 0. User context, and the one constraint that outranks everything here

- **Primary user:** the person setting up a *new* household — the second-estate reader (Bob at his two
  houses; the synthetic first-household seat). She has just picked a colour on a deliberately neutral
  slate-grey onboarding page, and the next screen is the first time the product is *hers*.
- **Core job:** *"Recognise, in the first second, that this place is mine and not a demo of someone
  else's."* Secondary: *"Act confidently — know which control is the affirmative one — without
  reading."*
- **Context of use:** phone, 414 × 848, A+ text, one-handed, half-attended, often on a poor
  connection. The three 09-06 walk seats each reported "a demo, or someone else's account" as their
  first thought when identity leaked; colour is the fastest-read half of that identity.
- **Assumptions made:** I read the code, `engine/palette.json`, the principles library and the
  09-06 review JSONs' summaries; I did **not** read
  `.user-research/2026-09-06-places-and-settings-journey.md` in full. Where I lean on it, I say so.
- **Confidence:** medium-high.

⭐ **THE CONSTRAINT THAT OUTRANKS EVERY RECOMMENDATION BELOW.** Mom's frozen Fernwood instance does
not move. The template already has the correct mechanism for this and it is ratified — the `:root`
block at `viewer.template.html:349-353` holds the *literal* greens, and the pre-paint block only
overrides them **when a stored accent exists**:

> *"These three tokens default to the exact greens this header has always used, so a reader who has
> never chosen — which today is everyone, including Mom's live app — sees no change whatsoever. Only
> a stored choice moves them."* `[paul-stated 2026-09-05]`

**Every token in §1 must be added the same way: literal Fernwood value as the `:root` default,
derivation applied only over a stored `--accent`.** That is not a caution I am adding; it is the
existing shipped pattern, and reusing it is what makes this whole change ungated for Mom.

---

## 1. The token set

**One input. Ten derived values. No second input.**

The governing idea, and the answer to Paul's "how best to define that": **a scheme is a monotonic
ladder off one hex.** Every surface that carries identity sits at a fixed distance from `--accent`
along a single lightness ramp — never a second hand-picked hue. That is what makes it deterministic,
what makes seven palette colours produce seven coherent schemes rather than seven bespoke ones, and
what makes "a new green" (or a new grey, or a new tan) a *claim that a new object exists* rather than
a paint job — the same argument the v2 button system already won on 2026-08-02.

### The ladder

| # | Token | Derivation | What it paints |
|---|---|---|---|
| 1 | `--accent` | **INPUT** — the chosen hex. Default `#2f5a3a` | the affirmative fill; masthead mid-stop; every filled ✓ button |
| 2 | `--accent-press` | `color-mix(in srgb, var(--accent) 72%, #000)` | pressed/active state of any affirmative |
| 3 | `--accent-ring` | `color-mix(in srgb, var(--accent) 18%, transparent)` | the focus glow (`0 0 0 3px`), paired with a solid `2px var(--accent)` outline |
| 4 | `--accent-ink` | `color-mix(in srgb, var(--accent) 92%, #000)` | links, inline accent text, chip labels, quiet-link tier |
| 5 | `--hdr-1` | `color-mix(in srgb, var(--accent) 55%, #000)` | masthead gradient, dark stop |
| 6 | `--hdr-2` | `var(--accent)` | masthead gradient, mid stop |
| 7 | `--hdr-3` | `color-mix(in srgb, var(--accent) 82%, #fff)` | masthead gradient, light stop; feedback-bubble resting gradient |
| 8 | `--wash-1` | `color-mix(in srgb, var(--accent) 7%, #fff)` | body ground, top of gradient |
| 9 | `--wash-2` | `color-mix(in srgb, var(--accent) 13%, #fff)` | body ground, bottom of gradient — **and** the fill of every accent chip/inset on a white card |
| 10 | `--edge-card` | `color-mix(in srgb, var(--accent) 18%, #fff)` | the card hairline (today `#d8eacc`) |
| 11 | `--edge-secondary` | **holds neutral** — see §2. Optionally `color-mix(in srgb, var(--accent) 66%, #fff)` in tranche 3 | outlined-secondary border |

**The feedback bubble needs no token of its own** — `viewer.template.html:4954` already paints it
`linear-gradient(135deg, var(--hdr-2), var(--hdr-3))` and `:4961` the pressed pair. It derives for
free the moment `--hdr-*` derive from `--accent`. That is already correct and is the model for the
rest.

### Three decisions inside the table worth naming

**(a) `--wash-2` does double duty on purpose.** The page's darker ground tint and the fill of an
accent chip on a white card are the same value. Two separate tokens would land 2–3% apart, which is
exactly the failure the 2026-08-24 colour audit measured — *`rgb(44,74,44)` used 30× and
`rgb(42,74,42)` used 20×, two units apart on one channel, no eye can separate them, both get copied
forward.* One token, used in two contexts that are never adjacent, is the honest answer. A chip on a
white card then reads as *a piece of the page's ground*, which is a coherent idea rather than an
accident.

**(b) `--accent-ink` is darker than `--accent`, and that is load-bearing.** As a fill under white
text, the palette's weakest member clears AAA comfortably. As *ink on near-white*, Dusk sits at
**7.40:1** — 0.40 above the AAA line the repo's own `tools/palette.py` enforces, which is one
rounding step of margin for a reader with documented difficulty reading. Darkening 8% takes Dusk to
**8.27:1** and, as a side effect, keeps a link visibly distinct from a filled button.

**(c) The press ratio is 72%, not onboarding's 84%, and it was chosen to reproduce what already
ships.** Fernwood's shipped pair is `--green-primary: #2f5a3a` → `--green-press: #1f4528`
(`viewer.template.html:105-106`). 72% of the fill computes to `#21412a` — **within 4 RGB units on
every channel** of the shipped press. So a Fernwood-default reader sees no change, and a reader who
picks Clay gets a press state that behaves exactly like the one Paul has been looking at for months.
`onboarding/index.html:79` currently uses 84%, which is a visibly shallower press. **Two derivations
for one idea is the same defect as two hexes for one colour** — pick 72% and change onboarding to
match, so the affirmative behaves identically on the setup page and the app.

### The derivation runs in CSS, not in JavaScript

Today `viewer.template.html:6399-6402` does three `setProperty` calls with a hand-rolled `mix()`.
That was right when there were three tokens; at eleven it becomes eleven JS calls that can drift from
the CSS they feed. **The pre-paint block should set exactly one property — `--accent` — and every
other token should be a `color-mix()` in the `:root` block**, which is where a reader looking for
"what colour is the pressed state?" will actually look.

Keep the existing fail-silent guard as written (`:6393`, regex-validated hex, `return` on anything
malformed) — *a broken personalisation must never cost a reader the working page underneath it* — and
keep the two-declaration fallback pattern already used at `onboarding/index.html:75-81`: a literal hex
on the first line for Safari < 16.2, the `color-mix()` on the second. Where `color-mix` is
unsupported the second declaration is simply invalid and the first stands, reproducing today's
behaviour exactly. Never worse, never a wrong colour.

### How I checked contrast, and what it says

I recomputed WCAG 2.x relative luminance by hand from each hex (sRGB linearisation, then
`0.2126R + 0.7152G + 0.0722B`, ratio `(L₁+0.05)/(L₂+0.05)`) — the same formula
`tools/palette.py:26-36` implements. **I validated the method against a number this repo already
holds:** `viewer.template.html:5050-5051` documents white on `#3a8a58` as **4.2:1**; my computation
returns **4.24**. ⚠️ **These are hand-computed, not executed** — this seat has no shell.
`python3 tools/palette.py` is the deterministic instrument and should be re-run before anything ships;
treat every figure below as a hypothesis until it agrees.

**White text on `--accent` (the affirmative fill) — the bar Paul asked about:**

| colour | hex | white-on-fill | as ink on `#fbfcfd` |
|---|---|---|---|
| Fern | `#2C4A2C` | 9.89 | 9.63 |
| Clay | `#7A3E2A` | 8.24 | 8.02 |
| Stone | `#3F5266` | 8.04 | 7.83 |
| Lake | `#2C5674` | 7.81 | 7.60 |
| Pine | `#2F5D3A` | 7.64 | 7.44 |
| Spruce | `#245C5C` | 7.61 | 7.41 |
| Dusk | `#6B4676` | 7.60 | 7.40 |

All seven clear **AA (4.5) by a wide margin and AAA (7.0)** on both jobs. The affirmative fill is safe
for every palette member. Band spread 2.23 — the known trade recorded in `palette.json:5`, unchanged
by anything here.

---

## ⚠️ The one contrast risk I found, and it is in the derivation, not the palette

**`--hdr-3` at the currently-shipped +28% white would fail AA for the palette's lighter members.**

The masthead is a 135° gradient and it carries **white text** — the h1, the subtitle, the address
line, the date line and the A/A+ chips. The lightest stop is where white text is most at risk, and the
address/date lines run wide enough to reach it.

The shipped JS uses `mix(0.28)` (`:6402`). Computed at that value, **Dusk gives 3.80:1** — below AA
(4.5) for normal text. Spruce, Pine and Stone land in the low 4s. Changing the derivation to **+18%
white (`82%` accent)** clears all seven:

| colour | `--hdr-3` @ +28% (shipped) | `--hdr-3` @ +18% (**recommended**) |
|---|---|---|
| Dusk | **3.80 ⛔** | 4.83 ✅ |
| Spruce | ~3.9 ⛔ | 4.87 ✅ |
| Pine | ~3.9 ⛔ | 4.86 ✅ |
| Lake | ~4.0 ⛔ | 4.95 ✅ |
| Stone | ~4.1 ⛔ | 5.00 ✅ |
| Clay | ~4.3 ⛔ | 5.19 ✅ |
| Fern | ~4.9 ✅ | 5.86 ✅ |

Two things follow, and the second is the more interesting one:

1. **Change the light-stop derivation to +18% before any second household picks a colour.** It costs
   one number. At +28% the masthead is *slightly* more luminous and *materially* less readable, on
   the one surface whose entire job is "this place is mine."
2. ⭐ **Fernwood's own literal `#3a8a58` is 4.24:1 and fails AA today.** It is grandfathered — the
   `:root` literal keeps Mom's page exactly as it is, and moving it is a gated Mom-facing change, not
   a token question. But it is worth stating plainly: **the derived path would be stricter than the
   literal it replaces.** That is the right direction for a system that is about to serve people
   nobody has met.

Two secondary notes: `--edge-card` at 18% is a very light hairline (≈1.1:1 against a white card).
That is **not** a WCAG 1.4.11 failure — 1.4.11 governs boundaries required to *identify a control*,
and a card edge is not a control — and today's `#d8eacc` on `#e2f0d8` is ≈1.06:1, so this is an
existing accepted condition, not a regression. And the ladder must stay **monotonic**: `--wash-1` <
`--wash-2` < `--edge-card` < `--accent`. If a future value breaks that order the card stops having an
edge, so any change to one of the four percentages is a change to all four.

---

## 2. What must NOT derive

**The rule, stated once so it is checkable:**

> **The scheme says WHOSE this is. A semantic colour says WHAT this is.**
> A colour whose *meaning* would change if the accent changed is not a scheme colour.
> Falsifier: *if a reader who picked Lake could no longer tell "ahead" from "her colour," it should
> never have derived.*

This is the direct application of the 2026-08-24 finding already in `fernwood.md` — *"a naive 'reduce
to eight colours' would break a working system… the target is naming, not flattening"* — and of the
`Register is carried by chrome, not just words` candidate.

**The exclusion list:**

| What | Where | Why it holds |
|---|---|---|
| **Care-type lexicon** — `CARE_COLORS` + `.c-/.b-/.bg-/.br-/.t-{type}` | `:15087` and the utility block | Six distinguishable actions, paired with six glyphs, consistent across dashboard teaser and card. `fernwood.md`'s glyph principle names this as *the canonical example of an icon system that earns its place*. Deriving collapses six identities into one hue family. |
| **`.peak-state.now / .ahead / .closed`** | `:3899-3901` | A three-way temporal semantic (green / blue / brown). If `.now` takes the accent, a **Lake** reader's `.ahead` (`#305880`) becomes indistinguishable from her own colour — the state stops being a state. |
| **Seismic severity** — `.prop-seismic-mag.light / .moderate / .strong` | `:1607-1609` | Ordered severity. ⚠️ The *base* chip at `:1602-1604` **does** derive; the three variants do not. This one selector block is the cleanest illustration of the whole rule. |
| **Sync pill — five states** | `:5736-5740` | Load-bearing under the physical-premise block: *no cell reception, coverage falls off with distance from the house.* `fn-sync-local-only` (amber) and `fn-sync-error` (red) mean **"your words may not have left this device."** A Clay accent would turn the error state into the brand colour. *Capture must not lie* — and a state that reads as chrome is a lie. |
| **`.pmap-sync.synced / .syncing`** | `:999-1001` | Same argument, zone-audio path. |
| **`.feedback-status.ok / .err`** | `:5060-5061` | Outcome, not identity. |
| **`.rv-badge` rainfall status chips** | `:2832` ff. | Measured-vs-modelled provenance signalling. Provenance honesty outranks cohesion. |
| **The warm machine/spec register** — `.vehicle-specs-panel.maint`, `.tips`, `.vnotes`; the cream feedback panel `#fbf8ee` | `:5025` ff. and the vehicles block | This is `Register is carried by chrome, not just words` doing its job. Two registers on one surface must be *structurally* distinguishable for the half-engaged reader. If the tan takes the accent, journal and machine collapse into one skin and she loses the visual routing. |
| **`.chorus-now` dark inset** | wildlife block | *"the only surface in the app that describes the property after nightfall, and the contrast is the point."* |
| **`--edge-secondary` and the outlined-secondary family** — `.gg-suggest-btn-no`, `.gg-suggest-btn-neutral` | `:107`, `:5380-5386`, `:5094-5097` | ⭐ **The most important one.** Standing rule 1 is *filled + ✓ for the affirmative, **outlined neutral** for secondary.* The secondary's whole job is to be the **absence** of the affirmative. If it takes the accent too, the grammar loses half its signal — everything on the card is her colour and nothing says "this is the one." Hold neutral. (§4 offers a tranche-3 option that de-warms it without accenting it.) |
| **Ink** — `#183524` where it paints body/title text | `:1750`, `:1962`, `:2226` | These read as "the accent, used as text," but they are the app's **ink**. They should be reclassified to an `--ink` token, **not** to `--accent-ink`. A Dusk reader does not want purple body copy. |

---

## 3. Inventory — the hardcoded greens in the affirmative grammar and its neighbours

`engine/viewer.template.html`. Grepped `#2a6040` · `#3a8a58` · `#183524` · `#2f5a3a` · `#1f4528` ·
`.gg-suggest-btn-yes` · the unified-input submit rules. **`#2f5d3a` and `#24543a` return zero hits in
the template** — `#2f5d3a` lives in the four signed-in pages (see §3d) and `#24543a` is not in this
codebase.

### 3a. ✅ ALREADY TOKENISED — the affirmative grammar is done

⭐ **This is the headline finding, and it reframes the whole job.** Paul's complaint was that Save and
"Save & consult the Almanac" stayed Fernwood green. They stayed green **not because they are
hardcoded** — they are not — **but because the token they read from was never wired to `--accent`.**

| line | rule | reads |
|---|---|---|
| `105-107` | `:root` | `--green-primary: #2f5a3a` · `--green-press: #1f4528` · `--edge-secondary: #8a7a4a` |
| `4548-4553` | `.ui-save-btn` | `var(--green-primary)` / `:active var(--green-press)` — **this is Paul's "Save"** |
| `5047-5053` | `.feedback-send` | `var(--green-primary)` |
| `5215`, `5231` | `.mom-queue-launcher-go` | `var(--green-primary)` / `var(--green-press)` |
| `5373-5379` | `.gg-suggest-btn-yes` | `var(--green-primary)` fill + border, `var(--green-press)` pressed — **the ratified affirmative** |
| `349-353` | `:root` | `--hdr-1/2/3` literals |
| `4954`, `4961` | `.feedback-ribbon` | already `var(--hdr-2)/var(--hdr-3)` and `var(--hdr-1)/var(--hdr-2)` — **already fully scheme-aware** |

**Consequence: making every affirmative in the app take her colour is a three-line change.** Not
thirty rules. The 2026-08-02 button pass did the hard part and nobody noticed it had also solved this.

### 3b. DERIVE — currently literal, should read a token

**The "now / active / selected" family** — state markers, the highest-value cohesion group after the
buttons:

| line | rule | literal | → |
|---|---|---|---|
| `1691` | `.main-card-header:focus-visible` | `outline #3a8a58` | `var(--accent)` + `--accent-ring` |
| `2114` | `.forecast-day.today` | `gradient #2a6040,#3d8a5e`; `border #2a6040` | `--hdr-2`/`--hdr-3` |
| `2226`, `2228` | `.filter-btn.active` (+ `.filter-count`) | `#183524`, `#2a6040` | `--accent-ink` / `--accent` |
| `2891` | `.cal-tab.active` | `#183524`, `#2a6040` | same |
| `3824` | `.plant-view-tab.active` | `#183524`, `#2a6040` | same |
| `3945` | `.wildlife-tab.active` | `#183524`, `#2a6040` | same |
| `2922-2923` | `.tl-month.current` | `border #3a8a58`; `shadow rgba(58,138,88,.2)` | `--accent` + ring |
| `2990` | `.hm-month-header.current` | `background #3a8a58` | `--accent` |
| `3018` | `.hm-cell.current-month` | `border #3a8a58` | `--accent` |
| `4962` | `.feedback-ribbon:focus-visible` | `outline #cfe6b8` | `--accent-ring` |

**Chips, insets and accent ink:**

| line | rule | literal | → |
|---|---|---|---|
| `655-657` | `.bio-deep-dive-chip` | `#2a6040` on `#eaf6e2`, border `#c4dcae` | `--accent-ink` on `--wash-2`, `--edge-card` |
| `668-669` | `.bio-take-part-title` | `#2a6040` | `--accent-ink` |
| `693` | `.bio-take-part-status.active` | `#e4f4dc` / `#2a6040` | `--wash-2` / `--accent-ink` |
| `1602-1604` | `.prop-seismic-mag` **base only** | `#e8f4e8` / `#2a6040` | `--wash-2` / `--accent-ink` ⚠️ `1607-1609` stay semantic |
| `1623-1631` | `.prop-action-chip` | `#e8f4e8` / `#b8d8b8` / `#2a6040` | wash / edge / ink |
| `1878-1884` | `.rain-local-note` | `border-left #3a8a58` | `--accent` |
| `2314` | `.peak-window-chip` | `#2a6040` on `#f0fae8`, border `#c8e0a8` | ink / wash / edge |
| `2641` | `.vehicle-manual a` | `#2a6040` | `--accent-ink` |
| `3472` | `.cel-nws-strip-label` | `#2a6040` | `--accent-ink` |
| `3891-3893` | `.plant-action-peak` | `#2a6040` on `#f0fae8` | ink / wash |
| `3907-3910` | `.plant-detail-season-tip` | `#2a6040`, `border-left #4a9e6b` | ink / accent |
| `1316` | `.pmap-grow-mic` | `gradient #2a6040,#3a8a58` | ⚠️ see below |

⚠️ **`.pmap-grow-mic` (`:1316`) is a v2-system violation as well as a scheme one.** It is a primary
commit wearing the *masthead gradient*. The v2 rule is explicit: *"Flat `var(--green-primary)` since
v2 — the gradients were half of why the greens read as 'all different' on one screen"* (`:4549-4550`).
It should be flat `var(--accent)`, not `--hdr-2`/`--hdr-3`. Fixing the scheme and fixing the shape
system are the same edit here.

**The quiet-link tier** — four rules that hand-copy the token values rather than reading them, so they
will not follow the accent even after tranche 1:

| line | rule | literals |
|---|---|---|
| `240-253` | `.card-later-link` (+ hover, focus) | `#4a6a3a`, `#b9cfa6`, `#2f5a28`, `#3a7a3a` |
| `4179`, `4182` | `.ack-change-link` | `#2f5a3a`, `#b9cfa6`, `#1f4528`, `#3a7a3a` |
| `4193`, `4199` | `.ack-inline-link` | `#2f5a3a`, `#1f4528`, `#e6f2da`, `#3a7a3a` |
| `4941` | `.mom-queue-general-toggle` | `#6a7a52`, `#bcc9a0` |
| `5103-5114` | `.mom-queue-addnote` | `#4a6a3a`, `#b9cfa6`, `#2f5a28`, `#3a7a3a` |

⚠️ **`#2f5a3a` and `#2f5a28` appear as literals here while `--green-primary` holds `#2f5a3a` five
lines above.** Two of these are *the token's own value, typed again.* Straight `var()` replacement,
zero rendering change.

### 3c. ⭐ Two near-duplicate greens, and three different answers to "no choice yet"

**`--green-primary` is `#2f5a3a`. Palette `pine` is `#2F5D3A`.** Three units apart on one channel. No
eye separates them; both will be copied forward. This is precisely the 2026-08-24 candidate —
*"two colours a reader cannot tell apart must be one token."* **Recommendation: reconcile Pine's hex
to `#2f5a3a`** so a reader who picks Pine gets *exactly* Fernwood's button green rather than an
invisible near-miss, and the app's default `--accent` is a genuine palette member rather than an
eighth colour that is not in the list. (Contrast barely moves: 7.64 → 7.68 on white.)

**And there are currently three defaults for a reader who has never chosen:**

| source | value |
|---|---|
| `engine/palette.json:6` | `"default": "stone"` → `#3F5266` |
| the four signed-in pages | `--accent: #2f5d3a` (Pine) |
| `viewer.template.html:350-352` | the green triple `#183524 / #2a6040 / #3a8a58` |

A token set cannot fix this; a single declared default must. **Recommend: `#2f5a3a` everywhere,
declared once in `palette.json` and read by all six surfaces.** Today the four pages and the app
disagree by three RGB units, which is invisible and therefore worse than a visible disagreement —
nothing will ever flag it.

### 3d. The four signed-in pages + onboarding

| file | state |
|---|---|
| `onboarding/index.html:59-83` | ⭐ **the reference implementation.** `--accent` with `--accent-on` and `--accent-ring` both derived via `color-mix`, plain-hex fallbacks, and a comment recording that they used to be independent hexes and it was wrong. **Copy this pattern; do not invent a second one.** |
| `estate/index.html:51, 65, 77, 124, 130, 141` · `:270-271` | `--accent: #2f5d3a`, set at runtime from `fw-accent`. Used for header, filled buttons, links, composer. **No press state, no ring, no ink** — the *same* value paints a header, a button fill and a link. |
| `homes/index.html:37, 46, 61, 78, 85` · `:152-153, 216` | identical shape, plus a `--accent` rail |
| `settings/place/index.html:31, 38, 57, 66-67, 74` · `:144-156, 178` | identical |
| `settings/account/index.html:36, 43, 71-72, 79` · `:146-153, 172, 198` | identical, reading `fw-profile-accent` first |

**One value doing three jobs is the defect on these four pages.** A header background, a button fill
and a link all take raw `--accent`: the link is over-heavy and the pressed state does not exist, so a
tap on "Save" gives no feedback at all. Adding `--accent-press` / `--accent-ring` / `--accent-ink` to
these four is a ~6-line-per-file change and it is the highest-value-per-keystroke work in this whole
document.

---

## 4. Order of application

Sequenced by **cohesion gained per unit of risk**, where "risk" means *how close does this get to
Mom's frozen surface*.

### ⭐ Tranche 1 — wire the input. ~6 lines. Zero rendering change for any current reader.

Everything here is a re-point of an existing token or a value that already equals its literal.

1. **`viewer.template.html:91-109`** — add to the `:root` token block: `--accent: #2f5a3a`,
   `--accent-press`, `--accent-ring`, `--accent-ink`, each with a plain-hex first declaration and a
   `color-mix()` second (the `onboarding/index.html:75-81` pattern).
2. **`viewer.template.html:105-106`** — re-point `--green-primary: var(--accent)` and
   `--green-press: var(--accent-press)`. **Keep the old names as aliases** so not one rule below them
   changes. *(Retire the green-flavoured names in tranche 3, once nothing reads them.)*
3. **`viewer.template.html:349-353`** — keep the three literals as defaults; add the three
   `color-mix()` derivations off `--accent` as second declarations.
4. **`viewer.template.html:6391-6403`** — replace the three `setProperty("--hdr-*")` calls with a
   single `setProperty("--accent", hex)`. Keep the regex guard and the fail-silent `return` exactly as
   written. **Delete the hand-rolled `mix()`** — the ladder now lives in CSS.
5. **`viewer.template.html:6402` → the light-stop derivation** — `+28%` white becomes `+18%` (the AA
   finding above). Fernwood's literal `#3a8a58` is unaffected; this only governs a chosen accent.
6. **`onboarding/index.html:79`** — change `--accent-on` from `84%` to `72%` so the setup page and the
   app press identically.
7. **The four signed-in pages** — add `--accent-press`, `--accent-ring`, `--accent-ink` beside the
   existing `--accent`; point `button.save` / `button.send` / `.ubtn` at the press state, `a` at
   `--accent-ink`, and every `:focus` at the ring.

**After tranche 1:** Save · "Save & consult the Almanac" · every ✓ affirmative · every pressed state ·
the masthead · the feedback bubble · every focus ring · every link on the four pages all carry her
colour. That is Paul's complaint, closed, in the fewest possible edits — because the 2026-08-02 button
pass had already built the plumbing.

**Verification before it ships:** `python3 tools/palette.py --check` (my ratios are hand-computed);
`python3 tools/build-viewer.py --check` (template ↔ `viewer.html` byte-identity); a walk at **414 ×
848 × A+** with **no** stored accent, confirming byte-identical rendering to today.

### Tranche 2 — the state-marker and chip families. ~30 rules. Mechanical, low risk.

Everything in §3b: tabs, `.current`, `.today`, filter counts, peak chips, `.rain-local-note`,
`.pmap-grow-mic` (flatten it while you are there), and the five quiet-link rules. All are literal →
`var()` swaps that evaluate to the same colour for a Fernwood-default reader.

**Why second, not first:** these are the difference between *the buttons are hers* and *the app is
hers*. Real cohesion gain, but each is one grep-and-replace, and none of them is the thing Paul
actually noticed tonight.

**Do the `.prop-seismic-mag` split deliberately** (`:1602-1604` derives, `:1607-1609` does not) and
leave a one-line comment saying why. That block is the worked example of §2 and the next reader will
otherwise "finish the job."

### Tranche 3 — the ground, the hairline and the neutral edge. GATED.

`--wash-1`, `--wash-2`, `--edge-card`, and optionally de-warming `--edge-secondary`.

⚠️ **This is the only tranche that can move Mom's surface, and only if the defaults are done wrong.**
The current body gradient `#edf7e6 → #e2f0d8` is a *yellow*-green and is **not derivable** from
`#2f5a3a` — a straight mix gives `#ecf0ed`, materially greyer. Same for the `#d8eacc` hairline. So:

- **Pin the Fernwood literals as the `:root` defaults.** Only a stored `--accent` moves them. This is
  the ratified 09-05 mechanism, applied unchanged — no new pattern, no new risk.
- The ladder must stay monotonic: `--wash-1` < `--wash-2` < `--edge-card` < `--accent`.
- **`--edge-secondary` is a genuine open question, not a task.** Holding it neutral is correct under
  standing rule 1 (§2), but the current warm tan `#8a7a4a` will fight a Dusk or Lake accent. If Paul
  wants it de-warmed without accenting it, `color-mix(in srgb, var(--accent) 66%, #fff)` is the
  shallowest mix that keeps every palette member above WCAG 1.4.11's 3:1 for a control boundary —
  **Dusk, the worst case, lands at 3.32:1**, against the current tan's documented 4.0:1. That is a
  real reduction in margin on a control edge for a reader with documented difficulty reading, so I do
  **not** recommend it by default. Ask Paul; do not decide it here.
- **Run the release cascade** (synthetic persona → Paul → Mom) before anything in this tranche
  reaches production, per the standing rule. Mom is gate 3, never gate 1.

---

## Open questions for Paul

1. **Does `--edge-secondary` belong to the scheme or to the neutral?** My recommendation is neutral
   (standing rule 1 needs the secondary to be the *absence* of the affirmative), but a warm tan beside
   a purple or blue accent will read as a leftover. Tranche 3, your call, numbers above.
2. **Reconcile Pine `#2F5D3A` to `#2f5a3a`?** Two greens three units apart in one system.
3. **One declared default across `palette.json`, the four pages and the app?** Today there are three.
4. **Is the masthead light-stop change (+28% → +18%) acceptable as a silent fix,** given it only
   affects readers who have chosen an accent — of whom there are currently none in production?

## Principles this review would propose

Both are **second occurrences** of things already in the library, which is the bar for promotion —
but the wording is mine, not Paul's, so they are proposals.

1. **A scheme is a monotonic ladder off one input; a semantic colour is not on the ladder.**
   *Scope:* cross-project. *Rationale:* this is the second occurrence of the 2026-08-24 Fernwood
   colour finding (*"the palette is right; it has no names"*), now with a concrete mechanism and a
   falsifier — *if a reader who picked Lake could no longer tell "ahead" from "her colour," it should
   never have derived.* The first occurrence named the disease; this one names the cure.

2. **A personalisation token must default to the literal it replaces.**
   *Scope:* cross-project. *Rationale:* second occurrence of the pattern Paul stated on 2026-09-05 for
   `--hdr-*` (*"a reader who has never chosen sees no change whatsoever"*), now generalised to a
   ten-token set and to a second surface class (ground, hairline). It is what lets a scheme ship
   ungated: personalisation is **additive over a working default**, never a replacement of it.
