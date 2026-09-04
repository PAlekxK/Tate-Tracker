#!/usr/bin/env node
// guru-replay.mjs — Guru 5a dispatch fixtures: drives worker.js's dispatchTool on the committed digest, no network.
//   node tools/guru-replay.mjs
// Every lookup is COMPLETE (never a model-chosen top-k), deterministically sorted, counted when truncated, or
// {found:false, reason} in the record's own words; a standing caveat rides verbatim; the door stays shut without vault.
import { dispatchTool, CORE_TOOLS, LOOKUP_STRINGS, bm25Rank, libTokens } from "../worker/worker.js";
import { readFileSync } from "node:fs";
const digest = JSON.parse(readFileSync(new URL("../worker/digest.json", import.meta.url), "utf8"));
let ok = true;
const check = (name, cond, detail) => { ok &&= !!cond; console.log(`  ${cond ? "✅" : "🔴"} ${name}${cond || detail === undefined ? "" : "  → " + JSON.stringify(detail).slice(0, 200)}`); };
console.log("guru-replay — dispatch fixtures\n");
const ctx = { digest, vaultOpen: false };
check("the lookup tools in the declared order", CORE_TOOLS.map(t => t.name).join(",").startsWith("get_plant,list_plants,list_weeds,get_species,get_zone,service_history,circuit_for,rhythms,turf_regime,fishing_species"));
const firstPlant = digest.plants.plants[0];
const gp = await dispatchTool("get_plant", { name: firstPlant.name }, ctx);
check("get_plant by exact name → the full entry", gp.found && gp.plant.id === firstPlant.id);
check("get_plant unknown → {found:false, reason: LOOKUP_STRINGS.NOT_IN_RECORD}", (await dispatchTool("get_plant", { name: "zzz-not-a-plant" }, ctx)).reason === LOOKUP_STRINGS.NOT_IN_RECORD);
const lp = await dispatchTool("list_plants", {}, ctx);
check("list_plants is complete and counted", lp.found && lp.total === digest.plants.plants.length && lp.shown === lp.total);
check("list_plants sorted by name", JSON.stringify(lp.rows.map(r => r.name)) === JSON.stringify([...lp.rows.map(r => r.name)].sort((a, b) => a.localeCompare(b))));
const sh = await dispatchTool("service_history", { vehicle: "bronco" }, ctx);
check("service_history bronco → {total:28, shown:10} newest first", sh.found && sh.total === 28 && sh.shown === 10 && sh.rows[0].date >= sh.rows[1].date, { total: sh.total, shown: sh.shown });
const shb = await dispatchTool("service_history", { vehicle: "bronco", topic: "brake", limit: 50 }, ctx);
check("…topic 'brake' filters IN THE TOOL and counts", shb.found && shb.total === 3 && shb.shown === 3, { total: shb.total });
const gti = await dispatchTool("service_history", { vehicle: "gti", limit: 2 }, ctx);
check("a record with a standing caveat returns it VERBATIM", gti.found && typeof gti.caveat === "string" && gti.caveat.startsWith("Summarized from scanned paper records"));
check("determinism: two identical calls → identical JSON", JSON.stringify(await dispatchTool("service_history", { vehicle: "bronco" }, ctx)) === JSON.stringify(sh));
check("circuit_for WITHOUT the vault → the login string, no circuit", (await dispatchTool("circuit_for", { what: "water heater" }, ctx)).reason === LOOKUP_STRINGS.LOGIN_REQUIRED);
const cf = await dispatchTool("circuit_for", { what: "water heater" }, { digest, vaultOpen: true });
check("circuit_for WITH the vault → the circuit(s)", cf.found && cf.circuits.length >= 1 && typeof cf.circuits[0].n === "number");
const amb = await dispatchTool("get_species", { name: "e" }, ctx);
check("an ambiguous name → AMBIGUOUS with sorted candidates, never a guess", amb.found === false && amb.reason === LOOKUP_STRINGS.AMBIGUOUS && Array.isArray(amb.candidates));
check("get_zone by id", (await dispatchTool("get_zone", { name: digest.zones[0].id }, ctx)).found);
check("turf_regime with no zone → all regimes, counted", (await dispatchTool("turf_regime", {}, ctx)).total === digest.turf.regimes.length);
check("fishing_species complete", (await dispatchTool("fishing_species", {}, ctx)).total === digest.fishing.species.length);
const nope = await dispatchTool("nope", {}, ctx);
check("an unknown tool → found:false with an `error`, no `reason` (nothing to relay)", nope.found === false && nope.error && !nope.reason);

// ── 5b: THE FENCES RESOLVE AGAINST CANON ─────────────────────────────────────────────────────────────────────────
// The six client parsers are lifted VERBATIM from the built viewer (a scratch copy missing one → the extractor THROWS,
// so a 404-shaped viewer scores nothing), then driven on fences that name canon entities. A fence whose entity the
// names index cannot resolve is a harness FAIL — never a client-side silent miss.
import { existsSync } from "node:fs";
const FENCE_FNS = ["parseSuggestionFence", "parseFollowupFence", "parseRegisterFence", "parseLogFence", "parseAddFence", "parseRemoveFence"];
function extractFenceParsers(html) {
  const grab = (startIdx) => {   // brace-matched function body from `function name(`
    let i = html.indexOf("{", startIdx), depth = 0;
    for (let j = i; j < html.length; j++) { if (html[j] === "{") depth++; else if (html[j] === "}") { depth--; if (depth === 0) return html.slice(startIdx, j + 1); } }
    throw new Error("unbalanced braces");
  };
  const kinds = html.match(/const SUGGEST_FENCE_KINDS = new Set\(\[[\s\S]*?\]\);/);
  if (!kinds) throw new Error("viewer has no SUGGEST_FENCE_KINDS — not the app, or the fence contract moved");
  let src = kinds[0] + "\n";
  for (const fn of FENCE_FNS) {
    const at = html.indexOf(`function ${fn}(`);
    if (at < 0) throw new Error(`viewer has no ${fn} — a parser is missing; the harness scores nothing`);
    src += grab(at) + "\n";
  }
  return new Function(src + `return {${FENCE_FNS.join(",")}};`)();
}
const viewerPath = new URL("../viewer.html", import.meta.url);
const P = extractFenceParsers(readFileSync(viewerPath, "utf8"));
check("six fence parsers lifted from the built viewer", FENCE_FNS.every(f => typeof P[f] === "function"));
const names = digest.core.names;
const norm = (x) => String(x || "").toLowerCase().trim();
const resolves = (section, name) => (names[section] || []).some(r => norm(r.name) === norm(name) || norm(r.id) === norm(name) || norm(r.sci) === norm(name));
const KIND_SECTION = { plant: "plants", bird: "birds", mammal: "mammals", amphibian: "amphibians", snake: "snakes", lizard: "lizards", fish: "fish" };
const plant = names.plants[0], bird = names.birds[0], vehicle = names.vehicles[0];
const prose = "The laurels by the porch are near the end of their bloom.";
// row 1 — suggest-species names a tracked bird → resolves
const r1 = P.parseSuggestionFence(`${prose}\n<!--suggest-species ${JSON.stringify({ kind: "bird", commonName: bird.name, scientificName: bird.sci || "x" })}-->`);
check("suggest-species: parsed, prose stripped, and the bird RESOLVES in names.birds", r1.suggestion && r1.displayText === prose && resolves(KIND_SECTION[r1.suggestion.kind], r1.suggestion.commonName));
// row 2 — suggest-log (observation) names a tracked plant → resolves
const r2 = P.parseLogFence(`${prose}\n<!--suggest-log ${JSON.stringify({ noteType: "observation", target: { name: plant.name } })}-->`);
check("suggest-log observation: the plant RESOLVES in names.plants", r2.log && r2.text === prose && resolves("plants", r2.log.targetName));
// row 3 — suggest-log (vehicle-note) names a machine → resolves
const r3 = P.parseLogFence(`Plug gap is fine.\n<!--suggest-log ${JSON.stringify({ noteType: "vehicle-note", target: { name: vehicle.name } })}-->`);
check("suggest-log vehicle-note: the machine RESOLVES in names.vehicles", r3.log && resolves("vehicles", r3.log.targetName));
// row 4 — suggest-remove names a tracked plant → resolves
const r4 = P.parseRemoveFence(`${prose}\n<!--suggest-remove ${JSON.stringify({ kind: "plant", name: plant.name })}-->`);
check("suggest-remove: the plant RESOLVES", r4.remove && resolves("plants", r4.remove.name));
// row 5 — suggest-add is for a plant NOT yet kept: it must NOT resolve (a resolvable name is the wrong fence)
const r5 = P.parseAddFence(`${prose}\n<!--suggest-add ${JSON.stringify({ kind: "plant", commonName: "Zebulon's Quixote Lily", scientificName: "Lilium zebuloni" })}-->`);
check("suggest-add: parsed, and the new plant does NOT resolve (that is what makes it an add)", r5.add && !resolves("plants", r5.add.commonName));
const r5b = P.parseAddFence(`${prose}\n<!--suggest-add ${JSON.stringify({ kind: "plant", commonName: plant.name })}-->`);
check("suggest-add naming a plant we ALREADY keep → harness FAIL (the wrong fence), asserted as detected", r5b.add && resolves("plants", r5b.add.commonName));
// row 6 — followup + register carry no entity: parse-and-strip only, and they compose
const r6 = P.parseRegisterFence(P.parseFollowupFence(`Oil is 10W-40.\n<!--suggest-followup {"prompt":"How much does it take?"}-->\n<!--register:machine-->`).text);
check("suggest-followup + register:machine: both stripped, followup kept, machine=true", r6.machine && r6.text === "Oil is 10W-40.");
// the CONTROL: an unresolvable entity in a resolving fence is a FAIL the harness must be able to say
const rX = P.parseLogFence(`${prose}\n<!--suggest-log ${JSON.stringify({ noteType: "observation", target: { name: "Zebulon's Quixote Lily" } })}-->`);
check("CONTROL: a log fence naming a plant the index cannot resolve → the harness says FAIL (not a silent client miss)", rX.log && !resolves("plants", rX.log.targetName));
// the MUTATION: a viewer missing one parser → the extractor THROWS
let threw = false;
try { extractFenceParsers(readFileSync(viewerPath, "utf8").replace("function parseLogFence(", "function parseLogFenceX(")); } catch (e) { threw = /parseLogFence/.test(String(e.message)); }
check("MUTATION: a viewer missing parseLogFence → the extractor throws naming it", threw);
// ── 6a: the scorer is DETERMINISTIC on a fixture (the model may cite, never select) ──
const fxShards = { torque: [["a", 2], ["b", 1]], blade: [["a", 1]], oil: [["c", 3]] };
const fxStats = { N: 3, avgdl: 10, dl: { a: 10, b: 10, c: 10 }, k1: 1.2, b: 0.75 };
const q = libTokens("the blade torque, and the torque again");
check("libTokens: lowercase, ≥3 chars, stopwords out, DISTINCT", JSON.stringify(q) === JSON.stringify(["blade", "torque", "again"]));
const s1 = bm25Rank(["torque", "blade"], fxShards, fxStats, 5), s2 = bm25Rank(["torque", "blade"], fxShards, fxStats, 5);
check("bm25Rank: the doc with both terms ranks first; total counts every doc with any term", s1.top[0].id === "a" && s1.total === 2);
check("bm25Rank: identical calls → identical output", JSON.stringify(s1) === JSON.stringify(s2));
check("bm25Rank: a term with no postings → total 0 (the tool then returns NO_SOURCE)", bm25Rank(["zebra"], fxShards, fxStats, 5).total === 0);
check("ties break on id, not on insertion order", bm25Rank(["oil"], { oil: [["z", 1], ["m", 1]] }, { N: 2, avgdl: 10, dl: { z: 10, m: 10 } }, 5).top[0].id === "m");
check("eleven tools; search_library is last in the declared order", CORE_TOOLS.length === 11 && CORE_TOOLS[10].name === "search_library");
console.log(`\nfences 6/6 · dispatch ${CORE_TOOLS.length} · scorer 5 · control 1 · mutation 1`);
console.log(`\n${ok ? "✅ controls hold." : "🔴 a control failed."}`);
process.exit(ok ? 0 : 1);
