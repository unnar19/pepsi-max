import Employee
import Listing
import Real_estate
import Report
import Search
import Ticket
from Exceptions import *

# Logic_wrapper is a gateway between UI and Logic classes.
# All UI classes can use the Logic wrapper but only a few
# methods are exposed. Hence, the logic wrapper controls
# all communication between UI and Logic

class Logic_wrapper:
    def __init__(self) -> None:
        pass

    def authenticate_employee(self, credentials: str):
        """Credentials contain username-field and password-field"""
        try:
            return Employee.authenticate(credentials)
        except IncorrectCredentialsException:
            return False

    def request_employee_list(self, id_: str):
        """Request list of employees"""
        return Employee.request_list(id_)
        
