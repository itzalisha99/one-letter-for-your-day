#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

The entry is exactly one letter: U.

U stands for "unhinged" — the word for today. A day that came off its
rails: plans derailed, small things went sideways, and by the evening the
whole day felt gloriously, honestly unhinged. It is vivid (a sharp picture,
not a vague mood), funny the moment you hear it, true to a real day, and U
is its natural initial — not the obvious pick (C for chaotic), the sharper
one. One byte, no newline, nothing else.
"""

import os

LETTER = "U"


def validate(letter: str) -> None:
    """Mirror the bounty gate: exactly one character, A to Z, not whitespace."""
    if len(letter) != 1:
        raise ValueError("entry must be exactly one character")
    if not ("A" <= letter <= "Z"):
        raise ValueError("entry must be a letter from A to Z")
    if letter.isspace():
        raise ValueError("entry must not be whitespace")
    letter.encode("utf-8")


def main() -> None:
    validate(LETTER)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
