contador = 0
limite = 10
cant_masc = 0
cant_fem = 0
cant_otro = 0
cant_iot_ia = 0
nombre_mayor = 0
mayor_edad = 0
tec_mayor = 0
cant_no_ia = 0


while contador != limite:
    contador += 1
    nombre_empleado = input("Ingrese su nombre: ")
    edad_empleado = int(input("Ingrese su edad: "))
    
    while True:
        genero_empleado = input("Ingrese su genero (Masculino: A, Femenino: B, Otro: C, : ")
        if genero_empleado == "A" or genero_empleado == "a":
            genero_empleado = "Masculino"
            cant_masc += 1
            break
        elif genero_empleado == "b" or genero_empleado == "B":
            genero_empleado = "Femenino"
            cant_fem += 1
            break
        elif genero_empleado == "c" or genero_empleado == "C":
            genero_empleado = "Otro"
            cant_otro += 1
            break
        else:
            print("Opcion invalida.")
    while True:
        tec_elegida = input("Seleccione una tecnologia (IA: A, RV/RA: B, IOT: C, : )")
        if tec_elegida == "a" or tec_elegida == "A":
            tec_elegida = "IA"
            break
        elif tec_elegida == "b" or tec_elegida == "B":
            tec_elegida = "RA/RV"
            break
        elif tec_elegida == "c" or tec_elegida == "C":
            tec_elegida = "IOT"
            break
        else:
            print("Opcion Invalida.")

    if edad_empleado >= mayor_edad:
            mayor_edad = edad_empleado
            nombre_mayor = nombre_empleado
            tec_mayor = tec_elegida


    if genero_empleado == "Masculino" and (tec_elegida == "IA" or tec_elegida == "IOT"):
        if edad_empleado >= 25 and edad_empleado <= 50:
            cant_iot_ia += 1

    if genero_empleado != "Femenino" and (edad_empleado >= 33 and edad_empleado <= 40):
        if tec_elegida != "IA":
            cant_no_ia += 1


porc_no_ia = (contador * cant_no_ia) / 100

print(".......................")
print(f"Empleados ingresados: {contador}")
print(f"Cant empleados que votaron por ia: {cant_iot_ia}")
print(f"Porcentaje de empleados que no votaron por ia: {porc_no_ia}")
print(f"Empleado de mayor edad: Nombre: {nombre_mayor}, Edad: {mayor_edad}, Tecnologia: {tec_mayor}")
print("------------------")