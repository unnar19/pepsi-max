from LogEmployee import LogEmployee
from LogRealEstate import LogRealEstate
from LogContractor import LogContractor
from LogReport import LogReport
from LogTicket import LogTicket
from Exceptions import *
import json


import LogEmployee

class DataAPI:
    def __init__(self) -> None:
        self.__employee = LogEmployee()
        self.__real_estate = LogRealEstate()
        self.__ticket = LogTicket()
        self.__contractor = LogContractor()
        self.__report = LogReport()
        self.__class_map = {
            "employee": self.__employee, \
            "real_estate": self.__real_estate, \
            "ticket": self.__ticket, \
            "contractor": self.__contractor, \
            "report": self.__report
        }

    ### CRUD METHODS

    def __redirect_request(self, data):
        """Parses key from request and returns corresponding LLclass"""
        return self.__class_map[json.loads(data)["key"]]

    def get_all(self, data: str):
        try:
            return self.__redirect_request(data).get_all()
        except DataNotFoundException:
            return False

    def get(self, data: str):
        try:
            return self.__redirect_request(data).get(data)
        except DataNotFoundException:
            return False

    def post(self, data: str):
        try:
            return self.__redirect_request(data).post(data)
        except IncorrectDataException:
            return False

    def put(self, data: str):
        try:
            return self.__redirect_request(data).put(data)
        except IncorrectDataException:
            return False

    def authenticate_employee_username(self, username: str):
        try:
            return self.log_employee.authenticate_username(username)
        except DataNotFoundException:
            return False

