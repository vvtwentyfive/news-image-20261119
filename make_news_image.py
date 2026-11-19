#!/usr/bin/env python3
"""Image for make.fun news-image-20261119.
Renders a 1024x1024 front-page-style collage summing up Thursday 19 Nov 2026.
Headlines grounded in web research 20 Nov 2026 (see NEWS-BRIEF.md).
Caveats honoured: Anthropic PRICED 18 Nov, first TRADED 19 Nov ("debuts");
Akvan landfall is 20 Nov noon ("bears down / evacuations under way");
no single number asserted for the Crimean Bridge attack count;
the uncorroborated "Democrats 56-seat Senate" claim is NOT used.
Run: python3 make_news_image.py  -> writes entry.png next to this script.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (245, 239, 227)
INK = (22, 19, 14)
RED = (179, 39, 30)
NAVY = (29, 45, 80)
TEAL = (14, 107, 107)
GOLD = (200, 155, 60)
CARD = (255, 253, 246)
GREY = (90, 84, 72)

FD = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FD + name, size)

F_TITLE = font("DejaVuSerif-Bold.ttf", 56)
F_KICK = font("DejaVuSans-Bold.ttf", 19)
F_HEAD = font("DejaVuSerif-Bold.ttf", 30)
F_HEAD_S = font("DejaVuSerif-Bold.ttf", 27)
F_DECK = font("DejaVuSans.ttf", 20)
F_DECK_S = font("DejaVuSans.ttf", 18)
F_FOOT = font("DejaVuSans.ttf", 15)
F_SUB = font("DejaVuSans-Bold.ttf", 20)
F_BIG = font("DejaVuSerif-Bold.ttf", 34)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(draw, text, fnt, width):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def panel(x, y, w, h, accent):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD,
                        outline=INK, width=2)
    d.rectangle([x, y, x + w, y + 8], fill=accent)

def kicker(x, y, text, color):
    d.text((x, y), text, font=F_KICK, fill=color)

def headline(x, y, text, fnt, width):
    lines = wrap(d, text, fnt, width)
    yy = y
    for ln in lines:
        d.text((x, yy), ln, font=fnt, fill=INK)
        yy += fnt.size + 4
    return yy

def deck(x, y, text, width, fnt=F_DECK):
    lines = wrap(d, text, fnt, width)
    yy = y
    for ln in lines:
        d.text((x, yy), ln, font=fnt, fill=(60, 54, 44))
        yy += fnt.size + 5
    return yy

# ---------- masthead ----------
d.text((36, 26), "THE WORLD IN ONE IMAGE", font=F_TITLE, fill=INK)
d.text((36, 100), "THURSDAY,  19  NOVEMBER  2026", font=F_SUB, fill=RED)
d.text((36, 128), "Six stories that defined the day", font=F_DECK, fill=GREY)
d.line([36, 158, 988, 158], fill=INK, width=3)
d.line([36, 164, 988, 164], fill=INK, width=1)

# ---------- lead: Shenzhen trilateral summit ----------
LX, LY, LW, LH = 36, 178, 952, 220
panel(LX, LY, LW, LH, RED)
kicker(LX + 24, LY + 22, "LEAD  \u00b7  SHENZHEN", RED)
# flag trio, right side (3 small flags, 64x42, inside the panel)
fx, fy, fw, fh = 756, LY + 26, 64, 42
d.rectangle([fx, fy, fx + fw, fy + fh], fill=(222, 41, 16))          # China
d.text((fx + 9, fy + 7), "\u2605", font=font("DejaVuSans-Bold.ttf", 24), fill=(255, 222, 0))
d.rectangle([fx + 74, fy, fx + 74 + fw, fy + fh], fill=(255, 255, 255), outline=INK)  # Russia
d.rectangle([fx + 74, fy + 14, fx + 74 + fw, fy + 28], fill=(0, 57, 166))
d.rectangle([fx + 74, fy + 28, fx + 74 + fw, fy + 42], fill=(213, 0, 50))
d.rectangle([fx + 148, fy, fx + 148 + fw, fy + fh], fill=(255, 255, 255), outline=INK)  # USA
for i in range(5):
    d.rectangle([fx + 148, fy + i * 9, fx + 148 + fw, fy + i * 9 + 4], fill=(178, 34, 52))
d.rectangle([fx + 148, fy, fx + 148 + 30, fy + 23], fill=(60, 59, 110))
d.text((fx + 2, fy + 50), "CN  \u00b7  RU  \u00b7  US", font=font("DejaVuSans-Bold.ttf", 15), fill=GREY)
yy = headline(LX + 24, LY + 52,
              "TRUMP, XI AND PUTIN HOLD FIRST-EVER TRILATERAL SUMMIT",
              F_BIG, 680)
deck(LX + 24, LY + 140,
     "Ninety minutes in Shenzhen on Ukraine, Iran, nukes, trade and AI \u2014 "
     "and a joint declaration pledging UN reform, nuclear-risk dialogue and "
     "more oil, with no breakthrough on any of it.",
     900, F_DECK_S)
d.text((LX + 24, LY + LH - 26),
       "JOINT DECLARATION ISSUED  \u00b7  NO BREAKTHROUGH ON UKRAINE, IRAN OR TRADE",
       font=font("DejaVuSans-Bold.ttf", 15), fill=NAVY)

# ---------- row 1 ----------
RY, RH = 412, 216
# Myanmar / ICJ panel
GX, GW = 36, 466
panel(GX, RY, GW, RH, NAVY)
kicker(GX + 20, RY + 20, "THE HAGUE  \u00b7  WORLD COURT", NAVY)
yy = headline(GX + 20, RY + 48, "WORLD COURT: MYANMAR COMMITTED GENOCIDE",
              F_HEAD_S, GW - 40)
deck(GX + 20, yy + 4,
     "ICJ rules 9\u20136 on the 2017 Rakhine clearance; orders restitution "
     "and reparations.", GW - 40, F_DECK_S)
# scales-of-justice pictogram, bottom-left
bx, by = GX + 20, RY + RH - 48
d.line([bx + 22, by, bx + 22, by + 40], fill=INK, width=3)
d.line([bx, by + 4, bx + 44, by + 4], fill=INK, width=3)
d.line([bx + 2, by + 4, bx + 2, by + 16], fill=INK, width=2)
d.line([bx + 42, by + 4, bx + 42, by + 16], fill=INK, width=2)
d.arc([bx - 8, by + 10, bx + 12, by + 26], 0, 180, fill=INK, width=2)
d.arc([bx + 32, by + 10, bx + 52, by + 26], 0, 180, fill=INK, width=2)
d.line([bx + 12, by + 40, bx + 32, by + 40], fill=INK, width=3)
d.text((bx + 62, by + 10), "9\u20136", font=font("DejaVuSans-Bold.ttf", 28), fill=NAVY)
# Riyadh panel
KX, KW = 522, 466
panel(KX, RY, KW, RH, RED)
kicker(KX + 20, RY + 20, "RIYADH", RED)
yy = headline(KX + 20, RY + 48, "HOUTHI MISSILE HITS RIYADH'S TALLEST TOWER",
              F_HEAD_S, KW - 40)
deck(KX + 20, yy + 4,
     "Windows blown out on seven to eight floors of the 80-storey PIF "
     "Tower; no injuries.", KW - 40, F_DECK_S)
# skyscraper pictogram, bottom-left (tower with cracked top corner)
bx, by = KX + 20, RY + RH - 56
d.rectangle([bx, by, bx + 26, by + 44], fill=NAVY, outline=INK, width=2)
d.polygon([(bx + 26, by), (bx + 26, by + 10), (bx + 16, by + 6)],
          fill=PAPER)
for wy in (by + 8, by + 18, by + 28):
    d.rectangle([bx + 5, wy, bx + 11, wy + 5], fill=GOLD)
    d.rectangle([bx + 15, wy, bx + 21, wy + 5], fill=GOLD)
d.rectangle([bx + 5, by + 38, bx + 11, by + 43], fill=(60, 54, 44))
d.text((bx + 40, by + 10), "80 STOREYS", font=font("DejaVuSans-Bold.ttf", 22), fill=INK)
d.text((bx + 40, by + 34), "PIF TOWER", font=font("DejaVuSans-Bold.ttf", 15), fill=GREY)

# ---------- row 2 ----------
RY2, RH2 = 642, 192
# Anthropic IPO panel
SX, SW = 36, 466
panel(SX, RY2, SW, RH2, TEAL)
kicker(SX + 20, RY2 + 18, "MARKETS  \u00b7  IPO", TEAL)
yy = headline(SX + 20, RY2 + 44, "ANTHROPIC DEBUTS IN RECORD $81.3BN IPO",
              F_HEAD_S, SW - 40)
deck(SX + 20, yy + 4,
     "Priced at $83 a share, the Claude maker debuts on Nasdaq as ANT, "
     "valued near $1.5tn.", SW - 40, F_DECK_S)
# rising-bars pictogram, bottom-left
bx, by = SX + 20, RY2 + RH2 - 30
for i, bh in enumerate((10, 16, 24)):
    d.rectangle([bx + i * 16, by + 26 - bh, bx + i * 16 + 11, by + 26],
                fill=TEAL, outline=INK, width=1)
d.line([bx + 52, by + 2, bx + 66, by + 14], fill=RED, width=3)
d.line([bx + 66, by + 14, bx + 80, by - 2], fill=RED, width=3)
d.polygon([(bx + 80, by - 2), (bx + 72, by - 2), (bx + 80, by + 6)], fill=RED)
d.text((bx + 92, by + 2), "ANT  \u00b7  NASDAQ", font=font("DejaVuSans-Bold.ttf", 15), fill=GREY)
# Cyclone Akvan panel
CX, CW = 522, 466
panel(CX, RY2, CW, RH2, NAVY)
kicker(CX + 20, RY2 + 18, "INDIA  \u00b7  CYCLONE", NAVY)
yy = headline(CX + 20, RY2 + 44, "CYCLONE AKVAN BEARS DOWN ON INDIA",
              F_HEAD_S, CW - 40)
deck(CX + 20, yy + 4,
     "50,000 evacuated; forecast to cross the Andhra\u2013Odisha coast by "
     "noon on Friday.", CW - 40, F_DECK_S)
# spiral pictogram, bottom-left
cx, cy = CX + 34, RY2 + RH2 - 16
for r, a0 in ((13, 0), (9, 60), (5, 120)):
    d.arc([cx - r, cy - r, cx + r, cy + r], a0, a0 + 300, fill=NAVY, width=4)
d.text((cx + 22, RY2 + RH2 - 28), "LANDFALL FRI NOON",
       font=font("DejaVuSans-Bold.ttf", 15), fill=GREY)

# ---------- COP31 band (full width) ----------
CY, CH = 848, 74
panel(36, CY, 952, CH, TEAL)
d.text((60, CY + 16), "COP31 DRAFT DROPS EVERY FOSSIL-FUEL MENTION",
       font=font("DejaVuSerif-Bold.ttf", 25), fill=INK)
d.text((60, CY + 50),
       "Negotiators slash the cover text from 144 paragraphs to 80 as talks enter their final hours.",
       font=F_DECK_S, fill=(60, 54, 44))

# ---------- footer ticker ----------
d.line([36, 934, 988, 934], fill=INK, width=2)
ticker = ("ALSO ON THE DAY:  Gaza raid ends west of the Yellow Line  \u00b7  "
          "Denmark votes 109\u20130 on Greenland deal  \u00b7  Record rain floods "
          "Florida's Space Coast  \u00b7  Crimean Bridge struck overnight  \u00b7  "
          "Trump: \u2018see what happens\u2019 on Iran after 1 Jan 2027  \u00b7  "
          "Diallo & Tashima challenge Infantino  \u00b7  589m children in conflict "
          "zones  \u00b7  Fiji drought disaster")
lines = wrap(d, ticker, F_FOOT, 952)
yy = 944
for ln in lines:
    d.text((36, yy), ln, font=F_FOOT, fill=INK)
    yy += 20

img.save("entry.png")
print("saved entry.png", img.size)
