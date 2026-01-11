#!/usr/bin/python
import sys

oldKey = None
maxVenta = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 2:
        continue

    thisKey, thisVenta = parts
    try:
        thisVenta = float(thisVenta)
    except ValueError:
        continue

    if oldKey and oldKey != thisKey:
        print "%s\t%.2f" % (oldKey, maxVenta)
        maxVenta = 0

    oldKey = thisKey
    if thisVenta > maxVenta:
        maxVenta = thisVenta

if oldKey is not None:
    print "%s\t%.2f" % (oldKey, maxVenta)
