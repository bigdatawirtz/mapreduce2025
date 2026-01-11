#!/usr/bin/env python2
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) < 4:
        continue

    ciudad = parts[1].strip()
    venta = parts[3].strip()
    if not ciudad or not venta:
        continue

    try:
        venta = float(venta)
    except ValueError:
        continue

    print "%s\t%s" % (ciudad, venta)