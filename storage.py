import json
# Guardar tareas
def guardar_tareas(lista_tareas):
    with open("data/tasks.json", "w") as archivo:
        json.dump(lista_tareas, archivo, indent=4)
# Cargar tareas
def cargar_tareas():
    try:
        with open("data/tasks.json", "r") as archivo:
            tareas = json.load(archivo)
            return tareas
    except (FileNotFoundError, json.JSONDecodeError):
        return []