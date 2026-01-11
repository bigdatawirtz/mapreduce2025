#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 5:
        continue

    fecha, ciudad, categoria, venta, metodo = parts
    try:
        venta = float(venta)
    except ValueError:
        continue

    print "total\t%.2f" % venta
