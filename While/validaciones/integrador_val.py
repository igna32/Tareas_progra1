"""
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, 
nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
    Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.
"""

apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
edad_valida = False
while edad_valida == False:
    if edad <= 17 or edad >= 91:
        edad = int(input("Ingrese nuevamente su edad: "))
    else:
        print("Edad ingresada validado.")
        edad_valida = True

estado_civil = input("Ingrese su estado civil, A- Soltero B- Casado C- Divorciado D- Viudo: ")
estado_valido = False

while estado_valido == False:
    match estado_civil:
        case "a":
            estado_civil = "Soltero/a"
            estado_valido = True
        case "b":
            estado_civil = "Casado/a"
            estado_valido = True
        case "c":
            estado_civil = "Divorciado/a"
            estado_valido = True
        case "d":
            estado_civil = "Viudo/a"
            estado_valido = True
        case _:
            estado_civil = False
        
n_legajo = int(input("Ingrese su nro de legajo: "))

legajo_valido = False

while legajo_valido == False:
    if n_legajo <= 999 or n_legajo >= 10000:
        n_legajo = int(input("Ingrese su nro de legajo: "))
    else:
        print("Legajo ingresado validado.")
        legajo_valido = True

print("--------------------------")
print(f"Su apellido es: {apellido}")
print(f"Su edad es: {edad}")
print(f"Su estado civil es: {estado_civil} ")
print(f"Su legajo es: {n_legajo}")
print("--------------------------")
