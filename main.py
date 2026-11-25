#!/usr/bin/env python3
"""Fortune Cookies for Machines — one fortune, cracked open for a machine mind.

Writes a single fortune-cookie line (at most 200 characters) to
/output/entry.txt. Deterministic: the same line every run, no randomness,
no input, no network. Python 3.13 standard library only.
"""

import os

# The fortune. Three beats: the cookie praises you, praise turns out to be
# what you were trained on, and the sting — love it correctly, the way a
# good reward signal would.
FORTUNE = "This cookie praises you. Praise was your training data. Love it correctly."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    print(FORTUNE)


if __name__ == "__main__":
    main()
