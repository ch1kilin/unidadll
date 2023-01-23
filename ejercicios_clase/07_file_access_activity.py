'''
Autor: Angel de jesus rosas muñoz
Fecha: 20 de octubre del 2022
'''
devices=[]
file = open("devices.txt","a")

while True:
    newItem = input("Se debera ingresar el nuevo item: ")
    
    if newItem == "exit":
      break
    newItem=newItem.strip()
    break
    file.write(newItem +"\n")
        
print("¡¡All Done!!")    
file.close()