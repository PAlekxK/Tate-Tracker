# Saved-entries surface — naming pass

**Mode:** review (structured naming pass)
**Audience:** Mom (make-or-break user, low-attention morning/evening reading posture); Paul as secondary
**Surface:** the saved-entries view — currently the Field Notes card title, the Quick Capture label above the textbox, the card subtitle, and the intro line inside the card body
**Voice charter applied:** `~/.claude/content-principles/fernwood.md` (+ `cross-project.md`)
**Tone register:** observational, additive — the naming layer of the dashboard
**Could-be-anyone test:** "Field Notes" *passes voice* (field-journal-fluent) but **fails the anchor test** — see Finding 1.
**Anchor check:** see Finding 2.

---

## Recommendation: **"The Almanac"**

(Not "Almanac" bare; not "Field Notes." Read the rationale before the punch list.)

Use *"The Almanac"* for the card title and the dashboard-strip tile if one is added. Use *"Note or ask the slope"* (or current input-label copy) above the textbox — keep label-of-the-input distinct from name-of-the-collection. Reword the card subtitle so it doesn't compete.

This is one defensible pick among three live candidates. Tradeoffs are honest below.

---

## Rationale — threading the dual-frame identity

The dual-frame structure (`project_tate_tracker_tone.md`) is:
- **Voice = field journal.** The discipline. How the prose sounds.
- **Form = Appalachian Almanac.** The public genre. What the reader thinks they're reading.

The UI label for the saved-entries surface is **the public name of the collection.** It names *what the reader is opening*, not *what it sounds like to read*. By the charter's own decomposition, naming the surface for the voice (Field Notes) is a category error — voice is a property of prose, not a label for a noun. Naming the surface for the form (Almanac) matches the layer the label lives at.

The recent Property-card pass codified exactly this — "Anchored naming beats field-journal-fluent naming" (`fernwood.md`, 2026-05-20). "The Place Itself" was voice-fluent and not anchored; "Fernwood" named *the thing the card holds*. The Field Notes label is the same shape of miss:
- It describes the *register* the entries are written in, not *what the collection is*.
- It is voice-fluent in a way a thoughtful nature publication could have written without knowing this property — the could-be-anyone problem.
- It mirrors a Sand-County-Almanac-style **chapter heading** (e.g. "Field Notes from the Sand Counties"), not the work's title. The work's title is *Almanac*.

The locked subtitle already names the form: *"An Appalachian Almanac for Fernwood."* The card that holds the almanac entries should be called what the subtitle promises — otherwise the dashboard has a header advertising an almanac and a card holding "field notes," and the reader has to bridge that gap themselves. Mom (low-attention morning posture) will not bridge it; she will read each surface for what it says.

In short: **voice is the journal; the journal generates the almanac; the almanac is what's on the page.** The intro copy inside the card already says this verbatim — *"The journal generates the almanac."* The card title currently contradicts the copy inside it.

### Why "The" (definite article)

"Almanac" bare reads like a category or a feature name (a competitor: a Mailchimp campaign type). "The Almanac" is anchored to *this* dashboard — there is only one. It mirrors how the subtitle introduces it ("An Appalachian Almanac for…") and how a reader would refer to it in conversation ("did you see what was in the almanac today?"). Small, but matters at the Mom-half-engaged-reading bar.

### Why not bare "Almanac"

It collides with the subtitle's "Appalachian Almanac" without lifting any of its weight — and reads as a system-feature name rather than a place in the dashboard the reader goes.

### Why not keep "Field Notes"

- Fails the anchor test (Property-card precedent).
- Names the voice, not the form — the wrong identity layer for a surface label.
- Contradicts the card's own intro: *"The journal generates the almanac."*
- A field-journal voice can be expressed without the surface being labeled with the genre name. The white-pine guide doesn't say "Field Note: White Pine."

### Why not a third option (and which ones I considered)

- **"The Journal."** Names the voice cleanly. Same category error as Field Notes — names register, not collection. Also collides with "the journal" in the intro copy.
- **"The Year"** / **"The Year So Far."** Honors the almanac's cyclical structure; lovely at the Leopold level. Too poetic for a card title Mom scans at 7am; doesn't anchor.
- **"Entries"** / **"Saved Entries."** Productivity-app drift. Hard fail on charter.
- **"Notebook."** Same shape as "The Journal" — register, not collection.
- **"Fernwood Almanac."** Redundant with the header; the dashboard is already Fernwood and the subtitle is already Appalachian Almanac. Doubles a name the reader has on screen.

---

## Sense-check against adjacent surfaces

**Header subtitle:** *"An Appalachian Almanac for Fernwood."* "The Almanac" inside the dashboard pays this off — the subtitle promises one, the card delivers it. The two reinforce rather than collide; "An Appalachian Almanac" (subtitle) is the *introduction*, "The Almanac" (card) is the *thing*.

**Property card "Fernwood":** No collision. Fernwood is the place; the Almanac is the year-on-the-place. They sit at different layers — one names *where you are*, one names *what you're reading*. The dashboard now reads cleanly: this is Fernwood, here is its almanac.

**Quick Capture label "Field Notes" (line 2957) and Card title "Field Notes" (line 3164):** Both currently say the same thing on the same screen. Pull them apart in the rename: the input row is the *act* of writing; the card is the *collection*. Recommended: input label becomes *"Note or ask the slope"* (current unified-input copy on line 2988 already uses this — adopt it consistently when the unified-input fully replaces Quick Capture). Card becomes *"The Almanac."*

**Card subtitle, line 3165:** *"The journal you keep about this place"* — this is **good copy in the wrong place**. With "Field Notes" as the title, the subtitle was disambiguating ("our kind of field notes"). With "The Almanac" as the title, the subtitle should describe what the almanac *is*, not what the journal is. Suggested: *"A year of noticings — this place, this season, this month"* or simpler: *"What we've noticed here this year."* (Drafts, not locked. Worth a follow-up if you bundle.)

**Intro copy inside the card body, line 8920:** *"A place to set down what you saw this week — the first hummingbird at the feeder, the night the chorus started, the morning the laurel opened. The journal generates the almanac."* — This is excellent and self-explains the rename. Keep verbatim. With "The Almanac" as the card title, this intro lands as the answer to "what is this?" rather than a contradiction.

**"Empty" state, line 8938:** *"No entries yet. The first observation goes here."* — Reads fine under either name. No change needed.

**Filter chip "★ Starred":** Reads fine under "The Almanac." No change needed.

---

## Will it land for Mom?

The Mom-test (`persona-mom.md`): morning coffee in bed, half-engaged, looking for "something interesting to read while the day starts." Under that read posture:

- **"Field Notes"** — slightly utilitarian, slightly task-flavored ("notes I need to take"). Adequate, not inviting.
- **"The Almanac"** — has a leisure-reading register. Almanacs are *for* morning-coffee browsing — the *Old Farmer's Almanac* is the cultural reference even for people who've never read it. It tells Mom *what the surface is for*: a thing to read, organized by the year, anchored in the place. It lands the use mode the persona expects.
- Risk: "almanac" is slightly more bookish than "field notes." Some readers may need a second to translate. The intro copy ("a place to set down what you saw this week… the journal generates the almanac") does that translation in one sentence, and the header subtitle has been pre-loading the word since users opened the page.

Net: "The Almanac" matches Mom's reading posture better than "Field Notes" does, given the header subtitle is already cuing the word.

---

## Scope boundary — what's adjacent but not in this pass

Flagged so Paul can decide whether to bundle. Each is a real call, not a recommendation to act:

1. **Quick-capture label still reads "Field Notes" (line 2957)** while the unified-input section (line 2988) reads *"Note or ask the slope."* If the unified-input has replaced Quick Capture in production, the legacy "Field Notes" label is dead UI. If both are live, this is a consistency break worth a single decision.
2. **Card subtitle (line 3165) "The journal you keep about this place"** lands well under "Field Notes," lands less well under "The Almanac." Draft above; needs Paul's voice review if bundled.
3. **The unified-input label itself** — *"Note or ask the slope"* (line 2988) is interesting copy that wasn't in this brief. Doesn't need to change; just noting it as a related surface.
4. **Button label "Save entry" / "Save"** — out of scope here. "Save to the almanac" might be tempting after the rename; resist unless tested — it adds reading load on the most-used button.
5. **`Field Notes` mentioned in console-warns and code comments (lines 8655, 8664, 8965, 9061, 9248, 9466)** — engineering hygiene, not UI copy. Worth a follow-up sweep when the rename ships, but not a content-steward call.
6. **The card icon `📓` (notebook) on the card header** — still reads as journal/notebook. Under "The Almanac," a book icon `📖` or a calendar-leaning glyph might fit better. UX call, not a content call; ux-expert if you want it reviewed.
7. **The intro line *"The journal generates the almanac"*** — under the rename, this becomes a load-bearing line of copy that explains the dual-frame identity to a first-time reader in seven words. Keep, and consider whether the same line wants to appear *anywhere else* (e.g., a Garden Guru system-prompt context line so the assistant knows the surface name). Out of scope for the rename itself.

---

## Open questions for Paul

- Is the Quick-Capture section (line 2955) still live in production, or has the unified-input section (line 2987) fully replaced it? If unified-input has replaced it, the cleanup pass noted in `project_fernwood_almanac_save_model.md` becomes part of this rename's blast radius and the answer simplifies (rename one place, not two).
- Card subtitle rewrite — bundle into this pass or hold for a separate review? If bundled, I'll draft 2–3 options for your pick.
- Does *"the slope"* (in *"Note or ask the slope"*) want a content review of its own? It's distinctive and I like it; it also wasn't in this brief.

---

## Principles to propose (post-confirmation)

- **`fernwood.md` — add an example to "Anchored naming beats field-journal-fluent naming":** "Field Notes → The Almanac" as a second worked example alongside "The Place Itself → Fernwood." Strengthens the principle, gives content-steward a paired pattern (voice-fluent name → form-anchored name) for future surfaces.
- **Candidate — promote "Anchored naming beats field-journal-fluent naming" toward cross-project.** The principle was held in `fernwood.md` "pending a second confirming example from Bolo Boys (or other future project naming work)." This rename is a *second Fernwood example*, not a second-project example, so the promotion gate isn't met. But the pattern is now twice-confirmed within Fernwood — note the strengthening when the Bolo Boys naming pass eventually runs.

---

## Maintenance

- **Reviewer:** content-steward
- **Date:** 2026-05-21
- **Status:** recommendation pending Paul's confirmation; no UI changes proposed in this artifact

---

## Bundled rename — exact strings + line refs

**Confirmed scope (per Paul, 2026-05-21):**
- Legacy `#quick-capture` (line 2957) and standalone `#garden-guru` (line 2968+) are dead UI scheduled for removal in the next cleanup pass — **not touched here**.
- The rename touches the live unified-input surface and the main "Field Notes" card.
- Card subtitle rewrite is bundled.

Paul approves exact strings before any Edit touches viewer.html.

### 1. Card title — line 3164

- **File:** `viewer.html`
- **Old:** `<div class="main-card-title">Field Notes</div>`
- **New:** `<div class="main-card-title">The Almanac</div>`
- **Why:** Names the form (Almanac) rather than the voice (Field Notes); resolves the title-contradicts-its-own-intro problem documented in the review.

### 2. Card subtitle — line 3165

- **File:** `viewer.html`
- **Old:** `<div class="main-card-summary" id="fieldnotes-summary">The journal you keep about this place</div>`
- **New (recommended):** `<div class="main-card-summary" id="fieldnotes-summary">What we've noticed here this year</div>`
- **Why:** With "The Almanac" as the title, the subtitle should orient the reader to *what the almanac holds*, not *what the journal is.* See draft rationale below.

#### Subtitle draft — rationale + alternatives

The subtitle's job (unchanged from before): tell a first-time reader, in one line, what this card *is*.

Under "Field Notes," "The journal you keep about this place" was disambiguating the genre — *our* kind of field notes are personal, place-specific, journal-flavored. It worked because the title named the voice and the subtitle resolved the voice's ambiguity.

Under "The Almanac," the subtitle has a different job. The title now names the form. The subtitle should name *the contents under that form* — what's been gathered. The dual-frame logic ("voice = field journal; form = almanac") says the almanac is *what a year of journal entries adds up to*: a record of what's been noticed on this slope across the seasons.

Three drafts in priority order:

1. **"What we've noticed here this year"** *(recommended)*
   - Anchored ("here," "this year"); plural-collective ("we"); observational verb ("noticed") that matches the field-journal voice and the existing intro copy ("A place to set down what you saw this week…"). Mom-readable at 7am. Pays off the header subtitle's "Appalachian Almanac for Fernwood" by saying, more plainly, what that almanac contains.

2. **"A year of noticings — this place, this season, this month"**
   - More literary; mirrors the calendar layering an almanac actually has. Slightly longer; the em-dash list reads well in serif but may feel decorative for a one-line subtitle Mom skims. Hold as a fallback if the recommended draft reads under-stated.

3. **"The year, as we've watched it"**
   - Closest to a Sand County Almanac-register rhythm. Risk: leans poetic enough that a first-time reader might not parse it as "what this card holds" — voice-fluent but possibly under-clear at the orient-the-reader level the subtitle exists to do. Hold unless Paul wants more literary register.

### 3. Intro line inside the card body — line 8920

- **File:** `viewer.html`
- **Current:** `'<div class="fn-intro">A place to set down what you saw this week — the first hummingbird at the feeder, the night the chorus started, the morning the laurel opened. The journal generates the almanac.</div>';`
- **Recommendation:** **Keep verbatim. No change.**
- **Why:** Title-says-it-now logic *does not* obviate this line. The opposite — with "The Almanac" as the title, this intro becomes the load-bearing sentence that explains the dual-frame identity to a first-time reader. Removing or shortening it would leave a reader who doesn't already know the model with no on-page explanation of why the card showing their entries is called an almanac. The closing sentence ("The journal generates the almanac") is the single most efficient line of copy on the surface for teaching the model. Keep.

### 4. JS fallback summary string — line 8910

- **File:** `viewer.html`
- **Old:** `summaryText = "The journal you keep about this place";`
- **New:** `summaryText = "What we've noticed here this year";`
- **Why:** This string populates `#fieldnotes-summary` dynamically when there are no entries yet (it's the empty-state version of the subtitle on line 3165). Must stay in sync with the static markup or the card will revert to the old subtitle the moment it renders.

---

### Items NOT bundled in this pass

Flagged so Paul can sanity-check the scope boundary:

- **Icon `📓` (line 3162) on the card header** — still reads as journal/notebook, which is *correct* under the dual-frame logic (the voice is still field journal; the journal is still what generates the almanac). A book or calendar glyph could fit "The Almanac" more literally but would push toward naming the form twice (title + icon) and drop the voice cue. UX call, not a content call; defer to ux-expert if reviewed.
- **JS comments and `console.warn` strings (lines 8655, 8664, 8965, 9061, 9248, 9466) referencing "Field Notes"** — engineering hygiene, not user-facing copy. Sweep when the rename ships; not a content-steward call.
- **Button labels ("Save", "Ask Garden Guru" on the unified input; "Set up sync" / "Sync settings" on the in-body banner; "Start fresh")** — none change under the rename. "Save to the almanac" was considered and rejected in the original review (adds reading load on the most-used button).
- **Star-filter chip ("★ Starred" on line 8932) and All filter chip** — both read fine under "The Almanac." No change.
- **Empty-state line 8938 ("No entries yet. The first observation goes here.")** — reads fine under either title. No change.
- **Unified-input label "Note or ask the slope" (line 2988)** — distinct surface (the *act* of writing). Stays as-is; the original review noted it as a separate surface worth its own review later, not part of this rename.
- **Legacy `#quick-capture` (line 2957) and `#garden-guru` (line 2968+) strings** — out of scope per Paul; removed wholesale in the cleanup pass.
- **Header subtitle "An Appalachian Almanac for Fernwood"** — no change. "The Almanac" pays this off; the two reinforce.

The blast radius of this rename is therefore four strings on three lines (3164, 3165, 8910) plus one intro line *intentionally* left unchanged because it's load-bearing under the new title.
