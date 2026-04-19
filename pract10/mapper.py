#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if line.startswith("year"):  # skip header
        continue
    try:
        parts = line.split(",")
        year = parts[0].strip()
        temp = float(parts[1].strip())
        print(f"{year}\t{temp}")
    except Exception:
        continue
