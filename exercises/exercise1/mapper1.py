#!/usr/bin/python
import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    # Comprobar que hai 5 campos
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        # Comprobar que o custo e numerico
        try:
            float(cost)
            print(store + "\t" + cost)
        except ValueError:
            continue

