sueldo_mensual = int(input("Ingrses su sueldo del mes: "))

if(sueldo_mensual > 7000):
    impuestos = sueldo_mensual * 0.08
    print(f"debe pagar {impuestos} de impuestos")
else:
    print("no debe pagar impuestos")

# sueldo_mensual = float(input("Ingrese su sueldo: "))

# if(sueldo_mensual > 7000):
#     impuestos = sueldo_mensual * 0.08
#     print("El saldo a pagar es: " + str(impuestos))
# else:
#     print("No tiene que pagar nada.")