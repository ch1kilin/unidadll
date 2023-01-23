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

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
    