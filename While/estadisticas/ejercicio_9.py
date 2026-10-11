#ANEXO

"""
9. Solicitar al usuario que ingrese como mínimo 5 números. 
Calcular la suma de los números ingresados y el promedio de 
los mismos.
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
