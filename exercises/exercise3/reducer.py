#!/usr/bin/python
import sys

current = None
max_sale = 0.0

for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) != 2:
        continue

    store = parts[0]

    try:
        value = float(parts[1])
    except:
        continue

    if current and current != store:
        print current + "\t" + "%.2f" % max_sale
        max_sale = 0.0

    current = store

    if value > max_sale:
        max_sale = value


if current:
    print current + "\t" + "%.2f" % max_sale

