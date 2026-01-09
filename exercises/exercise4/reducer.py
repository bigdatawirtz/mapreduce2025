#!/usr/bin/python
import sys

current_type = None
count = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t")

    if len(parts) != 2:
        continue

    payment_type = parts[0]

    try:
        value = int(parts[1])
    except:
        continue

    if current_type != payment_type:
        if current_type is not None:
            print current_type + "\t" + str(count)
        current_type = payment_type
        count = 0

    count += value

if current_type:
    print current_type + "\t" + str(count)

