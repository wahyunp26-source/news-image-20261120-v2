#!/usr/bin/env python3
"""Build the news-image-20261120 v2 entry page (1024x1024, JPEG).

Build-time only (Pillow). Composes entry.png from assets/ in the classic
newspaper front-page layout: kicker + huge serif date headline, stats strip,
region tabs, 3 big features, 10 medium stories, world map with pins,
23 more briefs, DATE CHECK strip, footer.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

W, H = 1024, 1024
PAPER = (247, 241, 222)   # cream paper
INK = (28, 28, 28)
RED = (168, 35, 42)       # brick red
NAVY = (30, 58, 95)
PANEL = (22, 40, 63)      # dark navy map panel
TEAL = (42, 122, 122)
OCHRE = (181, 126, 30)
GREEN = (46, 125, 50)
PURPLE = (106, 76, 147)
GRAY = (107, 101, 88)
RULE = (216, 207, 184)    # light divider

FONT_DIR = "/usr/share/fonts/truetype/liberation"


def font(name, size):
    path = os.path.join(FONT_DIR, name)
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)


SERIF = "LiberationSerif-Regular.ttf"
SERIF_B = "LiberationSerif-Bold.ttf"
SERIF_I = "LiberationSerif-Italic.ttf"
SANS = "LiberationSans-Regular.ttf"
SANS_B = "LiberationSans-Bold.ttf"


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels; returns list of lines."""
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


def draw_tracked(draw, cx, y, text, fnt, fill, tracking=2):
    """Draw text centered on cx with letter tracking."""
    widths = [draw.textlength(c, font=fnt) for c in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + tracking
    return total


def crop_to(im, tw, th):
    """Center-crop image to target aspect, then resize to (tw, th)."""
    sw, sh = im.size
    target = tw / th
    src = sw / sh
    if src > target:  # too wide: crop width
        nw = int(sh * target)
        x0 = (sw - nw) // 2
        im = im.crop((x0, 0, x0 + nw, sh))
    else:  # too tall: crop height
        nh = int(sw / target)
        y0 = (sh - nh) // 2
        im = im.crop((0, y0, sw, y0 + nh))
    return im.resize((tw, th), Image.LANCZOS)


def load(name):
    return Image.open(os.path.join(ASSETS, name)).convert("RGB")


# ---------------------------------------------------------------- content
STATS = [
    ("300,000+", "evacuated ahead of Cyclone Akvan"),
    ("3", "Kyiv bridges hit in missile wave"),
    ("-4.1%", "Nikkei, Asia's worst week since 2020"),
    ("2.3%", "Japan Oct headline CPI; BoJ eyed"),
    ("118", "Phillips' historic century vs India"),
    ("250,000", "landmines destroyed in Zimbabwe"),
]

REGIONS = [
    ("EUROPE", 9, NAVY),
    ("AMERICAS", 9, RED),
    ("ASIA-PACIFIC", 6, TEAL),
    ("MIDEAST", 4, OCHRE),
    ("AFRICA", 3, GREEN),
    ("OCEANIA", 3, PURPLE),
    ("WORLD / SPACE", 2, (85, 85, 85)),
]

BIG = [
    dict(n=1, img="f01.jpg", band_l="LANDFALL \u00b7 GUSTS 110 KM/H",
         band_r="CYCLONE AKVAN",
         kicker="01 \u00b7 ODISHA, INDIA \u00b7 CYCLONE",
         headline="Cyclone Akvan makes landfall in eastern India",
         caption="Severe storm crosses near Gopalpur; 300,000+ evacuated, "
                 "winds 90\u2013100 gusting 110 km/h, 423 rescue teams "
                 "deployed, schools shut. (IMD, Reuters)"),
    dict(n=2, img="f02.jpg", band_l="01:25 LOCAL \u00b7 7 WAVES",
         band_r="~30 MISSILES",
         kicker="02 \u00b7 KYIV, UKRAINE \u00b7 WAR",
         headline="Russia fires wave of ~30 ballistic missiles at Kyiv",
         caption="Seven overnight waves hit energy and transport sites; "
                 "fires burn in three districts; Dutch and Austrian "
                 "embassies damaged. (Kyiv Post, Reuters)"),
    dict(n=3, img="f03.jpg", band_l="UN CLIMATE SUMMIT",
         band_r="$120BN FINANCE GAP",
         kicker="03 \u00b7 ANTALYA, T\u00dcRK\u0130YE \u00b7 CLIMATE",
         headline="COP31 reaches its final day deadlocked",
         caption="Closing draft omits fossil-fuel phase-out while $120bn "
                 "adaptation finance stays unresolved; hosts push "
                 "\u201c35 by 35\u201d clean-power goal. (UN News, Reuters)"),
]

MED = [
    dict(n=4, img="f04.jpg", badge="ASIA -7% WK", bc=RED,
         kicker="04 \u00b7 SEOUL/TOKYO \u00b7 MARKETS",
         headline="AI sell-off sinks Asia to worst week since 2020",
         caption="Nikkei -4.1%, KOSPI -4.7%, SoftBank -16%, MSCI "
                 "Asia-Pacific down 7%. (Reuters)"),
    dict(n=5, img="f05.jpg", badge="2% TARGET", bc=NAVY,
         kicker="05 \u00b7 TOKYO \u00b7 ECONOMY",
         headline="Japan inflation hits 2.3%; BoJ hike eyed",
         caption="Oct headline CPI rises from 2.1%; core stays above 2% "
                 "for second month. (Reuters)"),
    dict(n=6, img="f06.jpg", badge="118 \u00b7 RECORD", bc=RED,
         kicker="06 \u00b7 WELLINGTON \u00b7 CRICKET",
         headline="Phillips makes history with 118 vs India",
         caption="First NZ batter with centuries in all 3 formats vs "
                 "India in a year: NZ 368. (ICC, AP)"),
    dict(n=7, img="f07.jpg", badge="WET \u00b7 FP2", bc=NAVY,
         kicker="07 \u00b7 LAS VEGAS \u00b7 FORMULA 1",
         headline="Russell fastest in wet Las Vegas GP practice",
         caption="Wet FP2: Russell 1:47.272, FP1 washed out. "
                 "(formula1.com)"),
    dict(n=8, img="f08.jpg", badge="XINGU", bc=NAVY,
         kicker="08 \u00b7 BRAZIL \u00b7 INDIGENOUS",
         headline="Raoni's land recognised",
         caption="Brazil recognises Chief Raoni's ancestral land. "
                 "(Brazil govt)"),
    dict(n=9, img="f09.jpg", badge="4 DEAD", bc=RED,
         kicker="09 \u00b7 MALATYA, T\u00dcRK\u0130YE \u00b7 CRASH",
         headline="Turkey helicopter crash kills 4",
         caption="Military helicopter crashes in Malatya, 4 dead. "
                 "(Turkish media)"),
    dict(n=10, img="f10.jpg", badge="1,000+ DRONES", bc=NAVY,
         kicker="10 \u00b7 LONDON \u00b7 UKRAINE AID",
         headline="UK pledges 1,000+ drones for Kyiv",
         caption="London pledges 1,000+ drones, \u00a3280m for Kyiv. "
                 "(UK govt)"),
    dict(n=11, img="f11.jpg", badge="YELLOW LINE", bc=OCHRE,
         kicker="11 \u00b7 GAZA \u00b7 WAR",
         headline="Gaza Yellow Line crossed",
         caption="Israeli forces cross the Yellow Line in Gaza. "
                 "(News wires)"),
    dict(n=12, img="f12.jpg", badge="6BN MILES", bc=NAVY,
         kicker="12 \u00b7 MERCURY \u00b7 SPACE",
         headline="BepiColombo reaches Mercury",
         caption="ESA/JAXA probe ends 6bn-mile trip; orbit insertion set "
                 "for Saturday. (ESA, BBC)"),
    dict(n=13, img="f13.jpg", badge="250,000", bc=NAVY,
         kicker="13 \u00b7 ZIMBABWE \u00b7 LANDMINES",
         headline="250,000 landmines destroyed",
         caption="HALO Trust destroys 250,000 landmines. (HALO Trust)"),
]

BRIEFS = [
    (14, "SUDAN", "Mine strike kills dozens", "Reuters"),
    (15, "VENEZUELA", "US deal averts oil sanctions", "Reuters"),
    (16, "YEMEN", "al-Dahi mosque fire kills worshippers", "Al Jazeera"),
    (17, "BANGLADESH", "Violence flares after verdict", "Reuters"),
    (18, "IRAQ", "Baghdad orders militia to disarm", "AP"),
    (19, "NORTH KOREA", "IAEA flags uranium enrichment", "Reuters"),
    (20, "BRAZIL", "Central bank injects $1bn to steady real", "Reuters"),
    (21, "SPAIN", "Snap-vote campaign heats up", "AFP"),
    (22, "FRANCE", "Italy beats France 3-1 in Paris", "AP"),
    (23, "MUSIC", "Rosal\u00eda sweeps Latin Grammys", "AP"),
    (24, "FOOTBALL", "Scaloni to coach Argentina to 2030", "AP"),
    (25, "TURIN", "Alcaraz, Sinner reach ATP Finals", "AP"),
    (26, "PACIFIC", "Cyclone Xavier strengthens", "Reuters"),
    (27, "UAE", "Fujairah crash shuts highway", "AP"),
    (28, "CHINA", "PBOC holds key rate steady", "Reuters"),
    (29, "USA", "Reporters told to bag phones at briefing", "AP"),
    (30, "MALAWI", "Fuel crisis deepens", "Reuters"),
    (31, "ISRAEL", "Czech leaders visit Jerusalem", "AFP"),
    (32, "USA", "Sanctions hit Comancheros, 'Ndrangheta", "Reuters"),
    (33, "GLOBAL", "Youth strike spans 25+ nations", "AP"),
    (34, "POLAND", "$50bn nuclear deal signed", "Reuters"),
    (35, "TECH", "Meta revises 2030 climate goal", "Reuters"),
    (36, "AUSTRALIA", "Terror-law overhaul urged", "AFP"),
]

def draw_tracked_left(draw, x, y, text, fnt, fill, tracking=2):
    """Draw text left-aligned from x with letter tracking."""
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x


# pin number -> (x, y) on the page (map image at x 24..344, y 712..872).
# Calibrated by eye against the generated map's landmasses; the
# Europe/Mideast cluster is spread a few px so the pins stay readable.
PINS = {
    1: (245, 786), 2: (186, 748), 3: (184, 770), 4: (292, 764),
    5: (310, 772), 6: (321, 831), 7: (71, 772), 8: (124, 809),
    9: (196, 758), 10: (171, 753), 11: (200, 776), 13: (203, 819),
}
PIN_KEY = [
    "1 Odisha", "2 Kyiv", "3 Antalya", "4 Seoul/Tokyo", "5 Tokyo",
    "6 Wellington", "7 Las Vegas", "8 Brazil", "9 Malatya", "10 London",
    "11 Gaza", "12 Mercury (space)", "13 Zimbabwe",
]

DATE_CHECK = ("First reported Thursday 19 Nov, so NOT shown as Friday's "
              "news: Trump\u2013Xi\u2013Putin Shenzhen summit itself \u00b7 "
              "ICJ Myanmar Rohingya genocide verdict \u00b7 Houthi missile "
              "hits Riyadh tower \u00b7 US Senate rejects Iran war-powers "
              "bill \u00b7 Denmark Greenland defence deal \u00b7 Microsoft "
              "explains 12 Nov outage.")

# ---------------------------------------------------------------- build
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 16
CW = W - 2 * M  # 992

# --- header
draw_tracked_left(d, M, 10, "THE WORLD IN ONE DAY", font(SANS_B, 13), RED, 2)
d.text((W - M, 12), "FRIDAY'S NEWS \u00b7 ONE PAGE \u00b7 36 STORIES \u00b7 6 CONTINENTS",
       font=font(SANS_B, 10), fill=INK, anchor="ra")
d.text((W // 2, 26), "Friday 20 November 2026", font=font(SERIF_B, 58),
       fill=INK, anchor="ma")
d.text((W // 2, 92),
       "Cyclone Akvan strikes India \u00b7 Ballistic missiles hit Kyiv \u00b7 "
       "COP31 deadlocked on final day \u00b7 Asian AI sell-off",
       font=font(SERIF_I, 15), fill=RED, anchor="ma")
d.rectangle([M, 112, W - M, 114], fill=INK)
d.rectangle([M, 117, W - M, 117], fill=INK)

# --- stats strip (6 cells)
cell = CW / 6
for i, (num, cap) in enumerate(STATS):
    cx = M + cell * i + cell / 2
    d.text((cx, 122), num, font=font(SANS_B, 23), fill=RED, anchor="ma")
    for j, line in enumerate(wrap(d, cap, font(SANS, 9), cell - 16)):
        d.text((cx, 149 + j * 11), line, font=font(SANS, 9), fill=INK,
               anchor="ma")
    if i:
        x = M + cell * i
        d.line([x, 124, x, 168], fill=RULE, width=1)
d.line([M, 174, W - M, 174], fill=RULE, width=1)

# --- region tabs
x = M
y_tab = 180
for name, count, color in REGIONS:
    label = f"{name} {count}"
    f = font(SANS_B, 10)
    tw = d.textlength(label, font=f)
    d.rounded_rectangle([x, y_tab, x + tw + 14, y_tab + 20], radius=9,
                        fill=color)
    d.text((x + 7, y_tab + 10), label, font=f, fill=(255, 255, 255),
           anchor="lm")
    x += tw + 14 + 6
d.text((W - M, y_tab + 10), "ALL STORIES: FRI 20 NOV 2026, ANY TIME ZONE",
       font=font(SANS_B, 9), fill=GRAY, anchor="rm")

# --- 3 big features
col_w, gap = 324, 10
for i, f in enumerate(BIG):
    x0 = M + i * (col_w + gap)
    im = crop_to(load(f["img"]), col_w, 108)
    img.paste(im, (x0, 208))
    # bottom band on the image
    d.rectangle([x0, 208 + 108 - 18, x0 + col_w, 208 + 108], fill=PANEL)
    d.text((x0 + 6, 208 + 108 - 9), f["band_l"], font=font(SANS_B, 9),
           fill=(255, 255, 255), anchor="lm")
    d.text((x0 + col_w - 6, 208 + 108 - 9), f["band_r"],
           font=font(SANS_B, 9), fill=(255, 255, 255), anchor="rm")
    d.text((x0, 320), f["kicker"], font=font(SANS_B, 11), fill=RED)
    hl = wrap(d, f["headline"], font(SERIF_B, 16), col_w)
    for j, line in enumerate(hl[:2]):
        d.text((x0, 334 + j * 18), line, font=font(SERIF_B, 16), fill=INK)
    cap = wrap(d, f["caption"], font(SANS, 10), col_w)
    for j, line in enumerate(cap[:3]):
        d.text((x0, 372 + j * 12), line, font=font(SANS, 10), fill=INK)

# --- 10 medium stories, 2 rows of 5
med_w = (CW - 4 * 8) // 5  # 192
for r in range(2):
    y0 = 415 + r * 134
    for c in range(5):
        f = MED[r * 5 + c]
        x0 = M + c * (med_w + 8)
        im = crop_to(load(f["img"]), med_w, 60)
        img.paste(im, (x0, y0))
        # badge tag, top-left of the image
        bf = font(SANS_B, 8)
        bw = d.textlength(f["badge"], font=bf)
        d.rectangle([x0, y0, x0 + bw + 10, y0 + 13], fill=f["bc"])
        d.text((x0 + 5, y0 + 6), f["badge"], font=bf,
               fill=(255, 255, 255), anchor="lm")
        d.text((x0, y0 + 64), f["kicker"], font=font(SANS_B, 9), fill=RED)
        hl = wrap(d, f["headline"], font(SERIF_B, 12), med_w)
        for j, line in enumerate(hl[:2]):
            d.text((x0, y0 + 76 + j * 14), line, font=font(SERIF_B, 12),
                   fill=INK)
        cap = wrap(d, f["caption"], font(SANS, 9), med_w)
        for j, line in enumerate(cap[:2]):
            d.text((x0, y0 + 106 + j * 11), line, font=font(SANS, 9),
                   fill=INK)

# --- map + briefs headers
d.text((M, 684), "WHERE IT HAPPENED", font=font(SANS_B, 12), fill=INK)
d.text((362, 684), "ALSO ON FRIDAY 20 NOVEMBER \u2014 23 MORE STORIES",
       font=font(SANS_B, 13), fill=INK)
d.text((W - M, 686), "World Briefs (14\u201336)", font=font(SANS, 9),
       fill=GRAY, anchor="ra")
d.line([362, 702, W - M, 702], fill=RULE, width=1)

# --- map panel (dark navy)
d.rectangle([M, 706, 352, 956], fill=PANEL)
m = crop_to(load("map.jpg"), 320, 160)
img.paste(m, (24, 712))
for n, (px, py) in PINS.items():
    d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED,
              outline=(255, 255, 255), width=1)
    d.text((px, py), str(n), font=font(SANS_B, 8), fill=(255, 255, 255),
           anchor="mm")
# pin key, two columns
kf = font(SANS, 9)
for i, label in enumerate(PIN_KEY):
    col = 0 if i < 7 else 1
    row = i if i < 7 else i - 7
    d.text((24 + col * 164, 880 + row * 11), label, font=kf,
           fill=(240, 236, 220))

# --- briefs, two columns
bf = font(SANS, 9)
bbf = font(SANS_B, 9)
for i, (n, loc, text, src) in enumerate(BRIEFS):
    col = 0 if i < 12 else 1
    row = i if i < 12 else i - 12
    x0 = 362 + col * 330
    y0 = 708 + row * 20
    num = f"{n} "
    d.text((x0, y0), num, font=bbf, fill=RED)
    nx = x0 + d.textlength(num, font=bbf)
    head = f"{loc} \u2014 "
    d.text((nx, y0), head, font=bbf, fill=INK)
    tx = nx + d.textlength(head, font=bbf)
    d.text((tx, y0), f"{text} ({src})", font=bf, fill=INK)

# --- DATE CHECK strip
d.rectangle([M, 962, W - M, 992], fill=(242, 221, 210))
d.rectangle([M, 962, 104, 992], fill=RED)
d.text((60, 977), "DATE CHECK", font=font(SANS_B, 11),
       fill=(255, 255, 255), anchor="mm")
dc = wrap(d, DATE_CHECK, font(SANS, 9), W - M - 112 - 8)
for j, line in enumerate(dc[:2]):
    d.text((112, 966 + j * 12), line, font=font(SANS, 9), fill=INK)

# --- footer
d.text((M, 999), "Every story here happened, or was first reported, on "
       "Friday 20 November 2026 in at least one time zone.",
       font=font(SANS, 8), fill=GRAY)
d.text((W - M, 999), "36 STORIES \u00b7 6 CONTINENTS \u00b7 SOURCES: Reuters, "
       "AP, AFP, BBC, IMD, UN News, Al Jazeera, ICC, EU Council, PBOC.",
       font=font(SANS_B, 8), fill=GRAY, anchor="ra")

out = os.path.join(HERE, "entry.png")
img.save(out, "JPEG", quality=88, optimize=True)
print("saved", out, os.path.getsize(out), "bytes")
