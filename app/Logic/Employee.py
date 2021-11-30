import Data.Data_wrapper as Data_wrapper
import json
from Exceptions import *

class Employee:


    def __init__(self) -> None:
        pass

    def authenticate_user(self, credentials: str):
        """
        1. Parse json from UI
        2. Check if username is registered
        3. Check if passwords match
        4. Return id
        """
        
        # Start by parsing json credentials
        ui_load = json.loads(credentials)
        username, password = ui_load['username'], ui_load['password']

        # If username is registered, Data_wrapper._authenticate_user returns id and registered password
        data_load = json.loads(
            Data_wrapper.authenticate_user(
                json.dumps({"username":username})))

        # If username is not registered, Data_wrapper._authenticate_user returns false
        if not data_load:
            raise IncorrectUsernameException
        
        else:
            # If passwords don't match, raise exception
            id_, registered_password = data_load['id'], data_load['password']
            if password != registered_password:
                raise IncorrectPasswordException

            # If user is authenticated, return user id.
            # User id should symbolize a logged in user.
            else:
                return json.dumps({"id":id_})

    def __get_role(self, id_: str):
        # If username is not registered, Data_wrapper._authenticate_user returns false
        data_load = json.loads(Data_wrapper.get_role(id_))
        if not data_load:
            raise IncorrectIdException
        else:
            return data_load['role']

    def request_list(self, id_: str):
        role = self.__get_role(id_)







