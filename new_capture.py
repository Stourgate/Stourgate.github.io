#!/usr/bin/env python3
"""
Creates a new capture (snapshot) folder with its _index.md.

Usage:
    python3 new_capture.py <slug> <title> <cutoff> <previous_cutoff>

Example:
    python3 new_capture.py part-eight "February 2023" \\
        2023-02-28T23:59:59+01:00 2023-01-31T23:59:59+01:00

Creates:
    content/snapshots/part-eight/_index.md

Run this from the root of the stourgate repo (same level as content/).
Write your posts for the capture (content/posts/<month>/<slug>/index.md),
build and check locally, then commit and push whenever it's ready. There's
no separate flip-to-live step, anything present in this repo is public.
"""

import os
import sys

CAPTURE_INDEX = """---
title: "{title}"
date: {cutoff}
cutoff: {cutoff}
previous_cutoff: {previous_cutoff}
draft: false
---
"""


def main():
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(1)

    slug = sys.argv[1]
    title = sys.argv[2]
    cutoff = sys.argv[3]
    previous_cutoff = sys.argv[4]

    base = os.path.join("content", "snapshots", slug)

    if os.path.exists(base):
        print(f"ERROR: {base} already exists, not overwriting anything.")
        sys.exit(1)

    os.makedirs(base)
    with open(os.path.join(base, "_index.md"), "w") as f:
        f.write(CAPTURE_INDEX.format(
            title=title, cutoff=cutoff, previous_cutoff=previous_cutoff
        ))
    print(f"Created {base}/_index.md")
    print("Now write your posts for this capture under content/posts/<month>/.")


if __name__ == "__main__":
    main()
