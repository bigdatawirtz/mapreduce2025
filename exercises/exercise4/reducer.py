#!/usr/bin/python
import sys

current = None
count = 0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 2:
        continue

    key = parts[0]
    try:
        value = int(parts[1])
    except:
        continue

    if current and current != key:
        print current + "\t" + str(count)
        count = 0

    current = key
    count += value

if current:
    print current + "\t" + str(count)

