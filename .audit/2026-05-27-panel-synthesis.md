# Fernwood — Panel Synthesis, 2026-05-27

Five-expert audit (ux-expert, engineering-partner, ai-advisor, content-steward, user-researcher) anchored on the 5/26 telemetry rollup. This file reconciles findings into one prioritized list.

**Source artifacts:**
- `.ux-reviews/2026-05-27-portfolio-audit.json` (10 findings)
- `.engineering/2026-05-27-portfolio-audit.json` (8 findings)
- `.ai-advisor/2026-05-27-research-incorporation.md` (8 directions)
- `.content-reviews/2026-05-27-portfolio-audit.json` (12 findings)
- `.user-research/persona-mom.md` + `.user-research/jtbd-2026-05-27.md`

---

## Strong convergence — what the panel agrees on

### 1. Kill the star (⭐). Promote revisit-frequency as the implicit signal.

**Three agents converged independently:** ai-advisor, ux-expert, user-researcher.

- Data: 0 stars across 104 entry_revisits in 6 days. Mom has 55 revisits, 0 stars. Decisive.
- The assumed "tap to curate" pattern doesn't exist as Mom-or-Paul behavior. The actual curation signal is already running: revisit ratio ~17:1.
- **Action:** Remove ☆ from entry headers + "★ Starred (0)" filter chip. Keep `isStarred` field for backward compat. Replace the filter with a "Most revisited" sort on the Almanac view.
- **Downstream:** The 🚩 meta-feedback affordance promotion gate (per `project_fernwood_almanac_save_model.md`) doesn't unlock either. Clean answer per `feedback_defer_affordances_pending_signal`. The T+30 Mom interview asks "what mattered most" — that answers the decoder question (invisible vs. wrong model vs. redundant) without needing to keep the UI.

### 2. Research and info land as inline depth inside high-engagement cards — not as new cards.

**ux-expert + ai-advisor converged**, with content-steward providing the voice principle.

- Plants and Weather get 60 views each. Worth Considering gets 5. Mom hasn't shown she opens new cards readily.
- The right pattern: **richer content goes inside the cards Mom already opens.** "Last year on this slope," "you noted X last spring," "laurels were peak that week."
- New cards are an option only when (a) the content can't fit inside an existing card and (b) Mom has shown a job that wants its own surface.
- Content-steward's pairing principle: *research deepens the data layer; voice governs the prose wrap.* As much research as the almanac warrants — but the prose wrap stays property-anchored.

### 3. The Garden Guru photo flow is broken in a way that explains the telemetry — not just stylistically off.

**Engineering F1 is the load-bearing finding.** `viewer.html:10148-10149` accepts only `kind === "plant" || "animal"`. Garden Guru's system prompt emits specific animal kinds (`mammal`, `bird`, `amphibian`, etc.). Animal photos drop silently — no buttons, just prose.

- This is probably the real cause of the "4 image_attached vs 3 species_id_confirmed" gap.
- "Black Bear correctly skipped because already canonical" in CLAUDE.md is likely wrong — the fence dropped it client-side, not server-dedup'd.
- Also probably explains why Step A "Not quite" / Step B "Skip this one" branches haven't been exercised.

**One-line fix at the kind check, plus `console.warn` for future drift.**

**Validation gate:** pull the 5/22 Black Bear conversation from KV (`wrangler kv key get conversation:<id>`) and check whether the prose contains an unparsed `<!--suggest-species kind: "mammal" ... -->` comment. If yes, F1 confirmed.

---

## The "do these this week" punch list (S-effort, high-leverage)

In order:

| # | Item | Source | Effort |
|---|---|---|---|
| 1 | **Suggest-species kind fence fix** — accept all 5 emitted kinds (`plant`, `animal`, `mammal`, `bird`, `amphibian`, plus the others in Garden Guru's prompt) at `viewer.html:10148-10149`; add `console.warn` on drop | eng F1 | S |
| 2 | **iOS `session_end` reliability** — call `fireSessionEnd()` inside MetricsCollector's `visibilitychange→hidden` handler after `flushSync()`. `sessionEndFired` already guards double-fire | eng F2 | S |
| 3 | **Garden Guru system prompt community name** — `worker/worker.js:452` "Mesic Cove / Montane Oak mosaic" → "Cove Forest + Low-to-Mid Elevation Oak Forest" (matches CLAUDE.md + candidates.json). Requires worker redeploy | content F1 | S |
| 4 | **Star retirement** — remove ☆ from entry headers + filter chip; replace with "Most revisited" sort | convergent | S–M |
| 5 | **Sources card editorial pass** — content-steward identified ~10-12 specific lines with proposed rewrites in `.content-reviews/2026-05-27-portfolio-audit.json` F6 | content F6 | S |
| 6 | **Worth Considering voice pass** — rewrite the 5 Mt. Cuba cultivar entries + autumn bentgrass to lead with property fit, citation second. Drop "Flagged for inclusion by Mom" prose (badge does that job) | content F3, F2 | S |

Validate F1 first by checking the 5/22 KV conversation; that confirms the diagnosis before the fix.

---

## Paul-decisions queued (these gate larger work)

### D1. Worth Considering — Mom-facing or Paul-only?

ux-expert F1: placement says Paul-only (between Recent Updates and Sources, no strip tile, 5 views), but "Mom's pick" badge says Mom-facing. Pick one:
- **Mom-facing:** give it a strip tile alongside Plants/Weather/etc; commit to keeping voice property-first (per content-steward F3)
- **Paul-only ops surface:** rename "Mom's pick" → "Mom suggested" or similar; accept low view count as correct

### D2. Dashboard stack policy as it grows

ux-expert F5: 9 cards, strip carries 6. New ships (map, Phase G readouts) need a policy first:
- **A. Tiered strip with tiles for everything** — every card earns a tile, scrolling strip
- **B. Strip-is-Mom-priority, tail-is-Paul-ops** — keep strip lean, allow ops content below without tiles

Worth Considering broke the implicit rule and the telemetry shows the cost. Decide before next card ships.

### D3. Paul-as-user — device shift or builder-only?

user-researcher: Paul's mapped iPhone went silent after 5/21. Two readings:
- Paul switched primary device (telemetry profile needs re-mapping in `tools/people.json`)
- Paul-as-builder-only, Mom is the actual primary user

**Resolution path:** Paul checks Safari profile on current iPhone + updates `tools/people.json`. Either reading is fine; what's not fine is designing for the three-performer model by default while this is unresolved.

### D4. Garden Guru asks-vs-guesses drift

ux-expert F9: rubric says ask clarifying questions about vague descriptions; observed behavior on the brown-bird-at-feeder conversation was guess-with-hedges. All 10 conversations are 2-turn — the asking pattern would lengthen them.
- **Accept the drift, update the rubric:** edit the system prompt to legitimize guess-with-hedges for vague descriptions
- **Iterate the system prompt:** push harder on asking, accept that 2-turn ceiling reflects unsuccessful interactions

### D5. Seeded prompts — confirm they exist

ux-expert F3 + content-steward open question: 3 seeded in-voice prompts referenced in the unified-input memory don't appear to be in `viewer.html` under any name greppable. Either shipped under different naming, deferred from the redesign, or memo is wrong. Confirm before either retires or restores.

---

## Strategic directions — "incorporate more info and research"

Ranked by panel consensus. All assume the principle: **inline depth in high-engagement cards, voice governs prose wrap, depth-filter still applies (only what Paul observes on this property).**

### Tier 1 — Ship-it-this-month

**SD1. Seasonal "what's on the property right now" inline callouts** (ai-advisor #1, S, free, no AI)
- 1–3-line editorial block per major card surfacing the most relevant `peakWindow` / `monthsActive` / `events.json` / `references.json` framing for the current week.
- Zero new data — the dashboard already knows mountain laurel peaks May 21–June 4; it just doesn't say so on the front.
- Lands inside Plants card (60 views), Wildlife card, etc. — ux-expert's "inline depth" pattern.
- **Validation:** does Mom or Paul revisit cards more often on the weeks the callout is most active?

**SD2. "Last year on the property" inline note inside Plants card** (ux-expert + ai-advisor #3 minimum-shape)
- Reads from accumulated observations: "You noted the mountain laurel opening April 25 last year — watch for it now."
- Field-journal voice: memory, not database row.
- Lives inline, not as a new card.
- **This is the Phase G minimum viable shape.** First consumer is the Plants card; cadence is render-time computation from canonical observations (eng F8 — don't pre-compute and write back to KV).

### Tier 2 — After T+30 Mom interview clarifies

**SD3. Almanac entry context** (ux-expert + user-researcher Job 2)
- 55 revisits on Mom's device. When she returns to an entry, pull weather + phenology for that date inline: "Saved May 18 — laurels were peak that week."
- Depth where she already returns.
- Becomes possible once the Phase G observations index exists (per SD2).

**SD4. Photo-reply enrichment** (ux-expert)
- After a Garden Guru photo-ID reply, small "others like this on the property" carousel pulling from existing JSON.
- Same surface, richer content — no new card.
- Mom's killer flow; deepen what's already working.

**SD5. Look-ahead-by-week** (user-researcher Job 5, unserved)
- Mom's existing scan behavior is present/today-tense. Forward-look at week-resolution, across plants/wildlife/celestial.
- Could be a 7-day mini-strip at the top of an existing card, or its own row above the dashboard cards (testing D2).

### Tier 3 — If/when the pattern justifies a new surface

**SD6. "Worth Watching" card** (ai-advisor #2)
- Observable-but-not-yet-present species. Depth-filter gated.
- Same shape as Worth Considering, different content. Only ship if D2 lands on tiered strip + Worth Considering earns its tile first.

**SD7. "Place Stories" card** (ai-advisor #2)
- Cat 7 history anchors from `research-resources.md` — Cherokee land, AT terminus, Connahaynee Lodge.
- ~10–15 research entries move from appendix to surface. Visit-friendly content; deepens the property identity.
- Same constraint: only ship after the dashboard-stack policy decision (D2).

**SD8. Conversation-browse UI** (user-researcher Job 6, unserved)
- Already named open in CLAUDE.md but unbuilt. Look up a past Garden Guru answer.
- Compounding-value play. Without it, the personal-library win at 3 months can't materialize.

---

## Voice principles to add to charter

content-steward proposes two new principles:

1. **Research deepens the data layer; voice governs the prose wrap.** As much research/info as the almanac warrants. The prose wrap (intro, first sentences, summaries) stays property-anchored. The line between "deepening the journal" and "becoming a content site" lives in the prose layer, not the data layer.

2. **Operator-mode register is a legitimate flex for procurement/decision content.** Sources card's nursery-listing register is correct for that surface; references.json should be brought into journal voice; candidate entries should be property-first. Two-register model > three-voice mess.

---

## T+30 Mom-interview additions (~mid-June 2026)

per user-researcher. The locked meta-feedback question (`PHASE_E_MVP.md` ~line 229) stays. Add:

1. **"Tell me about the last entry that mattered to you."** Decodes the dead star — invisible vs. wrong model vs. redundant.
2. **"Tell me about the last Garden Guru answer."** Decodes the 2-turn ceiling.
3. **"What made you change the text size?"** Validates the no-glasses constraint in her words.
4. **"Was there a bloom you almost missed?"** Tests Job 7 (forward-look need).

Three are high-priority; carry the others only if conversation has room.

---

## What this synthesis defers

- **Phase G full architecture** — ai-advisor and engineering-partner converged on "render-time computation from canonical observations, on-demand `rollup-observations.py` script as the AI seam." The full Phase G design waits until SD2 ships and proves the consumption pattern.
- **Audio commit ordering** (eng F4) — same architectural shape as the 5/26 storage incident. Fix before Phase H tackling un-canon'd-audio, not now.
- **viewer.html size** (eng F3) — verdict is hold the line. 11.3K lines well within carry-cost. Watch-flag at one IIFE module crossing 1,500 lines or two modules needing shared helpers.
- **`research-resources.md` known gaps** (UGA SBG/GNPI 2025 PDF 404; TACF GA pathway; HRI sourcing; GFC 2026-27 seedling catalog; Mt. Cuba beyond hydrangea) — long-tail content backlog, no engineering work needed.

---

## Suggested order of operations

1. **This week (S-effort):** validate F1 against KV, then ship punch list items 1–3 + 6 (eng one-liners + content one-liners + Worth Considering voice pass). All small.
2. **After Mom validates the kind-fence fix solves the photo flow:** ship punch list item 4 (star retirement) + 5 (Sources editorial pass).
3. **In parallel:** Paul decides D1, D2, D3, D5 (D4 can wait for T+30).
4. **After Tier 1 strategic directions ship and ~30 more days of telemetry:** assess SD3–SD5 and revisit Phase G shape.
5. **T+30 Mom interview** in ~mid-June. Carry the four prep questions. Findings reset the Tier 2/3 picks.
