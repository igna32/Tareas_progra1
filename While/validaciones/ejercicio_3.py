"""
3.Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
"""

nota = int(input("Ingrese una nota: "))

seguir = True

while seguir:
    if nota >= 1 and nota <= 10:
        print("Numero validado")
        seguir = False
    else:
        nota = int(input("Ingrese una nota: "))
        pass