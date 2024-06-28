from menu import imprimir_menu
from datos import crear_tarea,obtener_todas_las_tareas
import json

salir = True


#with open('test.json') as testF:
 #   texto = testF.read()
 #   print(texto)
#
 #   data = json.loads(texto)
 #   print(data)
 #   print(data['usuarios'])


test_data= {
    'texto': 'Hola Mundo',
    'estado': True,
    'valor': 3.1
}

print(test_data)

json_text = json.dumps(test_data)
print(json_text)

with open('datos.json','w') as datos_file:
    datos_file.write(json_text)
    datos_file.close()


while not salir:
    imprimir_menu()
    resp = input("Ingrese una opcion: ")

    if resp =='0':
        salir = True
    elif resp == '1':
        print('\n------ Todas las Tareas------')
        Tareas = obtener_todas_las_tareas()
        for Tarea in Tareas:
            index = Tareas.index(Tarea)
            print(f'{index + 1}. {Tarea['titulo']}')
    elif resp == '2':
        pass
    elif resp == '3':
        pass
    elif resp == '4':
        titulo_tarea = input('ingrese la nueva tarea: ')
        crear_tarea(titulo_tarea)
        print('\nTarea Agregada!\n\n')
    elif resp == '5':
        pass
    else:
        print(f"la opcion '{resp}' no es valida ")