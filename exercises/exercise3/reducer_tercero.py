#!/usr/bin/python
import sys
maxSale = 0.0
oldKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)
    if oldKey and oldKey != thisKey:
        print(f"{oldKey}\t{maxSale}")
        maxSale = 0.0  # reiniciamos para la nueva clave.
    oldKey = thisKey
    if thisSale > maxSale:
        maxSale = thisSale
# Imprimimos el último par.
if oldKey is not None:
    print(f"{oldKey}\t{maxSale}")