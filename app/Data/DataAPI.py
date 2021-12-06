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

    def get_all(self, data: json) -> json:
        key = self.__parse_key(data)
        try:
            return self.__redirect_request(key).get_all()
        except DatabaseEmptyException as error:
            return self.__format_error_message(error)

    def post(self, data: json) -> json:
        key = self.__parse_key(data)
        try:
            return self.__redirect_request(key).post(data)
        except IncorrectDataException as error:
            return self.__format_error_message(error)


    def put(self, data: json) -> json:
        key = self.__parse_key(data)
        try:
            return self.__redirect_request(key).put(data)
        except IncorrectDataException as error:
            return self.__format_error_message(error)


    ### HELPERS

    def __parse_key(self, data: json) -> str:
        """Parses key from request"""
        return json.loads(data)["key"]

    def __redirect_request(self, key):
        """Parses key from request and returns corresponding LLclass"""
        return self.__class_map[key]

    def __format_error_message(self, error):
        """
        Returns json formatted error message
        """
        return json.dumps(
            {"type": False, "message": str(error)}
        )

