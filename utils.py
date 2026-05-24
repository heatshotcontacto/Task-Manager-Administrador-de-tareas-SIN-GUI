# Funcion para validar el menú 
def mostrar_menu():
    while True:
        try:
            opcion = int(input('-- GESTOR DE TAREAS --- \n Ingrese una opcion \n 1. Añadir tarea \n 2. Eliminar tarea \n 3. Ver tareas \n 4. Completar tareas \n 5. Salir \n Opcion:'))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print('Opción invalida')
        except ValueError:
            print('Ingrese solo números')