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
        #2021-01-08 09:38        A Corunha       Musica  47.25   cash
        hora_total = data[0]
        coste = data[3]

        partes_fecha = hora_total.split(" ")
        if len(partes_fecha) > 1:
            hora = partes_fecha[1].split(":")[0] # Coge el "09"
            print(hora + "\t" + coste)