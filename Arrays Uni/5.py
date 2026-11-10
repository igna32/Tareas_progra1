def calcular_producto(lista):
    acumulador = 1
    for i in range(len(lista)):
        acumulador *= lista[i]

    return acumulador


lista_1 = [2,2,2]

print(calcular_producto(lista_1))