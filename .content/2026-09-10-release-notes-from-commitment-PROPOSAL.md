# THE RELEASE NOTE AS A DERIVED THING — shape, a draft for this build, and its falsifier · PROPOSAL

- row: proposed — BACKLOG.md § ▶️ NEXT (content; pairs with the build-description chain)
- objective: O5 — ⚠️ **inherited from the sibling DESIGN, not independently derived**
- class: engine · declared — the *product* log is identical at every household
- kind: content proposal
- stage: concept
- seats: content-steward → this file
- ready: agent-proposed 2026-09-10 — Paul rules
- stage-note: 2026-09-10 — written read-only at HEAD `8eadcb6`; closes L4 of
  `.plans/2026-09-10-build-description-chain-DESIGN.md`. ⛔ **Nothing here ships.** `RELEASE_NOTES.md`
  and `viewer.html` were not edited. Every authored line reaching a person is human-confirmed.
- audience: **a household reader** — the person who set the place up, at any household, reading the
  *Recent updates* card. ⛔ Not Mom: her legacy Fernwood is frozen and **this note does not reach her app.**
- surface: `RELEASE_NOTES.md` → `tools/build-release-notes.py` → the *Recent updates* card
- charter: `~/.claude/content-principles/fernwood.md` + `cross-project/voice-and-stance.md`
- tone register: **plain-report** — a reader who is new here, mid-setup, and does not yet know what
  the app is allowed to do for them

---

## 0 · The short version

1. The note's **title** is derived (from the committed row's `note:` field); its **bullets** are authored.
2. The *what-you-can-do / what-did-not-change / what-we-are-not-yet-doing* structure **fits the voice —
   as bullet ORDER, never as sub-headings.** The parser drops them; see §1c.
3. ⭐ The strongest falsifier is the **mirror** of P4, not P4 itself: assert the title's **absence**
   for every committed row the walk did not reach. §3.

---

## 1 · THE SHAPE

### a · Which field comes from where

| in the note | derived from | rule |
|---|---|---|
| `## YYYY-MM-DD` | the deploy | the date it reached an origin, never the commit date |
| `— Title` | **L1/P2 · the committed row's `note:` field** | one title per row, or the row reads `none — <reason>` and is silent here |
| the **do**-bullets | **L3 · a committed id with a `read-against-scope` line that a seat walked and passed** | one bullet per walked id, max |
| the **no-longer**-bullets | the committed row's *done means* cell, read against what the walk actually did | describes what stopped being wrong, not what was fixed |
| the **not-yet**-bullets | the commitment's own excluded scope | verbatim in intent from beat 6, never re-decided here |
| everything else | ⛔ nowhere. If no link supplies it, it is not in the note | |

### b · The three moves, and why they fit this voice

They are already latent in the log. `2026-09-07` runs *the shortcut is back* → *nothing was lost* →
*the sky page says less now*; `2026-09-01` closes on *some of the zones are still in progress… more
names may still move*. So the structure is a discipline over ordering, not a new form.

⭐ **What it buys, in charter terms:** the *not-yet* move is the only place this project has ever had
to say **what it is not doing**, and a reader mid-setup needs that more than a reader of a mature app.
It is `soften framing rather than delete` applied to scope instead of to species prose.

### c · ⛔ AS ORDER, NOT AS SUB-HEADINGS — and this is mechanical, not taste

`tools/build-release-notes.py:51-66` builds a bullet **only** from a line starting `- `. A non-bullet
line is appended to the open bullet, or — after a blank line — **dropped silently**. So a
`**What you can do now**` sub-heading either **vanishes from the app** or is **swallowed into the
previous sentence**, and the repo's own script prints a bullet count that looks right either way
(the exact failure recorded in that function's comment, found 2026-08-01 by diffing the payload).
**The bolded lead clause of each bullet does the heading's job.** One list, ordered: do · no-longer ·
not-yet.

### d · ⛔ What a note must never claim

1. **A capability no seat walked.** If gate ① holds no passed `read-against-scope` line for the id,
   there is no do-bullet. A candidate is named as a candidate or not at all.
2. **A thing that is being wired.** "Now" means at the deployed sha, on the reader's screen.
3. **Anyone's feedback.** Attribution is the ribbon's job `[2026-08-04]`; a change nobody caused
   belongs here, and a change somebody caused is named *there*, without a name here.
4. **A place.** ⭐ This log is identical at every household, so the charter's anchor inverts: it may
   not name Fernwood, its laurels, its pond or its gauge. **It is anchored in the reader's own record
   instead** — *your home*, *the shelf*, *what this account holds*. That is what keeps it off the
   could-be-anyone floor without borrowing another household's place.
5. **Repo words.** `estate`, `instance`, `QA`, `production`, `legacy`, `sha`, `beat`. Mom's frozen
   Fernwood is **legacy** in this repo and **never "production"** — and neither word ever reaches a
   household surface.
6. **Completeness.** "Nothing else changed" is a promise only as true as the discipline behind it.
7. **The reader's reaction.** No *you'll love*, no *finally*, no *we're excited* — describe, don't grade.

---

## 2 · THE DRAFT ENTRY FOR THIS BUILD

⛔ Copy only. Not written to `RELEASE_NOTES.md`. Ships only after Paul's read **and** a walk.

```markdown
## 2026-09-10 — An account first, your home when you're ready

- **Signing up creates an account, and nothing else.** No home is waiting for you when
  you arrive, and nobody is handed one they did not create. An empty shelf on a new
  account is the ordinary state, not a sign that something went wrong.
- **The empty shelf has stopped saying two things that were not true.** It used to send
  you back to a link you had already used, and it used to name a home nobody had made.
  It does neither now.
- **Two questions during setup say more plainly what they are.** The interests question
  names things you actually do rather than categories to file yourself under, and the
  address question says what the address is not used for.
- **A home that has just been founded has no Garden Guru reading of it yet.** The Guru
  learns a place from that place's own record, and a new one has none to read. That
  will change as the record fills.
- **Not in this build:** inviting anyone, joining a house somebody else set up, or
  keeping a second home on the same account. None of the three are here yet.
```

**Held out — the candidate, and it is the one bullet that would be a lie today:**

> *"**Setting up your home from the address step now founds it** — one place, made by you, on your
> own account."* — ⛔ **being wired now.** It enters the note at the lap where a seat walks J0 at the
> deploy sha and passes, and not before.

### Provenance — what each bullet is owed

| bullet | committed row | link it derives from | class |
|---|---|---|---|
| account-only | *(id set at beat 6)* | L1 *done means* + a walked signup | do / no-longer |
| empty shelf | *(id)* | L1 *done means*; two removals, both walked | no-longer |
| two questions | *(id)* | L1 + `elicitation-lens` reading of the newest walk | no-longer |
| Guru has no reading yet | *(id)* | L1 — an honest limit, stated because §1d·6 forbids silence dressed as completeness | no-longer |
| not in this build | beat 6's excluded scope | L1 only — never re-decided here | not-yet |
| *(held) founding* | *(id)* | ⛔ **no walk exists** | candidate |

⚠️ Ids are blank because lap 5's committed rows carry none — that is exactly what P1 fixes.

---

## 3 · THE FALSIFIER

**a · The check, and it is the mirror of P4.** P4 asserts *presence*: a row naming a title has a
matching heading. Alone it cannot catch over-claiming. Add the other direction, which needs no new
data and parses no prose:

> **For every committed row with no passed `read-against-scope` line, assert its `note:` title does
> NOT appear as a `## <date> — <title>` heading in `RELEASE_NOTES.md`.**

⛔ **What it does not cover, on its own face:** it reads the **heading**, never the bullets. A note
with an honest title and an over-claiming fourth bullet passes green. It also cannot tell a true
claim from a false one — only whether a walk stands behind the item at all.

**b · The reader's falsifier, which is the one that catches (a)'s gap.** *Every do-bullet must be
followable by a household reader, in the app, using only the bullet.* A bullet that cannot be turned
into a journey stop is not a do-bullet — it belongs in no-longer or not-yet. This is deliberately the
same test the harness applies: **a do-bullet is an action list wearing prose.**

**c · The charter's own falsifier, and this build sits directly on it.** `Read the whole card aloud`
[2026-08-24]: the title is now **derived** and the bullets **authored** — the precise shape that
shipped *"what you wrote back changed"* over *"the radar stays where it is."* So: **read the title and
the first bullet as one sentence before every deploy.** If they disagree, the `note:` field is wrong —
never edit a bullet to make a derived title true.

**d · What would falsify the SHAPE.** Two consecutive laps whose notes carry **no do-bullet at all** —
then this log is a repair record, the do-move is ceremony, and the structure reverts to a plain list.

---

## 4 · ⛔ WHAT I DECLINE, AND OPEN QUESTIONS FOR PAUL

- **Which log an item lands in** (product vs. place) — the design's §5·1 contradiction. It is a content
  call and it is **Paul's**, not mine, until the engine log exists at all.
- **Version numbers** (`CYCLE-LOG.md:1636`). If versions land, the identifier is a version and `note:`
  should name it, not a title. **Do not build the field twice** — rule this before P2 ships.
- **Does this note ship at all this lap**, given the founding bullet is held out. A note of four
  no-longers and one not-yet is honest and thin. My read: **ship it** — thin and true beats padded,
  and §1d·6 forbids padding it with the candidate.
- **Two proposed principles, NOT written to the library** pending his word: *(i)* Fernwood charter —
  **a shared log is anchored in the reader's own record, not in a place** (§1d·4); *(ii)* candidate,
  cross-project — **a do-claim needs a walk behind it**: never claim a capability your own test never
  exercised. Second-project evidence not yet in hand.
