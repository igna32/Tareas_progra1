

def crear_lista(elementos):
    lista = []
    for i in range(elementos):
        a = input("Ingrese algo: ")
        lista += [a]
    return lista


print(crear_lista(5))