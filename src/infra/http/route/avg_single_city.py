from flask import jsonify, request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.avg_single_city as avg_single_city
import flask


def route(app: flask.app.Flask):
    @app.route('/avgsiglecity/<city>', methods=['GET'])
    @auth.requires_auth
    def request_get_avg_single_city(city):
        try:
            response = avg_single_city.avg_single_city(city)

            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500