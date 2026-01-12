#!/usr/bin/python

import sys

totalNumSales = 0
totalCostSales = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")

	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	numSales, costSale = data_mapped

	totalNumSales += float(numSales)
	totalCostSales += float(costSale)

print("N Ventas: "+str(totalNumSales)+"\t"+"Total vendido: "+str(totalCostSales))
