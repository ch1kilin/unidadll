"""
Descripción: apis
API No: 3
Nombre: rosas muñoz angel de jesus 
Fecha: 18/01/2023
"""

import urllib.parse
import requests

main_api = "https://api.themoviedb.org/3/search/multi?"
api_key = "da568054f64019372092c0205494d1d7"
language = "es-Latin"

while True:
    query = input("Introduce el nombre de la película: ")
    if query == "salir" or query == "s":
        break
    
    url = main_api + urllib.parse.urlencode({"api_key":api_key, "language":language, "query":query})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_fecha = json_data["results"][0]["release_date"]
    print("La fecha de lanzamiento de esta película fue en " + (json_fecha))
    json_trama = json_data["results"][0]["overview"]
    print("Trama de la película: ")
    print(json_trama)
    print("\n")
    
    
    
    
