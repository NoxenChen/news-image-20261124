#!/usr/bin/env python3
"""Render the 24 November 2026 world-news poster as a 1024x1024 PNG.

Drawn entirely with PIL shapes and text -- no downloaded images.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 48
INK = (12, 12, 12)
ACCENT = (178, 34, 34)          # deep red
BLUE = (18, 52, 110)            # deep blue for the lead motif
GREY = (90, 90, 90)
RULE = (200, 200, 200)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, text, fnt, fill=INK):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size + 4


def main():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    y = 28
    # ---- Masthead -------------------------------------------------------
    y = draw_centered(d, y, "THE WORLD IN ONE IMAGE", font(SERIF_B, 56))
    d.rectangle([MARGIN, y + 2, W - MARGIN, y + 7], fill=ACCENT)
    y += 18
    y = draw_centered(d, y, "TUESDAY, 24 NOVEMBER 2026", font(SANS_B, 48),
                      fill=ACCENT)
    d.line([MARGIN, y + 4, W - MARGIN, y + 4], fill=INK, width=3)
    y += 16

    # ---- Lead story -----------------------------------------------------
    motif_x0, motif_y0 = W - MARGIN - 190, y + 14
    motif_x1, motif_y1 = W - MARGIN, motif_y0 + 180
    text_w = motif_x0 - MARGIN - 24

    lead_f = font(SERIF_B, 46)
    ly = y
    for line in wrap(d, "JENSEN HUANG REINSTATED AS NVIDIA CEO",
                     lead_f, text_w):
        d.text((MARGIN, ly), line, font=lead_f, fill=INK)
        ly += 52
    d.rectangle([MARGIN, ly + 2, MARGIN + 120, ly + 7], fill=ACCENT)
    ly += 18
    deck_f = font(SANS, 24)
    deck = ("Board reverses unanimously, 11 days after he stepped "
            "down amid a \u201cspy\u201d row \u2014 after a push "
            "by Trump. Shares surge.")
    for line in wrap(d, deck, deck_f, text_w):
        d.text((MARGIN, ly), line, font=deck_f, fill=INK)
        ly += 30

    # Motif: chip outline with a rising arrow chart inside
    d.rectangle([motif_x0, motif_y0, motif_x1, motif_y1], outline=BLUE, width=4)
    for i in range(5):  # pins top / bottom
        px = motif_x0 + 26 + i * 34
        d.line([px, motif_y0 - 12, px, motif_y0], fill=BLUE, width=4)
        d.line([px, motif_y1, px, motif_y1 + 12], fill=BLUE, width=4)
    for i in range(4):  # pins left / right
        py = motif_y0 + 34 + i * 42
        d.line([motif_x0 - 12, py, motif_x0, py], fill=BLUE, width=4)
        d.line([motif_x1, py, motif_x1 + 12, py], fill=BLUE, width=4)
    d.rectangle([motif_x0 + 30, motif_y0 + 30, motif_x1 - 30, motif_y1 - 30],
                outline=BLUE, width=3)
    d.text((motif_x0 + 52, motif_y0 + 40), "NVDA", font=font(SANS_B, 28),
           fill=BLUE)
    pts = [(motif_x0 + 42, motif_y1 - 52), (motif_x0 + 76, motif_y1 - 76),
           (motif_x0 + 104, motif_y1 - 64), (motif_x0 + 136, motif_y1 - 94),
           (motif_x0 + 160, motif_y1 - 86)]
    d.line(pts, fill=ACCENT, width=5, joint="curve")
    ax, ay = pts[-1]
    d.polygon([(ax, ay - 16), (ax + 18, ay + 2), (ax - 2, ay + 10)],
              fill=ACCENT)

    y = max(ly, motif_y1 + 12) + 8
    d.line([MARGIN, y, W - MARGIN, y], fill=RULE, width=2)
    y += 14

    # ---- Stories 2-6 ----------------------------------------------------
    stories = [
        ("COP31 TALKS COLLAPSE IN ANTALYA",
         "Climate summit ends with no deal; final text drops fossil-fuel phase-out."),
        ("DEMOCRATS WIN BIGGEST HOUSE MAJORITY IN DECADES",
         "2026 midterms hand Democrats their largest House majority in decades."),
        ("AT LEAST 14 KILLED IN RUSSIAN STRIKES ON KYIV REGION",
         "Ukraine says it sank a Russian warship in a sea-drone attack off Libya."),
        ("NATO VOWS SPACE DEFENCE",
         "Allies warn Russia may launch a nuclear space weapon next month."),
        ("SWISS FOREIGN MINISTER CASSIS IN CHINA",
         "Fifth round of China\u2013Switzerland foreign-minister strategic dialogue."),
    ]
    head_f = font(SERIF_B, 40)
    deck2_f = font(SANS, 24)
    num_f = font(SANS_B, 40)
    for i, (head, deck) in enumerate(stories, start=2):
        d.text((MARGIN, y), str(i), font=num_f, fill=ACCENT)
        tx = MARGIN + 52
        tw = W - MARGIN - tx
        hy = y
        for line in wrap(d, head, head_f, tw):
            d.text((tx, hy), line, font=head_f, fill=INK)
            hy += 45
        for line in wrap(d, deck, deck2_f, tw):
            d.text((tx, hy), line, font=deck2_f, fill=GREY)
            hy += 29
        y = hy + 6
        if i < 6:
            d.line([MARGIN, y - 4, W - MARGIN, y - 4], fill=RULE, width=1)

    # ---- Footer ---------------------------------------------------------
    d.line([MARGIN, H - 62, W - MARGIN, H - 62], fill=INK, width=2)
    draw_centered(d, H - 50, "24 November 2026  \u00b7  World news in one image",
                  font(SANS, 24), fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
