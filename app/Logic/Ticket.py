import json
from Data.DataAPI import DataAPI
from Exceptions import *

class Ticket:
    def __init__(self) -> None:
        self.data_api = DataAPI()