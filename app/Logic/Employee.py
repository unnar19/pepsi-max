import json
from Data.DataAPI import DataAPI
from Exceptions import *

class Employee:

    def __init__(self) -> None:
        self.data_api = DataAPI()

    def authenticate(self, data: str):
        # Parse user input
        ui_load = json.loads(data)['data']
        ui_email, ui_password = ui_load['email'], ui_load['password']

        # Parse DB response
        data_load = json.loads(self.get_all(data))['data']

        id_ = ''

        for key, val in data_load.items():
            if val['email'] == ui_email:
                id_ = key
                password = val['password']
                role = val['role']
                name = val['name']
                break

        if not id_:
            raise IncorrectEmailException

        elif ui_password != password:
            raise IncorrectCredentialsException

        else:
            return json.dumps({"data": {"name": name, "role": role, "id":id_}})



        
        


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






