from flask import jsonify,request
from src.infra.utility.http import Http
import src.infra.http.auth as auth
import src.controller.uploadfile as uploadfile
import flask


def route(app: flask.app.Flask):
    @app.route('/uploadfile', methods=['POST'])
    @auth.requires_auth
    def request_post_import():
        try:
            response = uploadfile.uploadfile(request)

            return jsonify(response), 200

        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500