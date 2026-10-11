""" 
6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar 
más). Calcular la suma delos números ingresados y el promedio de los mismos.
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
