#!/usr/bin/python
import sys

total_sales = 0.0

for line in sys.stdin:
    try:
        # Solo necesitamos el valor de venta
        key, value = line.strip().split("\t")
        total_sales += float(value)
    except ValueError:
        continue

# Imprime el total absoluto de ventas
print("TOTAL\t" + str(total_sales))

