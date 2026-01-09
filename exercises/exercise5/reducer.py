#!/usr/bin/python
import sys

totals = {}

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 2:
        continue
    key = parts[0]
    try:
        val = float(parts[1])
    except:
        continue
    if key in totals:
        totals[key] += val
    else:
        totals[key] = val

for k in totals:
    print k + "\t" + "%.2f" % totals[k]

