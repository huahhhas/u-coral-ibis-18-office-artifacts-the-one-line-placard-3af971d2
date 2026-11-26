#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic: no randomness, no
network, no clock. The placard is at most 180 characters.
"""

import os

# Final placard: same conceit, tightened. The condition note
# ("jammed") is the curator's deadpan detail that sells the artifact.
LINE = (
    "Stapler, c. 1998. Pressed steel, jammed. Ritual binding device "
    "of the Filing Clerks; one squeeze joined two pages \u2014 and "
    "two souls \u2014 for eternity."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
