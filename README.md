📌 Task_06_Deep_Fake
🎯 Objective

This project is part of the SU OPT Research sequence.
The goal of Task 06 is to document attempts at producing a "deep fake" or "AI street interview" using prior LLM work, focusing more on the process, workflow, and documentation rather than on the final polished product.

🗣️ Project Theme

AI Street Interview: Syracuse Men’s Lacrosse 2013
Topic chosen from prior LLM work: a recap of the 2013 Syracuse Men’s Lacrosse season and outlook for the following year.
The interview is scripted as a back-and-forth between an Interviewer and a Guest, capturing the feel of a campus street interview.

🗂️ Folder Structure
Task_06_Deep_Fake/
├── data/
│   └── interview.txt          # Final script (plain text)
├── output/
│   ├── interview_audio.aiff   # Main deliverable (AIFF audio file)
│   └── interview_audio.wav    # (Optional) WAV conversion for compatibility
├── scripts/                   # (Optional) Helper scripts
├── README.md                  # Documentation (this file)

⚙️ Methodology / Workflow
1. Script Preparation

Wrote the interview script in data/interview.txt (9 segments: interviewer + guest).

Content is based on Syracuse Men’s Lacrosse 2013 recap and adjustments for future seasons.

2. Audio Generation

Used macOS built-in say command (offline, no dependencies):

say -v Alex -o output/interview_audio.aiff -f data/interview.txt


-v Alex: chooses the Alex voice (male US voice).

Alternative: -v Samantha for a female voice.

-o: output file path.

-f: read script directly from a text file.

3. Optional WAV Conversion

Converted AIFF → WAV for cross-platform compatibility:

afconvert -f WAVE -d LEI16 output/interview_audio.aiff output/interview_audio.wav

4. Playback / Verification

Checked audio locally with:

afplay output/interview_audio.aiff

✅ Deliverables

Primary Audio File → output/interview_audio.aiff

Optional Conversion → output/interview_audio.wav

Both files contain a continuous narrated interview generated via TTS.

📊 Process Log (Required Documentation)

Initial Attempt → Tried Python-based edge-tts (failed due to SSL / 403 handshake errors).

Next Attempt → Tried pyttsx3 with pydub/aifc (incompatible compressed AIFF-C output).

Final Working Solution → Simplified to macOS native say tool → produced stable, offline audio.

Key Decision → Focused on documenting workflow, errors, and fixes as required by assignment.

Time Log:

30m troubleshooting Python libraries

10m preparing interview script

5m generating audio with say

5m documenting process

≈ 50 minutes total

🔒 Ethics & Notes

Voices are synthetic and AI-generated.

Interview content is fictional; no impersonation of real individuals.

Clearly labeled as part of a research task.

Goal was to explore workflow and feasibility, not production of deceptive media.

🚀 How to Reproduce

On macOS, open Terminal in project root.

Run:

say -v Alex -o output/interview_audio.aiff -f data/interview.txt
afplay output/interview_audio.aiff


(Optional) Convert to WAV:

afconvert -f WAVE -d LEI16 output/interview_audio.aiff output/interview_audio.wav



