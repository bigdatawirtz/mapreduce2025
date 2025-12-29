# cat testsales.txt | python3 mapper.py | sort | python3 reducer.py

#!/usr/bin/python
import sys

current_store = None
max_cost = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    store, cost = data
    
    if current_store is None:
        current_store = store
    
    if store != current_store:
        print(current_store + "\t" + str(max_cost))
        current_store = store
        max_cost = 0
    
    try:
        cost_value = float(cost)
        if cost_value > max_cost:
            max_cost = cost_value
    except ValueError:
        continue

if current_store is not None:
    print(current_store + "\t" + str(max_cost))
