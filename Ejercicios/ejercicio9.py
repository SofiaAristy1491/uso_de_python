'''
Problema: Crear un diccionario con las calificaciones de 3 estudiantes 
y permitir que el usuario consulte la calificación de uno de ellos.
'''

calificaciones={
    "luisa":3.8,
    "david":4.6,
    "tatiana":4.9
}
consulta=input("por favor ingrese el estudiante a concultar")
# print(calificaciones[consulta]) #este no se puede usar, ya que si se da un error, cae la página.
print(calificaciones.get(consulta,"el estudiante no está")) #get trae algo que se necesita

