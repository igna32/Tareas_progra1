"""
Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación.
Por defecto es del 1 al 10.
"""

def tabla_multiplicar(numero, inicio=1, fin=10):
    tabla = ""

    for i in range(inicio, fin + 1):
        tabla += f"{numero} x {i} = {numero * i}\n"

    return tabla


n = int(input("Ingrese un numero: "))

print(tabla_multiplicar(n), end="")