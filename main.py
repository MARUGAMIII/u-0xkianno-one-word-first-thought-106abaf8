#!/usr/bin/env python3
"""One Word, First Thought entry.

Writes exactly one original word to /output/entry.txt: the first word
that comes to mind, nothing else.

The word: "defenestration" — the act of throwing someone out of a
window. Nobody expects it as a first thought, it paints an instant,
absurd little scene, and the fact that English keeps a dedicated word
for such a specific act is its own spark of wit.
"""

import os

WORD = "defenestration"


def _check_gate(word: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 24
    characters, not only whitespace, and the task requires exactly one
    word — so the word must be a single run of letters, no spaces.
    """
    assert word, "word must not be empty"
    assert word.isalpha(), "entry must be exactly one word (letters only)"
    assert " " not in word and "\t" not in word, "entry must contain no spaces"
    assert 1 <= len(word) <= 24, "entry must be 1 to 24 characters"


def main() -> None:
    _check_gate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
