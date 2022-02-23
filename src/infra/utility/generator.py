from datetime import datetime
from random import uniform

class Generator:
    def __init__(self):
        pass

    @staticmethod
    def date_now_isoformat():
        return datetime.now().date().isoformat()

    @staticmethod
    def radom_string_number() -> str:
        now = str(round(datetime.timestamp(datetime.now())))
        random_variable = str(int(uniform(0, 1000000)))

        return now + random_variable
