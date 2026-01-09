#!/usr/bin/python
import sys

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 5:
        continue

    payment = parts[4]
    print payment + "\t1"

