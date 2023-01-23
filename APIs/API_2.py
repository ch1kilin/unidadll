"""
Descripción: apis
API No: 2
Nombre: rosas muñoz angel de jesus 
Fecha: 18/01/2023
"""

import urllib.parse
import requests

main_api = "https://www.abbreviations.com/services/v2/grammar.php?"
key = "j878g39yx378pa77djthzzpn"
idU = "8193"
token = "hUR2LjqmfI1k6YSs"
formato = "json"

while True:
    texto = input("Ingresa el texto ")
    if texto == "salir" or texto == "s":
        break
    
    url = main_api + urllib.parse.urlencode({"uid": idU,"tokenid":token,"text":texto,"format":formato})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_mensaje = json_data["matches"][0]["message"]
    print("Se encontró el siguiente error gramatical :")
    print(json_mensaje)
    json_palabra = json_data["matches"][0]["replacements"][0]["value"]
    print("Lugar del error:  ", json_palabra)
    print("\n")
    

