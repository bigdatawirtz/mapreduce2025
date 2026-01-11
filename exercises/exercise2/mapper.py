#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) < 4:
        continue

    category = parts[2]
    cost = parts[3]
    try:
        cost = float(cost)
    except ValueError:
        continue
    print "%s\t%s" % (category, cost)