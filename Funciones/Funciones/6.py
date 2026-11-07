"""
Crea una función que verifique si un número dado es par o impar. 
La función debe imprimir un mensaje indicando si el número es par o impar.

"""

def es_par(numero):
    if numero % 2 == 0:
        par = True
    else:
        par = False

    if par:
        resultado = "Es par"
    else:
        resultado = "Es impar"
    
    return resultado

num = int(input("Ingrese un numero: "))

print(es_par(num))