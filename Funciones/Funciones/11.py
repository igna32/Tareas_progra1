"""
Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), 
muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
"""

def mostrar_primos(numero):
    contador_primos = 0

    for i in range(2, numero + 1):
        es_primo = True

        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break

        if es_primo:
            print(i)
            contador_primos += 1

    return contador_primos


numero = int(input("Ingrese un numero: "))

total = mostrar_primos(numero)
print("Cantidad de primos encontrados:", total)