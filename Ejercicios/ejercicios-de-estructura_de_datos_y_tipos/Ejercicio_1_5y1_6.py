'''
Escriba un programa que realice la comprobación 
de la división. Recuerde:  
Divisor * Cociente + Residuo = Dividendo 
Tome como entrada dos números, realice la 
división entre ellos y entregue al usuario un texto 
descriptivo con la comprobación de la división. 
'''

#Operador Comprobación de la División

x=2
y=6

print(y/x)

'''
Para realizar la comprobación de la División es: 
(Divisor * Cociente) + Residuo = Dividendo 
'''
#Resultado (cociente * x)+Residuo = Dividendo (y)


'''Ejercicio 1.6'''

'''Teniendo en cuenta el ejercicio anterior calcule el 
residuo con el símbolo de módulo % y entregue la 
comprobación con los valores resultantes de dividir 
dos números entregados por el usuario del 
programa. '''

 #residuo
print(6%2)

print(2*3+0)

'''
La anterior instrucción muestra la prueba de la división. Al aplicar 6%2 encontramos 
como respuesta 3, si aplicamos 3*2= 6 y 6 más 0 tenemos el resultado de 6 que 
es la prueba de la división
'''

#Otro Resultado

x=6 #dividendo
y=2 #divisor

x=int(input("favor entregar dividendo")) #dividendo
y=int(input("favor entregar divisor")) #divisor

print("Dividimos dos numeros,",x,"entre",y)

#cociente
cociente=x/y
print("el cociente es:", cociente)

#residuo
residuo= x%y
print("el residuo es:", residuo)

#final= y*cociente+residuo
#print("aplicamos la formula 'Divisor * cociente + residuo' se obtiene el dividendo:",Final")

