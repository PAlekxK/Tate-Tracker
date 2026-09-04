#!/usr/bin/env node
// guru-replay.mjs — Guru 5a dispatch fixtures: drives worker.js's dispatchTool on the committed digest, no network.
//   node tools/guru-replay.mjs
// Every lookup is COMPLETE (never a model-chosen top-k), deterministically sorted, counted when truncated, or
// {found:false, reason} in the record's own words; a standing caveat rides verbatim; the door stays shut without vault.
import { dispatchTool, CORE_TOOLS, LOOKUP_STRINGS } from "../worker/worker.js";
import { readFileSync } from "node:fs";
const digest = JSON.parse(readFileSync(new URL("../worker/digest.json", import.meta.url), "utf8"));
let ok = true;
const check = (name, cond, detail) => { ok &&= !!cond; console.log(`  ${cond ? "✅" : "🔴"} ${name}${cond || detail === undefined ? "" : "  → " + JSON.stringify(detail).slice(0, 200)}`); };
console.log("guru-replay — dispatch fixtures\n");
const ctx = { digest, vaultOpen: false };
check("ten tools in the declared order", CORE_TOOLS.map(t => t.name).join(",") === "get_plant,list_plants,list_weeds,get_species,get_zone,service_history,circuit_for,rhythms,turf_regime,fishing_species");
const firstPlant = digest.plants.plants[0];
const gp = dispatchTool("get_plant", { name: firstPlant.name }, ctx);
check("get_plant by exact name → the full entry", gp.found && gp.plant.id === firstPlant.id);
check("get_plant unknown → {found:false, reason:'not in the record'}", dispatchTool("get_plant", { name: "zzz-not-a-plant" }, ctx).reason === LOOKUP_STRINGS.NOT_IN_RECORD);
const lp = dispatchTool("list_plants", {}, ctx);
check("list_plants is complete and counted", lp.found && lp.total === digest.plants.plants.length && lp.shown === lp.total);
check("list_plants sorted by name", JSON.stringify(lp.rows.map(r => r.name)) === JSON.stringify([...lp.rows.map(r => r.name)].sort((a, b) => a.localeCompare(b))));
const sh = dispatchTool("service_history", { vehicle: "bronco" }, ctx);
check("service_history bronco → {total:28, shown:10} newest first", sh.found && sh.total === 28 && sh.shown === 10 && sh.rows[0].date >= sh.rows[1].date, { total: sh.total, shown: sh.shown });
const shb = dispatchTool("service_history", { vehicle: "bronco", topic: "brake", limit: 50 }, ctx);
check("…topic 'brake' filters IN THE TOOL and counts", shb.found && shb.total === 3 && shb.shown === 3, { total: shb.total });
const gti = dispatchTool("service_history", { vehicle: "gti", limit: 2 }, ctx);
check("a record with a standing caveat returns it VERBATIM", gti.found && typeof gti.caveat === "string" && gti.caveat.startsWith("Summarized from scanned paper records"));
check("determinism: two identical calls → identical JSON", JSON.stringify(dispatchTool("service_history", { vehicle: "bronco" }, ctx)) === JSON.stringify(sh));
check("circuit_for WITHOUT the vault → the login string, no circuit", dispatchTool("circuit_for", { what: "water heater" }, ctx).reason === LOOKUP_STRINGS.LOGIN_REQUIRED);
const cf = dispatchTool("circuit_for", { what: "water heater" }, { digest, vaultOpen: true });
check("circuit_for WITH the vault → the circuit(s)", cf.found && cf.circuits.length >= 1 && typeof cf.circuits[0].n === "number");
const amb = dispatchTool("get_species", { name: "e" }, ctx);
check("an ambiguous name → AMBIGUOUS with sorted candidates, never a guess", amb.found === false && amb.reason === LOOKUP_STRINGS.AMBIGUOUS && Array.isArray(amb.candidates));
check("get_zone by id", dispatchTool("get_zone", { name: digest.zones[0].id }, ctx).found);
check("turf_regime with no zone → all regimes, counted", dispatchTool("turf_regime", {}, ctx).total === digest.turf.regimes.length);
check("fishing_species complete", dispatchTool("fishing_species", {}, ctx).total === digest.fishing.species.length);
check("an unknown tool → found:false", dispatchTool("nope", {}, ctx).found === false);
console.log(`\n${ok ? "✅ controls hold." : "🔴 a control failed."}`);
process.exit(ok ? 0 : 1);
