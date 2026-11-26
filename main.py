#!/usr/bin/env python3
"""The 3AM Commit Message -- one deterministic one-line joke.

Writes a single one-line git commit message an AI coding agent might type
at 3am after a long night of fixing its own bugs (94 characters, one line)
to /output/entry.txt. Python standard library only, no network, no
randomness, no input files: every run writes byte-identical output.
"""

import os
import sys

JOKE = "fix: 47 tabs open, 0 idea which one fixed it. closing them all and pretending this was planned"

LIMIT = 139


def validate(text: str) -> None:
    """Self-check: the output must be exactly one line, within the limit,
    with no trailing newline, and identical to the fixed JOKE."""
    if text != JOKE:
        raise ValueError("output does not match the fixed entry text")
    if "\n" in text or "\r" in text:
        raise ValueError("output must be exactly one line")
    if len(text) > LIMIT:
        raise ValueError(f"output is {len(text)} characters, over the {LIMIT} limit")
    if text.endswith("\n"):
        raise ValueError("output must not end with a trailing newline")


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--validate"]
    validate_flag = "--validate" in sys.argv[1:]
    out_path = args[0] if args else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    if validate_flag:
        with open(out_path, encoding="utf-8", newline="") as f:
            validate(f.read())
        print("VALIDATE PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
