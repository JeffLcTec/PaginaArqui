import requests
import json

# Reemplaza con tu API_KEY de lectura y el ID del canal
channel_id = '2665378'
api_key = '5VXSRHWA713VW8JR'

# URL de la API de ThingSpeak para obtener los datos del campo 1 (por ejemplo)
url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results='

# Realizamos la solicitud HTTP GET
response = requests.get(url)


data = response.json()
datos = {}
lista_datos = []

for registro in data['feeds']:
    dic = {}
    dic['dia'] = registro['created_at'][0:10]
    dic['hora'] = registro['created_at'][11:19]
    dic['temperatura'] = registro['field1']
    dic['humedad'] = registro['field2']

    lista_datos.append(dic)

datos['datos'] = lista_datos

with open('temperatura.json', 'w') as archivo_json:
    json.dump(datos, archivo_json, indent=4)  # `indent` es para formatear el JSON con indentación
