import json
from datetime import datetime

# Leer el archivo JSON existente
with open('temperatura.json', 'r') as file:
    data = json.load(file)

# Simular la actualización de datos
nuevo_dato = {
    "dia": datetime.now().strftime("%Y-%m-%d"),
    "hora": datetime.now().strftime("%H:%M"),
    "temperatura": 25.3,
    "humedad": 60
}
data.append(nuevo_dato)

# Guardar los nuevos datos en el archivo JSON
with open('temperatura.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Archivo JSON actualizado.")
