#!/usr/bin/python
import sys

current = None
total = 0.0

for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) != 2:
        continue

    key = parts[0]

    try:
        value = float(parts[1])
    except:
        continue

    if current and current != key:
        print current + "\t" + "%.2f" % total
        total = 0.0

    current = key
    total += value

if current:
    print current + "\t" + "%.2f" % total


