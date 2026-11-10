
def retornar_mas_grande(lista):
    mas_grande = 0
    for i in range(len(lista)):
        if lista[i] > lista[mas_grande]:
            mas_grande = i

    return mas_grande

lista_numeros = [1,33,2,2,4]

print(retornar_mas_grande(lista_numeros))