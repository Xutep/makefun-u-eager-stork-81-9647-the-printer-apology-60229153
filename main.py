#!/usr/bin/env python3
"""The Printer Apology: one-line apology from an office printer.

Writes a single deterministic line (<=120 chars) to /output/entry.txt.
Stdlib only.
"""

import os

APOLOGY = (
    "Sorry I ate your boarding pass. Cheap paper, a rogue staple, "
    "and you shouting like I'd filed for divorce."
)


def main() -> None:
    assert 1 <= len(APOLOGY) <= 120, len(APOLOGY)
    assert APOLOGY.strip() == APOLOGY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(APOLOGY)
    # Read-back: the file the judge grades must hold exactly this line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == APOLOGY


if __name__ == "__main__":
    main()
