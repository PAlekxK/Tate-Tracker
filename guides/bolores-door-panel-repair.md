# Bolores — Door Panel Repair Guide (both doors)

*1989 Ford Bronco Eddie Bauer · chestnut interior*

> **Scope note (2026-08-28):** this guide was written driver-side-first (that panel is cracked through with broken clip mounts). Everything in STEPS 0–6 is **door-agnostic** — material check, mesh-weld, backing patches, clip pockets, removal technique. The **passenger** panel is a different and much milder job; its own state, findings and sequence live in **STEP 7** at the bottom. Read STEP 7 first if you're working the passenger side.

The goal: structurally sound panel that mounts solidly (no rattle — this is what gates the audio build), with the visible face filled and sanded **ready for primer**. Repair-in-place is the plan; sourcing a replacement panel is the fallback if the repair doesn't hold.

> **As of 2026-06-22 this job lives inside a bigger project — a full repaint (exterior + interior) with Larry prepping/priming and his buddy's shop spraying.** That changes two things here: (1) you no longer color-match the panel yourself — fill and sand it to primer-ready and the shop sprays the chestnut with everything else (kills the hardest part of this job); (2) the door has to come off for paint *anyway*, so every door job converges into one teardown. See **"The refinish & reassembly sequence"** below for where this fits.

> **One teardown, four jobs.** Pulling this panel is also when you (1) diagnose the driver door **power lock** — meter the switch → actuator, prime suspect is the door-jamb boot wiring; (2) **check the inside door-handle mount** and rivet in a reinforcement plate if the metal's cracked (see the new section below); and (3) lay **door sound-deadening** on the bare shell. Do them as one session so you only open the door once.

---

## The refinish & reassembly sequence (the big picture)

The repaint is the pivot event — a quality exterior + interior refinish forces the truck substantially apart, so the smart play is to make **every "apart-state" job happen inside that one window.** Order:

- **Phase 0 — now, no teardown:** oil change, coolant flush, finish the rear-window/tailgate check. Keeps her healthy while the cosmetic project takes its time.
- **Phase 1 — scope the bodywork (the gate):** walk the truck with Larry/the shop, scope the wheel-well rust + dents, decide who does the metalwork. Nothing comes apart until this is known. (See `guides/bolores-walkaround.md`.)
- **Phase 2 — the big teardown (do everything apart-state here):** pull interior panels, headliner, seats (→ upholstery), carpet; strip exterior trim/lights/mirrors/handles. **Per door:** power-lock fix → handle-reinforcement plate if cracked → panel crack repair + fill + **sand to primer-ready** (this guide's Steps 0–4 + clip rebuild). Do the metal bodywork. **Pre-run the audio wiring now**, even though the build is last — this is the one move that saves a future teardown.
- **Phase 3 — paint (the shop):** factory two-tone exterior + interior panels sprayed a fresh, consistent chestnut. Seats reupholstered in parallel.
- **Phase 4 — reassembly = the soundproofing window:** sound-deadener goes on the now-exposed door shells / floor / roof (nearly free in labor — every surface is already open), *then* new headliner over the roof deadener, *then* reinstall the freshly-sprayed panels + carpet + seats, *then* exterior trim/glass.
- **Phase 5 — audio, last:** amp + subs + speakers on the pre-run wiring. Panels are solid and deadened, so it sings.

---

## STEP 0 — The material check (do this FIRST, before buying any adhesive)

**Everything downstream depends on what the panel is actually made of.** The chemicals that bond ABS will *not* bond polypropylene, and vice-versa. Don't buy the adhesive system until you've confirmed the substrate.

> **What the research says (2026-06-20):** these '87–91 Bronco/F-series panels are a one-piece molded **rigid thermoplastic**, and they're almost certainly **ABS** — every reproduction panel (DashSkin, LMC, Classic Industries) is vacuum-formed ABS, and the failure you've got (rigid plastic cracked through + snapped clip tabs) is the classic ABS-panel failure mode. Nobody has confirmed a recycling stamp on an *original* panel, though, so still run the test below before you bond — if acetone does nothing, it's PP and the adhesive column changes. *(Note: the mesh-weld / hot-stapler reinforcement in Step 2 works on ABS **or** PP — it's mechanical, not adhesive — so that part is material-agnostic.)*

**Find the recycling stamp** — a small triangle with letters, molded into the **back** of the panel:

| Stamp | Material | Bonds easily? |
|---|---|---|
| `>ABS<` | ABS | ✅ Yes — best case. Solvent-welds *and* epoxies. |
| `>PP<` | Polypropylene | ⚠️ No — needs special primer/adhesive (see PP column below). |
| `>PE<` / `>HDPE<` | Polyethylene | ⚠️ No — same problem as PP (low surface energy). |
| `>PVC<` | PVC | Bonds with PVC cement; epoxy OK. |
| No stamp | unknown | Run the two tests below. |

**If there's no stamp, two quick tests:**
1. **Float test** — drop a small shaving in water. **Floats = PP or PE** (the hard-to-bond ones). **Sinks = ABS** (or PVC). PP/PE are less dense than water; ABS is denser.
2. **Acetone test** — dab acetone on a hidden spot and wait ~30 sec. **Gets tacky / softens / dulls = ABS** (acetone attacks it — which is exactly why acetone welds it). **No effect = PP/PE.**

**→ Write the result here once you know it:** `Substrate = __________`

---

## STEP 1 — Materials & shopping list

### Buy now (needed regardless of substrate)
- [ ] **ABS sheet stock** — 1/16" (0.06") for contoured backing patches, plus a little 1/8" for rebuilding clip mounts. Black is fine (it's all hidden). [Cut-to-size at TAP Plastics](https://www.tapplastics.com/product/plastics/cut_to_size_plastic/abs_sheets/524) (small pieces, both thicknesses — verified in stock; don't buy a 4×8 sheet). *(Even if the panel turns out to be PP, ABS sheet is still the backing material — you just change the adhesive.)*
- [ ] **Heat gun** — to form the ABS backing to the panel's contour. *(You have one.)*
- [ ] **Plastic welder / hot-stapler** *(for the mesh-weld method + rebuilding clip tabs — see Step 2)* — [ATOLS hot-stapler kit](https://www.amazon.com/ATOLS-Plastic-Welding-Machine-Stapler/dp/B091T368MK) (~$20, verified) or [Harbor Freight 70770](https://www.harborfreight.com/hot-stapler-kit-70770.html) (~$30, verified). A plain soldering iron also works for melting mesh in.
- [ ] **Stainless reinforcing mesh** *(rebar for plastic — best for clip tabs + any crack reaching a panel edge)* — [Polyvance 2045-10](https://www.polyvance.com/Reinforcing-Mesh-1/2045-10/) (industry standard) or a [cheaper generic 5-pack](https://www.amazon.com/Welding-Plastic-Reinforcing-Stainless-Thermoplastic/dp/B08XK52T29). Skip if you go solid-sheet-backing only.
- [ ] **Plastic trim / door-panel removal tools** — the forked nylon pry tools, so you pull the panel without snapping *more* clips.
- [ ] **Door-panel retainer clip kit** — correct Ford part #s (N801925-S / N802900-S): [Icyhaws 50-pc](https://www.amazon.com/Icyhaws-Retainer-Compatible-N801925-S-N802900-S/dp/B0FC2SVY5D) (~$8, verified). Replace them all while you're in there.
- [ ] **(Optional — easiest snapped-post fix) Mounting-post repair kit** — [Blue Truck Parts `DPPRK87`](https://bluetruckparts.com/products/dpprk87) (~$34), brackets engineered for the '87–91 Bronco/F-series panel that bond on to recreate broken mounting posts + color-matched screw-hole caps. ✅ **ON SHELF since 2026-06-22** — Blue Truck Parts, $30.59 + $2.72 = **$33.31**, order `06-14809-51927`, two eBay line items that day. DETERMINISTIC-MATCH verified in `.private/service-records/bronco-1989/VERIFICATION-2026-07-22.md`. **Paul-confirmed 2026-08-28:** the kit **includes the color-matched screw-hole caps**, the bracket mounts on the **back** of the panel (invisible when installed), and it **ships cyanoacrylate (super glue) gel** as its adhesive. Do not re-buy. *(This line previously read "Found via research — stock not independently verified" — the guide was two months behind the receipt.)*
- [ ] **Degreaser** — isopropyl alcohol (90%+) and/or acetone, plus clean rags. *Non-negotiable: nothing bonds to years of skin oil + Armor-All.*
- [ ] **Sandpaper** — 80/120/220 grit (scuff for adhesion + knock down repairs) and 320/400 for finish.
- [ ] **Nitrile gloves, mixing sticks, plastic spreaders, painter's tape, clamps / spring clamps.**
- [ ] **Flexible filler for the show face** — [3M EZ Sand 35887 / 05887](https://www.autobodytoolmart.com/product/3m-ez-sand-multi-purpose-repair-material-35887/automotive-adhesive) (verified in stock). *Not* rigid Bondo on a flexing panel. ⚠️ The older 3M **05895** is sold out everywhere now — 35887/05887 is the same flexible-filler family and is the in-stock substitute.

### Buy AFTER the Step 0 material check (substrate-specific bonding)

| Application | If panel is **ABS** | If panel is **PP / PE** |
|---|---|---|
| **Back-side structural bond** (ABS sheet → panel) | **Acetone or MEK solvent weld** (chemically fuses ABS-to-ABS — strongest), *and/or* **JB Weld** (2-part epoxy) as reinforcement. Belt + suspenders: solvent-weld, then epoxy the edges. | **Plastic welding with PP rod** (melt PP-to-PP — the real fix), **or** a low-surface-energy adhesive **+ its primer**: e.g. **Loctite 401 + 770 Polyolefin Primer**, or a **3M adhesion promoter + flexible repair**, or a **methacrylate (MMA / Plexus)** adhesive rated for PP. Plain epoxy will *not* hold. |
| **Crack fill — hidden back** | JB Weld (rigid is fine where it doesn't flex) | PP-rated structural adhesive (same as above) |
| **Crack fill — visible front face** | **Flexible** plastic filler, then sand + color-match | **Flexible** plastic filler rated for PP (e.g. with adhesion promoter), then color-match |
| **Color match** | Chestnut interior dye / SEM Color Coat (vinyl & plastic adhesion paint), or a matched interior trim paint | same |

> **Why flexible on the front:** a door panel flexes every time you lean on it or close the door. Rigid epoxy at a crack edge telegraphs and re-cracks. Structure comes from the *back*; the front is cosmetic and wants to move a little.

---

## STEP 2 — The repair sequence

1. **Remove the panel.** Window crank / handle hardware off first, then work the perimeter clips with the nylon tools. Note which clips are broken vs. which pockets are broken — different fixes (Step 4).
2. **Fix the lock wiring while it's off.** (See the power-lock restoration item — meter switch → actuator, suspect the jamb-boot wiring.) Easiest with the panel out of the way.
3. **Degrease everything.** Both faces, every bond area. Isopropyl/acetone until the rag comes away clean. Let it flash off.
4. **Scuff the bond areas** with 80–120 grit so the adhesive has tooth. Wipe again.
5. **Stop the cracks, then reinforce from the back — two methods, pick per spot.** First, **drill a tiny hole at each crack's *end*** so it can't keep splitting, and tape/align the crack from the *front*. Then reinforce the back one of two ways:
   - **(a) Mesh-reinforced weld** — *strongest*; use it on stressed spots, clip tabs, and any crack that runs to a panel edge. Lightly V-groove the crack, run a bead of melted ABS (rod or acetone slurry) to fuse it, lay the stainless mesh over it and **iron/weld it down until it sinks flush into the softened plastic**, then skim a thin layer of melted ABS over the mesh to bury it. The mesh is rebar — it only works *embedded in molten plastic*, **never dry-trapped under a glued sheet**.
   - **(b) Solid ABS backing patch** — *simpler*; great for cracks in the flat field. Cut ABS sheet to span the crack with overlap, heat-form it to the contour (*keep the gun moving* so it doesn't bubble; hold till cool or it springs back), and bond it per your Step-0/1 substrate (acetone-weld or ABS cement if ABS; promoter + flexible adhesive if PP). Here the *sheet itself* is the reinforcement — no mesh needed.

   You can **stack both** on a high-stress spot (mesh-weld the crack, then patch a sheet over the zone). But don't rely on dry mesh sandwiched under a glued sheet — pick mesh-*embedded* **or** solid-sheet as the spanning method. Match weld **rod to the plastic** (ABS rod on ABS), and **ventilate** — melting ABS smells.
6. **Rebuild the clip mounts** (Step 4).
7. **Fill the front face** with flexible filler (3M EZ Sand 35887), sand 220 → 320 → 400 to **primer-ready**. **Stop here — don't color-match.** Under the full-repaint plan the panel goes to the booth and gets sprayed chestnut with the rest of the interior, so your job is a smooth, sound substrate. (Only color-match yourself if the repaint plan falls through.)
8. **Hand the panel off for paint, then reinstall** with the new clip kit during reassembly. Confirm it sits tight with no rattle — that's the bar that unblocks soundproofing + subs.

---

## STEP 3 — (covered in sequence above)

## STEP 4 — The broken clip pockets / bosses

These are **not** the dash bezel's screw bosses — different geometry, different load — so we're not reusing that exact heat-shrink trick. A panel clip pocket is a flat slotted/"doghouse" mount that a push-in clip snaps *through*, and it sees a pull-out load when you tug the panel off. Approaches to try (decide hands-on once you see what's left of each pocket):

- **If only the clip is broken, not the panel pocket** → just use the new clip kit. Done.
- **Easiest for snapped posts** → the **Blue Truck Parts `DPPRK87`** mounting-post kit (Step 1) — brackets bond on to recreate the posts, purpose-built for this exact panel.
- **If the pocket/tab is torn off the panel** → two strong DIY options: **(i) mesh-weld a new tab** — shape it from stainless mesh and melt it into the panel (the strongest fix, and mesh can form a tab a flat sheet can't); or **(ii) fabricate a mount from 1/8" ABS** — cut a backing plate with a correctly-sized slot/hole for the clip, then bond it to the panel (substrate-appropriate adhesive) so the plate carries the pull-out load across a wide glued area, not a single weak point. A fender washer behind the slot spreads the load further.
- **If a whole section of edge is gone** → back it with a heat-formed ABS strip first (Step 2.5), then build the new pocket onto *that*, so you're mounting to fresh material.

The principle: spread the load over a **large bonded area** of fresh ABS rather than trusting the original cracked plastic at a point.

---

## STEP 5 — Inside door-handle mount (while the panel's off)

**Different failure, same teardown.** This is *not* the plastic panel and *not* the clip pockets — it's the **sheet metal of the door shell** behind the **inside release handle**. On '80–'97 OBS Ford trucks/Broncos this metal fatigues and cracks, so the handle flexes and eventually won't pull the latch — the classic "roll the window down and get out from the outside handle." It's one of the most common failures on these trucks.

**Check it with the panel off:** wiggle the inside handle and look at the metal it bolts to. Loose / flexing / visibly cracked = needs the fix.

**The fix — a reinforcement plate (no welding):**
- A **14-gauge steel plate** that sits over the handle area and **rivets onto the inner door metal**, giving the handle a solid anchor even on a severely cracked door. Rivets are included with most kits; a cheap rivet gun does it.
- Well-proven — sold by **Solo Motorsports, OBS Solutions, Bronco Graveyard, LMR**, plus generic pairs on eBay/Amazon. Forum consensus (FullSizeBronco, Ford Truck Enthusiasts) is "stupid easy" and that it fully solves the flex. The name-brand plates have the longest track record; if buying a generic, glance at the seller's feedback first.
- Sold as a **driver + passenger pair** — and the failure is symmetric, so do **both doors** while everything's open.

Install: remove panel + handle → set the plate → drill for rivets → rivet on → reattach the handle. Do it in the same Phase-2 door session as the panel repair and the power-lock diagnosis.

---

## STEP 6 — The one-removal protocol (old plastic; open the door ONCE)

*Added 2026-07-27, from Paul's concern: every on/off cycle is another chance to crack 37-year-old plastic.*

**The count is forced, and it's better than it feels.** The panel has to be off the truck for the
chestnut spray — that's non-negotiable, and it's the *last* time it comes off. Which means:

> **Any install of that panel before paint is a wasted cycle by definition.**

So the optimum is **1 removal + 1 install**, with the panel simply *staying off* in between — through
bench repair, through the shop, through reassembly. That's not a big-bang weekend; it's a two-day
teardown followed by months of unhurried access. **The risk isn't the work, it's closing the window early.**

### What fills the window

1. **Teardown (both doors, one session).** This is the two days. Panels off, vapor barriers off (cut at
   the butyl bead and **save them as templates**), survey, photograph, bag + label fasteners per door.
   Do the diagnosis that has no paint dependency: **meter the lock circuit** (switch → jamb boot →
   actuator — the step deferred since Feb 2026; reconcile the on-shelf TRQ actuator against the
   "already replaced" note while in there), check **both** inside handles for the fatigue crack (Step 5),
   assess regulator, glass channels, hinge pins. **Order parts off what you find.**
2. **Bench, in parallel (weeks).** Steps 0–4 of this guide. Cure times make it naturally slow — it fills
   the waiting rather than competing with anything.
3. **Truck + panels at paint.** Nothing to do.
4. **Truck back — the cavity, then close.** Cavity prep (see the fork below) → deaden → fit every new
   part → pre-run the amp/sub wiring **plus a spare pull string** → **test everything with the panel
   still off** → new water shield → panel on with NEW clips. Once.

### The cavity prep fork — clean is mandatory, paint is conditional

Butyl needs a **clean, sound** surface, not a fresh one. Intact factory coating is actually a *better*
substrate than new paint, because it's already cured. Strip, clean, **look**, then decide:

- **Just dirty?** Vacuum, degrease, dry, deaden. Same session, no cure gate. Most likely outcome.
- **Surface rust or flaking?** Treat it — but for the *door's* sake, not the deadener's. Sealing rust
  under butyl is how you find a hole in five years.
- **Perforated at the bottom?** Different job. Worth knowing regardless.

**The cure gate is free here.** It only costs if you're trying to finish in a weekend — and you're not,
because the panel is off for the shop anyway. So if the insides get cleaned and painted simply because
you want them clean and painted, that's a fine reason and it costs nothing.

### ⚠️ What forces a second cycle

Every item here is somebody re-opening a door they'd already closed:

1. **Reusing old clips.** 37-year-old retainers are brittle; reused ones don't seat, the panel sits
   proud, and off it comes again. Buy enough of the Icyhaws set for **both** doors.
2. **Buttoning up before testing.** Window up/down, lock cycling, speaker playing, handle pulling the
   latch, mirror moving — all verified **with the panel off.** This single rule prevents most re-entries.
3. **Skipping an age-based part because "it still works."** At 37 years with the panel off, *works* is
   not a reason to skip a $15 part: glass run channels and fuzzies, weatherstrip, regulator lube, door
   check strap, hinge bushings.
4. **Not pre-running wire.** Already planned for the amp/subs — add a pull string for whatever hasn't
   been thought of yet.
5. **Doing only the driver's door.** The reinforcement plates ship as a pair anyway (Step 5).

### Removing it without breaking it

- **Do it WARM.** ABS cracks cold and flexes warm — Georgia in July/August is ideal; an unheated space
  in January is the worst possible time.
- **Proper trim fork, prying AT each clip, never between them.** Mid-span prying is exactly what cracks
  a panel.
- **Expect to break clips** — that's fine, that's why new ones are bought in advance. *The clips are
  consumable. The panel is what you're protecting.*

### Door-specific deadening cautions

- **Don't seal the door drains.** Water always gets into a door; one that can't drain rots bottom-up.
  This is the most common way people damage a truck while improving it.
- **Go easy on mass.** CLD on the inside of the outer skin + foam on the inner is the standard door
  treatment and it's what makes the Kappas sound right. Piling MLV into a door adds weight the hinges
  carry, and OBS Ford doors are heavy and sag-prone already. (Judgment, not a spec.) Check hinge pins
  and bushings while it's apart.
- **Cavity wax last.** After deadening, shoot Fluid Film / Woolwax into the bottom of the door and
  confirm the drains run. Doors rot bottom-up from the inside, and this is the **only** time that
  access exists. ~$20.

### Open, gated on Larry

**Are the doors going to bare metal, or scuffed and sprayed?** Scuff-and-spray → cavity work can happen
before paint, no conflict. Stripping / heat / filler / any metalwork on a door skin → **wait**, because
heat on the outer skin cooks butyl applied to the back of that same skin, and if they cut a door,
everything done inside it is gone. See `guides/bolores-shop-shortlist.md` → "Questions to bring to Larry."

---

## Cautions

- **Acetone is the ABS test *and* the ABS weld — but it also attacks the show-face finish.** Keep it to the back / hidden areas and the hidden bond lines.
- **Heat gun on ABS:** form, don't cook. Bubbling/shiny scorch = too hot.
- **Color match is the hard part** (you flagged this). Test the dye/paint on a hidden spot first; chestnut is easy to miss warm-vs-cool.
- **If the repair doesn't hold** → fallback is sourcing an '87–91 Bronco / F-series driver panel in chestnut. Long lead, so it's worth keeping an eye on listings even while you attempt the repair.

---

*Companion to the `bronco-1989` restoration list in `vehicles.json` → "Driver door panel."*

---

## STEP 7 — THE PASSENGER DOOR PANEL (bench session opened 2026-08-28)

*Written live while Paul had the panel on the bench. This section is the single source of truth for the passenger side; STEPS 0–6 above still supply the technique.*

### State as found — and it's good news

The passenger panel is in **substantially better shape than the driver's**. Photo-confirmed 2026-08-28, panel off the truck and on the bench:

- **Retainer clips still seated in their pockets** around the perimeter — several intact along the bottom edge. This is the big difference from the driver side ("cracked through with broken clip mounts"). The passenger job may be a **strip-clean-repair-refinish**, not a structural rebuild.
- **One damaged screw hole**, previously stopgapped by Paul with a **metal washer glued on with cyanoacrylate** to spread load and stop the tear-out progressing. Correct instinct; it held for months.
- **Back-side insulation pad** present, glued over the flat lower/middle field — torn and ragged around the openings, partially detached, with a slit cut through it near centre by someone at some point.
- ⚠️ **UNRESOLVED — a dark line runs through the lower field** in both photos. Molding seam or crack? **Fingernail-test it after the gross clean** (grime hides hairline cracks — this is why cleaning precedes assessment). Catches = crack, and STEP 2 applies.

### The insulation — identified, and what replaces it

**What it is:** **recycled cotton shoddy** — garnetted textile waste, needle-punched into a batt. The colored flecks (red/green/blue threads through the gray) are the identifying tell. Standard automotive insulator through the '80s–'90s. **Not** fiberglass, **not** jute, **no asbestos concern** on an '89 trim pad. Dusty and possibly moldy — wear a mask, bag it as it comes off.

**What it was doing** — read it off the placement: it covers the big *unsupported flat field* and stops short of the reinforced perimeter. That makes it an **anti-drum absorber and anti-buzz spacer**, not a thermal blanket. Ranked by what actually matters:
1. Damping the flat field so the door doesn't sound like a drum head on close.
2. Keeping plastic off inner door metal so it doesn't buzz. **This is the one that gates the audio build.**
3. Trivial thermal benefit — a rounding error.

**Remove it: YES.** Four reasons, and the last one forces it regardless of the others:
- Already torn, ragged and lifting free — a partially-detached damper doesn't damp.
- Recycled cotton is a moisture sponge and a nesting medium (same mechanism the record caught in the bed corner: *"degraded jute/carpet remnant sitting directly in the wet corner"*).
- It's glued over exactly the field any backing patch would bond to.
- The Phase-4 soundproofing plan supersedes it anyway.

**Replace it: YES — and this is not optional.** Strip it and fit nothing and you get precisely what it was preventing: hollow slap on close, plus buzz where the panel touches metal. Self-inflicted, on the truck whose whole audio build is gated on "no rattle."

**Replacement spec — 1/8" closed-cell foam (CCF), cut from the old pad as a template.** NOT a new fiber pad.

> ⚠️ **BUTYL IS NOT THE REPLACEMENT.** Per the four-layer model in `vehicles.json`: butyl CLD is **layer 1 (DAMPING)** and belongs on the door's **outer skin, bonded to metal**. The shoddy pad was doing **layers 2 (DECOUPLING) and 4 (ABSORPTION)**. Different job, different surface, different material. **Paul does not currently own a layer-2 material — CCF is a shopping item.** (Butyl leftovers on the panel's biggest flat field are a marginal bonus, not the fix.)

**Two rules on the CCF:**
- **Same thickness as the old pad or thinner.** Old pad measures ~1/4"; go 1/8" for margin. Thicker → panel stands proud → nearby clips fight it → you have built the rattle you were preventing. (Same fitment trap as the Carpet entry.)
- **Find the rub marks first.** Before binning the pad, look for shiny/worn spots on the panel back and the door shell where they've contacted for 37 years. **Foam or felt tape at those specific points is the highest-value move in this whole job.** Full-field foam is the nice-to-have; the contact points are the actual fix.

**Timing: the CCF goes on at REASSEMBLY, not now.** Don't put foam on a panel that still has to be masked and handled around a spray booth. Right now: pull the pad, **trace the template onto paper or cardboard immediately** (in case the pad disintegrates), keep the pad flat.

### The glued washer — removal (SOLVED 2026-08-28)

**Outcome: it twisted off cleanly. Underside of the washer showed no plastic — the bond failed at the glue, the panel lost no material.**

**What worked:** grip the washer with pliers and **twist it in plane**. It resisted at first; enough torque sheared it.

**Why that's the move:** cyanoacrylate has decent tensile strength and poor shear. Twisting shears a thin glue film. **Prying or lifting loads the *panel* in peel — that's the one action that can tear a disc of ABS out of an already-damaged hole and make the problem worse.** Twist, never lift.

**Things that were considered and are recorded so they aren't re-litigated:**
- ⛔ **Oil soak does NOT work.** Cured CA is not soluble in oil and does not "rehydrate" — it's polymerized, not dried out. The ubiquitous online advice is for superglue **on skin** (where oil softens the *skin*) and for **sticker/tape residue** (a different adhesive chemistry that oils genuinely do dissolve). Vegetable and olive oil are the same thing here; neither works. If soaking anyway, use **mineral oil** — vegetable oils oxidize to a gummy film — and time-box it to an hour.
- ⛔ **Do not use a soldering iron.** 700°F on a metal washer sitting on ABS will mark it in seconds. This was suggested in-session and retracted.
- ✅ **Heat is NOT a real danger if the tool can't reach the threshold.** ABS softens ~221°F; a hair dryer tops out ~150°F and physically cannot get there. A heat gun on low, kept moving, is what this guide already prescribes for heat-forming ABS. Choose a tool whose ceiling is below the failure point rather than being careful with one that isn't.
- ✅ **If grip fails** (thin washer, nothing to hold): shock it laterally with a punch and light hammer taps — CA is brittle and fails better under impulse than steady force — or **grind the washer away** with a Dremel. Zero load on the panel.
- 💡 **Best insight, if it recurs: the goal is FLUSH, not REMOVED.** Filing/sanding a thin washer down flush solves the actual problem and keeps its load-spreading benefit. Only fully remove it if the bracket needs to bond chemically to bare ABS.

### The DPPRK87 bracket install

**What the kit is** (Paul-confirmed 2026-08-28, holding the part — this beats the June research note): the bracket mounts on the **back** of the panel and is **invisible** when installed; the kit **includes the color-matched screw-hole caps**; and it **ships cyanoacrylate gel** as its adhesive.

**What the CA gel tells you — this is the load-bearing inference:**
- **The bracket is a locator and load-spreader. The SCREW carries the load.** CA gel is not a structural adhesive for a load path. Consequence: bond area matters less than feared, and **not overtightening the screw matters much more** — over-torque into brittle 37-year-old ABS is almost certainly what tore the hole out originally, and a new bracket torqued the same way fails the same way. Snug, then stop. A nylon or rubber-backed washer under the head spreads bearing load and adds compliance.
- **Corroborating evidence on substrate:** a vendor specializing in '87–91 Ford panels shipping CA gel implicitly asserts the panel takes CA well → **points ABS** (CA is mediocre on polypropylene). Supports the STEP 0 hypothesis; does **not** replace the acetone test.
- ⚠️ **CA gel has essentially NO GAP FILL.** So **flatness matters in BOTH directions** — a dish means the bracket bonds only at its rim. *(An earlier in-session note said "a slight dish is fine, a bump is not." That was epoxy logic and is wrong for this adhesive.)* Sand the CA ring flat with 120 on a **rigid block**, then check by test-fitting the bracket and looking for light under it — not by feel.
- ⚠️ **CA gel gives up around 180°F.** A paint bake runs 140–180°F. → **Question for Larry: does interior trim get baked, and at what temperature?**
- ✅ **Adequacy: CA is good enough here.** Evidence from this very session — the old washer's CA bond, on a dirty unprepped 37-year-old surface, required pliers and real torque to shear. A scuffed, degreased, flat bond will be considerably better. Don't second-guess the vendor's choice.
- 💡 **Optional belt-and-suspenders:** tack with the supplied gel, then epoxy the perimeter once it's held. Matches this guide's existing ABS pattern ("solvent-weld, then epoxy the edges") and Paul's proven `vehicles.json` **"Screw-boss rebuild"** technique (heat-shrink form + JB Weld), whose note reads *"arguably more durable than the original brittle plastic."*

**Handling CA gel:** no repositioning — dry-fit and **pencil the outline first**, then commit. Scuff **both** faces (3D-printed parts have a glossy print skin and handling oils; PETG especially bonds badly unabraded — the layer lines give good tooth once scuffed through). Degrease immediately before, not earlier. Press and hold; don't crush.

**Before/after paint?** The bracket is back-side and invisible, so it is **not** paint-dependent. Default: **bond it now** rather than leaving the panel half-repaired for months waiting on a booth date — the bake risk is small and the failure mode is a re-glue of a part nobody can see. The **color-matched caps go on AFTER paint** regardless; they're finished parts, you don't spray them.

### Cleaning — you clean TWICE, and the first one comes earlier than instinct says

**1. Gross clean — BEFORE you assess.** Soap, water, degreaser, both faces. Not cosmetic. Two reasons: **grime hides hairline cracks** (you cannot honestly survey a dirty panel, and assessment is the whole point of having it bare), and sanding/scraping a dirty panel **drives contaminants into** the plastic. Then **dry completely** — a full day or blow it out; old panels hold water in seams and nothing bonds to damp.

**2. Local bond prep — at each joint, immediately before bonding.** Scuff, degrease, bond. Never rely on last month's big clean to serve today's joint.

**3. Final prep clean — immediately before it goes to Larry.**
> ⚠️ **HIGHEST-STAKES CLEANING OF THE WHOLE JOB: the show face.** Decades of Armor-All means **silicone**, and silicone is *the* fisheye contaminant in a paint booth. Multiple passes with a proper wax-and-grease remover, **fresh rag each pass**. **Gloves from this point forward** — skin oil after the final wipe undoes it. Raise it with Larry directly; a protectant-soaked 37-year-old interior panel is a known shop headache.

⚠️ Adhesive residue from the pad: **mineral spirits or 3M adhesive remover — NOT acetone** (acetone is the ABS solvent-weld and will haze and soften the panel). Then isopropyl to lift the oily film every adhesive remover leaves.

### THE SEQUENCE

```
strip → gross clean → dry → assess (+ acetone test) → repair (incl. bracket)
      → filler & sand show face → final prep clean → BOOTH
      → color-match caps + CCF + hardware + NEW clips → test with panel OFF → install ONCE
```

**Now — strip & document**
- [ ] Photograph the back before anything else comes off
- [ ] Pull the shoddy pad, keep it **intact and flat** — it's the CCF cut pattern
- [ ] **Trace the template onto paper/cardboard immediately**
- [ ] Note/photograph the **rub marks** on the panel back
- [ ] Remove hardware: door pull, courtesy light, switch plate, trim
- [ ] Bag + label fasteners **by location**, not in one pile

**Now — gross clean, then dry a full day**

**Now — assess (the real payoff of having it bare)**
- [ ] Fingernail-test the line in the lower field — crack or molding seam?
- [ ] Survey **every** screw hole. The one that failed was just first — same age, same brittleness. Two kit orders are on shelf, so there's material
- [ ] Survey every clip pocket up close
- [ ] ⭐ **Acetone test → record the substrate.** STEP 0 gate, open since June, never confirmed on an original panel. Decides the adhesive column for BOTH doors. `Substrate = __________`

**Now — repair (bench, unhurried; cure times are free here)**
- [ ] Sand the CA ring flat, 120 on a block; test-fit for light underneath
- [ ] Bond the DPPRK87 bracket (dry-fit → pencil → scuff → degrease → gel)
- [ ] Any cracks: **drill the crack ends first**, then back-reinforce per STEP 2
- [ ] Rebuild any broken clip pockets (STEP 4)
- [ ] Flexible filler on the show face → 220 → 320 → 400. **Stop at primer-ready. No color matching.**

**Later — at reassembly, after paint**
- [ ] Color-matched screw-hole caps
- [ ] CCF from the template + felt tape at the contact points
- [ ] Hardware back on; **NEW clips** (Icyhaws 50-pc, on shelf)
- [ ] **Test window, lock, speaker, handle with the panel still OFF**
- [ ] Panel on. Once.

### OPEN — needs Paul

1. ⏸ **Acetone test — DEFERRED by Paul 2026-08-28** ("rather not do an acetone test... I could do one later when it's fully clean"). Working assumption is therefore **ABS — ASSUMED, NOT VERIFIED**, resting on three independent lines: (a) every repro panel (DashSkin, LMC, Classic Industries) is vacuum-formed ABS; (b) the driver panel's failure — rigid plastic cracked through, snapped clip tabs — is the classic ABS mode; (c) Blue Truck Parts, an '87–91 Ford panel specialist, ships **CA gel** with its kit, and CA is mediocre on polypropylene. **Where the assumption actually bites: only crack repair.** The bracket (vendor-supplied CA gel) and the CCF (adhesive-backed) are both substrate-agnostic, so under the 8/28 resequence this gate blocks nothing until a crack needs a bonded backing patch. Run it then, on a clean panel.
2. **Is the line in the lower field a crack?** Fingernail test after the gross clean.
3. ✅ **RESOLVED 2026-08-28 — the blue/silver sheet is CLD butyl, and Paul already owns 36 sq ft of it.**
   **CUKWUYBY Butyl Sound Deadening, 80 mil (2 mm), 36 sq ft, 33 sheets @ 15.75" × 9.84" — ASIN `B0F1MV7GRF`. Amazon product page reads "Last purchased Feb 23, 2026."** 3-layer: aluminium foil / butyl core / adhesive. $42.49 as read 2026-08-28 (typical $48.99); 4.7★, 441 ratings.
   **Paul's read was right: it's butyl and it belongs on metal.** → **LAYER 1 (DAMPING) IS FULLY STOCKED. Buy no butyl.**
   ⚠️ **PARTS-RECORD GAP — the record was wrong, not Paul.** `AMAZON-PARTS.md` carries the *Sound Deadener Application Roller* ($9.03, 2026-02-24) but **not the mat bought the day before**, and `CANDIDATE-ROWS.md` still says *"door sound-deadening not yet done (discussed only)"* — true of the install, false of the purchase. Feb 23–24 2026 is the same window as the NVX baffles and the Kappa door-speaker install; the deadener was bought for that job and never laid. **Fold the mat into `AMAZON-PARTS.md` as ON SHELF.**
   💡 Relevant review on that listing, from a custom shop: used this exact material on **two early-Bronco builds**, ~three boxes per truck for full interior coverage, reports doors *"have a much more solid feel and sound when they close."* Caution from the same review: **foil lifts if a piece ends on a bend or tight radius — plan seams on flat areas and roll the edges down.** (Paul owns the roller.)
4. ✅ **RESOLVED 2026-08-28 — see "THE 8/28 RESEQUENCE" below.** Paul's call: restore and reinstall now, accept a second removal at paint.
5. **For Larry:** does interior trim get baked, and at what temperature? (CA gel limit ~180°F.)

### Still to fold into `vehicles.json` (held 2026-08-28 — concurrent GTI session in this repo)

- A **"Passenger door panel"** restoration item (none exists; the record has driver-side only)
- The shoddy-pad finding + CCF replacement spec + the layer-1-vs-layer-2 distinction
- DPPRK87 status: **ON SHELF**, contents confirmed, ships CA gel
- The washer removal result (panel intact)


---

## ⭐ THE 8/28 RESEQUENCE — restore and reinstall NOW; the one-removal protocol is deliberately spent

**`paul-decided 2026-08-28`:** *"Restore the door panels, put them on, and then just be ready to take them off when there's a full painting. We're not gonna wait on the full painting to restore and work on these door panels because I don't want them to rattle or get worse in any of the cracks."*

**This overrides STEP 6's one-removal optimum, and the override is correct.** STEP 6 was never a principle — it was arithmetic, and it rested on one premise: *the booth is near-term, so any install before paint is a wasted cycle by definition.* With paint now indefinite, that premise is gone and the trade inverts. Leaving both doors gutted for a year to bank one cycle is worse than spending it. **Accepted cost: one extra removal per door.** Mitigation is unchanged — work WARM, pry AT each clip, clips are consumable and the panel is what you're protecting.

### ⚠️ THE CONSEQUENCE THAT CHANGES THE WORK: "primer-ready" no longer works

"Stop at primer-ready, the shop sprays the chestnut" existed **only** because the panel went bench → booth with no stop in between. A panel going back on the truck for an indefinite stretch can't wear gray filler — which drags **color-matching** back into scope, the single hardest part of this job and the thing the repaint plan was celebrated for killing.

**Don't take that bait. SPLIT THE JOB by side of the panel:**

> ### 🔧 DO NOW — the back (structural, invisible, no paint dependency)
> - Back-side crack reinforcement — **stops propagation**, which is half of what Paul asked for
> - DPPRK87 bracket at the torn screw hole
> - Clip-pocket rebuilds — ⭐ **this is the rattle fix**
> - CCF on the panel back — the other half of the rattle fix
>
> ### ⏸ DEFER TO THE BOOTH WINDOW — the show face (cosmetic)
> - Flexible filler, 220 → 320 → 400, final prep clean, spray
>
> **Why defer:** show-face filler done now would sit for a year, get handled, and need re-sanding before the booth anyway. You'd do it twice and colour-match a panel that gets resprayed. The panel goes back on **structurally sound and quiet, still wearing its original chestnut and whatever cracks show on the face.** It looks how it looks today — but it doesn't rattle and it doesn't get worse. That is exactly the ask.

### What moves EARLIER as a result

Three items were parked at "after paint" in STEP 7 and now belong in this session:

1. **CCF on the panel back — fit it NOW.** Reassembly is now. Buy the foam before buttoning up (still a shopping item; see the layer-model warning in STEP 7 — butyl is not it).
2. ⚠️ **The vapor barrier must be properly RESEALED, not just templated.** Saving it as a template was sufficient when the door was staying open. A panel going back on over a compromised water shield **puts water in the cab.** Butyl tape or a new barrier before the panel goes on. Non-optional now.
3. **All apart-state work, done in this session** — lock metering (switch → jamb boot → actuator; reconcile the on-shelf TRQ unit), BOTH inside-handle fatigue checks, glass run channels and fuzzies, hinge pins/bushings, door check strap, cavity inspection + cavity wax. Accepting a second cycle is no reason to pay for a third.

**Unchanged and now more important, not less:** test window, lock, speaker, handle **with the panel still OFF.** A reinstall you've committed to is a reinstall you don't want to undo.

### ⚠️ STILL GATED ON LARRY — butyl on the door's outer SKIN

Do **not** lay CLD on the outer skin yet. If the doors later go to bare metal, or see heat/filler/metalwork, deadener on the back of that skin gets cooked or cut out. Laying it now is a bet on what Larry does to the doors. **CCF on the plastic panel carries no such exposure — that's free to do today.** It is specifically the *metal* that waits.

### Revised sequence

```
strip → gross clean → dry → assess (+ acetone test)
      → BACK-SIDE repair: cracks, bracket, clip pockets
      → CCF on panel back  →  reseal vapor barrier
      → test everything with panel OFF  →  panel ON  (cycle 1 of 2)
      ...
      → [booth window opens] → panel OFF → show face: filler, sand, spray
      → colour-matched caps → panel ON  (cycle 2 of 2, final)
```

**Clip budget:** the Icyhaws 50-pc kit now has to cover **two** installs across **two** doors. Count what's left after this round and re-buy early — reused brittle retainers are item #1 on STEP 6's what-forces-another-cycle list, and at ~$8 a kit there is no reason to be short.


---

## STEP 8 — PARTS: what's on shelf vs. what to buy (as of 2026-08-28)

> ⚠️ Prices read off Amazon 2026-08-28 and **will drift** — treat them as an order-of-magnitude, re-check at purchase.

### ✅ ALREADY OWNED — do not re-buy
| Item | Detail |
|---|---|
| **Butyl CLD (layer 1)** | CUKWUYBY 80 mil, 36 sq ft, 33 sheets — ASIN `B0F1MV7GRF`, bought **2026-02-23**. Enough for both doors many times over. |
| **Deadener roller** | $9.03, 2026-02-24. Non-negotiable for butyl — unrolled CLD is decorative. |
| **DPPRK87 bracket kit** | Blue Truck Parts, 2× orders 2026-06-22, $33.31. Includes colour-matched screw-hole caps + CA gel. |
| **Icyhaws panel clips** | 50 pc, 2026-06-22, $8.70 — but see the clip-budget note below. |

### 🛒 TO BUY

**1. CCF — closed-cell foam, 1/8", adhesive-backed → the panel-back layer. THE ONE THING BLOCKING REASSEMBLY.**
Sponge neoprene is the right pick here over PE foam: it's compliant, conforms, and is exactly what you want at a rub point.
- *Sponge Neoprene Foam Sheet with Adhesive, 1/8" × 12" × 59"* — **~$12.97**, 4.4★ (395). ≈4.9 sq ft ≈ one panel field. **Recommended — buy two.**
- Alternatives: *Storystore 1/8" × 12" × 59"* ~$12.99, 4.2★ (566) · *78" × 12" × 1/8" marine roll w/ adhesive* ~$13.99, 4.5★ (42).
- ⛔ **Do NOT buy Siless Liner / PE liner 36 sq ft (~$44.95) for this job.** It's 4 mm and sized for floors and tunnels — a later-phase purchase, not this weekend's.

**2. Butyl sealant tape → resealing the vapor barrier. NON-OPTIONAL under the resequence.**
Wide flat ribbon beats round rope for a door water shield — it seals the barrier edge properly.
- ⭐ *Dicor `BT-1834-1` Butyl Seal Tape, 1/8" × 3/4" × 30'* — **~$18.35**, 4.7★ (**12.9K** ratings), #1 Top Rated. 30 ft does both doors with margin. **Recommended.**
- Alternatives: *XFasten 1/2" × 30' × 1/8"* ~$14.99, 4.6★ (2.8K) · *Second Skin Butyl Tape 20 ft* ~$24.50, 4.7★ (1.2K) · *LLPT rope 3/8" × 16.5 ft* ~$14.99, 4.4★ (650) for a factory-like round bead.
- ⚠️ Filter out the crawl-space/foundation listings that dominate this search — 2" × 90' double-sided, $37–110. Wrong product, wrong scale.

**3. More panel clips — the budget is now TWO installs × TWO doors.**
- ⭐ *GoaMotors 100 pc `N801925-S`* — **~$11.93**, 4.5★ (137). Double the count, correct Ford P/N, deeper reviews. **Recommended over re-buying the 50 pc.**
- Same-as-before: *Icyhaws 50 pc* ~$7.49 (5 ratings).
- Reused brittle retainers are item #1 on STEP 6's what-forces-another-cycle list. At ~$12 there is no reason to be short.

**4. Optional, ~$5 — foam gasket tape for the rub points.**
*Car Speaker Sealing Tape / foam grip tape, 3 mm × 10 mm × 16.5 ft* — ~$5.09, 4.7★ (420). For the specific contact points found on the panel back. Cheapest high-value item in this whole job.

### 💡 Free upgrade you already own
A sheet or two of the CUKWUYBY butyl on the panel's **largest flat field** damps it — the layer-1 job applied to plastic. Less dramatic than on steel (plastic is already more self-damping) and strictly optional, but it's paid for and sitting there. Keep it to the flat field, then CCF over the top: **CLD first, foam second.** Do not add mass out near the clip pockets.

⚠️ This is the **panel**, not the door skin. **Butyl on the outer SKIN stays gated on Larry** — see the resequence section.
