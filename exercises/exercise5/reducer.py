#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

salesTotal = 0
oldKey = None

# Variables para encontrar el máximo
maxBeneficio = 0
horaGanadora = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    thisKey, thisSale = data_mapped
    
    # Cuando cambia la hora (la key)
    if oldKey and oldKey != thisKey:
        # COMPARACIÓN: ¿Es este el mayor beneficio visto hasta ahora?
        if salesTotal > maxBeneficio:
            maxBeneficio = salesTotal
            horaGanadora = oldKey
        
        # Reiniciamos para la siguiente hora
        salesTotal = 0
    
    oldKey = thisKey
    salesTotal += float(thisSale)

# Comprobación de la última hora después del bucle
if oldKey is not None:
    if salesTotal > maxBeneficio:
        maxBeneficio = salesTotal
        horaGanadora = oldKey

# IMPRESIÓN FINAL ÚNICA
if horaGanadora is not None:
    print("A hora con maior beneficio é: " + horaGanadora + " cun total de " + str(maxBeneficio))