"""
Ingresar un número. Mostrar cada número primo que hay entre el 1 y el 
número ingresado. Informar cuántos números primos se encontraron.
"""

numero = int(input("Ingrese un numero: "))
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

     