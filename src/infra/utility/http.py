from werkzeug.local import LocalProxy


class Http:
    def __init__(self):
        pass

    @staticmethod
    def handle_generic_http_error(err):
        return {
                'status': False,
                'error': str(err)
        }

