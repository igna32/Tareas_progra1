"""
7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
Calcular la suma delos números positivos y el producto de los negativos.
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
