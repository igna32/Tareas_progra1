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


