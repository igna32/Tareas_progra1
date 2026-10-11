"""
Solicitarle al usuario el ingreso de un color. 
Validar que el mismo sea Rojo, Verde o Azul.
"""

color = input("Ingrese un color: ")

seguir = True

while seguir:
    if color == "rojo" or color == "verde" or color == "azul":
        seguir = False
        print("Color validado")
    else:
        color = input("Ingrese un color")