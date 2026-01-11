#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue

    date, time, store, item, cost, payment = data
    # Cambiamos la clave a 'item' (categoría)
    print("{0}\t{1}".format(item, cost))