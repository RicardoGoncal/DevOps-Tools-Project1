from src.infra.utility.environment import load_dotenv
import src.infra.http.server as server
import config
import os


if __name__ == '__main__':
    config.base_path = os.path.dirname(__file__)
    load_dotenv()
    server.run()
