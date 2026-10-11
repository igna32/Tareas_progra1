"""
8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.
"""


contador = 1
primer_valor = int(input("ingrese un numero: "))
maximo = primer_valor
minimo = primer_valor

while contador < 10 :
    contador += 1
    valor = int(input("ingrese un numero: "))
    if valor > maximo:
        maximo = valor
    if valor < minimo:
        minimo = valor



print(f"El valor maximo ingresado es: {maximo}")
print(f"El valor minimo ingresado es: {minimo}")
