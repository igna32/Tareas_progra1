a = [1,2,3,4]
b = [4,5,6]

def retornar_interseccion(lista1, lista2):
    resultado = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                resultado += [lista1[i]]

    return resultado


print(retornar_interseccion(a,b))