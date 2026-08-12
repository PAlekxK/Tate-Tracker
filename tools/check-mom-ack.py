#!/usr/bin/env python3
"""check-mom-ack.py — is the acknowledgment ribbon still true, and did it ship?

The third sibling of check-data-inline.py and check-digest-fresh.py, same
contract: read-only, exit 0 = say nothing, exit 1 = surface it.

WHY THIS EXISTS. Paul's loop has four legs — she gives input → it lands in the
record → **it is reflected back TO HER so she knows she was heard** → she is
asked for more. Leg 3 is the one whose entire purpose is emotional reassurance,
and it was the only leg with no mechanism at all. On 2026-07-26 the ribbon was
found **8 days stale**, still naming the panicle hydrangea, during the exact
week Mom told Paul she doubted whether her answers were any good — while she was
actively contributing moss, a household-systems idea and two Garden Guru
questions. The 7/22 design tied the ribbon's refresh to the fold step; when Paul
corrected that in CLAUDE.md, the correction was still prose. **A principle
without a check is a policy statement, and a policy statement is what stayed
stale for 8 days.**

THE TRICK IS ONE FIELD. `MOM_ACK_DATA.acknowledgedThrough` — the newest input
the ribbon covers. It converts "is the ribbon stale?" from an unanswerable
question into a comparison. (`answeredOn`, the field it replaces, was a date
with no defined meaning and no consumer, which is how it managed to be
simultaneously present and useless.)

WHAT IT CHECKS
  R1 · ack staleness      today − acknowledgedThrough   🟢 ≤3d · 🟡 4–7d · 🔴 >7d
  R2 · uncovered arrivals input newer than the ribbon    any ≥1 surfaces; oldest >72h 🔴
  R3 · specificity        does the ribbon NAME what she actually gave?
                          → printed for Paul's eye, never asserted (see below)
  shipped                 viewer.html committed AND pushed — CLAUDE.md already
                          says shipping means a push, since Pages serves the
                          file. A ribbon written, committed and not pushed is
                          exactly as stale to Mom as one never written.

WHAT IT MUST NOT DO — and does not: write the message, generate a message, or
advance the clock on its own. It computes the TRIGGER and the EVIDENCE; the
human computes the WORDS. R3 is deliberately not automated: a template can only
ever produce "thanks for your feedback," which is worse than silence at the
moment she is doubting herself.

ATTRIBUTION IS NOT ASSERTED. A deviceId is a browser storage bucket, not a
person; Paul shares his phone with Mom; Safari ITP evicts the id. So the output
says "input landed that the ribbon doesn't cover" — never "Mom gave input." If
it was Paul's own test tap, one command clears it:
    python3 tools/check-mom-ack.py --acknowledged-through 2026-07-26T13:04:00Z

OFFLINE: runs the local half (ribbon + push state), says the app channels are
unverified, and exits 0. A session-start check that hard-fails on a bad network
is a check Paul learns to skip, and a skipped check is worth less than none.

Usage:
    python3 tools/check-mom-ack.py                          # the session-start check
    python3 tools/check-mom-ack.py --verbose                # print even when green
    python3 tools/check-mom-ack.py --acknowledged-through TS  # stamp the clock only
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402

GREEN, AMBER, RED = "🟢", "🟡", "🔴"

CHANNEL_LABEL = {
    "feedback": "confirm queue / notes",
    "observations": "field notes",
    "zone-audio": "voice capture",
    "guru": "Garden Guru",
}


def staleness(days):
    """R1 thresholds (user-researcher, 2026-07-26). Ping on AMBER — red means
    it has already failed."""
    if days is None:
        return RED, "unknown"
    if days <= 3:
        return GREEN, f"{days}d"
    if days <= 7:
        return AMBER, f"{days}d"
    return RED, f"{days}d"


def main():
    ap = argparse.ArgumentParser(description="Is Mom's acknowledgment ribbon current, and did it ship?")
    ap.add_argument("--verbose", action="store_true", help="Print the report even when everything is green")
    ap.add_argument("--json", action="store_true",
                    help="Emit the findings as JSON (which RULES fired, not just an exit code) "
                         "so a caller can tell UNREAD apart from STALE.")
    ap.add_argument("--acknowledged-through", metavar="TS", default=None,
                    help="Stamp MOM_ACK_DATA.acknowledgedThrough to this ISO timestamp "
                         "(use when the uncovered input was yours, not hers). Writes the CLOCK only, never the message.")
    ap.add_argument("--days", type=int, default=60, help="How far back to read the channels (default 60)")
    ap.add_argument("--mark-read", metavar="CHANNEL", default=None,
                    help="Attest that you have actually READ a channel through its newest input "
                         "(feedback | observations | zone-audio | guru | zone-describe). "
                         "For channels with no reader tool, your read IS the action.")
    args = ap.parse_args()

    if args.mark_read:
        tok = momlib.resolve_token()
        if not tok:
            print("error: no token.", file=sys.stderr)
            return 2
        st = momlib.latest_mom_input(tok, days=args.days)
        ch = next((c for c in st["channels"] if c["name"] == args.mark_read), None)
        if ch is None:
            print(f"error: unknown channel {args.mark_read!r}. Known: "
                  + ", ".join(c["name"] for c in st["channels"]), file=sys.stderr)
            return 2
        if not ch["latest"]:
            print(f"· {args.mark_read} has no input to read.")
            return 0
        momlib.mark_channel_read(args.mark_read, ch["latest"], by="human attestation")
        print(f"✓ {args.mark_read} marked read through {momlib.et_str(ch['latest'])}")
        return 0

    if args.acknowledged_through:
        ts = args.acknowledged_through
        if momlib.parse_ts(ts) is None:
            print(f"error: {ts!r} is not an ISO-8601 timestamp (try 2026-07-26T13:04:00Z)", file=sys.stderr)
            return 2
        momlib.set_acknowledged_through(ts)
        print(f"✓ acknowledgedThrough = {ts}  ({momlib.et_str(ts)})")
        print("  The MESSAGE is untouched — if it no longer names what she gave, rewrite it by hand.")
        print("  Then COMMIT AND PUSH: Pages serves viewer.html, so a commit alone never reaches her.")
        return 0

    ribbon = momlib.ribbon_state()
    if not ribbon["found"]:
        print("⚠️  MOM_ACK_DATA not found in viewer.html — the ribbon can't be checked.", file=sys.stderr)
        return 1
    # An ack block that parses but renders NOTHING is the failure that killed the
    # whole card on 2026-08-04 while every check stayed green. Guard the invariant.
    if not ribbon["rendered_text"].strip():
        print("⚠️  MOM_ACK_DATA renders NO TEXT — message, changes[] and closing are all empty.",
              file=sys.stderr)
        print("    The acknowledgment card is blank on her screen. This is not a stale ribbon;",
              file=sys.stderr)
        print("    it is an absent one.", file=sys.stderr)
        return 1

    ack = ribbon["acknowledged_through"]
    problems = []

    # ---- the local half (works offline) ----
    if not ribbon["shipped"]:
        problems.append(("NOT SHIPPED", "; ".join(ribbon["not_shipped_why"])))

    if not ack:
        legacy = ribbon["legacy_answered_on"]
        problems.append((
            "NO CLOCK",
            "MOM_ACK_DATA has no `acknowledgedThrough`, so staleness is unanswerable"
            + (f" (legacy answeredOn: {legacy})" if legacy else "")))

    # ---- the app-channel half (needs the Worker) ----
    token = momlib.resolve_token()
    state, offline = None, False
    if not token:
        offline = True
    else:
        state = momlib.latest_mom_input(token, days=args.days)
        if state["errors"] and not any(c["latest"] for c in state["channels"]):
            offline = True

    uncovered = []
    newest = None
    if state and not offline:
        newest = state["latest"]
        uncovered = momlib.channels_since(state, ack)

    # ⭐ A channel nobody has READ cannot be green, whatever the ribbon says.
    # On 2026-07-26 this check reported ALL GREEN while five zone recordings sat
    # unlistened and fourteen Guru conversations unread — because the ribbon's
    # clock is cleared by stamping a timestamp, which is not the act of reading
    # anything. A detection mechanism must be clearable only by the action it is
    # detecting the absence of.
    unread = momlib.unread_channels(state) if (state and not offline) else []
    if unread:
        problems.append(("UNREAD", f"{len(unread)} channel(s) hold input nothing has read"))

    if newest and ack and newest > ack:
        oldest_uncovered = min((c["latest"] for c in uncovered), default=newest)
        age_h = None
        d = momlib.parse_ts(oldest_uncovered)
        if d:
            age_h = int((dt.datetime.now(dt.timezone.utc) - d).total_seconds() // 3600)
        problems.append((
            "STALE",
            f"input landed that the ribbon doesn't cover (oldest uncovered "
            f"{age_h}h ago)" if age_h is not None else "input landed that the ribbon doesn't cover"))

    # ---- machine-readable, for the board ----
    #
    # ⭐ WHY THIS EXISTS (2026-08-12). `mom-cycle-status.py` used to derive "the
    # return leg is owed" from this tool's EXIT CODE, which is 1 for any problem —
    # so R2b UNREAD ("nobody has looked at what landed") and STALE ("the ribbon is
    # behind her") rendered as the same 🔴 at the same leg. They are different
    # states with different costs: one is a five-minute read, the other is a Mom-
    # facing card at Paul's gate. A caller that cannot tell them apart has to
    # collapse them, so the discrimination has to live HERE.
    if args.json:
        print(json.dumps({
            "problems": [k for k, _ in problems],
            "detail": {k: v for k, v in problems},
            "offline": offline,
            "acknowledged_through": ack,
            "newest_input": newest,
            "unread": [u["name"] for u in unread],
            "uncovered": [c["name"] for c in uncovered],
            "shipped": ribbon["shipped"],
        }, indent=2, ensure_ascii=False))
        return 1 if problems else 0

    # ---- report ----
    if not problems and not args.verbose:
        return 0

    if problems:
        print("🎗  Mom's acknowledgment ribbon needs you.\n")
    else:
        print("🎗  Mom's acknowledgment ribbon — all green.\n")

    days = momlib.days_since(ack) if ack else None
    dot, age = staleness(days) if ack else (RED, "no clock")
    print(f"  R1 ack staleness      {dot} {age}")
    print(f"     ribbon covers through : {momlib.et_str(ack) if ack else '(no acknowledgedThrough field)'}")
    if offline:
        print(f"     newest input          : (couldn't reach the Worker — app channels unverified)")
    else:
        print(f"     newest input          : {momlib.et_str(newest) if newest else '(none in range)'}")

    if not offline and state:
        n = len(uncovered)
        dot2 = GREEN if n == 0 else RED
        if n and uncovered:
            oldest = min(c["latest"] for c in uncovered)
            hrs = momlib.days_since(oldest)
            dot2 = RED if (hrs is not None and hrs * 24 > 72) else AMBER
        unread_names = {c["name"] for c in unread}
        print(f"\n  R2 uncovered arrivals {dot2} {n} channel(s) with input past the ribbon")
        print(f"     {'':2s} {'channel':22s} {'newest input':22s} {'read through':22s}")
        for c in state["channels"]:
            mark = "›" if c in uncovered else " "
            label = CHANNEL_LABEL.get(c["name"], c["name"])
            when = momlib.et_str(c["latest"]) if c["latest"] else "—"
            rt = next((u.get("readThrough") for u in unread if u["name"] == c["name"]), "")
            if c["name"] in unread_names:
                read_col = (momlib.et_str(rt) if rt else "NEVER READ") + "  ⚠️"
            else:
                read_col = "up to date" if c["latest"] else "—"
            print(f"     {mark} {label:22s} {when:22s} {read_col}")
        if state["errors"]:
            print(f"     ⚠️  couldn't read: {', '.join(state['errors'])}")
        if unread:
            print(f"\n  R2b UNREAD            🔴 nothing has actually read: "
                  + ", ".join(u["name"] for u in unread))
            print( "     The ribbon's clock is cleared by a stamp; that is not the act of reading.")
            print( "     Read it, then attest:  python3 tools/check-mom-ack.py --mark-read <channel>")
            # CORRECTED 2026-07-29. This line used to claim "read-mom-feedback.py and
            # read-mom-zone-audio.py mark their own channel." Only the first one does —
            # read-mom-zone-audio.py never calls mark_channel_read and holds no momlib
            # reference at all, so anyone trusting this line believed the zone-audio
            # channel was self-attesting when nothing was reading it. Same failure class
            # this repo keeps re-learning: prose asserting another file's behaviour with
            # nothing checking the assertion.
            print( "     (read-mom-feedback.py marks its own channel. read-mom-zone-audio.py")
            print( "      does NOT — attest zone-audio by hand after you have listened.)")

    if token and not offline:
        receipts = momlib.ack_receipts(token, days=args.days)
        if receipts:
            newest_r = max(r["ts"] for r in receipts if r["ts"])
            print(f"\n  RECEIPT               {GREEN} she tapped \"Got it\" — {momlib.et_str(newest_r)}"
                  f"  ({len(receipts)} total)")
            print("     The first hard evidence an acknowledgment ever REACHED her.")
            print("     Not proof she felt heard — nothing can be — but an act, not exposure.")
        else:
            print("\n  RECEIPT               ⚪ no \"Got it\" tap recorded yet")
            print("     momack_shown is exposure, not reading. Until she taps, delivery is unmeasured.")

    print(f"\n  R3 specificity        — NOT machine-checkable; read it yourself:")
    # Print what she would actually READ. Until 2026-08-08 this printed
    # `message` alone, which the 08-04 changes[] migration had left permanently
    # empty — so the check displayed "" and nobody could tell blind from clean.
    if ribbon["message"]:
        print(f"     {ribbon['message']}")
    for c in ribbon["changes"]:
        tgt = (c or {}).get("card")
        print(f"     · {(c or {}).get('text','')}" + (f"   → [{tgt}]" if tgt else ""))
    if ribbon["closing"]:
        print(f"     {ribbon['closing']}")
    print(f"     Does that name what she actually GAVE? A generic thank-you does not tell her")
    print(f"     she was heard. Adopt her words; never improve them.")

    print(f"\n  shipped               {GREEN if ribbon['shipped'] else RED} "
          + ("committed and pushed" if ribbon["shipped"] else "; ".join(ribbon["not_shipped_why"])))

    if problems:
        print("\n  ↳ What to do:")
        print("     1. Name what she actually gave — her words — in MOM_ACK_DATA.message")
        print("     2. Set MOM_ACK_DATA.acknowledgedThrough to the newest input it covers")
        print("     3. COMMIT AND PUSH (Pages serves viewer.html; a commit alone never reaches her)")
        print("     · Vary the close — never repeat the same closing phrase two refreshes running.")
        if newest and ack and newest > ack:
            # ⚠️ This used to suggest the GLOBAL newest timestamp, which is a
            # cross-channel mute: stamp your own 1:48pm test tap and her 9:17am
            # Guru question is silently "acknowledged" too. Name what the stamp
            # would swallow, so the mute is never accidental.
            print(f"     · If that input was YOURS, not hers, you can stamp the clock — but")
            print(f"       a stamp covers EVERY channel up to that instant. It would cover:")
            for c in uncovered:
                print(f"         · {CHANNEL_LABEL.get(c['name'], c['name'])} "
                      f"(newest {momlib.et_str(c['latest'])})")
            per_channel = min((c["latest"] for c in uncovered), default=newest)
            if per_channel != newest:
                print(f"       To cover only the OLDEST uncovered one, stamp that instead:")
                print(f"         python3 tools/check-mom-ack.py --acknowledged-through {per_channel}")
            print(f"       To cover all of it:")
            print(f"         python3 tools/check-mom-ack.py --acknowledged-through {newest}")
        print()
        return 1

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
