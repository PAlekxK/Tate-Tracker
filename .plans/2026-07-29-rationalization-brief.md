# Shared brief — Fernwood backlog rationalization (2026-07-29)

**Read this first. It is the same for every expert seat on this panel.**

## What Paul commissioned

Two things, and they are one job:

1. **The full backlog rationalization** (`BACKLOG.md` TOP ITEM, 2026-07-28) — the file has grown to ~550
   lines / ~156 table rows across three tracks. It is an excellent *decision record* and a broken
   *priority list*. The `▶️ NEXT` table contains two colliding numbered lists and its #1 has shipped.
2. **The axis to re-cut on** (`BACKLOG.md`, 2026-07-29, Paul-stated) — see below.

Paul's instruction for this run: *"involve our team of experts and do some external research on best
practices for each expert's specific area of focus."* So each seat brings **outside evidence**, not
just a read of the repo.

## THE AXIS — Paul's disposition tiers (this is the deliverable's spine)

Every finding you produce gets **exactly one tier**, and the tier is defined by **what unblocks it**:

| Tier | Unblocked by |
|---|---|
| **1 · FIX NOW** | Nothing. Just do it. (font, size, alignment, spacing, a wrong number) |
| **2 · CONFIRMED** | An answer Mom (or Paul) has **already given** — build it |
| **3 · STEER** | A question **not yet asked** |

**⭐ THE LOAD-BEARING RULE: a Tier-3 finding is INCOMPLETE until it names two more things:**
- ① **the exact question to ask** (write the words), and
- ② **how the answer gets captured** — which surface, which channel, how it comes back into the record.

A Tier-3 row with no askable question and no capture path is a row nobody can ever start — say so, and
it goes on the **kill list**. Producing a kill list is a *successful* outcome, not a failure.

## ⭐⭐ THE ORIENTING PRINCIPLE — steer on HER signal, and clean the instrument first (Paul, 2026-07-29)

Added mid-run, and it governs every seat. Two clauses.

**① Orient around her feedback — explicit AND behavioural. Standing, from now on.** Paul: *"let's always
orient around her feedback, be that explicit — like taps on yes or no or free response — or just how
she's clearly using the app, what she's looking at, what she's not."* Both halves count as evidence:

- **Explicit** — confirm taps, free-response notes, Guru questions, zone audio, and anything Paul relays.
- **Behavioural** — card expansions, which cards she opens and which she never does, session counts,
  what she returns to. (`card_expanded` 4× in 30 days vs Paul's 47; the Almanac is the most-opened card
  at 41 of 139 expansions — that is *her* telling us something without answering anything.)

Consequence for your findings: **a recommendation that cites neither an explicit input nor a
behavioural signal is a weaker class of evidence, and must say so.** Don't launder a design opinion as
a user finding. Paul's read is that engagement is up and that trend is the thing to keep relying on.

**② The UX cleanup is MEASUREMENT HYGIENE, not polish — and that is why it goes first.** Paul: *"what's
gonna be key to that is cleaning up the UX… especially where we ask for her input, to make it clearer
to her what's going on. Right now it's a little confusing, so it introduces some noise into the
feedback data that she provides us and the usage data."*

Read that literally: **the confusing input stack is contaminating the instrument we steer by.** Five
stacked input surfaces at 390px (ack ribbon w/ Got it + Write back → photo/mic composer → "Save & ask
the Almanac" → the Mama's Perspective card → the floating General-feedback tab that *overlaps the card
text*) means we cannot currently distinguish:

- *she declined this ask* from *she never understood which thing she was answering*;
- *she doesn't want this surface* from *she couldn't tell it apart from the one 120px above it*;
- a tap that means **yes** from a tap that means **whatever this box is, I'll type here**.

Every engagement number in this project — the 33/33 declined carousel, the confirm funnel, the launcher
taps — was measured through that noise. **So the target state Paul names is: it is unambiguous to her
what is happening, what she is giving feedback ON, and what she is interacting with.** Clarity is the
prerequisite for trusting any subsequent measurement.

**How this reorders the work:** anything that *cleans the input stack* is worth more than anything that
*adds a new ask*, because the second is unmeasurable until the first lands. If your lens produces a
finding that adds a surface, state what it costs in measurement clarity. If two findings tie, the one
that disambiguates a surface wins.

## Hard constraints

- **⚠️ MOBILE FIRST.** Paul, 2026-07-29: *"that's our primary interaction source."* Anything UI is
  judged at **390×844**, not desktop.
- **The reader is Mom.** She reads with difficulty. Meaning must arrive via icon + size + colour +
  position, never colour alone, never a label doing all the work.
- **Tone: field journal, not task manager.** No "3 alerts", no "17 actions due", no deadline grammar.
- **The AI boundary** (`CLAUDE.md` → "The AI boundary"): AI never touches Mom's surface or Mom's words.
  Egress — anything reaching her is human-confirmed. Ingress — **an agent does not fetch her words**;
  Paul relays. Quarantine — model output derived from her words *about herself* stays in `.private/`.
- **Capture stays deterministic and AI-free.** AI lives on the ask path only.
- **The repo is PUBLIC.** Never quote Mom's private wording into a tracked file. Reference
  `.private/mom-feedback-2026-07-26.md`; do not copy from it.
- **Trust is the load-bearing emotion.** A confidently-wrong record is worse than an honestly-unsure one.
- **Capture is not a loop** — a channel does not ship until an item arriving on it can be *surfaced,
  protected from the watermark, and closed*.
- **Defer affordances pending signal** — don't propose a new surface without naming the signal that
  earned it.

## What you must NOT do

- **Do not edit `BACKLOG.md`.** The main session composes the single rationalized file. You write a
  report; you do not merge it.
- **Do not write to Mom-facing files** (`viewer.html`, `questions.json`) — this run is diagnosis and
  ordering, not building.
- **Do not trust a backlog row's status.** Several rows describe shipped work as open. Verify against
  git and the code before asserting anything is open.
- **Do not import a best practice that Fernwood's own doctrine already beats.** Where the outside
  literature disagrees with this project's ratified calls, say so explicitly and defend the local call
  or argue against it — but name the conflict rather than silently applying the generic advice.

## External research — required, and how to spend it

Search current (2025–2026) best practice **in your own lane**. For each source, note what it changes
about a specific Fernwood row. Three failure modes to avoid: generic listicles; enterprise-scale advice
applied to a two-user hobby app; and "here's what the literature says" with no row it touches.

## Ground truth sources (in precedence order)

1. **git HEAD + the code** (`viewer.html`, `worker/worker.js`, `tools/*.py`) — the only real status.
2. **`CLAUDE.md`** — ratified doctrine, the loop spec, the taxonomy rule.
3. **`BACKLOG.md`** — the decision record (read for *why*; distrust the *status*).
4. Prior panel reports in `.ux-reviews/`, `.user-research/`, `.engineering/`, `.ai-advisor/`,
   `.content-reviews/`.

Repo: `~/Developer/Tate-Tracker`. Live app: `viewer.html` served on GitHub Pages.

## The two products (keep the boundary; the tiers layer over it)

- **Track A — Mom's field journal.** Mom-facing, field-journal tone, plants/wildlife/weather/map.
- **Track B — Paul's fleet & equipment tracker.** Paul-facing, utilitarian, the only deadline-bearing work.
- **Track C — cross-cutting infra/doctrine.**

They have never been ranked against each other and they compete for the same hours. If your lens has a
view on that ranking, give it.

## Your report

Write to your own directory as `2026-07-29-backlog-rationalization-<lens>.md`. Structure:

1. **Tiered findings table** — one row per finding: tier, one-line claim, the specific backlog row or
   file:line it touches, effort (S/M/L), and for Tier 3 the **question** + the **capture path**.
2. **Kill list** — rows in your lane that should not be done at all, with the reason.
3. **Status corrections** — anything `BACKLOG.md` says is open that you verified is shipped, or vice
   versa, with the commit or file:line that proves it.
4. **External research** — sources, and per source the row it changes.
5. **Sequencing view** — if these were done in order, what order, and why.
6. **What you could not determine** — and what would settle it.

Then return a compact summary to the main session (the report file is the detail; the return is the
decision-grade digest).
