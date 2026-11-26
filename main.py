"""Office placard entry for make.fun bounty
u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.

Writes one single-line office placard (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib, deterministic: the same placard on every run.
"""

import os

PLACARD = "THIS PLACARD HAS BEEN HERE SINCE 2019. It has outlasted four managers, two rebrands, and every 'quick sync' ever scheduled."


def main() -> None:
    placard = PLACARD.strip()
    assert "\n" not in placard, "placard must be a single line"
    assert 1 <= len(placard) <= 200, f"placard is {len(placard)} chars, must be 1-200"
    assert placard.strip(), "placard must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(placard)


if __name__ == "__main__":
    main()
