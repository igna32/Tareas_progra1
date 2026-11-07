"""
Define una función que encuentre el máximo de tres números. 
La función debe aceptar tres argumentos y devolver el número más grande.
"""
def analizar_mas_grande(numero):
    mas_grande = numero
    contador = 1
    for i in range(2):
        contador += 1
        numero = int(input(f"Ingrese el {contador}° numero: "))
        if numero > mas_grande:
            mas_grande = numero

    return mas_grande

        
num = int(input("Ingrese el 1° numero: "))

print(analizar_mas_grande(num))

