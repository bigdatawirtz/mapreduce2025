#!/usr/bin/python
import sys

# Leemos linea a linea desde la entrada estandar
for line in sys.stdin:
    # Quitamos espacios sobrantes y separamos por tabulador
    data = line.strip().split("\t")
    
    # CONTROL DE ERRORES:
    # Solo procesamos si la linea tiene exactamente 5 campos
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        # Imprimimos: Tienda (clave) y Coste (valor)
        print(store + "\t" + cost)