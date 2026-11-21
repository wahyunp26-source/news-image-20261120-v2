#!/usr/bin/env python3
"""news-image-20261120 v2 entrypoint (stdlib only).

Copies entry.png (beside this file) into $MAKEFUN_OUTPUT_DIR
(default /output) and verifies the copy byte-for-byte.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        print("missing entry.png beside main.py", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(DST)
    if src_size != dst_size:
        print(f"size mismatch: {src_size} != {dst_size}", file=sys.stderr)
        return 1
    with open(SRC, "rb") as f:
        src_bytes = f.read()
    with open(DST, "rb") as f:
        dst_bytes = f.read()
    if src_bytes != dst_bytes:
        print("bytes differ after copy", file=sys.stderr)
        return 1
    print(f"wrote {DST} ({dst_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
