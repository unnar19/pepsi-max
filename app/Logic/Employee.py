from Logic.Base import Base
from Exceptions import *
import json

class Employee(Base):
    
    def __init__(self) -> None:
        return super().__init__("employee")

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

    def authenticate(self, data: json) -> json:
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
                    raise IncorrectCredentialsException(self._key, 'AUTH')

                # Return session variables
                else:
                    return json.dumps({"type": "object", "data": {"name": val["name"], "role": val["role"], "id":key, "destination":val["destination"]}})

        # Email not found..
        raise IncorrectCredentialsException(self._key, 'AUTH')