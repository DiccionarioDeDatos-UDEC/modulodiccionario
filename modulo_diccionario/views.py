# modulo_diccionario/views.py
import os
import json
from flask import Blueprint, jsonify, request
from .services import (
    servicio_agregar_tabla,
    servicio_obtener_tablas,
    verificar_nombre_tabla_existente
)
from .models import cargar_datos_json

modulo_diccionario = Blueprint('modulo_diccionario', __name__)


@modulo_diccionario.route('/tablas', methods=['GET'])
def get_tablas():
    tablas = servicio_obtener_tablas()
    return jsonify(tablas)

@modulo_diccionario.route('/tablas/agregar', methods=['POST'])
def post_tabla():
    data = request.json
    nombre = data.get("nombre")
    descripcion = data.get("descripcion")
    columnas = data.get("columnas", [])

    if verificar_nombre_tabla_existente(nombre):
        return jsonify({"error": "Ya existe una tabla con ese nombre."}), 400

    servicio_agregar_tabla(nombre, descripcion, columnas)
    return jsonify({"message": "Tabla agregada con éxito."}), 201


@modulo_diccionario.route('/estadisticas', methods=['GET'])
def get_estadisticas():
    data = cargar_datos_json()
    # Contar las tablas en "ejemplos_tablas" y actualizar "total_tablas"
    data["estadisticas"]["total_tablas"] = len(data.get("ejemplos_tablas", []))
    return jsonify({"estadisticas": data["estadisticas"]})