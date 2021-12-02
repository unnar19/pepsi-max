from Data.DataAPI import DataAPI
from Exceptions import *

class RealEstate:
    def __init__(self) -> None:
        self.data_wrapper = DataAPI()

    def get_all(self, data: str):
        return self.data_api.get_all(data)

    def get(self, data: str):
        return self.data_api.get(data)

    def post(self, data: str):
        if self.__is_boss(data):
            
            if self.__is_new(data):
                return self.data_api.post(data)
            
            else:
                raise EmailAlreadyExistsException
        else:
            raise UnauthorizedReguestException

