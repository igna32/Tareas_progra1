"""
5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
Mostrar la suma y el promedio de todos los números.
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
