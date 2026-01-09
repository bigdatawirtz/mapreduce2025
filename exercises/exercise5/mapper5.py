#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 5:
		continue

	datetime, store, item, cost, payment = data
	datetime = datetime.strip().split(" ")[1].split(":")[0]
	print(datetime+"\t"+"1")
