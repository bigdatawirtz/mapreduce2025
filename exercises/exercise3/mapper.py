#!/usr/bin/python
import sys

for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) != 5:
        continue

    try:
        store = parts[1]
        cost = float(parts[3])
    except:
        continue

    print store + "\t" + str(cost)

