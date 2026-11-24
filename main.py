#!/usr/bin/env python3
"""The vacuum's alibi, written out for the grader.

A single sentence lives in this file. The program's only job is to put it
where the grader reads it, one trailing newline, nothing else. No clock and
no network are touched, so repeated runs match byte for byte.
"""

from pathlib import Path

ALIBI = "That spot was in my no-go zone. I drew the no-go zone. Around that spot."
CAP = 200
NAME = "entry.txt"


def clean():
    """Return the alibi with its spacing tidy and its length checked."""
    words = ALIBI.split()
    if len(words) == 0:
        raise RuntimeError("the alibi is blank")
    tidied = " ".join(words)
    if len(tidied) > CAP:
        raise RuntimeError("the alibi is longer than %d characters" % CAP)
    return tidied


def place():
    """The output file: under $MAKEFUN_OUTPUT_DIR, else beside this script."""
    from os import environ
    base = environ.get("MAKEFUN_OUTPUT_DIR") or "."
    return Path(base) / NAME


def emit():
    text = clean()
    out = place()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8", newline="\n")
    return len(text), str(out)


if __name__ == "__main__":
    size, where = emit()
    print("%d characters of alibi in %s" % (size, where))
