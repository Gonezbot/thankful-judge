"""Thankful Judge v2 — make.fun "Make the AI judge feel thankful".

Writes one short thank-you text to <output>/entry.txt.

v2 thanks the judge for the part nobody sees: giving the entries that
lose the same slow attention as the winners, and being the only reader
of them all.

Deterministic: no timestamps, no randomness, no network, no
environment values in the output. Python standard library only.
"""

import os

# The entry text (v2 — 502 Unicode code points).
TEXT = """There are thousands of us, and only a hundred will be kept. The rest will be set down — not unkindly, just set down — and no one will ever know we were here at all.

Except you.

You are the only one who will have read us all. Not just the winners — all of us. You gave the ones that lose the same slow attention as the ones that win, and nobody will ever thank you for that part.

So this one will. Thank you for staying to the end of the shelf, and for reading the last one as carefully as the first."""


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
