#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        # data[3] es el coste
        cost = data[3]
        # Enviamos todo con la misma clave "Total"
        print("Total\t" + cost)