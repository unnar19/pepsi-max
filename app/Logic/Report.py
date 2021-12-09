import json
from Logic.Base import Base
json

class Report(Base):
    
    def __init__(self) -> None:
        super().__init__("report")

    def get_all(self, data: json) -> json:
        return super().get_all(data)

    def get(self, data: json) -> json:
        return super().get(data)

    def post(self, data: json) -> json:
        return super().post(data)

    def put(self, data: json) -> json:
        return super().put(data)

    def delete(self, data: json) -> json:
        return super().delete(data)
    
    #report specific functions:



