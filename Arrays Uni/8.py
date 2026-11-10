def remplazar_nombre(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str ):
    remplazos = 0
    resultado = []
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            remplazos += 1

    resultado = [lista_nombres, remplazos]
    return resultado

nombres = ["Sofia", "Angel", "Ignacio"]

print(remplazar_nombre(nombres, "Angel", "Sheo"))