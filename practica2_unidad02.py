'''
Nombre: ROSAS MUÑOZ ANGEL DE JESUS
Fecha: 15/01/23
Descripcion: Ordenar pizza 
'''

import requests
while True:
	url = "https://order-pizza-api.herokuapp.com/api/swagger.json"
	json_data = requests.get(url).json()
	descripcion= json_data ['info']  ['description']
	fun= json_data['info'] ['title']
	ver= json_data ['info'] ['version']
	name= json_data['paths'] ['/auth'] ['post'] ['parameters'] [0] ['schema'] ['properties'] ['username'] ['description']
	pas= json_data['paths'] ['/auth'] ['post'] ['parameters'] [0] ['schema'] ['properties'] ['password'] ['description']

	salida=input("Desea salir: ")
	print("=======================")
	print("Nombre de la API: "+fun)
	print("Descripion: "+descripcion)
	print("Version de la API: " +ver)
	print("Nombre del Usuario registrado: "+name)
	print("Contraseña de Dicho usuario: "+pas)
	print("=======================")
	if salida == "si" or "SI" or "Si":
		break

