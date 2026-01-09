import sys

maxSale = None
oldkey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thiskey, thisSale = data_mapped

    
    try:
        thisSale = float(thisSale)
    except ValueError:
        continue

    
    if oldkey and oldkey != thiskey:
        print(oldkey+'\t'+str(maxSale))
        maxSale = None

    oldkey = thiskey

    if maxSale is None or thisSale > maxSale:
        maxSale = thisSale


if oldkey is not None:
    print(oldkey+'\t'+str(maxSale))

