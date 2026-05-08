# Tate Tracker — Research Resources

A curated library of publications, organizations, and live data sources relevant to **282 Church Mountain Road, Jasper, GA** — assembled for the dashboard's "support local wildlife and plants, especially indigenous" goal.

Each entry includes:
- **Why it's relevant** to this specific property (zone, elevation, watershed, Bortle 3, etc.)
- **Dashboard integration idea** — concrete suggestion mapped to a viewer.html section
- **Depth tier** — Surface fact / Card subtitle / Deep-dive link / Live data source

---

## Top finds — the surprising stuff worth flagging

A few discoveries worth highlighting before the categorized list:

1. **The property's namesake history is real and rich.** Lake Sequoyah is in Pickens County at Tate Mountain Estates (~6.2 miles from Jasper, 38 acres) and was built around 1929 by Col. Sam Tate. The property's "Tate Tracker" name maps directly onto a piece of local history — there is genuine narrative material here for the Property card.

2. **You're on Cherokee land.** Pickens County was Cherokee Nation territory from 1793 until the 1838 Indian Removal. Talking Rock Creek (~6 miles from the property) was a major Cherokee settlement. The "indigenous plants" language in your stated goal hits differently with this context — and the EBCI's modern Center for Cherokee Plants gives you a direct, non-appropriative way to engage the heritage.

3. **The Etowah is one of the most biodiverse small river systems in North America.** Two federally-listed darters (Etowah Darter, Cherokee Darter) are *only* found in this watershed. Your property drains into their habitat. This is a marquee Wildlife card story.

4. **Bortle 3 puts you in the top tier of the Eastern US.** Stephen C. Foster State Park (the only IDA-certified site in Georgia) is Bortle 2; you're functionally one tier from the best dark sky in the state.

5. **Total lunar eclipse visible from Georgia on March 3, 2026.** Featured-event candidate for the celestial section.

6. **You're inside the textbook habitat for shade-grown native NTFPs** (ramps, ginseng, ginseng, sochan, goldenseal). The Appalachian Beginning Forest Farmer Coalition exists exactly to support this.

---

## Quick reference — live data sources (CORS-enabled, no key)

These are ready to wire directly into `viewer.html` with browser fetch:

| Source | Endpoint | Variable |
|---|---|---|
| **USGS NWIS** streamflow + gage height | `https://waterservices.usgs.gov/nwis/iv/?format=json&sites=02389150&parameterCd=00060,00065` | Etowah at GA-9 nr Dawsonville |
| **USGS NWIS** water temperature | `...&parameterCd=00010` | Trout-relevant water temp |
| **USGS Earthquakes** GeoJSON | `https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude=34.5496&longitude=-84.3674&maxradiuskm=200&minmagnitude=2.5&orderby=time&limit=1` | Last regional quake |
| **NWS api.weather.gov** sky cover | `GET /points/34.5496,-84.3674` → follow `forecastGridData` → `properties.skyCover.values[]` | Astronomy-relevant cloud forecast |
| **NASA SVS Dial-a-Moon** | `https://svs.gsfc.nasa.gov/vis/a000000/a005400/a005415/frames/730x730_1x1_30p/moon.NNNN.jpg` (NNNN = hour-of-year) | Live moon image |
| **Open-Meteo** (already integrated) | Add `cloud_cover_low/mid/high`, `visibility` | Stargazing score components |

These need a key + server-side proxy (CORS not supported):
- **AirNow AQI** — `https://www.airnowapi.org/aq/observation/latLong/current/?...` (free key)
- **NOAA NCEI Climate Normals** — `https://www.ncei.noaa.gov/access/services/data/v1` (free token)
- **US Drought Monitor** — `https://usdmdataservices.unl.edu/api/CountyStatistics/...&aoi=13227` (FIPS 13227 = Pickens County GA)

---

## Quick reference — programs Paul might enroll in / apply for

Concrete one-time actions, ordered by friction:

| Friction | Program | Cost | Outcome |
|---|---|---|---|
| Lowest | Register on Homegrown National Park map | Free | Property added to national grassroots biodiversity map |
| Low | NestWatch enrollment (Cornell) | Free | Citizen-science nest monitoring |
| Low | iNaturalist account + Pickens Co observations | Free | Cross-references Amphibians/Wildlife data |
| Low | FrogWatch USA training (Auburn chapter) | $10-15 | Authoritative monthsActive data for Amphibians tab |
| Low | SE Bumble Bee Atlas grid adoption | Free + 2 surveys/yr | Grounds the Pollinators story; aligns with Xerces |
| Low | Project FeederWatch (winter) | $18/yr | Winter Birds tab data |
| Low | Free Forest Stewardship Plan (GA Forestry Commission) | Free | Custom multi-resource plan for the property |
| Low | USFWS Partners for Fish and Wildlife site visit | Free | Free habitat-planning consultation |
| Medium | Birds Georgia Wildlife Sanctuary certification | $110 once | Mailable yard sign + 5-yr cert |
| Medium | NRCS EQIP / CSP cost-share | Free, application-based | Funded conservation practices |
| High | Conservation easement (Mountain Conservation Trust GA or GALT) | Legal cost | Permanent protection + tax benefits |

---

## Category 1: Extension & academia (Georgia-specific)

### Native Plants of North Georgia: A Photo Guide for Plant Enthusiasts (UGA Extension B 1339)
**URL:** https://extension.uga.edu/publications/detail.html?number=B1339 (PDF: https://fieldreport.caes.uga.edu/wp-content/uploads/2025/05/B-1339_4-1.pdf)
**What it is:** Free UGA Cooperative Extension photo-keyed bulletin covering native plants found specifically in North Georgia.
**Why it's relevant here:** The single most geographically-targeted Extension publication for the property — assumes the elevation, slope, and zone 7b/6b conditions of Pickens County. Far more useful than statewide guides.
**Dashboard integration idea:** Canonical "is it native to this property" reference. Link from any Plants > By Species detail card; use to vet draft additions before they leave staging.
**Depth tier:** Deep-dive link.

### Native Plants for Georgia, Part I: Trees, Shrubs, and Woody Vines (UGA Extension B 987)
**URL:** https://extension.uga.edu/publications/detail.html?number=B987
**What it is:** Flagship UGA Extension bulletin (Wade et al., revised 2024) on native woody plants suitable for Georgia landscapes.
**Why it's relevant here:** Directly covers most woody species already tracked — White Pine, native azaleas, dogwood, mountain laurel, oakleaf hydrangea, holly — with native-status notes and culture requirements.
**Dashboard integration idea:** Authoritative source for a "native status" badge on each Plant card (would flag boxwood and Japanese maple as non-native). Could power subtitles like "Native; common in north Georgia hardwood coves" on the Mountain Laurel card.
**Depth tier:** Card subtitle + deep-dive link.

### Native Plants for Georgia, Part III: Wildflowers (UGA Extension B 987-3)
**URL:** https://extension.uga.edu/publications/detail.html?number=B987-3
**What it is:** Companion to B 987 covering native wildflowers with culture, ID, and habitat (bog, dry sun, dry woodland, shaded streamside).
**Why it's relevant here:** Spec sheet for siting native ornamentals as the dashboard expands. The "shaded woodland adjacent to streams" framing matches the wooded ridge/cove conditions on Church Mountain Road.
**Dashboard integration idea:** Reference for any future Wildflowers sub-tab. Source for a "Worth checking this month" callout in March/April when ephemerals emerge.
**Depth tier:** Deep-dive link.

### Native Plants for Georgia, Part II: Ferns (UGA Extension B 987-2)
**URL:** https://extension.uga.edu/publications/detail.html?number=B987-2
**What it is:** Free Extension bulletin on Georgia's 36 genera, 119 species, and 12 hybrid native ferns.
**Why it's relevant here:** Shaded north-facing slopes at 2,959 ft routinely host Christmas fern, New York fern, and rattlesnake fern — natural additions to a habitat-focused dashboard.
**Dashboard integration idea:** Source if a Ferns category is added. Until then, a Surface fact in the Property profile: "Pickens County hosts ~30 of Georgia's native fern species."
**Depth tier:** Surface fact.

### UGA Extension — Pickens County Office
**URL:** https://extension.uga.edu/county-offices/pickens.html
**What it is:** Local Extension office offering soil testing, plant disease/pest ID, and Master Gardener programs.
**Why it's relevant here:** The actual front door for ground-truthing the property — soil samples and pest IDs go through here.
**Dashboard integration idea:** Permanent link on the Property profile under "Local resources." Plants card subtitle: "Soil tests run through UGA Pickens County."
**Depth tier:** Card subtitle + deep-dive link.

### Pollinator Garden Design Guide (UGA Extension B 1570-1)
**URL:** https://extension.uga.edu/publications/detail.html?number=B1570-1
**What it is:** Free UGA bulletin with appendices supplying Georgia-specific pollinator planting designs and species lists.
**Why it's relevant here:** Translates the "support local wildlife" goal into actionable plant combinations vetted for Georgia.
**Dashboard integration idea:** Georgia-specific design reference if a Pollinators sub-tab is added. Source for one-line callouts on the Plants card.
**Depth tier:** Deep-dive link.

### Selecting Trees and Shrubs as Resources for Pollinators (UGA Extension B 1483)
**URL:** https://extension.uga.edu/publications/detail.html?number=B1483
**What it is:** UGA Extension bulletin (Braman et al., 2023) ranking woody plants by pollinator value with bloom timing.
**Why it's relevant here:** Bridges the dashboard's woody-plant focus (azalea, hydrangea, mountain laurel, holly, dogwood) with the pollinator goal.
**Dashboard integration idea:** Source for a "pollinator value" badge on each woody Plant card (e.g., "Bloom: late spring — high bee value, per UGA B 1483").
**Depth tier:** Card subtitle.

### Beyond Butterflies: Gardening for Native Pollinators (UGA Extension B 1349)
**URL:** https://secure.caes.uga.edu/extension/publications/files/pdf/B%201349_1.PDF
**What it is:** UGA bulletin covering the full breadth of Georgia native pollinators (bees, flies, beetles, wasps).
**Why it's relevant here:** "Indigenous wildlife" extends to native bees and other invertebrates that don't show up in glossier guides.
**Dashboard integration idea:** Deep-reading link in Wildlife card. One-line factoid candidate: "Georgia hosts 500+ native bee species."
**Depth tier:** Surface fact + deep-dive link.

### Eco-Friendly Garden: Attracting Pollinators, Beneficial Insects, and Other Natural Predators (UGA Extension B 1456)
**URL:** https://extension.uga.edu/publications/detail.html?number=B1456
**What it is:** UGA on overwintering refuge, nectar/pollen continuity, and pest reduction through plant selection.
**Why it's relevant here:** Speaks to a "field journal, low-intervention" management philosophy — habitat structure over sprays.
**Dashboard integration idea:** Source for a low-key "leave the leaves" note on the Plants card in October/November copy.
**Depth tier:** Card subtitle.

### Connect to Protect — UGA State Botanical Garden of Georgia
**URL:** https://botgarden.uga.edu/connect-to-protect/
**What it is:** SBG's public-facing native plant program — curated lists, the Connect to Protect Native Plant Sale, and educational materials.
**Why it's relevant here:** Direct sourcing path for Georgia-genotype native plant material.
**Dashboard integration idea:** "Where to source native plants in Georgia" link on the Plants card. Tie native plant sale dates into Plants > This Month.
**Depth tier:** Card subtitle + deep-dive link.

### Mimsie Lanier Center for Native Plant Studies (UGA SBG)
**URL:** https://botgarden.uga.edu/conservation-science/mimsie-lanier-center-native-plant-studies/
**What it is:** SBG's research arm for native plant conservation, propagation, restoration; coordinates the Georgia Plant Conservation Alliance and Georgia native seed network (funded 2023).
**Why it's relevant here:** The serious end of "indigenous-first" — ecotype-correct seed and rare-plant propagation.
**Dashboard integration idea:** Deep-reading link in Property profile under "Conservation partners."
**Depth tier:** Deep-dive link.

### Native Trees of Georgia (Georgia Forestry Commission)
**URL:** https://gatrees.org/wp-content/uploads/2020/10/Native-Trees-of-GA-2013-Web-Version.pdf
**What it is:** Free 100+ page illustrated PDF guide by G. Norman Bishop (UGA), distributed by GFC.
**Why it's relevant here:** Self-contained tree ID reference at PDF scale — great offline companion for walking the woods. Covers the cove hardwood mix typical of 2,500–3,000 ft Blue Ridge.
**Dashboard integration idea:** "Tree ID field guide (PDF)" on the Property profile.
**Depth tier:** Deep-dive link.

### Georgia Forestry Commission — Forest Stewardship Program
**URL:** https://gatrees.org/forest-management-conservation/forest-stewardship-program/
**What it is:** Free state program pairing private landowners with consulting foresters and wildlife biologists to develop multi-resource Forest Stewardship Plans.
**Why it's relevant here:** Genuinely tailored guidance for a wooded mountain parcel — far more property-specific than any publication. Plans include wildlife and indigenous-species objectives.
**Dashboard integration idea:** Surface as "Free Forest Stewardship Plan available through GFC" in Property profile. One concrete next-step the dashboard can suggest without acting like a task manager.
**Depth tier:** Surface fact + deep-dive link.

### Warnell School of Forestry & Natural Resources — Outreach Publications
**URL:** https://www.warnelloutreach.org/publications.cfm
**What it is:** Free downloadable Warnell publications on forest management, wildlife habitat, urban forestry.
**Why it's relevant here:** Deepest Georgia-specific coverage of forest health, prescribed fire in Appalachian hardwoods, and wildlife habitat structure.
**Dashboard integration idea:** Resource link on Property profile or a hidden "Forestry" sub-section.
**Depth tier:** Deep-dive link.

### NC State Extension Gardener Handbook
**URL:** https://content.ces.ncsu.edu/extension-gardener-handbook
**What it is:** Comprehensive free full-text gardening handbook from NC State Extension.
**Why it's relevant here:** NC State's mountain-region material is often more directly applicable than UGA's Piedmont-leaning guidance, especially for cool-night/elevated sites.
**Dashboard integration idea:** Background reference for any Plant card with conditions that don't quite match UGA Piedmont expectations.
**Depth tier:** Deep-dive link.

### Clemson HGIC — Native Plants for Wildlife Resources
**URL:** https://hgic.clemson.edu/native-plants-for-wildlife-resources-for-home-gardeners/
**What it is:** Clemson Extension landing page plus a Carolina Yards database of ~300 plants filterable by wildlife supported.
**Why it's relevant here:** Upstate SC shares southern Appalachian flora with Pickens County GA. Filtering by wildlife outcome matches this dashboard's framing.
**Dashboard integration idea:** Cross-reference for the Wildlife card; "what supports what" lookup when populating bird/butterfly relationships per plant.
**Depth tier:** Deep-dive link.

---

## Category 2: Native plants & habitat

### North Georgia Mountains Chapter — Georgia Native Plant Society
**URL:** https://gnps.org/north-georgia-mountains/
**What it is:** GNPS's mountain chapter (formed 2021) covering Lumpkin, Towns, Union, White, Rabun counties; meetings at Union County Public Library in Blairsville, plus field trips, plant rescues, habitat certifications.
**Why it's relevant here:** The most ecologically aligned native-plant community for the property — Pickens is just south of the chapter's stated counties; species, soils, elevations are nearly identical.
**Dashboard integration idea:** Link as "Local chapter" on Property profile. Pull monthly meetings and native plant sale dates into Plants > This Month as soft prompts.
**Depth tier:** Card subtitle + deep-dive link.

### Georgia Native Plant Society — Plant of the Year
**URL:** https://gnps.org/
**What it is:** Statewide GNPS with member-voted annual Plant of the Year recognizing underused or ecologically important Georgia natives.
**Why it's relevant here:** A curated yearly nudge toward an indigenous species worth adding — a low-pressure recommendation engine that fits the field-journal tone.
**Dashboard integration idea:** Small "Plant of the Year" badge area on the Plants card showing the current GNPS pick. Updates once a year — almost zero maintenance.
**Depth tier:** Card subtitle.

### Audubon Plants for Birds (zip 30143)
**URL:** https://www.audubon.org/plantsforbirds
**What it is:** National Audubon's free zip-code-driven native plant database, filterable by bird family attracted, with bird-species lists per plant.
**Why it's relevant here:** Directly bridges the Plants card and Wildlife > Birds tab — for 30143, returns plants ranked by bird value.
**Dashboard integration idea:** Each plant on the Plants card carries a "supports N bird species (Audubon)" stat sourced from this database.
**Depth tier:** Card subtitle.

### Native Plant Finder (NWF / Tallamy / Shropshire) — zip 30143
**URL:** https://nativeplantfinder.nwf.org/
**What it is:** Free zip-code-driven database built on Doug Tallamy's research, ranking native plants by butterfly/moth caterpillar host count.
**Why it's relevant here:** Defensible, science-based answer to "which natives matter most for indigenous wildlife at 30143" — for north Georgia, dominated by oaks (~400+ Lepidoptera), willows, cherries, blueberries.
**Dashboard integration idea:** Pin a "Top keystone plants for 30143" mini-card in Plants — three or four species plus their Lepidoptera counts.
**Depth tier:** Card subtitle + deep-dive link.

### Homegrown National Park (Doug Tallamy)
**URL:** https://homegrownnationalpark.org/
**What it is:** Tallamy's grassroots biodiversity restoration project; site includes the keystone plants concept and a self-registration map.
**Why it's relevant here:** Philosophical anchor for the entire dashboard — "support local wildlife and plants, especially indigenous" is essentially the Homegrown National Park thesis.
**Dashboard integration idea:** Property profile subtitle: "Registered with Homegrown National Park" (once registered) — a quiet but meaningful identity marker.
**Depth tier:** Surface fact + deep-dive link.

### Keystone Plants by Ecoregion — National Wildlife Federation
**URL:** https://www.nwf.org/Native-Plant-Habitats/Plant-Native/Why-Native/Keystone-Plants-by-Ecoregion
**What it is:** NWF downloadable keystone-plant lists by EPA Level III ecoregion; for Pickens, Blue Ridge (66) / Southwestern Appalachians (68).
**Why it's relevant here:** The "if you only plant five things" answer for this specific ecoregion.
**Dashboard integration idea:** Source for a static "Keystone genera for the Blue Ridge: oak, cherry, willow, blueberry, goldenrod" surface fact on the Plants card.
**Depth tier:** Surface fact + deep-dive link.

### Mt. Cuba Center — Trial Garden Reports
**URL:** https://mtcubacenter.org/research/trial-garden/
**What it is:** Mt. Cuba's free multi-year native plant trial reports — Wild Hydrangea, Echinacea, Heuchera, Coreopsis, Baptisia, Monarda, Phlox, Helenium, Carex, Asters, Amsonia.
**Why it's relevant here:** The Wild Hydrangea report (2022) is directly applicable to the Hydrangea entries — currently ambiguous between native (H. arborescens, H. quercifolia) and non-native (H. macrophylla).
**Dashboard integration idea:** Plants > Hydrangea card subtitle: "Mt. Cuba's top wild hydrangea performer for the Mid-Atlantic: H. arborescens 'Haas' Halo'." Same pattern for any other genus that has a published trial.
**Depth tier:** Card subtitle + deep-dive link.

### Mt. Cuba Wild Hydrangea Top Performers (PDF)
**URL:** https://mtcubacenter.org/wp-content/uploads/2023/11/23034a-Trial-Garden-Top-Performers-Hydrangea-1.pdf
**What it is:** Two-page summary of Mt. Cuba's wild hydrangea trial top performers (H. arborescens and H. quercifolia selections).
**Why it's relevant here:** Direct, citable content for the existing Hydrangea entry — far more rigorous than nursery marketing.
**Dashboard integration idea:** Direct PDF link on the Hydrangea Plant card under "Recommended cultivars (Mt. Cuba)."
**Depth tier:** Deep-dive link.

### Xerces Society — Pollinator Conservation Resources: Southeast Region
**URL:** https://xerces.org/pollinator-resource-center/southeast
**What it is:** Curated hub: Southeast pollinator plant lists, native bee guides, nesting habitat instructions, monarch corridor materials, regional native plant nursery directory.
**Why it's relevant here:** Best-in-class invertebrate-focused source. Their Southeast plant list explicitly accounts for Appalachian conditions.
**Dashboard integration idea:** Anchor link for any Pollinators tab. Surface fact for Wildlife card: "~70% of native bees nest in the ground — leave bare patches."
**Depth tier:** Card subtitle + deep-dive link.

### Xerces Society — Pollinator Plants of the Southeast Region (PDF)
**URL:** https://xerces.org/sites/default/files/2018-05/17-053_03_XercesSoc_PollinatorPlants_Southeast-Region_web-3page.pdf
**What it is:** Free three-page region-specific PDF listing native plants highly attractive to native bees, butterflies, moths, hummingbirds.
**Why it's relevant here:** Compact enough to live as a printed companion at the homestead; tuned to the species pool the property can host.
**Dashboard integration idea:** Direct PDF download link from a Pollinators sub-tab or under "Field references" on the Property profile.
**Depth tier:** Deep-dive link.

### Georgia Botanical Society (BotSoc)
**URL:** https://www.gabotsoc.org/
**What it is:** Statewide native plant society publishing BotSoc News, the Tipularia botanical journal, and running a Spring Wildflower Pilgrimage. The 2026 Pilgrimage is May 1–3 in Clayton, GA — about 90 minutes from Jasper.
**Why it's relevant here:** Trips routinely visit Blue Ridge, Cohutta, and Chattahoochee NF — landscapes ecologically continuous with the property. Tipularia's southern Appalachian articles match the field-journal depth this dashboard wants.
**Dashboard integration idea:** Pull upcoming trip dates into Plants > This Month as low-pressure prompts. Tipularia issues become deep-reading links.
**Depth tier:** Deep-dive link.

### Georgia Botanical Society — 2026 Field Trips
**URL:** https://www.gabotsoc.org/field-trips-2/2026-field-trips/
**What it is:** 2026 BotSoc field trip calendar with date, location, leader, registration.
**Why it's relevant here:** Concrete dated events within an hour of Jasper.
**Dashboard integration idea:** Mirror trips into a "Worth checking this month" callout on the Plants card.
**Depth tier:** Card subtitle.

### Atlanta Botanical Garden — Southeastern Center for Conservation
**URL:** https://atlantabg.org/conservation-research/southeastern-center-for-conservation/
**What it is:** ABG's research center for imperiled Southeastern species, with active North Georgia mountain projects on rare orchids, magnolias, oaks.
**Why it's relevant here:** Their North Georgia fieldwork is geographically next door; species lists for at-risk natives are a candidate filter when adding plants.
**Dashboard integration idea:** Property profile deep-link: "Conservation work happening in our mountains."
**Depth tier:** Deep-dive link.

### Lady Bird Johnson Wildflower Center — Native Plant Database
**URL:** https://www.wildflower.org/plants/
**What it is:** Searchable database of 9,000+ North American native plants with state Recommended Species lists; filterable by light, soil, growth habit, bloom.
**Why it's relevant here:** Often the cleanest single reference page per species.
**Dashboard integration idea:** "More info" link on every Plant detail card (default outbound link if no UGA bulletin exists).
**Depth tier:** Deep-dive link.

### Birds Georgia (formerly Georgia Audubon) — Plants for Birds & Wildlife Sanctuary Certification
**URL:** https://www.birdsgeorgia.org/plants-for-birds.html
**What it is:** Georgia's Audubon affiliate runs Wildlife Sanctuary certification (600+ properties statewide), the Plants for Birds initiative (1M native plants goal), and twice-yearly native plant sales with Beech Hollow Wildflower Farms.
**Why it's relevant here:** Cleanest path to a meaningful, low-cost certification recognizing native plantings on Church Mountain Road — and a sourcing channel for hard-to-find Georgia natives.
**Dashboard integration idea:** Property profile subtitle: "Eligible for Birds Georgia Wildlife Sanctuary certification." Link Audubon native plant sale dates into Plants > This Month.
**Depth tier:** Card subtitle + deep-dive link.

### Georgia DNR — Create Backyard Habitat
**URL:** https://georgiawildlife.com/create-backyard-habitat
**What it is:** GA DNR's residential habitat creation page: nest box plans, brush pile guidance, mowing-less recommendations, native-plant-first messaging.
**Why it's relevant here:** State-level, free, tonally aligned with the field-journal voice — practical guidance like "mow less, ditch chemicals, plant natives" rather than urgent action lists.
**Dashboard integration idea:** Anchor link from Wildlife card. Source for one-liners like "Brush piles and standing dead trees are habitat features, not eyesores."
**Depth tier:** Card subtitle + deep-dive link.

---

## Category 3: Wildlife (state & federal)

### Georgia DNR — State Wildlife Action Plan 2025 (Blue Ridge Ecoregion)
**URL:** https://georgiawildlife.com/WildGeorgiaSWAP
**What it is:** Georgia's official 10-year (2025–2035) conservation roadmap identifying 1,062 Species of Greatest Conservation Need (SGCN) and the habitats essential for their survival, with dedicated story maps per ecoregion.
**Why it's relevant here:** The property is in the Blue Ridge ecoregion at 2,959 ft — the SWAP Blue Ridge story map flags the exact mountain-specific SGCN species (salamanders, high-elevation breeding warblers, native trout) the dashboard should care about.
**Dashboard integration idea:** Birds/Amphibians tab subtitle linking to the Blue Ridge story map. Tag matching species in species lists with a small "SGCN" marker.
**Depth tier:** Card subtitle + deep-dive link.

### eBird — Pickens County, GA (Cornell Lab)
**URL:** https://ebird.org/region/US-GA-227
**What it is:** Cornell's birding database with a dedicated Pickens County page showing recent sightings, hotspots, monthsPresent bar charts, and an illustrated checklist generated from real observations.
**Why it's relevant here:** Single best data source for the Birds tab's monthsPresent and status fields — eBird bar charts visualize exactly that. Free, public.
**Dashboard integration idea:** Link each Birds-tab species name to its eBird Pickens County bar chart (`ebird.org/species/[code]/US-GA-227`); "Recent sightings near you" subtitle linking to the county page. Use eBird abundance bars as source of truth for monthsPresent.
**Depth tier:** Surface fact + deep-dive link per species.

### USFWS IPaC — Information for Planning and Consultation
**URL:** https://ipac.ecosphere.fws.gov/
**What it is:** Federal interactive tool — draw a project area, get the official list of federally listed species, critical habitat, migratory birds known/believed to occur there.
**Why it's relevant here:** Authoritative federal species list for the exact 282 Church Mountain Rd parcel — most defensible source for any "federally listed species on or near this property" claim.
**Dashboard integration idea:** Wildlife card footer link: "Federally tracked species at this address (USFWS IPaC)." One-time pull, then surface a list of federally listed species the property might host (likely: Indiana bat, northern long-eared bat, monarch butterfly).
**Depth tier:** Deep-dive link.

### Birds Georgia — Wildlife Sanctuary Program
**URL:** https://www.birdsgeorgia.org/wildlife-sanctuary-program.html
**What it is:** Statewide private-property certification recognizing yards with 4+ food sources, 1+ water source, 4+ shelter options, no outdoor cats, native plant focus. Virtual assessment, $75 fee + $35 membership, 5-year renewal.
**Why it's relevant here:** Directly maps to "support indigenous wildlife and plants" — most concrete Georgia-specific certification with a mailable yard sign.
**Dashboard integration idea:** Small "Certifications" sub-card under Wildlife with a checklist mirroring requirements (food sources met, water source met, shelter count, cat-free) and an "Apply for certification" CTA. Field-journal phrasing: "Four shelter spots noted — sanctuary criteria met."
**Depth tier:** Card subtitle + deep-dive link.

### Audubon — Survival by Degrees Climate Visualizer
**URL:** https://www.audubon.org/climate/survivalbydegrees
**What it is:** ZIP-code-searchable tool modeling how 604 North American bird species' ranges shift under 1.5/2/3°C scenarios. Eight Georgia birds (Brown-headed Nuthatch, Eastern Whip-poor-will, Eastern Towhee) flagged as highly vulnerable.
**Why it's relevant here:** The property's 2,959 ft elevation is exactly the kind of high-elevation refuge where climate-stressed Appalachian breeders may persist longest.
**Dashboard integration idea:** Birds tab — small climate-vulnerability dot/icon next to each tracked species (sourced from Audubon's species list for ZIP 30143). Subtitle: "These birds are losing range — your mountain is part of their refuge."
**Depth tier:** Surface fact (per-species marker).

### iNaturalist — Pickens County, GA
**URL:** https://www.inaturalist.org/places/pickens-county
**What it is:** Crowd-sourced research-grade biodiversity database with a Pickens County page showing all observed taxa, observer counts, monthly activity charts.
**Why it's relevant here:** Best single source for amphibians and pollinators (eBird doesn't cover them). GA DNR's Wildlife Conservation Section uses iNaturalist data to time surveys for tracked species.
**Dashboard integration idea:** Amphibians tab — each species links to its Pickens County observation page (`inaturalist.org/observations?place_id=...&taxon_id=...`) so monthsActive can be verified against real local sightings. "Log this sighting on iNaturalist" CTA.
**Depth tier:** Card subtitle + deep-dive link per species.

### Southeast Bumble Bee Atlas (Xerces + GA DNR)
**URL:** https://www.bumblebeeatlas.org/pages/southeast
**What it is:** Community-science survey of bumble bees across GA/NC/SC/TN, jointly run by Xerces Society and Georgia DNR. Volunteers adopt a grid cell, attend free training, conduct two surveys per season. No fee.
**Why it's relevant here:** North Georgia mountain populations of native bumble bees (incl. potentially the at-risk American bumble bee, Bombus pensylvanicus) are under-surveyed; the property could adopt a nearby grid cell directly tied to the "support indigenous" goal.
**Dashboard integration idea:** "Pollinators" subsection or callout on Wildlife — citizen science enrollment CTA: "Adopt a bumble bee survey grid (free, May–Sep)." Show 2026 field season window.
**Depth tier:** Card subtitle + deep-dive link.

### USFWS Partners for Fish and Wildlife — Georgia Program
**URL:** https://www.fws.gov/project/georgia-partners-fish-and-wildlife
**What it is:** Free federal technical and financial assistance for private landowners doing wildlife habitat restoration. Voluntary, customized projects; landowner retains all rights and access. ~145 GA landowners enrolled, ~11,000 acres restored since 1995.
**Why it's relevant here:** Private land in a high-priority Blue Ridge habitat zone — eligible for free expert site visits and potential cost-share for stream/riparian restoration, native plantings, pollinator meadows.
**Dashboard integration idea:** Wildlife card footer or "Programs" section: "Free USFWS habitat planning visit — see if your property qualifies."
**Depth tier:** Deep-dive link.

### USDA Forest Service — Chattahoochee-Oconee NF Fire & Wildlife Management
**URL:** https://www.fs.usda.gov/r08/chattahoochee-oconee/fire/management
**What it is:** Operational hub for the national forest's prescribed-fire program (~35,000 acres burned annually Feb–Apr) and forest-management practices supporting fire-dependent species.
**Why it's relevant here:** Property is near/borders the Chattahoochee NF; prescribed-burn smoke days, post-burn songbird responses, and fire-dependent oak/pine ecology directly affect the property's wildlife calendar and outdoor planning.
**Dashboard integration idea:** Seasonal field-journal callout: "Prescribed-burn season nearby (Feb–Apr) — songbirds usually return strongly within weeks."
**Depth tier:** Card subtitle (seasonal) + deep-dive link.

### NestWatch (Cornell Lab)
**URL:** https://nestwatch.org/
**What it is:** Free national nest-monitoring citizen-science program with structured protocols. Free certification quiz; no fee.
**Why it's relevant here:** Mix of forest edge and likely hummingbird/bluebird/wren nest opportunities is ideal NestWatch habitat; natural extension of the Birds tab into breeding-season detail.
**Dashboard integration idea:** When a tracked species is in its nesting window (e.g., Eastern Bluebird Apr–Jul), surface a quiet prompt: "Worth checking nest boxes this month — log on NestWatch."
**Depth tier:** Card subtitle (seasonal) + deep-dive link.

### Project FeederWatch (Cornell Lab + Birds Canada)
**URL:** https://feederwatch.org/
**What it is:** November–April winter feeder survey. Pick "count days," report highest simultaneous count per species. $18/yr in US; account required.
**Why it's relevant here:** Property's elevation puts it in Junco/Purple Finch/White-throated Sparrow winter territory — Pickens County is right at the southern edge of some northern-finch irruption zones.
**Dashboard integration idea:** Birds tab — winter mode (Nov–Apr) shows feeder-relevant species first; subtle FeederWatch link.
**Depth tier:** Card subtitle (seasonal).

### Merlin Bird ID (Cornell Lab)
**URL:** https://merlin.allaboutbirds.org/
**What it is:** Free mobile app with photo ID, sound ID, step-by-step ID. Sound ID is the killer feature — point your phone at the woods for a real-time list of what's calling.
**Why it's relevant here:** The property is dense forest where most birds are heard before seen — Merlin Sound ID is the fastest way to validate the Birds tab's species list.
**Dashboard integration idea:** Birds tab footer: "Identify a call right now — open Merlin." Could surface the day's top likely audio detections (cross-reference monthsPresent + Merlin's regional pack).
**Depth tier:** Surface fact (app link).

### FrogWatch USA (AZA)
**URL:** https://www.aza.org/frogwatch
**What it is:** Citizen-science frog/toad call monitoring. 3-minute listening sessions Feb–Aug evenings. ~$10–15 training; chapter at Auburn University Museum of Natural History serves the Southeast.
**Why it's relevant here:** Property's elevation and likely seeps/streams are prime habitat for spring peeper, gray treefrog, American toad, and possibly mountain chorus frog — all detected by call. Directly populates Amphibians tab monthsActive.
**Dashboard integration idea:** Amphibians tab citizen-science callout: "Log frog calls 3 min after sunset (Feb–Aug) with FrogWatch USA." Each species' monthsActive bar can link to typical calling window.
**Depth tier:** Card subtitle + deep-dive link.

### SREL Herpetology — UGA Savannah River Ecology Lab
**URL:** https://srelherp.uga.edu/
**What it is:** Long-running UGA research site documenting 100+ amphibian and reptile species of GA/SC, with detailed species accounts (range maps, life history, calls). De facto Georgia herp reference.
**Why it's relevant here:** Has dedicated species accounts for the Blue Ridge salamanders/frogs likely on the property (Blue Ridge Two-lined Salamander, Spring Peeper, Gray Treefrog) — better than AmphibiaWeb for GA-specific natural history.
**Dashboard integration idea:** Amphibians tab — each species name links to its SREL account page (`srelherp.uga.edu/salamanders/[species]/` or `/frogs/[species]/`) for the deep-dive expand row.
**Depth tier:** Deep-dive link per species.

### Bat Conservation International — Build a Bat House
**URL:** https://www.batcon.org/about-bats/bat-gardens-houses/
**What it is:** Authoritative source for BCI-certified bat-house plans (≥25 in tall, ¾ in chambers, S/SE-facing, 6–8 hr sun) and White-Nose Syndrome research. WNS has decimated tri-colored bat and northern long-eared bat across the Southeast.
**Why it's relevant here:** North Georgia caves/hollows host species hit hard by WNS; a BCI-spec bat house at the property gives displaced colonies a clean alternative.
**Dashboard integration idea:** Wildlife card — "Bats" mention either as a fourth tab eventually, or as a Programs callout with one BCI link to certified plans. Phrasing: "Bat house worth installing — south-facing, 25 in tall."
**Depth tier:** Deep-dive link.

### Georgia Biodiversity Portal (GA DNR Natural Heritage)
**URL:** https://georgiabiodiversity.org/
**What it is:** GA DNR's official rare-species and natural-community database, including state-protected and federally-protected species ranked by Natural Heritage methodology. County-filterable lists.
**Why it's relevant here:** State-level companion to USFWS IPaC — surfaces state-listed species (not just federally listed) that may occur in Pickens County.
**Dashboard integration idea:** Wildlife card footer: "State-tracked rare species in Pickens County" deep-dive link. Cross-reference with USFWS IPaC.
**Depth tier:** Deep-dive link.

### Bumble Bees of the Eastern United States (Colla, Richardson & Williams — USFS)
**URL:** https://www.pollinator.org/pollinator.org/assets/generalFiles/BumbleBeeGuide2011.pdf
**What it is:** Free 103-page PDF field guide covering all 21 eastern US bumble bee species, with range maps, ID plates, host-plant info. Co-published by USDA Forest Service.
**Why it's relevant here:** Standard ID reference paired with the SE Bumble Bee Atlas — at 2,959 ft the property is in range of mountain-affiliated species like B. vagans and possibly B. fervidus.
**Dashboard integration idea:** Pollinators callout — "Eastern bumble bee field guide (PDF, free)" deep-dive link.
**Depth tier:** Deep-dive link.

### Hummingbirds at Home (National Audubon)
**URL:** https://www.audubon.org/conservation/about-hummingbirds-home
**What it is:** Free Audubon citizen-science program tracking hummingbird feeder visits and native nectar plant interactions. Climate-driven shifts focus.
**Why it's relevant here:** Ruby-throated Hummingbird is the only eastern US breeder and definitely uses the property (typical arrival mid-Apr in north GA mountains, departure early Oct).
**Dashboard integration idea:** Birds tab — when Ruby-throated's monthsPresent window opens, surface "Worth filling the feeder" + Hummingbirds at Home link. Pair with native-nectar-plant cross-reference (jewelweed, cardinal flower, bee balm).
**Depth tier:** Card subtitle (seasonal) + deep-dive link.

---

## Category 4: Land, soil, water

### USDA NRCS Web Soil Survey
**URL:** https://websoilsurvey.nrcs.usda.gov/app/
**What it is:** USDA's interactive tool for generating custom soil reports (series, slope, depth, drainage, suitability) for any user-drawn area, backed by SSURGO.
**Why it's relevant here:** The 282 Church Mountain Road property sits on Blue Ridge mountain soils — likely Edneyville, Ashe, Chestnut, or Junaluska series typical of Pickens County's steep forested slopes.
**Dashboard integration idea:** Property card → "Soil series" subtitle. One-time WSS lookup keyed to the property polygon; bake the dominant component name and key drainage/erosion class into static config. Link the subtitle to a saved WSS AOI report for the deep-dive.
**Depth tier:** Card subtitle (one-time lookup, baked in).

### USDA NRCS Soil Data Access (SDA) Web Services
**URL:** https://sdmdataaccess.nrcs.usda.gov/ (query help: https://sdmdataaccess.nrcs.usda.gov/QueryHelp.aspx)
**What it is:** REST API serving SSURGO spatial and tabular data via T-SQL queries; returns JSON. Also offers WFS/WMS endpoints. 100,000-row / 32 MB query cap.
**Why it's relevant here:** Programmatic alternative to WSS — pulls the soil component for the exact property coordinates instead of manually exporting a report.
**Dashboard integration idea:** Build-time script POSTing T-SQL against the property point (34.5496, -84.3674) to populate the Property card's soil field. CORS support is limited; treat as server-side or build-step lookup.
**Depth tier:** Live data source (build-time).

### USGS NWIS Water Services API (Instantaneous Values)
**URL:** https://waterservices.usgs.gov/ (docs: https://waterservices.usgs.gov/docs/instantaneous-values/instantaneous-values-details/)
**What it is:** REST API returning JSON/XML/RDB for current and historical streamflow, gage height, water temperature, and other parameters. Free, no auth.
**Why it's relevant here:** The obvious "live USGS stream gauge" data source. Etowah River gauges upstream and downstream of the property anchor the watershed health story.
**Dashboard integration idea:** Property/Weather card → live "Etowah at GA-9 near Dawsonville" discharge (cfs) and gage height. Endpoint: `https://waterservices.usgs.gov/nwis/iv/?format=json&sites=02389150&parameterCd=00060,00065&siteStatus=all`. **CORS enabled** — direct browser fetch works.
**Depth tier:** **Live data source** (CORS-enabled JSON).

### USGS Monitoring Locations — Etowah River near Dawsonville (02389150) & Canton (02392000)
**URL:** https://waterdata.usgs.gov/monitoring-location/USGS-02389150/ and https://waterdata.usgs.gov/monitoring-location/USGS-02392000/
**What it is:** Site pages for the two closest active USGS gauges on the mainstem Etowah.
**Why it's relevant here:** 02389150 is the most representative for "headwaters near my property." 02392000 gives long-term flow context downstream.
**Dashboard integration idea:** Hard-code these two site numbers as the dashboard's default streamflow context. 02389150 primary, 02392000 "downstream comparison."
**Depth tier:** Surface fact (gauge IDs).

### USGS StreamStats — Georgia
**URL:** https://streamstats.usgs.gov/ss/ (Georgia overview: https://www.usgs.gov/streamstats/georgia-streamstats)
**What it is:** Map-based web app delineating a watershed for any clicked stream point and computing flow statistics for ungauged streams.
**Why it's relevant here:** The unnamed creek behind 282 Church Mountain Road is almost certainly ungauged. StreamStats can produce a property-specific watershed area, mean annual flow estimate, and flood frequency.
**Dashboard integration idea:** Property card → "Watershed" subtitle with computed acreage, mean annual flow, 100-year flood Q. One-time delineation cached.
**Depth tier:** Card subtitle (one-time, cached) + deep-dive link.

### USGS Earthquake Hazards — GeoJSON Feeds & FDSN Event API
**URL:** https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php and https://earthquake.usgs.gov/fdsnws/event/1/
**What it is:** Real-time GeoJSON summary feeds (hour/day/week/month) and a customizable FDSN query API filtered by lat/lon/radius/magnitude/time.
**Why it's relevant here:** Southern Appalachians are seismically quiet but not silent — the 2018 Decatur, TN M4.4 was felt across north Georgia. A field-journal cue noting recent regional quakes adds character without being alarmist.
**Dashboard integration idea:** Property card subtitle → "Last regional quake." Endpoint: `https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude=34.5496&longitude=-84.3674&maxradiuskm=200&minmagnitude=2.5&orderby=time&limit=1`. **CORS enabled.**
**Depth tier:** **Live data source** (CORS-enabled GeoJSON).

### Georgia EPD Watershed Protection Branch — TMDLs and 303(d) Listings
**URL:** https://epd.georgia.gov/watershed-protection-branch/watershed-planning-and-monitoring-program/total-maximum-daily-loadings
**What it is:** Georgia's CWA implementation arm — publishes the biennial 303(d) impaired waters list, develops TMDLs, runs statewide ambient water-quality monitoring.
**Why it's relevant here:** Tells you whether your specific Etowah headwater tributary or downstream Lake Sequoyah is listed as impaired (sediment, fecal coliform, biota), directly informing the "support local wildlife and plants" goal.
**Dashboard integration idea:** Property card deep-dive: "Watershed status (GA EPD)." Pull the current 303(d) PDF and note relevant Etowah segment ID in static config; refresh annually.
**Depth tier:** Deep-dive link.

### USDA NRCS EQIP — Georgia
**URL:** https://www.nrcs.usda.gov/programs-initiatives/environmental-quality-incentives-program/georgia/environmental-quality
**What it is:** NRCS's flagship cost-share program — pays non-industrial private forest landowners to install conservation practices (forest stand improvement, prescribed burning, invasive removal, erosion control, wildlife habitat).
**Why it's relevant here:** "Support local wildlife and plants, especially indigenous" maps directly to EQIP forestry practices. Pickens County is fully eligible; sign-ups continuous, with annual ranking cutoffs.
**Dashboard integration idea:** "Programs you may qualify for" deep-dive in a Property or Stewardship section.
**Depth tier:** Deep-dive link.

### USDA NRCS Conservation Stewardship Program (CSP) — Georgia
**URL:** https://www.nrcs.usda.gov/programs-initiatives/conservation-stewardship-program/georgia/conservation-stewardship-program
**What it is:** Five-year working-lands payment program rewarding existing and new conservation activities; available on non-industrial private forest land.
**Why it's relevant here:** Complements EQIP — pays for ongoing stewardship rather than one-time installation, fitting an owner managing the property long-term for wildlife.
**Dashboard integration idea:** Pair with EQIP under a "Stewardship programs" deep-dive cluster.
**Depth tier:** Deep-dive link.

### USDA NRCS Plants Database
**URL:** https://plants.usda.gov/
**What it is:** Authoritative federal database of plant names, distribution by state and county, native/introduced status, wetland indicator, characteristics, images.
**Why it's relevant here:** Direct way to confirm which species are documented as native to Pickens County — exactly what "indigenous" needs.
**Dashboard integration idea:** Wildlife/Plants card deep-dive: "Native species in Pickens County." Curated subset baked in from the official site.
**Depth tier:** Deep-dive link.

### Coosa River Basin Initiative (CRBI)
**URL:** https://coosa.org/
**What it is:** Rome, GA-based 501(c)(3) since 1992; advocates and educates for the Upper Coosa basin (TN through NW Georgia to Weiss Dam, AL) — the most biologically diverse river basin in North America.
**Why it's relevant here:** The property drains directly into Etowah headwaters → Coosa basin. CRBI publishes the Etowah River User's Guide and runs Adopt-A-Stream and pollution litigation work locally.
**Dashboard integration idea:** Watershed card subtitle "Coosa basin" linking to CRBI's about/programs page.
**Depth tier:** Card subtitle + deep-dive link.

### Upper Etowah River Alliance (UERA)
**URL:** https://www.etowahriver.org/
**What it is:** Watershed nonprofit (founded 1998) covering the Etowah upstream of Lake Allatoona — explicitly serves Pickens, Cherokee, Dawson, Forsyth, Lumpkin counties. Runs Adopt-A-Stream and education.
**Why it's relevant here:** Most geographically specific watershed group for the property. Pickens County is one of UERA's five core counties; the upper Etowah's 92 native fish species and 5 endemics are core to the conservation story.
**Dashboard integration idea:** Watershed card primary affiliation link, above CRBI (broader). Subtitle "Upper Etowah Alliance — Pickens County watershed."
**Depth tier:** Card subtitle + deep-dive link.

### Mountain Conservation Trust of Georgia (MCT)
**URL:** https://mctga.org/
**What it is:** Accredited land trust focused exclusively on the North Georgia foothills and mountains; 7,500+ acres permanently protected via easements, fee acquisition, stewardship agreements.
**Why it's relevant here:** MCT's geographic mandate is precisely the property's region. The most directly aligned land trust if a conservation easement on Church Mountain Road ever makes sense.
**Dashboard integration idea:** Stewardship/Property deep-dive: "Conservation easement options." Link to mctga.org/conserving-your-land/conservation-options/.
**Depth tier:** Deep-dive link.

### Georgia Forestry Commission — Forest Stewardship Program
**URL:** https://gatrees.org/forest-management-conservation/forest-stewardship-program/
**What it is:** State program in which GFC field foresters write a free, custom multi-resource Forest Stewardship Plan for non-industrial landowners (timber, wildlife, soil/water, recreation, aesthetics).
**Why it's relevant here:** The free management plan is the practical entry point to most other programs (EQIP cost-share, Tree Farm certification, property tax conservation use). Pickens County is served.
**Dashboard integration idea:** Stewardship deep-dive: "Free GA Forestry forest plan (1-800-GA-TREES)." Pair with NRCS programs as a "first-step" cluster.
**Depth tier:** Deep-dive link.

### USDA Climate Hubs — Southeast Region
**URL:** https://www.climatehubs.usda.gov/hubs/southeast
**What it is:** USDA's regional translation arm linking USFS, ARS, NRCS climate science to working-lands managers; publishes vulnerability assessments and tools (TACCIMO).
**Why it's relevant here:** The Southern Appalachian forest section of the SE Hub's Vulnerability Assessment is directly applicable to a 2,959 ft Blue Ridge property thinking about long-term species shifts.
**Dashboard integration idea:** "Long view" deep-dive in the Property card.
**Depth tier:** Deep-dive link.

### Georgia-Alabama Land Trust (GALT)
**URL:** https://www.galandtrust.org/
**What it is:** The Southeast's largest land trust — 1,360+ properties / 518,000+ acres protected. Holds easements across Georgia, Alabama, adjacent states; partners with NRCS on ALE/WRE federal easement programs.
**Why it's relevant here:** Alternative or complement to MCT for conservation easements. Larger geographic reach but less North-Georgia-specific than MCT.
**Dashboard integration idea:** Pair with MCT under a "Land trust options" deep-dive cluster.
**Depth tier:** Deep-dive link.

### MountainTrue
**URL:** https://mountaintrue.org/
**What it is:** Southern Blue Ridge regional advocacy nonprofit, historically focused on Western North Carolina but now formally working in Towns and Union counties, GA after the Hiwassee River Watershed Coalition merger.
**Why it's relevant here:** Less directly aligned (Pickens not yet in MountainTrue's GA service area), but the most relevant Southern Blue Ridge regional voice on Nantahala-Pisgah and broader forest policy that affects upstream conditions.
**Dashboard integration idea:** Optional regional context link.
**Depth tier:** Surface fact / optional deep-dive.

### The Nature Conservancy — Upper Coosa River Basin (Georgia)
**URL:** https://www.nature.org/en-us/get-involved/how-to-help/places-we-protect/upper-coosa-river-basin/
**What it is:** TNC's place-based program for the Upper Coosa, with active conservation work in the Cohutta-Conasauga complex one ridge west of the property — protecting one of the most biodiverse river systems in North America (4,000 plant species, 250 endemic).
**Why it's relevant here:** Frames the property within the Upper Coosa biodiversity story; the Etowah and Conasauga are sister sub-basins of the same system.
**Dashboard integration idea:** Watershed card flavor/context: "You live in one of North America's most biodiverse river systems."
**Depth tier:** Deep-dive link.

---

## Category 5: Fishing & aquatic (Lake Sequoyah / regional)

> **Note on Lake Sequoyah identity:** Confirmed — Sequoyah Lake is a 38-acre reservoir at Tate Mountain Estates in Pickens County (~6.2 mi from Jasper, ~2,800 ft elevation), built by Col. Sam Tate around 1929. The property's "Tate Tracker" name has a real local-historical anchor here. Public-access status is unclear; appears HOA/private — confirm before publishing fishing-regulation content.

### Georgia DNR WRD — Trout Fishing & Stocking
**URL:** https://georgiawildlife.com/Fishing/Trout
**What it is:** Georgia's official trout regulations, stocking schedule, and stream classification page; weekly stocking reports published April–Labor Day. 160 streams stocked statewide.
**Why it's relevant here:** Pickens County borders the seasonal trout zone, and Chattahoochee NF streams within ~30 minutes of the property (Amicalola, Cartecay, Mountaintown Creek, Rock Creek) are stocked. Drives "best months" timing for trout.
**Dashboard integration idea:** Fishing tab → "This week's stocked streams near you." No public JSON API; weekly bulletin is HTML/PDF — scrape into static JSON cache or link as deep-dive.
**Depth tier:** Deep-dive link (with manual weekly cache).

### Georgia DNR WRD — Fisheries Management
**URL:** https://georgiawildlife.com/fishing/angler-resources
**What it is:** Annual Georgia Fishing Regulations Guide, regional fisheries reports, lake-specific reports (typically larger public lakes; small lakes like Sequoyah may not have a dedicated report).
**Why it's relevant here:** Source of truth for bass/crappie/bluegill/catfish regulations. Lake Sequoyah is small and likely private — verify whether GA fishing license rules apply or whether HOA-regulated.
**Dashboard integration idea:** Fishing tab footer: "GA fishing regulations" deep-dive.
**Depth tier:** Deep-dive link.

### Georgia Fishing Regulations (eRegulations)
**URL:** https://www.eregulations.com/georgia/fishing
**What it is:** Mobile-friendly version of GA's annual fishing regs — daily creel limits, length limits, season dates per species.
**Why it's relevant here:** Lake Sequoyah's species list maps directly to specific GA creel/length rules.
**Dashboard integration idea:** Each Fishing tab species row shows current creel + length limit pulled from eRegs; "Full GA fishing regs" deep-dive in tab footer.
**Depth tier:** Surface fact (per-species limits) + deep-dive link.

### USFWS Chattahoochee Forest National Fish Hatchery
**URL:** https://www.fws.gov/fish-hatchery/chattahoochee-forest
**What it is:** Federal hatchery in the Chattahoochee NF producing ~1 million rainbow, brook, brown trout annually for stocking into north Georgia public waters with GA DNR, USACE, TVA, USFS. ~9 of every 10 trout caught in Georgia originate here.
**Why it's relevant here:** Closest-fact "where do the trout come from" anchor for the field-journal voice.
**Dashboard integration idea:** Fishing tab subtitle/fact: "Your trout come from Chattahoochee Forest NFH."
**Depth tier:** Surface fact / card subtitle.

### Blue Ridge Mountain Trout Unlimited (Chapter 696)
**URL:** https://blueridgetu.com/ (TU page: https://www.tu.org/chapters/georgia/blue-ridge-mountain/)
**What it is:** TU chapter formed in 1988, based at Mineral Bluff (north of Blue Ridge); coldwater conservation, host of the annual Blue Ridge Trout Festival.
**Why it's relevant here:** Closest TU chapter to Pickens County / Jasper. The Georgia Foothills chapter is further east despite its name.
**Dashboard integration idea:** Fishing tab community deep-dive: "Local Trout Unlimited chapter."
**Depth tier:** Deep-dive link.

### USGS NWIS Water Services API — Stream Temperature & Flow for Trout Habitat
**URL:** https://waterservices.usgs.gov/
**What it is:** Same NWIS API; many north Georgia gauges report water temperature (parameterCd=00010) alongside discharge (00060) and gage height (00065). Trout stress above ~68°F.
**Why it's relevant here:** The Fishing tab can pull live water temp from the nearest gauge with that parameter. Water-temp percentile rounds out the field-journal feel.
**Dashboard integration idea:** Fishing tab → "Etowah water temp today." Endpoint: `https://waterservices.usgs.gov/nwis/iv/?format=json&sites=02389150&parameterCd=00010&siteStatus=all` (verify temp at this site; if not, find nearest gauge with 00010). **CORS enabled.**
**Depth tier:** **Live data source** (CORS-enabled JSON).

### Tennessee Aquarium Conservation Institute (TNACI) — Freshwater Information Network
**URL:** https://tnaqua.org/conservation/ and https://tnacifin.com/
**What it is:** Chattanooga-based research institute (founded 1996) focused on Southeast freshwater conservation — propagation/reintroduction of imperiled fish, including Etowah-system endemics like Etowah Darter and Cherokee Darter, plus Southern Appalachian Brook Trout.
**Why it's relevant here:** **The Etowah and Cherokee Darters are *only* found in the Etowah system that drains the property — federally listed and a marquee biodiversity story** for the Wildlife card. TNACI does the propagation work.
**Dashboard integration idea:** Wildlife card → "Endemic fish of the Etowah" subtitle linking to the Cherokee Darter species profile (e.g., https://tnacifin.com/fish/etowah-darter/). Surface fact about endemic richness.
**Depth tier:** Card subtitle + deep-dive link.

### Conasauga River Alliance
**URL:** https://www.murraycountyga.org/362/Conasauga-River-Alliance
**What it is:** 36-member federal/state/nonprofit/utility/aquarium coalition coordinating restoration across the 500,000-acre Conasauga watershed (~90 fish species, 10 federally listed).
**Why it's relevant here:** Sister Coosa-basin watershed one ridge west; useful regional context, not the property's direct watershed.
**Dashboard integration idea:** Optional regional context deep-dive in a "Coosa basin" cluster.
**Depth tier:** Deep-dive link.

### Southeastern Fishes Council (SFC)
**URL:** https://sfc8.wildapricot.org/
**What it is:** Nonprofit scientific society dedicated to freshwater and coastal fishes of the southeastern US; publishes Southeastern Fishes Council Proceedings.
**Why it's relevant here:** Primary scholarly venue for Etowah/Coosa endemic-fish research.
**Dashboard integration idea:** Optional deep-dive in a Wildlife/research footer cluster.
**Depth tier:** Deep-dive link.

### North American Native Fishes Association (NANFA)
**URL:** https://www.nanfa.org/
**What it is:** 1972 nonprofit bringing together amateur and professional ichthyologists; publishes American Currents quarterly; funds native-fish conservation grants.
**Why it's relevant here:** Hobbyist-friendly entry point to the same darter/minnow biodiversity story TNACI works on professionally; good for the field-journal personal-naturalist tone.
**Dashboard integration idea:** Wildlife card deep-dive: "Hobbyist native-fish community."
**Depth tier:** Deep-dive link.

### USGS BioData — Aquatic Bioassessment
**URL:** https://aquatic.biodata.usgs.gov/clearCriteria.action
**What it is:** USGS public archive of fish, macroinvertebrate, algae community samples plus stream habitat surveys (>21,000 samples at >3,000 sites since 1993).
**Why it's relevant here:** Source for actual fish-community survey data in the Etowah basin — "what species have actually been caught here" beyond stocking lists. **Caveat:** retrieval site has had recurring availability issues — verify before depending on it.
**Dashboard integration idea:** Optional Wildlife/Fishing deep-dive: "Historical fish surveys near you." Static link only.
**Depth tier:** Deep-dive link (verify availability).

### USFWS Partnership for the Upper Coosa
**URL:** https://www.fws.gov/project/partnership-upper-coosa
**What it is:** USFWS coordinating partnership for the Upper Coosa basin's federally listed aquatic species (fish, mussels, snails, crayfish), connecting NRCS, TNC, CRBI, and state agencies.
**Why it's relevant here:** Federal-side counterpart to state and nonprofit Coosa-basin work; useful for ESA-listed species framing.
**Dashboard integration idea:** Watershed/Wildlife deep-dive in the Coosa basin cluster.
**Depth tier:** Deep-dive link.

### Georgia Rivers (formerly Georgia River Network)
**URL:** https://garivers.org/coosa-river/ ; main site https://garivers.org/
**What it is:** Statewide river-advocacy nonprofit hosting the directory of local river groups (UERA, CRBI), Paddle Georgia events, basin-level summaries.
**Why it's relevant here:** Single jumping-off point for Georgia watershed groups; their Coosa River page is a clean basin summary.
**Dashboard integration idea:** Watershed card: "Find your local river group" deep-dive.
**Depth tier:** Deep-dive link.

---

## Category 6: Climate, dark sky, homesteading-adjacent

### Climate adaptation & long-term data

### NOAA NCEI Climate Data Online (CDO)
**URL:** https://www.ncei.noaa.gov/cdo-web/
**What it is:** Federal archive of historical weather/climate data with free programmatic access to daily summaries, hourly observations, and 1991-2020 U.S. Climate Normals.
**Why it's relevant here:** Authoritative long-term context for the Ambient Weather station's live readings — what's a "normal" May at this elevation, and how is the current month tracking?
**Dashboard integration idea:** Weather card subtitle: "May normal high 73°F, low 51°F (1991-2020)." Pull at month boundaries from `https://www.ncei.noaa.gov/access/services/data/v1`. Token required (free); CORS not officially supported — proxy server-side.
**Depth tier:** **Live data source** (cached monthly).

### NOAA NWS API (api.weather.gov)
**URL:** https://api.weather.gov ; docs at https://www.weather.gov/documentation/services-web-api
**What it is:** Free, no-key, CORS-enabled JSON forecast API. Gridpoint endpoint exposes `skyCover` as a percentage time series.
**Why it's relevant here:** Bortle 3 site; sky cover forecast is the single most useful astronomy variable. Open-Meteo gives a model blend; NWS gives the official forecaster's grid.
**Dashboard integration idea:** Weather card celestial subsection — render a 24-hour sky-cover sparkline. Flow: `GET /points/34.5496,-84.3674` → follow `properties.forecastGridData` → read `properties.skyCover.values[]`. CORS works in-browser.
**Depth tier:** **Live data source** (CORS-enabled, no key).

### PRISM Climate Group (Oregon State)
**URL:** https://prism.oregonstate.edu ; explorer at https://prism.oregonstate.edu/explorer/
**What it is:** 800m-resolution gridded climate dataset and 30-year normals (1991-2020) — much finer than NOAA's station-based normals, which matters in mountain terrain.
**Why it's relevant here:** At 2,959 ft on a Blue Ridge ridge, the closest NWS station (likely valley-floor Jasper or Blairsville) doesn't represent your microclimate. PRISM's 800m grid actually captures the elevation gradient.
**Dashboard integration idea:** One-time pull of PRISM 800m point values for 34.5496, -84.3674 (monthly Tmin/Tmax/precip normals); store as static reference data in Property card "Microclimate baseline."
**Depth tier:** Card subtitle (bake values in) + deep-dive link.

### Southeast Regional Climate Center (SERCC)
**URL:** https://sercc.com
**What it is:** UNC-Chapel Hill-housed NOAA-affiliated center serving GA + 7 other Southeast states. Provides NOWData, historical climate summaries, monthly perspectives, PRISM map products tailored to the Southeast.
**Why it's relevant here:** Best one-stop shop for "is this May unusually wet/dry/cool for north Georgia?" The SERCC Climate Perspectives tool (https://sercc.oasis.unc.edu/) compares the current period to climatology.
**Dashboard integration idea:** Deep-dive from Weather card footer: "How does this month compare? → SERCC Perspectives."
**Depth tier:** Deep-dive link.

### Southeast Climate Adaptation Science Center (USGS)
**URL:** https://secasc.ncsu.edu and https://www.usgs.gov/programs/climate-adaptation-science-centers/southeast-casc
**What it is:** USGS-funded, NC State-hosted research center producing downscaled climate projections and adaptation science for the Southeast, including the Southern Appalachians.
**Why it's relevant here:** Goes beyond historical normals into "what's coming" — projections for Southern Appalachian temperature, precip regime shifts, forest-ecosystem response. Directly relevant to the "support local wildlife and plants" goal under shifting conditions.
**Dashboard integration idea:** Property card → "Long view" subsection → static link to SECASC projections page.
**Depth tier:** Deep-dive link.

### NOAA Climate Resilience Toolkit Climate Explorer
**URL:** https://toolkit.climate.gov/tools/climate-explorer
**What it is:** Per-county graphs of past observed and projected future climate variables under two emissions futures.
**Why it's relevant here:** Pickens County has its own page — temperature/precipitation projections through end of century are pre-rendered. Most accessible "what does Pickens County look like in 2050?" view.
**Dashboard integration idea:** Property card → "Pickens County in 2050" link.
**Depth tier:** Deep-dive link.

### US Drought Monitor / Drought.gov
**URL:** https://droughtmonitor.unl.edu and https://www.drought.gov
**What it is:** Weekly authoritative drought classification (D0–D4) for every U.S. county, plus historical time series. Free APIs.
**Why it's relevant here:** Pickens County drought status directly affects watering decisions, fire risk, and what wildlife is pressuring water sources on the property.
**Dashboard integration idea:** Property card → small "Drought status" pill. USDM REST: `https://usdmdataservices.unl.edu/api/CountyStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=13227&...` (FIPS 13227 = Pickens County GA). JSON. CORS not advertised — proxy server-side. Updated Thursdays.
**Depth tier:** **Live data source** (server-side proxy).

### Dark sky & celestial

### DarkSky International
**URL:** https://darksky.org
**What it is:** Formerly the International Dark-Sky Association; the global authority on light pollution, lighting ordinances, the International Dark Sky Places certification program. Publishes Bortle scale references and model lighting codes.
**Why it's relevant here:** Property at Bortle 3 — exceptional for the Eastern US. Establishes vocabulary, certification context, lighting principles a homesteader could voluntarily adopt to preserve the asset.
**Dashboard integration idea:** Weather card celestial subsection: "Sky here: Bortle 3 (rural)" with deep-dive link to the Bortle scale page.
**Depth tier:** Surface fact + deep-dive link.

### Stephen C. Foster State Park (Georgia's only IDA Dark Sky Park)
**URL:** https://darksky.org/places/stephen-c-foster-state-park-dark-sky-park/ and https://gastateparks.org/StephenCFoster/Astronomy
**What it is:** Gold-tier International Dark Sky Park in the Okefenokee Swamp — Georgia's only IDA-certified site, and the only Gold-tier site in the Southeast.
**Why it's relevant here:** Useful Bortle reference point ("Stephen C. Foster is Bortle 2; here at Church Mountain Road we're Bortle 3"). A calibrated "darker than here" destination.
**Dashboard integration idea:** Property card microclimate notes → sky-quality reference: "Bortle 3; for Bortle 1–2, Stephen C. Foster SP is GA's only IDA-certified site."
**Depth tier:** Surface fact.

### Atlanta Astronomy Club (and Deerlick Astronomy Village)
**URL:** https://atlantaastronomy.org and https://deerlickgroup.com
**What it is:** AAC is the largest amateur astronomy club in the Southeast (founded 1947). Runs the annual Peach State Star Gaze at Deerlick Astronomy Village (Sharon, GA — about 2.5 hours east of Jasper, Bortle 2–3).
**Why it's relevant here:** Nearest organized astronomy community for a Pickens County stargazer.
**Dashboard integration idea:** Property card "Community" link list.
**Depth tier:** Deep-dive link.

### NASA Scientific Visualization Studio — Moon Phase & Eclipse Pages
**URL:** Daily moon: https://svs.gsfc.nasa.gov/5612/ ; 2026 libration: https://svs.gsfc.nasa.gov/5587 ; March 3 2026 lunar eclipse: https://svs.gsfc.nasa.gov/5606
**What it is:** Daily-updated rendered Moon images (Dial-a-Moon) and authoritative eclipse visualizations from NASA Goddard. Hourly Moon imagery for any moment of the year.
**Why it's relevant here:** Highest-quality public-domain Moon imagery. **The March 3, 2026 total lunar eclipse is visible from Georgia** — featured-event candidate.
**Dashboard integration idea:** Weather card celestial → Moon phase tile uses the Dial-a-Moon image. URL pattern: `https://svs.gsfc.nasa.gov/vis/a000000/a005400/a005415/frames/730x730_1x1_30p/moon.NNNN.jpg` (NNNN = hour-of-year, 1–8760). Compute current hour-of-year, fetch directly. Public-domain, no key. CORS allowed for static assets.
**Depth tier:** **Live data source** (image URL by hour).

### International Meteor Organization (IMO) Meteor Shower Calendar
**URL:** https://www.imo.net/resources/calendar/ ; 2026 PDF: https://www.imo.net/files/meteor-shower/cal2026.pdf
**What it is:** Authoritative annual meteor shower calendar with ZHRs, peak dates/times, radiant positions, Moon-interference notes.
**Why it's relevant here:** Bortle 3 is genuinely good meteor-watching territory — you can actually see the showers. The 2026 calendar with Moon phase correlation is exactly what the celestial card should highlight.
**Dashboard integration idea:** Weather card → "Next meteor shower" tile. No API; manually transcribe ~10 major showers from the 2026 PDF into static JSON (date, peak ZHR, parent body, Moon-interference flag). Refresh annually.
**Depth tier:** Card subtitle (static annual data).

### American Meteor Society
**URL:** https://www.amsmeteors.org/meteor-showers/meteor-shower-calendar/
**What it is:** US-focused meteor shower listing with date ranges and observing tips. Slightly more user-friendly than IMO.
**Why it's relevant here:** Cross-reference for IMO data; sometimes phrased better for journal-tone copy.
**Dashboard integration idea:** Source-of-truth backup; not a separate integration.
**Depth tier:** Deep-dive link.

### Stellarium Web
**URL:** https://stellarium-web.org (web app); https://stellarium.org (desktop, GPL)
**What it is:** Free open-source planetarium. Web version runs in any browser; desktop is far more capable.
**Why it's relevant here:** When a meteor shower or planetary conjunction shows up on the dashboard, the user wants to know "where do I look?" Stellarium answers for any lat/lon and time.
**Dashboard integration idea:** Celestial events → "Show in Stellarium" deep-link button. URL accepts coordinates and time params.
**Depth tier:** Deep-dive link.

### Open-Meteo cloud cover (already integrated)
**URL:** https://open-meteo.com
**What it is:** Already in your stack for forecast data. Exposes `cloud_cover`, `cloud_cover_low/mid/high`, `visibility` hourly variables — building blocks of an astronomical "clear sky" rating.
**Why it's relevant here:** No key, free, CORS-enabled. Pair with NWS skyCover for redundancy/cross-check.
**Dashboard integration idea:** Compute a simple "stargazing tonight" score from `cloud_cover` (low especially), `relative_humidity_2m`, Moon altitude+phase. Display as 5-bar chip on celestial section.
**Depth tier:** **Live data source** (already integrated; expand the variables requested).

### Time and Date AS — sun/moon reference
**URL:** https://www.timeanddate.com
**What it is:** Comprehensive sun/moon calculation reference. The free public web pages are excellent; the API costs $99+ with a 3-month trial only.
**Why it's relevant here:** Best free human-readable cross-check. Skip the API; reference link only.
**Dashboard integration idea:** Footer reference link. Compute sun/moon times locally (NOAA solar calculator algorithm or any astronomy library). The API is **not** worth $99 for this use case.
**Depth tier:** Deep-dive link. (API explicitly **not** recommended.)

### Air quality & burn

### AirNow API
**URL:** https://docs.airnowapi.org / signup at https://www.airnowapi.org
**What it is:** EPA's official real-time air quality API. Returns NowCast AQI by lat/lon or zip with categories and pollutant breakdowns including PM2.5 (wildfire smoke).
**Why it's relevant here:** Southern Appalachians get smoke from prescribed burns and from western US wildfires that drift east. AirNow tells you when it's a "stay inside" day vs. fine.
**Dashboard integration idea:** Weather card → AQI chip. Endpoint: `https://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=34.5496&longitude=-84.3674&distance=25&API_KEY=...`. Free key required; CORS not supported — proxy server-side.
**Depth tier:** **Live data source** (server-side proxy).

### Georgia Forestry Commission — Burn Permits & Interactive Map
**URL:** https://gatrees.org/burn-permits-and-notifications/ ; permit portal: https://georgiafc.firesponse.com/burn-permit/
**What it is:** Official Georgia burn permit system and interactive map of active wildfires and burn restrictions by county.
**Why it's relevant here:** **Pickens County has a state summer open burning ban May 1 – Sep 30** (Georgia EPD rule). Outside that window, permit required for most burns.
**Dashboard integration idea:** Property card → seasonally-conditional banner: "Summer burn ban active (May 1 – Sep 30)" during those months; outside that window, "Burn permit required — gatrees.org." Hardcode the seasonal logic.
**Depth tier:** Surface fact (date-conditional) + deep-dive link.

### Southern Fire Exchange
**URL:** https://southernfireexchange.org
**What it is:** Joint Fire Science Program-funded knowledge exchange for the Southeast. Publishes Fire Lines newsletter and fact sheets on prescribed fire, smoke management, growing-season burns. The 2026 "Be Smoke Savvy: Georgia Prescribed Fire Smoke Management Pocket Guide" is GA-specific.
**Why it's relevant here:** If the owner ever considers prescribed fire (a real management option in Southern Appalachian forests for wildlife and oak regeneration), SFE is the science source.
**Dashboard integration idea:** Property card → "Land management library" deep-dive.
**Depth tier:** Deep-dive link.

### Sustainable homesteading

### ATTRA Sustainable Agriculture (NCAT) — Appalachian publications
**URL:** https://attra.ncat.org ; regional landing: https://attra.ncat.org/about/regions/
**What it is:** NCAT's free sustainable agriculture publication library — 300+ topic guides, several specifically titled "Central and Southern Appalachian Region" (Climate-Smart Farming, Tree and Shrub Establishment, Alley Cropping, Upland Wildlife Habitat Management).
**Why it's relevant here:** Highest-signal, lowest-fluff source on this list for practical Southern Appalachian land management — written for working ground at this elevation and ecosystem. Free PDFs.
**Dashboard integration idea:** Property card → "Field references" link list. Highlight Climate-Smart Farming in C&S Appalachia and the Upland Wildlife Habitat Management guide.
**Depth tier:** Deep-dive link (high-value).

### Southern SARE
**URL:** https://southern.sare.org ; Georgia state page: https://southern.sare.org/sare-in-your-state/georgia/
**What it is:** USDA-NIFA-funded grants and outreach for Southern states. GA program co-administered by UGA and Fort Valley State. Producer Grants up to $15K — homesteaders sometimes qualify.
**Why it's relevant here:** Funding pathway if the property's wildlife/native-plant goals scale to a research-worthy project. Free online learning library (cover crops, agroforestry, pollinators).
**Dashboard integration idea:** Property card → "Funding & learning" deep-dive.
**Depth tier:** Deep-dive link.

### Appalachian Sustainable Development (ASD)
**URL:** https://asdevelop.org ; Agroforestry: https://asdevelop.org/programs-resources/agroforestry/
**What it is:** Central Appalachian nonprofit running an Agroforestry program focused on non-timber forest products (pawpaw, elderberry) and the Appalachian Harvest Herb Hub for wild-harvested medicinals.
**Why it's relevant here:** Shade-grown, native-forest agroforestry is exactly the model for a wooded mountain property aiming to "support local wildlife and plants, especially indigenous." Pawpaw, elderberry, ramps, ginseng all native to your forest type.
**Dashboard integration idea:** Property card → "Forest farming" subsection link.
**Depth tier:** Deep-dive link.

### Appalachian Beginning Forest Farmer Coalition
**URL:** https://www.appalachianforestfarmers.org and https://www.appalachianforestfarmers.org/ntfps
**What it is:** USDA-funded coalition focused on cultivating native non-timber forest products (ginseng, ramps, goldenseal, black cohosh) under existing forest canopy rather than clearing land.
**Why it's relevant here:** **Single most aligned organization with the property's stated values.** Bortle 3 + 2,959 ft + Blue Ridge mature forest = textbook habitat for shade-grown native NTFPs. They run trainings and a mentorship network.
**Dashboard integration idea:** Property card → featured "indigenous plant cultivation" link. Strong tie-in with Cherokee plant heritage.
**Depth tier:** Deep-dive link (high-value).

### Carolina Farm Stewardship Association
**URL:** https://carolinafarmstewards.org
**What it is:** NC/SC-focused organic ag nonprofit since 1979. Publishes the Organic Transition and Production Handbook (free) and offers technical assistance.
**Why it's relevant here:** Closest regional analog organization to GA. North Georgia mountains share more growing-condition DNA with western NC than south Georgia.
**Dashboard integration idea:** Reference link in homestead resources.
**Depth tier:** Deep-dive link.

### Appalachian Beekeepers Association of Georgia (Pickens-area chapter)
**URL:** http://www.pickensbeekeepers.com
**What it is:** Local beekeeping association serving Pickens and surrounding north Georgia counties; monthly meetings, on-site field training, mentorship.
**Why it's relevant here:** **A Pickens County resource — the most directly local org on this entire list.** Bees integral to "supporting local plants" because pollinator health drives native plant reproduction.
**Dashboard integration idea:** Property card → "Pollinator notes" subsection → direct link.
**Depth tier:** Deep-dive link.

### UGA Bee Program
**URL:** https://bees.caes.uga.edu
**What it is:** UGA's extension bee program — statewide association directory, beekeeping research, free publications.
**Why it's relevant here:** State-level technical backstop. Useful for variety selection (Italian vs. Russian for north GA winters), Varroa management timing tied to local nectar flows.
**Depth tier:** Deep-dive link.

### Native foodways / indigenous land knowledge

### Eastern Band of Cherokee Indians — Natural Resources & Center for Cherokee Plants
**URL:** Tribal: https://www.ebci.gov ; Natural Resources: https://ebci.com/services/departments/department-of-agricultural-natural-resources/natural-resources/ ; Tribal Extension: https://tribalextension.org/project/eastern-band-of-cherokee/
**What it is:** EBCI is the federally-recognized Cherokee tribe whose ancestral homeland *is* the Southern Appalachians (including Pickens County). The Center for Cherokee Plants preserves and propagates culturally significant seeds. The Tribal Extension program has 25+ years of mountain-agriculture knowledge.
**Why it's relevant here:** **Pickens County was Cherokee Nation territory from 1793–1838 (Trail of Tears removal).** The plants the Cherokee cultivated and tended for 6,000+ years — white oak, ramps (wasdi), sochan, ginseng, river cane — are still the native plants of this property. The single most authentic frame for "indigenous plants" on this land.
**Dashboard integration idea:** Property card → dedicated "On Cherokee land" subsection (field-journal tone). Static acknowledgment of the property's location in former Cherokee territory + link to EBCI Natural Resources for ongoing stewardship work.
**Depth tier:** Surface fact + deep-dive link.

### USDA Forest Service × EBCI — Culturally Significant Plants Research
**URL:** Research summary: https://research.fs.usda.gov/treesearch/64968 ; FS article: https://www.fs.usda.gov/inside-fs/delivering-mission/deliver/culturally-important-trees-eastern-cherokee
**What it is:** Active partnership managing forests in the Pisgah, Nantahala, Cherokee NF, and Great Smoky Mountains NP for ginseng, white oak, sochan, and ramps (wasdi) — led by Cherokee knowledge.
**Why it's relevant here:** Pickens County sits at the southern end of this same forest ecosystem. The same plant-management principles apply on Church Mountain Road. A real-world model of indigenous-led land stewardship.
**Dashboard integration idea:** Property card → "Stewardship reading" link. Particularly the open-access Ecology & Society paper on wasdi/ramps research.
**Depth tier:** Deep-dive link (high-value).

### Pickens County, GA Cherokee history references
**URL:** New Georgia Encyclopedia — Cherokee Removal: https://www.georgiaencyclopedia.org/articles/history-archaeology/cherokee-removal/ ; Pickens Historical Society: https://pickenshistoricalsociety.org/our-history/
**What it is:** Authoritative historical context for the property's location: Cherokee Nation 1793–1838, with settlements along Talking Rock Creek, Talona Creek, Long Swamp Creek (all near Jasper). Removal forts were built in this area in 1838.
**Why it's relevant here:** Specific local heritage rather than generic Cherokee context. Talking Rock is ~6 miles from the property; this was densely-settled Cherokee land.
**Dashboard integration idea:** Property card → "On Cherokee land" subsection → short field-journal-tone paragraph with reference link.
**Depth tier:** Surface fact + deep-dive link.

### USGS Indigenous Knowledge / Tribal Climate Resources
**URL:** https://www.usgs.gov/programs/climate-adaptation-science-centers/science/incorporating-indigenous-knowledges-federal-1 ; NPS TEK: https://www.nps.gov/subjects/tek/index.htm
**What it is:** Federal-side guidance and case-study library for engaging with Indigenous Knowledges in land management, per 2022 White House guidance.
**Why it's relevant here:** Honest framing for a non-Cherokee owner: how to learn from and credit Indigenous Knowledges respectfully rather than appropriating. Case-study library includes Southern Appalachian examples.
**Dashboard integration idea:** Property card → footer reference. Quiet placement; not a featured tile.
**Depth tier:** Deep-dive link.

---

## Resources intentionally omitted

A few well-known names that came up but aren't a fit for this property:

- **Longleaf Alliance** — confirmed not relevant. Longleaf pine's range is the Coastal Plain; at 2,959 ft in the Blue Ridge, the property is in Appalachian oak-hickory / cove hardwood forest types.
- **Cherokee Heritage Center (Tahlequah, OK)** — currently closed during planning period. EBCI sites above are more useful and more geographically appropriate (eastern homeland vs. post-Removal western nation).
- **Permaculture Research Institute** — international, mostly Australia/desert focus. Low signal for North Georgia.
- **Rodale Institute Southeast** — content is field-crop-organic focused, not homestead/wooded-property. Marginal fit.
- **Time and Date API** — $99+ paywall not justified; sun/moon math is computable locally.
- **Permies.com** — large active forum but mixed signal-to-noise. Useful for searching specific questions, not as primary reference.
- **USGS BioData** — verified but has had recurring availability issues; don't depend on uptime.
- **MountainTrue** — Pickens not yet in their GA service area (Towns and Union counties only); kept as optional regional context.
