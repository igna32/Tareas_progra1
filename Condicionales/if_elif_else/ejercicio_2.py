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
