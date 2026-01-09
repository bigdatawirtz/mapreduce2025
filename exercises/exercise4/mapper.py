#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t")

    # Comprobamos que haxa polo menos 5 columnas
    if len(parts) < 5:
        continue

    try:
        payment_type = parts[4]  # columna tipo de pago
    except:
        continue

    # Emitimos clave=tipo_pago, valor=1
    print payment_type + "\t1"

