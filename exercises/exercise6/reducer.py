#!/usr/bin/python
import sys

total = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 2:
        continue

    key, venta = parts
    try:
        total += float(venta)
    except ValueError:
        continue

print "TotalVentas\t%.2f" % total