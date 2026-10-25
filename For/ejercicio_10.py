"""
10.Ingresar un número. Determinar si el número es primo o no.
"""
numero = int(input("Ingresa un número: "))

if numero <= 1:
    print("NO es primo")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
            
    if es_primo:
        print("ES primo")
    else:
        print("NO es primo")