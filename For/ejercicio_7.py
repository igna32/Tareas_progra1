"""
7.Mostrar los números pares que hay desde la unidad hasta el número 50.
"""

num = int(input("Ingrese un numero: "))

for i in range(num,51):
    if i % 2 == 0:
        print(i)
