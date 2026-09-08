#!/usr/bin/env python3
"""watch-feedback.py — what has arrived on an estate, and has anyone disposed of it?

    python3 tools/watch-feedback.py                          # every declared environment
    python3 tools/watch-feedback.py --env home
    python3 tools/watch-feedback.py --env home --brief       # write Paul's disposition sheet
    python3 tools/watch-feedback.py --dispose '<key>' --as act --why "became BACKLOG row X"
    python3 tools/watch-feedback.py --arm-check              # F6: may the next beat 1 open?
    python3 tools/watch-feedback.py --selftest               # offline

⭐ BEATS F1 · F2 · F6 of the feedback-consolidation loop
(`.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md` §C.1): **sweep → label → 👤 Paul
disposes → researcher reads → carry to a row → arm.** This tool is the machine half. Beat F3 is
Paul's and nothing here does it; F4 and F5 are seats and nothing here calls one.

⛔ WHY IT EXISTS. The release loop ends at Paul's clear and **has no successor beat** — nothing owned
the words a real person left on the way through. Ten records landed on `est-e6696a` on 2026-09-07 and
were read only because Paul asked. That is the 2026-07-26 finding (*capture is not a loop*)
reproduced on a new estate, and it is this corpus's oldest shape: **a writer with no reader.**

⭐ IT DISCOVERS CHANNELS, IT DOES NOT RESTATE THEM. It enumerates `<estate>:` and groups by key kind,
so a channel nobody built a reader for is **named on this tool's face** rather than being invisible
until someone remembers it. The design's §E said "anything that is not /api/feedback" could not be
seen; enumerating the store rather than polling one route is what removes that bound.

⭐ AND IT NEEDS NO WORKER CREDENTIAL. The design (§C.3) recorded production as unreadable *by
construction* because `.private/fernwood-token-home` does not exist, and warned that building the
sweep on the verification seat's leftover administrator token would make it die at the first
revocation. Reading the store through the same local wrangler auth `grant-mint.py` already uses
retires both problems: there is no token file to be missing and no credential to be revoked.

⛔ THE MODEL DOES NOT READ THE WORDS, AND THAT IS THE POINT OF THE SPLIT.
*"AI never touches an estate's people or their words… the administrator's eyes sit between the model
and the estate's people, both directions."* So verbatim `note` text is streamed from the store to
`.private/` and **never printed**: the terminal gets the LABELS (record id · personId · ts · surface ·
screen · producing control · whether a note is present and how long it is) plus the path Paul opens.

⚠️ **WHICH HALF OF THE BOUNDARY THIS IS, said plainly so the quarantine file is not mistaken for a
violation.** A *tool* writing a person's verbatim words into `.private/` is the **deterministic
capture path**, which is allowed to touch them and always has been — that is what `.private/` is for.
The line the boundary draws is the **MODEL** reading them. This file is on the correct side of it in
both directions: the bytes go store → disk without passing through a printed line, and nothing here
summarises, classifies or interprets a sentence anybody wrote.

⛔ **THERE IS DELIBERATELY NO `--words` FLAG, AND ITS ABSENCE IS THE CONTROL. Do not add one.** An
affordance that exists gets used — usually by a later session that does not know why it should not —
and a comment saying "don't use this" is not a control, it is a suggestion. Paul loses no access:
the verbatim file and the disposition sheet are right there, one `open` away. Someone who wants the
words on screen opens the file, which puts the administrator's eyes exactly where the rule puts them.

⛔ IT ASSERTS NOTHING ABOUT WHO ANYONE IS. Paul is several person-ids today. It prints ids and
divergence against the register; a human names the human.

⛔ NEVER GREEN BY ABSENCE, and the destination is proved before any count is believed — an empty
listing means "empty" only after the namespace has said who it is. Both controls are imported from
`watch-accounts.py` rather than re-typed, because a SECOND copy of a fail-closed control is a copy
that drifts, and this one is the one that must never quietly return zero.

⛔ THE DISPOSITION IS PER (env, estate, channel, record id). A batch may never be cleared by one of
its members (`CLAUDE.md`, 2026-08-28). There is no watermark at all: an undisposed record is listed
every run, forever, so nothing can bury one. There is no `--dispose-all`.
"""
import argparse, re, collections, datetime as dt, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PRIVATE = os.path.join(ROOT, ".private")
SWEEPS = os.path.join(PRIVATE, "feedback-sweep")
STATE = os.path.join(PRIVATE, "watch-feedback-state.json")
# ⭐ THE DISPOSITIONS ARE TRACKED, and they are the only part of this that is. Sited beside
# `arrival-dispositions.json` for the same reason that file is tracked: a disposition is a fact about
# OUR OWN CONDUCT — whether anybody looked — and in `.private/` it would be invisible to the repo's
# own memory, which is exactly where "did we ever answer this person?" has to be answerable.
# ⛔ It carries NO note text and no note length. The words stay in `.private/`; this records only
# that a record existed, and what was decided about it.
DISPOSITIONS_FILE = os.path.join(ROOT, "feedback-dispositions.json")

# ⭐⭐ WHICH ENVIRONMENTS CAN BLOCK A LAP `[paul-ruled 2026-09-07, process-audit G1]`
# ⛔ THE PROBLEM THIS FIXES. Beat 11 exits at "zero records undisposed" and beat 10's gate is
# "the board may not be laid out while records nobody has read are sitting in the store." Measured
# 2026-09-07: 477 awaiting — qa 431 · lab 38 · home 7 · prod 1. Disposal is deliberately one
# hand-written reason per record with no `--dispose-all`, and F3 is Paul's beat alone. So both
# conditions were UNREACHABLE and the lap could not close: ~2 hours of Paul writing justifications
# for machine output. An exit condition no mechanism can produce is not an exit condition.
# ⭐ THE FIX IS A DEFINITION, NOT A BULK CLEAR. `qa` and `lab` are estates the loop drives with its
# OWN synthetic walkers — every record there was written by us. `home` and `prod` are the estates
# real people reach. The gate was always meant to mean *a person said something and nobody has read
# it*; counting our own walkers' form-fills made it mean something else and defeated it.
# ⛔ NOTHING IS HIDDEN AND NOTHING IS MASS-DISPOSED. Non-gating records are still swept, still
# listed, still individually disposable, and still counted in the header — they simply do not BLOCK.
# Same posture as watch-accounts' "unacknowledged and not hidden".
# ⭐ WHY NOT A `--dispose-class` (the other route on the table): a bulk disposition over a named
# class is precisely the `--dispose-all` this tool refuses to have, and once built it could clear
# real records as easily as synthetic ones. The cheaper fix needs no such tool, so it does not get
# one. `[[feedback_reuse_vocabulary_before_adding_state]]`
# ⚠️ FALSIFIER, and it is checkable at any sweep: if a HUMAN ever leaves feedback on `qa` or `lab`,
# this definition silently stops it gating. Verified 2026-09-07 for the 469 records then present —
# all 38 lab notes are fixtures (`seq 1`-`seq 8`, `burst 6`, "This is a test run", "A place",
# "Testing", `1 Example Road`) and qa's 431 are 428 onboarding form-fills plus 3 probes. Paul's own
# 09-05 lab walk findings went to GATE2-paul-findings.md as spoken findings, NOT into this store.
# ⭐ Re-read that if the definition is ever widened.
GATING_ENVS = {"home", "legacy"}

# ⭐ ONE COPY OF THE STORE READER, IMPORTED — never a second implementation. `kv`,
# `destination_agrees`, `environments`, `register_persons` and the Unreadable contract all live in
# watch-accounts.py; re-typing the destination proof here is exactly how a fail-closed control
# becomes a control in only one of the two places that need it. The filename has a hyphen, so it is
# loaded by path rather than imported by name.
_spec = importlib.util.spec_from_file_location("watch_accounts", os.path.join(HERE, "watch-accounts.py"))
wa = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(wa)
Unreadable, Refuse, ENVIRONMENTS = wa.Unreadable, wa.Refuse, wa.ENVIRONMENTS
now_iso, ago = wa.now_iso, wa.ago

# ---- what this tool knows about the channels it may find -------------------------------------
# ⭐ A KIND THIS TOOL DOES NOT READ IS NAMED, NOT SKIPPED. "We have no reader for this" and "there is
# nothing here" must never print the same thing — that is the same rule as UNREADABLE, one level out.
READS_HERE = ("feedback",)
READ_ELSEWHERE = {
    "metrics": "release-gate.py clause 5 · read-mom-engagement.py (frozen estate only)",
    "grant": "watch-accounts.py",
    "account": "watch-accounts.py",
    "chat-budget": "the Worker itself (a daily spend counter, not an arrival)",
    "cost-log": "/api/cost-log",
    # ⭐ MOVED OUT OF `NO_READER` 2026-09-07, the day they stopped being unread. Both were built this
    # lap: `72b9276` added tools/watch-door.py to read them, `b8aa535` added GET
    # /api/onboarding-metrics. ⛔ Correcting the STRING in NO_READER would not have been enough —
    # anything in that dict prints "NO TOOL READS IT" regardless of what its reason says, so a
    # corrected reason under the wrong heading is a truer sentence that still reads false.
    "door": "watch-door.py — arrivals, and who reached the door without getting through",
    "onboarding-metrics": "watch-door.py · GET /api/onboarding-metrics (worker.js, 2026-09-07)",
}
# Kinds that carry a person's input and have NO deterministic reader anywhere. Listing them by name
# is the whole remedy — and the entries here are a CLAIM ABOUT THE WORLD that expires the moment
# someone writes a reader, so they must be re-read whenever one is built.
NO_READER = {
    # ⚠️ `door` and `onboarding-metrics` LIVED HERE UNTIL 2026-09-07 and their entries said "there is
    # no GET route anywhere" and "no tool in this repo reads it". Both were falsified the same evening
    # by this lap's own commits, and both kept printing for hours — at every beat 0, and at beat 6
    # where this tool GATES the commitment point. A tool that describes the world it lives in has to
    # be re-read when that world changes, and nothing connected the two.
    "observations": "read only by the frozen estate's mom-cycle tools",
    "zone-audio": "read only by the frozen estate's mom-cycle tools",
    "conversations": "read only by the frozen estate's mom-cycle tools",
}

DISPOSITIONS = ("act", "fold", "hold", "not-a-finding")

# A daily key is `YYYY-MM-DD`. Used to decide whether a channel's keys may be CALLED days.
DATE_KEY_RX = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# §C.5's labelling contract. ⛔ COUNTED, NEVER GRADED: a grade would read red on every record written
# before the contract existed, which is the permanently-red alarm this repo forbids. Its own
# falsifier is in the design — if coverage sits at 100% for two laps, delete the line.
def labels(rec):
    ctx = rec.get("context") or {}
    control = ctx.get("questionId") or ctx.get("field") or ctx.get("type")
    return {
        "personId": bool(rec.get("personId")),
        "estate+env": bool(rec.get("estateId") and rec.get("env")),
        "ts": bool(rec.get("ts")),
        "surface": bool(ctx.get("surface")),
        "screen-or-step": bool(ctx.get("screen") or ctx.get("step")),
        "control": bool(control),
    }


def control_of(rec):
    ctx = rec.get("context") or {}
    return ctx.get("questionId") or ctx.get("field") or ctx.get("type") or None


def summarise(rec):
    """The LABELS only. `note` is reduced to presence and length and never carried further."""
    ctx = rec.get("context") or {}
    note = rec.get("note")
    return {
        "id": rec.get("id"), "ts": rec.get("ts"), "personId": rec.get("personId"),
        "surface": ctx.get("surface"), "screen": ctx.get("screen") or ctx.get("step"),
        "control": control_of(rec), "sentiment": rec.get("sentiment"),
        "sessionId": rec.get("sessionId"), "deviceId": rec.get("deviceId"),
        "noteChars": len(note) if isinstance(note, str) else 0,
        "labels": labels(rec),
    }


# ---- the sweep ---------------------------------------------------------------------------------
def channels(env, estate):
    """Every key kind present on this estate, with its dates. Raises Unreadable — never a zero."""
    wa.destination_agrees(env)
    found = collections.defaultdict(list)
    for key in wa.kv_list(env, "%s:" % estate):
        parts = key.split(":", 2)
        if len(parts) == 3:
            found[parts[1]].append(parts[2])
    return {k: sorted(v) for k, v in found.items()}


def read_feedback(env, estate, dates):
    """Every feedback record across `dates`. A day that will not parse is an Unreadable DAY, reported
    by name — one bad day may not silence the others, and it may not vanish either."""
    records, bad = [], []
    for d in dates:
        key = "%s:feedback:%s" % (estate, d)
        try:
            rows = wa.kv_get(env, key)
        except Unreadable as e:
            bad.append((d, str(e)))
            continue
        if not isinstance(rows, list):
            bad.append((d, "the day's value is %s, not a list of records" % type(rows).__name__))
            continue
        for r in rows:
            if isinstance(r, dict):
                records.append((d, r))
    return records, bad


def load_state():
    if not os.path.exists(STATE):
        return {"_comment": "watch-feedback.py — dispositions are keyed per (env, estate, channel, "
                            "record id). There is no watermark, so nothing can bury a record.",
                "envs": {}, "records": {}}
    with open(STATE, encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    os.makedirs(PRIVATE, exist_ok=True)
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    os.replace(tmp, STATE)


def load_dispositions():
    if not os.path.exists(DISPOSITIONS_FILE):
        return {"_comment": "Per-record dispositions for feedback arrivals, keyed "
                            "(env|estate|channel|record id). ⛔ THIS FILE IS TRACKED IN A PUBLIC "
                            "REPO. No note text and no personId ever land here — the words live in "
                            ".private/ and person ids live in the private sibling's grants.json. A "
                            "`why` is written by a human and goes public with it: say where the "
                            "record went, never what anybody said. A batch may never be cleared by "
                            "one of its members, so there is no bulk write and no watermark.",
                "dispositions": {}}
    with open(DISPOSITIONS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_dispositions(disp):
    tmp = DISPOSITIONS_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(disp, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    os.replace(tmp, DISPOSITIONS_FILE)


def rec_key(env, estate, channel, ident):
    return "%s|%s|%s|%s" % (env, estate, channel, ident)


def sweep(envs, state, disp, days=None, write=True, chan=channels, feed=read_feedback, keep=None):
    """F1 + F2. `keep` receives (env, date, raw_records) so the VERBATIM can be written to `.private/`
    without ever passing through a printed line."""
    try:
        known = wa.register_persons()
    except Unreadable:
        known = None

    report = []
    for env in envs:
        cfg = ENVIRONMENTS.get(env) or {}
        estate = cfg.get("estate")
        row = {"env": env, "estate": estate, "result": None, "why": None,
               "channels": {}, "unread_channels": [], "channel_key_shape": {},
               "records": [], "undisposed": [],
               "bad_days": [], "coverage": (0, 0), "divergent": [],
               "lastCheckedAt": (state["envs"].get(env) or {}).get("lastCheckedAt")}
        if not estate:
            row["result"] = "UNREADABLE"
            row["why"] = "the environment declares no ESTATE_ID in worker/wrangler.toml"
            report.append(row); continue
        try:
            found = chan(env, estate)
        except Unreadable as e:
            row["result"], row["why"] = "UNREADABLE", str(e)
            report.append(row); continue

        row["result"] = "READ"
        row["channels"] = found
        for kind, dates in sorted(found.items()):
            if kind in READS_HERE or kind in READ_ELSEWHERE:
                continue
            # ⭐ Say what the keys ACTUALLY are before naming them. A channel keyed by date gets
            # "day"; anything else gets "key", and the reader is not told a span of time that the
            # store never claimed.
            row["channel_key_shape"][kind] = (
                "day" if dates and all(DATE_KEY_RX.match(str(d)) for d in dates) else "key")
            row["unread_channels"].append((kind, len(dates),
                                           NO_READER.get(kind, "no reader is known to this tool")))

        dates = sorted(found.get("feedback", []))
        if days:
            cutoff = (dt.date.today() - dt.timedelta(days=days - 1)).isoformat()
            dates = [d for d in dates if d >= cutoff]
        records, bad = feed(env, estate, dates)
        row["bad_days"] = bad
        if keep:
            keep(env, estate, records)

        ok = 0
        for _d, rec in records:
            s = summarise(rec)
            row["records"].append(s)
            if all(s["labels"].values()):
                ok += 1
            k = rec_key(env, estate, "feedback", s["id"])
            st = state["records"].get(k)
            if st is None:
                # `.private/` remembers WHEN WE FIRST SAW IT — an observation about us, not a
                # decision. The decision lives in the tracked register and only a human writes one.
                st = {"firstSeenAt": now_iso(), "env": env, "estate": estate,
                      "channel": "feedback", "id": s["id"], "ts": s["ts"]}
                if write:
                    state["records"][k] = st
            if not (disp["dispositions"].get(k) or {}).get("disposition"):
                row["undisposed"].append((k, s, st))
            if known is not None and s["personId"] and \
                    s["personId"] not in known.get(estate, wa.EMPTY_ESTATE)["all"]:
                row["divergent"].append(s["personId"])
        row["coverage"] = (ok, len(records))
        # ⛔ THE CONSTANT-id CAPTURE LIE IS DELIBERATELY NOT REPORTED HERE, and deleting the check
        # that tried to is the finding. `worker.js:3082-3085` is idempotent on a client-supplied id
        # and answers 200 {duplicate:true} while `homes/index.html:243` posts a CONSTANT one, so the
        # second use in any UTC day is DROPPED and the screen still says it landed.
        # ⚠️ This tool reads what is IN the store. The dropped post is not in the store. There is no
        # arrangement of these records from which the loss can be inferred — §E of the design says it
        # in one line: *the sweep cannot count what never landed.*
        # ⛔ A first version flagged "one producing control wrote more than one record", and on its
        # FIRST LIVE RUN it accused `name` and `address` — which were two different people each
        # completing onboarding once. A checker that dresses a non-finding as a finding costs more
        # than the gap it was covering, because the next reader has to disprove it. The honest
        # instrument is a POSITIVE CONTROL (post the same control twice, assert two records), which
        # is a test and not a sweep. Recorded as a blind spot; not re-derived as a heuristic.
        row["divergent"] = sorted(set(row["divergent"]))

        if write:
            prev = state["envs"].get(env) or {}
            state["envs"][env] = {"lastCheckedAt": now_iso(), "result": "READ",
                                 "watchingSince": prev.get("watchingSince") or now_iso()}
        report.append(row)

    if write:
        for row in report:
            if row["result"] == "UNREADABLE":
                prev = state["envs"].get(row["env"]) or {}
                state["envs"][row["env"]] = dict(prev, lastCheckedAt=now_iso(),
                                                 result="UNREADABLE", why=row["why"])
    return report


def render(report, show_all=False):
    lines = []
    unread = [r for r in report if r["result"] == "UNREADABLE"]
    # ⭐ TWO COUNTS, NEVER ONE `[paul-stated 2026-09-08]`. This line used to print one
    # undifferentiated total "awaiting Paul's disposition" — 587 of them — while the F6 ARM
    # line at the bottom of the same output, `GATING_ENVS`, and beat 11's own exit condition
    # ALL already scoped the obligation to a REAL ESTATE, where the true figure was ZERO.
    # Three parts of the loop agreed and the one number a reader sees first did not, so the
    # headline read as a backlog of 587 things Paul owed. It is a count without its predicate,
    # which is this corpus's most-repeated instrument defect, committed by the instrument
    # written to find it.
    # ⛔ SYNTHETIC RECORDS ARE OUR OWN TEST EXHAUST, NOT SOMEBODY'S INPUT — they are a finding
    # SOURCE and belong in the backlog's rationalization, never in a per-record queue with a
    # human's name on it. Real-estate records stay per-record and stay his: those are people's
    # words, and both the AI boundary and the per-arrival rule bind there.
    gating   = sum(len(r["undisposed"]) for r in report if r["env"] in GATING_ENVS)
    synthetic = sum(len(r["undisposed"]) for r in report if r["env"] not in GATING_ENVS)
    lines.append("📥 Feedback watch — %d environment(s) · %d awaiting Paul on a REAL ESTATE "
                 "· %d on our own environments (backlog material, not his queue) · %d unreadable"
                 % (len(report), gating, synthetic, len(unread)))
    for r in report:
        # ⭐ ONE LINE PER ENVIRONMENT, EVERY RUN — a quiet estate and a dead watcher must never look
        # the same. This is the Mom-check counter's discipline, and the reason it exists.
        if r["result"] == "UNREADABLE":
            lines.append("   ⚠️ %-5s · %-10s — UNREADABLE · ? records · last checked %s"
                         % (r["env"], r["estate"] or "no estate", ago(r["lastCheckedAt"])))
            lines.append("        %s" % r["why"])
            continue
        ok, total = r["coverage"]
        lines.append("   %s %-5s · %-10s — %d record(s) · %d awaiting disposition · %d of %d fully "
                     "labelled · checked %s"
                     % ("🔔" if r["undisposed"] else "·", r["env"], r["estate"], total,
                        len(r["undisposed"]), ok, total, ago(r["lastCheckedAt"])))
        for d, why in r["bad_days"]:
            lines.append("        ⚠️ %s is UNREADABLE — %s (this day is not counted above)" % (d, why))
        shown = r["undisposed"] if show_all else r["undisposed"][:8]
        for k, s, st in shown:
            missing = [n for n, v in s["labels"].items() if not v]
            lines.append("        🔔 %s · %s · %s · %s/%s · %s · note %s"
                         % (s["id"], s["ts"], s["personId"] or "no personId",
                            s["surface"] or "—", s["screen"] or "—", s["control"] or "—",
                            "%d chars" % s["noteChars"] if s["noteChars"] else "none"))
            lines.append("           %s%s" % (k, ("  ⚠️ unlabelled: " + ", ".join(missing)) if missing else ""))
        if len(r["undisposed"]) > len(shown):
            lines.append("        … and %d more awaiting disposition — `--env %s --all` prints every one"
                         % (len(r["undisposed"]) - len(shown), r["env"]))
        for kind, n, why in r["unread_channels"]:
            # ⛔ "day(s)" WAS A LIE ON ANY CHANNEL NOT KEYED BY DATE `[process-audit G8, 2026-09-07]`.
            # The number is len(keys); for `library` that printed "holds 8114 day(s)" — 22 years —
            # in every beat-0 sweep, because that channel's keys are not dates at all. The COUNT was
            # right and the NOUN was wrong, which is the failure mode this repo names
            # `[[reference_match_payload_not_container]]`: a plausible number under a word that does
            # not describe it is worse than an error, because nobody checks it.
            shape = r.get("channel_key_shape", {}).get(kind) or "key"
            lines.append("        📦 channel `%s` holds %d %s(s) and NO TOOL READS IT — %s"
                         % (kind, n, shape, why))
        if r["divergent"]:
            lines.append("        ⚡ personId(s) the local register does not know at %s: %s"
                         % (r["estate"], ", ".join(r["divergent"])))
    # ⭐ THE FOOTER FOLLOWS THE SAME SPLIT `[paul-stated 2026-09-08]`. It used to fire on ANY
    # undisposed record and address Paul by name, so 587 synthetic form-fills printed a standing
    # instruction to a human who owed nothing — the same count-without-its-predicate defect as the
    # headline, one screen lower. Real-estate records are people's words and stay his, per record.
    # Synthetic records are our own walk exhaust: they are a finding SOURCE, and they are read in
    # context at the backlog's rationalization, never one at a time with his name on them.
    if gating:
        lines.append("")
        lines.append("   ⛔ Beat F3 is PAUL'S. Nothing here reads what anyone wrote; the words are in")
        lines.append("      %s — open them, then:" % os.path.relpath(SWEEPS, ROOT))
        lines.append("      python3 tools/watch-feedback.py --dispose '<key>' --as act|fold|hold|not-a-finding --why \"…\"")
    elif synthetic:
        lines.append("")
        lines.append("   ✅ Nothing on a real estate is undisposed — Paul owes none of the %d below." % synthetic)
        lines.append("      They are OUR OWN walk exhaust (%s). They are backlog material, read in"
                     % ", ".join(sorted(r["env"] for r in report if r["undisposed"] and r["env"] not in GATING_ENVS)))
        lines.append("      context at rationalization, not a per-record queue.")
    return "\n".join(lines)


# ---- F3's artefacts (written for Paul; never printed) ------------------------------------------
def write_sweep(env, estate, records):
    """The VERBATIM, straight from the store to `.private/`. Gitignored, and it is the only place a
    person's own sentences come to rest on this machine."""
    if not records:
        return None
    os.makedirs(SWEEPS, exist_ok=True)
    path = os.path.join(SWEEPS, "%s-%s.json" % (env, dt.date.today().isoformat()))
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"env": env, "estateId": estate, "sweptAt": now_iso(),
                   "records": [r for _d, r in records]}, f, indent=2, ensure_ascii=False)
    return path


def write_brief(report, state):
    """§C.1 F3: one screen of *who · when · which screen · what they said*, for the administrator's
    eyes. It carries the words, so it is written into `.private/` and its PATH is what gets printed."""
    os.makedirs(SWEEPS, exist_ok=True)
    path = os.path.join(SWEEPS, "DISPOSITION-SHEET-%s.md" % dt.date.today().isoformat())
    out = ["# Disposition sheet — %s" % dt.date.today().isoformat(), "",
           "Beat F3. Every record below needs **its own** disposition: `act` · `fold` · `hold` · "
           "`not-a-finding`. A batch may not be cleared by one of its members.", ""]
    for r in report:
        if r["result"] != "READ":
            out += ["## %s — UNREADABLE" % r["env"], "", r["why"] or "", ""]
            continue
        out += ["## %s · %s — %d awaiting disposition" % (r["env"], r["estate"], len(r["undisposed"])), ""]
        raw = {}
        p = os.path.join(SWEEPS, "%s-%s.json" % (r["env"], dt.date.today().isoformat()))
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                raw = {x.get("id"): x for x in json.load(f).get("records", [])}
        for k, s, _st in r["undisposed"]:
            note = (raw.get(s["id"]) or {}).get("note")
            out += ["- **%s** · %s · person `%s` · %s/%s · control `%s`"
                    % (s["id"], s["ts"], s["personId"] or "—", s["surface"] or "—",
                       s["screen"] or "—", s["control"] or "—"),
                    "  - said: %s" % (("> " + str(note)) if note else "_(no note — this was a tap, not words)_"),
                    "  - dispose: `python3 tools/watch-feedback.py --dispose '%s' --as <act|fold|hold|not-a-finding> --why \"…\"`" % k,
                    ""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    return path


def dispose(state, disp, key, how, why):
    """⛔ ONE RECORD, one disposition, one reason. There is no `--dispose-all` and no pattern match:
    a clear that names a SET rather than its members is the failure `check-arrival-dispositions.py`
    exists to stop, where a channel reads attested while a record in it was never opened."""
    # A key is disposable only once a sweep has SEEN it in the store, so nothing invented can be
    # disposed. ⚠️ That knowledge lives in `.private/`, which is gitignored — if it is lost, one
    # sweep restores it, and the tracked dispositions themselves are never at risk.
    if key not in state["records"]:
        raise Refuse("no record %r is known — run the sweep first and copy a key from its output" % key)
    seen = state["records"][key]
    if how not in DISPOSITIONS:
        raise Refuse("disposition %r is not one of %s" % (how, ", ".join(DISPOSITIONS)))
    if not (why or "").strip():
        raise Refuse("--why is required. ⭐ `nobody looked` and `we looked and it was fine` must never "
                     "record the same thing, and only the reason tells them apart")
    st = disp["dispositions"].get(key)
    if st and st.get("disposition"):
        raise Refuse("%s was already disposed %s as %r (%s)"
                     % (key, st["disposedAt"], st["disposition"], st["why"]))
    # ⛔ NO personId, DELIBERATELY. A person id is a pseudonymous identifier for a real human, and
    # this repo is public — which is exactly why `grants.json` lives in the private sibling rather
    # than here. The store already holds the attribution; this file records only our own conduct.
    st = {k: seen.get(k) for k in ("env", "estate", "channel", "id", "ts")}
    st.update(disposition=how, why=why.strip(), disposedAt=now_iso())
    disp["dispositions"][key] = st
    return st


def arm_check(report):
    """F6. ⛔ IT COMPUTES NO LAP AGE AND NEVER SAYS A LAP IS LATE — the loop rests, and only an
    UNDISPOSED ARRIVAL blocks it. Fail-closed: an unreadable environment is not green."""
    lines, blocked = [], False
    for r in report:
        gating = r["env"] in GATING_ENVS
        if r["result"] == "UNREADABLE":
            # ⛔ UNREADABLE BLOCKS FROM ANY ENVIRONMENT, gating or not. "We could not look" is never
            # downgraded by where we could not look — the fail-closed half is not what G1 relaxed.
            lines.append("   ⛔ %-5s — UNREADABLE, so it is NOT green: %s" % (r["env"], r["why"]))
            blocked = True
        elif r["undisposed"] and not gating:
            lines.append("   ▫ %-5s — %d undisposed, NOT gating (this loop's own walkers write here; "
                         "still listed and still disposable)" % (r["env"], len(r["undisposed"])))
        elif r["undisposed"]:
            lines.append("   ⛔ %-5s — %d record(s) awaiting Paul's disposition" % (r["env"], len(r["undisposed"])))
            blocked = True
        elif r["bad_days"]:
            lines.append("   ⛔ %-5s — %d day(s) unreadable, so its count is not trustworthy"
                         % (r["env"], len(r["bad_days"])))
            blocked = True
        else:
            lines.append("   ✅ %-5s — every arrival disposed" % r["env"])
    gating_n = sum(len(r["undisposed"]) for r in report if r["env"] in GATING_ENVS)
    other_n = sum(len(r["undisposed"]) for r in report if r["env"] not in GATING_ENVS)
    head = ("🔒 F6 ARM — the next beat 1 is BLOCKED" if blocked else "🔓 F6 ARM — nothing gating is undisposed")
    head += ("  ·  %d awaiting on a real estate%s"
             % (gating_n, (" (+%d on a synthetic estate, not gating)" % other_n) if other_n else ""))
    return "\n".join([head] + lines), blocked


# ---- selftest ----------------------------------------------------------------------------------
def selftest():
    global STATE, SWEEPS
    import tempfile
    fails = []

    def check(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            fails.append(name)

    global DISPOSITIONS_FILE
    tmp = tempfile.mkdtemp()
    STATE = os.path.join(tmp, "state.json")
    SWEEPS = os.path.join(tmp, "sweeps")
    DISPOSITIONS_FILE = os.path.join(tmp, "feedback-dispositions.json")

    chans = {"home": {"feedback": ["2026-09-07"], "grant": ["x"], "account": ["y"],
                      # ⚠️ `zone-audio` is the fixture BECAUSE it is still genuinely unread. This
                      # used `onboarding-metrics`, which moved to READ_ELSEWHERE on 2026-09-07 when a
                      # reader was built — and the control correctly FAILED rather than passing over
                      # a channel that no longer had anything to name. A fixture that names a real
                      # member of the set under test has to be re-pointed when that set changes;
                      # re-pointing it keeps the BEHAVIOUR asserted, which is what the control is for.
                      "zone-audio": ["2026-09-06", "2026-09-07"], "door": ["2026-09-06"]}}
    recs = {("home", "2026-09-07"): [
        {"id": "fb-1", "ts": "2026-09-07T15:00:00Z", "personId": "p-a", "estateId": "est-e6696a",
         # ⚠️ A SENTINEL NOBODY WOULD WRITE IN PROSE. It was "the words", which appears verbatim in
         # this tool's own F3 footer and in the register's `_comment` — so the leak checks below
         # failed on the tool DESCRIBING the boundary rather than on it crossing one. A leak test
         # whose needle can occur innocently is a test that cries wolf until someone deletes it.
         "env": "home", "note": "QQ-VERBATIM-SENTINEL-QQ", "sentiment": None, "sessionId": "s1", "deviceId": None,
         "context": {"surface": "app", "screen": "card-property", "questionId": "q1", "type": "t"}},
        {"id": "onboard-x", "ts": "2026-09-07T15:01:00Z", "personId": "p-a", "estateId": "est-e6696a",
         "env": "home", "note": None, "sentiment": None, "sessionId": "s1", "deviceId": None,
         "context": {"field": "place-name", "step": "s1", "type": "onboard"}},
        {"id": "homes-second-home", "ts": "2026-09-07T15:02:00Z", "personId": "p-a",
         "estateId": "est-e6696a", "env": "home", "note": None, "sentiment": None,
         "sessionId": None, "deviceId": None, "context": {"screen": "homes", "type": "add-home"}},
        # ⭐ A SECOND PERSON USING THE SAME CONTROL AS `onboard-x`. This is what the deleted
        # duplicate-control heuristic accused on its first live run, so the guard below is only
        # meaningful while this record exists. Do not remove it to tidy the fixture.
        {"id": "onboard-y", "ts": "2026-09-07T15:03:00Z", "personId": "p-b", "estateId": "est-e6696a",
         "env": "home", "note": None, "sentiment": None, "sessionId": "s2", "deviceId": None,
         "context": {"field": "place-name", "step": "s1", "type": "onboard"}},
    ]}
    dead, badday = set(), set()

    def fake_chan(env, estate):
        if env in dead:
            raise Unreadable("pretend outage")
        return chans[env]

    def fake_feed(env, estate, dates):
        out, bad = [], []
        for d in dates:
            if (env, d) in badday:
                bad.append((d, "pretend corrupt day")); continue
            out += [(d, r) for r in recs.get((env, d), [])]
        return out, bad

    st, dp = load_state(), load_dispositions()
    rep = sweep(["home"], st, dp, chan=fake_chan, feed=fake_feed, keep=write_sweep)
    out = render(rep)
    check("every record arrives awaiting a disposition", len(rep[0]["undisposed"]) == 4)
    check("coverage is COUNTED, not graded", rep[0]["coverage"] == (1, 4) and "1 of 4 fully labelled" in out)
    check("a channel with no reader is NAMED, not skipped",
          any(c[0] == "zone-audio" for c in rep[0]["unread_channels"]) and "NO TOOL READS IT" in out)
    # ⛔ REGRESSION GUARD on a check that was DELETED. Two different people each using the same
    # control once is normal onboarding, and a first version reported it as a suspected capture lie
    # on its first live run. Nothing may re-derive that heuristic.
    check("two people using the same control is not reported as a finding",
          "wrote more than one record" not in out and "dup" not in out.lower())
    check("a channel another tool reads is not reported as unread",
          not any(c[0] in ("grant", "account") for c in rep[0]["unread_channels"]))
    # ⛔ THE BOUNDARY: the words go to `.private/` and never into a printed line.
    check("no record's note text appears anywhere in the output", "QQ-VERBATIM-SENTINEL-QQ" not in out)
    p = os.path.join(SWEEPS, "home-%s.json" % dt.date.today().isoformat())
    check("the verbatim IS written, to .private, so Paul loses nothing",
          os.path.exists(p) and "QQ-VERBATIM-SENTINEL-QQ" in open(p, encoding="utf-8").read())
    brief = write_brief(rep, st)
    check("the disposition sheet carries the words and is written under .private",
          "QQ-VERBATIM-SENTINEL-QQ" in open(brief, encoding="utf-8").read() and brief.startswith(SWEEPS))

    # ⭐ PER-RECORD: disposing one leaves its siblings open.
    k1 = rec_key("home", "est-e6696a", "feedback", "fb-1")
    dispose(st, dp, k1, "act", "became a row")
    rep = sweep(["home"], st, dp, chan=fake_chan, feed=fake_feed)
    check("disposing one record leaves its siblings awaiting", len(rep[0]["undisposed"]) == 3)
    # ⛔ THE SPLIT: the decision is tracked, the words are not, and neither file holds the other's job.
    save_dispositions(dp)
    written = open(DISPOSITIONS_FILE, encoding="utf-8").read()
    check("the disposition register carries the decision", "became a row" in written)
    check("the disposition register carries NO note text", "QQ-VERBATIM-SENTINEL-QQ" not in written)
    for bad_call, label in (((k1, "act", "again"), "re-disposing is refused"),
                            ((k1 + "x", "act", "y"), "an unknown key is refused"),
                            ((rec_key("home", "est-e6696a", "feedback", "onboard-x"), "shrug", "y"),
                             "an unknown disposition is refused"),
                            ((rec_key("home", "est-e6696a", "feedback", "onboard-x"), "act", " "),
                             "a disposition with no reason is refused")):
        try:
            dispose(st, dp, *bad_call); check(label, False)
        except Refuse:
            check(label, True)

    # F6 is fail-closed in three separate ways.
    txt, blocked = arm_check(rep)
    check("F6 blocks while anything is undisposed", blocked and "BLOCKED" in txt)
    for k, _s, _st in list(rep[0]["undisposed"]):
        dispose(st, dp, k, "not-a-finding", "looked; nothing in it")
    rep = sweep(["home"], st, dp, chan=fake_chan, feed=fake_feed)
    txt, blocked = arm_check(rep)
    check("F6 opens once every arrival is disposed", not blocked and "nothing gating is undisposed" in txt)

    # ⭐ G1's MUTATION PROOF `[paul-ruled 2026-09-07]`. The change above relaxed WHICH environments
    # can block, and a relaxation that is not proven both ways is how a gate quietly stops gating.
    # These two legs are a PAIR and must stay a pair: the same undisposed record blocks from a real
    # estate and does not block from a synthetic one.
    qa_chan = {"qa": {"feedback": ["2026-09-07"]}}
    qa_recs = {("qa", "2026-09-07"): [
        {"id": "fb-synth", "ts": "2026-09-07T15:00:00Z", "personId": "p-qa-synth-1",
         "estateId": "est-qa0001", "env": "qa", "note": "seq 1", "sentiment": None,
         "sessionId": "s9", "deviceId": None, "context": {"surface": "app"}}]}
    st2, dp2 = {"envs": {}, "records": {}}, {"dispositions": {}}
    def qa_chan_fn(env, estate):
        return qa_chan[env]

    def qa_feed_fn(env, estate, dates):
        return [(d, r) for d in dates for r in qa_recs.get((env, d), [])], []

    rep_qa = sweep(["qa"], st2, dp2, chan=qa_chan_fn, feed=qa_feed_fn)
    txt_qa, blocked_qa = arm_check(rep_qa)
    check("G1 an undisposed record on a SYNTHETIC estate does NOT block F6",
          not blocked_qa and "NOT gating" in txt_qa)
    check("G1 ...and it is still COUNTED and named, never hidden",
          "1 undisposed" in txt_qa and len(rep_qa[0]["undisposed"]) == 1)
    # ⛔ The fail-closed half is NOT relaxed: unreadable blocks from anywhere.
    def dead_chan(env, estate):
        raise Unreadable("pretend canary empty")

    rep_bad = sweep(["qa"], {"envs": {}, "records": {}}, {"dispositions": {}},
                    chan=dead_chan, feed=qa_feed_fn)
    _t, blocked_bad = arm_check(rep_bad)
    check("G1 an UNREADABLE synthetic estate still BLOCKS — 'we could not look' is never downgraded",
          blocked_bad)
    check("F6 says nothing about how old anything is",
          "late" not in txt.lower() and "overdue" not in txt.lower() and "days" not in txt.lower())

    badday.add(("home", "2026-09-07"))
    rep = sweep(["home"], st, dp, chan=fake_chan, feed=fake_feed)
    out = render(rep)
    txt, blocked = arm_check(rep)
    check("a day that will not parse is reported by NAME, not silently dropped",
          rep[0]["bad_days"] and "is UNREADABLE" in out)
    check("and it blocks F6 rather than reading as a clean, empty day", blocked)
    check("its records are not counted as zero", "? records" in out or "0 record(s)" in out)
    badday.clear()

    dead.add("home")
    rep = sweep(["home"], st, dp, chan=fake_chan, feed=fake_feed)
    out = render(rep)
    txt, blocked = arm_check(rep)
    check("an unreadable environment reports UNREADABLE", rep[0]["result"] == "UNREADABLE")
    check("it prints ? for the count, never 0", "? records" in out)
    check("an unreadable environment is NOT green at F6", blocked and "NOT green" in txt)
    dead.clear()

    # A new arrival after everything was disposed is open again.
    recs[("home", "2026-09-07")].append(
        {"id": "fb-2", "ts": "2026-09-07T16:00:00Z", "personId": "p-b", "estateId": "est-e6696a",
         "env": "home", "note": "later", "sentiment": None, "sessionId": None, "deviceId": None,
         "context": {"surface": "app", "screen": "s", "questionId": "q2", "type": "t"}})
    rep = sweep(["home"], st, dp, chan=fake_chan, feed=fake_feed)
    _txt, blocked = arm_check(rep)
    check("a later arrival re-blocks F6 even though its siblings were disposed",
          [u[1]["id"] for u in rep[0]["undisposed"]] == ["fb-2"] and blocked)

    check("the store reader is IMPORTED from watch-accounts, not re-implemented",
          wa.destination_agrees.__module__ == "watch_accounts")

    # ⛔ read_feedback's OWN honesty, exercised directly. The bad-day assertions above run against
    # `fake_feed` and therefore never touched this function — proven by a mutation that deleted its
    # `bad.append(...)` and still passed the whole suite. A fake that stands in for the thing under
    # test tests the fake.
    real_get = wa.kv_get
    canned = {"est-x:feedback:2026-01-01": [{"id": "a"}, {"id": "b"}],
              "est-x:feedback:2026-01-03": {"not": "a list"}}

    def fake_get(env, key):
        if key not in canned:
            raise Unreadable("pretend missing day")
        return canned[key]

    wa.kv_get = fake_get
    try:
        got, bad = read_feedback("home", "est-x", ["2026-01-01", "2026-01-02", "2026-01-03"])
        check("read_feedback returns the good day's records", [r["id"] for _d, r in got] == ["a", "b"])
        check("a day it cannot read is NAMED in bad_days, never dropped",
              [d for d, _w in bad] == ["2026-01-02", "2026-01-03"])
        check("a day whose value is not a list of records is a bad day, not zero records",
              any("not a list" in w for _d, w in bad))
        check("one bad day does not silence the good ones", len(got) == 2 and len(bad) == 2)
    finally:
        wa.kv_get = real_get
    print("selftest: %s (%d failure(s))" % ("PASS" if not fails else "FAIL", len(fails)))
    return 0 if not fails else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--env", action="append")
    ap.add_argument("--days", type=int, help="only sweep the last N dates present in the store")
    ap.add_argument("--brief", action="store_true", help="write Paul's F3 disposition sheet and print its path")
    ap.add_argument("--dispose", help="a record key printed by a run")
    ap.add_argument("--as", dest="how", help="act | fold | hold | not-a-finding")
    ap.add_argument("--why", help="what happened to it — required. ⛔ goes into a TRACKED, PUBLIC "
                                   "file: say where the record went, never what anybody said")
    ap.add_argument("--arm-check", action="store_true", help="F6: may the next beat 1 open?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    state, disp = load_state(), load_dispositions()
    if a.dispose:
        try:
            st = dispose(state, disp, a.dispose, a.how or "", a.why or "")
        except Refuse as e:
            print("⛔ %s" % e, file=sys.stderr); return 2
        save_dispositions(disp)
        print("✅ %s disposed as %s — %r" % (a.dispose, st["disposition"], st["why"]))
        print("   📝 %s is TRACKED — commit it; the words stay in .private/"
              % os.path.relpath(DISPOSITIONS_FILE, ROOT))
        return 0

    envs = a.env or sorted(ENVIRONMENTS)
    for e in envs:
        if e not in ENVIRONMENTS:
            print("⛔ %r is not declared in worker/wrangler.toml (declared: %s)"
                  % (e, ", ".join(sorted(ENVIRONMENTS))), file=sys.stderr)
            return 2

    report = sweep(envs, state, disp, days=a.days, keep=write_sweep)
    save_state(state)
    # ⭐ THE REGISTER EXISTS EVEN WHEN IT IS EMPTY. An absent file and a file recording that nobody
    # has looked yet are different facts, and only the second one is discoverable by a reader who
    # does not already know this loop exists. It carries no note text, so an empty register is
    # exactly the honest artefact: the mechanism is here, and nothing has been disposed.
    if not os.path.exists(DISPOSITIONS_FILE):
        save_dispositions(disp)

    if a.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print(render(report, show_all=a.all))
    if a.brief:
        print("\n📄 disposition sheet → %s" % os.path.relpath(write_brief(report, state), ROOT))
    if a.arm_check:
        txt, _blocked = arm_check(report)
        print("\n" + txt)

    if any(r["result"] == "UNREADABLE" for r in report):
        return 3
    return 1 if any(r["undisposed"] or r["bad_days"] for r in report) else 0


if __name__ == "__main__":
    sys.exit(main())
