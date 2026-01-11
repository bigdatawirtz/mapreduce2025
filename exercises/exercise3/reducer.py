#!/usr/bin/python
import sys

salesMax = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    
    try:
        currentSale = float(thisSale)
    except ValueError:
        continue

    if oldKey and oldKey != thisKey:
        print("{0}\t{1}".format(oldKey, salesMax))
        salesMax = 0

    oldKey = thisKey
    
    # Comparamos para quedarnos con el mayor
    if currentSale > salesMax:
        salesMax = currentSale

if oldKey != None:
    print("{0}\t{1}".format(oldKey, salesMax))