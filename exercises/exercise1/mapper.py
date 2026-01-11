#!/usr/bin/python
import sys

# Formato: date, time, store, item, cost, payment
for line in sys.stdin:
    data = line.strip().split("\t")
    
    # Control de errores: descarta si no hay 6 columnas
    if len(data) != 6:
        continue

    date, time, store, item, cost, payment = data
    print("{0}\t{1}".format(store, cost))