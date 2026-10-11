"""
5. Solicitar el ingreso de 5 números, calcular la suma de los números 
ingresados y el promedio.
Mostrar la suma y el promedio por pantalla.
"""

contador = 0
suma = 0

while contador < 5:
    contador += 1
    num_ingresado = int(input("Ingrese un numero: "))
    suma += num_ingresado

print(suma)
calculo_promedio = suma / 5

print(calculo_promedio)
