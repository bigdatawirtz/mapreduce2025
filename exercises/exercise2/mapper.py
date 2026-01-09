#!/usr/bin/python
import sys

for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) != 5:
        continue

    try:
        category = parts[2]
        cost = float(parts[3])
    except:
        continue

    print category + "\t" + str(cost)

