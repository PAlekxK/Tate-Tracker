#!/usr/bin/env python3
"""Transcribe Mom's staged zone-audio recordings — the CHARACTERIZE middle layer.

Companion to read-mom-zone-audio.py: that tool DOWNLOADS her verbatim recordings
(deterministic, AI-free) into .private/mom-zone-audio/; this one makes a MECHANICAL
MODEL READ of those already-captured files so what she said is searchable and can
feed the (Paul-gated) fold-to-canon step.

THE AI BOUNDARY (load-bearing — [[feedback_no_ai_on_capture]] + the A6 backlog row):
  Transcription is a model read of HER VOICE. It is allowed ONLY as this sanctioned
  off-device seat:
    • off-device  — runs on Paul's machine (whisper.cpp, local), never in the Worker.
    • post-storage — the audio was stored verbatim + AI-free FIRST; this never sits
      on the capture path.
    • Paul-facing — the transcript is written to .private/ (gitignored), NEVER reaches
      Mom's surface and NEVER auto-folds to canon.
    • hypothesis-until-checked — every transcript is stamped [transcript-UNVERIFIED];
      it is inference, not capture, until Paul checks it against the audio. Same rule
      as the Hillyer case's whisper.cpp characterize step (Discipline #5).

Deterministic otherwise: same file in → same transcript out; re-runs skip files already
transcribed unless --force.

Usage:
  python3 tools/transcribe-mom-zone-audio.py            # transcribe any new staged files
  python3 tools/transcribe-mom-zone-audio.py --force    # re-transcribe all
  python3 tools/transcribe-mom-zone-audio.py --model <path-to-ggml.bin>
"""
import argparse
import datetime as dt
import os
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(REPO, ".private", "mom-zone-audio")

MODEL_CANDIDATES = [
    os.path.expanduser("~/.local/share/whisper-models/ggml-base.en.bin"),
    os.path.expanduser("~/LocalProjects/hillyer-case/_intake/2026-06-27_batch38_imessage/_audio/models/ggml-base.en.bin"),
]


def find_model(override):
    if override:
        return override if os.path.isfile(override) else None
    for p in MODEL_CANDIDATES:
        if os.path.isfile(p):
            return p
    return None


def which(binary):
    from shutil import which as _w
    return _w(binary)


def transcribe_one(webm, model, tmpdir):
    """webm -> 16k mono wav -> whisper-cli -> plain text (stripped). None on failure."""
    wav = os.path.join(tmpdir, "clip.wav")
    r = subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", webm, "-ar", "16000", "-ac", "1", wav],
        capture_output=True, text=True,
    )
    if r.returncode != 0 or not os.path.isfile(wav):
        return None, "ffmpeg: " + (r.stderr.strip() or "convert failed")
    r = subprocess.run(
        ["whisper-cli", "-m", model, "-f", wav, "-nt", "-np"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return None, "whisper: " + (r.stderr.strip() or "transcribe failed")
    return r.stdout.strip(), None


def zone_and_date(basename):
    # <date>__<zone>__<id>.webm
    parts = basename[:-5].split("__")
    date = parts[0] if len(parts) > 0 else "?"
    zone = parts[1].replace("-", " ").title() if len(parts) > 1 else "?"
    return zone, date


def main():
    ap = argparse.ArgumentParser(description="Transcribe staged zone-audio (off-device, UNVERIFIED).")
    ap.add_argument("--model", help="path to a whisper.cpp ggml model (.bin)")
    ap.add_argument("--force", action="store_true", help="re-transcribe files that already have a transcript")
    args = ap.parse_args()

    if not which("ffmpeg") or not which("whisper-cli"):
        sys.exit("need `ffmpeg` and `whisper-cli` on PATH (brew install ffmpeg whisper-cpp).")
    model = find_model(args.model)
    if not model:
        sys.exit("no whisper model found. Pass --model <ggml.bin> or place one at "
                 "~/.local/share/whisper-models/ggml-base.en.bin.")
    if not os.path.isdir(AUDIO_DIR):
        sys.exit("no staged audio at " + AUDIO_DIR + " — run read-mom-zone-audio.py first.")

    webms = sorted(f for f in os.listdir(AUDIO_DIR) if f.endswith(".webm"))
    if not webms:
        print("No staged recordings. Run read-mom-zone-audio.py first.")
        return

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    did, skipped, empty, failed = 0, 0, 0, 0
    print("🎤→📝 Transcribing staged zone-audio (model: " + os.path.basename(model) + ")\n")
    with tempfile.TemporaryDirectory() as tmp:
        for w in webms:
            src = os.path.join(AUDIO_DIR, w)
            out = os.path.join(AUDIO_DIR, w[:-5] + ".transcript.txt")
            zone, date = zone_and_date(w)
            if os.path.getsize(src) == 0:
                print(f"  ∅ {zone} ({date}) — empty recording, skipped")
                empty += 1
                continue
            if os.path.isfile(out) and not args.force:
                print(f"  ⏭  {zone} ({date}) — already transcribed")
                skipped += 1
                continue
            text, err = transcribe_one(src, model, tmp)
            if err:
                print(f"  ✗ {zone} ({date}) — {err}")
                failed += 1
                continue
            header = (
                "[transcript-UNVERIFIED] — a MODEL READ of Mom's voice, not her verbatim words.\n"
                "Inference until Paul checks it against the audio; never auto-folds to canon; never reaches Mom.\n"
                f"zone: {zone}  ·  recorded: {date}  ·  transcribed: {stamp} (whisper.cpp {os.path.basename(model)})\n"
                f"source audio: {w}\n"
                + "-" * 72 + "\n"
            )
            with open(out, "w", encoding="utf-8") as f:
                f.write(header + (text or "(no speech detected)") + "\n")
            preview = (text or "(no speech detected)").replace("\n", " ")[:80]
            print(f"  ✓ {zone} ({date}) → {os.path.basename(out)}\n      “{preview}”")
            did += 1

    print(f"\nDone: {did} transcribed, {skipped} already-done, {empty} empty, {failed} failed.")
    print("Transcripts are in .private/mom-zone-audio/ (gitignored, UNVERIFIED — check against the audio before folding).")


if __name__ == "__main__":
    main()
