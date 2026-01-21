import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        # Usamos una clave fija para agrupar todo
        print("Total_Vendas" + "\t" + cost)