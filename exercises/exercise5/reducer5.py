#!/usr/bin/python
import sys
salesTotal = 0
oldKey = None
max_hour = ""
max_count = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, thisSale = data_mapped
    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldKey and oldKey != thisKey:
        if salesTotal > max_count:
            max_count = salesTotal
            max_hour = oldKey
        oldKey = thisKey;
        salesTotal = 0
    oldKey = thisKey
    salesTotal += float(thisSale)
# Escribe o ultimo par, unha vez rematado o bucle
if oldKey != None:
    if salesTotal > max_count:
        max_count = salesTotal
        max_hour = oldKey
    print(str(int(max_hour))+"\t"+str(max_count))

# Para que me devolviera un resultado en el hadoop streaming le puse -D mapred.reduce.tasks=1