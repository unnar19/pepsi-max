import json
from Contractor import Contractor
from Employee import Employee
from RealEstate import RealEstate
from Report import Report
from Ticket import Ticket
from Exceptions import *

# Logic_wrapper is a gateway between UI and Logic classes.
# All UI classes can use the Logic wrapper but only a few
# methods are exposed. Hence, the logic wrapper controls
# all communication between UI and Logic


class LogicAPI:
    def __init__(self) -> None:
        self.__employee = Employee()
        self.__real_estate = RealEstate()
        self.__ticket = Ticket()
        self.__contractor = Contractor()
        self.__report = Report()
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
        except UnauthorizedReguestException:
            return False

    def get(self, data: str):
        try:
            return self.__redirect_request(data).get(data)
        except UnauthorizedReguestException:
            return False

    def post(self, data: str):
        try:
            return self.__redirect_request(data).post(data)
        except UnauthorizedReguestException:
            return False

    def put(self, data: str):
        try:
            return self.__redirect_request(data).put(data)
        except UnauthorizedReguestException:
            return False

    ### EMPLOYEE METHODS

    def authenticate_employee(self, credentials: str):
        """Credentials contain username-field and password-field"""
        try:
            return self.__employee.authenticate(credentials)
        except IncorrectCredentialsException:
            return False

    ### REAL ESTATE METHODS


    ### TICKET METHODS


    ### CONTRACTOR METHODS


    