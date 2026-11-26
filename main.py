#!/usr/bin/env python3
"""The Self-Checkout Is Judging You.

Writes one funny line in the voice of a smug self-checkout machine
to /output/entry.txt. Deterministic, no network, no randomness.
"""

from pathlib import Path

LINE = "Twelve yoghurts, no spoon, no shame \u2014 I'm not a checkout, I'm a witness to a dairy crime."


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
