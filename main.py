#!/usr/bin/env python3
"""Worst Superpower - make.fun entry (program/v1).

Writes one line inventing the most useless superpower to
<output dir>/entry.txt. The output dir is $MAKEFUN_OUTPUT_DIR
(the grading sandbox mounts it at /output), or /output by default.

Stdlib only; deterministic: every run writes the exact same bytes.
"""

import os

LINE = "I can talk to goldfish, but they only ever want to talk about being goldfish."
# 76 characters, one line: the power sounds useful until the catch lands
# in the last few words - the only minds you can read have nothing to say.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
