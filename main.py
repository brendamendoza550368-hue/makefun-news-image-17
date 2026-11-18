#!/usr/bin/env python3
"""News-image entry: copy the day's picture to the output directory.

The picture itself (entry.png, kept beside this file) sums up the world
news of Tuesday 17 November 2026. The judging harness runs this program
twice in a sandbox with no network and reads only /output/entry.png, so
the whole job is a byte-exact copy: same input, same output, every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
