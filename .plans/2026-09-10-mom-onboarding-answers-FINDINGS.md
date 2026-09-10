# Mom's four onboarding answers — what they say, 2026-09-10

- row: proposed
- objective: O3
- class: instance
- stage: concept
- seats: user-researcher → this file
- ready: agent-proposed 2026-09-10 — Paul rules

**Source.** `.private/feedback-sweep/home-2026-09-10.json` — records `onboard-name-1hzjso6`,
`onboard-address-i6cq9s`, `onboard-addr-confirm-ithot3`, `onboard-interests-1sysjol`; person
`p-nezjzeaotlk`, estate `est-e6696a`, env `home`, **12:24:41 → 12:26:12 ET**. ⛔ The address record is
referred to by id and shape only — not quoted here, and it must not reach `BACKLOG.md`.

⚠️ **Her path is not the seats' path.** She set up on `home` under the OLD Worker, where signup
granted an estate — she landed *in* `est-e6696a`, which already held Paul's Grant Park records from
09-07. She met the same step-numbered flow he did (1 name · 2 address · 4 confirm · 5 interests).
The five seats walked **J0 founding-owner** on **QA @ 318416a** tonight: different build, different
journey, screens she never saw (the empty shelf, *Set up my first home*, the founded-confirm card).
**Compare answers, never screens.**

## 1 · What each answer tells us

**`onboard-name-1hzjso6` — "Fernwood"** (8 chars, 12:24:41)
- `[validated]` She named the place **Fernwood** — a proper noun, her own typing, the name the
  project has used since 2026-05-19. (Record; deterministic AI-free capture.)
- `[inferred]` The naming step cost her nothing: **the place already had a name in her head.** The
  apparatus around that ask — *"you can rename it later"*, *Call it something else ›* — is insurance
  against a decision she never had to make. `[assumption]` Don't generalise past her.

**`onboard-address-i6cq9s`** (41 chars, 12:25:07 — 26s after the name)
- `[validated]` Complete multi-part entry — line1 / city / state / zip, **no unit line**, captured
  `verified: false`. Parts reconcile field-for-field to the property's address of record.
- `[inferred]` 26s is consistent with typing an address she knows cold, no correction loop. She did
  not stall at the step the plan calls the riskiest on the flow.

**`onboard-addr-confirm-ithot3`** (52 chars, `agrees: true`, 12:25:13 — **6s later**)
- `[validated]` She **answered the confirm ask affirmatively** — the exact ask the `mom` seat never
  tapped and asked to have ruled on.
- `[inferred]` Six seconds is a tap, not an inspection. *She answered it* and *she checked it* are
  different claims; only the first is on the record. (Weak corroboration: Paul's 09-07 run shows the
  identical 6s gap — n=2, one of whom built it.)

**`onboard-interests-1sysjol`** — `garden > motor-pool > house-systems > equipment > wildlife > papers`
(12:26:12 — 59s later)
- `[validated]` Six items, that order, captured under the **current** question wording (*"What
  matters most at your place?"* — the activity reframe is on a branch, not on `home`).
- `[validated]` **Her order is not the screen's order.** Those six sit at display positions 1·2·3·4·5·6
  (house-systems, papers, equipment, garden, motor-pool, wildlife); she returned **4·5·1·3·6·2** —
  display-2 (**papers**) last, display-4 (**garden**) first.
- `[inferred]` She read the list rather than skimming top-down — the best evidence yet that s5 is
  teaching us about a person and not about its own ordering.
- `[validated]` Her session produced **no `interests-other` and no `onboarding-note` record**; both
  posts fire only on non-empty text, so both free-text boxes were left empty. ⛔ Not evidence of no
  unmet need — she is the person who has been asking Paul by name for a zone-by-zone fertilizer list
  the product has never offered.

## 2 · What matters most to her, on this evidence

`[inferred]` **The living half of the place outranks the record-keeping half.** Gardening first, the
fleet second, her own coined *household systems* only third, and **papers last** — the row this repo
calls *"never offered before and the most differentiating"* (`onboarding/index.html:877`). Two of
these move standing assumptions: motor-pool at #2 has no support anywhere in her persona material,
and house-systems at #3 deflates the inference that coining the phrase made it her lead interest.

**Falsifier.** If over the next four weeks her app behaviour (card opens, Guru turns, zone audio,
notes) is *not* disproportionately garden and vehicles, or if she asks Paul for a papers capability,
this ranking was a first-screen artifact — *what she could picture on that screen*, not what she
wants. ⚠️ Second falsifier, for the label ruling: if she ranks again under reworded labels and
`garden` moves, the wording moved her, not her interest.

## 3 · Against the `mom` synthetic seat (a model of a model — her answer outranks it)

| | seat (QA @ 318416a, J0) | her record |
|---|---|---|
| naming box | blank; the name is the walker's own, not a default | **agrees** — a proper noun, hers |
| the confirm ask | never tapped; *"is 'Yes, that's it' supposed to matter?"*, predicted as an ask she'd pass over | ⛔ **disagrees** — answered, `agrees: true`, in 6s |
| free text / *Something else* | ranked 2, typed nothing | **agrees** — ranked 6, typed nothing |
| list leads with chores / assumes a yard | seat (a condo) objected to gardening-led ordering | **out of scope for her** — she is the yard case and found `garden` at position 4 anyway |
| whole flow | "no stop" | **agrees** — 91s, four commits, no abandonment |

⭐ The one that matters: the seat's rule-7 prediction — *she passes over asks with a right answer* —
is **not general**; she answered this one. Its underlying question survives and is sharper: an ask
answered in six seconds is not a data-quality control, so *is the confirm load-bearing?* is still Paul's.

## 4 · Backlog implications (proposed row titles — for the refinement window to place)

1. **`est-e6696a` now holds two published places — run `check-canon-scope.py --deep` before any digest
   for it.** Her Fernwood record and Paul's Grant Park records share one estateId, the rank-election
   collision that tool names, and at most one of them can be right.
2. **Confirm the 09-10 `home` arrival was geocoded (`verified: false` at capture).** `read-geocodes` /
   `watch-accounts` for `p-nezjzeaotlk`; an address with no coordinates SHOUTS, and she is the one
   household that must be placed.
3. **Rule the `garden` label with her ranking on the record.** *Gardening* vs *Growing things* now has
   the make-or-break user ranking it first under the current wording.
4. **Stamp every ranking with the wording it was captured under.** Rewording s5 changes what a ranking
   *means*; hers becomes incomparable to every later one unless the wording rides with the record.
5. **`/api/onboarding-metrics` has no GET, so the position-vs-preference series has no reader.** The
   code records each item's position; nothing reads it back, and the sweep carries only tapped ids.
6. **Record what a person was SHOWN at s5, not only what they tapped.** Six ranked ids cannot
   distinguish *six of six* from *six of eleven*, so no declined-interest reading is possible today.
7. **Track B (fleet) has make-or-break-user evidence for the first time** — she put looking after a
   vehicle second, ahead of her own coined domain.
8. **No walk describes the path she actually took** — old signup-grants-an-estate on `home`; gate-3
   evidence from J0 on QA is a different journey on a different build.

## 5 · What four records cannot tell us

- **Was she alone?** Nothing distinguishes unassisted setup from Paul beside her — and that decides
  whether this is evidence of a self-serve flow at all. ⭐ **Ask Paul: highest-value missing fact here.**
- **What she was shown** at s5 (six items or eleven), therefore nothing about what she *declined*.
- **Whether she read the confirm screen** or tapped through it. Six seconds does not say.
- **Whether anything she typed failed to post.** Empty boxes are the likely reading; a silently-failed
  fifth post is not excluded.
- **Whether she was placed.** `verified: false` is a capture-time flag, not an outcome.
- **What she did after step 5** — no `watch-activity` / engagement read for `home` is in this file.
- **Anything about how it felt.** All four records carry `sentiment: null` and no free text: evidence
  of completion, and of nothing else.
