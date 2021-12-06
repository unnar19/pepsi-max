from Data.LogEmployee import LogEmployee
from Data.LogRealEstate import LogRealEstate
from Data.LogContractor import LogContractor
from Data.LogReport import LogReport
from Data.LogTicket import LogTicket
from Data.LogDestination import LogDestination
from Exceptions import *
import json

class DataAPI:

    def __init__(self) -> None:
        self.__employee = LogEmployee()
        self.__real_estate = LogRealEstate()
        self.__ticket = LogTicket()
        self.__contractor = LogContractor()
        self.__report = LogReport()
        self.__destination = LogDestination()
        self.__class_map = {
            "employee": self.__employee, \
            "real_estate": self.__real_estate, \
            "ticket": self.__ticket, \
            "contractor": self.__contractor, \
            "report": self.__report, \
            "destination": self.__destination
        }

    ### CRUD METHODS

    def __redirect_request(self, data):
        """Parses key from request and returns corresponding LLclass"""
        return self.__class_map[json.loads(data)["key"]]

    def get_all(self, data: json) -> json:
        try:
            return self.__redirect_request(data).get_all()
        except DataNotFoundException:
            return False

    def get(self, data: json) -> json:
        try:
            return self.__redirect_request(data).get()
        except DataNotFoundException:
            return False

    def post(self, data: json) -> json:
        try:
            return self.__redirect_request(data).post(data)
        except IncorrectDataException:
            return False

    def put(self, data: json) -> json:
        try:
            return self.__redirect_request(data).put(data)
        except IncorrectDataException:
            return False

    # def authenticate_employee_username(self, data: str):
    #     """data parameter is """
    #     try:
    #         return self.__employee.get_all(data)
    #     except DataNotFoundException:
    #         return False

