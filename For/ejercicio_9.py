"""
9.Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. 
Mostrar la cantidad de divisores encontrados.
"""

num = int(input("Ingrese un numero: "))
divisor = 0

for i in range(0, num):
    divisor += 1
    if num % divisor == 0:
        print(divisor)
