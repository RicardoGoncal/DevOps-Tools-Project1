from flask import jsonify
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.avg_car_make as avg_car_make
import flask


def route(app: flask.app.Flask):
    @app.route('/avgfabricante', methods=['GET'])
    @auth.requires_auth
    def request_get_avg_fabricante():
        try:
            response = avg_car_make.avg_car_make()

            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500