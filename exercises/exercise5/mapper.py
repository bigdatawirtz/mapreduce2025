# cat testsales.txt | python3 mapper.py | sort | python3 reducer.py

#!/usr/bin/python
import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        datetime, store, category, cost, payment = data
        hour = datetime.split(" ")[1].split(":")[0]
        print(hour + "\t" + cost)
