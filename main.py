"""Entry for the make.fun competition "One Line, One Chill".

The program writes a single sentence of horror to /output/entry.txt.
The gate: the file must be UTF-8 text of 1 to 200 characters, not only
white space, and the line itself must be one sentence that frightens
in a single breath. The judge weighs, in order: how frightening the
line is, how vivid, how original, and how well the sentence is built,
with the last word landing the blow.

The scare here is built on a specific, wrong detail rather than gore:
a lullaby app that plays a sixth song nobody recorded, and a baby who
answers it with a hum she is not yet able to make.
"""

LINE = (
    "The lullaby app had five songs, but at 3 a.m. it played a sixth, "
    "a woman humming off-key, and my baby, who cannot hum, hummed back."
)


def build_entry() -> str:
    """Return the entry line, asserting it satisfies the gate."""
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
    assert LINE.strip(), "entry must not be only white space"
    return LINE


def main() -> None:
    text = build_entry()
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
