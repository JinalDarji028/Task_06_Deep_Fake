"""
Create a simple static-card video and attach the generated audio.
This avoids ImageMagick by drawing text with Pillow (PIL).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip
import argparse

OUT_DIR = Path("output")
AUDIO = OUT_DIR / "interview_audio.mp3"

def make_poster(title: str, subtitle: str, outfile: Path, size=(1280, 720)):
    W, H = size
    img = Image.new("RGB", size, color=(24, 24, 28))
    draw = ImageDraw.Draw(img)

    # Try default system fonts; fallback to PIL's
    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 64)
        subtitle_font = ImageFont.truetype("DejaVuSans.ttf", 36)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    # Title
    tw, th = draw.textsize(title, font=title_font)
    draw.text(((W - tw)//2, H//2 - th - 20), title, fill=(255,255,255), font=title_font)

    # Subtitle
    sw, sh = draw.textsize(subtitle, font=subtitle_font)
    draw.text(((W - sw)//2, H//2 + 10), subtitle, fill=(200,200,200), font=subtitle_font)

    # Footer
    footer = "AI-Generated Interview • For research only"
    fw, fh = draw.textsize(footer, font=subtitle_font)
    draw.text(((W - fw)//2, H - fh - 40), footer, fill=(160,160,160), font=subtitle_font)

    img.save(outfile)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", default="AI Street Interview")
    parser.add_argument("--subtitle", default="Analytics Recap")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    poster = OUT_DIR / "poster.png"
    make_poster(args.title, args.subtitle, poster)

    if not AUDIO.exists():
        raise SystemExit(f"Missing audio file: {AUDIO}. Run generate_audio.py first.")

    audio = AudioFileClip(str(AUDIO))
    img_clip = ImageClip(str(poster)).set_duration(audio.duration)
    video = img_clip.set_audio(audio)
    out_mp4 = OUT_DIR / "interview_video.mp4"
    video.write_videofile(str(out_mp4), fps=30, codec="libx264", audio_codec="aac")
    print(f"Wrote {out_mp4}")

if __name__ == "__main__":
    main()