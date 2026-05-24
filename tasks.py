# Funcion para agregar tareas
def agregar_tarea(lista_tareas):
    titulo = input('Ingrese su tarea: ')
    tarea = {"titulo" : titulo, "completada" : False} # Variable de diccionario que se guarda con el nombre de la tarea
    lista_tareas.append(tarea) # Del diccionario qeu se creo aprende en la lista vacia
    print(f'Tarea añadida : {tarea["titulo"]}') 
# Funcion para eliminar tareas
def eliminar_tarea(lista_tareas):
    #if len(tareas) == 0:
    #if not len(lista_tareas):
    if not lista_tareas:
        print('No hay tareas por eliminar')
    else:
        while True:
            try:
                for indice, tarea in enumerate(lista_tareas): # numera cada cosa del diccionario que guardamos 
                    print(f'{indice + 1}. {tarea["titulo"]}') # imprime el mesane y le suma + 1 para que el usuario pueda entender
                numero_usuario = int(input('Seleccione que tarea desea eliminar: '))
                indice_real = numero_usuario - 1 # para que python entienda se le resta un menos -1 para que al mometno del que el usuario ponga 1 en realidadd sea 0
                #if 0 < numero_usuario <= len(tareas):
                if 0 <= indice_real < len(lista_tareas): # Es más profecional 
                    tarea_eliminada = lista_tareas.pop(indice_real) # con .pop eliminamos el dato 
                    print(f'Usted elimino la tarea {tarea_eliminada["titulo"]}') # Aqui se elimina segun el número que haya peusto el usuario
                    break
                else:
                    print('Número Invalido')
            except ValueError:
                print('Ingrese solo números')
        #print(f'Usted elimino la tarea {tarea["titulo"]}') # Aqui se elimina segun el número que haya peusto el usuario
# Funcion para mostrar tareas
def mostrar_tareas(lista_tareas):
    #if len(tareas) == 0:
    #if not len(lista_tareas):
    if not lista_tareas: # Más profecional    
        print('No hay tareas pendientes')
    else:
        for indice, tarea in enumerate(lista_tareas):
            if not tarea["completada"]: # Se usa esto de manera más profecional
            #if tarea["completada"] == False:
                estado = 'Pendiente' # Uso de variables temporales
            else:
                estado = 'Completada' # Uso de variables temporales
            print(f'{indice + 1}. {tarea["titulo"]} esta {estado}')
# Funcion para completar tareas
def completar_tareas(lista_tareas):
    if not lista_tareas: # Si no hay tareas por completar "FALSE"
        print('No hay tareas por completar')
    else:
        while True:
            try:
                for indice, tarea in enumerate(lista_tareas): # numera cada cosa del diccionario que guardamos 
                    if tarea["completada"]: # Se usa esto de manera más profecional  
                        estado = 'Completada' # Uso de variables temporales
                    else:
                        estado = 'Pendiente'
                    print(f'{indice + 1}. {tarea["titulo"]}, estado: {estado}') # imprime las tareas enumeradas y con su estado
                numero_usuario = int(input('Seleccione que tarea desea completar: '))
                indice_real = numero_usuario - 1 # para que python entienda se le resta un menos -1 para que al mometno del que el usuario ponga 1 en realidadd sea 0
                #if 0 < numero_usuario <= len(tareas):
                if 0 <= indice_real < len(lista_tareas): # Es más profecional 
                    if lista_tareas[indice_real]["completada"]:
                        print('La tarea ya está completada')
                    else:
                        lista_tareas[indice_real]["completada"] = True
                        print(
                            f'Tarea completada: {lista_tareas[indice_real]["titulo"]}')
                        break
                else:
                    print('Número inválido')
            except ValueError:
                print('Ingrese solo números')