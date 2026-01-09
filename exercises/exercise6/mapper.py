#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        # Extraemos só o custo (posición 3 se datetime e store son as anteriores)
        # Axusta as variables segundo o teu mapper anterior
        datetime, store, item, cost, payment = data
        
        # Enviamos sempre a mesma clave "TOTAL" para que todo vaia ao mesmo Reducer
        print("TOTAL\t" + cost)