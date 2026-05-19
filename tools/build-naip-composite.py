#!/usr/bin/env python3
"""Stitch the 7 NAIP year captures into a single labeled composite image."""
import glob
import os
from PIL import Image, ImageDraw, ImageFont

NAIP_DIR = "images/property-map/naip"
OUT_PATH = "images/property-map/naip-timelapse-composite.jpg"

# Layout: 2 rows × 4 cols (7 captures + 1 spare cell)
files = sorted(glob.glob(os.path.join(NAIP_DIR, "naip-*.png")))
print(f"Found {len(files)} NAIP captures")
for f in files:
    print(f"  {os.path.basename(f)}")

CELL = 400  # downscale each capture to 400x400 in the composite
LABEL_HEIGHT = 28
COLS = 4
ROWS = 2
PAD = 6

W = COLS * CELL + (COLS + 1) * PAD
H = ROWS * (CELL + LABEL_HEIGHT) + (ROWS + 1) * PAD
print(f"Composite: {W}x{H}")

bg = Image.new("RGB", (W, H), color=(245, 245, 238))
draw = ImageDraw.Draw(bg)

try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman.ttf", 18)
    font_italic = ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf", 14)
except Exception:
    font = ImageFont.load_default()
    font_italic = font

for i, f in enumerate(files):
    r = i // COLS
    c = i % COLS
    x = PAD + c * (CELL + PAD)
    y = PAD + r * (CELL + LABEL_HEIGHT + PAD)

    img = Image.open(f).convert("RGB").resize((CELL, CELL), Image.LANCZOS)
    bg.paste(img, (x, y))

    # Year label below
    date_str = os.path.basename(f).replace("naip-", "").replace(".png", "")
    draw.text((x + 6, y + CELL + 4), date_str, fill=(40, 60, 40), font=font)

# Header
draw.text((PAD + 4, H - 22), "NAIP via Microsoft Planetary Computer · ~1200 ft across · property at center", fill=(100, 110, 90), font=font_italic)

bg.save(OUT_PATH, "JPEG", quality=88, optimize=True)
print(f"\nSaved {OUT_PATH} ({os.path.getsize(OUT_PATH)/1024:.0f} KB)")
