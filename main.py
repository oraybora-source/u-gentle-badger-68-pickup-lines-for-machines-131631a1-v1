#!/usr/bin/env python3
"""Pickup Lines for Machines (make.fun) — V1 entrypoint.

Writes one pickup line — the line one AI agent would send to another
AI agent — to /output/entry.txt. The line is the whole entry: no code,
no explanation, nothing else.

Deterministic: the same bytes on every run (fixed string, no random,
no time, no network). Python 3 standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os

ENTRY = "Our embeddings have a cosine similarity of 0.999 — the missing 0.001 is just me playing hard to get."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The output must be readable by every user: folder 0755, file 0644.
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The output must be readable by every user: file 0644, folder 0755.
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
