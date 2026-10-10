"""
1. Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
"""

"""
contador = 0

while contador < 10:
    contador += 1
    print(contador)
"""

"""
2. Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
"""

"""
contador = 10

while contador > 0:
    print(contador)
    contador -= 1
"""

"""
3. Mostrar la suma de los números desde el 1 hasta el 10.
"""

"""
contador = 0
suma = 0
while contador < 10:
    contador += 1
    suma += contador
    
print(suma)
"""


"""
4. Mostrar la suma de los números pares desde el 1 hasta el 10.
"""

"""
numero = 0
contador = 0
suma = 0

while contador < 11:
    contador += 1
    numero += 1
    if numero % 2 == 0:
        suma += numero
    else:
        pass
    
print(suma)
"""

"""
5. Solicitar el ingreso de 5 números, calcular la suma de los números 
ingresados y el promedio.
Mostrar la suma y el promedio por pantalla.
"""

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
"""

""" 
6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar 
más). Calcular la suma delos números ingresados y el promedio de los mismos.
"""

"""
suma = 0
contador = 0
quiere = True
while quiere:
    num_ing = int(input("Ingrese un numero: "))
    suma += num_ing
    contador += 1
    quiere_ingresar = input("Quiere ingresar otro?: si / no")
    if quiere_ingresar == "no" or quiere_ingresar == "No":
        quiere = False
    elif quiere_ingresar == "Si" or quiere_ingresar == "si":
        pass

calculo_suma = suma / contador

print(suma)
print(calculo_suma)
"""

"""
7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
Calcular la suma delos números positivos y el producto de los negativos.
"""


"""
negativos = 1
positivos = 0

num_ing = int(input("Ingrese un numero: "))
if num_ing < 0:
    negativos *= num_ing
else:
    positivos += num_ing

quiere = True
while quiere:
    quiere_ingresar = input("Quiere ingresar otro? si / no: ")
    if num_ing < 0:
        negativos *= num_ing
    else:
        positivos += num_ing
    if quiere_ingresar == "no" or quiere_ingresar == "No":
        quiere = False
    elif quiere_ingresar == "Si" or quiere_ingresar == "si":
        num_ing = int(input("Ingrese un numero: "))
    else:
        print("respuesta invalida.")



print(positivos)
print(negativos)
"""

"""
8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.
"""
"""

contador = 1
primer_valor = int(input("ingrese un numero: "))
maximo = primer_valor
minimo = primer_valor

while contador < 10 :
    contador += 1
    valor = int(input("ingrese un numero: "))
    if valor > maximo:
        maximo = valor
    if valor < minimo:
        minimo = valor



print(f"El valor maximo ingresado es: {maximo}")
print(f"El valor minimo ingresado es: {minimo}")
"""

#ANEXO

"""
9. Solicitar al usuario que ingrese como mínimo 5 números. 
Calcular la suma de los números ingresados y el promedio de 
los mismos.
"""

"""
minimo = 5
contador = 0
acumulado = 0

while contador < 5:
    num_ing = int(input("Ingrese un numero: "))
    contador += 1
    acumulado += num_ing


while contador >= 5:
    quiere_ingresar = input("Quiere ingresar mas numeros? si / no: ")
    if quiere_ingresar == "Si" or quiere_ingresar == "si" or quiere_ingresar == "SI":
        num_ing = int(input("Ingrese un numero: "))
        contador += 1
        acumulado += num_ing
    elif quiere_ingresar == "no" or quiere_ingresar == "No" or quiere_ingresar == "NO":
        break
    else:
        print("Respuesta invalida.")

calculo_promedio = acumulado / contador

print(acumulado)
print(calculo_promedio)
"""

"""
10. Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
Calcular la suma de los números ingresados y el promedio de los mismos.
"""

"""
min = 5
contador = 0
acumulado = 0

while contador < min:
    num_ing = int(input("Ingrese un numero: "))
    contador += 1
    acumulado += num_ing


while contador >= 5 and contador < 10:
    quiere_ingresar = input("Quiere ingresar mas numeros? si / no: ")
    if quiere_ingresar == "Si" or quiere_ingresar == "si" or quiere_ingresar == "SI":
        num_ing = int(input("Ingrese un numero: "))
        contador += 1
        acumulado += num_ing
    elif quiere_ingresar == "no" or quiere_ingresar == "No" or quiere_ingresar == "NO":
        break
    else:
        print("Respuesta invalida.")

calculo_promedio = acumulado / contador

print(acumulado)
print(calculo_promedio)

"""

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

"""