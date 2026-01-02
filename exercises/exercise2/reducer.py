# cat testsales.txt | python3 mapper.py | sort | python3 reducer.py

#!/usr/bin/python
import sys

current_category = None
total_cost = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    category, cost = data
    
    if current_category is None:
        current_category = category
    
    if category != current_category:
        print(current_category + "\t" + str(total_cost))
        current_category = category
        total_cost = 0
    
    try:
        total_cost += float(cost)
    except ValueError:
        continue

if current_category is not None:
    print(current_category + "\t" + str(total_cost))
