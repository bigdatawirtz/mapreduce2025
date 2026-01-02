# cat testsales.txt | python3 mapper.py | sort | python3 reducer.py

#!/usr/bin/python
import sys

total_sales = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    key, cost = data
    
    try:
        total_sales += float(cost)
    except ValueError:
        continue

print("total\t" + str(total_sales))
