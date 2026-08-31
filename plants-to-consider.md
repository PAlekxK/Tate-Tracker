# Plants to consider — a growing reference

Plants worth thinking about adding to Fernwood, especially natives, protected species we can foster, and anything that supports the local ecology and ecoregion. This is distinct from `plants.json` — that file tracks what *is* on the property and how to care for it. This file tracks what *could be* on the property.

**Direction set by Paul (2026-05-19):** "We should think about eventually having a piece of, or collection of information curated around plants to try to plant, especially focusing on what's native, things that are protected that we can try to foster, especially if we can try to support the local ecology."

**Thread activated 2026-05-26.** Win-state locked: operational + reference (start with 3-5 candidates plantable fall 2026 / spring 2027, structured so the same artifact grows into the durable reference). Surface: dashboard "Candidates" card with structured JSON. Sourcing: programs + named nurseries + freshness tags.

**Discovery pass complete.** Full landscape, four-tier mental model, candidate categories, schema proposal, card design directions, and open questions live at [`.research/2026-05-26-plants-to-consider-discovery.md`](.research/2026-05-26-plants-to-consider-discovery.md). The sections below are the seed material the discovery pass built on.

**Imminent flag:** GNPS North Georgia Mountains chapter sale Saturday May 30, 2026, Union County Farmers Market, Blairsville (~45 min from Fernwood). Most ecologically-aligned single sourcing event of the year.

---

## Categories worth filling out (when active)

- **Native species for the planted zones** — bed candidates for the eastern/western patio zones, pond area, fairway-edge-west. Pulled from natural-community typology (Mesic Cove / Montane Oak mosaic at 2,873 ft).
- **Protected / at-risk species to look for and foster** — if found on the property, leave alone and support; rich-cove special-concern flora list is the starting point.
- **Restoration targets** — American chestnut and Eastern + Carolina hemlock are the two big landowner-participation species at this elevation.
- **Keystone / pollinator plants** — high-leverage species (oak, willow, cherry, blueberry, goldenrod) that punch above their weight ecologically.
- **Native cultivar trials** — Mt. Cuba Center's trial reports for native cultivars (their wild hydrangea trial, monarda trial, coreopsis trial, baptisia trial, etc.) — gold-standard evaluations of which cultivar of native species X performs best in the Mid-Atlantic / Appalachian range.

---

## Seed entries (initial — grow this list over time)

### Restoration targets (sourced from research-resources.md Cat 2)

| Species | Why | Partner |
|---|---|---|
| American chestnut (*Castanea dentata*) | Dominant canopy here pre-blight; this slope was once chestnut canopy | [The American Chestnut Foundation](https://tacf.org/) — Restoration Chestnut 1.0 (released 2005), GA chapter |
| Eastern hemlock (*Tsuga canadensis*) | Cool-drainage native; threatened by Hemlock Woolly Adelgid since 2012 in GA | [GFC HWA program](https://gatrees.org/hemlock-woolly-adelgid-hwa-in-georgia/) + [Hemlock Restoration Initiative](https://savehemlocksnc.org/) |
| Carolina hemlock (*Tsuga caroliniana*) | Range-limited Appalachian hemlock; under ESA review (2023) | Same partners as Eastern hemlock |

### Rich-cove special-concern flora (sourced from GA DNR — look-don't-pick if found, support if present)

Cucumber-root · galax · trailing arbutus · partridge-berry · round-leaved violet · umbrella leaf (in seepages) · turk's-cap lily · bee balm · Canadian wood nettle · Pink Lady's Slipper (*Cypripedium acaule*) · other native orchids

Full list with habitat associations: [GA DNR Natural Communities thumbnail PDF](https://georgiawildlife.com/sites/default/files/wrd/pdf/rare-data/natural_communities_thumbnail_accounts.pdf)

### Reference sources for picking native cultivars

- **[Mt. Cuba Center trial reports](https://mtcubacenter.org/research-publications/)** — multi-year evaluations of native cultivars. Especially relevant for any future native hydrangea (smooth / oakleaf), monarda, coreopsis, baptisia, asters, goldenrods, phlox, echinaceas planting decisions.
- **[Natural Communities of Georgia](https://www.naturalcommunitiesofgeorgia.com/)** — what should naturally grow at this elevation and aspect
- **[UGA SBG + GNPI recommended native nurseries (June 2025)](https://botgarden.uga.edu/wp-content/uploads/2023/04/Recommended-Native-Plant-Nurseries-List-GNPI-SBG-June-2025-1.pdf)** — ethical-provenance sourcing for any addition
- **[NWF Keystone Plants by Ecoregion](https://www.nwf.org/garden-for-wildlife/about/native-plants/keystone-plants-by-ecoregion)** — high-leverage genera (oak, willow, cherry, blueberry, goldenrod) at the family / genus level
- **research-resources.md Cat 2** in this repo — the assembled set of organizations, partners, and integration ideas

---

## How this connects later

- **Map view zones** — each candidate can carry a preferred zone hint. Pond area / fairway-edge-west / forest-interior all want different plants.
- **plants.json** — when a candidate moves from "considering" to "planted," it migrates into plants.json with full care calendar + photo + scientific name.
- **Phase E conversational layer** — "what could I plant near the pond?" becomes a query the assistant can answer by combining this file + the natural community typology + the zone data.
- **Phase G observations as knowledge layer** — observations like "found galax on the north slope today" could surface here as "already present, protect."

---

## Next steps (post-discovery, 2026-05-26)

1. **Session 2 — schema design.** Lock the `candidates.json` + `sources.json` shapes; freshness convention; promotion path (candidate → planted). Discovery doc has a starting draft.
2. **Session 3 — card design.** Engage ux-expert + content-steward for the Candidates card. Voice, naming, Mom-mode considerations.
3. **Session 4 — build.** Implement JSON + card render. Populate first operational batch (3-5 candidates Paul plants fall 2026 / spring 2027).
4. **Parallel — chase the gaps surfaced in discovery:** *(updated 2026-05-26 after the gap-chase pass)*
   - ~~UGA SBG/GNPI 2025 nursery list PDF is 404~~ ✓ **Resolved** — real URL has `-1-1-1` suffix, not `-1`. Working URL captured in `sources.json._meta.ugaNurseryListPdf`. Cross-referenced: Native Forest Nursery + Baker Environmental + Beech Hollow confirmed on 2025 list; Rock Spring Restorations dropped from 2025 list (flagged in `lastVerified`); two new nurseries added — The Herb Crib (Blairsville, same town as the May 30 GNPS sale) + North Georgia Native Plant Nursery (Canton).
   - ~~TACF GA chapter — landowner pathway~~ ✓ **Resolved** — pathway is national membership → Potential Orchard Steward form → stewardship plan with GA Science Coordinator → germplasm agreement. Multi-year commitment; chapter's own framing is that survival is not guaranteed. `frictionTier` raised to `high` in `sources.json`; chestnut candidate `notes` rewritten with the honest framing. Contact: gachapter@tacf.org, (828) 281-0047. Landowner intro: https://tacf.org/ga-news/so-you-want-to-plant-some-chestnuts/
   - ~~HRI — resistant-hemlock-stock sourcing~~ ✓ **Resolved** — resistant stock NOT yet available to landowners. Only actionable step is HWA treatment of existing hemlocks (imidacloprid + dinotefuran soil drench, DIY-friendly). Two ornamental hybrids ('Traveler', 'Crossroads') coming "in the near future" but landscape-only, not forest restoration. Hemlock candidate `notes` rewritten to split ACTIONABLE NOW vs FUTURE / NOT YET AVAILABLE. Contact for waitlist: 828-252-4783, info@savehemlocksnc.org.
   - GFC 2026-2027 seedling species catalog (publishes ~July 1, 2026) — still pending; set a reminder.
   - ~~Mt. Cuba current top picks for monarda, baptisia, echinacea, coreopsis~~ ✓ **Resolved** — added 4 new cultivar-trial candidates: 'Claire Grace' wild bergamot (clean native fit), 'Screamin' Yellow' baptisia (with 'Purple Smoke' alternative noted for stricter regional-native), 'Pica Bella' purple coneflower (clean native fit), 'Summer Sunshine' coreopsis (with 'Zagreb' alternative noted — C. palustris is coastal plain, not Blue Ridge). Cultivar-trial category now has 5 entries.
5. **Parallel — zone-naming pass.** The map view is paused awaiting Paul's zone vocabulary. Candidates `zoneAffinity` depends on it. ~30-min conversation.
6. **Cross-reference with field observations.** When Paul or Mom spot a candidate species already present (galax, trailing arbutus, lady's slipper), promote it from "consider sourcing" to "foster what's here."
