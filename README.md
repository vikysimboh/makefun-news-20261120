# makefun-news-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/vikysimboh/makefun-news-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/vikysimboh/makefun-news-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# Sum up 20 November's world news in one image

Entry for the make.fun bounty
[Sum up 20 November's world news in one image](https://make.fun/bounty/news-image-20261120)
— $250, 50 places paid. Deadline: Saturday 22 November 2026, 00:00 UTC
(08:00 WITA).

## The image

A 1024×1024 newspaper front page, "Friday 20 November 2026",
summarising the day in 40 stories across 7 regions and 12 fields:
3 headline cards, 12 medium cards, 25 one-line stories, a world map,
a date-check box and a numbers box. Modelled on the structure of the
previous day's winning front page, with 20 November stories only.

Headlines: Trump, Xi and Putin sign a peace declaration in Shenzhen;
the ICJ rules Myanmar committed Rohingya genocide; Russia strikes
Kyiv bridges, killing eight. The Shenzhen summit and the ICJ ruling
are dated 19 November in the cards, as they happened then.

## How it runs

`main.py` is Python 3.13, standard library only. It copies the
`entry.png` shipped in this repository to `/output/entry.png`
(or `$MAKEFUN_OUTPUT_DIR/entry.png` when that is set, for local runs):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network, no third-party packages, deterministic — two runs write
byte-identical output.

## Files

- `main.py` — entrypoint, stdlib only
- `entry.png` — the image, 1024×1024
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
