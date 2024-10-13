import requests
import json

# URL de la API de FireBase para obtener los datos del campo 1 (por ejemplo)
url = "https://iotproject-45a5c-default-rtdb.firebaseio.com/datos.json?auth=g6QDgZRCchCTsIiCWUAS2Wv1Von3W37rvU4ADer9"

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
