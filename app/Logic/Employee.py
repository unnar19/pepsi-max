from Logic.Base import Base
from Exceptions import *
import json

class Employee(Base):
    
    def __init__(self) -> None:
        super().__init__("employee", "email")

    def get_all(self, data: str):
        return super().get_all(data)

    def get(self, data: str):
        return super().get(data)

    def post(self, data: str):
        return super().post(data)

    def put(self, data: str):
        return super().put(data)

    def authenticate(self, data: str):
        # Parse user input
        ui_load = json.loads(data)['data']
        email, password = ui_load['email'], ui_load['password']

        # Parse DB response
        data_load = json.loads(self.get_all(data))['data']

        # Search submitted email address in DB
        for key, val in data_load.items():
            if val['email'] == email:

                # Check password
                if password != val["password"]:
                    raise IncorrectPasswordException

                # Return session variables
                else:
                    return json.dumps({"data": {"name": val["name"], "role": val["role"], "id":key}})

        # Email not found..
        raise IncorrectEmailException








