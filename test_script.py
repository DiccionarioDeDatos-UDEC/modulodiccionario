import json
import os

# Ruta al archivo JSON
JSON_FILE_PATH = 'modulo_ddl_dml/data.json' 

def cargar_datos_json():    #Carga datos de Json e inicia estructura
    print("Cargando datos JSON...")  # Mensaje de depuración
    if not os.path.exists(JSON_FILE_PATH):
        inicializar_archivo_json()
    #AlonDur
    with open(JSON_FILE_PATH, 'r') as file:
        data = json.load(file)
        print("Datos cargados:", data)  
        return data

def inicializar_archivo_json():
    if not os.path.exists('modulo_ddl_dml'):
        os.makedirs('modulo_ddl_dml')  
    #AlonDur
    data_inicial = {"tablas": {}}
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data_inicial, file, indent=4)
    print(f"Archivo {JSON_FILE_PATH} creado y inicializado.")  

def guardar_datos_json(data):
    """Guarda datos en el archivo JSON."""
    try:
        with open(JSON_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error al guardar datos: {e}")
#AlonDur
def agregar_tabla(nombre_tabla, columnas):    #Agrega tabla
    data = cargar_datos_json()
    if nombre_tabla not in data['tablas']:
        data['tablas'][nombre_tabla] = {'columnas': columnas}
        guardar_datos_json(data)
        print(f"Tabla '{nombre_tabla}' agregada con columnas: {columnas}")
    else:
        print(f"La tabla '{nombre_tabla}' ya existe.")

if __name__ == "__main__":
    data = cargar_datos_json()
    print("Datos iniciales:", data)
    #AlonDur
    agregar_tabla("test_table", ["col1", "col2"])
    
    # Listar tablas
    print("Tablas después de agregar:", cargar_datos_json()['tablas'])
