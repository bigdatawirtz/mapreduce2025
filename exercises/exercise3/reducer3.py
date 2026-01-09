#!/usr/bin/python
import sys

salesTotal = []
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    # Emit result when key changes
    if oldKey is not None and oldKey != thisKey:
        print(oldKey + "\t" + str(max(salesTotal)))
        salesTotal = []

    oldKey = thisKey
    salesTotal.append(float(thisSale))

# Emit last key
if oldKey is not None:
    print(oldKey + "\t" + str(max(salesTotal)))

