"""One sentence for a traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from 1800, to /output/entry.txt.
Deterministic: the same sentence every run.
"""

import os

SENTENCE = (
    "Picture the great libraries of the world joined by one road of light "
    "to your door, so the page you ask for arrives in a heartbeat and an "
    "answer comes back just as fast."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.strip() == SENTENCE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
