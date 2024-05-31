from uuid import uuid4

_tareas = []

def crear_tarea(Titulo: str):
    nueva_tarea = {
        'id': uuid4(),
        'titulo': Titulo,
        'completada': False
    }

    _tareas.append(nueva_tarea)

def obtener_todas_las_tareas():
    return _tareas