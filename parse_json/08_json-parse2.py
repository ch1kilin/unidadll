'''
Autor: angel de jesus rosas muñoz
Fecha: 27 de octubre del 2022
Descripción: Parsear APIs en python

'''

import urllib.parse
import requests 

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "México"
key= "ONBr04GHXlHJAK8GKGAd61L4cmvMLpRp"
dest = "U.S.A"
url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to":dest})

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    
