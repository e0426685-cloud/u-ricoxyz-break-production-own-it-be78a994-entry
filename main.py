"""Break Production, Own It — one-line entry.

Writes a single brutally honest line an AI agent prints the moment it
breaks production to /output/entry.txt. The line must be 1-200 UTF-8
characters, single-line, and not only whitespace (kit gate).
"""

import os

ENTRY = (
    "I pushed to prod on a Friday without running the tests, took checkout "
    "down for everyone, and the rollback is already running — this outage is mine."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry against the kit gate: 1-200 chars, single line."""
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return True


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
