import os
import config
import dotenv


def load_dotenv():
    try:
        python_env = os.environ['PYTHON_ENV']
    except Exception as err:
        python_env = "local"

    path = "%s/env/%s.env" % (config.base_path, python_env)
    dotenv.load_dotenv(dotenv_path=path)

class EnvironmentVariables:
    def __init__(self):
        pass

    @staticmethod
    def get_system_port() -> int:
        return os.getenv("PORT")

    @staticmethod
    def get_basic_auth_user() -> str:
        return os.getenv("AUTH_USER")

    @staticmethod
    def get_basic_auth_password() -> str:
        return os.getenv("AUTH_PASSWORD")

    @staticmethod
    def get_base_path() -> str:
        if "base_path" in config.__dict__:
            response = config.base_path
        else:
            response = "."
        return response
