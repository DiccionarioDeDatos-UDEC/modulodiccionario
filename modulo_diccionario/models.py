# modulo_diccionario/models.py
import json
import os

# Ruta del archivo JSON
JSON_FILE_PATH = os.path.join('instance', 'diccionario.json')

def cargar_datos_json():
    """Carga datos desde el archivo JSON o retorna estructuras vacías."""
    if not os.path.exists(JSON_FILE_PATH):
        return {
            "ejemplos_tablas": [],
            "relaciones": [],
            "estadisticas": {
                "total_tablas": 0,

            }
        }
    
    with open(JSON_FILE_PATH, 'r') as file:
        return json.load(file)

        # Actualizar el conteo de tablas en "estadisticas"
    data["estadisticas"]["total_tablas"] = len(data.get("ejemplos_tablas", []))
    return data

def guardar_datos_json(data):
    """Guarda datos en el archivo JSON."""
    try:
        with open(JSON_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error al guardar datos: {e}")

# Funciones para manejar tablas
def agregar_tabla(nombre, descripcion, columnas):
    """Agrega una nueva tabla con sus columnas al archivo JSON."""
    data = cargar_datos_json()
    nuevo_id = len(data["ejemplos_tablas"]) + 1  # Generar un nuevo ID
    nueva_tabla = {
        'id': nuevo_id,
        'nombre': nombre,
        'descripcion': descripcion,
        'columnas': columnas,
        'registros': []  # Inicializar la clave 'registros' como una lista vacía
    }
    data["ejemplos_tablas"].append(nueva_tabla)

    # Actualizar estadísticas al agregar una nueva tabla
    data["estadisticas"]["total_tablas"] += 1

    guardar_datos_json(data)

def obtener_tablas():
    """Devuelve la lista de tablas con columnas."""
    return cargar_datos_json()["ejemplos_tablas"]
