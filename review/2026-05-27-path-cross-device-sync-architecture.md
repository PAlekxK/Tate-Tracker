# Path Eval — Cross-device sync architecture for Fernwood

**Date:** 2026-05-27
**Mode:** Path Evaluation
**Subject:** Why does edit-on-laptop / read-on-phone lag, and what's the right sync posture?
**Supersedes:** Earlier framing in this file (GH Pages deploy reliability only) — that's now §6 below.

## The observed phenomenon

Today: Paul drew zones on laptop → chip said "synced" → Worker auto-committed `Zone update` + `Re-inline ZONES_DATA` pairs to `main` (`git log` shows 8 zones) → GH Pages served updated `zones.json` (curl-verified) → **iPhone PWA still showed old zones, hard-refresh didn't fix it.** Every link claimed green; the system as a whole was red.

## 1. Walking the chain — where the lag actually lives

| Hop | Best case | Realistic worst case | Bites here? |
|---|---|---|---|
| Worker `/api/zone-save` accepts write | < 1 s | < 1 s | No. This is what the chip currently measures, and it's honest at this hop. |
| Worker writes to KV | seconds | eventually consistent across edge POPs, 10–60 s | Possible but small. |
| Worker commits to GitHub (×2: `zones.json` + viewer.html re-inline) | 1–3 s | 5–10 s, occasional failure | Yes — and failure is silent at the chip. |
| GH Pages picks up commit and deploys | 30 s – 3 min | 5–15 min on bad days; sometimes needs retry | **Yes — primary deploy-tail source.** |
| GH Pages CDN propagates new `zones.json` to the iPhone's edge POP | seconds | up to ~10 min for cold edges | Yes. |
| iOS Safari HTTP cache | n/a if fresh | serves stale until TTL expires; PWAs are worse | **Yes — "hard refresh" on iOS PWA is *not* a real cache buster.** |
| PWA app-shell cache (if a SW is registered) | n/a | indefinite without explicit version-bump | Likely culprit if a SW exists; needs check. |
| Inlined `ZONES_DATA` in viewer.html as fallback | n/a | shadows fresh `zones.json` if the JSON fetch fails *or* if init reads inline before fetch resolves | **Yes — silent shadowing risk.** |
| localStorage `tateTracker.zones.v1` (if cached) | n/a | shadows everything until invalidated | Yes if it exists for zones. |

Honest read: today's lag is almost certainly **iOS PWA cache + GH Pages deploy tail stacking**. Worker→KV→git→Pages probably finished under 2 min; the iPhone was reading a cached `viewer.html` (with stale inlined `ZONES_DATA`) and never refetched `zones.json`. The chip said synced because *writes* were synced. *Reads* were never measured.

## 2. The architectural question — write-through-git vs. KV-direct-read

Current shape: every device writes to one Worker → Worker commits to git → every device reads from GH Pages. The git round-trip exists because inlined `ZONES_DATA` is the cold-start fallback; keeping it fresh requires a re-inline commit on every write. That's the load-bearing reason for the per-edit commit pair, *and* the propagation-tail amplifier.

The alternative worth taking seriously: **warm devices read from KV directly via Worker; cold start still uses inlined `ZONES_DATA`; git remains the long-term canon.**

- Write path unchanged.
- Read path on warm load: `GET /api/zones` → KV → seconds end-to-end. No git, no Pages, no CDN tail.
- Inlined `ZONES_DATA` becomes a true cold-start fallback (first paint before JS) and a disaster-recovery snapshot, not the steady-state source.
- Re-inline commits become *batchable* — they no longer gate cross-device freshness, so they drop from every-edit to nightly or per-session. Commit-cadence problem collapses with the same change.

This is the same pattern the Worker already uses for observations and conversations. Zones drifted into write-through-git because the inlined-fallback pattern matched the existing JSON files; the cost only shows up at multi-device read time.

## 3. The chip is reporting the wrong thing

"Synced" today means: Worker 200'd the write. It should mean one of:

| Phase | What's true | Mom needs | Paul needs |
|---|---|---|---|
| Write accepted | Worker has it | silent (hidden) | "Saved to cloud" |
| KV propagated | Other devices *could* read it now | silent | "Other devices can see it" |
| Git + Pages caught up | Cold loads will get the new data | silent | "Published" |
| All known devices caught up | Mom, Paul-phone, laptop on current version | silent | "Everyone's on this version" |

Mom: one bit — fine or not fine. Per [[project_fernwood_mom_reading_accessibility]], multi-state copy isn't readable; chip stays hidden when fine, becomes a single obvious affordance when not.

Paul: more state is legible and useful. The Worker already knows `deviceId` per request; it can stamp `lastSeenVersion` per device on every read and answer "is everyone caught up?" That capability is sitting unused. Implementation cost is small (one KV key, one field on read responses, one chip-state on the laptop view); diagnostic value when today happens again is large.

**Posture, not implementation:** Paul-on-laptop and Mom-on-phone don't need the same chip. Same component, parameterized by audience — quiet for Mom, verbose for Paul, no code fork.

## 4. Recommendation

Reposition the deploy-health pulse as one piece of a three-part posture, in this order:

1. **Diagnose today's specific failure first.** Confirm whether iPhone PWA is caching `viewer.html`, whether a service worker is registered, and whether `zones.json` was refetched on the stale visit. The right architecture is downstream of knowing what actually broke. One session of Paul-side instrumentation, no commits.
2. **Move zones to KV-direct-read for warm loads (§2).** Collapses the cross-device propagation tail from "deploy + CDN + cache TTL" to "KV consistency window" — the durable fix for the canonical Paul-laptop-edits / Mom-phone-reads flow. Inlined `ZONES_DATA` stays as cold-start fallback; re-inline commit moves off the per-edit critical path.
3. **Rebuild the chip around honest phases (§3)** — silent-for-Mom, multi-state-for-Paul. Use existing `deviceId` to answer "has the other device caught up?"

The original deploy-health pulse becomes a *fallback monitor*, not the primary fix. It still has a role — catching the case where a cold device hits stale Pages — but it stops being load-bearing once warm reads bypass that path.

## 5. What this does not change

- GH Pages stays. No host migration. Path 3 in §6 still disqualified by Mom's home-screen icon.
- Git remains the long-term canon. KV is the freshness layer, git is the durable layer.
- The Worker's existing auth + endpoint shape carries this without redesign.

## 6. Original deploy-reliability sub-question (historical)

The deploy-reliability framing from this morning is still valid as a *subcomponent*: GH Pages publish has a non-zero failure rate, commit cadence is the amplifier, the chip lying about deploy state is the user-facing harm. Trade-off table preserved — now scoped to "what to do about the cold-read path *after* warm reads move off git."

| Path | Complexity | Scalability | Future features | Future-Paul-with-Claude | Learning value |
|---|---|---|---|---|---|
| 1. Accept failures | None added | Same | Nothing | Easiest | Low |
| 2. Deploy-health pulse | Small | Same | Health-check foundation | High | High |
| 3. Move hosts (CF Pages) | Medium-high | Better | Co-located w/ Worker | Migration scar | Medium |
| 4. Dual deploy + Worker failover | High | Best | A/B + canary | Heavy | Disproportionate |

## Decisions / open questions for Paul

- Diagnose first: can Paul reproduce today's stale read with devtools open (iPhone, or Paul-on-laptop simulating a cold PWA load) before any architectural change?
- Is there a service worker registered for the PWA? If yes, that's almost certainly today's primary culprit and changes the order of attack.
- Confirm direction: does the KV-direct-read posture (§2) feel right as the next architectural move, or is there a reason to keep zones on write-through-git that I'm missing?
- Chip redesign (§3) is gated on §2 landing — no point reshaping the chip around phases the architecture no longer has.

## Principles invoked

- *Don't migrate working infrastructure without a functional reason* (cross-project)
- *Sanitize at the storage boundary* ([[feedback_sanitize_at_storage_boundary]]) — sibling here: *measure the user-visible state, not the nearest internal hop*
- *Mom-no-glasses single-bit affordances* ([[project_fernwood_mom_reading_accessibility]])

## Principles to propose

- *The sync indicator should report the user-visible state, not the nearest internal hop.* Came directly out of "chip said synced, phone showed old data." Candidate for cross-project — applies anywhere Paul builds a multi-device personal tool.
