"""
Crear una función que reciba un número y retorne True si el 
número es primo, False en caso contrario.
"""

def es_primo(numero):
    if numero <= 1:
        primo = False
    else:
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break

    return primo


num = int(input("Ingrese un numero: "))

print(es_primo(num))