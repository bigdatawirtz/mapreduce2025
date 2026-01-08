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
        sales_total = 0

    try:
        old_key = this_key
        sales_total += float(this_sale)
    except ValueError:
        continue

if old_key is not None:
    print(old_key + "\t" + str(sales_total))