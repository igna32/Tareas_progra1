def calcular_promedio(lista):
    positivos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            positivos += lista[i]

    promedio = positivos / len(lista)

    return promedio


lista_1 = [5,-7,9]

print(calcular_promedio(lista_1))