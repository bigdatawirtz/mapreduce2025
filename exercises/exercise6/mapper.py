#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue

    date, time, store, item, cost, payment = data
    # Clave estática para agrupar todo junto
    print("{0}\t{1}".format("Total_Ventas", cost))