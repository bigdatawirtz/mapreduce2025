#!/usr/bin/python
import sys

for line in sys.stdin:
    cols = line.strip().split("\t")
    if len(cols) != 5:
        continue
    try:
        hour = cols[0].split(" ")[1].split(":")[0]
        amount = float(cols[3])
    except:
        continue
    print hour + "\t" + str(amount)
