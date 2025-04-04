'''solicitar una edad y clasificarla
en menores de edad (0-17), adultos(18-64) y
adultos mayores (+65)
para ejercicios usar el if elif else
y tambien usar matcha/case
'''

menor_de_edad=range(0,18)
adulto=range(18,64)
adulto_mayores=range(64,100)

edad=int(input("ingrese la edad"))
if edad in menor_de_edad:
   print("es menor de edad")
elif edad in adulto:
    print("es adulto")
else:
    print("es adulto mayor")
    