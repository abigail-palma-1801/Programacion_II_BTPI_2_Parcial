from menu import imprimir_menu


salir = False

while not salir:
    imprimir_menu()
    resp = input("Ingrese una opcion: ")

    if resp =='0':
        salir = True
    elif resp == '1':
        pass
    elif resp == '2':
        pass
    elif resp == '3':
        pass
    elif resp == '4':
        pass
    elif resp == '5':
        pass
    else:
        print(f"la opcion '{resp}' no es valida ")