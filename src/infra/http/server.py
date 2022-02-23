from flask import Flask
from src.infra.utility.environment import EnvironmentVariables
import glob
import os
from importlib import import_module


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.secret_key = 'development'

    def _build_routes(self):
        path_folder_route = "./src/infra/http/route"
        import_base = "src.infra.http.route"
        for path in glob.glob(f"{path_folder_route}/*.py"):
            filename = os.path.basename(path).replace(".py", "")
            module_import = f"{import_base}.{filename}"
            try:
                import_module(module_import).route(self.app)
            except (ImportError, AttributeError):
                raise ImportError(module_import)

        return self

    def build(self):
        self._build_routes() \
            .app.run(debug=False,
                     host='0.0.0.0',
                     port=EnvironmentVariables.get_system_port(),
                     threaded=True
                     )


def run():
    server = Server()
    server.build()
