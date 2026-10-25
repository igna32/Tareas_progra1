"""
8.Realizar un programa que permita mostrar una pirámide de números. 
Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
"""

numero = int(input("ingrese un numero: "))

for i in range(1, numero + 1):
    for j in range(1 , i + 1):
        print(j, end="")

    print()

