from flask import jsonify
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.example as example
import flask


def route(app: flask.app.Flask):
    @app.route('/example', methods=['GET'])
    @auth.requires_auth
    def request_get_example():
        try:
            response = example.get()

            return jsonify(response), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500

    @app.route('/example', methods=['POST'])
    @auth.requires_auth
    def request_post_example():
        try:
            response = example.post()

            return jsonify(response), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
