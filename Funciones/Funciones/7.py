"""
Crea una función que verifique si un número dado es par o impar. 
La función retorna True si el número es par, False en caso contrario.
"""

def es_par(numero):
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False

    return resultado

num = int(input("Ingrese un numero: "))

print(es_par(num))

