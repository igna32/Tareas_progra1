"""
4. Mostrar la suma de los números pares desde el 1 hasta el 10.
"""


numero = 0
contador = 0
suma = 0

while contador < 11:
    contador += 1
    numero += 1
    if numero % 2 == 0:
        suma += numero
    else:
        pass
    
print(suma)
