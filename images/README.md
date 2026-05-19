# Images

Photographic content for the species and items shown in the dashboard. The viewer reads these as ordinary relative paths (`<img src="images/...">`) — no build step.

## Conventions

- One subdirectory per category: `birds/`, `amphibians/`, `fishing/`, `plants/`, `vehicles/`.
- Filenames are the corresponding `id` field from the JSON record, with `.jpg` extension. Example: `images/birds/ruby-throated-hummingbird.jpg`.
- Photos are width-constrained to ~800px (small enough for fast load, large enough to look sharp at the ~500px hero display in the expanded body on retina screens). The same file is used for both the 44×44 thumbnail in the always-visible header and the hero photo at the top of the expanded body.
- Each subdirectory contains an `_attribution.json` file capturing the source/author/license for any image not photographed locally.

## Sourcing

For species where local photographs are not yet available, photos are pulled from **Wikimedia Commons** under permissive licenses (CC BY, CC BY-SA, public domain). A unified pipeline handles all categories:

```bash
python3 tools/fetch-photos.py --category birds
python3 tools/fetch-photos.py --category amphibians
python3 tools/fetch-photos.py --category fishing
python3 tools/fetch-photos.py --category plants
python3 tools/wire-photos.py --category {birds|amphibians|fishing|plants}
```

`fetch-photos.py` calls the Wikipedia REST summary API for each species, follows the lead image to its Commons file, downloads an 800px-wide JPEG, and writes attribution metadata to `_attribution.json`. `wire-photos.py` merges that into the source JSON file and re-inlines the `{CATEGORY}_DATA` constant in `viewer.html` (the runtime reads from the inlined const, not a fetch — keep it in sync).

For **vehicles and equipment** (and eventually your own garden photos), drop locally-shot JPEGs at `images/{category}/{id}.jpg` and skip the attribution step. The viewer suppresses the credit line when no `attribution` object is present on the item.

### Plants — genus-level reference caveat

Several plants in `plants.json` are specific cultivars (Berry Box® Pyracomeles, Yuki Cherry Blossom® Deutzia, named Clematis hybrids, mixed Hosta cultivars, pond Iris). Wikimedia photos for those exact cultivars usually don't exist, so the fetcher falls back to a genus-level photo:

- **Azalea** → Rhododendron flower (azaleas are a Rhododendron subgenus)
- **Pyracomeles (Berry Box)** → Pyracantha berries (×Pyracomeles is a Pyracantha × Osteomeles hybrid; no dedicated photos exist)
- **Yuki Cherry Blossom Deutzia** → generic Deutzia (cultivar-specific photos rare on Commons)
- **Clematis** → 'Nelly Moser' (one of the candidate cultivars)
- **Hosta** → generic Hosta cultivar
- **Pond Iris** → Iris versicolor (Northern Blue Flag)

These are placeholders that show genus-level character. They should eventually be replaced with photos of the actual specimens in the garden — which is what `plants.draft.json:qualityPhotosForFutureIntegration` is tracking.

## Birds

| Species | Author | License | Source |
|---|---|---|---|
| Barred Owl | Mdf | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Strix-varia-005.jpg) |
| Belted Kingfisher | JeffreyGammon | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:BeltedKingfisherJG_Male.jpg) |
| Broad-winged Hawk | Julie Waters | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Julie_Waters_broad_winged_hawk.JPG) |
| Carolina Chickadee | Dan Pancamo | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Carolina_Chickadee1_by_Dan_Pancamo.jpg) |
| Dark-eyed Junco | Cephas | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Junco_hyemalis_hyemalis_CT1_(cropped).jpg) |
| Eastern Towhee | Paul Danese | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:20241004_eastern_towhee_pleasant_valley_PD207764.jpg) |
| Great Blue Heron | DallasPenner | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:GreatBlueHeronInARiver.jpg) |
| Indigo Bunting | Dan Pancamo | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Indigo_Bunting_by_Dan_Pancamo_4.jpg) |
| Ovenbird | Rhododendrites | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Ovenbird_(90497).jpg) |
| Pileated Woodpecker | Joshlaymon | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:PileatedWoodpeckerFeedingonTree,_crop.jpg) |
| Rose-breasted Grosbeak | John Harrison | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:RosebreastedGrosbeak08.jpg) |
| Ruby-throated Hummingbird | jeffreyw | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Archilochus_colubris_-flying_-male-8.jpg) |
| Scarlet Tanager | Rhododendrites | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Scarlet_tanager_in_GWC_(50867).jpg) |
| White-throated Sparrow | Cephas | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Zonotrichia_albicollis_CT1.jpg) |
| Wild Turkey | Paul Danese | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:20260428_tom_wild_turkey_matthaei_botanical_gardens_PD08952.jpg) |
| Wood Thrush | Charles J. Sharp | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Wood_thrush_(Hylocichla_mustelina)_Peten.jpg) |

## Amphibians

| Species | Author | License | Source |
|---|---|---|---|
| American Bullfrog | Carl D. Howe | CC BY-SA 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:North-American-bullfrog1.jpg) |
| American Toad | Cephas | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bufo_americanus_PJC1.jpg) |
| Fowler's Toad | Rstanton13 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Anaxyrus_fowleri_Stanton_2_(cropped).jpg) |
| Gray Treefrog | Randidawn | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Gray_tree_frog_in_arboreal_forest_habitat,_MA.jpg) |
| Green Frog | Contrabaroness | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Male_Green_Frog_-_Hunterdon_County,_NJ.jpg) |
| Marbled Salamander | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Marbled_salamander_(14367751333).jpg) |
| Red-backed Salamander | Alex Karasoulos | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Adult_Female_Plethodon_cinereus.jpg) |
| Slimy Salamander | Caudatejake | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Plethodon_glutonosus.jpg) |
| Spotted Salamander | D. Gordon E. Robertson | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Spotted_Salamander,_Cantley,_Quebec.jpg) |
| Spring Peeper | USGS | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:H_crucifer_USGS.jpg) |
| Two-lined Salamander | Brian Gratwicke | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Northern_Two-lined_Salamander_Eurycea_bislineata.jpg) |
| Upland Chorus Frog | MH Herpetology | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Upland_chorus_frog_(Pseudacris_feriarum).jpg) |

## Fishing (Lake Sequoyah)

| Species | Author | License | Source |
|---|---|---|---|
| Bluegill | Paleo1954 | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bluegill_(cropped).jpg) |
| Crappie | Robert W. Hines (USFWS) | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Black_crappie_and_white_crappie_fish.jpg) |
| Largemouth Bass | USFWS Mountain Prairie | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Largemouth_Bass_(Micropterus_salmoides)_June_2023_(cropped).jpg) |

## Plants

Genus-level references where the actual cultivar is trademarked or hybrid (see caveat above).

| Plant | Author | License | Source |
|---|---|---|---|
| Azalea (Rhododendron genus) | Prayushk | CC BY 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Rhododendron_flower_(Ghorepani,_Nepal).jpg) |
| Boxwood | MPF | CC BY 2.5 | [Commons](https://commons.wikimedia.org/wiki/File:Buxus_sempervirens.jpg) |
| Butterfly Weed (Asclepias tuberosa) | Derek Ramsey (Ram-Man) | GFDL 1.2 | [Commons](https://commons.wikimedia.org/wiki/File:Butterfly_Weed_Asclepias_tuberosa_Umbel.jpg) |
| Clematis (Nelly Moser proxy) | Jolly Janner | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Clematis_%27Nelly_Moser%27.JPG) |
| Elpis Clematis (Clematis macropetala proxy) | Wilrooij | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Clematis_macropetala_02.jpg) |
| Yuki Cherry Blossom Deutzia (Deutzia gracilis proxy) | — | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Deutzia_gracilis.jpg) |
| Dogwood (Cornus florida) | Eric Hunt | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Cornus_florida_Arkansas.jpg) |
| Holly (Ilex aquifolium) | Jürgen Howaldt | CC BY-SA 2.0 de | [Commons](https://commons.wikimedia.org/wiki/File:Ilex-aquifolium_(Europaeische_Stechpalme-1).jpg) |
| Hosta (mixed cultivars proxy) | — | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hosta_Bressingham_Blue.JPG) |
| Hydrangea | Jacob Malcom | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hydrangea_arborescens_139866012.jpg) |
| DreamCloud Hydrangea (H. macrophylla white proxy) | Sasipriya Narayanaswamy | CC BY-SA 4.0 | [Commons](https://commons.wikimedia.org/wiki/File:Hydrangea_macrophylla_white_flower.jpg) |
| Pond Iris (Iris versicolor) | D. Gordon E. Robertson | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Blue_Flag,_Ottawa.jpg) |
| Japanese Maple | Kurt Stüber | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Acer_palmatum0.jpg) |
| Mountain Laurel | Arx Fortis | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Kalmia_Latifolia.jpg) |
| Pyracomeles (Berry Box → Pyracantha proxy) | Laitr Keiows | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Red_pommes_of_Firethorn_(Pyracantha).jpg) |
| White Pine | US FWS | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Pinus_strobus_trees.jpg) |
| Summer Cascade Wisteria (W. macrostachya proxy) | Jaknouse | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Wisterria_macrostachya_flowers1.jpg) |

## Replacing a photo

If a particular photo isn't quite right, two ways to override:

1. **Use a different Commons file**: edit `tools/fetch-photos.py`, add the species id to that category's `file_overrides` dict (with the desired `File:Foo.jpg` title) or `page_overrides` dict (with a different Wikipedia article title). Then `python3 tools/fetch-photos.py --category {cat} {id} --force` followed by `python3 tools/wire-photos.py --category {cat}`.
2. **Use a local photo**: drop a JPEG at `images/{category}/{id}.jpg` and remove that item's entry from `_attribution.json` (or update its fields manually). Then run `wire-photos.py` again to re-inline. Removing the `attribution` object from the source JSON will suppress the credit line — appropriate for locally-shot photos.
