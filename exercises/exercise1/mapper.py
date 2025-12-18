import sys

for line in sys.stdin:
    # Eliminamos espacios en blanco extra y dividimos por tabulador
    data = line.strip().split("\t")
    
    # MODIFICACIÓN: Solo procesamos si hay exactamente 5 campos
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        print(store + "\t" + cost)
    else:
        # Si no tiene 5 campos, la línea se ignora (se descarta)
        continue