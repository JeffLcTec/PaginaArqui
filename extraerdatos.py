import requests
import json

# Reemplaza con tu API_KEY de lectura y el ID del canal
channel_id = '2665378'
api_key = '5VXSRHWA713VW8JR'

# URL de la API de ThingSpeak para obtener los datos del campo 1 (por ejemplo)
url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results=10'

# Realizamos la solicitud HTTP GET
response = requests.get(url)

# Verificamos si la solicitud fue exitosa
if response.status_code == 200:
    # Convertimos la respuesta en formato JSON a un diccionario de Python
    data = response.json()
    with open('temperatura.json', 'w') as archivo_json:
        json.dump(data, archivo_json, indent=4)  # `indent` es para formatear el JSON con indentación
else:
    print(f"Error al obtener los datos: {response.status_code}")
