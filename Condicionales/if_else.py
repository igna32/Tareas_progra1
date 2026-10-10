"""
IF - ELSE -ELIF

A partir del ingreso de la altura en centímetros de 
un jugador de baloncesto, el programa deberá determinar la posición del 
jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot
"""

altura = int(input("Ingrese su altura: "))

if altura < 160:
    mensaje = "Posicion es BASE"
elif altura >= 160 and altura < 180:
    mensaje = "Posicion es ESCOLTA"
elif altura >= 180 and altura < 200:
    mensaje = "Posicion es ALERO"
else: 
    mensaje = "Posicion es ALA-PIVOT O PIVOT"

print(mensaje)




"""
Calcular una nota aleatoria entre el 1 y el 10 inclusive, 
para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota
 es ...

"""

nota_ingresada = int(input("Ingrese una nota entre 1 y 10: "))

if nota_ingresada >= 1 and nota_ingresada <= 10:
    if nota_ingresada >= 6 and nota_ingresada <= 10:
        mensaje = f"Promocion directa, la nota es: {nota_ingresada}" 
    elif nota_ingresada == 4 or nota_ingresada == 5:
        mensaje = f"Aprobado, la nota es: {nota_ingresada}"
    else:
        mensaje = f"Desaprobado, la nota es: {nota_ingresada}" 
else:
    mensaje = "Nota ingresada invalida"

print(mensaje)
