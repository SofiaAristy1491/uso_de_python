x=520
y=60

'''
condicional if elf else
if then else
'''
#cada que abre un if, no se coloca un else
if x > y:  #evaluar si x es mayor que y
    print("x es mayor a y")

#caso2 ---> if else
if x < y:
    print("x es menos que y")
else: #no evalua condiciones, si no se cumpple que se hace
    print("x es mayor que y")


#caso 3 ---> uso de if elif else
if x < y:
    print("x es menor que y")
elif x==y: #condición 
    print("x es igual a y")
elif x/y==8: #condición
    print("x divido y es igual a 8")
else: #de lo contrario
    print("x es mayor que y")

    

    #Variante 1

    #uso distinto del if

    if x%2==0 and x>500:  #multiples condiciones a evaluar
      print("x es par y mayor que 500")
 
#caso de uso el login a una aplicación

# usuario=input("por favor ingrese su usuario")
# password=input("por favor ingrese su password")

# if usuario=="sofia" and password=="1234":
#     print("usuario puede ingresar")
# else:
#     print("usuario o contraseña incorrectos")

usuario=input("por favor ingrese su usuario")


if usuario=="sofia":
    password=input("por favor ingrese su password")
    if password=="1234":
     print("usuario puede ingresar")
    else:
        print("contraseña incorrecta")
else:
    print("usuario incorrecto")
print("ejecucion terminada")