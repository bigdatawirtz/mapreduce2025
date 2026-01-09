#!/usr/bin/python
import sys

for line in sys.stdin:
    cols = line.strip().split("\t")
    if len(cols) != 5:
        continue
    try:
        val = float(cols[3])
    except:
        continue
    print "TOTAL\t" + str(val)
