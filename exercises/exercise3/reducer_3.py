#!/usr/bin/python
import sys
maxSale = 0.0
oldKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)
    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldKey and oldKey != thisKey:
        print(oldKey+"\t"+str(maxSale))
        oldKey = thisKey;
        maxSale = 0.0
    oldKey = thisKey
    if thisSale > maxSale: maxSale = thisSale
# Escribe o ultimo par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey+"\t"+str(maxSale))