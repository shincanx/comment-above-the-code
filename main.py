#!/usr/bin/env python3
"""Entry for make.fun's "The Comment Above the Code" bounty.

Writes one line, as if it were the comment a developer left above fragile
production code, to entry.txt in the output directory.
"""

import os

ENTRY = "// This function only works on Tuesdays. Nobody knows why. We stopped asking in 2021."

# Gate the bounty seals: one line, 1-200 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only whitespace"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
