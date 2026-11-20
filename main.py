"""Entry for make.fun bounty news-image-20261120.
Copies the shipped entry.png to the output directory.
Python 3.13, standard library only, no network, deterministic.
The image is a dense newspaper front page for Friday 20 November
2026: 40 stories across 7 regions and 12 fields, modelled on the
structure of the previous day's winning front page.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
