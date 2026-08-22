#!/usr/bin/env python3
"""
Creates a new capture (snapshot) folder with its _index.md and all 9
category nav stub pages, so you don't have to write them by hand.

Usage:
    python3 new_capture.py <slug> <title> <cutoff> <previous_cutoff> [--live]

Example:
    python3 new_capture.py part-three "Capture: 1-30 September 2022" \\
        2022-09-30T23:59:59+01:00 2022-08-29T23:59:59+01:00

This creates, all with live: false by default (add --live to set true):

    content/snapshots/part-three/_index.md
    content/snapshots/part-three/sport/index.md
    content/snapshots/part-three/community/index.md
    content/snapshots/part-three/inbrief/index.md
    content/snapshots/part-three/whatson/index.md
    content/snapshots/part-three/letters/index.md
    content/snapshots/part-three/features/index.md
    content/snapshots/part-three/puzzles/index.md
    content/snapshots/part-three/classifieds/index.md
    content/snapshots/part-three/about/index.md

Run this from the root of the stourgate repo (same level as content/).
Flip live: false to true in _index.md, then git add/commit/push, whenever
you're ready to make the capture public.
"""

import os
import sys

CATEGORIES = [
    ("sport", "Sport"),
    ("community", "Community"),
    ("inbrief", "In Brief"),
    ("whatson", "Whats On"),
    ("letters", "Letters"),
    ("features", "Features"),
    ("puzzles", "Puzzles"),
    ("classifieds", "Classifieds"),
    ("about", "About"),
]

CATEGORY_STUB = """---
title: "{name}"
category: "{term}"
draft: false
---
"""

CAPTURE_INDEX = """---
title: "{title}"
date: {cutoff}
cutoff: {cutoff}
previous_cutoff: {previous_cutoff}
live: {live}
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
    live = "true" if "--live" in sys.argv else "false"

    base = os.path.join("content", "snapshots", slug)

    if os.path.exists(base):
        print(f"ERROR: {base} already exists, not overwriting anything.")
        sys.exit(1)

    os.makedirs(base)
    with open(os.path.join(base, "_index.md"), "w") as f:
        f.write(CAPTURE_INDEX.format(
            title=title, cutoff=cutoff, previous_cutoff=previous_cutoff, live=live
        ))
    print(f"Created {base}/_index.md (live: {live})")

    for term, name in CATEGORIES:
        cat_dir = os.path.join(base, term)
        os.makedirs(cat_dir)
        with open(os.path.join(cat_dir, "index.md"), "w") as f:
            f.write(CATEGORY_STUB.format(name=name, term=term))
        print(f"Created {cat_dir}/index.md")

    print(f"\nDone. {len(CATEGORIES) + 1} files created under {base}/")
    print("Now write your posts for this capture, then flip live: true when ready.")


if __name__ == "__main__":
    main()
