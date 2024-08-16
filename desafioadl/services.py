from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    return {'tareas': tareas, 'subtareas': subtareas}

def crear_nueva_tarea(descripcion, eliminada=False):
    tarea = Tarea.objects.create(descripcion=descripcion, eliminada=eliminada)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion, eliminada=False):
    tarea = Tarea.objects.get(id=tarea_id)  # Obtener la instancia de Tarea
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion, eliminada=eliminada)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    Tarea.objects.filter(id=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.filter(id=subtarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(tareas_y_subtareas):
    for tarea in tareas_y_subtareas['tareas']:
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in tarea.subtareas.all():
            print(f".... [{subtarea.id}] {subtarea.descripcion}")
