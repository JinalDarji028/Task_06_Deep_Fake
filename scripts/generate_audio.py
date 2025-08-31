# scripts/generate_audio_mac.py
# Simple macOS-only generator: uses `say` command to synthesize each line
# and stitches into one WAV. No internet, no ffmpeg, no pyttsx3.

import subprocess, shlex
from pathlib import Path
import yaml
import aifc, wave

DATA_YAML = Path("data/interview_script.yaml")
OUT_DIR = Path("output"); OUT_DIR.mkdir(parents=True, exist_ok=True)
SEG_DIR = OUT_DIR / "segments"; SEG_DIR.mkdir(parents=True, exist_ok=True)

def load_script():
    with open(DATA_YAML, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def synth_with_say(text: str, out_aiff: Path, voice: str):
    cmd = f'say -v {shlex.quote(voice)} -o {shlex.quote(str(out_aiff))} --data-format=LEI16@22050 {shlex.quote(text)}'
    subprocess.run(cmd, shell=True, check=True)

def concat_aiff_to_wav(aiff_files, out_wav, gap_ms=250):
    if not aiff_files:
        raise RuntimeError("No segments to stitch.")

    with aifc.open(str(aiff_files[0]), 'r') as a0:
        nch = a0.getnchannels()
        sw  = a0.getsampwidth()
        fr  = a0.getframerate()

    gap_frames = int(fr * (gap_ms / 1000.0))
    silence = b"\x00" * gap_frames * nch * sw

    with wave.open(str(out_wav), 'wb') as out:
        out.setnchannels(nch)
        out.setsampwidth(sw)
        out.setframerate(fr)

        for i, fp in enumerate(aiff_files):
            with aifc.open(str(fp), 'r') as af:
                if (af.getnchannels(), af.getsampwidth(), af.getframerate()) != (nch, sw, fr):
                    raise RuntimeError(f"AIFF params mismatch in {fp}")
                out.writeframes(af.readframes(af.getnframes()))
            if i != len(aiff_files) - 1:
                out.writeframes(silence)

def main():
    script = load_script()
    seg_aiffs = []

    for i, seg in enumerate(script["segments"], start=1):
        voice = seg.get("voice", "Alex")
        text  = seg["text"]
        aiff  = SEG_DIR / f"{i:02d}_{seg['speaker']}.aiff"

        print(f"[say] {i:02d} {seg['speaker']} ({voice}): {text[:60]}...")
        synth_with_say(text, aiff, voice)
        seg_aiffs.append(aiff)

    final_wav = OUT_DIR / "interview_audio.wav"
    concat_aiff_to_wav(seg_aiffs, final_wav, gap_ms=250)
    print(f"\n✅ Wrote {final_wav}")

if __name__ == "__main__":
    main()
