cargo_fijo = 7000
costo_m3 = 200
bonificacion = 0
recargo = 0
iva = 0.21
descuento_adicional = 0

consumo = int(input("Ingrese cuantos metros cubicos consume: "))
tipo_usuario = input("Ingrese su tipo de cliente (residencial, " \
"comercial, industrial): ")

match tipo_usuario:
    case "residencial":
        if consumo < 30:
            bonificacion = 0.10
        elif consumo > 80:
            recargo = 0.15
    case "comercial":
        if consumo > 150 and consumo < 300:
            bonificacion = 0.08
        elif consumo > 300:
            bonificacion = 0.12
        elif consumo < 50:
            recargo = 0.05
    case "industrial":
        if consumo > 500 and consumo < 1000:
            bonificacion = 0.20
        elif consumo > 1000:
            bonificacion = 0.30
        elif consumo < 200:
            recargo = 0.10

#                        x        200
subtotal_de_consumo = consumo * costo_m3


if tipo_usuario == "residencial" and subtotal_de_consumo < 35000:
    descuento_adicional = 0.05

#mostrar subtotal
print(f"El costo del consumo sin agregados o descuentos es: {subtotal_de_consumo}")

bonificacion_correspondiente = subtotal_de_consumo * bonificacion

if bonificacion > 0:
    print(f"Corresponde una bonificacion de -{bonificacion_correspondiente}")

    restar_bonificacion = subtotal_de_consumo - bonificacion_correspondiente

    subtotal = restar_bonificacion

    print(f"El subtotal con la bonificacion es {subtotal}")
else:
    subtotal = subtotal_de_consumo

recargo_correspondiente = subtotal * recargo

if recargo > 0:
    print(f"Corresponde una recargo de +{recargo_correspondiente}")

    sumar_recargo = subtotal + recargo_correspondiente
    subtotal = sumar_recargo
    print(f"El subtotal con recargo es {subtotal}")
else:
    pass


print(f"Se aplica el cargo fijo de +{cargo_fijo}")
subtotal = subtotal + cargo_fijo

if descuento_adicional > 0:
    descuento_correspondiente = subtotal * descuento_adicional
    restar_descuento = subtotal - descuento_correspondiente
    subtotal = restar_descuento
    print(f"Corresponde un descuento especial de {descuento_correspondiente}")
    print(f"El subtotal con descuento correspondiente es {subtotal}")

iva_total = subtotal * iva
sumar_iva = subtotal + iva_total
subtotal = sumar_iva


print(f"Corresponde un IVA de {iva_total}")

print(f"El subtotal con IVA es: {subtotal}")



print(f"El total a pagar es: {subtotal}")