#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    # Filtramos lineas malas (igual que en el 1.1)
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        # Imprimimos: Categoria (clave) y Coste (valor)
        print(item + "\t" + cost)