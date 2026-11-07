"""
Diseña una función que calcule la potencia de un número. 
La función debe recibir la base y el exponente como argumentos y devolver el resultado.
"""

def calcular_potencia(a, b):
    resultado = a ** b
    return resultado

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese la base: "))

print(calcular_potencia(base, exponente))