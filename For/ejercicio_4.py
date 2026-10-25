"""
4.Ingresar un número y mostrar la tabla de multiplicar de ese número. 
Por ejemplo si se ingresa el numero 5:
"""

num = int(input("Ingrese un numero: "))
multiplicador = 0


for i in range(10):
    multiplicador += 1
    print(f"{num} * {multiplicador} =", num * multiplicador)
