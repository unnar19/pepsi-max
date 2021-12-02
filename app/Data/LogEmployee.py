import json
from Data.LogBase import LogBase
from Exceptions import *

class LogEmployee(LogBase):

    def __init__(self) -> None:
        super().__init__("employee")

    def get_all(self):
        return super().get_all()

    def post(self, data: json):
        return super().post(data)

    def put(self, data: str):
        return super().put(data)

    def __is_empty(self):
        return super().__is_empty()

    def __validate_json(self, data: str):
        return super().__validate_json(data)

    def __get_all_dict(self) -> dict:
        return super().__get_all_dict()

    def __get_next_id(self):
        return super().__get_next_id()

if __name__ == "__main__":
    pass
