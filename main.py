# importación de librerías 
from utils import mostrar_menu
from tasks import agregar_tarea
from tasks import eliminar_tarea
from tasks import mostrar_tareas
from tasks import completar_tareas
from storage import guardar_tareas
from storage import cargar_tareas
programa_activo = True # Booleando que indica si esta encendido (True) o apagado (False)
tareas = cargar_tareas() # Lista vacia en la cual se guardaran los datos que se añadan
while programa_activo: # Inicio del bucle, se pone la variable programa_activo y dependiendo si es True o False se ejecutara o no
    menu = mostrar_menu()
    if menu == 1:
        agregar_tarea(tareas)
        guardar_tareas(tareas)
    elif menu == 2:
        eliminar_tarea(tareas)
        guardar_tareas(tareas)
    elif menu == 3:
        mostrar_tareas(tareas)
    elif menu == 4:
        completar_tareas(tareas)
        guardar_tareas(tareas)
    elif menu == 5:
        print('Salir')
        programa_activo = False  #Asigna de variable False y se detiene el programa
    else:
            print('Opción Invalida')
    
    
