# Two-pass review pilot — fresh eyes + doctrine pass (2026-08-03)

Pilot of the process Paul described 2026-08-03: *"a fresh-eyes review, and then another review
with all of our design principles held in mind… what are some easy fixes that really make it
look intentional rather than like it's just been scrambled around."*

- **Pass 1 — fresh eyes**: un-primed general agent, world-class-consumer-app calibration, zero
  project context, browsing the live app (localhost:8765 serving working tree, md5-verified) at
  390×844 via Playwright. Told only who the reader is. Hard rule: no submits/answers (live backend).
- **Pass 2 — doctrine pass**: second agent loaded with `~/.claude/design-principles/fernwood.md`
  + cross-project libraries, re-verified pass 1's claims against the live DOM, adjudicated each
  finding (violation / deliberate-per-doctrine / needs-Paul), added coherence findings, produced
  the intentionality punch list.

**Process verdict:** worked. Fresh eyes independently flagged the Mama's Perspective heaviness
(carousel behind 6px dots, duplicate "Write me back", 9-line ack) and the feedback-ribbon overlap
— both things Paul had just raised — plus a trust-blocker nobody was looking at (internal agent
notes rendering on the Machines card). The doctrine pass earned its keep in BOTH directions:
it killed two false positives (the "35,007px page" was the reviewer's own all-expanded state;
the scroll-yank did not reproduce over 32s of monitoring) and it re-classified the strip↔card
"duplication bug" as the Paul-ratified "Strip teases, card holds" contract. An un-adjudicated
fresh-eyes report would have sent us re-litigating settled doctrine.

**Also confirmed by direct code read (main session):** the Save-button shrink Paul reported is
`body.fab-extended .ui-action-row { margin-right: 58px }` (viewer.html:4674) composing with the
ribbon's collapse-at-24px rule (viewer.html:11509-11527) — Save measured 278px→336px across the
first inch of scroll. And the FN_STORAGE_KEY TDZ bug is real: `renderVehicles()` at init calls
`fnLoadAll()` (viewer.html:16801) before the `const` at :16782 evaluates → 16 caught
ReferenceErrors, vehicle field notes silently never render.

---

## Pass 1 — fresh-eyes report (verbatim)

**1. Internal working notes and AI-verification metadata leak into the Machines card — severity: blocker (for trust)**
The 2016 VW GTI entry renders a wall of italic small print that is clearly an internal maintenance/agent log, not reader copy: "Purchased 4/1/2021 from CarMax Roswell… (Paul-confirmed 7/23; the lien-release letters date it by June 2021). Date/mileage are scan reads off the purchase packet; full detail in private records", "see the .research/2026-07-08 plan", "(see serviceHistory)". The 2006 F-150 shows, verbatim, *"STX (read off a body badge/VIN in the ChatGPT mine, 2026-07-22 — model-read, verify)"*. To a first-time reader this is incomprehensible, and reads like the app is broken or showing someone else's notes.

**2. Developer test data displayed as real content in the Almanac — severity: major**
Entries "July 30 — updated from a different device" and "July 30 — local stamp test", each with a red "Delete" link; "LOCAL ONLY" pill on the header. [Pass 2: the entries are the reviewing browser's own localStorage, not shipped content; the pill/CTA/Delete chrome IS shipped.]

**3. Badge/name layout collision breaks the Wildlife lists — severity: major**
Status badges overlay and clip species names ("Eastern Chipmunk" covered by "Year-round resident (less active in deep winte"); bird names truncate at ~11 characters ("Ruby-throated Hummingbi…").

**4. The page is the same content twice, in two different systems — severity: major**
Glance card set (›) + full card set (Open ▼) below a photo band; sets don't match (Machines only in glance set; Fairway/Weeds only in full set); "Fernwood Almanac" appears three times on one page. [Pass 2: duplication itself is the ratified strip/card contract; the set mismatch and one-name-three-doors stand.]

**5. No navigation once you're in — severity: major**
Tab strip is position:static and scrolls away; page measured 35,007px with cards expanded; Close only at card top; tab list doesn't match page sections. [Pass 2: 35,007px was the reviewer's own all-expanded state — ~4,600px as landed; jump-strip incompleteness/order and no bottom-Close stand.]

**6. Scroll position yanked mid-read — severity: major**
scrollY 1400 → 188 ~30s after load. [Pass 2: did NOT reproduce over 32s of monitoring; likely the reviewer's own expandCard auto-scroll. Needs-Paul: has he/Mom ever felt it? Instrument before fixing.]

**7. Time and unit formats inconsistent everywhere — severity: major**
"20:37" (Sky) vs "7:53 PM" (Fishing); within one Fishing card "07:08/20:28" two lines from "7:53 PM–8:33 PM"; "29.66 inHg" vs "1004 HPA"; "43 km vis" on a °F app; "in 10d".

**8. Developer/sync plumbing one tap from Mom's surface — severity: major**
Sync modal: device ID, Worker URL placeholder "tate-tracker.your-subdomain…", "paste the SHARED_TOKEN value", "worker/README.md"; footer "build 2026-05-28 — KV-direct + honest chip".

**9. Real JavaScript errors silently break vehicle almanac notes — severity: major**
16× "Cannot access 'FN_STORAGE_KEY' before initialization" from fnLoadAll via renderVehicleItem — per-vehicle notes silently fail.

**10. Jargon density in Weather / Sky / Fishing details — severity: minor (cumulatively major)**
"8th percentile" rainfall tiles, "mag/arcsec²", "Clouds: 54% lo / 0% mid / 0% hi", unlabeled rain-chance %, fishing ●●● with no legend at the glance.

**11. Mama's Perspective: warm idea, heavy execution — severity: minor**
9-line justified ack with three inline link-buttons of unguessable behavior; "Got it"+"Write me back"; second block with four more buttons (duplicate "Write me back"); carousel of 5 questions behind tiny ‹ › + 6px dots (4 of 5 invisible). Praised: the question pattern itself (property photo + "Yes, it has the stripe") — "best-in-class inclusive design."

**12. Fishing forecast credibility — severity: minor**
All 8 windows "●●● Prime"; Tue/Wed/Thu/Sun non-chronological; "0 mph NNE · light chop"; bespoke blue/slate visual language.

**13. Chip and emoji typography glitches — severity: minor**
"Inspect" chip breaks across lines (🔍 orphaned); emoji flush against text ("☁️Tonight:"); Ovenbird (a bird) in the Plants card's worth-noticing list.

**14. Repetitive template copy — severity: minor**
Three consecutive "If you've thought about cuttings from the {X}, this is the window"; White Pine paragraph states drought-tolerance twice.

**15. Floating "General feedback" bubble covers content — severity: minor**
Hid "2.14\" next 7d" and mid-paragraph words; worse with A+ text.

**16. Long italic passages vs the accessibility goal — severity: minor**
Land·Sky·History ~10-line italic serif; map labels pile into an unreadable clump; "+ Add a place" edit button on a read-mostly surface.

**17. Inconsistent row furniture in Plants By-Species — polish**
Some photos, some none; ~9px gray Latin names; six levels of nesting on a phone.

**18. Sky & Stars — polish**
Event titles truncate; "severe/significant/moderate" moon-interference jargon; "in 10d/63d/133d".

**What genuinely works:** the voice where it's the real product ("It grows by a day, every day"); the Mama's Perspective question pattern; the A/A+ control; plain-language action lines on glance cards; the NASA moon photo and the Bronco's told-as-a-story history.

**Gut read:** "There is a lovely, coherent product inside this page… but a first-time visitor doesn't meet that product… It currently feels like a very good private notebook that a very capable engineer keeps for himself, with the family-facing veneer applied unevenly on top. The fix is less about adding polish than about subtracting: one structure instead of two, one clock, one register, and a hard wall between what the reader sees and what the operator (and his agents) know."

---

## Pass 2 — doctrine-pass adjudication + punch list (verbatim)

### A. Adjudication

| # | Verdict | Key adjudication |
|---|---------|------------------|
| 1 | CONFIRMED-VIOLATION | Tone-coherence (canon-track) + half-engagement. NOT excused by provenance-honesty — doctrine already owns the right artifact (confidence chips); provenance is a visual property, not a prose dump. |
| 2 | PARTLY | Test entries = reviewer's own localStorage. Shipped: caps "LOCAL ONLY" pill, "Set up sync" CTA, red Delete links → Tone-coherence violation. |
| 3 | CONFIRMED-VIOLATION | Half-engagement + no-glasses reader model. |
| 4 | PARTLY — mostly DELIBERATE | Strip↔card duplication = Paul-ratified "Strip teases, card holds" (F12 answer). Stands: Fairway/Weeds missing strip leads; "Fernwood Almanac" one-name-three-doors. Machines-in-Reference-drawer is IA-deliberate (glance/repository). |
| 5 | PARTLY | 35,007px = reviewer's own state (~4,600px as landed). Stands: jump strip incomplete + order matches neither page nor stable dimension (Menu-order-is-a-place, paul-ratified); no bottom Close on long cards (Friction kills). |
| 6 | NEEDS-PAUL / not reproduced | 32s monitor at y=1400: zero movement. Ask Paul/Mom if ever felt; instrument, don't fix blind. |
| 7 | CONFIRMED-VIOLATION | Consistency>precision (paul-stated), One-engine-one-verdict (canon; two formatters over one station read). Note 20:28 vs 20:37 sunset is NOT a bug — terrain-corrected, well-explained. Clock format only. |
| 8 | CONFIRMED-VIOLATION | Tone-coherence; "privacy is light" doesn't make dev plumbing Mom-facing. One admin flag gates all of it. |
| 9 | CONFIRMED-VIOLATION | Reproduced. TDZ ordering bug. |
| 10 | PARTLY | Glance-layer jargon violates Glossary-coverage-is-not-readability (paul-ratified); deep-card spec rows legitimized by Register-carried-by-chrome (candidate). Card HAS a dot legend; gap is at the glance. |
| 11 | CONFIRMED-VIOLATION | Core question pattern is doctrine-correct 3× over — keep untouched. Rest: see (b). |
| 12 | CONFIRMED-VIOLATION | Verdict engine that never says No fails provenance-honesty (paul-stated); "0 mph NNE" nonsense copy; bespoke tile tint violates One-shell-one-signal. Engine fix ≠ punch-list-sized. |
| 13 | CONFIRMED-VIOLATION | Icons-earn-their-place (canon); Ovenbird-in-Plants violates structure-fit candidate. |
| 14 | CONFIRMED-VIOLATION | Lead-with-synthesis (canon). |
| 15 | CONFIRMED-VIOLATION | Shipped control is a chat bubble with speech-balloon glyph — violates its OWN authorizing candidate (bookmark-ribbon-not-chat-FAB). Its Material-FAB behavior directly causes owner item (a). |
| 16 | PARTLY | Vehicle italics → fix with 1. Land·Sky·History italics = deliberate journal voice, A+ is the valve. Map clump + "+ Add a place" = real; gate the latter with 8's admin flag. |
| 17 | CONFIRMED-VIOLATION (polish) | One-shell-one-signal. |
| 18 | CONFIRMED-VIOLATION (minor) | "Severe" = monitoring vocabulary; the glyph fix (traffic lights→★) already rebuilt this lexicon once, the severity WORDS survived it. |
| (a) Save-button shrink | CONFIRMED-VIOLATION | Measured 278→336px across first inch of scroll. Friction-kills + form-excellence. "The poster child of locally-good patches composing into scrambled." |
| (b) Mama's card | CONFIRMED-VIOLATION (core deliberate) | 1,257px, four jobs at once. Receipt-vs-consequence, One-shell-one-signal (3 dark commit buttons), loop-close-at-glance, Pick-the-object (dots+arrows = a queue with a denominator). Preserve the question pattern + ✓/× grammar. Pushes the ratified landing strip to y≈1,800. |

### B. Coherence findings the cold pass missed
1. **Weather tile/card register inversion** — tile reads "67°F · Mainly clear · H 71° / L 62°" (the half-engagement canon's literal worked example of failure) while the journal pull ("Muggy morning — heavy air, slow to dry") sits down on the card. Cheapest coherence win: tile consumes the card's sentence.
2. **Provenance grammar fragmenting** — Weather's ratified source tags vs Fishing's "MEASURED" caps vs Almanac's "LOCAL ONLY" vs Machines' parenthetical prose. Four vocabularies for one concept.
3. **Ribbon contradicts its authorizing candidate** (chat bubble vs bookmark ribbon) — one decision resolves (a), 15, and the register leak.
4. **"worth handling (Paul) · emissions first"** — assignee annotation on Mom's surface.
5. **Caps-chip drift re-accreting** — "7 ITEMS", "LOCAL ONLY", "MEASURED".
6. **"Fernwood Almanac" one-name-three-doors** (write-composer vs look-back tile vs card).
7. **Mixed disclosure-caret conventions** between input-stack cards and main cards.

### C. Intentionality punch list (ranked by intentionality-restored-per-effort)
1. Freeze Save geometry: ribbon always-slim on phones; delete `body.fab-extended` + 58px clearance (viewer.html:4674, :11519-11522). → resolves (a), most of 15
2. One clock: 12h AM/PM everywhere (Sky tile, Fishing sun row). → 7
3. One pressure: Fishing consumes Weather's formatter + source tag; delete "1004 HPA · MEASURED". → 7, part of 12
4. Strip curator notes from Machines render (parentheticals → non-rendered fields; keep confidence chips). → 1, part of 16
5. Admin flag: hide Set-up-sync, LOCAL ONLY, Delete links, build footer, "+ Add a place" behind a localStorage maintainer flag. → 2, 8, part of 16
6. Fix FN_STORAGE_KEY TDZ (declare before first caller). → 9
7. Weather tile lead = the card's sentence; H/L stays on card. → B1, part of 10
8. Shrink Mama's ack to a folded receipt (one line + "Look back ›"); one "Write me back" per card. → half of 11/(b)
9. Kill carousel furniture: one question + "Another question ›" link instead of dots+arrows. → rest of 11/(b)
10. Emoji spacing + chip nowrap pass; wildlife badge wrap CSS. → 13, 3
11. Synthesize the triple cutting-window line. → 14
12. De-alarm sweep: "severe"→"washes it out"; "0 mph NNE · light chop"→"calm · light chop"; "in 10d"→"in 10 days". → 18, parts of 12/10
13. Un-tint the Fishing tile. → 12's register note
14. Jump strip = page order, complete; bottom "Close" on long cards. → 5's residue
15. Rename the composer header (e.g. "Set something down") so "Fernwood Almanac" names only reading surfaces. → 4's residue, B6

Not punch-list-sized (→ backlog): the fishing verdict engine that never says No; the Mama's-card default-collapse decision.

### D. Ratified-principle conflicts for Paul — ADJUDICATED `[paul-stated 2026-08-03]`
1. **Teaching label vs stable geometry** (the ribbon) — **Paul's call: the chat bubble stays exactly as-is** (extended at top, slim on scroll), and a momentary cover-up of content is acceptable — *"it seems more natural in a way when there is a little cover up in the moment of the scroll… we can expect that people understand the relationship between the two objects."* This REVERSES pass 2's always-slim recommendation and the bookmark-ribbon-not-chat-bubble candidate's read of this control — do not re-propose slimming it. Consequence shipped same day: the 58px `fab-extended` clearance was deleted (viewer.html ~4663), so the Save button keeps one geometry at every scroll position — which was the original complaint. Verified live at 390×844: button constant at 336px through a scroll cycle, and the extended ribbon no longer overlaps the Save button at rest anyway (button bottom y=500 vs ribbon top y=691 — the clearance was guarding an overlap the 8/02 IA reorder had already dissolved).
2. **Machine status chrome** — **skipped, leave as-is; revisit in the future.** Not adjudicated; the amber status chip stays.
3. **Mama's-card default-collapse / strip altitude** — **parked as a question to explore later.** The jump-strip tabs cover navigation for now, and Paul's posture: *"let's not do too much more before getting mom's feedback at this point."* Punch-list items 8–9 (ack shrink, carousel rework) and the rest of the list are HELD behind that same gate — Mom's feedback comes first.
