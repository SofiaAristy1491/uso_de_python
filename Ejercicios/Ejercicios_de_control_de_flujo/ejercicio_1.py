'''
crear una lista de palabras predefinida y pedir al 
usuario una palabra. indicar si está en la lista o no
'''
mi_lista=["enero", "febrero", "marzo"]
consulta=input("ingrese el mes a buscar")

if consulta in  mi_lista:
    print("la palabrqa se encuentra en la lista")

if  mi_lista.count(consulta)>0:
    print("la palabrqa se encuentra en la lista")