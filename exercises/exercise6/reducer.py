#!/usr/bin/python
import sys

current_key = None
total = 0.0

for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t")

    if len(parts) != 2:
        continue

    key = parts[0]

    try:
        value = float(parts[1])
    except:
        continue

    if current_key != key:
        if current_key is not None:
            print current_key + "\t" + "%.2f" % total
        current_key = key
        total = 0.0

    total += value


if current_key:
    print current_key + "\t" + "%.2f" % total

