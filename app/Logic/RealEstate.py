import Data.DataAPI as DataAPI
from Exceptions import *

class RealEstate:
    def __init__(self) -> None:
        self.data_wrapper = DataAPI()

    def get_all(self):
        return self.data_wrapper.get_real_estates_all()

    def get(self, id_: str):
        return self.data_wrapper.get_real_estate(id_)

    def post(self, data: str):
        return self.data_wrapper.post_real_estate(data)

    def put(self, data: str):
        return self.data_wrapper.put_real_estate(data)