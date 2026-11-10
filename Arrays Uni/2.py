def crear_lista(elementos):
    lista = []
    for i in range(elementos):
        a = input("Ingrese algo: ")
        lista += [a]
    return lista


def ingresar_numeros():
    cantidad = int(input("Ingrese la cantidad de numeros: "))
    return crear_lista(cantidad)


print(ingresar_numeros())