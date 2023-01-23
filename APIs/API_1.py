"""
Descripción: apis
API No: 1
Nombre: rosas muñoz angel de jesus 
Fecha: 18/01/2023
"""

import urllib.parse
import requests

main_api = "http://ws.audioscrobbler.com/2.0/?"
funcion = "artist.getinfo"
key = "20551f6c54a2dd03681e7c51d6dc8047"
formato = "json"

while True:
    artista = input("Ingresa el artista: ")
    if artista == "salir" or artista == "s":
        break
    
    url = main_api + urllib.parse.urlencode({"method": funcion,"artist":artista, "api_key":key, "format":formato})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_informacion = json_data["artist"]["bio"]["summary"]
    print("\n")
    print("*INFORMACION DEL ARTISTA:* ")
    print(str(json_informacion))
    print("\n")

