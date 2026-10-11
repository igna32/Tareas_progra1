"""
Integrador While
1. Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez
finalizada la carga determinar:
A. La suma acumulada de los números negativos.
B. La suma acumulada de los números positivos.
C. La cantidad de números negativos ingresados.
D. El promedio de los números positivos.
E. El número positivo más grande.
F. El porcentaje de números negativos ingresados, respecto del total de ingresos.

"""

positivos = 0
cant_positivos = 0
negativos = 0
cant_negativos = 0
contador = 0

numero = int(input("Ingrese el primer numero: "))
contador += 1
if numero < 0:
    cant_negativos += 1
    negativos += numero
elif numero >= 0:
    cant_positivos += 1
    positivos += numero
    posit_mas_gr = numero



while True:
    quiere_ingresar = input("Quiere ingresar otro numero? si / no: ")
    if quiere_ingresar == "No" or quiere_ingresar == "no" or quiere_ingresar == "NO":
        break
    elif quiere_ingresar == "Si" or quiere_ingresar == "si" or quiere_ingresar == "SI":
        numero = int(input("Ingrese el primer numero: "))
        contador += 1
        if numero < 0:
            cant_negativos += 1
            negativos += numero
        elif numero >= 0:
            cant_positivos += 1
            positivos += numero
            if numero > posit_mas_gr:
                posit_mas_gr = numero

print("--------------------------------------------")
print(f"La suma de los Nros negativos es: {negativos}")
print()
print(f"La suma de los Nros positivos es: {positivos}")
print()
print(f"Ingresó {cant_negativos} nros negativos")
print()
promedio_positivos = positivos / cant_positivos
print(f"El promedio de Nros positivos es {promedio_positivos}")
print()
print(f"El numero positivos mas grande es: {posit_mas_gr}")
print()
porcentaje_neg = (cant_negativos / contador) * 100
print(f"El porcentaje de numeros negativos es %{porcentaje_neg}")
print("--------------------------------------------")
