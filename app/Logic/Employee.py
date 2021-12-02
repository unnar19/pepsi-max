import json
from Data.DataAPI import DataAPI
from Exceptions import *

class Employee:

    def __init__(self) -> None:
        self.data_api = DataAPI()

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

    def get_all(self, data: str):
        return self.data_api.get_all(data)

    def get(self, data: str):
        return self.data_api.get(data)

    def post(self, data: str):
        if self.__is_boss(data):
            return self.data_api.post(data)
        else:
            raise UnauthorizedReguestException

    def put(self, data: str):
        if self.__is_boss(data):
            return self.data_api.put(data)
        else:
            raise UnauthorizedReguestException

    def __is_boss(self, data: str):
        # Maybe an id_ authentication, returning the role would be better here
        return json.loads(data)['role'] == 'Boss'






