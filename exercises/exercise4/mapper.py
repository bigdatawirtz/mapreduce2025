#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) < 5:
        continue

    payments = parts[4].lower()
    print "%s\t1" % payments