'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''

# entrada1="8 9" #todo #input lo guarda como un texto y es en comillas
# print(map(int,entrada1)) #map es un mapeo, es un recorrido de los datos de una lista
# #la respuesta es un 8 9 (de un texto pasa a un numero)
# print(map(int,entrada1.split()))
# #la rta es 8,, 9 (8 espacio 9)
# print(set(map(int,entrada1.split()))) #set es una función que convierte un texto o numeros y los convierte en conjunto
# #la respuesta es {8,9}

conjunto1=set(map(int,input("ingrese los numeros del primer conjunto").split()))
conjunto2=set(map(int,input("ingrese los numeros del segundo conjunto").split()))
union=conjunto1 | conjunto2 # | es un o (unión)

interseccion= conjunto1 & conjunto2 # & es un caracter que expresa una i
#otra forma
#interseccion= conjunto1.intersection(conjunto2) 
print(conjunto1,conjunto2,union,interseccion) #set (o un conjunto vacio)