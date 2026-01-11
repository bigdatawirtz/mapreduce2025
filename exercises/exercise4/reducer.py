#!/usr/bin/python
import sys

oldKey = None
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 2:
        continue

    thisKey, value = parts
    try:
        value = int(value)
    except ValueError:
        continue

    if oldKey and oldKey != thisKey:
        print "%s\t%d" % (oldKey, count)
        oldKey = thisKey
        count = 0

    oldKey = thisKey
    count += value

if oldKey is not None:
    print "%s\t%d" % (oldKey, count)
