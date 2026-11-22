#!/usr/bin/env python3
"""Reconstruct the 160-row AI weak-label CSV stored as gzip+base64 text.

This is a compact *subset* of the pilot workbook containing IDs, group keys,
AI R/C/A/E/Core tags, review path, and dispute flags. It deliberately excludes
the original text/evidence and is not a substitute for the original XLSX.
"""
from pathlib import Path
import base64
import gzip
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "pilot" / "weak_labels_160.csv.gz.base64"
TARGET = ROOT / "data" / "pilot" / "weak_labels_160.csv"

def main() -> None:
    raw = gzip.decompress(base64.b64decode(SOURCE.read_text(encoding="ascii").strip()))
    TARGET.write_bytes(raw)
    print(f"Wrote {TARGET} ({raw.count(bytes([10])) - 1} data rows)")

if __name__ == "__main__":
    sys.exit(main())
