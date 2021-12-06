import json
from Logic.Contractor import Contractor
from Logic.Employee import Employee
from Logic.RealEstate import RealEstate
from Logic.Report import Report
from Logic.Ticket import Ticket
from Logic.Destination import Destination
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
        self.__destination = Destination()
        self.__class_map = {
            "employee": self.__employee, \
            "real_estate": self.__real_estate, \
            "ticket": self.__ticket, \
            "contractor": self.__contractor, \
            "report": self.__report, \
            "destination": self.__destination
        }
        self.__exception_return = {"type": False}

    ### CRUD METHODS

    def __redirect_request(self, data):
        """Parses key from data and returns corresponding LLclass"""
        return self.__class_map[json.loads(data)["key"]]

    def get_all(self, data: json) -> json:
        """
        Sends GET ALL request to LL
        """
        try:
            return self.__redirect_request(data).get_all()
        except UnauthorizedRequestException:
            return json.dumps(self.__exception_return)

    def get(self, data: json) -> json:
        """
        Sends GET request to LL
        """
        try:
            return self.__redirect_request(data).get(data)
        except UnauthorizedRequestException:
            return json.dumps(self.__exception_return)

    def post(self, data: json) -> json:
        """
        Sends POST request to LL

        """
        try:
            return self.__redirect_request(data).post(data)
        except UnauthorizedRequestException:
            return json.dumps(self.__exception_return)
        except EmailAlreadyExistsException:
            return json.dumps(self.__exception_return)

    def put(self, data: json) -> json:
        """
        Sends PUT request to LL
        """
        try:
            return self.__redirect_request(data).put(data)
        except UnauthorizedRequestException:
            return json.dumps(self.__exception_return)
        except NoIdException:
            return json.dumps(self.__exception_return)
        except IncorrectDataException:
            return json.dumps(self.__exception_return)

    def delete(self, data: json) -> json:
        """
        Sends DELETE request to LL
        """
        try:
            return self.__redirect_request(data).delete(data)
        except UnauthorizedRequestException:
            return json.dumps(self.__exception_return)
        except NoIdException:
            return json.dumps(self.__exception_return)
        except IncorrectDataException:
            return json.dumps(self.__exception_return)
        except IncorrectIdException:
            return json.dumps(self.__exception_return)
            

    ### EMPLOYEE METHODS

    def authenticate_employee(self, data: str):
        """
        Sends AUTH request to LL
        
        Data field contains username-field and password-field
        """
        try:
            return self.__employee.authenticate(data)
        except IncorrectEmailException:
            return json.dumps(self.__exception_return)
        except IncorrectPasswordException:
            return json.dumps(self.__exception_return)

    ### REAL ESTATE METHODS


    ### TICKET METHODS


    ### CONTRACTOR METHODS


    ### DESTINATION METHODS


    