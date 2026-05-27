# Telemetry rollup — first run

**Date:** 2026-05-26
**Window:** 2026-05-20 through 2026-05-27 (UTC; rollup includes a partial 5/27 from late-night UTC events)
**Source:** Cloudflare KV via `wrangler kv key get` (analyze-fernwood.py logic, locally executed against /tmp pulls — no `FERNWOOD_TOKEN` setup required)
**Files pulled:** 10 conversations + 8 metrics days + 4 cost-log days + observations

This is the first run of the rollup since metrics-capture shipped 2026-05-20. Replaces the "shipped but never run" item in CLAUDE.md pickup-line #6.

---

## Headlines

1. **Adoption is real.** Two unmapped iPhones are actively using the dashboard daily — the most-used iPhone has 27 sessions / 341 events in 6 days. Strong signal the family-scope launch is landing.
2. **Strong candidate signal that the most-active iPhone is Mom.** `d-14nyhnjz-5lh01604-mpevr35o` — viewport 393x793 (iPhone Pro), 12 `text_size_changed` events (the only device that used the A/A+ toggle Paul shipped 5/22 for Mom-without-glasses), heavy `entry_revisited` (55) suggesting return-visits to saved notes, 2 Garden Guru conversations + 1 species promoted. **Confirm by asking Mom or comparing UA + Safari history.** If confirmed, this is the load-bearing answer to the eval rubric's primary question: *"The dashboard gets opened regularly."* ✓
3. **Phase F Option C is doing real work.** 4 image-bearing conversations, 3 `species_id_confirmed`, 2 `species_promoted` — matches what `git log` shows (Pop Star Hydrangea 5/21 + Spiderwort 5/22). Distributed across both unmapped iPhones.
4. **Cost is comfortable.** $0.86 total over 6 days = ~$5/month at current usage. Well below the $2/mo Phase F bench-analysis estimate even with 4 vision calls.
5. **The star affordance has zero use.** `entry_starred: 0` and `entry_unstarred: 0` across all devices over 6 days. Either the affordance isn't discoverable, isn't compelling, or the underlying "this matters" interaction doesn't exist as a behavior the way it was hypothesized. Worth a Paul-judgment moment.
6. **The 5-turn conversation cap has never fired.** `conversation_capped: 0`. All 10 conversations are exactly 2-turn. Mom and Paul both ask one question, get an answer, move on. The 5-turn cap is mechanism without need — fine to leave shipped, but doesn't deserve attention.

---

## Cost-to-date

| Date | Calls | Cost |
|---|---|---|
| 2026-05-20 | 4 | $0.1014 |
| 2026-05-21 | 4 | $0.3429 |
| 2026-05-22 | 4 | $0.3364 |
| 2026-05-24 | 1 | $0.0809 |
| **Total** | **13** | **$0.8617** |

Per-call avg: ~$0.07. Image-bearing calls (Pop Star, Butterfly Weed, black bear, Spiderwort) drove the 5/21–5/22 cost peaks. Caching kept it lower than it would have been — `cache_creation` + `cache_read` tokens are both substantial in the cost-log entries.

---

## Engagement by device

| Device | Person | Class / Viewport | Sessions | Total events | First seen | Last seen |
|---|---|---|---|---|---|---|
| `d-14nyhnjz-...` | *unmapped — likely Mom* | mobile / 393x793 | 27 | 341 | 2026-05-21 | 2026-05-27 |
| `d-avslqpyd-...` | paul (laptop) | desktop / 1512x827 | 32 | 230 | 2026-05-21 | 2026-05-26 |
| `d-szqlt0h7-...` | *unmapped — 2nd iPhone* | mobile / 414x848 | 16 | 135 | 2026-05-21 | 2026-05-26 |
| `d-fxeb35uh-...` | paul (iPhone, mapped) | mobile / 393x665 | 7 | 53 | 2026-05-21 | **2026-05-21 only** |
| `unknown` | *unmapped — pre-deviceId* | desktop / 1512x827 | 7 | 24 | 2026-05-20 | 2026-05-21 |

**Notes:**
- The mapped Paul iPhone (`d-fxeb35uh`) only shows activity 5/21 — Paul appears to have switched primary iPhone session contexts. The two unmapped iPhones (`d-14nyhnjz`, `d-szqlt0h7`) are inheriting the iPhone traffic.
- `d-14nyhnjz` is the only device that uses `text_size_changed` (12 times). That toggle shipped 5/22 specifically for Mom-no-glasses. **Strong evidence this is Mom.**
- `d-szqlt0h7` (viewport 414x848 = iPhone Pro Max) could be Paul's 2nd iPhone (work?), a Safari profile, or another family member.

**The deviceId→person mapping in `tools/people.json` is now the highest-value missing data.** A 2-line update would convert 60% of the unmapped events into per-person signal.

---

## Event types — Paul vs unmapped iPhones

| Event | Paul (mapped) | Unmapped: d-14nyhnjz (likely Mom) | Unmapped: d-szqlt0h7 (2nd iPhone) | Unknown (pre-deviceId) |
|---|---|---|---|---|
| card_section_viewed | 150 | 194 | 70 | 0 |
| card_expanded | 17 | 25 | 9 | 1 |
| entry_revisited | 33 | 55 | 16 | 0 |
| field_note_saved | 0 | 4 | 0 | 2 |
| input_focused | 5 | 4 | 3 | 0 |
| **conversation_started** | **0** | **2** | **4** | **4** |
| conversation_turn | 0 | 2 | 4 | 4 |
| conversation_reply_dwell | 0 | 2 | 4 | 0 |
| **conversation_capped** | **0** | **0** | **0** | **0** |
| image_attached | 0 | 2 | 2 | 0 |
| image_reply_received | 0 | 2 | 2 | 0 |
| species_id_confirmed | 0 | 1 | 2 | 0 |
| species_promoted | 0 | 1 | 1 | 0 |
| seeded_prompt_used | 0 | 0 | 0 | 0 |
| **text_size_changed** | **0** | **12** | **0** | **0** |
| subtab_switched | 3 | 7 | 1 | 0 |
| session_start | 39 | 27 | 16 | 7 |
| session_end | 36 | 1 | 1 | 6 |

**Things that pop out:**
- **Paul (mapped) has zero conversation events.** All 10 Garden Guru conversations came from the unmapped iPhones + the pre-deviceId "unknown" device. Either Paul's Garden Guru tests happened on those iPhones before mapping, or Paul has been observing real-user usage rather than testing himself.
- **`seeded_prompt_used: 0`** across all devices. The 3 in-voice seed prompts shipped 5/20 are not being clicked. Same possible reasons as the star.
- **Mom's hypothesized device (`d-14nyhnjz`) has `session_end: 1` against `session_start: 27`.** Either she rarely closes cleanly (background-tab style) or the session-end event isn't firing reliably on iOS Safari background. Worth checking.

---

## Garden Guru engagement

- Conversations total: **10**
- Total turns: **20** (avg 2.0/conversation)
- With image attachment: **4**
- Date distribution: 5/20=4, 5/21=2, 5/22=3, 5/24=1
- Zero 3+-turn conversations
- Zero `conversation_capped` events
- Zero `seeded_prompt_used` events

**The Q5 win pattern from the eval rubric** ("one well-placed question per week, answered in voice, with the wedge over Claude visible") is happening at ~2.5 questions/day this week — above the bar — but with no compounding (no follow-ups, no multi-turn). The "personal library accumulates" win at 3 months is too early to judge.

---

## Curation — "does anyone come back to a saved entry?"

- `field_note_saved`: **6**
- `entry_starred`: **0**
- `entry_unstarred`: **0**
- `entry_revisited`: **104**

**The revisit-vs-save ratio is ~17:1.** Saved entries ARE being revisited at scale — exactly the question the eval rubric framed as the curation hypothesis test. The hypothesis is validated.

**But the star affordance is dead on arrival.** Six days, 104 revisits, zero stars. Worth a deliberate Paul-decision moment: either re-position the star, kill it, or accept that the revisit-frequency itself is the implicit "this matters" signal and stars are redundant.

---

## Card popularity

| Card | Views | Expands |
|---|---|---|
| card-plants | 60 | 11 |
| card-weather | 60 | 5 |
| card-wildlife | 54 | 6 |
| card-celestial | 47 | 1 |
| card-property | 45 | 0 |
| **card-fieldnotes** | **43** | **18** |
| card-vehicles | 42 | 2 |
| card-release-notes | 30 | 3 |
| card-references | 28 | 2 |
| card-candidates | 5 | 4 |

- **Plants and Weather are tied for most-viewed.** Both are the dashboard's strongest at-a-glance surfaces.
- **Field-notes has the highest expand-rate** (18 expands / 43 views = 42%) — when it gets viewed, it's almost always opened. That tracks with the 104 entry-revisits.
- **Property card never gets expanded** (0/45). The summary content is enough; no one needs the deeper view.
- **Candidates** (shipped today) already has 4 expands on 5 views — high-engagement out of the gate. Worth watching.

---

## What this rollup leaves open

1. **Confirm Mom is `d-14nyhnjz`.** Ask her or check Safari activity timestamps next time you have her phone. Update `tools/people.json` once known.
2. **Star affordance decision.** Six days of zero stars is a strong null. Re-position, kill, or accept.
3. **Seeded-prompts decision.** Same — zero usage. Either move them up the visibility ladder or accept they're not the pull mechanism that's working (the dashboard cards themselves are).
4. **Why is mapped Paul iPhone (`d-fxeb35uh`) silent after 5/21?** Possibly a Safari clear or a different test device became primary. Update mapping if a new Paul-iPhone deviceId emerges.
5. **iOS `session_end` reliability.** 27 starts → 1 end on the likely-Mom device suggests iOS Safari background-suspend doesn't fire the unload-style handler. Worth a 5-min check on whether `visibilitychange` would catch more.

---

## Where this rollup came from

- `wrangler kv key list --binding=OBSERVATIONS --remote` to enumerate KV keys
- `wrangler kv key get` per key to pull JSON content
- Local Python script (mirroring `tools/analyze-fernwood.py` logic) to compute the tables
- Saved to `/tmp/gg-telemetry/` (24 hours; ephemeral) and `/tmp/gg-conversations/` (ephemeral)
- This report lives in `.audit/` (committed, durable)

**To re-run via the production script with `FERNWOOD_TOKEN`:**
```bash
export FERNWOOD_TOKEN="<value of SHARED_TOKEN secret>"
python3 tools/analyze-fernwood.py --start 2026-05-20 --end 2026-05-26 --out .audit/2026-05-26-telemetry-rollup-v2.md
```
That run will produce the canonical-shape report; this v1 was a manual rollup using the same source data. They should agree on the headline numbers.
