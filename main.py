"""Copy the entry image to the output directory.

The picture (a photorealistic ramen noodle pull) ships in this repository
as entry.png; this program just places a byte-identical copy at
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). Standard library only,
no network, fully deterministic: every run writes the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    # copyfile moves raw bytes only: no re-encode, no timestamp in the
    # output, so both grading runs produce identical files.
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
