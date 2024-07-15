

def crear_usuario(nombre:str, alumnos:int, horas_clase:int, estado:bool=True):
    if nombre == 'Abigail':
        print('El nombre es Abigail')
        
    crear_clase = {
        'nombre': nombre,
        'alumnos': alumnos,
        'horas_clase': horas_clase,
        'estado': estado
        }

    return crear_clase

usuario_1 = crear_usuario('Matematicas','50','20')

print(usuario_1)