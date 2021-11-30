import json
import Employee
import RealEstate
import Report
import Ticket
from Exceptions import *

# Logic_wrapper is a gateway between UI and Logic classes.
# All UI classes can use the Logic wrapper but only a few
# methods are exposed. Hence, the logic wrapper controls
# all communication between UI and Logic


class LogicWrapper:
    def __init__(self) -> None:
        self.employee = Employee()

    def authenticate_employee_credentials(self, credentials: str):
        """Credentials contain username-field and password-field"""
        try:
            return self.employee.authenticate(credentials)
        except IncorrectCredentialsException:
            return False

    def get_employees_all(self):
        """Get json array of all employees"""
        return self.employee.get_all()

    def get_employee_data(self, id_: str):
        """Get all jsondata for employee with id: id_"""
        return self.employee.get(id_)

    def post_employee_data(self, data: str):
        """Submit filled json schema for new employee"""
        try:
            return self.employee.create_new(data)
        except UnauthorizedReguestException:
            return False

    def put_employee_data(self, data: str):
        """Submit filled and modified json schema for registered employee"""
        try:
            return self.employee.update(data)
        except UnauthorizedReguestException:
            return False

        
