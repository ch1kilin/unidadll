'''
Nombre: ROSAS MUÑOZ ANGEL DE JESUS
Fecha: 15/01/23
Descripcion: API de clima

Link: https://www.visualcrossing.com/weather/weather-data-services
'''


import requests
import urllib.parse

while True:
    include= "day"
    main_api = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Mexico?"
    metric = "metric"
    key = "NMELQKWQPZFSY6MA9E4CZCPKW"
    cont= "json"
    url = main_api + urllib.parse.urlencode({"unitGroup":metric,"include":include,"key":key,"contentType":cont})
    print(url)
    json_data = requests.get(url).json()
    #print(json_data)
    max= json_data ['days'] [0] ['tempmax']
    min= json_data ['days'] [0] ['tempmin']
    humedad= json_data ['days'] [0] ['humidity']
    print("El clima del de hoy es:")
    print ("La temperatura MAX: "+ str(max))
    print ("La temperatura MIN: "+ str(min))
    print ("La humedad en el aire es de: "+ str(humedad))
    salida = input("Desea continuar:")
    if salida == "salida" or salida == "s" :
        break
    

 

