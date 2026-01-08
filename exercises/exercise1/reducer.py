#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

# Inicializamos variables
sales_total = 0
old_key = None

# Procesamos línea por línea desde la entrada estándar
for line in sys.stdin:
    # 1. Limpiamos y dividimos
    data_mapped = line.strip().split("\t")
    
    # 2. Validación de formato
    if len(data_mapped) != 2:
        continue
        
    this_key, this_sale = data_mapped

    # 3. Cambio de llave (Ruptura de control)
    if old_key and old_key != this_key:
        # Imprimimos resultado de la tienda anterior
        # Usamos concatenación simple (+) para compatibilidad total
        print(old_key + "\t" + str(sales_total))
        
        # Reiniciamos para la nueva tienda
        sales_total = 0

    # 4. Acumulamos el valor (con manejo de errores)
    try:
        old_key = this_key
        sales_total += float(this_sale)
    except ValueError:
        # Si el precio no es un número válido, lo ignoramos
        continue

# 5. Emitir el último resultado después del bucle
if old_key is not None:
    print(old_key + "\t" + str(sales_total))