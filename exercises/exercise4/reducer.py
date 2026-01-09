#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

# Variables para el conteo actual
countTotal = 0
oldKey = None

# Variables para rastrear al ganador absoluto
maxCount = 0
winnerKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisCount = data_mapped

    # Cuando cambia la llave, evaluamos si la anterior es la ganadora
    if oldKey and oldKey != thisKey:
        if countTotal > maxCount:
            maxCount = countTotal
            winnerKey = oldKey
        countTotal = 0

    oldKey = thisKey
    countTotal += int(thisCount)

# Comprobación para la última llave del archivo
if oldKey is not None:
    if countTotal > maxCount:
        maxCount = countTotal
        winnerKey = oldKey

# AL FINAL: Solo imprimimos el que más veces apareció
if winnerKey is not None:
    print("O tipo de pago máis utilizado é: " + winnerKey + " con " + str(maxCount) + " vendas.")