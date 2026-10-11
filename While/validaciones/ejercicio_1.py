"""
Validaciones

1.Pedir el ingreso de una clave. Validar que el ingreso del 
usuario sea correcto. Tendrá intentos indeterminados.

"""

clave = input("Ingrese una clave: ")
validar_clave = input("Ingrese la clave ingresada anteriormente: ")

while True:
    if validar_clave != clave:
        validar_clave = input("Clave Incorrecta, reingrese la clave ingresada anteriormente: ")
    else:
        print("Clave correcta")
        break
        