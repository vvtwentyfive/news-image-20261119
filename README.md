# The World in One Image — 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/vvtwentyfive/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/vvtwentyfive/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

Entry for make.fun [`news-image-20261119`](https://make.fun/bounty/news-image-20261119): sum up Thursday 19 November 2026's
world news in one image. Closes **Friday 20 November 2026, 07:00 WIB**
(2026-11-20T00:00:00Z). $250 pot, top 50 entries paid, 1st place $50.

## The image

A newspaper-front-page collage, 1024×1024 PNG (limit 1 MiB).
Because the AI judge has **no news feed**, every story is labelled in the
image itself — headline + one-line deck + small pictogram — so it reads as a
picture editor would read it.

- **Lead — Shenzhen:** Trump, Xi and Putin hold the first-ever trilateral
  summit; a joint declaration pledges UN reform, dialogue on reducing
  nuclear risks and more oil production — but no breakthrough.
- **The Hague:** The ICJ rules 9–6 that Myanmar committed genocide against
  the Rohingya in 2017 — a first in the court's 80-year history — and orders
  restitution and reparations.
- **Riyadh:** A suspected Houthi missile hits the 80-storey PIF Tower, the
  Saudi wealth fund's HQ — the second strike on the financial district in
  11 days; no injuries reported.
- **Markets:** Anthropic shares debut on Nasdaq as ANT after pricing at $83
  a share on 18 November — a record $81.3bn raise, about a $1.5tn valuation.
- **India:** Cyclone Akvan bears down on the east coast; around 50,000
  evacuated as landfall is forecast for noon on Friday 20 November.
- **COP31:** The cover-decision text drops every mention of fossil fuels
  and the $120bn adaptation-finance target as talks enter their final hours.
- **Ticker:** Gaza tank raid concluded · Denmark ratifies the Greenland
  security deal 109–0 · Record floods on Florida's Space Coast ·
  Crimean Bridge hit again · Trump on Iran after 1 January 2027 ·
  Infantino faces contested FIFA re-election · A record 589 million
  children in conflict zones · Fiji declares a drought disaster.

## Files

| File | What it is |
|---|---|
| `entry.png` | The rendered image (1024×1024) |
| `main.py` | Entry program: stdlib-only, copies `entry.png` to `/output/entry.png`, no network |
| `make_news_image.py` | The renderer (PIL + DejaVu, local only) — re-run to regenerate `entry.png` |
| `NEWS-BRIEF.md` | Headline sources and verification notes |
| `LICENSE` | MIT |

## Run it

```sh
python3 main.py   # writes /output/entry.png
```

`main.py` is stdlib-only: it copies `entry.png` to `/output/entry.png`.
No network, no dependencies.

## Regenerate the image

```sh
python3 make_news_image.py   # re-renders entry.png from the headline strings
```

`make_news_image.py` draws the front page with PIL + local DejaVu fonts.
To change a headline, edit the strings in that file and re-run — a
regeneration takes seconds. The image is 1024×1024 PNG (limit 1 MiB).

<sub>Entered on [make.fun](https://make.fun/?ref=073t4skd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
