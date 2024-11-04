import os
import json
from flask import Blueprint, jsonify, request   #Reponder Y solicitudes
from .services import (
    servicio_agregar_tabla,
    servicio_obtener_tablas,
    crear_relacion,
    listar_relaciones,
    borrar_relacion,
    servicio_obtener_columnas,
    verificar_nombre_tabla_existente
)
from .models import cargar_datos_json

modulo_diccionario = Blueprint('modulo_diccionario', __name__) #Organizar rutas


@modulo_diccionario.route('/tablas', methods=['GET'])
def get_tablas():
    #obtene tablas
    tablas = servicio_obtener_tablas()
    return jsonify(tablas) #AlonDur

@modulo_diccionario.route('/tablas/<string:nombre_tabla>/columnas', methods=['GET'])
def get_columnas(nombre_tabla):    #Columnas de una tabla en co,un 
    columnas = servicio_obtener_columnas(nombre_tabla)
    return jsonify(columnas)

@modulo_diccionario.route('/tablas/agregar', methods=['POST'])
def post_tabla():
    data = request.json
    nombre = data.get("nombre")
    descripcion = data.get("descripcion")
    columnas = data.get("columnas", [])

    if verificar_nombre_tabla_existente(nombre):
        return jsonify({"error": "Ya existe una tabla con ese nombre."}), 400 #msg

    servicio_agregar_tabla(nombre, descripcion, columnas)
    return jsonify({"message": "Tabla agregada con éxito."}), 201     #msg


@modulo_diccionario.route('/estadisticas', methods=['GET'])
def get_estadisticas():
    data = cargar_datos_json()    #actualizar estadisticas de tablas dashboard
    data["estadisticas"]["total_tablas"] = len(data.get("ejemplos_tablas", []))
    return jsonify({"estadisticas": data["estadisticas"]})

@modulo_diccionario.route('/relaciones', methods=['GET'])
def obtener_relaciones_endpoint():
    relaciones = listar_relaciones()
    return jsonify(relaciones), 200

@modulo_diccionario.route('/relaciones', methods=['POST'])
def agregar_nueva_relacion():
    data = request.json
    tabla_origen = data.get('tabla_origen')
    columna_origen = data.get('columna_origen')
    tabla_destino = data.get('tabla_destino')
    columna_destino = data.get('columna_destino')
    tipo_relacion = data.get('tipo_relacion')
#AlonDur
   
    if not all([tabla_origen, columna_origen, tabla_destino, columna_destino, tipo_relacion]):    #Calida que los campos esten ocupados
        return jsonify({"message": "Todos los campos son requeridos."}), 400

    try:
        crear_relacion(tabla_origen, columna_origen, tabla_destino, columna_destino, tipo_relacion)
        return jsonify({"message": "Relación creada exitosamente."}), 201
    except Exception as e:
        print(f"Error al crear relación: {e}") 
        return jsonify({"message": "Error al crear relación."}), 500

@modulo_diccionario.route('/relaciones', methods=['DELETE'])
def eliminar_relacion():
    data = request.get_json()

    tabla_origen = data.get('tabla_origen')
    tabla_destino = data.get('tabla_destino')

    if not tabla_origen or not tabla_destino:
        return jsonify({"message": "Datos inválidos"}), 400

    try:
       
        borrar_relacion(tabla_origen, tabla_destino)  
        return '', 204 
    except Exception as e:
        print(f"Error al eliminar relación: {e}")  # Registra el error en la consola
        return jsonify({"message": "Error al eliminar relación."}), 500
