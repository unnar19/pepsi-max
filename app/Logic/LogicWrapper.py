import Employee
import Listing
import RealEstate
import Report
import Search
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

    def get_employee_list(self, fields: str):
        """Request list of employees"""
        return self.employee.get_list(fields)

    def post_employee_data(self, data: str):
        """Register new employee"""
        return self.employee.register(data)