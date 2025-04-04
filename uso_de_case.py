dia=input("ingrese el dia de la semana").lower() #input tiene muchas herramientas que se adiciona al final
match dia:
    case "sabado" | "domingo":
        print(f"{dia} es fin de semana")
    case "lunes":
        print(f"{dia} es el dia más dificil")
    case "martes" | "miercoles" | "jueves":
         print("es un dia normal")
    case _: 
        print("texto no es un dia de la semana")
