'''
Autor: angel de jesus rosas muñoz
Fecha: 27 de octubre del 2022
Descripción: Parsear APIs en python

'''

import urllib.parse
import requests 

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key= "ONBr04GHXlHJAK8GKGAd61L4cmvMLpRp"
    url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to":dest})
    
    print("URL: " + (url))