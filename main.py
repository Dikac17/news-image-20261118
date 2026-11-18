#!/usr/bin/env python3
"""news-image-20261118 entry (Python 3.13, standard library only).

The image is the entry: a newspaper front page summing up the world's news
of Wednesday 18 November 2026 -- burning tankers in the Strait of Hormuz,
the Kerch Bridge struck again, Gaza facing winter, and COP31 in its final
days. This program only copies it to /output/entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# Deterministic by construction: the same file is copied, byte for byte,
# on every run -- no network, no clock, no randomness.
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
