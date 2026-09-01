# Vehicle conversation mine — DR200S · Bronco · GTI

**Written 2026-09-01.** Agent-produced. **PROPOSAL ONLY — nothing here has been written to
`vehicles.json`, `cycle/requests.jsonl`, any guide, or any commit.** This file is the only
artifact created.

**Instrument:** `~/LocalProjects/conversation-corpus/corpus.sqlite` (rebuilt 2026-09-01),
queried directly over SQL and via `corpus_search.py`.

**Ground truth read first:** `vehicles.json` (22 machines, 61 service rows fleet-wide — 3 rows
`dr200s-2017`, 22 rows `gti-2016`, 28 rows `bronco-1989`), `cycle/fleet/CYCLE-MAP.md`,
`cycle/fleet/cycle-state.json`, `cycle/fleet/FIELD-NOTES.md`, `cycle/requests.jsonl`, plus
`guides/blue-thunder-starting-diagnosis.md` and `guides/bolores-door-panel-repair.md` when a
finding looked absent from the card.

---

## 0 · THE HEADLINE, before the detail

**The record is downstream of these very conversations, and it shows.** Nearly everything I
found is already in `vehicles.json` — often in more detail, with better provenance, and with
caveats the transcript itself does not carry. That is not a null result; it is a measurement
that the capture path is working. The genuinely NEW material is small, and I have kept it small
rather than padding it.

**What the corpus does add that the record cannot:** Paul's own words, dated and attributable,
behind facts the card states in the third person — and the shape of how the work actually got
done (§4), which is a first-class deliverable here.

### ⚠️ THE INSTRUMENT'S HARD BOUNDARY — read before trusting any absence

```
corpus date range: 2026-07-03T12:50Z → 2026-09-01T12:23Z
```

**Fifty-nine days.** The corpus holds **no Claude Code transcript from before 2026-07-03.**

Consequences you must not forget:

- The Bronco was bought **October 2025**. Twelve of her 28 service rows predate the corpus.
  The tailgate/window/lock campaign of Oct–Dec 2025 is **not in this corpus as it happened** —
  only as *later discussion of it*.
- The DR-Z400S 2025 overhaul and the DR200's 2025-05-09 fuel diagnosis reached the record
  through the **OpenAI/ChatGPT export mine** (sessions `800a4f5d` 7/22 and `702a4ee7` 7/14) and
  the Gmail/Takeout receipt mine (`b5e6f33d` 7/20). This corpus indexes the *mining sessions*,
  not the original ChatGPT threads. **Do not read this corpus as the full history of these
  conversations.**
- **Absence here is not evidence.** It never was, and with a 59-day window it is especially not.

---

## 1 · What I searched, and what I sampled

### Queries run

| Query axis | Method | Raw volume |
|---|---|---|
| `bronco` / `bolores` | SQL `LIKE`, all roles, non-sidechain | 40 sessions with ≥1 hit; top session 242 term-hits |
| `gti` / `golf` | same | 40+ sessions; top 75 term-hits |
| `dr200` / `blue thunder` | same | 23 sessions; top 42 term-hits |
| Misspelling/alias sweep | `belorus, beloris, baloris, veloris, valoris, bolorus, dolores, booth under, desert storm, the four hundred, drz, dr-z, mk7, vw, volkswagen` + every shop name in the record (`express oil, eurofed, autobahn, jim ellis, autohaus, midas, cannon automotive, lmc, tim's auto, cherokee muffler, vip tires`) | 62 Paul-prose messages, 28 not caught by the plain-name sweep |
| Maintenance-vocabulary cross-cut | 52 maintenance keywords × 19 vehicle tokens, restricted to Paul's prose | **73 messages** — this was the main harvest |

**Noise filter applied to "Paul's prose":** role=`user`, `sidechain=0`, and the message must not
begin with `<command-name>`, `<task-notification>`, `<system-reminder>`, `<local-command-caveat>`,
`[Image`, `[Request interrupted`, `Caveat:`, or an autonomous-run mission prompt. Without this,
"user" messages are ~70% harness plumbing and tool results. **Raw hit counts in this corpus
massively overstate human content** — e.g. `dr200`/`blue thunder` returns 16 role=user rows of
which **5** are Paul actually speaking.

### Sessions I read in full (Paul's side, every prose turn)

| Session | Date | Vehicle | What it is |
|---|---|---|---|
| `7353af46-3abf-4993-b0d1-abc313dc99fb` | 08-30 | DR200S | The starting investigation. Richest DR200 session in the corpus. |
| `eb42c4bb-1da4-43f6-8b54-46b9f9fcb379` | 07-27 | DR200S | Carb fuel weep; the fall-put-away decision. |
| `e082d006-ffbb-4812-b582-c118be98607d` | 07-08 | DR200S | Manuals research pass. |
| `36d08199-c975-4f8f-9ed6-182547b0d1e0` | 08-28 | Bronco | Passenger door panel, bench day. Longest single vehicle session. |
| `d1103fa9-bd6d-4a25-a948-7e87c4766244` | 08-28 PM | Bronco | Panel cleaning + the Amazon order that wasn't. |
| `d49f3af6-a8b7-4e20-81af-e75b24107f4b` | 08-29 | Bronco | Cleaning-product adjudication. |
| `b346626c-a2df-4598-ba26-f9b1914c10c5` | 08-19 | Bronco | The coolant flush, live, in the driveway. |
| `6366e7ee-7db4-48c8-9feb-c1ec2fb8e133` | 07-27 | Bronco | Carpet/headliner/sequencing. |
| `9d8882c7-a837-47d4-a8cd-23a98d2f2be4` | 08-27 | Bronco | Headliner sourcing. |
| `0559c5db-60ad-44be-a69c-5862e5cdb71a` | 08-03 | Bronco | The 3D-model portfolio idea. |
| `da4cf806-aba1-4c40-a31a-133cccac201d` | 08-09 | Bronco | Photo-album narration — **highest-yield NEW-fact session.** |
| `3c7fd59f-7124-4c2a-b2d1-2878275dc10c` | 08-10 | mixed | Photo-burst narration. |
| `6e32e5cc-f433-4775-86ec-6a33896801ff` | 07-10 | GTI | The founding "mine my service-record photos" session. |
| `b4e81051-e041-4e48-bba8-b43c36241b45` | 07-11 | GTI | Express Oil visit ingested. |
| `ba621675-f4b0-41a0-9cd6-757fb56721c4` | 07-23 | GTI | Remaining documents ingested. |
| `b4726cf5-fd8f-44a3-a055-94132246b634` | 08-27 | GTI | Coolant-boiling hypothesis research. |
| `658f7a12-8311-439b-a35f-166b22882c29` | 08-28 | GTI | VW of Marietta receipt; the brake-fluid contradiction. |
| `702a4ee7 · 800a4f5d · f6b68608 · ed04005e · 9d5693b5` | 07-14→07-23 | all | The ChatGPT/Gmail export mines. |

### What I did NOT read

- **Every assistant turn.** I read assistant output only where it was load-bearing (the 8/28
  Amazon cart sequence, the 8/30 crank-budget answer). ~41,900 assistant messages / 27.5 MB
  in the corpus; I sampled perhaps 15 of them in full.
- **All 8,235 sidechain (subagent) messages.** Excluded deliberately — Paul does not speak
  there, and their findings are derivative of sessions I did read. **A subagent research
  finding not folded back into a main session would be invisible to this report.**
- **The five-agent maintenance audit of 2026-07-25** (`d3499a49`) beyond its Paul turns.
- **The 12 Bronco sessions of 2026-07-11 → 07-22** that ingest document photographs — I read
  Paul's turns but not the per-document reads. Those produced `.private/service-records/` and
  are better read there than re-derived from transcript.
- **Anything before 2026-07-03.** See §0.

---

## 2 · Findings, per vehicle

Tags: **DID** (Paul states he did it) · **PLANNED** (discussed, outcome unknown) ·
**ADVISED** (assistant proposed) · **ASKED** (Paul asked, answer unknown/unrecorded).
Marks: **NEW** = absent from `vehicles.json` · **IN-CARD** = already in `vehicles.json` ·
**IN-GUIDE** = in a `guides/` file but *not* on the card.

---

### 2.1 · `dr200s-2017` — Suzuki DR200S, "Blue Thunder"
> ⚠️ NOT `drz400s-2001` ("Desert Storm", the DR-Z400S 398 cc). Paul disambiguated these himself
> on 2026-07-22 (`800a4f5d`): *"booth under is the two hundred, Desert Storm is the four hundred."*
> ("booth under" = a dictation mangle of "Blue Thunder".) **Two findings below were nearly
> misfiled across this line — see D-6.**

**D-1 · No PARK position on the ignition switch — `DID` (read at the machine) · IN-GUIDE, NOT ON CARD**
2026-08-30, `7353af46`, 20:51 ET:
> *"There's no park mode that I can see. Just on, off, and lock"*
Carried at `guides/blue-thunder-starting-diagnosis.md:290`. **Not in `vehicles.json`.** It
matters because a park position is a classic parasitic-drain suspect on a bike that keeps
losing charge, and its absence *eliminates a branch*. A machine fact that only lives in a guide
is one card-read away from being re-asked.

**D-2 · There is an inline fuel filter, and Paul reads fuel level off it — `DID` · NEW**
2026-08-30, `7353af46`, 16:39 ET:
> *"I checked, and the fuel level was low in the fuel filter so I filled it up wit and then ran
> it and drove it around yesterday."*
`fuel filter` appears **nowhere** on the DR200S card and **nowhere** in the starting-diagnosis
guide. The DR-Z400S card records an *APE Racing inline fuel filter* — so there is a real risk
of the two bikes' fitments being conflated. **Unresolved:** whether the 200 has an aftermarket
see-through inline filter fitted, or whether Paul means the sediment bowl / a fuel-level read
somewhere else. **This is an ASK-PAUL, not a fold.**

**D-3 · Petcock left ON RESERVE overnight, then a no-start next morning — `DID` · partially IN-CARD**
2026-08-30, `7353af46`, 16:39 ET:
> *"It ran fine, but I left the Petco on reserve and then it wouldn't start this morning"*
The card carries the *flooding hypothesis* (petcock left on → float needle → overnight flood)
and the guide's standing rule is *"Petcock OFF whenever she is parked."* But the specific dated
observation — **RESERVE specifically, overnight, followed by a no-start** — is not written
down as an episode. It is the single cheapest natural experiment on the flooding branch, and it
already ran once.

**D-4 · Battery pulled and contacts torqued down — `DID` · NEW (undated)**
2026-08-30, `7353af46`:
> *"We did take the bike battery out and really tighten down the contacts."*
Date unknown; Paul reports it as already-done background. Distinct from the 2026-07-21 row
(*Mom cleaned the electrical contacts and reset the contact points*) — that is a different
person, a different action, and a recorded date. **Do not merge them.** If they *are* the same
event, only Paul can say so.

**D-5 · The three-starts-in-an-hour discharge run — `DID` · IN-CARD and IN-GUIDE**
2026-08-30 18:02 ET, quoted here because the card paraphrases it:
> *"so you know went down, fired it up turned it off pretty quickly then went back 30 minutes
> later and did the same thing and then went back 30 minutes later or so, and it started kind
> of clearly struggling the starter, and it barely started seemed like it had low battery"*
And 18:01 ET, the trickle-charger finding:
> *"OK i left it sitting with the trickle charger attached (unpowered) and it seems to have lost charge"*
Both are fully folded. Nothing to do.

**D-6 · ⚠️ TWO ITEMS THAT LOOK LIKE THE 200 AND ARE THE 400 — misfiling hazard**
- 2026-07-22, `800a4f5d`: *"The vacuum padcock works just fine now. And the fuel screw washer is
  back in. The bike is running very well right now."* → this is the **DR-Z400S**; the record has
  it correctly on `drz400s-2001` ("RESOLVED SINCE (Paul-confirmed 2026-07-22)").
- 2026-07-22, `f6b68608`: *"I also repaired the clutch handle on the hundred by extending the
  broken off part with a screw and using zip ties and duct tape"* — dictation says "the hundred";
  Paul corrects himself three minutes later: *"I repaired the four hundred."* The record has it
  on `drz400s-2001` dated 2026-07-21. **Correct. Leave it.**
This is exactly the failure `tools/vehicle-brief.py` (beat 0) exists to prevent, and it shows up
twice in one afternoon.

**D-7 · Fall put-away replaces the spring oil change — `PLANNED` · IN-CARD, quote worth adding**
2026-07-27, `eb42c4bb`, three turns that produced the whole schedule:
> *"I think, realistically, I don't have time. The bikes have been running. We don't put that
> many miles on them, so there's not gonna be an oil change this year."*
> *"If the smart thing to do is to change oil when we put them up, that's even better, and let's
> set a schedule reminder for when you get starting to get too cold to ride. And that's a good
> way to spend a fall evening."*
> *"for both bikes, let's make sure that there's a reminder to do a full oil change and carb
> cleaning maintenance, you know, next spring."*
The card carries the decision. It does not carry the **reason** (low annual mileage), which is
the part that would let a future session re-derive it. `paul-decided 2026-07-27`.

**D-8 · Mom needs a fixed pre-start checklist — `ASKED`, unresolved as an acronym · NEW**
2026-08-30, `7353af46`, 20:52 ET:
> *"What about, like, a very simple acronym or something that would be the initial checklist
> every time mom wants to start the bike? Like, kill switch, choke, gas. right, were the most
> critical things she has to check."*
The guide has a numbered checklist (kill switch → choke → look in the tank). **It has no
acronym.** Paul asked for a mnemonic specifically, for a non-technical rider, and the artifact
that came back was a list. That is a real (small) unmet ask, and it sits on Mom's surface —
which makes it Track A/Track B boundary work, not a pure fleet item.

**D-9 · Carb rebuild kit — `PLANNED`, no order · IN-CARD**
The card's *"Carburetor refurbish — Mikuni BST31SS rebuild kit"* is `planned`, Paul's call
2026-08-30. **No order exists.** Confirmed against the transcript: nothing in the corpus shows a
kit being bought. Absence is not evidence of non-purchase, but there is also no stated intent to
order beyond "do it at the next decommission."

---

### 2.2 · `bronco-1989` — 1989 Ford Bronco, "Bolores"

**B-1 · ⭐ Body-to-tailgate wiring harness repair — `DID` · NEW · date unknown**
2026-08-09, `da4cf806`, 02:33 ET, narrating the tailgate photo cluster:
> *"thirty three through thirty six were repairing the wiring. I found a crimp in some of the
> wires and some signs of oxidation where the wiring harness goes from the body into the
> tailgate, which is a common crimp point, and I did some wiring repair there."*
`crimp` = 0 hits in `vehicles.json`. `oxidation` = 1 hit, and it is about **paint**, not wiring.
This is a completed electrical repair at a known failure point, and the record does not have it.
It is directly relevant to the tailgate/rear-window electrical work that *is* recorded
(2025-10-24 Dorman 742-251 lift motor; 2025-10-15 Dorman 901-302 switch) — plausibly the same
campaign, but **I cannot date it and will not infer it from the photo cluster.**

**B-2 · Ashtray removed, cigarette-lighter power outlet replaced — `DID` · NEW · date unknown**
Same message, same session:
> *"twenty nine thirty one thirty two. We're all about removing the ashtray and replacing the
> cigarette lighter power outlet there because that didn't work."*
`ashtray` and `cigarette` = 0 hits in `vehicles.json`. A completed interior electrical repair
with a stated failure ("that didn't work") and no row.

**B-3 · Non-working amp found and uninstalled — `DID` · NEW · date ≈ head-unit install**
2026-07-14, `702a4ee7`, 20:18 ET:
> *"There was an existing amp that didn't seem to work that I uninstalled. And, yes, that's when
> I installed the head unit and the speakers together"*
`vehicles.json` has *"Audio — head unit + speakers"* as `done` and *"Amp + subwoofer — three
paths (Phase 5)"* as `long-term`. Neither records that **a prior-owner amp was present, was
tested as non-working, and was removed.** That matters for the Phase-5 amp decision — it means
there is already amp wiring in the truck, and it means one amp position has already been proven
dead. Paired with the 7/14 negative: *"no, I've not bought an Amp or Subs."*

**B-4 · Rear carpet stripped completely; door switches pulled for diagnosis — `DID` · IN-CARD (consequence), NEW (the acts)**
Same 8/09 message:
> *"Number fifteen and sixteen are both pictures of the passenger door. Automatic window and door
> lock switches. same for eighteen. That's when I was taking them out to kinda diagnose them.
> twenty one through twenty four. We're me taking out the rear carpet completely."*
The card states the *state* ("ALL THE INTERIOR CARPETING IS ALREADY OUT", Paul, 2026-07-27) but
not that the passenger-side window and lock switches were removed and bench-diagnosed. Relevant
to the open `Driver door power lock — diagnosing` item, which is about the **driver** side.

**B-5 · Latch/striker bushings across door and tailgate — `DID` · partially IN-CARD**
Same session, 02:48 ET:
> *"three twenty three three forty two was replacing the latch bushings for where the door and
> the tailgate latches. Those... that striker plastic housing or whatever that is that ensures
> the door doesn't rattle."*
The card has the **tailgate** striker bushing (Dorman 38424, 2025-12-22). Paul's phrasing says
**door and tailgate**. Either the door bushings are a second undocumented job, or he is
describing the one job loosely. **Ask; do not fold.**

**B-6 · ⭐ Paul's own dating rule — `paul-stated`, and it should be doctrine · NEW as a stated rule**
2026-08-09, `da4cf806`, 02:50 ET:
> *"I think the twelve twenty two record is just based on receipts though. Right? So I didn't
> necessarily buy it and then have it shipped to me and installed the same day. So where we have
> photos of the actual installed at timing should, you know, be marked and supersede the purchase
> date. But let's keep track of the purchase date and our dataset in case these questions come
> up again, so it's all clear."*
This is a **rule about the record's own grain** — install date ≠ purchase date, photo evidence
outranks receipt date for install, and both are kept. Several Bronco rows are dated by receipt
(2025-11-02, 2025-11-03, 2025-11-20, 2025-11-23, 2025-12-22, 2025-10-08, 2025-10-15). Under
Paul's own rule those are **purchase dates wearing install-date clothes.** I did not audit them.

**B-7 · Coolant flush, done live — `DID` · IN-CARD, exhaustively**
2026-08-19 `b346626c` → 08-21 `57150bb3` → road-verified 08-24. The card's
`sr-2026-08-19-coolant-drain-flush-refill` row is one of the most complete in the repo. Quotes
worth preserving as provenance for figures the card asserts:
> *"It seems okay. Um, it's not really rusty or milky or anything, just a diluted kinda green.
> Um, just to note, the current mileage is one ten three two point five."* (20:43, the clean-drain
> three-way negative + the 11,032.5 odometer)
> *"Okay. I put in the full bottle of concentrate, the full jug. I don't have distilled water."* (22:12)
> *"Okay. I added three quarters of the remaining, uh, jug."* (22:19)
> *"The truck has been running. It's warm. The upper tube from the radiator is hot to the touch.
> The level of the coolant is stable, and there's hot air coming out."* (08-21 19:15 — the three-signal burp confirmation)
Nothing to add. **The card is more careful than the transcript** — it holds the glycol % as
arithmetic, not a measurement, which no turn in the conversation forced it to do.

**B-8 · Front-left tire on the F-150, not the Bronco — `DID` · IN-CARD (on `f150-2006`)**
2026-08-19, 21:57 ET Paul says *"the front left tire on the truck was low, and I filled it up
today. That one fifty."* — mid-Bronco-job, so "the truck" was ambiguous; he corrects at 22:03:
*"the F150 is what I'm talking about the gray F150."* The record already documents the misfile
and the correction, and correctly refuses to guess the pressure. **A clean example of the
record catching its own error; leave it.**

**B-9 · Passenger door panel bench day — `DID` · IN-CARD**
2026-08-28, `36d08199`. The washer removal, in his words:
> *"it's a very thin washer and very hard to grab onto it with pliers so I tried there didn't
> really seem to budge easily, but I didn't want to start pulling and twisting at the panel too much"*
> *"OK it twisted off!"*
> *"that's cured superglue, which I've since removed. So it was the ring of superglue that was
> sitting underneath the washer, and I've since scraped it off, and it's clean."*
Fully in `sr-2026-08-28-passenger-door-panel-bench`.

**B-10 · Panel cleaning method — `DID` · IN-GUIDE, NOT ON CARD**
2026-08-28 18:38 ET, `d1103fa9` (a *separate* session from the bench session, started after it):
> *"I peeled off a bunch of the residue glue that was there and then I've gone over it now a
> couple times with just a rag and then a core sponge using just dawn soap and then wiping it all
> off real well and going back over and then finally used a little water down isopropyl alcohol
> to get a little more of the sticky stuff off and now it's pretty dang clean I mean, I don't
> think it makes sense to just scrub it all the way down at some point it just damages the door"*
`guides/bolores-door-panel-repair.md` carries it (lines 543, 653, 674). The **card's
2026-08-28 service row does not** — that row stops at "panel off, washer removed, findings."
The cleaning is a distinct completed step done the same evening.

**B-11 · CA ring sanded off; bracket bond is next — `DID` + `PLANNED` · IN-GUIDE**
2026-08-29, `d49f3af6`:
> *"Okay. I've got the glue off, and we'll continue to check that it's flat. That dark line is
> part of the pad, not the panel. This panel, the passenger side panel is in really good shape
> relative to the driver side panel."*
> *"I'm gonna do one more clean, sandpaper the corner after verifying there are no scratches
> there, and I'll glue in that support brace."* (`PLANNED` — no confirmation in the corpus)
Guide has it at line 244 and the 08-29 bench section. **No service row on the card for 08-29.**

**B-12 · ⭐⭐ THE ORDER THAT WASN'T — `DID`, and it validates the parts rule**
2026-08-28, `36d08199` 14:44 ET: *"OK I just ordered them"* (butyl tape, neoprene ×2, clips ×2).
2026-08-28, `d1103fa9` 20:04 ET, ~5½ hours later:
> *"I think something went wrong with my amazon order. It got partially cancelled. I seem to be
> missing the butyl tape"*
20:12 ET: *"OK I just orderd it"*.
`guides/bolores-door-panel-repair.md:456` records the resolution, and it is **worse than a
cancellation**:
> *"Paul reported a 'partial cancellation'; the browser check found **no cancellation at all** —
> the tape and the clips had **never been placed**. Both were still sitting in the active cart."*
Net: **the Icyhaws clips were never ordered at all**, and the guide corrects the record.
This is [[reference_parts_record_under_reports]] measured live, in one afternoon, in both
directions — a stated order that never happened, *and* a stated cancellation that never
happened. The order numbers are filed in `.private/service-records/TOOLS.md`.
**Nothing here needs doing. It needs quoting, forever, as the case study.**

**B-13 · Headliner — `PLANNED`/`ASKED` · IN-CARD (the 32 KB item)**
2026-08-27 `9d8882c7` + 2026-08-28 `a168e341`. Paul on the phone with LMC:
> *"OK I'm on the phone with LMC now. ON hold. What's the link to the page with the headliners?"*
> *"I started to check out in on LMC and this is kind of what I got. Basically you can see the
> headliner saddle 335 and with other items included it's 9725 for"* (dictation garble — the
> shipping figure did not transcribe cleanly)
> *"we definitely have kind of come to a conclusion on LMC being the place to buy the headliner
> and saddle being the right color ... these watches [swatches] are on the way"*
**NOT ORDERED.** Swatches stated as on the way — no order number in the corpus for either.

**B-14 · Clear-coat stopgap — `ASKED`, open · NEW**
2026-08-31, `7e7a625b`, 23:44 ET:
> *"the clearcoat is partially fading on the hood of the car and I see advertisement for like
> poppies patina and wipe on clearcoat and I wonder if that's a stopgap solution until I can
> actually get it really ready for a full paint job"*
`clearcoat` (one word) = 0 in `vehicles.json`; the paint block discusses *failing clear coat* as
the reason for the full respray but carries **no stopgap-preservation option**. This is a live
question asked 36 hours ago with no recorded answer in the corpus.

**B-15 · "LMC order bank" — `PLANNED`/started**
2026-08-18, `d72bad07`: *"I think I want to start an LMC order bank"* →
`.private/service-records/bronco-1989/ORDER-BANK.md` exists. Closed.

**B-16 · Seats already reupholstered by a prior owner — `DID` (by someone else) · IN-CARD**
2026-07-26, `f02cf158`: *"They've definitely been reupholstered at some point."* Card has it
under the driver-seat upholstery item (`quoting`).

**B-17 · Jump starter bought and RETURNED — `DID` · NEW · parts-record relevant**
2026-07-22, `f6b68608`, 20:17 ET:
> *"The jump starter, I think I bought it, and it was too small for the Bronco, so I returned it."*
Note the hedge — *"I think I bought it."* This is a **return**, i.e. an over-report the parts
record could otherwise carry as an owned item. It does not appear in `vehicles.json`. (Separately,
an AVAPOW jump pack **is** in the DR200's kit per the card — a different unit, on a different
machine. **Do not merge.**)

**B-18 · The 3D interactive-Bronco idea — `PLANNED`, filed as an idea**
2026-08-03, `0559c5db`:
> *"you think we can make a three d model of the dirt bikes? We're the Bronco somehow and then be
> able to click on different parts and show details of the repairs that I've done ... Could be a
> cool showpiece for, like, my portfolio."*
> *"Let's file this in a way as an idea within Fernwood, but we've got lots of other stuff to do.
> So first feasibility study."*
Repeated 2026-08-03 in `a8a12ced`. **Portfolio-adjacent, not maintenance.** Flagged because it is
the one place Paul names the *audience* for this whole record.

---

### 2.3 · `gti-2016` — 2016 VW Golf GTI (MK7 Autobahn, manual, APR Stage 1)

**G-1 · ⭐ DIY coolant diagnosis on/around 2025-10-20 — `DID` (hedged) · NEW**
2026-08-10, `3c7fd59f`, 23:00 ET, narrating a dated photo burst:
> *"Monday twentieth of October twenty twenty five. I was working on my GTI trying to diagnose a
> coolant[,] if memory serves, but that's my GTI and me working on it in the parking area."*
The card's coolant item lists four observations: 2025-09-15 (Cannon invoice), 2026-02-02 (tank
swap), 2026-07-11 (Express Oil pressure test), 2026-08-28 (pink under the car).
**2025-10-20 is not among them.** If real, it pushes the DIY investigation back ~3½ months before
the February tank swap, and it means the loss has been actively chased for **at least ten
months**, not seven.
⚠️ **Two reasons not to promote this on its own:** Paul hedges with *"if memory serves"*, and the
date comes from photo metadata narrated aloud, not from the world. **Photo-side confirmation
exists** (this was a photo-organizer burst review) — that is the cheapest way to firm the date;
the *subject* still rests on Paul's memory.

**G-2 · Locksmiths called first and could not cut this key — `DID` · NEW**
2026-07-14, `702a4ee7`, 20:40 ET:
> *"Alright. The locksmiths that I've called are not able to make this kind of key. So what should
> I be looking at for pricing from a VW dealership all in?"*
And 20:33, working the key's own markings:
> *"I read the FCC ID as best I can. ID n p g e s one two p q one. That's FCC ID n b g e s one two
> p q one. Maybe that q is a zero. Maybe the g is something else."*
`locksmith` = 0 hits in `vehicles.json`. The card has the 2026-08-04 prepay ($220.53) and the
2026-08-26 cut-and-program. It does **not** record that the aftermarket route was tried and
closed first — which is the entire justification for paying dealer rate, and the thing anyone
re-reading this in two years would otherwise second-guess. **Six weeks of latency between the
locksmith dead-end (7/14) and the dealer order (8/04) is also unexplained in the record.**

**G-3 · Cone-strike repair, in his words — `DID` · IN-CARD**
2026-07-22, `f6b68608`, 19:53 ET:
> *"had an incident where a traffic cone fell off the back of a truck in front of me and got
> sucked under the GTI and did some damage to the front grill and under panels, um, but I... a
> lot a lot of the panel attachment points got snapped, so it didn't get put back together, but
> I kind of forced it into place using some washers on all the attaching screws, um, duct tape
> and elbow grease. But it's pretty solid as far as a fix goes and avoids having to buy a bunch
> of new body parts."*
Card has the 2026-07-21 row. This quote is the **repair-vs-replace reasoning** ("avoids having
to buy a bunch of new body parts") that the row summarizes. It also cross-references the open
`cycle/requests.jsonl` entry about the ten unread 07-21 GTI repair photos.

**G-4 · Spark plugs already installed, research done afterwards — `DID` + `ADVISED` · IN-CARD**
2026-07-14, `ed04005e`, 14:32 and 14:46 ET:
> *"Those are spark plugs for my GTI since it's got a two, and I use those."*
> *"They're already installed in the car and doing well, um, but let's do the research to inform a
> reminder for the next time I change the spark plugs and so on."*
Produced `.research/2026-07-14-gti-spark-plug-setup.md` and the card's NGK R7437-8 / 0.024" gap /
20k-mile entry. **Note the direction of travel: the part went in first, the spec was researched
second, for next time.** That is a real and recurring pattern (see §4, S-6).

**G-5 · Express Oil visit — `DID`, and Paul challenged the model's own read — `IN-CARD`**
2026-07-11, `b4e81051`:
> *"OK took my GTI to express oil change and they gave it a full check over and share that the
> occasional coolant top off is somewhat normal for the car (look into that and see if that's
> true) they hooked it up to a pressure tester and found no leak"*
> *"WHere are you getting the empty resrvoir fact from?"*
> *"Let's note it as an observation. But I think the fact express oil change conducted a pressure
> test and didn't find a leak is a powerful and important observation"*
> *"I think that was in relation to how they replaced the brake fluid, right? I don't think there
> was any work done on the pads. Review the entire service record, did they inspect the pads?"*
All folded. ⭐ Note the last one: **on 2026-07-11 Paul himself flagged that no pad inspection was
on that ticket** — the exact gap that two dealers later closed in the other direction. The card's
rear-brake item says the Express Oil checklist "measures brake FLUID LEVEL, not pad thickness."
**That caveat originates in Paul's question, not in the analysis.**

**G-6 · The brake-fluid contradiction — `DID` (the visit), `PLANNED` (the confrontation) · IN-CARD**
2026-08-28, `658f7a12`, 14:00 ET — the whole finding in one turn:
> *"I asked him about the coolant they offered you know a full diagnostic which would've cost $220
> which I declined so they did the multi point inspection ... there is some coolant I see you
> still under my car and I had to refill it recently like a week or two ago or top it off ... they
> also pointed out that my brake fluid is really black which I would like to better understand how
> to inspect it myself and what that makes me wonder is whether express oil made some kind of
> mistake and didn't perform the service they said on my car ... the value is really checking it
> against espresso oil logically."*
14:22 ET, his own eyeball read:
> *"it's clearly the brake fluid reservoir and not the cooling reservoir, and it's a very dark
> gray, if not black color."*
14:32 and 14:05 ET — the **unresolved** action:
> *"is it worth just taking it into Express oil and talking to them? I think that's my first
> inclination is to say, hey. Like, they probably don't want this to get out or whatever ... I'm
> sure this was just an honest mistake. Let's make it right. Maybe I can get a partial refund for
> them to do my brakes for free or something."*
> *"I just don't wanna get into a big confrontation, but I do wanna be sure that I get everything
> taken care of."*
Card is current. **The Express Oil conversation has not happened** — `PLANNED`, still open.

**G-7 · Coolant is PINK — `DID` (observation) · IN-CARD**
2026-08-28, `658f7a12`, 15:02 ET:
> *"It's definitely a pink color when I see it. Um, it's not bright pink. It's watery, but it is
> a pink coolant color. I'll get a picture of the coolant later for you to look at."*
⚠️ **The photograph he promised does not appear anywhere in the corpus.** The card treats the
colour as settled on the strength of this verbal read plus the elimination argument (manual → no
ATF; electric steering → no PSF). That reasoning is sound, but **the confirming photo is an
open loop that nobody closed.**

**G-8 · The tune-runs-hotter coolant hypothesis — `ASKED` → `ADVISED` · IN-RESEARCH**
2026-08-27, `b4726cf5`, 22:25 ET:
> *"if my engine is running hotter cause it's tuned do I need a different kind of nonstop coolant
> to rent this from expanding too much and boiling over and leaking out of the [reservoir]"*
→ `.research/2026-08-27-gti-coolant-boiling-hypothesis.md`. Paul's own disposition, 00:37:
> *"OK save this research to our GTI database. No need to update the card at this point"*
**`paul-decided`: research filed, card deliberately NOT updated.** A future sweep that finds
this research and folds it into the card would be *overturning a decision*, not filling a gap.

**G-9 · New expansion-tank cap fitted — `DID` · card asks the question it answers**
2026-08-28, `b4726cf5`, 00:39 ET:
> *"I got a new cap from AutoZone or something like that."*
The card's coolant item lists as "STILL UNKNOWN and all free … **what is stamped on the cap now
fitted**." Paul's answer is partial (an AutoZone cap, brand/rating unstated, date unstated) but
it is not nothing — it establishes the cap is **aftermarket and not original**, which was one of
the two things the card wanted to know. `AutoZone` = 0 hits in `vehicles.json`.

**G-10 · Registration/emissions clock — `DID` (established) · IN-CARD**
2026-07-11, `b4e81051`: *"My birthday is June third, so both the GTI and [Bolores] are due"*; and
*"the Tiguan and f one fifty are in my mom's name … Moms burthday is September 21st."* Both
folded into the `registration` blocks.

---

## 3 · Candidate `cycle/requests.jsonl` entries — **NOT APPENDED**

Only **NEW + DID** items qualify. Everything `PLANNED`, `ADVISED` or `ASKED` is excluded by rule.
Paste-ready; a human appends. Each carries its own evidence and its own limit.

```json
{"from":"conversation-corpus","what":"BRONCO — BODY-TO-TAILGATE WIRING HARNESS REPAIR IS COMPLETED WORK WITH NO ROW. Paul, narrating his own photos 2026-08-09 (session da4cf806-aba1-4c40-a31a-133cccac201d, 02:33 ET): 'thirty three through thirty six were repairing the wiring. I found a crimp in some of the wires and some signs of oxidation where the wiring harness goes from the body into the tailgate, which is a common crimp point, and I did some wiring repair there.' Grep: 'crimp' = 0 hits in vehicles.json; the single 'oxidation' hit is about PAINT. ⚠️ DATE UNKNOWN — he is describing a photo cluster, not stating a date, and the cluster date was not read out. Plausibly part of the Oct–Dec 2025 tailgate/rear-window campaign (2025-10-24 Dorman 742-251 lift motor, 2025-10-15 Dorman 901-302 switch) but THAT IS INFERENCE, not evidence. What to do: get the date off the photos, then add a serviceHistory row. Do not date it from the neighbouring rows.","opened":"2026-09-01"}
{"from":"conversation-corpus","what":"BRONCO — ASHTRAY REMOVED AND CIGARETTE-LIGHTER POWER OUTLET REPLACED, completed, no row. Same message, same session (da4cf806, 2026-08-09 02:33 ET): 'twenty nine thirty one thirty two. We're all about removing the ashtray and replacing the cigarette lighter power outlet there because that didn't work.' Grep: 'ashtray' = 0 and 'cigarette' = 0 in vehicles.json. A stated failure ('that didn't work') and a stated fix. ⚠️ DATE UNKNOWN, same reason as the harness item — and the two are adjacent photo clusters, so they may or may not be the same session at the truck.","opened":"2026-09-01"}
{"from":"conversation-corpus","what":"BRONCO — A PRIOR-OWNER AMP WAS PRESENT, TESTED NON-WORKING, AND REMOVED. Paul 2026-07-14 (session 702a4ee7-6174-4b5c-90f8-6ea5dc6579a8, 20:18 ET): 'There was an existing amp that didn't seem to work that I uninstalled. And, yes, that's when I installed the head unit and the speakers together so you can look at that conversation to deduce the timing.' vehicles.json has 'Audio — head unit + speakers' as done and 'Amp + subwoofer — three paths (Phase 5)' as long-term; neither records the removed unit. WHY IT MATTERS FOR PHASE 5: it means amp wiring may already be run in this truck, and one amp position has already been proven dead. Paired negative, same session: 'no, I've not bought an Amp or Subs.' ⚠️ Date = 'the same time as the head-unit install' per Paul; that install's own date should be read off the record, not assumed.","opened":"2026-09-01"}
{"from":"conversation-corpus","what":"BRONCO — A JUMP STARTER WAS BOUGHT AND RETURNED (over-report guard). Paul 2026-07-22 (session f6b68608-b0d8-4b1d-8639-43f0260e3b53, 20:17 ET): 'The jump starter, I think I bought it, and it was too small for the Bronco, so I returned it.' NOTE HIS HEDGE — 'I think I bought it.' This is a RETURN, i.e. exactly the direction the parts record has been measured over-reporting. It is not in vehicles.json, which is currently correct; file it so a future receipt sweep that finds the purchase does not book it as owned. ⛔ DO NOT MERGE with the AVAPOW jump pack recorded in the DR200S kit — different unit, different machine.","opened":"2026-09-01"}
{"from":"conversation-corpus","what":"BRONCO — PANEL CLEANING (2026-08-28 evening) IS IN THE GUIDE BUT NOT ON THE CARD. Paul, session d1103fa9-bd6d-4a25-a948-7e87c4766244, 18:38 ET — a SEPARATE session started after the bench session closed: 'I peeled off a bunch of the residue glue that was there and then I've gone over it now a couple times with just a rag and then a core sponge using just dawn soap and then wiping it all off real well and going back over and then finally used a little water down isopropyl alcohol to get a little more of the sticky stuff off and now it's pretty dang clean.' guides/bolores-door-panel-repair.md carries this (lines 543/653/674); vehicles.json's sr-2026-08-28-passenger-door-panel-bench row stops at panel-off + washer + findings. Also uncarded: the 2026-08-29 bench work (session d49f3af6, 'I've got the glue off' — the cured CA ring sanded off the torn screw hole). ⚠️ THE PATTERN, not just the gap: hands-on steps are landing in guides and not in serviceHistory, so the card under-reports how far this job has actually progressed.","opened":"2026-09-01"}
{"from":"conversation-corpus","what":"GTI — LOCKSMITH ROUTE WAS TRIED AND CLOSED BEFORE THE DEALER KEY. Paul 2026-07-14 (session 702a4ee7-6174-4b5c-90f8-6ea5dc6579a8, 20:40 ET): 'Alright. The locksmiths that I've called are not able to make this kind of key. So what should I be looking at for pricing from a VW dealership all in?' Grep: 'locksmith' = 0 in vehicles.json. The card records the 2026-08-04 prepay ($220.53) and the 2026-08-26 cut-and-program but not WHY the dealer was the only route — which is the whole justification for dealer rate. Same session 20:33, he read the key's own FCC ID off the fob and flagged his own uncertainty on two characters ('Maybe that q is a zero. Maybe the g is something else') — a model-read value that was never cleared. ⚠️ ALSO UNEXPLAINED: six weeks between the locksmith dead-end (7/14) and the order (8/04).","opened":"2026-09-01"}
{"from":"conversation-corpus","what":"GTI — A DIY COOLANT DIAGNOSIS APPEARS TO PREDATE EVERY OBSERVATION ON THE CARD. Paul, narrating a dated photo burst 2026-08-10 (session 3c7fd59f-7124-4c2a-b2d1-2878275dc10c, 23:00 ET): 'Monday twentieth of October twenty twenty five. I was working on my GTI trying to diagnose a coolant[,] if memory serves, but that's my GTI and me working on it in the parking area.' The card's coolant item lists 2025-09-15, 2026-02-02, 2026-07-11 and 2026-08-28 — NOT 2025-10-20. If real it means the loss has been actively chased for ~10 months, not ~7, and it puts a DIY attempt 3.5 months BEFORE the Feb-2026 expansion-tank swap. ⛔ DO NOT FOLD AS-IS: Paul hedges ('if memory serves'), and the DATE comes from photo metadata read aloud while the SUBJECT comes from memory. The date is cheap to firm from the photo side (this was a photo-organizer burst review); the subject still needs Paul.","opened":"2026-09-01"}
{"from":"conversation-corpus","what":"DR200S — TWO MACHINE FACTS THAT LIVE ONLY IN THE GUIDE OR NOWHERE. (1) NO PARK POSITION on the ignition switch. Paul at the machine 2026-08-30 (session 7353af46-3abf-4993-b0d1-abc313dc99fb, 20:51 ET): 'There's no park mode that I can see. Just on, off, and lock.' Carried at guides/blue-thunder-starting-diagnosis.md:290; ABSENT from vehicles.json. It eliminates a parasitic-drain branch on a bike that keeps losing charge — a card-only reader would re-ask it. (2) AN INLINE FUEL FILTER, used as the fuel-level tell. Same session, 16:39 ET: 'I checked, and the fuel level was low in the fuel filter so I filled it up.' 'fuel filter' = 0 hits on the DR200S card AND 0 in the starting guide. ⚠️ DISAMBIGUATION HAZARD: the DR-Z400S card records an APE Racing inline fuel filter, so this is exactly the kind of fact that migrates to the wrong bike. ASK PAUL what is fitted on the 200 before writing anything.","opened":"2026-09-01"}
{"from":"conversation-corpus","what":"DR200S — BATTERY PULLED AND CONTACTS TORQUED, undated, reported as already-done. Paul 2026-08-30 (session 7353af46, 16:39 ET), closing his opening account: 'We did take the bike battery out and really tighten down the contacts.' ⛔ DO NOT MERGE with the 2026-07-21 serviceHistory row ('Mom cleaned the electrical contacts and reset the contact points'). Different actor ('we'), different action (removing the battery and torquing terminals vs cleaning contact points), and the 7/21 row has a date this does not. If they are the same event only Paul can say so — and if they are NOT, the record is missing an electrical intervention that sits directly on the open charging-system investigation.","opened":"2026-09-01"}
```

**Deliberately excluded from the above, and why:**

| Item | Why not filed |
|---|---|
| B-14 clear-coat stopgap (`poppies patina` / wipe-on clear) | `ASKED` 2026-08-31, no outcome. A live question, not a fact. Belongs on BACKLOG.md if anywhere. |
| G-6 the Express Oil conversation | `PLANNED`, and it is Paul's to have. Filing it would put a decision he has not made into a fact store. |
| B-13 headliner / swatches | `PLANNED`. Stated as "on the way" with no order number — the exact thing rule 3 forbids promoting. |
| D-9 carb rebuild kit | `PLANNED`, already on the card as `planned`. Nothing changed. |
| B-5 door latch bushings | Genuinely ambiguous between "one job described loosely" and "a second undocumented job." An ask, not an entry. |
| B-6 Paul's install-date-supersedes-purchase-date rule | Not a vehicle fact — it is doctrine about the record. See §5. |
| Everything about the DR-Z400S | Out of scope for this brief, and correctly recorded already. |

---

## 4 · The interaction proof points — **how this work actually gets done**

This is the second half of the ask and, I think, the more durable half. Ten recurring shapes,
each with a named example. They are not stylistic observations; each one is a *different
division of labour* between Paul and the assistant, and several are shapes the assistant could
not have imposed — Paul invented them.

### S-1 · DIAGNOSE-FROM-SYMPTOM, with the symptom explicitly distrusted
**Example: DR200S starting, 2026-08-30 (`7353af46`).**
Paul does not open with "fix this." He opens by naming the epistemic problem:
> *"I'm trying to figure out if we can do a systematic check somehow to really establish some
> facts cause she's potentially mixing up different issues"*
and then supplies the counterexample himself — *"sometimes it's hard to tell whether it's just
low battery because mom's been trying to fire it with low gas."*
The output is **not a diagnosis.** It is a numbered test protocol with pass bands (T1 resting
voltage ≥12.4 V, T2 cranking voltage collapse below ~9.5 V, T3 charging 13.0–16.0 V @ 5,000 rpm,
T5 parasitic draw), a **printable test sheet**, and a **results log that records the tests that
have NOT been run.** The card says so out loud: *"These are OBSERVATIONS, NOT DIAGNOSES — no test
in the protocol has been run yet."*
**Why this is the strongest proof point in the corpus:** the same symptom ("won't start") has
resolved to three unrelated causes on this one bike in sixteen months — fuel (2025-05-09),
electrical contacts (2026-07-21), kill switch (undated). The system *knows that about itself*
and refuses to let the fourth episode inherit a verdict. Paul's instruction was
`"yeah, let's definitely go ahead and test all this. I mean, record it."` — **test and record,
as one instruction.**

### S-2 · LIVE JOB COACHING — the assistant as the second person in the driveway
**Example: Bronco coolant flush, 2026-08-19 (`b346626c`).**
Paul is holding tools. The turns are short and sequential:
> *"I used the pet cock. How can I drain the rest?"* → *"Okay. I've got the Bronco running with
> the heat on now."* → *"Okay. Tell me what to do next."* → *"How do I know when it's full? or
> when there's enough"*
This is a **manual that answers back**, and the value shows up in the *stop*: with no distilled
water on hand, tap was declined and the job was **paused mid-refill with the exact state of the
truck written down** — 7 qt neat concentrate in, ~2 qt short, engine not started, cap sitting
loose. Two days later (`57150bb3`) it resumed and closed on a three-signal burp confirmation that
Paul read off the truck.
Same shape at the bench, 2026-08-28: *"it's a very thin washer and very hard to grab onto it with
pliers"* → a technique (shear cyanoacrylate **in plane**, don't peel) → *"OK it twisted off!"*
**within eight minutes.**

### S-3 · PART-SOURCING, with the purchase gated on Paul's click
**Example: Bronco door-panel materials, 2026-08-28 (`36d08199`).**
> Paul: *"Can you go and look at those? see if you can find recommendations on Amazon for me to buy."*
> Paul: *"add those three to my amazon cart"*
> Assistant: *"Adding to cart — not checking out; the purchase stays your click."*
Then Paul pushes back on two dimensions (a colour: *"Is there a black version of the tape we can
use?"*; and quality), the cart is **revised in place** with the trade stated honestly
(*"Dicor has the deeper reputation … that's the honest trade you're making for black"*), and only
then: *"OK I just ordered them."*
⭐ **The best moment is the one that removed a purchase:** the assistant found Paul already owned
36 sq ft of butyl deadener bought 2026-02-23, and said *"Buy no butyl … the record was the thing
that was wrong, not you."* **Part-sourcing that ends in "you already have this" is the shape
working, not failing.**

### S-4 · INTERPRET-AN-INVOICE, and adjudicate two shops against each other
**Example: the brake-fluid contradiction, 2026-08-28 (`658f7a12`).**
Paul's own framing is the method statement:
> *"there's value [in] having this Volkswagen inspection, but the value is really checking it
> against espresso [Express] oil logically."*
Two receipts, 46 days and 1,084 miles apart, disagree. The assistant reasons from **mechanism** —
brake fluid is a static hydraulic column, so there is no path by which a freshly exchanged
reservoir re-darkens in six weeks — and the record **reopens an item that had been marked done.**
It also holds the opposite caution in the same breath: *"'really black' is a subjective call from
someone selling a $264.99 flush."*
Earlier instance of the same shape, 2026-07-11: Paul reads the ticket back at the model —
*"WHere are you getting the empty resrvoir fact from?"* — and demotes a claim to an observation.

### S-5 · DECIDE-REPAIR-VS-REPLACE, and SEQUENCE A BUILD
Three clean examples, one of which later **broke**, which is the interesting part.
- **Handlebars (DR200S):** a re-bent steel bar is permanently weakened → replace beats
  re-straighten. Closed 2026-07-12.
- **Cone strike (GTI):** *"I kind of forced it into place using some washers … duct tape and elbow
  grease. But it's pretty solid as far as a fix goes and avoids having to buy a bunch of new body
  parts."* Repair chosen explicitly over parts.
- **Door panels (Bronco):** Paul states a physical constraint the assistant could not have known —
  *"I really wanna try to minimize the amount of times I'm taking them on and off because it's old
  plastic, and it just introduces more chances of breaking"* — and gets a **one-removal protocol**
  built around it. ⭐ **Then on 2026-08-28 he killed it himself:** *"we're gonna do... restore the
  door panels, put them on, and then just be ready to take them off when there's a full painting,
  but we're not gonna wait on the full painting."* The optimum was arithmetic resting on
  "the booth is near-term", and that premise died. **The record says so, in those words.**

### S-6 · PREP-ME-FOR-THE-SHOP (and, afterwards, TELL-ME-WHAT-I-BOUGHT)
Two directions across the same doorway.
- **Before:** 2026-07-08 *"do you have estimates for what you expect these prices to be at express
  oil versus auto[bahn] so I can sense check initial quotes"*; 2026-07-09 *"I want to call express
  oil change … so you can help me prep an interview guide."* → `.research/2026-07-09-gti-express-oil-call-guide.md`.
  2026-08-28, rehearsing the awkward one: *"I just don't wanna get into a big confrontation, but I
  do wanna be sure that I get everything taken care of."*
- **After:** 2026-07-14, the plugs are **already in the car** — *"They're already installed in the
  car and doing well, um, but let's do the research to inform a reminder for the next time."*
**The research is for the next time, not this time.** That is a maintenance *record* posture, not
a shopping posture, and it is the single clearest signal that Paul is building an asset here
rather than solving today's problem.

### S-7 · NARRATE-MY-PHOTOS-INTO-A-RECORD — the capture path, and it is AI-free
**Example: `da4cf806` 08-09, `3c7fd59f` 08-10, `cc490cbb` 08-14, `6d181dec` 08-17, `22d3ba25` 08-29.**
Paul reads a contact sheet aloud, by index, in one breath:
> *"Number fifteen and sixteen are both pictures of the passenger door. Automatic window and door
> lock switches. same for eighteen. That's when I was taking them out to kinda diagnose them.
> twenty one through twenty four. We're me taking out the rear carpet completely."*
**This is where undated DIY work enters the record at all** — and it is the source of B-1, B-2 and
B-4 in §2, three completed repairs the receipt trail could never have produced. The model does
not read the photos for facts; Paul supplies the meaning and the model files it. That is exactly
the *capture stays AI-free* stance, arrived at in practice.
⭐ **And it produced its own governing rule** (B-6): *"where we have photos of the actual install
timing should … supersede the purchase date. But let's keep track of the purchase date."*

### S-8 · CHALLENGE-THE-MODEL — Paul as the instrument of last resort
The corpus is dense with this, and the record is visibly shaped by it:
| Date | Paul | What it killed |
|---|---|---|
| 2026-08-30 | *"There is no kickstarter ont he 200 or the 400 they both are electric start only"* | A manual-sourced spec, an entire diagnostic branch, and the assumption that the on-disk manual matched the bike. **Spawned beat 0 of the fleet loop.** |
| 2026-07-11 | *"WHere are you getting the empty resrvoir fact from?"* | A vision read being carried as fact. |
| 2026-07-29 | *"the truck has working AC, so that would imply the AC has not been removed. Right?"* | Half of the 2018 emissions-delete assertion. |
| 2026-08-29 | *"That dark line is part of the pad, not the panel."* | A crack that did not exist. |
| 2026-07-22 | *"booth under is the two hundred, Desert Storm is the four hundred."* | A vehicle-identity collision, pre-emptively. |
**The direction is always the same: a confident model claim, one physical look, claim dies.** The
fleet loop's beat 0 and beat 4 exist because of this pattern, not despite it.

### S-9 · STATED-ORDER vs ORDER-NUMBER — the shape that caught itself
2026-08-28, in a single afternoon (§2, B-12): *"OK I just ordered them"* → *"It got partially
cancelled"* → the browser check finds **no cancellation and no order** — the tape and clips had
never been placed. The guide's conclusion is the reusable artefact:
> *"a stated order is a hypothesis until the order number is read."*
**Both error directions in one event**, on the same axis the parts record has been measured
failing on. This is the case study to keep.

### S-10 · QUARANTINE THE OUTSIDE VOICE — Paul's own architectural call
2026-08-30, `7353af46`, 20:11 ET, unprompted:
> *"I think it's important to also get kinda third party forum takes, which can be kind of
> dangerous. So the… that information may need to be sequestered and treated as differently than
> the user's manual. but I do think kind of a forum search web search should be a part of the whole
> getting up to speed."*
Both halves in one sentence: **bring it in, and do not let it touch the record.** That became
`cycle/fleet/FIELD-NOTES.md` and its operative rule — *never take a NUMBER from a forum, take a
QUESTION* — within the hour. **The user specified an information-architecture constraint before
any harm occurred.** That is the proof point I would put in front of anyone asking what these
interactions are actually like.

### Cross-cutting: the shape of the ask itself
Roughly four in five of these openings are voice-dictated run-ons that (a) name the machine by
nickname, (b) state a symptom or a scope, and (c) **carry a separate instruction about the
record** — *"let's record all this"*, *"go ahead and fold today's findings into the record"*,
*"Please log all this"*, *"let's make sure all this is written down clearly so we can revise it
and have a single source of truth."*
**He is running two loops per session: fix the thing, and make the record carry it.** The second
instruction is almost never merged into the first, and it is almost never omitted.

---

## 5 · Open questions — only Paul can settle these

1. **DR200S — what fuel filter is on the 200?** (D-2) He read a fuel level "in the fuel filter."
   Is there a see-through inline filter fitted, and if so, whose? The DR-Z400S has a recorded APE
   Racing inline filter and this is a live cross-contamination risk between the two bikes.
2. **DR200S — is "we took the battery out and tightened the contacts" (D-4) the same event as the
   2026-07-21 row, or a separate, later intervention?** If separate, the charging investigation is
   missing an electrical touch.
3. **Bronco — when did the tailgate-harness repair (B-1) and the ashtray / power-outlet job (B-2)
   happen?** Both are completed work with no date. The photo dates would settle it; I refused to
   infer them from adjacent rows.
4. **Bronco — "latch bushings for where the door AND the tailgate latches" (B-5): one job or two?**
   The record has only the tailgate striker bushing (Dorman 38424).
5. **Bronco — is the removed non-working amp (B-3) still on the shelf, and is its wiring still in
   the truck?** This changes the Phase-5 amp scope materially.
6. **GTI — was 2025-10-20 a coolant-diagnosis day?** (G-1) He hedged with "if memory serves." The
   photo date is firm; the subject is not.
7. **GTI — the promised coolant photograph (G-7) was never sent.** The card treats the pink read
   as settled. Does he still want it confirmed on an image, or is the elimination argument enough?
8. **GTI — six weeks between the locksmith dead-end (2026-07-14) and the dealer key order
   (2026-08-04).** Was something else tried in between?
9. **GTI — is the Express Oil conversation (G-6) still on?** It is the only genuinely
   time-sensitive open item across all three vehicles, and it has been sitting since 8/28.
10. **Bronco — the clear-coat stopgap question (B-14) asked 2026-08-31 has no recorded answer.**
    Still live, or overtaken?
11. **DR200S — does Paul still want the pre-start ACRONYM for Mom (D-8),** or does the numbered
    checklist in the guide close it? This one crosses into Track A.
12. **Doctrine — should B-6 ("install date supersedes purchase date; keep both") be promoted to a
    stated rule of the fleet record?** If yes, several Bronco rows currently dated by receipt
    (2025-10-08, 10-15, 11-02, 11-03, 11-20, 11-23, 12-22) are purchase dates presented as service
    dates. **I did not audit them, and the audit is not free.**

---

## 6 · Coverage statement

**What this report rests on:** 18 sessions read in full on Paul's side, ~73 maintenance-bearing
prose messages harvested from the whole corpus, plus targeted assistant-side reads. Every finding
tagged, every quote timestamped and attributed to a session id, every NEW claim grep-checked
against `vehicles.json` and — where the card was silent — against the relevant `guides/` file.

**What it does not cover:** anything before 2026-07-03; 8,235 sidechain messages; ~41,900
assistant turns beyond the sampled ones; the document-ingestion detail of the July record mines.

**The one thing I would not want misread:** the small size of §3 is a finding about the *record*,
not about the corpus. Track B's capture path is working well enough that fifty-nine days of
conversation yielded nine candidate entries, five of them undated. The gaps that remain are
almost all of one kind — **completed hands-on work that entered through photographs or a guide and
never reached `serviceHistory`.** That is a specific, fixable seam, and it is where I would point
lap 1 of the fleet cycle.
