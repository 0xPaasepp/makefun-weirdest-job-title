#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes a single original job title to /output/entry.txt.
Pure standard library, deterministic: every run writes the same bytes.
"""

import os

TITLE = "Professional Mourner for Billionaires' Funerals"


def main() -> None:
    # Gate self-check: the sealed scorer only accepts 1-60 characters.
    if not 1 <= len(TITLE) <= 60 or not TITLE.strip():
        raise SystemExit("entry title fails the 1-60 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
