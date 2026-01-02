# cat testsales.txt | python3 mapper.py | sort | python3 reducer.py

#!/usr/bin/python
import sys

hour_sales = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    hour, cost = data
    
    try:
        cost_value = float(cost)
        if hour in hour_sales:
            hour_sales[hour] += cost_value
        else:
            hour_sales[hour] = cost_value
    except ValueError:
        continue

if hour_sales:
    max_hour = max(hour_sales, key=hour_sales.get)
    max_sales = hour_sales[max_hour]
    print(max_hour + "\t" + str(max_sales))
