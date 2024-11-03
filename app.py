from flask import Flask
from flask_cors import CORS  # Importa CORS
from modulo_diccionario.views import modulo_diccionario


app = Flask(__name__)

# Configura CORS
CORS(app)  # Permite solicitudes desde cualquier origen

# Registra los Blueprints
app.register_blueprint(modulo_diccionario)


if __name__ == '__main__':
    app.run(debug=True)
