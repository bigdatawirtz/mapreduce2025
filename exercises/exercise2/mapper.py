#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    data = line.split("\t")

    if len(data) == 5:
        # data[2] es la CATEGORÍA
        # data[3] es el COSTE
        ciudad = data[1]
        coste = data[3]
        print(ciudad + "\t" + coste)