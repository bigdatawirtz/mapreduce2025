import sys

salesMax = 0.0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    
    try:
        thisSale = float(thisSale)
    except ValueError:
        continue

    # Si cambiamos de clave (tienda), imprimimos el máximo de la anterior
    if oldKey and oldKey != thisKey:
        print(oldKey + "\t" + str(salesMax))
        oldKey = thisKey
        salesMax = 0.0

    oldKey = thisKey
    # Comparamos para encontrar el máximo
    if thisSale > salesMax:
        salesMax = thisSale

# Imprimir el último registro
if oldKey != None:
    print(oldKey + "\t" + str(salesMax))