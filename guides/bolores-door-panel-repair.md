# Bolores — Driver Door Panel Repair Guide

*1989 Ford Bronco Eddie Bauer · chestnut interior · driver-side door panel, cracked through with broken clip mounts*

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
- [ ] **(Optional — easiest snapped-post fix) Mounting-post repair kit** — [Blue Truck Parts `DPPRK87`](https://bluetruckparts.com/products/dpprk87) (~$34), brackets engineered for the '87–91 Bronco/F-series panel that bond on to recreate broken mounting posts + color-matched screw-hole caps. *(Found via research — stock not independently verified.)*
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
