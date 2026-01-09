#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

sales_total = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue

    this_key, this_sale = data_mapped

    try:
        # Sumamos cada valor ao acumulador global
        sales_total += float(this_sale)
    except ValueError:
        continue

# IMPORTANTE: O print vai fóra do bucle 'for' para que só se execute UNHA vez
print("Total absoluto de vendas:\t" + str(round(sales_total, 2)))