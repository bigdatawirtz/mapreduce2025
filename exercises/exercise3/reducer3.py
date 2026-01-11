#!/usr/bin/python
import sys
maxSales = 0
oldKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, thisSale = data_mapped
    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldKey and oldKey != thisKey:
        print(oldKey+"\t"+str(maxSales))
        oldKey = thisKey;
        maxSales = 0
    oldKey = thisKey
    # Actualiza o maximo se esta venta e maior
    if float(thisSale) > maxSales:
        maxSales = float(thisSale)
# Escribe o ultimo par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey+"\t"+str(maxSales))