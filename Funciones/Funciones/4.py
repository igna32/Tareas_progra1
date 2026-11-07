"""
Escribir una función que calcule el área de un rectángulo. 
La función recibe la base y la altura y retorna el área. 
"""
def calcular_area(base, altura):
    area = base * altura
    return area

base = int(input("Ingrese la base: "))
altura = int(input("Ingrese una altura: "))


print(calcular_area(base, altura))