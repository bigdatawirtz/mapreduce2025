import sys

# Iterar sobre cada linea de la entrada estándar
for line in sys.stdin:
    data = line.strip().split("\t")
    # Control de errores: Comprobamos si la linea tiene exactamente 5 campos
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        # Emitimos: tienda (Key) y coste (Value)
        print(store + "\t" + cost)