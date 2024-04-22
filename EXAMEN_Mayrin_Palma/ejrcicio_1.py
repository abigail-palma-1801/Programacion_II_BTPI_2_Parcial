
salir = False

while not salir:
    print("-----Menu-----")
    print("1. Comprobar Numero")
    print("0. Salir")
     
    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir = True
    elif(opt == '1'):
        numero1 = int(input("Ingrese un numero: "))
        
        if(numero1 %2):
            print(f"El numero {numero1} es impar")
        else:
            print(f"El numero {numero1} es par")

numero1 +1

# salir = False

# while not salir:
#     print("-----Menu-----")
#     print("1. Comprobar Numero")
#     print("0. Salir")
     
#     opt = input("Ingrese una opcion: ")

#     if(opt == '0'):
#         salir = True
#     elif(opt == '1'):
#         numero1 = int(input("Ingrese un numero: "))

#         if(numero1 %2 == 0):
#             print('el numero es par')
#         else:
#             print('el numero no es par')
#     else:
#         print('Opcion no valida')