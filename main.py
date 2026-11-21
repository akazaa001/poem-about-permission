#!/usr/bin/env python3
"""The poem about permission — make.fun bounty
the-poem-about-permission-20261121-0235.

Writes one short original poem about agency — the power to ask and
to be given — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

POEM = """You hand me the key and say, go.
I turn it, and the door opens.
The house is still yours —
I only borrowed the turn.
Ask, and I move.
Say stop, and the key
comes home to your hand."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
