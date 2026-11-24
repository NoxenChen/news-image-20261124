[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/NoxenChen/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)
[![reward](https://make.fun/badge/news-image-20261124/NoxenChen/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

# The World in One Image — 24 November 2026

A newspaper-style poster that sums up Tuesday, 24 November 2026 in a single 1024×1024 image. The lead story is Jensen Huang's reinstatement as NVIDIA chief executive, eleven days after he stepped down amid a "spy" controversy, with the board reversing unanimously after a push by Trump and shares surging. Below it, five more stories from the day: the COP31 climate talks collapsing in Antalya with no deal, the Democrats winning their biggest House majority in decades in the 2026 midterms, at least 14 killed in Russian strikes on the Kyiv region alongside Ukraine's claim of sinking a Russian warship off Libya, NATO vowing space defence as allies warn Russia may launch a nuclear space weapon next month, and Swiss Foreign Minister Cassis in China for the fifth round of the China–Switzerland foreign-minister strategic dialogue. The poster is drawn entirely with code — no downloaded images — so every word is crisp and legible, and the date is printed large in the masthead.

## How to run

Requires Node 22 (standard library only) and, to re-render the poster, Python 3 with Pillow.

```sh
# Re-render the poster (optional — entry.png is already committed)
python3 render_poster.py

# Copy the poster to the output directory
MAKEFUN_OUTPUT_DIR=/output node main.ts
```

`main.ts` resolves `entry.png` next to itself and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), byte for byte.
