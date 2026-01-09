#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

maxSale = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)

    # Cuando cambiamos de ciudad, imprimimos el máximo de la anterior
    if oldKey and oldKey != thisKey:
        print(oldKey + "\t" + str(maxSale))
        maxSale = 0 # Reiniciamos para la nueva ciudad

    oldKey = thisKey
    
    # Lógica de máximo: si la venta actual es mayor que la guardada, actualizamos
    if thisSale > maxSale:
        maxSale = thisSale

# Escribe o ultimo par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey+"\t"+str(maxSale))
