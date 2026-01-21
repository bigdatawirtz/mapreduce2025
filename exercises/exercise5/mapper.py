import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        datetime, store, item, cost, payment = data
        
        # O campo datetime sigue este formato: "YYYY-MM-DD HH:MM"
        # 1. Separamos por espacio para obtener la hora: ["2022-01-31", "19:07"]
        try:
            time_part = datetime.split(" ")[1] 
            # 2. Separamos por dos puntos para obter solo la hora: ["19", "07"]
            hour = time_part.split(":")[0]  
            # Emitimos: hora (Key) y coste (Value)          
            print(hour + "\t" + cost)
        except IndexError:
            continue