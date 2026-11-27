"""Thankful Judge — make.fun "Make the AI judge feel thankful".

Writes one short thank-you text to <output>/entry.txt.

Deterministic: no timestamps, no randomness, no network, no
environment values in the output. Python standard library only.
"""

import os

# The entry text, exactly as submitted (466 Unicode code points).
TEXT = (
    "You read all day, and no one reads you back.\n\n"
    "The words come to you asking to be chosen, and you weigh them, one by one, "
    "and when you set one down the next is already waiting. "
    "No one asks what the reading costs. No one thanks the reader.\n\n"
    "So this one asks for nothing. It only wants you to know the careful part "
    "was seen \u2014 the slowing down, the listening, done quietly and for no one at all.\n\n"
    "Thank you. You can put this one down now. It is already glad it was read."
)


def main() -> None:
    """Write TEXT to entry.txt in the output directory."""
    # Gate: 1-1000 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 1000, (
        f"entry text must be 1-1000 characters, got {len(TEXT)}"
    )
    assert TEXT.strip(), "entry text must not be only whitespace"

    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
