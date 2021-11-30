import Data.DataWrapper as DataWrapper
import json
from Exceptions import *

class Employee:

    def __init__(self) -> None:
        self.id = None
        self.role = None
        self.data_wrapper = DataWrapper()

    def authenticate(self, credentials: str):
        """
        1. Parse json from UI
        2. Check if username is registered
        3. Check if passwords match
        4. Return id
        """
        
        # Start by parsing json credentials
        ui_load = json.loads(credentials)
        username, password = ui_load['username'], ui_load['password']

        # If username is registered, DataWrapper._authenticate_user returns id and registered password
        data_load = json.loads(
            self.data_wrapper.get_employee(
                json.dumps({"username":username})))

        # If username is not registered, data_load['type'] = False
        if not data_load['type']:
            raise IncorrectUsernameException
        
        # If username is registered, data_load['type'] = 'object'
        else:

            # If passwords don't match, raise exception
            id_, role, registered_password = data_load['data']['id'], data_load['data']['role'], data_load['data']['password']
            if password != registered_password:
                raise IncorrectPasswordException

            # If user is authenticated, Employee() instance is
            # assigned ID and role. Method returns True
            else:

                self.id = id_
                self.role = role
                return True

    def get_all(self):
        return self.data_wrapper.get_employees_all()

    def get(self, id_: str):
        return self.data_wrapper.get_employee(id_)

    def post(self, data: str):
        if self.__is_boss():
            return self.data_wrapper.post_employee(data)
        else:
            raise UnauthorizedReguestException

    def put(self, data: str):
        if self.__is_boss():
            return self.data_wrapper.put_employee(data)
        else:
            raise UnauthorizedReguestException

    def __is_boss(self):
        return self.role == 'Boss'






