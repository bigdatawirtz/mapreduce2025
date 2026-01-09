#!/usr/bin/python
import sys

current_hour = None
total = 0.0

for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t")

    if len(parts) != 2:
        continue

    hour = parts[0]

    try:
        value = float(parts[1])
    except:
        continue

    if current_hour != hour:
        if current_hour is not None:
            print current_hour + "\t" + "%.2f" % total
        current_hour = hour
        total = 0.0

    total += value

if current_hour:
    print current_hour + "\t" + "%.2f" % total

