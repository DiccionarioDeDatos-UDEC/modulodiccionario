from flask import Blueprint
from .views import modulo_diccionario
# Crear el Blueprint
modulo_diccionario = Blueprint('modulo_diccionario', __name__)

# Importar las vistas para evitar problemas de importación circular
from .views import *
