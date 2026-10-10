"""
1.Mostrar los números ascendentes desde el 1 al 10
"""

"""

for i in range(1,11):
    print(i)

"""


"""
2.Mostrar los números descendentes desde el 10 al 1
"""
"""
for i in range(10,0,-1):
    print(i)

"""

"""
3.Ingresar un número. Mostrar los números desde 0 hasta el número 
ingresado.
"""

"""
numero = int(input("Ingrese un numero "))

for i in range(0, numero + 1):
    print(i)

"""

"""
4.Ingresar un número y mostrar la tabla de multiplicar de ese número. 
Por ejemplo si se ingresa el numero 5:
"""

"""
num = int(input("Ingrese un numero: "))
multiplicador = 0


for i in range(10):
    multiplicador += 1
    print(f"{num} * {multiplicador} =", num * multiplicador)

"""

"""
5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
Mostrar la suma y el promedio de todos los números.
"""
"""

suma = 0
contador = 0

for i in range(10):
    num = int(input("Ingrese un numero: "))
    if num == 0:
        break
    contador += 1
    suma += num


print(suma)
print(suma / contador)

"""

"""
6.Imprimir los números múltiplos de 3 entre el 1 y el 10.
"""

"""
for i in range(3,11):
    if i % 3 == 0:
        print(i)

"""

"""
7.Mostrar los números pares que hay desde la unidad hasta el número 50.
"""
"""
num = int(input("Ingrese un numero: "))

for i in range(num,51):
    if i % 2 == 0:
        print(i)

"""

"""
Realizar un programa que permita mostrar una pirámide de números. 
Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
"""

numero = int(input("ingrese un numero: "))

for i in range(1, numero + 1):
    for j in range(1 , i + 1):
        print(j, end="")

    print()

