"""One Star for Monday — entry program.

Writes the one-line, one-star review of Monday (as if Monday were a
restaurant) to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

LINE = "One star. Monday seated me at 7 a.m., served last week's coffee, then billed me for the whole week."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back verification: the file must hold exactly the line, no more.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    assert written.strip(), "entry.txt must not be only whitespace"
    assert 1 <= len(written) <= 180, "entry.txt outside the 1-180 char gate"
    assert len(written.split()) <= 25, "entry exceeds 25 words"


if __name__ == "__main__":
    main()
