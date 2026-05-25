# Task Manager 📝

Task Manager es una aplicación de consola desarrollada en Python que permite gestionar tareas de manera sencilla.

El programa permite:

- Añadir tareas
- Eliminar tareas
- Ver tareas
- Marcar tareas como completadas
- Guardar tareas automáticamente usando JSON

---

# Tecnologías utilizadas

- Python 3
- JSON
- Programación modular
- Manejo de archivos
- Funciones (`def`)
- Manejo de errores (`try-except`)

---

# Estructura del proyecto

```bash
TASK MANAGER/
│
├── data/
│   └── tasks.json
│
├── main.py
├── README.md
├── storage.py
├── tasks.py
└── utils.py
```

---

# Explicación de archivos

## `main.py`

Archivo principal del programa.

Se encarga de:

- Ejecutar el sistema
- Controlar el menú principal
- Gestionar la interacción entre módulos
- Ejecutar las funciones principales del Task Manager

---

## `tasks.py`

Contiene todas las funciones relacionadas con la gestión de tareas.

Funciones incluidas:

- `agregar_tarea()`
- `eliminar_tarea()`
- `mostrar_tareas()`
- `completar_tareas()`

---

## `storage.py`

Módulo encargado de la persistencia de datos usando archivos JSON.

Funciones incluidas:

- `guardar_tareas()`
- `cargar_tareas()`

---

## `utils.py`

Contiene funciones auxiliares del sistema.

Actualmente incluye:

- `mostrar_menu()`

---

## `data/tasks.json`

Archivo donde se almacenan las tareas de forma permanente.

Permite mantener la información guardada incluso después de cerrar el programa.

---

# Cómo ejecutar el proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/heatshotcontacto/Task-Manager-Administrador-de-tareas-SIN-GUI.git
```

## 2. Entrar a la carpeta del proyecto

```bash
cd Task-Manager-Administrador-de-tareas-SIN-GUI
```

## 3. Ejecutar el programa

```bash
python main.py
```

---

# Ejemplo de uso

```text
1. Añadir tarea
2. Eliminar tarea
3. Ver tareas
4. Completar tareas
5. Salir
```

---

# Características

- ✅ Validación de entradas
- ✅ Persistencia de datos con JSON
- ✅ Estructura modular
- ✅ Manejo de errores
- ✅ Menú interactivo
- ✅ Guardado automático de tareas

---
# No tomar en cuenta (Logica principal)
```text 
ejemplo.py
```

