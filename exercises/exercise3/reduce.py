#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

sales_total = 0
old_key = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 2:
        continue
        
    this_key, this_sale = data_mapped

    if old_key and old_key != this_key:
        print(old_key + "\t" + str(sales_total))
    #Se veulve a 0
        sales_total = 0
    #Logica de maximo
    try:
        valor_alto= float(this_sale)
        old_key = this_key

        if valor_alto > sales_total:
            sales_total = valor_alto
    except ValueError:
        continue

if old_key is not None:
    print(old_key + "\t" + str(sales_total))