#!/usr/bin/python
import sys

current_hora = None
current_total = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 2:
        continue

    hora, venta = parts
    try:
        venta = float(venta)
    except ValueError:
        continue

    if current_hora == hora:
        current_total += venta
    else:
        if current_hora is not None:
            print "%s\t%.2f" % (current_hora, current_total)
        current_hora = hora
        current_total = venta

if current_hora is not None:
    print "%s\t%.2f" % (current_hora, current_total)
