#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) < 4:
        continue

    fecha_hora = parts[0]
    venta = parts[3]

    try:
        venta = float(venta)
        hora = fecha_hora.split()[1].split(":")[0]
    except:
        continue

    print "%s\t%f" % (hora, venta)
