// telemetry-walk.js — the BASELINE TELEMETRY WALK
// ============================================================================
// A leg of the mom-cycle, not a calendar item `[paul-stated 2026-08-08]`:
// "it's worth having a baseline telemetry test that we probably work into the
// cycle... not necessarily monthly. We don't know what the cycle is, but
// whatever the mom feedback cycle is." Cadence is deliberately unset — this
// runs once per lap, wherever the lap lands.
//
// WHAT IT ANSWERS, and what it does not
// -------------------------------------
// `check-telemetry.py` reads the RECORD: has this event ever fired? It cannot
// tell a broken call site from a path nobody has walked. This walks the paths,
// so a zero becomes attributable: WIRED-BUT-UNUSED, or genuinely BROKEN.
//
// It does NOT prove the POST or the Worker leg works — deliberately, see below.
// That leg is independently evidenced by 44 event names arriving in the record.
//
// ⭐ WHY IT CANNOT POLLUTE — and why that is structural, not a promise
// -------------------------------------------------------------------
// Run it against a LOCAL server (`python3 -m http.server 8765`). On localhost,
// `tateTracker.sync.v1` is unset, so `WorkerAPI.isConfigured()` is false and
// `MetricsCollector.flush()` returns before sending (viewer.html ~16699).
// `track()` still runs and still buffers — which is exactly the half we are
// testing. So the events are REAL and the network leg is INERT by construction.
//
// Verified on the 2026-08-08 run: `attempted_network: 0`, `worker_configured:
// false`. Nothing left the browser. The fetch/sendBeacon block below is
// belt-and-braces on top of that, not the thing being relied on.
//
// This is why the walk beats the alternatives Paul's constraint ruled out:
//   · `tateTracker.metricsExclude` makes track() a NO-OP — it would prove
//     nothing, since nothing is recorded.
//   · Walking the LIVE site would require the Worker token in a browser
//     profile and would overwrite a real deviceId. A synthetic test device
//     (`d-telemetrytest-harness-v1`, people.json) exists for that case, but it
//     is the FALLBACK for an end-to-end test, not the default.
//
// ⛔ PATHS THAT ARE NOT SAFE TO WALK — even here
// ----------------------------------------------
// Anything POSTing to /api/feedback writes into MOM'S ANSWER RECORD, which no
// metrics exclusion covers: a confirm-card answer, a free-text note, and the
// acknowledgment "Got it" (viewer.html:11147 posts an `ack-receipt`). Those are
// excluded by choice. The localhost inertness would in fact stop them too —
// they are excluded anyway, because defending Mom's record with a shim I wrote
// in the same session is a single point of failure, and this repo does not
// trust those.
//
// HOW TO RUN
// ----------
//   cd ~/Developer/Tate-Tracker && python3 -m http.server 8765
//   lsof -nP -iTCP:8765 -sTCP:LISTEN     # verify the PID, never a curl 200
//   open http://localhost:8765/viewer.html
//   paste this file into the console, then: await telemetryWalk()
//
// Record the result in MOM-CYCLE-LOG.md for the lap.

window.telemetryWalk = async function telemetryWalk() {
  const TEL = [];
  const BLOCKED = [];

  // Belt-and-braces: neutralise both network legs regardless of config.
  const origFetch = window.fetch;
  window.fetch = function (u) {
    const url = String((u && u.url) || u || "");
    if (url.includes("/api/")) { BLOCKED.push(url); return Promise.resolve(new Response("{}", { status: 200 })); }
    return origFetch.apply(this, arguments);
  };
  const origBeacon = navigator.sendBeacon && navigator.sendBeacon.bind(navigator);
  if (origBeacon) navigator.sendBeacon = function (u) { BLOCKED.push("beacon:" + u); return true; };

  // mpTrack() and both inner track() shims resolve MetricsCollector.track by
  // PROPERTY LOOKUP at call time (viewer.html 10635 / 11935 / 19515), so
  // wrapping the property catches all three. Checked, not assumed — a shim that
  // had captured the reference at definition time would silently bypass this.
  const origTrack = MetricsCollector.track;
  MetricsCollector.track = function (type, fields) {
    TEL.push({ type, fields: fields || {} });
    return origTrack.apply(this, arguments);
  };

  // The walk list. Each entry: [label, resolver]. A resolver returning null is
  // reported as ELEMENT ABSENT rather than silently passing — an absent control
  // is a finding (it is how momack_unfolded was caught).
  const PATHS = [
    ["jump strip → Vehicles",            () => document.querySelector('.jump-strip a[data-jump="card-vehicles"]')],
    ["Household authorship door",        () => document.querySelector('#household-add-link')],
    ["Mama's Perspective envelope",      () => document.querySelector('.mp-head-toggle')],
    ["Launcher dismiss (Another day)",   () => [...document.querySelectorAll('.card-later-link')]
                                                 .find(e => e.closest('.mom-queue-launcher, #mom-queue-launcher'))],
    ["Composer: Save while empty",       () => {
        const b = [...document.querySelectorAll('button')].find(x => /Save & consult the Almanac/i.test(x.textContent || ''));
        const ta = b && b.closest('*').querySelector('textarea');
        if (ta) ta.value = "";     // the empty-submit branch is the thing under test
        return b;
      }],
  ];

  // ⭐ RESET THE DAY-SCOPED DISMISSALS FIRST (2026-08-08, found by the harness
  // failing its own second run). The launcher dismiss writes today's date to
  // localStorage and the launcher then stops rendering for the rest of the day —
  // so walk #2 reported ELEMENT ABSENT and would have read as a regression.
  // A baseline that only works the first time each day is not a baseline. This
  // clears only day-scoped UI state; it never touches feedback, drafts or canon.
  // Key names read off viewer.html:10559 and 10702 — NOT guessed. A reset that
  // clears a misspelled key silently does nothing and the walk looks fine.
  const DAY_KEYS = [
    "tateTracker.zoneJourney.launcherDismissed.v1",  // viewer.html:10702
    "tateTracker.momQueue.snoozed.v1",               // viewer.html:10559
  ];
  for (const k of DAY_KEYS) { try { localStorage.removeItem(k); } catch (e) {} }
  // Re-render so the cleared state is reflected before we look for controls.
  try { if (typeof MomQueue !== "undefined" && MomQueue.render) MomQueue.render(); } catch (e) {}

  const results = [];
  for (const [label, resolve] of PATHS) {
    const el = resolve();
    if (!el) { results.push({ path: label, fired: null, status: "ELEMENT ABSENT" }); continue; }
    const n = TEL.length;
    el.click();
    await new Promise(r => setTimeout(r, 60));
    const fired = TEL.slice(n).map(e => e.type);
    results.push({ path: label, fired, status: fired.length ? "OK" : "NO EVENT — investigate" });
  }

  // Structural assertions that a click cannot make.
  const structural = {
    ack_changes_rendered: document.querySelectorAll('.ack-changes li').length,
    ack_read_rest_control: document.querySelectorAll('.ack-read-rest').length,   // 0 ⇒ momack_unfolded unreachable
    legacy_prose_branch_live: document.querySelectorAll('.ack-msg-lead').length, // 0 ⇒ changes[] branch is the live one
  };

  MetricsCollector.track = origTrack;
  window.fetch = origFetch;
  if (origBeacon) navigator.sendBeacon = origBeacon;

  const out = {
    results,
    structural,
    worker_configured: (function () {
      try { const c = JSON.parse(localStorage.getItem("tateTracker.sync.v1") || "{}"); return !!(c.workerUrl && c.token); }
      catch (e) { return false; }
    })(),
    attempted_network: BLOCKED.length,
  };
  // worker_configured MUST be false and attempted_network 0 on a clean run. If
  // either is otherwise you are not on localhost, and the run is not inert.
  console.log(JSON.stringify(out, null, 1));
  return out;
};
