"""
Escribe una función que calcule el área de un círculo. 
La función debe recibir el radio como parámetro y devolver el área.
"""

def calcular_area(r):
    area = 3.14 * (r **2)
    return area

radio = float(input("Ingrese el radio del circulo: "))

print(calcular_area(radio))