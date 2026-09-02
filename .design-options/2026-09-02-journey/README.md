# 2026-09-02 · the customer journey — cold open → login → select → arrive

Two exhibit sets, both at **414 × A+** — Mom's *measured* conditions, not the 390 × A convention.
Width verified from inside the iframe; `text-lg` verified as **applied** (`body.className`), not merely
stored.

| set | question | recommendation |
|---|---|---|
| `door/` | Does the login sit **before** the app, **inside** it, or **once** at the threshold? | **R1-B, the room** |
| `selector/` | At two grants, what is the switch — and what does she see at **one**? | **R1-SA, the masthead is the control** |

⚠️ **Frames 2 and 3 do not exist in code.** These are appearance-and-affordance mocks injected into
the live viewer. **No behaviour is claimed** — there is no auth, and no place-switching. What is real:
the components (`.gg-suggest-btn-yes` is the ratified affirmative button itself, not a lookalike), the
type, the palette, the viewport and the data.

⛔ **No invented data.** Every string describes an affordance; none asserts a fact about the world.

**"Midtown condo"** is a placeholder second estate at Paul's instruction — *"we don't have to have any
content behind it, but that can be a placeholder there just to help make the design feel right."*

**Constrained by** `.ux-reviews/2026-09-02-login-door-and-selector.md` (same-day norms pass; it
constrained the option set rather than ratifying it). **Credential shape is held constant** across all
three door options so placement is the single variable — it is its own later round, and it is the one
question only she can answer.

`harness.html` is the capture rig. ⚠️ It re-derives `measure-nesting-width.js`'s `inFrame()` at its
**pre-fix** version — correct for localhost, but it means this stage and the leg-6e ship gate look at
the app through two different frames. See the skill's run log, friction 7.
