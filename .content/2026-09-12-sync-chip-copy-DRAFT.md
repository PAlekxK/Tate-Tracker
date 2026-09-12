# Zone-save sync copy — DRAFT for Paul's gate

- surface: the map sync chip + the zone-save outbox (`engine/viewer.template.html`)
- plan: `.plans/2026-09-07-capture-write-path-PLAN.md` step 5 · build plan `.engineering/2026-09-12-capture-write-path-build-PLAN.md` B3
- seat: content-steward, convened 2026-09-12 as the OWED seat (the plan waives ux-expert for steps 1–4 and owes both at step 5)
- status: ⛔ **DRAFT. Nothing here has shipped and no word below has reached a resident.**

> ### ✅ R6 RULED — the resident-facing noun for a zone edit is **“edit”** `[paul-stated 2026-09-12: "edit is fine"]`
> This was the open question holding three of the drafts below. ✅ Checked against `VOCABULARY.md` §4
> before recording: **`edit` is not in the rejected register** (zero hits), so it collides with nothing
> and no prior rejection is being re-proposed. Every `<noun>` slot below is now filled with **edit**.
> ⚠️ **`estate` still never reaches a user-facing surface** (§4) — it is correct only in a JSON `hint`,
> which is a developer surface.

---

## ⛔ READ FIRST — the premise this copy was commissioned under was WRONG, and it shrinks the job

The plan's step 5 assumes the chip distinguishes `kv` from `kv+git` and therefore needs a new state.
**It does not, and never did.** `handleZonesSyncStatus` computes `allCaughtUp` entirely from KV — canon
is `_meta.lastBuiltAt` written by the KV put; device stamps are `zones-last-seen:<id>` written by
`GET /api/zones`. **Git appears nowhere in that path.** ux-expert reached this independently the same
day. The three states already mean *saving → the Worker has it → your other phones have it*, and all
three are reachable at a household the moment step 1 lands.

⭐ **So the honest fix is a corrected code comment (`viewer.template.html:14054`), not a new state.**

⛔⛔ **AND THE REAL MOM-FACING SURFACE IS THE FAILURE STATE, NOT THE SUCCESS LABELS.**
`getZoneAudienceMode()` defaults to **`"quiet"`** and `render()` hides the chip in **every state except
`failed`**. So a resident never reads *“saved to cloud”* or *“live everywhere”* at all — **the only chip
words that can reach her are the failure ones.** That is where the copy effort belongs, and it inverts
the plan's assumption about which words matter.

---

## State A — the edit is held on the phone (out of Wi-Fi range)

### A-i · the ack at the moment of saving

| | option | trade-off |
|---|---|---|
| **A1 ⭐ recommended** | `Saved on your phone — it'll reach the record next time you're back on Wi-Fi. ✓` | **Verbatim reuse** of two shipped sentences (`:11417`, `:13156`). Zero new vocabulary; she has read this exact line on two other channels. Cost: names no object. |
| A2 | `Fern Garden is saved on your phone — it'll reach the record next time you're back on Wi-Fi. ✓` | Confirms *which* edit is held — matters more for zones than audio, because a save is a whole-record write she may make several of. Cost: the panel already renders the name directly above (`:11603`), so the anchor is likely redundant here. |

### A-ii · the standing line when she opens the panel

*(deliberately no `✓` — a tick answers something she just did; this is a status, per the comment at `:11613`)*

| | option | trade-off |
|---|---|---|
| **A3 ⭐ recommended** | `1 edit is still on your phone — it'll go to the record when you're back on Wi-Fi.`<br>`N edits are still on your phone — they'll go to the record when you're back on Wi-Fi.` | Identical grammar to the shipped audio line (`:11618`), so the panel speaks **one voice for both channels**. Now unblocked by the R6 ruling. |
| A4 | `What you wrote here is still on your phone — it'll go to the record when you're back on Wi-Fi.` | Avoids the count and the noun. Cost: loses the count, which is the one thing telling her whether she is one edit or six behind. |

## State B — it reached the record

| | option | trade-off |
|---|---|---|
| B1 | `✓ in the record` | Shortest; reuses the world's middle noun. Cost: loses the landed-vs-propagated distinction. |
| **B2 ⭐ recommended** | `✓ saved to the record` | Keeps the **verb** from the held line, so the pair reads as one journey with a changed location — which is the ratified mechanism at `:11412`: *distinguished by naming the location in words she reads, not by a mark she must decode.* Cost: one word longer; wants a width check. |
| B3 | `✓ written down` | The most Fernwood-native verb in the corpus. ⛔ **Not here** — it names the act, not the destination, and the destination is this state's entire information content. |

⛔ **Hard constraint:** whichever wins **must not read as the lesser half of a pair.** At a household
this is the terminal state, not a waiting room.

## State C — visible on her other devices

| | option | trade-off |
|---|---|---|
| **C1 ⭐ recommended** | **Retire the state.** No third label; `synced` fades to idle. | `"✓ live everywhere"` **over-claims**: `allCaughtUp` needs only `devices.length > 0`, and `handleZoneSave` **stamps the editing device itself** before returning — so on a one-device household *“everywhere”* resolves true by counting **the phone that just made the edit**. The 30-day TTL means the claim gets *easier to satisfy as coverage gets worse.* Costs her nothing: in quiet mode she never sees it. |
| C2 | `✓ on your other phone too` | Honest — quantifies over exactly the set the mechanism knows. Cost: makes a claim about hardware, a noun this world otherwise avoids. |
| C3 | `✓ Paul's copy has it too` | ⛔ **Ruled out** — attributes a device to a person, and a deviceId is a browser bucket, not a person. |

## State D — it did not get through ⭐ THE ONE SHE CAN ACTUALLY SEE

⛔ **Once the held-on-phone path exists, an out-of-range save is HELD, not FAILED** — and today it
renders as a ⚠ alarm. On this property, out-of-range is the *normal* condition, not the exception.

**The detail sentence:**

| case | copy | note |
|---|---|---|
| **the Worker refused ⭐** | `That didn't get through — your words are still here. Worth trying again when you're back on Wi-Fi.` | **Verbatim reuse** of the shipped `:13157` line. If the edit is not words, `what you wrote is still here`. |
| the phone can't hold it | `This phone can't hold the edit — that one didn't get saved. Worth letting Paul know.` | Grammar lifted whole from `ZONE_AUDIO_CANNOT_HOLD` (`:11427`), including the escalation and the deliberate absence of `✓`. |
| the phone is full | `The phone is holding all it can, so that one didn't get saved. What's waiting will go when you're back on Wi-Fi, and there'll be room again.` | Near-verbatim `ZONE_AUDIO_FULL` (`:11429`); carries its own remedy. Cost: long at A+. |

**The chip label** (replacing `⚠ sync failed`):

| | option | trade-off |
|---|---|---|
| **D-a ⭐ recommended** | `⚠ didn't get through` | Names the **damage, not the classification** — *sync failed* is a classification, which the register rules forbid. Reuses `:13157`'s verb phrase so chip and detail **read as one sentence when she taps**. |
| D-b | `⚠ not saved yet` | Her terms. Cost: *yet* promises a retry the can't-hold case cannot make. |
| D-c | `⚠ still on this phone` | Correct in the held case only; unusable as the single label. |

⭐ **The `⚠` is NOT softened.** This is the one condition where the cost of her missing it is her work
not landing — which is exactly the audience test.

---

## ⛔⛔ CRITICAL — independent of every word above

`renderDetails()` prints `lastError` **raw** (`:14155`), built at `:14267` as `"HTTP " + status + ": " + body`.
At a household that string is:

```
HTTP 503: {"error":"github-not-configured","hint":"set GITHUB_TOKEN and GITHUB_REPO worker secrets"}
```

**The resident's single visible sync state would instruct her to set Worker secrets that are forbidden
at her deployment by ruling.** Step 1 removes the 503; **this path survives it.**

⚠️ **LATENT, not live** — `instance/home.json:31` lists `zones` in its `absent` array, so the zone
surface does not render at a household and **no resident has ever seen this chip.** It becomes a wall
the moment this plan succeeds. *(Stated precisely: “Mom is being shown a raw 503” would be false.)*

## Where this reuses rather than mints

| line | source | how |
|---|---|---|
| A1 | `:11417` + `:13156` | **verbatim** |
| A3 | `:11618`–`:11619` | grammar verbatim, object swapped to **edit** |
| D (refused) | `:13157` | **verbatim** |
| can't-hold / full | `:11427` / `:11429` | grammar verbatim, object swapped |
| the three nouns *your phone · the record · Wi-Fi* | `:11412` | unchanged |
| **minted:** `✓ saved to the record` | — | built from the held line's own verb |
| **minted:** `⚠ didn't get through` | `:13157`'s verb phrase | half-minted at most |

**Two mints, one a compression of a shipped sentence.**

## Flags

- ⚠️ **`:7300` quotes the chip labels verbatim** in the Sync-settings help text. If a label moves, that
  string moves **in the same commit** — *a correction must sweep the files quoting it.*
- ⚠️ **`:13737` says “online” where every other line says “Wi-Fi”** — a pre-existing divergence in the
  shipped file. Flagged so this pass does not add a third variant beside it. **Open.**
- ⚠️ **The `✓` convention** is ratified as *“we have your words”* (`:11414`). A zone edit is a name plus
  geometry, not words. Either widen the comment to *“we have what you gave us”* or accept the stretch —
  but **record the decision**, or the next reader re-derives it. **Open, small.**
- ⛔ **“Everything is changeable” does NOT attach here.** A sync state is not something she gave;
  attaching it would make it a standing footer, which the 2026-08-04 rule forbids.
- ⛔ **No copy was rendered at 414 × 848 × A+.** Every length judgement is by eye. Per the standing rule
  the winning labels want `measureNestingWidth.herConditions()` before they ship.
