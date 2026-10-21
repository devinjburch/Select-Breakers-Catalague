#!/usr/bin/env python3
"""Deterministic post-merge normalisations (safe to re-run).

* Square D switch units filed as component_type "other" -> "switch-unit".
"""
import re

from common import DATA, load, save


def main():
    p = DATA / "parts" / "SQD.json"
    parts, n = load(p, []), 0
    for x in parts:
        if x["component_type"] == "other" and re.search(r"switch unit|fusible switch", x["title"], re.I):
            x["component_type"] = "switch-unit"
            n += 1
    save(p, parts)
    print(f"normalize: {n} component types updated")


if __name__ == "__main__":
    main()
