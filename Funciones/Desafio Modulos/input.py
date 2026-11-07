def get_int(mensaje: str, mensaje_error:str, minimo: int, maximo:int, reintentos:int) -> int|None:
    contador = 0
    while contador < reintentos:
        contador += 1
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            resultado = numero
            break
        else:
            print(mensaje_error)
            resultado = None

    return resultado



def get_float(mensaje: str, mensaje_error:str, minimo: int, maximo:int, reintentos:int) -> int|None:
    contador = 0
    while contador < reintentos:
        contador += 1
        numero = float(input(mensaje))
        if numero >= minimo and numero <= maximo:
            resultado = numero
            break
        else:
            print(mensaje_error)
            resultado = None

    return resultado

def get_string(mensaje: str, mensaje_error:str, longitud: int, reintentos:int) -> int|None:
    contador = 0
    while contador < reintentos:
        contador += 1
        texto = input(mensaje)
        if len(texto) <= longitud:
            resultado = texto
            break
        else:
            print(mensaje_error)
            resultado = None

    return resultado

