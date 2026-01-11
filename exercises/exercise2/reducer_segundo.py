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
        print(f"{oldKey}\t{salesTotal}")
        salesTotal = 0  # Reiniciamos para la nueva clave.
    oldKey = thisKey
    salesTotal += float(thisSale)
# Imprimimos el último par.
if oldKey is not None:
    print(f"{oldKey}\t{salesTotal}")