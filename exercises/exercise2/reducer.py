#!/usr/bin/env python2
import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 2:
        continue

    thisKey, thisSale = parts
    try:
        thisSale = float(thisSale)
    except ValueError:
        continue

    if oldKey and oldKey != thisKey:
        print "%s\t%.2f" % (oldKey, salesTotal)
        salesTotal = 0

    oldKey = thisKey
    salesTotal += thisSale

if oldKey != None:
    print "%s\t%.2f" % (oldKey, salesTotal)
