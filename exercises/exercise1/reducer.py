#!/usr/bin/python
import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    thisKey, thisSale = data_mapped
    if oldKey and oldKey != thisKey:
        print "%s\t%.2f" % (oldKey, salesTotal)
        salesTotal = 0
    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey is not None:
    print "%s\t%.2f" % (oldKey, salesTotal)
