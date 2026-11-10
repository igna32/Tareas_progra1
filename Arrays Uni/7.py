def retornar_posiciones(lista):
    maximo = lista[0]
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]

    indices = []
    for i in range(len(lista)):
        if lista[i] == maximo:
            indices += [i]
            
    return indices

lista_1 = [1, 3, 44, 44, 44]
print(retornar_posiciones(lista_1))