"""One sentence for a traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from 1800, to /output/entry.txt.
Deterministic: the same sentence every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
OUTPUT_ENV_VAR = "OUTPUT_DIR"


def resolve_output_path() -> str:
    """Pick a writable output path.

    Honors OUTPUT_DIR when set; otherwise prefers /output (the bounty
    harness location) and falls back to ./output when /output is not
    writable, so the entry still lands somewhere deterministic.
    """
    override = os.environ.get(OUTPUT_ENV_VAR)
    if override:
        return os.path.join(override, "entry.txt")
    try:
        os.makedirs("/output", exist_ok=True)
        probe = os.path.join("/output", ".write-probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("")
        os.remove(probe)
        return OUTPUT_PATH
    except OSError:
        os.makedirs("output", exist_ok=True)
        return os.path.join("output", "entry.txt")


SENTENCE = (
    "Cook sailed three years to circle the world; your letter rides a road "
    "of light around it before the ink dries, and any book you name comes "
    "home with the answer."
)


def validate_sentence(sentence: str) -> None:
    """Gate: the entry must be exactly one sentence within the limit."""
    assert 1 <= len(sentence) <= 200, f"length {len(sentence)} out of range"
    assert sentence.strip() == sentence, "leading/trailing whitespace"
    assert "\n" not in sentence, "must be a single line"
    assert sentence.endswith("."), "must end with a period"
    assert sentence.count(".") == 1, "must contain exactly one sentence"
    assert sentence.encode("utf-8").decode("utf-8") == sentence, "not UTF-8 clean"


def main() -> None:
    validate_sentence(SENTENCE)
    path = resolve_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == SENTENCE, "written output differs from sentence"
    print(f"wrote {len(SENTENCE)} chars to {path}")


if __name__ == "__main__":
    main()
