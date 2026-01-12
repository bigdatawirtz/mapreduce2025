#!/usr/bin/python
import sys

maxSale = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    
    # Convertimos a float para comparar numeros
    try:
        thisSale = float(thisSale)
    except ValueError:
        continue

    # Si cambiamos de tienda, imprimimos el maximo de la anterior
    if oldKey and oldKey != thisKey:
        print(oldKey + "\t" + str(maxSale))
        oldKey = thisKey
        maxSale = 0

    oldKey = thisKey
    
    # Nos quedamos con el mayor valor
    if thisSale > maxSale:
        maxSale = thisSale

# Imprimir el ultimo
if oldKey != None:
    print(oldKey + "\t" + str(maxSale))