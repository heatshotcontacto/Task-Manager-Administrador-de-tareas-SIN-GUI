programa_activo = True # Booleando que indica si esta encendido (True) o apagado (False)
tareas = [] # Lista vacia en la cual se guardaran los datos que se añadan
def agregar_tarea():
    titulo = input('Ingrese su tarea: ')
    tarea = {"titulo" : titulo, "completada" : False} # Variable de diccionario que se guarda con el nombre de la tarea
    tareas.append(tarea) # Del diccionario qeu se creo aprende en la lista vacia
    print(f'Tarea añadida : {tarea["titulo"]}') 
while programa_activo: # Inicio del bucle, se pone la variable programa_activo y dependiendo si es True o False se ejecutara o no
    try: # Ejecuta si todo esta super bien y pone números enteros o int
        menu = int(input('Ingrese una opcion \n 1. Añadir tarea \n 2. Eliminar tarea \n 3. Salir \n 4. Ver tareas \n Opcion: '))
        if menu == 1:
            titulo = input('Ingrese su tarea: ')
            tarea = {"titulo" : titulo, "completada" : False} # Variable de diccionario que se guarda con el nombre de la tarea
            tareas.append(tarea) # Del diccionario qeu se creo aprende en la lista vacia
            print(f'Tarea añadida : {tarea["titulo"]}')
        elif menu == 2:
            #if len(tareas) == 0:
            if not len(tareas):
                print('No hay tareas por eliminar')
            else:
                while True:
                    try:
                        for indice, tarea in enumerate(tareas): # numera cada cosa del diccionario que guardamos 
                            print(f'{indice + 1}. {tarea["titulo"]}') # imprime el mesane y le suma + 1 para que el usuario pueda entender
                        numero_usuario = int(input('Seleccione que tarea desea eliminar: '))
                        indice_real = numero_usuario - 1 # para que python entienda se le resta un menos -1 para que al mometno del que el usuario ponga 1 en realidadd sea 0
                        #if 0 < numero_usuario <= len(tareas):
                        if 0 <= numero_usuario < len(tareas): # Es más profecional 
                            tarea_eliminada = tareas.pop(indice_real) # con .pop eliminamos el dato 
                            print(f'Usted elimino la tarea {tarea_eliminada["titulo"]}') # Aqui se elimina segun el número que haya peusto el usuario
                            break
                        else:
                            print('Número Invalido')
                    except ValueError:
                        print('Ingrese nuevamente sus datos')
            #print(f'Usted elimino la tarea {tarea["titulo"]}') # Aqui se elimina segun el número que haya peusto el usuario
        elif menu == 3:
           print('Salir')
           programa_activo = False  #Asigna de variable False y se detiene el programa
        elif menu == 4:
            #if len(tareas) == 0:
            if not len(tareas): # Más profecional
                print('No hay tareas pendientes')
            else:
                for indice, tarea in enumerate(tareas):
                    if not tarea["completada"]: # Se usa esto de manera más procecional
                    #if tarea["completada"] == False:
                        estado = 'Pendiente' # Uso de variables temporales
                    else:
                        estado = 'Completada' # Uso de variables temporales
                    print(f'{indice + 1}. {tarea["titulo"]} esta {estado}')
        else:
            print('Opción Invalida')
    except ValueError: # Imprime si el dato es invalido (Por si añade texto o str a la condicion)
        print('Debe ingresar solo números')