"""Write the 3 AM excuse entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads the single-line entry shipped beside this script (entry.txt) and
copies it byte-for-byte to the grader's output directory, setting mode
0644 explicitly so the grader can read it as another user.
"""

import os
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError) as exc:
        print(f"error: cannot read entry.txt: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if not text.strip():
        print("error: entry.txt is empty or whitespace only", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    try:
        with open(dst, "w", encoding="utf-8") as f:
            f.write(text)
        os.chmod(dst, 0o644)
    except OSError as exc:
        print(f"error: cannot write {dst}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
