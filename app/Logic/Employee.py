import Data.DataAPI as DataAPI
import json
from Exceptions import *

class Employee:

    def __init__(self) -> None:
        self.data_api = DataAPI()

    def authenticate(self, data: str):
        """
        1. Parse json from UI
        2. Check if username is registered
        3. Check if passwords match
        4. Return id
        """
        
        # Start by parsing json data
        ui_load = json.loads(data)
        username, password = ui_load['data']['username'], ui_load['data']['password']

        # If username is registered, DataAPI._authenticate_user returns id and registered password
        data_load = json.loads(
            self.data_api.get_employee(
                json.dumps({"username":username})))

        # If username is not registered, data_load['type'] = False
        if not data_load['type']:
            raise IncorrectUsernameException
        
        else:

            # If passwords don't match, raise exception
            id_, role, registered_password = data_load['data']['id'], data_load['data']['role'], data_load['data']['password']
            if password != registered_password:
                raise IncorrectPasswordException

            # If user is authenticated, method returns json(id_ , role)
            else:
                return json.dumps({"id":id_, "role":role})

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
        return data['role'] == 'Boss'






