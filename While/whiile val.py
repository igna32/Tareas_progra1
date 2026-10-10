"""
Validaciones

1.Pedir el ingreso de una clave. Validar que el ingreso del 
usuario sea correcto. Tendrá intentos indeterminados.

"""
"""

clave = input("Ingrese una clave: ")
validar_clave = input("Ingrese la clave ingresada anteriormente: ")

while True:
    if validar_clave != clave:
        validar_clave = input("Clave Incorrecta, reingrese la clave ingresada anteriormente: ")
    else:
        print("Clave correcta")
        break
        
"""

"""
2.Pedir el ingreso de una clave. Validar que el ingreso del usuario sea 
correcto. Solo tendrá 3 intentos.
"""
"""
clave_registrada = input("Ingrese una clave: ")

intentos = 0
intentos_max = 3
acertado = False

while intentos < intentos_max and not acertado:
    clave = input("Ingresar una clave: ")
    if clave == clave_registrada:
        print("Clave Correcta.")
        acertado = True
    else:
        intentos += 1
        print(f"Clave incorrecta. Te quedan {intentos_max - intentos} intentos.")

if not acertado:
    print("Has superado el número máximo de intentos. Cuenta bloqueada.")

"""

"""
3.Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
"""

nota = int(input("Ingrese una nota: "))

