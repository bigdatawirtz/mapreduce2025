#!/usr/bin/python
import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        hora = datetime.split()[1].split(":")[0]
        print(hora + "\t" + cost)