#!/usr/bin/python
import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        print(payment + "\t1")