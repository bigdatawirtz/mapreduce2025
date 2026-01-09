#!/usr/bin/python
import sys

total = 0.0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 2:
        continue
    try:
        total += float(parts[1])
    except:
        continue

print "TOTAL\t" + "%.2f" % total

