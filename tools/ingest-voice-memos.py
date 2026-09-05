#!/usr/bin/env python3
"""ingest-voice-memos.py — transcribe Paul's own Voice Memos, and say which ones nothing has read.

    python3 tools/ingest-voice-memos.py                 # what is missing (reads nothing, writes nothing)
    python3 tools/ingest-voice-memos.py --since 7       # only the last 7 days (default: 3)
    python3 tools/ingest-voice-memos.py --transcribe    # transcribe what has no transcript
    python3 tools/ingest-voice-memos.py --unread        # transcripts NOTHING in the repos cites

WHY THIS EXISTS. On 2026-09-04, eight memos were recorded. Six were transcribed in one manual 14:23
batch — so it caught everything before 14:23 and nothing after — and **three of those six were then
cited by nothing in either repo.** The next day a whole session re-derived the account/property split
and asked an agent to design a prioritization axis, both of which were sitting in his own words from
the day before. Capture depended on someone remembering, and the day it was not remembered nobody
could tell.

⭐ SO THE SECOND HALF IS THE POINT. Transcribing is easy and was never really the gap. `--unread`
answers *did anything ever READ this* — a transcript nothing cites is indistinguishable from one that
was never made, and it is the failure that actually cost something.

⛔ THIS IS PAUL'S OWN VOICE, NOT MOM'S. Her audio has its own path with its own consent rules
(`transcribe-mom-zone-audio.py`); nothing here touches it. Transcripts land in `.private/`
(gitignored) and are a MODEL READ — `[transcript-UNVERIFIED]`, never promoted to canon on their own.
"""
import argparse, datetime as dt, glob, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".private", "voice-memos")
SRC = os.path.expanduser("~/Library/Group Containers/group.com.apple.VoiceMemos.shared")
MODELS = [os.path.expanduser("~/.local/share/whisper-models/ggml-base.en.bin"),
          os.path.expanduser("~/LocalProjects/hillyer-case/_intake/2026-06-27_batch38_imessage/_audio/models/ggml-base.en.bin")]
MIN_SECONDS = 5          # below this it is a pocket tap, not a memo — 2026-09-04 had a 0s one
SEARCH_ROOTS = [ROOT, os.path.join(os.path.dirname(ROOT), "fernwood-private")]


def duration(path):
    try:
        r = subprocess.run(["afinfo", path], capture_output=True, text=True, timeout=30)
        m = re.search(r"estimated duration: ([\d.]+)", r.stdout)
        return float(m.group(1)) if m else 0.0
    except Exception:
        return 0.0


def recordings(since_days):
    cutoff = dt.datetime.now() - dt.timedelta(days=since_days)
    out = []
    for p in glob.glob(os.path.join(SRC, "**", "*.m4a"), recursive=True):
        b = os.path.basename(p)
        m = re.match(r"(\d{8})[ _-](\d{6})", b)
        if not m:
            continue
        try:
            when = dt.datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S")
        except ValueError:
            continue
        if when < cutoff:
            continue
        out.append({"path": p, "when": when,
                    "key": when.strftime("%Y-%m-%d-%H%M"), "dur": duration(p)})
    return sorted(out, key=lambda r: r["when"])


def transcript_for(key):
    hits = glob.glob(os.path.join(OUT, key + "-*.txt"))
    return hits[0] if hits else None


def find_model():
    for m in MODELS:
        if os.path.exists(m):
            return m
    return None


def transcribe(rec, model):
    with tempfile.TemporaryDirectory() as td:
        wav = os.path.join(td, "a.wav")
        if subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", rec["path"],
                           "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", wav],
                          capture_output=True).returncode != 0:
            return None
        r = subprocess.run(["whisper-cli", "-m", model, "-f", wav, "-nt", "-np"],
                           capture_output=True, text=True, timeout=1800)
        return r.stdout.strip() or None


def cited(path):
    """Does ANYTHING in either repo name this transcript? A stem grep, so a rename hides it —
    that is a known limit, stated rather than papered over."""
    stem = os.path.splitext(os.path.basename(path))[0]
    for root in SEARCH_ROOTS:
        if not os.path.isdir(root):
            continue
        r = subprocess.run(["grep", "-rl", "--exclude-dir=.git", "--exclude-dir=node_modules",
                            "--exclude-dir=.private", stem, root], capture_output=True, text=True)
        if r.stdout.strip():
            return r.stdout.strip().splitlines()
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", type=int, default=3, help="days back (default 3)")
    ap.add_argument("--transcribe", action="store_true")
    ap.add_argument("--unread", action="store_true")
    a = ap.parse_args()

    if a.unread:
        rows = sorted(glob.glob(os.path.join(OUT, "*.txt")))
        orphans = [f for f in rows if not cited(f)]
        print("voice memos — %d transcript(s), %d that NOTHING cites\n" % (len(rows), len(orphans)))
        for f in orphans:
            print("  ⛔ read by nothing   %s" % os.path.basename(f))
        if not orphans:
            print("  ✅ every transcript is cited somewhere")
        print("\n  ⚠️  A stem grep. A transcript whose content was folded WITHOUT citing it reads as")
        print("     unread here — the fix is to cite the source, which is the habit this enforces.")
        return 1 if orphans else 0

    recs = recordings(a.since)
    if not recs:
        print("voice memos — nothing recorded in the last %d day(s)" % a.since)
        return 0
    missing = [r for r in recs if r["dur"] >= MIN_SECONDS and not transcript_for(r["key"])]
    print("voice memos — %d recording(s) in the last %d day(s)" % (len(recs), a.since))
    for r in recs:
        t = transcript_for(r["key"])
        mark = "✅" if t else ("·" if r["dur"] < MIN_SECONDS else "⛔")
        note = os.path.basename(t) if t else ("false start, skipped" if r["dur"] < MIN_SECONDS else "NO TRANSCRIPT")
        print("  %s %s  %5.0fs  %s" % (mark, r["key"], r["dur"], note))

    if not missing:
        print("\n✅ every recording over %ds has a transcript" % MIN_SECONDS)
        return 0
    if not a.transcribe:
        print("\n⛔ %d untranscribed. Run with --transcribe." % len(missing))
        return 1

    model = find_model()
    if not model:
        print("\n⛔ no whisper model found; looked in:\n   " + "\n   ".join(MODELS))
        return 2
    os.makedirs(OUT, exist_ok=True)
    for r in missing:
        print("\n  transcribing %s (%.0fs)…" % (r["key"], r["dur"]))
        text = transcribe(r, model)
        if not text:
            print("     ⛔ failed — left alone, not written empty")
            continue
        # the slug is the author's job: a name is a claim about content and this tool does not make one
        dest = os.path.join(OUT, r["key"] + "-untitled.txt")
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
        print("     ✅ %s  ⚠️ rename the -untitled slug to what it is about" % os.path.basename(dest))
    print("\n⚠️  Transcribed is not ingested. Run --unread to see what nothing has read yet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
