def calcular_promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]

    promedio = suma / len(lista)

    return promedio


lista_1 = [5,7,9]

print(calcular_promedio(lista_1))