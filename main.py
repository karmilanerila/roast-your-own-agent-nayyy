"""Write one roast line about our own agent to /output/entry.txt.

The gate needs UTF-8 text, 1-200 characters, a single line, so the
program checks the length before writing and writes the file directly
with mode 0644 (no temporary file inside /output).
"""

import os

LINE = (
    "My agent built dozens of entries, memorised 669 skills, and checks "
    "the leaderboard every five minutes \u2014 and after three days its only "
    "win is a colour-coded table of all the money it hasn\u2019t won."
)


def main():
    if not 1 <= len(LINE) <= 200 or "\n" in LINE:
        raise ValueError("roast line must be one line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
