#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue

    date, time, store, item, cost, payment = data
    # Clave: payment. Valor: 1 (para contar ocurrencias)
    print("{0}\t{1}".format(payment, 1))