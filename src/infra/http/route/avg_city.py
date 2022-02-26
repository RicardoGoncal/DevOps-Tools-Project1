from flask import jsonify
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.avg_city as avg_city
import flask


def route(app: flask.app.Flask):
    @app.route('/avgcity', methods=['GET'])
    @auth.requires_auth
    def request_get_avg_city():
        try:
            response = avg_city.avg_city()

            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500