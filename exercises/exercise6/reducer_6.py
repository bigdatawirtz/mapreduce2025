#!/usr/bin/python
import sys
salesTotal = 0
oldKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    thisKey, thisSale = data_mapped
    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldKey and oldKey != thisKey:
        print(oldKey+"\t"+str(salesTotal))
        salesTotal = 0
    oldKey = thisKey
    salesTotal += float(thisSale)
# Escribe o ultimo par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey+"\t"+str(salesTotal))