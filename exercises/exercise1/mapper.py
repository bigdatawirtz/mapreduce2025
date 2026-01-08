#!/usr/bin/python
import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    datetime, store, item, cost, payment = data
    print(store+"\t"+cost)