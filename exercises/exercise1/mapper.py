#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    data = line.split("\t")
    if len(data) != 5:
        continue
    datetime, store, category, cost, payment = data
    # print compatible con Python 2
    print(store + "\t" + cost)

