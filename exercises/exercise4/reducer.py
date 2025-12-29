# cat testsales.txt | python3 mapper.py | sort | python3 reducer.py


#!/usr/bin/python
import sys

payment_counts = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    payment, count = data
    
    try:
        count_value = int(count)
        if payment in payment_counts:
            payment_counts[payment] += count_value
        else:
            payment_counts[payment] = count_value
    except ValueError:
        continue

if payment_counts:
    max_payment = max(payment_counts, key=payment_counts.get)
    max_count = payment_counts[max_payment]
    print(max_payment + "\t" + str(max_count))
