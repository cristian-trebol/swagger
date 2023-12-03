from flask import Blueprint
from flask_restx import Api
from user import api as ejemplo_api

# Crear un Blueprint para las rutas
routes_blueprint = Blueprint('routes', __name__)

# Crear un objeto Api para el Blueprint
api = Api(routes_blueprint)

# Agregar el espacio de nombres y el recurso al objeto Api del Blueprint
api.add_namespace(ejemplo_api, path='/user')
