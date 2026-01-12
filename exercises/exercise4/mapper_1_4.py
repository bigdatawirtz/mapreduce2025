#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    # Filtro de seguridad
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        # Imprimimos: Metodo de pago (clave) y 1 (valor)
        print(payment + "\t1")