import json #Usar datos en JSon 
from .models import cargar_datos_json, guardar_datos_json, agregar_tabla, obtener_tablas, obtener_columnas_de_tabla, agregar_relacion, obtener_relaciones, eliminar_relacion 

#Agregar tabla
def servicio_agregar_tabla(nombre, descripcion, columnas):
    if verificar_nombre_tabla_existente(nombre):
        return False  
        #Si ya esxiste no deja 
    agregar_tabla(nombre, descripcion, columnas) #AlonDur
    return True  # Se agregó con éxito

def verificar_nombre_tabla_existente(nombre):
    tablas = obtener_tablas()  # Esta función debe devolver todas las tablas para ver si hay una con ese nombre
    return any(tabla['nombre'] == nombre for tabla in tablas)  # Compara el nombre


def servicio_obtener_tablas():    #Retorna las tablas
    return obtener_tablas()

def servicio_obtener_columnas(nombre_tabla):    #Retorna las columnas
    return obtener_columnas_de_tabla(nombre_tabla)

def crear_relacion(tabla_origen, columna_origen, tabla_destino, columna_destino, tipo_relacion):     #Crea relacion 
   #AlonDur
    agregar_relacion(tabla_origen, columna_origen, tabla_destino, columna_destino, tipo_relacion)

def listar_relaciones():
    return obtener_relaciones()

def borrar_relacion(tabla_origen, tabla_destino):
    eliminar_relacion(tabla_origen, tabla_destino)






