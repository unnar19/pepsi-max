import json
from Data.LogBase import LogBase
from Exceptions import *

class LogTicket(LogBase):

    def __init__(self) -> None:
        super().__init__("ticket")

    def get_all(self):
        return super().get_all()

    def post(self, data: json):
        return super().post(data)

    def put(self, data: str):
        return super().put(data)


if __name__ == "__main__":
    pass
