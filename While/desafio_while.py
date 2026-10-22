

contador = 0
limite = 5
cant_masc = 0
cant_iot_ia = 0
nombre_mayor = 0
mayor_edad = 0
tec_mayor = 0
cant_no_ia = 0


while contador != limite:
    nombre_empleado = input("Ingrese su nombre: ")
    edad_empleado = int(input("Ingrese su edad: "))
    if edad_empleado >= mayor_edad:
        mayor_edad = edad_empleado
        nombre_mayor = nombre_empleado
    genero_empleado = input("Ingrese su genero (Masculino: A, Femenino: B, Otro: C, : ")
    tec_elegida = input("Seleccione una tecnologia (IA: A, RV/RA: B, IOT: C, : )")
    contador += 1
    falta_validar = True
    while falta_validar:
         
    match genero_empleado:
        case "a" | "A":
            genero_empleado = "Masculino"
            cant_masc += 1
            if edad_empleado >= mayor_edad:
                mayor_edad = edad_empleado
                nombre_mayor = nombre_empleado
                tec_mayor = tec_elegida
            falta_validar = True
            while falta_validar:
                if tec_elegida == "a" or tec_elegida == "A":
                    tec_elegida = "IA"
                    falta_validar = False
                elif tec_elegida == "b" or tec_elegida == "B":
                    tec_elegida = "RA/RV"
                    falta_validar = False
                elif tec_elegida == "c" or tec_elegida == "C":
                    tec_elegida = "IOT"
                    falta_validar = False
                else:
                    tec_elegida = input("Error, seleccione una tecnologia (IA: A, RV/RA: B, IOT: C, : )")

            if edad_empleado >= 25 and edad_empleado <= 50:
                if tec_elegida == "IA" or tec_elegida == "IOT":
                    cant_iot_ia += 1
            if edad_empleado >= 33 and edad_empleado <= 40:
                if tec_elegida != "IA":
                    cant_no_ia += 1
        case "b" | "B":
            genero_empleado = "Femenino"
        case "c" | "C":
            genero_empleado = "Otro"
        case _:
            genero_empleado = input("Error. Ingrese su genero (Masculino: A, Femenino: B, Otro: C, : ")



porc_no_ia = cant_no_ia / contador * 100


print(".......................")
print(f"Cant empleados que votaron por ia: {cant_iot_ia}")
print(f"Porcentaje de empleados que no votaron por ia: {porc_no_ia}")
print(f"Empleado de mayor edad: Nombre: {nombre_mayor}, Edad: {mayor_edad}, Tecnologia: {tec_mayor}")
print("------------------")