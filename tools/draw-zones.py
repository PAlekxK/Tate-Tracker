#!/usr/bin/env python3
"""
Draw the gardening zones on top of the GEP leaf-off base image as a first-pass
prototype. Polygons are guesses — Paul corrects from there.

Zone definitions use FRACTIONAL coordinates (0-1) of the image so they're easy
to iterate on without re-measuring pixels every time the base image changes.

Output: images/property-map/zones-prototype.jpg
"""
from PIL import Image, ImageDraw, ImageFont

BASE = "images/property-map/gep-2015-03-leafoff.png"
OUT = "images/property-map/zones-prototype.jpg"

# Each zone: id, name, type, polygon (list of (x_frac, y_frac) points), fill color (RGB)
# House is at approximately (0.46, 0.20) in the image (the pin)
# Driveway curves up from lower-left
# Fairway opens to the south and southeast
ZONES = [
    {
        "id": "western-patio",
        "name": "Western patio",
        "type": "planted",
        "color": (200, 100, 220),  # purple
        "polygon": [(0.36, 0.18), (0.42, 0.18), (0.42, 0.26), (0.36, 0.26)],
    },
    {
        "id": "eastern-patio",
        "name": "Eastern patio",
        "type": "planted",
        "color": (240, 130, 80),  # orange
        "polygon": [(0.51, 0.18), (0.57, 0.18), (0.57, 0.26), (0.51, 0.26)],
    },
    {
        "id": "pond-area",
        "name": "Pond area",
        "type": "planted",
        "color": (60, 130, 200),  # blue
        "polygon": [(0.42, 0.27), (0.51, 0.27), (0.51, 0.36), (0.42, 0.36)],
    },
    {
        "id": "front-lawn",
        "name": "Front lawn",
        "type": "turf",
        "color": (90, 200, 110),  # bright green
        "polygon": [(0.34, 0.36), (0.58, 0.36), (0.62, 0.50), (0.30, 0.50)],
    },
    {
        "id": "fairway-meadow",
        "name": "Fairway meadow",
        "type": "meadow",
        "color": (220, 200, 80),  # gold
        "polygon": [(0.25, 0.50), (0.65, 0.50), (0.75, 0.85), (0.20, 0.92)],
    },
    {
        "id": "fairway-edge-west",
        "name": "Western fairway edge",
        "type": "planted",
        "color": (50, 160, 90),  # leaf green
        "polygon": [(0.13, 0.32), (0.25, 0.50), (0.20, 0.92), (0.05, 0.92), (0.05, 0.40)],
    },
    # forest-interior intentionally not drawn — it's a placeholder zone and would
    # cover everything else on the image; we'll list it in the legend instead.
]


def main():
    base = Image.open(BASE).convert("RGBA")
    W, H = base.size

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    try:
        font_label = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 30)
        font_legend = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
        font_legend_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
    except Exception:
        font_label = ImageFont.load_default()
        font_legend = ImageFont.load_default()
        font_legend_bold = ImageFont.load_default()

    # Pass 1: fill polygons
    for z in ZONES:
        pts = [(int(x * W), int(y * H)) for (x, y) in z["polygon"]]
        fill = (*z["color"], 90)
        outline = (*z["color"], 220)
        draw.polygon(pts, fill=fill, outline=outline)

    # Pass 2: stroke polygons more visibly with a thicker line
    for z in ZONES:
        pts = [(int(x * W), int(y * H)) for (x, y) in z["polygon"]]
        outline = (*z["color"], 240)
        # Draw multiple polygon outlines to fake a thicker stroke
        for offset in range(3):
            draw.polygon(pts, outline=outline)

    # Pass 3: labels at centroid with white background pill
    for z in ZONES:
        pts = [(int(x * W), int(y * H)) for (x, y) in z["polygon"]]
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        label = z["name"]
        bbox = draw.textbbox((0, 0), label, font=font_label)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        pad = 8
        # White pill
        draw.rounded_rectangle(
            [cx - tw/2 - pad, cy - th/2 - pad, cx + tw/2 + pad, cy + th/2 + pad],
            radius=10,
            fill=(255, 255, 255, 240),
            outline=(*z["color"], 240),
            width=2,
        )
        draw.text((cx - tw/2 - bbox[0], cy - th/2 - bbox[1]), label, fill=(20, 20, 20, 255), font=font_label)

    # Composite overlay onto base
    out = Image.alpha_composite(base, overlay)

    # Add a legend at the bottom
    legend_h = 130
    final = Image.new("RGB", (W, H + legend_h), color=(245, 245, 238))
    final.paste(out.convert("RGB"), (0, 0))
    legend_draw = ImageDraw.Draw(final)

    # Legend title
    legend_draw.text((20, H + 12), "Zones prototype — first pass (positions are guesses, correct from here)",
                     fill=(60, 70, 50), font=font_legend_bold)

    # Legend chips
    x = 20
    y = H + 50
    chip_w = 30
    chip_h = 18
    gap = 12
    for z in ZONES:
        legend_draw.rectangle([x, y, x + chip_w, y + chip_h], fill=z["color"], outline=(60, 60, 60))
        text = f"{z['name']} ({z['type']})"
        legend_draw.text((x + chip_w + 6, y - 2), text, fill=(30, 30, 30), font=font_legend)
        bbox = legend_draw.textbbox((0, 0), text, font=font_legend)
        x += chip_w + 6 + (bbox[2] - bbox[0]) + gap + 8
        if x > W - 250:
            x = 20
            y += 30

    # forest-interior legend entry (no polygon drawn on map)
    legend_draw.rectangle([x, y, x + chip_w, y + chip_h], fill=(120, 100, 70), outline=(60, 60, 60))
    legend_draw.text((x + chip_w + 6, y - 2), "Forest interior (placeholder)", fill=(30, 30, 30), font=font_legend)

    final.save(OUT, "JPEG", quality=88, optimize=True)
    import os
    print(f"Saved {OUT} ({os.path.getsize(OUT)/1024:.0f} KB) — {W}x{H+legend_h}")


if __name__ == "__main__":
    main()
