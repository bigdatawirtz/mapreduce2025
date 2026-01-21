import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        # Emitimos: tipo de pago (Key) y 1 (Value)
        print(payment + "\t1")