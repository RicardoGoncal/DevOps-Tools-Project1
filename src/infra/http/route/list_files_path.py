from flask import jsonify,request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.list_files_path as list_files_path
import flask


def route(app: flask.app.Flask):
    @app.route('/listfilespath', methods=['GET'])
    @auth.requires_auth
    def request_get_files_path():
        try:
            response = list_files_path.list_files_path()

            return jsonify(response), 200

        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500