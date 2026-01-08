#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

# El mapper lee línea por línea desde la entrada estándar
for line in sys.stdin:
    # 1. Limpiamos espacios en blanco al inicio y final (incluye el \n)
    line = line.strip()
    
    # 2. Ignoramos líneas vacías que a veces aparecen al final de los bloques
    if not line:
        continue

    # 3. Dividimos por tabulador
    data = line.split("\t")

    # 4. VALIDACIÓN: Solo procesamos si la línea tiene exactamente 5 campos
    # Según tu estructura: fecha_hora, ciudad, categoría, precio, método_pago
    if len(data) == 5:
        # Extraemos solo lo que nos interesa (Tienda y Coste)
        # Usamos índices para ser más rápidos
        store = data[1]
        cost = data[3]
        
        # Opcional: Podrías validar que el coste sea un número antes de imprimir
        # Pero eso también lo puede manejar el Reducer.
        print(store + "\t" + cost)
    else:
        # Si la línea tiene 4, 6 o cualquier otro número de campos, 
        # simplemente la ignoramos (descarte) y pasamos a la siguiente.
        continue