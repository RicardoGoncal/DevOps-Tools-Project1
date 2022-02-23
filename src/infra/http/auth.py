
from flask import jsonify, request
from functools import wraps
from src.infra.utility.environment import EnvironmentVariables

def check_auth(username, password):
    """Função utilizada para validar o username e o password
    com base no padrão apresentado em .env
    """
    return username == EnvironmentVariables.get_basic_auth_user() and password == EnvironmentVariables.get_basic_auth_password()

def authenticate():
    """Sends a 401 response that enables basic auth"""
    response = {
        'status': False,
        'message': 'Unauthorized'
    }
    return jsonify(response), 401

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated