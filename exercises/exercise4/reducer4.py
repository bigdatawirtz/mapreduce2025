#!/usr/bin/python
import sys
totalPayment = 0
oldKey = None
max_payment = ""
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
        if totalPayment > max_count:
            max_count = totalPayment
            max_payment = oldKey
        oldKey = thisKey;
        totalPayment = 0
    oldKey = thisKey
    totalPayment += 1
# Escribe o ultimo par, unha vez rematado o bucle
if oldKey != None:
    if totalPayment > max_count:
        max_count = totalPayment
        max_payment = oldKey
    print(max_payment+"\t"+str(max_count))

# Para que me devolviera un resultado en el hadoop streaming le puse -D mapred.reduce.tasks=1