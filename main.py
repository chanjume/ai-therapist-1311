#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — one-line diagnosis, <= 200 chars.

Writes the diagnosis to /output/entry.txt.
"""
import os

# The joke's turn lands at the end: the "diagnosis" is not anxiety but
# a counted habit (214 unsent texts) plus a second twist (a PhD in
# rehearsing arguments from 2019), delivered in a calm clinical voice.
DIAGNOSIS = (
    "Session 9, 3:07 a.m.: Mr. Alvarez, you don't have anxiety. "
    "You have 214 unsent texts to your ex \u2014 each a masterpiece, "
    "none sent \u2014 and a PhD in rehearsing arguments from 2019."
)


def main() -> None:
    line = DIAGNOSIS.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
