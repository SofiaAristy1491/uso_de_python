'''
TIPOS DE DATOS
strings: Cadenas de textos <class 'str'>
'''
dato:"Enca24"
dato_2:'Enca24'

#print(type(dato))
#print(type(dato_2))

#concatenación de strings
texto_1="programa"
texto_2="Desarrollador junior"

enunciado=texto_1 + texto_2
print(enunciado)

#indexación de strings
#la indexación se refiere a acceder a un elemento de una cadena en una posición
nombre="Maria Sofia"
print(nombre[0])
'''
python es un lenguaje indexado en cero
'''
# print(nombre[4])
#print(nombre[15])
# print(nombre[-1])

#slicing de cadenas (porción de la cadena) usamos los [] y el parentesis
# print(nombre[:])
# print(nombre[0:3]) #esta forma de porcionas no incluye el extremo derecho (Mar)
# print(nombre[2:4]) #ri
# print(nombre[0:-4]) #la ultima posición no la incluye (Maria S)

nombre= "Maria S o f i a"
#                   -4 -3 -2 -1   

'''Tipos de datos numéricos'
'<class 'int'> : se refiere a números enteros'
'<class 'float'> : se refiere anumeros flotantes que contienen dacimales'
'''
x=5
#print(type(x))
y=5.0
#print(type(y))

'''
datos boolean
1,0 ó Falso / Verdadero
<class 'bool'>
True
False
'''
asistencia=True
#print(type(asistencia))
#print(not asistencia)

'''
TIPOS DE ESTRUCTURAS
SETS: se definen en Python con {,,,,}
TUPLAS: se definen en Python con (,,,,)
LISTAS: se definen en Python con [,,,,]
DICCIONARIOS: se definen en Python con {'clave':'valor',''clave_2':'valor_2',,} 
#la parejita se establce con : y se separan con dos comas ,,
'''

#sets o conjuntos
'''
se utilizan para almacenar infromación cuando no interesa el orden ni la posición 
no permite valores duplicados
<class 'set'>
'''
#conjunto_1={"a","b","c"}
#conjunto_2={"d","e","f"}

#print(type(conjunto_1))
#print(conjunto_1)

'''
los métodos indican las cosas que podemos hacer con los objetos
'''
#Métodos de los conjuntos (las cosas que puedo hacer con el objeto)
#conjunto_1.add("h")
##print(conjunto_1)

#conjunto_2.remove("h") #KeyError: 'h' no esta en el conjunto

# otro ejemplo

#conjunto_2.remove("f")
#print(conjunto_2) # me saca la f del conjunto_2

#otra variable

#conjunto_3=conjunto_1.union(conjunto_2)
#print(conjunto_3)

#aplicar un método
#conjunto_3.update(conjunto_1)
#print(conjunto_3)

#otro ejemplo

#conjunto_2.update(conjunto_1)
#print(conjunto_2)

#conjunto_2.clear()
#print("resultado: " ,conjunto_2)

#conjunto_2.clear()
#print(conjunto_2)

#en python todo es un objeto
# se invocan abriendo y cerrando parentesis con los métodos establecidos

'''
TUPLAS
son estructuras en pythonmás rígidas,son inmutables,
almacenan distintos tipos de datos
'''
#tupla_1=(1,1,1,1,1,1,1,1,1,1,"b",true) 
#numeros letras booleanos
#print(type(tupla_1))
#print(tupla_1.count("b"))  
#devuelve el numero de ocurrencia de un valor

#print(tupla_1.index("b"))

'''
Uso de listas
[] se definen asi con corchetes
'''

mi_lista=[9,5,8,15,True] #con las comillas seria un texto, en este caso se hace con boolan
print(mi_lista)
print(len(mi_lista)) #función de python len (longitud)
mi_lista.append(False) #alica un método a la lista
print(sum(mi_lista)) #función de python sum

'''
uso de diccionario'''
'''se define con llaves{} y necesita un valor {clave:valor}'''

estudiantes={"andres": {"edad":25, "ciudad origen":"cali"}, "jose":22, "diana":26}
print(estudiantes.keys())
print(estudiantes.values())
print(estudiantes.pop("diana")) #remover un dato
print(estudiantes)

#listas conjunto de elementos para un orden
#diccionario para hacer un poco mas de detalle en un elemento, nombres y datos, edad

