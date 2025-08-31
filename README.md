# Task_06_Deep_Fake

This repo documents my end-to-end workflow to turn a prior LLM narrative into an AI-generated “street interview” (audio-first, with an optional static video). The emphasis is on process documentation: tools tried, prompts, iterations, and results—even if imperfect.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/generate_audio.py
python scripts/make_static_video.py --title "AI Street Interview" --subtitle "Analytics Recap"
```

Deliverable: AI-generated “street interview” audio.

Approach (error-proof, offline):
1) Wrote interview lines in `data/interview.txt`.
2) Generated audio with macOS built-in TTS:
   `say -v Alex -o output/interview_audio.aiff --data-format=LEI16@22050 -f data/interview.txt`
3) (Optional) Converted AIFF→WAV with `afconvert`.

Notes:
- No Python, ffmpeg, or network TTS used; avoids prior environment errors.
- Ethics: Fictional voices; clearly AI-generated; no impersonation.

Output:
- `output/interview_audio.aiff` (and optionally `output/interview_audio.wav`)
