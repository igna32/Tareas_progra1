"""
Match

Una agencia de viajes nos pide informar si hacemos viajes a lugares según la 
estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario 
mostrar “No se viaja”. 
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del plata y Cataratas.
Si es otoño: se viaja a todos los lugares.
Si es primavera: se viaja a todos los lugares menos Bariloche.

"""

estacion = input("Ingrese cuando quiere viajar(invierno, verano, otoño, primavera): ")
destino = input("Ingrese a donde quiere viajar:(bariloche, mar del plata, cataratas) ")

match estacion:
    case "invierno":
        if destino == "bariloche":
            mensaje = "Se viaja"
        elif destino == "mar del plata" or destino == "catartas":
            mensaje = "No se viaja"
        else:
            mensaje = "Destino invalido"
    case "verano":
        if destino == "mar del plata" or destino == "cataratas":
            mensaje = "Se viaja"
        elif destino == "bariloche":
            mensaje = "No se viaja"
        else:
            mensaje = "Destino invalido"
    case "otoño":
        mensaje = "Se viaja"
    case "primavera":
        if destino == "mar del plata" or destino == "cataratas":
            mensaje = "Se viaja"
        elif destino == "bariloche":
            mensaje = "No se viaja"
        else:
            mensaje = "Destino invalido"

print(mensaje)