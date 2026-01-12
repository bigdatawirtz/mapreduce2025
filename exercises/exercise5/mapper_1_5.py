#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        
        # Extraemos la hora
        # datetime es "2021-11-09 18:27"
        try:
            full_time = datetime.split(" ")[1] # Coge "18:27"
            hour = full_time.split(":")[0]     # Coge "18"
            
            # Imprimimos: Hora (clave) y Coste (valor)
            print(hour + "\t" + cost)
        except IndexError:
            continue